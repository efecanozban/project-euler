def main():
    longest_chain = 0
    starting_point_leads_to_longest_chain = 1
    for starting_point in range(1, 1000001):
        chain_segment = starting_point
        counter = 1
        while True:
            if chain_segment == 1:
                if counter > longest_chain:
                    longest_chain = counter
                    starting_point_leads_to_longest_chain = starting_point
                break
            elif chain_segment % 2 == 0:
                chain_segment //= 2
                counter += 1

            else:
                chain_segment = chain_segment * 3 + 1
                counter += 1

    print(starting_point_leads_to_longest_chain)


main()

# answer: 837799
# 30.03.2020