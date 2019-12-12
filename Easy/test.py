




s = 'Hello World !'
out = s[::2]
if not len(s) % 2:
    out += s[::-1]
else:
    out += s[::-1]
print(''.join(out))


