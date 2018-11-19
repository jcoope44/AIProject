import csv
import county

def get_counties():
    with open('Counties.csv') as counties:
        reader = csv.reader(counties, delimiter=',')
        all_counties = {}

        next(reader)
        for row in reader:
            i = 0
            for county_name in row:
                if i == 0:
                    all_counties[county_name] = county.County(county_name)
                else:
                    if county_name != '':
                        all_counties[row[0]].neighbors.append(county_name)
                i += 1
        return all_counties

