# 📈 Stock Scraper for Yahoo Finance
This project is a Python-based web scraper that extracts real-time stock market data from Yahoo Finance using Selenium and Pandas. It automates web navigation, retrieves stock data, processes it, and saves it in an Excel file for further analysis.

## 🚀 Features
✅ Automated Web Scraping – Uses Selenium to interact with Yahoo Finance dynamically.
✅ Stock Data Extraction – Fetches symbol, price, change, percentage change, volume, market cap, P/E ratio, and more.
✅ Data Cleaning – Processes and converts raw data into structured formats using Pandas & NumPy.
✅ Excel Export – Saves the cleaned stock data into an Excel file for easy analysis.
✅ Pagination Handling – Extracts stock data across multiple pages automatically.

## 📦 Installation
Ensure you have Python 3.x and the required dependencies installed.

## 1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/kapilshrirampatil/stock_scrapper.git
cd stock-scraper

## 2️⃣ Install Dependencies
bash
Copy
Edit
pip install selenium pandas numpy

## 3️⃣ Set Up Chrome WebDriver
Download ChromeDriver that matches your Chrome version from https://developer.chrome.com/docs/chromedriver/downloads.
Place the WebDriver in the system path or specify its location in the script.

## 🔥 Usage
Running the Scraper
bash
Copy
Edit
python stock_scraper.py
The script will:
✅ Open Yahoo Finance in a Chrome browser.
✅ Navigate to the Most Active Stocks section.
✅ Scrape stock details like price, volume, market cap, and P/E ratio.
✅ Clean the extracted data.
✅ Save the output as most active stocks.xlsx.

## 📊 Sample Output
The extracted stock data will look like this:

Symbol	Name	Price (USD)	Change	% Change	Volume (M)	Avg Vol (M)	Market Cap (B)	P/E Ratio	52-Week Change
AAPL	Apple	172.50	+1.20	+0.70%	50	45	2.5T	28.5	+18%
TSLA	Tesla	780.10	-5.30	-0.67%	30	28	800B	90.2	+25%


## 🛠️ Customization
Change the timeout in StockScrapper(driver, timeout=5) to modify the Selenium wait time.

Modify XPath selectors if Yahoo Finance changes its page structure.

Add more stock categories (e.g., gainers, losers) by adjusting navigation logic in access_stock().

## 🚧 Limitations & Future Enhancements
🚨 Dynamic Webpage – Yahoo Finance's layout may change, requiring updates to XPath selectors.
💡 Multi-Stock Support – Extend the script to track specific stock tickers instead of trending stocks.
📊 Data Visualization – Integrate Matplotlib or Seaborn to visualize stock trends.
🔄 Scheduled Scraping – Automate data collection with a scheduler (cron jobs / Task Scheduler).

⭐ If you find this project useful, give it a star! 🚀
