# 🌐 Documentação Detalhada — Versão Web (HTML + JS)

## 🔹 Arquivo: index.html e style.css

### 📌 Descrição
Interface web aprimorada (com visual moderno e responsivo) que permite ao usuário verificar se um IP de destino pertence à mesma rede de um IP fixo. Exibe máscara em decimal e binário, além do resultado da comparação.

---

### 🔎 Análise e Diferenças da Nova Versão

#### 1. Separação de Estilos (Melhor Prática)
A principal mudança estrutural foi a **separação do CSS** em um arquivo externo (`style.css`). O HTML agora usa a tag `<link rel="stylesheet" href="style.css">`, tornando o código mais limpo, fácil de manter e melhorando o cache do navegador.

#### 2. Design e Estilização (Novo CSS)
O CSS foi reescrito para criar um design moderno:
* **Fonte:** Inclusão da fonte **Poppins**.
* **Layout Centrado:** Uso de `position: absolute`, e `transform: translate(-50%, -50%)` para **centralizar o contêiner** na tela.
* **Elementos:** Campos (`input`) e botão (`button`) com bordas arredondadas (`border-radius: 15px`).
* **Efeito Sombra:** A caixa principal (`.container`) ganhou uma sombra proeminente e colorida.

#### 3. Estrutura HTML
A estrutura se manteve amplamente a mesma, com campos de entrada (`<input>`) para **bits** e **IP de destino**, e uma `div` de saída (`id="saida"`) para exibir os resultados.

---

### 📂 Estrutura do Código (JavaScript)

A lógica de cálculo de rede utiliza manipulação de bits (Bitwise Operators) para replicar a funcionalidade de rede.

#### 1. Constante `IP_ORIGEM`
- Define o IP fixo usado como referência.

#### 2. Função `bitsParaMascara(bits)`
- Converte bits da máscara em decimal usando a operação de **Shift Left (`<<`)** e **Unsigned Right Shift (`>>> 0`)**.

#### 3. Função `ipParaInteiro(ip)`
- Transforma um IP em valor inteiro de 32 bits usando o método `reduce()` e o operador **`<< 8`**.

#### 4. Função `mascaraBinario(mascaraDecimal)`
- Converte a máscara decimal para binário (octetos) usando o método `map()` e `padStart(8, "0")`.

#### 5. Função Principal `verificar()`
- Obtém valores de entrada do usuário.
- Verifica se o IP destino pertence à mesma rede utilizando o **operador AND bitwise ($\&$)**:
    ```javascript
    let redeOrigem = ipOrigemInt & mascaraInt;
    let redeDestino = ipDestinoInt & mascaraInt;
    // Compara se o endereço de rede calculado é o mesmo
    ```
- Exibe o resultado na tela usando um **operador ternário**.

---

### Resumo dos Símbolos Principais (JavaScript)

| Símbolo | Função |
| :--- | :--- |
| `&` | O operador **AND bitwise**. Realiza a operação lógica bit a bit (cálculo do endereço de rede). |
| `<<` | Operador de **shift left**. Desloca bits para a esquerda. |
| `>>>` | Operador de **unsigned right shift**. Deslocamento para a direita sem sinal, garantindo inteiros positivos de 32 bits. |
| `? :` | O **operador ternário** para condicionais curtas. |