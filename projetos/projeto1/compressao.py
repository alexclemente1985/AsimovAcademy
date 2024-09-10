from PIL import Image
import os


def compressao():
    reduct_fact = 0.5
    compressed_path = "compressed_imgs"

    # Caso pasta de arquivos comprimidos não exista, será criada
    if compressed_path not in os.listdir():
        os.mkdir(compressed_path)

    files_path = 'fotos'

    # lista arquivos de imagem jpg apenas
    files = [i for i in os.listdir(files_path) if 'jpg' in i]

    # Para fins de informação no final do processo de compressão
    size_before = 0
    size_after = 0

    for file in files:
        # Obtenção do caminho do arquivo atual
        file_path = os.path.join(files_path, file)
        # Criação do caminho para o arquivo atual comprimido
        new_path = os.path.join(compressed_path, file)

        # Somatório dos tamanhos originais de cada arquivo, feito a cada iteração
        size_before += os.stat(file_path).st_size

        img = Image.open(file_path)
        # Aplicação do fator de redução para redução proporcional de largura e altura da imagem
        new_width = int(reduct_fact * img.size[0])
        new_height = int(reduct_fact * img.size[1])

        # Redução da imagem com o mínimo de distorção
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img.save(new_path, 'JPEG', optimize=True, quality=90)

        #Somatório dos valores de tamanho após a compressão, a cada iteração
        file_stats = os.stat(new_path)
        size_after += file_stats.st_size

    #Tamanhos estão em bytes e tem que serem convertidos em Mb (tamanho/(1024*1024))

    #Variação absoluta dos tamanhos, em Mb
    diff = (size_before - size_after) / (1024 * 1024)
    #Variação percentual dos tamanhos
    perc = (diff / (size_before / (1024 * 1024))) * 100
    #Valores de tamanho antes e depois, em Mb
    size_before_mb = size_before / (1024 * 1024)
    size_after_mb = size_after / (1024 * 1024)

    print(f"Tamanho anterior (Mb): {size_before_mb} | Tamanho após compressão (Mb): {size_after_mb}")
    print("Diferença na redução (Mb): ", diff)
    print(f"Redução percentual dos arquivos: {round(perc, 2)}%")


compressao()
