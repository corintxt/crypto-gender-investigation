Ultimately I want to assemble a CSV with a list of company names & GitHub org names, and tell the script to slowly run through it, getting all of the commit data, then parsing for gender.

Step 1: Assemble data for all companies

Step 2: Give gender scraper a directory to look in where CSVs are stored


TO-DO: need to put in control flow, so that I can make keyboard interrupts without needing to start the whole thing again.

---

* As [GitHub notes](https://help.github.com/en/articles/viewing-contribution-activity-in-a-repository), you can only access the top 100 contributors to a repo. For most cryptocurrency projects this is all contributors, but for some (e.g. bitcoin with 600) it is only a fraction.
* The repositories scraped don't necessarily represent the entire codebase of the proejcts. Some projcects (like EOS) only put a subset of open source elements on their public GitHub.