from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3300_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_14BE",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(1160, 0, 48100, 0)
    OP_6B(2600, 0)
    SetChrPos(0x101, 1200, 0, 47440, 0)
    SetChrPos(0x102, -10, 0, 47200, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E")
    SetChrPos(0x107, 2240, 0, 46790, 0)

    label("loc_10E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D")
    SetChrPos(0x106, 940, 0, 45200, 0)

    label("loc_12D")

    OP_0D()
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(    #0
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)

    ChrTalk(    #1
        0xFE,
        "...*sniffle*...Nnnn...*hic*...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)

    ChrTalk(    #2
        0xFE,
        "...*sniffle*...*SOOOOOOB*...\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x5A, 0x64, 0xBB8, 0x0)
    OP_94(0x1, 0xFE, 0x10E, 0x64, 0xBB8, 0x0)
    OP_63(0xFE)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #3
        0xFE,
        "#5SF-Faye! Forgive me!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #4
        0xFE,
        "Huh...?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 270, 800)
    Sleep(200)
    OP_8C(0xFE, 91, 800)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #5
        0xFE,
        (
            "Uh...\x01",
            "Did I just say that out loud?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #6
        0x101,
        (
            "#509F#4PUh, yeah. You were shouting\x01",
            "at the top of your lungs.\x01",
            "(And crying gently...pffft.)\x02\x03",

            "'Faye! Forgive me!'\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #7
        0xFE,
        "Crap. I even said her name?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#505F#4PHm? Faye?\x02\x03",

            "Why does that name ring a bell?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #9
        0x107,
        (
            "#064FHmmm... Faye...\x02\x03",

            "Maybe it's the girl in the\x01",
            "factory basement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#010FOh, yeah... The girl who got\x01",
            "the gas tank for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #11
        0x101,
        "#000F#4PThat was it. Blue-collar type.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #12
        0xFE,
        (
            "Wait...\x01",
            "You know my Faye?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #13
        0x101,
        (
            "#000F#4PYeah. She helped us finish\x01",
            "up an assignment earlier.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #14
        0x102,
        "#010FWe're bracers.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 225, 400)

    ChrTalk(    #15
        0xFE,
        "Bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "That's perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#501F#4PHuh...? \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#014FDo you have a request for us?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #19
        0xFE,
        (
            "Yes. It's just a personal\x01",
            "errand, but I want you to\x01",
            "do a job for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Would now be a good time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#505F#4PWell, we'll help if we can...\x02\x03",

            "#000F...but first, I want to know\x01",
            "what it is you want us to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "R-Right... I, um...want you to\x01",
            "deliver a letter to Faye for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "She and I were seeing each other...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But we hit kind of a rough patch, and we ended\x01",
            "up breaking up recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "But I want to make it up to her.\x01",
            "That's why I wrote the letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Could I persuade you to deliver\x01",
            "the letter to her? Just whenever\x01",
            "your work takes you to Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DD")

    label("loc_88F")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #27
        0xFE,
        "Oh, it's you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "What do you say? Will\x01",
            "you deliver my letter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD")

    FadeToDark(300, 0, 70)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1")

    ChrTalk(    #29
        0x101,
        (
            "#006F#4PShouldn't be a big deal.\x02\x03",

            "What do you think, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FFine by me.\x02\x03",

            "We're not in any rush,\x01",
            "so sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C4")

    label("loc_9B1")


    ChrTalk(    #31
        0x101,
        "#006F#4POkay.\x02",
    )

    CloseMessageWindow()

    label("loc_9C4")


    ChrTalk(    #32
        0xFE,
        "Really?! That's great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I have it right here...\x01",
            "Please take care of it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        "\x07\x00Received \x07\x02Letter to Faye\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #35
        0x101,
        (
            "#006F#4POf course we will.\x02\x03",

            "#505FBut stirring a woman's emotions\x01",
            "with a letter can be kinda tough.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #36
        0x107,
        "#064FHuh? Is that true?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #37
        0xFE,
        "R-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#017FI really don't think it's our place\x01",
            "to offer advice on this, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 225, 400)

    ChrTalk(    #39
        0xFE,
        (
            "N-No, don't worry about it.\x01",
            "It's good to get a female\x01",
            "perspective, sometimes.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #40
        0xFE,
        (
            "...So, a letter alone won't\x01",
            "do it, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#505F#4PProbably not...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #42
        0x101,
        (
            "#508F#4POh, I know. How about\x01",
            "some kind of gift?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #43
        0xFE,
        (
            "Great idea...but I didn't\x01",
            "get anything to give her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Damn it. I can't just go\x01",
            "shopping while I'm on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#003F#4PThat's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Uhhh...\x01",
            "I hate to ask, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Could I also get you to\x01",
            "pick up something to go\x01",
            "along with the letter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#004F#4PHuh...? \x02\x03",

            "You want us to go gift-shopping\x01",
            "for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Right. You can buy something\x01",
            "in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Get the gift and deliver it\x01",
            "to her along with the letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #51
        0x101,
        (
            "#506F#4PW-Well, I don't have\x01",
            "a problem with it...\x02\x03",

            "#505F...but this is kind of\x01",
            "a big responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        "#018FI'm sure you're up to the task.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Faye's usually in her work\x01",
            "clothes, working with all\x01",
            "that loud machinery...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "But I really want to get her\x01",
            "something cute, that'll speak\x01",
            "to her feminine side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x107,
        (
            "#064FSomething cute...?\x02\x03",

            "Like a stuffed animal?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(    #56
        0xFE,
        (
            "I, uh... I think that'd be\x01",
            "kinda babyish for her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#007F#4POkay...something cute...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #58
        0xFE,
        (
            "I'll go ahead and give you some\x01",
            "money to cover the cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It's not much, I know, but\x01",
            "please get something for her.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #60
        "\x07\x00Received \x07\x041000\x07\x00 mira.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    AddMira(1000)

    ChrTalk(    #61
        0x101,
        (
            "#006F#4PWill do.\x02\x03",

            "So, we'll accept your request,\x01",
            "but...\x02\x03",

            "But just buying a gift in Zeiss...?\x02\x03",

            "Are you sure you want\x01",
            "to leave it up to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Yes. I think it'll work out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Thank you for this...really.\x02",
    )

    CloseMessageWindow()
    OP_3E(0x35E, 1)
    OP_28(0x31, 0x4, 0x2)
    OP_28(0x31, 0x4, 0x4)
    OP_28(0x31, 0x4, 0x8)
    OP_28(0x31, 0x1, 0x1)
    OP_28(0x31, 0x1, 0x2)
    OP_28(0x31, 0x1, 0x4)
    OP_28(0x31, 0x1, 0x8)
    OP_A2(0x8)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_14B0")

    label("loc_120B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EE")

    ChrTalk(    #64
        0x101,
        (
            "#007F#4PS-Sorry... I don't think\x01",
            "we can, right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#010FI apologize for any inconvenience.\x02\x03",

            "We're currently focused\x01",
            "on a prior obligation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #66
        0xFE,
        "Ah...a-all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "D-Don't trouble yourselves,\x01",
            "then. It's really no big deal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #68
        0xFE,
        "Sorry to have taken up your time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#003F#4PI'm just sorry that we couldn't\x01",
            "be of any help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#010FExcuse us...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(800)
    OP_63(0xFE)

    ChrTalk(    #71
        0xFE,
        (
            "...Keep my sleep-talking to\x01",
            "yourselves, please?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AA")

    label("loc_13EE")


    ChrTalk(    #72
        0x101,
        "#003F#4PSorry, but we're still busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Don't trouble yourselves,\x01",
            "then. It's really no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Sorry to have taken up your time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#007F#4PI wish we could do something...\x02",
    )

    CloseMessageWindow()

    label("loc_14AA")

    OP_28(0x31, 0x1, 0x8000)

    label("loc_14B0")

    OP_4B(0xFE, 255)
    OP_43(0xB, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    def Function_3_14BE(): pass

    label("Function_3_14BE")

    EventBegin(0x0)
    EventEnd(0x0)
    Return()

    # Function_3_14BE end

    SaveToFile()

Try(main)
