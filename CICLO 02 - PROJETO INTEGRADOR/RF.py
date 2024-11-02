# Teste para Requisito Funcional (RF)

from app import adicionar_colaborador, listar_colaboradores

def test_adicionar_colaborador():
    colaborador = {
        "nome": "João Silva",
        "cpf": "12345678900",
        "cargo": "Técnico"
    }
    adicionar_colaborador(colaborador)
    assert len(listar_colaboradores()) > 0
    assert listar_colaboradores()[0]["nome"] == "João Silva"

