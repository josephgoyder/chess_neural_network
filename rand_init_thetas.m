function [a] = rand_init_thetas(Theta1_size, Theta2_size, Theta3_size, n)

for i = 1 : n,
  

  disp(["Creating dataset ", num2str(i)])
  tic
  
  x1 = rand(Theta1_size);
  x2 = rand(Theta1_size);
  x3 = rand(Theta1_size);

  Theta1 = log(x1 / (1 - x1));
  Theta2 = log(x2 / (1 - x2));
  Theta3 = log(x3 / (1 - x3));
  a = 1;

  save(["A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(i) ".mat"], "Theta1", "Theta2", "Theta3");
  toc

end