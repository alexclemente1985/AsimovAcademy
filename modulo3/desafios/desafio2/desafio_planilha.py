from pathlib import Path

import pandas as pd

#Desafio: criar uma pasta com planilhas exclusivas para cada estado, a partir das abas da planilha clientes.xlsx
def desafio_planilha():
    main_sheet = Path.joinpath(Path.cwd().parents[1], 'arquivos_mod3','clientes.xlsx')
    export_folder = Path.joinpath(Path.cwd(), 'exportacoes')

    if not main_sheet.exists():
        print("Planilha original não encontrada...")
        return

    '''
    df_rs = pd.read_excel(main_sheet, sheet_name="RS")
    df_sc = pd.read_excel(main_sheet, sheet_name="SC")
    df_pr = pd.read_excel(main_sheet, sheet_name="PR")
    df_sp = pd.read_excel(main_sheet, sheet_name="SP")
    '''

    #Obtenção de todas as abas -> sheet_name=None
    df_main_dict = pd.read_excel(main_sheet, sheet_name=None)

    if not export_folder.exists():
        Path.mkdir(export_folder)

    '''
    df_rs.to_excel(Path.joinpath(export_folder, 'RS_.xlsx'), index=False, sheet_name="RS")
    df_sc.to_excel(Path.joinpath(export_folder, 'SC_.xlsx'), index=False, sheet_name="SC")
    df_pr.to_excel(Path.joinpath(export_folder, 'PR_.xlsx'), index=False, sheet_name="PR")
    df_sp.to_excel(Path.joinpath(export_folder, 'SP_.xlsx'), index=False, sheet_name="SP")
    '''

    for nome_aba, tabela in df_main_dict.items():
        tabela.to_excel(Path.joinpath(export_folder,f'{nome_aba}.xlsx'), index=False, sheet_name=nome_aba)

    clients_folder = Path.joinpath(export_folder, 'clients')
    if not clients_folder.exists():
        Path.mkdir(clients_folder)

    with pd.ExcelWriter(Path.joinpath(clients_folder, 'clientes_consolidada.xlsx')) as consol:
        for arquivo in export_folder.glob("*.xlsx"):
            tabela_dict = pd.read_excel(arquivo, sheet_name=None)
            for aba, tab in tabela_dict.items():
                tab.to_excel(consol, sheet_name=aba, index=False)

    '''
    #Solução Professor
    with pd.ExcelWriter(Path.joinpath(clients_folder, 'clientes_consolidada.xlsx')) as consol:
        for arquivo in export_folder.glob("*.xlsx"):
            tabela = pd.read_excel(arquivo)
            #.stem -> obtem o nome do arquivo sem o sufixo .xlsx
            tabela.to_excel(consol, sheet_name=arquivo.stem, index=False)
    '''

desafio_planilha()