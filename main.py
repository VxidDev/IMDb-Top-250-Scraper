import pathlib , csv , subprocess
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from colorama import Fore , Style , init
from random import uniform
from time import sleep

init()

def Message(text):
    subprocess.run("clear")
    print(Style.BRIGHT + Fore.WHITE + text + Style.RESET_ALL)

subprocess.run("clear")

while True:
    try:
        target_amount = int(input(f"{Style.BRIGHT + Fore.WHITE}Enter target amount:{Style.RESET_ALL} "))
        if target_amount <= 0:
            raise ValueError("negative")
        elif target_amount > 250:
            raise ValueError("over")
        break
    except ValueError as e:
        if str(e) in "over":
            print(f"{Style.BRIGHT + Fore.WHITE}Input {Fore.RED}must{Fore.WHITE} be a number under 250!{Style.RESET_ALL}")
        elif str(e) in "negative":
            print(f"{Style.BRIGHT + Fore.WHITE}Input {Fore.RED}must{Fore.WHITE} be a number greater then 0!{Style.RESET_ALL}")
        else:
            print(f"{Style.BRIGHT + Fore.WHITE}Input{Fore.RED} must{Fore.WHITE} be a number!{Style.RESET_ALL}") 

Message("Getting script's path...")

path = pathlib.Path(__file__).resolve().parent

Message("Initializing browser...")

options = Options()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options)

browser.get("https://www.imdb.com/chart/top/")

output = []

while len(output) < target_amount:
    elements = browser.find_elements(By.XPATH , "//div[contains (@class , 'cli-parent') and contains (@class , 'li-compact')]")

    for element in elements[len(output):]:
        if len(output) < target_amount:
            metadata = element.find_element(By.XPATH , ".//div[contains (@class , 'cli-title-metadata')]")
            metadata_elements = metadata.find_elements(By.XPATH , ".//span[contains (@class , 'cli-title-metadata-item')]")
 
            title = element.find_element(By.XPATH , ".//div[contains (@class , 'cli-title') and contains (@class , 'ipc-title--title')]")
            link = element.find_element(By.XPATH , ".//a[@class='ipc-title-link-wrapper']").get_attribute("href")

            try:
                release = metadata_elements[0].text
                lenght = metadata_elements[1].text
                for_rating = metadata_elements[2].text
            except IndexError:
                for_rating = "Unknown"

            output.append([str(title.text).split(maxsplit=1)[1] , release , lenght , for_rating , link])
        
        Message(f"{Style.BRIGHT + Fore.WHITE}Scraping...\nSuccessful scrapes: {Fore.GREEN}{len(output)}{Style.RESET_ALL}")
    
    sleep_time = uniform(0.5 , 2)

    Message(f"Sleeping {round(sleep_time , 2)}s...")

    sleep(sleep_time)

Message("Quitting browser...")

browser.quit()

Message("Writing data to .csv...")

with open(f"{path}/results.csv" , "w") as file:
    writer = csv.writer(file)
    for title , release , lenght , for_rating , link in output:
        writer.writerow([f" {title} " , f" {release} " , f" {lenght} " , f" {for_rating} " , f" {link} "])

Message(f"{Fore.GREEN}Done!{Fore.WHITE} Results at 'results.csv'")

