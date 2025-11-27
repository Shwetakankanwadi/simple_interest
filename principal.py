import sys

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    principal = 1000
    rate = 5
    time = 2
    
simple_interest = (principal*rate*time) / 100

print("Principal Amount:",principal)
print("Rate of Interest:",rate)
print("Time (Years):",time)
print("Simple Interest:",simple_interest)
