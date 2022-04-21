function p = predict(Theta1, Theta2, can_p, X)

m = size(X, 1);

p = zeros(size(X, 1), 1);

X = [ones(m, 1) X];


a_2 = sigmoid(X * Theta1');

a_2 = [ones(size(a_2), 1) a_2];

for i = can_p,
  if can_p = 1:
    p = sigmoid(X(i) * Theta2'(i));
  end

[z p] = max(p, [], 2);   

end
