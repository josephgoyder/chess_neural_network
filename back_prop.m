function [J, grad] = nnCostFunction(Theta, X, y, lambda)

  load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])
  
  options = optimset('MaxIter', 50);

  J = 0;
  Theta1_grad = zeros(size(Theta1)); 
  Theta2_grad = zeros(size(Theta2));
  Theta3_grad = zeros(size(Theta3));
  
m = size(X, 1);

p = zeros(1, 850);

X = [ones(m, 1) X];

a_2 = sigmoid(X * Theta1);

a_2 = [ones(size(a_2), 1) a_2];

a_3 = sigmoid(a_2 * Theta2);

a_3 = [ones(size(a_3), 1) a_3];

h_x = feedforward_prop_config_o_layer(p, Theta3, can_p, a_3);

J = (1/m) * sum(sum((-y.*log(h_x))-((1-y).*log(1-h_x))));


  %%%%%% WORKING: Backpropogation (Vectorized Implementation) %%%%%%%
  % Here X is including 1 column at begining
  A1 = X; % 5000 x 401
  
  Z2 = A1 * Theta1;  % m x hidden_layer_size == 5000 x 25
  A2 = sigmoid(Z2); % m x hidden_layer_size == 5000 x 25
  A2 = [ones(size(A2,1),1), A2]; % Adding 1 as first column in z = (Adding bias unit) % m x (hidden_layer_size + 1) == 5000 x 26
  
  Z3 = A2 * Theta2;  % m x num_labels == 5000 x 10
  A3 = sigmoid(Z3); % m x num_labels == 5000 x 10
  A3 = [ones(size(A3,1),1), A3];
  
  Z4 = A3 * Theta3;
  A4 = sigmoid(Z4)

  DELTA4 = A4 - y;
  DELTA3 = (DELTA4 * Theta3') .* [ones(size(Z3,1),1) sigmoidGradient(Z3)];
  DELTA3 = DELTA3(:,2:end); % 5000 x 25 %Removing delta2 for bias node
  DELTA2 = (DELTA3 * Theta2') .* [ones(size(Z2,1),1) sigmoidGradient(Z2)]; % 5000 x 26
  DELTA2 = DELTA2(:,2:end); % 5000 x 25 %Removing delta2 for bias node
  
  Theta1_grad = (1/m) * (DELTA2' * A1); % 25 x 401
  Theta2_grad = (1/m) * (DELTA3' * A2); % 10 x 26  
  Theta3_grad = (1/m) * (DELTA4' * A3);
  
  %%%%%%%%%%%% Part 3: Adding Regularisation term in J and Theta_grad %%%%%%%%%%%%%
  reg_term = (lambda/(2*m)) * (sum(sum(Theta1'(:,2:end).^2)) + sum(sum(Theta2'(:,2:end).^2)) + sum(sum(Theta3'(:,2:end).^2)));
  
  %Costfunction With regularization
  J = J + reg_term;
  
  %Calculating gradients for the regularization
  Theta1_grad_reg_term = (lambda/m) * [zeros(size(Theta1', 1), 1) Theta1'(:,2:end)]; % 25 x 401
  Theta2_grad_reg_term = (lambda/m) * [zeros(size(Theta2', 1), 1) Theta2'(:,2:end)]; % 10 x 26
  Theta3_grad_reg_term = (lambda/m) * [zeros(size(Theta3', 1), 1) Theta3'(:,2:end)]; % 10 x 26

  
  %Adding regularization term to earlier calculated Theta_grad
  Theta1_grad = Theta1_grad + Theta1_grad_reg_term;
  Theta2_grad = Theta2_grad + Theta2_grad_reg_term;
  Theta3_grad = Theta3_grad + Theta3_grad_reg_term;
    
  % =========================================================================
  
  % Unroll gradients
  grad = [Theta1_grad(:) ; Theta2_grad(:) ; Theta3_grad(:)];

  initial_nn_params = [Theta1(:) ; Theta2(:) ; Theta3(:)]

  costfunction = @(p)(J, grad)

  [nn_params, cost] = fmincg(costfunction, initial_nn_params, options)

  Theta1 = reshape(nn_params(1:(size(Theta1)(1) * size(Theta1)(2))), size(Theta1))
  Theta2 = reshape(nn_params(((size(Theta1)(1) * size(Theta1)(2)) + 1):(size(Theta1)(1) * size(Theta1)(2)) + (size(Theta2)(1) * size(Theta2)(2))), size(Theta2))
  Theta3 = reshape(nn_params(end - (size(Theta2)(1) * size(Theta2)(2)) + 1:end), size(Theta3))

  save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"], Theta1, Theta2, Theta3)

end