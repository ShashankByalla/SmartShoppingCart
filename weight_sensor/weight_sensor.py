import random
import time

def read_weight():
    weight = random.uniform(0.5, 5.0)  # Simulate weight in kg
    print(f"Weight detected: {weight:.2f} kg")
    return weight

if __name__ == "__main__":
    while True:
        time.sleep(2)  # Wait for 2 seconds before reading again
        read_weight()
