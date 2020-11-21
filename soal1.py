arrBerat = []
bMin = 0
bMax = 0

def hitungMin(arrBerat):
    nMin = arrBerat[0]
    for n in range(1, len(arrBerat)):
       if(arrBerat[n] < nMin):
            nMin = arrBerat[n]
    return nMin

def hitungMax(arrBerat):
    nMax = arrBerat[0]
    for n in range (1, len(arrBerat)):
        if(arrBerat[n] > nMax):
            nMax = arrBerat[n]
    return nMax


def rerata(arrBerat):
    total = sum(arrBerat) / n
    return total


print('Masukkan Banyak Data Berat Balita : ', end=" ")
n = int(input())

for i in range(n):
    berat = float(input(f'Masukkan Berat Balita Ke-{i+1} : '))
    arrBerat.append(berat)

print("-----------------------------------------------------------------")
print("Berat balita maximum: ", hitungMax(arrBerat))
print("Berat balita minimum: ", hitungMin(arrBerat))
print("Rerata berat balita: ", rerata(arrBerat))
print("-----------------------------------------------------------------")

