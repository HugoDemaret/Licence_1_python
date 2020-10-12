rice_mass = float(758000000000)
n = float(2**63)
i = 1
while rice_mass < ((n)*0.0025):
    i +=1
    rice_mass += 758000000000
print(i)
