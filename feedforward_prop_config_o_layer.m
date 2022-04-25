function p = feedforward_prop_config_o_layer(p, Theta, can_p, a)



for i = 1 : 76,
  
  if can_p(i),
    p(i) = sigmoid(a * Theta(:, i));
  endif
end
p