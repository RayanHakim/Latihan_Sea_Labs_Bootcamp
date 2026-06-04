# Valid Sudoku:
# Periksa apakah papan Sudoku 9x9 valid sesuai aturan baris,
# kolom, dan sub-box 3x3.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if num in rows[r]:
                    return False

                if num in cols[c]:
                    return False

                if num in boxes[box_index]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True

# Penjelasan:
# - Gunakan 3 kelompok set:
#     1. rows  -> menyimpan angka yang sudah muncul di setiap baris
#     2. cols  -> menyimpan angka yang sudah muncul di setiap kolom
#     3. boxes -> menyimpan angka yang sudah muncul di setiap kotak 3x3
#
# - Untuk setiap sel:
#     - Lewati jika berisi '.'
#     - Hitung indeks sub-box:
#           (r // 3) * 3 + (c // 3)
#     - Jika angka sudah ada di row/col/box, Sudoku tidak valid.
#     - Jika belum ada, simpan ke set.
#
# - Jika seluruh papan diperiksa tanpa duplikasi,
#   maka Sudoku valid.