def esconde_palavra(word: str, chutes: str) -> str:
    resp = ""
    for letra in word:
        if letra in chutes:
            resp = resp + letra + " "
        else:
            resp = resp + "_"
    return resp

palavra = "Alemanha"
letras_chutadas = ""
err = 0
segredo = esconde_palavra(palavra, letras_chutadas)
while '_' in segredo and err <6:
 print(segredo)
 print(f"erros: {err}")
 letra = input("letra: ").lower()
 if not letra in palavra.lower():
     err = err + 1
 letras_chutadas = letras_chutadas + letra
 segredo = esconde_palavra(palavra, letras_chutadas)

if err >= 6:
    print(f"voce foi enforcado, a palavra era {palavra}")
else:
    print(f"parabens, vc acertou a {palavra}")


  
