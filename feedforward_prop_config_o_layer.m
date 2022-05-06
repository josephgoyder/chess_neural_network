function p = feedforward_prop_config_o_layer(p, Theta, can_p, a)

[a, m] = size(Theta)

for i = 1 : m;
  
  if can_p(i),
    p(i) = sigmoid(a(i) * Theta(i));
  endif
end

