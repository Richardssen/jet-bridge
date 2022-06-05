import logging

from jet_bridge.utils.backend import register_token
from jet_bridge.db import Session


def register_token_command():
    try:
        session = Session()
        token, created = register_token(session)

        if not created and token:
            logging.info(f'Token already exists: {token.token}')
        elif not created:
            logging.info('Token creation failed')
        elif token:
            logging.info(f'Token created: {token.token}')
    finally:
        session.close()
