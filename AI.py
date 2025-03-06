from matplotlib.widgets import Slider
import random
import matplotlib.pyplot as plt
import copy

    
        
def Activation(x):
    e=2.718281828459045
    return (e**x)/(1+e**x)
def calculate(input,bias,weight):
    
    for a in range(len(bias)):
        layer=bias[a]
        for b in range(len(bias[a])):
            
            for c in range(len(input)):
                layer[b]+=input[c]*weight[a][b][c]
            layer[b]=Activation(layer[b])
        


            
        input=layer.copy()
    
    return layer

class NeuralNet():
    def __init__(self,layers,input):
        #temp=[[1,5]]
        #weight=[[[3,4],[5,]]]
        self.bias=[[0 for b in range(a)] for a in layers]
        layers.insert(0,input)
        self.weights=[[[0 for c in range(layers[a-1])] for b in range(layers[a])] for a in range(1,len(layers))]
    def cost(self,data,expected):
        tot=[0,0]
        for a in range(len(data)):

            temp=calculate(data[a],copy.deepcopy(self.bias),copy.deepcopy(self.weights.copy()))
            for b in range(len(temp)):
                tot[0]+=abs(temp[b]-expected[a][b])            
                
            tot[1]+=1
        return tot[0]/tot[1]            
    
    def gradient(self,data,expected,rate):
        h=0.0001
        org=self.cost(data,expected)
        temp=[]
        for a in range(len(self.weights)):
            for b in range(len(self.weights[a])):
                for c in range(len(self.weights[a][b])):
                    self.weights[a][b][c]+=h
                    dcost=self.cost(data,expected)-org
                    self.weights[a][b][c]-=h
                    temp.append(dcost/h)
        for a in range(len(self.bias)):
            for b in range(len(self.bias[a])):
                self.bias[a][b]+=h
                dcost=self.cost(data,expected)-org
                self.bias[a][b]-=h
                temp.append(dcost)

        num=0
        #apply changes to weights and biases
        for a in range(len(self.weights)):
            for b in range(len(self.weights[a])):
                for c in range(len(self.weights[a][b])):
                    self.weights[a][b][c]-=temp[num]*rate
                    num+=1
        for a in range(len(self.bias)):
            for b in range(len(self.bias[a])):
                self.bias[a][b]-=temp[num]*rate
                num+=1
        return org


        # r=open('cache.txt','w')
        # lowest=1
        # bias,weights=0,0
        # for a in range(low,high):
        #     for b in range(low,high):
        #         for c in range(low,high):
        #             self.bias=[[a]]
        #             self.weights=[[[b,c]]]
        #             temp=self.cost(data,expected)
        #             if temp<lowest:
        #                 lowest=temp
        #                 bias=copy.deepcopy(self.bias)
        #                 weights=copy.deepcopy(self.weights)
        #                 print(lowest)
                        
        # return bias,weights

      
    
           
#calculate the error contributing per change in h for every node. thats dcost/h. then that *learnrate subtract that from the weight to move down the gradient descent. p-ick random data each time to ensure quick.