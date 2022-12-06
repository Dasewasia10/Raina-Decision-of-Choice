################################################################################
## Inisialisasi
################################################################################

init offset = -1

init -999 python:
    def newest_slot_tuple():
        """
        Returns a tuple with the newest slot page and name.
        """
        newest = renpy.newest_slot()

        if newest is not None:
            page, name = newest.split("-")
            return (page, name)

    class Continue(Action):
        """
        Loads the last save file.
        """

        def __call__(self):

            if not self.get_sensitive():
                return

            # Assign variables from the tuple.
            newest_page, newest_name = newest_slot_tuple()

            # Load the file using the newest slot information.
            FileLoad(newest_name, confirm=False, page=newest_page, newest=True)()

        def get_sensitive(self):
                
            # Insensitive in-game.
            if not main_menu:
                return False

            # Insensitive during replay mode.
            if _in_replay:
                return False

            # Get the tuple.
            newest = newest_slot_tuple()

            # Insensitive if no new slot files.
            if newest is None:
                return False

            # Assign variables from the tuple.
            newest_page, newest_name = newest

            # Insensitive if the newest save is '_reload-*'
            if newest_page == '_reload':
                return False
                
            # This action returns true if the file is loadable.
            return FileLoadable(newest_name, page=newest_page)
            
init python:
    config.has_quicksave = False
    config.has_autosave = False
################################################################################
## Gaya
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
    color gui.text_color
    outlines gui.name_text_outlines

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    yalign 0.5
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Layar In-game
################################################################################


## Layar Say ###################################################################
##
## Layar say di gunakan untuk menampilkan dialog kepada pemain. Ini menggunakan
## dua parameter, who dan what, yang merupakan nama karakter yang berbicara dan
## text yang akan di tampilkan, masing-masing. (Kedua parameter dapat berisi
## None jika tidak ada nama yang di berikan.
##
## Layar ini harus membuat text yang dapat di tampilkan dengan id "what", yang
## di mana Ren'Py menggunakan ini untuk mengatur tampilan text. Ini juga dapat
## membuat sesuatu yang dapat di tampilkan dengan id "who" dan id "window" untuk
## mengaplikasikan properti gaya.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Jika ada gambar di sisi, tampilkan di atas text. Jangan tampilkan di
    ## versi HP[Handphone)(Android) - Karena tidak ada ruang.
    if not renpy.variant("small"):
        zorder 10
        add SideImage() xalign 0.0 yalign 1.0 zoom 0.25 xoffset -100 yoffset 700


## Buat namebox tersedia untuk mengatur gaya melalui objek karakter.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    color gui.selected_color
    outlines gui.name_text_outlines
    xpos 25
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Layar masukkan/input ########################################################
##
## Layar ini di gunakan untuk menampilkan renpy.input. Parameter prompt
## digunakan untuk meneruskan text yang di prompt/minta.
##
## Layar ini harus membuat input yang dapat di tampilkan dengan id "input" untuk
## menerima berbagai parameter masukan.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Layar Pilihan ###############################################################
##
## Layar ini digunakan untuk menampilkan pilihan dalam game yang disajikan oleh
## menu statement. Satu parameter, item, adalah daftar objek, masing-masing
## dengan bidang keterangan dan tindakan.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    
    style_prefix "choice"
    
    for i in items:
        vpgrid:
            if len(items) % 2 == 0 or len(items) == 1:
                cols 2
            if len(items) % 3 == 0:
                cols 3

            allow_underfull True
            
            xalign 0.5
            yalign 0.6
            yanchor 0.5

            spacing gui.choice_spacing
            
            for i in items:
                textbutton i.caption action i.action
                    
        for n, i in enumerate(items, 1): # n would be the number starting from 1
            if n<10:
                key str(n) action i.action


style choice_hbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Layar Menu Cepat/Quick Menu #################################################
##
## Menu cepat ditampilkan dalam game untuk memudahkan akses ke menu di luar
## game.

init:
    transform customzoom:
        zoom 0.7
        
