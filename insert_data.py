import requests
from src.infra.config import DBConnectionHandler


def count_articles():
    data = requests.get("https://api.spaceflightnewsapi.net/v3/articles/count")
    return data.json()


qtd_articles = count_articles()


def find_articles(limit, start):
    url = (
        f"https://api.spaceflightnewsapi.net/v3/articles?_limit={limit}&_start={start}"
    )
    data = requests.get(url)
    return data.json()


start = 0
limit = 200


with DBConnectionHandler() as connection:
    collection = connection.get_collection("spaceFlight")

    while limit + start <= qtd_articles:
        collection.insert_many(find_articles(limit, start))
        start = limit + start
        print(start)

    print(qtd_articles)
    collection.insert_many(find_articles(qtd_articles, start))
