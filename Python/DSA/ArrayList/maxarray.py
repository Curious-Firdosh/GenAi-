

def find_max_element(arr):
  
   if not arr:
        return None
   
   max_Value = arr[0]
   
   for num in arr:
        if num > max_Value:
            max_Value = num
    
   return max_Value       
    
        

       
    
arrIntegers = [-7,-8,-80]
print(find_max_element(arrIntegers))