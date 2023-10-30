n=int(input())
c=0
for i in range(2**n):
    if '11' not in bin(i):
        c+=1
print(c)
        


"""
The function accepts an integer 'n' as its argument where 'n' is the number of bits. Implement the function to find and return the count of all distinct binary strings of length 'n' without consecutive set bits (i.e. without consecutive 1's).
Note:
n>=0
If n= 0 return -1
Do not allocate extra memory
I
Example:
Input:
n:3
Output:
5
All possible 3 bit binary strings are 000, 001, 010, 011, 100, 101,110 and 111. Count of binary strings without consecutive set bits is 5(000,001,010,100 and 111)

"""