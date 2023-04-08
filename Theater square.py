import math

n, m, a = map(int, input("Enter the size of the rectangle and size of each flagstone").split())

row = math.ceil(n/a)
col = math.ceil(m/a)

print("Total no of flagstones required: ", row*col)
    