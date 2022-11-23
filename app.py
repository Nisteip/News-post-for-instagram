from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    url = "https://www.businesstoday.in/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    outerdata = (soup.find_all("div", class_ = "bn_item_title", limit = 7))
    finalNews = []
    for data in outerdata:
        news = data.h3.a["title"]
        #finalNews += "\u2022 " + news + "\n"
        finalNews.append(news)

    return render_template("index.html", News = finalNews)