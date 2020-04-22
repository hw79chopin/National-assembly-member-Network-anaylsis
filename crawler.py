# 의원님들 정보 크롤링

start_time = time.time()
list_date = []
list_bill = []
list_status = []
list_content = []
list_proposer = []
count = 0
for page in range(1, 250):
    driver.get('http://watch.peoplepower21.org/index.php?mid=Euian&show=1&page=' + str(page) + '&title=&rec_num=100&lname=&sangim=&bill_result=')
    print("{} 페이지 크롤링 시작!".format(page), '*'*170)
    for bill in range(1, 101):
        count +=1
        print('-'*10, '시작', '-'*10)
        if (driver.find_elements_by_css_selector('body')[0].text == 'XE cannot connect to DB.') | (driver.find_elements_by_css_selector('body')[0].text == 'DB鞐瓣舶 鞐愲煬!'): 
            driver.get('http://watch.peoplepower21.org/index.php?mid=Euian&show=1&page=' + str(page) + '&title=&rec_num=100&lname=&sangim=&bill_result=')
        bills = driver.find_elements_by_css_selector('tbody tr')
        temp_date = bills[bill-1].text.rsplit(")", 1)
        status = bills[bill-1].text.rsplit(' ', 1)[-1]
        list_status.append(status)
        string = ''
        for i in temp_date[:-1]:
            string = string + i + ')'
            temp = string.split(' ', 1)
            list_date.append(temp[0])
            list_bill.append(temp[1])
        driver.find_element_by_xpath('//*[@id="ea_list"]/table/tbody/tr[' + str(bill) + ']/td[2]/a').send_keys(Keys.ENTER)
        content = driver.find_elements_by_css_selector('#summaryContentDiv')
        if len(content)==0:
            list_content.append('내용없음')
        elif '\n' not in content[0].text :
            list_content.append(content[0].text)
        else:
            list_content.append(content[0].text.split('\n',1)[1].replace('\n',' '))
        proposer = driver.find_elements_by_css_selector('#collapseTwo > div > div > div')
        if len(proposer) == 0:
            list_proposer.append('내용없음')
        else:
            list_proposer.append(proposer[0].text.replace('\n', ' '))
        driver.back()
        print('{} 법안 크롤링 완료!'.format(temp[1]))
        if count % 100 == 0:
            print('총 {}개의 법안 크롤링 완료!'.format(count))
print("---{}초 걸렸슴둥---".format(time.time()-start_time))



# 의원님들 정보 크롤링
list_name = []
list_party = []
list_region = []
list_elected_times = []
list_committee = []
list_education = []
list_career = []
list_tel = []
list_email = []
list_bill_count = []
list_committee_attend = []
list_meeting_attend = []
list_property = []
for page in range(1,11):
    if page != 1:
        driver.get('http://watch.peoplepower21.org/?mid=AssemblyMembers&mode=search&party=&region=&sangim=&gender=&elect_num=&page=' + str(page))
    for person in range(1, 31):
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[' + str(person) + ']/div').click()
        
        full_name = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > h1')
        party = driver.find_elements_by_css_selector('div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(1) > td:nth-child(2)')
        region = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(2) > td:nth-child(2) > a')
        elected_times = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(3) > td:nth-child(2)')
        committee = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(4) > td:nth-child(2) > a')
        education = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(5) > td:nth-child(2)')
        career = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(6) > td:nth-child(2)')
        tel = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(7) > td:nth-child(2)')
        email = driver.find_elements_by_css_selector('#content > div > div > div > div.panel.panel-default > div.panel-body > div > div.col-md-9.col-lg-9 > table > tbody > tr:nth-child(8) > td:nth-child(2) > a')
        bill_count = driver.find_elements_by_css_selector('#collapse1 > div > h3 > span')
        committee_attend = driver.find_elements_by_css_selector('#collapse2 > div > span > span > span > span')
        meeting_attend = driver.find_elements_by_css_selector('#collapse3 > div > p:nth-child(3) > span > span > span > span')
        property_ = driver.find_elements_by_css_selector('#collapse5 > div > table > tbody > tr.info')
        if len(committee) != 0:
            list_committee.append(committee[0].text)
        else:
            list_committee.append(np.nan)
        if len(committee_attend) != 0:
            list_committee_attend.append(committee_attend[0].text)
        else:
            list_committee_attend.append(np.nan)
        if len(property_) != 0:
            list_property.append(property_[0].text)
        else:
            list_property.append(np.nan)
        list_name.append(full_name[0].text)
        list_party.append(party[0].text.split(' ', 1)[-1])
        list_region.append(region[0].text)
        list_elected_times.append(elected_times[0].text)
        list_education.append(education[0].text.replace('\n', '/'))
        list_career.append(career[0].text.replace('\n', '/'))
        list_tel.append(tel[0].text)
        list_email.append(email[0].text)
        list_bill_count.append(bill_count[0].text)
        list_meeting_attend.append(meeting_attend[0].text)
        driver.back()