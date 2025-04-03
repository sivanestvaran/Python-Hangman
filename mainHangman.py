from game import hangman
a = hangman.Hangman()
a.play()

print()
print("Correct Letter entered : ",a.correctLetters)
print("Mistake Letter entered : ",a.mistakeLetters)

del a