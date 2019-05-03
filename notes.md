# Female developers in cryto

## Links
* Women in crypto reluctant to admit there are few women in crypto. -[Quartz](https://qz.com/1262167/the-first-rule-of-being-a-woman-in-crypto-is-you-do-not-talk-about-being-a-woman-in-crypto/)
  "Women in the industry primarily hold roles in business development, marketing, and fundraising, rather than in coding and development."
* A [woman is leading a team](https://www.wired.com/story/fight-over-specialized-chips-threatens-ethereum-split/) developing an ASIC-resistant mining algorithm for Ethereum
* CoinDance - [Bitcoin community engagement by gender](https://coin.dance/stats/gender) // this gets quoted all the time but based on very little...
* [Motherboard](https://motherboard.vice.com/en_us/article/8xz9yk/the-sexist-trolls-doubting-black-hole-researcher-katie-bouman-need-to-learn-to-code) - Trolls doubted how many code commits were made by the lead black hole researcher.
* [AI Now study](http://fortune.com/2019/04/23/artificial-intelligence-diversity-crisis/) on gender in AI.

-----

## Process

* We took the top 100 projects by market cap (Y2050?) as present on OnChainFX on April 3 2019.
* Not all of these projects put code in a public repo. Also, for a few projects the coin is just one part of a much bigger project (E.g. BAT as a project of Brave; Sia as a project of Nebulous Labs; Cardano as a project of ?). We discarded these projects and pulled more projects from the list until the total sample size was 100.
* I also discarded projects which were run by just a single user, or hosted under a personal GitHub account.



## Classification
Various sites exist to classify names by gender. These include https://genderize.io/ and https://gender-api.com/.

My analysis is limited by Genderize's database. They haven't made this available which makes it difficult to audit. Having manually checked results, there seems to be some evidence of bias towards (foreign names? unisex names?)

* One type of analysis: can find the team with the most 'ambiguously gendered' team members, i.e. most people whose gender could only be inferred with low probability.

When scraped:
Monthly limit: 100.000
Remaining names: 74.314


Ultimately I want to assemble a CSV with a list of company names & GitHub org names, and tell the script to slowly run through it, getting all of the commit data, then parsing for gender.

Step 1: Assemble data for all companies

Step 2: Give gender scraper a directory to look in where CSVs are stored


TO-DO: need to put in control flow, so that I can make keyboard interrupts without needing to start the whole thing again.

* Also: some projects are set up as users (Monero) not orgs. 

---
## References


* As [GitHub notes](https://help.github.com/en/articles/viewing-contribution-activity-in-a-repository), you can only access the top 100 contributors to a repo. For most cryptocurrency projects this is all contributors, but for some (e.g. bitcoin with 600) it is only a fraction.
* The repositories scraped don't necessarily represent the entire codebase of the proejcts. Some projcects (like EOS) only put a subset of open source elements on their public GitHub.
* [Ars Technica](https://arstechnica.com/information-technology/2016/02/data-analysis-of-github-contributions-reveals-unexpected-gender-bias/) - Women more likely to have commits accepted.
* [WIRED](https://www.wired.com/2017/06/diversity-open-source-even-worse-tech-overall/) - Diversity in open source worse than in tech overall. 
* [Github open source survey](https://opensourcesurvey.org/2017/)