# 📦 Projeto Kafka Dockerizado: Produtor e Consumidor

Este projeto demonstra um cluster Apache Kafka resiliente rodando em Docker com 3 brokers, configurado para alta disponibilidade e escalabilidade. O objetivo é simular a comunicação Pub/Sub (Publish-Subscribe) e Fila Distribuída (Consumer Groups) usando scripts Python.

## ⚙️ Pré-requisitos

Para executar este projeto, você precisará ter instalado e configurado em sua máquina:

- **Docker** e **Docker Compose**
- **Python 3** e **pip** (para o ambiente virtual)

---

## 🚀 Guia de Execução

Siga os passos abaixo na ordem para iniciar o cluster, criar o tópico e executar as aplicações Python.

### Passo 1: Inicializar o Cluster Kafka (3 Brokers)

O cluster é definido no arquivo `docker-compose.yml` e inclui o Zookeeper e 3 Brokers Kafka.

1.  **Navegue até o diretório raiz do projeto** (onde o `docker-compose.yml` está).
2.  **Inicie o Cluster:** O comando `-d` executa os contêineres em segundo plano.

    ```bash
    docker-compose up -d
    ```

3.  **Aguarde a Inicialização:**
    Aguarde cerca de **10 a 15 segundos** para garantir que todos os brokers estejam totalmente prontos e o Controller tenha sido eleito.

4.  **Verifique o Status do Cluster:**

    ```bash
    docker ps
    ```

### Passo 2: Criar o Tópico `PRODUCTS`

O tópico será criado com 2 partições e um fator de replicação de 3, garantindo resiliência contra a falha de até 2 brokers.

1.  **Crie o Tópico:**
    Estamos usando a conexão interna do Docker (`kafka-broker1:29092`) para garantir a estabilidade.

    ```bash
    docker exec kafka-broker1 kafka-topics --create --topic PRODUCTS --bootstrap-server kafka-broker1:29092 --partitions 2 --replication-factor 3
    ```

2.  **Verifique o Tópico e o Balanceamento de Liderança:**
    Este comando deve mostrar que as réplicas 1, 2 e 3 estão envolvidas nas partições.

    ```bash
    docker exec kafka-broker1 kafka-topics --describe --topic PRODUCTS --bootstrap-server kafka-broker1:29092
    ```

    Caso tanto o "create" quanto o "describe" não funcionem com o kafka-broker1 troque pelos outros brokers:

### ⚠️ Solução de Problemas: Falha na Criação do Tópico

Se o comando de criação (`create`) ou verificação (`describe`) do tópico falhar com o `kafka-broker1`, isso geralmente indica que o broker não conseguiu se comunicar rapidamente com o Controller do cluster.

**Solução:** Tente o mesmo comando usando outro broker como ponto de contato. Use os comandos abaixo, que utilizam a **conexão interna correta** do Docker.

#### Tentativa com `kafka-broker2`

Use o Broker 2 como ponto de contato.

**1. Comando CREATE (Criação do Tópico):**

````bash
docker exec kafka-broker2 kafka-topics --create --topic PRODUCTS --bootstrap-server kafka-broker2:29093 --partitions 2 --replication-factor 3

### Passo 3: Configurar e Executar a Aplicação Python

1.  **Crie e Ative o Ambiente Virtual (`venv`):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para macOS/Linux
    # Ou: .\venv\Scripts\activate   # Para Windows (PowerShell)
    ```

2.  **Instale as Dependências:**

    O arquivo `requirements.txt` lista todas as bibliotecas necessárias.

    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute os Consumers (Modo Fila Distribuída):**
    Abra **duas janelas/abas de terminal separadas** e execute o `consumer.py` em cada uma (certifique-se de que o `venv` está ativo em ambas).

    - **Terminal 1 (Consumer 1):**

      ```bash
      python consumer.py
      ```

    - **Terminal 2 (Consumer 2):**

      ```bash
      python consumer.py
      ```

    ```
      > 💡 **Nota:** Como ambos estão no mesmo **Consumer Group**, eles dividirão a carga: um lerá a Partição 0 e o outro a Partição 1.

    ```

4.  **Execute o Produtor:**
    Abra uma **terceira janela/aba** de terminal e execute o produtor para começar a enviar mensagens:

    ```bash
    python producer.py
    ```

### 🗑️ Limpeza (Shutdown)

Para parar e remover os contêineres e a rede criada pelo Docker Compose:

```bash
docker-compose down
````
