import hashlib
import multiprocessing
import time
import os
import sys

# গ্লোবাল ভ্যারিয়েবল (পাসওয়ার্ড পেলে এখানে সেভ হবে)
found_password = None

def get_hash(password, hash_type):
    if hash_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()

def crack_process(start_digit, target_hash, hash_type, queue):
    """এই ফাংশনটি প্রতিটি CPU কোরের জন্য আলাদা করে চলবে"""
    prefix = str(start_digit)
    
    # ৭ ডিজিট (০০০০০০০ থেকে ৯৯৯৯৯৯৯) পর্যন্ত লুপ
    for i in range(10000000):
        # প্রথম ডিজিট + বাকি ৭ ডিজিট (যেমন: 1 + 2345678 = 12345678)
        password = f"{prefix}{i:07d}"
        
        if get_hash(password, hash_type) == target_hash:
            # পাসওয়ার্ড পাওয়া গেছে! Queue-তে পাঠিয়ে দাও
            queue.put(password)
            return

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[96m" + "="*55)
    print("       ARGUSLENS - ULTRA FAST HASH CRACKER")
    print("="*55 + "\033[0m")
    print("\033[93m[*] Limit: 8-digits (Numbers only: 0-9)\033[0m")
    print("\033[93m[*] Supported: md5, sha1, sha256\033[0m\n")

    target_hash = input("\033[92m[?] Enter target hash: \033[0m").strip().lower()
    hash_type = input("\033[92m[?] Enter hash type (md5/sha1/sha256): \033[0m").strip().lower()

    if hash_type not in ["md5", "sha1", "sha256"]:
        print("\033[91m[-] Invalid hash type!\033[0m")
        sys.exit()

    print("\n\033[94m[+] Starting Multiprocessing Brute-Force...\033[0m")
    
    cores = multiprocessing.cpu_count()
    print(f"\033[94m[+] Using {cores} CPU Cores for maximum speed.\033[0m")
    print("\033[90m[*] Please wait, this might take a minute or two...\033[0m\n")
    
    start_time = time.time()
    
    # ডাটা আদান-প্রদানের জন্য Queue ব্যবহার করা হচ্ছে
    queue = multiprocessing.Queue()
    processes = []

    # ১০টি আলাদা প্রসেস তৈরি করা (0 থেকে 9 দিয়ে শুরু হওয়া সংখ্যার জন্য)
    # যদি ৮ কোর থাকে, তবে ১০টি প্রসেস পালাক্রমে চলবে
    for i in range(10):
        p = multiprocessing.Process(
            target=crack_process, 
            args=(i, target_hash, hash_type, queue)
        )
        processes.append(p)
        p.start()

    # রেজাল্ট আসা পর্যন্ত অপেক্ষা করা
    result = None
    try:
        # Queue থেকে রেজাল্ট নেওয়া (৫ মিনিট পর্যন্ত অপেক্ষা করবে)
        result = queue.get(timeout=300)
    except Exception:
        pass

    # রেজাল্ট পাওয়া গেলে বাকি সব প্রসেস জোরপূর্বক বন্ধ করা
    for p in processes:
        p.terminate()
        p.join()

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    print("\n" + "-"*55)
    if result:
        print(f"\033[92m[✅] PASSWORD FOUND: {result}\033[0m")
        print(f"\033[92m[⏱️] Time taken: {time_taken} seconds\033[0m")
    else:
        print("\033[91m[❌] PASSWORD NOT FOUND in 8-digit numeric space.\033[0m")
    print("-"*55)

if __name__ == "__main__":
    main()