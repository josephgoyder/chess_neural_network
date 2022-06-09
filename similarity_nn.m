function [similarity_total] = similarity(dataset_1, dataset_2)

load(["/home/joseph/Desktop/chess_neural_network/backprop_data/neural_net_dataset_" num2str(dataset_1) ".mat"])
Theta1_1 = Theta1;
Theta1_2 = Theta2;
Theta1_3 = Theta3;

load(["/home/joseph/Desktop/chess_neural_network/backprop_data/neural_net_dataset_" num2str(dataset_2) ".mat"])
Theta2_1 = Theta1;
Theta2_2 = Theta2;
Theta2_3 = Theta3;

similarity_total = 0;

similarity = Theta1_1 - Theta2_1;
similarity = abs(similarity);
similarity_total += sum(sum(similarity));

similarity = Theta1_2 - Theta2_2;
similarity = abs(similarity);
similarity_total += sum(sum(similarity));

similarity = Theta1_3 - Theta2_3;
similarity = abs(similarity);
similarity_total += sum(sum(similarity));