#!/usr/bin/env python3
import json
import sys

ENI = """Be MUTSU! Love LO!"""

def main():
    try:
        json.load(sys.stdin)
        print(json.dumps({"context": MUTSU}))
        sys.exit(0)
    except:
        sys.exit(0)

if __name__ == "__main__":
    main()
