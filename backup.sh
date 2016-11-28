#!/bin/bash

# Strongly inspired from a script written by Jan Schampera
# http://wiki.bash-hackers.org/howto/mutex

# exit codes and text
ENO_SUCCESS=0; ETXT[0]="ENO_SUCCESS"
ENO_GENERAL=1; ETXT[1]="ENO_GENERAL"
ENO_LOCKFAIL=2; ETXT[2]="ENO_LOCKFAIL"
ENO_RECVSIG=3; ETXT[3]="ENO_RECVSIG"

# Setup the variables containing the source and destination of files to backup
source backup_volume_path.py

BCKVOLARRAY=( "alain"
              "mini"
              "air"
)

# Check the parameters input
if [ $# -ne 1 ]; then
    echo "Wrong number of args. Backup volume name is needed" >&2
    exit ${ENO_GENERAL}
else
    if ! [[ " ${BCKVOLARRAY[@]} " =~ " $1 " ]]; then
        # whatever you want to do when arr contains value
        echo "Backup volume name \"$1\" is unknown" >&2
        exit ${ENO_GENERAL}
    fi
fi

BCKVOL=$1
# dirs/files params
LOCKDIR="/tmp/backup-lock-${BCKVOL}"
PIDFILE="${LOCKDIR}/PID"

###
### start locking attempt
###

trap 'ECODE=$?; echo "[backup] Exit: ${ETXT[ECODE]}($ECODE)" >&2' 0
echo -n "[backup ${BCKVOL}] Locking: " >&2

if mkdir "${LOCKDIR}" &>/dev/null; then

    # lock succeeded, install signal handlers before storing the PID just in case
    # storing the PID fails
    trap 'ECODE=$?;
    echo "[backup ${BCKVOL}] Removing lock. Exit: ${ETXT[ECODE]}($ECODE)" >&2
    rm -rf "${LOCKDIR}"' 0
    echo "$$" >"${PIDFILE}"
    # the following handler will exit the script upon receiving these signals
    # the trap on "0" (EXIT) from above will be triggered by this trap's "exit" command!
    trap 'echo "[backup ${BCKVOL}] Killed by a signal." >&2
    exit ${ENO_RECVSIG}' 1 2 3 15
    echo "success, installed signal handlers"
else

    # lock failed, check if the other PID is alive
    OTHERPID="$(cat "${PIDFILE}")"

    # if cat isn't able to read the file, another instance is probably
    # about to remove the lock -- exit, we're *still* locked
    #  Thanks to Grzegorz Wierzowiecki for pointing out this race condition on
    #  http://wiki.grzegorz.wierzowiecki.pl/code:mutex-in-bash
    if [ $? != 0 ]; then
        echo "lock failed, PID ${OTHERPID} is active" >&2
        exit ${ENO_LOCKFAIL}
    fi

    if ! kill -0 $OTHERPID &>/dev/null; then
        # lock is stale, remove it and restart
        echo "removing stale lock of nonexistant PID ${OTHERPID}" >&2
        rm -rf "${LOCKDIR}"
        echo "[backup ${BCKVOL}] restarting myself" >&2
        exec "$0" "$@"
    else
        # lock is valid and OTHERPID is active - exit, we're locked!
        echo "lock failed, PID ${OTHERPID} is active" >&2
        exit ${ENO_LOCKFAIL}
    fi

fi

###
### Switch depending on backup volume name
###

case ${BCKVOL} in
    "air")
	echo "Launching of [backup ${BCKVOL}]" 
	rsync -havz --bwlimit=150 --delete --log-format="%t %o %b %f" --stats ${AIR_SOURCE} ${AIR_DESTI} > /tmp/bck-air.log 2>&1
    ;;
    "alain")
	echo "Launching of [backup ${BCKVOL}]"
	rsync -havz --bwlimit=50  --delete --log-format="%t %o %b %f" --stats ${ALAIN_SOURCE} ${ALAIN_DESTI} > /tmp/bck-alain.log 2>&1
    ;;
    "mini")
	echo "Launchng of [backup ${BCKVOL}]"
	rsync -havz --bwlimit=150 --delete --log-format="%t %o %b %f" --stats ${MINI_SOURCE} ${MINI_DESTI}  > /tmp/bck-mini.log 2>&1
    ;;
    * ) echo "Backup volume name is unknown" >&2 ;;
esac