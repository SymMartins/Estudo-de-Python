medida = float(input("Digite uma medida "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a:'.format(medida))
print('{} km \n{} Hm \n{} Dam \n{} Dm \n{} Cm \n{} Mm'.format(km, hm, dam, dm, cm, mm))