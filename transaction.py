class Transaction():
    def __init__(self, id, sender_id, recipient_id, amount, size = 8000):
        self.id = id
        self.sender = sender_id
        self.recipient = recipient_id
        self.amount = amount
        self.size = size
        