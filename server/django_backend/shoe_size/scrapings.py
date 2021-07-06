from django.shortcuts import render, redirect
from .models import OwnShoes, ShoesDataset
from django_API import my_settings
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#1. download webdriver which should be correct version
#2. setting webriver.exe file path and fit executable_path
def get_data(request):
    driver  = webdriver.Chrome(executable_path=my_settings.CHROME_WEBDRIVER_PATH)
    
    search_pages = 5
    brand = '나이키'
    driver.get(f'https://search.musinsa.com/search/musinsa/goods?q={brand}+운동화&list_kind=small&sortCode=pop&sub_sort=&page=2&display_cnt=0&saleGoods=&includeSoldOut=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&saleCampaign=false&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&d_cat_cd=')
    
    goods_url = []
    goods_amount = 90
    for i in range(1, goods_amount+1):
        try:
            try:
                goods_elem = driver.find_element_by_xpath(f'//*[@id="searchList"]/li[{i}]/div[4]/div[2]/p[2]/a')
                url = goods_elem.get_attribute('href')
            except:
                pass
            try:
                goods_elem = driver.find_element_by_xpath(f'//*[@id="searchList"]/li[{i}]/div[3]/div[2]/p[2]/a')
                url = goods_elem.get_attribute('href')
            except:
                pass
            
            if url:
                goods_url.append(url)
        except:
            print("Goods Except Point: ", i)
    
    print(goods_url)
    print("legnth: ", len(goods_url))
    
    driver.get(goods_url[2])
    
    reviewer_hash = {}
    reviews_amount = 1
    for i in range(1, reviews_amount+1):
        try:
            reviewer_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[1]/a')
            reviewer_elem = reviewer_elem.get_attribute('href').split('hash_id=')[1]
            reviewer_elem = reviewer_elem.split('&type')[0]
            print(reviewer_elem)
            reviewer_hash[reviewer_elem] = {}
            model_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div[2]/a')
            model_elem = model_elem.get_attribute('text')
            print(model_elem)
            reviewer_hash[reviewer_elem]['model_name'] = str(model_elem)
            
            size_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[2]/div[2]/div[2]/p/span')
            size_elem = size_elem.get_attribute('text')
            reviewer_hash[reviewer_elem]['shoe_size'] = str(size_elem)
            
            size_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[1]')
            size_review_elem = size_review_elem.get_attribute('text')
            reviewer_hash[reviewer_elem]['size_review'] = str(size_review_elem)
            
            ball_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[4]')
            ball_review_elem = ball_review_elem.get_attribute('text')
            reviewer_hash[reviewer_elem]['ball_review'] = str(ball_review_elem)
            
            comfort_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[5]')
            comfort_review_elem = comfort_review_elem.get_attribute('text')
            reviewer_hash[reviewer_elem]['comfort_review'] = str(comfort_review_elem)
            
            comment_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[5]/div[1]/div/div[1]/span')
            comment_review_elem = comment_review_elem.get_attribute('text')
            reviewer_hash[reviewer_elem]['comment_review'] = str(comment_review_elem)
            
        except:
            print("Review Except Point: ", i)
    print(reviewer_hash)
    # hash id(리뷰작성자)
    # //*[@id="wrapEstimateList"]/div/div[1]/div[1]/a
    # //*[@id="wrapEstimateList"]/div/div[2]/div[1]/a

    # 모델이름
    # //*[@id="wrapEstimateList"]/div/div[1]/div[2]/div/div[2]/div[2]/div/a
    # //*[@id="wrapEstimateList"]/div/div[2]/div[2]/div/div[2]/div[2]/div/a

    # 구매 사이즈
    # //*[@id="wrapEstimateList"]/div/div[1]/div[2]/div/div[2]/div[2]/p
    # //*[@id="wrapEstimateList"]/div/div[2]/div[2]/div/div[2]/div[2]/p

    # 사이즈 리뷰
    # //*[@id="wrapEstimateList"]/div/div[1]/div[2]/div/div[4]/ul/li[1]
    # //*[@id="wrapEstimateList"]/div/div[2]/div[2]/div/div[4]/ul/li[1]

    # 발볼 리뷰
    # //*[@id="wrapEstimateList"]/div/div[1]/div[2]/div/div[4]/ul/li[4]
    # //*[@id="wrapEstimateList"]/div/div[2]/div[2]/div/div[4]/ul/li[4]

    # 착화감 리뷰
    # //*[@id="wrapEstimateList"]/div/div[1]/div[2]/div/div[4]/ul/li[5]
    # //*[@id="wrapEstimateList"]/div/div[2]/div[2]/div/div[4]/ul/li[5]

    # 리븊 코멘트
    # //*[@id="wrapEstimateList"]/div/div[1]/div[2]/div/div[5]/div[1]/div/div[1]/span
    # //*[@id="wrapEstimateList"]/div/div[2]/div[2]/div/div[5]/div[1]/div/div[1]/span
    #driver.close()
    return redirect('http://127.0.0.1:8000/')

