from __future__ import print_function
import sys
import signal

num_args = len(sys.argv)
assert (num_args >= 2)

machine = sys.argv[1]

# OPEN THE SPECIFIED MACHINE
RM = open(machine)
print (RM.readline())

# INIT INSTRUCTION ARRAY
inst = int(RM.readline())
IS = []
lines = inst*['']
print(inst)

# INIT THE REGISTERS SET, READING FROM ARGV FOR INITIAL VALUES
input_regs = RM.readline().split()
regs = {}
a = 2
for r in input_regs:
    if (num_args > a):
        regs[r] = int(sys.argv[a])
        a+=1
    else:
        regs[r] = 0
print(regs)

#READ INSTRUCTION
i = 0
while(i < inst):
    line = RM.readline()
    lines[i]+= line
    if line.startswith('//'):
        print("COMMENT: ",end='') 
    else:
        IS.append(line.split()[1:])
        #instruction type
        #HALT
        if(IS[i][0] == 'halt'):
            IS[i][0] = 0  
        #INC
        elif(IS[i][0] == 'inc'):
            IS[i][0] = 1
            if IS[i][1] not in regs:
                regs[IS[i][1]] = 0
            IS[i][2] = int(IS[i][2])
        #DEC
        elif(IS[i][0] == 'dec'):
            IS[i][0] = 2
            if IS[i][1] not in regs:
                regs[IS[i][1]] = 0
            IS[i][2] = int(IS[i][2])
            IS[i][3] = int(IS[i][3])
        else:
            print("illegal instruction", IS[i][0])
            sys.exit(1)
        i += 1
    print(line, end='')
print(IS)

for e in lines:
    print (e, end='')
print(regs)
print(len(IS))
i = 0
while(True):
    #instruction type
    #HALT
    if(IS[i][0] == 0):
        break
    #INC
    elif(IS[i][0] == 1):
        regs[IS[i][1]] += 1
        i = IS[i][2]
    #DEC
    elif(IS[i][0] == 2):
        if(regs[IS[i][1]] == 0):
            i = IS[i][3]
    #DEC
        else:
            regs[IS[i][1]] -= 1
            i = IS[i][2]
    else:
        print("illegal instruction", IS[i][0])
        sys.exit(1)
    print(i, regs)
print(regs)
