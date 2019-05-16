import os

from flask import abort, Flask, jsonify, request

from virgil_crypto import VirgilCrypto
import sys


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form['token'] == 'IP4seaOAjBd4DxlcDyGPpCar'
    is_team_id_valid = request.form['team_id'] == 'THZUV8F9Q'

    return is_token_valid and is_team_id_valid


@app.route('/e2ee', methods=['GET','POST'])
def e2ee():
    message_to_encrypt = request.form['text']
    if not is_request_valid(request):
        abort(400)

    crypto = VirgilCrypto()
    key_pair = crypto.generate_keys()
    private_key = key_pair.private_key
    public_key = key_pair.public_key


    data_to_encrypt = message_to_encrypt.encode()

    reciver_list = [public_key]
    encrypted_data = str(crypto.encrypt(data_to_encrypt, *reciver_list))
    return jsonify(
        response_type='in_channel',
        text=encrypted_data,
        replace_original= True,
        delete_original=True,
    )
