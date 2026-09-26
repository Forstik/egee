# time = 42 * 60 + 30
# k = 2
# n =  44 * 1000
# bitrate = 295905280
# tracks = 12
# header = 110 * 1024 * 8
# i = 16
# V = k * time * i * n
# V_al = V + header * 12
# q = V_al // bitrate
# print(q)

# time = 7 * 60
# k = 4
# i = 32
# n = 44000
# bitrate = 3 * 1024 * 8
# V = k * time * i * n
# q = V / bitrate
# print(q // 3600)

# time = 49 * 60
# k = 2
# bitrate = 245839600
# i = 16
# n = 48000
# tracks = 7
# header = 55 * 2 ** 13
# V = n * time * k * i
# V_1 = V + header * 7
# q = V_1 // bitrate
# print(q)

# time = 35 * 60 + 50
# k = 2
# n = 20000
# i = 32
# V_album = 339 * 2 ** 23
# tracks = 13
# V_songs = k * time * i * n
# header_kb = (V_album - V_songs) / 13
# header_kb = header_kb // 2 ** 13
# print(header_kb)

# from math import ceil
# i = 8
# time = 2 * 60 + 20
# n = 28000
# k = 2
# V = k * time * i * n
# V_kb = V / 2 ** 13
# print(ceil(V_kb))

time = 4 * 60 + 18
i = 16
n = 20000
k = 1
V = time * i * n * k
V_kb = V / 2 ** 23
print(V_kb)

