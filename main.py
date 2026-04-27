from scripts.scraper import scrape_data
from scripts.transform import transform_data
from scripts.load import load_data

all_data = []

for page in range(1,51):
    print(f"scraping pages:{page}")
    data = scrape_data(page)
    all_data.extend(data)


df = transform_data(all_data)
load_data(df)
print(f"Total_data: {len(df)}")
