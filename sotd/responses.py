def doResponse(message):
    message = str(message)
    message = message.lower()

    if message == "!setTime":
        tobeDesTime = str(input("Enter the desired time (24:00)"))
        tobeDesTime = tobeDesTime.strip()
        return tobeDesTime
    #note: get this into src n change it

    elif message == "!help":
        return("I post the most recent seal from r/seals, you can tell me when to post by inputting '!setTime' \
            then entering the time you would like me to post.")
    #make it ban anyone who says they hate seals?

    else:
        return("Sorry, that isn't a valid command, ask '!help' to see what I can do, or double-check your spelling")
