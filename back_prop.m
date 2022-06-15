function[J] = back_prop(Theta, X, y, lambda)

  load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])
  options = optimset('MaxIter', 50);


  input_layer_size = size(Theta1)(1)
  Theta1 = Theta1';
  hidden_layer_size = size(Theta2)(1)
  Theta2 = Theta2';
  hidden_layer_2_size = size(Theta3)(1)
  output_layer_size = size(Theta3)(2) - 1
  Theta3 = Theta3';
  nn_params = [Theta1(:); Theta2(:); Theta3(:)]

  y = y';

  J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, hidden_layer_2_size, output_layer_size, X, y, lambda)

  costfunction = @(p)nnCostFunction(p, input_layer_size, hidden_layer_size, hidden_layer_2_size, output_layer_size, X, y, lambda);

  newTheta1 = randInitializeWeights(input_layer_size, hidden_layer_size)
  newTheta2 = randInitializeWeights(hidden_layer_size, hidden_layer_2_size)
  newTheta3 = randInitializeWeights(hidden_layer_2_size, output_layer_size)

  initial_nn_params = [newTheta1(:) ; newTheta2(:) ; newTheta3(:)];

  [nn_params, cost] = fmincg(costfunction, initial_nn_params, options);

  Theta1 = reshape(nn_params(1:(size(Theta1)(1) * size(Theta1)(2))), size(Theta1));
  Theta1 = Theta1';
  Theta2 = reshape(nn_params(((size(Theta1)(1) * size(Theta1)(2)) + 1):(size(Theta1)(1) * size(Theta1)(2)) + (size(Theta2)(1) * size(Theta2)(2))), size(Theta2));
  Theta2 = Theta2';
  Theta3 = reshape(nn_params(end - (size(Theta3)(1) * size(Theta3)(2)) + 1:end), size(Theta3));
  Theta3 = Theta3';

  save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"], "Theta1", "Theta2", "Theta3")
