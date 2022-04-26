function [new_theta1, new_theta2] = mutation(Theta1, Theta2, mutation_rate)

new_theta1 = Theta1;
new_theta2 = Theta2;

for i = 1 : size(Theta1, 1),
  for j = 1 : length(Theta1),
    a = randi(mutation_rate*2);
    if a == 1,
      new_theta1(i, j) = 1 - new_theta1(i, j);
    if a == 2,
      new_theta2(i, j) = 1 - new_theta2(i, j);
    endif
    endif
  endfor
end