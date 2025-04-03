import google.generativeai as palm
from audiorecognition.apikey import apikey
palm.configure(api_key=apikey)
import pprint
for model in palm.list_models():
    pprint.pprint(model)
