"""
conversions.py
--------------

Unit conversion functions for the Scientific Calculator.
"""


class Converter:

    # ======================================
    # Temperature
    # ======================================

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5 / 9 + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9 / 5 + 32

    # ======================================
    # Length
    # ======================================

    @staticmethod
    def meter_to_kilometer(m):
        return m / 1000

    @staticmethod
    def kilometer_to_meter(km):
        return km * 1000

    @staticmethod
    def meter_to_centimeter(m):
        return m * 100

    @staticmethod
    def centimeter_to_meter(cm):
        return cm / 100

    @staticmethod
    def meter_to_millimeter(m):
        return m * 1000

    @staticmethod
    def millimeter_to_meter(mm):
        return mm / 1000

    @staticmethod
    def meter_to_inch(m):
        return m * 39.3701

    @staticmethod
    def inch_to_meter(i):
        return i / 39.3701

    @staticmethod
    def meter_to_feet(m):
        return m * 3.28084

    @staticmethod
    def feet_to_meter(ft):
        return ft / 3.28084

    # ======================================
    # Weight
    # ======================================

    @staticmethod
    def kilogram_to_gram(kg):
        return kg * 1000

    @staticmethod
    def gram_to_kilogram(g):
        return g / 1000

    @staticmethod
    def kilogram_to_pound(kg):
        return kg * 2.20462

    @staticmethod
    def pound_to_kilogram(lb):
        return lb / 2.20462

    @staticmethod
    def kilogram_to_ounce(kg):
        return kg * 35.274

    @staticmethod
    def ounce_to_kilogram(oz):
        return oz / 35.274

    # ======================================
    # Speed
    # ======================================

    @staticmethod
    def kmph_to_mps(speed):
        return speed / 3.6

    @staticmethod
    def mps_to_kmph(speed):
        return speed * 3.6

    # ======================================
    # Time
    # ======================================

    @staticmethod
    def seconds_to_minutes(sec):
        return sec / 60

    @staticmethod
    def minutes_to_seconds(mins):
        return mins * 60

    @staticmethod
    def minutes_to_hours(mins):
        return mins / 60

    @staticmethod
    def hours_to_minutes(hours):
        return hours * 60

    @staticmethod
    def hours_to_seconds(hours):
        return hours * 3600

    @staticmethod
    def seconds_to_hours(sec):
        return sec / 3600