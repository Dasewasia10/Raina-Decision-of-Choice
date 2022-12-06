label adventurer_adegan_prolog:
        
    $ quick_menu = True
    
    show bg pantai with fade 
    play sound air_laut fadein 1.0 fadeout 1.0
    """...

    Pantai?

    Ah iya. Aku ke sini karena para pedagang itu.

    Aku mengambil misi untuk mengawal mereka selama berada di pulau sini.

    Misi? 

    Memangnya untuk apa? Apa ada masalah di sini?

    Ah, lupakan, lupakan.{w} Ada ingatan aneh yang masuk lagi.

    Lagian tidak mungkin aku lupa.{w} Misi ini diadakan karena ada laporan munculnya sosok aneh di dekat bibir pantai.

    Oke, sip.{w} Jadi, aku mesti ke arah mana dulu?
    """

    menu:
        "Kanan":
            jump masa_lalu_prolog_kanan
        "Kiri":
            jump masa_lalu_prolog_kiri

    label masa_lalu_prolog_kanan:
        show bg pantai with dissolve

        play music hari_senang fadein 0.5 fadeout 0.5

        play sound people fadein 0.5 fadeout 0.5

        """Okelah, aku akan langsung mendatangi mereka dulu.

        Tampaknya rame, juga.

        Oh iya, mungkin aku bisa dapat beberapa barang bagus.

        Lumayan.

        ...

        ....

        .....
        """

        show bg pantai with fade
        """
        Ah, waktunya istirahat. 

	    Jalan-jalan sebentar, lah.
        """
        
        jump masa_lalu_prolog
        
    label masa_lalu_prolog_kiri:
        show bg pantai with dissolve
        """Oh, okelah. 

        Kayaknya mereka bakal aman-aman saja.

        Aku berkeliling saja, kalau gitu.
        """
        
        stop sound 

        jump masa_lalu_prolog
        
    label masa_lalu_prolog:

        stop music
        
        play sound air_laut fadein 1.0 fadeout 1.0

        """...

        ....

        Hm. Sepertinya ada sesuatu di sana.

        Tampaknya di sana ada sesuatu.

        ...
        
        ....
        
        Eh?

        Tunggu sebentar. Siapa di sana?
        """

        show cg mm_raina_masa_lalu with fade

        play music hari_senang fadein 0.5 fadeout 0.5
        
        r happy4_little "Hmm, hmm..."
        p "Perempuan?"
        
        """Dia sedang bersenandung dengan tenang, sembari terbaring di atas air laut di tepi pantai.
        
        Wajahnya asing. Apa dia ikut rombongan pedagang di sana?
        
        Kalau iya, kenapa dia malah ada di sini?
        
        Sendirian, pula.
        """

        r neutral "Oh, ternyata ada orang."
        r "Sedang apa di sini?"
        p "Itukan pertanyaanku."
        r happy6 "Ah, benar juga."
        r teehee "Hehe, seperti yang kau lihat, aku sedang menikmati alam."
        "Dengan berendam di air asin begitu?"
        r happy3_little "Air lautnya hangat.{w} Tidak dingin.{w} Tidak panas.{w} Sangat nyaman."
        r "Apalagi kalau sekalian berjemur di bawah sinar matahari yang hangat."
        r smirk "Hehe."
        p "..."
        p "Perempuan aneh."
        r confused "Eh, jahat sekali mulutnya sama orang yang baru ditemui."
        p "Bukan masalah buatku."
        r happy2_little "Hmm."
        "Kenapa dia menatapku begitu?"
        r "Tampaknya kau cowok yang bisa bikin cewek nangis cuman dari ngomong doang."
        p "Maksud?"
        r smirk_little "Heh."
        "Kok tahu-tahu nih perempuan jadi ngeselin, ya?"
        r neutral "Ucapan dingin begitu, masih tidak sadar, rupanya."
        p "Kenapa malah ngurusin cara ngomongku?"
        r happy "Nah, itu!"
        r "Kalo bukan aku, cewek biasa bakal lari ketakutan."
        r happy4 "Aku jadi kasihan sama cewek-cewek di desa sini."
        "Malah makin sewot."
        "Tenang, tenang. Jangan sampai buat keributan tak penting di sini."
        p "Lupakan itu. Kau mending segera naik ke pantai."
        r confused "Kenapa?"
        p "Di situ banyak bulu babi."
        hide cg mm_raina_masa_lalu

        play music keadaan_genting fadein 0.5 fadeout 0.5
        
        show raina_masa_lalu scared at sprite_karakter
        r "EH?!"
        "Dia langsung terlompat dari posisinya dan langsung pergi ke daerah pantai yang tak terkena air laut."
        "Yah, tampaknya tak perlu waktu lama buat dia menyadarinya."
        
        show raina_masa_lalu noclue_little
        r "Tunggu dulu."
        r "Bulu babi kan tinggalnya di terumbu karang. Mana ada terumbu karang di sini."
        p "Baru sadar, toh."
        r "!"
        
        show raina_masa_lalu angry_soft
        r "Kurang ajar! Jahat!"
        p "Hahahahaha!"
        p "Balasan dariku."
        stop music
        
        show raina_masa_lalu angry_shy
        """Dia masih menatapku dengan sangat kesal.
        
        Tampaknya dia tidak lupa kalau pakaiannya basah semua.
        
        Karena tepat setelah dia mengumpat, dia berlari ke batu terdekat yang sudah ada handuk tebal dan pakaian ganti di atasnya.
        
        Ternyata dia tidak sekedar berendam tanpa mikir sebelumnya.
        
        Lalu dia kembali menatapku dengan kesal.
        """

        play music hari_senang fadein 0.5 fadeout 0.5

        show raina_masa_lalu shy2_half
        r "Apa kau keberatan?"
        p "Ah, maaf. Aku balik ke rombongan di sana, kalo gitu."
        hide raina_masa_lalu
        
        "Aku tahu dengan sangat kode yang barusan, jadi aku segera pergi dari sana dan kembali."
        "..."
        "...."
        p "Ternyata masih rame juga di sini."
        p "Tidak mengherankan dari pedagang terkenal."
        mn "Makasih pujiannya, bang!"
        mn "Tapi karena kau laki, aku gak bakal kasih bonus."
        p "Ck."
        fn "Aku kembali."
        mn "Oh, kerja bagus. Jadi gimana?"
        fn "Yah, Pak kades bilang boleh-boleh aja, sih."
        fn "Tapi beliau bilang pengen liat dulu orangnya kayak gimana."
        mn "Hadeh."
        mn "Kemana pula dia sekarang?"
        fn "Paling berendam di bagian laut agak jauh dari sini. Macam gak tahu aja."
        "Berendam di laut?"
        p "Yang kalian cari perempuan?"
        mn "Wah, hebat juga kau tahu."
        
        pause 0.5
        mn "Tunggu."
        "?"
        mn "Kalo aku gak salah lihat, kau dari arah sana."
        mn "Jadi kau lihat orangnya?"
        p "Aku bahkan ngajak ngobrol dia."
        p "Tapi dianya malah ngajak ribut."
        mn "Ah."
        fn "Ah, itu orangnya."
        p "Jadi beneran dia, ya?"
        mn "Ya, gitulah."
        fn "Kalo gitu, boleh minta tolong kasih tahu di mana dia sekarang?"
        p "Boleh sih. Tapi-"
        
        show raina_masa_lalu smirk at sprite_karakter
        r "Gak perlu nyari."
        fn "Lah, orangnya muncul."
        mn "Kau ini. Bukannya bantu-bantu malah ngilang."
        
        show raina_masa_lalu teehee_little
        r "Ehehe, maaf."
        mn "Padahal ini terakhir kali kau di sini."
        
        "?"
        
        r "Ah, jadi habis dari tempatnya pak kades, ya?"
        
        fn "Gitulah."
        
        "??"
        
        r "Kau di situ. Kenapa malah jadi bingung sendiri?"
        
        p "Ah, itu..."
        
        p "Aku gak nangkap kalian ngomongin apa."
        
        r "Owalah, kirain apa."
        
        mn "Kalau begitu, aku saja yang beritahu."
        
        mn "Dia ini, mulai hari ini bakal tinggal di desa ini."
        
        $ raina_name = "Raina"
        
        p "Eh?"
        
        r "Jadi, begitulah."
        
        r "Ehehe."
        hide raina_masa_lalu
        
        show bg langit with dissolve
        """Setelah itu, dia beserta beberapa orang dari rombongan pedagang sebelumnya mendatangi tempat pak kades.
        
        Entah kenapa mereka juga membawaku, dengan alasan pak kades memang memanggilku. Itu menurut informasi dari perempuan yang mendatangi pak kades sebelumnya.
        
        Perbincangan pun dilakukan, membahas bagaimana Raina akan tinggal, seperti di mana dia tinggal, yang mengurus, dll.
        
        Pak kades secara sepihak menawarkan tempatku untuk itu, dengan alasan kami berdua sudah tampak akrab.
        
        Darimananya?
        
        Lagi, alasannya juga karena rumahku cukup luas dan aku tinggal sendiri, jadi masih bisa kalau ditambah satu anggota lagi.
        
        Kok gitu alasannya.
        
        Niatnya mau menolak, tapi mereka yang dari rombongan memaksaku.

        Dan tebak aku memilih apa?
        """
        
        menu:
            "Membiarkannya tinggal di tempatku.":
                call adding_one( "Bond", + 2 ) from _call_adding_one_8
                $ tinggal_seatap = True
                "Yah, melakukan itu tidak merugikanku sama sekali, sih."
            "Meminta dia tinggal di rumah bibi sebelah tempat tinggalku.":
                call adding_one( "Bond", - 1 ) from _call_adding_one_9
                "Mau aku tinggal sendiri, bukan berarti aku bisa asal ajak perempuan tinggal seatap denganku."
                "Mikir dikit lah, pak kades."
                
        """Dengan begitu, keputusan telah ditetapkan.
        
        Dan mulai dari hari ini, Raina resmi tinggal di desa.
        
        Ada banyak yang terjadi setelahnya, tapi mari kita simpan itu untuk nanti.
        
        Lalu, sudah satu tahun sejak kedatangan Raina.
        """
        
        stop music

        stop sound

        call adding( "Trust" , + 10) from _call_adding # Kepercayaan

        pause 0.3

        call adding( "Bond" , + 7 ) from _call_adding_1 # Ikatan/Kedekatan

        pause 0.3

        call adding( "Knowledge" , + 10) from _call_adding_2 # Pengetahuan akan MC

        pause 0.3

        call adding( "Interest" , + 12) from _call_adding_3 # Ketertarikan
                    
        jump adventurer_adegan001

