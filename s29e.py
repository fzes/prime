from time import time

n = int(input('Enter n?'))
tik = time()

prime_numbers = [2]
c = [[2, 3]]
end = 2
for i in range(3,n,2):
    for p in prime_numbers:
        if i % p == 0:
            break
    else:
        pre_end = end
        end = i
        prime_numbers.append(i)
        if end-pre_end ==2:
            c.append([pre_end, end])    
    
print('numbers of prime numbers less than "n" = ', len(prime_numbers))
#print(prime_numbers)
print(c)
tok = time()
print('time of prosses=', tok-tik, 'seconds')