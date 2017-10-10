#-*- coding: utf8 -*-
import requests
from flask.ext.babel import gettext
from config import MS_TRANSLATOR_CLIENT_SECRET
from xml.etree import ElementTree
from json import dumps


def microsoft_translate(text, sourceLang, destLang):
    if MS_TRANSLATOR_CLIENT_SECRET == "":
        return gettext('Error: translation service not configured.')
    try:
        # get access token
        translateUrl = 'https://api.microsofttranslator.com/v2/http.svc/Translate'
        cognitiveServiceUrl = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        requestHeader = {'Ocp-Apim-Subscription-Key': MS_TRANSLATOR_CLIENT_SECRET}
        responseResult = requests.post(cognitiveServiceUrl, headers=requestHeader)
        token = responseResult.text

        # translate
        params = {
            'appId': 'Bearer ' + token,
            'text': text.encode('utf-8'),
            'from': sourceLang,
            'to': destLang
        }
        requestHeader = {'Accept': 'application/xml'}
        responseResult = requests.get(translateUrl, params=params, headers=requestHeader )
        response = ElementTree.fromstring(responseResult.text.encode('utf-8')).text
        response = dumps("{\"response\":" + response +"}")
        print(response)
        return response
    except:
       return gettext('Error: Unexpected error.')

