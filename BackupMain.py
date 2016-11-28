#!/usr/local/bin/python3.5
# encoding: utf-8
'''
Created on 25 nov. 2016

@author: FredJod

'''

from classes.pidfile import PidFile
from classes.pidfile import ProcessRunningException
import os, sys, getopt
import backup_volume_path

PIDDIR = "/tmp/bck.lock."

def usage():
    print ('Usage: backup.py -v <volume>')
    sys.exit()    

def main(argList):
    try:
        opts, args = getopt.getopt(argList,"hv:")
        if len(opts) == 0:
            raise getopt.GetoptError("Error: No option specified")
        for opt, arg in opts:
            if opt == '-h':
                usage()
            elif opt == '-v':
                volume = arg
    except getopt.GetoptError as e:
        print (e.msg)
        usage()

    try:
        with PidFile(PIDDIR+volume):
            # launch backup
            if volume == 'air':
                os.system("rsync -havz --bwlimit=150 --delete --log-format=\"%t %o %b %f\" --stats " + backup_volume_path.AIR_SOURCE + " " + backup_volume_path.AIR_DESTI + " > /tmp/bck-air.log 2>&1")
            elif volume == 'alain':
                os.system("rsync -havz --bwlimit=50  --delete --log-format=\"%t %o %b %f\" --stats " + backup_volume_path.ALAIN_SOURCE + " " + backup_volume_path.ALAIN_DESTI + " > /tmp/bck-alain.log 2>&1")
            elif volume == 'mini':
                os.system("rsync -havz --bwlimit=150 --delete --log-format=\"%t %o %b %f\" --stats " + backup_volume_path.MINI_SOURCE + " " + backup_volume_path.MINI_DESTI + " > /tmp/bck-mini.log 2>&1")
            else:
                print('ERR: '+ volume + '. Unknown volume name')      
    except ProcessRunningException as e:
        print (str(e))           
            
if __name__ == "__main__":
    main(sys.argv[1:])

