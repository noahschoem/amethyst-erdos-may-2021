This directory contains the following Jupyter notebooks, with the following recommended execution order:

1. (Optional) raw_pdfs_to_text: is responsible for extracting textual information from the World Bank loan PDFs and writing to text files.
   As the relevant text files can already be found in the data directory, running this is optional.
 
2. Extract_Attributes_From_Texts: Parses the raw texts from the pdfs to extract just the lines that we are interested in. It extracts the parts needed to find the date, country code, project name, project description and amount of the loan. 

3. Convert_Currency: Uses the information about loan and currency extracted before to identify the most common currencies, and extract the loan amount using these. Using a historic currency exchange, converts all loan amounts to US dollars. 

4. Identify_Country: Uses a fuzzy match to identify the country for each loan. Some common mistakes are fixed by hand. 

5. Project Classifier: Uses nlp tools and dimension reduction to identify the 10 biggest sectors that the loans are used for. By looking at the most common words per sector and some random PDF's in each sector, we give them more representative names, such as 'Health Care', 'Education', etc.  

6. Clean_Extracted_Attributes: Creates a .csv file only with the columns that we need and droping all missing values. 

The rest can be run in any order, after the above are executed:

* Pivoting table for tableau: An R script that aggegrates loan amounts by country and topic per year. Writes to loans_by_topic in the data directory, which gets used for our Tableau app.

* Identifying Impact via Pvalues: This notebook displays timed data on which loan categories composed what percentage of loans per year.
    Additionally, For each country receiving loans in one of four target categories, this notebook looks at the impact of our chosen category indicator to determine whether the loan had an impact.