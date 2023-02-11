capitals = {"KalTim": "Samarinda", "Bali": "Denpasar"}
print(capitals["KalTim"])
capitals["JaTim"] = "Surabaya"
print(capitals)
capitals["KalSel"] = "Banjarmasin"
print(len(capitals))
for k in capitals:
    print(capitals[k], "adalah ibukota dari ", k)
