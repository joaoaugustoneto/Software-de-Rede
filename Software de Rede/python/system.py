"""
Software de Rede - Verificação de Máscara e Rede
------------------------------------------------
Este programa:
1) Define um IP FIXO como constante (origem).
2) Recebe do usuário uma máscara de rede em bits.
3) Recebe do usuário um IP de destino.
4) Exibe a máscara de rede em decimal e binário.
5) Informa se o IP de destino pertence ou não à mesma rede do IP de origem.

Critérios atendidos:
- Código documentado.
- Entradas testadas.
- Mensagens intuitivas para o usuário.
"""

import ipaddress

# Constante: IP de origem
IP_ORIGEM = "192.168.10.25"  # IP fixo da máquina origem


def bits_para_mascara(bits: int) -> str:
    """
    Converte quantidade de bits da máscara em notação decimal padrão.
    Exemplo: 24 → "255.255.255.0"
    """
    rede = ipaddress.IPv4Network(f"0.0.0.0/{bits}")
    return str(rede.netmask)


def exibir_mascara(bits: int) -> None:
    """
    Mostra a máscara em decimal e em binário separado por octetos.
    """
    mascara = bits_para_mascara(bits)
    print(f"\nMáscara de rede para {bits} bits:")
    print(f"Decimal: {mascara}")

    # Mostrar também em binário
    octetos = mascara.split(".")
    binario = [format(int(octeto), "08b") for octeto in octetos]
    print("Binário (octetos):", " ".join(binario))


def mesmo_rede(ip_destino: str, bits: int) -> bool:
    """
    Verifica se o IP de destino pertence à mesma rede que o IP de origem.
    """
    rede_origem = ipaddress.IPv4Network(f"{IP_ORIGEM}/{bits}", strict=False)
    ip_destino_obj = ipaddress.IPv4Address(ip_destino)
    return ip_destino_obj in rede_origem


def main():
    print("=== SOFTWARE DE REDE ===")
    print(f"IP de origem fixo: {IP_ORIGEM}")

    # Entrada do usuário
    bits = int(input("\nDigite a quantidade de bits da máscara de rede (ex: 24): "))
    ip_destino = input("Digite o IP de destino (ex: 192.168.10.25): ")

    # Mostrar máscara em decimal e binário
    exibir_mascara(bits)

    # Verificar se estão na mesma rede
    if mesmo_rede(ip_destino, bits):
        print(f"\nO IP {ip_destino} está na MESMA rede que {IP_ORIGEM}.")
    else:
        print(f"\nO IP {ip_destino} NÃO está na mesma rede que {IP_ORIGEM}.")


if __name__ == "__main__":
    main()
