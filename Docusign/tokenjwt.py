'''
Gerando um Token JWT da DocuSign com Python: Um Guia Completo
A obtenção de um JSON Web Token (JWT) é um passo fundamental para a autenticação em integrações de serviço com a API da DocuSign, permitindo que sua aplicação atue em nome de um usuário de forma segura. Este guia detalha o processo para gerar esse token utilizando a linguagem de programação Python, abordando os pré-requisitos, o fluxo de autenticação e um exemplo de código prático.

Pré-requisitos Essenciais
Antes de iniciar o desenvolvimento, é crucial que você tenha as seguintes informações e configurações em sua conta de desenvolvedor da DocuSign:

Chave de Integração (Client ID): Um identificador único para a sua aplicação.

ID do Usuário (User ID): O GUID do usuário que a sua aplicação irá personificar.

Par de Chaves RSA: Uma chave privada, que será usada para assinar o JWT, e uma chave pública, que será registrada na DocuSign.

Concessão de Consentimento: O usuário a ser personificado deve conceder permissão para que a sua aplicação atue em seu nome. Este é um passo único, geralmente realizado através de uma URL de consentimento.

Endpoint de Autenticação: O endereço do servidor de autenticação da DocuSign (diferente para ambientes de desenvolvimento e produção).

O Fluxo de Autenticação JWT Grant
A DocuSign utiliza o fluxo de concessão de JWT (JWT Grant) do padrão OAuth 2.0 para este tipo de autenticação. O processo, em alto nível, consiste em:

Construção do JWT: Sua aplicação cria um JWT contendo um conjunto de "claims" (informações) como o emissor (sua chave de integração), o "assunto" (o ID do usuário a ser personificado), o público (o endpoint de autenticação), e as datas de emissão e expiração.

Assinatura do JWT: O JWT é assinado utilizando a sua chave privada RSA com o algoritmo RS256.

Troca pelo Token de Acesso: O JWT assinado é enviado para o endpoint de token da DocuSign através de uma requisição POST.

Recebimento do Token de Acesso: Se o JWT for válido e o consentimento tiver sido concedido, a DocuSign retorna um token de acesso. Este token será utilizado no cabeçalho de autorização (Authorization: Bearer SEU_TOKEN_DE_ACESSO) em todas as chamadas subsequentes à API da DocuSign.

Implementação em Python
Para facilitar a interação com a API da DocuSign, é altamente recomendável utilizar a biblioteca oficial docusign-esign. Caso ainda não a tenha instalada, utilize o pip:
pip install docusign-esign
A seguir, um exemplo de código que demonstra como obter o token de acesso:

Observações Importantes:

Segurança da Chave Privada: Mantenha sua chave privada em um local seguro e nunca a exponha no código-fonte do lado do cliente.

Gerenciamento do Token: O token de acesso tem uma validade limitada (geralmente uma hora). Sua aplicação deve ser capaz de detectar a expiração do token e solicitar um novo quando necessário.

Escopos: O escopo (scope) define as permissões que sua aplicação está solicitando. signature e impersonation são comuns para a API de eSignature.

Ambientes: Lembre-se de utilizar a authorization_server correta para o ambiente que você está utilizando (desenvolvimento ou produção).

Ao seguir estas diretrizes e utilizar o código de exemplo como ponto de partida, você estará apto a gerar tokens JWT e se autenticar com sucesso na API da DocuSign, abrindo um leque de possibilidades para a automação de seus fluxos de trabalho de assinatura de documentos.

'''
#pip install docusign-esign
#pip install PyJWT
#pip install requests

import jwt
import time
import requests

# --- Configurações ---
# Substitua pelos seus dados de produção ou desenvolvimento
DS_JWT = {
    "ds_client_id": "08027d3c-4795-4818-a0d7-0e748804c48b",  # Sua Chave de Integração (Client ID)
    # O ID do usuário que você deseja personificar (User ID)
    "ds_impersonated_user_id": "5d6a430e-1b51-461f-bd7c-96d05188d6a5",
    
    "private_key_file": "/workspaces/python/Docusign/chaveprivada.pem",
    "authorization_server": "account-d.docusign.com"  # Para ambiente de desenvolvimento, use "account.docusign.com" para produção
}

import pandas as pd
#df = pd.read_csv('/workspaces/python/Docusign/chaveprivada.pem', sep='-')
df =  pd.read_csv ('/workspaces/python/Docusign/CLIC_ATUALIZA_DIA_ELEK.csv', sep='|')
#df = pd.read_csv ('/workspaces/python/Replica/CLIC_ATUALIZA_DIA_ELEK.csv', sep='|')
print (df.head(5))

def get_docusign_jwt_token():
    """
    Constrói e assina um JWT para obter um token de acesso da DocuSign.
    """
    try:
        with open(DS_JWT["private_key_file"], "r") as key_file:
            private_key = key_file.read()

        iat = int(time.time())
        exp = iat + 3600  # O token de acesso expira em 1 hora

        payload = {
            "iss": DS_JWT["ds_client_id"],
            "sub": DS_JWT["ds_impersonated_user_id"],
            "iat": iat,
            "exp": exp,
            "aud": DS_JWT["authorization_server"],
            "scope": "signature impersonation"
        }

        # Gera o token JWT
        jwt_token = jwt.encode(
            payload,
            private_key,
            algorithm="RS256"
        )

        # Troca o JWT por um token de acesso
        token_url = f"https://{DS_JWT['authorization_server']}/oauth/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": jwt_token
        }

        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()  # Lança uma exceção para respostas de erro

        return response.json()["access_token"]

    except FileNotFoundError:
        return "Erro: O arquivo da chave privada não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# --- Exemplo de uso ---
'''
if __name__ == "__main__":
    access_token = get_docusign_jwt_token()
    if "Erro" not in access_token:
        print("Token de Acesso obtido com sucesso:")
        print(access_token)
    else:
        print(access_token)

    '''