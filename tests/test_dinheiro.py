import pytest

from domain.dinheiro import Dinheiro

def test_deve_retornar_a_soma_de_dois_dinheiros_mesma_moeda():
    # Arranjo
    m_12_brl = Dinheiro(12, "BRL")
    m_14_brl = Dinheiro(14, "BRL")
    esperado = Dinheiro(26, "BRL")

    # Acão
    retornado = m_12_brl.adiciona(m_14_brl)

    # Asserção
    # esperado.__eq__(retornado)
    assert esperado == retornado
   
def test_deve_exececao_a_soma_de_dois_dinheiros_moeda_diferentes():
    # Arranjo
    m_12_brl = Dinheiro(12, "BRL")
    m_14_usd = Dinheiro(14, "USD")
    
    # Acão
    # Asserção
    with pytest.raises(RuntimeError):
        retornado = m_12_brl.adiciona(m_14_usd)