from queue import PriorityQueue
import numpy as np
import sys
from graph import *
from copy import deepcopy
from peer import *
from block import *
from transaction import *
from event import *

class Simulate():
    def __init__(self, numPeers, slowPerc, lowCpuPerc, txnDelayMeanTime, maxSimTime, maxBlockSize , maxTransactionSize, miningFee):
        self.numPeers = numPeers
        self.slowPerc = slowPerc
        self.lowCpuPerc = lowCpuPerc
        self.txnDelayMeanTime = txnDelayMeanTime
        self.maxSimTime = maxSimTime
        self.maxBlockSize = maxBlockSize
        self.maxTransactionSize = maxTransactionSize
        self.miningFee = miningFee
        self.events = PriorityQueue()
        self.c = [[]*numPeers]
        self.trxn_id = 1
        self.blk_id = 1

        # Hash Power
        self.avgInterArrivalTime = 600*1000
        self.lowHashPow = 100 / (10 - 9*self.lowCpuPerc)
        self.highHashPow = 10*self.lowHashPow

        # rho_ij in ms, c_ij in bits/ms
        self.rho = np.random.uniform(10, 500, (self.numPeers, self.numPeers))
        self.c = [[]*self.numPeers]
        self.peers = []

    def run(self):
        slows_mask = np.random.permutation([True] * int(self.numPeers * self.slowPerc/100) + [False] * (self.numPeers - int(self.numPeers * self.slowPerc/100)))
        lows_mask = np.random.permutation([True] * int(self.numPeers * self.lowCpuPerc/100) + [False] * (self.numPeers - int(self.numPeers * self.lowCpuPerc/100)))
        peers = []
        for i in range(self.numPeers):
            peers.append(Peer(i, slows_mask[i], lows_mask[i]))
        

        
        CreateNetwork(peers)

        debug(peers)

        self.peers = peers
        self.c = [[5 if peers[i].isSlow or peers[j].isSlow else 100 for j in range(self.numPeers)] for i in range(self.numPeers)] * (1000)

        # Initializing Transaction ids and block ids
        Genesis = Block(self.blk_id, None, -1, 0, None, [0]*self.numPeers, 0)
        firstTask = Event(0, 'recBlock', 0, self, None, Genesis )
        self.events.put(firstTask)

        while (not self.events.empty()) and self.events.queue[0].time <= self.maxSimTime:
            event = self.events.get()
            print(event.event_type, event.peer_id, event.time)
            event.handleEvents()


        print("Simulation completed")
        print("Total blocks mined: ", self.blk_id)
        print("Total peers: ", self.numPeers)
        print("Total transactions: ", self.trxn_id)
       





