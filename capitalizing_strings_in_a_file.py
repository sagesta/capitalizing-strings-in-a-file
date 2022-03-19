file = input ("please enter a file name\n")
try:
    fname = open(file)
except:
    print ("you have entered an incorrect name\n")
    exit()

for line in fname:
    line = line.rstrip()
    line = line.upper()
    print (line)