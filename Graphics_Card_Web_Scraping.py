import urllib.request
import csv
from lxml import etree
from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
    
def main():
    
    default_url = 'https://whattomine.com/coins?aq_480=1&aq_68xt=1&a_68xt=true&aq_68=0&aq_67xt=0&aq_66xt=0&aq_vii=0&aq_5700xt=0&aq_5700=0&aq_5600xt=0&aq_vega64=0&aq_vega56=0&aq_3090=0&aq_3080Ti=0&aq_3080=0&aq_3080L=0&aq_3070Ti=0&aq_3070=0&aq_3070L=0&aq_3060Ti=0&aq_3060TiL=0&aq_3060=0&aq_3060L=0&aq_55xt8=0&aq_580=0&aq_570=0&aq_470=0&aq_fury=0&aq_380=0&aq_2080Ti=0&aq_2080=0&aq_2070=0&aq_2060=0&aq_166s=0&aq_1660Ti=0&aq_1660=0&aq_1080Ti=0&aq_1080=0&aq_1070Ti=0&aq_1070=0&aq_10606=0&aq_1050Ti=0&eth=true&factor%5Beth_hr%5D=64.00&factor%5Beth_p%5D=150.00&e4g=true&factor%5Be4g_hr%5D=64.00&factor%5Be4g_p%5D=150.00&zh=true&factor%5Bzh_hr%5D=90.00&factor%5Bzh_p%5D=150.00&cnh=true&factor%5Bcnh_hr%5D=0.00&factor%5Bcnh_p%5D=0.00&cng=true&factor%5Bcng_hr%5D=3300.00&factor%5Bcng_p%5D=180.00&cnr=true&factor%5Bcnr_hr%5D=0.00&factor%5Bcnr_p%5D=0.00&cnf=true&factor%5Bcnf_hr%5D=0.00&factor%5Bcnf_p%5D=0.00&eqa=true&factor%5Beqa_hr%5D=0.00&factor%5Beqa_p%5D=0.00&cc=true&factor%5Bcc_hr%5D=7.00&factor%5Bcc_p%5D=140.00&cr29=true&factor%5Bcr29_hr%5D=0.00&factor%5Bcr29_p%5D=0.00&ct31=true&factor%5Bct31_hr%5D=2.20&factor%5Bct31_p%5D=150.00&ct32=true&factor%5Bct32_hr%5D=0.90&factor%5Bct32_p%5D=150.00&eqb=true&factor%5Beqb_hr%5D=36.00&factor%5Beqb_p%5D=150.00&rmx=true&factor%5Brmx_hr%5D=0.00&factor%5Brmx_p%5D=0.00&ns=true&factor%5Bns_hr%5D=0.00&factor%5Bns_p%5D=0.00&al=true&factor%5Bal_hr%5D=110.00&factor%5Bal_p%5D=150.00&ops=true&factor%5Bops_hr%5D=44.00&factor%5Bops_p%5D=190.00&eqz=true&factor%5Beqz_hr%5D=0.00&factor%5Beqz_p%5D=0.00&zlh=true&factor%5Bzlh_hr%5D=0.00&factor%5Bzlh_p%5D=0.00&kpw=true&factor%5Bkpw_hr%5D=33.00&factor%5Bkpw_p%5D=200.00&ppw=true&factor%5Bppw_hr%5D=0.00&factor%5Bppw_p%5D=0.00&x25x=true&factor%5Bx25x_hr%5D=0.00&factor%5Bx25x_p%5D=0.00&mtp=true&factor%5Bmtp_hr%5D=0.00&factor%5Bmtp_p%5D=0.00&vh=true&factor%5Bvh_hr%5D=0.00&factor%5Bvh_p%5D=0.00&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=coinex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=&commit=Calculate'

    nvdia_url_list = []

    amd_url_list = []

    n = 1
    PATH = 'C:\chromedriver.exe'

    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
          'AppleWebKit/537.11 (KHTML, like Gecko) '
          'Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}

    # opening up connection grabbing the page
    req = urllib.request.Request(url = default_url, headers = header)
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, 'html.parser')
    data_order_num = page_soup.findAll('div', {'class': 'col'})
    nvdia_cards = page_soup.findAll('div',{'class': 'hash-adapt ck-button-nv'})
    amd_cards = page_soup.findAll('div',{'class': 'hash-adapt ck-button-amd'})
    containersA = page_soup.findAll('input', {'class': 'form-control resets-adapt'})
    algos = page_soup.findAll('span', {'class': 'btn btn-default' })

    num_of_graphics_cards = len(data_order_num)

    #print(len(data_order_num)) output is 42

    # for getting each url for each card
    num_of_graphics_cards -= 1
    tree = etree.HTML(page_html)
    nvdia_check = 'ck-button-nv'
    amd_check = 'ck-button-amd'

    while n <= num_of_graphics_cards:

        driver = webdriver.Chrome(PATH)
        driver.get(default_url)

        default_element = driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/div[1]/div[1]/label/div/div/span')
        driver.execute_script("arguments[0].click();", default_element)

        element = tree.xpath(f'/html/body/div[2]/form/div[1]/div[1]/div[{n}]/label/div')
        content = etree.tostring(element[0])
        string = content.decode()

        if string.find(nvdia_check) != -1:

            new_element = driver.find_element_by_xpath(f'/html/body/div[2]/form/div[1]/div[1]/div[{n}]/label/div/div')

            driver.execute_script("arguments[0].click();", new_element)

            calculate_element = driver.find_element_by_xpath('/html/body/div[2]/form/div[6]/div[2]/div/input')
            driver.execute_script("arguments[0].click();", calculate_element)

            current_url = driver.current_url

            if current_url == default_url and n != 1:
                continue

            n += 1
            print(current_url)
            nvdia_url_list.append(current_url)
            driver.quit()

        else:

            new_element = driver.find_element_by_xpath(f'/html/body/div[2]/form/div[1]/div[1]/div[{n}]/label/div/div')

            driver.execute_script("arguments[0].click();", new_element)

            calculate_element = driver.find_element_by_xpath('/html/body/div[2]/form/div[6]/div[2]/div/input')
            driver.execute_script("arguments[0].click();", calculate_element)

            current_url = driver.current_url

            if current_url == default_url and n != 1:
                continue

            n += 1
            print(current_url)
            amd_url_list.append(current_url)
            driver.quit()

    #for all algorithms
    algos_list = [algo.text.strip('\n') for algo in algos]

    # this space list needs to be two longer than algos_list
    space_list = []
    v = -2
    while v <= len(algos_list):
        space_list.insert(0, ' ')
        v += 1

    algos_list.insert(0, ' ')
    algos_list.insert(0, ' ')

    with open('test Mining Equipment Effciency.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(space_list)
        csv_writer.writerow(algos_list)

        c = 1
        k = 0
        d = 0
        while c <= num_of_graphics_cards:

            if c <= len(nvdia_url_list):
                # opening up connection grabbing the page
                req = urllib.request.Request(url = nvdia_url_list[k], headers = header)
                uClient = uReq(req)
                page_html = uClient.read()
                uClient.close()

                # html parsing
                page_soup = soup(page_html, 'html.parser')
                containersA = page_soup.findAll('input', {'class': 'form-control resets-adapt'})
                nvdia_cards = page_soup.findAll('div',{'class': 'hash-adapt ck-button-nv'})
                #nvdia_cards = page_soup.findAll('div',{'class': 'input-group-append hash-adapt ck-button-nv'})

                #for all nvdia graphics cards
                nvdia_cards_list = [card.text.strip('\n') for card in nvdia_cards]

                #for all hash rates and watts from each card
                hash_rate_list = []
                watts_list = []
                for containerA in containersA:
                    id = containerA['id']
                    value = containerA['value']
                    if id[-1:] == 'r':
                        hash_rate_list.append(value)
                    else:
                        watts_list.append(value)

                #for all effciencies from each card
                nvdia_eff_list = []
                for hash_rate, watts in zip(hash_rate_list, watts_list):
                    hash_rate = float(hash_rate)
                    watts = float(watts)
                    try:
                        eff = hash_rate/watts
                    except ZeroDivisionError:
                        eff = 0.0
                    formatted_effciency = format(eff, '.4f')
                    nvdia_eff_list.append(formatted_effciency)

                nvdia_eff_list.insert(0, nvdia_cards_list[k])
                nvdia_eff_list.insert(0, ' ')
                print(nvdia_eff_list)

                csv_writer.writerow(nvdia_eff_list)

                k += 1
                c += 1
                print('-------------------------------------------')

            else:

                # opening up connection grabbing the page
                req = urllib.request.Request(url = amd_url_list[d], headers = header)
                uClient = uReq(req)
                page_html = uClient.read()
                uClient.close()

                # html parsing
                page_soup = soup(page_html, 'html.parser')
                containersA = page_soup.findAll('input', {'class': 'form-control resets-adapt'})
                amd_cards = page_soup.findAll('div',{'class': 'hash-adapt ck-button-amd'})

                #for all amd graphics cards
                amd_cards_list = [card.text.strip('\n') for card in amd_cards]

                #for all hash rates and watts from each card
                hash_rate_list = []
                watts_list = []
                for containerA in containersA:
                    id = containerA['id']
                    value = containerA['value']
                    if id[-1:] == 'r':
                        hash_rate_list.append(value)
                    else:
                        watts_list.append(value)

                #for all effciencies from each card
                amd_eff_list = []
                for hash_rate, watts in zip(hash_rate_list, watts_list):
                    hash_rate = float(hash_rate)
                    watts = float(watts)
                    try:
                        eff = hash_rate/watts
                    except ZeroDivisionError:
                        eff = 0.0
                    formatted_effciency = format(eff, '.4f')
                    amd_eff_list.append(formatted_effciency)

                amd_eff_list.insert(0, amd_cards_list[d])
                amd_eff_list.insert(0, ' ')
                print(amd_eff_list)

                csv_writer.writerow(amd_eff_list)

                d += 1
                c += 1
                print('-------------------------------------------')

if __name__ == "__main__":
    main()
