# Team Amethyst: Analysis of World Bank Loans

<p align="center">
  <a href="">
      Video coming soon!<img width="525" height="300" src="figures/video_screenshot.png">
  </a>
</p>

This project's purpose is to extract information from World Bank loan documents from 1990 to 2019 and identify major trends in the World Bank's development loans program.

This project is part of The Erdos Institute's [data science boot camp](https://www.erdosinstitute.org/code) and is an answer to [Qarik](https://www.qarik.com/)'s data challenge. Data sources include World Bank loan documents, provided by Qarik, and ancillary data from the World Bank and World Economic Forum as found and described in our data directory.

## Table of contents
  - [Process](#process)
  - [Results](#results)
  - [Actionable Insights](#actionable-insights)
  - [Using the code](#using-the-code)
  
## Process

Our extraction and data cleaning happens in three main stages:

1. Extracting text from the PDFs. For PDFs with embedded text, [pdfminer.six](https://pdfminersix.readthedocs.io/) was used. For scanned images, optical character recognition from [Tesseract](https://github.com/madmaze/pytesseract) was employed.
2. Uniformization. Where possible, loans were mapped to country codes, and loan amounts were converted into US Dollars using historical currency exchange rates.
3. Loan Categorization. To categorize the loans into broad target categories, non-negative matrix factorization (NNMF) was employed on project titles and descriptions. Exploratory runs revealed that:
  * NNMF on word bigrams was the appropriate tool over single words
  * NNMF was a better choice than Latent Dirichlet Allocation
  * Ten major categories was a suitable number.
  
In the end, we were able to extract loan amounts and categorize for (??? TODO: find out) percent of the loan documents.
Manual inspection of sampled loans indicates that our loan categorization algorithm is roughly 90% accurate.

## Results
TODO: write me!


## Actionable Insights
TODO: write me!


## Using the code

The project code spans several notebooks that may be found in the notebooks/ directory.
Imports and dependencies are found at the top of each notebook. To run the notebooks, an installation of Python and Jupyter are required, as are various Python packages and other software as noted in each notebook.
