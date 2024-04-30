#!/usr/bin/env python3

import argparse
import os
from utils import read_in_configs, get_util_flags, cover_array_commands, fuzz

def get_args():
    parser = argparse.ArgumentParser(description="Covering Array Fuzzer")
    parser.add_argument("-t", type=int, help="Strength of the covering array")
    parser.add_argument("-v", type=int, help="Number of levels of each factor")
    parser.add_argument("-u", "--utility", type=str, help="Name of the utility")

    return parser.parse_args()

def main(t, v, utility):

    # Generate commands based on the covering array
    df = read_in_configs()
    flags = get_util_flags(df, utility)
    commands = cover_array_commands(utility, flags, t, v)

    # Run the fuzzer with the generated commands
    try:
        results = fuzz(commands)
        print(results)
    except Exception as e:
        print(f"An error occurred while running the fuzzer: {e}")

if __name__ == "__main__":

    args = get_args()
    main(args.t, args.v, args.utility)
