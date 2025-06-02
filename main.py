import math

def variance(data, mean):
    n = len(data)
    total = 0
    for i in range(n):
        total += pow((data[i]-mean),2)

    return total/n

def skewness(data, mean, std):
    n = len(data)
    total = 0
    for i in range(n):
        total += pow((data[i]-mean),3)

    return total/(n * pow(std,3))

def kurtosis(data, mean, std):
    n = len(data)
    total = 0
    for i in range(n):
        total += pow((data[i]-mean),4)

    return total/(n * pow(std,4))

data = [20,10,45,25,60,55,18,70,15,90]
n = len(data)
mean = sum(data)/n

varians = variance(data,mean)
std = math.sqrt(varians)

skew = skewness(data, mean, std)
kurto = kurtosis(data, mean, std)

print(f"Data: {data}")
print(f"Banyak Data: {n}")
print(f"Mean Data: {mean:1.0f}")
print(f"Varians: {varians:1.0f}")
print(f"Standard Deviasi: {std:0.2f}")
print(f"Skewness: {skew:0.2f}")
print(f"Kurtosis: {kurto:0.2f}")