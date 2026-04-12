import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from pathlib import Path

BASE_URL = "https://www.google.com/search?q="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
OUTPUT_PATH = Path(__file__).resolve().parent / "latlong.csv"

def get_coordinates(sector):
    search_term = f"sector {sector} gurgaon latitude and longitude"
    try:
        response = requests.get(BASE_URL + search_term, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')   # type: ignore 
            # Google often changes this class; if it fails, we return "Not Found"
            coordinates_div = soup.find("div", class_="Z0LcW") 
            return coordinates_div.text if coordinates_div else "Not Found"
    except Exception as e:
        return f"Error: {e}"
    return "Not Found"

# 1. Use a list to collect data (Much faster than appending to a DataFrame)
results = []

for sector in range(1, 116):
    print(f"Scraping Sector {sector}...")
    coordinates = get_coordinates(sector)
    results.append({"Sector": f"Sector {sector}", "Coordinates": coordinates})
    
    # 2. Add a tiny delay so Google doesn't block your IP
    time.sleep(1.5) 

# 3. Create the DataFrame all at once at the end
df = pd.DataFrame(results)

# Save results
df.to_csv(OUTPUT_PATH, index=False)
print("Done! Data saved to latlong.csv'")
