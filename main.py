def is_monotonic(array):
    def is_stonks(array):
        i = 0
        while i < len(array) - 1:
            if array[i] <= array[i + 1]:
                i += 1
            else:
                return False
                break
        return True
    
    def is_not_stonks(array):
        i = 0
        while i < len(array) - 1:
            if array[i] >= array[i + 1]:
                i += 1
            else:
                return False
                break
        return True
    
    return is_stonks(array) or is_not_stonks(array)
