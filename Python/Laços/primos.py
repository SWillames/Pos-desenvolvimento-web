#coding: utf-8
limite = 1000
numero = 2
c = 1
p = 0
print "Primos: ",
while numero < 1000:
    i = numero -1
    while i > 1:
        if numero % i == 0: break
        i -= 1
        c += 1
    else:
        print numero,
        p += 1
    numero += 1

print "\n\nForam encontrados %d números primos." %p
print "Foram necessárias %d comparações." %c
print "\n"

print "==========EXECUÇÃO MELHORADA============"
c1 = 1
p1 = 0
print "Primos: ",
for numero in xrange(2, limite+1):
    #Melhoria
    for i in xrange(2,(numero/2)+1):
        if numero % i == 0: break
        c1 += 1
    else:
        print numero,
        p1 += 1
print "\n\nForam encontrados %d números primos." %p1
print "Foram necessárias %d comparações, %d a menos quando feita com logica usada no while." % (c1, c-c1)
print "\n"
print "==========EXECUÇÃO AINDA MELHOR============"
print "Primos: 2",

c2, p2, primos, limite = 1, 1, [2,], 1000

for numero in xrange(3,limite+1,2): #pula de dois em dois
    ehprimo = 1
    for i in primos:
        c += 1 # mudei de lugar
        if numero % i == 0:
            ehprimo = 0
            break
        if i > sqrt(numero):
            break
    if (ehprimo):
        primos.append(numero)
        print numero,
        p += 1

print "\n\nForam encontrados %d números primos." %p2
print "Foram necessárias %d comparações, %d a menos quando feita com logica usada no while." % (c2, c1-c2)
