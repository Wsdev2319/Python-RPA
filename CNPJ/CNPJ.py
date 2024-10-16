import http.client
import json
import pandas as pd

def obter_cnpj(cnpj):
    conexao = http.client.HTTPConnection("www.receitaws.com.br")
    conexao.request("GET", f'/v1/cnpj/{ cnpj }')
    resposta = conexao.getresponse()
    dados = resposta.read()
    empresa = json.loads(dados.decode('utf-8'))
    conexao.close()
    
    if empresa.get('status','') == 'ERRO':
        return empresa.get('message', 'ERRO desconhecido.')
    else:
        return empresa
    
    
cnpj_exemplo = "331573312000162" 
   
dados_empresa = obter_cnpj(cnpj_exemplo)
print(dados_empresa)