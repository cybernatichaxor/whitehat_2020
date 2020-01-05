from pwn import *
import math


def CountTriangles(n): 
    count = 0; 
      
    for i in range(n, 1, -1): 
        l = 1; 
        r = i - 1; 
        while(l < r): 
            if(l + r > i): 
                count += r - l;  
                r -= 1;  
              
            else: 
                l += 1;  
    return count;

def CountTriangles2(n):
    if(n <= 4):
        return 0
    else:
        n = n-4
        return int(math.floor((n+2) * (n+4) * ((2*n)+3) / 24))


conn = remote('15.164.75.32',1999)
count = 1
while(count < 4):
    print conn.recvuntil('n = ')
    n = conn.recvline()
    print n
    conn.sendline(str(CountTriangles2(int(n))))
    count = count + 1

print conn.recvall()
