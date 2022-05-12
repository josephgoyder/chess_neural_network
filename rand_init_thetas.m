function [] = rand_init_thetas(Theta1_size, Theta2_size, Theta3_size, n)

for i = 1 : n,
  Theta1 = rand(Theta1_size);
  Theta2 = rand(Theta2_size);
  Theta3 = rand(Theta3_size);
  
  save(["/Users/joseph_chiao/Desktop/Advance Research/Machine Learning/Chess engine/chess_neural_network/engine_data/neural_net_dataset_" num2str(i) ".mat"], "Theta1", "Theta2", "Theta3");

end
