from flask import Flask, jsonify, request
from services.uf_service import UfService

app = Flask(__name__)


@app.route('/ufs', methods=['GET'])
def get_ufs():
    date = request.args.get('date')

    if date is None:
        return jsonify(
            {'error': 'Date parameters are required'}
            ), 400
    try:
        uf_service = UfService()
        ufs = uf_service.get_ufs(date)
    except Exception as e:
        return jsonify({'errors': str(e)}), 400
    return jsonify({'ufs': ufs}), 200


if __name__ == '__main__':
    app.run(debug=True)
