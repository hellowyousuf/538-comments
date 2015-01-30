<h1> FiveThirtyEight.com Facebook Comments Scraper (Selenium) </h1>

Modules - the heavy lifting is done in selFTE.py which uses selenium as the browser automation tool to execute javascript on page and attach to the virtual DOM for FB comments. selFTE.py uses the Firefox driver, so make sure that you have Firefox installed.

splcity.py extracts the bare city name (i.e. San Francisco from San Francisco, CA) from the full location. This is critical for importing locations into CartoDB, but nothing else really.

Usage - the fte-write.sh script expects 3 arguments, an input file of urls (one url per line). An intermediate file (second arg) which selFTE writes to. Finally, it needs an output file for the splcity script to write to...

The compare.csv file is an example input file of urls
