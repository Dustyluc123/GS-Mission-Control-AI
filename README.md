#  Mission Control AI - FIAP a Marte

## Informações do Projeto
* **Nome da Missão:** HELIOS ENERGY EDITION FIAP a Marte
* **Trilha Temática:**  EnviroSat (Observação Ambiental e Sustentabilidade Terrestre)
* **Disciplina:** Prompt Engineering and Artificial Intelligence
* **Instituição:** FIAP - Ciências da Computação (2026.1)
* **Equipe:** Dustyuc

---

## Sobre o Projeto
O **Mission Control AI** é um sistema de suporte à decisão baseado em terminal (CLI interativa estilo *Claude Code*) projetado para gerenciar o ecossistema energético e operacional da sonda Helios. O sistema monitora variáveis críticas de telemetria orbital e utiliza inteligência artificial generativa de ponta para fornecer diagnósticos em tempo real, mitigando riscos de falhas no espaço profundo e garantindo o impacto positivo da missão na Terra.

---

## Arquitetura do Sistema e Injeção de Contexto
A aplicação foi construída utilizando uma arquitetura modular em Python puro, sem o uso de frameworks pesados, garantindo alta eficiência e tempo de resposta. 

O fluxo de dados opera em ciclo fechado:
1. O módulo `telemetria.py` extrai a matriz multidimensional de sensores orbitais.
2. O módulo `alertas.py` roda de forma determinística avaliando os thresholds lógicos em Python.
3. O módulo `engine.py` realiza a **Injeção Dinâmica de Dados**, unificando os logs lógicos do Python, as médias operacionais e a pergunta do operador dentro de um prompt rico contextualizado.
4. O pacote completo é enviado via API para o modelo **gpt-oss:120b** hospedado na **Ollama Cloud**.

---

## Engenharia de Prompts (System Prompt)
Localizado em `prompts/system_prompt.md`, o prompt de sistema foi projetado utilizando técnicas avançadas de contextualização de LLMs:
* **Definição de Persona:** Estabelece a IA como o computador de bordo "Helios Core AI", adotando um tom técnico, preciso e consultivo.
* **Mitigação de Alucinações:** Restrições explícitas foram implementadas para impedir que a IA invente dados fora da matriz de telemetria injetada dinamicamente.
* **Ancoragem Terrestre:** Vincula o sucesso energético dos painéis solares da sonda diretamente ao funcionamento dos payloads de monitoramento da Floresta Amazônica na Terra.

---

## Proposta de Valor e Modelo de Negócio (Frente 6)

### 1. Qual o problema real terrestre que esta missão resolve?
A Helios Solar Probe, operando sob a arquitetura EnviroSat, resolve a latência e a interrupção no fornecimento de dados de radiação e sensoriamento térmico para monitoramento de desmatamento ilegal e focos de incêndio florestal na Amazônia Legal brasileira. Ao garantir a estabilidade do sistema de energia fotovoltaico da sonda, salvaguardamos o fluxo ininterrupto de dados para os sistemas DETER/PRODES do INPE e ações em solo do IBAMA.

### 2. Quem paga pela solução?
O modelo de financiamento é híbrido. O desenvolvimento de base e infraestrutura conta com investimentos públicos de agências de fomento e ministérios do Meio Ambiente/Ciência e Tecnologia. A camada de insights analíticos refinados e predições climáticas de risco é comercializada para o setor privado (grandes empresas do agronegócio focadas em compliance ESG e fundos de investimentos internacionais focados em créditos de carbono).

### 3. Métrica de Impacto Coletivo
Garantir o funcionamento contínuo e inteligente da Helios viabiliza a cobertura analítica de **5 milhões de hectares monitorados**, permitindo respostas rápidas que estimam mitigar a queima descontrolada de biomas e evitar a emissão de **120.000 toneladas de CO₂** na atmosfera anualmente.

### 4. Modelo de Negócio
A monetização corporativa ocorre através do modelo **DaaS (Data-as-a-Service)**, onde empresas privadas assinam feeds recorrentes de dados preditivos processados pela nossa IA. Para órgãos governamentais de fiscalização ambiental e brigadas de incêndio, o acesso aos alertas de risco crítico é totalmente gratuito e prioritário, estruturado sob uma concessão de utilidade pública de longo prazo.

---

## 🛠️ Como Executar o Projeto

1. Certifique-se de ter o Python 3.10+ instalado.
2. Clone o repositório e instale as dependências obrigatórias:
   ```bash
   pip install -r requirements.txt
3. Crie um arquivo .env na raiz do projeto com o seu token oficial de acesso:
    ```bash 
    Plaintext
    OLLAMA_API_KEY=seu_token_aqui
4. Execute a aplicação principal:
    ```Bash
    python main.py