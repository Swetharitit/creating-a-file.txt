def PrintFriendsNames(friend1, friend2, friend3):
    # Create a list of friends in reverse order
    friends = [friend3, friend2, friend1]
    
    # Join the names with commas, adding "and" before the last name
    output = f"Hi {', '.join(friends[:-1])} and {friends[-1]}"
    
    # Print the output
    print(output)

# Example usage
PrintFriendsNames("Mahesh", "Suresh", "Devesh")
