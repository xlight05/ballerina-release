import os
from json import dumps

from httplib2 import Http

import constants


def send_message(message):
    build_chat_id = os.environ[constants.ENV_BALLERINA_BUILD_CHAT_ID]
    build_chat_key = os.environ[constants.ENV_BALLERINA_BUILD_CHAT_KEY]
    build_chat_token = os.environ[constants.ENV_BALLERINA_BUILD_CHAT_TOKEN]

    url = 'https://chat.googleapis.com/v1/spaces/' + build_chat_id + \
          '/messages?key=' + build_chat_key + '&token=' + build_chat_token
    bot_message = {
        'text': message}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
