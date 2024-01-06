import requests

def google_search(query, api_key, cse_id, **kwargs):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id
    }
    params.update(kwargs)
    response = requests.get(search_url, params=params)
    return response.json()

def save_results_to_file(results, filename="search_results.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in results.get('items', []):
            file.write(f"Title: {item['title']}\n")
            file.write(f"Snippet: {item['snippet']}\n")
            file.write(f"Link: {item['link']}\n")
            file.write("\n")

api_key = "YOUR APİ KEY"
cse_id = "YOUR CSE ID"

# Burada arama sorgusuna istediğiniz telefon numarasını yazın
search_results = google_search(" +901111111111", api_key, cse_id, num=5)
save_results_to_file(search_results)
