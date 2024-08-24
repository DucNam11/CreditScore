from flask import Flask, abort, jsonify
from server.controllers import SAVED_INSTALLMENTS_DATA

def get_client_installment_info(client_id):  # noqa: E501
    """Get a client's installment information by ID

    Returns a single client's installment information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: InstallmentInformation
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_INSTALLMENTS_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = SAVED_INSTALLMENTS_DATA[SAVED_INSTALLMENTS_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)

def get_clients_installment_info():  # noqa: E501
    """Get all clients' installment information

    Returns installment information for all clients # noqa: E501

    :rtype: MultipleInstallmentInformation
    """
    return jsonify(SAVED_INSTALLMENTS_DATA.to_json(orient="records"))