label adventurer_adegan001:
    show screen control()
    show screen stat_box()
    
    show bg r_utama with fade
    
    play sound bird_chirping loop fadein 1.0 fadeout 1.0 

    play music hari_senang fadein 0.5 fadeout 0.5
        
    "..."
    
    "Hari ini mesti ke balai kota, lalu setelahnya..."
    
    "Hmm..."
    
    play sound masak loop fadein 0.5 fadeout 0.5
    show raina_masa_lalu happy4_little at sprite_karakter
    
    p "Raina?"
    
    show raina_masa_lalu neutral
    r "Ya? Kenapa, [player!t]?"
    
    p "Jangan lupa kita mesti ke balai kota habis ini!"
    
    r "Ah, iya."
    hide raina_masa_lalu
    
    """Raina masih cantik dan imut seperti biasa.
    
    Dia juga rajin.{w} Saking rajinnya, dia tiap hari bangun pagi buatin sarapan.
    
    Harusnya dia gak usah repot-repot begitu.
    
    Tapi tiap kita bilang itu kepadanya,{w} dia bersikeras melakukannya sebagai balas budi.
    
    Padahal aku tidak melakukan apa-apa, malah bibi seberang rumah yang mestinya jauh lebih dia balas budi.
    
    Ngomong-ngomong, sudah setahun sejak dia datang ke desa ini.
    """
    
    show raina_masa_lalu happy6 at sprite_karakter
    r "Oiya, [player!t]."
    p "?"
    
    show raina_masa_lalu neutral
    r "Hari ini kita mesti pergi ke balai kota, kan?"
    p "Iya. Memangnya kenapa?"
    
    show raina_masa_lalu happy5_little
    r "Gapapa. Takut lupa aja."
    
    stop sound
    
    show raina_masa_lalu blink
    r "Oke, sarapan dah jadi."
    p "Iya!"
    hide raina_masa_lalu
    
    "Sembari menyiapkan makanan, aku membantu menyiapkan tempat makan di tengah ruangan."
    "Setelahnya, kita duduk lesehan di hadapan makanan yang baru selesai dimasak."
    
    "Makanannya enak."
    "Mencium baunya saja sudah nagih."
    "Kita pun makan.{w} Makanannya memang sangat enak, aku sampai melahapnya dengan mantap."
    
    show raina_masa_lalu geli at sprite_karakter
    "Aku juga bisa melihatnya tertawa kecil."
    hide raina_masa_lalu
    
    "...{p}...."
    hide bg r_utama with dissolve 
    
    pause 0.7 
    
    show bg r_utama with dissolve 
    
    show raina_masa_lalu happy at sprite_karakter
    r "Oke, biar aku aja yang bersihkan mejanya. Kau pergi siap-siap aja."
    
    show raina_masa_lalu smirk_little
    r "Nanti misinya keburu diambil orang."
    p "Iya, iya."
    
    hide raina_masa_lalu

    hide bg r_utama with dissolve

    pause 0.7
    
    show bg d_rumah with dissolve 
    
    pause 0.3
    
    show raina_masa_lalu neutral at sprite_karakter with dissolve
    r "Ayo, [player!t]!"
    hide raina_masa_lalu
    
    hide bg d_rumah with dissolve

    pause 1.0

    stop music

    show bg balai_kota with dissolve

    play sound people
    
    show raina_masa_lalu ouch_little at sprite_karakter with dissolve

    play music hari_senang2 fadein 0.5 fadeout 0.5
        
    r "Akhirnya sampai juga."
    
    show raina_masa_lalu neutral
    r "Ayo, kita liat bilah pengumuman di situ."
    hide raina_masa_lalu with dissolve
    
    "Rame sekali, tidak seperti biasanya."
    
    "Tampaknya lagi banyak yang pengen ngambil misi."

    show raina_masa_lalu confused at sprite_karakter with dissolve 
    r "Hmm..."
    p "Sudah ketemu misi yang bagus, kah?"
    r "Sudah, sih.{w} Tapi aku bingung mesti milih yang mana."
    r "Bantuin, dong!"
    p "Okelah."
    
    ## Penentu arah cerita dimulai dari sini
    label memilih_misi_penting:
        menu:
            "Menyelidiki pantai":
                jump menyelidiki_pantai
            "Mengumpulkan material":
                jump mengumpulkan_material
            # "Menjelajahi reruntuhan":
            #     jump menjelajahi_reruntuhan
    
    label menyelidiki_pantai:
        call adding( "Trust" , -1) from _call_adding_4 # Kepercayaan
        
        pause 0.3
        
        call adding( "Bond" , +2 ) from _call_adding_5 # Ikatan/Kedekatan
        
        pause 0.3
        
        call adding( "Knowledge" , +1) from _call_adding_6 # Pengetahuan akan MC
        
        pause 0.3
        
        call adding( "Interest" , +5) from _call_adding_7 # Ketertarikan
        
        show raina_masa_lalu happy
        r "Pilihan bagus."
        r "Hari ini panas banget, juga."
        r "Aku pergi ke resepsionis, kalo gitu."
        
        jump adventurer_adegan002_menyelidiki_pantai
        
    label mengumpulkan_material:

        call adding( "Bond" , +1) from _call_adding_8 # Ikatan/Kedekatan
        
        pause 0.3
        
        call adding( "Knowledge" , +2) from _call_adding_9 # Pengetahuan akan MC
        
        pause 0.3
        
        call adding( "Interest" , -2) from _call_adding_10 # Ketertarikan
        
        show raina_masa_lalu happy2 at sprite_karakter
        r "Ah, boleh-boleh aja sih."
        r "Di hutan juga keknya lagi adem."
        r "Ayo kita ambil." 
        
        jump adventurer_adegan002_mengumpulkan_material
        

