import requests
import bs4

def get_tor_session():
    session = requests.session()
    session.proxies = {
        "http":"socks5://127.0.0.1:9050",
        "https":"socks5://127.0.0.1:9050"
    }

    return session

session = get_tor_session()
url2 = "http://httpbin.org/ip"
url = "https://www.ac04.tamacc.chuo-u.ac.jp/ActiveCampus/module/Login.php"
data = {
    "mode":"Login",
    "clickcheck":0,
    "login":"18D8104032K",
    "passwd":"kishimoto1"
}

res = session.post(url,data=data)
res.raise_for_status

soup = bs4.BeautifulSoup(res.text,"html.parser")
soup = str(soup)

if "失敗" in soup:
    print("password is wrong")
else:
    print("connection sucsess")
