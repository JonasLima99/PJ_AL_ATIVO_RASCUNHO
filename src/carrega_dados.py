import pandas as pd
import gspread 

credenciais_filename = "credenciais.json"

idAlunosAtivos = "190NUZo4_28W--0J9dyTOUdAwjuLi7dIqaFgwtrLRNM4"
index = 0

def carrega_dados_brutos():
    
    gc = gspread.service_account(filename=credenciais_filename)

    planilhaCompleta = gc.open_by_key(idAlunosAtivos)
    planilha = planilhaCompleta.get_worksheet(index)
    dados = planilha.get_all_records()

    df = pd.DataFrame(dados)

    #Criando cópia local
    df.to_csv('dados brutos.csv', index=False, encoding='utf-8')

    print('Dados carregados com sucesso')

    return df

print(carrega_dados_brutos())