# Baseball Game: hitung total skor berdasarkan operasi pada record skor.

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))

        return sum(record)

# Penjelasan:
# - Gunakan list sebagai stack untuk menyimpan skor.
# - Angka biasa ditambahkan ke record.
# - "+" menambahkan jumlah dua skor terakhir.
# - "D" menambahkan dua kali skor terakhir.
# - "C" menghapus skor terakhir.
# - Setelah semua operasi diproses, jumlahkan seluruh skor.