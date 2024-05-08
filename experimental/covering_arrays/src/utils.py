#!/usr/bin/env python

import os
import pandas as pd
import random
import subprocess

def read_in_configs(path_to_configs="./data/flags/MacOS.csv"):
    if not os.path.exists(path_to_configs):
        raise FileNotFoundError(f"The file '{path_to_configs}' does not exist.")

    try:
        df = pd.read_csv(path_to_configs, sep=',')
        return df
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

def get_util_flags(df, util):
    """
    Load flags for a particular utility.

    Args:
        df (pandas.DataFrame): DataFrame containing the utility flags.
        util (str): Name of the utility to retrieve flags for.

    Returns:
        list: List of flags for the specified utility, or an empty list if no flags are found.
    """
    if 'program' not in df.columns:
        raise ValueError("The DataFrame does not contain a 'program' column.")

    if util not in df['program'].values:
        raise ValueError(f"The utility '{util}' does not exist in the DataFrame.")

    flags = df.loc[df['program'] == util, 'flags'].values
    if len(flags) == 0:
        return []

    return flags[0].split(',')

def sample_command(command_utility, command_flags, prob = 0.5):
    """
    Generates a random command based on the given parameters.
    
    Args:
        command_utility: The utility or purpose of the command.
        command_flags: A list of flags or options for the command.
        prob: The probability of including each flag in the command. Default is 0.5.
    
    Returns:
        A randomly generated command as a string.
    """
    flags = [flag for flag in command_flags if random.random() < prob]
    
    command = command_utility + " " + " ".join(flags)

    return command

def sample_commands(n, command_utility, command_flags, prob = 0.5):
    """
    Generates a random subset of commands based on the given parameters.
    
    Args:
        n: The number of commands to sample.
        command_utility: The utility or purpose of the commands.
        command_flags: A list of flags or options for the commands.
        prob: The probability of including each command in the subset. Default is 0.5.
    
    Returns:
        A list of randomly sampled commands.
    """
    commands = [sample_command(command_utility, command_flags, prob) for _ in range(n)]
    return commands

def read_in_covering_array(t, k, v, file_path="./data/covering_arrays/"):
    """
    Reads in a covering array from a table created by NIST.
    Notation: CA(t, k, v)
    t : strength of array, number of factors covered simultaneously (2, 3, ...)
    k : number of factors
    v : number of levels of each factor
    """
    file_name = f"ca.{t}.{v}^{k}.txt"
    file_location = os.path.join(file_path, file_name)

    try:
        with open(file_location, "r") as f:
            out = f.read().splitlines()
            out = out[1:]  # remove first line, which is number of configs in CA
            out = [a.strip() for a in out]
        return out
    except FileNotFoundError:
        raise FileNotFoundError(f"Covering array file '{file_name}' not found.")
    except IOError:
        raise IOError(f"Error reading covering array file '{file_name}'.")

def cover_array_commands(util, flags, t, v):
    k = len(flags)
    cover_array = read_in_covering_array(t, k, v)
    commands = []

    for config in cover_array:
        command = util

        # Split the configuration into indicators for each flag
        indicators = config.split()

        for idx, indicator in enumerate(indicators):
            if indicator == '-':
                # If the indicator is '-', randomly choose '0' or '1'
                indicator = random.choice('01')

            if indicator == '1':
                # If the indicator is '1', add the corresponding flag to the command
                command += ' ' + flags[idx]

        commands.append(command)

    return commands

def fuzz(commands, timeout = 10, fnull = open(os.devnull, 'w')):
    retcodes = [
        subprocess.call(command, shell=True, stdout=fnull, stderr=subprocess.STDOUT, timeout=timeout)
        for command in commands
    ]
    df = pd.DataFrame({'command': commands, 'return_code': retcodes})
    return df
