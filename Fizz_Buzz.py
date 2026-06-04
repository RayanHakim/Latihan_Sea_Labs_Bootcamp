# FizzBuzz:
# Cetak daftar string dari 1 sampai n dengan aturan:
# kelipatan 3 -> "Fizz"
# kelipatan 5 -> "Buzz"
# kelipatan 3 dan 5 -> "FizzBuzz"

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

# Penjelasan:
# - Iterasi dari 1 sampai n.
# - Cek kondisi kelipatan 3 dan 5 terlebih dahulu (paling spesifik).
# - Lalu cek kelipatan 3 atau 5.
# - Jika tidak memenuhi semua kondisi, masukkan angka sebagai string.