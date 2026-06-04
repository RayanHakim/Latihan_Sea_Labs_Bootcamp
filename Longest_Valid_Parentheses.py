# Longest Valid Parentheses:
# Cari panjang substring tanda kurung valid terpanjang.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length

# Penjelasan:
# - Gunakan stack untuk menyimpan indeks '('.
# - Inisialisasi stack dengan -1 sebagai penanda awal.
# - Jika menemukan '(', simpan indeksnya.
# - Jika menemukan ')', hapus pasangan '(' terakhir.
# - Jika stack kosong, simpan indeks ')' sebagai batas baru.
# - Jika stack tidak kosong, hitung panjang substring valid:
#       panjang = indeks saat ini - indeks teratas stack
# - Simpan panjang maksimum yang ditemukan.