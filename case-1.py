def add(
    x: int, y: float
) -> float:  # Nao sao tipos fixos sao anotacoes aqui vira uma documentacao
    return x + y


# Se eu quero que seja obrigatorio mas sem usar bibliotecas
def add(x: int, y: float) -> float:
    if not isinstance(x, int) or not isinstance(y, (int, float)):
        raise TypeError("Tipos incorretos fornecidos!")
    return x + y


val = add(2.1, 5)
print(val)
