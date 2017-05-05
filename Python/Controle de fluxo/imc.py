#coding: utf-8
print( '========Programa para calcular IMC - Massa corporal========')

peso = raw_input (' Digite seu peso: ')
altura = raw_input ('Digite a sua altura: ')
imc = float(peso)/(float(altura)*float(altura))

print 'Seu IMC é : ', imc
