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
    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = 'undefined'
    cities = ['washington','new york','chicago','ny','new york city']
    while city == 'undefined':
        input_city =input('\nPlease enter the city (New York, Chicago or Washington) you want to analyze:\n')
        if input_city.lower() in cities:
            if input_city.lower() == 'ny' or input_city.lower() == 'new york city' or input_city.lower() == 'new york':
                city = 'new york city'
            else:
                city = input_city.lower()
        else:
            print('\nThis city is unfortunately not in our database. Please choose one of the following:\nNew York, Chicago or Washington.\n')

    # TO DO: get user input for month (all, january, february, ... , june)

    month = 'undefined'
    months = ['january','february','march', 'april', 'may', 'june', 'all']
    while month == 'undefined':
        input_month =input('\nPlease enter the month (e.g. March) you want to analyze or enter \"all\" to analyze all months available:\n')
        if input_month.lower() in months:
            month = input_month.lower()
        else:
            print('\nThis month is not in our database. Please choose one of the following:\nJanuary, February, March, April, May, June or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = 'undefined'
    days = ['sunday','monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while day == 'undefined':
        input_day =input('\nPlease enter the day (e.g. Monday) you want to analyze or enter \"all\" to analyze all days available:\n')
        if input_day.lower() in days:
            day = input_day.lower()
        else:
            print('\nPlease choose one of the following:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day only if applicable.
    Also tracks the time taken to load date.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    month_name={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    month_as_name=month_name[df['month'].mode()[0]]
    print('\nMost common MONTH:', month_as_name)

    # TO DO: display the most common day of week

    df['day'] = df['Start Time'].dt.dayofweek
    day_name={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    day_as_name = day_name[df['day'].mode()[0]]
    print('Most common DAY OF WEEK:',day_as_name)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    print('Most common START HOUR:',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip (meaning start to end station)."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    start_station_bookings = df['Start Station'].value_counts().max()

    print('\nThe most popular START STATION was {} with {} pickups.'.format(start_station, start_station_bookings))

    # TO DO: display most commonly used end station

    end_station = df['End Station'].mode()[0]
    end_station_bookings = df['End Station'].value_counts().max()

    print('The most popular END STATION was {} with {} returns.'.format(end_station, end_station_bookings))

    # TO DO: display most frequent combination of start station and end station trip

    most_freq_comb = df.groupby(['Start Station', 'End Station']).size().idxmax()
    most_freq_count = df.groupby(['Start Station', 'End Station']).size().max()

    print('The most popular COMBINATION of start station and end station was from {} to {} which was used {} times.'.format(most_freq_comb[0],most_freq_comb[1],most_freq_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # TO DO: display total travel time

    

    # TO DO: display mean travel time

    print('MEAN TRAVEL TIME was {} minutes.'.format(int(df['Trip Duration'].mean()/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_stats = df['User Type'].value_counts()

    print('\nUser Stats:')
    print('\nUser(s):',user_stats.loc['Subscriber'])
    print('Subscriber(s):',user_stats.loc['Customer'])
    if 'Dependent'in user_stats.index:
        print('Dependent(s):',user_stats.loc['Dependent'])

    # TO DO: Display counts of gender

    if 'Gender' not in df.columns:
        print('\nGENDER STATS are unfortunately not available for this city.')
    else:
        gender_stats = df['Gender'].value_counts()
        print('\nGender Stats:')
        print('\nMale(s):',gender_stats.loc['Male'])
        print('Female(s):',gender_stats.loc['Female'])

    # TO DO: Display earliest, most recent, and most common year of birth
    # --> I changed the calculation to age instead of year of birth

    if 'Birth Year' not in df.columns:
        print('\nAGE STATS are unfortunately not available for this city.')
    else:
        max_age = pd.datetime.now().year - df['Birth Year'].min()
        min_age = pd.datetime.now().year - df['Birth Year'].max()
        most_pop_age = pd.datetime.now().year - df['Birth Year'].mode()[0]

        print('\nAge Stats:')
        print('\nMax Age:', int(max_age))
        print('Min Age:', int(min_age))
        print('Most Popular Age:', int(most_pop_age))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display raw data

    i=0
    request_raw = input('Do you want to see raw data? Use ENTER to see raw data or \'no\' to abort.\n')

    while request_raw != 'no':
        print(df.iloc[i:i+5])
        i += 5
        request_raw = input('Do you want to see more raw data? Use ENTER to see more raw data or \'no\' to abort.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
