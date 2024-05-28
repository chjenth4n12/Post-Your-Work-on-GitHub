import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Please enter the city: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Please choose 1 option in Chicago, New York City or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the month: ').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('Please choose 1 option in all, january, february,..., june: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter day of week: ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Please choose 1 day of week monday, tuesday, wednesday, thursday, friday, saturday, sunday: ").lower()

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
    # Load data frame for the selected city
    df = pd.read_csv(CITY_DATA[city])
    print(df)
    # Format start date and end date yyyy-mm-dd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Get Month from start time and create new column month
    df['month'] = df['Start Time'].dt.month
    
    # Filter with month
    if month != 'all':
        monthList = ['january', 'february', 'march', 'april', 'may', 'june']
        month = monthList.index(month) + 1
        df = df[df['month'] == month]
    
    # Get day of week by Start Time and create new column day_of_week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # Filter with day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Display the most common month: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Display the most common day of week: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    # Get hour from Start Time and create new column hour
    df['hour'] = df['Start Time'].dt.hour
    print("Display the most common start hour: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Display most commonly used start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Display most commonly used end station: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Display most frequent combination of start station and end station trip: ", df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime = df['Trip Duration'].sum() / 3600.0
    print("Display total travel time: ", totalTravelTime)

    # TO DO: display mean travel time
    meanTravelTime = df['Trip Duration'].mean() / 3600.0
    print("Display mean travel time: ", meanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Display counts of user types: ", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print("Display counts of gender: ", df['Gender'].value_counts())
        
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        mostRecent = int(df['Birth Year'].max())
        mostCommonYearOfBirth = int(df['Birth Year'].mode()[0])
        print("Earliest: ", earliest)
        print("Most recent: ", mostRecent)
        print("Most common year of birth: ", mostCommonYearOfBirth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_display(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == "yes":
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
