# Mookit-Scraping

This scraper is created to fetch information from Mookit.

Steps for use:
1. Log into the platform, go to the course page for which we want to scrape the links. Example link should look like this, https://hello.iitk.ac.in/cs711a21/#/home (<b>THIS IS IMPORTANT</b>).

2. Download the page by pressing `Ctrl+S` -> Download Complete page and place it to the same directory where the `run.sh` is.

3. Run `./run.sh n`, where `n` is the number of lectures you want to scrape. A folder named same as the course name will be created, with `index.html` (the original HTML given) and `data.csv` (the scraped data).