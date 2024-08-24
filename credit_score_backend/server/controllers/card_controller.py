from flask import Flask, abort, jsonify
from server.controllers import SAVED_CARD_DATA


def get_client_card_info(client_id):  # noqa: E501
    """Get a client's card information by ID

    Returns a single client's card information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: CardInformation
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_CARD_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = SAVED_CARD_DATA[SAVED_CARD_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)


def get_clients_card_info():  # noqa: E501
    """Get all clients' card information

    Returns card information for all clients # noqa: E501

    :rtype: MultipleCardInformation
    """
    return SAVED_CARD_DATA.to_json(orient="records")