function [n] = reproduction(dataset_1, dataset_2, new_dataset_1, new_dataset_2)

disp(["Reproducing between dataset ", num2str(dataset_1)," and dataset " num2str(dataset_2)])
tic

load(["/home/joseph/Desktop/chess_neural_network/parent_engine_data/neural_net_dataset_" num2str(dataset_1) ".mat"])
Theta1_1 = reshape(Theta1, 1, []);
Theta2_1 = reshape(Theta2, 1, []);
Theta3_1 = reshape(Theta3, 1, []);


load(["/home/joseph/Desktop/chess_neural_network/parent_engine_data/neural_net_dataset_" num2str(dataset_2) ".mat"])
Theta1_2 = reshape(Theta1, 1, []);
Theta2_2 = reshape(Theta2, 1, []);
Theta3_2 = reshape(Theta3, 1, []);

a = randi(2, 1, length(Theta1_1)) - 1;
for i = 1 : length(a),
  if a(i),
    Theta1_1(i) = Theta1_2(i);
    Theta1_2(i) = Theta1_1(i);
  endif
end
Theta1_1 = reshape(Theta1_1, [size(Theta1)]);
Theta1_2 = reshape(Theta1_2, [size(Theta1)]);

a = randi(2, 1, length(Theta2_1)) - 1;
for i = 1 : length(a),
  if a(i),
    Theta2_1(i) = Theta2_2(i);
    Theta2_2(i) = Theta2_1(i);
  endif
end
Theta2_1 = reshape(Theta2_1, [size(Theta2)]);
Theta2_2 = reshape(Theta2_2, [size(Theta2)]);

a = randi(2, 1, length(Theta3_1)) - 1;
for i = 1 : length(a),
  if a(i),
    Theta3_1(i) = Theta3_2(i);
    Theta3_2(i) = Theta3_1(i);
  endif
end
Theta3_1 = reshape(Theta3_1, [size(Theta3)]);
Theta3_2 = reshape(Theta3_2, [size(Theta3)]);

Theta1 = Theta1_1;
Theta2 = Theta2_1;
Theta3 = Theta3_1;
save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(new_dataset_1) ".mat"], "Theta1", "Theta2", "Theta3");

Theta1 = Theta1_2;
Theta2 = Theta2_2;
Theta3 = Theta3_2;
save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(new_dataset_2) ".mat"], "Theta1", "Theta2", "Theta3");
n = 0;

toc
end