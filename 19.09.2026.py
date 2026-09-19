# from math import log2
# from os import times_result
#
# res = 1024 * 768
# bitrate = 1310720
# N = 4096
# T = 300
#
# # N = 2 ** i
# i = log2(N)
# img_size = res * i
#
# package_size = bitrate * T
# img_in_package = package_size // img_size
# print(img_in_package)

# from math import log2, ceil
# res = 2764 * 1793
# N = 7026
# img_in_package = 148
# bitrate = 18349566
# i = ceil(log2(N))
# img_size = res * i
# package_size = img_size * img_in_package
# time = package_size / bitrate
# print(int(time))

# from math import log2, ceil
# res = 1024 * 960
# palitra = 16384
# package = 400
# i = ceil(log2(palitra)) #вес одного пикселя
# img_size = res * i
# mem_size = img_size * package / 2 ** 23
# print(int((mem_size)))

# res = 512 * 750
# memory_size = 80 * 2 ** 13
# i = memory_size // (res * 0.65)
# N = 2 ** i
# print(N)

# res = 2560 * 5040
# memory_size = 14175 * 2 ** 13
# i = memory_size // res
# N = 2 ** i
# print(N)

# res = 1024 * 960
# img_in_package = 32
# bitrate = 1474560
# T = 140
# package_size = bitrate * T
# img_size = package_size / img_in_package
# i = img_size // res
# N = 2 ** i
# print(N)

# from math import log2, ceil
# res = 1024 * 768
# i = 23
# res_compressed = 800 * 600 #res сжатого изображения
# i_compressed = 22 #глубинка цвета сжатого изображения
# img_size = res * i
# img_size_compressed = res_compressed * i_compressed
# result = img_size * 100 - img_size_compressed * 100
# res_kb = result // 2 ** 13
# print(res_kb)
