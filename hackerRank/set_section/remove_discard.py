"""
Task

You have a non-empty set , and you have to execute commands given in lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer , the number of elements in the set .
The second line contains space separated elements of set . All of the elements
are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next lines contains either pop, remove and/or discard commands followed by
their associated value.


"""

n = input()
s = set(map(int, raw_input().split())) 
for _ in range(int(raw_input())):
    command=[i for i in raw_input().strip().split()]
    if(command[0]=='pop'):s.pop()
    elif(command[0]=='remove'):s.remove(int(command[1]))
    elif(command[0]=='discard'):s.discard(int(command[1]))
    

print sum(s)
