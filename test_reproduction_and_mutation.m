clear ; close all; clc

load(["/Users/joseph_chiao/Desktop/Advance Research/Machine Learning/Chess engine/chess_neural_network/engine_data/neural_net_dataset_1.mat"])
Theta1_1 = Theta1;
Theta2_1 = Theta2;
Theta3_1 = Theta3;

load(["/Users/joseph_chiao/Desktop/Advance Research/Machine Learning/Chess engine/chess_neural_network/engine_data/neural_net_dataset_2.mat"])
Theta1_2 = Theta1;
Theta2_2 = Theta2;
Theta3_2 = Theta3;

tic

[Theta1_1, Theta1_2] = reproduction(Theta1_1, Theta1_2);
[Theta2_1, Theta2_2] = reproduction(Theta2_1, Theta2_2);
[Theta3_1, Theta3_2] = reproduction(Theta3_1, Theta3_2);

[Theta1_1] = mutation(Theta1_1, 100);
[Theta1_2] = mutation(Theta1_2, 100);
[Theta2_1] = mutation(Theta2_1, 100);
[Theta2_2] = mutation(Theta2_2, 100);
[Theta3_1] = mutation(Theta3_1, 100);
[Theta3_2] = mutation(Theta3_2, 100);

total_time = toc()
particular_time = total_time / 100
per_data_time = particular_time / 10000

%new_theta1
%new_theta2