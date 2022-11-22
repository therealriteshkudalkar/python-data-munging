'''Main File'''

import re
import sys


def read_and_extract(filename):
    with open(filename, encoding="utf8") as dat_file:
        lines = dat_file.readlines()

        temps = []

        for line in lines:
            if line == '\n':
                continue

            streamlined_data = line.strip().split()
            
            day = streamlined_data[0]
            if not day.isdigit():
                continue

            max_temp = int(re.search('\d+' ,streamlined_data[1])[0])
            min_temp = int(re.search('\d+', streamlined_data[2])[0])

            temps.append((max_temp, min_temp, day))

        min_grad = sys.maxsize
        min_grad_day = 0

        for max_t, min_t, day in temps:
            curr_grad = max_t - min_t
            if curr_grad < min_grad:
                min_grad = curr_grad
                min_grad_day = day

        print("Day", min_grad_day)


def read_and_extract_2(filename):
    '''A file to extract'''

    with open(filename, encoding="utf8") as dat_file:
        lines = dat_file.readlines()

        for_against = []

        for line in lines:
            if line == '\n':
                continue

            streamlined_line = line.strip().split()

            team_num = re.search('\d+', streamlined_line[0])
            if not team_num:
                continue

            team_name = streamlined_line[1]
            team_for = int(streamlined_line[6])
            team_against = int(streamlined_line[8])

            for_against.append((team_name, team_for, team_against))

        min_diff = sys.maxsize
        min_diff_team = "NA"

        for team_name, team_for, team_against in for_against:
            curr_diff = abs(team_against - team_for)
            if curr_diff < min_diff:
                min_diff = curr_diff
                min_diff_team = team_name

        print(min_diff_team)


def main():
    '''Main method'''

    filename = 'data/weather.dat'
    read_and_extract(filename)

    filename_2 = 'data/football.dat'
    read_and_extract_2(filename_2)

if __name__ == "__main__":
    main()