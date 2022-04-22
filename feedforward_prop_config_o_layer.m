function p = predict(Theta, can_p, a)

for i = 1 : size(can_p, 1),
  
  if can_p(i),
    p(i) = sigmoid(X(i) * Theta'(i));
  
  endif

end