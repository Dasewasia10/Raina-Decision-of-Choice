## Ending screen
# Berisi tulisan-tulisan motivasi setelah menyelesaikan plot
screen ending_screen():
    zorder 101
    
    add "gui/op1.png"
    
    python:
        stat_rerata = ([Trust]+[Bond]+[Knowledge]+[Interest]) / 4
        playtime = FileJson(slot, "playtime", empty=0, missing=0)
        
        minutes, seconds = divmod(int(playtime), 60)
        hours, minutes = divmod(minutes, 60)
        total_seconds = [hours]*3600 + [minutes]*60 + [seconds]
        
    frame:
        style "delete_frame_bg"
        
        if stat_rerata < 21 and total_seconds > 4000:
            text _("Kamu kurang menjalin hubungan baik dengan Raina. Juga, kamu bermain terlalu lama."):
                size 40
                xalign 0.45
                yalign 0.83
    
    timer 10.0 action [Hide('loading_screen_ingame'), With(speed_dissolve)]
