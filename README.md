In this coding project, I utilized gradient descent to train a neural network to identity the simple relationships on a graph.
This is a simple visualization to help understand how a more complex AI model would function.
An AI can be thought of as a pattern recognition software.
For example if we want to make an AI recognize a balloon, there could be two axis. Shininess, and roundness. Then if we graph out all of our data points we might see a clear correlation.
What the AI does is use a neural network to find the relationships betweens the characteristics of these objects - Balloons are often shiny and round. So we could draw a line at y=x^2. 

But a balloon could be heart-shaped, or could be rough. So we need thousands of these dimensions to properly classify a balloon image.

For this visualization I just focused on two-axis.

![Screenshot 2025-03-10 213052](https://github.com/user-attachments/assets/6f5a6241-ef24-4d83-b789-16fa04edcf2f)

I have a very simple neural network. It has 2 input layers, they are x and y (the coordinates of a point); 1 hidden layer with two nodes. And one node at the end that serves as an output (The probabaility the point is a balloon or not)
![image](https://github.com/user-attachments/assets/564285eb-06e7-4953-962f-2ddee4307f4a)

Each node has weights and biases which alter the input values, and output the probability that the point would correctly classify as 0 or 1 (balloon or not). However, how do we make sure that the output is 0 or 1. We need to at an activation function.
The activation function is similar to a neuron in your brain, it takes some input for it to fire. We can do the same thing for each node. We need the activation function to ensure non-linearity. Nothing in the real world is ever that simple.
I use a sigmoid function to ease the activation in. The reason we need this easing is so that small changes in the neural network won't result in immiediate big changes for the output (this is important for training the network).

If we just plug in random weights and biases, then the network will output random values, that have little correlation. So we need to find a way to determine a network's effectiveness. You can use a cost function.
For example if we plug in the point (5,5) we might get 0.3, while in reality the expected solution is 0 (the point is not a balloon). So the cost for that data point is 0.3. A cost function runs the network through every single point in the training data, and averages the cost.
Now we need to minimize the cost.

For training the neural network I used gradient descent. Basically we can think of our network as a cost landscape. We can simplify things down a lot. Lets just say there is one node with one weight and one bias. Then the x axis is the weight and the y axis is the bias. The z axis is the cost those weights and bias combinations yield. We need to get the combination that yields the lowest cost. So we need to descend down this mountain. We can start off at a random starting point.
We then use calculus (too complicated to explain in this short document. I may make a video about it in the future) to find the x and y slope at that point. We can then go in the direction of the slope, simulating an object falling from the slope. The object will then gradually find its way down (I'm oversimplifiying).
![image](https://github.com/user-attachments/assets/ad37e589-4d5d-45ca-87c1-697c03110dca)

Obviously there are thousands of dimensions, billions for some AI. This is the power of using machines. It may be easy for a human to point out the lowest point on a 2d graph or a 3d graph, we are good at those dimensions. But 100d or 10000d, that is impossible.
Through this method I was able to succesfully train an AI to classify a set of points.
Training Data: All points above y=x^2 are balloons. All below are not


![Screenshot 2025-03-10 213052](https://github.com/user-attachments/assets/6f5a6241-ef24-4d83-b789-16fa04edcf2f)
