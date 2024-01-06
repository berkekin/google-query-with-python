# google-query-with-python

EN: This code is a Python script that utilizes Google's Custom Search API to conduct a specific query search and save the obtained results to a file. Here's a breakdown of the code:

Google Search Function (google_search):

This function performs a query search on the internet using Google's Custom Search API.
query: Represents the query to be searched.
api_key: Your personal API key for using Google's API.
cse_id: Your Custom Search Engine ID.
**kwargs: A flexible argument that allows adding additional parameters.
The function returns a response in JSON format from the API.
Save Results to File Function (save_results_to_file):

This function saves the search results returned by google_search to a file.
Results are written to the file with each search result's title (title), snippet (snippet), and link (link).
The file is opened using UTF-8 encoding and saved by default as "search_results.txt".
API Keys and Search Query:

The api_key and cse_id should be replaced with your actual API key and Custom Search Engine ID.
For example, this code snippet searches for the phone number "+901111111111" and returns a maximum of 5 results.
This script is particularly useful for those who want to conduct fast and effective internet searches for specific queries and neatly save these results, such as for quick research on a topic or collecting specific data.




TR: 
Elbette, işte kodunuzun hem İngilizce hem de Türkçe tanıtımı:

İngilizce Tanıtım:
This code is a Python script that utilizes Google's Custom Search API to conduct a specific query search and save the obtained results to a file. Here's a breakdown of the code:

Google Search Function (google_search):

This function performs a query search on the internet using Google's Custom Search API.
query: Represents the query to be searched.
api_key: Your personal API key for using Google's API.
cse_id: Your Custom Search Engine ID.
**kwargs: A flexible argument that allows adding additional parameters.
The function returns a response in JSON format from the API.
Save Results to File Function (save_results_to_file):

This function saves the search results returned by google_search to a file.
Results are written to the file with each search result's title (title), snippet (snippet), and link (link).
The file is opened using UTF-8 encoding and saved by default as "search_results.txt".
API Keys and Search Query:

The api_key and cse_id should be replaced with your actual API key and Custom Search Engine ID.
For example, this code snippet searches for the phone number "+901111111111" and returns a maximum of 5 results.
This script is particularly useful for those who want to conduct fast and effective internet searches for specific queries and neatly save these results, such as for quick research on a topic or collecting specific data.

Türkçe Tanıtım:
Bu kod, Google'ın Özel Arama API'sini kullanarak belirli bir sorgu için internet üzerinde arama yapmayı ve elde edilen sonuçları bir dosyaya kaydetmeyi sağlayan bir Python scriptidir. Kodun ayrıntılı açıklaması şu şekildedir:

Google Arama Fonksiyonu (google_search):

Bu fonksiyon, Google'ın Özel Arama API'si kullanılarak internet üzerinde bir sorgu gerçekleştirir.
query: Aranacak sorguyu temsil eder.
api_key: Google API'sini kullanmak için gerekli kişisel API anahtarınız.
cse_id: Google Özel Arama Motoru ID'nizi belirtir.
**kwargs: Ekstra parametreler eklemenize izin veren esnek bir argümandır.
Fonksiyon, API'dan JSON formatında bir yanıt döndürür.
Sonuçları Dosyaya Kaydetme Fonksiyonu (save_results_to_file):

Bu fonksiyon, google_search tarafından döndürülen arama sonuçlarını bir dosyaya kaydeder.
Sonuçlar, her bir arama sonucunun başlığı (title), özeti (snippet) ve bağlantısı (link) ile birlikte dosyaya yazılır.
Dosya, UTF-8 kodlaması kullanılarak açılır ve varsayılan olarak "search_results.txt" adında bir dosyaya kaydedilir.
API Anahtarları ve Arama Sorgusu:

api_key ve cse_id değerlerinin gerçek API anahtarınız ve Özel Arama Motoru ID'niz ile değiştirilmesi gerekmektedir.
Örneğin, bu kod parçasında "+901111111111" olarak belirtilen telefon numarası için bir arama yapılır ve en fazla 5 sonuç döndürülür.
Bu script, özellikle belirli sorgular için internet üzerinden hızlı ve etkili bir şekilde arama yapmak ve bu sonuçları düzenli bir şekilde kaydetmek isteyenler için kullanışlıdır. Örneğin, belirli bir konu hakkında hızlı bir araştırma yapmak veya belirli verileri toplamak için idealdir.
