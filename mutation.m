function [new_theta] = mutation(Theta, mutation_rate)

new_theta = reshape(Theta, 1, []);

m = length(new_theta);

a = randi(mutation_rate * 10, 1, 10);

for i = 1:10,
  if a(i)<=m,
    new_theta(a(i)) = 1 - new_theta(a(i));
  endif
end

new_theta = reshape(new_theta, [size(Theta)]);