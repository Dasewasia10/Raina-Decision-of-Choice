## REUSABLE CODE
## Memanggil variabel yang di update lalu ditampilkan pada layar permainan
# Untuk variabel lebih dari satu
label adding( what, value ): # who, 

    $ renpy.context_dynamic( "varName", "message" )

    # Stat Raina
    if what == "Trust":
        $ message = "Kepercayaan "
        $ varName = "Trust"
    elif what == "Bond":
        $ message = "Kedekatan "
        $ varName = "Bond"
    elif what == "Knowledge":
        $ message = "Pengetahuan "
        $ varName = "Knowledge"
    elif what == "Interest":
        $ message = "Ketertarikan "
        $ varName = "Interest"
    
    # Potion
    elif what == "pd_poison":
        $ message = "Potion Poison "
        $ varName = "potion_debuff_poison"
    elif what == "pd_slow":
        $ message = "Potion Slow "
        $ varName = "potion_debuff_slow"
    elif what == "pd_paralyse":
        $ message = "Potion Paralyse "
        $ varName = "potion_debuff_paralyse"
        
    else:
        "Oops, an error happened, unknown point category '[what]'. Please, notify the author of this game."
        return

    # Memasukkan value.
    if value < 0:
        $ message += "- {}".format( abs( value ) )
    else:
        $ message += "+ {}".format( value )

    #  Attribution of the point(s).
    $ setattr( store, varName, getattr( store, varName ) + value )

    show screen loading_screen_ingame(message) with speed_dissolve

    return
    
## Memanggil variabel yang di update lalu ditampilkan pada layar permainan
# Untuk satu variabel 
label adding_one( what, value ): # who, 

    $ renpy.context_dynamic( "varName", "message" )

    # Stat Raina
    if what == "Trust":
        $ message = "Kepercayaan "
        $ varName = "Trust"
    elif what == "Bond":
        $ message = "Kedekatan "
        $ varName = "Bond"
    elif what == "Knowledge":
        $ message = "Pengetahuan "
        $ varName = "Knowledge"
    elif what == "Interest":
        $ message = "Ketertarikan "
        $ varName = "Interest"
    
    # Potion
    elif what == "pd_poison":
        $ message = "Potion Poison "
        $ varName = "potion_debuff_poison"
    elif what == "pd_slow":
        $ message = "Potion Slow "
        $ varName = "potion_debuff_slow"
    elif what == "pd_paralyse":
        $ message = "Potion Paralyse "
        $ varName = "potion_debuff_paralyse"
        
    else:
        "Oops, an error happened, unknown point category '[what]'. Please, notify the author of this game."
        return

    # Memasukkan value.
    if value < 0:
        $ message += "- {}".format( abs( value ) )
    else:
        $ message += "+ {}".format( value )

    #  Attribution of the point(s).
    $ setattr( store, varName, getattr( store, varName ) + value )

    show screen notify(message)

return
    
## Menu memilih potion, akan dipakai berulang kali
# Memanggil label ini dengan baris => call potion_coiching
label potion_coiching:
    $ chance = renpy.random.randint(0, 20)
    menu:
        "Poison Potion" if 14 < chance <= 17:
            $ punya_potion_debuff_poison = True
            call adding_one( "pd_poison", +1 ) from _call_adding_one
        "Slow Potion" if 0 < chance <= 13:
            $ punya_potion_debuff_slow = True
            call adding_one( "pd_slow", +1 ) from _call_adding_one_1
        "Paralyse Potion" if 10 < chance <= 16:
            $ punya_potion_debuff_paralyse = True
            call adding_one( "pd_paralyse", +1 ) from _call_adding_one_2
        "Gak jadi deh":
            call adding_one( "Trust", -1 ) from _call_adding_one_3
            
            show raina_masa_lalu shy_little
            r "O{w}-Okelah."
            "Dia tampaknya sedikit kecewa, tapi sudahlah."
            
    return

## Digunakan untuk mengakses isi_tas dan menggunakan atau tidak barang di dalamnya
label get_item_in_isi_tas:
    menu:
        "Poison Potion" if potion_debuff_poison > 0:
            call adding_one( "pd_poison", -1 ) from _call_adding_one_4
        "Slow Potion" if potion_debuff_slow > 0:
            call adding_one( "pd_slow", -1 ) from _call_adding_one_5
        "Paralyse Potion" if potion_debuff_paralyse > 0:
            call adding_one( "pd_paralyse", -1 ) from _call_adding_one_6
        "Sepertinya tidak perlu.":
            call adding_one( "Trust", -1 ) from _call_adding_one_7
            
## Penghitung waktu
label countTotalTime:
    $ calc_total_run()
    $ minutes, seconds = divmod(int(persistent.runtime), 60)
    $ hours, minutes = divmod(minutes, 60)
    $ all_seconds = (hours * 3600) + (minutes * 60) + seconds
    "Total waktu kamu bermain adalah sepanjang [hours] {u}jam{/u}, [minutes] {u}menit{/u} dan [seconds] {u}detik{/u} atau sepanjang [all_seconds] {u}detik{/u}"
    return