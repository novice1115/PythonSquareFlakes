"""
Create 3 different classes Length, Weight, and Time
Add respective attributes to store values.
Add static methods for conversion of different units.
Example:
Length: cm to inches, kilometer to miles, etc
Weight: KG to pounds, gram to Ounces, etc.
Time: seconds to hours, milliseconds to seconds
"""

class Length:
    @staticmethod
    def mile_to_kilometers(mile):
        return mile*1.6
    
    @staticmethod
    def kilometers_to_mile(kilometers):
        return kilometers/0.621

class Weight:
    @staticmethod
    def pounds_to_kilograme(pounds):
        return pounds/2.2
    
    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms*2.2

class Time:
    @staticmethod
    def seconds_to_hours(seconds):
        return seconds/3600

    @staticmethod
    def hours_to_seconds(hours):
        return hours*3600

print(Length.kilometers_to_mile(2))
print(Length.mile_to_kilometers(2))
print(Weight.kilograms_to_pounds(10.6))
print(Weight.pounds_to_kilograme(190))
print(Time.hours_to_seconds(3.5))
print(Time.seconds_to_hours(360.2))