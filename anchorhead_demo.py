# This file is basically a short demo of the game Anchorhead, by Michael Gentry.
#   The text used is almost entirely taken from Anchorhead. The original game
#   was made using Inform v6.15 (Library 6/7), and my demo version is intended
#   for Python 2.7. I created this file for Exercise 36 of Learn Python the Hard
#   Way, the goal of which is to make a game using the skills learned up to that
#   point of the book. I thought the exercise would be much more interesting if
#   I were to mimic a game I really enjoyed. For reference, the full game can be
#   found at http://pr-if.org/play/anchorhead/ (at least as of this writing.
#                       -- Aron Neu, 6/11/2017

# Import modules
from sys import exit            # to end the game
from random import randint      # for the flavor text
from time import sleep          # for a typewriter effect in the intro
import os                       # allows CLS and PAUSE
import sys                      # also used for the typewriter effect

# Initialize variables
#   The real estate office front door and desk begin the game locked
#   The trash can in the alley begins the game away from the building
#   You begin the game NOT standing on the trash can.
#   You begin the game NOT being able to recall the name Verlac
#   You begin the game without the house keys
# RE_DESK_LOCKED isn't actually necessary in this demo version of the game, but
#   I left it in since it's logical to include (and because I might expand this
#   project at a later time.)
RE_door_locked = True
RE_desk_locked = True
trash_placed = False
on_can = False
Verlac_knowledge = False
house_keys = False

# Defining the prompt character for user input
prompt = ">"

# This defines a function that clears the screen.
# Apparently cls is the Windows command to clear the screen, while clear is
#   used in Linux. This was a suggestion found on Stack Overflow.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')                            # NOTE: I don't know where to find a list of os.system commands

# These next two functions are just to add ambiance. Every time the player
#   enters some input, there is a chance of some flavor text appearing.
#   This flavor text depends on whether the player is indoors or outdoors,
#   with one function for each.
def background_out():
    result = randint(1, 20)
    if result == 1:
        print "Overhead, the swollen clouds flicker ominously with a greenish haze of sheet lightning.\n"
    elif result == 2:
        print "A sudden gust of wind blows a cold spray of rain into your face.\n"
    elif result == 3:
        print "In the distance, you can hear the lonesome keening of a train whistle drifting on the wind.\n"
    elif result == 4:
        print "The rain slackens off momentarily to a weak drizzle, then returns afresh in a brief, freezing downpour.\n"
    elif result == 5:
        print "The clouds overhead mutter restlessly to themselves.\n"

def background_in():
    result = randint(1, 20)
    if result == 1:
        print "You can hear a fly buzzing around, right around your head.\n"
    elif result == 2:
        print "You can hear a fly buzzing around, somewhere nearby.\n"
    elif result == 3:
        print "You can hear a fly buzzing around, hovering over the back of your neck.\n"
    elif result == 4:
        print "You can hear a fly buzzing around, somewhere in the next room.\n"
    elif result == 5:
        print "Through the walls, you can faintly hear the rumble of distant thunder.\n"

# ON PRINTING: The triple-quotes are often used after PRINT with text that
#   doesn't begin until the next line. This served two purposes: to start the
#   PRINT after a blank line appears on the terminal, and to help ensure even
#   width of the lines (that's longer than the Python-style 80 character limit
#   would allow for).

# The in-game help function prints some directional text
def help():
    print """
The primary commands in this game are simply abbreviated cardinal directions (nw, n, ne, e,
se, s, sw, w).  Additionally, typing i or inventory will display your current inventory, and
typing l or look will describe your surroundings. Beyond that, just try to describe what it
is you want to do (i.e., search the desk). Typing quit or exit will leave the game. Note
that this version of the game is not only incomplete but also woefully inadequate, so your
action choices are fairly limited.\n"""

# The player has the ability to check their inventory at any time. I don't
#   really know how to handle an inventory properly yet.  This is clunky, but
#   it works fine for this limited "demo."
def inv():
    print """
You are wearing your wedding ring, your trenchcoat, and your clothes; in addition, you
have in your hand your umbrella."""
    if house_keys == True:
        print "Your keyring includes a key to the house and a key to the cellar.\n"
    else:
        print "It's a strange feeling, not having any keys.  Moving certainly is a bit unnerving.\n"

