 # . square pattern

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
       print("*", end =" ")
    print()

# 2. hollow square pattern
# 1. take inputs
# 2. print square 
# 3. apply a condition

n=5 
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

 #3. rectangle pattern
n=5 
m=7
for i in range(1,n+1):
    for j in range(1,m+1):
        print("*", end=" ")
    print()
    
# hollow rectangle
n=5 
m=7
for i in range(1,n+1):
    for j in range(1,m+1):
        if i==1 or i==n or j==1 or j==m:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

# rightangle triangle left aligned , inverse also

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
        
    print()
    
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
        
    print()
    
 #hollow rightangle triangle left aligned , inverse also
 
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        
    print()
    
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        
    print()

# rightangle triangle right aligned , inverse also
n = 5
for i in range(1, n+1):
    # spaces
    for j in range(1, n-i+1):
        print(" ", end=" ")
    
    # stars
    for j in range(1, i+1):
        print("*", end=" ")
    
    print()
n = 5
for i in range(n,0,-1):
    # spaces
    for j in range(1, n-i+1):
        print(" ", end=" ")
    
    # stars
    for j in range(1, i+1):
        print("*", end=" ")
    
    print()
    

n = 5
for i in range(1, n+1):
    # spaces
    for j in range(1, n-i+1):
        print(" ", end=" ")
    
    # stars
    for j in range(1, i+1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()

n = 5
for i in range(n, 0, -1):
    # spaces
    for j in range(1, n-i+1):
        print(" ", end=" ")
    
    # stars
    for j in range(1, i+1):
        if i == n or i == 1 or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()





