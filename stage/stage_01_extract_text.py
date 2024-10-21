import requests
from bs4 import BeautifulSoup
import os
from src.Log import logger
from src.constants import CONFIG_FILEPATH


class TextExtractor:
    def __init__(self, url, output_file):
        self.url  = url
        self.output_file = output_file
    
    def extract_entire_content(self):
        """
        Returns the extractd text as a text file
        Args:
            None
        Reutrns:
            None
        """

        try:
            # Send a GET request to the website
            logger.info("-- Getting response using url --")
            response = requests.get(self.url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the content of the website using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Get the entire text content from the website
                entire_content = soup.get_text(separator='\n')  # separator adds new lines for readability
                
                # Save the extracted content to a text file
                with open(self.output_file, 'w', encoding='utf-8') as file:
                    file.write(entire_content)
                
                logger.info(f"---- Entire content extracted and saved to {self.output_file} ----")
            else:
                logger.info(f"---- Failed to retrieve the webpage. Status code: {response.status_code} ----")
        except Exception as e:
            logger.error(f"----An error occurred: {e}----")

# # URL of the website to scrape
# url = "https://brainlox.com/courses/category/technical"
# url2= "https://brainlox.com/courses/4f629d96-5ed9-4302-ae0e-3479c543a49e"


# # File to save the extracted content
# output_file = "website_content.txt"

# # Call the function to extract and save the content
# p = TextExtractor(url, output_file)
# p.extract_entire_content()


if __name__ == "__main__":
    print(CONFIG_FILEPATH)


