def letter_score(letter: str) -> int:
    points = ord(letter.lower()) - ord("a") + 1
    if letter.isupper():
        points *= 2
    
    return points

def word_score(word: str) -> int:
    score = 0
    
    for letter in word:
        score += letter_score(letter)
    return score

def battle(our_team: str, opponent:str) -> str:
    our_score = 0
    their_score = 0
    our_battle = our_team.split(" ")
    their_battle = opponent.split(" ")
    for our_word, their_word in zip(our_battle, their_battle):
        wordA = word_score(our_word)
        wordB = word_score(their_word)

        if wordA > wordB:
            our_score += 1
        elif wordB > wordA:
            their_score += 1

    if our_score > their_score:
        return "We win"
    elif their_score > our_score:
        return "We lose"
    else:
        return "Draw"

    

