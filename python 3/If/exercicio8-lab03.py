print("Informe o preço de três produtos e para saber qual produto você deve comprar, a escolha é sempre pelo mais barato!\n")

p1 = float(input('Preço do primeiro produto: R$'))
p2 = float(input('Preço do segundo produto: R$'))
p3 = float(input('Preço do terceiro produto: R$'))

if p1 < p2 and p1 < p3:
    print("Deve-se comprar o produto 1, pois eh o mais barato")
elif p2 < p1 and p2 < p3:
    print("Deve-se comprar o produto 2, pois eh o mais barato")
elif p3 < p1 and p3 < p2:
    print("Deve-se comprar o produto 3, pois eh o mais barato")
elif p1 == p2 and p1 and p2 < p3:
    print("Deve-se comprar os produtos 1 e 2 pois são mais baratos!")
elif p1 == p3 and p1 and p3 < p2:
    print("Deve-se comprar os produtos 1 e 3 pois são mais baratos!")
elif p2 == p3 and p2 and p3 < p1: 
    print("Deve-se comprar os produtos 2 e 3 pois são mais baratos!")
else:
    print("Todos produtos possuem o mesmo valor, portanto não tem um mais barato!")
    
    
    
    


