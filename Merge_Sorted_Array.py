# Merge Sorted Array:
# Gabungkan dua array terurut ke dalam nums1 secara in-place
# sehingga hasil akhirnya tetap terurut.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Penjelasan:
# - Gunakan tiga pointer:
#     p1 = elemen terakhir data valid di nums1
#     p2 = elemen terakhir di nums2
#     p  = posisi terakhir hasil merge
#
# - Bandingkan elemen terbesar dari kedua array.
# - Masukkan yang lebih besar ke posisi p.
# - Geser pointer yang digunakan.
# - Jika nums2 masih memiliki elemen tersisa,
#   salin semuanya ke nums1.
#
# - Tidak perlu mengembalikan nilai karena nums1
#   dimodifikasi langsung (in-place).