label adventurer_adegan002_menyelidiki_pantai:
    stop music

    hide raina_masa_lalu with dissolve
    
    pause 1.5
    
    show raina_masa_lalu neutral at sprite_karakter with dissolve
    r "Oke, misi kita sudah terdaftar."
    
    show raina_masa_lalu blink
    r "Ayo, cepat pulang."
    r "Kita mesti siap-siap."
    hide raina_masa_lalu with dissolve
    
    """Bersemangat sekali.
    
    Dia memang suka pantai sih.
    
    Setelahnya, kami kembali ke rumah, lalu mengambil beberapa perlengkapan.
    """
    
    stop sound 
    
    show bg d_rumah with dissolve
    
    show bg r_utama with dissolve

    play music hari_senang2 fadein 0.5 fadeout 0.5
        
    "Hmm, aku akan membawa tombak dan pedangku, untuk berjaga-jaga."
    "Lalu untuk jaring, pisau, karung, dan lain-lain.{w} Hmm..."
    "Kuserahkan ke Raina saja."
    
    show raina_masa_lalu confused at sprite_karakter
    "..."
    p "Ada apa, Raina?"
    
    show raina_masa_lalu btm at sprite_karakter
    r "Ah, enggak. Cuman bingung mesti bawa {i}potion{/i} apa."
    p "Sangat terlihat."
    r neutral "Ne, bantuin milih, dong!"
    
    p "Eh. Kenapa gak milih sendiri?"

    show raina_masa_lalu teehee at sprite_karakter
    r "Kan aku bingung."
    
    show raina_masa_lalu neutral
    p "Okelah, kupilihkan."
    
    show raina_masa_lalu smirk_little
    r "Yeay!"
    
    ## Menu memilih potion, akan dipakai berulang kali
    call potion_coiching from _call_potion_coiching
    
    jump adventurer_adegan003_menyelidiki_pantai
        
