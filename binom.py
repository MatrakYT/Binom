ilk_sayi=input("ilk değişken: ")
ikinci_sayi=input("İkinci değişken: ")
ust_sayi=input("ust sayi: ")
islem=input("islem: ")

n=0
v=int(ust_sayi)+1
b=int(ust_sayi)
while not v == n:
    a=f"({b} {n})*{ilk_sayi} üssü {b-n}*{ikinci_sayi} üssü {n} {islem}"
    print(a)
    n+=1