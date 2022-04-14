#!/usr/bin/python3

import re
import subprocess

def diskCapacity():
    """Functions returns integer/float that represents total size of /opt/bsi
    in human readable format with gigabytes """

    opt_bsi_size = subprocess.check_output("df -h /opt/bsi", shell=True).decode()
    pattern = r"(\d+(?:\.\d+)?)"
    result = re.findall(pattern, opt_bsi_size)
    result = float(result[0]) if '.' in result[0] else int(result[0])
    return result

def elkSnapsSize():
    """Function returns integer/float that represents how much gigabytes elasticsearch's 
    monthly snaps totally taking space in /opt/bsi/data"""

    opt_bsi_data = subprocess.check_output("cd /opt/bsi/data && du -sh elasticsearch", shell=True).decode()
    pattern_elk = r"(\d+(?:\.\d+)?)"
    result_elk = re.findall(pattern_elk, opt_bsi_data)
    result_elk = float(result_elk[0]) if '.' in result_elk[0] else int(result_elk[0])
    return result_elk

def diskAvail():
    """Functions returns integer/float that represents available size of /opt/bsi
    in human readable format with gigabytes """

    opt_bsi_avail = subprocess.check_output("df -h /opt/bsi", shell=True).decode()
    pattern_avail = r"(\d+(?:\.\d+)?)"
    result_avail = re.findall(pattern_avail, opt_bsi_avail)
    result_avail = float(result_avail[2]) if '.' in result_avail[2] else int(result_avail[2])
    return result_avail

def calculate():
    """ Function displays how much elasticsearch's montly snaps could fit in available space"""
    print("\nTotal size of /opt/bsi is:", diskCapacity(),"G\n")
    print("Available space:", diskAvail(),"G\n")
    print("Total size of elasticsearch's snaps:", elkSnapsSize(),"G\n")
    snaps_count = int(input("Enter total number of monthly snaps: "))
    print(f"\nSince montly-snaps policy was defined, {snaps_count} snapshot(s) captured which one(s) take {elkSnapsSize()}G space all together.\n")

    total_snaps_size = elkSnapsSize()
    if snaps_count > 1:
        try:
            each_snap = total_snaps_size / snaps_count
            print(f"Each snapshot needs around ~{each_snap:.2f}G for every month.")
        except ZeroDivisionError:
            pass
    
    display = input("\nDisplay number of monthly snaps could fit in available space: y/n ")

    if display == "y":
        diskAvailable = diskAvail()
        result = diskAvailable / each_snap
        print(f"\nApproxmately {result:.1f} monthly snap(s) could fit in the /opt/bsi available space.")

calculate()
