import argparse
from simulator import *

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    # Adding arguments
    parser.add_argument('--numPeers', type=int, required=True, help='Number of peers')
    parser.add_argument('--slowPerc', type=float, required=True, help='Percentage of nodes that are slow')
    parser.add_argument('--lowCpuPerc', type=float, required=True, help='Percentage of nodes with low CPU')
    parser.add_argument('--txnDelayMeanTime', type=float, required=True, help='Mean time for transaction delay')
    parser.add_argument('--maxSimTime', type=int, required=True, help='Maximum simulation time')
    parser.add_argument('--maxBlockSize', type=int, required=False, default= 1000, help='Maximum block size in KB')
    parser.add_argument('--maxTransactionSize', type=int, required=False, default= 1, help='Maximum transaction size in KB')
    parser.add_argument('--miningFee', type=float, required=False, default= 50, help='Mining fee in coins')

    # Parsing arguments
    args = parser.parse_args()

    # Accessing the arguments
    numPeers = args.numPeers
    slowPerc = args.slowPerc
    lowCpuPerc = args.lowCpuPerc
    txnDelayMeanTime = args.txnDelayMeanTime
    maxSimTime = args.maxSimTime
    maxBlockSize = args.maxBlockSize
    maxTransactionSize = args.maxTransactionSize
    miningFee = args.miningFee

    S = Simulate(numPeers, slowPerc, lowCpuPerc, txnDelayMeanTime, maxSimTime, maxBlockSize , maxTransactionSize, miningFee)
    S.run()
    print("modda gudu")