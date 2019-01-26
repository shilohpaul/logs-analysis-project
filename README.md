# Logs Analysis Project

This project accesses a database, called news, and answers three questions
about the information in the database which are:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1 percent of requests lead to errors?

## Contributors
The news database and newsdata.sql file were provided by Udacity. The
logs-analysis.py program was written by Shiloh Paul

## What You'll Need to Install

1. Download the data from Udacity and unzip the file: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2. Install python: https://www.python.org/downloads/release/python-361/
3. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
4. Install Vagrant: https://www.vagrantup.com/downloads.html

## Get Started

1. clone this repository
2. cd into the vagrant repository
3. Run `vagrant up`
4. Run `vagrant ssh`
5. cd into `\vagrant`
6. Run `psql -d news -f newsdata.sql` to load the news database and run the
code in the newsdata.sql file.
7. Run `python3 logs-analysis.py` from the command line.
