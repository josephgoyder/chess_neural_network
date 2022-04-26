clear ; close all; clc

X = [1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0];

Theta1 = rand(36,24) - 0.5;
Theta2 = rand(25, 76) - 0.5;

can_p = zeros(1,76);
for i = 1:76,
  can_p(i) = randi(2) - 1;
  end
can_p;

J = feedforward_prop(Theta1, Theta2, can_p, X)