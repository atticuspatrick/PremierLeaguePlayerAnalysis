# Atticus Patrick and Owen Patrick
# CS 021 Final Project
# This program is a tool that can be used to analyze Premier League soccer player data from 2014/15 to 2018/19.
# The data points that this programs reads in come from a soccer statistics website Understat.com. We have created text
# files unique to 20 different players with data points extracted from this website to be read into the program. The
# program reads in data about a user specified player, including years played (2014/15 to 2018/19), appearances
# made, goals scored, assists, expected goals, and expected assists (as a reminder, expected goals and assists are
# statistics in soccer calculated based on a number of factors, such as the angle towards the goal and proximity to the
# goal, describing the statistical likelihood of a certain shot becoming a goal or a certain pass becoming an assist).
# It then gives the option for the user to see a summary of the player's statistics, a bar graph of goals vs expected
# goals for each year, and finally a bar graph of assists vs expected assists for each year.

# define main
def main():
    # import matplotlib for data visualization later on (Atticus)
    import matplotlib.pyplot as plt
    import numpy as np

    # ask user which player they want to see data of (and incorporate exception handling) (Atticus & Owen)
    try:
        print("Welcome to our Premier League player analysis program. You can enter a player's name to view an analysis"
              " of their data.")
        print(" ")
        name1 = input("Enter the player's full name (i.e. Sadio Mane): ")

        # assign each player's name to their text file (Atticus)
        name = file_conversion(name1)

        # read in the player the user wants to see, call list_creator to make each line of the text file into a list,
        # and call data_filter to organize the data points into lists for year, appearances made, goals scored,
        # expected goals, assists, and expected assists (Atticus)
        infile = open(name, "r")
        y1, y2, y3, y4, y5 = list_creator(infile)
        yr, app, g, a, xg, xa = data_filter(y1, y2, y3, y4, y5)
        yr.reverse()
        app.reverse()
        g.reverse()
        a.reverse()
        xg.reverse()
        xa.reverse()

        # Ask user what they would like with the data: summary of stats, g vs xg graph,
        # a vs xa graph. (Owen)
        summary = input(
            "Would you like to see a summary of the player's statistics from their past 5 seasons?"
            " (enter y if yes, hit enter if no): ")
        if summary == 'y' or summary == 'Y':
            total_app = float(app[0]) + float(app[1]) + float(app[2]) + float(app[3]) + float(app[4])
            total_g = float(g[0]) + float(g[1]) + float(g[2]) + float(g[3]) + float(g[4])
            total_a = float(a[0]) + float(a[1]) + float(a[2]) + float(a[3]) + float(a[4])
            avg_xg = (float(xg[0]) + float(xg[1]) + float(xg[2]) + float(xg[3]) + float(xg[4])) / 5
            avg_g = (float(g[0]) + float(g[1]) + float(g[2]) + float(g[3]) + float(g[4])) / 5
            avg_a = (float(a[0]) + float(a[1]) + float(a[2]) + float(a[3]) + float(a[4])) / 5
            avg_xa = (float(xa[0]) + float(xa[1]) + float(xa[2]) + float(xa[3]) + float(xa[4])) / 5
            print(" ")
            print(name1, "played", total_app, "games over the last 5 seasons and had", total_g, "goals and", total_a,
                  "assists.\nHe had an average of", format(avg_xg, ".2f"),
                  "expected goals per season versus an average of", format(avg_g, ".2f"),
                  "actual goals per season.\nHe had an average of", format(avg_xa, ".2f"),
                  "expected assists per season versus an average of", format(avg_a, ".2f"),
                  "actual assists per season.")

        # bar graph of goals vs expected goals in each year (Owen)
        print(" ")
        xgGraph = input("Would you like to see a graph of Goals vs. xG? (enter y if yes, hit enter if no): ")
        if xgGraph == 'y' or xgGraph == 'Y':
            goals_graph(yr, g, xg, np, plt)

        # bar graph of assists vs expected assists in each year (Owen)
        print(" ")
        xaGraph = input("Would you like to see a graph of Assists vs. xA? (enter y if yes, hit enter if no): ")
        if xaGraph == 'y' or xaGraph == 'Y':
            assists_graph(yr, a, xa, np, plt)

        print(" ")
        print("Thank you for using our program, and a big thanks to Understat.com for the data used.")

        # close infile
        infile.close()

    # handle exceptions (Atticus)
    except IOError:
        name = input("File not found")
    except ValueError:
        print("Value Error")

