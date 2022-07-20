function [p, time] = feedforward_prop(X, Theta1, Theta2, Theta3)

tic;

m = size(X, 1);

p = zeros(1, 850);

X = [ones(m, 1) X];

a_2 = sigmoid(X * Theta1);

a_2 = [ones(size(a_2), 1) a_2];

a_3 = sigmoid(a_2 * Theta2);

a_3 = [ones(size(a_3), 1) a_3];

p = sigmoid(a_3 * Theta3);

time = toc;

end