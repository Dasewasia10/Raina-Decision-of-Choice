### ADD SCREEN
## Untuk memunculkan dan menyembunyikan
screen control():
    # Untuk Tas
    frame:
        style "delete_frame_bg"
        
        align (0.95, 0.05)
        xminimum 80
        imagebutton auto "gui/button/bag_buttontext_id_%s.png":
            action If(renpy.get_screen("isi_tas"), Hide("isi_tas"), Show("isi_tas"))

# stat_box pada Raina terhadap MC
screen stat_box():
    if not renpy.get_screen('choice'):
        frame:
            style "delete_frame_bg"
            background "gui/stats_content_id.png" xoffset -75 yoffset -60
            
            align (0.97, 0.95)
            vbox:
                style_prefix "stat_box"
                
                text _("Kepercayaan")
                text _("[Trust]")
                text _("Kedekatan")
                text _("[Bond]")
                text _("Pengetahuan")
                text _("[Knowledge]")
                text _("Ketertarikan")
                text _("[Interest]")

style stat_box_vbox is vbox

style stat_box_text:
    size 30
    xoffset 60
    yoffset 55
    xalign 0.5
    
# isi_tas
screen isi_tas():
    add "gui/bag_content.png" xalign 0.97 yalign 0.15
    
    frame:
        style "delete_frame_bg"
        top_margin 50
        
        align (0.95, 0.15)
        side ("c r"):
            area (1,0,580,400)
            
            viewport id "isi_tas_scroller":
                draggable True mousewheel True
                vbox:
                    if punya_potion_debuff_poison and potion_debuff_poison >= 1:
                        hbox:
                            text _("Poison")
                            text _(" : ")
                            text _("[potion_debuff_poison]")
                    if punya_potion_debuff_slow and potion_debuff_slow >= 1:
                        hbox:
                            text _("Slow")
                            text _(" : ")
                            text _("[potion_debuff_slow]")
                    if punya_potion_debuff_paralyse and potion_debuff_paralyse >= 1:
                        hbox:
                            text _("Paralyse")
                            text _(" : ")
                            text _("[potion_debuff_paralyse]")
                    
                    elif not (punya_potion_debuff_poison or punya_potion_debuff_slow or punya_potion_debuff_paralyse):
                        text _("Tas Kosong")
            vbar value YScrollValue("isi_tas_scroller")
        
## Memanggil layar press to start
screen press_to_start():
    tag menu
    add im.Scale("gui/overlay/main_menu.png", 1920, 1280) #The background you wish to use.
    
    add im.Scale("press_to_start.png", 1920, 1280) xalign 0.5 yalign 0.5 at transform_blink #The "Press to Start" text. I am using an image for that. The image is displayed at the middle with our blinking transformation.
    
    button:
        xysize (config.screen_width, config.screen_height)
        action Show("main_menu", transition=dissolve)
        
    #timer 50 action Jump("opening") #when left alone for 50 seconds, it jumps to the opening label.

style slot_prompt_label:
    xalign .5

style slot_prompt_text_input_input:
    size 18
    xalign .5

## Hover teks untuk menu
# Screen dari tombol start
screen continue_text_id:
    if main_menu:
        zorder -1
    add "gui/button/continue_text_id.png" xalign 0.117 yalign 0.4
    
screen newstart_text_id:
    if main_menu:
        zorder -1
    add "gui/button/newstart_text_id.png" xalign 0.117 yalign 0.4
    
screen startmenu_main_menu():
    frame:
        style "delete_frame_bg"
        align (0.31 , 0.51)
        
        hbox:
            imagebutton auto "gui/button/continue_%s_main_menu.png":
                xpos 15
                ypos 35
                hovered Show("continue_text_id", transition=speed_dissolve)
                unhovered Hide("continue_text_id", transition=speed_dissolve)
                action If("renpy.newest_slot(r'\d+') != None", Continue())
            
            null width 10
            
            imagebutton auto "gui/button/newstart_%s_main_menu.png":
                xpos 30
                ypos 35
                hovered Show("newstart_text_id", transition=speed_dissolve)
                unhovered Hide("newstart_text_id", transition=speed_dissolve)
                action Start()
#-----------------------------------------------------------------
# Tulisan hover dari tombol
screen start_text_id:
    if main_menu:
        zorder -1
    add "gui/button/start_text_id.png":
        if main_menu:
            xalign 0.117 yalign 0.4

screen setting_text_id:
    if main_menu:
        zorder -1
    add "gui/button/setting_text_id.png":
        if main_menu:
            if renpy.get_screen('main_menu'):
                xalign 0.117 yalign 0.4
            else:
                xalign 0.455 yalign 0.2
        else:
            xalign 0.556 yalign 0.2

screen about_text_id:
    if main_menu:
        zorder -1
    add "gui/button/about_text_id.png":
        if main_menu:
            if renpy.get_screen('main_menu'):
                xalign 0.117 yalign 0.4
            else:
                xalign 0.66 yalign 0.2
        else:
            xalign 0.758 yalign 0.2

screen exit_text_id:
    if main_menu:
        zorder -1
    add "gui/button/exit_text_id.png":
        if main_menu:
            if renpy.get_screen('main_menu'):
                xalign 0.117 yalign 0.4
            else:
                xalign 0.88 yalign 0.2
        else:
            xalign 0.98 yalign 0.2