screen quick_menu():
    
    ## Memastikan ini muncul di atas layar yang lain.
    zorder 100

    if quick_menu and not renpy.get_screen('choice'):

        hbox:
            style_prefix "quick"

            xalign 0.78
            yalign 0.7
            
            imagebutton auto "gui/button/log_%s.png"  action ShowMenu('history') at customzoom
            
            null width 10
    
            imagebutton auto "gui/button/skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) at customzoom
            
            null width 10
            
            imagebutton auto "gui/button/auto_%s.png" action Preference("auto-forward", "toggle") at customzoom


## Kode ini memastikan layar quick_menu di tampilkan di dalam permainan,
## kapanpun player tidak secaralangsung menyembunyikan antarmuka.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Layar Menu Utama dan Menu Permainan
################################################################################

## Layar navigasi ##############################################################
##
## Layar ini di ikutsertakan di menu utama dan permainan, dan menyediakan
## navigasi ke menu lainnya, dan untuk memulai permainan.

screen navigation():
    
    if renpy.get_screen('main_menu'):
        style_prefix "navigation"
        
        if main_menu:
            imagebutton auto "gui/button/start_%s_main_menu.png":
                xpos 190 ypos 500
                hovered Show("start_text_id", transition=speed_dissolve)
                unhovered Hide("start_text_id", transition=speed_dissolve)
                action If(renpy.get_screen("startmenu_main_menu"), 
                    Hide("startmenu_main_menu", transition=speed_dissolve), 
                    Show("startmenu_main_menu", transition=speed_dissolve))
                
            imagebutton auto "gui/button/feedback_%s_main_menu.png":
                xpos 85 ypos 615
                hovered Show("feedback_text_id", transition=speed_dissolve)
                unhovered Hide("feedback_text_id", transition=speed_dissolve)
                action OpenURL("https://forms.gle/E5HpiXdw8Jw17XJF9")

        imagebutton auto "gui/button/load_%s_main_menu.png":
            xpos 115 ypos 475
            hovered Show("load_text_id", transition=speed_dissolve)
            unhovered Hide("load_text_id", transition=speed_dissolve)
            action If("renpy.newest_slot(r'\d+') != None", ShowMenu("load"))

        imagebutton auto "gui/button/setting_%s_main_menu.png":
            xpos 385 ypos 475
            hovered Show("setting_text_id", transition=speed_dissolve)
            unhovered Hide("setting_text_id", transition=speed_dissolve)
            action ShowMenu("preferences")
        
        imagebutton auto "gui/button/gallery_%s_main_menu.png":
            xpos 160 ypos 700
            hovered Show("gallery_text_id", transition=speed_dissolve)
            unhovered Hide("gallery_text_id", transition=speed_dissolve)
            action ShowMenu("galeri_utama")
        
        imagebutton auto "gui/button/about_%s_main_menu.png":
            xpos 340 ypos 700
            hovered Show("about_text_id", transition=speed_dissolve)
            unhovered Hide("about_text_id", transition=speed_dissolve)
            action ShowMenu("credit")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            imagebutton auto "gui/button/help_%s_main_menu.png":
                xpos 430 ypos 615
                hovered Show("help_text_id", transition=speed_dissolve)
                unhovered Hide("help_text_id", transition=speed_dissolve)
                action ShowMenu("help")

        if renpy.variant("pc"):
            imagebutton auto "gui/button/exit_%s_main_menu.png":
                xpos 250 ypos 780
                hovered Show("exit_text_id", transition=speed_dissolve)
                unhovered Hide("exit_text_id", transition=speed_dissolve)
                action Quit(confirm=True)
            
    else:
        hbox:
            style_prefix "navigation"
            
            xpos 650
            ypos 50
            
            spacing 40

            if not main_menu:
                imagebutton auto "gui/button/save_%s_main_menu.png":
                    hovered Show("save_text_id", transition=speed_dissolve)
                    unhovered Hide("save_text_id", transition=speed_dissolve)
                    action ShowMenu("save")

            imagebutton auto "gui/button/load_%s_main_menu.png":
                hovered Show("load_text_id", transition=speed_dissolve)
                unhovered Hide("load_text_id", transition=speed_dissolve)
                action If("renpy.newest_slot(r'\d+') != None", ShowMenu("load"))

            imagebutton auto "gui/button/setting_%s_main_menu.png":
                hovered Show("setting_text_id", transition=speed_dissolve)
                unhovered Hide("setting_text_id", transition=speed_dissolve)
                action ShowMenu("preferences")
            
            if main_menu:
                imagebutton auto "gui/button/gallery_%s_main_menu.png":
                    hovered Show("gallery_text_id", transition=speed_dissolve)
                    unhovered Hide("gallery_text_id", transition=speed_dissolve)
                    action ShowMenu("galeri_utama")
            
            if not main_menu:
                imagebutton auto "gui/button/return_%s_main_menu.png":
                    hovered Show("return_text_id", transition=speed_dissolve)
                    unhovered Hide("return_text_id", transition=speed_dissolve)
                    action MainMenu()
            
            imagebutton auto "gui/button/about_%s_main_menu.png":
                hovered Show("about_text_id", transition=speed_dissolve)
                unhovered Hide("about_text_id", transition=speed_dissolve)
                action ShowMenu("credit")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                imagebutton auto "gui/button/help_%s_main_menu.png":
                    hovered Show("help_text_id", transition=speed_dissolve)
                    unhovered Hide("help_text_id", transition=speed_dissolve)
                    action ShowMenu("help")

            if renpy.variant("pc"):
                imagebutton auto "gui/button/exit_%s_main_menu.png":
                    hovered Show("exit_text_id", transition=speed_dissolve)
                    unhovered Hide("exit_text_id", transition=speed_dissolve)
                    action Quit(confirm=True)
            
