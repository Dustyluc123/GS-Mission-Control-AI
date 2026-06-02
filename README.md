# GS-PCAP: Mission Control AI - FIAP a Marte

## Sobre o Projeto

Este projeto foi desenvolvido de forma integrada para atender aos requisitos das disciplinas de **Pensamento Computacional e Automação com Python** e **Soluções em Energias Renováveis e Sustentáveis**, no primeiro semestre do curso de Ciências da Computação da FIAP. O sistema simula um ecossistema de monitoramento, controle e gestão inteligente de uma microrrede aeroespacial isolada para a missão espacial experimental " FIAP a Marte". O objetivo principal é aplicar lógica de programação e conceitos de física/engenharia de energia para automatizar a análise de dados de telemetria, calcular o balanço de potência ativa, identificar anomalias e sugerir ações de eficiência energética, garantindo a autossustentabilidade operacional da nave. 

A motivação para este projeto reside na crescente demanda por sistemas autônomos e inteligentes capazes de processar grandes volumes de dados em tempo real, especialmente em cenários críticos como missões espaciais. A solução proposta aborda o desafio de transformar dados brutos de sensores em informações acionáveis, minimizando a intervenção humana e otimizando a tomada de decisões em ambientes complexos. O público-alvo inclui estudantes de computação, engenheiros de software e entusiastas de automação e inteligência artificial.

## Funcionalidades

O sistema implementa as seguintes funcionalidades essenciais para o monitoramento da missão:

*   **Coleta de Dados de Telemetria**: Simulação da obtenção de dados brutos de diversos sensores da nave, incluindo temperatura interna, comunicação com a base, sistema de energia (bateria), suporte de oxigênio e estabilidade operacional.
*   **Classificação de Parâmetros Individuais**: Análise de cada parâmetro de telemetria para determinar seu status (NORMAL, ATENÇÃO, CRÍTICO), atribuir uma pontuação de risco e gerar mensagens de status e recomendações específicas para cada anomalia detectada.
*   **Formatação Visual de Medidas**: Apresentação dos dados de telemetria com suas respectivas unidades de medida (°C para temperatura e % para os demais parâmetros), garantindo clareza e padronização.
*   **Análise de Tendência Geral da Missão**: Avaliação matemática do histórico de pontuações de risco para identificar a tendência global da missão (melhorando, piorando ou estável), fornecendo uma visão macro da saúde operacional da nave.
*  **Análise de Balanço de Potência Ativa (kW):** Modelagem matemática integrada que calcula, a cada ciclo orbital, a relação entre a Potência Solar Gerada pelos painéis fotovoltaicos e a Potência Consumida pelas cargas do sistema.
* **Cálculo do Índice de Sustentabilidade Energética (ISE):** Indicador estatístico inovador que quantifica a eficiência ecológica global da missão, mensurando a porcentagem de tempo em que a sonda operou em regime autossustentável (sem degradação acelerada do banco de armazenamento ou uso de fontes não renováveis).

## Arquitetura e Estrutura

O projeto adota uma arquitetura modular baseada em funções, organizada em um arquivo `main.py` dentro do diretório `src`. A aplicação foi desenhada como um ciclo fechado de dados (Data Loop), estruturado para processar matrizes multidimensionais sem o uso de bibliotecas externas. 

A inteligência do sistema baseia-se em um motor de regras lógicas estruturado para atuar como um Sistema de Gerenciamento pelo Lado da Demanda (DSM). Ele analisa thresholds (limites) operacionais e converte dados brutos em tomadas de decisão automatizadas para mitigação de estresse térmico, realinhamento de painéis solares e corte de cargas críticas em cenários de subgeração energética.

## Stack Tecnológica

*   **Linguagem de Programação**: Python 3
*   **Bibliotecas**: Não utiliza bibliotecas externas, focando na implementação de lógica pura em Python.

## Principais Aprendizados

Durante o desenvolvimento deste projeto, foram explorados e consolidados conceitos fundamentais de programação e pensamento computacional, tais como:

*   **Estruturas de Dados**: Utilização de listas e matrizes para representar dados de telemetria.
*   **Lógica Condicional**: Implementação de regras complexas para classificação de status e geração de recomendações.
*   **Modularização de Código**: Organização do projeto em funções bem definidas, promovendo a reutilização e a clareza do código.
*   **Automação de Análise**: Desenvolvimento de um sistema capaz de processar e interpretar dados automaticamente, simulando um cenário de monitoramento em tempo real.
*   **Resolução de Problemas**: Abordagem estruturada para identificar problemas (anomalias nos dados) e propor soluções (recomendações).

## Como Executar

Para executar o projeto localmente, siga os passos abaixo:

1.  **Clonar o Repositório**:
    ```bash
    git clone https://github.com/Dustyluc123/GS-PCAP.git
    cd GS-PCAP
    ```

2.  **Navegar até o Diretório do Código**:
    ```bash
    cd src
    ```

3.  **Executar o Script Principal**:
    ```bash
    python3 main.py
    ```

## Estrutura de Diretórios

```
GS-PCAP/
├── src/
│   └── main.py
└── README.md
```

## Melhorias Futuras

*   **Interface Gráfica (GUI)**: Desenvolvimento de uma interface de usuário para visualização mais intuitiva dos dados e status da missão.
*   **Integração com Sensores Reais**: Adaptação do sistema para receber dados de sensores físicos ou APIs de telemetria em tempo real.
*   **Machine Learning**: Implementação de algoritmos de aprendizado de máquina para predição de falhas e otimização de rotas.
*   **Geração de Relatórios**: Funcionalidade para gerar relatórios detalhados sobre o desempenho da missão e eventos críticos.

## Autor

**Lucas Barreto Santana**

*   **RM**: 573149
*   **LinkedIn**: [lucas](https://www.linkedin.com/in/ucasbarretosantana-67aa932b6/)
*   **GitHub**: [Dustyluc123](https://github.com/Dustyluc123)
*   **E-mail**: [lucasbrsantana@gmail.com ](mailto:lucasbrsantana@gmail.com ) 

## Licença

Este projeto é disponibilizado exclusivamente para fins acadêmicos, educacionais e de demonstração de portfólio. Todos os direitos reservados.
