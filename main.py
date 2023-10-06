import time
import random

def display_progress_bar(percentage):
    bar_length = 50
    block = int(round(bar_length * percentage))
    progress = "|" + "=" * block + "-" * (bar_length - block) + "|"
    print(f"\r{progress} {percentage * 100:.2f}%", end='')

def fake_quantum_computation():
    print("Initializing Quantum Data Encryption...")
    time.sleep(2)
    
    print("\nLoading Quantum Bits (Qubits)...")
    for _ in range(5):
        time.sleep(0.5)
        print(f"Loaded Qubit {_ + 1}")
    
    print("\nStarting Quantum Encryption Process...")
    for i in range(101):
        time.sleep(0.05)
        display_progress_bar(i/100.0)
    
    time.sleep(1)
    print("\n\nEncryption Successful!")
    time.sleep(1)
    print(f"Encryption Key: {''.join([str(random.randint(0, 9)) for _ in range(16)])}")

if __name__ == "__main__":
    try:
        fake_quantum_computation()
    except KeyboardInterrupt:
        print("\n\nQuantum Encryption Aborted!")

