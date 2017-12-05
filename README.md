# PlaqueScraper
Purpose: to scrape plaque data from the old Aberdeen City Council site

## Intro

On 30 November 2017, Aberdeen City Council relaunched its website. In so doing, subtantial amounts of content and functionality was either written off or temporarilt shelved. 

This is the first of a series of scrapers needed to quickly grab that content before it vanishes forever. 

Some of that content has been located under [this page](https://online.aberdeencity.gov.uk/Services/)

At its heart the Plaques system is simple. It uses a [base url](https://online.aberdeencity.gov.uk/Services/CommemorativePlaque/PlaqueDetail.aspx?Id=) which is concatenated with a record number to create a functioning record page such as [this](https://online.aberdeencity.gov.uk/Services/CommemorativePlaque/PlaqueDetail.aspx?Id=1)

Records appear to fall in the range 1 to 114 - but not all are present. 

Record pages are not uniform - some have 5, 6, 7 or 8 para sections. 

## Aim
The aim of this script if to use URLLib to grab the HTML of the page, then Beautiful Soup to isolate the main bulk of the page where the content lies. 

We then iterate through <p> tags in that section, and (mostly) split the fields on ":" - retaining the content

As a quick and dirty fix I have created an output HTML file for each plaque (using the origina ID in the name) with paras with IDs representing the type of content - name, location type etc. 

## Issues
The code choked on a number of pages where, I suspect, the original HTML contained some cut-and-paste text from another system which introduced off characters. At present I and stripping that out rather than do better error trapping! This is a quick hack, after all.

## To be done
At present I do not grab the photographs of the plaque.

I need to do something better with the output - XML would be an improvement.

The code is not very pythonic - so could be cleaned up a bit!