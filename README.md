# PrintContatosWhatsapp
## Sobre
Ferramenta de RPA para tirar Screenshots de listas de contatos de grupos no whatsapp e transformar em lista de números de telefone utilizando o recurso de ORM do Gemini.
## Modo de uso
1. Dê um pull no repositório ou baixe e extraia o arquivo compactado;
2. Certifique-se de ter o python instalado.
3. Instale as dependências do projeto com `pip install -r requirements.txt`
4. Crie um arquivo com o nome .env coloque a sua chave da API do Gemini no formato `GEMINI_KEY="[sua chave]"`; 
5. Coloque a área a ser escaneada e o nome do grupo no arquivo configuracoes.json. Para isso ache a coordenada em pixel da tela onde começa a caixa de contatos em "left" e "top" e coloque a largura e altura da caixa de contatos em "width" e "height" respectivamente (eu usei o GreenShot para fazer isso).
6. Abra a página com os contatos
7. Inicie o programa com `python ./main.py` no terminal
8. Após terminar a raspagem, as screenshots estarão na pasta Pendente;
9. Ainda no terminal digite `python ./gemini.py` para executar o OCR e salvar a lista em output.txt