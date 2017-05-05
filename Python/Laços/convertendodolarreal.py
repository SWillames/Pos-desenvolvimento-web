print "======CONVERSOR======="
print "para usar o conversor tem que digitar o valor inicial e o valor final!!"

valini = int(raw_input (' Digite o valor inicial: '))
valfin = int(raw_input (' Digite seu peso: '))
d = 3.249
for p in xrange(valini, valfin):
    print 'US$ %5.2f = RS$ %5.2f' %(p, p * d)
    print '-' * 20
