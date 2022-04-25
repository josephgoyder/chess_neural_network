function p = feedforward_prop(Theta1, Theta2, can_p, X)

m = size(X, 1);

p = zeros(size(X, 1), 1);

X = [ones(m, 1) X];

a_2 = sigmoid(X * Theta1);

a_2 = [ones(size(a_2), 1) a_2];

p = feedforward_prop_config_o_layer(p, Theta2, can_p, a_2);


[z p] = max(p, [], 2);   

end
