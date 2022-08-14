function [theta] = get_theta_bog(theta_num, layer)

    % load(["C:\\Users\\076-jgoyder\\Chess engine\\chess_neural_network\\engine_data\\neural_net_dataset_" num2str(Theta) ".mat"])
    % load(["/Users/joseph_chiao/Desktop/Advance Research/Machine Learning/Chess engine/chess_neural_network/engine_data/neural_net_dataset_" num2str(Theta) ".mat"])
    load(["/home/joseph/Desktop/chess_neural_network/best_of_generations/neural_net_dataset_" num2str(theta_num) ".mat"])
    if layer == 1,
        theta = Theta1;
    endif
    
    if layer == 2,
        theta = Theta2;
    endif 
    
    if layer == 3,
        theta = Theta3;
    endif 