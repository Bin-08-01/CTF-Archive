a=[0x48, 0x54, 0x42, 0x7b, 0x54, 0x48, 0x33, 0x5f, 0x53, 0x33, 0x43, 0x52, 0x33, 0x54, 0x53, 0x5f, 0x34, 0x52, 0x33, 0x5f, 0x52, 0x33, 0x56, 0x33, 0x34, 0x4c, 0x33, 0x44, 0x5f, 0x31,0x4e,0x5f,0x54,0x48,0x33,0x5f,0x44,0x33,0x42,0x55,0x47,0x47,0x33,0x52,0x7d]

flag = ""

for i in a:
    flag += chr(i)
print(flag)