import sys, string, md5hash

print("Enter your full name: ")
line = sys.stdin.readline()
line = line.rstrip()

md5_obj = md5hash.new()
md5_obj.update(line)

print(md5_obj.hexidigest())