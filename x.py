import threading
import time

# Function that simulates a long-running task
def long_running_task():
    start_time = time.time()

    print("Long-running task started")

    count = 0
    for _ in range(10**8):  # Simulate a task that takes time to complete
        count += 1
    print("Long-running task completed")
    print("--- %s seconds ---" % (time.time() - start_time))
# Function that simulates a shorter task
def short_task():
    print("Short task started")
    count = 0
    for _ in range(10**6):  # Simulate a task that takes less time to complete
        count += 1
    print("Short task completed")

# Main function to run threads
def main():
    # Creating threads
    thread1 = threading.Thread(target=long_running_task)
    thread2 = threading.Thread(target=short_task)

    # Starting threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()



if __name__ == "__main__":
    main()
pass
