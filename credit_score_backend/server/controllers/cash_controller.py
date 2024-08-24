
from flask import Flask, abort, jsonify
from server.controllers import SAVED_CASH_DATA


def get_client_cash_info(client_id):  # noqa: E501
    """Get a client's cash information by ID

    Returns a single client's cash information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: CashInformation
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_CASH_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = SAVED_CASH_DATA[SAVED_CASH_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)


def get_clients_cash_info():  # noqa: E501
    """Get all clients' cash information

    Returns cash information for all clients # noqa: E501

    :rtype: MultipleCashInformation
    """
    return SAVED_CASH_DATA.to_json(orient="records")