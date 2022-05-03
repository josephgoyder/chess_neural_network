clear ; close all; clc

Theta1 = ones(100, 100);
Theta2 = zeros(100, 100);

new_theta1 = ones(size(Theta1));
new_theta2 = zeros(size(Theta2));

mutated_theta1 = zeros(size(Theta1));
mutated_theta2 = zeros(size(Theta2));


tic()
for i = 1 : 100,
  [new_theta1, new_theta2] = reproduction(new_theta1, new_theta2);
  [new_theta1] = mutation(new_theta1, 1000);
  [new_theta2] = mutation(new_theta2, 1000);
end
%end
total_time = toc()
particular_time = total_time / 100
per_data_time = particular_time / 10000

%new_theta1
%new_theta2