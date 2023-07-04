def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    tengah = len(arr) // 2
    half_kiri = arr[:tengah]
    hals_kanan = arr[tengah:]
    
    half_kiri = mergesort(half_kiri)
    hals_kanan = mergesort(hals_kanan)
    
    return merge(half_kiri, hals_kanan)


def merge(left, right):
    hasil = []
    x = 0
    y = 0 
    
    while x < len(left) and y < len(right):
        if left[x] > right[y]:
            hasil.append(left[x])
            x += 1
        else:
            hasil.append(right[y])
            y += 1
    
    while x < len(left):
        hasil.append(left[x])
        x += 1
    
    while y < len(right):
        hasil.append(right[y])
        y += 1
    
    return hasil


data = input("Input angka satu persatu (batasi dengan spasi): ").split()
data = [int(i) for i in data]

data = mergesort(data)

print("Data terurut dari besar ke kecil:", data)