import requests

def fetch_photo(query):
    # Replace with your actual Unsplash Access Key
    access_key = 'ya1qVTdp_TKvLQ5XeaNteHVtcFSgNZj7pHm0q7pYTfg'

    url = 'https://api.unsplash.com/search/photos'
    headers = {
        'Authorization': f'Client-ID {access_key}',
    }

    params = {
        'query': query,
        'per_page': 1,
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            photos = data.get('results', [])
            if photos:
                src_original_url = photos[0]['urls']['full']
                return src_original_url
            else:
                print("No photos found for the given query.")
        elif response.status_code == 403:
            print("Error 403: Forbidden - Check your API key or rate limits.")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    return None

# Example usage of the function
query = 'AI'
src_original_url = fetch_photo(query)
if src_original_url:
    print(f"Original URL for query '{query}': {src_original_url}")
else:
    print("Failed to fetch the image.")
