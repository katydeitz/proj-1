import requests
import json

# Function to fetch literature from GBIF API for a given query (Raffaelea fungi in this case)
def fetch_literature(query):
    url = f"https://api.gbif.org/v1/literature/search?q={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:  # If request is successful
            return response.json()  # Return the JSON data from the API response
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to process the API response and write the relevant information to a file
def process_and_write_literature(data, output_file):
    if data and 'literature' in data:
        # Open file to write the results
        with open(output_file, 'w') as file:
            for item in data['literature']:
                title = item.get('title', 'No Title Available')
                year = item.get('year', 'No Year Available')
                authors = item.get('authors', 'No Authors Available')
                doi = item.get('doi', 'No DOI Available')

                # Write information to the file
                file.write(f"Title: {title}\n")
                file.write(f"Year: {year}\n")
                file.write(f"Authors: {authors}\n")
                file.write(f"DOI: {doi}\n")
                file.write("\n" + "-"*40 + "\n")  # Separator for entries

        print(f"Literature information written to {output_file}")
    else:
        print("No relevant literature found or data is unavailable.")

# Main script
def main():
    query = "Raffaelea"
    output_file = "raffaelea_literature.txt"

    # Fetch literature data from the GBIF API
    literature_data = fetch_literature(query)

    # Process the data and write to the file if relevant literature is found
    process_and_write_literature(literature_data, output_file)

if __name__ == "__main__":
    main()
