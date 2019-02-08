# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["강력한 채찍", "당근", "도움말"]
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"강력한 채찍":
        dataSend = {
            "message": {
                "text": "벌써 침대에 드러누웠어?"
            }
        }
    elif content == u"당근":
        dataSend = {
            "message": {
                "text": "http://thediversitytimes.ca/2017/08/09/august-%EC%9C%84%EB%8C%80%ED%95%9C-%EA%B2%8C%EC%B8%A0%EB%B9%84/"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "이러이러한 챗봇이야, 이렇게 사용하렴^^"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "반가워"
            }
        }
    elif u"힘들" in content:
        dataSend = {
            "message": {
                "text": "배부른 소리 하는구나.."
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "그런 헛소리를 할때가 아니야.."
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
