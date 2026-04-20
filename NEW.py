s = "abc"
total = 0

for i in range(len(s)):
    reversed_pos = 26 - (ord(s[i]) - ord('a'))

    print(ord(s[i]) - ord('a'))
    print(reversed_pos)
    
    total += reversed_pos * (i + 1)

print(total)
print(ord('b'))