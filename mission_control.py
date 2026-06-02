# ====================================================================
# MISSION CONTROL AI - HELIOS SOLAR PROBE (FIAP A MARTE)
# SISTEMA INTELIGENTE DE GESTÃO ENERGÉTICA E SUSTENTABILIDADE OPERACIONAL
# ====================================================================

# Configurações Globais da Missão
NOME_MISSAO = " FIAP a Marte"
EQUIPE = "DUSTYLUC"

# Customização Semântica para Soluções em Energia e Sustentabilidade
AREAS_MONITORADAS = [
    "Temperatura do Módulo Térmico",
    "Comunicação com a Base Terrestre",
    "Sistema de Armazenamento de Energia (Bateria)",
    "Suporte de Oxigênio e Pressão Atmosférica",
    "Estabilidade e Eficiência Dinâmica"
]

NOMES_CURTOS = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]


# 1. FUNÇÃO: Obter Dados da Missão (Exigência Acadêmica)
def obter_dados_missao():
    """Retorna a matriz com os dados brutos de telemetria energética e operacional."""
    return [
        [24, 92, 88, 96, 90],
        [27, 80, 72, 94, 85],
        [31, 65, 58, 91, 70],
        [36, 42, 38, 87, 55],
        [39, 28, 19, 78, 35],
        [34, 55, 32, 82, 50]
    ]


# 2. FUNÇÃO: Classificar Parâmetro Individual sob a Ótica de Eficiência
def classificar_parametro(indice, valor):
    """
    Analisa os limites lógicos aplicando conceitos de mitigação de estresse térmico, 
    balanço de potência ativa e eficiência de transmissão.
    Retorna: (Status, Pontuação de Risco, Mensagem de Status, Recomendação)
    """
    # 0: Temperatura (Estresse térmico e dissipação)
    if indice == 0:
        if valor < 18: 
            return "ATENÇÃO", 1, "Temperatura baixa (Subconsumo térmico)", "Otimizar reuso de calor dissipado pelos computadores de bordo"
        elif valor <= 30: 
            return "NORMAL", 0, "Temperatura térmica estável", ""
        elif valor <= 35: 
            return "ATENÇÃO", 1, "Temperatura elevada", "Redirecionar fluxo de refrigeração passiva orbital"
        else: 
            return "CRÍTICO", 2, "Superaquecimento de módulos", "Acionar resfriamento criogênico de emergência e mitigar perda térmica"
        
    # 1: Comunicação (Potência de transmissão)
    elif indice == 1:
        if valor < 30: 
            return "CRÍTICO", 2, "Sinal crítico (Alto desperdício de potência de transmissão)", "Pausar telemetria pesada e concentrar potência na antena Banda X"
        elif valor <= 59: 
            return "ATENÇÃO", 1, "Comunicação instável com atenuação orbital", "Realinhar antenas fototônicas para reduzir perdas de propagação"
        else: 
            return "NORMAL", 0, "Comunicação estável e eficiente", ""
        
    # 2: Bateria (Estado de Carga - SoC e Fontes Renováveis)
    elif indice == 2:
        if valor < 20: 
            return "CRÍTICO", 2, "Apagão iminente no banco de baterias de Íons de Lítio", "Cortar cargas não essenciais e acionar células de combustível de hidrogênio reserva"
        elif valor <= 49: 
            return "ATENÇÃO", 1, "Geração solar fotovoltaica abaixo da demanda de consumo", "Otimizar ângulo de inclinação dos painéis solares em relação ao vetor do Sol"
        else: 
            return "NORMAL", 0, "Balanço energético autossustentável (Geração > Consumo)", ""
        
    # 3: Oxigênio (Suporte à vida e consumo do módulo)
    elif indice == 3:
        if valor < 80: 
            return "CRÍTICO", 2, "Oxigênio em nível crítico (Falha no sistema de eletrólise)", "Acionar tanques de oxigênio químico de emergência"
        elif valor <= 89: 
            return "ATENÇÃO", 1, "Oxigênio abaixo do ideal", "Inspecionar filtros e otimizar recicladores biológicos para reduzir consumo passivo"
        else: 
            return "NORMAL", 0, "Nível de oxigênio sustentável", ""
        
    # 4: Estabilidade (Consumo cinético e propulsão)
    elif indice == 4:
        if valor < 40: 
            return "CRÍTICO", 2, "Instabilidade operacional crítica (Desperdício de energia cinética)", "Ativar giroscópios magnéticos de alta eficiência para travamento de atitude"
        elif valor <= 69: 
            return "ATENÇÃO", 1, "Eficiência dinâmica reduzida", "Ajustar propulsores iônicos de baixa potência para correção orbital limpa"
        else: 
            return "NORMAL", 0, "Alinhamento dinâmico e consumo estável", ""


