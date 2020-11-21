klub1 = []
klub2 = []

InputKlub1 = str(input("Klub A : " ))
InputKlub2 = str(input("Klub B : " ))

n = 1
while n >= 1:
    skor = input("Masukkan Skor Pertandingan : ")
    skor = skor.split()
    skor1 = int(skor[0])
    skor2 = int(skor[1])
    if skor1 < 0 or skor2 < 0:
        break

    klub1.append(skor1)
    klub2.append(skor2)

for a in range(len(klub2)):
    if klub1[a] > klub2[a]:
        print("Hasil ",a + 1,": ",InputKlub1)
    elif klub1[a] < klub2[a]:
        print("Hasil ",a + 1 ,": ",InputKlub2)
    elif klub1[a] == klub2[a] :
        print("Hasil ",a + 1,": SERI")