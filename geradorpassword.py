#Gerador de Senhas em Python
#Password Generator 
#Instagram: @luanoliveira.ti
#Description: In this basic python script, we generate a new password using random chars and copying for clipboard. Very Lazy!
import random
import pyperclip

#Define Chars for the new password
minusculo = "abcdefghijklmnopqrstuvxyz" #LOWERCASE
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVXYZ" #UPPERCASE
numeros="1234567890" #numbers
especiais="!_-.;:[]()" # Special Chars

#Append All for random func.
tudo = minusculo+maiusculo+numeros+especiais 
tamanho = 12 # length of password
#Generating the password
senha="".join(random.sample(tudo,tamanho)) 
#OUTPUT
print("=========================================")
print("\nTa aqui a senha seu preguiçoso: "+senha)
pyperclip.copy(senha)
print("\nA senha gerada foi copiada para a área de Transferencia!")
print("=========================================")
