import time
import random 

#atributos
vida = 50
vida_max = 50
dano = 10
defesa = 10
energia = 150
energia_max = 150
level = 1
xp = 0
#
rodada = 1
#
arma_atual = "nenhuma"
armadura_atual = "nenhuma"
equipamento_atual = "nenhuma"
dano_arma = 0
defesa_armadura = 0
dano_equipamento = 0
defesa_equipamento = 0

#
biotipos = ["Robusto", "Ágil", "Resistente", "Intelectual"]
biotipo = ""
bonus_xp = 0
batalhas = 0
#
nivel_inv = 1
qtd_livre = 0
inventario = {}
#
locais = ["vila", "floresta", "montanha", "rio"]
local_antigo = ""
local = "vila"
eventos_f = []

banco_de_itens = {
"Espada de Madeira": {"tipo": "arma", "quantidade": 1, "dano": 5},

"Espada de Pedra" : {"tipo": "arma", "quantidade": 1, "dano": 7},

"Espada de Ferro" : {"tipo": "arma", "quantidade": 1, "dano": 10},

"Espada de Obsidiana" : {"tipo": "arma", "quantidade": 1, "dano": 17},

"Adaga improvisada" : {"tipo": "arma", "quantidade": 1, "dano": 4},

"Adaga" : {"tipo": "arma", "quantidade": 1, "dano": 6},


"Escudo de Madeira": {"tipo": "equipamento", "quantidade": 1, "defesa": 2},

"Escudo de Ferro": {"tipo": "equipamento", "quantidade": 1, "defesa": 4},

"Escudo de Obsidiana": {"tipo": "equipamento", "quantidade": 1, "defesa": 8},

"Amolador de Espada": {"tipo": "equipamento", "quantidade": 1, "dano": random.randint(1, 4)},

"Soco ingles": {"tipo": "equipamento", "quantidade": 1, "dano": random.randint(2, 3)},


"Armadura de Sucata": {"tipo": "armadura", "quantidade": 1, "defesa": 7},

"Armadura de Ferro": {"tipo": "armadura", "quantidade": 1, "defesa": 9},

"Armadura de Diamante": {"tipo": "armadura", "quantidade": 1, "defesa": 15},


"Carne Magra": {"tipo": "comida", "quantidade": 1, "energia": 20},

"Carne Gorda": {"tipo": "comida", "quantidade": 1, "energia": 30},

"Carne Magra assada": {"tipo": "comida", "quantidade": 1, "energia": 30},

"Carne Gorda assada": {"tipo": "comida", "quantidade": 1, "energia": 40},

"Cogumelo Champignon": {"tipo": "comida", "quantidade": 1, "energia": 5},

"Cogumelo Amanita muscaria": {"tipo": "comida", "quantidade": 1, "energia": -50},

"Maça": {"tipo": "comida", "quantidade": 1, "energia": 6},

"Pão": {"tipo": "comida", "quantidade": 1, "energia": 15},

"Mel": {"tipo": "comida", "quantidade": 1, "energia": 15},

"BOLACHINHA": {"tipo": "comida", "quantidade": 1, "energia": random.randint(-15, 45)},


"Poção de Cura pequena": {"tipo": "cura", "quantidade": 1, "cura": 10},

"Poção de Cura": {"tipo": "cura", "quantidade": 1, "cura": 20},

"Poção de Cura grande": {"tipo": "cura", "quantidade": 1, "cura": 30},

"bandagen": {"tipo": "cura", "quantidade": 1, "cura": 5},

"kit médico completo" : {"tipo": "cura", "quantidade": 5, "cura": 100},


"Madeira" : {"tipo": "material", "quantidade": 1},

"Pedra" : {"tipo": "material", "quantidade": 1},

"Ferro" : {"tipo": "material", "quantidade": 1},

"Carvão" : {"tipo": "material", "quantidade": 1},

"Sipó" : {"tipo": "material", "quantidade": 1},

"Diamante" : {"tipo": "material", "quantidade": 1},

"Graveto" : {"tipo": "material", "quantidade": 1},

"Pano" : {"tipo": "material", "quantidade": 1},

"Obsidiana" : {"tipo": "material", "quantidade": 1}
}

