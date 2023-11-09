'''
Author: LetMeFly
Date: 2023-11-09 11:20:56
LastEditors: LetMeFly
LastEditTime: 2023-11-09 20:11:05
'''
import json
from os import path, listdir
from urllib.parse import quote
from flask import Flask, send_file

CONFIG = json.loads(open('settings.json', encoding='utf-8').read())
app = Flask(__name__)



def generate1html(data: list) -> str:
    html = '<html><body>'
    for name in data:
        html += f'<a href="{name}/">{name}</a><hr>'
    html += '</body></html>'
    return html


@app.route('/<path:uri>')
def main(uri):
    temp = uri.split('/')
    name = temp[0]
    thispath = CONFIG['folders'][name]
    for i in temp[1:]:
        if i:
            thispath += '/' + i
    if path.isdir(thispath):
        return generate1html(listdir(thispath))
    else:
        return send_file(thispath, quote(path.basename(thispath)), as_attachment=True)



@app.route('/')
def index():
    data = []
    for name, thispath in CONFIG['folders'].items():
        if not path.exists(thispath):
            return f'CONFIG error! \'{name}\' -> \'{thispath}\' not exists'
        data.append(name)
    return generate1html(data)

app.run(host=CONFIG['ip'], port=CONFIG['port'])