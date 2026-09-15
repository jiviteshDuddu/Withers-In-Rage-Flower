# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Rage")
default time_to_live = 10
default flower_state = "rage"
# The game starts here.

label start:
    play music "audio/Last 10 sec.mp3" volume 0.4

    $ time_to_live = 10
    $ flower_state = "rage"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene white

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show screen rage
    # These display lines of dialogue.

    e "I am the Flower Rage."

    e "I am a flower whose birth borns out in anger."
    e "I have ten seconds to wither."
    e "In each second, a emotion color flower will come to you and tries to blend into them"
    e"But I cant be 2 emotions at same time"
    # This ends the game.

    jump countdown
label countdown:
    play music "audio/Last 10 sec.mp3" volume 0.4

    while time_to_live > 0:
        pause 1
        $ time_to_live-=1
        if time_to_live == 9:
            call pink_flower from _call_pink_flower

        if time_to_live == 8:
            call blue_flower from _call_blue_flower
        if time_to_live==7:
            call excitement from _call_excitement
        if time_to_live==6:
            call illusion from _call_illusion
        if time_to_live==5:
            call BlankBeauty from _call_BlankBeauty
        if time_to_live==0:
            jump ending

label pink_flower:
    play music "audio/Last 10 sec.mp3" volume 0.4
    show screen rage
    e "The Flower of Love has come."
    show screen love_attack
    menu:
        "Blend into me(Love), Rage.":
            $ flower_state = "love"
            show screen love
            e"The love becomes my flower."
        "Reject Love Flower":
            "I remain as rage."
    return
label blue_flower:
    play music "audio/Last 10 sec.mp3" volume 0.4

    show screen rage
    e "I as the Blue Flower, give you the enlightment of peace."
    show screen Blue
    menu:
        "Blend into me(Peace), Rage.":
            $ flower_state = "peace"
            show screen Blue1
        "Reject Peace Flower":
            "I remain as rage."
    return
label excitement:
    play music "audio/Last 10 sec.mp3" volume 0.4
    show screen rage
    e"The Excitement Flower, it wants happiness to you."
    show screen excitement
    menu:
        "Blend into me(Excitement), Rage.":
            $ flower_state = "excitement"
            show screen excite
        "I do not want happiness":
            "I remain as rage."
    return
label illusion:
    play music "audio/Last 10 sec.mp3" volume 0.4
    show screen rage
    e"I Green Flower, exist as illusion and cant be seen."
    show screen illusion
    menu:
        "Blend into me(Illusion), Rage.":
            $ flower_state = "illusion"
            show screen illusion1
        "Reject Your Flower being illusion":
            "I remain as rage."
    return
label BlankBeauty:
    play music "audio/Last 10 sec.mp3" volume 0.4
    show screen rage
    e"The Blank Beauty Flower, it is a flower that has beauty but a blank face."
    show screen BlankBeauty
    menu:
        "Blend into me(Blank Beauty), Rage.":
            $ flower_state = "blank_beauty"
            show screen BlankBeauty1
        "Reject Your Flower being Blank Beauty":
            "I remain as rage."
    return
label ending:
    play music "audio/Last 10 sec.mp3" volume 0.4
    show screen rage
    if flower_state == "rage":
        e "Until the end, I was rage."
        e"Now its time to wither"
    elif flower_state == "love":
        show screen love
        e "I became love."
        e"So, I bloom softly."
    elif flower_state == "peace":
        show screen Blue1
        e "Rage converted into peace."
        e "I stay with calm still."
    elif flower_state == "excitement":
        show screen excite
        e"I dance in excitement now"
        e" I shine in burn brightly"
    elif flower_state == "illusion":
        show screen illusion1
        e"I never existed as I become one"
        e"I am already not alive"
    elif flower_state == "blank_beauty":
        show screen BlankBeauty1
        e"I am beautiful without a face"
    return