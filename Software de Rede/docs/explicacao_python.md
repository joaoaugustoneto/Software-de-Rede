
# 🐍 Documentação Detalhada — Versão Compilador (Python)

## 🔹 Arquivo: software\_rede.py

### 📌 Descrição
Este script em Python permite verificar se um **IP de destino** informado pertence à mesma rede de um **IP fixo de origem** (`IP_ORIGEM`), usando uma máscara de rede fornecida em bits. Ele utiliza a biblioteca nativa **`ipaddress`** do Python para realizar cálculos de rede de forma eficiente e robusta.

---

### 📚 Bibliotecas Utilizadas

| Biblioteca | Propósito |
| :--- | :--- |
| **`ipaddress`** | Simplifica o trabalho com endereços e redes IPv4/IPv6, permitindo criar objetos que representam redes (`IPv4Network`) e endereços (`IPv4Address`). |

---

### 📂 Estrutura do Código

#### 1. Constante de Origem
```python
IP_ORIGEM = "192.168.10.25"
````

  - **Função:** Define o IP fixo usado como referência para comparação.

#### 2\. Função `bits_para_mascara(bits: int) -> str`

```python
def bits_para_mascara(bits: int) -> str:
    rede = ipaddress.IPv4Network(f"0.0.0.0/{bits}")
    return str(rede.netmask)
```

  - **Lógica Central:** Utiliza **`ipaddress.IPv4Network`** para calcular a máscara decimal a partir da quantidade de bits.

#### 3\. Função `exibir_mascara(bits: int) -> None`

  - Chama `bits_para_mascara` para obter a máscara decimal.
  - **Binário:** Usa **List Comprehension** (`[format(int(o), "08b") for o in octetos]`) para converter cada octeto para sua representação binária de 8 dígitos.

#### 4\. Função `mesmo_rede(ip_destino: str, bits: int) -> bool`

```python
def mesmo_rede(ip_destino: str, bits: int) -> bool:
    rede_origem = ipaddress.IPv4Network(f"{IP_ORIGEM}/{bits}", strict=False)
    ip_destino_obj = ipaddress.IPv4Address(ip_destino)
    return ip_destino_obj in rede_origem
```

  - **Verificação:** Utiliza o **Operador de Pertinência (`in`)** do `ipaddress` para verificar se o objeto de endereço de destino (`ip_destino_obj`) está contido no objeto de rede de origem (`rede_origem`).

#### 5\. Função `main()`

  - **Função:** Controla o fluxo do programa, recebe entradas do usuário (`input()`) e chama as funções de cálculo e exibição.

-----

### 🔑 Resumo dos Símbolos Principais (Python)

| Símbolo | Função |
| :--- | :--- |
| **`def`** | Define uma função ou método. |
| **`->`** | Indica o tipo de retorno esperado de uma função (type hinting). |
| **`f"..."`** | Define uma f-string (string formatada). |
| **`in`** | Operador de Pertinência. Verifica se um elemento está contido em uma coleção. |
| **`[... for ... in ...]`** | List Comprehension. Constrói uma lista a partir de uma expressão. |
