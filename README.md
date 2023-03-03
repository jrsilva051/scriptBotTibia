# Script Bot para Tibia

  Este projeto foi desenvolvido utilizando linguagem python, utilizando para realizar algumas funções no jogo de rgp Tibia.
  O script é customizável possuindo uma dicionário de configurações para que o jogador possa adequar ao seu personagem.
  As funções são executadas em threads separadas para garantir que todas as funções sejam executadas ao mesmo tempo sem interferir umas nas outras.

### Curar vida e mana do personagem
- Utilizando a biblioteca Pyautogui, o script realiza screenshots da tela em duas regiões diferente, posteriormente utilizada a biblioteca Open CV (cv2) para processar as imagens.
    Para realizar a leitura dos textos contidos nas imagens, utilizei o software Tesseract OCR e aplico as regras utilizando as configurações customizadas.
    As ações no jogo são realizadas utilizado o método hotkey da biblioteca Pyautogui e os tempos de exaustão do personagem é controlado através da biblioteca time.
 
### Manter o personagem logado
-  O personagem se mantem logado através de movimentos realizados pelo método hotkey da biblioteca Pyautogui a cada 4 minutos e meio.
  
### Garante que o personagem se alimente
- Este controle é feito utilizando as bibliotecas Pyautogui e time, realizando a ação a cada 1 minuto.

### Tecnologias utilizadas
- Python - (https://www.anaconda.com/products/distribution)
- Tesseract OCR - (https://github.com/tesseract-ocr/tesseract)
- Open CV - (https://pypi.org/project/opencv-python)
- Numpy - (https://numpy.org/)
- Pyautogui - (https://pyautogui.readthedocs.io)
- Threading - (https://docs.python.org/3/library/threading.html)
