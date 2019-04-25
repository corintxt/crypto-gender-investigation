# Diversity Crisis: 95% of Blockchain Code Contributors are Men

[NAME] is one of the leading contributors to [CODEBASE], with over [NUMBER] commits. She's also a woman. And this puts her firmly in the minority.

[QUOTE FROM WOMAN]

Some limited statistics are available about the gender balance of major blockchain teams. 

Anecdotally, developers working in the field have long maintained that the people actually writing the code are overwhelmingly male, but there's been little more than anecdotal evidence—until now.



# Methodology

On April 3rd 2019, we used Messari's [OnChainFX dashboard](https://messari.io/onchainfx) to gather a list of the top 100 crypto projects by market cap. For these projects, we compiled a spreadsheet linking each project to the GitHub account where all of the repositories for the project code are hosted.

Projects were discarded if too many of the organization's repositories were unrelated to the core project—for example Cardano is just one product of blockchain engineering studio [IOHK](https://iohk.io/), and is hosted within a company [GitHub account](https://github.com/input-output-hk) that includes Ethereum clients and other projects not connected to the Cardano blockchain. Likewise, Basic Attention Token is hosted on an account that also includes the codebase for Brave Browser. Whenever a cryptocurrency project was discarded from the initial list of 100, a replacement was drawn from items 101-120 from the on the OnChainFX list, maintaining the overall number.

Using the [GitHub API](https://developer.github.com/v3/) and a custom Python script, we queried each of the 100 organizations to obtain a list of every repository belonging to the organization, and the number of commits made to each repository, by username. We then queried each account to obtain data for each user that had filled in the `name` field with a real name.

![]![corintxt-user-api](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/corintxt-user-api.png)

*Sample response from an API call querying a GitHub username*

With a separate script we queried each real name against a database maintained by [Genderize.io](https://genderize.io/), a web service that attempts to determine the gender of a first name. For each name, Genderize returns a predicted gender along with a probability estimate that the inferred gender is correct.

![genderize-api](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/genderize-api.png)

*Genderize API documentation example*

We then merged the dataset of genderized names with the dataset of usernames and commits, creating a new dataset [LINK] of code commits with predicted gender grouped by organization, from which the conclusions in this article are drawn. 

### Limitations of GitHub API

**CHECK: ** Using this method, we obtain data about the top 100 contributors to the `master` branch of each repo.

<https://github.com/bancorprotocol/contracts/graphs/contributors>

=> Run the test script again with a test csv input file to double check results—why are the number of commits so low for some of the projects (compared to total number of commits listed when visiting the repo homepage?)

=> `202` response code means the data for this repo is not cached. This means data from the repo is not returned. That means we should run the script again for this repo. In actual fact, when we get a 202 response we need to wait and query again until we get 200. (e.g. **Bancor**)



---

Before examining the conclusions it should be noted that [gender is complicated](https://www.huffingtonpost.ca/2017/05/10/understanding-gender-identity_n_16542822.html): Having a name that is parsed as female does not equate to being a woman and vice versa. The male/female binary is itself a reductive way to examine gender, so the findings of this investigation can only give a fuzzy representation of the gender identity of blockchain developers.

## What we found

In total we scraped data on 2,793,387 code commits across 100 projects. Of these, 1.98 million were made by people with male-identified names, and only 139,054 were made by people with female-identified names. The remaining 678,011 commits were made by users who did not provide a real name, or (in a smaller number of cases) provided a name that could not be parsed as a given gender.

This means that in total, GitHub users with female names account for **less than 5 percent** of the commits to the top 100 cryptocurrency priojects—**4.978 percent** to be exact.

This means that, ignoring commits by users of unknown gender, 14 times more commits were made by male-named developers than female-named developers.

![gender_commits](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/gender_commits.png)

There was also a discrepancy in the average number of commits made by each of the three groups. Male-named developers in the dataset made eight more commits than female-named developers on average, while developers of unknown gender (who generally had not filled in a real name) made the fewest commits.

![average_commits](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/average_commits.png)

### Individual projects

The discrepancy in gender balance is more or less consistent across projects, but with some outliers.

The project with the highest percentage of commits by female-named users was X.

The project with the worst gender imbalance was Y.



=> Which branch and time period are we getting commits from?



## A systemic problem

After decades of gender imbalance, many fields of technology are starting to have a reckoning with the fact that they skew disproportionately male.

- [Motherboard](https://motherboard.vice.com/en_us/article/8xz9yk/the-sexist-trolls-doubting-black-hole-researcher-katie-bouman-need-to-learn-to-code) - Trolls doubted how many code commits were made by the lead black hole researcher.
- [AI Now study](http://fortune.com/2019/04/23/artificial-intelligence-diversity-crisis/) on gender in AI.



### Issues

- We counted commits, not lines of code. Different developers and organizations have different styles of committing, so number of commits is only a rough proxy for contribution to a project. However, counting the number of lines of code is also only a proxy—a bug fix that requires only three lines of code may represent many hours of work to arrive at the appropriate solution. 
- Many projects begin as forks of another project—e.g. Litecoin, TK and TK which are bitcoin forks, and Ethereum Classic, TK and TK. When a project is forked, the initial commit history is maintained, meaning that the users who have committed to the early Bitcoin codebase are counted multiple times. However, since the codebases of early cryptocurrency projects like Bitcoin and Ethereum were foundational for the development of blockchain technology as a whole, counting these commits once for each separate fork arguably represents the outsize influence that the authors of these code commits have had.
- Parsing names - we count just the male/female, not the probability.
- Gender is complicated!!
- Are women more or less likely to enter a real name? (Pull requests more frequently accepted...)