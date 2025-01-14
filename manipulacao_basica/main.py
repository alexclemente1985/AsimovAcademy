import pypdf
from pathlib import Path

def manipulacao_basica():
    caminho_pdf = Path.joinpath(Path(__file__).parents[1],'documentos','dom_casmurro.pdf')

    #Leitura de pdf
    leitor_pdf = pypdf.PdfReader(caminho_pdf)

    print("Leitor PDF: ")
    print(leitor_pdf,'\n')

    print("## Exibição das páginas ##")
    print(leitor_pdf.pages,'\n')

    print("## Exibição de página específica ##")
    print(leitor_pdf.pages[0],'\n')

    print("## Exibição de metadados ##")
    print(leitor_pdf.metadata)
    print(leitor_pdf.metadata.author)
    print(leitor_pdf.metadata.creation_date,'\n')


    #Extração de páginas do pdf

    caminho_pdf_2 = Path.joinpath(Path(__file__).parents[1],'documentos','vpt_minecraft.pdf')

    leitor_pdf_2 = pypdf.PdfReader(caminho_pdf_2)

    pagina_4 = leitor_pdf_2.pages[3]

    escritor_pdf = pypdf.PdfWriter()
    escritor_pdf.add_page(pagina_4)

    new_file_path = Path.joinpath(Path(__file__).parent,'documentos_gerados','vpt_minecraft_pg4.pdf')

    # Maneira do professor (usar direto o .write com caminho do arquivo)
    #escritor_pdf.write(new_file_path)

    with open(new_file_path, 'wb') as new_file:
        escritor_pdf.write(new_file)

    # Inserindo mais páginas (da página 0 até a 2 -> as três primeiras páginas)
    new_file_path_2 = Path.joinpath(Path(__file__).parent,'documentos_gerados','vpt_minecraft_pg1-3.pdf')
    ## limpeza do escritor para reutilização
    escritor_pdf.remove_page(0,clean=True)

    for pagina in leitor_pdf_2.pages[:3]:
        escritor_pdf.add_page(pagina)

    with open(new_file_path_2, 'wb') as new_file:
        escritor_pdf.write(new_file)

    escritor_pdf.close()

    ## Inserindo páginas em ordem inversa
    new_file_path_3 = Path.joinpath(Path(__file__).parent,'documentos_gerados','vpt_minecraft_inv_pages.pdf')

    escritor_pdf = pypdf.PdfWriter()

    for pagina in leitor_pdf_2.pages[3:0:-1]:
        escritor_pdf.add_page(pagina)

    with open(new_file_path_3, 'wb') as new_file:
        escritor_pdf.write(new_file)

    escritor_pdf.close()

    # Concatenando arquivos

    escritor_pdf = pypdf.PdfWriter()

    for pagina in leitor_pdf.pages[:3]:
        escritor_pdf.add_page(pagina)
    for pagina in leitor_pdf_2.pages[:3]:
        escritor_pdf.add_page(pagina)

    new_file_path_4 = Path.joinpath(Path(__file__).parent,'documentos_gerados','vpt_minecraft_combinacao.pdf')

    with open(new_file_path_4, 'wb') as new_file:
        escritor_pdf.write(new_file)

    escritor_pdf.close()

    # Obtenção de páginas específicas de arquivos diferentes
    escritor_pdf = pypdf.PdfWriter()
    caminhos = [caminho_pdf, caminho_pdf_2]
    leitores_pdf = [pypdf.PdfReader(caminho) for caminho in caminhos]

    indices = [1,3,8]

    for index in indices:
        for leitor in leitores_pdf:
            pagina = leitor.pages[index]
            escritor_pdf.add_page(pagina)

    new_file_path_5 = Path.joinpath(Path(__file__).parent,'documentos_gerados','vpt_minecraft_paginas_idx.pdf')

    with open(new_file_path_5, 'wb') as new_file:
        escritor_pdf.write(new_file)
    escritor_pdf.close()



manipulacao_basica()