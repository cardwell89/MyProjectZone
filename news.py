import requests 


# https: //newsapi.org/
news_api_key="6f81efa391a242bc866aca2db6f64839"
url = f"http://newsapi.org/v2/top-headlines?country=sa&apiKey={news_api_key}"
main_page = requests.get(url).json()
article = main_page["articles"]
head = []
for ar in article:
    head.append(ar["description"])
    for i in range(6):
        print(f"{i + 1} {head[i]} \n")