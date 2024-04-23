#Script to get the average from a list of numbers

def find_average(numbers):
        if not numbers:
            print ("Empty")            
        else:
            sum_of_list = 0
            for i in range(len(numbers)):
                sum_of_list += numbers[i]                                               
                average = sum_of_list/len(numbers)
            print (average) 
            pass

def find_average_user():
    input_string = input('Enter elements of a list separated by space \n')
    user_list = input_string.split()		##Get user input on a list of numbers
    #print('string list: ', user_list)
    numbers = [int(i) for i in user_list]	##Convert user input str to int
    print (numbers)
    sum_of_list = 0
    for i in range(len(numbers)):
        sum_of_list += numbers[i]
        average = sum_of_list/len(numbers)
    print (average)

if __name__ == "__main__":
        find_average([2, 2, 2, 4, 6, 8, 20])
        find_average([])
        find_average_user()

