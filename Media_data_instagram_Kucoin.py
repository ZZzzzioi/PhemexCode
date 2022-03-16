#coding:utf-8
import pygsheets
import pandas as pd
import numpy as np
from selenium import webdriver
import time
import datetime

#get_Youtube_data
def get_youtube_data(driver, url_youtube):
    driver.get(url_youtube)
    time.sleep(3)
    ytb_subscribers = driver.find_element_by_xpath('/html/body/div[12]/div/div[3]/div[3]/span[2]').text.replace('K', '').replace(' ', '')
    ytb_video_views = driver.find_element_by_xpath('/html/body/div[12]/div/div[3]/div[4]/span[2]').text.replace(' ', '')
    time.sleep(3)
    ytb_subscriber_rank = driver.find_element_by_xpath('/html/body/div[17]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/p').text.replace('st', '').replace(' ', '').replace('th', '')
    ytb_video_views_rank = driver.find_element_by_xpath('/html/body/div[17]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/p').text.replace('th', '').replace(' ', '').replace('st', '')
    return driver, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank

#get_Instagram_data
def get_instagram_data(driver, url_instagram):
    time.sleep(3) 
    driver.get(url_instagram)    
    time.sleep(5) 
    itg_followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span').get_attribute('title')
    return driver, itg_followers

#get_Facebook_data
def get_facebook_data(driver, url_facebook):
    driver.get(url_facebook)
    time.sleep(2)
    fb_page_likes = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[2]/p[3]').text.replace(' page likes', '').replace(' ', '')
    fb_talking_about = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[2]/p[4]').text.replace(' talking about this', '').replace(' ', '')
    return driver, fb_page_likes, fb_talking_about

#get_twitter_data
def get_twitter_data(driver, url_twitter):
    time.sleep(3)
    driver.get(url_twitter)
    time.sleep(30)
    tw_followers = driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[3]/div[2]/span[2]').text.replace(' ', '')
    tw_likes = driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[3]/div[4]/span[2]').text.replace(' ', '')
    tw_tweets = driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[3]/div[5]/span[2]').text.replace(' ', '')
    return driver, tw_followers, tw_likes, tw_tweets

#get_Telegram_data
def get_telegram_data(driver, url_telegram):
    driver.get(url_telegram)
    time.sleep(10)
    tg_information = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]').text
    tg_information_list = tg_information.split(',')
    tg_members = tg_information_list[0].replace('members', '').replace(' ', '')
    tg_online = tg_information_list[1].replace('online', '').replace('', '')
    return driver, tg_members, tg_online

def get_data(driver, url_ytb, url_facebook, url_twitter, url_telegram = None):
    #get_data
    try:
        driver, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank = get_youtube_data(driver, url_ytb)
    except:
        ytb_subscribers = ytb_video_views = ytb_subscriber_rank = ytb_video_views_rank = None
    
    try:
        driver, fb_page_likes, fb_talking_about = get_facebook_data(driver, url_facebook)
    except:
        fb_page_likes = fb_talking_about = None
    
    try:
        driver, tw_followers, tw_likes, tw_tweets = get_twitter_data(driver, url_twitter)
    except:
        tw_followers = tw_likes = tw_tweets = None
    time.sleep(3)
    try:
        driver, tg_members, tg_online = get_telegram_data(driver, url_telegram)
    except:
        tg_members = tg_online = None
    

    #get_date
    Media_data = pd.DataFrame()
    ISOTIMEFORMAT = '%Y-%m-%d' #define time format
    start_date = datetime.datetime.strptime('2021-07-05', ISOTIMEFORMAT)
    now_date = datetime.datetime.now()
    row_index = (now_date - start_date).days+2
    date = datetime.datetime.strftime(now_date, ISOTIMEFORMAT)

    Media_data = [date, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank, 
                fb_page_likes, fb_talking_about, 
                tw_followers, tw_likes, tw_tweets,
                tg_members, tg_online]
    return driver, Media_data, row_index


def get_Deribit_data(driver, url_ytb, url_facebook, url_twitter, url_telegram = None):
    #get_data
    try:
        driver, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank = get_youtube_data(driver, url_ytb)
    except:
        ytb_subscribers = ytb_video_views = ytb_subscriber_rank = ytb_video_views_rank = None
    
    try:
        driver, fb_page_likes, fb_talking_about = get_facebook_data(driver, url_facebook)
    except:
        fb_page_likes = fb_talking_about = None
    
    try:
        driver, tw_followers, tw_likes, tw_tweets = get_twitter_data(driver, url_twitter)
    except:
        tw_followers = tw_likes = tw_tweets = None
    time.sleep(3)
    try:
        driver, tg_members, tg_online = get_telegram_data(driver, url_telegram)
    except:
        tg_members = tg_online = None
    

    #get_date
    Media_data = pd.DataFrame()
    ISOTIMEFORMAT = '%Y-%m-%d' #define time format
    start_date = datetime.datetime.strptime('2021-08-09', ISOTIMEFORMAT)
    now_date = datetime.datetime.now()
    row_index = (now_date - start_date).days+2
    date = datetime.datetime.strftime(now_date, ISOTIMEFORMAT)

    Media_data = [date, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank, 
                fb_page_likes, fb_talking_about, 
                tw_followers, tw_likes, tw_tweets,
                tg_members, tg_online]
    return driver, Media_data, row_index


