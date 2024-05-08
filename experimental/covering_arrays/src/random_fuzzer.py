#!/usr/bin/env python3

import argparse
import utils

def get_args():
    # Get command-line arguments
    
    parser = argparse.ArgumentParser(description="Covering Array Fuzzer")

    parser.add_argument("-n",
                        "--number",
                        type=int,
                        help="Number of times to fuzz utility")
    
    parser.add_argument("-u",
                        "--utility",
                        type=str,
                        help="Name of the utility")
    
    parser.add_argument("-d",
                        "--debug",
                        action=argparse.BooleanOptionalAction,
                        default=False,
                         help="Include this flag to print debugging information")

    return parser.parse_args()

def main():

    args = get_args()
    utility = args.utility

    # Generate commands based on the covering array
    df = utils.read_in_configs(path_to_configs="./data/flags/Windows.csv")
    flags = utils.get_util_flags(df, utility)
    commands = utils.sample_commands(args.number, utility, flags)

    # Run the fuzzer with the generated commands
    try:
        results = utils.fuzz(commands)
        if args.debug:
            print(results.head(n = 10))
    except Exception as e:
        print(f"An error occurred while running the fuzzer: {e}")

if __name__ == "__main__":
    main()
