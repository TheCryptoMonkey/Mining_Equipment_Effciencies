# Mining_Equipment_Effciencies
Hello, 

This project's main goal is to scrape data from https://whattomine.com/ and to calculate the efficiency of each GPU posted on their website. This will therefore make the decision process easier for a miner to figure out what GPUs to buy on a hash rate per watt basis.
All of the calculations are on the basis that https://whattomine.com/ has given reliable and accurate data for each GPU respectively. These calculations are also not "hard and fast" numbers. Based on different overclock settings and different flashed VBIOSes you are able to achieve better or worse efficiency based on the settings you input. This data is meant to be a high overview on the efficiency of these graphics cards.
This is the code and the end result of the data cleanup from the scrape.
This project is still currently being worked on. 


Things to know:
The Graphics_Card_Web_Scraping.py program takes time to gather all of the data. Don't worry about the errors on the command line and don't worry when the browser stalls.
If you want to make this process go faster you can use the Both_URL_Lists.txt and replace the nvdia_list and the amd_list with these lists.
If you want to see end result of this scrape, then you can go to the Mining Equipment Effciency.csv file in this repository or to the Google Sheets web page at the end of this README.

The current goals for this project:
1. To learn more about the Google Cloud Platform, Google Sheets API, and Google Drive API.
2. To automate the process of importing my data into Google Sheets.
3. To automate the process of formatting my data in Google Sheets.
4. To gather more data for other mining equipment and for improving the current (GPU Efficiencies) sheet. 

Here is the data in Google Sheets: https://docs.google.com/spreadsheets/d/1HWsU_Res9zf6dKOMAwBBYzYXqNYjMD0M7nXxYF-Ctdg/edit?usp=sharing
There are still some things that are not yet done in this spreadsheet. Such as some of the color highlighting. This will be updated in the future.
