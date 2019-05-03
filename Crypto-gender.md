# Diversity Crisis: 95% of Blockchain Code Contributors are Men

[NAME] is one of the leading contributors to [CODEBASE], with over [NUMBER] commits. She's also a woman. And this puts her firmly in the minority.

[QUOTE FROM WOMAN]

Some limited statistics are available about the gender balance of major blockchain teams. 

Anecdotally, developers working in the field have long maintained that the people actually writing the code are overwhelmingly male, but there's been little more than anecdotal evidence—until now.

## A systemic problem

After decades of gender imbalance, many fields of technology are starting to have a reckoning with the fact that they skew disproportionately male.

- [AI Now study](http://fortune.com/2019/04/23/artificial-intelligence-diversity-crisis/) on gender in AI.



# Methodology

On April 3rd 2019, we used Messari's [OnChainFX dashboard](https://messari.io/onchainfx) to gather a list of the top 100 crypto projects by market cap. For these projects, we compiled a spreadsheet linking each project to the GitHub account where all of the repositories for the project code are hosted.

Projects were discarded if too many of the organization's repositories were unrelated to the core project—for example Cardano is just one product of blockchain engineering studio [IOHK](https://iohk.io/), and is hosted within a company [GitHub account](https://github.com/input-output-hk) that includes Ethereum clients and other projects not connected to the Cardano blockchain. Likewise, Basic Attention Token is hosted on an account that also includes the codebase for Brave Browser. Whenever a cryptocurrency project was discarded from the initial list of 100, a replacement was drawn from items 101-120 from the on the OnChainFX list, maintaining the overall number.

Using the GitHub API and a custom Python script, we queried each of the 100 organizations to obtain a list of every repository belonging to the organization, and then the number of commits made to the master branch of each repository by developer username. (Since many cryptocurrency projects start as forks of other projects e.g. Litecoin as a fork of Bitcoin, we requested data from the [repository API](https://developer.github.com/v3/repos/#list-organization-repositories) using the `?type=source`  parameter to omit forked repositories—without which, commits from a forked codebase would have been counted multiple times in the final dataset.)

We then queried each user account to check which users had filled in the `name` field with a real name, as shown below.

![]![corintxt-user-api](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/corintxt-user-api.png)

*Sample response from an HTTP request querying the author's own GitHub account*

With a separate script, we queried each listed real name against a database maintained by [Genderize.io](https://genderize.io/), a web service that attempts to determine the gender of a first name. For each name, Genderize returns a predicted gender along with a probability estimate that the inferred gender is correct.

![genderize-api](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/genderize-api.png)

*Genderize documentation example*

We then merged the dataset of genderized names with the dataset of usernames and commits, creating a new dataset [**LINK?**] of code commits with predicted gender grouped by organization, from which the conclusions in this article are drawn. 

Before examining the conclusions it should be noted that [gender is complicated](https://www.huffingtonpost.ca/2017/05/10/understanding-gender-identity_n_16542822.html): Having a name that is parsed as female does not equate to being a woman and vice versa. The male/female binary is itself a reductive way to examine gender, so these findings only give a fuzzy representation of the gender identity of blockchain developers.

## What we found

In total we scraped data on 1,029,456 code commits across 100 projects. Of these, 692,741 were made by people with male-identified names, and only 48,289 were made by people with female-identified names. The remaining 288,426 commits were made by users who did not provide a real name, or (in a smaller number of cases) provided a name that could not be parsed as a given gender.

This means that in total, GitHub users with female names account for **less than 5 percent** of the commits to the top 100 cryptocurrency priojects—**4.69 percent** to be exact.

GitHub users with male names make **67.3 percent** of the commits to the top 100 cryptocurrency projects, with the remaining **28 percent** made by developers of unknown gender.

![gender_commits](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/gender_commits_1.png)

There was also a discrepancy in the average number of commits made by each of the three groups. Male-named developers in the dataset made thirteen more commits than female-named developers on average, and ten more commits than developers of unknown gender.

![average_commits](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/average_commits.png)

#### From commits to users

If we simply count the number of developers rather than the number of commits the picture is similar, but with a slightly smaller disparity between groups. Of the GitHub user accounts in the dataset, the breakdown is as follows:

***Contributors to the top 100 cryptocurrency projects:***

| male-named | female-named | unknown | total|
| ---- | ------ | ------- | ------- |
| 5062 | 417    | 3313    |8792|

![user_gender](/home/corin/Dropbox/CODE/RC/Crypto-Scraper/images/gender_usernames_1.png)

As the chart above shows, developers of unknown gender now make up a higher proportion of the total. In most cases these developers had simply not provided information for the `name` field of their GitHub profile; in a smaller number of cases, developers entered a name of ambiguous gender, or for which gender could not be inferred.

An open question is what we can assume about the gender of developers who choose not to enter a real name—for example, in a male-dominated field, are women more likely to obscure their real name to avoid discrimination?



As one study found, female-named developers were more likely to have contributions to open source project accepted. [LINK]



### Individual projects

The discrepancy in gender balance is more or less consistent across projects, but with some outliers.

The project with the highest percentage of commits by female-named users was X.

The project with the worst gender imbalance was Y.





### Limitations

...of the GitHub API

**CHECK: ** Using this method, we obtain data about the top 100 contributors to the `master` branch of each repo. This is all GitHub's API will return. Most projects have fewer than 100 contributors. (Could test how many)

Also: why in some cases is a single repo owner not counted as a contributor? Something to do with the age of accounts - after a certain time period, these contributions simply do not show up.

<https://github.com/bancorprotocol/contracts/graphs/contributors>

...of the project in general

- We counted commits, not lines of code. Different developers and organizations have different styles of committing, so number of commits is only a rough proxy for contribution to a project. However, counting the number of lines of code is also only a proxy—a bug fix that requires only three lines of code may represent many hours of work to arrive at the appropriate solution.
  - [Motherboard](https://motherboard.vice.com/en_us/article/8xz9yk/the-sexist-trolls-doubting-black-hole-researcher-katie-bouman-need-to-learn-to-code) - Trolls doubted how many code commits were made by the lead black hole researcher.
- Parsing names - we count just the male/female, not the probability.
- Are women more or less likely to enter a real name? (Pull requests more frequently accepted...)