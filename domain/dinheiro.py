class Dinheiro:
    """O dinheiro do calculador

    A classe contém o valor e a moeda do dinheiro do calculador.
    """

    def __init__(self, valor, moeda):
        """Inicializa o dinheiro com o valor e moeda.

        Args:
            valor: O valor do dinheiro.
            moeda: A moeda do dinheiro.
        """
        self._valor = valor
        self._moeda = moeda

    def adiciona(self, dinheiro):
        """Adiciona dois dinheiros de uma mesma moeda.

        Args:
            dinheiro: Um dinheiro.
        """
        if self._moeda != dinheiro._moeda:
            raise RuntimeError("Dinheiros com moedas diferentes")
        return Dinheiro(self._valor + dinheiro._valor, self._moeda)

    def __eq__(self, outro):
        return (self._valor, self._moeda) == (outro._valor, outro._moeda)
