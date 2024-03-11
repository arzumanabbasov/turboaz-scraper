# TurboAzScraper

## Overview

The TurboAzScraper is a web scraping tool designed to extract car information from the Azerbaijani car sales website Turbo.az. It consists of two main scripts: `getlinks.py` and `scrapecars.py`. 

### `getlinks.py`

This script is responsible for retrieving the links to individual car listings on Turbo.az. It navigates through the website, extracts the links, and saves them to a text file for later use.

### `scrapecars.py`

The `scrapecars.py` script utilizes the links obtained by `getlinks.py` to scrape detailed information about each car. It collects data such as the city, market, make, model, production year, and various other details. The scraped information is then stored in CSV files for further analysis.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arzumanabbasov/turbo-az-scraper.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### `getlinks.py`

Run this script to obtain links to car listings on Turbo.az:

```bash
python getlinks.py
```

### `scrapecars.py`

Run this script to scrape detailed information about cars from the obtained links:

```bash
python scrapecars.py
```

## Features

- **Link Extraction:** `getlinks.py` extracts links to car listings from Turbo.az and saves them to a text file.
- **Data Scraping:** `scrapecars.py` uses the extracted links to gather detailed information about each car listing.
- **Customizable:** Both scripts can be adapted to specific needs through configuration and code modifications.
- **Data Storage:** Scraped data is stored in CSV files for easy analysis.

## Configuration

Adjust settings in the scripts to suit your needs. For example, modify the base directory (`BASE_DIR`) or customize the data fields in `scrapecars.py` as necessary.

## Dependencies

- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)

Install the required dependencies using:

```bash
pip install -r requirements.txt
```


