from django.db import models
import random

class Student:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()


class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        self.sneaky = False # remove after testting

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):


    def __init__(self, sneaky=True, **kwargs):
        super().__init__(**kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))


    def hide(self, light_level):
        return self.sneaky and light_level < 10

