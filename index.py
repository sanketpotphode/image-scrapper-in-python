import requests
from bs4 import BeautifulSoup as bs
import os

URL = 'https://unsplash.com/s/photos/gallery'  # Replace with the desired URL

# Send a GET request to the URL
req = requests.get(URL)

# Create a BeautifulSoup object to parse the HTML
soup = bs(req.text, 'html.parser')

# Find all image tags
image_tags = soup.find_all('img')

# Create a directory to store the downloaded images
image_directory = 'images'  # Name of the desired directory
os.makedirs(image_directory, exist_ok=True)

for img in image_tags:
    # Get the source URL of the image
    img_url = img['src']
    
    # Download the image
    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()
        
        # Extract the image file name from the URL
        img_filename = img_url.split('/')[-1]
        
        # Save the image to the directory
        img_path = os.path.join(image_directory, img_filename)
        with open(img_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Image downloaded: {img_filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

print("Image scraping and downloading complete.")