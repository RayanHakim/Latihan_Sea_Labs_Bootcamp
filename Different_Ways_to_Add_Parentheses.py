# Different Ways to Add Parentheses:
# Hitung semua kemungkinan hasil dari berbagai cara
# menambahkan tanda kurung pada ekspresi matematika.

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i + 1:])

                    for left in left_results:
                        for right in right_results:
                            if ch == "+":
                                results.append(left + right)
                            elif ch == "-":
                                results.append(left - right)
                            else:
                                results.append(left * right)

            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return solve(expression)

# Penjelasan:
# - Cari setiap operator (+, -, *) dalam ekspresi.
# - Bagi ekspresi menjadi bagian kiri dan kanan.
# - Hitung semua kemungkinan hasil dari kiri dan kanan secara rekursif.
# - Gabungkan seluruh kombinasi hasil sesuai operator.
# - Jika tidak ada operator, berarti ekspresi hanya angka,
#   sehingga langsung dikembalikan sebagai hasil.
# - Memoization digunakan agar sub-ekspresi yang sama
#   tidak dihitung berulang kali.