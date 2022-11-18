#! kullanıcıdan vize ve final notları alacak.
#! vize %40  final %60 etkili olacak
#! vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
#! uygulama ortalamayı hesaplayacak ve ortalamaya göre
#! 0-49 FF
#! 50-60 DD
#! 60-70 CC
#! 70-80 BB
#! 80-100 AA
#! not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız.

vizeInput = input()
vizeGrade = float(vizeInput)

finalInput = input()
finalGrade = float(finalInput)

ortalama = float(vizeGrade*0.4 + finalGrade*0.6 )

print(f"Not Ortalamasi = {ortalama}")

if (ortalama>=0) & (ortalama<= 49):
    print("FF")
elif (ortalama>=50) & (ortalama<=60):
    print("DD")
elif (ortalama>60) & (ortalama<=70):
    print("CC")
elif (ortalama>70) & (ortalama<=80):
    print("BB")
elif (ortalama>80) & (ortalama<=100):
    print("AA")
else:
    print("Hata")   
