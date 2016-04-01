#! /usr/bin/python

import sys

from itertools import (
    cycle,
    islice
)

def find_survivor(number):
    """
    Find survivor gives the surviving number for the following problem
    There are N people standing in a circle. Let's number them 0 through (N-1).
    Person 0 has a sword. He kills the person alive to his left and passes the sword along to the next (alive) person.
    That person in turn kills the person alive to his left and the sword on.
    This continues till there is only one person alive.
    """
    
    survivors = range(number)
    left = number
    sword_index = 0
    sword_number = 0
    while left > 1:
        # Create a circle from the survivors of last iteration
        circle = cycle(survivors)
        # Go to the person with the sword currently
        circle_from_sword = islice(circle, sword_index, None)
        not_killed = circle_from_sword.next()
        # The person next to him is killed
        killed = circle_from_sword.next()
        print "%s kills %s" % (not_killed, killed)
        left = left - 1
        # And the next person is awarded the sword and survivor circle recreated
        sword_number = circle_from_sword.next()
        print "%s recieves the sword" % sword_number
        survivors.remove(killed)
        sword_index = survivors.index(sword_number)

    return sword_number

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "The number of arguments are too few. Add the number of total people"
    else:
        print "The final survivor is %s" %(find_survivor(int(sys.argv[1])))