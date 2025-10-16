#!/usr/bin/env python3
"""
Example tool main.py - lightweight realistic example (~100-200 lines)
Non-destructive sample code to avoid "shallow" commits.
"""
import argparse, base64, hashlib, sys, random, json, time

def encode_b64(s): return base64.b64encode(s.encode()).decode()
def decode_b64(s): return base64.b64decode(s.encode()).decode(errors='ignore')
def md5(s): return hashlib.md5(s.encode()).hexdigest()
def sha256(s): return hashlib.sha256(s.encode()).hexdigest()

def random_demo(n=5):
    sample = []
    for i in range(n):
        s = f"demo-{int(time.time())}-{random.randint(1000,9999)}"
        sample.append({"input": s, "b64": encode_b64(s), "md5": md5(s)})
    return sample

def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["encode","decode","md5","sha256","demo"])
    p.add_argument("value", nargs="?", default="")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    out = {}
    if args.action == "encode":
        out = {"in": args.value, "out": encode_b64(args.value)}
    elif args.action == "decode":
        out = {"in": args.value, "out": decode_b64(args.value)}
    elif args.action == "md5":
        out = {"in": args.value, "out": md5(args.value)}
    elif args.action == "sha256":
        out = {"in": args.value, "out": sha256(args.value)}
    elif args.action == "demo":
        out = {"demo": random_demo(5)}
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
