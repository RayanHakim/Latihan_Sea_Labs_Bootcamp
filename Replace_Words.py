# Replace Words:
# Ganti setiap kata dalam kalimat dengan root terpendek
# yang menjadi prefix dari kata tersebut.

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        words = sentence.split()
        result = []

        for word in words:
            replacement = word

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in dictionary:
                    replacement = prefix
                    break

            result.append(replacement)

        return " ".join(result)

# Penjelasan:
# - Simpan dictionary ke set agar pencarian cepat.
# - Pecah sentence menjadi kata-kata.
# - Untuk setiap kata:
#     - cek prefix dari depan satu per satu
#     - jika ketemu root di dictionary, langsung pakai itu
#     - pilih yang paling pendek otomatis karena stop di pertama ketemu
# - Gabungkan kembali menjadi kalimat.