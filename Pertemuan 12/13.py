lemari = {}
buku = {}
album = {}
buku['novel'] = 7
buku['majalah'] = 9
album['musik'] = 4
lemari['novel'] = buku
lemari['buku'] = buku
lemari['album'] = album
print(len(lemari['buku']))