# Displaying patterns

def display_pattern(n):
    line = []
    last = []
    for i in range (n+1):
        num = str(i)
        last.insert(0,num)
        lastline = ' '.join(last)
        
    for i in range (n+1):
        num = str(i)
        line.insert(0,num)
        newline = ' '.join(line)
        print (newline.rjust(len(lastline)))
    
display_pattern(10)
