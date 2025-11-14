import stdio
import stdrandom

# 1. Rastgele 4 farklı rakam oluştur
digits = []
while len(digits) < 4:
    d = stdrandom.uniformInt(0, 10)
    if d not in digits:
        digits += [d]

# 2. Oyunu başlat
stdio.writeln("4 haneli farklı rakamlardan oluşan sayıyı tahmin et!")
stdio.writeln("Her tahminden sonra doğru yerdeki rakam sayısını + olarak alırsın.")

while True:
    stdio.write("Tahminini gir : ")
    guess = stdio.readString()

    # Tahmin kontrolü (4 rakam ve hepsi farklı mı)
    if len(guess) != 4 or not guess.isdigit():
        stdio.writeln("Lütfen 4 rakamdan oluşan bir sayı gir.")
        continue
    if len(set(guess)) != 4:
        stdio.writeln("Rakamlar birbirinden farklı olmalı.")
        continue

    # + sayısını hesapla (doğru yerde doğru rakam)
    plus = 0
    for i in range(4):
        if int(guess[i]) == digits[i]:
            plus += 1

    stdio.writeln('+' + str(plus))

    # Eğer hepsi doğruysa kazanır
    if plus == 4:
        stdio.writeln("Tebrikler! Sayıyı doğru tahmin ettin!")
        break
