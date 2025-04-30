def apakah_prima(bil):
    if bil < 2:
        return False
    for i in range (2,int(bil**0.5) + 1):
        if bil % i == 0:
            return False
    return True

def temukan_prima (data):
    prima = [bil for bil in data if apakah_prima(bil)]
    return prima, len (prima)

data = [4,5,11,12,14,16,16,19]

bilangan_prima, jumlah_prima = temukan_prima(data)

print("Yang termasuk bilangan prima: ", bilangan_prima)
print('Jumlah bilangan prima dalam data: ', jumlah_prima)