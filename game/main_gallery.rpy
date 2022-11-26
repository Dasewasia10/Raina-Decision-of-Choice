screen galeri_utama():
    
    tag menu

    default which_gallery = "raina_masa_lalu_gallery"
    
    use game_menu(_("Galeri"), scroll="viewport"):
        
        frame:
            style "delete_frame_bg"
                
            vbox:
                spacing 30
                
                imagebutton auto "gui/button/gallery_raina_masa_lalu_button_%s.png":
                    action SetScreenVariable("which_gallery", "raina_masa_lalu_gallery")
                imagebutton auto "gui/button/coming_soon_button_%s.png"
    
    if which_gallery == "raina_masa_lalu_gallery":
        use raina_masa_lalu_gallery
    #elif which_gallery == "raina_modern_gallery":
        #use raina_modern_gallery
