function [n] = morph(dataset, morph_rate)

    disp(["Morphing dataset ", num2str(dataset)])

    #Load Theta
    load(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(dataset) ".mat"])
    % load(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(dataset) ".mat"])
    
    % Flatten all Thetas
    new_theta_1 = reshape(Theta1, 1, []);
    new_theta_2 = reshape(Theta2, 1, []);
    new_theta_3 = reshape(Theta3, 1, []);
    
    m1 = length(new_theta_1);
    m2 = length(new_theta_2);
    m3 = length(new_theta_3);
    
    for i = 1 : m1,
        new_theta_1(i) *= 1 + randn() * morph_rate;
    endfor

    for i = 1 : m2,
        new_theta_2(i) *= 1 + randn() * morph_rate;
    endfor

    for i = 1 : m3,
        new_theta_3(i) *= 1 + randn() * morph_rate;
    endfor
    
    % Reshape Thetas
    Theta1 = reshape(new_theta_1, [size(Theta1)]);
    Theta2 = reshape(new_theta_2, [size(Theta2)]);
    Theta3 = reshape(new_theta_3, [size(Theta3)]);
    tic
    
    % Save files
    save(["/home/joseph/Desktop/chess_neural_network/engine_data/neural_net_dataset_" num2str(dataset) ".mat"], "Theta1", "Theta2", "Theta3");
    % save(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(dataset) ".mat"], "Theta1", "Theta2", "Theta3");
    toc
    n = 0;
    
    end