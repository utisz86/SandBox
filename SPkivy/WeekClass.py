import datetime

my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()

class WeekClass:
    def __init__(self, foodEvents=[
        "Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal",
        "Belsöség", "Burgonya", "Édesség", "Magvak", "Üditő",
         "Sport"],
         weekDays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        weekMin = [0,  0,  0, 0,  1,  0, 0, 0, 3, 0, 15],
        weekMax = [28,14, 21, 14, 14, 2, 3, 2, 3, 2, 50],
        dayMax  = [4,  2,  3,  2, 2,  2, 3, 2, 3, 2, 10],
        foodInfo =["Zöldség/Gyümölcs: 1 adag = 10 dkg friss, párolt vagy főtt, idényjellegű zöldség vagy gyümölcs (pl. 1 közepes paprika, paradicsom, 1 közepes alma vagy narancs) vagy 1 kis tányér saláta vagy 1 kis pohárnyi bogyós gyümölcs. Fogyassz száraz hüvelyeseket (pl. babot, lencsét, csicseriborsót, szóját) levesek, főzelékek, saláták, krémek részeként.",
        "Gabona: 1 adag = 1 db péksütemény (pl. kifli vagy zsemle) vagy 1 közepes szelet kenyér/kalács vagy 12 evőkanál (20 dkg:3) főtt tészta/rizs vagy 3 evőkanál gabonapehely/müzli",
        "Hús/Tej: 1 adag = 2 dl tej/joghurt/kefír vagy 5 dkg túró vagy 3 dkg sajt vagy 1 tenyérnyi szelet (10 dkg) hús vagy 1 szelet (15 dkg) hal vagy 3-4 szelet (5 dkg) felvágott vagy 1 db tojás",
        "Magvak: pl. diót, mandulát, mogyorót, tökmagot, napraforgómagot."]):
        self.weekyear = year
        self.weekNumber = week_num
        self.foodEvents = foodEvents
        self.weekMin = weekMin
        self.weekMax = weekMax
        self.weekDays = weekDays
        self.dayMax = dayMax
        self.data = [[0] * len(weekDays) for i in range(len(foodEvents))]
        self.foodInfo = foodInfo
        
     