function [n] = mutation(dataset, mutation_rate)

disp(["Mutating dataset ", num2str(dataset)])


load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(dataset) ".mat"])
% load(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(dataset) ".mat"])

new_theta_1 = reshape(Theta1, 1, []);
new_theta_2 = reshape(Theta2, 1, []);
new_theta_3 = reshape(Theta3, 1, []);

m1 = length(new_theta_1);
m2 = length(new_theta_2);
m3 = length(new_theta_3);

a1 = randi(m1, 1, floor(1/mutation_rate * m1));
a2 = randi(m2, 1, floor(1/mutation_rate * m2));
a3 = randi(m3, 1, floor(1/mutation_rate * m3));

for a = a1,
  epsilon_init = sqrt(6)/(sqrt(m1));
  new_theta_1(a) = - epsilon_init + rand(1) * 2 * epsilon_init ;
endfor  

for a = a2,
  epsilon_init = sqrt(6)/(sqrt(m2));
  new_theta_2(a) = - epsilon_init + rand(1) * 2 * epsilon_init ;
endfor  

for a = a3,
  epsilon_init = sqrt(6)/(sqrt(m3));
  new_theta_3(a) = - epsilon_init + rand(1) * 2 * epsilon_init ;
endfor  

Theta1 = reshape(new_theta_1, [size(Theta1)]);
Theta2 = reshape(new_theta_2, [size(Theta2)]);
Theta3 = reshape(new_theta_3, [size(Theta3)]);
tic
save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(dataset) ".mat"], "Theta1", "Theta2", "Theta3");
% save(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(dataset) ".mat"], "Theta1", "Theta2", "Theta3");
toc
n = 0;



end