import random

yapılanTahmin = 0

print('Selam! İsmini Öğrenebilir miyim?\n')
benimAdım = input()

numara = random.randint(1,20)
print ('Tamam ' + benimAdım+ ' 1 ile 20 arasında bir numara düşünüyorum.')

while yapılanTahmin < 6:

    print('Bir tahmin yapın: ')
    tahmin = input()
    tahmin = int(tahmin)

    yapılanTahmin = yapılanTahmin + 1

    if tahmin < numara:
        print ('Tahmininiz çok düşük.')
    
    if tahmin > numara:
        print ('Tahmininiz çok yüksek.')

    if tahmin == numara:
        break

if tahmin == numara:
    yapılanTahmin = str(yapılanTahmin)
    print('İyi iş, ' + benimAdım + ' Numaramı ' + yapılanTahmin + ' tahminde buldun')
if tahmin != numara:
    numara = str(numara)
    print ('Hayır. Seçtiğim numara ' + numara + 'idi')