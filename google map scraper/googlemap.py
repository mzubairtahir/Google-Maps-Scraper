from selenium import webdriver
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

link=''  #link
driver.get(link)

sleep(5)
print('checking start...')

try: #it will scroll down the results
    element=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[1]')
except:
    print('Not found')
else:
    initialPos=0
    for i in range(1,201):  #*2
        driver.execute_script(f'arguments[0].scroll({initialPos},{i*300});',element)
        initialPos=i*300
        sleep(3)

sleep(2)
try:
    allResults=driver.find_elements_by_class_name('hfpxzc')  #all the hotels
except:
    print('hotels not found')
else:
    print(f'Total elements found: {len(allResults)}')

    for i in allResults:
        i.click()
        try:
            sleep(3)
            explainResults=driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div')
        except:
            print('Explain Results not found...')
        else:
            sleep(8)
            html=explainResults.get_attribute('outerHTML')
            soup=BeautifulSoup(html,'html.parser') #soup of explain page
            name=soup.find('h1',class_='DUwDvf fontHeadlineLarge').text.strip()
            allInfoBars=soup.find_all('div',class_='AeaXub')
            for j in allInfoBars:
                link=j.find('img').get('src')
                text=j.text

                if link==locationLink:
                    address=text.strip()
                
                elif link==websiteLink:
                    website=text.strip()

                elif link==phoneLink:
                    phone=text.strip()


                else:
                    pass

            data={
                'Name':name,
                'Address':address,
                'Website':website,
                'Phone':phone
            }

            finalData.append(data)



dataFrame=pd.DataFrame(finalData)
dataFrame.to_excel('Hotels.xlsx',index=False)
logo()


# driver.close()



