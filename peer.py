class Peer():
    def __init__(self, id, isSlow, isLowCPU, longestBlk=None):
        self.id = id
        self.isSlow = isSlow
        self.isLowCPU = isLowCPU
        self.neighbors = []
        self.transaction_ids = set()
        self.block_ids = set()
        self.transactions = []  
        self.longestBlk = None

    # def add_neighbor(self, peer):
    #     self.neighbors.append(peer)
    #     peer.add_neighbor(self)

    def clear_neighbors(self):
       self.neighbors = []

