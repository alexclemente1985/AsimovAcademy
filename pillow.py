from PIL import Image
from pathlib import Path

def pillow():
    imagem = Image.open(Path.joinpath(Path.cwd(), 'imgs','image.jpg'))
    imagem.show()
    print('formato da imagem')
    print(imagem.format)
    print('Modo de imagem')
    print(imagem.mode)
    print('tamanho, largura e altura: ', imagem.size, imagem.width, imagem.height)
    print('Informação da imagem: ', imagem.info)

    #Redimensionamento da imagem:
    im1 = imagem.resize(size=(200,500))
    imagem.show()

    #Corte da imagem
    im2 = imagem.crop((0,0,100,300))
    if not Path.joinpath(Path.cwd(), 'imgs', 'saves').exists():
        Path.mkdir(Path.joinpath(Path.cwd(), 'imgs', 'saves'))

    im1.save(Path.joinpath(Path.cwd(), 'imgs','saves',"imagem_save1_resize.jpg"))
    im2.save(Path.joinpath(Path.cwd(), 'imgs','saves',"imagem_save2_crop.jpg"))

    #Transposição de imagens
    im3 = imagem.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    im3.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    im3.save(Path.joinpath(Path.cwd(), 'imgs','saves',"imagem_save3_flip.jpg"))

    #Criação de thumbnails de imagem
    im3.thumbnail((90,90))

pillow()