label adventurer_adegan003_menyelidiki_pantai:
    show bg d_rumah with dissolve
    
    hide raina_masa_lalu with dissolve
    
    show raina_masa_lalu neutral at sprite_karakter with dissolve
    p "Kau dah siap, belum?"
    r "Dah."
    
    show raina_masa_lalu smirk2_little
    r "Yok!"
    
    hide raina_masa_lalu
    
    show bg hutan with dissolve
    """Kita pun berangkat ke lokasi.
    
    Tempatnya tidak begitu jauh, namun perlu waktu perjalanan yang cukup lama.
    
    Cuacanya memang panas, tapi udaranya tetap terasa sejuk ketika sudah sampai di dalam daerah hutan.
    """
    
    show cg masa_lalu_1 with flash

    play music happy_ending fadein 0.5 fadeout 0.5
        
    p "Raina?"
    r neutral "Kenapa, [player]?"
    p "Ah, enggak."
    p "Cuman kepikiran, pas kau pertama kali ke desa ini."
    r happy "Ah, pas itu, ya."
    r happy4 "Jadi keingat juga."
    r shy2 "Jahat sekali kau pas itu."
    p "Eh."
    p "Benar juga. Tolong lupakan."
    r smirk_little "Gak mau."
    r "Lagian, pas itu juga kau-"
    hide cg masa_lalu_1 with dissolve
    
    show raina_masa_lalu happy6 at sprite_karakter with dissolve
    r "Ah."
    r "Ayo cepat. Keburu gelap."
    p "Ah iya. Okeoke."
    hide raina_masa_lalu with dissolve
    
    hide bg hutan
    
    stop music

    pause 0.7
    
    show bg pantai with dissolve

    show raina_masa_lalu happy2 at sprite_karakter with dissolve

    play sound air_laut fadein 1.0 fadeout 1.0

    play music hari_senang2 fadein 0.5 fadeout 0.5

    r "Wah, akhirnya sampai!"
    p "Iyah." 

    hide raina_masa_lalu
    """
    Pasirnya masih hangat-hangat panas, udaranya masih segar, bau laut yang terasa asin.

    Cukup jarang buat ke sini, selain karena jauh, juga karena aku sudah disibukkan dengan kegiatan di desa.
    """
    
    show raina_masa_lalu happy at sprite_karakter with dissolve
    p "Waktunya kita patroli."
    r "Ayo!"

    hide raina_masa_lalu
    """
    Kami memulai penelusuran dari sisi Barat pantai. 

    Titik yang kami ambil adalah titik yang sama ketika para pedagang yang membawa Raina datang setahun yang lalu.

    Kami mengecek mulai dari keadaan pasir, udara, air laut, dan sebagainya.

    Kami juga mengecek apakah ada benda-benda aneh yang muncul.

    Kalau ada pertanyaan mengapa sampai ada misi seperti ini, itu karena sejak 5 tahun yang lalu ada berbagai keanehan yang terjadi pada desa ini.

    Namun detailnya tidak bisa kuungkap lebih lanjut, karena aku juga kurang tahu.
    
    Kami terus menelusuri menuju arah Timur pantai, hingga kami berhenti untuk istirahat di dekat sebuah batu besar di bibir pantai.
    """

    show raina_masa_lalu neutral at sprite_karakter with dissolve
    p "Kita istirahat aja dulu."
    r "Oke."
    
    hide raina_masa_lalu
    "..."
    "...."

    show raina_masa_lalu neutral at sprite_karakter with dissolve

    stop music

    r "Hey, [player!t]."
    p "Apa?"
    r "Aku penasaran, apa kau punya keinginan atau semacamnya?"
    p "Kenapa tiba-tiba nanya begitu?"
    r happy6 "Yah, gak ada apa-apa, sih."
    r happy5 "Cuman penasaran aja."
    p "Hmm"
    
    """Keinginan? Bisa dibilang, sudah cukup lama aku berada di desa ini. 
    
    Sudah sejak lahir, lebih tepatnya.

    Orang tuaku juga sudah tidak ada.

    Selain menjadi berguna buat desa, tidak ada hal lain yang ingin kulakukan.

    Tetapi sejak aku bertemu dengannya, aku sepertinya telah menemukan jawabannya.

    Apa yang harus kubalas? 
    
    Apa aku perlu mengatakannya sekarang?
    """

    menu:
        "Aku menyukaimu.":
            jump adventurer_adegan004_menyelidiki_pantai_romanceroute
        "Ingat mendiang.":
            jump adventurer_adegan004_menyelidiki_pantai_adventureroute
    
    label adventurer_adegan004_menyelidiki_pantai_romanceroute:
        p "Sebenarnya, aku pengen mengatakan sesuatu kepadamu."

        show raina_masa_lalu confused at sprite_karakter
        r "Kenapa tiba-tiba?"
        p "Aku...{w} Menyukaimu."
        r "..."

        show raina_masa_lalu shy2_half
        r "Eh?!"
        r "Sejak kapan?"
        p "Mungkin, sekitar setengah tahun belakangan ini."

        show raina_masa_lalu shy_little
        r "O-Oke."
        p "Dan aku ingin kalau kita {w}menjalin status di atas berteman."
        p "Setidaknya itulah, {w}keinginanku."

        show raina_masa_lalu noclue_little
        r "Eh, begitu?"
        r "Hmm"

        hide raina_masa_lalu
        "Dia tampak sedang berpikir keras."
        "Apa aku memang terlalu tiba-tiba?"

        show raina_masa_lalu happy4_little at sprite_karakter with dissolve

        play music happy_ending fadein 0.5 fadeout 0.5
        
        r "Fufu"

        show raina_masa_lalu happy3_little
        r "I'm in your care."
        p "Eh?"
        r "Maksudnya, aku akan menerima permintaanmu."

        if Bond > 20:
            scene cg masa_lalu_2 with flash
        r "Mohon bantuannya, [player!t]!"

        """Lalu semenjak hari itu, aku dan Raina berpacaran.
        
        Dia juga tampak senang.

        Syukurlah.

        Setelahnya, kami langsung kembali ke balai kota.
        """

        call adding( "Trust" , + 9) from _call_adding_11 # Kepercayaan

        pause 0.3

        call adding( "Bond" , + 15) from _call_adding_12 # Ikatan/Kedekatan

        pause 0.3

        call adding( "Knowledge" , + 2) from _call_adding_13 # Pengetahuan akan MC

        pause 0.3

        call adding( "Interest" , + 7) from _call_adding_14 # Ketertarikan

        if Bond > 20:
            hide cg masa_lalu_2 with flash

        jump masa_lalu_epilog

    label adventurer_adegan004_menyelidiki_pantai_adventureroute:
        p "Sebenarnya. Aku ingin menjadi penjaga garis pantai."

        show raina_masa_lalu confused at sprite_karakter
        r "Penjaga garis pantai?"
        p "Iyah."
        r "Apa aku boleh tahu alasannya?"
        p "Itu pekerjaan ayahku dulu."

        show raina_masa_lalu shock_little
        r "Ah."

        show raina_masa_lalu shy2

        play music flashback fadein 0.5 fadeout 0.5
        
        r "Itu..."

        show raina_masa_lalu happy5
        r "Maaf."
        p "Tak apa. Lagipula itu sudah lama, juga."
        p "Ayah sangat gagah saat itu, walau yang dia lawan sangat sulit untuk dikalahkan."

        show raina_masa_lalu neutral
        p "Yah, lawannya mundur sih, tapi ayah sudah tidak tertolong."
        p "Aku jelas bersedih saat itu, tapi aku juga jadi bertekad untuk meneruskan kerjaan ayah."
        p "Aku masih 12 tahun saat itu, jadi mungkin aku masih tampak kekanak-kanakan saat mengatakannya pada ibu."
        r "Ibumu..."
        p "Ah, ibu meninggal beberapa bulan setelahnya."
        p "Tubuhnya memang tidak sehat sejak lama, sih."

        show raina_masa_lalu sad_little
        p "Sejak saat itu, aku diasuh oleh bibi yang merawatmu sekarang hingga aku sanggup tinggal sendiri."
        r "Jadi begitu."
        p "Eh, kau nangis?!"
        r "Habisnya, setelah setahunan ini aku penasaran, akhirnya aku tahu, jadi..."
        p "Gak usah ditangisi. Yang ditinggal aja udah tabah."
        hide raina_masa_lalu

        show bg langit_sore with dissolve
        """
        Setelah kami beristirahat, kami pun melanjutkan penelusuran hingga sore hari.

        Lalu kami kembali ke balai kota untuk melaporkan hasil penelusuran kami.

        Hasil yang damai, sih. Namun itulah yang kami satu desa inginkan.
        """

        call adding( "Trust" , + 2) from _call_adding_15 # Kepercayaan

        pause 0.3

        call adding( "Bond" , + 7) from _call_adding_16 # Ikatan/Kedekatan

        pause 0.3

        call adding( "Knowledge" , + 15) from _call_adding_17 # Pengetahuan akan MC

        pause 0.3

        call adding( "Interest" , + 12) from _call_adding_18 # Ketertarikan

        jump masa_lalu_epilog

