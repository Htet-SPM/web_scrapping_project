# web_scrapping_project_batch 5
# Apple Product Web Scraper

A Python-based web scraping tool that collects **Apple product information** from the Mobile King Myanmar website and exports the extracted data to Excel files.

The scraper automatically detects the available product pages, extracts product names, prices, and links, and saves the results with an extraction timestamp.

## Features

* Scrapes Apple products from Mobile King Myanmar
* Automatically detects the number of available product pages
* Extracts:

  * Product name
  * Product price
  * Product URL
* Displays scraping progress using `tqdm`
* Adds the extraction date and time to the output
* Exports data to Excel using Pandas
* Creates both:

  * A timestamped historical Excel file
  * A `Last Update Data.xlsx` file containing the latest results

## Technologies Used

* **Python 3**
* [Requests](https://pypi.org/project/requests/) — HTTP requests
* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) — HTML parsing
* [tqdm](https://pypi.org/project/tqdm/) — Progress bar
* [Pandas](https://pypi.org/project/pandas/) — Data processing
* [OpenPyXL](https://pypi.org/project/openpyxl/) — Excel file generation

## Requirements

Make sure Python 3.x is installed on your computer.

Install the required Python packages:

```bash
pip install requests beautifulsoup4 tqdm pandas openpyxl
```

Or install them from a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```text
requests
beautifulsoup4
tqdm
pandas
openpyxl
```

## How It Works

The scraper follows these steps:

```text
Website
   │
   ▼
Get Main Product Category Page
   │
   ▼
Detect Number of Pages
   │
   ▼
Generate Page URLs
   │
   ▼
Scrape Each Product Page
   │
   ├── Product Name
   ├── Product Price
   └── Product Link
   │
   ▼
Store Data in Lists
   │
   ▼
Create Pandas DataFrame
   │
   ▼
Export to Excel
```

## Configuration

The website URL is configured in the main section of the Python script:

```python
my_url = "https://mobilekingmyanmar.com/product-category/apple"
```

To scrape a different supported product category, update this URL:

```python
my_url = "YOUR_PRODUCT_CATEGORY_URL"
```

> **Note:** The scraper depends on the HTML structure and CSS classes used by the target website. If the website changes its HTML structure, the extraction functions may need to be updated.

## Extracted Data

The scraper collects the following information:

| Column               | Description                               |
| -------------------- | ----------------------------------------- |
| `Name`               | Product name                              |
| `Price`              | Product price                             |
| `Link`               | Product URL                               |
| `Extracted DateTime` | Date and time when the data was collected |

Example:

| Name          |     Price | Link        | Extracted DateTime  |
| ------------- | --------: | ----------- | ------------------- |
| iPhone 16 Pro | 3,500,000 | Product URL | 2026-10-05 17:30:00 |
| iPhone 16     | 2,800,000 | Product URL | 2026-10-05 17:30:00 |

## Output Files

The script generates two Excel files.

### 1. Historical Record

A timestamped file is created using the current date and time:

```text
Exported Data 2026-10-05 17-30-00.xlsx
```

This allows previous scraping results to be retained as historical records.

### 2. Latest Data

The latest scraping results are also saved as:

```text
Last Update Data.xlsx
```

This file is overwritten each time the scraper runs and therefore always contains the latest available data.

## Output Location

The current implementation saves the files to:

```text
C:\Users\htethtet.aung\Documents\PythonBasic\WebDataCollection\Daily Record Files\
```

You should change this path to a location appropriate for your computer.

For example:

```python
output_path = "C:\\Users\\YourName\\Documents\\WebData\\"
```

A more portable approach would be to use `pathlib` instead of a hard-coded Windows path.

## Running the Scraper

Clone the repository:

```bash
git clone https://github.com/your-username/apple-product-web-scraper.git
```

Navigate to the project directory:

```bash
cd apple-product-web-scraper
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Python script:

```bash
python scraper.py
```

During execution, a progress bar will show the scraping progress:

```text
100%|████████████████████████████████| 5/5
```

After the scraping process is complete, the following message will be displayed:

```text
Product Info are exported as excel file successfully...
```

## Project Structure

A recommended project structure is:

```text
apple-product-web-scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
│
└── output/
    ├── Last Update Data.xlsx
    └── Exported Data YYYY-MM-DD HH-MM-SS.xlsx
```

## Main Functions

### `create_bsObj()`

Creates a BeautifulSoup object from a website URL.

```python
def create_bsObj(website_url):
```

It sends an HTTP request to the website and parses the returned HTML.

### `create_page_url_list()`

Determines the number of available pages and creates a list of URLs for each page.

```python
def create_page_url_list(website_url):
```

### `extract_name()`

Extracts the product name from the product HTML element.

```python
def extract_name(item_tag_var):
```

### `extract_price()`

Extracts and converts the product price into a numeric value.

```python
def extract_price(item_tag_var):
```

### `extract_link()`

Extracts the product URL.

```python
def extract_link(item_tag_var):
```

### `export_as_excel()`

Creates a Pandas DataFrame and exports the collected product information to Excel.

```python
def export_as_excel(name_list, price_list, link_list):
```

## Important Considerations

### Website Structure

The scraper relies on specific HTML classes such as:

```text
page-numbers
wd-entities-title
woocommerce-Price-amount amount
product-wrapper
```

If these classes change, the scraper may stop working correctly.

### HTTP Requests

The current implementation uses:

```python
requests.get(website_url)
```

For production use, it is recommended to add a timeout and error handling:

```python
requests.get(website_url, timeout=10)
```

### HTTP Status Codes

The current code only creates the BeautifulSoup object when the response status code is `200`.

Additional error handling could be added for:

* Connection errors
* Timeout errors
* HTTP 404
* HTTP 403
* Server errors

### Website Terms and Policies

Before running the scraper regularly, make sure your usage complies with the target website's terms of service, `robots.txt`, and applicable laws. Avoid sending requests too frequently and consider adding a delay between requests for responsible scraping.

## Possible Improvements

Future versions could include:

* Request timeout and exception handling
* Automatic retry for failed requests
* Request delays to reduce server load
* Logging
* Configuration through a `.env` or configuration file
* Command-line arguments for selecting categories
* Automatic daily scheduling
* Database storage
* Price-change tracking
* Email notifications when prices change
* Support for multiple product categories
* Portable output paths instead of hard-coded Windows directories
* Duplicate product detection

## License

This project is provided for educational and personal use.

If you plan to publish or distribute this project, add an appropriate license, such as the MIT License, based on how you intend others to use the code.

## Disclaimer

This project is intended for educational purposes and demonstrates how Python can be used for web data collection and Excel-based reporting.

Users are responsible for ensuring that their use of the scraper complies with the target website's policies and applicable laws.
