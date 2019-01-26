import psycopg2

# 1. What are the most popular three articles of all time?
top_articles = """
SELECT articles.title, count(log.id) as num
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug) and log.status LIKE '%200%'
GROUP BY articles.title
ORDER BY num desc
LIMIT 3;"""

# 2. Who are the most popular article authors of all time?
popular_authors = """
SELECT authors.name, count(*) as num
FROM articles
JOIN authors on authors.id = articles.author
JOIN log ON log.path = CONCAT('/article/', articles.slug)
GROUP BY authors.name
ORDER BY num desc
LIMIT 4;
"""

# 3. On which days did more than 1% of requests lead to errors?
percent_errors = """
WITH logTotal AS(
SELECT time::date as LogDay, count(*)
AS requests
FROM log
GROUP BY time::date
ORDER BY time::date
),
errTotal AS(
SELECT time::date as ErrDay, count(*)
AS requests
FROM log
WHERE status like '%404%'
GROUP BY time::date
ORDER BY time::date
),
percentError AS(
SELECT logTotal.LogDay, round(cast((100*errTotal.requests) as numeric) / cast(logTotal.requests as numeric),2)
AS percent
FROM logTotal, errTotal
WHERE errTotal.ErrDay = logTotal.LogDay
)
SELECT * FROM percentError WHERE percent > 1.0;
"""

#Execute the query and return the results of the query
def execute_query_get_results(request):
    conn = psycopg2.connect("news")
    cursor = conn.cursor()
    cursor.execute(request)
    results = c.fetchall()
    conn.close()
    return results

results_articles = execute_query_get_results(top_articles)
results_authors = execute_query_get_results(popular_authors)
results_errors = execute_query_get_results(percent_errors)

#Print results of queries

def print_results(query):
    for i in range(len(query)):
        print ('\t' + str(query[i][0]) + ' | ' + str(query[i][1]))

print ("What are the most popular three articles of all time?")
print_results(results_articles)
print ("Who are the most popular article authors of all time?")
print_results(results_authors)
print("On which days did more than 1 percent of requests lead to errors?")
print_results(results_errors)
