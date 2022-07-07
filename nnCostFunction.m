function [J, grad] = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, hidden_layer_2_size, output_layer_size, X, y, lambda)
    
  % Reshape all Thetas into one nn_params
  Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), hidden_layer_size, (input_layer_size + 1));
  Theta2 = reshape(nn_params((hidden_layer_size * (input_layer_size + 1) + 1 ): (hidden_layer_2_size * (hidden_layer_size + 1)) + (hidden_layer_size * (input_layer_size + 1))), hidden_layer_2_size, (hidden_layer_size + 1));
  Theta3 = reshape(nn_params(length(nn_params) - ((hidden_layer_2_size + 1) * output_layer_size) + 1:end), output_layer_size, (hidden_layer_2_size + 1));

  % Create gradients
  J = 0;
  Theta1_grad = zeros(size(Theta1)); 
  Theta2_grad = zeros(size(Theta2));
  Theta3_grad = zeros(size(Theta3));
  
  % Feedprop 
  m = size(X, 1);
  p = zeros(1, 850);
  X = [ones(m, 1) X];
  a_2 = sigmoid(X * Theta1');
  a_2 = [ones(size(a_2), 1) a_2];
  a_3 = sigmoid(a_2 * Theta2');
  a_3 = [ones(size(a_3), 1) a_3];
  h_x = sigmoid(a_3 * Theta3');

  % Compute cost
  J = (1/m) * sum(sum((-y.*log(h_x))-((1-y).*log(1-h_x))))

  % Compute gradient
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
  
  % Regularize cost
  reg_term = (lambda/(2*m)) * (sum(sum(Theta1(:,2:end).^2)) + sum(sum(Theta2(:,2:end).^2)) + sum(sum(Theta3(:,2:end).^2)));
  J = J + reg_term;
  
  % Regularize grad
  Theta1_grad_reg_term = (lambda/m) * [zeros(size(Theta1, 1), 1) Theta1(:,2:end)]; 
  Theta2_grad_reg_term = (lambda/m) * [zeros(size(Theta2, 1), 1) Theta2(:,2:end)];
  Theta3_grad_reg_term = (lambda/m) * [zeros(size(Theta3, 1), 1) Theta3(:,2:end)];
  Theta1_grad = Theta1_grad + Theta1_grad_reg_term;
  Theta2_grad = Theta2_grad + Theta2_grad_reg_term;
  Theta3_grad = Theta3_grad + Theta3_grad_reg_term;
  
  % Reshape grad
  grad = [Theta1_grad(:) ; Theta2_grad(:) ; Theta3_grad(:)];

end