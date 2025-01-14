"""
#501(prac7)---29/08/19---
#AIM: Implement feed forward back propagation neural network learning algorithm.
"""


#please download and install numpy first 

import numpy as np

class NeuralNetwork():
    def __init__(self):
        #seeding for random number generation
        np.random.seed()

        #converting weights to a 3 by 1 matrix
        self.synaptic_weights=2*np.random.random((3,1))-1

    #x is output variable
    def sigmoid(self, x):
        #applying the sigmoid function
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        #computing derivative to the sigmoid function
        return x*(1-x)

    def train(self,training_inputs,training_outputs,training_iterations):

        #training the model to make accurate predictions while adjusting
        for iteration in range(training_iterations):
            #siphon the training data via the neuron
            output=self.think(training_inputs)

            error=training_outputs-output

            #performing weight adjustments
            adjustments=np.dot(training_inputs.T,error*self.sigmoid_derivative(output))

            self.synaptic_weights+=adjustments

    def think(self,inputs):
        #passing the inputs via the neuron to get output
        #converting values to floats

        inputs=inputs.astype(float)
        output=self.sigmoid(np.dot(inputs,self.synaptic_weights))

        return output

if __name__=="__main__":

    #initializing the neuron class
    neural_network=NeuralNetwork()

    print("Beginning randomly generated weights: ")
    print(neural_network.synaptic_weights)

    #training data consisting of 4 examples--3 inputs & 1 output
    training_inputs=np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_outputs=np.array([[0,1,1,0]]).T

    #training taking place
    neural_network.train(training_inputs,training_outputs,15000)

    print("Ending weights after training: ")
    print(neural_network.synaptic_weights)

    user_input_one=str(input("User Input One: "))
    user_input_two=str(input("User Input Two: "))
    user_input_three=str(input("User Input Three: "))

    print("Considering new situation: ",user_input_one,user_input_two,user_input_three)
    print("New output data: ")
    print(neural_network.think(np.array([user_input_one,user_input_two,user_input_three])))

"""
OUTPUT:

Beginning randomly generated weights: 
[[-0.89078318]
 [-0.34733271]
 [-0.49265857]]
Ending weights after training: 
[[10.08710295]
 [-0.20735667]
 [-4.83718482]]
User Input One: 6
User Input Two: 8
User Input Three: 12
Considering new situation:  6 8 12
New output data: 
[0.69371529]
"""
