# Amazon Spending Calculator
Simple script to calculate the total amount you've spent on Amazon.
>I'm lazy and this script is not going to be maintained, it will probably break in the future as amazon continues to update their webapp. Feel free to fork and modify as you want. Email me at cheemaahmad016@gmail.com

I'm running ubuntu 22.04 and the instructions below are for that:

## Requirements
- Python
- Selenium
- BeautifulSoup
- Chrome WebDriver 

## Setup
1. Install Python libraries:
   ```bash
   pip install selenium beautifulsoup4
   ```

## Usage
1. Run Chrome with remote debugging:
   ```bash
   google-chrome --remote-debugging-port=9222
   ```
2. Manually log in to your Amazon account in this Chrome instance.
3. Run the script.

## Script Features
- Iterates through each page of the Amazon order history for a specified range of years.
- Extracts and prints the price information.
- Automatically navigates to the next year once the current year's pages are exhausted.

>Amazon, please don't sue, thanks