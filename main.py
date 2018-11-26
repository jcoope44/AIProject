import readFile
import county
import colorMap

all_counties = readFile.get_counties()

color_string = input('Enter colors to use in a comma seperated list (red,blue,green,...): ')
colors = color_string.replace(' ', '').split(',')

for key in all_counties:
    all_counties[key].possible_colors = colors.copy()

success = colorMap.color_map(colors, all_counties)
while not success:
    color_string = input('Not enough colors added. Add more: ')
    colors.extend(color_string.replace(' ', '').split(','))
    for key in all_counties:
        all_counties[key].possible_colors = colors.copy()
    success = colorMap.color_map(colors, all_counties)
    
for key in all_counties:
        if hasattr(all_counties[key], 'color'):
            print(key, ': ', all_counties[key].color)
        else:
            print(key, ': No Color')

