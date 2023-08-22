'''
Stores configuration parameters and hyperparameters for your project
eg:

class Config:
    def __init__(self):
        self.batch_size = 32
        self.lr = 0.001
        self.epochs = 10
        # Add more hyperparameters here
    
    def print_config(self):
        print("Configuration:")
        print(f"Batch size: {self.batch_size}")
        print(f"Learning rate: {self.lr}")
        print(f"Epochs: {self.epochs}")
        # Print other hyperparameters
    
config = Config()

then import into main.py!
'''