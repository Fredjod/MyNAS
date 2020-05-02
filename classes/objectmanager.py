#!/usr/local/bin/python3.5
# encoding: utf-8

'''
Created on 18 déc. 2016

@author: home
'''

from classes.node import *

def createNode ( name,
                 remoteAddress,
                 maxUpBw,
                 maxDownBw,
                 maxSpace
                ):
    
        aNode = Node()
        aNode.set_name(name)
        aNode.set_remote_address(remoteAddress)
        aNode.set_max_up_bw(maxUpBw)
        aNode.set_max_down_bw(maxDownBw)
        aNode.set_max_space(maxSpace)
        return aNode

def createVolume ( name,
                   path,
                   nodeId
                ):
    
        aVol = Volume()
        aVol.set_name(name)
        aVol.set_path(path)
        aNode = Node(nodeId)
        volumes = aNode.get_volumeList()     
        volumes.append(aVol.objID);
        aNode.set_volumeList(volumes)
        aVol.set_myNode(aNode.objID)
        return aVol

def createBatch ( periodicity,
                   timeTrigger,
                   fromVolumeName,
                   toVolumeName
                ):
    
        aBatch = Batch()
        aBatch.set_periodicity(periodicity)
        aBatch.set_time_trigger(timeTrigger)
        aBatch.set_from_volumeId (
                                 aBatch.findObjectId("<class 'classes.node.Volume'>", 
                                                     key = '_name',
                                                     value = fromVolumeName,
                                                     unique = True
                                                     )[0]
                                 )
        aBatch.set_to_volumeId (
                                 aBatch.findObjectId("<class 'classes.node.Volume'>", 
                                                     key = '_name',
                                                     value = toVolumeName,
                                                     unique = True
                                                     )[0]
                                 )
        return aBatch

    

import unittest

class TestNode(unittest.TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_createNode(self):
        
        # Create a new Node
        aNode = createNode(name = 'raspberry-fred', 
                   remoteAddress = 'ttg09.ddns.net',
                   maxUpBw = 200,
                   maxDownBw = 100,
                   maxSpace = 500
                   )

        self.assertEqual(aNode.get_name(), 'raspberry-fred')
        aNode.deleteObj()
        
    def test_createVolume(self):
        # Create a Volume and attach to a Node
        aNode = Node(12);
        aVol = createVolume(name = 'homemini',
                     path = '/mnt/backup/homemini-128b-500g', 
                     nodeId = aNode.objID
                     )
        self.assertEqual(aVol.get_myNode(), 12)
        aVol.deleteObj()
        

    def test_readNode(self):
        aNode = Node(12);
        self.assertEqual(aNode.get_name(), 'raspberry-fredouille')


    def test_createBatch(self):
        aBatch = createBatch (
                              periodicity = PERIODICITY_DAY, 
                              timeTrigger = 2, # every day at 2:00 am
                              fromVolumeName = 'home-mini', 
                              toVolumeName = 'home-mini'
                              )
        self.assertEqual(aBatch.get_to_volumeId(), 51)
        aVol = Volume(aBatch.get_to_volumeId())
        aNode = Node (aVol.get_myNode())
        self.assertEqual(aBatch.get_to_volumeId(), 51)
        self.assertEqual(aNode.get_remote_address(), 'ttg09.ddns.net')
        aBatch.deleteObj()

if __name__ == '__main__':
    unittest.main()