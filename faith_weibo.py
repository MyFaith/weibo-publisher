# coding: utf-8

from weibo import Client
import requests
import json

APP_KEY = ''
APP_SECRET = ''
CALLBACK = ''
USERNAME = ''
PASSWORD = ''

def getClient(app_key, app_secret, call_back, username, password):
    client = Client(api_key=app_key, api_secret=app_secret, redirect_uri=call_back, username=username, password=password)
    return client

def getAir():
    url = 'http://apis.haoservice.com/air/cityair'
    formdata = {
        'key': '8d5ee679d76d400aaeaef7433a2539bf',
        'city': '天津',

    }
    result = requests.post(url, data=formdata).text
    json_data = json.loads(result)
    return json_data['result']

def getWeather():
    url = 'http://apis.haoservice.com/weather'
    formdata = {
        'key': '31861627bb4c479889fffa6ae08aedb9',
        'cityname': '天津'
    }
    result = requests.post(url, data=formdata).text
    json_data = json.loads(result)
    return json_data['result']

if __name__ == '__main__':
    c = getClient(APP_KEY, APP_SECRET, CALLBACK, USERNAME, PASSWORD)

    # -------------------获取空气质量-------------------
    airdata = getAir()
    # 城市
    city = airdata['CityName']
    # 空气质量
    quality = airdata['Quality']
    # PM2.5
    aqi = airdata['AQI']
    # 更新时间
    update_time = airdata['UpdateTime']
    # -------------------获取天气信息-------------------
    weatherdata = getWeather()
    # 星期
    week = weatherdata['today']['week']
    # 温度
    temperature = weatherdata['today']['temperature']
    # 天气
    weather = weatherdata['today']['weather']
    # 风向
    wind = weatherdata['today']['wind']
    # 更新时间
    date = weatherdata['today']['date_y']
    # -------------------发布微博-------------------
    weibo_content = u'今天是%s %s，%s，温度【%s】，%s，空气质量【%s】，PM2.5【%s】，更新时间【%s】'%(date, week, weather, temperature, wind, quality, aqi, update_time)
    c.post('statuses/update', status=weibo_content)






