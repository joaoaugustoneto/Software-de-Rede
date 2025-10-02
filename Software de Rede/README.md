# 🖥️ Software de Rede – Máscara e Verificação de IP

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como parte de uma atividade prática de Redes de Computadores.
O objetivo é criar um **software intuitivo e funcional** que:

1. Trabalhe com um **IP de origem fixo** (constante no código).
2. Permita que o usuário informe a **máscara de rede em bits**.
3. Permita que o usuário informe um **IP de destino**.
4. Exiba a **máscara em decimal e em binário (por octetos)**.
5. Informe se o IP destino pertence ou não à mesma rede do IP de origem.

O software foi desenvolvido em duas versões:
- **Versão Console (Python)**
- **Versão Web (HTML + JavaScript)**

---

## 🚀 Funcionalidades
- Conversão automática de **máscara em bits → decimal**.
- Exibição da máscara em **binário, por octetos**.
- Verificação se o **IP destino** está na mesma rede que o **IP fixo**.
- Interface **intuitiva e simples**.

---

## ⚙️ Tecnologias Utilizadas
- **Python 3.x** (com a biblioteca padrão `ipaddress`)
- **HTML5, CSS3 e JavaScript**

---

## 📂 Estrutura do Projeto
/ (root)
├── web/                 # Contém index.html e style.css
├── python/              # Contém software_rede.py
├── docs/                # Contém a documentação detalhada
└── README.md            # Documentação principal (Este arquivo)


---

## ▶️ Como Executar

### 🔹 Versão Python (console)
1. Certifique-se de ter o **Python 3.x** instalado.
2. Navegue até a pasta `python/` no terminal e execute o script:
   ```bash
   cd python/
   python software_rede.py
   ```
3. Informe a máscara em bits e o IP de destino.

**Exemplo de execução:**
=== SOFTWARE DE REDE ===
IP de origem fixo: 192.168.10.25

Digite a quantidade de bits da máscara de rede (ex: 24): 24
Digite o IP de destino (ex: 192.168.10.25): 192.168.10.30

Máscara de rede para 24 bits:
Decimal: 255.255.255.0
Binário (octetos): 11111111 11111111 11111111 00000000

O IP 192.168.10.30 está na MESMA rede que 192.168.10.25.


---

### 🔹 Versão Web (HTML + JavaScript)
1. Navegue até a pasta `web/`.
2. Abra o arquivo **`index.html`** em qualquer navegador moderno.
3. Insira os dados e clique em **Verificar Rede**.

---

## 🛠️ Melhorias Futuras

### Versão Python
- [ ] Adicionar **tratamento de exceções** para entradas inválidas.
- [ ] Implementar o uso de **argumentos de linha de comando** (`argparse`).

### Versão Web
- [ ] Adicionar **validação de formato de IP** (via Regex no JavaScript).
- [ ] Aprimorar o **tratamento de erros** exibindo mensagens na UI (interface do usuário).

---

## 👨‍💻 Autores

Projeto desenvolvido por 
**[João Augusto E. Neto, Eduardo Gomes da Cunha, Guilherme Miranda da conceição, Gustavo de Melo Marques Coelho]**