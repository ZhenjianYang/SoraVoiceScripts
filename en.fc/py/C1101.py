from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1101   ._SN',
        MapName             = 'Bose',
        Location            = 'C1101.x',
        MapIndex            = 49,
        MapDefaultBGM       = "ed60030",
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
        'Kyle',                                 # 9
        'Sky Bandit',                           # 10
        'Sky Bandit',                           # 11
        'Sky Bandit',                           # 12
        'Sky Bandit',                           # 13
        'Sky Bandit Ship',                      # 14
        'Sky Bandit Ship (Shadow)',             # 15
        'General Morgan',                       # 16
        'Royal Army Officer',                   # 17
        'Royal Army Soldier',                   # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Royal Army Soldier',                   # 21
        'Royal Army Soldier',                   # 22
        'Royal Army Soldier',                   # 23
        'Royal Army Soldier',                   # 24
        'Royal Army Soldier',                   # 25
        'Royal Army Soldier',                   # 26
        'Royal Army Soldier',                   # 27
        'Royal Army Soldier',                   # 28
        'Royal Army Soldier',                   # 29
        'Royal Army Soldier',                   # 30
        'Royal Army Soldier',                   # 31
        'Royal Army Soldier',                   # 32
        'Royal Army Soldier',                   # 33
        'Royal Army Soldier',                   # 34
        'Royal Army Soldier',                   # 35
        ' ',                                    # 36
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
        Unknown_3A              = 49,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH00300 ._CH',             # 01
        'ED6_DT07/CH00304 ._CH',             # 02
        'ED6_DT07/CH00305 ._CH',             # 03
        'ED6_DT07/CH00306 ._CH',             # 04
        'ED6_DT07/CH01380 ._CH',             # 05
        'ED6_DT07/CH00360 ._CH',             # 06
        'ED6_DT07/CH00364 ._CH',             # 07
        'ED6_DT07/CH00100 ._CH',             # 08
        'ED6_DT07/CH00101 ._CH',             # 09
        'ED6_DT07/CH00110 ._CH',             # 0A
        'ED6_DT07/CH00111 ._CH',             # 0B
        'ED6_DT07/CH00120 ._CH',             # 0C
        'ED6_DT07/CH00121 ._CH',             # 0D
        'ED6_DT07/CH00122 ._CH',             # 0E
        'ED6_DT07/CH00301 ._CH',             # 0F
        'ED6_DT07/CH02080 ._CH',             # 10
        'ED6_DT07/CH01650 ._CH',             # 11
        'ED6_DT07/CH01600 ._CH',             # 12
        'ED6_DT07/CH00361 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH00300P._CP',             # 01
        'ED6_DT07/CH00304P._CP',             # 02
        'ED6_DT07/CH00305P._CP',             # 03
        'ED6_DT07/CH00306P._CP',             # 04
        'ED6_DT07/CH01380P._CP',             # 05
        'ED6_DT07/CH00360P._CP',             # 06
        'ED6_DT07/CH00364P._CP',             # 07
        'ED6_DT07/CH00100P._CP',             # 08
        'ED6_DT07/CH00101P._CP',             # 09
        'ED6_DT07/CH00110P._CP',             # 0A
        'ED6_DT07/CH00111P._CP',             # 0B
        'ED6_DT07/CH00120P._CP',             # 0C
        'ED6_DT07/CH00121P._CP',             # 0D
        'ED6_DT07/CH00122P._CP',             # 0E
        'ED6_DT07/CH00301P._CP',             # 0F
        'ED6_DT07/CH02080P._CP',             # 10
        'ED6_DT07/CH01650P._CP',             # 11
        'ED6_DT07/CH01600P._CP',             # 12
        'ED6_DT07/CH00361P._CP',             # 13
    )

    DeclNpc(
        X                   = -1550,
        Z                   = 0,
        Y                   = 400,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x80,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x80,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -31320,
        Y                   = -1000,
        Z                   = -13400,
        Range               = -30300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFBF28,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 9230,
        Y                   = -1000,
        Z                   = 28440,
        Range               = 6690,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x6B6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )


    ScpFunction(
        "Function_0_50A",          # 00, 0
        "Function_1_56D",          # 01, 1
        "Function_2_5A8",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_5D4",          # 04, 4
        "Function_5_1F8B",         # 05, 5
        "Function_6_21B8",         # 06, 6
        "Function_7_23E5",         # 07, 7
        "Function_8_246B",         # 08, 8
        "Function_9_340D",         # 09, 9
        "Function_10_3EEB",        # 0A, 10
        "Function_11_3FC8",        # 0B, 11
        "Function_12_40A5",        # 0C, 12
        "Function_13_4182",        # 0D, 13
    )


    def Function_0_50A(): pass

    label("Function_0_50A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_526"),
        (108, "loc_538"),
        (109, "loc_54E"),
        (110, "loc_54E"),
        (111, "loc_54E"),
        (SWITCH_DEFAULT, "loc_56C"),
    )


    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535")
    OP_A2(0x320)
    Event(0, 4)

    label("loc_535")

    Jump("loc_56C")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54B")
    OP_A2(0x329)
    Event(0, 9)

    label("loc_54B")

    Jump("loc_56C")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_569")
    OP_A2(0x328)
    Event(0, 8)

    label("loc_569")

    Jump("loc_56C")

    label("loc_56C")

    Return()

    # Function_0_50A end

    def Function_1_56D(): pass

    label("Function_1_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_592")
    OP_1B(0x0, 0x0, 0xA)
    OP_1B(0x1, 0x0, 0xB)
    OP_1B(0x2, 0x0, 0xC)
    OP_1B(0x3, 0x0, 0xC)
    OP_1B(0x5, 0x0, 0xD)

    label("loc_592")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x387), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A7")

    Return()

    # Function_1_56D end

    def Function_2_5A8(): pass

    label("Function_2_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A8")

    label("loc_5BD")

    Return()

    # Function_2_5A8 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D3")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_3_5BE")

    label("loc_5D3")

    Return()

    # Function_3_5BE end

    def Function_4_5D4(): pass

    label("Function_4_5D4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-13820, 0, -21910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -14020, 0, -25740, 0)
    SetChrPos(0x102, -13880, 0, -27430, 0)
    SetChrPos(0x103, -12570, 0, -26210, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -2330, 0, 540, 270)
    SetChrPos(0x9, -5040, 0, 1610, 120)
    SetChrPos(0xA, -6710, 0, 660, 132)
    SetChrPos(0xB, -5140, 0, -1420, 66)
    SetChrPos(0xC, -6480, 0, -1100, 68)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, 9990, 0, -2360, 341)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#003F#5PMan, it's bright in here...\x02\x03",

            "#505FHuh? Isn't that the...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#012F#5P(Quiet, Estelle...)\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(    #2
        0x103,
        (
            "#022F#5P(It looks like we've hit\x01",
            "the jackpot...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_779():
        OP_6D(-7840, 0, 13100, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_779)

    def lambda_791():
        OP_67(0, 5220, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_791)

    def lambda_7A9():
        OP_6B(9500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A9)

    def lambda_7B9():
        OP_6C(25000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B9)
    OP_21()
    OP_1D(0x57)
    Sleep(6000)

    def lambda_7D1():
        OP_6D(-4300, 3000, -10, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D1)

    def lambda_7E9():
        OP_6E(138, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E9)
    Sleep(4000)

    ChrTalk(    #3
        0x8,
        (
            "#201F#4PForget about the heavy things and\x01",
            "focus on the food provisions and\x01",
            "valuables.\x02\x03",

            "And hurry it up, will ya?\x01",
            "It's only a matter of time before\x01",
            "someone finds this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "#2P#1KGot it, Kyle.\x02",
    )


    ChrTalk(    #5
        0xA,
        "#1P#1KRoger that, Kyle.\x02",
    )


    ChrTalk(    #6
        0xB,
        "#4P#1KUnderstood, Kyle.\x02",
    )


    ChrTalk(    #7
        0xC,
        "#3P#1KOkay, Kyle.\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    Sleep(100)
    Fade(1000)
    OP_6D(-13820, 0, -21910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(332, 0)
    OP_0D()

    ChrTalk(    #8
        0x101,
        (
            "#580F(What's an airliner doing in a\x01",
            "place like this...?)\x02\x03",

            "(I guess that kid wasn't seeing\x01",
            "things after all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#020F(This looks like an area that used\x01",
            "to be used for strip mining...)\x02\x03",

            "(It certainly turned out to be a great\x01",
            "place to hide something of this size.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#012F(Yeah, who would have thought\x01",
            "to look here?)\x02\x03",

            "(Look at that. Aren't they loading the\x01",
            "airliner cargo into their own ship?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#006F(Let's worry about that later!)\x02\x03",

            "(We've got to figure out a way to bag\x01",
            "these guys before they get away again!)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-4110, 0, 490, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(5070, 0)
    OP_6C(69000, 0)
    OP_6E(213, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x102, 10)
    SetChrChipByIndex(0x103, 12)
    SetChrPos(0x101, -10010, 0, -10600, 26)
    SetChrPos(0x102, -9790, 0, -12210, 25)
    SetChrPos(0x103, -8430, 0, -11060, 23)
    OP_0D()

    ChrTalk(    #12
        0x8,
        (
            "#203FSo this is our third trip, huh?\x02\x03",

            "Man, Don can be a real slave-driver\x01",
            "sometimes.\x02\x03",

            "#200FOh well, once this is all taken care of\x01",
            "we'll be able to sit back and negotiate\x01",
            "a nice, fat ransom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1PHold it right there!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D13():
        TurnDirection(0xFE, 0x101, 800)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D13)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D38():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D38)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D62():
        TurnDirection(0xFE, 0x101, 800)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D62)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_D87():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D87)
    Sleep(50)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #14
        0x8,
        "#201F#6PWho in the...?!\x02",
    )

    CloseMessageWindow()

    def lambda_DBE():
        OP_6D(-4960, 0, -4910, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBE)

    def lambda_DD6():
        OP_6C(69000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DD6)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #15
        0x101,
        (
            "#502FThe scorching flames of justice shall\x01",
            "never fade away as long as evil thrives\x01",
            "in this world...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #16
        0x101,
        (
            "#508F#3SThe League of Extraordinary Bracers\x01",
            "has arrived!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x102)
    OP_63(0x103)
    OP_63(0x8)
    OP_63(0x9)
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0xC)

    ChrTalk(    #17
        0x101,
        "#505FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        "#018FThe 'League of'...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#025FYou bonehead. Why do you always\x01",
            "get carried away like that?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #20
        0x101,
        (
            "#503FWhat's with you two...? Now I look\x01",
            "like a big fool saying that stuff\x01",
            "all alone...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 6)
    SetChrChipByIndex(0xC, 6)
    SetChrChipByIndex(0xA, 6)
    SetChrChipByIndex(0xB, 6)
    SetChrChipByIndex(0x8, 1)
    SetChrChipByIndex(0x8, 15)
    OP_8E(0x8, 0xFFFFEFFC, 0x0, 0xFFFFF84E, 0x1388, 0x0)
    SetChrChipByIndex(0x8, 1)

    ChrTalk(    #21
        0x8,
        (
            "#201FYou're...the ones who Josette had\x01",
            "a run-in with back in Rolent!\x02\x03",

            "This can't be right! You're not supposed\x01",
            "to be here this early!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#509F#2P...It can't be right? We're not supposed\x01",
            "to be here this early...?\x02\x03",

            "What the heck are you talking\x01",
            "about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#022F#2PIn accordance with the laws of the Bracer Guild,\x01",
            "you are hereby under arrest and charged with the\x01",
            "hijacking of an airliner and its passengers.\x02\x03",

            "I hope for your sakes you'll come along quietly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#201FN-Now hold on just a minute!\x02\x03",

            "Are you trying to tell me that...\x01",
            "only the three of you came here\x01",
            "to arrest us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#009F#2PYou see anyone else, bandit boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#204FSo you're not involved with the\x01",
            "others then, huh?\x02\x03",

            "#201FThen that simplifies things...\x01",
            "Let's get 'em, boys!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 15)

    def lambda_136B():
        OP_92(0xFE, 0x103, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_136B)
    Sleep(50)
    SetChrChipByIndex(0xC, 19)

    def lambda_138A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_138A)
    Sleep(50)
    SetChrChipByIndex(0xB, 19)

    def lambda_13A9():
        OP_92(0xFE, 0x102, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13A9)
    Sleep(50)
    SetChrChipByIndex(0x9, 19)

    def lambda_13C8():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13C8)
    Sleep(50)
    SetChrChipByIndex(0xA, 19)

    def lambda_13E7():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13E7)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 13)

    def lambda_1410():
        OP_6D(-3960, 0, -3910, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1410)

    def lambda_1428():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1428)
    Sleep(50)
    SetChrChipByIndex(0x101, 9)

    def lambda_1447():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1447)
    Sleep(50)
    SetChrChipByIndex(0x102, 11)

    def lambda_1466():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1466)
    Sleep(300)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_14C4"),
        (SWITCH_DEFAULT, "loc_14C9"),
    )


    label("loc_14C4")

    OP_B4(0x0)
    Jump("loc_14C9")

    label("loc_14C9")

    OP_6D(-5750, 0, -5350, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(5070, 0)
    OP_6C(69000, 0)
    OP_6E(212, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 7)
    SetChrChipByIndex(0xA, 7)
    SetChrChipByIndex(0xB, 7)
    SetChrChipByIndex(0xC, 7)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x102, 10)
    SetChrChipByIndex(0x103, 12)
    SetChrPos(0x8, -5830, 0, -4580, 216)
    SetChrPos(0x9, -4000, 0, -5410, 258)
    SetChrPos(0xA, -4760, 0, -2930, 184)
    SetChrPos(0xB, -8260, 0, -3290, 156)
    SetChrPos(0xC, -2270, 0, -3270, 232)
    SetChrPos(0x101, -9950, 0, -7740, 49)
    SetChrPos(0x102, -9710, 0, -9600, 31)
    SetChrPos(0x103, -7170, 0, -8440, 358)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #27
        0x8,
        (
            "#203FOw... You guys are tougher\x01",
            "than I thought.\x02\x03",

            "#200FIt's no wonder Josette got\x01",
            "beat by you three.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#502FSweet-talk won't get you anywhere,\x01",
            "buddy!\x02\x03",

            "#005FIt's time to surrender and let the\x01",
            "passengers go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#202FHa ha ha! You really don't know\x01",
            "anything, do you?\x02\x03",

            "What was that you called yourselves?\x01",
            "'League of the Exceptionally Dim' or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#509FYou making fun of my awesome team name?\x01",
            "...You're dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#016FLook out...!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    OP_99(0x8, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x8, 1)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 3)

    def lambda_1810():
        OP_6C(50000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1810)
    OP_99(0x8, 0x0, 0x3, 0x3E8)
    OP_99(0x8, 0x0, 0x3, 0x3E8)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x8, 4)
    SoundLoad(127)
    SetChrPos(0x23, -7460, -3000, -6780, 339)
    PlayEffect(0x0, 0xFF, 0x8, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x23, 0, 0, 0, 0)
    OP_99(0x8, 0x0, 0x1, 0x3E8)
    Sleep(1300)
    OP_22(0x7F, 0x0, 0x64)
    OP_11(0xFF, 0xFF, 0xFF, 0xA410, 0x17318, 0x0)
    SetMapFlags(0x10)
    StopSound(0x2C24, 0xE09C, 0x7D0)
    Sleep(2000)

    ChrTalk(    #32
        0x101,
        "#580FWhat...is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x103,
        (
            "#024FYou've gotta be kidding me...\x01",
            "another smokescreen?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_22(0x79, 0x0, 0x64)
    OP_22(0xCC, 0x0, 0x64)
    OP_22(0xCD, 0x0, 0x64)
    SetChrPos(0x8, 2280, 0, -8280, 117)

    ChrTalk(    #34
        0x8,
        (
            "#202FAh ha ha ha ha ha ha!\x02\x03",

            "It's too bad about the rest of the\x01",
            "cargo, but we'll just have to live\x01",
            "without it!\x02\x03",

            "Later, bracers!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, 6450, 100, -820, 341)
    SetChrPos(0xE, 6450, 100, -820, 341)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    PlayEffect(0x1, 0x2, 0xE, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_A1(0xD, 0x0)
    OP_A1(0xE, 0x1)

    def lambda_1A5D():

        label("loc_1A5D")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1A5D")

    QueueWorkItem2(0x101, 1, lambda_1A5D)

    def lambda_1A6E():

        label("loc_1A6E")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1A6E")

    QueueWorkItem2(0x103, 1, lambda_1A6E)

    def lambda_1A7F():

        label("loc_1A7F")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1A7F")

    QueueWorkItem2(0x102, 1, lambda_1A7F)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x6)

    def lambda_1A9E():
        OP_6C(26000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A9E)
    Sleep(1000)

    def lambda_1AB3():
        OP_6B(6000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AB3)
    StopSound(0xA794, 0x1BD50, 0x2710)
    Sleep(1000)

    def lambda_1AD5():
        OP_6D(-8130, 0, -15090, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AD5)
    OP_43(0x103, 0x3, 0x0, 0x7)
    Sleep(5000)

    def lambda_1AF9():
        OP_6D(-9300, 0, -10850, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AF9)
    OP_6B(5170, 2000)
    OP_20(0x5DC)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_0D()
    OP_21()
    OP_1D(0x1E)
    Sleep(500)

    ChrTalk(    #35
        0x101,
        (
            "#007F*gag* *cough* *cough*\x02\x03",

            "Ow ow ow...\x01",
            "Some of it got in my eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#012FDon't worry, it's not poisonous...\x01",
            "It looks like it was a typical smoke\x01",
            "canister.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x103, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)
    OP_8E(0x103, 0xFFFFDFD0, 0x0, 0xFFFFD364, 0x7D0, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)

    ChrTalk(    #37
        0x103,
        (
            "#022FTheir ship is already out of sight...\x02\x03",

            "#025FThis is getting really old. It's not once,\x01",
            "but twice now that they've gotten away.\x02\x03",

            "If I get demoted for this at the guild,\x01",
            "there's not much I can say in my\x01",
            "defense.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x103, 400)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #38
        0x101,
        (
            "#009FOh, Schera...\x02\x03",

            "Quit acting like it was all\x01",
            "your fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#012FWe're responsible for letting them\x01",
            "get away, too.\x02\x03",

            "If we've got time to kick ourselves\x01",
            "over this, then there's got to be some\x01",
            "other constructive things we can do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #40
        0x103,
        (
            "#026F#4PWell, well...\x01",
            "You sound like you should be\x01",
            "the senior bracer.\x02\x03",

            "#020FWell, at least we were able to take\x01",
            "back the airliner, so how about we\x01",
            "have a look?\x02\x03",

            "The passengers may be inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#006FRight...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -12570, 0, -19040, 0)
    SetChrPos(0x102, -12570, 0, -19040, 0)
    SetChrPos(0x103, -12570, 0, -19040, 0)
    OP_6D(-12570, 0, -19040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    OP_28(0x36, 0x1, 0x200)
    OP_28(0x36, 0x1, 0x400)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_5D4 end

    def Function_5_1F8B(): pass

    label("Function_5_1F8B")


    def lambda_1F91():
        OP_8F(0xFE, 0xFFFF029A, 0xFA0, 0xFFFF1E2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F91)

    def lambda_1FAC():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1FAC)
    Sleep(1000)

    def lambda_1FBF():
        OP_8F(0xFE, 0xFFFF9AF2, 0x4A38, 0xFFFEF71E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FBF)
    Sleep(500)

    def lambda_1FDF():
        OP_8F(0xFE, 0xFFFF9AF2, 0x4A38, 0xFFFEF71E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FDF)
    Sleep(500)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 160)
    OP_70(0x0, 0xC8)

    def lambda_2011():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2011)
    Sleep(200)

    def lambda_2024():
        OP_8C(0xFE, 200, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2024)
    Sleep(200)

    def lambda_2037():
        OP_8C(0xFE, 200, 26)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2037)
    Sleep(200)

    def lambda_204A():
        OP_8C(0xFE, 200, 24)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_204A)
    Sleep(200)

    def lambda_205D():
        OP_8C(0xFE, 200, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_205D)
    Sleep(200)

    def lambda_2070():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2070)
    Sleep(200)

    def lambda_2083():
        OP_8C(0xFE, 200, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2083)
    Sleep(200)

    def lambda_2096():
        OP_8C(0xFE, 200, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2096)
    Sleep(200)

    def lambda_20A9():
        OP_8C(0xFE, 200, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20A9)
    OP_6F(0x0, 200)
    OP_70(0x0, 0xF0)

    def lambda_20C5():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20C5)
    Sleep(500)

    def lambda_20E5():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20E5)

    def lambda_20F3():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20F3)
    Sleep(500)

    def lambda_2113():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2113)
    Sleep(500)

    def lambda_2133():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2133)
    Sleep(500)

    def lambda_2153():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2153)
    Sleep(500)

    def lambda_2173():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2173)
    Sleep(500)

    def lambda_2193():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3A98, 0xFFFEF71E, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2193)
    Sleep(500)
    WaitChrThread(0xFE, 0x2)
    OP_71(0x0, 0x4)
    Return()

    # Function_5_1F8B end

    def Function_6_21B8(): pass

    label("Function_6_21B8")


    def lambda_21BE():
        OP_8F(0xFE, 0xFFFF029A, 0x3E8, 0xFFFF1E2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21BE)

    def lambda_21D9():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_21D9)
    Sleep(1000)

    def lambda_21EC():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21EC)
    Sleep(500)

    def lambda_220C():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_220C)
    Sleep(500)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 160)
    OP_70(0x0, 0xC8)

    def lambda_223E():
        OP_8C(0xFE, 200, 30)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_223E)
    Sleep(200)

    def lambda_2251():
        OP_8C(0xFE, 200, 28)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2251)
    Sleep(200)

    def lambda_2264():
        OP_8C(0xFE, 200, 26)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2264)
    Sleep(200)

    def lambda_2277():
        OP_8C(0xFE, 200, 24)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2277)
    Sleep(200)

    def lambda_228A():
        OP_8C(0xFE, 200, 22)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_228A)
    Sleep(200)

    def lambda_229D():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_229D)
    Sleep(200)

    def lambda_22B0():
        OP_8C(0xFE, 200, 18)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22B0)
    Sleep(200)

    def lambda_22C3():
        OP_8C(0xFE, 200, 16)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22C3)
    Sleep(200)

    def lambda_22D6():
        OP_8C(0xFE, 200, 15)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_22D6)
    OP_6F(0x0, 200)
    OP_70(0x0, 0xF0)

    def lambda_22F2():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22F2)
    Sleep(500)

    def lambda_2312():
        OP_8C(0xFE, 200, 20)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2312)

    def lambda_2320():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2320)
    Sleep(500)

    def lambda_2340():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2340)
    Sleep(500)

    def lambda_2360():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2360)
    Sleep(500)

    def lambda_2380():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2380)
    Sleep(500)

    def lambda_23A0():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23A0)
    Sleep(500)

    def lambda_23C0():
        OP_8F(0xFE, 0xFFFF9AF2, 0x3E8, 0xFFFEF71E, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_23C0)
    Sleep(500)
    WaitChrThread(0xFE, 0x2)
    OP_71(0x0, 0x4)
    Return()

    # Function_6_21B8 end

    def Function_7_23E5(): pass

    label("Function_7_23E5")

    Sleep(2000)
    OP_24(0x79, 0x5F)
    OP_24(0xCC, 0x5F)
    OP_24(0xCD, 0x5F)
    Sleep(200)
    OP_24(0x79, 0x5A)
    OP_24(0xCC, 0x5A)
    OP_24(0xCD, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x55)
    OP_24(0xCC, 0x55)
    OP_24(0xCD, 0x55)
    Sleep(200)
    OP_24(0x79, 0x50)
    OP_24(0xCC, 0x50)
    OP_24(0xCD, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    OP_24(0xCC, 0x46)
    OP_24(0xCD, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    OP_24(0xCC, 0x3C)
    OP_24(0xCD, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    OP_24(0xCC, 0x32)
    OP_24(0xCD, 0x32)
    Sleep(200)
    OP_23(0x79)
    OP_23(0xCC)
    OP_23(0xCD)
    Return()

    # Function_7_23E5 end

    def Function_8_246B(): pass

    label("Function_8_246B")

    EventBegin(0x0)
    OP_6D(-11700, 7200, 16590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -5960, 7200, 16680, 90)
    SetChrPos(0x102, -4940, 7200, 15330, 51)
    SetChrPos(0x103, -4230, 7200, 16900, 244)
    FadeToBright(1000, 0)
    OP_6D(-5220, 7200, 16540, 3000)

    ChrTalk(    #42
        0x101,
        (
            "#007F#3PWe checked it over, but it looks\x01",
            "like there's nobody inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#015FThere's a high possibility the\x01",
            "passengers were transferred\x01",
            "to the sky bandits' airship.\x02\x03",

            "#012FAnd then to wherever their\x01",
            "hideout is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#003F#3PAgreed.\x02\x03",

            "But this sucks... Right when\x01",
            "I thought we had some clues,\x01",
            "we're back to zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x103,
        (
            "#020FCome on, cheer up already.\x02\x03",

            "It's not like every clue has\x01",
            "completely vanished.\x02\x03",

            "#027FWhy do you think the sky bandits\x01",
            "hid the airliner in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#004F#3PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#026FAs far as I can tell, the orbal energy in the ship\x01",
            "has completely stopped.\x02\x03",

            "Which means that the orbal engine was stripped\x01",
            "from the aircraft.\x02\x03",

            "I know this because the orbal energy in an\x01",
            "orbment gradually recharges over time.\x02\x03",

            "#022FFurthermore, the sky bandits made multiple trips\x01",
            "to carry off a large amount of cargo.\x02\x03",

            "Considering the time and risk involved, don't you\x01",
            "think it would have been more effective just to\x01",
            "take the entire airliner to their hideout?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#006F#3PYeah, that does seem a little\x01",
            "odd that they didn't...\x02\x03",

            "So, why'd they hide the airliner\x01",
            "here then?\x02\x03",

            "#505FUm, all I can think of is that\x01",
            "they did it in order to...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Sort the cargo.]\x01",                                                 # 0
            "[Move the hostages aboard their own aircraft.]\x01",                    # 1
            "[Steal the orbal engine.]\x01",                                         # 2
            "[Keep clear of the Royal Army's search party.]\x01",                    # 3
            "[Ditch the Linde, because their hideout is somewhere weird.]\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A9D"),
        (1, "loc_2B67"),
        (2, "loc_2C27"),
        (3, "loc_2CED"),
        (4, "loc_2DEF"),
        (SWITCH_DEFAULT, "loc_2E1C"),
    )


    label("loc_2A9D")


    ChrTalk(    #49
        0x103,
        (
            "#026FIt's true this may have been a\x01",
            "good place to sort the cargo\x01",
            "because of the space...\x02\x03",

            "#027FHowever, it doesn't account for\x01",
            "the fact that they didn't take\x01",
            "the airliner to their hideout.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x1)
    Jump("loc_2E1C")

    label("loc_2B67")


    ChrTalk(    #50
        0x103,
        (
            "#026FIt's true they would have needed to\x01",
            "land in order to move the hostages...\x02\x03",

            "#027FHowever, it doesn't account for\x01",
            "the fact that they didn't take\x01",
            "the airliner to their hideout.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x1)
    Jump("loc_2E1C")

    label("loc_2C27")


    ChrTalk(    #51
        0x103,
        (
            "#026FIt's true they would have needed\x01",
            "to land in order to remove the\x01",
            "orbal engine...\x02\x03",

            "#027FHowever, it doesn't account for\x01",
            "the fact that they didn't take\x01",
            "the airliner to their hideout.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x1)
    Jump("loc_2E1C")

    label("loc_2CED")


    ChrTalk(    #52
        0x103,
        (
            "#026FIt's true the airliner is rather\x01",
            "large and easily seen...\x02\x03",

            "#027FAnd in that sense, it would seem highly\x01",
            "likely that they would leave it in a\x01",
            "different place than their hideout.\x02\x03",

            "However, that alone couldn't be\x01",
            "considered a decisive reason.\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x2)
    Jump("loc_2E1C")

    label("loc_2DEF")


    ChrTalk(    #53
        0x103,
        "#021FYes, that's exactly right.\x02",
    )

    CloseMessageWindow()
    OP_2B(0x35, 0x3)
    Jump("loc_2E1C")

    label("loc_2E1C")

    Sleep(400)

    ChrTalk(    #54
        0x103,
        (
            "#020FFrom my guess, I would imagine\x01",
            "that their hideout is in a slightly\x01",
            "peculiar place.\x02\x03",

            "Maybe 10 to 15 arge in size...\x02\x03",

            "In short, a peculiar place on which\x01",
            "only a small aircraft like the sky\x01",
            "bandits' airship could land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#008F#3PInteresting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#015FHow about terrain covered with\x01",
            "extreme differences in height,\x01",
            "like mountains and ravines...?\x02\x03",

            "#012FThat seems like a likely place\x01",
            "for the sky bandits' hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x103,
        (
            "#022FYes, that's what I've been\x01",
            "thinking, too.\x02\x03",

            "#522FHowever, if that's the case...then we\x01",
            "may be unable to do anything else.\x02\x03",

            "There's the possibility that their\x01",
            "hideout may be in a place we can't\x01",
            "reach by foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#505F#3PTh-Then what CAN we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        (
            "#025FWell...\x02\x03",

            "I hate to say it, but we may have\x01",
            "to share our conclusions with the\x01",
            "army and ask for their cooperation.\x02\x03",

            "Because they're the ones with\x01",
            "the patrol ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#009F#3PWhat...? Now you're trying to tell\x01",
            "us we should go crawling back to\x01",
            "the army and ask them for help?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#010FEither way, we still have to report\x01",
            "to them about the airliner.\x02\x03",

            "Personally speaking, I still think\x01",
            "we should cooperate with the army,\x01",
            "whatever their attitude may be.\x02\x03",

            "Especially if that means bringing\x01",
            "the hostages back safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#007F#3PI guess you're right...\x02\x03",

            "This isn't the time or place to be\x01",
            "letting my personal feelings get\x01",
            "the best of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020FFor the time being, let's get back\x01",
            "to the guild and report our findings\x01",
            "to Lugran.\x02\x03",

            "We should be able to contact\x01",
            "the Haken Gate if we use the\x01",
            "orbal telephone.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x36, 0x1, 0x800)
    OP_28(0x36, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_8_246B end

    def Function_9_340D(): pass

    label("Function_9_340D")

    EventBegin(0x0)
    OP_6D(-9690, 2130, 10650, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(293, 0)
    SetChrPos(0x101, -10200, 1630, 9500, 180)
    SetChrPos(0x103, -9190, 1620, 9480, 180)
    SetChrPos(0x102, -9720, 2020, 10410, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x10, -9650, 0, 2260, 0)
    SetChrPos(0x11, -11190, 0, 2770, 24)
    SetChrPos(0x12, -12650, 0, 3420, 24)
    SetChrPos(0x13, -14120, 0, 4070, 24)
    SetChrPos(0x14, -15860, 0, 4850, 24)
    SetChrPos(0x15, -16590, 0, 3200, 24)
    SetChrPos(0x16, -14940, 0, 2470, 24)
    SetChrPos(0x17, -13390, 0, 1780, 24)
    SetChrPos(0x18, -11940, 0, 1130, 24)
    SetChrPos(0x19, -10330, 0, 610, 24)
    SetChrPos(0x1A, -8189, 0, 2810, 336)
    SetChrPos(0x1B, -6820, 0, 3430, 336)
    SetChrPos(0x1C, -5550, 0, 4000, 336)
    SetChrPos(0x1D, -4190, 0, 4600, 336)
    SetChrPos(0x1E, -8870, 0, 510, 336)
    SetChrPos(0x1F, -7450, 0, 1150, 336)
    SetChrPos(0x20, -6170, 0, 1720, 336)
    SetChrPos(0x21, -4870, 0, 2300, 336)
    SetChrPos(0x22, -3390, 0, 2960, 336)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    FadeToBright(1000, 0)
    OP_20(0x5DC)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        (
            "#580F#1PHuh?!\x02\x03",

            "Wh-What the heck?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#017F#3PGreat... Now this was something\x01",
            "I did not expect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#025F#3PI wonder if we should be glad,\x01",
            "since they've saved us the trouble of\x01",
            "having to contact them...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x65)
    Fade(2000)
    OP_6D(9600, 0, -2009, 0)
    OP_67(0, 13000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(280000, 0)
    OP_6E(483, 0)

    def lambda_37A5():
        OP_67(0, 6570, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37A5)
    Sleep(2500)

    def lambda_37C2():
        OP_6C(39000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37C2)

    def lambda_37D2():
        OP_6E(350, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37D2)
    OP_6D(-10180, 340, 6490, 6000)

    ChrTalk(    #67
        0x10,
        (
            "#2PWe have found a suspicious\x01",
            "armed group!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x1B,
        "#2PPut your hands in the air! All of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x12,
        (
            "#5PWhat is this world coming to? A woman\x01",
            "and two kids are the sky bandits...?\x01",
            "Though the girl DOES look shifty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#509FHey now...that's just rude.\x01",
            "And who are you calling sky bandits?!\x02\x03",

            "Can't you see this shiny emblem\x01",
            "on my chest?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -9410, 0, -4900, 0)
    ClearChrFlags(0xF, 0x80)

    NpcTalk(    #71
        0xF,
        "Old Man's Voice",
        "#1PHmph! The bracer emblem, huh...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #72
        0xF,
        "Old Man's Voice",
        (
            "#1PI hope you don't think for a moment\x01",
            "something like that proves your\x01",
            "innocence.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39FA():
        OP_8E(0xFE, 0xFFFFDA58, 0x0, 0x11D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_39FA)
    Sleep(500)

    def lambda_3A1A():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3A1A)

    def lambda_3A28():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3A28)
    WaitChrThread(0x19, 0x1)

    def lambda_3A3B():
        OP_8F(0xFE, 0xFFFFD59E, 0x0, 0x30C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3A3B)

    def lambda_3A56():
        OP_8F(0xFE, 0xFFFFDF62, 0x0, 0x226, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_3A56)

    def lambda_3A71():

        label("loc_3A71")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3A71")

    QueueWorkItem2(0x19, 1, lambda_3A71)

    def lambda_3A82():

        label("loc_3A82")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3A82")

    QueueWorkItem2(0x1E, 1, lambda_3A82)

    def lambda_3A93():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3A93)
    WaitChrThread(0x10, 0x1)

    def lambda_3AA6():
        OP_8F(0xFE, 0xFFFFDD6E, 0x0, 0x76C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3AA6)

    def lambda_3AC1():

        label("loc_3AC1")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_3AC1")

    QueueWorkItem2(0x10, 1, lambda_3AC1)

    def lambda_3AD2():
        OP_6D(-9140, 1050, 8950, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AD2)

    def lambda_3AEA():
        OP_6E(306, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3AEA)
    WaitChrThread(0xF, 0x1)

    ChrTalk(    #73
        0x101,
        "#004FG-General Morgan?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        "#014FWhy are you here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xF,
        (
            "#163FAfter looking over the reports of my men, I\x01",
            "found this place to have been insufficiently\x01",
            "investigated, so I came to see for myself...\x02\x03",

            "#160FWho would have thought the lot of you\x01",
            "were conspiring with the sky bandits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#022FMight I get you to stop with the\x01",
            "accusations, General?\x02\x03",

            "We happened to find this place\x01",
            "one step ahead of your men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xF,
        (
            "#161FIf that's the truth, then why don't\x01",
            "you tell me where the sky bandits\x01",
            "are?\x02\x03",

            "Are the hostages inside that\x01",
            "airliner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#013FWe almost had the sky bandits,\x01",
            "but they managed to escape...\x02\x03",

            "And there are no hostages to be\x01",
            "found here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xF,
        (
            "#163FHmph! It looks like the truth\x01",
            "has come out...\x02\x03",

            "Most likely, you notified the sky\x01",
            "bandits to let them know we were\x01",
            "coming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#005FW-Wait a minute here!\x01",
            "How about you cut with the crap!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #81
        0xF,
        "#162F#5SMy thoughts exactly!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #82
        0xF,
        (
            "#162F#3SAll right, men!\x01",
            "Take them into custody!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_28(0x36, 0x1, 0x2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_340D end

    def Function_10_3EEB(): pass

    label("Function_10_3EEB")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F03")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3F0A")

    label("loc_3F03")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3F0A")


    def lambda_3F10():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F10)

    def lambda_3F1E():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F1E)

    ChrTalk(    #83
        0x103,
        (
            "#020FWe don't have time to be looking\x01",
            "around anywhere else.\x02\x03",

            "Right now, our first priority should\x01",
            "be investigating the airliner.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_10_3EEB end

    def Function_11_3FC8(): pass

    label("Function_11_3FC8")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3FE7")

    label("loc_3FE0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3FE7")


    def lambda_3FED():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FED)

    def lambda_3FFB():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FFB)

    ChrTalk(    #84
        0x103,
        (
            "#020FWe don't have time to be looking\x01",
            "around anywhere else.\x02\x03",

            "Right now, our first priority should\x01",
            "be investigating the airliner.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFF830, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_11_3FC8 end

    def Function_12_40A5(): pass

    label("Function_12_40A5")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40BD")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_40C4")

    label("loc_40BD")

    TurnDirection(0x103, 0x0, 400)

    label("loc_40C4")


    def lambda_40CA():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40CA)

    def lambda_40D8():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40D8)

    ChrTalk(    #85
        0x103,
        (
            "#020FWe don't have time to be looking\x01",
            "around anywhere else.\x02\x03",

            "Right now, our first priority should\x01",
            "be investigating the airliner.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x7D0, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_12_40A5 end

    def Function_13_4182(): pass

    label("Function_13_4182")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419A")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_41A1")

    label("loc_419A")

    TurnDirection(0x103, 0x0, 400)

    label("loc_41A1")


    def lambda_41A7():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41A7)

    def lambda_41B5():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41B5)

    ChrTalk(    #86
        0x103,
        (
            "#020FWe don't have time to be looking\x01",
            "around anywhere else.\x02\x03",

            "Right now, our first priority should\x01",
            "be investigating the airliner.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_4182 end

    SaveToFile()

Try(main)
