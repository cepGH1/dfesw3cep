
cepVar2 = open("teams.txt", "r")
cepVar3 = cepVar2.readlines()
print(cepVar3)
cepVar3.insert(0 , "this is a new line\n")
champs = cepVar3.pop(1)

print(cepVar3[0], cepVar3[3])
cepVar2.close
bigString = ""
for x in cepVar3:
    bigString = bigString + x
cepVar4 = open("teams.txt", "w")
cepVar4.write(bigString)

cepVar4.close()
cepVar5 = open("teams.txt", "r")
cepVar6 = cepVar5.readlines()
print(cepVar6)
for y in cepVar6:
    print(y)



