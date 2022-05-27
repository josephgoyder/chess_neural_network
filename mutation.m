function [n] = mutation(dataset, mutation_rate)

disp(["Mutating dataset ", num2str(dataset)])


load(["C:\\Users\\076-jchiao\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(dataset) ".mat"])

new_theta_1 = reshape(Theta1, 1, []);
new_theta_2 = reshape(Theta2, 1, []);
new_theta_3 = reshape(Theta3, 1, []);

m1 = length(new_theta_1);
m2 = length(new_theta_2);
m3 = length(new_theta_3);

a1 = randi(mutation_rate * 50, 1, 50);
a2 = randi(mutation_rate * 50, 1, 50);
a3 = randi(mutation_rate * 50, 1, 50);


for i = 1:50,

  if a1(i) <= m1,
    x = rand;
    new_theta_1(a1(i)) = log(x / (1 - x));
  endif
  
  if a2(i) <= m2,
    x = rand;
    new_theta_2(a2(i)) = log(x / (1 - x));
  endif

  if a3(i) <= m3,
    x = rand;
    new_theta_3(a3(i)) = log(x / (1 - x));
  endif

end

Theta1 = reshape(new_theta_1, [size(Theta1)]);
Theta2 = reshape(new_theta_2, [size(Theta2)]);
Theta3 = reshape(new_theta_3, [size(Theta3)]);
tic
save(["C:\\Users\\076-jchiao\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(dataset) ".mat"], "Theta1", "Theta2", "Theta3");
toc
n = 0;



end