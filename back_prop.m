function[J] = back_prop(Theta, X, y, lambda)

  load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])
  options = optimset('MaxIter', 50);

  Theta1 = Theta1';
  Theta2 = Theta2';
  Theta3 = Theta3';
  nn_params = (Theta1(:); Theta2(:); Theta3(:))

  X = X';
  y = y';

  costfunction = @(p)nnCostFunction(p, Theta, X, y, lambda);

  initial_nn_params = [Theta1(:) ; Theta2(:) ; Theta3(:)];

  [nn_params, cost] = fmincg(costfunction, initial_nn_params, options);

  Theta1 = reshape(nn_params(1:(size(Theta1)(1) * size(Theta1)(2))), size(Theta1));
  Theta1 = Theta1';
  Theta2 = reshape(nn_params(((size(Theta1)(1) * size(Theta1)(2)) + 1):(size(Theta1)(1) * size(Theta1)(2)) + (size(Theta2)(1) * size(Theta2)(2))), size(Theta2));
  Theta2 = Theta2';
  Theta3 = reshape(nn_params(end - (size(Theta3)(1) * size(Theta3)(2)) + 1:end), size(Theta3));
  Theta3 = Theta3';

  save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"], "Theta1", "Theta2", "Theta3")
