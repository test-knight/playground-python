import threading
import time

def critical_code(lock, thead_name):
    print(f"{thead_name} attempting to acquire lock...")
    with lock:
        print(f"{thead_name} has acquired lock. Entering critical section.")
        time.sleep(2)
        print(f"{thead_name} is releasing lock.")

lock = threading.Lock()

threads = []
for i in range(3):
    thread = threading.Thread(target=critical_code, args=(lock, f"Thread-{i+1}"))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# explain the code block above
