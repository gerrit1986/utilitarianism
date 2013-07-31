# -*- coding: utf-8 -*-

# = 1. Import Modules =
import math
import random


# = 2. Define Names =
names = ['Socrates', 'Plato', 'Aristotle', 'Hume', 'Kant', 'Wittgenstein', 
'Heidegger', 'Nietzsche', 'Schopenhauer']


# = 3. Helper Function for Updating the Clocks =
def updateClocks(population):
    for person in population:
        person.clock += 1


# = 4. Definition of Hedonistic Calculus Factors According to Chapter 2.4 =
# intensity, duration, certainty, propinquity, fecundity, purity, extent
intensity = 1
duration = 1

def getCertainty():
    return random.random()

def getPropinquity(person, judgement):
    """ Change pleasure or pain with respect to the amount of time that has 
        passed since the last congruent utterance to this person happened. """
    timestamp = person.getTimeStamp()
    if judgement > 0: # if judgement is positive
        if timestamp[0] >= 5 and timestamp == 'positive':
            propinquity = 2
        else:
            propinquity = 1
    elif judgement < 0: # if judgement is negative
        if timestamp[0] >= 5 and timestamp == 'negative':
            propinquity = 2
        else:
            propinquity = 1
    return propinquity

def getFecundity(judgement):
    random_number = random.random()
    if random_number >= 0.5 and judgement < 0: # if a negative judgement is rejected
        fecundity = 2
    else:
        fecundity = 1
    return fecundity

def getPurity(judgement,person):
    """ Takes the value ('positive', 'negative') of last utterance into 
        consideration. """
    last_judgement = person.timestamp[1]
    if (last_judgement == 'positive') and (judgement > 0):
        purity = 2
    elif (last_judgement == 'negative') and (judgement < 0):
        purity = 2
    elif (last_judgement == 'negative') and (judgement < 0):
        purity = 0.5
    elif (last_judgement == 'positive') and (judgement > 0):
        purity = 0.5
    else:
        purity = 1
    return purity

extent = 1


# = 5. Person Class with Properties and Methods for Persons =

class Person(object):
    population_number = 0
    
    def __init__(self, id_number, name):
        """
        Takes id_number (integer) and name (string).
        Generates a random initial pleasure value (float in between 0 and 1)
        and a random initial pain value (float in between 0 and 1).
		Updates population count.
        """
        self.id_number = id_number
        self.name = name
        self.pleasure = random.random()
        self.pain = random.random()
        self.clock = 0
        self.timestamp = (0,'not available')
        Person.population_number += 1
        last_judgement = 'not available'

    def getId(self):
        """
        Returns id_number of person instance.
        """
        return self.id_number

    def getName(self):
        """
        Returns name of person instance.
        """
        return self.name

    def getPleasure(self):
        """
        Returns pleasure value of person instance.
        """
        return self.pleasure

    def getPain(self):
        """
        Returns pain value of person instance.
        """
        return self.pain
    
    def getTimeStamp(self):
        return self.timestamp

    def getLastJudgement(self):
        return self.last_judgement

    def communicateMoralJudgement(self, person, judgement):
        """
        Communicates a moral judgement towards another person (not literally).
		Changes persons' pleasure or pain value depending the input value, 
        i. e. depending on the passed 'judgement' argument.
		Takes factors of the hedonistic calculus into consideration.
        """
        updateClocks(population)
        factors = intensity * duration * getPropinquity(person, judgement) * getFecundity(judgement) * getPurity(judgement,person) * extent
        # TODO: Apply those six factors above with effect on the quantities of pain or pleasure as well
        judgement = judgement * factors
        # There will be an utterance of a judgement if the certainty is greater or equal to 0.5
        certainty = getCertainty()
        if certainty >= 0.5:
            if judgement > 0:
                manner = "positively"
                person.last_judgement = 'positive'
                person.pleasure += judgement
                if person.pleasure > 1.0: # reset to upper bound if result was too high
                    person.pleasure = 1.0
                person.timestamp = (self.clock, 'positive') # modify person.timestamp
            
            elif judgement < 0:
                manner = "negatively"
                person.last_judgement = 'negative'
                person.pain -= judgement
                if person.pain > 1.0: # reset to upper bound if result was too high
                    person.pain = 1.0
                person.timestamp = (self.clock, 'negative') # modify person.timestamp
            # Uncomment two lines below for verbose output
            # print "%s judges %s %s, therefore %s is affected with the following impact: %s"\
            #        % (self.name, person.name, str(manner), person.name, str(judgement))


