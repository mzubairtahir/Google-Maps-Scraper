from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(options=option)

driver.implicitly_wait(10)

#==========================================

locationLink='''//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png'''
phoneLink='''//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png'''
websiteLink='''//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png'''

#==========================================

finalData=[]
sleep(3)

#===================================

def logo():
    logoVar='''

    ★彡[ꜱᴄʀᴀᴘᴇʀ ʙʏ ᴢᴜʙᴀɪʀ!]彡★

    '''

    print(logoVar)
#==================================

link='https://www.google.com/maps/search/hotels+in+California,+USA/@35.0254043,-121.5368567,7z/data=!3m1!4b1'
driver.get(link)

sleep(5)
print('working start...')

def parsing():
    try:
        sleep(3)
        explainResults=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div')
    except:
        print('Explain Results not found...')
    else:
        sleep(3)
        data={}

        html=explainResults.get_attribute('outerHTML')
        soup=BeautifulSoup(html,'html.parser') #soup of explain page
        name=soup.find('h1',class_='DUwDvf fontHeadlineLarge').text.strip()
        data.update({'Name':name})
        
        allInfoBars=soup.find_all('div',class_='AeaXub')

        
        for j in allInfoBars:
            

            link=j.find('img').get('src')
            text=j.text

            if link==locationLink:
                # address=text.strip()
                data.update({'Address':text.strip()})

            
            elif link==websiteLink:
                # website=text.strip()
                data.update({'website':text.strip()})


            elif link==phoneLink:
                # phone=text.strip()
                data.update({'phone':text.strip()})
                


            else:
                pass
    #     data={
    #     'Name':name,
    #     'Address':address,
    #     'Website':website,
    #     'Phone':phone
    # }

        finalData.append(data)




try: #it will scroll down the results
    element=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[1]')
except:
    print('Not found')
else:
    initialPos=0
    for i in range(1,26):  #*2
        driver.execute_script(f'arguments[0].scroll({initialPos},{i*300});',element)
        initialPos=i*300
        sleep(2)

try:
    allResults=driver.find_elements_by_class_name('hfpxzc')  #all the hotels
except:
    print('hotels not found')
else:
    print(f'Total elements found: {len(allResults)}')

    for i in allResults:
        sleep(1)
        try:
            i.click()




        except:
            try:
                i.send_keys(Keys.RETURN)
            except:
                continue
            else:
                parsing()
                
            

        else:
            parsing()
        



dataFrame=pd.DataFrame(finalData)
dataFrame.to_excel('Hotelslast2.xlsx',index=False)
logo()


# driver.close()



