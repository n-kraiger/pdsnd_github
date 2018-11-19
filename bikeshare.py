import pandas as pd
from datetime import datetime
from datetime import timedelta
import time

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_city():
    '''Returns the city data requested based on the city input from the user once prompted
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Your input was invalid, please input either Chicago, New York or Washington')

    # TO DO: get user input for month (all, january, february, ... , june)
def get_time_period():
    '''Returns the time period entered after the prompt
    '''
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'no time filter']:
        time_period = input('\nWould you like to look at the data by month, day,'
                            ' or have no time filter? Please enter "no time filter" for no time filter.\n')
        if time_period.lower() not in ['month', 'day', 'no time filter']:
            print('Your input was invalid, please type "month", "day" or "no time filter".')
    return time_period

def get_month():
    '''Returns the specific month entered after the prompt
    '''
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month would you like to see? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in months_dict.keys():
            print('Your input was invalid. Please type either "January", "February", "March", "April", "May", or "June"')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    '''Returns the specific day of the week entered after the prompt
    '''
    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:    
        is_int = False
        day = input('\nWhich day would you like to see? The day must be entered as an integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Your input is invalid, please enter a valid integer to see data for a specific day of the week.')
                day = input('\nWhich day would you like to see? The day must be entered as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))



    # TO DO: display the most common month
def common_month(df):
    '''Returns the most common month based on start time
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_comm_month = months[index - 1]
    print('The most common month is {}.'.format(most_comm_month))

    # TO DO: display the most common day of week
def common_day(df):
    '''Returns the most common day based on start time
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_comm_day = days_of_week[index]
    print('The most common day of week for start time is {}.'.format(most_comm_day))

    # TO DO: display the most common start hour
def common_hour(df):
    '''Returns the most common hour based on start time
    '''
    most_comm_hour = int(df['start_time'].dt.hour.mode())
    if 0 <= most_comm_hour < 13:
        am_pm = 'am'
        comm_hour_time = most_comm_hour
    elif 13 <= most_comm_hour < 24:
        am_pm = 'pm'
        comm_hour_time = most_comm_hour - 12
    print('The most common hour of day for start time is {}{}.'.format(comm_hour_time, am_pm))



    # TO DO: display most commonly used start and end stations
def common_stations(df):
    '''Returns the most common start and end stations
    '''
    comm_start = df['start_station'].mode().to_string(index = False)
    comm_end = df['end_station'].mode().to_string(index = False)
    print('The most common start station is {}.'.format(comm_start))
    print('The most common end station is {}.'.format(comm_end))


    # TO DO: display most frequent combination of start station and end station trip
def common_trip(df):
    '''Returns the most common trip based on start and end station
    '''
    most_comm_trip = df['journey'].mode().to_string(index = False)
    print('The most common trip is {}.'.format(most_comm_trip))
    
    # TO DO: display total and mean travel time
def trip_duration(df):
    '''Returns the total and average trip duration
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))
    
    # TO DO: Display counts of user types
def users(df):
    '''Returns the subscriber and customer user types
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

    # TO DO: Display counts of gender
def gender(df):
    '''Returns data for each gender
    '''
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))

    # TO DO: Display earliest, most recent, and most common year of birth
def birth_years(df):
    ''' Returns the youngest and oldest users, as well as the most common birth year
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most common birth year is {}.'.format(earliest, latest, mode))

def display_data(df):
    '''Returns the first 5 lines of data once requested by the user
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view raw data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view raw data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Your input was invalid. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break
    
    
def statistics():
    '''Calculates the descriptive statistics for the requested city and timeframe
    '''
    # Filter by city
    city = get_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])
    
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels
    
    pd.set_option('max_colwidth', 100)
    
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period
    time_period = get_time_period()
    if time_period == 'no time filter':
        df_filtered = df
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = get_month()
        elif time_period == 'day':
            filter_lower, filter_upper = get_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if time_period == 'no time filter':
        start_time = time.time()
        
        # Most common month  
        common_month(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()        

    if time_period == 'no time filter':
        start_time = time.time()
        
        # Most common day  
        common_day(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")    
        start_time = time.time()
    
    elif time_period  == 'month':
        start_time = time.time()
        
        # Most common day
        common_day(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")    
        start_time = time.time()
    
    elif time_period == 'day':
        start_time = time.time()
    
    # Most common hour of day
    common_hour(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # total trip duration
    trip_duration(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # Most common start and end stations
    common_stations(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # Most common trip
    common_trip(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # Types of users
    users(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    
    if city == 'chicago.csv' or city == 'new_york_city.csv' or city == 'washington.csv':
        print("\nCalculating the next statistic...")
        start_time = time.time()
        
        # Gender types
        gender(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

        # User age (oldest, youngest, common)
        birth_years(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))

    # Show 5 lines of raw data
    display_data(df_filtered)

    # Restart prompt
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
