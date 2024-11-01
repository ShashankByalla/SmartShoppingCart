import random
import json

def scan_item():
    items = json.load(open('../data/items.json'))
    scanned_item = random.choice(items)
    print(f"Scanned: {scanned_item['name']}")
    return scanned_item

if __name__ == "__main__":
    while True:
        input("Press Enter to scan an item...")
        scan_item()
