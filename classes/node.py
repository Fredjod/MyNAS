#!/usr/local/bin/python3.5
# encoding: utf-8
'''
Created on 25 nov. 2016

@author: FredJod

'''

from utils.sqlite_serial_object import SqLiteSerialObject
import threading

PERIODICITY_HOUR = 1 # trigger is a minute (0 .. 59)
PERIODICITY_DAY = 2 # trigger is an hour (0..23)
PERIODICITY_WEEK = 3 # trigger is a day of week (1..7)
PERIODICITY_MONTH = 4 # trigger is a day of month (1..28)


class Node(SqLiteSerialObject):
    '''
    classdocs
    '''

    def __init__(self, p_id = None):
        '''
        Constructor
        '''
        
        self._name = None
        self._remoteAddress = None
        self._maxUpBw = None
        self._maxDownBw = None
        self._maxSpace = None
        self._volumeList = []
        self._batchList = []
        super(Node, self).__init__(p_id)

    def get_batchList(self):
        return self._batchList


    def set_batchList(self, value):
        self._batchList = value
        super(Node, self).setObj()

    def get_volumeList(self):
        return self._volumeList


    def set_volumeList(self, value):
        self._volumeList = value
        super(Node, self).setObj()

    def get_remote_address(self):
        return self._remoteAddress


    def get_max_up_bw(self):
        return self._maxUpBw


    def get_max_down_bw(self):
        return self._maxDownBw


    def get_max_space(self):
        return self._maxSpace


    def set_remote_address(self, value):
        self._remoteAddress = value
        super(Node, self).setObj()


    def set_max_up_bw(self, value):
        self._maxUpBw = value
        super(Node, self).setObj()


    def set_max_down_bw(self, value):
        self._maxDownBw = value
        super(Node, self).setObj()

    def set_max_space(self, value):
        self._maxSpace = value
        super(Node, self).setObj()

    def get_name(self):
        return self._name


    def set_name(self, value):
        self._name = value
        super(Node, self).setObj()


class Volume(SqLiteSerialObject):
    '''
    classdocs
    '''

    def __init__(self, p_id = None):
        '''
        Constructor
        '''
        
        self._name = None
        self._path = None
        self._myNode = None
        super(Volume, self).__init__(p_id)

    def get_name(self):
        return self._name


    def get_path(self):
        return self._path


    def set_name(self, value):
        self._name = value
        super(Volume, self).setObj()


    def set_path(self, value):
        self._path = value
        super(Volume, self).setObj()

    def set_myNode(self, value):
        self._myNode = value
        super(Volume, self).setObj()


    def get_myNode(self):
        return self._myNode


class Batch (SqLiteSerialObject):
    '''
    classdocs
    '''

    def __init__(self, p_id = None):
        '''
        Constructor
        '''
        
        self._periodicity= None
        self._timeTrigger = None
        self._lastExecutionTime = None
        self._fromVolumeId = None
        self._toVolumeId = None
        self._runHistoryListId = []
        self._runInstanceId = None
        
        super(Batch, self).__init__(p_id)

    def execute(self):
        # check whether it is time to run
        # if yes: check whether an instance is already running
            # check if RunInstance object exists and its PID is actually running by the OS
        # if yes: exist
        # if no: check if enought bandwith is available
            # ...
        # if no: exist
        # if yes: check whether enought disk space is available
            # ...
        # Then create and run a RunInstance
        pass

    def get_periodicity(self):
        return self._periodicity


    def get_time_trigger(self):
        return self._timeTrigger


    def get_last_execution_time(self):
        return self._lastExecutionTime


    def get_from_volumeId(self):
        return self._fromVolumeId


    def get_to_volumeId(self):
        return self._toVolumeId


    def get_run_historyListId(self):
        return self._runHistoryListId


    def get_run_instanceId(self):
        return self._runInstanceId


    def set_periodicity(self, value):
        self._periodicity = value
        super(Batch, self).setObj()


    def set_time_trigger(self, value):
        self._timeTrigger = value
        super(Batch, self).setObj()


    def set_last_execution_time(self, value):
        self._lastExecutionTime = value
        super(Batch, self).setObj()


    def set_from_volumeId(self, value):
        self._fromVolumeId = value
        super(Batch, self).setObj()


    def set_to_volumeId(self, value):
        self._toVolumeId = value
        super(Batch, self).setObj()


    def set_run_historyListId(self, value):
        self._runHistoryListId = value
        super(Batch, self).setObj()


    def set_run_instanceId(self, value):
        self._runInstanceId = value
        super(Batch, self).setObj()


class RunInstance (SqLiteSerialObject, threading.Thread):
    '''
    classdocs
    '''

    def __init__(self, p_id = None):
        '''
        Constructor
        '''
        
        self._pid = None
        self._status= None
        self._bwUsed = None
        
        super(RunInstance, self).__init__(p_id)
        
    def run(self):
        # store the PID
        # buil rsync command line string
        # Execute rsync command
        # Record the logs
        pass

    def get_pid(self):
        return self._pid


    def get_status(self):
        return self._status


    def get_bw_used(self):
        return self._bwUsed


    def set_pid(self, value):
        self._pid = value
        super(RunInstance, self).setObj()


    def set_status(self, value):
        self._status = value
        super(RunInstance, self).setObj()


    def set_bw_used(self, value):
        self._bwUsed = value
        super(RunInstance, self).setObj()
        

class RunHistory (SqLiteSerialObject):
    '''
    classdocs
    '''

    def __init__(self, p_id = None):
        '''
        Constructor
        '''
        
        self._date = None
        self._status= None
        self._message = None
        self._logFile = None
        
        super(RunHistory, self).__init__(p_id)
        
    def get_date(self):
        return self._date


    def get_status(self):
        return self._status


    def get_message(self):
        return self._message


    def get_log_file(self):
        return self._logFile


    def set_date(self, value):
        self._date = value
        super(RunHistory, self).setObj()


    def set_status(self, value):
        self._status = value
        super(RunHistory, self).setObj()


    def set_message(self, value):
        self._message = value
        super(RunHistory, self).setObj()


    def set_log_file(self, value):
        self._logFile = value
        super(RunHistory, self).setObj()
        
        