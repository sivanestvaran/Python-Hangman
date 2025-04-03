
from game import hangman



a = hangman.Hangman()
#Test completed
# print(a.lifes(0))
# print(a.lifes(1))
# print(a.lifes(2))
# print(a.lifes(3))
# print(a.lifes(4))
# print(a.lifes(5))
# print(a.lifes(6))

#Test on blanks print
# a.guessLetter('l')
# a.guessLetter('h')
# a.guessLetter('z')
# a.guessLetter('x')
# a.guessLetter('e')
# a.guessLetter('p')
# a.guessLetter('o')
# a.guessLetter('v')
# a.guessLetter('b')
# # a.guessLetter('m')

a.play()


print()
print("Correct Letter entered : ",a.correctLetters)
print("Mistake Letter entered : ",a.mistakeLetters)