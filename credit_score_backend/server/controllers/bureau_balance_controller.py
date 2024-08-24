
from flask import Flask, abort, jsonify

from server.controllers import SAVED_BUREAU_BALANCE_DATA


def get_client_bureau_balance_info(client_id):  # noqa: E501
    """Get a client's bureau balance information by ID

    Returns a single client's bureau balance information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: BureauBalanceInformation
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_BUREAU_BALANCE_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = SAVED_BUREAU_BALANCE_DATA[SAVED_BUREAU_BALANCE_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)

def get_clients_bureau_balance_info():  # noqa: E501
    """Get all clients' bureau balance information

    Returns bureau balance information for all clients # noqa: E501

    :rtype: MultipleBureauBalanceInformation
    """
    return SAVED_BUREAU_BALANCE_DATA.to_json(orient="records")