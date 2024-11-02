# Teste para Requisito de Negócio (RN)

from app import autenticar_usuario

def test_autenticacao_usuario():
    assert autenticar_usuario("admin", "senha123") == True
    assert autenticar_usuario("admin", "senha_incorreta") == False
    assert autenticar_usuario("user", "senha456") == True
    assert autenticar_usuario("user", "senha_errada") == False
