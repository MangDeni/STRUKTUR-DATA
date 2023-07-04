def binary_search(data, cari):
    low = 0
    high = len(data) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if data[mid] < cari:
            low = mid + 1
        elif data[mid] > cari:
            high = mid - 1
        else:
            return mid
    return -1
# data = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 39]

# memasukkan data
data = input("Masukkan data (batasi dengan spasi): ").split()
data = [int(i) for i in data]

# print data
print("Data : ",data)
cari = int(input("Masukkan data yang ingin dicari : "))
result = binary_search(data, cari)
if result != -1:
    print("Data yang anda cari ditemukan pada indeks ke-", str(result))
else:
    print("Data yang Anda cari tidak ditemukan pada data")