import readFile
import county
import colorMap

all_counties = readFile.get_counties()
colors = ['red', 'blue', 'green', 'yellow']

for key in all_counties:
    all_counties[key].possible_colors = colors.copy()

success = colorMap.color_map(colors, all_counties)
if success:
    print('success')
else:
    print('failed :(')

for key in all_counties:
        if hasattr(all_counties[key], 'color'):
            print(key, ': ', all_counties[key].color)
        else:
            print(key, ': No Color')

