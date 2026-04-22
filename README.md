# 🔮 Duelo dos Elementos (Python + Turtle Graphics)

Este repositório contém um jogo de estratégia elemental desenvolvido em Python. O projeto foi criado para explorar conceitos de **Programação Orientada a Eventos** e **Interface Gráfica de Usuário (GUI)**, saindo do terminal convencional para uma experiência visual interativa.

## 🎯 Objetivo do Projeto
O objetivo foi desenvolver um sistema de "Pedra-Papel-Tesoura" expandido, onde o usuário interage com elementos gráficos na tela para duelar contra uma Inteligência Artificial (o Guardião).

## 🛠️ Tecnologias e Conceitos Aplicados
* **Linguagem**: Python 3.
* **Biblioteca Turtle**: Utilizada para a renderização da interface, desenho de botões e captura de eventos de clique (mouse).
* **Biblioteca Random**: Aplicada para gerar a imprevisibilidade nas jogadas do computador (O Guardião).
* **Dicionários**: Estruturas de dados utilizadas para gerenciar a lógica de dominância (quem vence quem) e o mapeamento de cores/elementos.
* **UX/UI**: Implementação de delays controlados (`time.sleep`) para simular o "pensamento" da máquina e melhorar a imersão do jogador.

## 🚀 Funcionalidades
* **Interatividade via Clique**: O jogador escolhe seu elemento clicando diretamente nos botões coloridos na tela.
* **Sistema de Placar**: Monitoramento em tempo real de vitórias e derrotas.
* **Feedback Dinâmico**: Mensagens personalizadas que indicam o status de cada rodada (Vitória, Derrota ou Empate).
* **Botão Sair**: Encerramento limpo da aplicação através da interface gráfica.

## 📂 Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Execute o arquivo principal:
   ```bash
   python Elementos.py