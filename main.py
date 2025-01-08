import requests
from bs4 import BeautifulSoup


# Define function
def fetch_document_content(url):
    # Fetch content
    response = requests.get(url)
    # Function takes single argument of url to Google document link
    if response.status_code != 200:
        # If request is unsuccessful then error message is printed
        print(f"Could not retrieve document: {response.status_code}")
        return

    # Parse content
    soup = BeautifulSoup(response.text, 'html.parser')
    # get_text method obtains text from the Google document
    data = soup.get_text("\n").strip().splitlines()
    # splitlines takes each new line and splits into a list of lines

    start_real_data = False
    # initialize flag and empty list
    real_data = []
    # iterate through parsed lines to find line containing y-coordinate
    for item in data:
        if start_real_data:
            real_data.append(item)
        else:
            if item == 'y-coordinate':
                # Once found, set start_real_data to true
                start_real_data = True
                # Subsequent lines contain relevant data to append to real_data

    print(real_data)
    # Print extracted data

    # Create dictionary for storing characters and coordinates
    char_positions = {}
    x = 0
    y = 0
    character = ""
    for index, item in enumerate(real_data):
        # Loop enumerates over data using mod to determine correct index
        # x is 0, character is 1, y is 2
        if index % 3 == 0:
            x = int(item.strip())
        if index % 3 == 1:
            character = item
        if index % 3 == 2:
            y = int(item.strip())
            # Store coordinate and character in char_position
            char_positions[(x, y)] = character
    print(char_positions)

    # Specify grid size parameters
    max_x = max(pos[0] for pos in char_positions) + 1
    max_y = max(pos[1] for pos in char_positions) + 1

    print(max_x, max_y)

    # Make grid and fill with characters and related coordinates
    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    for (x, y), character in char_positions.items():
        grid[y][x] = character

    # Print grid row by row
    for y in range(max_y - 1, -1, -1):
        # Reverse order of rows so y-coordinate values increase upward
        print(''.join(grid[y]))


doc_url = (
 "https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub")
fetch_document_content(doc_url)
