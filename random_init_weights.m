function [a] = random_init_weights(Theta1_size, Theta2_size, Theta3_size, n)

  """This function generate a neural network with randomized value"""


for i = 1 : n,
  

  disp(["Creating dataset ", num2str(i)])
  tic

  epsilon_init = sqrt(6)/(sqrt(Theta1_size(1))+sqrt(Theta1_size(2)));
  Theta1 = - epsilon_init + rand(Theta1_size) * 2 * epsilon_init ;
  epsilon_init = sqrt(6)/(sqrt(Theta2_size(1))+sqrt(Theta2_size(2)));
  Theta2 = - epsilon_init + rand(Theta2_size) * 2 * epsilon_init ;
  epsilon_init = sqrt(6)/(sqrt(Theta3_size(1))+sqrt(Theta3_size(2)));
  Theta3 = - epsilon_init + rand(Theta3_size) * 2 * epsilon_init ;

  a = 1;

  save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(i) ".mat"], "Theta1", "Theta2", "Theta3");
  toc

end