import requests
import json
from bs4 import BeautifulSoup
import tweepy
import time
import datetime

dt_now = datetime.datetime.now()
hh = dt_now.hour

def tweet(text):
    # 認証に必要なキーとトークン
    API_KEY = 'rDrE7RNmYwrFADBCWWaKwSkpn'
    API_SECRET = '3oTJodSMJ1wmyiL7E7Lgb412mSNRDw1izU1cQ9dnUBrCmIWige'
    ACCESS_TOKEN = '1406486692169609221-6TRkMfAoLYTxPS8oZSpZZFeNHZjxx2'
    ACCESS_TOKEN_SECRET = 'CyfwJOAsXlNtRdf1Wgj9n4RDgyXqZrwXStq5J4vYNt5mT'

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # キーワードからツイートを取得
    api = tweepy.API(auth)
    api.update_status(text)

team = {"阪神":"阪神タイガース",
        "巨人":"読売ジャイアンツ",
        "ヤクルト":"ヤクルトスワローズ",
        "DeNA":"横浜ベイスターズ",
        "中日":"中日ドラゴンズ",
        "広島":"広島東洋カープ",
        "ソフトバンク":"ソフトバンクホークス",
        "オリックス":"オリックスバファローズ",
        "楽天":"楽天ゴールデンイーグルス",
        "日本ハム":"日本ハムファイターズ",
        "ロッテ":"千葉ロッテマリーンズ",
        "西武":"西武ライオンズ"}

ho   = {"阪神":"とらほー",
        "巨人":"うさほー",
        "ヤクルト":"すわほー",
        "DeNA":"横浜優勝",
        "中日":"どらほー",
        "広島":"こいほー",
        "ソフトバンク":"たかほー",
        "オリックス":"おりほー",
        "楽天":"わしほー",
        "日本ハム":"はむほー",
        "ロッテ":"まりほー",
        "西武":"れおほー"}


twd = {"阪神":False,
        "巨人":False,
        "ヤクルト":False,
        "DeNA":False,
        "中日":False,
        "広島":False,
        "ソフトバンク":False,
        "オリックス":False,
        "楽天":False,
        "日本ハム":False,
        "ロッテ":False,
        "西武":False}


def live_scores():
    try:
        url = 'http://baseball.yahoo.co.jp/npb/schedule/'
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')

        games = soup.select('li.bb-score__item')

        for i in range(len(games)):
            score = games[i].find(class_ = 'bb-score__link').get_text()
            home = games[i].find(class_ = 'bb-score__homeLogo').get_text()
            away = games[i].find(class_ = 'bb-score__awayLogo').get_text()
            print(score,home,away)
            if score[:1] == "7":
                if score[-1:] == "表":
                    txt = "7回表" + team[away] + "のラッキーセブンでございます。 ファンの方、なおいっそうのご声援をお願いいたします。 #" + team[away] + " #" + ho[away]
                    if twd[away] == False:
                        tweet(txt)
                        twd[away] = True
                elif score[-1:] == "裏":
                    txt = "7回裏" + team[home] + "のラッキーセブンでございます。 ファンの方、なおいっそうのご声援をお願いいたします。 #" + team[home] + " #" + ho[home]
                    if twd[home] == False:
                        tweet(txt)
                        twd[home] = True
    except:
        pass


while True:
    dt_now = datetime.datetime.now()
    hh = dt_now.hour
    print(hh)
    if int(hh) > 12:
        live_scores()
    if int(hh) > 22:
        twd = {"阪神":False,
            "巨人":False,
            "ヤクルト":False,
            "DeNA":False,
            "中日":False,
            "広島":False,
            "ソフトバンク":False,
            "オリックス":False,
            "楽天":False,
            "日本ハム":False,
            "ロッテ":False,
            "西武":False}
        break
    time.sleep(60)
