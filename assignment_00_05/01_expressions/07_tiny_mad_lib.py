
def main():
    # Get the three inputs from the user to make the adlib
    game: str = input("Please type an any sports game name: ")
    verb: str = input("Please type a verb and press enter. ")

    SENTENCE_START: str = f"Today I am going to play {game} and I will {verb}"

    # Join the inputs together with the sentence starter
    print(SENTENCE_START)



if __name__ == '__main__':
    main()