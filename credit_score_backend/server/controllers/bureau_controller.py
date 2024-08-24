from flask import Flask, abort, jsonify
from server.controllers import SAVED_BUREAU_DATA


def get_client_bureau_info(client_id):  # noqa: E501
    """Get a client's bureau information by ID

    Returns a single client's bureau information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: BureauInformation
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_BUREAU_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = SAVED_BUREAU_DATA[SAVED_BUREAU_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)


def get_clients_bureau_info():  # noqa: E501
    """Get all clients' bureau information

    Returns bureau information for all clients # noqa: E501

    :rtype: MultipleBureauInformation
    """
    return SAVED_BUREAU_DATA.to_json(orient="records")