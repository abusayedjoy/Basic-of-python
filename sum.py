#check sum
def mysum(num_list):
    count = 0
    
    for number in num_list:
        count = count + number
        
    return count

print(mysum(range(5, 80)))
#end

   
#check square
def square_number(num):
  return num ** 2

print(square_number(50))
#end


#check even    
def is_even(number):
    return number % 2 == 0

print(is_even(50))
#end


#check string length
def string_len(mystring):
    count = 0
    
    for letter in mystring:
        count += 1
        
    return count

print(string_len("fuck you"))
#end


