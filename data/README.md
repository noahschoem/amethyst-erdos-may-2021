This directory contains the data sources used for this project. Raw data can be found in the following sources:

* world_bank_access_to_electricity_per_pop: From the World Bank. Describes what percentage of each country's population has access to electricity. Dates range from 1990 to 2018.
* world_econ_forum_electricity_quality_index: From the World Economic Forum. Describes the quality and reliability of each country's electrical grid on a scale of 1 (worst) to 7 (best). Dates range from 2007 to 2017.
* world_bank_electricity_per_cap: From the World Bank. Describes each country's power consumption (in kilowatt-hours) per capita. Dates range from 1960 to 2014.
* exchange_rates: TODO (also what's our source?)

Our processed data can be found in:

* pdfminer_texts/ : TODO
* pytesseract_texts: TODO
* Extracted_Attributes: A first-pass extraction of relatively simple data from each loan document.
* Extracted_Attributes_LoanUSD: First-pass extraction, plus conversion of each loan's currency to US Dollars where possible using the historical exchange rate information from exchange_rates.
* Extracted_Attributes_LoanUSD_Topics: First-pass extraction and currency conversion, plus the categorization of each loan as per our Project Classifier notebook, where possible.
* energy_grid_invest_vs_percent_difference: Per-country difference in the percentage of population with access to electricity, versus total loan investment in said country in Energy & Grid. Missing data on access percentage was linearly interpolated by country.