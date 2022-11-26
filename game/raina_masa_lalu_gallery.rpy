## raina_masa_lalu_gallery

init python:
    ## List gambar galeri
    galeri_cg_raina_masa_lalu_gallery = ["cg mm_raina_masa_lalu", "cg masa_lalu_1", "cg masa_lalu_2", "cg masa_lalu_3", "cg masa_lalu_4", "cg masa_lalu_5"]
    
    baris = 3
    kolom = 3
    #ukuran thumbnail (dalam pixel)
    thumbnail_x = 360
    thumbnail_y = 202
    
    ## Setting jumlah grid di dalam galeri
    sel = baris * kolom    
    g_cg = Gallery()
    for galeri_item in galeri_cg_raina_masa_lalu_gallery:
        g_cg.button(galeri_item + " butt")
        g_cg.image(galeri_item)
        g_cg.unlock(galeri_item)
    g_cg.transition = fade
    cg_page = 0
    
init +1 python:
    for galeri_item in galeri_cg_raina_masa_lalu_gallery:
        renpy.image (galeri_item + " butt", im.Scale(ImageReference(galeri_item), thumbnail_x, thumbnail_y))
        
screen raina_masa_lalu_gallery():
    frame:
        style "game_menu_galeri_raina_masa_lalu_content"

        vbox:
            grid kolom baris:
                spacing 20
                $ i = 0
                $ next_cg_page = cg_page + 1            
                if next_cg_page > int(len(galeri_cg_raina_masa_lalu_gallery) / sel):
                    $ next_cg_page = 0
                for galeri_item in galeri_cg_raina_masa_lalu_gallery:
                    $ i += 1
                    if i <= (cg_page + 1)*sel and i > cg_page * sel:
                        add g_cg.make_button(galeri_item + " butt", galeri_item + " butt", im.Scale("gui/op1.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (cg_page+1)*sel): #we need this to fully fill the grid
                    null
            frame:
                style "delete_frame_bg"
                
                xalign 0.5
                yoffset -160
                
                if len(galeri_cg_raina_masa_lalu_gallery) > sel:
                    textbutton _("Lainnya") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_galeri")]
                else:
                    textbutton _("{color=#40E0D0}Ini sudah semua{/color}")

style game_menu_galeri_raina_masa_lalu_content is empty

style game_menu_galeri_raina_masa_lalu_content:
    left_margin 680
    right_margin 45
    top_margin 300