############################################################################################################
## Autor: B3SA
############################################################################################################

##
from ast import Str
from typing import Any
import requests
import json
import base64
import pandas as pd
import sys
sys.path.append('../')
import Decript
import FuncoesEngenhariaSoftware as FES

from fortifyapi.fortify import FortifyApi

############################################################################################################
## Autenticacao resultado em token e sessao 
############################################################################################################


# Nome de usu rio e senha para autentica  o
username = auditCreds.split('\n')[0].replace('\n' , '').strip()
password = auditCreds.split('\n')[1].replace('\n' , '').strip()

# Codificando as credenciais em base64
creds = f'{username}:{password}'
creds_encoded = base64.b64encode(creds.encode('ascii')).decode('ascii')

# Cabe alho da solicita  o, incluindo a autentica  o b sica
headers = {
    'Authorization': 'Basic ' + creds_encoded,
    'Content-Type': 'application/json'
}