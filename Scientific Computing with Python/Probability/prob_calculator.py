# import random library for random.choice method and copy for copy.deepcopy
import random
import copy


# Create the class called Hat
class Hat:
    
    
    # When initialized takes variable number of arguments and creates a list of them
    def __init__(self, **hats):
        self.contents = []
        for hat in hats:
            for i in range(hats[hat]):
                self.contents.append(hat)

    # When called the draw function return a number of random selection from the list removing them once chosen. If larger than list then the list is emptied and the wwhole thing returned    
    def draw(self, number):
        picked = []
        if number >= len(self.contents):
            draw = copy.copy(self.contents)
            self.contents.clear()
            return draw
        else:
           for i in range(number):
                pick = random.choice(self.contents)
                self.contents.remove(pick)
                picked.append(pick)
           return picked
             
# When called experiment will run a number of iterations simulating taking balls out of the hat and returns the probability of an input expected result
def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
    
    m = 0
    
    # Create a deepcopy of the hat object so it is not directing to the original object list    
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        result = temp_hat.draw(num_balls_drawn)
        drawn = {}
        
        # Creates a dictionary of the balls drawn color: number
        drawn ={ball :result.count(ball) for ball in expected_balls}
        
        # Compares the drawn dictionary with the expected ball dictionary and returns a list of matches found (number can be equal or more than)    
        matches = {k :expected_balls[k] for k in expected_balls if k in drawn and expected_balls[k] <= drawn[k]}
        
        #Check if the matches list = the expected list. This will only be the case if all the expected ball or more are found
        if len(matches) == len(expected_balls):
            m += 1
              
    probability = float(m / num_experiments)     
    
    return probability
    
# Test Case 
hat = Hat(blue=3,red=2,green=6)

probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)


# Test Response Expected = 0.272 with margin for random selection
print(probability)