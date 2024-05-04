def wordremoverrepetition(user_input):
    with open(user_input, 'r+') as f:
        opening = f.read()
        words = opening.split()
        result = []
        
        for word in words:
            if word not in result:
                result.append(word)
        
        f.seek(0)
        f.truncate()
        f.write("**__".join(result))

user_input = str(input("Enter a file to revise and edit:::"))
wordremoverrepetition(user_input)