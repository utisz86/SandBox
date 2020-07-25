import datetime
import pickle
from WeekClass import WeekClass

def setup_weekdata():
    # Import
    # This week datas
    my_date = datetime.date.today()
    year, week_num, day_of_week = my_date.isocalendar()

    # Set up data
    # Check is there data for this week
    # if yes: open the file
    try:
        with open("week"+str(year)+str(week_num)+"_data.pkl", "rb") as input:
            weekdata = pickle.load(input)
    # if no: new class and save
    except:
        # Make new data object for the week data
        weekdata = WeekClass()
        # Save this weekdata object to a pickle file
        with open("week"+str(year)+str(week_num)+"_data.pkl", 'wb') as output:
            pickle.dump(weekdata, output, pickle.HIGHEST_PROTOCOL)

    return weekdata