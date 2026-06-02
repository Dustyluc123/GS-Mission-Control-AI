# 🛰️ Mission Control AI - Helios Solar Probe

<div align="center">

**Um sistema de inteligência artificial embarcado para monitoramento de radiação solar e anomalias térmicas orbitais**

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic%20Use-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)](README.md)

</div>

---

##  Informações do Projeto

| Campo | Descrição |
|-------|-----------|
| **Missão** | Helios Solar Probe |
| **Trilha Temática** | EnviroSat (Observação Ambiental e Sustentabilidade Terrestre) |
| **Disciplina** | Prompt Engineering and Artificial Intelligence |
| **Instituição** | FIAP - Faculdade de Informática e Administração Paulista |
| **Curso** | Ciências da Computação (1º Semestre - 2026) |

---

##  Descrição Geral da Solução

O **Mission Control AI** é um sistema computacional embarcado de suporte à decisão operado através de uma interface interativa de linha de comando. 

### Diferencial Técnico

Diferenciando-se de soluções de IA puramente decorativas, esta aplicação utiliza o modelo **gpt-oss:120b** hospedado na Ollama Cloud, integrado diretamente ao fluxo de execução operacional.

### Escopo Operacional

A Helios Solar Probe tem como missão primária:
- ✓ Capturar dados de radiação solar profunda
- ✓ Detectar anomalias térmicas orbitais
- ✓ Monitorar 5 milhões de hectares da floresta Amazônica brasileira
- ✓ Otimizar detecção de desmatamento ilegal e queimadas com latência reduzida

---

##  Arquitetura do Sistema

### Fluxo de Dados (Ciclo Fechado)

```
┌─────────────────┐
│   Telemetria    │  Gera leituras com variabilidade física coerente
└────────┬────────┘
         ↓
┌─────────────────┐
│    Alertas      │  Valida leituras contra limites críticos
└────────┬────────┘
         ↓
┌─────────────────┐
│  Motor IA (LLM) │  Consolida dados com memória temporal + system prompt
└────────┬────���───┘
         ↓
┌─────────────────┐
│   Interface CLI │  Apresentação visual e comandos do operador
└─────────────────┘
```

### Estrutura de Diretórios

```
gs-mission-control-ai/
│
├── main.py                    # Ponto de entrada unificado
├── requirements.txt           # Dependências com versões fixadas
├── .env.example              # Modelo de configuração ambiental
├── cenarios.json             # Vetores de teste estáticos
├── README.md                 # Esta documentação
│
├── prompts/
│   └── system_prompt.md      # Diretrizes de engenharia de prompt do LLM
│
├── src/
│   ├── __init__.py           # Inicialização de pacote
│   ├── telemetria.py         # Simulação dinâmica de sensores
│   ├── alertas.py            # Motor de regras determinísticas
│   ├── engine.py             # Cliente de IA + gerenciador de memória
│   └── ui.py                 # Interface CLI interativa
│
└── assets/
    ├── screenshot_banner.png
    └── screenshot_analise.png
```

---

##  Detalhamento dos Componentes

### Raiz do Projeto

| Arquivo | Função |
|---------|--------|
| **main.py** | Inicializa a aplicação e transfere execução para o laço interativo |
| **requirements.txt** | Especificação de dependências externas com versões fixadas |
| **.env.example** | Modelo de variáveis de ambiente (sem expor tokens) |
| **cenarios.json** | Dados JSON com cenários de voo pré-configurados |

### Pasta `prompts/`

- **system_prompt.md**: Diretrizes de engenharia de prompt para o LLM
  - Define escopo de atuação, tom e restrições antialucinação

### Pasta `src/`

| Módulo | Responsabilidade |
|--------|-----------------|
| **telemetria.py** | Simula dados de 5 eixos: Temperatura, Radiação, Pressão, Velocidade, Carga |
| **alertas.py** | Motor de regras que avalia telemetria contra thresholds críticos |
| **engine.py** | Gerencia conexão HTTP com Ollama Cloud + janela de memória temporal |
| **ui.py** | Interface CLI com `rich` e `prompt-toolkit` para comandos interativos |

---

## Design de Engenharia de Prompts e IA

