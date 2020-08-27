# 3) Estas 3 listas:
# 
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

#Lista De Vendas
vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]

#média de vendas
media1 = sum(vendas_armando)/len(vendas_armando)
media2 = sum(vendas_eduardo)/len(vendas_eduardo)
media3 = sum(vendas_paulo)/len(vendas_paulo)

#total de vendas
total1 = sum(vendas_armando)
total2 = sum(vendas_eduardo)
total3 = sum(vendas_paulo)

#quantiade de vendas
quant1 = len(vendas_armando) 
quant2 = len(vendas_eduardo)
quant3 = len(vendas_paulo)

#comissao do armando
if total1 >= 0.00 and total1 <= 1000.00:
    comissao1 = total1*(1/100)

elif total1 >= 1000.01 and total1 <= 2500.00:
    comissao1 = total1*(1.5/100)

elif total1 >= 2500.01 and total1 <= 5000.00:
    comissao1 = total1*(2/100)

else:
    comissao1 = total1*(3/100)

#comissao do eduardo
if total2 >= 0.00 and total2 <= 1000.00:
    comissao2 = total2*(1/100)

elif total2 >= 1000.01 and total2 <= 2500.00:
    comissao2 = total2*(1.5/100)

elif total2 >= 2500.01 and total2 <= 5000.00:
    comissao2 = total2*(2/100)

else:
    comissao2 = total2*(3/100)

#comissao do Paulo
if total3 >= 0.00 and total3 <= 1000.00:
    comissao3 = total3*(1/100)

elif total3 >= 1000.01 and total3 <= 2500.00:
    comissao3 = total3*(1.5/100)

elif total3 >= 2500.01 and total3 <= 5000.00:
    comissao3 = total3*(2/100)

else:
    comissao3 = total3*(3/100)

print(f"""Dados dos Vendedores:

Média de Venda dos Vendedores:
Armando: {media1}
Eduardo: {media2}
Paulo: {media3}

Total de Venda dos Vendedores: 
Armando: {total1}
Eduardo: {total2}
Paulo: {total3} 

Quantidade De Vendas dos Vendedores:
Armando: {quant1}
Eduardo: {quant2}
Paulo: {quant3}

Comissão de Cada Vendedor
Armando: {comissao1} 
Eduardo: {comissao2}
Paulo: {comissao3}""")