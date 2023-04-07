from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd






#==========================================
#Your inputs:
'''
Here you will insert link of page of google maps, having search results, that you want to scrape
'''


link_of_page=""    # <---- link of page
number_of_scrolls=10  
output_format= 0    # <---  it can be 0(excel) 1(csv)


#==========================================

''' 
These links are used to fetch exact data from info fields of that particular place.
Look below for better understanding of use of these links
'''

locationLink='''//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png'''
phoneLink='''//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png'''
websiteLink='''//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png'''

#==========================================

finalData=[]   #in which our final records will be append

#===================================

def logo():
    logoVar='''

    ★彡[ꜱᴄʀᴀᴘᴇʀ ʙʏ M ᴢᴜʙᴀɪʀ Tahir!]彡★

    '''

    print(logoVar)
#==================================

option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(options=option)

driver.implicitly_wait(10)
driver.get(link_of_page)

sleep(5)
print('working start...')

def parsing():
    try:
        sleep(3)
        infoSheet=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div')
    except:
        print('Explain Results not found...')
    else:
        sleep(3)
        data={}

        html=infoSheet.get_attribute('outerHTML')
        soup=BeautifulSoup(html,'html.parser') #soup of info page of that place
        name=soup.find('h1',class_='DUwDvf fontHeadlineLarge').text.strip()
        data.update({'Name':name})
        
        allInfoBars=soup.find_all('div',class_='AeaXub')

        
        for infoBar in allInfoBars:
            

            link=infoBar.find('img').get('src')
            text=infoBar.text

            if link==locationLink:
                data.update({'Address':text.strip()})

            
            elif link==websiteLink:
                data.update({'website':text.strip()})


            elif link==phoneLink:
                data.update({'phone':text.strip()})
                


            else:
                pass

        finalData.append(data)




try:   #it will scroll down the results
    element=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[1]')
except:
    element=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[1]')  #again found
else:
    initialPos=0
    for i in range(1,number_of_scrolls):  #*2
        driver.execute_script(f'arguments[0].scroll({initialPos},{i*300});',element)
        initialPos=i*300
        sleep(2)

try:
    allResults=driver.find_elements_by_class_name('hfpxzc')  #all the places in result
except:
    allResults=driver.find_elements_by_class_name('hfpxzc')  #re-founding
    
else:
    print(f'Total places found: {len(allResults)}')

    for i in allResults:
        sleep(1)
        try:
            i.click()

        except:
            try:
                i.send_keys(Keys.RETURN)
            except:
                continue # if any place's card is not clickable
            else:
                parsing()
                
            

        else:
            parsing()
        



dataFrame=pd.DataFrame(finalData)
if output_format==0:
    dataFrame.to_excel('output.xlsx',index=False)
elif output_format==1:
    dataFrame.to_csv('output.xlsx',index=False)

logo()


driver.close()



