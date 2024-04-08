from flask import Flask, request, jsonify
from model import model_

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process_json():
        data = request.get_json()
        print(f'{type(data)=}')
        if 'Задача en' in data and 'Обстановка en' in data and 'Оптимальный план en' in data and 'Предсказанный план' in data:
            result = your_function(data)

            return jsonify({'status': str(result)})
        else:
            return jsonify({'error': 'Недостаточно данных. Пожалуйста, укажите все 4 ключа.'}), 400

def your_function(data):
    return model_.predict(data)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
