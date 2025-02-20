import time

def stopwatch():
    while True:
        user_input = input("Press 'Y' to start or 'N' to stop the stopwatch: ").strip().upper()
        
        if user_input == 'Y':
            start_time = time.time()
            print("Stopwatch started. Press 'N' to stop.")
            
            while True:
                stop_input = input("Press 'N' to stop: ").strip().upper()
                if stop_input == 'N':
                    elapsed_time = time.time() - start_time
                    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
                    break
        
        elif user_input == 'N':
            print("Stopwatch not started. Exiting program.")
            break
        
        print("Press 'C' to continue or any other key to exit.")
        continue_input = input().strip().upper()
        if continue_input != 'C':
            break

if __name__ == "__main__":
    stopwatch()