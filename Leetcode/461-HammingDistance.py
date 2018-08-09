# 461. Hamming Distance
#

def hamming_distance(x, y):
    xbin = bin(x)[2:]
    ybin = bin(y)[2:]
    length = max(len(xbin), len(ybin))
    xbin = xbin.zfill(length)
    ybin = ybin.zfill(length)

    result = 0
    for i in range(length):
        if xbin[i] != ybin[i]:
            result += 1
    
    return result

if __name__ == '__main__':
    print(hamming_distance(2324, 3242444))

