function p = feedforward_prop_config_o_layer(p, Theta, can_p, a)

for i = 1 : length(Theta);
  
  if can_p(i),
    p(i) = sigmoid(a(i) * Theta(i));
  endif
end

