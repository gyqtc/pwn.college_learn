l = "78 78 78 78 7a 7c 7f 7f 71 71 73 73 73 75 75 74 74 77 76 76 69 68 6a 6d 6c 6c 6c 6f 6e 6e 6e 6e 61 61 60 60 63"
l = l.split(' ')
print(l)
print(len(l))
for i in range(len(l)):
    l[i] = chr(int(l[i], 16))
print(l)
for i in range(len(l)):
    l[i] = chr(ord(l[i]) ^ 0x19)
print(l)
t = l[8]
l[8] = l[23]
l[23] = t
print(l)
t = l[3]
l[3] = l[24]
l[24] = t
print(l)
s = []
i = 36
while i >= 0:
    s.append(l[i])
    i -= 1
print(s)
t = s[6]
s[6] = s[31]
s[31] = t
print(s)
l = []
i = 36
while i >= 0:
    l.append(s[i])
    i -= 1
print(l)
s = ''
for i in l:
    s += i
print(s)
