try:
    with open(nosaukums, 'r') as datne:
        saturs = datne.read()

#@# 1.
print(f"Simbolu skaits datne: {len(saturs)}")

#$# 2.
print(f"Pirmie 10 simboli: {saturs[:10]}")

#%# 3.
print(f"Pirmais simbols: {saturs[0]}, Pedejais simbols: {saturs[-1]}")
