from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2412   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2412.x',
        MapIndex            = 103,
        MapDefaultBGM       = "ed60086",
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
        'Black-Clad Man',                       # 9
        'Black-Clad Man',                       # 10
        'Agate',                                # 11
        'Masked Commander',                     # 12
        'Target Camera',                        # 13
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
        Unknown_3A              = 103,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00341 ._CH',             # 00
        'ED6_DT07/CH00151 ._CH',             # 01
        'ED6_DT07/CH00152 ._CH',             # 02
        'ED6_DT07/CH00260 ._CH',             # 03
        'ED6_DT07/CH00340 ._CH',             # 04
        'ED6_DT07/CH00341 ._CH',             # 05
        'ED6_DT07/CH00342 ._CH',             # 06
        'ED6_DT07/CH00344 ._CH',             # 07
        'ED6_DT07/CH00260 ._CH',             # 08
        'ED6_DT07/CH00261 ._CH',             # 09
        'ED6_DT07/CH00262 ._CH',             # 0A
        'ED6_DT07/CH00264 ._CH',             # 0B
        'ED6_DT07/CH00265 ._CH',             # 0C
        'ED6_DT07/CH02200 ._CH',             # 0D
        'ED6_DT06/CH20137 ._CH',             # 0E
        'ED6_DT06/CH20138 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH00341P._CP',             # 00
        'ED6_DT07/CH00151P._CP',             # 01
        'ED6_DT07/CH00152P._CP',             # 02
        'ED6_DT07/CH00260P._CP',             # 03
        'ED6_DT07/CH00340P._CP',             # 04
        'ED6_DT07/CH00341P._CP',             # 05
        'ED6_DT07/CH00342P._CP',             # 06
        'ED6_DT07/CH00344P._CP',             # 07
        'ED6_DT07/CH00260P._CP',             # 08
        'ED6_DT07/CH00261P._CP',             # 09
        'ED6_DT07/CH00262P._CP',             # 0A
        'ED6_DT07/CH00264P._CP',             # 0B
        'ED6_DT07/CH00265P._CP',             # 0C
        'ED6_DT07/CH02200P._CP',             # 0D
        'ED6_DT06/CH20137P._CP',             # 0E
        'ED6_DT06/CH20138P._CP',             # 0F
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -2060,
        TriggerZ            = 0,
        TriggerY            = 120820,
        TriggerRange        = 1500,
        ActorX              = -2060,
        ActorZ              = 1500,
        ActorY              = 120820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_1F3",          # 01, 1
        "Function_2_206",          # 02, 2
        "Function_3_24DC",         # 03, 3
        "Function_4_25C2",         # 04, 4
        "Function_5_2663",         # 05, 5
        "Function_6_283B",         # 06, 6
        "Function_7_2888",         # 07, 7
        "Function_8_28B5",         # 08, 8
        "Function_9_28E2",         # 09, 9
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Event(0, 2)
    Return()

    # Function_0_1EE end

    def Function_1_1F3(): pass

    label("Function_1_1F3")

    OP_16(0x2, 0xFA0, 0xFFFDECC0, 0xFFFF34E0, 0x30025)
    Return()

    # Function_1_1F3 end

    def Function_2_206(): pass

    label("Function_2_206")

    FadeToBright(2000, 0)
    LoadEffect(0x0, "craft\\\\cr201_00.eff")
    LoadEffect(0x1, "craft\\\\cr201_01.eff")
    LoadEffect(0x2, "craft\\\\cr201_02.eff")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-4600, 3000, 117500, 0)
    OP_6B(3400, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6C(52000, 0)
    SetChrPos(0x8, -4900, 0, 125700, 0)
    SetChrPos(0x9, -3900, 0, 125000, 0)
    SetChrPos(0xA, 5300, 0, 139100, 0)

    def lambda_2C5():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C5)
    OP_6D(-4600, 0, 117500, 5000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_2F5():
        OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0x1C4BC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F5)

    def lambda_310():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0x1CAFC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_310)
    WaitChrThread(0x9, 0x1)

    def lambda_330():
        OP_8C(0x9, 0, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_330)
    WaitChrThread(0x8, 0x1)

    def lambda_343():
        OP_8C(0x8, 0, 800)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_343)

    ChrTalk(    #0
        0x8,
        "#2P*huff* *huff*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "#2PStubborn bastard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2 op#A op#5
        0xA,
        "#10A#4PHey, hey, hey!\x05\x02",
    )

    Sleep(1300)

    def lambda_3A1():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A1)
    OP_43(0xA, 0x1, 0x0, 0x5)

    ChrTalk(    #3 op#A op#5
        0x9,
        (
            "#25A#6PAnd how the heck is he keeping\x01",
            "up with such a huge sword?!\x05\x02",
        )
    )

    Sleep(200)
    OP_43(0x8, 0x1, 0x0, 0x3)
    Sleep(200)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_6A(0x9)
    Sleep(2800)

    ChrTalk(    #4 op#A op#5
        0xA,
        (
            "#25A#1PHa...my training methods are\x01",
            "a little different.\x05\x02",
        )
    )

    Sleep(2700)

    ChrTalk(    #5 op#A op#5
        0xA,
        "#12A#5S#5PRrrrraaaaaahhhhh!\x05\x02",
    )

    WaitChrThread(0xA, 0x1)

    def lambda_487():
        OP_6C(348000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_487)
    Sleep(500)
    OP_96(0xA, 0xFFFFE0C0, 0x0, 0xE358, 0x1F4, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    OP_99(0xA, 0x7, 0x0, 0x7D0)
    ClearChrFlags(0xA, 0x800)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        "#6PDamn... We can't shake him!\x02",
    )

    CloseMessageWindow()

    def lambda_4EF():

        label("loc_4EF")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4EF")

    QueueWorkItem2(0x8, 0, lambda_4EF)

    def lambda_500():

        label("loc_500")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_500")

    QueueWorkItem2(0x9, 0, lambda_500)

    def lambda_511():
        OP_96(0x8, 0xFFFFECE6, 0x1E, 0xCB3E, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_511)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    Sleep(100)

    def lambda_543():
        OP_96(0x9, 0xFFFFE3CC, 0x14, 0xC648, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_543)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #7
        0x9,
        (
            "We have no choice!\x01",
            "Time to counter-attack!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "#051FI guess you're finally taking\x01",
            "me seriously.\x02\x03",

            "Good. I was getting sick of playing\x01",
            "tag with you fools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "He's not going to give up until\x01",
            "he's dead...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "What a stubborn idiot...\x01",
            "Does he really think he can\x01",
            "beat 2-to-1 odds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        "#051FHa ha. I think I already have.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "What...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "#054FEvery fight takes spirit. You lose\x01",
            "that, you've lost everything.\x02\x03",

            "And I figured out exactly what kind of\x01",
            "spirit you losers had when you took off\x01",
            "with your tails between your legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "S-Silence, guilder dog!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "We can handle you. You're in\x01",
            "for a painful death!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7DC():
        OP_6E(243, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_7DC)

    def lambda_7EC():
        OP_6D(-7660, 0, 57680, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7EC)
    PlayEffect(0x1, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_839():
        OP_99(0xFE, 0x0, 0x4, 0xA28)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_839)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)

    def lambda_861():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_861)

    def lambda_877():
        OP_94(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_877)
    Sleep(500)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Sleep(100)

    def lambda_89F():
        OP_94(0x1, 0xFE, 0x0, 0x2328, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_89F)
    Sleep(50)

    def lambda_8BA():
        OP_94(0x1, 0xFE, 0x0, 0x2328, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8BA)
    Sleep(400)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0xFF, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_90D():
        OP_99(0xFE, 0x4, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_90D)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 7)
    SetChrFlags(0x8, 0x20)

    def lambda_96C():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_96C)
    Sleep(50)
    PlayEffect(0x2, 0xFF, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 7)
    SetChrFlags(0x9, 0x20)

    def lambda_9D1():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9D1)

    def lambda_9E7():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9E7)
    Sleep(50)

    def lambda_A02():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A02)

    def lambda_A18():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A18)
    Sleep(50)

    def lambda_A33():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A33)

    def lambda_A49():
        OP_94(0x1, 0xFE, 0xB4, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A49)
    Sleep(50)

    def lambda_A64():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A64)

    def lambda_A7A():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A7A)
    Sleep(50)

    def lambda_A95():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A95)
    Sleep(450)
    Fade(1000)
    OP_44(0x0, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_6D(-7670, 0, 56050, 0)
    OP_6B(3000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6C(45000, 0)
    SetChrPos(0x8, -8400, 0, 54200, 0)
    SetChrPos(0x9, -9800, 0, 54800, 0)
    SetChrPos(0xB, -6700, 0, 58700, 180)
    TurnDirection(0xA, 0x8, 0)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)
    PlayEffect(0x2, 0xFF, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    ChrTalk(    #16
        0x8,
        "#2PGaaaahhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#2PD-Damn it...\x01",
            "We can't get caught now...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BEF():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BEF)

    def lambda_BFD():
        OP_99(0xFE, 0x5, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BFD)
    OP_96(0xA, 0xFFFFE37C, 0x0, 0xDC50, 0x2BC, 0xFA0)
    OP_44(0xA, 0x2)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(    #18
        0xA,
        (
            "#050F#6PHeh. Okay, how about you just\x01",
            "surrender and give me your full\x01",
            "confessions?\x02\x03",

            "Starting with who you are and\x01",
            "what you're after.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    SetChrPos(0xB, -4010, 0, 61460, 270)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #19
        0xB,
        "Man's Voice",
        (
            "#4PYou needn't concern yourself\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)
    OP_8C(0xA, 43, 600)

    ChrTalk(    #20
        0xA,
        "#052F#6PWha--?!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x51)
    SetChrChipByIndex(0xB, 13)
    ClearChrFlags(0xB, 0x80)

    def lambda_D6E():
        OP_6D(-6790, 0, 56980, 1500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D6E)

    def lambda_D86():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_D86)

    def lambda_D98():
        OP_8E(0xFE, 0xFFFFE5D4, 0x0, 0xE54C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D98)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 7)

    def lambda_DBD():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DBD)
    OP_96(0xA, 0xFFFFE890, 0x0, 0xD6D8, 0x2BC, 0xFA0)
    Sleep(500)

    ChrTalk(    #21
        0xA,
        "#055F#4PWh-When did you get here?\x02",
    )

    CloseMessageWindow()

    def lambda_E0E():
        OP_99(0x8, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E0E)

    ChrTalk(    #22
        0x8,
        "C-Commander!\x02",
    )

    CloseMessageWindow()

    def lambda_E30():
        OP_99(0x9, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E30)

    ChrTalk(    #23
        0x9,
        "You came for us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "#281FYou two are pitiful.\x02\x03",

            "You fail to report in as appointed,\x01",
            "and this is why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "W-We have no excuses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "We've had a lot of interference...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#050F#4PI get it... So you're the man\x01",
            "in charge?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)
    Sleep(400)

    ChrTalk(    #28
        0xB,
        (
            "#280FHa ha...\x01",
            "Only of this particular scene.\x02\x03",

            "Allow me to apologize on behalf\x01",
            "of my men. Could I persuade you\x01",
            "to overlook this incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "#055F#4PHuh?\x02\x03",

            "Okay, repeat that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "#280FI said that I'd like for you to\x01",
            "overlook this incident.\x02\x03",

            "We never had any intention of\x01",
            "running afoul of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "#054F#4PDon't make me laugh. You think I'm just\x01",
            "going to look the other way, and let you\x01",
            "get away with what you did?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "#281FAh, well. I had thought it a generous\x01",
            "offer, personally. Certainly a fairer\x01",
            "price than death.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)
    Sleep(400)

    ChrTalk(    #33
        0xB,
        (
            "#281FBoth of you, stand down.\x02\x03",

            "Return to the rendezvous point\x01",
            "at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(    #34
        0x8,
        "Y-Yes, sir!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 5)
    ClearChrFlags(0x8, 0x20)

    def lambda_11C8():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xAB7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11C8)

    ChrTalk(    #35
        0x9,
        "Thank you, commander!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 5)
    ClearChrFlags(0x8, 0x20)

    def lambda_1208():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xAB7C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1208)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)

    def lambda_122D():

        label("loc_122D")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_122D")

    QueueWorkItem2(0xA, 1, lambda_122D)
    Sleep(300)
    OP_44(0xA, 0xFF)

    ChrTalk(    #36
        0xA,
        "#054FWhere do you think you're going?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xB, 9)
    OP_8E(0xB, 0xFFFFE318, 0x0, 0xDEA8, 0x1B58, 0x0)

    def lambda_128C():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_128C)

    def lambda_129C():
        OP_6D(-9340, 0, 52260, 1000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_129C)

    def lambda_12B4():
        OP_97(0xFE, 0xFFFFEC14, 0xD034, 0xFFFEDB08, 0x36B0, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_12B4)
    SetChrChipByIndex(0xA, 1)
    OP_8E(0xA, 0xFFFFDF94, 0x0, 0xCF08, 0x1B58, 0x0)
    TurnDirection(0xA, 0xB, 0)

    def lambda_12F0():

        label("loc_12F0")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_12F0")

    QueueWorkItem2(0xB, 0, lambda_12F0)
    SetChrChipByIndex(0xA, 14)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)

    def lambda_1321():
        OP_96(0xFE, 0xFFFFE124, 0xFFFFFFCE, 0xD0AC, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1321)
    OP_22(0x1F5, 0x0, 0x64)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 800)
    OP_8F(0xB, 0xFFFFD760, 0x0, 0xC738, 0xFA0, 0x0)
    Sleep(500)
    WaitChrThread(0xB, 0x3)

    ChrTalk(    #37
        0xB,
        "#280F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "#057F#4PSon of a...\x02\x03",

            "#053FHeh, fine. The target may have\x01",
            "changed, but as long as I have\x01",
            "one...\x02\x03",

            "And you being the leader, I assume\x01",
            "you've got better information to offer\x01",
            "me than your underlings, anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "#280FHa... You think it'll be that\x01",
            "easy to make me talk?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_148C():

        label("loc_148C")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_148C")

    QueueWorkItem2(0xA, 0, lambda_148C)

    ChrTalk(    #40
        0xA,
        "#054F#4PI sure as hell intend to find out!\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x2B)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    def lambda_14E4():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_14E4)
    ClearChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 1)
    OP_94(0x1, 0xA, 0xB4, 0x1F4, 0x3E8, 0x0)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x3E8)
    OP_6A(0xC)
    OP_43(0x8, 0x1, 0x0, 0x6)
    OP_93(0xA, 0xB, 0x640, 0x2EE0, 0x0)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xB, 12)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_1589():
        OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1589)

    def lambda_159F():
        OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_159F)
    OP_9E(0xB, 0x1E, 0x0, 0x12C, 0x1388)
    WaitChrThread(0xB, 0x1)

    def lambda_15CD():
        OP_94(0x1, 0xFE, 0x0, 0x5DC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15CD)
    SetChrChipByIndex(0xB, 8)
    SetChrSubChip(0xB, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 7)
    OP_96(0xB, 0xFFFFCFF4, 0x514, 0xC47C, 0x578, 0x3A98)
    Sleep(100)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)
    OP_44(0xB, 0xFF)

    def lambda_162C():
        OP_96(0xFE, 0xFFFFD828, 0x514, 0xC670, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_162C)

    def lambda_164A():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_164A)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_1664():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xCF08, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1664)

    def lambda_1682():

        label("loc_1682")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1682")

    QueueWorkItem2(0xB, 0, lambda_1682)
    SetChrChipByIndex(0xA, 1)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xB, 0xFFFFDAE4, 0x0, 0xBAB8, 0x3E8, 0x2710)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_16BE():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_16BE)
    OP_6B(2900, 1000)
    SetChrChipByIndex(0xB, 9)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0xB, 0xFFFFDF94, 0x0, 0xC030, 0x1F4, 0xBB8)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1703():
        OP_6B(2500, 1000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1703)
    OP_96(0xB, 0xFFFFD954, 0x0, 0xC3B4, 0x1F4, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_172F():
        OP_8C(0xA, 30, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_172F)
    OP_96(0xB, 0xFFFFE188, 0x0, 0xCA58, 0x1F4, 0x2710)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1759():
        OP_96(0xB, 0xFFFFDCD8, 0x0, 0xCB20, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1759)
    OP_44(0xA, 0xFF)
    OP_22(0x1F9, 0x0, 0x64)
    OP_8C(0xA, 315, 1300)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 8)

    def lambda_1797():
        OP_96(0xFE, 0xFFFFDAE4, 0x1F4, 0xCABC, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1797)
    OP_8C(0xA, 135, 1600)
    Sleep(350)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_17D1():
        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_17D1)
    OP_8C(0xA, 225, 0)
    SetChrChipByIndex(0xA, 2)
    OP_99(0xA, 0x6, 0x7, 0x5DC)

    def lambda_17F6():
        OP_99(0xA, 0x5, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_17F6)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_180B():
        OP_99(0xFE, 0x2, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_180B)

    def lambda_181B():
        OP_96(0xB, 0xFFFFDD3C, 0x0, 0xDDE0, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_181B)
    Sleep(200)

    def lambda_183E():
        OP_8C(0xA, 0, 500)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_183E)
    Sleep(300)

    def lambda_1851():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1851)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_186B():
        OP_96(0xA, 0xFFFFDD3C, 0x0, 0xDA5C, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_186B)

    def lambda_1889():
        OP_99(0xA, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1889)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(200)

    def lambda_18A8():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18A8)
    OP_8F(0xB, 0xFFFFE34A, 0x0, 0xDDE0, 0x3A98, 0x0)
    WaitChrThread(0xA, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, -8610, -1000, 56740, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_96(0xB, 0xFFFFEC78, 0x0, 0xDD7C, 0x514, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(1000)

    def lambda_1942():
        OP_99(0xA, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1942)

    def lambda_1952():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1952)
    Sleep(500)

    ChrTalk(    #41
        0xA,
        (
            "#051FHmm... Not bad.\x01",
            "Not bad at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "#281FYou have an irrepressible passion,\x01",
            "but a great weight bears down upon\x01",
            "you...\x02\x03",

            "You are not...quite so different\x01",
            "from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#052F...\x02\x03",

            "...What did you just say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "#280FIt's a painful thing to be powerless\x01",
            "in a time of crisis. But you know\x01",
            "that feeling all too well, no?\x02\x03",

            "I can see it in your eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#052F...\x02\x03",

            "#053FHa ha ha, fine then.\x02\x03",

            "I don't know who you are,\x01",
            "but I think I like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        (
            "#280FThere is no shame in powerlessness.\x01",
            "There is no shame in being outmatched.\x01",
            "You and I both know that.\x02\x03",

            "Perhaps we could come to a mutually\x01",
            "beneficial arrangement...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        "#057F#5S#3PScrew you!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgaria0.eff")

    def lambda_1C13():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C13)
    PlayEffect(0x0, 0x0, 0xA, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(    #48
        0xA,
        (
            "#057F#3PDon't act like you know\x01",
            "anything about me!\x02\x03",

            "You're in for one hell of a\x01",
            "beatdown!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)

    ChrTalk(    #49
        0xB,
        "#280FHeh...\x02",
    )

    CloseMessageWindow()
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 12)

    def lambda_1CEB():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CEB)
    PlayEffect(0x0, 0x1, 0xB, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_1D3A():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D3A)
    Sleep(1000)

    def lambda_1D59():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1D59)

    def lambda_1D69():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D69)

    ChrTalk(    #50 op#A op#5
        0xA,
        "#15A#054FHyaaaaaahhhh!!\x05\x02",
    )

    Sleep(3000)

    def lambda_1DA5():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1DA5)

    ChrTalk(    #51 op#A op#5
        0xB,
        "#15A#282FRooooaaaaggh!!\x05\x02",
    )

    Sleep(3000)
    Sleep(500)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    OP_99(0xA, 0x0, 0x3, 0x7D0)

    def lambda_1DFD():
        OP_99(0xA, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1DFD)

    def lambda_1E0D():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1E0D)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 10)

    def lambda_1E34():
        OP_99(0xFE, 0x0, 0x3, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1E34)

    def lambda_1E44():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xDA5C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E44)

    def lambda_1E5F():
        OP_8E(0xFE, 0xFFFFEC78, 0x0, 0xDD7C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E5F)
    Sleep(100)
    OP_20(0x0)
    OP_22(0x9B, 0x0, 0x64)
    FadeToDark(1, 16777215, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    FadeToBright(200, 16777215)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    PlayEffect(0x0, 0x0, 0xC, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    PlayEffect(0x0, 0x1, 0xC, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    def lambda_1F27():
        OP_99(0xFE, 0x3, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1F27)

    ChrTalk(    #52
        0xB,
        "#281FGah...\x02",
    )

    OP_9E(0xB, 0x32, 0x0, 0x1F4, 0x1388)
    CloseMessageWindow()
    WaitChrThread(0xB, 0x3)
    SetChrChipByIndex(0xB, 11)
    OP_99(0xB, 0x1, 0x3, 0x4B0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1F7C():
        OP_99(0xA, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F7C)
    OP_8C(0xA, 225, 400)
    Sleep(500)

    ChrTalk(    #53
        0xA,
        (
            "#051FHeh... All talk, no shock.\x02\x03",

            "Bet the guild's going to looove\x01",
            "interrogating you...\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x99, 0x0, 0x64)
    OP_43(0xB, 0x1, 0x0, 0x7)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 0)
    Sleep(1000)

    ChrTalk(    #54
        0xA,
        "#052FWh-What the...?\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x8)
    Sleep(1000)
    OP_44(0xB, 0x1)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Sleep(500)

    ChrTalk(    #55
        0xA,
        "#055FIs that...the Body-Split Craft?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05Agate sensed something faint from the dark forest beyond.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_1D(0x53)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")
    SetMessageWindowPos(75, 250, -1, -1)

    AnonymousTalk(    #57
        "\x07\x05#25WHeh heh heh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrName("Man's Voice")

    AnonymousTalk(    #58
        (
            "#25WNice try, but you've got\x01",
            "a heavy heart.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #59
        (
            "#25WAnd a heavy heart makes for\x01",
            "a light blade...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #60
        0xA,
        (
            "#057FWhy don't you come out from\x01",
            "hiding and say that?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #61
        (
            "#25WWhen a warrior enters a skirmish,\x01",
            "he must be prepared to lose everything.\x01",
            "Otherwise, he can gain nothing.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #62
        (
            "#25WIn order to live as a man...you\x01",
            "must forgo all anger and grief.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #63
        "#40WWith that, I bid you farewell...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #64
        "\x07\x05The presence in the trees seemed to have vanished.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x1)

    def lambda_2369():
        OP_6D(-5100, 1400, 56900, 1600)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2369)
    WaitChrThread(0xA, 0x2)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 0)
    OP_9E(0xA, 0x14, 0x0, 0x3E8, 0x1388)

    ChrTalk(    #65
        0xA,
        (
            "#056F#50W#5P...\x02\x03",

            "#50WForgo...?\x02\x03",

            "#50WHow the hell am I supposed to\x01",
            "do that...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23F6():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_23F6)

    def lambda_2406():
        OP_67(0, 6000, -10000, 2300)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2406)

    def lambda_241E():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_241E)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_243C():
        OP_6B(5000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_243C)

    def lambda_244C():

        label("loc_244C")

        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0x1388)
        OP_48()
        Jump("loc_244C")

    QueueWorkItem2(0xA, 0, lambda_244C)
    SetChrSubChip(0xA, 1)

    ChrTalk(    #66 op#A op#5
        0xA,
        "#550F#5P#22A#5SAaaaarrrrrrrggh!\x05\x02",
    )

    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_AD(0x4003F, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x3FF)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_206 end

    def Function_3_24DC(): pass

    label("Function_3_24DC")

    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x2710, 0x0)

    def lambda_251E():
        OP_6C(324000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_251E)

    def lambda_252E():
        OP_67(0, 5200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_252E)

    def lambda_2546():
        OP_6D(-8000, 1300, 66400, 2700)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2546)
    ClearMapFlags(0x1)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0x10CC0, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFEC14, 0x0, 0xFBF4, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0xE54C, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFDA80, 0x0, 0xBD74, 0x32C8, 0x0)
    Return()

    # Function_3_24DC end

    def Function_4_25C2(): pass

    label("Function_4_25C2")

    SetChrFlags(0xFE, 0x40)
    OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x2710, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x2AF8, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0x10CC0, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFEC14, 0x0, 0xFBF4, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFE7C8, 0x0, 0xE54C, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0xC670, 0x2EE0, 0x0)
    Return()

    # Function_4_25C2 end

    def Function_5_2663(): pass

    label("Function_5_2663")

    OP_8E(0xFE, 0x0, 0x0, 0x20850, 0x2EE0, 0x0)
    OP_8E(0xFE, 0xFFFFDF30, 0x0, 0x186A0, 0x32C8, 0x0)
    OP_8E(0xFE, 0xFFFFD634, 0x0, 0x15180, 0x36B0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x0, 0x11A08, 0x3A98, 0x0)
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    SetChrFlags(0xFE, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0xFE, 0xFFFFE0C0, 0x5DC, 0x10360, 0x7D0, 0x1F40)

    def lambda_26E2():
        OP_6D(-7300, 0, 56400, 600)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_26E2)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 2)

    def lambda_2704():
        OP_99(0xA, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2704)

    def lambda_2714():
        OP_6C(24000, 800)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2714)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2729():
        OP_96(0xFE, 0xFFFFE37C, 0x0, 0xDC50, 0x7D0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2729)
    WaitChrThread(0xA, 0x0)

    def lambda_274C():
        OP_99(0xA, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_274C)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0xA, 0x3)
    OP_22(0x55, 0x0, 0x5A)
    PlayEffect(0x12, 0xFF, 0xFF, -6800, -2500, 55400, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x8, 0xA, 0)
    TurnDirection(0x9, 0xA, 0)

    def lambda_27C7():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27C7)

    def lambda_27DD():
        OP_96(0xFE, 0xFFFFEA84, 0x0, 0xD5AC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_27DD)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0xA, 400)

    def lambda_2807():
        OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2807)
    WaitChrThread(0x8, 0x1)

    def lambda_2822():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2822)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    Return()

    # Function_5_2663 end

    def Function_6_283B(): pass

    label("Function_6_283B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2887")
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_6_283B")

    label("loc_2887")

    Return()

    # Function_6_283B end

    def Function_7_2888(): pass

    label("Function_7_2888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28B4")
    Sleep(100)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    Sleep(100)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    Jump("Function_7_2888")

    label("loc_28B4")

    Return()

    # Function_7_2888 end

    def Function_8_28B5(): pass

    label("Function_8_28B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28E1")
    Sleep(50)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    Sleep(50)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    Jump("Function_8_28B5")

    label("loc_28E1")

    Return()

    # Function_8_28B5 end

    def Function_9_28E2(): pass

    label("Function_9_28E2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #67
        (
            "\x07\x05North: Ruan\x01",
            "South: Air-Letten - 175 selge \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_28E2 end

    SaveToFile()

Try(main)
