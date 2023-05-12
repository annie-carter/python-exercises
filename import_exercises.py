#from my function exercise
def is_vowel(letter):
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print('This is a vowel')
    else:
        print('This is a not a vowel')

# from function exerc    
def calculate_tip(bill, tip_perc):
    return bill / tip_perc
    

def get_letter_grade(score):
    if type(score) == int or type(score) == float:
        if(score < 60):
            return "F"
        elif(score < 70):
            return "D"
        elif(score < 80):
            return "C"
        elif(score < 90):
            return "B"
        elif(score <101):
            return "A"
    