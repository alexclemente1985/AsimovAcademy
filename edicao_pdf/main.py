import pypdf
from pathlib import Path

def edicao_pdf():
    caminho_pdf = Path.joinpath(Path(__file__).parents[1],'documentos','vpt_minecraft.pdf')
    documentos = Path.joinpath(Path(__file__).parent,'documentos_gerados')

    leitor_pdf = pypdf.PdfReader(caminho_pdf)
    escritor_pdf = pypdf.PdfWriter() 

    for pagina in leitor_pdf.pages:
        pg_rot = pagina.rotate(90)
        escritor_pdf.add_page(pg_rot)

    if not documentos.exists():
        documentos.mkdir() 

    novo_pdf = Path.joinpath(documentos, 'vpt_rotacionado.pdf')

    with open(novo_pdf, 'wb') as pdf:
        escritor_pdf.write(pdf)
    escritor_pdf.close()
    # Usando escritor clonando documento já de início
    
    escritor_pdf_2 = pypdf.PdfWriter(clone_from=caminho_pdf)
    for pagina in escritor_pdf_2.pages:
        pagina.rotate(180)
    
    novo_pdf_2 = Path.joinpath(documentos, 'vpt_rot_clone_writer.pdf')
    
    with open(novo_pdf_2, 'wb') as pdf:
        escritor_pdf_2.write(pdf)
    escritor_pdf_2.close()

    # Usando Transformation (mais opções de rotação)
        
    transform = pypdf.Transformation().rotate(45)
    escritor_pdf_3 = pypdf.PdfWriter(clone_from=caminho_pdf)

    for pagina in escritor_pdf_3.pages:
        pagina.add_transformation(transform)
    
    novo_pdf_3 = Path.joinpath(documentos, 'vpt_rot_transform_45.pdf')
    
    with open(novo_pdf_3, 'wb') as pdf:
        escritor_pdf_3.write(pdf)
    escritor_pdf_3.close()

    # Usando Translate
    translate = pypdf.Transformation().rotate(30).translate(tx=100)
    escritor_pdf_4 = pypdf.PdfWriter(clone_from=caminho_pdf)

    for pagina in escritor_pdf_4.pages:
        pagina.add_transformation(translate)
    
    novo_pdf_4 = Path.joinpath(documentos, 'vpt_rot_transform_30_translx_100.pdf')
    
    with open(novo_pdf_4, 'wb') as pdf:
        escritor_pdf_4.write(pdf)
    
    escritor_pdf_4.close()

    # Redimensionando pdf

    escritor_pdf_5 = pypdf.PdfWriter(clone_from=caminho_pdf)

    for pagina in escritor_pdf_5.pages:
        pagina.scale_by(0.5)
    
    novo_pdf_5 = Path.joinpath(documentos, 'vpt_scale_0_5.pdf')
    
    
    with open(novo_pdf_5, 'wb') as pdf:
        escritor_pdf_5.write(pdf)
    
    escritor_pdf_5.close()

    ## com scale_to

    escritor_pdf_6 = pypdf.PdfWriter(clone_from=caminho_pdf)

    for pagina in escritor_pdf_6.pages:
        pagina.scale_to(pypdf.PaperSize.A8.width, pypdf.PaperSize.A8.height)
    
    novo_pdf_6 = Path.joinpath(documentos, 'vpt_scale_to_A8.pdf')
    
    
    with open(novo_pdf_6, 'wb') as pdf:
        escritor_pdf_6.write(pdf)
    
    escritor_pdf_6.close()

    ## Usando Transformation

    scale = pypdf.Transformation().scale(sx=1.5, sy=0.5)
    escritor_pdf_7 = pypdf.PdfWriter(clone_from=caminho_pdf)

    for pagina in escritor_pdf_7.pages:
        pagina.add_transformation(scale)
    
    novo_pdf_7 = Path.joinpath(documentos, 'vpt_transf_scale_sx_sy.pdf')
    
    with open(novo_pdf_7, 'wb') as pdf:
        escritor_pdf_7.write(pdf)
    
    escritor_pdf_7.close()

    ## Usando o scale para desfazer a alteração anterior

    ### Para refazer, a escala aplicada terá multiplicar com o valor atual e resultar no valor 1 em cada eixo
    #### 1.5 * 0.6666 = 1 | 0.5 * 2 = 1
    scale = pypdf.Transformation().scale(sx=0.6666, sy=2)
    escritor_pdf_8 = pypdf.PdfWriter(clone_from=Path.joinpath(documentos,'vpt_transf_scale_sx_sy.pdf'))

    for pagina in escritor_pdf_8.pages:
        pagina.add_transformation(scale)
    
    novo_pdf_8 = Path.joinpath(documentos, 'vpt_transf_scale_sx_sy_reset.pdf')
    
    with open(novo_pdf_8, 'wb') as pdf:
        escritor_pdf_8.write(pdf)
    
    escritor_pdf_8.close()

    



edicao_pdf()