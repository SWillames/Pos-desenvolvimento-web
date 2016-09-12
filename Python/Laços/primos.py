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
    for i in xrange(2,numero):
        if numero % i == 0: break
        c1 += 1
    else:
        print numero,
        p1 += 1
print "\n\nForam encontrados %d números primos." %p1
print "Foram necessárias %d comparações, %d a menos quando feita com logica usada no while." % (c1, c-c1)
