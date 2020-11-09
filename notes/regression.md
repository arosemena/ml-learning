# Regression 📈

Regression problems are the ones that can be calculated by
tinkering with parameters and plugging them into a function
that returns a scalar.

## Hypothesis
The hypothesis is a function that uses input data combined
with paraters to obtain a scalar result, this is the goal
of most regression problems.

The parameters have to be calibrated using a training set
with a learning algorithm.

Example hypothesis with 1 variable(x):

    hθ(x) = θ0 + θ1 * x
    
`θ0` and `θ1` are the parameters that need to be calibrated
with a learning algo.

## Cost function

A cost function is used to determine how optimal are the
parameters in relation to training data using the hypothesis.

The cost function is represented with `J(θ)`, an example 
for 2 parameters would be:

    J(θ0, θ1) = (1/2*m) * ∑((hθ(xi) - yi)^2)

Where `m` is the number of training data rows and `∑` goes 
from `i=1` to `i=m`

The parameters will be optimized when the cost function reaches 0 
or it's close to it.

## Parameter optimization methods
The following are methods to improve the parameters and find the
optimal configuration of them so the cost function approaches 0

### Gradient descent
An iterative approach to finding optimal parameters for regression.

    θj := θj - α * (∂ / ∂θj) J(θ0, θ1)
    
`α` is the learning rate.

`j` represents the index of the iterating parameter

`∂ / ∂θj J(θ0, θ1)` is  partial derivative of the cost function

For a 2 parameter problem the equations would be:

    θ0 := θ0 - α * (1/m) * ∑((hθ(xi) - yi)^2)
    θ1 := θ1 - α * (1/m) * ∑((hθ(xi) - yi)^2 * xi)
    
Running these 2 operations over and over will eventually converge
to close to 0, giving us parameter values that can be used with
the hypothesis.

If the learning rate is too large it make cause divergence, if it's
too low it may take a long time to converge, it's a good idea to try
different learning rates to get an optimal result.

### Normal Equation
The normal equation allows you to calculate optimal 
parameters values in a single operation:

    inv(X' * X) * X * y 
    
where `X` is the matrix of the parameters including (x0 = 1)
and `X'` is the transpose of X.

This method does not scale as it computes in n^3 time, for a large
amount of parameters use gradient descent.