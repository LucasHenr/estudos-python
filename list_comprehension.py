#Dobrar o valor 

lista_precos = [500, 1000, 2000, 4000]

#Caso 1 - Utilizando o FOR

lista_de_precos_valor_dobrado = []
for preco in lista_precos:
         lista_de_precos_valor_dobrado.append(preco  * 2)

print(lista_de_precos_valor_dobrado)

#Caso 2  - Utilizando List Comprehension

lista_valor_dobrado_list_comprehension = [preco * 2 for preco in lista_precos]
print(lista_de_precos_valor_dobrado)


#OBS: List Comprehension , reduz a lista em uma linha código