# 3. FUNÇÃO: Formatação Visual de Medidas
def formatar_medida(indice, valor):
    """Adiciona a unidade de medida correta dependendo do dado analisado."""
    if indice == 0:
        return f"{valor} °C"
    return f"{valor}%"


# 4. FUNÇÃO: Analisar Tendência Geral da Saúde da Nave
def analisar_tendencia(pontuacoes):
    """Avalia matematicamente se a estabilidade global está convergindo ou degradando."""
    if not pontuacoes or len(pontuacoes) < 2:
        return "Dados insuficientes para calcular tendência."
        
    risco_inicial = pontuacoes[0]
    risco_final = pontuacoes[-1]
    
    if risco_final > risco_inicial:
        return "A missão apresentou tendência de PIORA energética e operacional em relação ao início."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de MELHORA e estabilização de sustentabilidade."
    else:
        return "A missão manteve o perfil de consumo e risco ESTÁVEL em relação ao início."


# 5. FUNÇÃO INOVADORA (Exclusiva para Energia): Fluxo de Potência Ativa e ISE
def calcular_metricas_sustentabilidade(dados):
    """
    Aplica conceitos físicos básicos simulando a Potência Gerada (solar) e o 
    consumo das cargas para gerar o Índice de Sustentabilidade Energética (ISE).
    """
    total_ciclos = len(dados)
    ciclos_sustentaveis = 0
    
    print("-" * 60)
    print("ANÁLISE VETORIAL: BALANÇO DE POTÊNCIA ATIVA EM ÓRBITA")
    print("-" * 60)
    
    for idx, ciclo in enumerate(dados):
        bateria = ciclo[2]
        # Simulação física: a geração solar varia com a eficiência de captação (representada pela bateria)
        potencia_gerada_solar = (bateria * 1.2)  # em kW (modelo conceitual sustentável)
        potencia_consumida_sistemas = 65.0       # carga base em kW necessária para manter a nave ativa
        balanco_potencia = potencia_gerada_solar - potencia_consumida_sistemas
        
        status_balanco = "SUPERÁVIT (Sustentável)" if balanco_potencia >= 0 else "DÉFICIT (Esgotamento)"
        if balanco_potencia >= 0:
            ciclos_sustentaveis += 1
            
        print(f"Ciclo {idx+1} -> Potência Solar: {potencia_gerada_solar:.1f} kW | Consumo Carga: {potencia_consumida_sistemas:.1f} kW | Balanço: {balanco_potencia:+.1f} kW [{status_balanco}]")
        
    ise = (ciclos_sustentaveis / total_ciclos) * 100
    return ise


