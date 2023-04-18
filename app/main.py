from flask import Flask, jsonify, request
from services.uf_service import UfService

app = Flask(__name__)


@app.route('/ufs', methods=['GET'])
def get_ufs():
    year = request.args.get('year')
    month = request.args.get('month')

    if not year or not month:
        return jsonify(
            {'error': 'Year and month parameters are required'}
            ), 400

    uf_service = UfService()
    ufs = uf_service.get_ufs(year, month)

    return jsonify({'ufs': ufs}), 200


if __name__ == '__main__':
    app.run(debug=True)