# The in-game quit function allows the player to exit without using CTRL+C
def quit():
    print "\nAre you sure you want to quit?\n"
    choice = raw_input(prompt).lower()
    if choice in ("y", "yes", "quit", "exit"):
        print "\nUntil next time, then.\n"
        exit()
    else: print "\nBack to it, then!\n"


################################################################################
#################### This is a quote to start the game off. ####################
################################################################################

# This is intended to be the first fxn called in the game.
def title_screen():
    clear()
# The spacing used here is quite intentional, both for the quote and author
#   (aligned with each other) and for the game title, which is a bit farther
#   out (likely more towards the screen center).
    quote1 = """
                    The oldest and strongest emotion of mankind
                    is fear, and the oldest and strongest kind
                    of fear is fear of the unknown.\n"""
    HPL = """
                    -- H.P. Lovecraft"""
    title = """
                       A N C H O R H E A D"""

    print "\n\n\n\n\n\n\n\n\n\n"

# These FOR loops mimic a typewriter effect, which might get annoying. But so
#   far, I think it looks neat. It's a text adventure, after all - and a dated
#   one at that (set in 1997). SLEEP() forces a pause, WRITE() is basically the
#   same as PRINT, and FLUSH() forces output (flushes the terminal's cache).
#   Sometimes the terminal's cache will save things in loops and output them
#   all at once for efficiency, which would ruin the typewriter effect.
    for char in quote1:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    sleep(0.5)

    for char in HPL:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    sleep(1)

    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

    for char in title:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    print "\n\n\n\n\n"

    sleep(1)

# prints "Press any key to continue . . ." and waits for any input
    os.system("pause")                                                          #NOTE: This "pause" is apparently Windows-specific, and frowned upon.
# At the end of this title screen fxn, I call the INTRO() fxn. This method of
#   breaking it up by fxns is not required, but it was the first thing I thought
#   of, and it works well to break up the code, too.
    intro()


################################################################################
######################### This is the introductory text. #######################
################################################################################

def intro():
    clear()

    intro_text = """\n
You take a deep breath of salty air as the first raindrops begin to spatter the pavement,
and the swollen, slate-colored clouds that blanket the sky mutter ominous portents
amongst themselves over the little coastal town of Anchorhead.

Squinting up into the glowering storm, you wonder how everything managed to happen so
fast. The strange phone call over a month ago, from a lawyer claiming to represent the
estate of some distant branch of Michael's family, was bewildering enough in itself... but
then the sudden whirlwind of planning and decisions, legal details and travel
arrangements, the packing up and shipping away of your entire home, your entire life...

Now suddenly here you are, after driving for the past two days straight, over a thousand
miles away from the familiar warmth of Texas, getting ready to move into the ancestral
mansion of a clan of relatives so far removed that not even Michael has ever heard of
them. And you've only been married since June and none of this was any of your idea in
the first place, and already it's starting to rain.

These days, you often find yourself feeling confused and uprooted.

You shake yourself and force the melancholy thoughts from your head, trying to focus on
the errand at hand. You're to meet with the real estate agent and pick up the keys to your
new house while Michael runs across town to take care of some paperwork at the
university. He'll be back to pick you up in a few minutes, and then the two of you can
begin the long, precarious process of settling in.

A sullen belch emanates from the clouds, and the rain starts coming down harder -- fat,
cold drops smacking loudly against the cobblestones. Shouldn't it be snowing in New
England at this time of year? With a sigh, you open your umbrella.

Welcome to Anchorhead...\n\n\n\n"""

    print "November, 1997."

    sleep(1)

# This typewriter effect is much faster.  I can read slightly faster than this,
#   but even so, it's kind of distracting and/or stressful when it's too fast.
    for char in intro_text:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()

    sleep(1)

# prints "Press any key to continue . . ." and waits for any input
    os.system("pause")                                                          #NOTE: This "pause" is apparently Windows-specific, and frowned upon.
# calls the FIRST_DAY fxn to progress
    first_day()


################################################################################
######################### Another quote, for day one. ##########################
################################################################################

def first_day():
    clear()
    quote2 = """
                    I was far from home, and the spell of the eastern
                    sea was upon me.\n"""
    HPL = """
                    -- H.P. Lovecraft"""

    print "\n\n\n\n\n"
    print "              * THE FIRST DAY *"
    print "\n\n\n\n\n"

    for char in quote2:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    sleep(0.5)

    for char in HPL:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    print "\n\n\n\n\n\n\n\n\n\n\n\n"

    sleep(1)

    # prints "Press any key to continue . . ." and waits for any input
    os.system("pause")                                                          #NOTE: This "pause" is apparently Windows-specific, and frowned upon.
    clear()

    print "ANCHORHEAD"
    print "An interactive gothic by Michael S. Gentry\n"
    print "(Type HELP for some instructions.)"

