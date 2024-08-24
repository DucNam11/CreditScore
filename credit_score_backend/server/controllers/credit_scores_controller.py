
from flask import Flask, abort, jsonify

from server.controllers import CREDIT_SCORE_DATA


def get_client_credit_score(client_id):  # noqa: E501
    """Get credit score of a client by ID

    Returns a single credit score # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: CreditScore
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in CREDIT_SCORE_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = CREDIT_SCORE_DATA[CREDIT_SCORE_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)


def get_clients_credit_score():  # noqa: E501
    """Get the credit scores of all clients

    Returns all clients' credit score # noqa: E501

    :rtype: CreditScores
    """
    return CREDIT_SCORE_DATA.to_json(orient="records")
