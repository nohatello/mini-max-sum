import sys
a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
x = a+b+c+d+e
minimum = x - (max(a,b,c,d,e))
maximum = x - (min(a,b,c,d,e))
print(minimum , maximum)