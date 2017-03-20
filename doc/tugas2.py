graph = {
             'Jln Bumi': ['Pasar Mayestik'],
             'Pasar Mayestik': ['Jln Rs Pertamina'],
             'Jln Rs Pertamina': ['Jln Pakubuwono'],
             'Jln Pakubuwono': ['Jln Lauser'],
             'Jln Lauser': ['Jln Kyai Maja'],
             'Jln Kyai Maja': ['Jln Hasanudin Dalam'],
             'Jln Hasanudin Dalam': ['Blok M Mall'], 
        }

def rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
        rute = rute + [lokasi_awal]
        if lokasi_awal == lokasi_tujuan:
            return rute
            if not graph.has_key(lokasi_awal):
                    return None
        rutependek = None
        for node in graph[lokasi_awal]:
            if node not in rute:
                rutebaru = rutepalingpendek(graph, node, lokasi_tujuan, rute)
                if rutebaru:
                    if not rutependek or len(rutebaru) < len(rutependek):
                        rutependek = rutebaru
        return rutependek
print("Rute Bus Kota SMPN 19 Jakarta - Blok M Mall")
print("(Jln Bumi-Pasar Mayestik-Rs Pertamina-Jln Pakubuwono-Jln Lauser-Jln Kyai Maja-Jln Hasanudin Dalam-Blok M Mall)")
print("Rima Rizky Lestari - 1144118")
print("\n")
lokasi_awal = raw_input("Masukan Lokasi Awal : ")
lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
hasilnya = rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
print "Rute Terpendek", hasilnya ,".",