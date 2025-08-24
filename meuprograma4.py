print( " seja bem vindo paulo silvio " )
valor_do_pedido = float (input (' digite o valor do pedido: '))
quantidade_parcelas = int (input ( ' digite a quantidade de parcelas: ')) 


if (quantidade_parcelas < 4):
     juros = (0/100)
elif (quantidade_parcelas >= 4 and quantidade_parcelas < 6):    
     juros = (4/100)
elif (quantidade_parcelas >= 6 and quantidade_parcelas < 9 ):
     juros = (8/100)
elif (quantidade_parcelas >= 9 and quantidade_parcelas < 13) :   
     juros = (16/100)

else:    
    juros = (32/100)  
valor_da_parcela= (valor_do_pedido * (1+juros)) / quantidade_parcelas

valor_total_parcelado= valor_da_parcela * quantidade_parcelas



print(f"Valor da parcela: R$   {  valor_da_parcela: }")
print(f"Valor total parcelado: R$ {  valor_total_parcelado: }")