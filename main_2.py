'''File for main function'''

from calculator import Calculator

def main():
    '''Main to execute'''

    calc_1 = Calculator("data/weather.dat", [0, 1, 2])
    print("Day with smallest temperature gradient: ", calc_1.execute())

    calc_2 = Calculator("data/football.dat", [1, 6, 8])
    print("Team with smallest difference in for and against: ", calc_2.execute())

if __name__ == "__main__":
    main()
