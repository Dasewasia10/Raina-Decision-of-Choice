### ADD TRANSFORM
## Transformasi and Opening
#Transformation for Logo    
transform transform_logo:
    on show:
        zoom 0.5
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0
        
#Transformation for background
transform transform_white:
    on show:
        alpha 0 
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0
        
#Transformation for blink
transform transform_blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

# Mengubah ukuran sprite karakter
transform sprite_karakter:
    zoom 0.3
    yoffset 150
    xalign 0.5
    
# Dissolve lebih cepat
default speed_dissolve = Dissolve(0.1)

# Transisi kiri ke kanan
default moveinoutdissolve = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)
default moveoutindissolve = ComposeTransition(dissolve, before=moveinright, after=moveoutleft)

## STYLE
style narator_text is text:
    xpos -60