# Calls the function for the first room after all this introductory text
    outside_office()


################################################################################
#################################    ROOM 1    #################################
################################################################################

# All the rooms are defined by their own functions, which activate relevant
#   global variables and print out a description. They each rely on a WHILE
#   loop to take in user input, and they rely on large IF blocks to capture
#   what I thought were the most likely user choices. Moving between rooms is
#   handled by calling the destination room's function.
# IF STATEMEMTS: It's worth noting that IF statements are order-sensitive. In
#   this game, the order matters in cases where the possible user input appears
#   in more than one check (ex: "window" in the alley.)  Generically, the order
#   I've chosen (that doesn't impact functionality) is look, help, inventory,
#   quit, non-useful travel choices, object interaction, and finally legitimate
#   travel choices.  This is simply for consistency between rooms.

def outside_office():
    global RE_door_locked
    global house_keys
    print """
OUTSIDE THE REAL ESTATE OFFICE
A grim little cul-de-sac, tucked away in a corner of the claustrophobic tangle of narrow,
twisting avenues that largely constitute the older portion of Anchorhead. Like most of the
streets in this city, it is ancient, shadowy, and leads essentially nowhere. The lane ends
here at the real estate agent's office, which lies to the east, and winds its way back toward
the center of town to the west. A narrow, garbage-choked alley opens to the southeast.\n"""

# After activating global variables and printing the room description, the
#   user choices are handled by WHILE loops that contain detailed IF blocks.
    while True:
# The addition of .LOWER() makes user input case-insensitive
        choice = raw_input(prompt).lower()
        if choice == "look" or choice == "l":
            outside_office()
        elif choice == "help":
            help()
        elif choice == "i" or choice == "inventory":
            inv()
        elif choice == "quit" or choice == "exit":
            quit()
# Every room will have some directions that aren't valid choices
        elif choice in ("nw", "n", "ne", "s", "sw"):
            print """
The street goes west from here. You can enter the office to the east or the alley to
the southeast.\n"""
        elif "knock" in choice:
            print """
You rap on the door's glass sharply, peering through it into the dark room inside. Nobody
answers. Strange; you just talked to the real estate agent - Miss Benson, you think it
was - yesterday. She was going to meet you here.\n"""
        elif "door" in choice and RE_door_locked == True:
            print "\nIt seems to be locked.\n"
# This door starts the game out locked, but you can unlock it once inside the
#   office. Traveling through the door isn't actually necessary, but it's
#   logical and a shorter path.
        elif choice == "e":
            print "\n(opening the real estate office door first)"
            if RE_door_locked == True:
                print "It seems to be locked.\n"
            else:
                office()
# In the full game, you can travel west right off the bat, but in this snippet,
#   I've only recreated four rooms.  Exploring the entire town right away can
#   be a bit confusing anyway, as your immediate goal is to get the house keys.
#   In this demo, it's really your _only_ goal.
        elif choice == "w":
            if house_keys == False:
                print """
You start heading west along the winding lane but soon change your mind and turn around.
You'll have plenty of time to explore Anchorhead once you've moved into your home. But first,
you need to get those keys from the real estate agent.\n"""
            else:
                print "Congratulations! You've finished my short demo of Anchorhead."
                print "Once I'm better at Python, I will likely try to improve and expand upon this."
                print "(But you might just want to play the real version in the meantime.)\n"
                exit()
        elif choice == "se":
            alley()
        else:
            print "\nThat's not a verb I recognize.\n"
# As this room is outdoors, it involves the background_out fxn.  This is
#   intentionally placed at the end of the WHILE loop.
        background_out()


################################################################################
#################################    ROOM 2    #################################
################################################################################

# Comments in rooms 2~4 will be a bit more sparse, as most of the code choices
#   have already been explained previously.
def alley():
    global on_can
    global trash_placed
# Every time you enter the alley, regardless of whether it's from the file room
#   or outside the office, you start out standing on the ground (and not on top
#   of the garbage can). This is called here to reset the variable to FALSE
#   whenever you enter the alley.
    on_can = False
    print """
ALLEY
This narrow aperture between two buildings is nearly blocked with piles of rotting
cardboard boxes and overstuffed garbage cans. Ugly, half-crumbling brick walls to either
side totter oppressively over you. The alley ends here at a tall, wooden fence.
High up on the wall of the northern building there enis a narrow, transom-style window.\n"""
    while True:
        choice = raw_input(prompt).lower()
