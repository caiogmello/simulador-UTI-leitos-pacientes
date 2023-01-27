# Problema 2 - Regulação de Leitos de UTI

## Pensamento para a solução do problema:

Nesse problema, fomos instruídos a elaborar um estudo com foco nas **estruturas de dados** e seus **algoritmos**, necessários para o funcionamento do núcleo do sistema de regulação de leitos.

### Para isso, precisei:

1. `cFila.py` - De um tipo abstrato de dados (TAD) do tipo **FIFO** (*first in first out*): 
    - Os primeiros pacientes a chegarem serão os primeiros a serem atendidos. Portanto, o melhor jeito de organizar esses pacientes seria com uma **fila**.
    - Visto que o TAD deveria ser **dinâmico** nesse caso, pois não há um limite de pacientes, preferi criar uma fila encadeada com nós simples.
    - Adiciona sempre no fim, remove sempre do início.
    
2. `cPilha.py` - De um tipo abstrato de dados (TAD) do tipo **FILO** (*first in last out*): 
    - " É importante considerar que os leitos de uma mesma categoria são alocados priorizando-se aqueles mais recentemente liberados". Portanto, o melhor jeito de 
    organizar esses leitos seria com uma **pilha**.
    - Visto que o TAD deveria ser **dinâmico** nesse caso, pois não há um limite de leitos, preferi criar uma pilha encadeada com nós simples.
    - Adiciona sempre no topo, remove sempre no topo.
3. `cPacientes.py` - Criar uma classe para organizar todas as operações possíveis com os pacientes da fila utilizando a `cFila.py`: 
    - 9 tipos de filas diferentes são criadas pela maior organização da UTI:
        - Fila de **emergência** neonatal;
        - Fila de **emergência** pediátrico;
        - Fila de **emergência** adulto;
        - Fila de **muita urgência** neonatal;
        - Fila de **muita urgência** pediátrico;
        - Fila de **muita urgência** adulto;
        - Fila de **urgência** neonatal;
        - Fila de **urgência** pediátrico;
        - Fila de **urgência** adulto;

    - **IDs aleatórios** para os pacientes são criados;
    - Pacientes são gerados e adicionados nas suas respectivas filas;
    - Envia pacientes para os leitos e os remove da fila;
    - Retorna estatísticas sobre quantidade nas filas.

4. `cLeitos.py` - Criar uma classe para organizar todas as operações possíveis com os leitos gerados pelos hospitais utilizando a `cPilha.py`:
    - 3 tipos de pilhas de leitos diferentes são criados:
        - Pilha de leito **neonatal**;
        - Pilha de leito **pediátrico**;
        - Pilha de leito **adulto**;
    -  **Hospitais de chegada** dos leitos e seus respectivos **IDs** são gerados aleatoriamente;
    -  Leitos são gerados com idade e gravidade aleatórias e adicionados nas suas respectivas pilhas;
    - Recebe pacientes e ocupa os leitos, removendo-os da pilha;
    - Retorna estatísticas sobre a quantidade de leitos disponíveis.

5. `cSimulador.py` - Criar uma classe pra gerar os pacientes e leitos e fazer uma simulação real de atendimento de pacientes aos leitos utilizando a `cPacientes.py` e a `cLeitos.py`:
    - Gera quantidade aleatória de leitos e pacientes;
    - Atende os pacientes e ocupa os leitos;
    - Mostra de maneira formatada e organizada as estatísticas:
        - Número de leitos disponíveis;
        - Mapa de leitos disponíveis;
        - Número de pacientes na fila;
        - Mapa de pacientes na fila;
        - Total de leitos gerados;
        - Número de pacientes atendidos;
6. `main.py` - Executa as funções do simulador de maneira contínua e infinita, mostrando todo o processo pelo terminal. A simulação ocorre entre intervalos curtos de tempo, realizados pela função `sleep()` do módulo `time`.



# Referências Bibliográficas:

[1] **Filas em Python | Algoritmos em Python**. Disponível em: https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/filas/

[2] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012..

[3] Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

[4] Erica Vartanian, **"6 coding best practices for beginner programmers"**. Disponível em:  https://www.educative.io/blog/coding-best-practices

[5] Matt Cone, **Markdown Cheat Sheet - A quick reference to the Markdown syntax**. Disponível em: https://www.markdownguide.org/cheat-sheet/

[6] **Print Colors in Python terminal**. Disponível em: https://www.geeksforgeeks.org/print-colors-python-terminal/


‌