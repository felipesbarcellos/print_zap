from dotenv import load_dotenv
from google import genai
import glob
import shutil
import os
from loguru import logger

def run() -> None:
    load_dotenv()

    GEMINI_KEY = os.environ.get("GEMINI_KEY")
    client = genai.Client(api_key=GEMINI_KEY)

    image_list = []

    for file in glob.glob('Pendente/*.png'):
        myfile = client.files.upload(file=file)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[myfile, "Para cada usuário nas image, pegue o número dele e me retorne uma lista. Se houver apenas o nome e o número não constar, ignore. Quero apenas um texto com a lista de números"],
        )
        
        with open("output.txt",  mode="a", encoding="utf-8")  as f:
            f.write(response.text+"\n")
            
        shutil.move(file, f'./Tratado')

        logger.debug(response.text)

if __name__ == "__main__":
    run()

