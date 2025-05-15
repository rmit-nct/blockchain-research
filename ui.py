from transaction import Transaction
from block import Block
from blockchain import Blockchain
import time 

def main():
    difficulty = 3
    blockchain = Blockchain(difficulty)

    while True:    
        print("MENU BLOCKCHAIN")
        print("1. Add a transaction to the Blockchain.")
        print("2. Check if the blockchain is valid.")
        print("3. Show all block.")
        print("4. Exit.")
        
        choice = input("Choose an option (1-4): ").strip()
        
        match choice:
            case "1":
                sender = input("Enter sender name: ").strip()
                receiver = input("Enter receiver name: ").strip()
                while True:
                    try:
                        amount = float(input("Enter amount: ").strip())
                        break
                    except ValueError:
                        print("Amount must be a number! Please try again.")
            
                transaction = Transaction(sender, receiver, amount)
                previous_hash = blockchain.get_last_block().hash
                index = blockchain.get_new_index()
                new_block = Block(transaction, previous_hash, index)
                blockchain.add_block(new_block)
            
                print("Successful!.")
        
            case "2":
                if blockchain.is_chain_valid():
                    print("Blockchain is valid.")
                else:
                    print("Blockchain is NOT valid")
        
            case "3":
                print("---BLOCKCHAIN---")
                blockchain.print_chain()
                print("---END BLOCKCHAIN---")
    
            case "4":
                print("GOODBYE!")
                break

if __name__ == "__main__":
    main()