# -------------------------------------------------------------------------------
label splashscreen:
    scene black 
    $ renpy.pause(1, hard=True) 
    
    show white at transform_white 
    $ renpy.pause(1.5, hard=True) 
    
    show logo at transform_logo 
    $ renpy.pause(2, hard=True) 
    
    hide logo 
    $ renpy.pause(1.5, hard=True) 
    
    show logo2 at transform_logo 
    $ renpy.pause(2, hard=True) 
    
    hide logo2 
    $ renpy.pause(1.5, hard=True) 
    
    hide white 
    $ renpy.pause(2, hard=True) 
    
    #$ renpy.movie_cutscene('opening.webm') #Next we are showing our video. This one is skipable
    return

#label opening:
#    $ renpy.movie_cutscene('opening.webm')
#    jump before_main_menu 

label before_main_menu:
    call screen press_to_start 
        

# Game dimulai disini.
        
label start:
    
    ## Mematikan fungsi tombol ESC, klik kanan dan membuka menu
    $ _game_menu_screen = None
    
    ## Menghentikan musik lagu di main menu
    stop music

    ## Sembunyikan quick_menu sampai dialog cerita muncul
    $ quick_menu = False
    
    "Selamat datang pada Visual Novel Raina: Decision of Choice!"
    
    "Apapun pilihanmu nanti,{w} akan mencapai tujuan akhir yang berbeda-beda."
    
    "Dalam perjalananmu mencapai tujuan akhir itu,{w} akan ada seorang gadis yang akan selalu menemanimu."
    
    "Dia akan menemanimu,{w} kapanpun dan dimanapun kamu berada."
    
    "Tidak peduli alur cerita mana yang akan kamu pilih,{w} dia akan berada di sana."
    
    "Selalu."
    
    label inputName:
        scene white with dissolve
        
        python:
            player = renpy.input(_("{u}Siapakah namamu? (Silahkan ketikkan pada {i}keyboard{/i}-mu dalam 8 karakter){/u}"), allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSSTUVWXYZ", length=8)

            player = player.title()
            player = player.strip()
            if player == "":
                player = __("Dase")
        
        define p = Character('[player]', ctc="ctc_blink", ctc_position="nestled")

        "Apakah \"[player!t]\" benar namamu?"

        menu:
            "Benar":
                "Okesip, [player!t]."
            "Tidak, aku typo":
                "Santai, silahkan masukkan namamu kembali, kalau begitu."
                jump inputName
        
        "Selamat bermain! :)"
        jump pilihCerita
    # -------------------------------------------------------------------------------
    label pilihCerita:
        ## Mengaktifkan kembali fungsi tombol ESC, klik kanan dan membuka menu
        $ _game_menu_screen = 'save'
        $ save_name = player
        
        show bg common with fade
        
        "Halo!"
        
        "Terima kasih karena sudah mau mencoba bermain Visual Novel Raina : Decision of Choice."
        
        "Semoga kalian betah bermain! :)"
        
        "Disarankan untuk mematikan fitur Rollback pada Menu Preferensi, demi tercapainya ending yang akurat."
        
        "Jadi, Visual Novel ini ada beberapa pilihan cerita."
        
        "Mau pilih yang mana?"
        
        label pilih:
            menu :
                "Hidup sederhana dengan alam yang segar":
                    "Baguslah kalau sudah milih."
                    "Selamat menikmati alur ceritamu! :)"
                    $ persistent.raina_in_masa_lalu = True
                    jump adventurer_adegan_prolog
                    
                "Aku tertarik menjadi komikus":
                    "Mohon maaf, tapi cerita ini belum siap"
                    jump pilih
                    # jump komikus_adegan001
                    
                #"???":
                    #"Mohon maaf, tapi cerita ini belum siap"
                    #jump pilih
                    # jump ???_adegan001
    
$ persistent.runtime = 0
$ calc_total_run()
$ MainMenu(confirm=False)() # return 
