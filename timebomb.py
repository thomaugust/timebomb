def main():
    import subprocess
    import sleep
    import random

    subprocess.call(["shutdown","-s", "-f", "-t", "60"])

    print "You have 60 seconds until your computer shuts down"
    sleep(1)
    print "Guess a number between zero and a hundred"
    randNo = random.randint(0,100)
    def choice():
        guess = raw_input('> ')
        if guess > randNo:
            "You guessed too high."
            choice()
        if guess < randNo:
            "You guessed too low."
            choice()
        if guess == randNo:
            subprocess.call(["shutdown", "-a"])
            print "Shutdown cancelled."
            sleep(1)
            exit()

main()
