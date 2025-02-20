from tqdm import tqdm
import time

def en_progress(test):
    print("\n"+ test+"crypting...\n")
    for _ in tqdm(range(100)):
        time.sleep(0.03)  # Simulate work being done

def dec_progress(test):
    print("\n"+ test+"crypting...\n")
    for _ in tqdm(range(100)):
        time.sleep(0.02)