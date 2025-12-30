import datetime

# Mask Global Project - The Gate
# Excellence is our only identity.

def encrypt_message(message):
    # محرك التشفير السري
    return "".join([chr(ord(c) + 3) for c in message])

def log_attempt(status):
    with open("access_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] Attempt: {status}\n")

def enter_gate():
    secret_key = "MASK2025"
    print("--- Welcome to Mask Global Gate ---")
    user_input = input("Enter Excellence Key: ")
    
    if user_input == secret_key:
        print("\n[Access Granted]")
        log_attempt("SUCCESS")
        
        # نظام التشفير يظهر هنا فقط بعد النجاح
        msg = input("Enter message to encrypt: ")
        print(f"Cipher: {encrypt_message(msg)}")
    else:
        print("\n[Access Denied]")
        log_attempt("FAILED")

if __name__ == "__main__":
    enter_gate()



