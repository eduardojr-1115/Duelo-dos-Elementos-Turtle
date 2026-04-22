import turtle
import random
import time

# ==========================================
# 1. SETUP DE DADOS
# ==========================================
elementos = ["Fogo", "Água", "Terra", "Ar"]
cores = {"Fogo": "#FF4500", "Água": "#1E90FF", "Terra": "#8B4513", "Ar": "#F0F8FF"}
dominancia = {"Água": "Fogo", "Terra": "Água", "Ar": "Terra", "Fogo": "Ar"}
placar = {"Jogador": 0, "Guardião": 0}

tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Guardião dos Elementos - Debug Mode")
tela.setup(width=650, height=750)

escritor = turtle.Turtle()
escritor.hideturtle()
escritor.color("white")
escritor.penup()

placar_turtle = turtle.Turtle()
placar_turtle.hideturtle()
placar_turtle.penup()

# ==========================================
# 2. INTERFACE
# ==========================================
botoes = {}

def atualizar_placar():
    placar_turtle.clear()
    placar_turtle.color("white")
    placar_turtle.goto(0, 300)
    placar_turtle.write(f"VOCÊ: {placar['Jogador']}  |  GUARDIÃO: {placar['Guardião']}", 
                        align="center", font=("Arial", 18, "bold"))

def criar_interface():
    posicoes = {"Fogo": (-100, 100), "Água": (100, 100), "Terra": (-100, -100), "Ar": (100, -100)}
    
    for nome in elementos:
        # Primeiro criamos a tartaruga
        t = turtle.Turtle()
        t.penup()
        t.speed(0) # Velocidade máxima de desenho
        t.goto(posicoes[nome])
        
        # Desenha o quadrado
        t.shape("square")
        t.shapesize(5, 5)
        t.color(cores[nome])
        
        # Escreve o nome LOGO APÓS (Sobrepondo)
        # Usamos uma segunda tartaruga só para o texto não sumir
        txt = turtle.Turtle()
        txt.hideturtle()
        txt.penup()
        txt.speed(0)
        txt.goto(posicoes[nome][0], posicoes[nome][1] - 10)
        txt.color("black")
        txt.write(nome, align="center", font=("Arial", 12, "bold"))
        
        botoes[nome] = t

    # Botão Sair
    sair_btn = turtle.Turtle()
    sair_btn.shape("square")
    sair_btn.shapesize(1.5, 4)
    sair_btn.color("#B22222")
    sair_btn.penup()
    sair_btn.goto(230, -320)
    botoes["Sair"] = sair_btn
    
    txt_s = turtle.Turtle()
    txt_s.hideturtle()
    txt_s.penup()
    txt_s.goto(230, -330)
    txt_s.color("white")
    txt_s.write("SAIR", align="center", font=("Arial", 10, "bold"))

    atualizar_placar()

# ==========================================
# 3. LÓGICA DO DUELO
# ==========================================
def duelo_clicado(x, y):
    escolha_jogador = None
    
    if botoes["Sair"].distance(x, y) < 40:
        tela.bye()
        return

    for nome in elementos:
        if botoes[nome].distance(x, y) < 50:
            escolha_jogador = nome
            break
            
    if escolha_jogador:
        escritor.clear()
        escritor.goto(0, 240)
        escritor.write(f"Invocando: {escolha_jogador}...", align="center", font=("Arial", 14, "italic"))
        
        time.sleep(0.5)
        computador = random.choice(elementos)
        
        escritor.goto(0, 200)
        escritor.write(f"Guardião escolheu: {computador}", align="center", font=("Arial", 16, "bold"))
        
        escritor.goto(0, -280)
        if escolha_jogador == computador:
            escritor.color("yellow")
            escritor.write("EMPATE!", align="center", font=("Arial", 22, "bold"))
        elif dominancia[escolha_jogador] == computador:
            escritor.color("#32CD32")
            escritor.write("VITÓRIA!", align="center", font=("Arial", 26, "bold"))
            placar["Jogador"] += 1
        else:
            escritor.color("#DC143C")
            escritor.write("DERROTA...", align="center", font=("Arial", 26, "bold"))
            placar["Guardião"] += 1
        
        escritor.color("white")
        atualizar_placar()

# ==========================================
# 4. START
# ==========================================
criar_interface()
tela.onclick(duelo_clicado)
turtle.done()