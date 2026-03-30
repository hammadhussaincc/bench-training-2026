## What does each weight represent?

Each weight represents the importance of the input, higher the weights means more the fluence of the input.
In neural networks we start with random weights of each input and as the model learns we keep on updating the
weights to what suits our model.

## What is bias?

Bias means extra push or adjustment. If the input is zero the the output of the model will become zero, e.g
predicting if it will rain or not if the humidity is zero (x=0), our model will predict 0% chances of rain but
it can still rain so we always add a bias factor e.g b=0.1 hence even if the input values like humidity, clouds
are zero there is still 10% chances of rain.

## What changes if you use ReLU vs sigmoid?

When we use ReLU network output changes. ReLU turns all the negative values into zero and keeps the positive values
unchaged, hence produces output from zero to very large positive numbers and allows stronger signals to pass hence
solving the vanishing gradient problem (caused by using sigmoid which squashes all inputs into smaller values which
makes the learning slower). ReLU is better to be used in hidden layers while sigmoid is better used on the ouput layer
to make the model predict in yes/no fashion.
