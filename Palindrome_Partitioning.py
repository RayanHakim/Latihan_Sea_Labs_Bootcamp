# Palindrome Partitioning:
# Bagi string menjadi beberapa substring sehingga setiap substring adalah palindrome.
# Kembalikan semua kemungkinan pembagian yang valid.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result

# Penjelasan:
# - Gunakan backtracking untuk mencoba semua kemungkinan pembagian string.
# - Setiap substring yang dipilih harus palindrome.
# - Jika substring valid:
#       1. Tambahkan ke path.
#       2. Lanjutkan pencarian dari posisi berikutnya.
#       3. Kembalikan keadaan sebelumnya (backtrack).
# - Jika sudah mencapai akhir string, simpan hasil partisi saat ini.
# - Fungsi is_palindrome() digunakan untuk mengecek apakah substring palindrome.