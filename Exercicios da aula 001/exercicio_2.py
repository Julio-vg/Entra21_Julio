menu = "Cadastro De Funcionários do Entra-21 \n\n {0}\n{1}\n{2}\n{3}\n{4}\n\n\nFim do Menu.\n"

print(menu.format("\n" "1) Cadastrar funcionário", "2) Listar funcionários", "3) Editar funcionário", "4) Deletar funcionário", "5) Sair"))

opcao = int(input("Selecione uma função:"))

if opcao == 1:
    print("Informe os dados do novo funcionário.")

elif opcao == 2:
    print("Lista de funcionários.")

elif opcao == 3:
    print("Informe os novos dados do funcionário.")

elif opcao == 4:
    print("Informe a ID do funcionario que você deseja deletar do sistema.")

elif opcao == 5:
    print("Obrigado por usar o programa.")

else:
    print("Opção Inválida!")
