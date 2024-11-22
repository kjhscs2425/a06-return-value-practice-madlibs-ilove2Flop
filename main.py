
def play_madlibs():

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb ending in -ing: ")
    place = input("Enter a place: ")
    building = input("Enter a type of building: ")
    name1 = input("Enter a name of a person: ")
    verb2 = input("Enter a verb ending in -ing: ")
    noun2 = input("Enter a noun: ")
    madeupword = input("Enter a made up word: ")
    color = input("Enter a color: ")
    name2 = input("Enter a name of a person: ")

    story = f"It was a Monday afternoon {name2} was {verb} to his {building}. He looked around to make sure {name1} wasn't there but little did he know {name1} was right behind him. He turned around and shouted {madeupword} and all went {color}. When he woke up he was in a {noun} and he looked forward and saw {name1} holding a {noun2} and screamed."
    print(story)

if __name__ == "__main__":
    play_madlibs()