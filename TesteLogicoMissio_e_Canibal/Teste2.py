from os import system
import time

missio_mar1 = 3
cani_mar1 = 3
missio_mar2 = 0
cani_mar2 = 0
fim = False

def saida():
    global missio_mar1, cani_mar1, missio_mar2, cani_mar2, fim
    continuar = input("Deseja continuar? \n[S]-Sim \n[N]-Não\n").strip().upper()
    if continuar == "S":
        missio_mar1 = 3
        cani_mar1 = 3
        missio_mar2 = 0
        cani_mar2 = 0
        jogo()
    else:
        print("Saindo")
        time.sleep(1)
        system("cls")
        print("Saindo.")
        time.sleep(1)
        system("cls")
        print("Saindo..")
        time.sleep(1)
        system("cls")
        print("Saindo...")
        fim = True

def validar_estado():
    if (cani_mar1 > missio_mar1 > 0) or (cani_mar2 > missio_mar2 > 0):
        print("\nVocê PERDEU! Os canibais comeram os missionários!")
        saida()
    elif missio_mar2 == 3 and cani_mar2 == 3:
        print("\nVocê GANHOU! Todos atravessaram com segurança!")
        saida()

def estado_margens(passar1="_", passar2="_", lado="ida"):
    system("cls")
    barco_mar1 = f"{' ' * (6 - missio_mar1 - cani_mar1)}{'M' * missio_mar1}{'C' * cani_mar1}"
    barco_mar2 = f"{' ' * (6 - missio_mar2 - cani_mar2)}{'M' * missio_mar2}{'C' * cani_mar2}"

    if lado == "ida":
        print("                      __             ")
        print(f"{barco_mar2}               /_/   {barco_mar1}") 
        print(f"-------------______\{passar1}|{passar2}/-------------")
    else:
        print("             __                               ")
        print(f"{barco_mar2}       \_\           {barco_mar1}") 
        print(f"-------------\{passar1}|{passar2}/______-------------")
    
    print(f"Margem 1: Missionários: {missio_mar1}, Canibais: {cani_mar1}")
    print(f"Margem 2: Missionários: {missio_mar2}, Canibais: {cani_mar2}\n")


def animar_navegacao(lado="ida"):
    if lado == "ida":
        system("cls")
        print("                      __             ") 
        print("                     /_/              ") 
        print("-------------______\_|_/-------------")
        time.sleep(0.2)
        system("cls")
        print("                     __             ") 
        print("                    /_/              ") 
        print("-------------_____\_|_/_-------------")
        time.sleep(0.2)
        system("cls")
        print("                    __             ") 
        print("                   /_/              ") 
        print("-------------____\_|_/__-------------")
        time.sleep(0.2)
        system("cls")
        print("                   __             ") 
        print("                  /_/              ") 
        print("-------------___\_|_/___-------------")
        time.sleep(0.2)
        system("cls")
        print("                  __             ") 
        print("                 /_/              ") 
        print("-------------__\_|_/____-------------")
        time.sleep(0.2)
        system("cls")
        print("                 __             ") 
        print("                /_/              ") 
        print("-------------_\_|_/_____-------------")
        time.sleep(0.2)
        system("cls")
        print("                __             ") 
        print("               /_/              ") 
        print("-------------\_|_/______-------------")
    else:
        system("cls")
        print("             __             ") 
        print("             \_\              ") 
        print("-------------\_|_/______-------------")
        time.sleep(0.2)
        system("cls")
        print("              __             ") 
        print("              \_\              ")  
        print("-------------_\_|_/_____-------------")
        time.sleep(0.2)
        system("cls")
        print("               __             ") 
        print("               \_\              ")  
        print("-------------__\_|_/____-------------")
        time.sleep(0.2)
        system("cls")
        print("                __             ") 
        print("                \_\              ")  
        print("-------------___\_|_/___-------------")
        time.sleep(0.2)
        system("cls")
        print("                 __             ") 
        print("                 \_\              ")  
        print("-------------____\_|_/__-------------")
        time.sleep(0.2)
        system("cls")
        print("                  __             ") 
        print("                  \_\              ")  
        print("-------------_____\_|_/_-------------")
        time.sleep(0.2)
        system("cls")
        print("                   __             ") 
        print("                   \_\              ")  
        print("-------------______\_|_/-------------")


def escolher_passageiros(margem_atual):
    global missio_mar1, cani_mar1, missio_mar2, cani_mar2
    passar1, passar2 = "_", "_"

    while True:
        estado_margens(passar1, passar2, "ida" if margem_atual == 1 else "volta")
        passar1 = input("Quem deve entrar no barco? [M]-Missionário [C]-Canibal: ").strip().upper()
        if passar1 == "M" and ((missio_mar1 if margem_atual == 1 else missio_mar2) > 0):
            if margem_atual == 1:
                missio_mar1 -= 1
            else:
                missio_mar2 -= 1
            break
        elif passar1 == "C" and ((cani_mar1 if margem_atual == 1 else cani_mar2) > 0):
            if margem_atual == 1:
                cani_mar1 -= 1
            else:
                cani_mar2 -= 1
            break
        else:
            print("Escolha inválida ou insuficiente na margem. Tente novamente.")

    while True:
        estado_margens(passar1, passar2, "ida" if margem_atual == 1 else "volta")
        passar2 = input("Deseja adicionar mais alguém? [M]-Missionário [C]-Canibal [N]-Não: ").strip().upper()
        if passar2 == "N":
            break
        elif passar2 == "M" and ((missio_mar1 if margem_atual == 1 else missio_mar2) > 0):
            if margem_atual == 1:
                missio_mar1 -= 1
            else:
                missio_mar2 -= 1
            break
        elif passar2 == "C" and ((cani_mar1 if margem_atual == 1 else cani_mar2) > 0):
            if margem_atual == 1:
                cani_mar1 -= 1
            else:
                cani_mar2 -= 1
            break
        else:
            print("Escolha inválida ou insuficiente na margem. Tente novamente.")

    return passar1, passar2

def atualizar_margens(passar1, passar2, margem_atual):
    global missio_mar1, cani_mar1, missio_mar2, cani_mar2
    if margem_atual == 1:
        if passar1 == "M": missio_mar2 += 1
        if passar1 == "C": cani_mar2 += 1
        if passar2 == "M": missio_mar2 += 1
        if passar2 == "C": cani_mar2 += 1
    else:
        if passar1 == "M": missio_mar1 += 1
        if passar1 == "C": cani_mar1 += 1
        if passar2 == "M": missio_mar1 += 1
        if passar2 == "C": cani_mar1 += 1

def jogo():
    margem_atual = 1
    global fim
    while not fim:
        estado_margens()
        passar1, passar2 = escolher_passageiros(margem_atual)
        animar_navegacao("ida" if margem_atual == 1 else "volta")
        atualizar_margens(passar1, passar2, margem_atual)
        margem_atual = 2 if margem_atual == 1 else 1
        validar_estado()

jogo()