# In the Alley, LOOK can't just call ALLEY(), because the function also sets
#   on_can to FALSE. So here it just prints instead.
        if choice == "look" or choice == "l":
            print """
ALLEY
This narrow aperture between two buildings is nearly blocked with piles of rotting
cardboard boxes and overstuffed garbage cans. Ugly, half-crumbling brick walls to either
side totter oppressively over you. The alley ends here at a tall, wooden fence.
High up on the wall of the northern building there is a narrow, transom-style window.\n"""
        elif choice == "help":
            help()
        elif choice == "i" or choice == "inventory":
            inv()
        elif choice == "quit" or choice == "exit":
            quit()
        elif choice in ("ne", "e", "se", "s", "sw", "w"):
            print "\nYou can only exit the alley to the northwest.\n"
        elif "box" in choice:
            print "\nThe boxes are much too flimsy to be of use.\n"
        elif "fence" in choice:
            print """
Unfortunately, the fence is too far from the window to be of much use.  It's also
intimidatingly tall.  You have no intention of climbing it today.\n"""
        elif "on" in choice and "can" in choice:
            print "\nYou clamber onto the wobbling garbage can, precariously balanced.\n"
            on_can = True
            if trash_placed == True:
                print "You can just reach the lower edge of the window from here.\n"
        elif "off" in choice and "can" in choice:
            if on_can == True:
                print "\nCarefully, you descend.\n"
                on_can = False
            else:
                print "\nBut you aren't on the garbage can at the moment.\n"
# The option to push the garbage can under the window has to be placed before
#   the travel option "n" or "window", because they both check for "window",
#   and this one needs precedence.
        elif "push" in choice or "move" in choice and "can" in choice:
            if "wall" in choice or "window" in choice:
                print """
Grunting and holding your breath, you manhandle one of the filthy cans under the window.\n"""
                trash_placed = True
            else:
                print "\nYou push the garbage cans around aimlessly.\n"
# The option to travel north or enter the window has to be placed after the
#   option to push the can under the window.  See previous comment.
        elif "wall" in choice:
            print """
You don't trust your grip on the bricks in this rain. You'll have to find another way.\n"""
        elif choice == "n" or "window" in choice:
            if on_can == False:
                print "\nThe window is too high.\n"
            elif trash_placed == False:
                print """
Hmm. You still can't quite reach, because the garbage can is too far away from the wall.
Perhaps if you pushed it closer...\n"""
            else:
                print """
You open the transom window and close your umbrella in preparation for the effort. It's
a tight squeeze, but you just manage to wriggle through, dropping quietly to the floor
inside."""
                file_room()
        elif choice == "nw":
            if on_can == True:
                print "\nYou'll have to get off the garbage can first.\n"
            else:
                outside_office()
        else:
                print "\nThat's not a verb I recognize.\n"
# As this room is outdoors, it involves the background_out fxn.  This is
#   intentionally placed at the end of the WHILE loop.
        background_out()


################################################################################
#################################    ROOM 3    #################################
################################################################################

# Comments in rooms 2~4 will be a bit more sparse, as most of the code choices
#   have already been explained previously.
def file_room():
    global Verlac_knowledge
    global house_keys
    print """
FILE ROOM
Peering through the murk, you can make out the blocky outlines of filing cabinets lining
the walls and a doorway to the west. A window high up on the south wall lets in a very
faint illumination.\n"""
    while True:
        choice = raw_input(prompt).lower()
        if choice == "look" or choice == "l":
            file_room()
        elif choice == "help":
            help()
        elif choice == "i" or choice == "inventory":
            inv()
        elif choice == "quit" or choice == "exit":
            quit()
        elif choice in ("nw", "n", "ne", "e", "se", "sw"):
            print "\nYou can't go that way.\n"
        elif "fly" in choice:
            print """
The fly immediately goes silent, before you can even move, and you fail to locate it.
It's as if it senses your thoughts. Creepy.\n"""
        elif "fil" in choice or "cabinet" in choice:
            if Verlac_knowledge == False or "verlac" not in choice:
                print """
There must be hundreds of files here, too many to browse through. You'll have to look up
something specific if you want to find anything.\n"""
            else:
                print """
Strange; the file on the Verlac property has been cleaned out. Title, deed, all the papers,
all of it gone. There is, however, a set of keys tucked down in the hanging folder. You
quickly pocket them. Now you just need to find Michael.\n"""
                house_keys = True
        elif choice == "s":
            alley()
        elif choice == "w":
            office()
        else:
                print "\nThat's not a verb I recognize.\n"
