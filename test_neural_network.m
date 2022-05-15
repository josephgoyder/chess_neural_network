clear ; close all; clc

X = zeros(1,97);
can_p = zeros(1,850);


for i = 1:105,
  can_p(i) = randi(2) - 1;
  end

##for i = 1:97;
##  X(i) = randi(2) - 1;
##  end


for i = 1 : 8,
  i

  [J, T] = feedforward_prop(can_p, X, i)


end
