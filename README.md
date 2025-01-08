### Explanation

1. **Import Libraries**
- `requests` makes the HTTP requests to the web to fetch content from the Google document.
- `BeautifulSoup` from the `bs4` module is used for web scraping and parsing the data retrieved therein.

2. **Define the Function**
- The function `fetch_document_content` is defined. It takes as its single argument the URL link to the specified published Google document.

3. **Fetching the Content**
- We make an HTTP GET request to the URL link, which if unsuccessful, prints an error message to the console.

4. **Parsing Document Content**
- `BeautifulSoup` parses the content. The `get_text` method obtains the text, `splitlines()` splits new lines into lists of new lines.

5. **Data Extraction**
- Code initializes the empty list with `real_data = []`, then iterates through the parsed content of `data` searching for the line containing 'y-coordinate' and appends all data found thereafter to the list.

6. **Dictionary for Storing Characters with Corresponding Coordinates**
- `char_positions` initializes dictionary for storing coordinates (keys) and characters (values) as ordered, immutable, indexed collections of data.
- Loop enumerates over `real_data` and uses mod to determine index positions, then stores coordinates with their corresponding characters in `char_positions`.

7. **Grid Sizing**
- To create a 2D grid, we need to first calculate maximum x and y coordinates and then print out the sizes.

8. **Populate the Grid with Data**
- We initialize the grid with spaces and dimensions relative to max x and max y values.
- Loop fills in the grid with data found in `char_positions`.

9 **Print Grid and Voila!**
- We print the grid one row at a time, using `range(max_y -1, -1, -1)` to ensure printing of rows occurs in reverse order. This is for alignment with coordinate systems in which the values on the y axis increase upward, so it is visually correct.

