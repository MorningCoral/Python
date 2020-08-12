# Converting milliseconds to hours, minutes, and seconds

# 1s = 1000 ms
# 1 min = 60 s = 60000 ms
# 1h = 60 min = 3600000

def convert_ms(n):
    h = n // 3600000
    m = (n % 3600000) // 60000
    s = ((n % 3600000) % 60000) // 1000
    print('{0}:{1}:{2}'.format(h,m,s))
