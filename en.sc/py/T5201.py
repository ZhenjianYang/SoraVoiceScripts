from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5201   ._SN',
        MapName             = 'Other',
        Location            = 'T5201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60117",
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
        'Joshua',                               # 9
        'Josette',                              # 10
        'Kyle',                                 # 11
        'Don',                                  # 12
        'White Bouquet',                        # 13
        'Sword',                                # 14
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


    AddCharChip(
        'ED6_DT27/CH03010 ._CH',             # 00
        'ED6_DT27/CH03100 ._CH',             # 01
        'ED6_DT27/CH03770 ._CH',             # 02
        'ED6_DT27/CH03760 ._CH',             # 03
        'ED6_DT26/CH20264 ._CH',             # 04
        'ED6_DT27/CH03101 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03010P._CP',             # 00
        'ED6_DT27/CH03100P._CP',             # 01
        'ED6_DT27/CH03770P._CP',             # 02
        'ED6_DT27/CH03760P._CP',             # 03
        'ED6_DT26/CH20264P._CP',             # 04
        'ED6_DT27/CH03101P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1C3",          # 01, 1
        "Function_2_1FC",          # 02, 2
        "Function_3_154B",         # 03, 3
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_1C2")

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1C2")
    OP_A3(0x10F1)
    Event(0, 3)

    label("loc_1C2")

    Return()

    # Function_0_19A end

    def Function_1_1C3(): pass

    label("Function_1_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF")
    OP_23(0x1C3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x448, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FB")
    OP_23(0x1C3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FB")

    Return()

    # Function_1_1C3 end

    def Function_2_1FC(): pass

    label("Function_2_1FC")

    EventBegin(0x0)
    OP_DB()
    OP_22(0x1C3, 0x0, 0x64)
    OP_6D(450, -1000, -8810, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrPos(0x9, -2500, -1000, 14100, 0)
    SetChrPos(0xB, -3480, -1000, 13100, 0)
    SetChrPos(0xA, -1600, -1000, 13100, 0)
    SetChrPos(0x8, -2750, -900, 28300, 0)
    SetChrPos(0xC, -2850, -1000, 28850, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 16)
    OP_E5(0x8, 0x0, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    FadeToBright(1000, 0)

    def lambda_2D6():
        OP_6D(-1730, -1000, 28380, 7000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D6)
    WaitChrThread(0x8, 0x0)
    Fade(500)
    OP_6D(-2180, -1000, 29400, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(1500, 0)
    OP_0D()
    Sleep(500)
    OP_DC()

    NpcTalk(    #0
        0x8,
        "Black-Haired Boy",
        (
            "#6P...\x02\x03",

            "Karin... I'm home.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 17)
    ClearChrFlags(0xC, 0x80)
    SetChrSubChip(0xC, 7)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #1
        0x9,
        "Girl's Voice",
        "#1PH-Heeey...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x9,
        "Girl's Voice",
        "#1PJoshuaaaa, where did you goooo?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_3E4():
        OP_6D(-1650, -1000, 23080, 3500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E4)

    def lambda_3FC():
        OP_67(0, 9500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3FC)

    def lambda_414():
        OP_6B(1700, 3500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_414)
    Sleep(1000)

    def lambda_429():
        OP_8E(0xFE, 0xFFFFF790, 0xFFFFFC18, 0x49B6, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_429)
    Sleep(200)

    def lambda_449():
        OP_8E(0xFE, 0xFFFFFB1E, 0xFFFFFC18, 0x4506, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_449)
    Sleep(600)

    def lambda_469():
        OP_8E(0xFE, 0xFFFFF51A, 0xFFFFFC18, 0x4402, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_469)
    WaitChrThread(0x9, 0x0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x9,
        "#415F#5PPhew! Good! Here you are!\x02",
    )

    CloseMessageWindow()

    def lambda_4CC():
        OP_8E(0xFE, 0xFFFFF510, 0xFFFFFC18, 0x64FA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4CC)

    def lambda_4E7():
        OP_6D(-1740, -1000, 27700, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4E7)

    def lambda_4FF():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4FF)
    Sleep(100)

    def lambda_51C():
        OP_8E(0xFE, 0xFFFFF8F8, 0xFFFFFC18, 0x5F8C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_51C)
    Sleep(400)

    def lambda_53C():
        OP_8E(0xFE, 0xFFFFF290, 0xFFFFFC18, 0x5D48, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_53C)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x9,
        (
            "#210F#2PSheesh, don't freak me out like that!\x01",
            "Running off on your own...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x8,
        "#1035F#6PHmph... Why did you follow me?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        (
            "#1030F#6PI told you. I have personal business\x01",
            "here, and you did not need to come.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x9,
        (
            "#212F#2POh, thanks, real cute with\x01",
            "the gratitude, there!\x02\x03",

            "#214FAnd after I ran out here\x01",
            "to look for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "#200F#2PYeah! Plus being all, 'hey, mind\x01",
            "your own business'? That's like\x01",
            "ASKING us to follow you.\x02\x03",

            "Don't quite get the interest, though.\x01",
            "Nothing but burned-out shells and\x01",
            "ruins here. Place looks old, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        (
            "#197F#2PWe lived up on the northern\x01",
            "march a few years back, but...\x02\x03",

            "I never heard anything about a town\x01",
            "in the south burning to the ground.\x01",
            "Bit of a shock, this.\x02\x03",

            "#190FWhat was this village called, lad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "#1033F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #11
        0x8,
        "#1035F#6PHamel. That's what it was called...once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        "#213F#2PHamel... Never heard of it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, -180, 400)
    Sleep(300)

    ChrTalk(    #13
        0x9,
        "#212F#5PKyle, you ever heard of it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "#204F#2PDoesn't ring any bells, I'm afraid.\x02\x03",

            "#207FYou got anything, Don?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "#192F#5PHmmm... Hang about a second...\x02\x03",

            "#198FThe Imperial government might've said\x01",
            "something about a 'Hamel' way back when...\x02\x03",

            "#197FNo, been too long. Can't remember\x01",
            "what it was about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        "#413F#5PReal help, bro, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #17
        0x8,
        (
            "#1031F#6P...My business here is done.\x02\x03",

            "I...thank you for coming out here, even\x01",
            "though it doesn't really concern you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    Sleep(300)

    ChrTalk(    #18
        0x9,
        (
            "#413F#2PWell, it's no big, but... \x01",
            "mind if I ask something?\x02\x03",

            "#212FYou're acting way differently\x01",
            "than the first time we met.\x02\x03",

            "You aren't leading us on\x01",
            "or anything, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#1035F#6P...That's a little ironic, coming from you.\x02\x03",

            "#1031FAs I seem to recall, you were putting on\x01",
            "quite the performance when we first met.\x02\x03",

            "What I used to do was...\x01",
            "not really all that different.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #20
        0x9,
        (
            "#216F#2PWhaaaat...\x02\x03",

            "So, what, is this the\x01",
            "'real you' or something?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1033F#6P'The real me'... If you want to\x01",
            "think of it that way, you can.\x02\x03",

            "#1035FThe point is, I'm hardly a 'bracer' any\x01",
            "longer...and I'm certainly not the young\x01",
            "junior bracer you remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "#203F#2PHmm... We're obviously missing some details,\x01",
            "but I can respect the fact that you have your\x01",
            "own reasons for doing what you do.\x02\x03",

            "#200F'Sides. You seem a bit easier to trust now,\x01",
            "what with being more...honest, in a way.\x02\x03",

            "Not quite like before, when you were...\x01",
            "wearing a sheep's skin, I guess you'd\x01",
            "call it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "#1034F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#490F#2PBesides, we owe you for saving\x01",
            "us from the Royal Army.\x02\x03",

            "We'll let your little...insolences...\x01",
            "slide for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#1035F#6PYou hardly need to let anything\x01",
            "'slide.'\x02\x03",

            "#1031FI saved you because I\x01",
            "require some useful pawns.\x02\x03",

            "All I need is for you to work\x01",
            "enough to pay that debt back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "#198F#2PGuh. You really have a thing for\x01",
            "getting the last word in, don't you...?\x02\x03",

            "#490FWell, it doesn't matter to us. Your plan\x01",
            "is exactly what we needed, anyway.\x02\x03",

            "We'll be making plenty of use of you,\x01",
            "too, 'Mister Chessmaster.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#1031F#6P...As you wish.\x02\x03",

            "#1035FSimply remaining in my company\x01",
            "puts you in a great deal of danger.\x02\x03",

            "I will support you to the best of my\x01",
            "ability through what is to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#212F#2P'To the best of'...? Feh. Ungrateful,\x01",
            "unreliable, AND uncute!\x02\x03",

            "#215FAnd to think I thought, even for a second...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "#1034F#6PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "#214F#2PAhhhhhh, SHUT IT! Just drop it, okay?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "#203F#2PJosette, calm down.\x02\x03",

            "#200FThe point is, we're allies until\x01",
            "we all achieve our goals.\x02\x03",

            "#202FWe'll be countin' on you, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#1030F#6P...\x02\x03",

            "#1035FYes...as am I, with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "#490F#2PAhem! Well, shall we head out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#1031F#6PYes... Let's return.\x02",
    )

    CloseMessageWindow()

    def lambda_1372():
        OP_6D(-1950, -1000, 30090, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1372)

    def lambda_138A():
        OP_67(0, 7140, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_138A)

    def lambda_13A2():
        OP_6B(1840, 1500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_13A2)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    ChrTalk(    #35
        0x8,
        (
            "#1032F#5PTo the land being swallowed by\x01",
            "the creeping shadow...to Liberl.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400AD, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1040)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x122), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0xD, 0x0, 0x0, 0x0)

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1496")
    ShowSaveMenu()

    label("loc_1496")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_20(0x1388)
    OP_AE(0xC8)
    OP_24(0x1C3, 0x5F)
    Sleep(200)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x55)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x4B)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x41)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x37)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x2D)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x23)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_21()
    OP_23(0x1C3)
    Sleep(1000)
    OP_A3(0x1040)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1FC end

    def Function_3_154B(): pass

    label("Function_3_154B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x2)
    OP_22(0x1C3, 0x1, 0x46)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x101, -2830, -1000, 27070, 0)
    SetChrPos(0x102, -3640, -960, 28120, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(5280, -1000, 36730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    OP_D2(0x260201, 0x260206, 0x6)
    OP_D2(0x260202, 0x260207, 0x7)
    OP_D2(0x260203, 0x260208, 0x8)
    OP_D2(0x26022E, 0x260231, 0x9)
    OP_D2(0x260235, 0x26023A, 0xA)
    OP_D2(0x26022E, 0x260231, 0xB)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x102, 6)
    OP_7E(0xFD44, 0xFAD8, 0x96, 0x73, 0x1)
    FadeToBright(1000, 0)

    def lambda_164A():
        OP_6D(-2160, -1000, 29130, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_164A)

    def lambda_1662():
        OP_67(0, 7350, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1662)

    def lambda_167A():
        OP_6B(1790, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_167A)

    def lambda_168A():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_168A)

    def lambda_169A():
        OP_6E(444, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_169A)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #36
        0x102,
        (
            "#1035F#5PKarin, I'm back.\x02\x03",

            "#1041FHere, this is from Loewe.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_99(0x102, 0x0, 0x6, 0x3E8)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x102, 7)
    SetChrChipByIndex(0xD, 6)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x80)
    SetChrSubChip(0xD, 12)
    SetChrPos(0xD, -3650, -1100, 28360, 0)
    ClearChrFlags(0xD, 0x80)
    OP_0D()
    Sleep(1000)
    OP_99(0x102, 0x8, 0xB, 0x5DC)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #37
        0x102,
        "#1053F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1017FIt's so good to see that smile, Joshua.\x02\x03",

            "I bet Loewe likes it, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #39
        0x102,
        (
            "#1035F#5PYeah...\x02\x03",

            "#1043FLoewe and Karin were as close as\x01",
            "I've ever known two people to be...\x02\x03",

            "#1054FThey wanted to be together forever,\x01",
            "I think. And now they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1003FYeah...\x02\x03",

            "#1025FHey, can I say hi to Karin, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1053F#5POf course.\x02",
    )

    CloseMessageWindow()

    def lambda_18CC():
        OP_6D(-2620, -790, 29440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18CC)

    def lambda_18E4():
        OP_8F(0xFE, 0xFFFFF060, 0xFFFFFC18, 0x6B58, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18E4)
    Sleep(100)
    OP_8F(0x101, 0xFFFFF588, 0xFFFFFC22, 0x6D88, 0x3E8, 0x0)
    WaitChrThread(0x102, 0x2)

    def lambda_191D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_191D)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #42
        0x101,
        (
            "#1012F#2PUm, hi, Karin. Nice to meet you.\x02\x03",

            "#1006FI'm Estelle! Estelle Bright.\x02\x03",

            "I'm...well, for a little while I was sort of\x01",
            "trying to be his replacement sister without\x01",
            "knowing it...but I couldn't really replace you.\x01",
            "I guess now I'm, um, his girlfriend.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 11)
    SetChrSubChip(0x102, 0)
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(100)

    ChrTalk(    #43
        0x102,
        "#1048F#5PYou 'guess'? That's terrible.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 0)
    OP_99(0x101, 0x0, 0x2, 0x5DC)
    Sleep(100)

    ChrTalk(    #44
        0x101,
        (
            "#1013F#2PS-Sorry... Still not really used to it...\x02\x03",

            "It's kinda, y'know...embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1052F#5POh, for the...\x02\x03",

            "#1054F*sigh* It's still so very you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1019F#2PSo very what?\x01",
            "Do I detect an entendre, buster?\x02\x03",

            "Y'know, when nobody else is around,\x01",
            "you can sure be--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x2, 0x0, 0x7D0)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    def lambda_1C01():
        OP_99(0x102, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C01)

    ChrTalk(    #47
        0x101,
        (
            "#1013F#2PEr, sorry, I was in the middle of saying\x01",
            "hello, wasn't I.\x02\x03",

            "#1017FUm, so, I wanted to say hello, and come\x01",
            "with Joshua to see his original home.\x02\x03",

            "I... I'm looking forward to what's to\x01",
            "come for the two of us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x2)
    OP_0D()
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    Fade(250)
    SetChrSubChip(0x101, 9)
    SetChrChipByIndex(0xC, 8)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrSubChip(0xC, 12)
    SetChrPos(0xC, -2670, -900, 28900, 0)
    ClearChrFlags(0xC, 0x80)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #48
        0x101,
        "#1012F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1035F#5PThank you, Estelle.\x02\x03",

            "#1041FI'm sure Karin is very happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0xA, 0xB, 0x514)
    Sleep(200)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)

    def lambda_1DB6():
        OP_6D(-2830, -780, 28720, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DB6)
    OP_8F(0x101, 0xFFFFF524, 0xFFFFFC18, 0x6AFE, 0x3E8, 0x0)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 11)
    SetChrSubChip(0x102, 0)
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(100)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x0)
    Sleep(200)

    ChrTalk(    #50
        0x101,
        (
            "#1008F#2PHaha... I hope so.\x02\x03",

            "#1007FI know I'm still sort of a dunce, and\x01",
            "not the most reliable person ever...\x02\x03",

            "I have to admit I'm a bit worried what I'd do\x01",
            "if she ever thought, 'You're not good enough to\x01",
            "be Joshua's girlfriend, Estelle Bright! Shoo!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1054F#5PHaha. I think you're over thinking it a bit.\x02\x03",

            "#1053FIf anything, I think Karin would have\x01",
            "loved you.\x02\x03",

            "You two would've been a nice contrast,\x01",
            "in terms of personality.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 24)
    Sleep(300)

    ChrTalk(    #52
        0x101,
        "#1016F#2PHaha, you think so?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 25)
    Sleep(500)

    ChrTalk(    #53
        0x101,
        (
            "#1019F#2P...And there goes my entendre radar again,\x01",
            "mister.\x02\x03",

            "So you're saying I'm not as strong deep\x01",
            "down or as calm and quiet as your sister,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#1052F#5PUh-um, no! I really do think you're\x01",
            "strong deep down, actually.\x02\x03",

            "#1054FCalm and quiet...\x01",
            "Well, not exactly like Karin, no.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #55
        0x101,
        "#1007F#2PGeh...\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1041F#5PBut I'm not complaining.\x02\x03",

            "Always bright, optimistic, and shining\x01",
            "like the sun.\x02\x03",

            "#1049FThat's the girl I fell in love with.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(300)

    ChrTalk(    #57
        0x101,
        "#1004F#2P#3SAh!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #58
        0x101,
        (
            "#1013F#5PWh-Wh-Whaaaat was that...?\x02\x03",

            "You know how to go for the jugular\x01",
            "with the embarrassment, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1044F#5PSorry, did you not like it?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)
    Sleep(500)

    ChrTalk(    #60
        0x101,
        (
            "#1019F#2P#3SOf course I LIKED it!\x01",
            "That is so not the issue here!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1052F#5PI don't...quite get the problem,\x01",
            "I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1007F#2P*sigh*... Okay we've said our hellos,\x01",
            "so let's be off!\x02\x03",

            "I can see Karin rolling her eyes at us\x01",
            "from the cloud tops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1044F#5POh... Yeah. I guess.\x02\x03",

            "#1043F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1015F#2PHm? What is it?\x02",
    )

    CloseMessageWindow()
    OP_99(0x102, 0x2, 0x0, 0x5DC)
    Sleep(500)

    ChrTalk(    #65
        0x102,
        (
            "#1043F#5PAre you...really sure about this?\x02\x03",

            "You really want to leave Liberl and follow me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1004F#2POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#1035F#5PMy journey to atone for the sins I committed\x01",
            "in the society's name is my problem.\x02\x03",

            "So is my desire to strengthen myself\x01",
            "and live up to Loewe.\x02\x03",

            "#1043FI'm still not sure...if I want to wrap you\x01",
            "up in all this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 11)
    SetChrSubChip(0x101, 11)
    OP_99(0x101, 0xB, 0xD, 0x708)
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#1007F#2POh, for the love of...\x01",
            "You always miss the important part.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x102, 0x0, 0x2, 0x5DC)
    Sleep(500)

    ChrTalk(    #69
        0x102,
        "#1044F#5PHm?\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0xD, 0xF, 0x5DC)
    Sleep(300)

    ChrTalk(    #70
        0x101,
        (
            "#1006F#2PRagnard said it, didn't he?\x01",
            "This whole mess was just the beginning.\x02\x03",

            "Besides, I SERIOUSLY doubt the society's\x01",
            "plans are all played out.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0xF, 0x11, 0x5DC)
    Sleep(300)

    ChrTalk(    #71
        0x101,
        (
            "#1029F#2PAnd when those snakes strike from the grass\x01",
            "again, I want to be even stronger than Dad.\x02\x03",

            "You're not the only one who has someone\x01",
            "to live up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1054FStronger than Cassius...\x01",
            "That's a tall order.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x11, 0x13, 0x5DC)
    Sleep(300)

    ChrTalk(    #73
        0x101,
        "#1006F#2PWell, go big or go home, right?\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x13, 0x15, 0x5DC)
    Sleep(300)

    ChrTalk(    #74
        0x101,
        (
            "#1012F#2PPlus, I made that promise to Loewe.\x01",
            "And I really want to see more places\x01",
            "beyond Liberl!\x02\x03",

            "I'd also like to try and find Renne, if we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x15, 0x17, 0x5DC)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #75
        0x101,
        "#1008F#2P#1000FAnd...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(100)

    def lambda_2920():
        OP_6D(-3300, -780, 28870, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2920)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xFFFFF31C, 0xFFFFFC18, 0x6B08, 0x3E8, 0x0)
    Sleep(100)
    SetChrFlags(0x102, 0x800)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x101, 0x80)
    SetChrSubChip(0x102, 3)
    OP_99(0x102, 0x3, 0x7, 0x5DC)
    Sleep(500)

    ChrTalk(    #76
        0x102,
        "#1044F#5PEstelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006F#2PAND. C'mon, Joshua, do I really need a\x01",
            "reason to be with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1044F#5POh...\x02\x03",

            "#1040F...\x02\x03",

            "#1053FNo... Of course not.\x02\x03",

            "#1054FYou're all the reason you need,\x01",
            "all by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1016F#2PExactly!\x02\x03",

            "#1017FSee, Joshua, what would you do if I wasn't\x01",
            "around to point things out to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#1049F#5PHaha. You're right, I'd be doomed.\x02",
    )

    CloseMessageWindow()

    def lambda_2AEB():
        OP_99(0xFE, 0x8, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2AEB)

    def lambda_2AFB():
        OP_6D(-4070, -1000, 40590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AFB)

    def lambda_2B13():
        OP_67(0, 7350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B13)

    def lambda_2B2B():
        OP_6B(1790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B2B)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0xFDE4, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS177._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x400, 0x0, 0xFDE4, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS178._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x7, 0, -386000, 3000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(500)
    OP_C6(0x1, 0x3, -1, 0, 0)
    SetMessageWindowPos(80, 340, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #81
        (
            "\x07\x00Let's go, Estelle.\x02\x03",

            "I have no idea where this path will lead us...\x02\x03",

            "But I'm sure something awaits us at the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(340, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #82
        (
            "\x07\x00Yeah!\x02\x03",

            "One step at a time!\x01",
            "We'll walk it together to the end!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x2)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x7, 0, 0, 4000)
    OP_C7(0x0, 0x1, 0x0)
    Sleep(1000)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS179._CH")
    OP_C6(0x2, 0x3, -1, 3000, 0)
    Sleep(3500)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_56(0x2)
    OP_C6(0x2, 0x3, 16777215, 3000, 0)
    Sleep(4000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x31, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x417, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D7D")
    OP_A2(0x22B3)

    label("loc_2D7D")

    OP_A2(0x2242)
    OP_C4(0x0, 0x10)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x1B, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x31, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DAA")
    OP_A2(0x22B3)

    label("loc_2DAA")

    OP_3F(0x415, 1)
    OP_3F(0x418, 1)
    OP_3F(0x234, 1)
    OP_3F(0x5B, 1)
    OP_3F(0x151, 1)
    OP_A2(0x22AE)
    OP_A2(0x22B5)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #83
        (
            "\x07\x05～About Clear Data～\x01",
            "Congratulations on beating Trails in the Sky SC! If you save\x01",
            "your clear data and load it from the title screen, you can\x01",
            "play through the game again with all data carried forward!\x06\x18\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Save Clear Data\x01",             # 0
            "Return to Title Screen\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE8")
    OP_DD()
    EventBegin(0x4)

    label("loc_2EE8")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x10)
    OP_A3(0x2242)
    FadeToDark(0, 0, -1)
    OP_20(0xBB8)
    SetMapFlags(0x2000000)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_23(0x1C3)
    OP_21()
    Sleep(3000)
    OP_B4(0x1)
    Return()

    # Function_3_154B end

    SaveToFile()

Try(main)
