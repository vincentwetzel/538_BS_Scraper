key_districts_list_of_lists = [
    ["Minnesota", 7],
    ["Pennsylvania", 8],
    ["Pennsylvania", 17],
    ["Arizona", 2],
    ["California", 49],
    ["Iowa", 1],
    ["Pennsylvania", 7],
    ["Arizona", 1],
    ["Nevada", 4],
    ["New Hampshire", 4],
    ["Florida", 27],
    ["Virgina", 10],
    ["New Jersey", 11],
    ["Colorado", 6],
    ["Kansas", 3],
    ["Minnesota", 2],
    ["Minnesota", 3],
    ["Michigan", 11],
    ["Nevada", 3],
    ["New Jersey", 7],
    ["California", 10],
    ["Iowa", 3],
    ["California", 45],
    ["New York", 19],
    ["Washington", 8],
    ["Illinois", 6],
    ["California", 48],
    ["California", 25],
    ["Maine", 2],
    ["Michigan", 8],
    ["Kansas", 2],
    ["New Jersey", 3],
    ["California", 39],
    ["New York", 22],
    ["Utah", 4],
    ["Minnesota", 1],
    ["North Carolina", 9],
    ["Kentucky", 6],
    ["Florida", 26],
    ["Texas", 7],
    ["Virginia", 7],
    ["New Mexico", 2],
    ["Pennsylvania", 1],
    ["Florida", 15],
    ["North Carolina", 13],
    ["Ohio", 12],
    ["Illinois", 14],
    ["Virginia", 5],
    ["Texas", 32],
    ["Nebraska", 2],
    ["Georgia", 6],
    ["Virginia", 2],
    ["Pennsylvania", 10],
    ["Montana", 1],
    ["Illinois", 12],
    ["Illinois", 13],
    ["Florida", 6],
    ["Michigan", 7],
    ["New York", 27],
    ["California", 50],
    ["New York", 11],
    ["Wisconsin", 1],
    ["Washington", 3],
    ["Ohio", 1],
    ["Washington", 5],
    ["New York", 24],
    ["Alaska", 1],
    ["Texas", 23],
    ["North Carolina", 2],
    ["Minnesota", 8],
    ["Georgia", 7],
    ["Arizona", 8],
    ["Iowa", 4],
    ["Michigan", 6],
    ["Florida", 16],
    ["Wisconsin", 6],
    ["California", 21],
    ["Pennsylvania", 16],
    ["Arkansas", 2],
    ["Florida", 18],
    ["New York", 2],
    ["California", 4],
    ["Ohio", 14],
    ["Florida", 25],
    ["Texas", 21],
    ["Missouri", 2],
    ["Texas", 22],
    ["New York", 23],
    ["Colorado", 3],
    ["South Carolina", 1],
    ["West Virginia", 3],
    ["Oklahoma", 5],
    ["Indiana", 9],
    ["California", 1],
    ["Texas", 31],
    ["Texas", 2],
    ["North Carolina", 8],
    ["New York", 21],
    ["New York", 1],
    ["Ohio", 10],
    ["Arizona", 6],
    ["Michigan", 1],
    ["North Carolina", 7],
    ["California", 22],
    ["Ohio", 7],
    ["Indiana", 2]
]

from bs4 import BeautifulSoup
import urllib.request


def main():
    source = urllib.request.urlopen(
        get_538_house_forecast_url(key_districts_list_of_lists[0]))
    soup = BeautifulSoup(source, features='lxml')  # Might need to change features=

    print("Title: " + str(soup.title))
    print("Attributes: " + str(soup.title.name))
    print("Values: " + str(soup.title.string))
    print("Beginning navigation: " + str(soup.title.parent.name))
    print("Specific values: " + str(soup.p))
    print("--------------------------------")

    #for val in key_districts_list_of_lists:
    #    print(get_538_house_forecast_url(val))

    print_district_partisanship(soup)



def get_538_house_forecast_url(lst):
    return ("https://projects.fivethirtyeight.com/2018-midterm-election-forecast/house/"
            + lst[0].replace(" ", "-") + "/" + str(lst[1])).lower()


def print_district_partisanship(soup_object):
    # Do some clever math to figure out where "District partisanship" is in the table.
    pos = 0
    for val in soup_object.find_all("td", class_="category"):
        if "District partisanship" in val:
            break
        pos += 1

    district_partisanship_explanation = (str(soup_object.find_all("td", class_="explanation")[pos].contents[0]).strip())
    # print(">>>FULL EXPLANATION:" + district_partisanship_explanation)
    if "Trump in 2016" in district_partisanship_explanation:
        print("Trump won this district in 2016!")
    elif "Clinton in 2016" in district_partisanship_explanation:
        print("Clinton won this district in 2016!")
    else:
        print("ERROR: Cannot determine who won this district in 2016.")

    if "Romney in 2012" in district_partisanship_explanation:
        print("Romney won this district in 2012!")
    elif "Obama in 2012" in district_partisanship_explanation:
        print("Obama won this district in 2012!")
    else:
        print("ERROR: Cannot determine who won this district in 2012.")


if __name__ == "__main__":
    main()
