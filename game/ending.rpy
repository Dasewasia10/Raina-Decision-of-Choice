## Ending screen
# Berisi tulisan-tulisan motivasi setelah menyelesaikan plot
screen ending_screen():
    zorder 101
    
    add "gui/loading_tips_screen.png"
    
    python:
        stat_rerata = (Trust+Bond+Knowledge+Interest) / 4
        playtime = persistent.runtime
        
        minutes, seconds = divmod(int(playtime), 60)
        hours, minutes = divmod(minutes, 60)
        total_seconds = hours*3600 + minutes*60 + seconds
        
    frame:
        style "delete_frame_bg"

        if stat_rerata < 21 and total_seconds > 8000:
            text _("Kamu kurang menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Juga, kamu bermain terlalu lama."):
                style "ending_text2"
        
        elif 21 < stat_rerata < 40 and total_seconds < 4000:
            text _("Kamu tampaknya telah menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Namun, kamu sepertinya bermain terlalu cepat."):
                style "ending_text2"

        elif stat_rerata > 40 and 8000 > total_seconds > 4000:
            text _("Kamu sangat hebat dalam menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Kamu juga bermain dengan cukup tepat waktu."):
                style "ending_text2"

        elif stat_rerata < 21 and total_seconds < 4000:
            text _("Kamu kurang menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Namun, kamu sepertinya bermain terlalu cepat."):
                style "ending_text2"
        
        elif 21 < stat_rerata < 40 and total_seconds > 8000:
            text _("Kamu tampaknya telah menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Juga, kamu bermain terlalu lama."):
                style "ending_text2"

        elif 21 < stat_rerata < 40 and 8000 > total_seconds > 4000:
            text _("Kamu tampaknya telah menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Kamu juga bermain dengan cukup tepat waktu."):
                style "ending_text2"

        elif stat_rerata > 40 and total_seconds < 4000:
            text _("Kamu sangat hebat dalam menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Namun, kamu sepertinya bermain terlalu cepat."):
                style "ending_text2"

        elif stat_rerata < 21 and 8000 > total_seconds > 4000:
            text _("Kamu kurang menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Kamu juga bermain dengan cukup tepat waktu."):
                style "ending_text2"

        elif stat_rerata > 40 and total_seconds > 8000:
            text _("Kamu sangat hebat dalam menjalin hubungan baik dengan Raina."):
                style "ending_text"
            text _("Juga, kamu bermain terlalu lama."):
                style "ending_text2"

    timer 10.0 action [Hide('ending_screen'), With(speed_dissolve)]

style ending_text:
    size 40
    xalign 0.45
    yalign 0.8

style ending_text2:
    size 40
    xalign 0.45
    yalign 0.9