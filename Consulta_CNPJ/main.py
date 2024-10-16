import http.client
import json
import pandas as pd

def limpar_cnpj(cnpj):
    
    return ''.join(filter(str.isdigit, cnpj))

def obter_dados(cnpj):
    
    cnpj = limpar_cnpj(cnpj)
    conexao = http.client.HTTPSConnection('www.receitaws.com.br')
    conexao.request('GEt', f"/v1/cnpj/{cnpj}")
    resposta = conexao.getresponse()
    
    print(f"Processando CNPJ {cnpj}: Status {resposta.status}")
    
    if resposta.status != 200:
        
        conexao.close()
        
        return None
    
    dados = resposta.read()
    conexao.close()
    empresa = json.loads(dados.decode('utf-8'))
    
    if 'status' in empresa and empresa['status'] == 'ERROR':
        print(f"ERRO ao Buscar dados para o CNPJ {cnpj}: {empresa.get('message', 'Sem mensagem de erro')}")
        
        return empresa

def formatar_dados(empresa):
    
    campos_interesse = ['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'atividade_principal']
    
    dados_formatados = {campo: empresa.get(campo, '') for campo in campos_interesse}
    
    if 'atividade_principal' in empresa and empresa['atividade_principal']:
        dados_formatados['atividade_principal'] = empresa['atividade_principal'[0].get('text')]
        
        return dados_formatados

def salvar_dados(resultados,nome_arquivo,nome_aba='Dados'):
    
    with pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        
        try:
            
            worksheet = writer.book[nome_aba]
            start_row = worksheet.max_row
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=True)
            
        except KeyError:
            
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=False, startrow=start_row)
    
caminho_planilha = "CNPJ.xlsx"

try:
    planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name='CNPJ', dtype={'CNPJ': str})
    
except FileNotFoundError:
    print(f"Arquivo {caminho_planilha} não encontrado")

resultados = []

for cnpj in planilha_cnpjs['CNPJ'].dropna():
    
    print(f"Lendo CNPJ: {cnpj}")
    dados_empresa = obter_dados(str(cnpj))
    
    if dados_empresa:
        dados_formatados = formatar_dados(dados_empresa)
        
        resultados.append(dados_formatados)

if resultados:
    
    resultados_df = pd.DataFrame(resultados)
    
    salvar_dados(resultados_df, caminho_planilha)
    
print("Dados das empresa foram salvo na planilha na aba 'Dados'.")