function [new_theta1, new_theta2] = reproduction(Theta1, Theta2)

new_theta1 = zeros(size(Theta1));
new_theta2 = zeros(size(Theta2));

a = 0;

for i = 1 : size(Theta1, 1),
  for j = 1 : length(Theta1),
    a = randi(2) - 1;
    if a,
      new_theta1(i, j) = Theta1(i, j);
      new_theta2(i, j) = Theta2(i, j);
    else,
      new_theta1(i, j) = Theta2(i, j);
      new_theta2(i, j) = Theta1(i, j);
      
    endif
    
  endfor
end

end