import time

def invalid():
    print("Sorry, that's not a vaild input. Please try again.")

print("HARRY'S BIZARRE ADVENTURE")
time.sleep(1)
question1 = True
while question1:
    print("Would you like to play?")
    print("A. Yes.")
    print("B. No.")
    choice1 = input()
    if choice1 == 'A':
        question1 = False
        print("Starting now...")
        time.sleep(1.5)
        print("----")
        time.sleep(1)
        print("Harry wakes up. It's 6.30 AM. He has a flight to attend today.")
        time.sleep(1)
        print("He gets out his bed and prepares for his day.")
        time.sleep(1)
        print("He packs everything, and goes to the airport safe and sound.")
        time.sleep(1)
        print("However, when he gets there, he realises his lucky charm is missing!")
        time.sleep(1)
        question2 = True
        while question2:
            print("But his flight is coming soon... What should he do about it?")
            print("A. Go get his lucky charm back and risk missing his flight.")
            print("B. Stay in the airport and wait for the flight.")
            choice2 = input()
            if choice2 == 'A':
                question2 = False
                print("Harry then goes back home to get his lucky charm.")
                time.sleep(1)
                print("He believes he will have a lot of luck on his journey with it.")    
                time.sleep(1)      
                print("And then, he proceeds to head back to the airport.")
                time.sleep(1)
                print("He notices he missed his initial flight, so he sits to wait more.")
                time.sleep(1)
                print("And then... it finally began.")
                time.sleep(1)
                print("The flight goes smoothly, and he arrives to the new land safe and sound.")
                time.sleep(1)
                print("He goes on with getting a hotel room for now and whatnot.")
                time.sleep(1)
                print("Harry goes outside, to shop for food supplies, but then...")
                time.sleep(1)
                print("He notices a shady man looking over to him!")
                time.sleep(1)
                print("The man approaches him, saying he wants 10 dollars.")
                time.sleep(1)
                print("He offers to give a mushroom in exchange.")
                question3A = True
                while question3A:
                    print("THe mushroom might be bad! What should Harry do?")
                    print("A. Give the 10 dollars to the man.")
                    print("B. Refuse to give any money to the man.")
                    choice3A = input()
                    if choice3A == 'A':
                        question3A = False
                        print()
                    elif choice3A == 'B':
                        question3A = False
                        print()
                    else:
                        invalid()
                        time.sleep(1)
            elif choice2 == 'B':
                question2 = False
                print("Harry proceeds to stay in the airport and patiently wait for his flight.")
                time.sleep(1)
                print("Time goes by, and he gets in the plane.")
                time.sleep(1)
                print("During the flight, he wonders how having no lucky charm will affect him.")
                time.sleep(1)
                print("And he finally arrives in the unknown land, but then...")
                time.sleep(1)
                print("Harry realises he forgot his passport as well!")
                time.sleep(1)
                question3C = True
                while question3C:
                    print("What should he do now?!")
                    print("A. Test his luck and talk it over with the border control")
                    print("B. Sneak through the security and border control")
                    choice3C = input()
                    if choice3C == 'A':
                        question3C = False
                        print("No luck. Harry gets jailed for illegal immigration.")
                        time.sleep(1)
                        print("-- JAILED ENDING --")
                        tryagain = True
                        print("Would you like to try again?")
                        print("A. Yes")
                        print("B. No")
                        tryagainanswer = input()
                        if tryagainanswer == 'A':
                            tryagain = False
                            question1 = True
                        elif tryagainanswer == 'B':
                            tryagain = False
                            print("Closing game...")
                            time.sleep(1)
                        else:
                            invalid()
                            time.sleep(1)
                            tryagain = True
                    elif choice3C == 'B':
                        question3C = False
                        print("Harry successfully manages to sneak through the security.")
                        time.sleep(1)
                        print("...Or is he?")
                        time.sleep(1)
                        print("Oh no! The border control is after him!")
                        time.sleep(1)
                        question4B = True
                        while question4B:
                            print("Act quick!")
                            print("A. Give in to the security")
                            print("B. RUN FOR IT!")
                            choice4B = input()
                            if choice4B == 'A':
                                question4B = False
                                print("Giving in got Harry jailed for illegal immigration.")
                                time.sleep(1)
                                print("-- JAILED ENDING --")
                                tryagain = True
                                print("Would you like to try again?")
                                print("A. Yes")
                                print("B. No")
                                tryagainanswer = input()
                                if tryagainanswer == 'A':
                                    tryagain = False
                                    question1 = True
                                elif tryagainanswer == 'B':
                                    tryagain = False
                                    print("Closing game...")
                                    time.sleep(1)
                                else:
                                    invalid()
                                    time.sleep(1)
                                    tryagain = True
                            elif choice4B == 'B':
                                question4B = False
                                print("Harry then starts sprinting like he's being chased by a serial killer.")
                                time.sleep(1)
                                print("After a while, the border control gives up...")
                                time.sleep(1)
                                print("...At least for now.")
                                time.sleep(1)
                                print("Well, Harry better make the most of his time now.")
                                time.sleep(1)
                                print("He chooses to stay at a hotel for now.")
                                time.sleep(1)
                                print("However, while trying to get a room, the reception starts questioning him.")
                                time.sleep(1)
                                question5D = True
                                while question5D:
                                    print("What can Harry do to avoid being reported?")
                                    print("A. Bribe the reception to let him get a room still")
                                    print("B. Try searching somewhere else and go through the same process")
                                    print("C. Try searching somewhere else but break into the room")
                                    choice5D = input()
                                    if choice5D == 'A':
                                        question5D = False
                                        print("Harry then tries to offer double the room price so the reception doesn't expose him.")
                                        time.sleep(1)
                                        print("The reception, after a bit of thinking, decides to accept the offer.")
                                        time.sleep(1)
                                        print("And so, Harry gets to stay the night at the hotel safely.")
                                        time.sleep(1)
                                    elif choice5D == 'B':
                                        print("Harry decides to look through other hotels and attempt getting a room again.")
                                        print("Once again, he gets questioned by the reception.")
                                        question5D = True
                                    elif choice5D == 'C':
                                        question5D = False
                                        print("Harry decides to look through other hotels, but this time, he'll try breaking in.")
                                        time.sleep(1)
                                        print("It'll be quite hard, but he won't just sleep outside, right?")
                                        time.sleep(1)
                                        print("And so, he makes his way into an empty room without paying for it.")
                                        time.sleep(1)
                                        print("He's safe and sound for now until someone notices him.")
                                        time.sleep(1)
                                        print("Oh... Harry's getting a bit hungry.")
                                        time.sleep(1)
                                        print("He gets out to try and buy something, but then he encounters a hotel maid.")
                                        time.sleep(1)
                                        print("The maid is confused, because Harry isn't on the room owner list.")
                                        time.sleep(1)
                                        print("At least from the maid's memory anyway.")
                                        time.sleep(1)
                                        question6D = True
                                        while question6D:
                                            print("What will Harry do to avoid discourse with the maid and the hotel?")
                                            print("A. Lie and say he paid full service")
                                            print("B. Say he simply didn't pay maid service")
                                            choice6D = input()
                                            if choice6D == 'A':
                                                question6D = False
                                                print("Harry decides to try and lie about paying full service.")
                                                time.sleep(1)
                                                print("The maid squints her eyes at Harry, and goes to check the list again.")
                                                time.sleep(1)
                                                print("...Harry better get out ASAP!")
                                                time.sleep(1)
                                                print("He runs away while the maid is gone, and goes to a store in range.")
                                                time.sleep(1)
                                                print("The maid comes back to the hotel, and notices Harry is suddenly gone.")
                                                time.sleep(1)
                                                print("This can't be a good sign.")
                                                time.sleep(1)
                                                print("Either way, Harry got enough time to buy some sandwiches, snacks and drinks.")
                                                time.sleep(1)
                                                print("However, when he's back, he encounters the maid once again.")
                                                time.sleep(1)
                                                print("The maid warns Harry about how she will report him to the reception.")
                                                time.sleep(1)
                                                print("Quick, Harry needs to do something!")
                                                time.sleep(1)
                                                print("")
                                    else:
                                        invalid()
                                        time.sleep(1)
                            else:
                                invalid()
                                time.sleep(1)
                    else:
                        invalid()
                        time.sleep(1)
            else:
                invalid()
                time.sleep(1)

    elif choice1 == 'B':
        question1 = False
        print("Closing game...")
        time.sleep(1)
    else:
        invalid()
        time.sleep(1)