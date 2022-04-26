clear ; close all; clc

Theta1 = ones(25, 25);
Theta2 = zeros(25, 25);

new_theta1 = zeros(size(Theta1));
new_theta2 = zeros(size(Theta2));

mutated_theta1 = zeros(size(Theta1));
mutated_theta2 = zeros(size(Theta2));

[new_theta1, new_theta2] = reproduction(Theta1, Theta2);

[mutated_theta1, mutated_theta2] = mutation(new_theta1, new_theta2, 1000);

x = new_theta1 - mutated_theta1