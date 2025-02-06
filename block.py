class Block():
    def __init__(self, id, prevBlock, miner_id, timestamp, transactions, balances, depth):
        self.id = id
        self.prevBlock = prevBlock
        self.miner_id = miner_id
        self.timestamp = timestamp
        self.transactions = transactions
        self.balances = balances
        self.depth = depth

        