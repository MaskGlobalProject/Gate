# Mask Global Project - The Gate
# Excellence is our only identity.

def enter_gate():
    secret_key = "MASK2025"  
    
    print("--- Welcome to Mask Global Gate ---")
    user_input = input("Please enter the Excellence Key: ")
    
    if user_input == secret_key:
        print("Access Granted. Welcome to the future.")
    else:
        print("Access Denied. Only excellence is allowed here.")

if __name__ == "__main__":
    enter_gate()

