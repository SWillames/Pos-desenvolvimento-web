#coding: utf-8
nota1 = float(raw_input("Digite a 1 nota: "))

nota2 = float(raw_input("Digite a 2 nota: "))

nota3 = float(raw_input("Digite a 3 nota: "))

media = (nota1 + nota2 + nota3)/3.0

if media < 4.0:
    print "Sua media é %4.2f, Situação: REPROVADO!" %(media)
elif 4.0 <= media < 7.0:
    print "Sua media é %4.2f, Situação: PROVA FINAL" %(media)
    provafinal = float(raw_input("Digite a nota da prova final: "))
    mediaFinal = (provafinal + media)/2
    if mediaFinal < 6.0:
        print "Sua media final é %4.2f, Situação: REPROVADO" %(mediaFinal)
    else:
        print "Sua media final é %4.2f, Situação: APROVADO" %(mediaFinal)
else:
    print "Sua media é %4.2f, Situação: APROVADO!" %(media)
