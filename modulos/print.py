import json
import time
from loguru import logger
from pyautogui import *
from datetime import datetime
    
class PrintContacts():
    def __init__(self):
        screenshot_region = self._get_screenshot_region()
        self.screenshot_region = screenshot_region
        pass

    def _get_screenshot_region(self):
        with open('configuracoes.json') as f:
            self.data = json.load(f)
            screenshot_region = (self.data["left"], self.data["top"], self.data["width"], self.data["height"])
        return screenshot_region

    def localiza_e_foca_pesquisa(self) -> None | str:
        IMAGEM = 'pesquisa.png'
        try:
            pos_pesquisa = locateOnScreen(IMAGEM, confidence=0.6, grayscale=1)
        except ImageNotFoundException:
            logger.error(f"Ocorreu um erro ao tentar localizar a imagem.")            
        if pos_pesquisa != None:
            pos_pesquisa = (pos_pesquisa.left.__int__(),
                            pos_pesquisa.top.__int__(),
                            pos_pesquisa.width.__int__(),
                            pos_pesquisa.height.__int__())
            pos_x = pos_pesquisa[0]+ (pos_pesquisa[2]/2)
            pos_y = pos_pesquisa[1]+(pos_pesquisa[3]/2)
            moveTo(pos_x, pos_y, duration=0.5)
            click()
            press("tab", presses=3, interval=0.2)
            return
        return "Não foi possível localizar a barra de pesquisa."

    def print(self, title:str = ""):
        """Print the contacts screen with the resolution passed to the class
        """
        title = self.data["group_name"] if title == "" else title
        tempo_inicial = time.time()
        self.localiza_e_foca_pesquisa()
        moveRel(500)
        i = 1
        tentativas = 0
        while True:
            date = str(datetime.now()).replace(":","")
            filename = f"./Pendente/{title}_{i}_{date}.png"
            i += 1
            screen1 = screenshot(imageFilename=filename, region=self.screenshot_region)
            press('pgdn')
            sleep(0.8)
            screen2 = screenshot(imageFilename=filename, region=self.screenshot_region)
            if screen1 == screen2:
                if tentativas > 3:
                    logger.info("Finalizado")
                    tentativas = 0
                    tempo_final = time.time()
                    duracao = tempo_final - tempo_inicial
                    logger.info(f"Duração {duracao} segundos")

                    break
                self.localiza_e_foca_pesquisa()
                logger.warning(f"Imagem semelhante à anterior")
                logger.debug(f"Tentativa: {tentativas}")
                tentativas += 1
                continue