receitas = {

    # Armas

    "Espada de Madeira": {
        "Madeira": 4,
        "Graveto": 1,
        "Sipó": 1
    },

    "Espada de Pedra": {
        "Pedra": 5,
        "Graveto": 1,
        "Sipó": 1
    },

    "Espada de Ferro": {
        "Ferro": 5,
        "Madeira": 1,
        "Sipó": 2
    },

    "Espada de Obsidiana": {
        "Obsidiana": 5,
        "Madeira": 1,
        "Sipó": 2
    },

    "Adaga improvisada": {
        "Pedra": 2,
        "Graveto": 1
    },

    "Adaga": {
        "Ferro": 1,
        "Madeira": 1,
        "Sipó": 1
    },


    # Escudos

    "Escudo de Madeira": {
        "Madeira": 4,
        "Sipó": 2
    },

    "Escudo de Ferro": {
        "Ferro": 5,
        "Madeira": 2,
        "Sipó": 2
    },

    "Escudo de Obsidiana": {
        "Obsidiana": 6,
        "Madeira": 2,
        "Sipó": 2
    },


    # Armaduras

    "Armadura de Sucata": {
        "Ferro": 3,
        "Pano": 2
    },

    "Armadura de Ferro": {
        "Ferro": 8,
        "Pano": 2
    },

    "Armadura de Diamante": {
        "Diamante": 8,
        "Ferro": 4,
        "Pano": 2
    },


    # Equipamentos

    "Amolador de Espada": {
        "Pedra": 2,
        "Ferro": 1
    },

    "Soco ingles": {
        "Ferro": 2,
        "Pano": 1
    },


    # Comidas

    "Carne Magra assada": {
        "Carne Magra": 2,
        "Carvão": 2
    },

    "Carne Gorda assada": {
        "Carne Gorda": 2,
        "Carvão": 2
    },


    # Itens de cura

    "Poção de Cura pequena": {
        "Cogumelo Champignon": 2,
        "Maça": 1
    },

    "Poção de Cura": {
        "Poção de Cura pequena": 2,
        "Cogumelo Champignon": 2
    },

    "Poção de Cura grande": {
        "Poção de Cura": 2,
        "Cogumelo Champignon": 3
    },

    "bandagen": {
        "Pano": 2
    },

    "kit médico completo": {
        "bandagen": 5,
        "Pano": 5,
        "Poção de Cura grande": 2
    }
}
#

#cores do sistema
C_PRETO = "\033[90m"
C_VERMELHO = "\033[91m"
C_VERDE = "\033[92m"
C_AMARELO = "\033[93m"
C_AZUL = "\033[94m"
C_ROXO = "\033[95m"
C_CIANO = "\033[96m"
C_BRANCO = "\033[97m"

F_PRETO = "\033[100m"
F_VERMELHO = "\033[101m"
F_VERDE = "\033[102m"
F_AMARELO = "\033[103m"
F_AZUL = "\033[104m"
F_ROXO = "\033[105m"
F_CIANO = "\033[106m"
F_BRANCO = "\033[107m"

N_VERDE = "\033[38;5;82m"
N_AZUL = "\033[38;5;51m"
N_ROXO = "\033[38;5;201m"
N_ROSA = "\033[38;5;198m"
N_LARANJA = "\033[38;5;208m"
N_AMARELO = "\033[38;5;226m"
N_CIANO = "\033[38;5;87m"
N_VERMELHO = "\033[38;5;196m"

RESET = "\033[0m"
rank_cor = C_VERDE
rank_texto = "Iniciante"
###

#funcoes de config

def cadastro():
        global jogador, biotipo, vida, energia, vida_max, energia_max, dano, defesa, classe, bonus_xp

        jogador = input("\nBoas Vindas novo aventureiro! Gostaria de se registrar?\nPrimeiro, Como você gostaria de ser chamado?\n:")
        while True:
                try:
                        n_classe = int(input("""Qual é a sua classe?
                        =============================
                        | 1 - Guerreiro     | (maior dano)               
                        | 2 - Tanque        | (maior defesa)            
                        | 3 - Sábio         | (maior ganho de xp)  
                        | 4 - Atleta        | (maior energia)
                        ==============================
                :"""))
                
                        break
                except ValueError:
                        print("Comando inexistente...\n")

        #modo admin de teste
        if jogador == "weslley safadao" and n_classe == 1:
                print("Ativando modo tiki yara aura admin...")
                time.sleep(3)
                ganhar_xp(10000)        
                biotipo = "Disciplinudo"
                b_txt = "+ 9999 aura"
                coletar_auto('Espada de Obsidiana', 2)
                coletar_auto('Madeira', 5)
                coletar_auto("Armadura de Diamante", 1)
                coletar_auto("kit médico completo", 3)
                coletar_auto("Madeira", 99)
                coletar_auto("Pedra", 99)
                coletar_auto("Ferro", 99)
                coletar_auto("Sipó", 99)
                coletar_auto("Graveto", 99)
                coletar_auto("Diamante", 99)
                coletar_auto("Graveto", 99)
                coletar_auto("Pano", 99)
                #

        if n_classe not in range(1, 5):
                n_classe = random.randint(1, 4)
                print("*Classe desconhecida*\nEscolhendo Classe aleatória... ")

        if n_classe == 1:
                classe = "Guerreiro"
                dano +=3
        elif n_classe == 2:
                classe = "Tanque"
                defesa += 3
        elif n_classe == 3:
                classe = "Sábio"
                bonus_xp += 3
        elif n_classe == 4:
                classe = "Atleta"
                energia_max += 20
                energia = energia_max


        if biotipo == "":
                biotipo = random.choice(biotipos)
        if biotipo == "Robusto":
                vida_max += 5
                vida = vida_max
                b_txt = "+5 Vida máxima"
        elif biotipo == "Ágil":
                        energia_max += 15
                        energia = energia_max
                        b_txt = "+15 Energia máxima"
        elif biotipo == "Resistente":
                        defesa += 2
                        b_txt = "+2 defesa"
        elif biotipo == "Intelectual":
                        bonus_xp += 2
                        b_txt = "+2 Bônus de XP"


        print(f"\nSeu Biotipo ideal classificado nos testes é: {biotipo} ({b_txt})")                

        ver_ficha()

        input("Seu cadastro de aventureiro foi concluido!\n-Aperte enter para comecar sua jornada.")



