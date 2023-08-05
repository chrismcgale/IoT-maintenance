import glob
import pandas
import numpy as np
import os

def moving_average(arr, window_size):
    # Define the convolution kernel (all elements equal to 1/window_size)
    kernel = np.ones(window_size) / window_size

    # Use the 'valid' mode to ignore the edges where the window doesn't fit
    moving_avg = np.convolve(arr, kernel, mode='valid')

    return moving_avg

files = glob.glob('.\data\\test_FD00[0-9].txt') + glob.glob('.\data\\train_FD00[0-9].txt')
    
for old_file_path in files:
    new_file_path = old_file_path.replace('.txt', '_agg.txt')
        
    # Delete the file if exists already
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
        

for old_file_path in files:
    with open(old_file_path, newline='') as file:
        new_file_path = old_file_path.replace('.txt', '_agg.txt')
        
        # Delete the file if exists already
        if os.path.exists(new_file_path):
            os.remove(new_file_path)
            
        csv_reader = pandas.read_csv(file, delimiter=' ')
        curr_id = -1
        window_size = 5
        
        window_values = []

        for line in csv_reader.to_numpy():
            
            # Incase of file end
            if np.issubdtype(line.dtype, object):
                break

            if line[0] != curr_id and curr_id != -1:
                stacked_array = np.vstack(window_values)
                std_dev_by_index = np.std(stacked_array, axis=0)
                moving_avg = np.sum(stacked_array, axis=0) / len(window_values)
                
                # Empty window
                while window_values:
                    # Output to new file
                    with open(new_file_path, 'a') as new_file:
                        # Only output aggregate values so we're not repeating
                        np.savetxt(new_file, np.append(moving_avg, std_dev_by_index), delimiter=' ', newline=" ", fmt="%.3f")
                        new_file.write('\n')
                    window_values.pop(0)
                
                # Reset window for new device
                curr_id = line[0]
                window_values = []
                
                
            sensor_data = line[5:26]
            window_values.append(sensor_data)
            
            # Remove oldest item from window if size is reached
            if len(window_values) > window_size:
                window_values.pop(0)
                
            # Calc moving average and std
            if len(window_values) == window_size:
                stacked_array = np.vstack(window_values)
                std_dev_by_index = np.std(stacked_array, axis=0)
                moving_avg = np.sum(stacked_array, axis=0) / window_size

                # Output to new file
                with open(new_file_path, 'a') as new_file:
                    # Only output aggregate values so we're not repeating
                    np.savetxt(new_file, np.append(moving_avg, std_dev_by_index), delimiter=' ', newline=" ", fmt="%.3f")
                    new_file.write('\n')
                    
        if len(window_values) > 0:
                    
            stacked_array = np.vstack(window_values)
            std_dev_by_index = np.std(stacked_array, axis=0)
            moving_avg = np.sum(stacked_array, axis=0) / len(window_values)
            
            # Empty window
            while window_values:
                # Output to new file
                with open(new_file_path, 'a') as new_file:
                    # Only output aggregate values so we're not repeating
                    np.savetxt(new_file, np.append(moving_avg, std_dev_by_index), delimiter=' ', newline=" ", fmt="%.3f")
                    new_file.write('\n')
                window_values.pop(0)
                