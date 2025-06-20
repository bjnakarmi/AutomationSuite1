import requests
from utils.config import CONFIG


def get_all_pending_owner(header):
    endpoint = 'api/stateOwner/getAll'
    params = {
        'page' : 1,
        'limit' : 2,
        'offset' : 0,
        'isPending': True,
        'countryId' : 5
    }
    response = requests.get(CONFIG['base_api'] + endpoint, params = params, headers=header)
    return response
