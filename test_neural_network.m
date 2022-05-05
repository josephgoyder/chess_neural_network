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
  J = feedforward_prop(can_p, X, i)
  toc

end