# As this room is indoors, it involves the background_in fxn.  This is
#   intentionally placed at the end of the WHILE loop.
        background_in()


################################################################################
#################################    ROOM 4    #################################
################################################################################

# Comments in rooms 2~4 will be a bit more sparse, as most of the code choices
#   have already been explained previously.
def office():
    global Verlac_knowledge
    global RE_door_locked
    global RE_desk_locked

    print """
OFFICE
Pallid gray light trickles in through the drawn blinds. The office is deserted, papers still
scattered across the top of the desk. The front door lies west, and the file room lies east.

Sitting on the corner of the paper-strewn desk are a telephone and an answering machine.

Someone seems to have left a cup of coffee sitting out, half-finished and cold.\n"""
    while True:
        choice = raw_input(prompt).lower()
        if choice == "look" or choice == "l":
            office()
        elif choice == "help":
            help()
        elif choice == "i" or choice == "inventory":
            inv()
        elif choice == "quit" or choice == "exit":
            quit()
        elif choice in ("nw", "n", "ne", "sw", "s", "se"):
            print """
The only exits are out the front door to the west, or back through the file room to the east.\n"""
        elif "fly" in choice:
            print """
The fly immediately goes silent, before you can even move, and you fail to locate it.
It's as if it senses your thoughts. Creepy.\n"""
        elif "unlock" in choice and "door" in choice:
            print "\nYou unlock the office door.\n"
            RE_door_locked = False
        elif "desk" in choice:
            print "\nOn the desk are some papers, a telephone and an answering machine."
            print "Sifting through the paperwork, you find nothing that catches your attention."
            if RE_desk_locked == True:
                print "Unfortunately, the desk drawer is locked and you do not have the key.\n"
        elif "paper" in choice:
            print "\nSifting through the paperwork, you find nothing that catches your attention.\n"
        elif "phone" in choice:
            print """
You start to dial out, but you can't get anything but a busy signal no matter how much you
jiggle the receiver. Frustrated, you hang up.\n"""
        elif "door" in choice and RE_door_locked == True:
            print "\nIt seems to be locked.\n"
        elif "drawer" in choice:
            print "\nThe desk drawer remains locked.\n"
        elif "coffee" in choice or "cup" in choice:
            print "\nIt would really be best to just ignore the cold, murky coffee.\n"
        elif "machine" in choice:
            print '''
A simple answering machine, with a small display indicating messages received and a
button labeled "PLAY".\n'''
        elif "play" in choice:
            print """
For a while there is nothing but a quiet hiss, followed by intermittent skirls of strange-
sounding static. It sounds like one of those annoying glitches where the caller hangs up
but the machine keeps recording anyway. Then, barely audible through the static, you
detect what sounds like a human voice whispering a single word:\n"""
# An attempt to print in bold, which yields yellow for some reason, which
#   probably sets the key text (Verlac.) apart from the rest better than bold
#   would have anyway. Maybe it prints bold on Linux.
            print '\033[93m' + '"Verlac."' + '\033[0m'
            print """
The machine beeps.

A brief shudder ripples up your back. You remember now, "Verlac" is the name of this branch
of Michael's family.\n"""
            Verlac_knowledge = True
        elif choice == "e":
            file_room()
        elif choice == "w":
            print "\n(opening the real estate office door first)"
            if RE_door_locked == True:
                print "It seems to be locked.\n"
            else:
                outside_office()
        else:
            print "\nThat's not a verb I recognize.\n"
        # As this room is indoors, it involves the background_in fxn.  This is
        #   intentionally placed at the end of the WHILE loop.
        background_in()


################################################################################
############################### Start the game! ################################
################################################################################

# Normally, the game begins by calling TITLE_SCREEN(), which later calls
#   INTRO(), which later calls FIRST_DAY(), which finally calls
#   OUTSIDE_OFFICE(), placing the user in the game.
title_screen()

# For troubleshooting and tweaking, it was often convenient to bypass all that
#   and just start in the first room.
# outside_office()