# this function adds ".txt" on the end of any name entered to match the text file name for the player's statistics
# (Atticus)
def file_conversion(n):
    return n + ".txt"

# this function reads the text file in and separates it out into lists based on each row in the text file (Atticus)
def list_creator(inputfile):
    player = inputfile.readlines()
    yr1819 = ""
    yr1718 = ""
    yr1617 = ""
    yr1516 = ""
    yr1415 = ""
    yr1819 += player[0]
    yr1718 += player[1]
    yr1617 += player[2]
    yr1516 += player[3]
    yr1415 += player[4]
    yr1819 = yr1819.strip("\n")
    yr1718 = yr1718.strip("\n")
    yr1617 = yr1617.strip("\n")
    yr1516 = yr1516.strip("\n")
    yr1415 = yr1415.strip("\n")
    yr1819 = list(yr1819.split("\t"))
    yr1718 = list(yr1718.split("\t"))
    yr1617 = list(yr1617.split("\t"))
    yr1516 = list(yr1516.split("\t"))
    yr1415 = list(yr1415.split("\t"))
    return yr1819, yr1718, yr1617, yr1516, yr1415

# this function adds the appropriate data from each list created by list_creator, filtering the data into lists of
# the year, appearances made, goals scored, expected goals, assists, and expected assists (Atticus)
def data_filter(yr1, yr2, yr3, yr4, yr5):
    year = []
    appearances = []
    goals = []
    assists = []
    xgoals = []
    xassists = []
    year.append(yr1[0])
    year.append(yr2[0])
    year.append(yr3[0])
    year.append(yr4[0])
    year.append(yr5[0])
    appearances.append(yr1[1])
    appearances.append(yr2[1])
    appearances.append(yr3[1])
    appearances.append(yr4[1])
    appearances.append(yr5[1])
    goals.append(yr1[2])
    goals.append(yr2[2])
    goals.append(yr3[2])
    goals.append(yr4[2])
    goals.append(yr5[2])
    assists.append(yr1[3])
    assists.append(yr2[3])
    assists.append(yr3[3])
    assists.append(yr4[3])
    assists.append(yr5[3])
    xgoals.append(yr1[4])
    xgoals.append(yr2[4])
    xgoals.append(yr3[4])
    xgoals.append(yr4[4])
    xgoals.append(yr5[4])
    xassists.append(yr1[5])
    xassists.append(yr2[5])
    xassists.append(yr3[5])
    xassists.append(yr4[5])
    xassists.append(yr5[5])
    int_appearances = []
    int_goals = []
    int_assists = []
    int_xgoals = []
    int_xassists = []
    for i in appearances:
        int_appearances.append(float(i))
    for i in goals:
        int_goals.append(float(i))
    for i in assists:
        int_assists.append(float(i))
    for i in xgoals:
        int_xgoals.append(float(i))
    for i in xassists:
        int_xassists.append(float(i))
    return year, int_appearances, int_goals, int_assists, int_xgoals, int_xassists

# this function creates a bar graph of the player's goals vs expected goals in each year (Owen & Atticus)
def goals_graph(yr, g, xg, np, plt):
    x = np.arange(len(yr))
    width = 0.4
    fig, ax = plt.subplots()
    bar1 = ax.bar(x - width / 2, g, width, label='Goals')
    bar2 = ax.bar(x + width / 2, xg, width, label='Expected Goals')
    ax.set_title('Goals vs. Expected Goals')
    ax.set_xticks(x)
    ax.set_xticklabels(yr)
    ax.legend()
    fig.tight_layout()
    plt.show()

# this function creates a bar graph of the player's assists vs expected assists in each year (Owen & Atticus)
def assists_graph(yr, a, xa, np, plt):
    x = np.arange(len(yr))
    width = 0.4
    fig, ax = plt.subplots()
    bar1 = ax.bar(x - width / 2, a, width, label='Assists')
    bar2 = ax.bar(x + width / 2, xa, width, label='Expected Assists')
    ax.set_title('Assists vs. Expected Assists')
    ax.set_xticks(x)
    ax.set_xticklabels(yr)
    ax.legend()
    fig.tight_layout()
    plt.show()

# call main
main()