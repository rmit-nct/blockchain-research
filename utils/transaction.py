from datetime import datetime

class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float):
        self.sender = sender        
        self.receiver = receiver  
        self.amount = amount        
        self.timestamp = datetime.now() 
    def __str__(self):
        return f'Transaction from {self.sender} to {self.receiver} of {self.amount} at {self.timestamp}'
