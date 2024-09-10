from PIL import Image
import os


def marca_dagua():
    watermark_path = 'watermark_imgs'
    watermarked_imgs_path = 'watermarked_imgs'
    watermark = Image.open(os.path.join(watermark_path, 'watermark.png'))

    if watermarked_imgs_path not in os.listdir():
        os.mkdir(watermarked_imgs_path)

    #Obtenção dos valores da largura e altura da marca dágua
    width_w, heigth_w = watermark.size

    #Obtenção do caminho para as fotos originais
    files_path = '../fotos'

    # lista arquivos de imagem jpg apenas
    files = [i for i in os.listdir(files_path) if 'jpg' in i]

    for file in files:
        # Obtenção do caminho do arquivo atual
        file_path = os.path.join(files_path, file)
        # Criação do caminho para o arquivo atual com marca dágua
        new_path = os.path.join(watermarked_imgs_path, file)

        #Obtenção dos valores de largura e altura da imagem
        image = Image.open(file_path)
        w, h = image.size

        #Posicionamento da marca a uns 20% do final da imagem
        base_width = int(0.2 * w)
        #Obtenção do percentual de alteração da largura da logomarca para encaixar na posição
        w_percent = base_width / float(width_w)
        #Novo valor de altura para manter proporção da imagem da logomarca
        h_size = int(heigth_w * w_percent)

        #Redimensionamento da logomarca para posicionamento correto
        watermark = watermark.resize((base_width, h_size))

        #Tupla com posicionamento por meio das novas dimensões da logomarca;
        # tupla: diferença larguras = posição x; diferença alturas = posição y
        # necessário colocar a máscara de encaixe (terceiro parâmetro) para colocação correta da logo
        image.paste(watermark, (w - base_width, h - h_size), watermark)
        image.save(new_path, 'JPEG')


marca_dagua()
