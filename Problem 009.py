def main():
    for i in range(500):
        for j in range(500):
            for k in range(500):
                if i+j+k ==1000 and i**2 + j**2 == k**2:
                    print(i*j*k)
                    return 0
main()

# answer: 31875000
# 30.03.2020
