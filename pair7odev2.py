

n = int(input("kullanıcı sayısını giriniz: "))
toplamGecen = 0
toplamKalan = 0


for i in range(1,n+1):
    vizeGrade = float(input())
    finalGrade = float(input())
    ortalama = float(vizeGrade*0.4 + finalGrade*0.6 )
    if ortalama<50:
        print("Kaldiniz")
        toplamKalan+=1
    else:
        print("Geçtiniz")
        toplamGecen+=1

    print(f'Vize:{vizeGrade}  Final:{finalGrade}  Ort:{ortalama}')
print(f"Toplam Geçen: {toplamGecen}")
print(f"Toplam Kalan: {toplamKalan}")
