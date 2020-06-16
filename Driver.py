from datetime import datetime
import time

import WebScraper
import Email


password = input("Type your password and press enter:")

FILE_NAME = "times_to_send.txt"
file = open(FILE_NAME, "r")
file_lines = file.read().split("\n")
for i in range(len(file_lines)):
    if(file_lines[i].find("Breakfast:") != -1):
        BREAKFAST = file_lines[i].split(" ")[1]
    elif(file_lines[i].find("Lunch:") != -1):
        LUNCH = file_lines[i].split(" ")[1]
    elif(file_lines[i].find("Dinner:") != -1):
        DINNER = file_lines[i].split(" ")[1]

while(True):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt = dt_string.split(" ")
    cT = dt[1].split(":")
    currentTime = cT[0] + ":" + cT[1]
    print(currentTime)
    if (currentTime == BREAKFAST):
        print("BREAKFAST TIME")
        webData = WebScraper.Data(0).data
        print(webData)
        print("SENDING MESSAGE")
        Email.Email("visionpi001@gmail.com", password, "nchennoju@gmail.com", webData, dt[0], 0)
        print("DONE")
        time.sleep(60)
    elif (currentTime == LUNCH):
        print("LUNCH TIME")
        webData = WebScraper.Data(1).data
        print(webData)
        print("SENDING MESSAGE")
        Email.Email("visionpi001@gmail.com", password, "nchennoju@gmail.com", webData, dt[0], 1)
        print("DONE")
        time.sleep(60)
    elif (currentTime == DINNER):
        print("DINNER TIME")
        webData = WebScraper.Data(2).data
        print(webData)
        print("SENDING MESSAGE")
        Email.Email("visionpi001@gmail.com", password, "nchennoju@gmail.com", webData, dt[0], 2)
        print("DONE")
        time.sleep(60)
    time.sleep(5)