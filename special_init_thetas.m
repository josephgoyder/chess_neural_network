function [a] = rand_init_thetas(Theta1_size, Theta2_size, Theta3_size, n)

for i = 1 : n,
  

  disp(["Creating dataset ", num2str(i)])
  tic
  
  x1 = rand(Theta1_size);
  x2 = rand(Theta2_size);
  x3 = rand(Theta3_size);

  Theta1 = log(x1 ./ (1 - x1));
  Theta2 = log(x2 ./ (1 - x2));
  Theta3 = log(x3 ./ (1 - x3));


  a = 1;

  save(["C:\\Users\\076-jchiao\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(i+0.1) ".mat"], "Theta1", "Theta2", "Theta3");
  toc

end