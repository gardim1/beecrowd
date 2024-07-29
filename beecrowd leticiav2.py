import math

def calcular_anos(PA, PB, G1, G2):
    # Se a taxa de crescimento de A (G1) é menor ou igual à de B (G2), A nunca ultrapassará B
    if G1 <= G2:
        return "Mais de 1 seculo."

    # Calcula o número de anos (t) necessário para que a população de A ultrapasse a de B
    # Usando a fórmula: t = ln(PB / PA) / (ln((1 + G1 / 100) / (1 + G2 / 100)))
    t = (math.log(PB / PA) / (math.log(1 + G1 / 100) - math.log(1 + G2 / 100)))

    # Se t for maior que 100, retorna "Mais de 1 seculo." pois o tempo é muito longo
    if t > 100:
        return "Mais de 1 seculo."
    else:
        # Retorna o valor de t arredondado para cima, pois o número de anos deve ser inteiro
        return math.ceil(t)

# Exemplo de uso com casos de teste
test_cases = [
    (100, 150, 0.8, 0),        # A tem crescimento, B não. A ultrapassa em 51 anos
    (90000, 120000, 5.5, 3.5),   # A cresce mais rápido que B, ultrapassa em 16 anos
    (56700, 72000, 5.2, 3.0),    # A cresce mais rápido que B, ultrapassa em 12 anos
    (123, 2000, 3.0, 2.0),        # A cresce mais rápido que B, e ultrapassa 100 anos
    (100000, 110000, 1.5, 0.5),  # A cresce mais rápido que B, ultrapassa em 10 anos
    (62422, 484317, 3.1, 1.0)    # A cresce mais rápido que B, mas não ultrapassa em 100 anos
]

# Itera sobre cada caso de teste, aplicando a função calcular_anos e imprimindo o resultado
for PA, PB, G1, G2 in test_cases:
    print(calcular_anos(PA, PB, G1, G2))
