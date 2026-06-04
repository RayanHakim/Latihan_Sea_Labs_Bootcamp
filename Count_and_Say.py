# Count and Say:
# Bangun elemen ke-n dari urutan count-and-say menggunakan
# run-length encoding (RLE).

class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            current = []
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    current.append(str(count))
                    current.append(result[i - 1])
                    count = 1

            current.append(str(count))
            current.append(result[-1])

            result = "".join(current)

        return result

# Penjelasan:
# - Mulai dari countAndSay(1) = "1".
# - Untuk setiap langkah, baca string sebelumnya.
# - Hitung berapa kali suatu digit muncul berurutan.
# - Simpan sebagai:
#       jumlah + digit
# - Gabungkan hasil menjadi string baru.
# - Ulangi sampai mencapai n.