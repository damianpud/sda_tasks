def hamming(standard_a, standard_b):
    result = 0
    zipped_standards = zip(standard_a, standard_b)
    for pair in zipped_standards:
        if pair[0] != pair[1]:
            result += 1
    return result


if __name__ == '__main__':
    suspect_1 = input('1st suspect Dna: ')
    suspect_2 = input('2nd suspect Dna: ')
    child = input('Child DNA: ')
    dist_1 = hamming(suspect_1, child)
    dist_2 = hamming(suspect_2, child)
    if dist_1 < dist_2:
        print('Suspect #1 is a father.')
    else:
        print('Suspect #2 is a father.')