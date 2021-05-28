This directory contains the data sources used for this project. Raw data can be found in the following sources:

* world_bank_access_to_electricity_per_pop: From the World Bank. Describes what percentage of each country's population has access to electricity. Dates range from 1990 to 2018.
* exchange_rates: Historical exchange rates for global currencies.
* gdp_historical_data: Historical GDP data for each country.
* Literacy rate 15 and older: Historical data on literacy rates for age 15 and older for each country.
* Mortality rate of infant per 1000 live birth: Historical data on infant mortality rates per 1,000 live births for each country.
* world_bank_country_mappings: A cross-reference sheet that maps country codes, names, regions, and income levels.


Our processed data can be found in:

* pdfminer_texts/ : Loan documents successfully extracted with PDFMiner.six and saved as text files.
* pytesseract_texts: Loan documents without embedded text that were OCR'd with pytesseract and saved as text files.
* Extracted_Attributes: A first-pass extraction of relatively simple data from each loan document.
* Extracted_Attributes_LoanUSD: First-pass extraction, plus conversion of each loan's currency to US Dollars where possible using the historical exchange rate information from exchange_rates.
* Extracted_Attributes_LoanUSD_Topics: First-pass extraction and currency conversion, plus the categorization of each loan as per our Project Classifier notebook, where possible.
* All_Extracted_Data_From_PDFs: Our final dataset. Consists of all non-null entries from Extracted_Attributes_LoanUSD_Topics.
* Indicators_Delta: For each borrower and each of the four loan categories, contains the pertinent information for assessing loan impacts.
* loan_by_topic: Aggregated per-year loan totals for each country by loan category.