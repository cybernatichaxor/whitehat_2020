from pwn import *
import math


def CountTriangles(n): 
  
    #n = len(A); 
  
    #A.sort();  
  
    count = 0; 
      
    for i in range(n, 1, -1): 
        l = 1; 
        r = i - 1; 
        while(l < r): 
            if(l + r > i): 
  
                # If it is possible with a[l], a[r] 
                # and a[i] then it is also possible 
                # with a[l+1]..a[r-1],a[r] and a[i] 
                count += r - l;  
  
                # checking for more possible solutions 
                r -= 1;  
              
            else: 
  
                # if not possible check for  
                # higher values of arr[l] 
                l += 1;  
    #print("No of possible solutions: ", count);
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
    #print conn.recvline()
    conn.sendline(str(CountTriangles2(int(n))))
    count = count + 1
    #print conn.recvline()

print conn.recvall()
#print CountTriangles2(9999)
