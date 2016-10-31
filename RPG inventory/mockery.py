'''a =[1,3,5]
b=[2,4,6]
c=a+b
d= sorted(c)
d.reverse()
c[3] = 42
c.extend([7,8,9])
print(c[0:4])
print(d[-1])
print(len(d))


a = (2,4,6,8)
b = (10,12,14,16)
c= a+b
d= sorted(c)
print(d[3])
print(d[-3:])
print(len(d))


a = {1,2,3,4}
b = {1,3,5,7}

c = a | b
d = a - b
e = b - a 
f = a & b
g = a ^ b
print(c)

a = (list(range(21)))
b = (list(range(3, 13)))
c = (list(range(2, 51, 3)))
print(a, '\n', b, '\n', c)
'''
