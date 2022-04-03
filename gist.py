import os
import subprocess

# result = subprocess.run(["pwd"], capture_output=True)
# print(result.stdout.decode().split())

# stout_re = result.stdout.decode().split()

# home_dir = "/home/test/automate-with-python"

# if home_dir in stout_re:
#     print(f"{home_dir} is in {stout_re}")

# import shlex
# command_line = input()

# args = shlex.split(command_line)
# print(args)

# p = subprocess.Popen(args) # Success!

# p1 = Popen(["dmesg"], stdout=PIPE)
# p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
# p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
# output = p2.communicate()[0]

# output = subprocess.check_output("git add . && git commit -m 'commit from python subprocess module' && git push origin master", shell=True)
# print(output.decode())

