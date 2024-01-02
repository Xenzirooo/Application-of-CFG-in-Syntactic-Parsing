# Rules of the grammar
R = {
    "K" : [["S", "P"],["S", "A1"], ["S" ,"A2"], ["S", "A3"],["S", "A4"]],

    "A1" : ["P", "O"],
    "A2" : ["A1", "Pel"],
    "A3" : ["A1", "Ket"],
    "A4" : ["A2", "Ket"],

    "S": [
        ["Pronoun", "Pronoun"], ["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"],
        ["NP", "Adj"], ["PropNoun", "PropNoun"], ["Noun", "Pronoun"], ["Noun", "PropNoun"],
        ["kita"], ["ini"], ["kami"], ["itu"], ["mereka"], ["dia"], ["saya"], ["mereka"],
        ["saya"], ["anda"], ["ini"], ["ia"], ["tersebut"], ["dia"], ["itu"], ["tersebut"],
        ["kami"], ["beliau"], ["saya"], ["aku"], ["itu"], ["dia"], ["kita"], ["ini"],
        ["ia"], ["kami"], ["mereka"], ["kami"], ["aku"], ["kita"], ["itu"], ["ini"],
        ["saya"], ["dia"], ["itu"], ["kami"], ["saya"], ["aku"], ["dia"], ["ini"],
        ["mereka"], ["ia"], ["tersebut"], ["-nya"], ["kamu"], ["Dinda"], ["Rini"], ["Budi"],
        ["Sinta"], ["Irfan"], ["Ani"], ["Maya"], ["Adit"], ["Dian"], ["Fitri"], ["Agung"],
        ["Krisna"], ["Putra"], ["Adi"], ["Renata"], ["Bagas"], ["Putri"], ["Dinda"],
        ["Ardi"], ["Sekar"], ["Abi"], ["Anton"], ["Riski"], ["Bagas"], ["Bayu"], ["Juna"],
        ["Kevin"], ["Bali"], ["Manado"], ["Albert"], ["Desi"], ["Yudi"], ["Jakarta"],
        ["Abdi"], ["Ata"], ["Jalan"], ["Jimbaran"], ["Denpasar"], ["Bintang"], ["Putu"],
        ["Ronaldo"], ["Widya"], ["Wulan"], ["Made"], ["Puncak"], ["Bogor"], ["Kota"],
        ["Yogyakarta"], ["Irma"], ["Ana"], ["Anto"], ["Budi"], ["Amerika"], ["Nyoman"],
        ["Bandung"], ["Dokter"], ["Cahya"], ["LA"], ["Rumah"], ["Sakit"], ["Bali"],
        ["Mandara"], ["Bandara"], ["Ngurah"], ["Rai"], ["Bali"], ["Jimbaran"],
        ["Aokigahara"], ["Jepang"], ["Ryujin"], ["Senin"], ["Jurusan"], ["Informatika"],
        ["Universitas"], ["Udayana"], ["Tepung"], ["Terigu"], ["Anna"], ["Budi"], ["Andi"],
        ["Burhan"], ["Wayan"], ["Desa"], ["Penglipuran"], ["Bali"], ["Bu"], ["Indah"],
        ["Arkeologi"], ["Inggris"], ["Beni"], ["Budi"], ["Agung"], ["Andre"], ["Vema"],
        ["Anti"], ["Amel"], ["Rin"], ["Diana"], ["Andi"], ["Bandung"], ["Pinnochio"],
        ["Moana"], ["Kerobokan"], ["Indonesia"], ["Malaysia"], ["Elon"], ["Musk"],
        ["Madan"], ["Surtr"], ["Sinmara"], ["Kratos"], ["Yunani"], ["Tasya"], ["Thor"],
        ["Jormungandr"], ["Heimdall"], ["Aesir"], ["Adi"], ["Figo"], ["Alit"], ["Mona"],
        ["Brian"], ["Garry"], ["Bara"], ["Susan"], ["Jimbaran"], ["Risa"], ["Ani"],
        ["Widia"], ["Alit"], ["Susan"], ["Sasando"], ["Sumping"], ["Rendang"], ["Nusa"],
        ["Tenggara"], ["Timur"], ["Genggong"], ["Sumatera"], ["Selatan"], ["Lombok"],
        ["Louis"], ["Vuitton"], ["Taksa"], ["Pinus"], ["Dian"], ["Putu"], ["Rido"],
        ["Jovan"], ["Mamat"], ["Gita"], ["Ketut"], ["Dhimmas"], ["Adi"], ["Jeni"],
        ["Malaysia"], ["Tampak"], ["Siring"], ["Gianyar"], ["Indonesia"], ["Leonardo"],
        ["da"], ["Vinci"], ["Perang"], ["Dunia"], ["II"], ["Intan"], ["Pak"], ["Edi"],
        ["Beni"], ["Pak"], ["Arif"], ["ayah"], ["rani"], ["Anton"], ["siswa-siswa"]
    ],
    "P": [
        ["Adv", "VP"], ["Adj", "VP"], ["Verb", "VP"], ["Verb", "AdvP"],
        ["VP", "Verb"], ["Verb", "Verb"], ["Adj", "Verb"], ["Adv", "AdvP"],
        ["Adv", "Verb"], ["membaca"], ["mengikuti"], ["bermain"], ["membuat"],
        ["menghadiri"], ["mengoleksi"], ["memberikan"], ["belajar"], ["membaca"],
        ["mengunjungi"], ["memasak"], ["menampilkan"], ["menyiapkan"], ["membawa"],
        ["merayakan"], ["mendengar"], ["melihat"], ["menelepon"], ["menyiapkan"],
        ["menulis"], ["membelikan"], ["memasaki"], ["meminjami"], ["menawarkan"],
        ["memberitahukan"], ["menjanjikan"], ["menuduh"], ["menamai"], ["menobatkan"],
        ["menjahitkan"], ["membawakan"], ["memanggil"], ["menyebutkan"], ["mencarikan"],
        ["menjelaskan"], ["membuatkan"], ["menggambar"], ["menulis"], ["mengajar"],
        ["menonton"], ["makan"], ["menyimak"], ["melahirkan"], ["menari"], ["mengobrol"],
        ["bekerja"], ["bermain"], ["berjualan"], ["tertangkap"], ["melarikan"],
        ["merayakan"], ["berlatih"], ["melukis"], ["mencari"], ["berjumpa"],
        ["dilakukan"], ["mengucapkan"], ["menjadi"], ["mempersilakan"], ["masuk"],
        ["mengurung"], ["tutup"], ["dipukul"], ["diliburkan"], ["dimainkan"],
        ["bernyanyi"], ["belajar"], ["disebabkan"], ["menyiram"], ["tinggal"],
        ["berjalan"], ["ditemukan"], ["menabung"], ["menarik"], ["memikat"],
        ["pergi"], ["memiliki"], ["berlatih"], ["menonton"], ["mengunjungi"],
        ["pulang"], ["bermain"], ["menendang"], ["keluar"], ["bekerja"], ["berterimakasih"],
        ["membahas"], ["memberikan"], ["dilatih"], ["pergi"], ["berterima-kasih"],
        ["mencatat"], ["datang"], ["bekerja"], ["merokok"], ["ditemukan"],
        ["menyentuh"], ["dibuat"], ["berangkat"], ["menangis"], ["tersedu-sedu"],
        ["paham"], ["mencari"], ["kerja"], ["berkunjung"], ["berlari"], ["berada"],
        ["bersikap"], ["kirim"], ["berbicara"], ["meletakkan"], ["meloncat"],
        ["tinggal"], ["mengintip"], ["masuk"], ["duduk"], ["bersiap-siap"], ["masuk"],
        ["mati"], ["mengerjakan"], ["berjalan"], ["terpilih"], ["pindah"], ["ikut"],
        ["bertemu"], ["memiliki"], ["memutuskan"], ["pindah"], ["bekerja"], ["sampai"],
        ["pulang"], ["membawa"], ["berada"], ["merupakan"], ["berharap"], ["berakhir"],
        ["terletak"], ["menginap"], ["pergi"], ["bermain"], ["terjebak"], ["dibersihkan"],
        ["mencegah"], ["bangun"], ["terasa"], ["memilih"], ["meningkatkan"], ["mengatasi"],
        ["sengaja"], ["diletakkan"], ["digunakan"], ["menghemat"], ["diperlukan"],
        ["membuat"], ["senantiasa"], ["dijaga"], ["menghindari"], ["bekerja"],
        ["sama"], ["tercapai"], ["ditutup"], ["mempercepat"], ["sakit"], ["terluka"],
        ["jatuh"], ["pura-pura"], ["pergi"], ["dimarahi"], ["pulang"], ["masuk"],
        ["melanggar"], ["mengurangi"], ["bepergian"], ["mencegah"], ["mengikuti"],
        ["diperbaiki"], ["menjaga"], ["mendapatkan"], ["tumbuh"], ["dirawat"],
        ["dilakukan"], ["berlari"], ["berteriak"], ["bernyanyi"], ["memainkan"],
        ["bekerja"], ["menikmati"], ["berolahraga"], ["mencuri"], ["bersama"],
        ["tertarik"], ["minum"], ["digedor"], ["berteriak"], ["berjalan"], ["berangkat"],
        ["dituntut"], ["sengaja"], ["dipesan"], ["bernyanyi"], ["bunuh"], ["berbahasa"],
        ["bepergian"], ["tinggal"], ["bermain"], ["berkhotbah"], ["datang"],
        ["berdiskusi"], ["dipersilahkan"], ["memasuki"], ["terbuat"], ["terkenang"],
        ["menjadi"], ["berjumpa"], ["sengaja"], ["bertemu"], ["serupa"], ["terjadi"],
        ["datang"], ["berangkat"], ["bergantung"], ["keluar"], ["menyesal"], ["berdamai"],
        ["mengeluh"], ["berlawanan"], ["tergolong"], ["bercerita"], ["berdiskusi"],
        ["terbuat"], ["berhadapan"], ["bertemu"], ["siap"], ["bisa"], ["terdiri"],
        ["ditentukan"], ["pergi"], ["pulang"], ["duduk"], ["disusun"], ["disetrika"],
        ["dimasak"], ["dibuka"], ["belajar"], ["dipasang"], ["mengendarai"], ["diajarkan"],
        ["dimarahi"], ["dibuang"], ["dibersihkan"], ["disiram"], ["ditarik"], ["guling"],
        ["merupakan"], ["adalah"], ["ditanam"], ["berdebat"], ["bercerita"],
        ["menjawab"], ["mengetahui"], ["mempertanyakan"], ["didorong"], ["mogok"],
        ["membangkang"], ["bergurau"], ["dilukis"], ["berdiskusi"], ["menjelaskan"],
        ["menyangkul"], ["berasal"], ["berbelanja"], ["pergi"], ["terkena"], ["tidur"],
        ["terbuat"], ["dibuat"], ["menghadiri"], ["mempersiapkan"], ["teringat"],
        ["mempunyai"], ["makan"], ["mengirimkan"], ["membeli"], ["mendengarkan"]
    ],
    "O": [
        ["NP", "Adj"], ["NP", "Pronoun"], ["NP", "PropNoun"], ["Noun", "NP"],
        ["NP", "Noun"], ["Noun", "Noun"], ["Noun", "Adj"], ["Noun", "Pronoun"],
        ["Noun", "Verb"], ["ilmu"], ["hari"], ["nanti"], ["proses"], ["pencarian"],
        ["korban"], ["saat"], ["terima"], ["kasih"], ["perhatian"], ["teman-teman"],
        ["dosen"], ["kampus"], ["kakeknya"], ["kampus"], ["juara"], ["kelas"],
        ["kalinya"], ["diri"], ["kamar"], ["motor"], ["toko"], ["sepatu"],
        ["sementara"], ["waktu"], ["bapak"], ["temannya"], ["sekolah"], ["wabah"],
        ["penyakit"], ["game"], ["orang"], ["sepanjang"], ["perjalanan"], ["masa"],
        ["depan"], ["ayah"], ["luar"], ["kota"], ["musibah"], ["banjir"], ["hal"],
        ["bunga"], ["kebun"], ["guru"], ["kaki"], ["rumah"], ["sepeda"], ["samping"],
        ["danau"], ["hari"], ["wanita"], ["laki-laki"], ["bank"], ["suasana"],
        ["kampung"], ["pertunjukkan"], ["perhatian"], ["orang-orang"], ["sekitar"],
        ["tempat"], ["senyuman"], ["hati"], ["sikap"], ["pertandingan"], ["sepak bola"],
        ["museum"], ["negara"], ["kantor"], ["anak-anak"], ["kali"], ["bola"],
        ["lapangan"], ["orang"], ["tua"], ["anak-anaknya"], ["petang"], ["jutawan"],
        ["orang"], ["tuanya"], ["rasa"], ["cicak"], ["pahlawan"], ["masa"],
        ["lalunya"], ["perusahaan"], ["bonus"], ["karyawan"], ["makanan"], ["kantin"],
        ["cerita"], ["drama"], ["kebun"], ["teh"], ["daerah"], ["toko-toko"],
        ["buku"], ["sekolah"], ["bantuan"], ["keluarga"], ["latihan"], ["soft"],
        ["skill"], ["orang"], ["bu"], ["pengeluaran"], ["bulan"], ["anak"],
        ["kampus"], ["ruangan"], ["catatan"], ["saat"], ["ayah"], ["kantor"],
        ["tadi"], ["barang"], ["tugas"], ["kelompok"], ["hari"], ["sabtu"],
        ["lalu"], ["orang"], ["hal-hal"], ["politik"], ["kakak"], ["keponakan"],
        ["lapangan"], ["basket"], ["orang"], ["tuanya"], ["kecantikan"], ["seorang"],
        ["bidadari"], ["foto"], ["email"], ["kekurangan"], ["aplikasi"], ["baju"],
        ["dalam"], ["lemari"], ["adik"], ["piring"], ["atas"], ["meja"], ["bukit"],
        ["kucing"], ["mobil"], ["dekat"], ["pabrik"], ["gadis"], ["jejaka"],
        ["balik"], ["jendela"], ["belakang"], ["luar"], ["rumah"], ["aktris"],
        ["layar"], ["penyakit"], ["tanaman"], ["kekeringan"], ["soal"], ["nomor"],
        ["nenek"], ["tahun"], ["rapat"], ["awal"], ["pernikahan"], ["kakak"],
        ["kantor"], ["bus"], ["penumpang"], ["paket"], ["rumah"], ["hutan"],
        ["tempat"], ["rumahnya"], ["bukit"], ["kakak"], ["ipar"], ["komplek"],
        ["mobilitas"], ["penduduk"], ["dataran"], ["paus"], ["hutan"], ["bakau"],
        ["selokan"], ["bencana"], ["banjir"], ["rutin"], ["pagi"], ["hari"],
        ["mahasiswa"], ["koding"], ["seorang"], ["pemula"], ["produsen"], ["bahan-bahan"],
        ["kualitas"], ["mutu"], ["produk"], ["rasa"], ["peringatan"], ["larangan"],
        ["diri"], ["kemampuan"], ["keharusan"], ["fitur"], ["mode"], ["daya"],
        ["baterai"], ["adonan"], ["kue"], ["persatuan"], ["perpecahan"], ["tujuan"],
        ["perbaikan"], ["jalan"], ["toilet"], ["perut"], ["motor"], ["sekolah"],
        ["malam"], ["penjara"], ["hukum"], ["virus"], ["penyakit"], ["penularan"],
        ["simulasi"], ["bencana"], ["alam"], ["masyarakat"], ["desa"], ["penghargaan"],
        ["kebersihan"], ["lingkungan"], ["tanaman"], ["pelajaran"], ["olahraga"],
        ["ruangan"], ["hujan"], ["hari"], ["ibu"], ["pasar"], ["adik"], ["kijang"],
        ["gitar"], ["warga"], ["bakti"], ["udara"], ["pagi"], ["kancil"],
        ["pak"], ["tani"], ["timun"], ["keluarga"], ["anak-anak"], ["tablet"],
        ["air"], ["pintu"], ["pertandingan"], ["rekan"], ["rektorat"], ["kuliah"],
        ["motor"], ["ulang"], ["tahun"], ["hal"], ["kehidupan"], ["semua"],
        ["murid"], ["ujian"], ["adik"], ["pesta"], ["ulang"], ["tahun"], ["akhir"],
        ["semester"], ["pemikiran"], ["nilai"], ["pancasila"], ["para"], ["tamu"],
        ["ruangan"], ["sejalan"], ["vas"], ["bunga"], ["tanah"], ["liat"],
        ["janji"], ["manismu"], ["juara"], ["kelas"], ["suatu"], ["hari"],
        ["nanti"], ["teman"], ["lamanya"], ["capybara"], ["tikus"], ["badai"],
        ["hujan"], ["pekan"], ["lalu"], ["pemuda"], ["kampung"], ["sebelah"],
        ["bapak"], ["guru"], ["sekolah"], ["orang"], ["lain"], ["organisasi"],
        ["kampus"], ["tindakannya"], ["rumah"], ["kakaknya"], ["hidup"], ["donatur"],
        ["adiknya"], ["perkataan"], ["sejarah"], ["pendidikan"], ["kebutuhan"],
        ["dasar"], ["seorang"], ["anak"], ["kisah"], ["hidupnya"], ["ayah"],
        ["ustadz"], ["orang"], ["tuanya"], ["pemimpin"], ["ekonomi"], ["dunia"],
        ["lenganku"], ["titanium"], ["alkohol"], ["zat"], ["kedudukan"], ["gubernur"],
        ["setingkat"], ["menteri"], ["timnas"], ["rekan"], ["bisnisnya"],
        ["program"], ["pemberdayaan"], ["ekonomi"], ["masyarakat"], ["otonomi"],
        ["daerah"], ["minyak"], ["air"], ["siswa"], ["masalah"], ["produk"],
        ["milik"], ["tetanggaku"], ["peristiwa"], ["mata"], ["kuliah"], ["modul"],
        ["pilihan"], ["kubuat"], ["negeri"], ["ayahnya"], ["kiamat"], ["kelompok"],
        ["dewa"], ["penjualan"], ["strategi"], ["pemasaran"], ["nenek"], ["masa"],
        ["rapat"], ["karya"], ["tulis"], ["tema"], ["kucing"], ["perbuatannya"],
        ["seni"], ["music"], ["kebun"], ["nasib"], ["kakak"], ["pasar"], ["kakaknya"],
        ["paman"], ["hati"], ["laporan"], ["ketentuan"], ["pemuda"], ["penjahat"],
        ["sana"], ["pengunjung"], ["pacarku"], ["sd"], ["kursi"], ["merah"],
        ["sejajar"], ["meja"], ["lembaga"], ["negara"], ["lainnya"], ["baju"],
        ["bapak"], ["ibu"], ["ayam"], ["pintu"], ["guru"], ["olahraga"], ["adik"],
        ["meja"], ["pak"], ["tukang"], ["sepeda"], ["mobil"], ["paman"], ["ayah"],
        ["guru"], ["bayi"], ["seorang"], ["penculik"], ["santan"], ["daging"],
        ["kelapa"], ["makanan"], ["sungai"], ["sampah"], ["jamu"], ["rempah"],
        ["kopi"], ["hitam"], ["gelas"], ["keramik"], ["tanaman"], ["kakak"],
        ["alat"], ["musik"], ["pohon"], ["babi"], ["rambut"], ["tepung"],
        ["beras"], ["tas"], ["jaket"], ["bulu"], ["domba"], ["gitar"], ["awetan"],
        ["kulit"], ["buaya"], ["kayu"], ["pertanyaan"], ["mobil"], ["sayur"],
        ["rumah"], ["tugas"], ["lukisan"], ["orang"], ["bubur"], ["perbaikan"],
        ["penagihan"], ["kota"], ["polisi"], ["utang"], ["posisi"], ["tanah"],
        ["kedatangan"], ["pencuri"], ["tahun"], ["pilihan"], ["sungai"], ["surat"],
        ["taman"], ["mainan"], ["robot"], ["minggu"], ["yoga"], ["gim"],
        ["online"], ["nama"], ["pemenang"], ["acara"], ["siswa-siswa"], ["klasik"]
    ],
    "Noun": [["ilmu"], ["hari"], ["nanti"], ["proses"], ["pencarian"], ["korban"], ["saat"], 
        ["terima kasih"], ["perhatian"], ["teman-teman"], ["dosen"], ["kampus"], ["kakeknya"], 
        ["kampus"], ["juara"], ["kelas"], ["kalinya"], ["diri"], ["kamar"], ["motor"], ["toko"],
        ["sepatu"], ["sementara"], ["waktu"], ["bapak"], ["temannya"], ["sekolah"], ["wabah"], 
        ["penyakit"], ["game"], ["orang"], ["sepanjang"], ["perjalanan"], ["masa depan"], ["ayah"],
        ["luar kota"], ["musibah"], ["banjir"], ["hal"], ["bunga"], ["kebun"], ["guru"], ["kaki"],
        ["rumah"], ["sepeda"], ["samping"], ["danau"], ["hari"], ["wanita"], ["laki-laki"], ["bank"],
        ["suasana"], ["kampung"], ["pertunjukkan"], ["perhatian"], ["orang-orang"], ["sekitar"], ["tempat"], 
        ["senyuman"], ["hati"], ["sikap"], ["pertandingan"], ["sepak bola"], ["museum"], ["negara"], ["kantor"], 
        ["anak-anak"], ["kali"], ["bola"], ["lapangan"], ["orang"], ["tua"], ["anak-anaknya"], ["petang"],
        ["jutawan"], ["orang"], ["tuanya"], ["rasa"], ["cicak"], ["pahlawan"], ["masa lalunya"], ["perusahaan"],
        ["bonus"], ["karyawan"], ["makanan"], ["kantin"], ["cerita"], ["drama"], ["kebun"], ["teh"], ["daerah"], 
        ["toko-toko"], ["buku"], ["sekolah"], ["bantuan"], ["keluarga"], ["latihan"], ["soft skill"], ["orang"], 
        ["bu"], ["pengeluaran"], ["bulan"], ["anak"], ["kampus"], ["ruangan"], ["catatan"], ["saat"], ["ayah"], 
        ["kantor"], ["tadi"], ["pagi"], ["barang"], ["tugas"], ["kelompok"], ["hari"], ["sabtu"], ["lalu"], ["orang"], 
        ["hal-hal"], ["politik"], ["kakak"], ["keponakan"], ["lapangan"], ["basket"], ["orang"], ["tuanya"], ["kecantikan"],
        ["seorang"], ["bidadari"], ["foto"], ["email"], ["kekurangan"], ["aplikasi"], ["baju"], ["dalam"], ["lemari"], ["adik"], 
        ["piring"], ["atas"], ["meja"], ["bukit"], ["kucing"], ["mobil"], ["dekat"], ["pabrik"], ["gadis"], ["jejaka"], ["balik"],
        ["jendela"], ["belakang"], ["luar"], ["rumah"], ["aktris"], ["layar"], ["penyakit"], ["tanaman"], ["kekeringan"], ["soal"], 
        ["nomor"], ["nenek"], ["tahun"], ["rapat"], ["awal pagi"], ["pernikahan"], ["kakak"], ["kantor"], ["bus"], ["penumpang"],
        ["paket"], ["rumah"], ["hutan"], ["tempat"], ["rumahnya"], ["bukit"], ["kakak"], ["ipar"], ["komplek"], ["mobilitas"],
        ["penduduk"], ["dataran"], ["paus"], ["hutan"], ["bakau"], ["selokan"], ["bencana"], ["banjir"], ["rutin"], ["pagi"], 
        ["hari"], ["mahasiswa"], ["koding"], ["seorang"], ["pemula"], ["produsen"], ["bahan-bahan"], ["kualitas"], ["mutu"],
        ["produk"], ["rasa"], ["peringatan"], ["larangan"], ["diri"], ["kemampuan"], ["keharusan"], ["fitur"], ["mode"], ["daya"],
        ["baterai"], ["adonan"], ["kue"], ["persatuan"], ["perpecahan"], ["tujuan"], ["perbaikan"], ["jalan"], ["toilet"], ["perut"],
        ["motor"], ["sekolah"], ["malam"], ["penjara"], ["hukum"], ["virus"], ["penyakit"], ["penularan"], ["simulasi"], ["bencana"], 
        ["alam"], ["masyarakat"], ["desa"], ["penghargaan"], ["kebersihan"], ["lingkungan"], ["tanaman"], ["pelajaran"], ["olahraga"], 
        ["ruangan"], ["hujan"], ["hari"], ["ibu"], ["pasar"], ["adik"], ["kijang"], ["gitar"], ["warga"], ["bakti"], ["udara"], ["pagi"],
        ["kancil"], ["pak"], ["tani"], ["timun"], ["keluarga"], ["anak-anak"], ["tablet"], ["air"], ["pintu"], ["pertandingan"], ["rekan"], 
        ["rektorat"], ["kuliah"], ["motor"], ["ulang tahun"], ["hal"], ["kehidupan"], ["semua"], ["murid"], ["ujian"], ["adik"], ["pesta"], 
        ["ulang tahun"], ["akhir semester"], ["pemikiran"], ["nilai"], ["pancasila"], ["para"], ["tamu"], ["ruangan"], ["sejalan"], ["vas"],
        ["bunga"], ["tanah"], ["liat"], ["janji manismu"], ["juara"], ["kelas"], ["suatu hari nanti"], ["teman"], ["lamanya"], ["capybara"], 
        ["tikus"], ["badai hujan"], ["pekan"], ["lalu"], ["pemuda"], ["kampung"], ["sebelah"], ["bapak"], ["guru"], ["sekolah"], ["orang"], 
        ["lain"], ["organisasi"], ["kampus"], ["tindakannya"], ["rumah"], ["kakaknya"], ["hidup"], ["donatur"], ["adiknya"], ["perkataan"],
        ["sejarah"], ["pendidikan"], ["kebutuhan dasar"], ["seorang"], ["anak"], ["kisah"], ["hidupnya"], ["ayah"], ["ustadz"], ["orang"], 
        ["tuanya"], ["pemimpin"], ["ekonomi"], ["dunia"], ["lenganku"], ["titanium"], ["alkohol"], ["zat"], ["kedudukan"], ["gubernur"], 
        ["setingkat"], ["menteri"], ["timnas"], ["rekan bisnisnya"], ["program"], ["pemberdayaan ekonomi"], ["masyarakat"], ["otonomi daerah"],
        ["minyak"], ["air"], ["siswa"], ["masalah"], ["produk"], ["milik"], ["tetanggaku"], ["peristiwa"], ["mata"], 
        ["kuliah"], ["modul"], ["pilihan"], ["kubuat"], ["negeri"], ["ayahnya"], ["kiamat"], ["kelompok"], ["dewa"], ["penjualan"], 
        ["strategi"], ["pemasaran"], ["nenek"], ["masa"], ["rapat"], ["karya"], ["tulis"], ["tema"], ["kucing"], ["perbuatannya"],
        ["seni"], ["music"], ["kebun"], ["nasib"], ["kakak"], ["pasar"], ["kakaknya"], ["paman"], ["hati"], ["laporan"], ["ketentuan"],
        ["pemuda"], ["penjahat"], ["sana"], ["pengunjung"], ["pacarku"], ["sd"], ["kursi"], ["merah"], ["sejajar"], ["meja"], ["lembaga"],
        ["negara"], ["lainnya"], ["baju"], ["bapak"], ["ibu"], ["ayam"], ["pintu"], ["guru"], ["olahraga"], ["adik"], ["meja"], ["pak"],
        ["tukang"], ["sepeda"], ["mobil"], ["paman"], ["ayah"], ["guru"], ["bayi"], ["seorang"], ["penculik"], ["santan"], ["daging"], 
        ["kelapa"], ["makanan"], ["sungai"], ["sampah"], ["jamu"], ["rempah"], ["kopi"], ["hitam"], ["gelas"], ["keramik"], ["tanaman"], 
        ["kakak"], ["alat"], ["musik"], ["pohon"], ["babi"], ["rambut"], ["tepung"], ["beras"], ["tas"], ["jaket"], ["bulu"], ["domba"], 
        ["gitar"], ["awetan"], ["kulit"], ["buaya"], ["kayu"], ["pertanyaan"], ["mobil"], ["sayur"], ["rumah"], ["tugas"], ["lukisan"], 
        ["orang"], ["bubur"], ["perbaikan"], ["penagihan"], ["kota"], ["polisi"], ["utang"], ["posisi"], ["tanah"], ["kedatangan"], 
        ["pencuri"], ["tahun"], ["pilihan"], ["sungai"], ["surat"], ["perpisahan"], ["taman"], ["mainan"], ["robot"], ["minggu"], 
        ["yoga"], ["gim"], ["online"], ["nama"], ["pemenang"], ["acara"], ["nasi festival"], ["tahunan"], ["siswa-siswa"], ["klasik"]
        ],
    "Verb": [["mulai"], ["membaca"], ["mengikuti"], ["bermain"], ["membuat"], ["menghadiri"], ["mengoleksi"], ["memberikan"],
            ["belajar"], ["membaca"], ["mengunjungi"], ["memasak"], ["menampilkan"], ["menyiapkan"], ["membawa"], ["merayakan"],
            ["mendengar"], ["melihat"], ["menelepon"], ["menyiapkan"], ["menulis"], ["membelikan"], ["memasaki"], ["meminjami"], 
            ["menawarkan"], ["memberitahukan"], ["menjanjikan"], ["menuduh"], ["menamai"], ["menobatkan"], ["menjahitkan"], ["membawakan"], 
            ["memanggil"], ["menyebutkan"], ["mencarikan"], ["menjelaskan"], ["membuatkan"], ["menggambar"], ["menulis"], ["mengajar"], 
            ["menonton"], ["makan"], ["menyimak"], ["melahirkan"], ["menari"], ["mengobrol"], ["bekerja"], ["bermain"], ["berjualan"],
            ["tertangkap"], ["melarikan"], ["merayakan"], ["berlatih"], ["melukis"], ["mencari"], ["berjumpa"], ["dilakukan"],
            ["mengucapkan"], ["menjadi"], ["mempersilakan"], ["masuk"], ["mengurung"], ["tutup"], ["dipukul"], ["diliburkan"], 
            ["dimainkan"], ["bernyanyi"], ["belajar"], ["disebabkan"], ["menyiram"], ["tinggal"], ["berjalan"], ["ditemukan"], 
            ["menabung"], ["menarik"], ["memikat"], ["pergi"], ["memiliki"], ["berlatih"], ["menonton"], ["mengunjungi"], ["pulang"],
            ["bermain"], ["menendang"], ["keluar"], ["bekerja"], ["berterimakasih"], ["membahas"], ["memberikan"], ["dilatih"], ["pergi"], 
            ["berterima-kasih"], ["mencatat"], ["datang"], ["bekerja"], ["merokok"], ["ditemukan"], ["menyentuh"], ["dibuat"], ["berangkat"],
            ["menangis"], ["tersedu-sedu"], ["paham"], ["mencari"], ["kerja"], ["berkunjung"], ["berlari"], ["berada"], ["bersikap"], ["kirim"], 
            ["berbicara"], ["meletakkan"], ["meloncat"], ["tinggal"], ["mengintip"], ["masuk"], ["duduk"], ["bersiap-siap"], ["masuk"], ["mati"],
            ["mengerjakan"], ["berjalan"], ["terpilih"], ["pindah"], ["ikut"], ["bertemu"], ["memiliki"], ["memutuskan"], ["pindah"], ["bekerja"], 
            ["sampai"], ["pulang"], ["membawa"], ["berada"], ["merupakan"], ["berharap"], ["berakhir"], ["terletak"], ["menginap"], ["pergi"],
            ["bermain"], ["terjebak"], ["dibersihkan"], ["mencegah"], ["bangun"], ["terasa"], ["memilih"], ["meningkatkan"], ["mengatasi"],
            ["sengaja"], ["diletakkan"], ["digunakan"], ["menghemat"], ["diperlukan"], ["membuat"], ["senantiasa"], ["dijaga"], ["menghindari"], 
            ["bekerja"], ["sama"], ["tercapai"], ["ditutup"], ["mempercepat"], ["sakit"], ["terluka"], ["jatuh"], ["pura-pura"], ["pergi"], 
            ["dimarahi"], ["pulang"], ["masuk"], ["melanggar"], ["mengurangi"], ["bepergian"], ["mencegah"], ["mengikuti"], ["diperbaiki"], 
            ["menjaga"], ["mendapatkan"], ["tumbuh"], ["dirawat"], ["dilakukan"], ["berlari"], ["berteriak"], ["bernyanyi"], ["memainkan"], 
            ["bekerja"], ["menikmati"], ["berolahraga"], ["mencuri"], ["bersama"], ["tertarik"], ["minum"], ["digedornya"], ["berteriak"], 
            ["berjalan"], ["berangkat"], ["dituntut"], ["sengaja"], ["dipesan"], ["bernyanyi"], ["bunuh"], ["berbahasa"], ["bepergian"], 
            ["tinggal"], ["bermain"], ["berkhotbah"], ["datang"], ["berdiskusi"], ["dipersilahkan"], ["memasuki"], ["terbuat"], ["terkenang"],
            ["menjadi"], ["berjumpa"], ["sengaja"], ["bertemu"], ["serupa"], ["terjadi"], ["datang"], ["berangkat"], ["bergantung"], ["keluar"], 
            ["menyesal"], ["berdamai"], ["mengeluh"], ["berlawanan"], ["tergolong"], ["bercerita"], ["berdiskusi"], ["terbuat"], ["berhadapan"], 
            ["bertemu"], ["siap"], ["bisa"], ["terdiri"], ["ditentukan"], ["pergi"], ["pulang"], ["duduk"], ["disusun"], ["disetrika"], ["dimasak"],
            ["dibuka"], ["belajar"], ["dipasang"], ["mengendarai"], ["diajarkan"], ["dimarahi"], ["dibuang"], ["dibersihkan"], ["disiram"], ["ditarik"], 
            ["guling"], ["merupakan"], ["adalah"], ["ditanam"], ["berdebat"], ["bercerita"], ["menjawab"], ["mengetahui"], ["mempertanyakan"], ["didorong"],
            ["mogok"], ["membangkang"], ["bergurau"], ["dilukis"], ["berdiskusi"], ["menjelaskan"], ["menyangkul"], ["berasal"], ["berbelanja"], ["pergi"], 
            ["terkena"], ["tidur"], ["terbuat"], ["dibuat"], ["menghadiri"], ["mempersiapkan"], ["teringat"], ["mempunyai"], ["makan"], ["mengirimkan"], 
            ["membeli"], ["goreng"], ["lukis"], ["tampil"], ["mendengarkan"]
    ],
    "Adv": [["masih"], ["akan"], ["sangat"], ["sudah"], ["pernah"], ["sungguh-sungguh"], ["belum"], 
            ["sedang"], ["harus"], ["jarang"], ["akan"], ["sangat"], ["sedang"], ["baru"], ["saja"], 
            ["sudah"], ["tidak"], ["boleh"], ["belum"], ["sekali"], ["tentu"], ["harus"], ["sering"], 
            ["hampir"], ["selalu"], ["juga"], ["sedang"], ["sudah"], ["baru"], ["saja"], ["selalu"], 
            ["masih"], ["lebih"], ["sebelah"], ["secara"], ["bukan"], ["dengan"], ["harus"], ["sering"], 
            ["larut"], ["tidak"], ["jarang"], ["sambil"], ["terus"], ["bersama"], ["bisa"], ["sangat"],
            ["sengaja"], ["sering"], ["tidak"], ["pertamakalinya"], ["pasti"], ["sudah"], ["sangat"], 
            ["belum"], ["jarang"], ["masih"], ["beberapa"], ["kali"], ["harus"], ["akan"], ["selalu"], 
            ["sedang"], ["telah"], ["ingin"], ["tidak"], ["sedang"], ["baru"], ["saja"], ["sudah"], ["selalu"], ["sering"], ["telah"], ["sekarang"]
    ],
    "Adj": [["suka"], ["rajin"], ["senang"], ["indah"], ["baru"], ["merah"], ["hijau"], ["sering"], ["palsu"], 
            ["lucu"], ["miskin"], ["mewah"], ["pendek"], ["baru"], ["muda"], ["tradisional"], ["demam"], ["luang"], 
            ["pasti"], ["serius"], ["dini"], ["sepi"], ["baik"], ["keras"], ["takut"], ["enak"], ["menarik"], ["ramah"], 
            ["indah"], ["lengkap"], ["penting"], ["keras"], ["mandiri"], ["kecil"], ["baru"], ["hormat"], ["sendiri"], 
            ["mudah"], ["terkenal"], ["asing"], ["sulit"], ["tinggi"], ["malas"], ["panik"], ["macet"], ["subur"], ["baik"], 
            ["lincah"], ["lantang"], ["semangat"], ["cerdik"], ["seru"], ["kotor"], ["terbersih"], ["rendah"], ["hemat"], 
            ["sakit"], ["lapar"], ["ramai"], ["tenang"], ["malas"], ["adiktif"], ["terdahulu"], ["pahit"], ["sedikit"], ["senang"],
            ["gembira"], ["sesuai"], ["dulu"], ["malang"], ["cantik"], ["akustik"], ["ringan"], ["sembelit"], ["senang"], ["suka"], ["berwarna"], ["merah"]
    ],
    "PropNoun": [["dinda"], ["rini"], ["budi"], ["sinta"], ["irfan"], ["ani"], ["maya"], ["adit"], ["dian"], 
                ["fitri"], ["agung"], ["krisna"], ["putra"], ["adi"], ["renata"], ["bagas"], ["putri"], ["dinda"],
                ["ardi"], ["sekar"], ["abi"], ["anton"], ["riski"], ["bagas"], ["bayu"], ["juna"], ["Kevin"], ["Bali"],
                ["Manado"], ["Albert"], ["Desi"], ["Yudi"], ["Jakarta"], ["Abdi"], ["Ata"], ["Jalan"], ["Jimbaran"],
                ["Denpasar"], ["Bintang"], ["Putu"], ["Ronaldo"], ["Widya"], ["Wulan"], ["Made"], ["Puncak"], ["Bogor"], 
                ["Kota"], ["Yogyakarta"], ["Irma"], ["Ana"], ["Anto"], ["Budi"], ["Amerika"], ["Nyoman"], ["Bandung"], 
                ["Dokter"], ["Cahya"], ["LA"], ["Rumah"], ["Sakit"], ["Bali"], ["Mandara"], ["Bandara"], ["Ngurah"], 
                ["Rai"], ["Bali"], ["Jimbaran"], ["Aokigahara"], ["Jepang"], ["Ryujin"], ["Senin"], ["Jurusan"], ["Informatika"], 
                ["Universitas"], ["Udayana"], ["Tepung"], ["Terigu"], ["Anna"], ["Budi"], ["Andi"], ["Burhan"], ["Wayan"], ["Desa"], 
                ["Penglipuran"], ["Bali"], ["Bu"], ["Indah"], ["Arkeologi"], ["Inggris"], ["Beni"], ["Budi"], ["Agung"], ["Andre"], 
                ["Vema"], ["Anti"], ["Amel"], ["Rin"], ["Diana"], ["Andi"], ["Bandung"], ["Pinnochio"], ["Moana"], ["Kerobokan"], 
                ["Indonesia"], ["Malaysia"], ["Elon"], ["Musk"], ["Madan"], ["Surtr"], ["Sinmara"], ["Kratos"], ["Yunani"], ["Tasya"], 
                ["Thor"], ["Jormungandr"], ["Heimdall"], ["Aesir"], ["Adi"], ["Figo"], ["Alit"], ["Mona"], ["Brian"], ["Garry"], ["Bara"], 
                ["Susan"], ["Jimbaran"], ["Risa"], ["Ani"], ["Widia"], ["Alit"], ["Susan"], ["Sasando"], ["Sumping"], ["Rendang"], ["Nusa"],
                ["Tenggara"], ["Timur"], ["Genggong"], ["Sumatera"], ["Selatan"], ["Lombok"], ["Louis"], ["Vuitton"], ["Taksa"], ["Pinus"], 
                ["Dian"], ["Putu"], ["Rido"], ["Jovan"], ["Mamat"], ["Gita"], ["Ketut"], ["Dhimmas"], ["Adi"], ["Jeni"], ["Malaysia"], ["Tampak"], 
                ["Siring"], ["Gianyar"], ["Indonesia"], ["Leonardo"], ["da"], ["Vinci"], ["Perang"], ["Dunia"], ["II"], ["Intan"], ["Pak"], ["Edi"], 
                ["Beni"], ["Pak"], ["Arif"], ["Rani"], ["Anton"]
    ],
    "Prep": [["ke"], ["demi"], ["pada"], ["hingga"], ["atas"], ["di"], ["dari"], ["kepada"], ["para"], ["oleh"], ["karena"], ["dengan"], 
            ["dalam"], ["seperti"], ["sampai"], ["berkat"], ["terhadap"], ["tentang"], ["bagi"], ["ke"], ["atas"], ["bagi"], ["dalam"], 
            ["dari"], ["demi"], ["di"], ["hingga"], ["oleh"], ["pada"], ["sampai"], ["sejak"], ["tentang"], ["bersama"], ["beserta"],
            ["menuju"], ["terhadap"], ["bagaikan"], ["melalui"], ["mengenai"], ["karena"], ["sebab"], ["selain"], ["dengan"], ["ke"], 
            ["dari"], ["di"], ["antara"], ["pada"], ["bagi"], ["guna"], ["agar"], ["sebab"], ["sehingga"], ["karena"], ["di"], ["tentang"], 
            ["saat"], ["ke"], ["dengan"], ["untuk"], ["dari"], ["atas"], ["pada"], ["dalam"], ["sebelum"], ["setelah"], ["kepada"], ["oleh"], 
            ["pada"], ["karena"], ["hingga"], ["sampai"], ["sejak"], ["semenjak"], ["menjelang"], ["dari"], ["tentang"], ["mengenai"], ["ketika"], ["kemarin"], ["besok"], ["setiap"]
    ],
    "Pel": [["Adj", "Adj"], ["Adj", "Noun"]],
    "Ket": [["Prep", "NP"], ["Adv", "Noun"], ["Prep", "Noun"], ["kemarin"], ["besok"], ["lusa"]],
    "NP": [["NP", "Noun"], ["NP", "PropNoun"], ["NP", "Pronoun"], ["NP", "Noun"], ["NP", "Adj"], ["NP", "Adv"], ["Noun", "NP"], ["NP", "Adj"], ["Noun", "Adj"], ["Noun", "Pronoun"], ["Noun", "Verb"], ["Noun", "Noun"], ["Verb", "NP"]],
    "VP": [["VP", "Adj"], ["VP", "Adv"], ["Adj", "VP"], ["Adv", "VP"], ["Adv", "AdvP"],["Adj","P"]],
    "PP": [["Prep", "NP"], ["Prep", "VP"], ["Prep", "AdjP"], ["Prep", "AdvP"], ["Num", "NP"]],
    "AdjP": [["Adv", "AdjP"], ["Noun", "AdjP"]],
    "AdvP": [["Adv", "AdvP"], ["Adv", "Verb"]],
    "NumP": [["Num", "NumP"]]
}