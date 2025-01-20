import math

def length(lst):
    return len(lst)

def mean(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):
    if not lst:
        return None
    return max(lst) - min(lst)

def median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def standard_deviation(lst):
    if not lst:
        return None
    avg = mean(lst)
    variance = sum((x - avg) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)

def list_statistics(lst):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input must be a list of numeric values.")
    
    stats = {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }
    return stats

numbers = [1, 2, 3, 4, 5]
print("Length:", length(numbers))  #5
print("Mean:", mean(numbers))      # 3.0
print("Range:", range_of_list(numbers))  #  4
print("Median:", median(numbers))  # 3
print("Standard Deviation:", standard_deviation(numbers))  
print("Statistics:", list_statistics(numbers))

print("Empty list stats:", list_statistics([]))   
print("Single element stats:", list_statistics([42]))   
print("Negative numbers stats:", list_statistics([-3, -2, -1, 0, 1, 2, 3]))  
print("Floating-point stats:", list_statistics([1.5, 2.5, 3.5]))  
