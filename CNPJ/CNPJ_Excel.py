import http.client
import json
import pandas as pd

def obter_cnpj(cnpj):
    conexao = http.client.HTTPSConnection('www.receitaws.com.br')
    conexao.request('GET', f'/v1/cnpj/{ cnpj }')
    resposta = conexao.getresponse()
    print(f'Status da Reposta HTTP: {resposta.status}')
    
    if resposta.status != 200:
        return {'Status': 'ERROR', 'Message': f"Status da Reposta HTTP: {resposta.status}"}
    dados = resposta.read()
    conexao.close()
    
    try:
        empresa = json.loads(dados.decode('utf-8'))
        print(f'Empresa decodificada:{empresa}')
        return empresa
        
    except json.JSONDecodError as e:
        print(f'Erro na decodificaçao do JSON: {str(e)}')
        return {'status':'ERROR', 'Message': 'Erro na desodificaçao do JSON'}
    
def salvar_excel(dados_empresa, arquivo='dados_empresa.xlsx'):
    if dados_empresa.get('status') != 'ERROR':
        dados_empresa = tratar_dados(dados_empresa)
        
        
        df = pd.DataFrame([dados_empresa])
        df.to_excel(arquivo, index=False)
        print(f'Dados da empresa salvos com sucesso {arquivo}')
        
    else:
        print(f'Não ha dados para salvar. Mensagem de erro:')
        
def tratar_dados(dados):
    
     if'atividade_principal' in dados:
         dados['atividade_principal'] = ';'.join([ativ['text'] for ativ in dados['atividade_principal']])
         
     if'atividades_secundarias' in dados:
         dados['atividades_secundarias'] = ';'.join([ativ['text'] for ativ in dados['atividades_secundarias']])
         
     if 'qsa' in dados:
        dados['qsa'] = ';'.join([f"{q['nome']} {q.get('qual', '')}" for q in dados['qsa']])   
         
     if 'billing' in dados:
        dados['billing'] = str(dados['billing'])
        
     if 'extra' in dados:  
         dados['extra'] = str(dados['extra'])
        
     return dados
    
    

cnpj_exemplo = "33157312000162"
dados_empresa = obter_cnpj(cnpj_exemplo)
salvar_excel(dados_empresa)