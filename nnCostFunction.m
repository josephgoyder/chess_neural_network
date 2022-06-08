function [J, grad] = nnCostFunction(nn_params, Theta, X, y, lambda, can_p)

  load(["/home/joseph/Desktop/chess_neural_network/backprop_data/neural_net_dataset_" num2str(Theta) ".mat"])
  
  options = optimset('MaxIter', 50);
  
  Theta1 = reshape(nn_params(1:(size(Theta1)(1) * size(Theta1)(2))), size(Theta1));
  Theta2 = reshape(nn_params(((size(Theta1)(1) * size(Theta1)(2)) + 1):(size(Theta1)(1) * size(Theta1)(2)) + (size(Theta2)(1) * size(Theta2)(2))), size(Theta2));
  Theta3 = reshape(nn_params(end - (size(Theta3)(1) * size(Theta3)(2)) + 1:end), size(Theta3));

  Theta1 = Theta1';
  Theta2 = Theta2';
  Theta3 = Theta3';

  J = 0;
  Theta1_grad = zeros(size(Theta1)); 
  Theta2_grad = zeros(size(Theta2));
  Theta3_grad = zeros(size(Theta3));
  
m = size(X, 1);

p = zeros(1, 850);

X = [ones(m, 1) X];

a_2 = sigmoid(X * Theta1');

a_2 = [ones(size(a_2), 1) a_2];

a_3 = sigmoid(a_2 * Theta2');

a_3 = [ones(size(a_3), 1) a_3];


h_x = feedforward_prop_config_o_layer(p, Theta3', can_p, a_3);

J = (1/m) * sum(sum((-y.*log(h_x))-((1-y).*log(1-h_x))));

  A1 = X;
  Z2 = A1 * Theta1'; 
  A2 = sigmoid(Z2); 
  A2 = [ones(size(A2,1),1), A2]; 
  
  Z3 = A2 * Theta2';  
  A3 = sigmoid(Z3); 
  A3 = [ones(size(A3,1),1), A3];
  
  Z4 = A3 * Theta3';
  A4 = sigmoid(Z4);

  DELTA4 = A4 - y;
  DELTA3 = (DELTA4 * Theta3) .* [ones(size(Z3,1),1) sigmoidGradient(Z3)];
  DELTA3 = DELTA3(:,2:end); 
  DELTA2 = (DELTA3 * Theta2) .* [ones(size(Z2,1),1) sigmoidGradient(Z2)]; 
  DELTA2 = DELTA2(:,2:end); 
  
  Theta1_grad = (1/m) * (DELTA2' * A1); 
  Theta2_grad = (1/m) * (DELTA3' * A2); 
  Theta3_grad = (1/m) * (DELTA4' * A3);
  
  reg_term = (lambda/(2*m)) * (sum(sum(Theta1(:,2:end).^2)) + sum(sum(Theta2(:,2:end).^2)) + sum(sum(Theta3(:,2:end).^2)));
  
  J = J + reg_term;
  
  Theta1_grad_reg_term = (lambda/m) * [zeros(size(Theta1, 1), 1) Theta1(:,2:end)]; 
  Theta2_grad_reg_term = (lambda/m) * [zeros(size(Theta2, 1), 1) Theta2(:,2:end)];
  Theta3_grad_reg_term = (lambda/m) * [zeros(size(Theta3, 1), 1) Theta3(:,2:end)];

  Theta1_grad = Theta1_grad + Theta1_grad_reg_term;
  Theta2_grad = Theta2_grad + Theta2_grad_reg_term;
  Theta3_grad = Theta3_grad + Theta3_grad_reg_term;
    
  grad = [Theta1_grad(:) ; Theta2_grad(:) ; Theta3_grad(:)];

end