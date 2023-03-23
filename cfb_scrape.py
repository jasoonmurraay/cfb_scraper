import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://www.sports-reference.com'

year = 2022

# set up the base url for the FBS schools page
url = "https://www.sports-reference.com/cfb/schools/"

# use requests to get the HTML content of the FBS schools page
response = requests.get(url)
time.sleep(10)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
print("Soup: ", soup)

# find the table containing the FBS schools
table = soup.find("table", {"id": "schools"})
print("Table: ", table)

# find the rows of the table
rows = table.find_all("tr")

# create an empty list to hold the school names
schools = []

# loop through each row and extract the school name
for row in rows:
    # find the cells of the row
    cells = row.find_all("td")
    
    # skip the header row and any row that doesn't contain a school
    if len(cells) == 0 or cells[0].text.strip() == "":
        continue
    
    # extract the school name from the cells
    school_name = cells[0].text.strip()
    
    # make the school name lowercase and replace spaces with "-"
   
    
    # add the school name to the list of schools
    schools.append(school_name)
    print("Appended ", school_name)
    time.sleep(4)

# print the list of schools
print(schools)
categories = ["passing", "rushing", "receiving", "kicking", "punting", "scoring"]

for school in schools:
    for category in categories:
        school_name_url = school.lower().replace(" ", "-").replace("(", '').replace(")", '').replace('&', '').replace('--', '-')
        category_url = base_url + f'/cfb/schools/{school_name_url}/{category}.html'

        category_response = requests.get(category_url)
        print("Response: ", category_response.status_code)
        if category_response.status_code != 200:
            print(f"Error ", category_response.status_code)
            not_found = True
        else:
            not_found = False

        if not_found == False:
            category_soup = BeautifulSoup(category_response.content, "html.parser")
            
            # find the table containing the category stats
            category_table = category_soup.find("table", {"id": f"{category}"})
            if category_table is None:
                no_table = True
            else:
                no_table = False
            
            # extract the team's stats from the table
            if no_table == False:
                team_stats = []
                rows = category_table.find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    if len(cells) > 0:
                        team_stats.append([cell.text.strip() for cell in cells])
                # print the team's stats for the category
                print(f"Team: {school}, Category: {category}")
                for stat in team_stats:
                    print(", ".join(stat))
                print()
                time.sleep(4)
            else:
                time.sleep(4)
                continue
        else:
            time.sleep(4)
            continue

        

# loop through each row and extract the team stats

    
    # create the url for the team page
# 