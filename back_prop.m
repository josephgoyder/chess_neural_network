function[J] = back_prop(Theta, X, y, lambda)

  load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])
  % load(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(Theta) ".mat"])

  % Set max backprop iteration to 50
  options = optimset('MaxIter', 50);

  % Configure Thetas into nn_params
  input_layer_size = size(Theta1)(1) - 1;
  Theta1 = Theta1';
  hidden_layer_size = size(Theta2)(1) - 1;
  Theta2 = Theta2';
  hidden_layer_2_size = size(Theta3)(1) - 1;
  output_layer_size = size(Theta3)(2);
  Theta3 = Theta3';
  nn_params = [Theta1(:); Theta2(:); Theta3(:)];

  y = y';

  % Compute cost function for evaluation
  J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, hidden_layer_2_size, output_layer_size, X, y, lambda)

  %Create short hand for NN_params in the cost function
  costfunction = @(p)nnCostFunction(p, input_layer_size, hidden_layer_size, hidden_layer_2_size, output_layer_size, X, y, lambda);

  % backprop
  [nn_params, cost] = fmincg(costfunction, nn_params, options);

  % reshaping Thetas
  Theta1 = reshape(nn_params(1:(size(Theta1)(1) * size(Theta1)(2))), size(Theta1));
  Theta1 = Theta1';
  Theta2 = reshape(nn_params(((size(Theta1)(1) * size(Theta1)(2)) + 1):(size(Theta1)(1) * size(Theta1)(2)) + (size(Theta2)(1) * size(Theta2)(2))), size(Theta2));
  Theta2 = Theta2';
  Theta3 = reshape(nn_params(end - (size(Theta3)(1) * size(Theta3)(2)) + 1:end), size(Theta3));
  Theta3 = Theta3';

  % save to file
  save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"], "Theta1", "Theta2", "Theta3")
  % save(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(Theta) ".mat"], "Theta1", "Theta2", "Theta3")
