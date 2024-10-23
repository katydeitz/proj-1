import requests
import re

# Function to fetch webpage content with a custom User-Agent header
def fetch_webpage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Webpage fetched successfully")
            return response.text
        else:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Function to extract 'foraging' related information using regular expressions
def extract_foraging_info(web_content):
    # Using regular expressions to find paragraphs or headings that mention 'foraging'
    foraging_info = re.findall(r'(?i)(<p>.*?foraging.*?</p>|<h\d>.*?foraging.*?</h\d>)', web_content)
    return [re.sub('<.*?>', '', item) for item in foraging_info]  # Remove HTML tags

# Main script
def main():
    url = 'https://namyco.org/'  # North American Mycological Association website
    webpage_content = fetch_webpage(url)

    if webpage_content:  # If webpage content is successfully fetched
        foraging_info = extract_foraging_info(webpage_content)

        if foraging_info:  # If any foraging-related info is found
            # Write the extracted information to a file
            output_file = 'nama_foraging_info.txt'
            with open(output_file, 'w') as file:
                for info in foraging_info:
                    file.write(info + '\n')

            print(f"Foraging information written to {output_file}")
        else:
            print("No foraging-related information found.")
    else:
        print("Webpage content could not be retrieved.")

if __name__ == "__main__":
    main()
