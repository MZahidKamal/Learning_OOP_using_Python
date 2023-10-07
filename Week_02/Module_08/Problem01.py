#-----------------------------------------------------------------------------------------------------------------------
# Python Mid Term Exam
# https://docs.google.com/document/d/1OZH_1S1pcmloJz-PZWwLVbLcx0Zob1YVoWNTvVIXUNI/edit
# Problem 01:
"""
Make a class named Star_Cinema which will have one class attribute named hall_list which is an empty list initially.
Make a method named entry_hall() to insert an object of class Hall (Described below) inside its hall_list.
"""
#-----------------------------------------------------------------------------------------------------------------------
class StarCinema:
    hall_list = []

    def entry_hall(self, hall):                 # Here hall will be an object of class Hall.
        self.hall_list.append(hall)
#-----------------------------------------------------------------------------------------------------------------------
