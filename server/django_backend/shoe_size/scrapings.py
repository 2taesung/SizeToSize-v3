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
    
    brand = '나이키'
    driver.get(f'https://magazine.musinsa.com/?r=home&mod=search&keyword={brand}%20운동화')
    
    goods_no = []
    pages = 20
    for i in range(1, pages+1):
        try:
            goods_elem = driver.find_element_by_xpath(f'//*[@id="wrapper"]/div[2]/div[2]/div[3]/div/div[2]/ul/li[{i}]')
            goods_no.append(goods_elem.get_attribute('goods_no'))
        except:
            print("Goods Except Point: ", i)
    # driver.close()
    print(goods_no)
    print("legnth: ", len(goods_no))
    
    goods_id = goods_no[0]
    driver.get(f'https://store.musinsa.com/app/goods/{goods_id}')
    
    reviewer_hash = {}
    for i in range(1, pages+1):
        try:
            reviewer_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[1]/a')
            reviewer_elem = reviewer_elem.get_attribute('href').split('hash_id=')[1]
            reviewer_elem = reviewer_elem.split('&type')[0]
            print(reviewer_elem)
            reviewer_hash[reviewer_elem] = {}
            
            model_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[2]/div[2]/div/a')
            reviewer_hash[reviewer_elem]['model_name'] = str(model_elem)
            
            shoe_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[2]/div[2]/p')
            #size_elem = shoe_elem.split('(')[0]
            #standard_elem = shoe_elem.split('(')[0]
            reviewer_hash[reviewer_elem]['shoe_size'] = str(shoe_elem)
            
            size_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[1]')
            reviewer_hash[reviewer_elem]['size_review'] = str(size_review_elem)
            
            ball_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[4]')
            reviewer_hash[reviewer_elem]['ball_review'] = str(ball_review_elem)
            
            comfort_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[4]/ul/li[5]')
            reviewer_hash[reviewer_elem]['comfort_review'] = str(comfort_review_elem)
            
            comment_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div/div[5]/div[1]/div/div[1]/span')
            reviewer_hash[reviewer_elem]['comment_review'] = str(comment_review_elem)
            
        except:
            print("Review Except Point: ", i)
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
    driver.close()
    return redirect('http://127.0.0.1:8000/')

