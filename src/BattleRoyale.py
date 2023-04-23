import csv
class SuperPower:
    def __init__(self, name, intelligence, strength, speed, durability, power, combat):
        self.name = name
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.durability = durability
        self.power = power
        self.combat = combat

    def getStats(self):
        return self.strength + self.durability + self.power

    def getBonus(self):
        return 0


class Hero(SuperPower):
    def getStats(self):
        return self.intelligence + self.speed + self.combat

    def getBonus(self):
        bonus = super().getBonus()
        if self.intelligence > 90:
            bonus += 10
        elif self.combat < 70:
            bonus -= 15
        return bonus


class Villain(SuperPower):
    def __init__(self, name, intelligence, strength, speed, durability, power, combat):
        super().__init__(name, intelligence, strength, speed, durability, power, combat)
        self.__name = name
        self.__intelligence = intelligence
        self.__strength = strength
        self.__speed = speed
        self.__durability = durability
        self.__power = power
        self.__combat = combat

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname

    @property
    def intelligence(self):
        return self.__intelligence

    @intelligence.setter
    def intelligence(self, newintelligence):
        if isinstance(newintelligence, int) and 0 <= newintelligence <= 105:
            self.__intelligence = newintelligence
        else:
            raise ValueError("It must be an integer between 0 and 105.")

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, newstrength):
        if isinstance(newstrength, int) and 0 <= newstrength <= 105:
            self.__strength = newstrength
        else:
            raise ValueError("It must be an integer between 0 and 105.")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, newspeed):
        if isinstance(newspeed, int) and 0 <= newspeed <= 105:
            self.__speed = newspeed
        else:
            raise ValueError("It must be an integer between 0 and 105.")

    @property
    def durability(self):
        return self.__durability

    @durability.setter
    def durability(self, newdurability):
        if isinstance(newdurability, int) and 0 <= newdurability <= 105:
            self.__durability = newdurability
        else:
            raise ValueError("It must be an integer between 0 and 105.")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, newpower):
        if isinstance(newpower, int) and 0 <= newpower <= 105:
            self.__power = newpower
        else:
            raise ValueError("It must be an integer between 0 and 105.")

    @property
    def combat(self):
        return self.__combat

    @combat.setter
    def combat(self, newcombat):
        if isinstance(newcombat, int) and 0 <= newcombat <= 105:
            self.__combat = newcombat
        else:
            raise ValueError("It must be an integer between")


    def getStats(self):
        return self.strength + self.durability + self.power

    def getBonus(self):
        if self.strength > 80:
            return 5
        elif self.durability > 80:
            return 5
        elif self.power > 80:
            return 5
        elif self.combat < 60:
            return -10
        else:
            return 0


heroes_and_villains = []

with open('../SuperpowerDataset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Alignment"] == "good":
            hero = Hero(row['Name'], int(row['Intelligence']), int(row['Strength']), int(row['Speed']), int(row['Durability']), int(row['Power']), int(row['Combat']))
            heroes_and_villains.append(hero)
        elif row["Alignment"] == "bad":
            villain = Villain(row['Name'], int(row['Intelligence']), int(row['Strength']), int(row['Speed']), int(row['Durability']), int(row['Power']), int(row['Combat']))
            heroes_and_villains.append(villain)


class Child(Hero):
    def __init__(self, name, intelligence, strength, speed, durability, power, combat, gender):
        super().__init__(name, intelligence, strength, speed, durability, power, combat)
        self.gender = gender

    def getBonus(self):
        if self.gender == "Male":
            return 10
        else:
            return super().getBonus()

class RedHair(Villain):
    def __init__(self, name, intelligence, strength, speed, durability, power, combat, haircolor):
        super().__init__(name, intelligence, strength, speed, durability, power, combat)
        self.haircolor = haircolor

    def getBonus(self):
        if self.haircolor == "Red":
            return 7
        else:
            return super().getBonus()
def getCharacterType(character_name):
    for character in heroes_and_villains:
        if character.name == character_name:
            return "Hero" if isinstance(character, Hero) else "Villain"
    return "Unknown"
