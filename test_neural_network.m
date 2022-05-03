clear ; close all; clc

X = zeros(1,96);
can_p = zeros(1,151);


for i = 1:151,
  can_p(i) = randi(2) - 1;
  end

for i = 1:96;
  X(i) = randi(2) - 1;
  end


for i = 1 : 100,
  i
  
  tic
  load(["/Users/joseph_chiao/Desktop/Advance Research/Machine Learning/Chess engine/chess_neural_network/engine_data/neural_net_dataset_" num2str(i) ".mat"])
  load_time = toc
  
  tic
  for i = 1:1,
  J = feedforward_prop(Theta1, Theta2, Theta3, can_p, X)
  end
  a = toc

end
