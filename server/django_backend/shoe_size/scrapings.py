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
    goods_amount = 90 # 15행
    # //*[@id="searchList"]/li[1]/div[4]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[2]/div[4]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[3]/div[3]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[4]/div[3]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[5]/div[4]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[6]/div[3]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[7]/div[4]/div[2]/p[2]/a
    # //*[@id="searchList"]/li[8]/div[3]/div[2]/p[2]/a
    for i in range(1, goods_amount+1):
        try:
            if driver.find_element_by_xpath(f'//*[@id="searchList"]/li[{i}]/div[4]/div[2]/p[2]/a'):
                print("4")
                #goods_elem = driver.find_element_by_xpath(f'//*[@id="searchList"]/li[{i}]/div[4]/div[2]/p[2]/a')
            if driver.find_element_by_xpath(f'//*[@id="searchList"]/li[{i}]/div[3]/div[2]/p[2]/a'):
                print("3")
                #goods_elem = driver.find_element_by_xpath(f'//*[@id="searchList"]/li[{i}]/div[3]/div[2]/p[2]/a')
            
            #print(goods_elem.get_attribute('href'))
            #goods_url.append(goods_elem.get_attribute('href'))
        except:
            print("Goods Except Point: ", i)
    # driver.close()
    # print(goods_url)
    # print("legnth: ", len(goods_url))
    
    # driver.get(goods_url[1])
    
    # reviewer_hash = {}
    # for i in range(1, pages+1):
    #     try:
    #         reviewer_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[1]/a')
    #         reviewer_elem = reviewer_elem.get_attribute('href').split('hash_id=')[1]
    #         reviewer_elem = reviewer_elem.split('&type')[0]
    #         print(reviewer_elem)
    #         reviewer_hash[reviewer_elem] = {}
            
    #         model_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[2]/div[2]/div/a')
    #         print(model_elem)
    #         reviewer_hash[reviewer_elem]['model_name'] = str(model_elem)
            
    #         shoe_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[2]/div[2]/p')
    #         #size_elem = shoe_elem.split('(')[0]
    #         #standard_elem = shoe_elem.split('(')[0]
    #         reviewer_hash[reviewer_elem]['shoe_size'] = str(shoe_elem)
            
    #         size_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[1]')
    #         reviewer_hash[reviewer_elem]['size_review'] = str(size_review_elem)
            
    #         ball_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[4]')
    #         reviewer_hash[reviewer_elem]['ball_review'] = str(ball_review_elem)
            
    #         comfort_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[5]')
    #         reviewer_hash[reviewer_elem]['comfort_review'] = str(comfort_review_elem)
            
    #         comment_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[5]/div[1]/div/div[1]/span')
    #         reviewer_hash[reviewer_elem]['comment_review'] = str(comment_review_elem)
            
    #     except:
    #         print("Review Except Point: ", i)
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