style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Layar Menu utama ############################################################
##
## Digunakan untuk menampilkan menu utama ketika Ren'Py dimulai.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Ini Memastikan Layar Menu Yang Lain Telah Di Timpa
    tag menu

    add gui.main_menu_background

    zorder -3
     
    ## Frame kosong ini menggelap di menu utama.
    frame:
        style "main_menu_frame"
                  
        default cg_adding = []
        python:
            if persistent.cg_masa_lalu_1:
                cg_adding.append("cg masa_lalu_1")
            if persistent.cg_masa_lalu_2:
                cg_adding.append("cg masa_lalu_2")
            if persistent.cg_masa_lalu_3:
                cg_adding.append("cg masa_lalu_3")
            if persistent.cg_masa_lalu_4:
                cg_adding.append("cg masa_lalu_4")
            if persistent.cg_masa_lalu_5:
                cg_adding.append("cg masa_lalu_5")
            
            if cg_adding:
                cg_di_layar_utama = renpy.random.choice(cg_adding)
            
        if cg_adding:
            add cg_di_layar_utama
        
    ## Pernyataan 'use' mengikutsertakan layar lain ke layar ini. Isi sebenarnya
    ## dari menu utama adalah layar navigasi.
    use navigation
    
    add "gui/logo.png" xalign 0.05 ypos 70 zoom 0.5
    
style main_menu_frame is empty
style main_menu_text is gui_text
style main_menu_title is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background im.Scale("gui/overlay/main_menu.png", 1920, 1280)

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")


## layar Menu Permainan ########################################################
##
## Ini menjalaskan struktur dasar yang paling sering di gunakan di layar menu
## permainan, ini ditampilkan beserta layar judul, dan menampilkan latar
## belakang,judul,dan navigasi.
##
## Parameter scroll dapat berisi 'None', atau "viewport" dan "vpgrid". Ketika
## layar ini di maksudkan untuk di gunakan dengan cabang satu atau lebih, yang
## di tempatkan di dalamnya.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    
    if main_menu:
        zorder -2
        add gui.main_menu_background
    else:
        zorder -2
        add gui.game_menu_background
        
    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Memesan tempat untuk bagian navigasi.
            frame:
                style "game_menu_navigation_frame"

            frame:
                if renpy.get_screen('history'):
                    style "game_menu_history_content"
                elif renpy.get_screen('preferences'):
                    style "game_menu_preferences_content"
                elif renpy.get_screen('save') or renpy.get_screen('load'):
                    style "game_menu_saveload_content"
                elif renpy.get_screen('help'):
                    style "game_menu_help_content"
                elif renpy.get_screen('credit'):
                    style "game_menu_credit_content"
                elif renpy.get_screen('galeri_utama'):
                    style "game_menu_galeri_utama_content"
                else:
                    style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    imagebutton auto "gui/button/back_arrow_%s.png":
        xpos 80
        ypos 880
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty

