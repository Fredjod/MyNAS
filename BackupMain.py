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
import logging

LOG_DIR="/usr/local/logs/"

def usage():
    print ('Usage: backup.py -v <volume>')
    sys.exit()    

def main(argList):
    logging.basicConfig(filename=LOG_DIR+"mynas.log", format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

    try:
        opts, args = getopt.getopt(argList,"hv:")
        if len(opts) == 0:
            raise getopt.GetoptError("No option specified")
        for opt, arg in opts:
            if opt == '-h':
                usage()
            elif opt == '-v':
                volume = arg
    except getopt.GetoptError as e:
        print (e.msg)
        usage()

    try:
        if volume in backup_volume_path.rsync_nodes:
            if os.path.isfile(LOG_DIR+"bck-"+volume+".log"):
                os.rename(LOG_DIR+"bck-"+volume+".log", LOG_DIR+"bck-"+volume+".1.log")
            with PidFile("/tmp/bck-"+volume+".lock"):
                # launch backup
                for i in range(len(backup_volume_path.rsync_nodes.get(volume).get("od"))):
                    try:
                        os.system(
                                  "rsync -havz --bwlimit=" +
                                  str(backup_volume_path.rsync_nodes.get(volume).get("bandwidth")) + 
                                  " --delete --log-format=\"%t %o %b %f\" --stats " + 
                                  backup_volume_path.rsync_nodes.get(volume).get("od")[i].get("o") + " " +
                                  backup_volume_path.rsync_nodes.get(volume).get("od")[i].get("d") + 
                                  " >> "+LOG_DIR+"bck-"+volume+".log 2>&1"
                                  )
                    except Exception as e:
                        logging.error("rsync execution failed: "+str(e)) 
                        
        else:
            logging.error("Unknown volume name: "+volume)      
    except ProcessRunningException as e:
        logging.error("Processus locking failed: "+str(e))           
            
if __name__ == "__main__":
    main(sys.argv[1:])

