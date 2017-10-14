from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4104   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60081",
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
        'Master Cryon',                         # 9
        'Cryon Bit',                            # 10
        'Cryon Bit',                            # 11
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
        'ED6_DT09/CH10840 ._CH',             # 00
        'ED6_DT09/CH10841 ._CH',             # 01
        'ED6_DT29/CH12460 ._CH',             # 02
        'ED6_DT29/CH12461 ._CH',             # 03
        'ED6_DT27/CH04000 ._CH',             # 04
        'ED6_DT07/CH00130 ._CH',             # 05
        'ED6_DT07/CH00140 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10840P._CP',             # 00
        'ED6_DT09/CH10841P._CP',             # 01
        'ED6_DT29/CH12460P._CP',             # 02
        'ED6_DT29/CH12461P._CP',             # 03
        'ED6_DT27/CH04000P._CP',             # 04
        'ED6_DT07/CH00130P._CP',             # 05
        'ED6_DT07/CH00140P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
    )

    DeclNpc(
        X                   = 960,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1960,
        Z                   = 0,
        Y                   = 8260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -600,
        Z                   = 0,
        Y                   = 8260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_14F",          # 01, 1
        "Function_2_17A",          # 02, 2
        "Function_3_2F7",          # 03, 3
        "Function_4_BFE",          # 04, 4
        "Function_5_C37",          # 05, 5
        "Function_6_C70",          # 06, 6
        "Function_7_C9D",          # 07, 7
        "Function_8_CD6",          # 08, 8
        "Function_9_D47",          # 09, 9
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Event(0, 3)
    Return()

    # Function_0_14A end

    def Function_1_14F(): pass

    label("Function_1_14F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B")
    OP_B1("t4104_y")
    Jump("loc_174")

    label("loc_16B")

    OP_B1("t4104_n")

    label("loc_174")

    OP_71(0x7, 0x4)
    Return()

    # Function_1_14F end

    def Function_2_17A(): pass

    label("Function_2_17A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2E1")

    label("loc_19F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2E1")

    label("loc_1B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2E1")

    label("loc_1D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2E1")

    label("loc_1EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2E1")

    label("loc_203")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2E1")

    label("loc_21C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2E1")

    label("loc_235")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2E1")

    label("loc_24E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2E1")

    label("loc_267")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2E1")

    label("loc_280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2E1")

    label("loc_299")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2E1")

    label("loc_2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2E1")

    label("loc_2CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2E1")

    label("loc_2F6")

    Return()

    # Function_2_17A end

    def Function_3_2F7(): pass

    label("Function_3_2F7")

    EventBegin(0x0)
    OP_6D(1520, 0, 1520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 0)
    OP_72(0x1, 0x10)
    SetChrPos(0x101, 440, 0, -25960, 0)
    SetChrPos(0x105, 2060, 0, -26560, 0)
    SetChrPos(0x104, -520, 0, -27220, 0)
    SetChrPos(0x108, 1280, 0, -27820, 0)

    def lambda_398():
        OP_6D(1520, 0, -18920, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_398)
    Sleep(500)
    OP_70(0x0, 0x64)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(100)
    OP_43(0x105, 0x1, 0x0, 0x5)
    Sleep(100)
    OP_43(0x104, 0x1, 0x0, 0x6)
    Sleep(100)
    OP_43(0x108, 0x1, 0x0, 0x7)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    Fade(500)
    OP_6D(1280, 0, -12260, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #0
        0x101,
        "#1000F#6PThe Grand Arena... Kinda nostalgic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        "#070FFeels like we were here just yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x104,
        (
            "#035FJust standing here has me recalling\x01",
            "the admiring roar of the audience.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4ED():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ED)
    Sleep(50)

    def lambda_500():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_500)
    Sleep(50)

    def lambda_513():
        OP_8C(0x104, 45, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_513)
    Sleep(50)

    def lambda_526():
        OP_8C(0x108, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_526)
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #3
        0x105,
        (
            "#040FYou were invited to the castle after\x01",
            "you won the Martial Arts Competition,\x01",
            "right, Estelle?\x02\x03",

            "#041FI wish I could have joined you on the\x01",
            "field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016F#6PAhaha. Thinking about it, I was still\x01",
            "pretty amateurish.\x02\x03",

            "#1006FBut, you know, once this whole thing\x01",
            "is cleared up, I'd like to take part in next\x01",
            "year's Martial Arts Competition.\x02\x03",

            "To test my own ability, for one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x108,
        (
            "#071FNow that sounds like Cassius'\x01",
            "daughter to me!\x02\x03",

            "#070FI'd like to join in on the action, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1016F#6PI, uh, don't really feel like I'd have\x01",
            "a chance against you, Zin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x104,
        (
            "#031FWell, then I shall sing from the seats\x01",
            "to cheer you on, Estelle.\x02\x03",

            "#030FI will serenade my love for you as\x01",
            "mightily as I can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1019F#6P...Pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        "#041FHaha...\x02",
    )

    CloseMessageWindow()
    OP_70(0x1, 0x64)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)

    def lambda_8C5():
        OP_8F(0xFE, 0x3C0, 0x0, 0xFFFFFB78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8C5)

    def lambda_8E0():
        OP_8F(0xFE, 0x7A8, 0x0, 0xFFFFF3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E0)

    def lambda_8FB():
        OP_8F(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFF3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8FB)

    def lambda_916():
        OP_6D(1880, 0, 5500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_916)

    def lambda_92E():
        OP_67(0, 5420, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_92E)

    def lambda_946():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_946)

    def lambda_956():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_956)

    def lambda_966():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_966)
    Sleep(50)

    def lambda_979():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_979)
    Sleep(50)

    def lambda_98C():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_98C)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x104, 5)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x105, 6)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x108, 7)
    SetChrSubChip(0x108, 0)
    SetChrPos(0x101, 320, 0, -8590, 0)
    SetChrPos(0x105, 1670, 0, -9190, 0)
    SetChrPos(0x104, -430, 0, -10240, 0)
    SetChrPos(0x108, 920, 0, -10990, 0)

    def lambda_A0B():
        OP_6D(1620, 0, -5360, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A0B)

    def lambda_A23():
        OP_6B(3400, 4000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A23)
    WaitChrThread(0x101, 0x2)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    OP_0D()

    ChrTalk(    #10
        0x101,
        "#1004FM-Monsters?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x108,
        (
            "#072FThis feels reminiscent of some\x01",
            "old coliseum games...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        (
            "#035FThe setting is certainly apt.\x02\x03",

            "#030FIt's a pity we lack an audience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        "#046F...Here they come!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    OP_43(0x8, 0x0, 0x0, 0x8)

    def lambda_B44():
        OP_8F(0xFE, 0x3C0, 0x0, 0xFFFFD468, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B44)

    def lambda_B5F():
        OP_8F(0xFE, 0x7A8, 0x0, 0xFFFFCCC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B5F)

    def lambda_B7A():
        OP_8F(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFCCC0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B7A)

    def lambda_B95():
        OP_6B(2600, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B95)
    Sleep(400)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x104, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD4")
    Battle(0xCEA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_BE1")

    label("loc_BD4")

    Battle(0xCE9, 0x0, 0x0, 0x0, 0xFF)

    label("loc_BE1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_BF1"),
        (0, "loc_BF6"),
        (SWITCH_DEFAULT, "loc_BFD"),
    )


    label("loc_BF1")

    OP_B4(0x0)
    Jump("loc_BFD")

    label("loc_BF6")

    Call(0, 9)
    Jump("loc_BFD")

    label("loc_BFD")

    Return()

    # Function_3_2F7 end

    def Function_4_BFE(): pass

    label("Function_4_BFE")

    OP_8E(0x101, 0x1B8, 0x0, 0xFFFFD530, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 360, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_4_BFE end

    def Function_5_C37(): pass

    label("Function_5_C37")

    OP_8E(0x105, 0x80C, 0x0, 0xFFFFD2D8, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_5_C37 end

    def Function_6_C70(): pass

    label("Function_6_C70")

    OP_8E(0x104, 0xFFFFFDF8, 0x0, 0xFFFFD044, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_6_C70 end

    def Function_7_C9D(): pass

    label("Function_7_C9D")

    OP_8E(0x108, 0x500, 0x0, 0xFFFFCDEC, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_C9D end

    def Function_8_CD6(): pass

    label("Function_8_CD6")

    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    Return()

    # Function_8_CD6 end

    def Function_9_D47(): pass

    label("Function_9_D47")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(1620, 0, -5360, 0)
    OP_67(0, 5420, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x104, 5)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x105, 6)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x108, 7)
    SetChrSubChip(0x108, 0)
    SetChrPos(0x101, 320, 0, -8590, 0)
    SetChrPos(0x105, 1670, 0, -9190, 0)
    SetChrPos(0x104, -430, 0, -10240, 0)
    SetChrPos(0x108, 920, 0, -10990, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    PlayEffect(0x0, 0x1, 0xFF, 720, 0, -3320, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x7, 0x4)

    ChrTalk(    #14
        0x101,
        "#1004FWh-Wha-Wha...?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrChipByIndex(0x108, 65535)
    OP_0D()

    ChrTalk(    #15
        0x101,
        "#1019FWh-What was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        "#044FIt was like a magic trick...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#030FWhat a fabulous display.\x02\x03",

            "#035FHe is a fitting rival, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        (
            "#075F*sigh* He's even weirder than\x01",
            "I thought he'd be.\x02\x03",

            "#070FWell, whatever. Let's check the contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1000FYep.\x02",
    )

    CloseMessageWindow()

    def lambda_FB3():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FB3)

    def lambda_FC3():
        OP_8E(0xFE, 0x208, 0x0, 0xFFFFEF0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC3)
    Sleep(400)

    def lambda_FE3():
        OP_90(0xFE, 0xFFFFFF38, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FE3)
    Sleep(50)

    def lambda_1003():
        OP_90(0xFE, 0xFFFFFF38, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1003)
    Sleep(50)

    def lambda_1023():
        OP_90(0xFE, 0xFFFFFF38, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1023)
    WaitChrThread(0x101, 0x1)
    Sleep(400)
    OP_70(0x7, 0x3C)
    OP_22(0x2B, 0x0, 0x64)
    OP_73(0x7)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #20
        "Received #2C#16IPortrait of Arseille#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #21
        "\x07\x05There was a card stuck to the bottom of the box.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05My princess, my rival, and brave bracers.\x02\x03",

            "Did you enjoy the show I prepared for your arrival?\x02\x03",

            "As I do not wish to upset the mood of our main role,\x01",
            "it is time for the supporting actors to take their bows.\x02\x03",

            "I hope you will look forward to our next chance meeting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #23
        0x101,
        (
            "#1009FPfft, some chance meeting.\x02\x03",

            "I wish he'd cut it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#042F#4PBut, there's something curious about it.\x02\x03",

            "Main role? Supporting actors...?\x01",
            "What does that mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1015FNow that you mention it...\x02\x03",

            "#1000FAh, screw it. Let's go return the\x01",
            "photo to the archives.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4135   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_D47 end

    SaveToFile()

Try(main)
