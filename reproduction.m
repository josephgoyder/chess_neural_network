function [new_theta1, new_theta2] = reproduction(Theta1, Theta2)

new_theta1 = reshape(Theta1, 1, []);

new_theta2 = reshape(Theta2, 1, []);

a = randi(2, 1, length(new_theta1)) - 1;

for i = 1 : length(new_theta1),
  if a(i),
    new_theta1(i) = Theta2(i);
    new_theta2(i) = Theta1(i);
      
  endif
    
  
end

new_theta1 = reshape(new_theta1, [size(Theta1)]);
new_theta2 = reshape(new_theta2, [size(Theta2)]);

end