import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL template (assuming year and drawing number are placeholders)
base_url = "https://www.walottery.com/winningnumbers/PastDrawings.aspx?gamename=dailykeno&unittype=year&unitcount={year}"

# Define start and end years (inclusive)
start_year = 1992
end_year = 1996  # Update with the current year

# Initialize empty list to store data
data = []

# Loop through years
for year in range(start_year, end_year + 1):
    # Loop through drawing numbers (logic might need adjustment based on website structure)
    #for drawing_number in range(1, 366):  # Adjust range for daily drawings
        url = base_url.format(year=year)
        print(url)

        # Make HTTP request
        response = requests.get(url)

        # Check for successful response
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            #print(soup)

            # Extract data from HTML (adjust selectors based on website structure)
            table = soup.find("div", class_="columns-container tables-container")  # Assuming date is in a span with class "Date"
            table_header=table.findAll("table",class_="table-viewport-large")
            for tab in table_header:
              date=tab.find("h2").text
              print(date)
              winning_numbers = [num.text for num in tab.find_all("td", class_="game-balls")]  # Assuming winning numbers are in divs with class "winning-number"

            # Append data to list
              data.append({
                    "Date": date,
                    "Winning Numbers": winning_numbers
                })
        else:
            print(f"Error fetching data for {url}")

# Create pandas DataFrame from data
df = pd.DataFrame(data)

# Save DataFrame to CSV (or desired format)
df.to_csv("wa_daily_keno.csv", index=False)

print("Scraping complete! Data saved to wa_daily_keno.csv")
