# redash_api.py
import os
import requests

# Configuration using environment variables for better security
API_KEY = os.getenv('REDASH_API_KEY')
BASE_URL = 'https://redash.yourcompany.com'

def fetch_query_results(query_id):
    """Fetch the results of a specific query using the Redash API."""
    headers = {'Authorization': f'Key {API_KEY}'}
    url = f'{BASE_URL}/api/queries/{query_id}/results'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['query_result']['data']['rows']
    else:
        print("Failed to fetch query results:", response.status_code)
        return None
