import requests
import re
import json
from jsonpath import jsonpath

def wydm(header,url):
    response = requests.get(url, headers=header)  # 开始访问并获取响应
    html = response.content.decode()  # 返回相应的网页代码
    return html
def zz(html):
    a = re.findall(r'class="js_song" title="(.+)">', html) #开始匹配
    b = re.findall(r'<a herf=".+" title="(.+)"', html)
    c = dict(zip(a, b)) #修改为键值对进行查看
    return c
def js(html):
    db_json = json.loads(html)
    a = jsonpath(db_json, "$..songInfo.name")  # 开始获取
    b = jsonpath(db_json, "$..album.name")
    c = dict(zip(a, b))
    return c
if __name__=="__main__":
    # 身份头部信息
    header = {
        'cache-control': 'max-age=600',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    #请求访问的网页
    url = 'https://u.y.qq.com/cgi-bin/musics.fcg?-=getSingerSong997871313490255&g_tk=5381&sign=zzamzq122zmjerf6be8abd941f9f2b62c18f39dd6266e6&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerSongList%22%3A%7B%22method%22%3A%22GetSingerSongList%22%2C%22param%22%3A%7B%22order%22%3A1%2C%22singerMid%22%3A%220025NhlN2yWrP4%22%2C%22begin%22%3A0%2C%22num%22%3A10%7D%2C%22module%22%3A%22musichall.song_list_server%22%7D%7D'
    html=wydm(header,url)
    print(js(html))
