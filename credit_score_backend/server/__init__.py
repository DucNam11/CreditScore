from flask import Flask
import os
import logging

# Import các route từ controllers
from server.controllers.application_controller import get_client_app_info, get_clients_app_info
from controllers.bureau_controller import get_client_bureau_info, get_clients_bureau_info
from controllers.bureau_balance_controller import get_client_bureau_balance_info, get_clients_bureau_balance_info
from controllers.card_controller import get_client_card_info, get_clients_card_info
from controllers.cash_controller import get_client_cash_info, get_clients_cash_info
from server.controllers.credit_scores_controller import get_client_credit_score, get_clients_credit_score
from controllers.installments_controller import get_client_installment_info, get_clients_installment_info
from controllers.previous_application_controller import get_client_previous_app_info, get_clients_previous_app_info

# Cấu hình logging
logging.basicConfig(level=logging.DEBUG)

def create_app():
    """Create a Flask application."""
    app = Flask(__name__)

    # Định nghĩa các route
    app.add_url_rule('/client_app/<int:client_id>', 'get_client_app_info', get_client_app_info)
    app.add_url_rule('/clients_app', 'get_clients_app_info', get_clients_app_info)
    app.add_url_rule('/client_bureau/<int:client_id>', 'get_client_bureau_info', get_client_bureau_info)
    app.add_url_rule('/clients_bureau', 'get_clients_bureau_info', get_clients_bureau_info)
    app.add_url_rule('/client_bureau_balance/<int:client_id>', 'get_client_bureau_balance_info', get_client_bureau_balance_info)
    app.add_url_rule('/clients_bureau_balance', 'get_clients_bureau_balance_info', get_clients_bureau_balance_info)
    app.add_url_rule('/client_card/<int:client_id>', 'get_client_card_info', get_client_card_info)
    app.add_url_rule('/clients_card', 'get_clients_card_info', get_clients_card_info)
    app.add_url_rule('/client_cash/<int:client_id>', 'get_client_cash_info', get_client_cash_info)
    app.add_url_rule('/clients_cash', 'get_clients_cash_info', get_clients_cash_info)
    app.add_url_rule('/client_credit_score/<int:client_id>', 'get_client_credit_score', get_client_credit_score)
    app.add_url_rule('/clients_credit_score', 'get_clients_credit_score', get_clients_credit_score)
    app.add_url_rule('/client_installment/<int:client_id>', 'get_client_installment_info', get_client_installment_info)
    app.add_url_rule('/clients_installment', 'get_clients_installment_info', get_clients_installment_info)
    app.add_url_rule('/client_previous_app/<int:client_id>', 'get_client_previous_app_info', get_client_previous_app_info)
    app.add_url_rule('/clients_previous_app', 'get_clients_previous_app_info', get_clients_previous_app_info)
    
    return app

init_app = create_app()