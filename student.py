""" A Student class as base for method testing """
from datetime import date, timedelta
import requests


class Student:
    """A Student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """Returns full name of student"""
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        """Returns email of student"""
        firstname = self._first_name.lower()
        lastname = self._last_name.lower()
        return f"{firstname}.{lastname}@email.com"

    def alert_santa(self):
        """Turns true if student has been naughty"""
        self.naughty_list = True

    def apply_extension(self, days):
        """Applies an extension prolonging the end date"""
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        firstname = self._first_name
        lastname = self._last_name
        response = requests.get(
            "http://company.com/course-schedule/" + firstname + "/" + lastname
        )

        if response.ok:
            return response.text
        return "Something went wrong with the request."