def get_kucoin_data(driver, url_ytb, url_facebook, url_twitter, url_telegram = None):
    #get_data
    try:
        driver, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank = get_youtube_data(driver, url_ytb)
    except:
        ytb_subscribers = ytb_video_views = ytb_subscriber_rank = ytb_video_views_rank = None
    
    try:
        driver, fb_page_likes, fb_talking_about = get_facebook_data(driver, url_facebook)
    except:
        fb_page_likes = fb_talking_about = None
    
    try:
        driver, tw_followers, tw_likes, tw_tweets = get_twitter_data(driver, url_twitter)
    except:
        tw_followers = tw_likes = tw_tweets = None
    time.sleep(3)
    try:
        driver, tg_members, tg_online = get_telegram_data(driver, url_telegram)
    except:
        tg_members = tg_online = None
    

    #get_date
    Media_data = pd.DataFrame()
    ISOTIMEFORMAT = '%Y-%m-%d' #define time format
    start_date = datetime.datetime.strptime('2021-12-14', ISOTIMEFORMAT)
    now_date = datetime.datetime.now()
    row_index = (now_date - start_date).days+2
    date = datetime.datetime.strftime(now_date, ISOTIMEFORMAT)

    Media_data = [date, ytb_subscribers, ytb_video_views, ytb_subscriber_rank, ytb_video_views_rank, 
                fb_page_likes, fb_talking_about, 
                tw_followers, tw_likes, tw_tweets,
                tg_members, tg_online]
    return driver, Media_data, row_index


def gsheet(token, sheet_index, data, row_index):
    #open the google spreadsheet ('pysheeetsTest' exists)
    Phemex_sheet = token.open('Media_data')
    #select the first sheet
    Phemex_work_space = Phemex_sheet[sheet_index]
    #Phemex_sheet.add_worksheet('test') add a new sheet

    #update the first sheet with df, starting at cell B2
    Phemex_work_space.update_row(row_index, data)


