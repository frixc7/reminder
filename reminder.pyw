import time
import winsound as ws
import sched
import pyttsx3

def say_sentence(sentence : str):
    """Gets the pyttsx3 module to say a sentence

    Args:
        sentence (str): the sentence to be said
    """
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()
    
def posture_reminder():
    """Reminder for fixing posture."""
    
    say_sentence("Remember to fix your posture.")

    scheduler.enter(delay = 900, priority = 3, action = posture_reminder) # calls for another reminder after delay
    
def break_reminder():
    """Reminder for taking a physical break."""
    
    for _ in range(3):
        say_sentence("It's time to take a physical break.")
        for _ in range(3):
            ws.Beep(4000, 500)
    
    scheduler.enter(delay = 3600, priority = 2, action = break_reminder) # calls for another reminder after delay
    
def sight_reminder():
    """Reminder to give your eyes a break from screentime."""
    
    for _ in range(55): # a lot of loops to bother you so that you get up from your desk
        say_sentence("It's time to give your eyes a break.")
        for _ in range(5):
            ws.Beep(5000, 250)
    
    scheduler.enter(delay = 7200, priority = 1, action = sight_reminder) # calls for another reminder after delay

scheduler = sched.scheduler(time.time, time.sleep)

"""Initial reminders"""
scheduler.enter(delay = 900, priority = 3, action = posture_reminder) 
scheduler.enter(delay = 3600, priority = 2, action = break_reminder)
scheduler.enter(delay = 7200, priority = 1, action = sight_reminder)

scheduler.run()
