#https://www.google.com/search?q=weather+manalapan&sca_esv=56f381dcf9f4ef77&sxsrf=ADLYWIIJjTbi4G3bXv9zzz9_V8X6SLV48A%3A1736643192900&source=hp&ei=eBKDZ6nNNLOHptQPhqPngQc&iflsig=AL9hbdgAAAAAZ4MgiOk67jjKqDp2ikdvvmlZgm689k1S&ved=0ahUKEwip6fKE_O6KAxWzg4kEHYbROXAQ4dUDCBk&uact=5&oq=weather+manalapan&gs_lp=Egdnd3Mtd2l6IhF3ZWF0aGVyIG1hbmFsYXBhbjIQEAAYgAQYsQMYgwEYRhiAAjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESOQdUABYtxtwAHgAkAEBmAH9BKABhRaqAQsyLjIuNC4xLjEuMbgBA8gBAPgBAZgCCKACpgzCAgoQIxiABBgnGIoFwgILEAAYgAQYsQMYgwHCAg4QLhiABBixAxjRAxjHAcICCxAuGIAEGLEDGNQCwgIIEAAYgAQYsQPCAhEQLhiABBixAxjRAxiDARjHAcICCBAuGIAEGLEDwgITEC4YgAQYsQMY0QMYxwEYigUYCsICCxAAGIAEGJIDGIoFmAMAkgcHMi4yLjMuMaAHtms&sclient=gws-wiz
#User agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0
# span id = womb_tm
from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    query = "manalapan"
    url = f'https://www.google.com/search?q=weather+{query}&sca_esv=56f381dcf9f4ef77&sxsrf=ADLYWIIJjTbi4G3bXv9zzz9_V8X6SLV48A%3A1736643192900&source=hp&ei=eBKDZ6nNNLOHptQPhqPngQc&iflsig=AL9hbdgAAAAAZ4MgiOk67jjKqDp2ikdvvmlZgm689k1S&ved=0ahUKEwip6fKE_O6KAxWzg4kEHYbROXAQ4dUDCBk&uact=5&oq=weather+manalapan&gs_lp=Egdnd3Mtd2l6IhF3ZWF0aGVyIG1hbmFsYXBhbjIQEAAYgAQYsQMYgwEYRhiAAjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESOQdUABYtxtwAHgAkAEBmAH9BKABhRaqAQsyLjIuNC4xLjEuMbgBA8gBAPgBAZgCCKACpgzCAgoQIxiABBgnGIoFwgILEAAYgAQYsQMYgwHCAg4QLhiABBixAxjRAxjHAcICCxAuGIAEGLEDGNQCwgIIEAAYgAQYsQPCAhEQLhiABBixAxjRAxiDARjHAcICCBAuGIAEGLEDwgITEC4YgAQYsQMY0QMYxwEYigUYCsICCxAAGIAEGJIDGIoFmAMAkgcHMi4yLjMuMaAHtms&sclient=gws-wiz'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'})
    temp =r.html.find('span#wob_tm', first=True).text
    #print(temp)
    unit =r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    #print(unit)
    desc= r.html.find('span#wob_dc', first=True).text
    #print(desc)
    return temp+" " + unit + " " + desc