def historia():
    time.sleep(1)
    print("===== Dia normal em Jaborá-SC =====")
    time.sleep(2)

    print("\n??? - Filho, consegue lavar os copos para a mamãe?")
    time.sleep(1.2)

    print("Sai dessa coroa, tô nos altos puxão no fogo livre com os resenhas")
    time.sleep(1.4)

    print("??? - Pelo menos pega os pila na mesa e vai comprar pão pra janta.")
    time.sleep(1.2)

    print("??? - A nutricionista mandou você se movimentar!.")
    time.sleep(1.2)

    print("!")
    time.sleep(0.5)

    print("(Vou botar tudo em gift card e falar que não tinha kkk levei vantagi)")
    time.sleep(1.6)

    print("Ok mamãe")
    time.sleep(1.2)
    input("\nEnter para continuar...")

    print("\n(Chegando...)")
    time.sleep(1.5)

    print("(POW!)")
    time.sleep(4)

    print("(*Você tropeçou e levantou com uma luz forte na cara*)")
    time.sleep(1.5)

    print("\neitha!")
    time.sleep(1.2)

    print("Aonde estou? Eu só virei a esquina")
    time.sleep(1.2)

    print("...")
    time.sleep(1.4)

    print("EU ESTOU NUM ISEKAI DE ANIME!")
    time.sleep(1.4)

    print("Finalmente vou falar japonês e vencer o rei demônio!")
    time.sleep(2)

    print("\n??? - Mãe, olha aquele gordinho esquisito gritando.")
    time.sleep(1.6)

    print("??? - Por isso você tem que parar de comer bolachinha recheada, pra nao ficar igual...\n")
    time.sleep(1.6)

    print("Essas pessoas não entendem minha AURA!")
    time.sleep(1.2)

    print("\nHomem misterioso - Cala a boca mr. Obesity!\n")
    time.sleep(1.2)

    print("!")
    time.sleep(0.8)

    print("Quem é você?")
    time.sleep(1.6)

    print("\nHomem misterioso - É o seguinte, aparentemente chamei a pessoa errada para cá..")
    time.sleep(2)

    print("mas eu não quero mais desconto do vale picanha\nentão dá teus pulos.\n")
    time.sleep(2)

    print("vale de gue?\n")
    time.sleep(1.6)

    print("Homem misterioso - talvez pedindo dinheiro na rua você nao morra.\n")
    time.sleep(2)

    print("Ma...")
    time.sleep(1.6)

    print("\n(Homem misterioso desaparece)\n")
    time.sleep(1.5)

    print("O que um protagonista como eu faria?")
    time.sleep(1.5)
    
    print("Já sei! Vou ir à guilda de aventureiros!\n")
    time.sleep(1.5)

    input("E assim começa sua aventura gulosa..\nEnter para continuar...")

    print("\nExplore a floresta e colete recursos e armas maneiras.")
    time.sleep(1.6)

    print("Aumente seu nivel enquanto tenta nao morrer.")
    time.sleep(1.6)

    print("(Você chegou a guilda de aventureiros para iniciantes da cidade)")
    time.sleep(3)

#funcoes do jogo
def acoes():
        try:
                acao = int(input("""
                
                - O que devo fazer agora?
                =
                | 1 - Explorar a floresta  ===========|
                | 2 - Inventário/Criar item  =========|
                | 3 - Checar Ficha  ==================|
                | 4 - Pegar recursos  ================| 
                =  
                :"""))

                if acao == 1:
                        explorar()
                elif acao == 2:
                        inventario_menu()
                if acao == 3:
                        ver_ficha()
                if acao == 4:
                        pegar_recursos()
        except ValueError:
                print("Comando inexistente...\n")
#                                                        

def explorar():
        global local
        while True:
                esc = input(f"\n{C_ROXO}Você está em {local}.{RESET}\n O que devo fazer?\n1 - explorar a área\n2 - explorar outro local\n3 - desistir de explorar\n: ")

                if esc == "1":
                        if local == "vila":
                                explorar_vila()
                                break
                        elif local == "floresta":
                                explorar_floresta()
                                break
                        elif local == "rio":
                                explorar_rio()
                                break
                        elif local == "montanha":
                                explorar_montanha()
                                break
                        else:
                                print("escolha inexistente...\n")

                elif esc == "2":
                        while True:
                                esc = input("\nPara onde devo ir?\n 1 - vila (lv. min:0)\n2 - floresta (lv. min:3)\n3 - rio (lv. min:8)\n4 - montanha (lv. min:12)")
                                if esc == "1":  
                                        local_antigo = local
                                        local = "vila"
                                        if local == local_antigo:
                                                print(f"Você ja está em {C_ROXO}{local}...{RESET}")
                                                break
                                        else:
                                                print(f"Você chegou a {C_ROXO}{local}{RESET}!")
                                                break
                                elif esc == "2":
                                        if level < 3:
                                                print("Você desistiu de ir por medo...")
                                                break
                                        local_antigo = local
                                        local = "floresta"
                                        if local == local_antigo:
                                                print(f"Você ja está em {C_ROXO}{local}...{RESET}")
                                                break
                                        else:
                                                print(f"Você chegou a {C_ROXO}{local}{RESET}!")
                                                break
                                elif esc == "3":
                                        if level < 8:
                                                print("Você desistiu de ir por medo...")
                                                break
                                        local_antigo = local
                                        local = "rio"
                                        if local == local_antigo:
                                                print(f"Você ja está em {C_ROXO}{local}...{RESET}")
                                                break
                                        else:
                                                print(f"Você chegou a {C_ROXO}{local}{RESET}!")
                                                break
                                elif esc == "4":
                                        if level < 12:
                                                print("Você desistiu de ir por medo...")
                                                break
                                        local_antigo = local
                                        local = "montanha"
                                        if local == local_antigo:
                                                print(f"Você ja está em {C_ROXO}{local}...{RESET}")
                                                break
                                        else:
                                                print(f"Você chegou a {C_ROXO}{local}{RESET}!")
                                                break
                                else:
                                        print("escolha inexistente")
                        
                        energia -= 15
                        print(f"Você perdeu 15 energia andando...{energia}/{energia_max}")

                elif esc == "3":
                        break
                                        
                else:
                        print("escolha inexistente...\n")

