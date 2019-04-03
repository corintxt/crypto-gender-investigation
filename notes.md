Ultimately I want to assemble a CSV with a list of company names & GitHub org names, and tell the script to slowly run through it, getting all of the commit data, then parsing for gender.

Step 1: Assemble data for all companies

Step 2: Give gender scraper a directory to look in where CSVs are stored

---

As [GitHub notes](https://help.github.com/en/articles/viewing-contribution-activity-in-a-repository), you can only access the top 100 contributors to a repo. For most cryptocurrency projects this is all contributors, but for some (e.g. bitcoin with 600) it is only a fraction.