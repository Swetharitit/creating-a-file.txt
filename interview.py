def PrintFriendsNames(friend1, friend2, friend3):
    
    friends = [friend3, friend2, friend1]
    
    
    output = f"Hi {', '.join(friends[:-1])} and {friends[-1]}"
    
    
    print(output)


PrintFriendsNames("Mahesh", "Suresh", "Devesh")