def explorar_vila():
        n = random.randint(1, 2)
        if n == 1:
                ladrao()
        elif n == 2:
                senhora()
        #elif n == 3:

        ##elif n == 4:
           
        #elif n == 5:
           

def explorar_floresta():
        n = random.randint(1, 5)
        if n == 1:
                lobo()
        elif n == 2:
                goblin()
        elif n == 3:
                lenhador()
        elif n == 4:
                macieira()
        elif n == 5:
                javali()


def explorar_rio():
        n = random.randint(1, 2)
        if n == 1:
                slime()
        elif n == 2:
                troca()
        #elif n == 3:

        ##elif n == 4:
           
        #elif n == 5:


def explorar_montanha():
        n = 1#random.randint(1, 5)
        if n == 1:
            golem()
        #elif n == 2:
   
        #elif n == 3:

        ##elif n == 4:
           
        #elif n == 5:


#eventos vila
def ladrao():
        lista = list(inventario.keys())
        if len(lista) > 0:
                item = lista[1]

                print(f"Passando por um caminho da vila, de repente um aruaceiro te ameaça por {item} de seu inventario.")
                time.sleep(1)
                while True:
                        esc = input(f"O que fazer?\n1 - lutar\n2 - entregar todos {item} do inventario\n: ")
                        if esc == "1":
                                combate("Ladrão", 25, range(12, 17), 7)
                                if vida > 0:
                                        coletar_recurso("Espada de Pedra", 1)
                                        coletar_recurso("Poção de Cura", 2)
                                break
                        if esc == "2":
                                del inventario[item]
                                print(f"{N_VERMELHO}Ladrão saiu com seu {item}...{RESET}")
                                time.sleep(1)
                                break
                        else:
                                print("Escolha inexistente...\n")

        else:
                print("Passando por um caminho da vila, de repente um aruaceiro tenta te roubar, mas vendo sua pobreza, ele ri e te oferece ajuda.")
                coletar_recurso("Diamante", 2)
#
def senhora():
        global energia
        print("Enquanto andava pela vila...\n")
        time.sleep(0.6)
        esc = input("Idosa - Olá meu fi, poderia me ajudar a procurar meu gatinho?\njusto agora que eu ia castrar ele...\n\nO que fazer?\n1 - Ajudar\n2 - Deixar a dignidade do gato\n:")
        while True:
                if esc == "1":
                        if random.randint(1, 3) != 3:
                                print("..")
                                time.sleep(2)
                                print("Você achou o gato e o devolveu para a senhora")
                                print("\nSenhora - Muito obrigada garotinho, tome isso como recompensa.")
                                coletar_recurso("Maça", random.randint(2, 5))
                                coletar_recurso("Pano", random.randint(2, 5))
                                energia -= 6
                                print(f"Você perdeu 6 energia{energia}/{energia_max}")
                                break
                elif esc == "2":
                        print("Você deu um migue e fugiu...")
                        energia -= 6
                        print(f"Você perdeu 6 energia{energia}/{energia_max}")
                        break
                else:
                        print("Escolha inválida...")
### eventos floresta
def lobo():
                time.sleep(1)
                print("Em sua caminhada, um lobo solitário surge da mata e tenta te atacar\n ")
                time.sleep(1)
                combate("Lobo", 20, range(17, 23), 10)
                if vida > 0:
                        coletar_recurso("Carne Magra", 3)

def goblin():
        lista = list(inventario.keys())
        if len(lista) > 0:
                item = random.choice(lista)
        if len(lista) == 0:
                coisa = "Sua mochila"
        else:
                coisa = f"{item} de seu inventario"
        print(f"Enquanto voce anda em um campo aberto, um goblin casual tenta roubar {coisa}\n")
        time.sleep(1)
        combate("Globin", 17, range(12, 23), 8)

        if vida > 0:
                coletar_recurso("Adaga", 1)
                if random.randint(1, 2) == 1:
                    coletar_recurso("Maça", random.randint(1, 3))

        if random.randint(1, 4) == 4 and len(lista)>0:
                inventario[item]["quantidade"] -= 1
                if inventario[item]["quantidade"] == 0:
                        del inventario[item]
                exibir_mochila()
                print(f"O goblin morreu... mas {item} dessapareceu! para onde foi?")

