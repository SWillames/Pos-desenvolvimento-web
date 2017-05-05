#coding: utf-8
aurelio = {'denominacao':'ilha solteira', 'populacao':23000, 'renda': 1500}
print aurelio
#ADICIONANDO NOVA CHAVE NO DICIONARIO
aurelio['vocacao'] = 'turismo'
print "Essa é o dicionario com uma nova caracteristica"
print aurelio
#REMOVENDO CHAVE DO DICIONARIO
del aurelio['denominacao']
print aurelio
