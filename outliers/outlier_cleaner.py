#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import math
    cleaned_data = []

    ### your code goes here
    errors = []
    for net, pred in zip(net_worths, predictions) :
        errors.append(math.sqrt((net - pred)**2))
    
    sorted_errors = sorted(errors)
    temp = int(math.floor(len(sorted_errors) * 0.9))
    max_errors = sorted_errors[temp :]
    
    for index in range(len(net_worths)) :
        error = (math.sqrt((net_worths[index] - predictions[index])**2))
        
        if error in max_errors:
            pass
        else:
            cleaned_data.append([ages[index], net_worths[index], error])
    
    return cleaned_data