# 6. FUNÇÃO PRINCIPAL: Motor da Aplicação e Emissão do Relatório
def main():
    dados = obter_dados_missao()
    total_ciclos = len(dados)
    
    pontuacoes_por_ciclo = []
    classificacoes_por_ciclo = []
    acumulado_por_area = [0, 0, 0, 0, 0]
    
    # Interface do Terminal
    print("=" * 60)
    print("MISSION CONTROL AI - SUSTAINABLE ENERGY EDITION")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {EQUIPE}")
    print(f"Ciclos Operacionais Analisados: {total_ciclos}")
    print("=" * 60)
    
    # Processamento Lógico Iterativo dos Ciclos
    for c_idx, ciclo in enumerate(dados):
        print(f"CICLO {c_idx + 1}")
        print("-" * 60)
        
        pontuacao_ciclo = 0
        recomendacoes_ciclo = []
        teve_critico = False
        
        for i in range(len(ciclo)):
            valor = ciclo[i]
            status, pontos, msg, rec = classificar_parametro(i, valor)
            
            pontuacao_ciclo += pontos
            acumulado_por_area[i] += pontos
            
            if status == "CRÍTICO": teve_critico = True
            if rec != "": recomendacoes_ciclo.append(rec)
                
            nome_campo = NOMES_CURTOS[i]
            medida_formatada = formatar_medida(i, valor)
            print(f"{nome_campo}: {medida_formatada} | {status} | {msg}")
            
        # Classificação de Severidade Baseada em Regras Lógicas
        if pontuacao_ciclo >= 6 or teve_critico:
            classificacao = "MISSÃO CRÍTICA"
        elif pontuacao_ciclo >= 3 or (pontuacao_ciclo >= 1 and not teve_critico):
            if pontuacao_ciclo <= 2:
                classificacao = "MISSÃO ESTÁVEL"
            else:
                classificacao = "MISSÃO EM ATENÇÃO"
        else:
            classificacao = "MISSÃO ESTÁVEL"
            
        # Comparação Temporal em Relação ao Estado de Risco Anterior
        if c_idx == 0:
            comparacao_ciclo = "Referência de Inicialização Energética"
        else:
            pontuacao_anterior = pontuacoes_por_ciclo[-1]
            if pontuacao_ciclo > pontuacao_anterior:
                comparacao_ciclo = "PIOR (Risco de estresse nos subsistemas aumentou)"
            elif pontuacao_ciclo < pontuacao_anterior:
                comparacao_ciclo = "MELHOR (Eficiência de consumo reestabelecida)"
            else:
                comparacao_ciclo = "IGUAL (Balanço de risco constante)"

        pontuacoes_por_ciclo.append(pontuacao_ciclo)
        classificacoes_por_ciclo.append(classificacao)
        
        if not recomendacoes_ciclo:
            texto_recomendacao = "Manter matriz de consumo otimizada e continuar captação solar limpa."
        else:
            texto_recomendacao = " + ".join(recomendacoes_ciclo)
            
        print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}/10")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Comparação com ciclo anterior: {comparacao_ciclo}")
        print(f"Diretriz de Mitigação: {texto_recomendacao}")
        print() 
        
    # Execução das Métricas Científicas de Energia
    ise_final = calcular_metricas_sustentabilidade(dados)
    print()
    
    # Cálculos Estatísticos para o Relatório Consolidado
    medias = []
    for i in range(5):
        soma_coluna = sum(ciclo[i] for ciclo in dados)
        medias.append(soma_coluna / total_ciclos)
        
    ciclo_mais_critico = pontuacoes_por_ciclo.index(max(pontuacoes_por_ciclo)) + 1
    maior_pontuacao = max(pontuacoes_por_ciclo)
    risco_medio = sum(pontuacoes_por_ciclo) / total_ciclos
    qtd_criticos = classificacoes_por_ciclo.count("MISSÃO CRÍTICA")
    
    tendencia_global = analisar_tendencia(pontuacoes_por_ciclo)
        
    max_acumulado = max(acumulado_por_area)
    indice_area_afetada = acumulado_por_area.index(max_acumulado)
    nome_area_afetada = AREAS_MONITORADAS[indice_area_afetada]
    
    # Conclusão Técnica e Ecológica Condicional
    if classificacoes_por_ciclo[-1] == "MISSÃO ESTÁVEL":
        conclusao = "A missão ocorreu dentro dos parâmetros sustentáveis esperados, com balanço de potência e armazenamento sob total controle automatizado."
    else:
        conclusao = "A missão apresentou severo estresse energético e instabilidade operacional durante os ciclos orbitais. Apesar da recuperação parcial observada nas leituras fotovoltaicas finais, subsistem subsistemas em atenção latente, exigindo a manutenção ativa das diretrizes de eficiência energética e restrição de consumo secundário."

    # Impressão do Relatório Final Unificado
    print("=" * 60)
    print("RELATÓRIO FINAL INTEGRADO: AUTOMAÇÃO & SUSTENTABILIDADE ENERGÉTICA")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {EQUIPE}")
    print(f"Ciclos Computados: {total_ciclos}")
    print(f"Média de Temperatura Térmica: {medias[0]:.2f} °C")
    print(f"Média de Eficiência de Sinal: {medias[1]:.2f}%")
    print(f"Média do Estado de Carga da Bateria (SoC): {medias[2]:.2f}%")
    print(f"Média de Suporte de Oxigênio: {medias[3]:.2f}%")
    print(f"Média de Estabilidade Sistêmica: {medias[4]:.2f}%")
    print(f"Índice de Sustentabilidade Energética (ISE): {ise_final:.1f}%")
    print("-" * 60)
    print(f"Vetor Crítico Identificado: Ciclo {ciclo_mais_critico} (Pico de estresse: {maior_pontuacao} pontos)")
    print(f"Índice de Risco Médio Operacional: {risco_medio:.2f}")
    print(f"Frequência de Ciclos com Classificação Crítica: {qtd_criticos}")
    print(f"Tendência de Longo Prazo da Trajetória: {tendencia_global}")
    print("-" * 60)
    print("Pontuação Acumulada de Sobrecarga por Vetor Monitorado:")
    for i in range(5):
        print(f" - {AREAS_MONITORADAS[i]}: {acumulado_por_area[i]} pontos")
    print()
    print(f"Módulo com Maior Desgaste de Infraestrutura: {nome_area_afetada}")
    print(f"Classificação Final da Operação: {classificacoes_por_ciclo[-1]}")
    print(f"Conclusão e Parecer de Engenharia:\n{conclusao}")
    print("=" * 60)


if __name__ == "__main__":
    main()