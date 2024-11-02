# Projeto de Grafos

## Representação computacional
Esta implementação do algoritmo de Ford-Fulkerson calcula o fluxo máximo em um grafo de fluxo,
ou seja, a maior quantidade de fluxo que pode passar de uma fonte a um sumidouro em um grafo 
com capacidades nas arestas. O algoritmo utiliza a técnica de busca em profundidade (DFS) 
para encontrar caminhos aumentantes enquanto houver fluxo disponível. Com o uso matriz de 
adjacência matriz_adjacencia não somente representando as capacidades originais das arestas, 
mas também permite manipular o fluxo residual diretamente, durante a execução do algoritmo

##  Algoritmo Ford Fulkerson
Implementação do algoritmo de Ford Fulkerson utilizando o DFS
- [x] Busca em largura (BFS)
- [x] Algoritmo Ford Fulkerson para caminhos mínimos

## Pré-requisitos
Antes de começar, certifique-se de ter o Python 3.10 (ou superior) instalado. Você pode verificar a versão instalada executando:

## Passo para a configração
1. Criar o ambiente virtual
```bash
python -m venv venv
```
2. Ativar o ambiente virtual
    - No windows 
    ```bash
    .\venv\Scripts\activate
    ```
   - No Linux
   ```bash
    source venv/bin/activate
   ```
3. Instalar as dependências
```bash
pip install -r requirements.txt
```

## Executando o projeto
Depois de configurar o ambiente virtual e instalar as dependências, você pode rodar o projeto diretamente. O arquivo principal para executar o projeto é main.py