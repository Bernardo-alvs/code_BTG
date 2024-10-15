salario = float(input("quanto é seu salário?"))
percentual_aumento = float(input("Qual foi o percentual de aumento?"))
aumento_salario = salario * (percentual_aumento/100) #Descobrir aumento do salário 
novo_salario = salario + aumento_salario
print(f"seu aumento de salario é {aumento_salario:.2f}")
print(f"Seu novo salário é R${novo_salario:.2f}")