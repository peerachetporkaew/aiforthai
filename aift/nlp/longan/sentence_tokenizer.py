import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def tokenize(text:str, pos:str=False, ner:str=False, sent:str=True, 
            sep:str='|', tag_sep:str='/', return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = 'https://api.aiforthai.in.th/longan/senttoken'
    payload = {'text':text, 'pos':pos, 'ner': ner, 'sent': sent, 'sep': sep, 'tag_sep': tag_sep}

    res = requests.post(url, data=payload, headers=headers)

    if return_json == False:
        return res.json()['result']
    else:
        return res.json()