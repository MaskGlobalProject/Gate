import datetime

# Mask Global Project - The Gate (Pro Version)
# Excellence is our only identity.

def log_attempt(status):
    # هذا الجزء ينشئ ملفاً يسجل تاريخ ومحاولات الدخول
    with open("access_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] Attempt: {status}\n")

def enter_gate():
    secret_key = "MASK2025"
    print("--- Welcome to Mask Global Gate ---")
    user_input = input("Please enter the Excellence Key: ")
    
    if user_input == secret_key:
        print("Access Granted. Welcome to the future.")
        log_attempt("SUCCESS")
    else:
        print("Access Denied. Only excellence is allowed here.")
        log_attempt("FAILED")

if __name__ == "__main__":
    enter_gate()


