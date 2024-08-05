#!/usr/bin/env python3


'''
OPS445 Assignment 2 - SUMMER 2024
Program: assignment1.py
The python code in this file is original work written by
Peter De Vos. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Peter De Vos - 118298165
Description: Assignment 2 - Version A
This script will return an end date, based off a starting date, and a number of days to count forward from it.
'''



import argparse
import os
import sys

def parse_command_args() -> object:
    """Set up argparse here. Call this function inside main."""
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",
                                     epilog="Copyright 2023")
    parser.add_argument("-H", "--human-readable", action='store_true', help="Prints sizes in human-readable format")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("program", type=str, nargs='?',
                        help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    return parser.parse_args()

def percent_to_graph(percent: float, length: int = 20) -> str:
    """Turns a percent 0.0 - 1.0 into a bar graph."""
    filledBarLength = int(percent * length)
    if percent * length > filledBarLength:
        filledBarLength += 1
    emptyBarLength = length - filledBarLength
    return '#' * filledBarLength + ' ' * emptyBarLength

def get_sys_mem() -> int:
    """Return total system memory (used or available) in kB."""
    memInfoFilePath = '/proc/meminfo'
    memTotalLine = 'MemTotal'
    with open(memInfoFilePath) as memInfoFile:
        for line in memInfoFile:
            if line.startswith(memTotalLine):
                return int(line.split()[1])
    return 0

def get_avail_mem() -> int:
    """Return total memory that is currently in use."""
    memInfoFilePath = '/proc/meminfo'
    memAvailableLine = 'MemAvailable'
    with open(memInfoFilePath) as memInfoFile:
        for line in memInfoFile:
            if line.startswith(memAvailableLine):
                return int(line.split()[1])
    return 0

def pids_of_prog(app_name: str) -> list:
    """Given an app name, return all PIDs associated with app."""
    return os.popen(f'pidof {app_name}').read().strip().split()

def rss_mem_of_pid(proc_id: str) -> int:
    """Given a process ID, return the Resident memory used."""
    rss = 0
    try:
        with open(f'/proc/{proc_id}/smaps') as f:
            for line in f:
                if line.startswith('Rss:'):
                    rss += int(line.split()[1])
    except FileNotFoundError:
        pass
    return rss

def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """Turn 1,024 into 1 MiB, for example."""
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    return f'{result:.{decimal_places}f} {suffixes[suf_count]}'

"""The issue is having nothing that takes the information found, manipulating it, and formatting it.
   To properly do this without global variables, 3 new functions we're created:
   format_memory_usage, prepare_memory_usage_output, and prepare_program_usage_output.
   I will explain what each does in their definitions."""

def format_memory_usage(firstLine: str, percentUsed: float, usedMemory: int, totalMemory: int, args) -> str:
    """This function calculates and formats the data into a string.
       Overall I chose to split the roles of gathering, calculating, and processing information.
       This function is used to format the memory gathered into a readable string.
       Rather than putting this code into bytes_to_human_r, I attempted modularity for easier function calls."""
    
    # Takes the percentage and creates the graph visualization
    barGraph = percent_to_graph(percentUsed, args.length)

    # Displays human-readable memory, or raw KiB format
    if args.human_readable:
        usedMemoryDisplay = bytes_to_human_r(usedMemory)
        totalMemoryDisplay = bytes_to_human_r(totalMemory)
    else:
        usedMemoryDisplay = str(usedMemory)
        totalMemoryDisplay = str(totalMemory)

    # Return the final formatted string
    return f"{firstLine:<12} [{barGraph}| {int(percentUsed * 100)}%] {usedMemoryDisplay}/{totalMemoryDisplay}"

def prepare_memory_usage_output(args) -> str:
    """This function does the calculations for system-wide memory usage."""
    totalMemory = get_sys_mem()  # Retrieve total memory
    availableMemory = get_avail_mem()  # Retrieve available memory
    usedMemory = totalMemory - availableMemory  # Calculate used memory
    percentUsed = usedMemory / totalMemory
    return format_memory_usage("Memory", percentUsed, usedMemory, totalMemory, args)

def prepare_program_usage_output(args) -> str:
    """This function gets the memory data for all processes under the program specified by the user
       and passes raw data to format_memory_usage to be correctly formatted.
       I utilize a list to add and append data entries to, depending on if it's for RSS memory."""

    # First, checking how much memory there is in total and the list of PIDs
    totalMemory = get_sys_mem()
    pids = pids_of_prog(args.program)

    # Returning a string if no PID is found
    if not pids:
        return f"{args.program} not found."

    memDataList = []  # List for the memory data
    totalProgramMemory = sum(rss_mem_of_pid(pid) for pid in pids)  # RAM/RSS memory total for specified program

    # Loop through the processes to find the percentage of the memory used by each process, and adding it to the list
    for pid in pids:
        rssMemory = rss_mem_of_pid(pid)
        percentUsed = rssMemory / totalMemory
        rawMemoryData = format_memory_usage(pid, percentUsed, rssMemory, totalMemory, args)  # Pass PID as identifier
        memDataList.append(rawMemoryData)

    # If the program uses memory, add a line for the program's total memory usage
    if totalProgramMemory > 0:
        percentUsed = totalProgramMemory / totalMemory
        rawMemoryData = format_memory_usage(args.program, percentUsed, totalProgramMemory, totalMemory, args)
        memDataList.append(rawMemoryData)

    # Combine all the list items and return them as a single string
    return "\n".join(memDataList)

if __name__ == "__main__":
    args = parse_command_args()

    if not args.program:
        memoryOutput = prepare_memory_usage_output(args)
        print(memoryOutput)
    else:
        programOutput = prepare_program_usage_output(args)
        print(programOutput)

