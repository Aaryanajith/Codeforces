n = int(input("Enter the number of friends"))

m = list(map(int, input("friends").split())) 

a = {}

for i in range(n):
    a[m[i]] = i+1
    
for i in range(n):
    print(a[i+1], end = " ")
