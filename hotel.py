def valorestadia(diaria, aumento, chegada):
    if chegada == 1:
        total = 31 * diaria
    else:
        if chegada <= 15:
            total = (31 - (chegada - 1)) * diaria + ((chegada - 1) * aumento)
        else:
            total = 15 * diaria + (31 - 15) * (diaria + 14 * aumento)

    print("O valor total a ser pago ao hotel pela estadia é:", total)

while True:
    print("--- Bem Vindo Ao Hotel ---")
    diaria = int(input("Insira o valor da diária no dia 1: "))
    aumento = int(input("Insira o aumento da diária a cada dia (do dia 2 até o dia 15): "))
    chegada = int(input("Insira o dia de chegada no hotel: "))

    valorestadia(diaria, aumento, chegada)

    again = input("Deseja calcular o valor para outra estadia? (Digite 's' para sim, ou qualquer outra tecla para sair): ")
    
    if again.upper() != 'S':
        break
