import requests

def search(query):
    api_key = r"AIzaSyCYg9S4-9LnUD2d5JMkliZMLHYN55_N3RM" 
    search_engine_id = r"47b0bb1432361489d"  # Replace with your actual search engine ID

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"

    response = requests.get(url)
    data = response.json()

    filtered_results = []
    for item in data["items"]:
      if item["kind"] == "customsearch#result":
        metatags = item["pagemap"]["metatags"][0]
        filtered_result = { # TODO: Need to use more filters for better parsing
          "og:image": metatags.get("og:image", None),
          # "og:height": int(metatags.get("og:height", 0)),
          # "og:width": int(metatags.get("og:width", 0)),
          "og:title": metatags.get("og:title", ""),
          #"og:type": metatags["og:type"],
        }
        if metatags.get("og:url"):
          filtered_result["og:url"] = metatags["og:url"]
        filtered_results.append(filtered_result)
        
    return filtered_results

# TODO: Download the images and store them in a appropriate folder
# TODO: Use the images to train the model and predict the correct image based on the prompt
