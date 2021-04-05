l1  = [1,5,4,8]
l2  = [8,4,5,9,8]
l3  = [8,8,7,5,4]

# TODO: method: 1

s1 = sum(l1)
s2 = sum(l2) 
s3 = sum(l3)

print(s1,s2,s3)

# TODO: method: 2

s1, s2, s3  = sum(l1), sum(l2), sum(l3)
print(s1,s2,s3)

# TODO: method: 3

s1, s2, s3 = map(sum,(l1,l2,l3))
print(s1,s2,s3)
