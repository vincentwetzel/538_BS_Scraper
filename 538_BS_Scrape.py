from bs4 import BeautifulSoup
import urllib.request


def main():
    source = urllib.request.urlopen(
        "https://projects.fivethirtyeight.com/2018-midterm-election-forecast/house/california/10/")
    soup = BeautifulSoup(source, features='lxml')  # Might need to change features=

    print("Title: " + str(soup.title))
    print("Attributes: " + str(soup.title.name))
    print("Values: " + str(soup.title.string))
    print("Beginning navigation: " + str(soup.title.parent.name))
    print("Specific values: " + str(soup.p))
    print("--------------------------------")

    # Do some clever math to figure out where "District partisanship" is in the table.
    pos = 0
    for val in soup.find_all("td", class_="category"):
        if "District partisanship" in val:
            break
        pos += 1

    district_partisanship_explanation = (str(soup.find_all("td", class_="explanation")[pos].contents[0]).strip())
    print(">>>EXPLANATION:" + district_partisanship_explanation)
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
