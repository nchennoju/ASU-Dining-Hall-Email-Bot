from bs4 import BeautifulSoup as soup
from selenium import webdriver
from datetime import datetime

class Data:

    '''
    meal = 0 -> Breakfast
    meal = 1 -> Lunch
    meal = 2 -> Dinner
    '''

    def __init__(self, meal):
        '''
        DATA FORMAT

        Index 0: Dining hall name
        Index 1: Dining hall state
        Index 2: Menu Items
        Index 3: Description
        '''
        self.data = []

        URL = "https://asu.campusdish.com/DiningVenues"
        PATH = 'C:\Program Files (x86)\chromedriver.exe'

        DATE_FORMAT = self.getDateFotmatted()

        driver = webdriver.Chrome(PATH)
        driver.get(URL)
        source = driver.page_source
        all_soup = soup(source, "html.parser")

        site_extension = self.getDiningHallNames(all_soup.findAll("span", {"class": "card-title"}), URL, DATE_FORMAT, meal)

        for i in range(len(site_extension)):
            info = []
            # change to site_extension[i] when done testing
            driver.get(site_extension[i])
            info.append(driver.title)
            print(driver.title)

            source = driver.page_source
            all_soup = soup(source, "html.parser")

            # Location Status of Dining hall
            if (len(all_soup.findAll("span", {"class": "locationstatus closed"})) != 0):
                info.append("Closed")
            elif (len(all_soup.findAll("span", {"class": "locationstatus open"})) != 0):
                info.append("Open")
            else:
                info.append("Unable to determine")

            # change to open when done testing
            if (info[1] == "Open"):
                menuItems = []
                items = all_soup.findAll("div", {"class": "menu__category"})
                print("\n--------- MENU ITEMS -----------\n")
                for j in range(len(items)):
                    more_soup = soup(str(items[j]), "html.parser")
                    menuItems.append(self.getItemName(more_soup.findAll("span", {"class": "item__name"})))
                print("\n--------- DESCRIPTION -----------\n")
                description = self.getItemDesctiption(all_soup.findAll("p", {"class": "item__content"}))
                info.append(menuItems)
                info.append(description)
                print("\n--------- DONE -----------\n")

            self.data.append(info)

        driver.quit()


    def getDateFotmatted(self):
        now = str(datetime.now())
        arrNow = now.split(" ")[0].split("-")
        formatted = "?date=" + arrNow[1] + "%2F" + arrNow[2] + "%2F" + arrNow[0]
        return formatted

    #Parse html
    def getDiningHallNames(self, html, url, formattedDate, meal):
        names = []
        index = 0
        for i in range(len(html)):
            while(str(html[i])[index] != ">" or index == len(html)):
                index += 1
            start = index + 1
            while(str(html[i])[index] != '<' or index == len(html)):
                index += 1

            name = str(html[i])[start:index]
            name = name.replace(' ', '')
            name = name.replace('-', '')
            if (name.find("Tooker") == -1):
                name = url + "/" + name + formattedDate + "&periodId=" + str(980+meal)
            else:
                name = url + '/TookerHouseDining' + formattedDate + "&periodId=" + str(980+meal)
            print(name)
            names.append(name)
            index = 0

        return names

    def getItemName(self, html):
        names = []
        for i in range(len(html)):
            index = str(html[i]).find("viewItem")
            while (str(html[i])[index] != '>' or index == len(str(html[i]))):
                index += 1
            start = index + 1
            while (str(html[i])[index] != '<' or index == len(str(html[i]))):
                index += 1

            name = str(html[i])[start:index]
            print(name)
            names.append(name)

        return names

    def getItemDesctiption(self, html):
        names = []
        for i in range(len(html)):
            index = 0
            while (str(html[i])[index] != '>' or index == len(str(html[i]))):
                index += 1
            start = index + 1
            while (str(html[i])[index] != '<' or index == len(str(html[i]))):
                index += 1

            name = str(html[i])[start:index]
            print(name)
            names.append(name)

        return names