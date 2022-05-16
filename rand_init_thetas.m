function [a] = rand_init_thetas(Theta1_size, Theta2_size, Theta3_size, n)

for i = 1 : n,
  
  tic
  
  i

  Theta1 = rand(Theta1_size)/Theta1_size(2);
  Theta2 = rand(Theta2_size)/Theta2_size(2);
  Theta3 = rand(Theta3_size)/Theta3_size(2);
  a = 1;
  save(["A:\\BLK2-MULZET-AD12\\076-JCHIAO\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(i) ".mat"], "Theta1", "Theta2", "Theta3");
  toc

end
