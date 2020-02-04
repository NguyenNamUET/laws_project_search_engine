import os

# coding: utf-8


# folder_input_path
folder_output_path = os.environ.get('folder_output_path', '/mydata')

ES_IP = os.environ.get('ES_IP', 'elasticsearch')
ES_USER = os.environ.get('ES_USER', 'user')
ES_PASS = os.environ.get('ES_PASS', '12345678')
ES_PORT = os.environ.get('ES_PORT', '9200')

minimum_should_match_for_search = "100"