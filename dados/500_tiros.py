from dados import echar_dados

datos = []

# populating list
for n in range(0,500):
   datos.append(echar_dados())

# data analytics

for tiro in datos: 
    print(sum(tiro))



