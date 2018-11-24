import county
import random

def color_map(colors, counties):
    counties_to_color = dict(counties)
    while len(counties_to_color) > 0:
        most_constrained = get_most_constrained(colors, counties, counties_to_color)
        if len(most_constrained.possible_colors) == 0:
            return False
        color = least_constraining_color(most_constrained, counties)
        most_constrained.color = color
        most_constrained.possible_colors = []
        update_neighbors(most_constrained, counties)
        arc_consistency(colors, counties)
        del counties_to_color[most_constrained.name]
    return True

def least_constraining_color(county, counties):
    lowest_constraint_count = 1000000
    least_constraining = ""
    for color in county.possible_colors:
        constraint_count = 0
        for neighbor in county.neighbors:
            if color in counties[neighbor].possible_colors:
                constraint_count += 1
        if constraint_count < lowest_constraint_count:
            lowest_constraint_count = constraint_count
            least_constraining = color
    return least_constraining
                

def update_neighbors(county, all_counties):
    for neighbor in county.neighbors:
        if county.color in all_counties[neighbor].possible_colors:
            all_counties[neighbor].possible_colors.remove(county.color)

def get_most_constrained(colors, counties, counties_to_color):
    highest_number_of_constraints = 0
    most_constrained = None
    for key in counties_to_color:
        if len(counties_to_color[key].neighbors) > highest_number_of_constraints:
            most_constrained = counties_to_color[key]
            highest_number_of_constraints = len(counties_to_color[key].neighbors)
        if len(counties_to_color[key].neighbors) == highest_number_of_constraints:
            has_more_choices = len(counties_to_color[key].possible_colors) > len(most_constrained.possible_colors)
            most_constrained = most_constrained if has_more_choices else counties_to_color[key]
    return most_constrained


def arc_consistency(colors, counties):
    for key in counties:
        if len(counties[key].possible_colors) == 1:
            for neighbor in counties[key].neighbors:
                if counties[key].possible_colors[0] in counties[neighbor].possible_colors:
                    counties[neighbor].possible_colors.remove(counties[key].possible_colors[0])