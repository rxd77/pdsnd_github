#test!!
#import 
import time
import pandas as pd
import numpy as np
#==========================================

#chicago.csv,new_york_city.csv,washington.csv
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#==========================================

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # Get user input for the city (CITY_DATA)
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter a valid city.')

    # Get user input for the month (Month)
    while True:
        month = input('Which month would you like to filter by? (all, january, february, ... , june) ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid input. Please enter a valid month.')

    # Get user input for the day of week (Week)
    while True:
        day = input('Which day of the week would you like to filter by? (all, monday, tuesday, ... sunday) ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid input. Please enter a valid day of the week.')

    print('-'*40)
    return city, month, day

#load_date
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
    # Load data from the CSV file for the specified city ============
    file_path = CITY_DATA[city]
    df = pd.read_csv(file_path)

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from the 'Start Time' column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


# The rest of the code for time_stats, station_stats, trip_duration_stats, user_stats functions remains to be completed based on your specific requirements and dataset.

# Ensure you handle potential issues like missing data appropriately.

# You may also need to adjust the main function to display relevant information based on your analysis.

# Make sure to test your code with different inputs to ensure it works correctly.

# The existing code structure provides a framework, and you need to fill in the details based on your specific needs.
#===================================================
#time_stats
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month: {common_month}")

    # Display the most common day of the week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(f"The most common day of the week: {common_day_of_week}")

    # Display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_start_hour = df['start_hour'].mode()[0]
    print(f"The most common start hour: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#station_stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station: {common_end_station}")

    # Display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start and end stations: {common_trip[0]} to {common_trip[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types:\n{user_types}")

    # Display counts of gender (if the 'Gender' column exists in your dataset)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Counts of gender:\n{gender_counts}")
    else:
        print("Gender information not available in this dataset.")

    # Display earliest, most recent, and most common year of birth (if the 'Birth Year' column exists in your dataset)
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {common_birth_year}")
    else:
        print("Birth year information not available in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df, start_idx):
    """Displays 5 rows of raw data starting from the specified index."""
    print('\nDisplaying 5 rows of raw data...\n')
    print(df.iloc[start_idx:start_idx + 5])
    print('-' * 40)

# The main function and other helper functions (get_filters, load_data) remain the same.
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask user if they want to see raw data
        start_idx = 0
        while True:
            show_raw_data = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n').lower()
            if show_raw_data == 'yes':
                display_raw_data(df, start_idx)
                start_idx += 5
            elif show_raw_data == 'no':
                break
            else:
                print("Invalid input. Please enter yes or no.")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#============================================
if __name__ == "__main__":
    main()
#============================================