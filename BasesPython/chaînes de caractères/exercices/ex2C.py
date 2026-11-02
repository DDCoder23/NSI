print(ord("z"))
mot = input("plaintext \n").lower()
clé = input("clé" )
ciphertext = []
for plain in mot :
    ci = ord(plain)
    if not plain == " ":
        ci = ord(plain)
        ci += int(clé)
        if ci > 122:
            ci -=26
    ciphertext.append(chr(ci))
    print(ci)
for i in range (len(ciphertext)):
    print(f"{ciphertext[i]}" )
    
    
    
    
