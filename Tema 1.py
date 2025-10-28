import string

articol = """Anunțul a fost făcut de primarul municipiului, Doru Dăncuș, în condiții de austeritate bugetară, creșteri de impozite și taxe de până la 70% pentru populație, precum și concedieri anunțate în sectorul bugetar. Chiar și așa, municipalitatea a ales să susțină financiar, în continuare, un club sportiv.

„Facem un efort constant de a menține funcțional clubul și, în limita bunului simț, pe lângă alte categorii de investiții, vom mai aloca din bugetul local suma de 10 milioane lei, pe lângă cei 15 milioane lei pe care clubul i-a primit de la începutul anului. Bugetul de funcționare va fi în limita parametrilor anului 2024, dar și cu obligații care prevăd rezultate în toate categoriile de competiții sportive”, a declarat vineri pentru Agerpres Doru Dăncuș."""

lungime = len(articol)
jumatate = lungime // 2

prima_parte = articol[:jumatate]
a_doua_parte = articol[jumatate:]

prima_parte = prima_parte.upper().strip()

a_doua_parte = a_doua_parte[::-1]
if a_doua_parte:
    a_doua_parte = a_doua_parte[0].upper() + a_doua_parte[1:]

punctuatie = ".,!?"
a_doua_parte = ''.join(ch for ch in a_doua_parte if ch not in punctuatie)

rezultat = prima_parte + a_doua_parte

print(rezultat)
