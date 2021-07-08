from django.shortcuts import render, redirect
from selenium.webdriver.common import service
from .models import OwnShoes, ShoesDataset
from django_API import my_settings
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#1. download webdriver which should be correct version
#2. setting webriver.exe file path and fit executable_path
def get_review_data(request):
    driver  = webdriver.Chrome(executable_path=my_settings.CHROME_WEBDRIVER_PATH)
    
    reviewer_hash = {}
    brand = '나이키'
    search_pages = 1 # 5
    for i in range(1, search_pages+1):
        driver.get(f'https://search.musinsa.com/search/musinsa/goods?q={brand}+운동화&list_kind=small&sortCode=pop&sub_sort=&page={i}&display_cnt=0&saleGoods=&includeSoldOut=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&saleCampaign=false&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&d_cat_cd=')
        
        goods_id = []
        goods_amount = 5 # 90
        for i in range(1, goods_amount+1):
            goods_elem = None
            url = None
            
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
                _id = url.strip('https://store.musinsa.com/app/goods/')
                goods_id.append(_id)
        
        for _id in goods_id:
            review_url = f'https://store.musinsa.com/app/reviews/goods_estimate_list/goods/{_id}/0/1?similar_no=&select_similar_no=&is_cache=N&sort=new'
            driver.get(review_url)
            review_pages = None
            try:
                review_pages_elem = driver.find_element_by_xpath(f'//*[@class="box_page_msg"]')
                review_pages_elem = review_pages_elem.get_attribute('textContent')
                review_pages = int(review_pages_elem.split(' ')[0])
                
            except:
                pass
            if review_pages:
                for i in range(1, review_pages+1):
                    review_url = f'https://store.musinsa.com/app/reviews/goods_estimate_list/goods/{_id}/0/{i}?similar_no=&select_similar_no=&is_cache=N&sort=new'
                    driver.get(review_url)
                    reviews_amount = 10
                    for i in range(1, reviews_amount+1):
                        try:
                            reviewer_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[1]/a')
                            reviewer_elem = reviewer_elem.get_attribute('href').split('hash_id=')[1]
                            reviewer_elem = reviewer_elem.split('&type')[0]
                            reviewer_hash[reviewer_elem] = {}
                        except:
                            pass
                        
                        try:
                            model_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div[2]/a')
                            model_elem = model_elem.get_attribute('text')
                            model_elem = model_elem.strip()
                            reviewer_hash[reviewer_elem]['model_name'] = str(model_elem)
                        except:
                            pass
                        
                        try:
                            size_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[2]/div[2]/p/span')
                            size_elem = size_elem.get_attribute('textContent')
                            size_elem = size_elem.strip()
                            reviewer_hash[reviewer_elem]['shoe_size'] = str(size_elem)
                        except:
                            pass
                        
                        try:
                            size_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[4]/div[2]/ul/li[1]/span')
                            size_review_elem = size_review_elem.get_attribute('textContent')
                            size_review_elem = size_review_elem.strip()
                            reviewer_hash[reviewer_elem]['size_review'] = str(size_review_elem)
                        except:
                            pass
                        
                        try:
                            ball_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[4]/div[2]/ul/li[4]/span')
                            ball_review_elem = ball_review_elem.get_attribute('textContent')
                            ball_review_elem = ball_review_elem.strip()
                            reviewer_hash[reviewer_elem]['ball_review'] = str(ball_review_elem)
                        except:
                            pass
                        
                        try:
                            comfort_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[4]/div[2]/ul/li[5]/span')
                            comfort_review_elem = comfort_review_elem.get_attribute('textContent')
                            comfort_review_elem = comfort_review_elem.strip()
                            reviewer_hash[reviewer_elem]['comfort_review'] = str(comfort_review_elem)
                        except:
                            pass
                        
                        try:
                            comment_review_elem = driver.find_element_by_xpath(f'//*[@id="wrapEstimateList"]/div/div[{i}]/div[4]/div[1]')
                            comment_review_elem = comment_review_elem.get_attribute('textContent')
                            comment_review_elem = comment_review_elem.strip()
                            while True:
                                if '\n' not in comment_review_elem:
                                    break
                                comment_review_elem = comment_review_elem.replace('\n', ' ')
                            reviewer_hash[reviewer_elem]['comment_review'] = str(comment_review_elem)
                        except:
                            pass
    print(reviewer_hash)
    print(len(reviewer_hash))
    driver.close()
    return redirect("http://127.0.0.1:8000")

