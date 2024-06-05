#Aula 8
#frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maçã"]
#for fruta in frutas:
#    print(fruta)

#Aula 9
#notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano":8.5}
#for chave, valor in notas.items():
#    print(chave)
#    print(valor)

#Aula 17
# chave minha api: 868c3a5905fa19ac77a45a777ffe20a0
# https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=868c3a5905fa19ac77a45a777ffe20a0

import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=868c3a5905fa19ac77a45a777ffe20a0"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])