### Técnicas Aplicadas no System Prompt

#### 1. Atribuição de Persona
Define a IA sob a identidade do computador de bordo **Helios Core AI**, estabelecendo tom técnico, consultivo e focado em engenharia de sistemas.

#### 2. Alinhamento e Ancoragem Física
O modelo correlaciona níveis de energia fotovoltaica com capacidade operacional dos payloads ópticos, garantindo coerência física nas respostas.

#### 3. Restrição de Confiabilidade
Implementa diretrizes rígidas contra alucinação: o modelo não deve inferir parâmetros operacionais ou criar telemetrias fictícias.

### Sistema de Múltiplas Personas Dinâmicas

Selecione personas em tempo real com `/persona <tipo>`:

```
/persona OPERADOR      → Foco em hardware, logs brutos, eficiência energética
/persona ASTRONAUTA    → Sistemas de suporte à vida, oxigênio, pressão
/persona CIENTISTA     → Impacto ecológico terrestre, análise ambiental
```

#### OPERADOR
- Engenharia de hardware
- Logs brutos de sistemas
- Eficiência da microrrede
- Procedimentos de mitigação técnica

#### ASTRONAUTA
- Sistemas de suporte à vida
- Gerenciamento de oxigênio
- Pressão e regulação térmica
- Segurança biológica da cápsula

#### CIENTISTA
- Análise de impacto ecológico terrestre
- Tradução de falhas espaciais em consequências ambientais
- Fiscalização da floresta Amazônica

---

## Proposta de Valor e Modelo de Negócio

### 1. Resolução do Problema Terrestre

O atraso em processar dados de satélites ambientais gera lacunas críticas na detecção de:
- Desmatamento ilegal
- Início de queimadas
- Anomalias térmicas

**Solução**: Processamento inteligente em tempo real com IA embarcada.

### 2. Clientes e Financiamento

#### Setor Público
- Contratos de prestação de serviços de segurança ambiental nacional
- Agência Espacial Brasileira
- Fundos de preservação climática

#### Setor Privado
- Relatórios analíticos de estresse térmico
- Dados meteorológicos para seguradoras agrícolas
- Empresas do agronegócio de grande escala

### 3. Métrica de Impacto Coletivo

Manutenção contínua de **5 milhões de hectares** de floresta amazônica através do gerenciamento inteligente da microrrede energética da sonda.

### 4. Modelo de Monetização

**DaaS (Data-as-a-Service)**
- Assinaturas corporativas mensais
- APIs para acesso a feeds de dados de sensores
- Relatórios automatizados e alertas prioritários

---

## Instalação e Execução

### Pré-requisitos

- Python 3.10 ou superior
- Conexão ativa com internet (API Ollama Cloud)
- Git

### Passo 1: Clonar e Navegar

```bash
git clone https://github.com/Dustyluc123/gs-mission-control-ai.git
cd gs-mission-control-ai
```

### Passo 2: Criar Ambiente Virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```plaintext
OLLAMA_API_KEY=seu_token_oficial_aqui
```

### Passo 5: Executar a Aplicação

```bash
python3 main.py
```

---

## Cenários Pré-Configurados

O arquivo `cenarios.json` contém três cenários de voo:

1. **Operação Nominal**: Condições normais de funcionamento
2. **Tempestade Solar**: Picos de radiação e variações de energia
3. **Eclipse Orbital**: Ausência de luz solar e modo de economia

---

## Melhorias Futuras

- [ ] **Sockets de Telemetria Real**: WebSockets para dados de satélites reais
- [ ] **Banco de Dados NoSQL**: Persistência histórica de ciclos operacionais
- [ ] **Observabilidade**: Integração com Prometheus e Grafana
- [ ] **API REST**: Exposição de endpoints para sistemas externos
- [ ] **Machine Learning**: Treinamento de modelos preditivos com dados históricos

---

## Autor

| Campo | Informação |
|-------|-----------|
| **Nome** | Lucas Barreto Santana |
| **RM** | 573149 |
| **Instituição** | FIAP |
| **Curso** | Ciências da Computação |



<div align="center">

**Desenvolvido com para a FIAP - 2026**

</div>
