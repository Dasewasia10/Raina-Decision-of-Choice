## Gambar yang diperlukan pada mekanik game
image black = "#000" #Black Background
image white = "#ffffff" #White Background
image logo = "logo.png"
image logo2 = "logo2.png"

# CTC / Click to Continue
image ctc_blink:
    "gui/arrow.png"
    xoffset 5 yoffset 5
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat 

## Background
image bg common:
    "gui/op1.png"
    zoom 1.7
image bg hutan = "images/BG/bg hutan.png"
image bg hutan_malam = im.MatrixColor("images/BG/bg hutan.png", im.matrix.tint(0.5,0.5,0.6) * im.matrix.brightness(-0.2))
image bg kamar = im.Scale("images/BG/bg kamar.jpg", 1920, 1280)
image bg r_utama = "images/BG/bg ruang_utama.jpg"
image bg k_mandi = im.Scale("images/BG/bg kamar_mandi.jpg", 1920, 1280)
image bg d_rumah = im.Scale("images/BG/bg depan_rumah.jpg", 1920, 1280)
image bg pantai = "images/BG/bg pantai.png"
image bg pantai_sepia = im.Sepia("images/BG/bg pantai.png")
image bg balai_kota = im.Scale("images/BG/bg balai_kota.png", 1920, 1280)
image bg js_masuk_hutan = "images/BG/bg jalan_setapak_masuk_hutan.png"
image bg langit = im.Scale("images/BG/bg langit.jpg", 1920, 1280)
image bg langit_sore = "images/BG/bg langit_sore.png"
image bg pm_reruntuhan = "images/BG/bg pintu_masuk_reruntuhan.png"

## Karakter
# ----Raina----

# Jika dipilih versi Masa Lalu
        
## Animation-like
image raina_masa_lalu tersipu:
    "raina_masa_lalu shock_little"
    pause 0.6
    "raina_masa_lalu shy2_half"
    pause 0.6
    "raina_masa_lalu happy3_half"
    pause 5.0
    repeat

image raina_masa_lalu marah_malu:
    # Angry, karena malu
    "raina_masa_lalu angry_little"
    pause 0.6
    "raina_masa_lalu angry_half"
    pause 0.6
    "raina_masa_lalu angry_full"
    pause 5.0
    repeat
    
image raina_masa_lalu berkedip:
    "raina_masa_lalu angry_little"
    pause 0.6
    "raina_masa_lalu blink"
    pause 0.6
    "raina_masa_lalu angry_full"
    pause 5.0
    repeat

image raina_masa_lalu btm: #btm = buka_tutup_mulut
    "raina_masa_lalu happy"    
    pause 0.6
    "raina_masa_lalu neutral" 

## CG Gallery
init -1:
    image cg mm_raina_masa_lalu = im.Scale("gui/overlay/main_menu.png", 1920, 1280)
    image cg masa_lalu_1 = "images/CG/CG 001.png"
    image cg masa_lalu_2 = "images/CG/CG 002.png"
    image cg masa_lalu_3 = "images/CG/CG 003.png"
    image cg masa_lalu_4 = "images/CG/CG 004.png"
    image cg masa_lalu_5 = im.Scale("images/CG/CG 005.png", 1920, 1280)
    #image cg modern_01 = "images/CG/CG 006.png"
    #image cg modern_02 = "images/CG/CG 007.png"
    #image cg modern_03 = "images/CG/CG 008.png"
    #image cg modern_04 = "images/CG/CG 009.png"
    #image cg modern_05 = "images/CG/CG 010.png"