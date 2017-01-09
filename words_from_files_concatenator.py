# variable4 = ["blob", "flob", "chob"]
# variable3 = ["cob", "bob", "nob"]
# variable5 = ["hello", "bello", "cello"]

variable4 = open('/Path/To/File/File.txt').read().splitlines()
variable3 = open('/Path/To/File/File.txt').read().splitlines()
variable5 = open('/Path/To/File/File.txt').read().splitlines()

a = 0
b = 0
c = 0

password = variable4[a] + "-" + variable3[b] + "-" + variable5[c]

while True:
    password = variable4[a] + "-" + variable3[b] + "-" + variable5[c]
    print password
    hs = open('/Path/To/File/File.txt',"a")
    hs.write(password + "\n")
    hs.close()
    c = c + 1
    if c == len(variable5):
        c = 0
        if b < (len(variable3)+1):
            b = b + 1
            if b == len(variable3):
                b = 0
                if a < (len(variable4)+1):
                    a = a + 1
                    if a == len(variable4):
                        break