label adventurer_adegan002_mengumpulkan_material:
    hide raina_masa_lalu with dissolve
    
    pause 1.5
    
    show raina_masa_lalu neutral at sprite_karakter with dissolve
    r "Oke, misi kita sudah terdaftar."
    
    show raina_masa_lalu blink
    r "Ayo, kita pulang."
    hide raina_masa_lalu with dissolve
    
    "Setelahnya, kami pulang."
    hide bg balai_kota with dissolve

    show bg r_utama with dissolve
    p "Oke, keranjang dan sabitnya sudah ada."
    
    show raina_masa_lalu neutral at sprite_karakter
    r "Aku juga udah siapin makanannya."
    r "Siapa tahu aja."
    p "Okelah."
    p "Ayo berangkat!"

    show raina_masa_lalu happy3_little
    r "Ayo!"
    hide raina_masa_lalu
    
    stop sound 

    hide bg r_utama with dissolve

    show bg js_masuk_hutan with dissolve
    "..."
    "...."
    p "Kita sudah sampai."

    show raina_masa_lalu neutral at sprite_karakter with dissolve
    r "Iyah."
    p "Okelah, langsung saja, kalo begitu."
    hide raina_masa_lalu with dissolve

    "..."
    "...."
    "....."
    "......"
    p "Mungkin sudah terkumpul beberapa."

    show raina_masa_lalu neutral at sprite_karakter with dissolve

    play music hari_senang2 fadein 0.5 fadeout 0.5
        
    r "Kalau gitu, ayo istirahat."
    p "Ya."
    """
    Material yang dibutuhkan tidak banyak untuk kali ini, hanya beberapa tanaman herbal untuk obat luka ringan dan demam ringan.

    Juga, tampaknya sayang kalau tidak menikmati sejuknya hutan hari ini.
    """
    r "Hari ini aku buatkan kentang rebus sama sambalnya."
    p "Woah, mantap!"
    r "Hehe"
    hide raina_masa_lalu

    "..."
    "...."

    p "Okelah, ayo kita lanjutkan nyarinya. Tinggal dikit lagi."

    show raina_masa_lalu neutral at sprite_karakter with dissolve
    r "Ayo."
    hide raina_masa_lalu
    
    show bg langit_sore with dissolve
    """
    Lalu setelahnya, kami melanjutkan misi pengumpulan.

    Dan ketika langit sudah menjadi jingga kemerahan, kami pun kembali ke balai kota untuk pelaporan dan penyerahan material.

    Dan kami terus melakukan hal tersebut dalam beberapa hari ke depan.
    """
    

    jump masa_lalu_epilog

label masa_lalu_epilog:
    hide cg
    hide bg
    hide raina_masa_lalu

    "Terima kasih telah memainkan Visual Novel ini. Untuk sekarang hanya sampai sini dulu."
    "Silahkan tunggu {i}full release{/i}-nya, ya? ;)"
    
    call screen ending_screen
    
return