style game_menu_preferences_content is empty
style game_menu_saveload_content is empty
style game_menu_history_content is empty
style game_menu_help_content is empty
style game_menu_credit_content is empty

style game_menu_galeri_utama_content is empty

style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 120
    right_margin 45
    top_margin 60
    bottom_margin 30

style game_menu_viewport:
    xsize 2000

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 340
    ypos 210
    xalign 0.5
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
    
style game_menu_saveload_content:
    left_margin -300
    right_margin 45
    top_margin 60
    bottom_margin 30
    
style game_menu_history_content:
    left_margin 20
    right_margin 45
    top_margin 250
    bottom_margin 30
 
style game_menu_help_content:
    left_margin -250
    right_margin 45
    top_margin 120

style game_menu_preferences_content:
    left_margin -300
    top_margin 100

style game_menu_galeri_utama_content:
    left_margin -300
    right_margin 45
    top_margin 250

style game_menu_credit_content:
    background "gui/credit/credit_add_screen.png"
    left_margin -350
    right_margin 45
    top_margin 100
    
## Layar About #################################################################
##
## Layar ini menampilkan credit dan informasi copyright tentang game dan Ren.Py.
##
## Tidak ada yang spesial dengan layar ini, semenjak ini juga berperan sebagai
## contoh bagaimana membuat layar custom.

