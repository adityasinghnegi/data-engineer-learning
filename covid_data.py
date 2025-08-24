import requests
import pandas as pd

# Step 1: Fetch data from API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)  # makes a GET request to the API
data = response.json()        # convert response to Python dictionary/list

# Step 2: Normalize into DataFrame (like a table)
df = pd.json_normalize(data)

# Step 3: Select useful columns only
df = df[["country", "cases", "deaths", "recovered", "active", "tests"]]

# Step 4: Save as CSV
df.to_csv("covid_data.csv", index=False)

print("✅ Data saved to covid_data.csv")