screen gallery_text_id:
    if main_menu:
        zorder -1
    add "gui/button/gallery_text_id.png":
        if main_menu:
            if renpy.get_screen('main_menu'):
                xalign 0.117 yalign 0.4
            else:
                xalign 0.555 yalign 0.2

screen help_text_id:
    if main_menu:
        zorder -1
    add "gui/button/help_text_id.png":
        if main_menu:
            if renpy.get_screen('main_menu'):
                xalign 0.117 yalign 0.4
            else:
                xalign 0.745 yalign 0.2
        else:
            xalign 0.84 yalign 0.2

screen load_text_id:
    if main_menu:
        zorder -1
    add "gui/button/load_text_id.png":
        if main_menu:
            if renpy.get_screen('main_menu'):
                xalign 0.117 yalign 0.4
            else:
                xalign 0.362 yalign 0.2
        else:
            xalign 0.458 yalign 0.2

screen save_text_id:
    if main_menu:
        zorder -1
    add "gui/button/save_text_id.png" xalign 0.36 yalign 0.2

screen return_text_id:
    if main_menu:
        zorder -1
    add "gui/button/return_text_id.png" xalign 0.668 yalign 0.2

screen feedback_text_id:
    if main_menu:
        zorder -1
    add "gui/button/feedback_text_id.png" xalign 0.117 yalign 0.4
    
## Custom Screen Credit
screen credit():
    tag menu
    use game_menu(_("Tentang Kami")):
        
        style_prefix "credit"
        
        frame:
            style "delete_frame_bg"
            
            hbox:
                vbox:
                    ypos 220
                    xalign 0.5
                    spacing 20
                    
                    label _("Dibuat menggunakan :")
                    
                    image "gui/credit/renpy_logo.png" xalign 0.8
                
                null width 220
                
                hbox:
                    vbox:
                        ypos 50
                        spacing 5
                        
                        label _("Dikembangkan oleh :")
                        
                        image "gui/credit/peepaaworks_logo.png" xoffset 130
                
                        null height 20
                        
                        vbox:
                            xoffset 50
                            
                            label _("dig.ccmixter.org")
                            
                            textbutton "https://dig.ccmixter.org":
                                text_size 40
                                action OpenURL("https://dig.ccmixter.org")
                            
                            text _("SFX, Backsound")
                            
                            null height 20
                            
                            label _("Aset musik gratis lainnya") xoffset -100
                            text _("SFX, Backsound")
                        
                    vbox:
                        ypos 100
                        
                        vbox:
                            spacing 20
                            
                            label _("Dasewasia | YukiHitoshi#7145")
                            
                            hbox:
                                spacing 20
                                xalign 0.5
                                xoffset 60
                                
                                imagebutton auto "gui/credit/facebook_logo_%s.png" action OpenURL("https://www.facebook.com/Dasewasia10")
                                imagebutton auto "gui/credit/twitter_logo_%s.png" action OpenURL("https://twitter.com/dasewasia")
                            
                            text _("Program, Skrip, GUI, BG") xoffset 60
                        
                        null height 50
                        
                        vbox:
                            spacing 20
                            xoffset 30
                            
                            label _("longmalin_ | Fazzkey#8758")
                            
                            hbox:
                                spacing 20
                                xalign 0.5
                                xoffset 60
                                
                                imagebutton auto "gui/credit/twitter_logo_%s.png" action OpenURL("https://twitter.com/long_malin")
                                imagebutton auto "gui/credit/fiverr_logo_%s.png" action OpenURL("https://www.fiverr.com/longmalin_?source=gig_page")
                            
                            text _("Art, Sprite, CG, BG") xoffset 60
                
            hbox:
                xoffset 1300
                yoffset 580
                xmaximum 500
                
                if gui.show_name:
                    text _("Version [config.version] © [year] {font=fonts/NotoSansJP-Bold.otf}ペーパー Works{/font}. All rights reversed.") size 30 xalign 0.5

style credit_vbox is vbox
style credit_text is main_menu_text

style credit_label_text:
    color gui.hover_color
    xoffset 90
    size 40
    
style credit_text:
    outlines [ (1, "#559D94", 2, 2) ]
    xalign 0.5
    size 30
    
## Loading screen di pertengahan game
screen loading_screen_ingame(message):
    zorder 101
    
    add "gui/loading_tips_screen.png"
    
    frame:
        style "delete_frame_bg"
        
        python:
            tips = ["Item yang akan diambil ketika persiapan terkadang {i}random{/i}.", "Jangan sembarangan percaya dengan orang lain.", "Raina akan selalu menemanimu, kapanpun itu.", "Raina akan selalu menemanimu, dimanapun itu."]
            to_random_tips = renpy.random.choice(tips)
            
            random_tips = []
            random_tips.append(to_random_tips)
        
        text _("[random_tips[0]]"):
            size 40
            xalign 0.45
            yalign 0.83
        
        text "[message!tq]":
            size 40
            xalign 0.45
            yalign 0.9
    
    timer 2.0 action [Hide('loading_screen_ingame'), With(speed_dissolve)]

## Style untuk screen di atas
style delete_frame_bg is empty
