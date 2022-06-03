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

maxes_i = zeros(1, 2);
maxes = zeros(1, 2);
for i = 1:length(p),
    for k = 1:2,
        if p(i) > maxes(k),
            maxes_i(k) = i;
            maxes(k) = p(i);
            break;
        endif
    endfor
end

choice_ratio = maxes(2) / (maxes(1) + maxes(2));
choice = rand;

if choice > choice_ratio,
    p = maxes_i(1);
endif

if choice < choice_ratio,
    p = maxes_i(2);
endif

time = toc;
end