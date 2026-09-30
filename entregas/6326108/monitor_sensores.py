def monitorar(lista):
    soma_leituras = 0.0
    qtd_validade = 0

    for leitura in lista:
        if leitura > 80.0:
            print(f"[DESCARTE] {leitura}C fora da faixa")
            continue

        elif leitura == -999.0: 
            print("[FALHA] Sensor corrompido")
            break

        else:
            print(f"[OK] Leitura de {leitura}C registrada.")
            soma_leituras += leitura
            qtd_validade += 1

    if qtd_validade > 0:
        media = soma_leituras / qtd_validade
        print(f"\nQuantidade de leituras válidas: {qtd_validade}")
        print(f"Média: {media:.2f}C")
    else:
        print("\nNenhuma leitura válida registrada.")


# IMPORTANTE: Você precisa chamar a função para ela rodar!
minhas_leituras = [25.0, 85.0, 30.0, -999.0, 20.0]
monitorar(minhas_leituras)