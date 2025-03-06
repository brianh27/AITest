
from AI import calculate,Activation,NeuralNet
import random
import matplotlib.pyplot as plt
import random




net=NeuralNet([1],2)

temp=[[random.random(),random.random()] for a in range(100)]
expected = [[0] if a[0]**2>a[1] else [1] for a in temp]

r=open('cache.txt','w')

cost=10
while cost>0.15:
    
    #combined = list(zip(temp, expected))
    #random.shuffle(combined)
    #temp, expected = zip(*combined)

    # Convert tuples back to lists
    
    
    
    cost=net.gradient(list(temp),list(expected),0.5)
    if cost<0.15:
        break
    print(cost)
    


net.bias=[[-7.273917210475178e-05, -7.27391721044916e-05], [-0.013895720714652112]]
net.weights=[[[-8.430919273031341, 7.211499486752432], [-8.430919273034629, 7.211499486759013]],[[5.586783754385817, 5.586783754392655]]] 
bias,weights=net.bias,net.weights

print(net.cost(temp,expected))
print(net.bias,net.weights)
fig, ax = plt.subplots()
training=[]
for a in range(20):
    for b in range(20):
        training.append([a/20,b/20,'gray'])

temp=[[random.random(),random.random()] for a in range(100)]
testdata=[]
for a in range(len(testdata)):
    if temp[a][0]>0.5:
        testdata.append([temp[a][0],temp[a][1],'red'])
    else:
        testdata.append([temp[a][0],temp[a][1],'blue'])
testdata=training+testdata
# Plot the initial points
scatter = ax.scatter(
    [x for x, y, color in testdata],  # x-coordinates
    [y for x, y, color in testdata],  # y-coordinates
    c=[color for x, y, color in testdata],  # colors
    s=50
)



# Function to update the points live
def update_points():
    while True:
        

        for a in range(20):
            for b in range(20):
                temp=calculate([testdata[a*20+b][0],testdata[a*20+b][1]],bias,weights)
                if temp[0]>0.5:
                    testdata[a*20+b][2]='gray'
                else:
                    testdata[a*20+b][2]='black'
        
        # Update the scatter plot data
        scatter.set_offsets(([[x, y] for x, y, color in testdata]))  # Update positions
        scatter.set_color([color for x, y, color in testdata])  # Update colors
        
        # Refresh the plot
        fig.canvas.draw_idle()
        
        # Pause for 1 second before the next update
        plt.pause(0.1)

# Start live updates
plt.show(block=False)  # Show the plot without blocking
update_points()