import http.client
import json
import pandas as pd

def obter_endereco(cep):
    
    conexao = http.client.HTTPSConnection('viacep.com.br')
    conexao.request("GET", f'/ws/{cep}/json/')
    resposta = conexao.getresponse()
    dados = resposta.read()
    endereco = json.loads(dados.decode('utf-8'))
    conexao.close()
    
    return endereco

def salvar_endereco(endereco, nome_arquivo='endereco.xlsx'):
    
    if 'erro' not in endereco:
        
        df = pd.DataFrame([endereco])
        df.to_excel(nome_arquivo, index=False)
        print(f'Dados salvos com sucesso no arquivo {nome_arquivo}')
    
    else:
        print('Não foi possivel salvar os dados: CEP não encontrado.')
      
    

cep_exemplo = "35365-000"

endereco_resultado = obter_endereco(cep_exemplo)
salvar_endereco(endereco_resultado)

print(endereco_resultado)