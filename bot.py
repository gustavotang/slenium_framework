from botcity.web import BotCityAgent
import time
import random

class MyAgent(BotCityAgent):
    def __init__(self):
        super().__init__()

    def action(self, *args, **kwargs):
        self.log("Iniciando a ação do agente.")

        # Exemplo de interação com um elemento da página
        self.click_button("id_do_botao")
        self.log("Botão clicado.")

        # Exemplo de preenchimento de formulário
        self.fill_text_field("id_do_campo", "Texto de exemplo")
        self.log("Campo de texto preenchido.")

        # Exemplo de espera
        self.wait(2)

        # Exemplo de movimento do mouse
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        self.move_mouse(x, y)
        self.log(f"Mouse movido para a posição ({x}, {y}).")

        # Exemplo de captura de tela
        self.take_screenshot("screenshot_exemplo.png")
        self.log("Captura de tela realizada.")

        self.log("Ação do agente finalizada.")
        return super().action(*args, **kwargs)

if __name__ == "__main__":
    agent = MyAgent()
    agent.start()