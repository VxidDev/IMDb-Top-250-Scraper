# IMDb Top 250 Scraper

A Selenium-based script to scrape IMDb's Top 250 movies. It extracts movie titles, release dates, length, ratings, and links, then saves the results to a CSV file.

## Features

- Headless browser scraping using Selenium
- Handles messy class names with XPath
- Extracts metadata for each movie
- Randomized delays to mimic human browsing
- Outputs results to a clean CSV file

## Requirements

- Python 3.x
- Selenium
- Firefox + Geckodriver
- Colorama

Install dependencies via pip:

```bash
pip install selenium colorama
```
Ensure Firefox and Geckodriver are installed and added to your system PATH.

## Usage

Run the script:
```
python main.py
```

1. Input the number of movies to scrape (max 250)

2. The script will scrape data and save results.csv in the same folder

   Progress updates are printed to the terminal

### Notes

Works best for IMDb Top 250 (static page)

Random sleep delays are included to reduce server load

Make sure your internet connection is stable
