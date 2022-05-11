clear ; close all; clc

X = zeros(1,97);
can_p = zeros(1,105);


for i = 1:105,
  can_p(i) = randi(2) - 1;
  end

for i = 1:97;
  X(i) = randi(2) - 1;
  end


for i = 1 : 100,
  i
  tic
  [J, T] = feedforward_prop(X, i)
  toc

end
