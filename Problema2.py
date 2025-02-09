def killer(suspect_info, dead):
    for suspect_info, seenpeople in suspect_info.items():
        if all(people in seenpeople for people in dead):
            return suspect_info
        pass
    suspect_info = {'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
    
    dead = ['Lucas', 'Bill']
    
    suspect = killer(suspect_info, dead)
    
    if suspect:
        print(f"The suspect is {suspect}")
    else: print(f"No suspect found.")
