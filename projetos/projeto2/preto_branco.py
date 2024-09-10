from PIL import Image
import os
def preto_branco():
    greyscale_path = "greyscale_imgs"
    # Caso pasta de arquivos comprimidos não exista, será criada
    if greyscale_path not in os.listdir():
        os.mkdir(greyscale_path)

    files_path = '../fotos'

    # lista arquivos de imagem jpg apenas
    files = [i for i in os.listdir(files_path) if 'jpg' in i]

    for file in files:
        # Obtenção do caminho do arquivo atual
        file_path = os.path.join(files_path, file)
        # Criação do caminho para o arquivo atual em preto e branco
        new_path = os.path.join(greyscale_path, file)

        #Abertura da imagem e conversão em preto e branco (parâmetro 'L')
        image = Image.open(file_path).convert('L')
        image.save(new_path, "JPEG")

    print("Imagens convertidas em P&B com sucesso na pasta 'greyscale_imgs'.")

preto_branco()