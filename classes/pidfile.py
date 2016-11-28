#!/usr/local/bin/python3.5
# encoding: utf-8
'''
Created on 25 nov. 2016

@author: FredJod did the Python v3.5 adaptation
Inspired by Anarcat (http://stackoverflow.com/questions/1444790/python-module-for-creating-pid-based-lockfile)

'''

import sys
import os
import errno
from builtins import str


class PidFile(object):
    '''    
    Manage a PID (Process ID) file for avoiding the launch of multiple instance of a given process
    '''

    def __init__(self, path, log=sys.stdout.write, warn=sys.stderr.write):
        '''
        Constructor
        '''
        self.pidfile = path
        self.log = log
        self.warn = warn

    def __enter__(self):
        try:
            self.pidfd = open(self.pidfile, 'x')
            self.log('locked pidfile %s\n' % self.pidfile)
        except OSError as e:
            if e.errno == errno.EEXIST:
                pid = self._check()
                if pid:
                    self.pidfd = None
                    raise ProcessRunningException('process already running in %s as pid %s' % (self.pidfile, pid));
                else:
                    self._remove()
                    self.pidfd = open(self.pidfile, 'x')
            else:
                raise

        self.pidfd.write(str(os.getpid()))
        self.pidfd.close()
        return self

    def __exit__(self, t, e, tb):
        # return false to raise, true to pass
        if t is None:
            # normal condition, no exception
            self._remove()
            return True
        elif t is ProcessRunningException:
            # do not remove the other process lockfile
            return False
        else:
            # other exception
            if self.pidfd:
                # this was our lockfile, removing
                self._remove()
            return False

    def _remove(self):
        self.log('removed pidfile %s' % self.pidfile)
        os.remove(self.pidfile)

    def _check(self):
        """check if a process is still running the process id is expected to be in pidfile, which should exist.
        if it is still running, returns the pid, if not, return False."""
        with open(self.pidfile, 'r') as f:
            try:
                pidstr = f.read()
                pid = int(pidstr)
            except ValueError:
                # not an integer
                self.log("not an integer: %s" % pidstr)
                return False
            try:
                os.kill(pid, 0)
            except OSError:
                self.log("can't deliver signal to %s" % pid)
                return False
            else:
                return pid

class ProcessRunningException(Exception):
    pass