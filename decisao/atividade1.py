#  01 )

n = int(input("Digite um numero "))
n2 = int(input("Digite outro numero "))

if n>n2 :
   print (" o ", n ,"e o maoir numero")
elif n<n2:
     print (" o ", n2 ,"e o maoir numero")
else:
    print ("Os numeros sao iguais")
print ("FIM PROGRAMA ")



#  02 )


n = int(input("Digite um numero: "))


if n % 2 == 0:
    print("O número", n, "é par")
else:
    print("O número", n, "é ímpar")

print("FIM DO PROGRAMA")


 
#  03 )

estadoCivil = (input("Digite Alguma LETRA > C : S : D : V : O , representando seu estado civil \n :"))

if estadoCivil == 'C':
    print("Voce e casado")
elif estadoCivil == 'S':
    print("Voce e solteiro")
elif estadoCivil == 'D':
    print("Voce e divorciado")
elif estadoCivil == 'V':
    print("Voce e viuvo")
else:
    ("estado Civil Invalido")

print("FIM DO PROGRAMA")



#  04 )

n = int(input("Digite sua idade  "))

if n < 18 :
   print ("Entrada negada")

print ("FIM PROGRAMA ")


#  05 )

n = int(input("Digite sua idade  "))

if n >= 18 :
    print ("Seja Bem Vindo")
else:
    print ("Entrada negada")
print ("FIM PROGRAMA ")


#  06 )

vogal = (input("Digite uma letra :\n"))

if vogal == 'A':
    print ("a letra e uma vogal")
elif vogal == "E" :
    print ("a letra e uma vogal")
elif vogal == "I" :
    print ("a letra e uma vogal")
elif vogal == "O" :
    print ("a letra e uma vogal")
elif vogal == "U" :
    print ("a letra e uma vogal")
else:
    print ("a letra e uma consoante")
print ("FIM PROGRAMA ")


 

#  07 )

n = (input("Digite a sua altura"))
n2 = (input("Digite a sua altura"))

if n>n2 :
   print (" A pessoa 1  ea maior ")
elif n<n2:
     print (" A pessoa 2  ea maior ")
else:
    print ("Os dois tem a mesma altura")
print ("FIM PROGRAMA ")






#  08 )


n = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = input("Qual operação gostaria de fazer? DIVISAO, SOMA, SUBTRACAO, MULTIPLICACAO: ")


if soma == 'DIVISAO':
    if n2 != 0:
        resuldivi = n / n2  #
        print("O resultado é", resuldivi)
    else:
        print("Erro: Não é possível dividir por zero!")
        
elif soma == 'SOMA':
    resuldsoma = n + n2
    print("O resultado é", resuldsoma)
    
elif soma == 'MULTIPLICACAO':
    resuldmul = n * n2
    print("O resultado é", resuldmul)
    
elif soma == 'SUBTRACAO':
    resulsub = n - n2
    print("O resultado é", resulsub)
    
else:
    print("Opção inválida! Digite o nome da operação corretamente.")

print("FIM PROGRAMA")
