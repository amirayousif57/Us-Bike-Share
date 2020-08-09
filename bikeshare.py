import time
import pandas as pd
import numpy as np
import calendar

def loaddata(df,month,day):
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    
    df['day_of_week'] =df['Start Time'].dt.day
    df['day_of_week_name'] =df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    df['End Time']=pd.to_datetime( df['End Time'])
    df['end hour']=df['End Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]
        

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]
    
   
    return df
def getmyfilters(choice):
    month="all"
    day="all"
    if choice=="both":
        month=get_month_correct()
        day=Get_day_correct()
    elif choice=="month":
        month=get_month_correct()
    elif choice=="day":
        day=Get_day_correct()
    return month ,day
def get_month_correct():
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     month=str(input("Which month ? January , February , March ,April , May , or June "))
     while month.lower() not in months:
        month=str(input("Which month ? January , February , March ,April , May , or June "))
     return months.index(month.lower())+1
def Get_day_correct():
    while True:
        day=input("which day please enter your reponse as number (e.g.sunday=1)")
        try:
            day=int(day)
            while day>7 or day<=0:
             try:
                 day=int(input("enter a number between 1-7 which day please enter your reponse as number (e.g.sunday=1)"))
             except:
                 print("please enter value between 1 and 7")
        except:
            print("please enter a valid number")
            continue
        else:
            break
      
  
    return day

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
    CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv',
                'washington': 'washington.csv' }
    city=str(input("Would you like to see data for Chicago, New york city or  Washington): "))
    while(CITY_DATA.get(city.lower())==None):
        print("please choose a city from the options with a correct spelling")
        city=str(input("Would you like to see data for Chicago, New york city or  Washington): "))
    city=CITY_DATA[city]
    choice =str(input("Would you like to like to filter databy month ,day ,both or not at all: type none for no filters"))
    choice=choice.lower()
    choices=['month','day','both','none']
    while choice not in choices:
        choice =str(input("Would you like to like to filter databy month ,day ,both or not at all: type none for no filters"))
    
    month, day=getmyfilters(choice)
    return city, month, day
    # TO DO: get user input for month (all, january, february, ... , june)
  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


print('-'*40)



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    df
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(city)
    # filter months and days
    df=loaddata(df,month,day)
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    monthscount=df['month'].unique()
    monthscount=len(monthscount)
    if monthscount>1:
        #print most common month
        month_mode=df["month_name"].mode()[0]
        
        print("most common month is {} ".format(month_mode))

    # TO DO: display the most common day of week
    daycount=df['day_of_week'].unique()
    daycount=len(daycount)
    if daycount>1:
        day_mod=df['day_of_week_name'].mode()[0]
        print("most common day {} ".format(day_mod))


    # TO DO: display the most common start hour
    
    hour_mod=df['start hour'].mode()
    print("most common start hour : {}".format(hour_mod[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station=df['Start Station'].mode()

    sscount=len(df['Start Station'].value_counts())
    # TO DO: display most commonly used end station
    pop_end_station=df['End Station'].mode()
    
    escount=len(df['End Station'].value_counts())
    # TO DO: display most frequent combination of start station and end station trip
    new_df=df['Start Station']+" To: "+df['End Station']
    combine=new_df.mode()
    print("Popular start station: {} , count {}".format( pop_start_station[0],sscount))
    print("Popular end station: {} , count {}".format( pop_end_station[0],escount))
    print("popular Start and end stations are:\n{}".format(combine[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))	
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaldue=df['Trip Duration'].sum()
    print ("Total trip duration :{}".format(totaldue))
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print ("Mean trip duration :{}".format(mean_travel_time))
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("user types are:\n {} ".format(user_types))

#print(user_types)

    # TO DO: Display counts of gender
    gender=""
    if('Gender' in df.columns):
        gender=user_types = df['Gender'].value_counts()
        print("gender counts:\n{}".format(gender))
    else:
        gender="No gender data in this city"
        print (gender)
    




    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year=""
    if('Birth Year' in df.columns):
        birth_year = df['Birth Year'].mode()[0]
        print("Most common birth year: {} ".format(birth_year))
        birth_year = df['Birth Year'].min()
        print("Earlist birth year: {} ".format(birth_year))
        birth_year = df['Birth Year'].max()
        print("Most recent birth year: {} ".format(birth_year))
    else:
        #dont display any thing
        birth_year="No birth year in this city"
        print(birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
