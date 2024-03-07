from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Ribeiro', idade=42)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ribeiro').first()
    pessoa.idade = 21
    pessoa.name = "Marcos"
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ribeiro').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #alterar_pessoa()
    exclui_pessoa()
    consulta_pessoas()

