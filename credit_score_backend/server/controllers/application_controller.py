

from flask import Flask, abort, jsonify

from server.controllers import SAVED_APP_DATA



def get_client_app_info(client_id):  # noqa: E501
    """Get a client's banking information by ID

    Returns a single client's banking information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: ApplicationInformation
    """
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_APP_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    client_data = SAVED_APP_DATA[SAVED_APP_DATA["SK_ID_CURR"] == client_id].to_json(orient="records")
    return jsonify(client_data)

def get_clients_app_info():  # noqa: E501
    """Get all clients' banking information

    Returns banking information for all clients # noqa: E501

    :rtype: MultipleApplicationInformation
    """
    return SAVED_APP_DATA.to_json(orient="records")

print(get_clients_app_info)