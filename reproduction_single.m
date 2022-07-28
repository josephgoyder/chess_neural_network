function [n] = reproduction_single(dataset_1, dataset_2, new_dataset)

  tic
disp(["Reproducing between dataset ", num2str(dataset_1)," and dataset " num2str(dataset_2)])

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
  endif
end
Theta1 = reshape(Theta1_1, [size(Theta1)]);

a = randi(2, 1, length(Theta2_1)) - 1;
for i = 1 : length(a),
  if a(i),
    Theta2_1(i) = Theta2_2(i);
  endif
end
Theta2 = reshape(Theta2_1, [size(Theta2)]);

a = randi(2, 1, length(Theta3_1)) - 1;
for i = 1 : length(a),
  if a(i),
    Theta3_1(i) = Theta3_2(i);
  endif
end
Theta3 = reshape(Theta3_1, [size(Theta3)]);

save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(new_dataset) ".mat"], "Theta1", "Theta2", "Theta3");

n = 0;
toc

end

