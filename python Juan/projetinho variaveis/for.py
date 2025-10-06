# Atividade 1
usuarios = ["admin", "ana", "joana", "marcos"]
for usuario, id_usuario in zip(usuarios, range(1001, 1005)):
    print(f"Usuário: {usuario}, ID: {id_usuario}")

numero = 123456
print(str(len(str(numero))))

# Atividade 2
senha = input("Digite sua senha: ")
  
if len(senha) == 8:
         print("Senha válida.")
else:
         print("Senha inválida.")