# = 6. Functions for the Evaluation of Pain and Pleasure Values =

def calculateSumOfPleasure(population):
    """
    Calculates sum of pleasure for the whole population.
    Takes a list of persons. Always starts with overall_pleasure = 0.
    :param population: a list of persons
    """
    overall_pleasure = 0.0
    for person in population:
        overall_pleasure += person.getPleasure()
    return overall_pleasure

def calculateAveragePleasure(population):
    """
    Calculates the average pleasure for the whole population.
    Takes a list of persons. Uses calculateSumOfPleasure as helper function.
    :param population: a list of persons
    """
    overall_pleasure = calculateSumOfPleasure(population)
    average_pleasure = overall_pleasure / len(population)
    print average_pleasure
    return average_pleasure

def calculateSumOfPain(population):
    """
    Calculates sum of pain for the whole population.
    Takes a list of persons. Always starts with overall_pain = 0.
    :param population: a list of persons
    """
    overall_pain = 0.0
    for person in population:
        overall_pain += person.getPain()
    return overall_pain

def calculateAveragePain(population):
    """
    Calculates the average pain for the whole population.
    Takes a list of persons. Uses calculateSumOfPain as helper function.
    :param population: a list of persons
    """
    overall_pain = calculateSumOfPain(population)
    average_pain = overall_pain / len(population)
    print average_pain
    return average_pain


# = 7. Simulation Flow =


# == 7.1 Initialize 10 Persons, Create a Population ==

person0 = Person(0, random.choice(names))
person1 = Person(1, random.choice(names))
person2 = Person(2, random.choice(names))
person3 = Person(3, random.choice(names))
person4 = Person(4, random.choice(names))
person5 = Person(5, random.choice(names))
person6 = Person(6, random.choice(names))
person7 = Person(7, random.choice(names))
person8 = Person(8, random.choice(names))
person9 = Person(9, random.choice(names))
population = [person0, person1, person2, person3, person4, person5, person6, 
person7, person8, person9]


# == 7.2 Run the Simulation ==

# === 7.2.1 Show Initial Average Pleasure of Population ===
print "POSITVE SCENARIO INITIAL VALUE - AVERAGE PLEASURE:"
average_pleasure = calculateAveragePleasure(population)
print "POSITIVE SCENARIO INITIAL VALUE - AVERAGE PAIN:"
average_pain = calculateAveragePain(population)


# === 7.2.2 Articulate Utterances of a) Ten Positive Moral Judgements ===
person1.communicateMoralJudgement(person2, +0.3)
person2.communicateMoralJudgement(person3, +0.5)
person3.communicateMoralJudgement(person1, +0.1)
person4.communicateMoralJudgement(person5, +0.1)
person5.communicateMoralJudgement(person1, +0.8)
person9.communicateMoralJudgement(person3, +0.4)
person7.communicateMoralJudgement(person2, +0.7)
person6.communicateMoralJudgement(person8, +0.6)
person9.communicateMoralJudgement(person7, +0.2)
person2.communicateMoralJudgement(person9, +0.7)


# === 7.2.3 Show the Effect on Populations's Pleasure ==
print "POSITIVE SCENARIO RESULT - AVERAGE PLEASURE:"
average_pleasure = calculateAveragePleasure(population)
print "POSITIVE SCENARIO RESULT - AVERAGE PAIN:"
average_pain = calculateAveragePain(population)
print "###################################################"


