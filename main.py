import readFile
import county

all_counties = readFile.get_counties()

for key in all_counties:
    print(all_counties[key].name)
    for county_name in all_counties[key].neighbors:
        print('    ' + county_name)