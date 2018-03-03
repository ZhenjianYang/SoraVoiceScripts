from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2410   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Pot',                                  # 9
        'Tea',                                  # 10
        'Tea',                                  # 11
        'Tea',                                  # 12
        'Tea',                                  # 13
        'Matron Theresa',                       # 14
        'Daniel',                               # 15
        'Mary',                                 # 16
        'Clem',                                 # 17
        'Polly',                                # 18
        'Jill',                                 # 19
        'Kettle Lid',                           # 20
        'Target Camera',                        # 21
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02590 ._CH',             # 03
        'ED6_DT07/CH02500 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT06/CH20021 ._CH',             # 09
        'ED6_DT07/CH02573 ._CH',             # 0A
        'ED6_DT07/CH02390 ._CH',             # 0B
        'ED6_DT07/CH02393 ._CH',             # 0C
        'ED6_DT06/CH20094 ._CH',             # 0D
        'ED6_DT06/CH20095 ._CH',             # 0E
        'ED6_DT06/CH20096 ._CH',             # 0F
        'ED6_DT06/CH20097 ._CH',             # 10
        'ED6_DT26/CH20784 ._CH',             # 11
        'ED6_DT26/CH20278 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02590P._CP',             # 03
        'ED6_DT07/CH02500P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT06/CH20021P._CP',             # 09
        'ED6_DT07/CH02573P._CP',             # 0A
        'ED6_DT07/CH02390P._CP',             # 0B
        'ED6_DT07/CH02393P._CP',             # 0C
        'ED6_DT06/CH20094P._CP',             # 0D
        'ED6_DT06/CH20095P._CP',             # 0E
        'ED6_DT06/CH20096P._CP',             # 0F
        'ED6_DT06/CH20097P._CP',             # 10
        'ED6_DT26/CH20784P._CP',             # 11
        'ED6_DT26/CH20278P._CP',             # 12
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703944,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
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
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 14600,
        Direction           = 0,
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
        X                   = 35100,
        Z                   = 0,
        Y                   = 2300,
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
        X                   = 35300,
        Z                   = 0,
        Y                   = -35300,
        Direction           = 270,
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
        X                   = -3400,
        Z                   = 0,
        Y                   = 1700,
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
        X                   = 32500,
        Z                   = 0,
        Y                   = -34400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 65554,
        ChipIndex           = 0x12,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2E2",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_30C",          # 02, 2
        "Function_3_322",          # 03, 3
        "Function_4_1929",         # 04, 4
        "Function_5_1993",         # 05, 5
        "Function_6_19CF",         # 06, 6
        "Function_7_1A17",         # 07, 7
        "Function_8_1A5F",         # 08, 8
        "Function_9_1ADD",         # 09, 9
        "Function_10_1B05",        # 0A, 10
        "Function_11_1B66",        # 0B, 11
        "Function_12_1BE6",        # 0C, 12
        "Function_13_331F",        # 0D, 13
        "Function_14_334F",        # 0E, 14
        "Function_15_337D",        # 0F, 15
        "Function_16_33B2",        # 10, 16
        "Function_17_3407",        # 11, 17
    )


    def Function_0_2E2(): pass

    label("Function_0_2E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_301")
    SetMapFlags(0x10000000)
    Event(0, 12)
    Jump("loc_30A")

    label("loc_301")

    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_30A")

    Return()

    # Function_0_2E2 end

    def Function_1_30B(): pass

    label("Function_1_30B")

    Return()

    # Function_1_30B end

    def Function_2_30C(): pass

    label("Function_2_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_30C")

    label("loc_321")

    Return()

    # Function_2_30C end

    def Function_3_322(): pass

    label("Function_3_322")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-560, 0, 3500, 0)
    OP_67(0, 3800, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(30000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x105, -1400, 0, -3500, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -1580, 0, 4620, 270)
    SetChrPos(0x18, -1200, 0, -3500, 180)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -4260, 600, 6460, 0)
    SetChrPos(0x12, -4260, 600, 5460, 0)
    SetChrPos(0x13, -3560, 600, 5460, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)

    def lambda_41F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_41F)

    def lambda_431():
        OP_8E(0xFE, 0xFFFFFC54, 0x0, 0xA50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_431)
    Sleep(1000)

    def lambda_451():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_451)

    def lambda_463():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_463)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)

    ChrTalk(    #0
        0x105,
        "#044F#12P...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0x1)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x15, 0x18, 400)
    Sleep(300)

    ChrTalk(    #1
        0x15,
        (
            "#752F#5PThere you are, Clem! Where have you\x01",
            "been all this time?\x02\x03",

            "Everyone else has long--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    def lambda_53D():

        label("loc_53D")

        TurnDirection(0xFE, 0x105, 600)
        OP_48()
        Jump("loc_53D")

    QueueWorkItem2(0x18, 2, lambda_53D)
    Sleep(600)

    def lambda_553():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0x9EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_553)
    Sleep(100)

    def lambda_573():
        OP_8F(0xFE, 0x50, 0x0, 0x8C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_573)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    ChrTalk(    #2
        0x15,
        (
            "#753F#5PGoodness...\x02\x03",

            "#751FIs that you, Kloe?\x02\x03",

            "You've grown so much, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#049F#12P#40WMatron, I...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_612():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_612)
    Sleep(1000)

    ChrTalk(    #4 op#A op#5
        0x105,
        "#043F#12P#30AIt's you... It's really you!\x05\x02",
    )

    Sleep(500)
    OP_21()
    OP_1D(0xB2)
    Sleep(500)

    def lambda_66D():
        OP_6B(2960, 800)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_66D)

    def lambda_67D():
        OP_8F(0xFE, 0xFFFFFAB0, 0x0, 0x870, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67D)
    Sleep(580)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 17)
    SetChrSubChip(0x105, 0)

    def lambda_6B6():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0xA50, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6B6)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #5
        0x105,
        "#049F#12PI-I... I...\x02",
    )

    CloseMessageWindow()
    OP_43(0x105, 0x2, 0x0, 0x4)
    Sleep(2000)

    ChrTalk(    #6
        0x15,
        (
            "#751F#5POh, dear. I see you still look exactly\x01",
            "the same when you're crying.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0x2)

    ChrTalk(    #7
        0x105,
        "#047F#12PW-Well, I...I...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0xFFFFFFCE, 2000, 0x18, 0x1B, 0x12C, 0x0)
    OP_43(0x105, 0x2, 0x0, 0x4)
    Sleep(2000)

    ChrTalk(    #8
        0x18,
        (
            "#774F#11PWha...?\x02\x03",

            "Wh-What's going on here?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)
    OP_44(0x105, 0x2)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)

    def lambda_7E9():
        OP_6B(3060, 1000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_7E9)

    def lambda_7F9():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0x564, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7F9)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        (
            "#045F#12PHeehee...\x02\x03",

            "#540FI-I'm sorry... I didn't mean to hug you out\x01",
            "of nowhere. Before I knew it, I...\x02\x03",

            "I was just so happy to see you again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x15,
        (
            "#750F#5POh, that's no reason for you to apologize.\x02\x03",

            "#751FIt's lovely to see you again, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        "#048F#12PYou, too! *sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x15,
        (
            "#751F#5POh, look at you. You're still the same darling\x01",
            "young lady I've always known after all, aren't\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x18, 380)
    Sleep(300)

    ChrTalk(    #13
        0x15,
        (
            "#750F#1PI'm glad you finally came back, too, Clem.\x02\x03",

            "But I wish you wouldn't run away like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #14
        0x18,
        "#772F#11PI-I just went to look for something, that's all!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x105, 300, 500)
    Sleep(600)
    OP_8C(0x105, 30, 500)
    Sleep(600)
    OP_8C(0x105, 345, 500)
    Sleep(500)

    ChrTalk(    #15
        0x105,
        (
            "#542F#12PUmm... If you don't mind me asking, Matron...\x01",
            "where is Joseph?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x105, 380)
    Sleep(500)

    ChrTalk(    #16
        0x15,
        (
            "#754F#5P...\x02\x03",

            "You haven't heard the news, then?\x02\x03",

            "#757FI'm afraid he's no longer with us.\x02\x03",

            "He passed away about four years\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#044F#12P...\x02\x03",

            "#40WHe...passed away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x15,
        (
            "#754F#5POne day, he went out shopping in Ruan\x01",
            "and was caught up in an accident.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(300)

    def lambda_C0A():
        OP_8F(0xFE, 0xFFFFFA88, 0x0, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C0A)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #19
        0x105,
        (
            "#043F#40W#12P...\x02\x03",

            "#049F...I'm... I'm so sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x15,
        "#750F#5PSweetie, why are you apologizing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#542F#12P#40WI... I had no idea...\x02\x03",

            "If I hadn't been acting so stubbornly...\x02\x03",

            "#043FIf I hadn't convinced myself I shouldn't come,\x01",
            "even though I love it here...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #22
        0x105,
        (
            "#049F#40WIf I'd just been more honest with myself...#500W　\x01",
            "#15W#3SIf I'd just come here from the beginning...!#2S\x02",
        )
    )

    Sleep(800)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_9E(0x105, 0x7, 0x0, 0xC8, 0x7D0)
    Sleep(800)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x19, 500, 2000, 14700, 180)
    SetChrPos(0x17, 500, 2000, 14700, 180)
    SetChrPos(0x16, 1000, 2000, 14700, 180)

    NpcTalk(    #23
        0x19,
        "Child's Voice",
        "#4PAhahaha!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x17,
        "Child's Voice",
        "#4PIs somebody here?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #25
        0x105,
        "#044F#12P#40W...?\x02",
    )

    CloseMessageWindow()
    OP_44(0x18, 0x2)

    def lambda_EA1():

        label("loc_EA1")

        TurnDirection(0xFE, 0x17, 500)
        OP_48()
        Jump("loc_EA1")

    QueueWorkItem2(0x18, 2, lambda_EA1)
    Sleep(100)

    def lambda_EB7():

        label("loc_EB7")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_EB7")

    QueueWorkItem2(0x15, 2, lambda_EB7)

    def lambda_EC8():
        OP_67(0, 3600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_EC8)

    def lambda_EE0():
        OP_8E(0xFE, 0x190, 0x0, 0x1B58, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_EE0)
    Sleep(600)
    OP_43(0x19, 0x3, 0x0, 0x6)
    Sleep(600)
    OP_43(0x16, 0x3, 0x0, 0x7)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x19, 0x1)
    WaitChrThread(0x16, 0x1)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #26
        0x17,
        "Girl",
        (
            "#1714FOh, THERE you are, Clem! \x02\x03",

            "#1715FWhere have you been all this time?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F93():
        OP_8E(0xFE, 0xC8, 0x0, 0x1068, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_F93)
    Sleep(300)
    OP_43(0x19, 0x3, 0x0, 0x8)
    Sleep(300)

    def lambda_FBF():
        OP_8E(0xFE, 0x4B0, 0x0, 0xE60, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_FBF)
    WaitChrThread(0x16, 0x1)
    TurnDirection(0x16, 0x18, 500)
    WaitChrThread(0x19, 0x3)

    NpcTalk(    #27
        0x19,
        "Young Girl",
        (
            "#1733F#6POooh!\x02\x03",

            "What're you crying for?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #28
        0x105,
        "#043F#11PU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0x2)
    OP_44(0x18, 0x2)
    OP_44(0x15, 0x2)
    TurnDirection(0x15, 0x105, 400)
    Sleep(300)

    ChrTalk(    #29
        0x15,
        (
            "#751F#5PThese are the children I'm looking after\x01",
            "at the moment.\x02\x03",

            "#750FEveryone, say hello to our visitor.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("Children")

    AnonymousTalk(    #30
        "\x07\x00#4SOkay!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_111E():
        OP_6D(710, 0, 3690, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_111E)

    def lambda_1136():
        OP_6B(2960, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1136)

    def lambda_1146():
        OP_6C(38000, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1146)

    def lambda_1156():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1156)

    def lambda_1164():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x9C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1164)
    OP_43(0x16, 0x3, 0x0, 0x9)
    Sleep(300)
    OP_8C(0x18, 225, 400)
    Sleep(800)
    OP_8C(0x19, 45, 400)
    Sleep(800)
    WaitChrThread(0x16, 0x3)

    NpcTalk(    #31
        0x17,
        "Girl",
        "#1718F#5PI'm Mary!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x19, 90, 400)
    Sleep(300)

    NpcTalk(    #32
        0x19,
        "Young Girl",
        "#1730F#6P...Huh? What's going on?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #33
        0x16,
        "Boy",
        "#1721F#11PHiya!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 500)
    Sleep(300)

    ChrTalk(    #34
        0x18,
        "#772F#11PCome on, Polly! You gotta say hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        "#044F#12P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x15,
        (
            "#750F#5PKloe?\x02\x03",

            "The Mercia Orphanage you love is right here,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#542F#12P#40W...\x02\x03",

            "#041F#20WSo it is!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12E6():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_12E6)

    ChrTalk(    #38
        0x15,
        (
            "#750F#5PMaybe we should all have some tea? Now seems\x01",
            "like as good a time as any.\x02\x03",

            "#751FWill you give me a hand making it, Kloe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#048F#12POf course!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 0, 500)
    OP_43(0x15, 0x3, 0x0, 0xA)
    Sleep(500)

    def lambda_13A5():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x8AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13A5)
    Sleep(400)

    def lambda_13C5():

        label("loc_13C5")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13C5")

    QueueWorkItem2(0x17, 2, lambda_13C5)

    def lambda_13D6():

        label("loc_13D6")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13D6")

    QueueWorkItem2(0x18, 2, lambda_13D6)

    def lambda_13E7():

        label("loc_13E7")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13E7")

    QueueWorkItem2(0x16, 2, lambda_13E7)

    def lambda_13F8():

        label("loc_13F8")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_13F8")

    QueueWorkItem2(0x19, 2, lambda_13F8)

    def lambda_1409():
        OP_8F(0xFE, 0xFFFFF574, 0x0, 0x500, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1409)
    Sleep(200)

    def lambda_1429():
        OP_8F(0xFE, 0xFFFFF678, 0x0, 0xA00, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1429)
    Sleep(200)

    def lambda_1449():
        OP_8F(0xFE, 0xFFFFFC68, 0x0, 0xA3C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1449)
    Sleep(200)

    def lambda_1469():
        OP_8F(0xFE, 0xFFFFFBF0, 0x0, 0x654, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1469)
    WaitChrThread(0x105, 0x1)
    OP_43(0x105, 0x3, 0x0, 0xB)
    Sleep(500)
    OP_8C(0x105, 90, 500)
    Sleep(1000)
    OP_8C(0x105, 280, 500)
    Sleep(1000)
    FadeToDark(2000, 0, 120)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x18\x07\x0C#40WFrom that day forward, I stopped avoiding\x01",
            "the orphanage. I made a habit of going there\x01",
            "whenever the opportunity presented itself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #41
        "\x18\x07\x0C#40WI buckled. Exactly the way I thought I would.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x18\x07\x0C#40WI was the same weak little girl I always was,\x01",
            "forever craving the warmth of the orphanage\x01",
            "and forever wanting to be surrounded by the\x01",
            "lovely matron and the children.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "\x18\x07\x0C#40WWhen I was there, the world felt bathed in\x01",
            "happiness and smiling faces.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x18\x07\x0C#40WBecause I never knew my mother and father, all my\x01",
            "memories of this place were the only ones I had of\x01",
            "my childhood...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x18\x07\x0C#40WFor me, the orphanage I could visit now was exactly\x01",
            "the same as the one I fondly remembered from then.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x18\x07\x0C#40WWhen I was there, I could be at peace; I could keep\x01",
            "deceiving myself for as long as I needed to.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #47
        "\x18\x07\x0C#40WYet when I was there, I knew.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x18\x07\x0C#40WI knew my heart wasn't as pure as I wanted to think\x01",
            "it was. My garden, beautiful as it was, continued to\x01",
            "stay enclosed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_20(0xFA0)
    OP_21()
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x00#40WOne month later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_322 end

    def Function_4_1929(): pass

    label("Function_4_1929")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1992")

    def lambda_1938():
        OP_9E(0xFE, 0x5, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1938)
    Sleep(1800)

    def lambda_1957():
        OP_9E(0xFE, 0x9, 0x0, 0x4B0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1957)
    Sleep(5000)

    def lambda_1976():
        OP_9E(0xFE, 0x7, 0x0, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1976)
    Sleep(3400)
    Jump("Function_4_1929")

    label("loc_1992")

    Return()

    # Function_4_1929 end

    def Function_5_1993(): pass

    label("Function_5_1993")


    def lambda_1999():
        OP_8F(0xFE, 0xFFFFF9C0, 0x0, 0xC58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1999)
    WaitChrThread(0x17, 0x1)

    def lambda_19B9():
        OP_8F(0xFE, 0xFFFFF678, 0x0, 0xA00, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_19B9)
    Return()

    # Function_5_1993 end

    def Function_6_19CF(): pass

    label("Function_6_19CF")


    def lambda_19D5():
        OP_8E(0xFE, 0x1F4, 0x0, 0x2864, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_19D5)
    WaitChrThread(0x19, 0x1)

    def lambda_19F5():
        OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x1F04, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_19F5)
    WaitChrThread(0x19, 0x1)
    OP_8C(0x19, 180, 600)
    Return()

    # Function_6_19CF end

    def Function_7_1A17(): pass

    label("Function_7_1A17")


    def lambda_1A1D():
        OP_8E(0xFE, 0x3E8, 0x0, 0x25A8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1A1D)
    WaitChrThread(0x16, 0x1)

    def lambda_1A3D():
        OP_8E(0xFE, 0x528, 0x0, 0x1F04, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1A3D)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 180, 600)
    Return()

    # Function_7_1A17 end

    def Function_8_1A5F(): pass

    label("Function_8_1A5F")


    def lambda_1A65():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0x1950, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1A65)
    WaitChrThread(0x19, 0x1)

    def lambda_1A85():
        OP_8E(0xFE, 0xFFFFF678, 0x0, 0xA28, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1A85)
    WaitChrThread(0x19, 0x1)

    def lambda_1AA5():

        label("loc_1AA5")

        TurnDirection(0xFE, 0x19, 500)
        OP_48()
        Jump("loc_1AA5")

    QueueWorkItem2(0x105, 2, lambda_1AA5)

    def lambda_1AB6():
        OP_8E(0xFE, 0xFFFFF678, 0x0, 0x3D4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1AB6)
    WaitChrThread(0x19, 0x1)
    TurnDirection(0x19, 0x105, 500)
    Sleep(300)
    Return()

    # Function_8_1A5F end

    def Function_9_1ADD(): pass

    label("Function_9_1ADD")


    def lambda_1AE3():
        OP_8E(0xFE, 0x1D6, 0x0, 0x596, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1AE3)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 270, 600)
    Return()

    # Function_9_1ADD end

    def Function_10_1B05(): pass

    label("Function_10_1B05")


    def lambda_1B0B():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x2508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B0B)
    WaitChrThread(0x15, 0x1)

    def lambda_1B2B():
        OP_8E(0xFE, 0xFFFFF1A0, 0x0, 0x2508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B2B)
    WaitChrThread(0x15, 0x1)

    def lambda_1B4B():
        OP_8E(0xFE, 0xFFFFF1A0, 0x0, 0x3908, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1B4B)
    WaitChrThread(0x15, 0x1)
    Return()

    # Function_10_1B05 end

    def Function_11_1B66(): pass

    label("Function_11_1B66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BE5")
    OP_62(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x16, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_11_1B66")

    label("loc_1BE5")

    Return()

    # Function_11_1B66 end

    def Function_12_1BE6(): pass

    label("Function_12_1BE6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-720, 0, 8640, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -2720, 0, 8260, 200)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, -2500, 240, 6020, 270)
    SetChrChipByIndex(0x1A, 12)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x105,
        (
            "#542F#5PWait here for a minute. I'll go and make us some\x01",
            "tea.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 320, 500)
    OP_43(0x105, 0x0, 0x0, 0x11)
    Sleep(500)
    SetChrSubChip(0x1A, 2)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    SetChrSubChip(0x1A, 1)
    Sleep(600)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    SetChrSubChip(0x1A, 2)
    Sleep(1200)
    SetChrSubChip(0x1A, 0)
    Sleep(1000)
    OP_22(0xA4, 0x0, 0x64)
    Fade(250)
    SetChrPos(0x1A, -1580, 0, 6020, 270)
    ClearChrFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)
    Sleep(500)

    def lambda_1D4A():
        OP_6D(-1740, 0, 14180, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_1D4A)

    def lambda_1D62():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0x2468, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D62)
    WaitChrThread(0x1A, 0x1)

    def lambda_1D82():
        OP_8E(0xFE, 0xFFFFF434, 0x0, 0x2468, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1D82)
    WaitChrThread(0x1A, 0x1)

    def lambda_1DA2():
        OP_8E(0xFE, 0xFFFFF434, 0x0, 0x30AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1DA2)
    WaitChrThread(0x1A, 0x1)
    Sleep(500)

    ChrTalk(    #51
        0x1A,
        (
            "#1892F#12PLook...\x02\x03",

            "#645FI-I'm sorry, Kloe.\x02\x03",

            "What I said was really, really insensitive,\x01",
            "and I'm really sorry for ever saying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#543F#5PDon't worry about it, Jill.\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #53
        0x105,
        (
            "#049F#5PWhen I was younger...\x02\x03",

            "#542F...I lost both of my parents, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x1A,
        "#643F#12PYou...did?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x1A, 400)
    Sleep(300)

    ChrTalk(    #55
        0x105,
        (
            "#542F#5PThat's why what you said bothered me.\x02\x03",

            "#543FIn my head, I saw myself in them.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_6D(-2440, 240, 8340, 0)
    OP_67(0, 4360, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, -5260, 240, 7300, 90)
    SetChrChipByIndex(0x105, 7)
    SetChrSubChip(0x105, 0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, -2500, 240, 7300, 270)
    SetChrChipByIndex(0x1A, 12)
    SetChrSubChip(0x1A, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, -3540, 600, 7080, 0)
    SetChrPos(0x12, -4480, 600, 7080, 0)
    SetChrPos(0x10, -4100, 650, 6600, 0)
    Sleep(1200)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x105,
        (
            "#543F#6PI didn't want to think that just because someone\x01",
            "was an orphan, they were unfortunate by default.\x02\x03",

            "I didn't want to think that alone meant they were\x01",
            "doomed to spend life unable to have the same kind\x01",
            "of happiness that others did.\x02\x03",

            "I didn't want anyone to say it--or even think it.\x02\x03",

            "#049FBut that wasn't because I was thinking of the\x01",
            "children here...\x02\x03",

            "...It was because I was thinking about myself.\x01",
            "I didn't want to be thought of as a 'poor little\x01",
            "girl,' either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x1A,
        (
            "#1892F#11PUmm...\x02\x03",

            "Kloe, I really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        (
            "#047F#6PPlease allow me to finish.\x02\x03",

            "#042FI wanted to think I was getting angry on the\x01",
            "children's behalf, but now I know I wasn't.\x02\x03",

            "All I cared about was myself.\x02\x03",

            "I knew that, too, and that's why being called a\x01",
            "model student or being spoken of like some kind\x01",
            "of exemplary human being irritated me so much.\x02\x03",

            "#049F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x1A,
        "#643F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x105,
        (
            "#049F#6P#40WI'm such a hypocrite, aren't I?\x02\x03",

            "Lashing out at you as if I'm sticking up for other\x01",
            "people, when in reality I'm only thinking of myself.\x02\x03",

            "I didn't want to admit it, even though I knew deep\x01",
            "down...\x02\x03",

            "#047FI shouldn't have been so annoyed by it, but I was.\x02\x03",

            "I really am sorry.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #61
        0x1A,
        (
            "#1892F#11PN-No...\x02\x03",

            "#1893FNo! You're clearly not the one at fault, Kloe!\x01",
            "#3SThis is on me, and I'm sorry!#2S\x02\x03",

            "Why you were angry with me doesn't matter\x01",
            "when I said something I never should've said\x01",
            "from the get-go!\x02\x03",

            "I had no idea what kind of life you or the kids\x01",
            "here had led, and I just...\x02\x03",

            "I wasn't trying to imply you were a hypocrite\x01",
            "or anything at all...\x02\x03",

            "#1892FI wanted to apologize to you earlier, I just...\x01",
            "I just...\x02\x03",

            "I didn't know how, I suppose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        "#543F#6P...Same here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x1A,
        (
            "#647F#11PI take back everything I said about the children,\x01",
            "too.\x02\x03",

            "#1890FI had no right to be judging them when I'd never\x01",
            "even been here or met them.\x02\x03",

            "I didn't know the first thing about what I was\x01",
            "talking about.\x02\x03",

            "#1893FI hope you'll forgive me!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #64
        0x105,
        (
            "#543F#6P...Well, then.\x02\x03",

            "#542FWould you like to meet them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x1A,
        "#643F#11PReally?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6F(0x2, 10)
    OP_6F(0x3, 20)
    OP_6F(0x4, 15)
    OP_6F(0x5, 15)
    OP_6D(36900, 0, -32900, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrFlags(0x17, 0x2)
    SetChrFlags(0x19, 0x2)
    SetChrPos(0x18, 37940, 1500, -36940, 225)
    SetChrPos(0x16, 37940, 200, -36940, 225)
    SetChrPos(0x17, 37960, 1500, -32830, 225)
    SetChrPos(0x19, 37960, 200, -32830, 225)
    SetChrChipByIndex(0x18, 13)
    SetChrSubChip(0x18, 0)
    SetChrChipByIndex(0x16, 14)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x17, 15)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x19, 16)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x105, 0x4)
    SetChrPos(0x105, 34000, 0, -30160, 180)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    ClearChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 34000, 0, -30160, 180)
    SetChrChipByIndex(0x1A, 11)
    SetChrSubChip(0x1A, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_29AC():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF7900, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_29AC)
    Sleep(800)
    OP_43(0x105, 0x3, 0x0, 0x10)
    WaitChrThread(0x1A, 0x1)
    Sleep(500)
    OP_8C(0x1A, 270, 500)
    Sleep(1000)
    OP_8C(0x1A, 90, 500)

    ChrTalk(    #66
        0x1A,
        (
            "#643F#6PThey sleep in bunk beds, huh?\x02\x03",

            "#640FI'm kinda jealous.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A34():
        OP_6D(37810, 0, -33430, 2500)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2A34)
    OP_43(0x105, 0x0, 0x0, 0xF)

    def lambda_2A53():
        OP_8E(0xFE, 0x9088, 0x0, 0xFFFF7900, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2A53)
    WaitChrThread(0x1A, 0x1)
    OP_8C(0x1A, 180, 600)
    Sleep(1000)
    OP_8C(0x1A, 10, 600)
    Sleep(500)
    WaitChrThread(0x105, 0x0)
    WaitChrThread(0x1C, 0x0)

    ChrTalk(    #67
        0x19,
        "Achoo!\x02",
    )

    OP_9E(0x19, 0xA, 0xA, 0xC8, 0x7D0)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #68
        0x1A,
        "#641F#12PAhaha. That's adorable!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8F(0x1A, 0x909C, 0x0, 0xFFFF7A2C, 0x3E8, 0x0)
    Sleep(300)
    OP_22(0x186, 0x0, 0x64)
    Fade(500)
    OP_70(0x3, 0xF)
    OP_73(0x3)
    OP_0D()
    Sleep(300)
    OP_8F(0x1A, 0x9088, 0x0, 0xFFFF7900, 0x3E8, 0x0)
    Sleep(300)

    def lambda_2B30():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2B30)
    Sleep(100)
    OP_8C(0x105, 90, 400)
    Sleep(500)

    ChrTalk(    #69
        0x1A,
        "#649F#11PThey really do look cute when they're sleeping.\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1A)
    Sleep(500)

    ChrTalk(    #70
        0x1A,
        "#1890F#11PNow I feel even worse for being so mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x105,
        (
            "#047F#6PI was more in the wrong, Jill.\x02\x03",

            "#049FI knew very well that you didn't actually mean\x01",
            "any harm with what you said.\x02\x03",

            "All my frustrations just built to a point where\x01",
            "I took it out on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x1A,
        (
            "#644F#11PS-Seriously, don't worry about it. Let's call\x01",
            "our faults a draw, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        (
            "#543F#6PHeehee. We're just going around in circles,\x01",
            "aren't we?\x02\x03",

            "Still, in a way, I'm kind of glad this happened.\x01",
            "It helped me sort out my own feelings.\x02\x03",

            "In fact, I feel more at peace with myself right\x01",
            "now than I have in a long time.\x02\x03",

            "#542FBecause it's just hit home just how important\x01",
            "this place truly is to me...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #74
        0x105,
        (
            "#045F#6PAlthough to tell you the truth, all this fighting\x01",
            "has tired me out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x1A,
        (
            "#643F#11PYou, too, huh?\x02\x03",

            "#645FI barely slept a wink last night...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x1A)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #76
        0x1A,
        "#649F#11PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x105,
        "#041F#6PHeeheehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x1A,
        (
            "#640F#11PAnyway...\x02\x03",

            "#648FYou wanna get going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x105,
        "#048F#6PYeah.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2FA7():
        OP_6D(36900, 0, -32900, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2FA7)
    OP_43(0x105, 0x0, 0x0, 0xD)
    OP_43(0x1A, 0x0, 0x0, 0xE)
    WaitChrThread(0x105, 0x0)
    OP_71(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14)
    OP_73(0x0)

    def lambda_2FE9():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF8A30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2FE9)
    WaitChrThread(0x1A, 0x0)

    def lambda_3009():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF8A30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3009)
    WaitChrThread(0x1A, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 20)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    Sleep(1000)

    ChrTalk(    #80
        0x1A,
        (
            "#644F#12PIt feels kind of weird to finally be able \x01",
            "to talk to you openly like this, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30A9():
        OP_6B(3800, 20000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_30A9)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #81
        "\x07\x0C#40WWe've been sharing a room all this time...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #82
        (
            "\x07\x0C#40W...but this is the first time I feel like you've\x01",
            "truly opened up to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #83
        (
            "\x07\x0C#40WFighting aside, that alone's made me pretty \x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x0C#40WYeah. I'm happy, too.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(2000)
    Fade(2000)
    OP_44(0x1C, 0xFF)
    OP_6D(-720, 0, 13700, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(65000, 0)
    OP_6E(280, 0)

    def lambda_3218():
        OP_6D(-600, 0, 3640, 20000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_3218)

    def lambda_3230():
        OP_6C(25000, 20000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3230)
    Sleep(4000)
    SetChrName("")

    AnonymousTalk(    #85
        "\x07\x0C#40WThanks for coming today, Jill.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x0C#40WI'm glad I did!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x0C#40WMay this be the start of a long and\x01",
            "fruitful friendship.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #88
        "\x07\x0C#40WHeehee. I hope so.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1BE6 end

    def Function_13_331F(): pass

    label("Function_13_331F")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0x848A, 0x0, 0xFFFF796E, 0x5DC, 0x0)
    OP_8E(0xFE, 0x8412, 0x0, 0xFFFF7FD6, 0x5DC, 0x0)
    Return()

    # Function_13_331F end

    def Function_14_334F(): pass

    label("Function_14_334F")

    Sleep(1000)
    OP_8E(0xFE, 0x848A, 0x0, 0xFFFF796E, 0x5DC, 0x0)
    OP_8E(0xFE, 0x83F4, 0x0, 0xFFFF7B8A, 0x5DC, 0x0)
    Return()

    # Function_14_334F end

    def Function_15_337D(): pass

    label("Function_15_337D")

    Sleep(1000)
    OP_8E(0xFE, 0x858E, 0x0, 0xFFFF7AE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8BD8, 0x0, 0xFFFF78C4, 0x7D0, 0x0)
    OP_8C(0x105, 45, 400)
    Return()

    # Function_15_337D end

    def Function_16_33B2(): pass

    label("Function_16_33B2")


    def lambda_33B8():
        OP_8E(0xFE, 0x84D0, 0x0, 0xFFFF8080, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_33B8)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    Sleep(300)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 20)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    Sleep(300)
    OP_8C(0x105, 180, 400)
    Return()

    # Function_16_33B2 end

    def Function_17_3407(): pass

    label("Function_17_3407")


    def lambda_340D():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0x3854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_340D)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -2990, 300, 15280, 0)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)
    LoadEffect(0x0, "map\\mp068_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -2990, 500, 15280, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x3C)
    Sleep(3000)
    LoadEffect(0x1, "map\\onsen00.eff")
    PlayEffect(0x1, 0x1, 0xFF, -3100, 1300, 15430, 0, 0, 0, 100, 200, 100, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_17_3407 end

    SaveToFile()

Try(main)
