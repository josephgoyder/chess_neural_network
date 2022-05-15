function p = feedforward_prop_config_o_layer(p, Theta, can_p, a)

[z, m] = size(Theta);

for i = 1 : m;
  
  if can_p(i),
    p(i) = sigmoid(a * Theta(:, i));
  endif
end

