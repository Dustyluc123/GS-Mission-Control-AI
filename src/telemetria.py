import random

def coletar():
    """
    Gera dinamicamente um novo ciclo de leitura de telemetria com flutuações físicas.
    Retorna: [Temperatura (°C), Comunicação (%), Bateria (%), Oxigênio (%), Estabilidade (%)]
    """
    # Flutuações normais baseadas em ranges aceitáveis
    temp = round(random.uniform(23.0, 34.0), 1)
    comunicacao = random.randint(60, 98)
    bateria = random.randint(50, 95)  # Definido como bateria
    oxigenio = random.randint(85, 100)
    estabilidade = random.randint(70, 98)
    
    # 15% de chance de injetar uma anomalia severa de sensor para testar a reatividade da IA
    if random.random() < 0.15:
        anomalias = [
            [42.3, random.randint(60, 80), random.randint(40, 55), 95, 90],  # Superaquecimento
            [round(random.uniform(22, 28), 1), random.randint(70, 90), 14, 92, 85],   # Apagão de Bateria
            [31.2, 18, random.randint(60, 80), 94, 32]                       # Falha de Sinal/Atitude
        ]
        return random.choice(anomalias)
        
    return [temp, comunicacao, bateria, oxigenio, estabilidade]  # Corrigido para bateria!