def avaliar(dados):
    """Avalia os limites lógicos e retorna uma lista de strings com os alertas detetados."""
    alertas = []
    ultimo_ciclo = dados[-1]
    
    # 0: Temperatura
    if ultimo_ciclo[0] > 35: alertas.append("CRÍTICO: Superaquecimento de módulos!")
    elif ultimo_ciclo[0] > 30: alertas.append("ATENÇÃO: Temperatura elevada!")
        
    # 1: Comunicação
    if ultimo_ciclo[1] < 30: alertas.append("CRÍTICO: Sinal crítico com alto desperdício de potência!")
    elif ultimo_ciclo[1] <= 59: alertas.append("ATENÇÃO: Comunicação instável!")
        
    # 2: Bateria
    if ultimo_ciclo[2] < 20: alertas.append("CRÍTICO: Apagão iminente no banco de baterias!")
    elif ultimo_ciclo[2] <= 49: alertas.append("ATENÇÃO: Geração solar fotovoltaica abaixo da demanda!")
        
    # 3: Oxigénio
    if ultimo_ciclo[3] < 80: alertas.append("CRÍTICO: Falha no sistema de eletrólise de Oxigénio!")
        
    # 4: Estabilidade
    if ultimo_ciclo[4] < 40: alertas.append("CRÍTICO: Instabilidade operacional cinética!")
        
    return alertas if alertas else ["Todos os subsistemas operando em regime estável e autossustentável."]