# === 7.2.4 Reset the values after evaluating the positive scenario ===
person0 = Person(0, random.choice(names))
person1 = Person(1, random.choice(names))
person2 = Person(2, random.choice(names))
person3 = Person(3, random.choice(names))
person4 = Person(4, random.choice(names))
person5 = Person(5, random.choice(names))
person6 = Person(6, random.choice(names))
person7 = Person(7, random.choice(names))
person8 = Person(8, random.choice(names))
person9 = Person(9, random.choice(names))
population = [person1, person2, person3, person4, person5, person6, person7, 
person8, person9]

print "NEGATIVE SCENARIO INITIAL VALUE - AVERAGE PLEASURE:"
average_pleasure = calculateAveragePleasure(population)
print "NEGATIVE SCENARIO INITIAL VALUE - AVERAGE PAIN:"
average_pain = calculateAveragePain(population)


# === 7.3.1 Articulate Utterances of b) Ten Negative Moral Judgements ===
person1.communicateMoralJudgement(person2, -0.3)
person2.communicateMoralJudgement(person3, -0.5)
person3.communicateMoralJudgement(person1, -0.1)
person4.communicateMoralJudgement(person5, -0.1)
person5.communicateMoralJudgement(person1, -0.8)
person9.communicateMoralJudgement(person3, -0.4)
person7.communicateMoralJudgement(person2, -0.7)
person6.communicateMoralJudgement(person8, -0.6)
person9.communicateMoralJudgement(person7, -0.2)
person2.communicateMoralJudgement(person9, -0.7)


# === 7.3.2 Check The Effect on Populations's Pain ===
print "NEGATIVE SCENARIO RESULT - AVERAGE PLEASURE:"
average_pleasure = calculateAveragePleasure(population)
print "NEGATIVE SCENARIO RESULT - AVERAGE PAIN:"
average_pain = calculateAveragePain(population)
print "###################################################"


# === 7.3.3 Reset the values after evaluating the negative scenario ===

person0 = Person(0, random.choice(names))
person1 = Person(1, random.choice(names))
person2 = Person(2, random.choice(names))
person3 = Person(3, random.choice(names))
person4 = Person(4, random.choice(names))
person5 = Person(5, random.choice(names))
person6 = Person(6, random.choice(names))
person7 = Person(7, random.choice(names))
person8 = Person(8, random.choice(names))
person9 = Person(9, random.choice(names))
population = [person1, person2, person3, person4, person5, person6, person7, 
person8, person9]

print "BALANCED SCENARIO INITIAL VALUE - AVERAGE PLEASURE:"
average_pleasure = calculateAveragePleasure(population)
print "BALANCED SCENARIO INITIAL VALUE - AVERAGE PAIN:"
average_pain = calculateAveragePain(population)


# === 7.4.1 Articulate Utterances of c) Five Positive and Five Negative Moral 
# Judgements ===
person1.communicateMoralJudgement(person2, -0.3)
person2.communicateMoralJudgement(person3, -0.5)
person3.communicateMoralJudgement(person1, +0.5)
person4.communicateMoralJudgement(person5, +0.3)
person5.communicateMoralJudgement(person1, -0.5)
person9.communicateMoralJudgement(person6, +0.8)
person7.communicateMoralJudgement(person2, -0.7)
person6.communicateMoralJudgement(person8, +0.2)
person9.communicateMoralJudgement(person7, -0.2)
person2.communicateMoralJudgement(person9, +0.7)


# === 7.4.2 Show the Effect on The Population's Pleasure ===
print "BALANCED SCENARIO RESULT - AVERAGE PLEASURE:"
average_pleasure = calculateAveragePleasure(population)


# === 7.4.3 Show the Effect on The Population's Pain ===
print "BALANCED SCENARIO RESULT - AVERAGE PAIN:"
average_pain = calculateAveragePain(population)
