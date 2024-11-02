# Teste para Requisito Não Funcional (RNF)

from app import listar_colaboradores

def test_desempenho_listagem(benchmark):
    result = benchmark(listar_colaboradores)
    assert result is not None  # Garante que o resultado foi retornado