def macieira():
        tamanho = random.choice(["pequena", "media", "grande"])
        if tamanho == "pequena":
                macas = 4
        elif tamanho == "media":
                macas = 6
        else:
                macas = 8

        print(f"Voce achou uma macieira {tamanho}")
        coletar_recurso("Maça", macas)

def lenhador():
        print("Você acaba encontrando um lenhador cortando arvores perto de uma cabana...")
        time.sleep(0.7)
        print("-Epa, neném!")
        time.sleep(0.5)
        esc = input("-Quanto tempo que nao vejo alguem!.. por acasso vc nao gostaria de comprar estas carnes gordas? apenas 2 ferros cada!(S/N)")
        if esc.upper() == "S": 
                carnes = int(input("-Quantas?"))
                ferros = carnes * 2

                if inventario.get("Ferro", {}).get("quantidade", 0) < ferros:
                        print("Voce nao tem os ferros necessarios...")
                        print("-nao aceito fiado! vaza daqui buti")
                        return
                else:
                        inventario["Ferro"]["quantidade"] -= ferros
                        if inventario["Ferro"]["quantidade"] == 0:
                                del inventario["Ferro"]
                        coletar_auto("Carne Gorda", carnes)
                        exibir_mochila()
        else:
                print("ok... até mais!")

def javali():
        global energia
        print("Você avista de longe um javali grande e gordo aparentemente perdido...")
        time.sleep(1)
        while True:
                esc = input("O que devo fazer?\n1 - atacar\n2 - ignorar\n: ")
                if esc == "1":
                        print("Você se aproxima e tenta atacar.")
                        combate("Javali", 28, range(15, 25), 15)
                        if vida > 0:
                                coletar_recurso("Carne Gorda", 4)
                        break
                elif esc == "2":
                        energia -= 6
                        limitar_status
                        print(f"Você se afastou sem ser percebido\nvocê perdeu {N_LARANJA}6 energia{RESET} pela caminhada{N_LARANJA}({energia}/{energia_max}){RESET}")
                        break
                else:
                        print("Escolha inválida...")


#eventos rio
def slime():
        print("Enquanto você caminhava perto do rio, um slime normal bem aguado se aproxima..")
        combate("Slime", 5, range(10, 15), 2)
        time.sleep(1)
        print("Espera.. há mais um levemente maior deles..")
        combate("Slime", 10, range(12, 17), 2)
        time.sleep(1.5)
        print("Na verdade tem MUITOS deles!!")
        combate("Montanha Pegajosa", 50, range(24, 28), 15)
        if vida > 0:
                coletar_recurso("Poção de Cura pequena", 3)


def troca():
        global energia, energia_max, vida, vida_max, dano, defesa
        print("Ao caminhar perto ao rio, você acaba escutando uma voz estranha vindo de mais a frente.")
        time.sleep(1)
        while True:
                esc = input("O que devo fazer?\n1 - Seguir a voz\n2 - ignorar\n:")
                if esc == "1":
                        print("Você avança e vê um gogumelo falante cantando algo...")
                        time.sleep(1)
                        esc = input(f"Gogumelo - Todo {classe} tem um principio acertivo para seguir como base, tal será usada em prol de sua alma em cada batalha, mesmo pessoas com dignidade fraca como você.\nqual a sua se tornará?\n1 - Minha vitalidade.\n2 - Meu combustivel.\n3 - Minha luxuria.\n: ")
                        if esc == "1":
                                vida_max += 5
                                vida += 5
                                energia_max -=5
                                energia -= 5
                                dano -=2
                                defesa +=2
                                print("seu corpo ascende ao céu...")
                        elif esc == "2":
                                vida_max -= 5
                                vida -= 5
                                energia_max +=5
                                energia += 5
                                dano +=2
                                defesa -=2
                                print("seu corpo ascende a terra...")
                        elif esc == "3":
                                vida_max -= 5
                                vida -= 5
                                energia_max -=5
                                energia -= 5
                                dano -=2
                                defesa -=2
                                print("você sonha com prazeres...")

                        time.sleep(0.5)
                        print("Você desmaiou...")
                        time.sleep(3)
                        print("\nVocê acordou se sentindo diferente. O que será?")
                        energia -= 8
                        print(f"\n você perdeu {N_LARANJA}8 energia{RESET}\n{energia}/{energia_max}")

                if esc == "2":
                        print("Você desvia para longe...")
                        energia -= 8
                        print(f"\n você perdeu {N_LARANJA}8 energia{RESET}\n{energia}/{energia_max}")


#eventos montanha
def golem():
        print("Ao andar pelas rochas monte acima, de repente, algumas rochas se juntam e formam um golem enorme.\nele nâo parece estar muito contente em te ver...\n")
        while True:
                esc = input("O que fazer?\n1 - lutar\n2 - Oferecer pedras para o acalmar")
                if esc == "1":
                        combate("Golem", 100, range(20, 40), 50)
                        if vida > 0:
                                coletar_recurso("Pedra", 40)
                                coletar_recurso("Ferro", 10)
                                coletar_recurso("Obsidiana", 3)
                        break
                elif esc == "2":
                        if "Pedra" in inventario:
                                del inventario["Pedra"]
                                print("Golem apenas esmagou suas pedras...")
                        else:
                                print("Você nem pedras tinha...")
                        combate("Golem", 100, range(20, 40), 50)
                        if vida > 0:
                                coletar_recurso("Pedra", 40)
                                coletar_recurso("Ferro", 10)
                                coletar_recurso("Obsidiana", 3)  
