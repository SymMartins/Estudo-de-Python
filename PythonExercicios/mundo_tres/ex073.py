"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocação.
depois mostre:
A = Apenas os 5 primeiro colocados.
B = Os últimos 4 colocados da tabela.
C = Uma lista com os times em ordem alfabética.
D = Em que posição na tabela está o time do Santos."""

times = ('Corintias', 'Bragantino', 'Atlético-MG', 'Coritiba', 'São Paulo',
         'Santos', 'Cuiabá', 'Internacinal', 'Avaí', 'América-MG',
         'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará-SC',
         'Athletico-PR', 'Atlético-GO', 'Goias', 'Juventude', 'Fortaleza')

print('-=' * 15)
print(f'A lista do Brasileirão 2022: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-=' * 15)
print(f'A ordem alfabética dos times é: {sorted(times)}')
print('-=' * 15)
print(f'A posição do Santos é a {times.index("Santos")+1}ª')

"""(tupla.index) mostra a posição na qual o time Santos está!
Lembre-se que tem que comolar o (+1) pois a tupla começa na posição (0)"""
