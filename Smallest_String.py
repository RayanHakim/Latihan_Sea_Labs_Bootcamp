# Smallest String With A Given Numeric Value:
# Buat string sepanjang n dengan total nilai karakter = k,
# dan hasilnya harus yang paling kecil secara leksikografis.

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ["a"] * n
        k -= n

        for i in range(n - 1, -1, -1):
            add = min(25, k)
            result[i] = chr(ord('a') + add)
            k -= add

        return "".join(result)

# Penjelasan:
# - Awalnya isi semua karakter dengan 'a' (nilai 1).
# - Kurangi k sebanyak n karena setiap posisi sudah bernilai 1.
# - Mulai dari belakang, tambahkan nilai sebanyak mungkin
#   (maksimal 25 karena 'a' -> 'z' selisihnya 25).
# - Mengisi dari belakang membuat bagian depan tetap sekecil mungkin,
#   sehingga string menjadi paling kecil secara leksikografis.
# - Gabungkan array karakter menjadi string dan kembalikan hasilnya.