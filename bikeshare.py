import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['chicago', 'new york city', 'washington']
    city = input('Please enter a city from the list: chicago, new york city, washington.\n ').lower()
    while city not in city_list:
        city = input('Sorry you have to choose city from the list: chicago, new york city, washington.\n ').lower()
        if city in city_list:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please select months from january to june or all.\n ').lower()
    while month not in month_list:
        month = input('Sorry you have to choose from the first six months of the year or all.\n ').lower()
        if month in month_list:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select any days from monday to sunday or all.\n ').lower()
    while day not in days_list:
        day = input('Sorry you have to choose from days of the week or all.\n ').lower()
        if day in days_list:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #read city csv file
    df = pd.read_csv(CITY_DATA[city])
    #to convert object to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    #create month column
    df['month'] = df['Start Time'].dt.month
    #create day column
    df['day'] = df['Start Time'].dt.dayofweek
    #create hour column
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        #filter by month
        df = df[df['month'] == month_list.index(month)]

    if day != 'all':
        #filter by day
        df = df[df['day'] == days_list.index(day)-1]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    travel_month = df['month'].mode().iloc[0]
    print("the data showed that month {} is the most common travel month".format(travel_month))

    # TO DO: display the most common day of week
    travel_day = df['day'].mode().iloc[0]
    print("day {} found as the most common day of week for travel".format(travel_day))

    # TO DO: display the most common start hour
    start_hour = df['hour'].mode().iloc[0]
    print("{}: is the most common start hour for travel".format(start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode().iloc[0]
    print("the most start station used was {} ".format(start_station))


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode().iloc[0]
    print("the most end station used was {}".format(end_station))


    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station']+ " , " + df['End Station']).mode().iloc[0]
    print("{} : are the most combination of start station and end station trip".format(combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print("{} : is the total travel times for the trip dutraion".format(total))


    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("the data indicated that the mean of the travel time was {}".format(mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print("the counts of user types are shown as below:\n{}".format(users))

    # Gender and birthyear columns are available only in NYC and chicago so :
    if CITY_DATA == 'chicago' or CITY_DATA == 'new york city':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("the frequency of Male and Female are shown as below:\n{}".format(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        birthyear = df['Birth Year']

        earliest_birth = birthyear.min()
        print("the earliest birthday year is : {}".format(earliest_birth))
        recent_birth = birthyear.max()
        print("the most recent birthday year is : {}".format(recent_birth))
        common_birth = birthyear.mode()[0]
        print("the most common birthday year is : {}".format(common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def row_data(df):
    print(df.head(5))
    line = 0
    while True:
        next_lines = input('\nWould you like to get the followed five rows of data ? Enter yes or no.\n')
        if next_lines.lower() != 'yes':
            break
        else:
            line = line + 5
            print(df.iloc[line:line+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

# the below links were used as a reference
#https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587
#https://www.geeksforgeeks.org/how-to-display-most-frequent-value-in-a-pandas-series/
#https://stackoverflow.com/questions/21082671/find-and-select-the-most-frequent-data-of-column-in-pandas-dataframe
#http://introtopython.org/while_input.html
#https://dfrieds.com/data-analysis/value-counts-python-pandas.html
