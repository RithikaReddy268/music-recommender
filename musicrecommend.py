x= input('''How are you feeling right now? Happy, sad, lonely, relaxed, stressed, excited, or bored?
I'll suggest a song based on your mood to help you feel even better.
''').lower()
if x=="happy":
    print("Listen to 'Happy' by Pharrell Williams.It perfectly matches your vibe.")
elif x=="sad":
    print("Listen to 'Let Her Go' by Passenger.you can feel better.")
elif x == "lonely":
    print("listen to 'Someone Like You' by Adele.You can feel better.")
elif x == "stressed":
    print("listen to 'Weightless' by Marconi Union.You can feel better.")
elif x == "relaxed":
    print("listen to 'Banana Pancakes' by Jack Johnson.You will enjoy it.")
elif x == "excited":
    print("listen to 'Can't Stop the Feeling!' by Justin Timberlake.You will like it.")
elif x == "bored":
    print("listen to 'Uptown Funk' by Mark Ronson ft. Bruno Mars.You can feel better.")
else:
    print("Sorry.I could'nt understand it.Try Again.")