def main():
    exchanges = {}
    exchanges['Phemex'] = ['https://socialblade.com/youtube/c/phemex', 'https://socialblade.com/facebook/page/phemex.official',
                            'https://socialblade.com/twitter/user/phemex_official', 'https://www.instagram.com/phemexofficial/',
                            'https://t.me/Phemex_EN']
    #tg, fb, tw, itg
    exchanges['Binance'] = ['https://t.me/BinanceExchange', 'https://socialblade.com/facebook/page/binance',
                            'https://socialblade.com/twitter/user/binance', 'https://socialblade.com/instagram/user/binance',
                            'https://socialblade.com/youtube/c/binanceyoutube']
    #tg, tw, fb, itg, ytb
    exchanges['OKEx'] = ['https://t.me/OKXOfficial_English', 'https://socialblade.com/twitter/user/okx',
                        'https://socialblade.com/facebook/page/okx', 'https://socialblade.com/instagram/user/okex_exchange',
                        'https://socialblade.com/youtube/c/okxcryptoexchange']
    #tg, tw, ytb, fb, itg
    exchanges['Huobi'] = ['https://t.me/huobiglobalofficial', 'https://socialblade.com/twitter/user/huobiglobal',
                        'https://socialblade.com/youtube/c/huobiglobal', 'https://socialblade.com/instagram/user/huobiglobalofficial',
                        'https://socialblade.com/facebook/page/huobiglobalofficial']
    #tw, tg, fb, itg, ytb
    exchanges['Bybit'] = ['https://socialblade.com/twitter/user/bybit_official', 'https://t.me/BybitEnglish',
                        'https://socialblade.com/facebook/page/bybit', 'https://socialblade.com/instagram/user/bybit_official',
                        'https://socialblade.com/youtube/c/bybit']
    #tg, tw, fb
    exchanges['FTX'] = ['https://t.me/FTX_Official', 'https://socialblade.com/twitter/user/ftx_official',
                        'https://socialblade.com/facebook/page/ftx.official']
    #fb, tw, itg
    exchanges['Coinbase'] = ['https://socialblade.com/facebook/page/coinbase', 'https://socialblade.com/twitter/user/coinbase',
                            'https://socialblade.com/instagram/user/coinbase']
    
    exchanges['Deribit'] = ['https://socialblade.com/youtube/c/deribit', 'https://socialblade.com/twitter/user/deribitexchange', 
                            'https://socialblade.com/facebook/page/deribitexchange', 'https://socialblade.com/instagram/user/deribitexchange',
                            'https://t.me/deribit']
    exchanges['Kucoin'] = ['https://socialblade.com/youtube/c/kucoinexchange', 'https://socialblade.com/twitter/user/kucoincom',
                            'https://socialblade.com/facebook/page/kucoin', 'https://t.me/Kucoin_Exchange']
    
    
    option = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    option.add_experimental_option("prefs", prefs) 
    option.add_argument('--start-maximized') # 最大化运行（全屏窗口）设置元素定位比较准确
    option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36')

    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://socialblade.com/')
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[6]/div/li[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[10]/div[2]/form/div[1]/input[1]').send_keys('Zisheng.ji@Phemex.com')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[10]/div[2]/form/div[2]/input').send_keys('Iieng@9737')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[10]/div[2]/form/div[3]/input').click()
    time.sleep(3)
    driver, Phemex, row_index_PH = get_data(driver, url_ytb = exchanges['Phemex'][0], url_facebook = exchanges['Phemex'][1], 
                                url_twitter = exchanges['Phemex'][2], url_telegram = exchanges['Phemex'][4])
    time.sleep(3)
    driver, Binance, row_index_BI = get_data(driver, url_ytb = exchanges['Binance'][4], url_facebook = exchanges['Binance'][1], 
                                url_twitter = exchanges['Binance'][2], url_telegram = exchanges['Binance'][0])
    time.sleep(3)
    driver, OKEx, row_index_OK = get_data(driver, url_ytb = exchanges['OKEx'][4], url_facebook = exchanges['OKEx'][2],
                                url_twitter = exchanges['OKEx'][1], url_telegram = exchanges['OKEx'][0])
    time.sleep(3)
    driver, Huobi, row_index_HB = get_data(driver, url_ytb = exchanges['Huobi'][2], url_facebook = exchanges['Huobi'][4],
                                url_twitter = exchanges['Huobi'][1], url_telegram = exchanges['Huobi'][0])
    time.sleep(3)
    driver, Bybit, row_index_BB = get_data(driver, url_ytb = exchanges['Bybit'][4], url_facebook = exchanges['Bybit'][2], 
                                url_twitter = exchanges['Bybit'][0], url_telegram = exchanges['Bybit'][1])
    time.sleep(3)
    driver, FTXs, row_index_FTX = get_data(driver, url_ytb = None, url_facebook = exchanges['FTX'][2],
                                url_twitter = exchanges['FTX'][1], url_telegram = exchanges['FTX'][0])
    time.sleep(3)
    driver, Coinbase, row_index_CB = get_data(driver, url_ytb = None, url_facebook = exchanges['Coinbase'][0], 
                                url_twitter = exchanges['Coinbase'][1], url_telegram = None)
    time.sleep(3)
    driver, Deribit, row_index_DB = get_Deribit_data(driver, url_ytb = exchanges['Deribit'][0], url_facebook = exchanges['Deribit'][2],
                                url_twitter = exchanges['Deribit'][1], url_telegram = exchanges['Deribit'][4])
    time.sleep(3)
    driver, Kucoin, row_index_DB = get_kucoin_data(driver, url_ytb = exchanges['Kucoin'][0], url_facebook = exchanges['Kucoin'][2],
                                url_twitter = exchanges['Kucoin'][1], url_telegram = exchanges['Kucoin'][3])
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(15)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys('nnull5382') #nnull5382  antonio@123
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys('antonio@123')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div[1]/div/form/div/div[3]').click()
    time.sleep(10)
    phemex_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/phemexofficial/')
    time.sleep(5)
    binance_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/binance/')                                                                      
    time.sleep(5)
    okex_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/okx_official/')
    time.sleep(5)
    huobi_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/huobiglobalofficial/')
    time.sleep(5)
    bybit_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/bybit_official/')
    time.sleep(5)
    ftx_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/ftx_official/')
    time.sleep(5)
    coinbase_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/coinbase/')
    time.sleep(5)
    deribit_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/deribitexchange/')
    time.sleep(5)
    kucoin_itg_followers = get_instagram_data(driver, 'https://www.instagram.com/kucoinexchange/')
    time.sleep(5)
    driver.quit()
    #get_data finish
    Phemex.insert(5, phemex_itg_followers[1])
    Binance.insert(5, binance_itg_followers[1])
    OKEx.insert(5, okex_itg_followers[1])
    Huobi.insert(5, huobi_itg_followers[1])
    Bybit.insert(5, bybit_itg_followers[1])
    FTXs.insert(5, ftx_itg_followers[1])
    Coinbase.insert(5, coinbase_itg_followers[1])
    Deribit.insert(5, deribit_itg_followers[1])
    Kucoin.insert(5, kucoin_itg_followers[1])

    token = pygsheets.authorize(service_file='D:\\Code\\Media_data\\token.json') #C:\CodeStorage\PY_Code\spider
    gsheet(token, 0, Phemex, row_index_PH)
    gsheet(token, 1, Binance, row_index_BI)
    gsheet(token, 2, OKEx, row_index_OK)
    gsheet(token, 3, Huobi, row_index_HB)
    gsheet(token, 4, Bybit, row_index_BB)
    gsheet(token, 5, FTXs, row_index_FTX)
    gsheet(token, 6, Coinbase, row_index_CB)
    gsheet(token, 7, Deribit, row_index_DB)
    gsheet(token, 8, Kucoin, row_index_DB)


if __name__ == '__main__':
    main()