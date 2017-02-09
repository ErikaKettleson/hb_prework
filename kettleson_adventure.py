import random

challenging = [
    'panda',
    'marmoset',
    'fennec fox',
    'marmoset',
    'murder of crows',
]
easy = [
    'old cat',
    'lazy dog',
    'goldfish',
    'easy-going turtle',
    'retired pig',
]
color_words = [
    'purple',
    'rainbow',
    'brightly hued',
    'iridescent',
    'magically bright',
]
drab_challenging = [
    'screech owl',
    'jerboa',
    'eagle',
    'basket of eels',
    'large pike',
]
drab_easy = [
    'plain old dog',
    'smallish catfish',
    'hamster',
    'chill snake',
    'middle-age brown cat',
]
straight_up_crazy = [
    'bridge troll',
    'unicorn', 'angler fish',
    'poisonous caterpillar',
    'bucket of piranhas',
    'fighting chicken',
]


def is_pet_intense():
    # is_pet_intense - does the user want an intense pet?
    print "Okay! Well, do you like a challenge with your pet? Y or N?"
    challenge = raw_input("...")
    desires_intense_pet = None
    if challenge.upper() == "Y":
        print "Awesome! Okay one more question!"
        desires_intense_pet = True
    elif challenge.upper() == "N":
        desires_intense_pet = False
    return desires_intense_pet


def is_pet_colorful():
    # is_pet_colorful - does the user want an colorful pet?
    print "Do you prefer a pet that is bright/colorful?"
    color = raw_input("... Y or N? ")
    desires_colorful_pet = None
    if color.upper() == 'Y':
        desires_colorful_pet = True
    elif color.upper() == 'N':
        desires_colorful_pet = False
    return desires_colorful_pet


def no_pets_for_you():
    # no_pets_for_you - prints insult if user inputs anthing but Yy or Nn
    print "SRSLY! I only understand Y or N!!! Good luck with this {}".format(
        random.choice(straight_up_crazy)
    )


def color_easy():
    # color_easy - prints a colorful and easy pet
    print "I see!"
    print "I think you'd do well with a {} {}!".format(
        random.choice(color_words),
        random.choice(easy),
    )


def drab_easy_pet():
    # drab_easy_pet - prints a drab yet easy pet
    print "I see....I think i have something in the back closet just for you!"
    print "Here's Johnny! Your new {}!".format(
        random.choice(drab_easy)
    )


def drab_challenge():
    # drab_challenge - prints a drab & difficult pet
    print "What a saint, taking in the hardest of the drab!"
    print "I think you these {} need some love!".format(
        random.choice(drab_challenging)
    )


def color_challenge():
    # color_challenge - prints a colorful and difficult pet
    print "You're my favorite kind of customer!"
    print "I think you are going to do great with a {} {}!".format(
        random.choice(color_words),
        random.choice(challenging),
    )


def final_determination(desires_intense_pet, desires_colorful_pet):
    # final_determination - uses 2 arguments about color & intensity
    # determines final pet suggestion
    if desires_intense_pet and desires_colorful_pet:
        color_challenge()
    elif desires_intense_pet and not desires_colorful_pet:
        drab_challenge()
    elif not desires_intense_pet and desires_colorful_pet:
        color_easy()
    else:
        drab_easy_pet()


def game():
    # introduces pet store game & asks if user is ready
    # once ready, user goes through 2 decisions
    # calls color fxn and intensity fxn and stores values
    # desires_intense_pet & desires_colorful_pet answers
    # will determine final determination
    user = raw_input("What's your name? ... ")
    print "Hi " + user + "!"
    print "You're at the best pet store in town! I'm here to help you choose!"
    print "Personally, I have always wanted a {}.".format(
        random.choice(straight_up_crazy)
    )
    print "But enough about me! I\'ll ask a few questions so we can hone in on your perfect pet!"
    print "...Ready? Y or N?"
    ready = raw_input("...")
    if ready.upper() == "N":
        print "If you're that nervous I'll just give you a {}! That should help!".format(
            random.choice(drab_easy)
        )
    elif ready.upper() == "Y":
        print "Great! " + user + " , let's do it!"
        desires_intense_pet = is_pet_intense()
        if desires_intense_pet is None:
            no_pets_for_you()
        elif not desires_intense_pet:
            print "I get it you already have your hands full with {}!".format(
                random.choice(straight_up_crazy)
            )
        print "I just have one more question for you!"
        desires_colorful_pet = is_pet_colorful()
        if desires_colorful_pet is None:
            no_pets_for_you()
        else:
            final_determination(desires_intense_pet, desires_colorful_pet)

game()
