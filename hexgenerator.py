import random

hexchars = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

key = ""
text = ""
for i in range(16):
    key += random.choice(hexchars)

for i in range(1000):
    text += random.choice(hexchars)

print(key)
print(text)