def main():
    import subprocess
    from time import sleep
    import random

    subprocess.call(["shutdown","-s", "-f", "-t", "30"])
    print "You have 30 seconds for each question."

    def q1():
        print "Question 1"
        sleep(0.5)
        print "Guess a number between zero and a hundred"
        randNo = random.randint(0,100)
        def choice():
            guess = input('> ')
            if guess > randNo:
                print "You guessed too high."
                sleep(0.5)
                choice()
            if guess < randNo:
                print "You guessed too low."
                sleep(0.5)
                choice()
            if guess == randNo:
                subprocess.call(["shutdown", "-a"])
                print "Shutdown cancelled."
                sleep(1)
                q2()

        choice()

    def q2():
        print 'Question 2'
        subprocess.call(["shutdown","-s", "-f", "-t", "30"])
        a = random.randint(0,100)
        b = random.randint(0,100)
        print '%i + %i is equal to?' % (a,b)
        def choice():
            guess = input('> ')
            if guess == a+b:
                print 'Correct!'
                subprocess.call(["shutdown", "-a"])
                sleep(1)
                q3()
            else:
                print 'Wrong!'
                choice()
        choice()

    def q3():
        print 'Question 3'
        subprocess.call(["shutdown","-s", "-f", "-t", "30"])
        print 'What is the scientific notation for a nanometer?'
        sleep(1)
        print 'A: 10e-9'
        print 'B: 10e9'
        print 'C: 10e-15'
        print 'D: 10e-12'
        def choice():
            guess = raw_input('> ')
            if guess == 'A' or 'a':
                print 'Correct!'
                subprocess.call(["shutdown", "-a"])
                sleep(1)
                q4()
            else:
                print 'Wrong!'
                choice()
        choice()

    def q4():
        print 'Final Question!'
        subprocess.call(["shutdown","-s", "-f", "-t", "30"])
        print 'You have one chance to get this right, or else.'
        print 'To the nearest ten, how many lines of code is this program?'
        def choice():
            guess = input('> ')
            if guess == 90:
                print 'Correct!'
                subprocess.call(["shutdown", "-a"])
                sleep(1)
                exit()
            else:
                print 'Wrong!'
                subprocess.call(["shutdown", "-a"])
                sleep(3)
                subprocess.call(["shutdown", "-s", "-f", "-t", "0"])
                exit()
        choice()

    q1()

main()
