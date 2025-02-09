def split_odd_and_even(n):
    num_str = str(n)  # Converte o número de entrada para uma string para facilitar a iteração sobre cada dígito
    resultado = []  # Inicializa a lista que armazenará os grupos de números pares ou ímpares
    parte_atual = ""  # String temporária para construir os grupos de dígitos pares ou ímpares

    def e_impar(digito):
        return int(digito) % 2 != 0  # Retorna True se o dígito for ímpar, False se for par

    # Itera sobre cada dígito na string do número
    for digito in num_str:
        # Se o dígito atual for ímpar e a parte atual estiver vazia ou também for ímpar, acrescenta o dígito
        if e_impar(digito) and (not parte_atual or e_impar(parte_atual[-1])):
            parte_atual += digito
        # Se o dígito atual for par e a parte atual estiver vazia ou também for par, acrescenta o dígito
        elif not e_impar(digito) and (not parte_atual or not e_impar(parte_atual[-1])):
            parte_atual += digito
        else:
            # Se o dígito atual for diferente em paridade do último dígito da parte atual, salva a parte atual na lista
            resultado.append(int(parte_atual))
            parte_atual = digito  # Inicia uma nova parte com o dígito atual
    # Após terminar a iteração, verifica se ainda há uma parte não adicionada ao resultado e a adiciona
    if parte_atual:
        resultado.append(int(parte_atual))

    return resultado  # Retorna a lista com os grupos separados

# Exemplo de uso:
resultado = split_odd_and_even(123456789)
print(resultado)  # Saída esperada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
