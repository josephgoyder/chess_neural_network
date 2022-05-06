function p = feedforward_prop(can_p, X, Theta)

load(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(Theta) ".mat"])

m = size(X, 1);

p = zeros(size(X, 1), 1);

X = [ones(m, 1) X];

a_2 = sigmoid(X * Theta1);

a_2 = [ones(size(a_2), 1) a_2];

a_3 = sigmoid(a_2 * Theta2);

a_3 = [ones(size(a_3), 1) a_3];

p = feedforward_prop_config_o_layer(p, Theta3, can_p, a_3);

[z p] = max(p, [], 2);   

end
