import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all book cards
books = soup.find_all("article", class_="product_pod")

print("Books Found:", len(books))

data = []

# Loop through all books
for book in books:

    # Title
    title = book.h3.a["title"]

    # Price
    price = book.find("p", class_="price_color").text

    # Rating
    rating = book.p["class"][1]

    # Availability
    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    # Product link
    link = book.h3.a["href"]

    full_link = "https://books.toscrape.com/catalogue/" + link

    # Image URL
    image = book.find("img")["src"]

    image_url = "https://books.toscrape.com/" + image

    # Print in terminal
    print(title)
    print(price)
    print(rating)
    print(availability)
    print(full_link)
    print(image_url)
    print("-" * 50)

    # Store data
    data.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability,
        "Product Link": full_link,
        "Image URL": image_url
    })

# Convert into DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Save into Excel
df.to_excel("all_books_data.xlsx", index=False)

print("All Data Saved Successfully")