#                              
def ver_ficha():
    print(f"\n ======== Ficha De Aventureiro ==========\n | Nome: {jogador} | Classe: {classe} | Biotipo: {biotipo} |\n | {N_AZUL}dano: {dano}{RESET} | {N_AZUL}defesa: {defesa}{RESET} | {N_VERMELHO}Vida: {vida}/{vida_max}{RESET} | {N_LARANJA}Energia: {energia}/{energia_max}{RESET} |\n | {rank_cor}Level: {level}({rank_texto}){RESET} | {N_AMARELO}XP: {xp}/10{RESET} | {N_AMARELO}Bônus XP: {bonus_xp}{RESET} | \n | Arma: {arma_atual} (+{dano_arma} dano) | Armadura: {armadura_atual} (+{defesa_armadura} defesa) | Equipamento: {equipamento_atual} (+ {dano_equipamento} dano/ {defesa_equipamento}) defesa | \n | Batalhas: {batalhas}\n ========================================")
    time.sleep(2)


def combate(inimigo, vida_inimigo, dano_inimigo, qtd_xp):
        global vida, vida_perdida,  jogador, rodada, energia, defesa_armadura, dano_arma, batalhas

        print(f"\033[100m\033[97m--- {jogador.upper()} VS {inimigo.upper()} ---\033[0m")

        while vida_inimigo > 0:
                print(f"-- Rodada {rodada} --")
                print(f"Vida {inimigo}:{vida_inimigo}\n")
                time.sleep(1)

                #inimigo
                ataque = random.choice(["s", "n", "s"])
                if ataque == "s":
                        defesa_atual = defesa + defesa_armadura
                        dano_inimigo_atual = random.choice(dano_inimigo) - defesa_atual
                        if dano_inimigo_atual < 0:
                                dano_inimigo_atual = 0
                        vida -= dano_inimigo_atual
                        limitar_status()

                        print(f"{inimigo} te acertou\n Você perdeu {dano_inimigo_atual} de vida . ({vida}/{vida_max})\n")

                        #se jogador morrer
                if vida <= 0:
                        return

                else:
                        print(f"Inimigo errou!\n")

                time.sleep(2)

                #jogador        
                ataque = random.choice(["s", "n", "s", "s"])
                if ataque == "s":
                        dano_atual = dano + dano_arma
                        vida_inimigo -= dano_atual
                        print(f"Você causou {dano_atual} de dano em {inimigo}\n")
                else:
                        print(f"Você errou!\n")
                time.sleep(0.5)
                rodada += 1
        print(f"{jogador} derrotou {inimigo}.")
        time.sleep(1)

        ganhar_xp(qtd_xp)

        energia -= 20
        limitar_status()
        print(f"Batalha encerada. {N_LARANJA}-20 energia{RESET}")
        batalhas += 1

        #

def ganhar_xp(q_xp):
        global xp, level, dano, defesa, vida_max, vida, energia_max, energia, rank, nivel_inv
        print(f"\nVocê ganhou {N_AMARELO}{q_xp} XP{RESET}")
        xp = q_xp + xp + bonus_xp
        while xp >= 10:
                level += 1
                xp -= 10

                dano += 1
                defesa += 1
                vida_max += 1
                vida += 1
                energia_max += 5
                energia += 5        

                if level % 5 == 0:
                        nivel_inv += 1        

                limitar_status()
                verificar_level()

                print(f"\n{N_VERDE}Você subiu de Nivel! (atributos melhorados) {RESET}")

def verificar_level():
    global level, rank_cor, rank_texto       

    if level < 5:
        rank_cor = N_VERDE
        rank_texto = "Iniciante"
    elif level < 10:       
        rank_cor = N_AMARELO
        rank_texto = "Butzinho"
    elif level < 20: 
        rank_cor = N_AZUL
        rank_texto = "Padrão"
    elif level < 35:       
        rank_cor = N_ROXO
        rank_texto = "Experiente"
    elif level < 100:      
        rank_cor = N_VERMELHO
        rank_texto = "Profissional"
    else:                  
        rank_cor = F_PRETO
        rank_texto = "ADMIN" 


def limitar_status():
        global vida, energia
        if vida > vida_max:
                vida = vida_max
        if energia > energia_max:
                energia = energia_max
        if energia <= 20:
                vida -= 10
                print("Você esta super cansado e com fome! (-10 vida)")
        if energia <= 0:
                vida = 0
                print("Você morreu da ataque cardiaco!")

#
def inventario_menu():
        exibir_mochila()

        while True:
                #
                acao = input("""
                1 - Criar/Ver lista de criações
                2 - Usar Item
                3 - Jogar item fora
                4 - sair
                : """)

        #
                if acao == "1":
                        criar()
                if acao == "2":
                        usar_item()
                if acao == "3":
                        tirar_item()
                if acao == "4":
                        break

