""" Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que consiga funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que sejamos monetários."""
from utilidadescev import dado
from utilidadescev import moeda

preco = dado.leiaDinheiro('Digite o preço R$: ')
moeda.resumo(preco, 35, 22)
