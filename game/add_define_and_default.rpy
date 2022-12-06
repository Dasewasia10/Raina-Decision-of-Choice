## Tergantung versi cerita terpilih
default persistent.raina_in_masa_lalu = False
default persistent.raina_in_modern = False

## Deklarasikan karakter yang digunakan di game.
if persistent.raina_in_masa_lalu:
    default raina_name = "???"
    define r = Character('[raina_name]', image="raina_masa_lalu", ctc="ctc_blink", ctc_position="nestled")
    define n = Character('Nyi Roro Kidul', ctc="ctc_blink", ctc_position="nestled")
define fn = Character('Female', ctc="ctc_blink", ctc_position="nestled")
define mn = Character('Male', ctc="ctc_blink", ctc_position="nestled")

## Checker jika CG sudah terbuka
default persistent.cg_masa_lalu_1 = False
default persistent.cg_masa_lalu_2 = False
default persistent.cg_masa_lalu_3 = False
default persistent.cg_masa_lalu_4 = False
default persistent.cg_masa_lalu_5 = False

## SFX
define bird_chirping = "audio/sfx/Birds-chirping-sound-effect.mp3"
define bird_chirping2 = "audio/sfx/birds-118246.mp3"
define footsteps_woodfloor = "<from 14 to 20>audio/sfx/footsteps in hardwood floors.mp3"
define masak = "<from 2 to 20>audio/sfx/frying-sound-effect.mp3"
define air_laut = "audio/sfx/sandy-beach-calm-waves-water-nature-sounds-8052.mp3"
define angin_hutan = "audio/sfx/wind-in-trees-117477.mp3"

## Backsound
define hari_senang = "<from 1 to 129>audio/airtone_-_spacedust_1.mp3"
define hari_senang2 = "<from 130>audio/airtone_-_spacedust_1.mp3"
define flashback = "audio/airtone_-_0450am_2.mp3"
define happy = "audio/airtone_-_reCreation_1.mp3"
define keadaan_genting = "audio/airtone_-_sleepwalking.mp3"
define dalam_reruntuhan = "audio/rocavaco_-_Adagio_teru.mp3"
define bertarung = "audio/Karstenholymoly_-_The_night_is_calling.mp3"
define happy_ending = "audio/Code Lyoko Evolution - Code Lyoko Evolution- love song.mp3"
define people = "<from 5>audio/People_Around.mp3"

## Default key
# Indikator Raina
default Trust = 0 # Kepercayaan
default Bond = 0  # Ikatan/Kedekatan
default Knowledge = 1 # Pengetahuan akan MC
default Interest = 3 # Ketertarikan

## Default untuk berbagai variabel
default flag = False
default player = ""

## Pada raina_masa_lalu
# Variabel penentu Raina tinggal seatap dengan MC
default tinggal_seatap = False

## Variabel item
default punya_potion_debuff_poison = False
default punya_potion_debuff_slow = False
default punya_potion_debuff_paralyse = False

init:
    # Jumlah Potion tersedia
    python:
        potion_debuff_poison = 0
        potion_debuff_slow = 0
        potion_debuff_paralyse = 0

    # Custom Transition
    $ flash = Fade(.25, 0, .75, color="#fff")
    
    $ config.rollback_enabled = True
    
init python:
    config.quit_action = Quit(confirm=True)
    
    if not persistent.runtime:
        persistent.runtime = 0

    def calc_total_run():
        persistent.runtime = renpy.get_game_runtime()
        renpy.clear_game_runtime()
    
    def save_playtime(d):
            d["playtime"] = renpy.get_game_runtime()
    config.save_json_callbacks = [save_playtime]
        