def usar_item():
        global armadura_atual, arma_atual, vida, defesa, energia, dano, dano_arma, defesa_armadura
        lista_nomes = list(inventario.keys())

        if not lista_nomes:
                print("Seu inventario esta vazio!")
                return

        exibir_mochila()

        num = int(input("Numero do item: "))       
        i = num - 1

        if i < 0 or i > len(lista_nomes) - 1:
                print("\n*Item inexistente*")
                return

        nome_item = lista_nomes[i]
        dados_item = inventario[nome_item]

        if dados_item["tipo"] != "arma" and dados_item["tipo"] != "armadura" and dados_item["tipo"] != "material":
                qtd = int(input("Quantidade: "))
                usar = input(f"Você quer usar: {qtd} {nome_item}?(S/N): ")
        else:
                usar = input(f"Você quer usar: {nome_item}?(S/N): ")
                qtd = 1

        if dados_item["tipo"] == "arma" and usar.upper() == "S":
                if nome_item == arma_atual:
                        print("Você ja está usando este item...")
                        return
                else:
                        if arma_atual != "nenhuma":
                                coletar_auto(arma_atual, 1)
                                print(f"{nome_item} voltou ao inventario.")
                        arma_atual = nome_item
                        dano_arma = dados_item["dano"]
                        print(f"{C_VERDE}Você equipou {nome_item} (+{dano_arma} dano){RESET}")

        elif dados_item["tipo"] == "cura" and usar.upper() == "S":
                vida += dados_item['cura']
                print(f"{C_VERDE}Você usou {nome_item} (+{dados_item['cura']} vida)({vida}/{vida_max}){RESET}")

        elif dados_item["tipo"] == "armadura" and usar.upper() == "S":
                if nome_item == arma_atual:
                        print("Você ja está usando este item...")
                        return
                else:
                        if armadura_atual != "nenhuma":
                                coletar_auto(arma_atual, 1)
                                print(f"{nome_item} voltou ao inventario.")
                        armadura_atual = nome_item
                        defesa_armadura = dados_item['defesa']
                        print(f"{C_VERDE}Você equipou {nome_item} (+ {defesa_armadura} defesa){RESET}")

        elif dados_item["tipo"] == "equipamento" and usar.upper() == "S":
                if nome_item == equipamento_atual:
                        print("Você ja está usando este item...")
                        return
                else:
                        if equipamento_atual != "nenhuma":
                                coletar_auto(equipamento_atual, 1)
                                print(f"{nome_item} voltou ao inventario.")
                        equipamento_atual = nome_item
                        if dados_item['defesa']:
                                defesa_equipamento += dados_item['defesa']
                                dano_equipamento = 0
                                print(f"{C_VERDE}Você equipou {nome_item} (+ {defesa_equipamento} defesa bonus){RESET}")
                        elif dados_item['dano']:
                                dano_equipamento += dados_item['dano']
                                defesa_equipamento = 0
                                print(f"{C_VERDE}Você equipou {nome_item} (+ {dano_equipamento} dano bonus){RESET}")

        elif dados_item["tipo"] == "comida" and usar.upper() == "S":
                energia += dados_item['energia']
                print(f"{C_VERDE}Você comeu {nome_item} (+{dados_item['energia']} energia)({energia}/{energia_max}){RESET}")

        elif dados_item["tipo"] == "material" and usar.upper() == "S":
                        print("Você não pode usar/equipar um material")
                        return

        if inventario[nome_item]['quantidade'] >= qtd:
                inventario[nome_item]['quantidade'] -= qtd
        else:
                print(f"{C_VERMELHO}Você não tem {qtd} {nome_item} para ser usado...{RESET}")
                return

        if inventario[nome_item]['quantidade'] == 0:
                del inventario[nome_item]
        print(f"{qtd} {nome_item} foi tirado do inventario")
        exibir_mochila()        
        limitar_status()


def exibir_mochila():
    global qtd_livre
    capacidade = nivel_inv * 2 + 3
    if capacidade > 30:
            capacidade = 30
    n = 1
    qtd = len(inventario.keys())
    qtd_livre = capacidade - qtd

    print(f"==== Mochila Nível {nivel_inv} ====\n")

    for item in inventario:
        quantidade = inventario[item]["quantidade"]
        tipo = inventario[item]["tipo"]

        print(f"| Item {n}: {item} | Qtd: {quantidade} | Tipo: {tipo}")
        n += 1

    print("| item * | **** | **** | **** | **** |\n" * qtd_livre)
    print(f"==== Capacidade ({qtd}/{capacidade})====")


def tirar_item():
        lista_nomes = list(inventario.keys())

        if not lista_nomes:
                print("Seu inventario esta vazio!")
                return

        escolha = int(input("Numero do item: "))        
        i = escolha - 1

        if i < 0 or i > len(lista_nomes) - 1:
                print("\n*Item inexistente*")
                return

        nome_item = lista_nomes[i]
        del inventario[nome_item]

        print(f"{N_VERMELHO}{nome_item} desapareceu do inventario. {RESET}")

        exibir_mochila()

#

def coletar_recurso(item, quantidade):
    global nivel_inv, capacidade
    exibir_mochila()
    if qtd_livre == 0:
        print(f"Seu inventario esta cheio!\nVocê nao conseguio coletar {quantidade} {item}")
        return

    escolha = input(f"Você achou {quantidade} {item}! deseja coletar para a mochila?(S/N): ")

    if escolha.upper() == "S":
        if item in inventario:
            inventario[item]["quantidade"] += quantidade
        else:
            inventario[item] = banco_de_itens[item].copy()
            inventario[item]['quantidade'] = quantidade

        print(f"\nVocê coletou {item}!")
        exibir_mochila()

