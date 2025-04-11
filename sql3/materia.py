from db import conn

def listar_materias():
    with conn.cursor() as cursor:
        sql = '''
            SELECT id, nome, sigla, descricao
            FROM materias 
        '''
        cursor.execute(sql)
        dados = cursor.fetchall()
    
    return dados

def buscar_materia_pela_sigla(sigla: str):
    with conn.cursor() as cursor:
        sql = '''
            SELECT id, nome, sigla, descricao
            FROM materias 
            WHERE sigla = %s
        '''

        cursor.execute(sql, (sigla,))
        dado = cursor.fetchone()

    return dado


def cadastrar_materia(nome: str, sigla: str, descricao: str | None = None):
    with conn.cursor() as cursor:
        sql = '''
            INSERT INTO materias (nome, sigla, descricao)
            VALUES (%s, %s, %s)
        '''

        cursor.execute(sql, (nome, sigla, descricao))
    
    conn.commit() # Obrigatório para Persistir os Dados


def atualizar_materia(id: int, nome: str, sigla: str, descricao: str | None = None):
    with conn.cursor() as cursor:
        sql = '''
            UPDATE materias
            SET nome = %s, sigla = %s, descricao = %s
            WHERE id = %s
        '''

        cursor.execute(sql, (nome, sigla, descricao, id))
    
    conn.commit() # Obrigatório para Persistir os Dados

def menu():
    while True:
        print(' Gerenciar Matérias '.center(30, '='))
        print('[1] - Listar Matérias')
        print('[2] - Cadastrar Matéria')
        print('[3] - Editar Matéria')
        print('[4] - Voltar')
        print('=' * 30)

        resp = input('Selecione uma opção: ')

        if resp == '1':
            materias = listar_materias()

            for id, nome, sigla, _ in materias:
                print(f'{id} - {nome} ({sigla})')
        elif resp == '2':
            nome = input('Digite o nome da matéria: ')
            sigla = input('Digite a sigla da matéria: ')

            materia = buscar_materia_pela_sigla(sigla)

            if materia is not None:
                print('Já existe uma materia com essa sigla.')
                continue

            descricao = input('Descrição (Opcional): ')
            descricao = descricao if descricao.strip() != '' else None

            cadastrar_materia(nome, sigla, descricao)
            print('Materia Cadastrada com Sucesso!')
        
        elif resp == '3':
            # Listar as Matérias para Edição
            materias = listar_materias()

            for id, nome, sigla, _ in materias:
                print(f'[{id}] - {nome} ({sigla})')

            # Informar o ID da matéria que ele quer editar
            materia_id = int(input('Selecione a matéria: '))

            # Pedindo novos dados da matéria
            nome = input('Digite o novo nome da matéria: ')
            sigla = input('Digite a nova sigla da matéria: ')

            # Buscar uma matéria com a sigla informada
            # Pode ser uma Tupla ou "None"
            materia = buscar_materia_pela_sigla(sigla)

            # Se ele achar outra matéria que não é a que está sendo editada
            # Então ele mostra a mensagem de validação
            if materia is not None and materia[0] != materia_id:
                print('Já existe uma materia com essa sigla.')
                continue

            descricao = input('Descrição (Opcional): ')
            descricao = descricao if descricao.strip() != '' else None


            atualizar_materia(materia_id, nome, sigla, descricao)
            print('Matéria Atualizada com Sucesso.')      9
        elif resp == '4':
            break
        else:
            print('Opção Inválida!')

if __name__ == '__main__':
    menu()