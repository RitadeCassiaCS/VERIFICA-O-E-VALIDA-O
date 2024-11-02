# Função para adicionar um colaborador ao sistema

colaboradores = []

def adicionar_colaborador(colaborador):
    colaboradores.append(colaborador)

def listar_colaboradores():
    return colaboradores


# Função de autenticação de usuário

usuarios = {
    "admin": "senha123",
    "user": "senha456"
}

def autenticar_usuario(username, password):
    return usuarios.get(username) == password

