user_name = input("your name: ")
user = ""
end = "bye"
def addition(add):
    switcher = {

    }
    return switcher.get(add)
def repsonse_bombe(rep):
    switcher = {
        "i'm fine": "That's great.",
    }
    return switcher.get(rep)
def con_bombe(con):
    switcher = {
        "hi": "Hii " + user_name + ", how are you?",
        "how are you?": "I'm fine, thank you.",
        "are you male?": "Well technically i'm a programme so i don't have any specific gender, but according to my name I'm a male.",
        "hmm": "Ok, so how can i help you?",

    }
    return switcher.get(con)
def day_greeting(greetings):
    switcher = {
        #MORNING.
        "good morning": "Good Morning",
        "hi, good morning": "Hi, Good morning.",
        "hi, good morning bombe": "Hi, Good morning " + user_name + ".",
        #AFTERNOON.
        "good afternoon": "Good Afternoon.",
        "hi, good afternoon": "hi " + user_name + ", Good Afternoon.",
        "hi, good afternoon bombe": "Hi " + user_name + ", Good Afternoon.",
        #EVENING.
        "good evening": "Good evening.",
        "hi, good evening": "hi " + user_name + ", Good Evening.",
        "hi, good evening bombe": "Hi " + user_name + ", Good Evening.",
        #NIGHT.
        "good night": "Good Night",
        "good night bombe": "Hi " + user_name + ", Good Night.",
        #NORMAL GREETINGS.
        "have a good day": "Thank you " + user_name + ", you too have a good day.",
        #END.
        "bye": "ok, bye see you soon."
    }
    return switcher.get(greetings, "on it.")
while user != end:
    user = input("You: ")
    user = user.lower()
    if user == "good morning" or user == "hi, good morning" or user == "hi, good morning bombe":
               # ALL THE ELEMENTS FOR GOOD MORNING COME IN THIS STATEMENT.
        greetings = user
        print("Bombe: ",day_greeting(greetings))
    elif user == "good afternoon" or user == "hi, good afternoon" or user == "hi, good afternoon bombe":
            # ALL THE ELEMENTS FOR GOOD AFTERNOON COME IN THIS STATEMENT.
        greetings = user
        print("Bombe: ", day_greeting(greetings))
    elif user == "good evening" or user == "hi, good evening" or user == "hi, good evening bombe":
            # ALL THE ELEMENTS FOR GOOD EVENING COME IN THIS STATEMENT.
        greetings = user
        print("Bombe: ", day_greeting(greetings))
    elif user == "good night" or user == "good night bombe":
            #ALL THE ELEMENTS FOR GOOD NIGHT COME IN THIS STATEMENT.
        greetings = user
        print("Bombe: ", day_greeting(greetings))
    elif user == "bye":
            # THE END STATEMENT WHICH STOPS THE PROGRAMME.
        greetings = user
        print("Bombe: ", day_greeting(greetings))
    elif user == "have a good day":
        greetings = user
        print("Bombe: ", day_greeting(greetings))
    elif user == "i'm fine":
        rep = user
        print("Bombe: ", repsonse_bombe(rep))
    elif user == "hmm":
        con = user
        print("Bombe: ", con_bombe(con))
    elif user == "hi" or "how are you?":
        con = user
        print("Bombe: ", con_bombe(con))
