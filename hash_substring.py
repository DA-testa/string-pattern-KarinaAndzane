# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    mode = input()
    if 'I' in mode:
        return (input().rstrip(), input().rstrip())
#         first_line = input()   # pattern
#         second = input()         # text
        
    elif 'F' in mode:
         filename=input()
         with open ("./tests/"+filename, mode ='r') as fails:
            return (fails.readline().rstrip(), fails.readline().rstrip())
#                 first_line = fails.readline() # pattern
#                 second = fails.readline()     # text

    else:
        print("error")          
        
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    
    # return (input().rstrip(), input().rstrip())
def hashing (part):
    hash = 0
    for i in range(0,n):
        char = ord(part[i] % 96)
        hash = (hash*10+char)
    return hash
    
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
        result=[]
        n = len(pattern)
        m = len(text)-n
        hashed_pattern = hashing (substring)
            
            
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

