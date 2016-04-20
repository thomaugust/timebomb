def main():
    import subprocess
    from time import sleep
    import random

    subprocess.call(["shutdown","-s", "-f", "-t", "60"])

    print "You have 60 seconds until your computer shuts down"
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
            exit()

    choice()

main()
