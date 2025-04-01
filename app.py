from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

charadas = [
    {'id': 1, 'pergunta': 'O que é, o que é? Cai em pé e corre deitado.', 'resposta': 'Chuva'},
    {'id': 2, 'pergunta': 'O que é, o que é? Tem cabeça, tem dente, tem barba, não é gente e fala como a gente.', 'resposta': 'Alho'},
    {'id': 3, 'pergunta': 'O que é, o que é? Quanto mais se tira, maior fica.', 'resposta': 'Buraco'},
    {'id': 4, 'pergunta': 'O que é, o que é? Feito para andar e não anda.', 'resposta': 'Rua.'},
    {'id': 5, 'pergunta': ' O que é, o que é? Dá muitas voltas e não sai do lugar.', 'resposta': 'Relógio'},
    {'id': 6, 'pergunta': 'O que é, o que é? Tem 5 dedos, mas não tem unha', 'resposta': 'Luva'},
    {'id': 7, 'pergunta': '. O que é, o que é? Pode passar diante do sol sem fazer sombra.', 'resposta': 'Vento'},
    {'id': 8, 'pergunta': 'O que é, o que é? Nasce a socos e morre a facadas.', 'resposta': 'Pão'},
    {'id': 9, 'pergunta': 'O que é, o que é? Subindo o sol vai se encurtando, descendo o sol vai se alongando.', 'resposta': 'Sombra'},
    {'id': 10, 'pergunta': '  O que é, o que é? Quanto maior menos se vê.', 'resposta': 'Escuridão'}
]

@app.route('/')
def index():
    return 'API TÁ ON'

@app.route('/charadas', methods=['GET'])
def charada_aleatoria():
    charada = random.choice(charadas)
    return jsonify(charada), 200

@app.route('/charadas/<campo>/<busca>', methods=['GET'])
def busca(campo, busca):
    if campo not in ['id', 'pergunta', 'resposta']:
        return jsonify({'erro': 'campo inválido'}), 404
    
    if campo == 'id':
        busca = int(busca)

    for charada in charadas:
        if charada[campo] == busca:
            return jsonify(charada), 200
    else:
        return jsonify({'erro': 'não encontrado'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)