def coletar_auto(item, quantidade):
    global nivel_inv, capacidade
    exibir_mochila()
    if qtd_livre == 0:
        print(f"Seu inventario esta cheio!\nVocê nao conseguio coletar {quantidade} {item}")
        return

    if item in inventario:
        inventario[item]["quantidade"] += quantidade
    else:
        inventario[item] = banco_de_itens[item].copy()
        inventario[item]['quantidade'] = quantidade

        print(f"\nVocê coletou {quantidade} {item}!")
        exibir_mochila()


def ver_criacoes():
        n = 1
        for item in receitas:
                materiais = receitas[item]
                print(f"\n={n}=\n{item} :\n{materiais}")
                n += 1
#

def criar():
        ver_criacoes()
        receitas_lista = list(receitas.keys())
        i = int(input("Qual item você gostaria de criar?(0 p/ voltar)\n:")) - 1

        if i == -1:
            print("\n")
            return
        if i < 0 or i >= len(receitas_lista):
                print('\nReceita invalida')
                return
        
                
        receita = receitas_lista[i]
        material = receitas[receita]

        # verificar se tem os recursos necessários
        faltando = {}
        for mat, qtd_necessaria in material.items():
                qtd_atual = inventario.get(mat, {}).get("quantidade", 0)
                if qtd_atual < qtd_necessaria:
                        faltando[mat] = qtd_necessaria - qtd_atual

        if faltando:
                print(f"\n{N_VERMELHO}Você não tem os materiais necessários!{RESET}")
                for mat, qtd in faltando.items():
                        print(f" - Faltam {qtd}x {mat}")
                return

        # ver do espaco
        exibir_mochila()
        if receita not in inventario and qtd_livre == 0:
                print(f"{N_VERMELHO}Sua mochila está cheia! Não há espaço para {receita}.{RESET}")
                return

        # tirar materiais
        for mat, qtd_necessaria in material.items():
                inventario[mat]["quantidade"] -= qtd_necessaria
                if inventario[mat]["quantidade"] == 0:
                        del inventario[mat]

        # adicionar item criado
        qtd_criada = banco_de_itens[receita]["quantidade"]
        if receita in inventario:
                inventario[receita]["quantidade"] += qtd_criada
        else:
                inventario[receita] = banco_de_itens[receita].copy()

        print(f"\n{N_VERDE}Você criou {receita}!{RESET}")

        exibir_mochila()


def pegar_recursos():
        acao = input("""
        ==:
        1 - Coletar itens do chão
        2 - Quebrar Árvores
        3 - Mineirar
        4 - voltar
        ==: """)

        if acao == "1":
                coleta()
        elif acao == "2":
                coleta_arvores()
        elif acao == "3":
                coleta_mina()
        elif acao =="4":
                return
        else:
                print("Acão inexistente...")
                return

#
def coleta():
        global energia
        item1 = random.choice(["Pedra", "Sipó", "Graveto", "Pano", "Cogumelo Amanita muscaria", "Cogumelo Champignon"])
        item2 = random.choice(["Madeira", "Pedra", "Sipó", "Graveto", "Pano", "Cogumelo Amanita muscaria", "Cogumelo Champignon"])
        qtd1 = random.randint(1, 5)
        qtd2 = random.randint(1, 5)

        if random.randint(1, 6) == 6:
                print("\nVc não achou nada")
        else:
                coletar_auto(item1, qtd1)
                coletar_auto(item2, qtd2)

                if item1 == item2:
                        print("Você achou {qtd1 + qtd2} {item1}.")
                else:
                        print(f"\nVocê achou {qtd1} {item1} e {qtd2} {item2}\n")
        energia -= 15

        print(f"Voce gastou {N_LARANJA}15 energia{RESET}({energia}/{energia_max})")
        limitar_status()
#
def coleta_arvores():
        vida_arvore = random.randint(60, 180)
        qtd_madeiras = random.randint(10, 20)
        
        combate("Árvore", vida_arvore, [0, 1, 2])
        coletar_auto("Madeira", qtd_madeiras)
#
def coleta_mina():
        global energia
        qtd_pedra = random.randint(5, 12)

        if random.randint(1, 4) == 4:
                print("Vc não achou nada")
        else:
                item = random.choice(["Ferro", "Diamante", "Obsidiana"])
                qtd = random.randint(1, 5)

                coletar_auto(item, qtd)
                coletar_auto("Pedra", qtd_pedra)

        energia -= 20
        print(f"Voce gastou {N_LARANJA}20 energia{RESET}({energia}/{energia_max})")
        limitar_status()

# inicio
print(f"{F_BRANCO}{C_PRETO} ==BARRIGA OVERPOWER==\n\torigens{RESET}")
input("\nPressione enter para jogar\n")

# historia
ver_historia = input("Deseja ver a História inicial? (S/N): ")

if ver_historia.lower() == "s":
    historia()        

# jogo
cadastro()
while vida > 0:
    acoes()

print(f"\n{F_VERMELHO}{C_BRANCO} === Fim de Jogo === {RESET}\n")
print("Atributos conquistados:\n")
ver_ficha()
