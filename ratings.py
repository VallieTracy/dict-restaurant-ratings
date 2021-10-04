"""Restaurant rating lister."""


# put your code here
def restaurant_dictionary(file_name):
    file_open = open(file_name)
    dictionary = {}

    
 
    for line in file_open:
        line= line.rstrip()
        line_list= line.split(":")

        key = line_list[0]
        value = line_list[1]
        
        dictionary[key] = value[0]

    if add_yes_or_no== "Y":
        dictionary[added_restaurant] = added_rating
   
    for parlour, rating in sorted(dictionary.items()):
        print(f"{parlour} is rated {rating}.")

#restaurant_dictionary("scores.txt")

def add_a_restaurant():
      added_restaurant= input("Enter a new restaurant: ")
        added_rating= int(input("Enter a new rating: ")) # move into while loop so user doesn't get stuck in loop and can't choose again
        while added_rating <1 or added_rating > 5:
            print("Must be an integer between 1 and 5")
            added_rating= int(input("Enter a new rating: "))


def user_choices():

    print("What would you like to do? Your choices are:")
    print("S - seeing all the ratings")
    print("A - add a new restaurant")
    print("Q - quit")
    

    while True:
        user_input = input("Please enter S, A or Q:")
            if user_input == "Q":
                break
            elif user_input == 'S':
                restaurant_dictionary('scores.txt')
            elif user_input== "A":
                add_a_restaurant()
                
            
user_choices()