screen about():

    tag menu

    ## Pernyataan 'use' ini mengikutsertakan layar game_menu ke dalam layar ini.
    ## Percabangan vbox lalu di ikutsertakan kedalam viewport di dalam layar
    ## game_menu.
    use game_menu(_("Tentang"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versi [config.version!t]\n")

            ## gui.about biasanya di set di options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Dibuat Dengan {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Layar Load and Save #########################################################
##
## Layar ini bertanggungjawab untuk mengijinkan pemain menyimpan dan
## meload lagi. Semenjak mereke hampir memiliki hal yang sama, keduanya di
## implementasinan di percabangan layar ketiga, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Simpan"))

screen load():

    tag menu

    use file_slots(_("Muat"))


screen slots_note(slot):
    modal True
    
    default note = '{} - '.format(player)

    frame:
        style_prefix 'slot_prompt'

        has vbox

        label _('Buat catatan :')

        frame:
            style_prefix 'text_input'
            input:
                allow ('abcdefghijklmnopqrstuvwxyz'
                        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        '0123456789 -_!()@:;?<>,.#/')
                length 24
                value ScreenVariableInputValue('note')

        hbox:
            button:
                action (SetField(store, 'save_name', note.strip()),
                        FileSave(slot, confirm=False),
                        SetField(store, 'save_name', ''),
                        Hide('slots_note'))
                keysym 'input_enter'
                selected False
                sensitive note.strip()

                if FileLoadable(slot):
                    style_suffix 'warn_button'
                    text _('Overwrite') style_suffix 'warn_button_text'
                else:
                    text _('OK') style_suffix 'button_text'

            textbutton _('Cancel'):
                action Hide('slots_note')
                keysym 'game_menu'

style slot_prompt_button is menu_button:

    xysize (150, 50)

style slot_prompt_button_text is menu_button_text:

    size 30

style slot_prompt_frame is menu_frame:

    align (.5, .5)
    fit_first True
    padding (25, 35, 25, 25)
    xmaximum 650

style slot_prompt_hbox:
    spacing 50
    xalign .5

style slot_prompt_label:
    xalign .5

style slot_prompt_text_input_input:
    size 18
    xalign .5

style slot_prompt_vbox:
    spacing 20

style slot_prompt_warn_button take slot_prompt_button


style slot_prompt_warn_button_text:
    size 30


## Tampilan slot untuk save data
screen file_slots(title):
    
    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Otomatis save"), quick=_("Save cepat"))
    
    use game_menu(title):
        
        add "gui/saveload_add_screen.png" xpos -130 ypos -240
        
        fixed:

            ## Ini memastikan input akan mendapat event masuk sebelum tombol
            ## lainnya.
            order_reverse True

            ## Kolom slot file.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                yfill True
                xalign 0.0
                xoffset 560

                spacing gui.page_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    python:
                        ref = '{}-{}'.format(FileCurrentPage(), slot)
                        date = FileTime(slot, format=__('{#date_fmt}%B %d, %H:%M'),
                                            empty=__('{i}Kosong{/i}'))
                        noting = FileSaveName(slot)
                        playtime = FileJson(slot, "playtime", empty=0, missing=0) #### <- here
                        
                        # Mengambil waktu dalam bentuk jam : menit : detik
                        minutes, seconds = divmod(int(playtime), 60)
                        hours, minutes = divmod(minutes, 60)
                        action = FileAction(slot)
                        
                    hbox:
                        hbox:
                            button:
                                add FileScreenshot(slot) xalign 0.5
                                
                                action If(isinstance(action, FileSave),
                                        If(FileCurrentPage() == 'auto',
                                            None, Show('slots_note', None, slot)),
                                        action)
                                alt '{} {}. {}'.format(title, ref, date)
                                    
                                key "save_delete" action FileDelete(slot)
                        hbox:
                            null width gui.pref_spacing
                            
                            text '[ref]. [date]\n[noting]\n[hours:02d]:[minutes:02d]:[seconds:02d]':
                                style "slot_button_text"
                            
            ## Tombol untuk mengakses halaman lain.
            hbox:
                style_prefix "page"

                xalign 0.01
                yalign 0.5

                spacing gui.page_spacing

                grid 5 2:
                    spacing 20
                    
                    imagebutton auto "gui/button/saveload_1_%s.png" action FilePage(1)
                    imagebutton auto "gui/button/saveload_2_%s.png" action FilePage(2)
                    imagebutton auto "gui/button/saveload_3_%s.png" action FilePage(3)
                    imagebutton auto "gui/button/saveload_4_%s.png" action FilePage(4)
                    imagebutton auto "gui/button/saveload_5_%s.png" action FilePage(5)
                    
                    imagebutton auto "gui/button/saveload_6_%s.png" action FilePage(6)
                    imagebutton auto "gui/button/saveload_7_%s.png" action FilePage(7)
                    imagebutton auto "gui/button/saveload_8_%s.png" action FilePage(8)
                    imagebutton auto "gui/button/saveload_9_%s.png" action FilePage(9)
                    imagebutton auto "gui/button/saveload_10_%s.png" action FilePage(10)
        
style page_label is gui_label

style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    size 40

style slot_button:
    properties gui.button_properties("slot_button")
    xalign 0.0

style slot_button_text:
    color gui.accent_color
    xoffset 170
    yoffset 50
    xpos 150
    xalign 0.5
    size 40


## Layar preferensi/opsi #######################################################
##
## Layar preferensi mengijinkan pemain untuk mengkonfigurasi permainan untuk
## menyesuaikan gaya bermain masing masing individu.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferensi"), scroll="viewport"):
    
        null height (4 * gui.pref_spacing)
        
        hbox:
            vbox:
                box_wrap True
                
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        
                        null height (6 * gui.pref_spacing)
                        
                        label _("{u}Tampilan :{/u}")
                        
                        null height (2 * gui.pref_spacing)
                        
                        hbox:
                            imagebutton auto "gui/button/windows_%s_display_preference.png":
                                action Preference("display", "window")
                            
                            null width (2 * gui.pref_spacing)
                            
                            imagebutton auto "gui/button/fullscreen_%s_display_preference.png":
                                action Preference("display", "fullscreen")

                null height (4 * gui.pref_spacing)
                
                vbox:
                    xmaximum 500

                    label _("{u}Skip teks belum terlihat?{/u}")
                    style_prefix "check"
                    textbutton _("Aktifkan") action Preference("skip", "toggle")

            null width (10 * gui.pref_spacing)
            
            hbox:
                style_prefix "slider"
                box_wrap True
                
                vbox:
                    
                    label _("{u}Kecepatan Teks :{/u}")

                    bar value Preference("text speed")
                    
                    null height (2 * gui.pref_spacing)

                    label _("{u}Auto-Forward :{/u}")

                    bar value Preference("auto-forward time")

                vbox:
                    null height (6 * gui.pref_spacing)
                
                    label _("{u}Volume :{/u}")

                    null height gui.pref_spacing

                    if config.has_music:
                        label _("Musik")

                        hbox:
                            bar value Preference("music volume")

                    null height gui.pref_spacing

                    if config.has_sound:

                        label _("Suara")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Tes") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        null height (2 * gui.pref_spacing)
                        
                        label _("Vokal")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Tes") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Senyapkan Semua"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                
            null width (3 * gui.pref_spacing)
                
            vbox:
                style_prefix "radio"
                label _("{u}Nyalakan Rollback?{/u}")
                
                null height (2 * gui.pref_spacing)
                
                hbox:
                    textbutton _("Nyala") action ToggleField(config, "rollback_enabled",  true_value=True, false_value=False)
                    null width (2 * gui.pref_spacing)
                    textbutton _("Mati") action ToggleField(config, "rollback_enabled",  true_value=False, false_value=True)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin 5
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    size 40

style pref_vbox:
    xsize 400

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    idle_color '#E5FFFA'
    hover_color gui.hover_color
    selected_color '#40E0D0'
    properties gui.button_text_properties("radio_button")
    size 40

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    idle_color '#E5FFFA'
    hover_color gui.hover_color
    selected_color '#40E0D0'
    properties gui.button_text_properties("check_button")
    size 40

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 600


## Layar Riwayat ###############################################################
##
## Layar yang menampilkan History dialog kepada pemain. Semenjak tidak ada yang
## spesial tentang layar ini, ini memiliki akses ke history dialog yang di
## simpan di _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Hindari mempredisi layar ini, ini dapat berukuran sangat besar.
    predict False

    use game_menu(_("Riwayat"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Ini menampilkan layar secara semestinya jika history_height
                ## memiliki value None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Mengambil warna dari text 'who' dari karakter, jika
                        ## di set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Riwayat dialog kosong.")


## Ini menentukan tag apa yang diizinkan ditampilkan di layar sejarah/catatan.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    xoffset -30
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Layar Bantuan ###############################################################
##
## Layar yang memberikan informasi tentang keyboard dan mouse binding. Ini
## menggunakan layar lain (keyboard_help, mouse_help, and gamepad_help) untuk
## menampilkan bantuan yang sebenarnya.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Bantuan")): #, scroll="viewport")
        
        frame:
            style "delete_frame_bg"
            
            imagebutton auto "gui/button/help_%s_keyboard.png":                    
                ypos 200
                action SetScreenVariable("device", "keyboard")
            imagebutton auto "gui/button/help_%s_mouse.png":
                ypos 300
                action SetScreenVariable("device", "mouse")
    
    if device == "keyboard":
        use keyboard_help
    elif device == "mouse":
        use mouse_help

screen keyboard_help():
    add "gui/help_keyboard_add_screen.png"

screen mouse_help():
    add "gui/help_mouse_add_screen.png"
    
################################################################################
## Layar Tambahan
################################################################################


## Layar konfirmasi ############################################################
##
## Layar konfirmasi di panggil ketika Ren'Py mau menanyakan ke pemain pertanyaan
## ya atau tidak.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Memastikan layar lain tidak mendapatkan input ketika layar ini di
    ## panggil.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Ya") action yes_action
                textbutton _("Tidak") action no_action

    ## Klik kanan dan jawaban escape "Tidak".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Lompati indikator layar #####################################################
##
## layar skip_indicator di tampilkan untuk mengindikasian proses skipping sedang
## dalam proses.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Melompati")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## transform digunakan untuk mengkedipkan panah setelah yang lain.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Kami harus menggunakan font yang mempunyai glyph BLACK RIGHT-POINTING
    ## SMALL TRIANGLE didalamnya.
    font "DejaVuSans.ttf"


## Layar pemberitahuan #########################################################
##
## layar notify digunakan untuk menampilkan pesan kepada pemain. (Seperti,
## ketika game di simpan cepat atau screenshot di ambil.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 1.2 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color gui.accent_color


## Layar NVL ###################################################################
##
## Layar ini digunakan untuk dialog dan menu mode-NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Menampilkan dialog pada vpgrid atau vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ini mengendalikan angka maksimum entri mode-NVL yang dapat di tampilkan
## sekaligus.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Versi Mobile(HP/Handphone/Android)
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Semenjak mouse tidak ada, kami mengganti menu cepat dengan yang menggunakan
## tombol yang lebih besar dan sedikit, yang memudahkan untuk di sentuh.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu and not renpy.get_screen('choice'):

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Kembali") action Rollback()
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
