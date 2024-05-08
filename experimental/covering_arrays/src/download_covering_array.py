#!/usr/bin/env python3

import argparse
import utils

def get_args():
    parser = argparse.ArgumentParser(description="Covering Array Fuzzer")
    parser.add_argument("-t", type=int, help="Strength of the covering array")
    parser.add_argument("-k", type=int, help="Number of factors")
    parser.add_argument("-v", type=int, help="Number of levels of each factor")
    
    return parser.parse_args()

def main():

    args = get_args()

    utils.download_covering_array(args.t, args.k, args.v)
    return None

if __name__ == "__main__":
    main()
