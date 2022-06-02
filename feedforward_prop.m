function [p, time] = feedforward_prop(can_p, X, Theta)

tic;
% load(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(Theta) ".mat"])
% load(["/Users/joseph_chiao/Desktop/Advance Research/Machine Learning/Chess engine/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])
load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])

m = size(X, 1);

p = zeros(1, 850);

X = [ones(m, 1) X];

a_2 = sigmoid(X * Theta1);

a_2 = [ones(size(a_2), 1) a_2];

a_3 = sigmoid(a_2 * Theta2);

a_3 = [ones(size(a_3), 1) a_3];

p = feedforward_prop_config_o_layer(p, Theta3, can_p, a_3);

n = 2;
maxes_i = zeros(1, n);
maxes = zeros(1, n);
for i = 1:length(p),
    for k = 1:n,
        if p(i) > maxes(k),
            maxes_i(k) = i;
            maxes(k) = p(i);
            break;
        endif
    endfor
end

size(p)

choice = randi(n);
p = maxes(choice);


time = toc;
end