from PIL import Image
from pathlib import Path


def pillow():
    imgpath = Path.joinpath(Path.cwd(), 'imgs')
    imagem = Image.open(Path.joinpath(imgpath, 'image.jpg'))
    imagem.show()
    print('formato da imagem')
    print(imagem.format)
    print('Modo de imagem')
    print(imagem.mode)
    print('tamanho, largura e altura: ', imagem.size, imagem.width, imagem.height)
    print('Informação da imagem: ', imagem.info)

    # Redimensionamento da imagem:
    im1 = imagem.resize(size=(200, 500))
    imagem.show()

    # Corte da imagem
    im2 = imagem.crop((0, 0, 100, 300))
    if not Path.joinpath(imgpath, 'saves').exists():
        Path.mkdir(Path.joinpath(Path.cwd(), 'imgs', 'saves'))

    im1.save(Path.joinpath(Path.cwd(), 'imgs', 'saves', "imagem_save1_resize.jpg"))
    im2.save(Path.joinpath(Path.cwd(), 'imgs', 'saves', "imagem_save2_crop.jpg"))

    # Transposição de imagens
    im3 = imagem.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    im3.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    im3.save(Path.joinpath(imgpath, 'saves', "imagem_save3_flip.jpg"))

    # Criação de thumbnails de imagem
    im3.thumbnail((90, 90))

    # Tratamento de cores
    imagem2 = Image.open(Path.joinpath(imgpath, 'maca.jpg'))
    r, g, b = imagem2.split()

    # RGB - Red Green Blue
    ## Notação de 0-1 ou de 0-255 ou de 00-FF

    imagem3 = Image.merge("RGB", (b, g, r))
    imagem2.show()
    imagem3.show()

    # Jogando uma imagem em cima da outra
    #imagem.paste(imagem2)
    imagem.paste(imagem2, (400,300))

    imagem.show()


pillow()
