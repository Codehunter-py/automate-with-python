#!/usr/bin/env python3 

import sys 
import re 

usernames = {}
logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r"CRON \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1 
print(usernames)

