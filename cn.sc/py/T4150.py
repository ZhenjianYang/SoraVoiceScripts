from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4150   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4150.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '基库',                                 # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '村中的中年男性',                       # 14
        '贵族青年',                             # 15
        '船员',                                 # 16
        '城中中年妇女',                         # 17
        '街上中年男人２',                       # 18
        '街上中年女人２',                       # 19
        '街上中年男人',                         # 20
        '街上青年女人',                         # 21
        '伯登',                                 # 22
        '王国军士兵',                           # 23
        '王国军士兵',                           # 24
        '王都格兰赛尔·北街区',                 # 25
        '庭园大道方向',                         # 26
        '王都格兰赛尔·东街区',                 # 27
        '王都格兰赛尔·西街区',                 # 28
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
        'ED6_DT07/CH02320 ._CH',             # 00
        'ED6_DT26/CH20238 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01150 ._CH',             # 0A
        'ED6_DT26/CH20254 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02320P._CP',             # 00
        'ED6_DT26/CH20238P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01150P._CP',             # 0A
        'ED6_DT26/CH20254P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6280,
        Z                   = 0,
        Y                   = 2180,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -6430,
        Z                   = 0,
        Y                   = -22020,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -870,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 0,
        Y                   = -1920,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 6040,
        Direction           = 172,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -8540,
        Z                   = 250,
        Y                   = 4630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -5690,
        Z                   = 0,
        Y                   = -7580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 13060,
        Z                   = 250,
        Y                   = 4130,
        Direction           = 51,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -8230,
        Z                   = 250,
        Y                   = -31580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 7330,
        Z                   = 250,
        Y                   = -27330,
        Direction           = 37,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 4760,
        Z                   = 0,
        Y                   = -39600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = -29870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 10,
        Z                   = 250,
        Y                   = 36990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = -90220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54990,
        Z                   = 0,
        Y                   = -1130,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -44420,
        Z                   = 0,
        Y                   = -19990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5000,
        Y                   = -2000,
        Z                   = -65600,
        Range               = 5000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF0344,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_4C7",          # 01, 1
        "Function_2_536",          # 02, 2
        "Function_3_6B3",          # 03, 3
        "Function_4_722",          # 04, 4
        "Function_5_791",          # 05, 5
        "Function_6_7B5",          # 06, 6
        "Function_7_824",          # 07, 7
        "Function_8_893",          # 08, 8
        "Function_9_8AC",          # 09, 9
        "Function_10_8C5",         # 0A, 10
        "Function_11_8DE",         # 0B, 11
        "Function_12_8F7",         # 0C, 12
        "Function_13_910",         # 0D, 13
        "Function_14_929",         # 0E, 14
        "Function_15_942",         # 0F, 15
        "Function_16_95B",         # 10, 16
        "Function_17_974",         # 11, 17
        "Function_18_98D",         # 12, 18
        "Function_19_9A6",         # 13, 19
        "Function_20_9BF",         # 14, 20
        "Function_21_A45",         # 15, 21
        "Function_22_B21",         # 16, 22
        "Function_23_BD6",         # 17, 23
        "Function_24_1332",        # 18, 24
        "Function_25_15BD",        # 19, 25
        "Function_26_180E",        # 1A, 26
        "Function_27_1AB5",        # 1B, 27
        "Function_28_1D5C",        # 1C, 28
        "Function_29_1FAD",        # 1D, 29
        "Function_30_2051",        # 1E, 30
        "Function_31_28EF",        # 1F, 31
        "Function_32_293E",        # 20, 32
        "Function_33_298D",        # 21, 33
        "Function_34_29DC",        # 22, 34
        "Function_35_2A63",        # 23, 35
        "Function_36_2A67",        # 24, 36
        "Function_37_2A6B",        # 25, 37
        "Function_38_2A6F",        # 26, 38
        "Function_39_2A73",        # 27, 39
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_488")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_4B5")

    label("loc_488")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_494"),
        (SWITCH_DEFAULT, "loc_4B5"),
    )


    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_4B2")

    Jump("loc_4B5")

    label("loc_4B5")

    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_472 end

    def Function_1_4C7(): pass

    label("Function_1_4C7")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_71(0x2, 0x10)
    OP_71(0x0, 0x10)
    OP_71(0x3, 0x10)
    OP_71(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_524")
    OP_1B(0xA, 0x0, 0x1C)
    OP_1B(0xB, 0x0, 0x19)
    OP_1B(0xC, 0x0, 0x1A)
    OP_1B(0xD, 0x0, 0x19)
    OP_1B(0xE, 0x0, 0x1B)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_535")
    OP_1B(0x9, 0x0, 0x1D)

    label("loc_535")

    Return()

    # Function_1_4C7 end

    def Function_2_536(): pass

    label("Function_2_536")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_69D")

    label("loc_55B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_69D")

    label("loc_574")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_69D")

    label("loc_58D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_69D")

    label("loc_5A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_69D")

    label("loc_5BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D8")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_69D")

    label("loc_5D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F1")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_69D")

    label("loc_5F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_69D")

    label("loc_60A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_623")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_69D")

    label("loc_623")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_69D")

    label("loc_63C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_655")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_69D")

    label("loc_655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_69D")

    label("loc_66E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_687")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_69D")

    label("loc_687")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_69D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_69D")

    label("loc_6B2")

    Return()

    # Function_2_536 end

    def Function_3_6B3(): pass

    label("Function_3_6B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_721")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_3_6B3")

    label("loc_721")

    Return()

    # Function_3_6B3 end

    def Function_4_722(): pass

    label("Function_4_722")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_790")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_4_722")

    label("loc_790")

    Return()

    # Function_4_722 end

    def Function_5_791(): pass

    label("Function_5_791")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B4")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_5_791")

    label("loc_7B4")

    Return()

    # Function_5_791 end

    def Function_6_7B5(): pass

    label("Function_6_7B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_823")
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x1298, 0x0, 0xFFFFFB5A, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_6_7B5")

    label("loc_823")

    Return()

    # Function_6_7B5 end

    def Function_7_824(): pass

    label("Function_7_824")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_892")
    OP_8E(0xFE, 0xFFFFEE44, 0x0, 0xFFFFAFC4, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEEB2, 0x0, 0xFFFF6550, 0x9C4, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_7_824")

    label("loc_892")

    Return()

    # Function_7_824 end

    def Function_8_893(): pass

    label("Function_8_893")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_893 end

    def Function_9_8AC(): pass

    label("Function_9_8AC")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_8AC end

    def Function_10_8C5(): pass

    label("Function_10_8C5")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_8C5 end

    def Function_11_8DE(): pass

    label("Function_11_8DE")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_8DE end

    def Function_12_8F7(): pass

    label("Function_12_8F7")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_8F7 end

    def Function_13_910(): pass

    label("Function_13_910")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_910 end

    def Function_14_929(): pass

    label("Function_14_929")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_929 end

    def Function_15_942(): pass

    label("Function_15_942")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_942 end

    def Function_16_95B(): pass

    label("Function_16_95B")

    TalkBegin(0xFE)

    ChrTalk(    #8
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_95B end

    def Function_17_974(): pass

    label("Function_17_974")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_974 end

    def Function_18_98D(): pass

    label("Function_18_98D")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_98D end

    def Function_19_9A6(): pass

    label("Function_19_9A6")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0xFE,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_9A6 end

    def Function_20_9BF(): pass

    label("Function_20_9BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_9ED")

    ChrTalk(    #12
        0xFE,
        (
            "现在，鸟向西\x01",
            "飞去了没有呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A41")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_A41")

    ChrTalk(    #13
        0xFE,
        "呼，夜晚的冷气真令人心情舒畅。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "走在夜晚的市街上\x01",
            "不觉得也挺风雅吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A41")

    TalkEnd(0xFE)
    Return()

    # Function_20_9BF end

    def Function_21_A45(): pass

    label("Function_21_A45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_A87")

    ChrTalk(    #15
        0xFE,
        (
            "哎呀，这么晚了\x01",
            "打算去哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "出门要当心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1D")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_B1D")

    ChrTalk(    #17
        0xFE,
        (
            "似乎有武装的神秘人物\x01",
            "在这个地区出没呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "由于希德中校的指示王城\x01",
            "配备了一个中队呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "虽然不知道是什么人\x01",
            "对王都应该是没法下手的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1D")

    TalkEnd(0xFE)
    Return()

    # Function_21_A45 end

    def Function_22_B21(): pass

    label("Function_22_B21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_B6F")

    ChrTalk(    #20
        0xFE,
        "市街应该还安全……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "不过注意不要去\x01",
            "没什么人烟的地方哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD2")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_BD2")

    ChrTalk(    #22
        0xFE,
        "结社……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "目的果然还是\x01",
            "妨碍签字仪式吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "在有我们的王都地区\x01",
            "引起骚乱真是愚蠢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2")

    TalkEnd(0xFE)
    Return()

    # Function_22_B21 end

    def Function_23_BD6(): pass

    label("Function_23_BD6")

    EventBegin(0x0)
    AddParty(0x42, 0xFF, 0xFF)
    SetChrFlags(0x143, 0x80)
    OP_6D(-1140, 0, -63570, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(0, 0)
    OP_6E(580, 0)
    SetChrPos(0x101, 630, 0, -64819, 0)
    SetChrPos(0x109, -700, 0, -65820, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x109, 0x80)
    FadeToBright(2000, 0)

    def lambda_C59():
        OP_6D(50, 0, 5920, 14000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C59)

    def lambda_C71():
        OP_6C(320000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C71)

    def lambda_C81():
        OP_67(0, 14750, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C81)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    OP_6D(110, 0, -61800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(134000, 0)
    OP_6E(200, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x109, 0x80)

    def lambda_CEA():
        OP_8E(0xFE, 0x276, 0x0, 0xFFFF0FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEA)

    def lambda_D05():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0xFFFF0F38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D05)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #25
        0x101,
        (
            "#1002F#5P呼……\x01",
            "太阳下山了呢。\x02\x03",

            "艾尔贝离宫\x01",
            "会变成怎样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1060F不过，协会\x01",
            "可能也有联络了。\x02\x03",

            "嗨，去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1015F#5P嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)
    Sleep(500)

    ChrTalk(    #28
        0x101,
        (
            "#1007F#5P嗯……凯文先生。\x02\x03",

            "刚才真对不起。\x01",
            "对你乱发脾气了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #29
        0x109,
        (
            "#1061F没关系，没关系。\x02\x03",

            "是为了男朋友的事\x01",
            "脑子晕乎乎了吧？\x02\x03",

            "#1060F我不在意的，放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1017F#5P嘿嘿，谢谢。\x02\x03",

            "#1015F不过不好意思\x01",
            "不能完全信任你\x01",
            "这话是不会收回的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1068F哎呀，真服了你。\x02\x03",

            "#1060F不过也好，关于这个\x01",
            "也许协会也……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x143, 0x80)
    SetChrPos(0x143, 30, 300, -49360, 180)

    NpcTalk(    #32
        0x143,
        "男性的声音",
        "#2P艾丝蒂尔大人……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_F86():
        OP_6D(220, 0, -60300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F86)

    def lambda_F9E():
        OP_67(0, 7890, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F9E)

    def lambda_FB6():
        OP_6E(217, 2000)
        ExitThread()

    QueueWorkItem(0x143, 1, lambda_FB6)

    def lambda_FC6():
        TurnDirection(0xFE, 0x143, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC6)
    Sleep(50)

    def lambda_FD9():
        TurnDirection(0xFE, 0x143, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD9)
    OP_8E(0x143, 0x1E, 0x0, 0xFFFF1A96, 0xBB8, 0x0)
    WaitChrThread(0x143, 0x1)

    ChrTalk(    #33
        0x101,
        "#1004F咦，菲利普先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x143,
        (
            "#722F#6P你、你好。\x01",
            "今天早上真是失礼了。\x02\x03",

            "那个，艾丝蒂尔大人……\x02\x03",

            "您有在哪里\x01",
            "见过公爵阁下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1004F哎……\x01",
            "早上倒是见过……\x02\x03",

            "#1015F公爵先生怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x143,
        (
            "#722F#6P傍晚出去逛街\x01",
            "就没再回城里来。\x02\x03",

            "阁下能去的地方\x01",
            "我都找过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1007F啊啊真是的，这么忙的时候\x01",
            "到底在做什么……\x02\x03",

            "#1006F菲利普先生。\x01",
            "我们现在要回协会\x01",
            "请一起来吧。\x02\x03",

            "如果公爵先生有麻烦\x01",
            "说不定会发来联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x143,
        (
            "#722F#6P是、是啊……\x01",
            "那么请让我同行吧。\x02\x03",

            "#721F……对了，这位是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1062F啊，七耀教会的巡回神父\x01",
            "凯文·格拉汉姆。\x02\x03",

            "#1061F请多多指教～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x143,
        (
            "#720F#6P这真是冒昧了。\x02\x03",

            "我是公爵阁下\x01",
            "的管家，\x01",
            "名叫菲利普……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1007F啊～寒暄就省了吧。\x02\x03",

            "#1006F赶快回协会吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(290, 0, -61590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 290, 0, -61590, 0)
    SetChrPos(0x109, 290, 0, -61590, 0)
    SetChrPos(0x143, 290, 0, -61590, 0)
    OP_A2(0x1639)
    OP_1B(0xA, 0x0, 0x1C)
    OP_1B(0xB, 0x0, 0x19)
    OP_1B(0xC, 0x0, 0x1A)
    OP_1B(0xD, 0x0, 0x19)
    OP_1B(0xE, 0x0, 0x1B)
    OP_1B(0x9, 0x0, 0x1D)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_BD6 end

    def Function_24_1332(): pass

    label("Function_24_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1393")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1364")

    label("loc_135D")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1364")


    ChrTalk(    #42
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D8")

    label("loc_1393")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A9")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_13B0")

    label("loc_13A9")

    TurnDirection(0x106, 0x0, 400)

    label("loc_13B0")


    ChrTalk(    #43
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_15BC")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1515")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1440")

    ChrTalk(    #44
        0x101,
        (
            "#1002F没空磨蹭了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_1440")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147C")

    ChrTalk(    #45
        0x109,
        (
            "#1063F时间似乎无多。\x01",
            "赶紧去西街区那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_147C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BD")

    ChrTalk(    #46
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_14BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F7")

    ChrTalk(    #47
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F7")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_15BC")

    label("loc_1515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1561")

    ChrTalk(    #48
        0x101,
        (
            "#1000F……已经这么晚了。\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_1561")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159C")

    ChrTalk(    #49
        0x109,
        (
            "#1060F……已经这么晚了啊。\x01",
            "赶快去协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159C")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_15BC")

    Return()

    # Function_24_1332 end

    def Function_25_15BD(): pass

    label("Function_25_15BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1666")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_161E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E8")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_15EF")

    label("loc_15E8")

    TurnDirection(0x103, 0x0, 400)

    label("loc_15EF")


    ChrTalk(    #50
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663")

    label("loc_161E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1634")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_163B")

    label("loc_1634")

    TurnDirection(0x106, 0x0, 400)

    label("loc_163B")


    ChrTalk(    #51
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1663")

    Jump("loc_17ED")

    label("loc_1666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_176A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B0")

    ChrTalk(    #52
        0x101,
        (
            "#1002F没空磨蹭了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_16B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(    #53
        0x109,
        (
            "#1063F时间似乎无多。\x01",
            "赶紧去西街区那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_16EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172D")

    ChrTalk(    #54
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_172D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1767")

    ChrTalk(    #55
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1767")

    Jump("loc_17ED")

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17ED")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B2")

    ChrTalk(    #56
        0x101,
        (
            "#1000F……已经这么晚了。\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_17B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17ED")

    ChrTalk(    #57
        0x109,
        (
            "#1060F……已经这么晚了啊。\x01",
            "赶快去协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17ED")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_25_15BD end

    def Function_26_180E(): pass

    label("Function_26_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_186F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1839")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1840")

    label("loc_1839")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1840")


    ChrTalk(    #58
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B4")

    label("loc_186F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1885")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_188C")

    label("loc_1885")

    TurnDirection(0x106, 0x0, 400)

    label("loc_188C")


    ChrTalk(    #59
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B4")

    Jump("loc_1A3E")

    label("loc_18B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19BB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1901")

    ChrTalk(    #60
        0x101,
        (
            "#1002F没空磨蹭了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B8")

    label("loc_1901")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_193D")

    ChrTalk(    #61
        0x109,
        (
            "#1063F时间似乎无多。\x01",
            "赶紧去西街区那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B8")

    label("loc_193D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197E")

    ChrTalk(    #62
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B8")

    label("loc_197E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B8")

    ChrTalk(    #63
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B8")

    Jump("loc_1A3E")

    label("loc_19BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A03")

    ChrTalk(    #64
        0x101,
        (
            "#1000F……已经这么晚了。\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3E")

    label("loc_1A03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3E")

    ChrTalk(    #65
        0x109,
        (
            "#1060F……已经这么晚了啊。\x01",
            "赶快去协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3E")

    OP_59()

    def lambda_1A45():
        OP_6D(-3370, 0, 11000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A45)
    Fade(1000)
    SetChrPos(0x0, -3370, 0, 12430, 180)
    SetChrPos(0x1, -3370, 0, 12430, 180)
    SetChrPos(0x2, -3370, 0, 12430, 180)
    SetChrPos(0x143, -3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_26_180E end

    def Function_27_1AB5(): pass

    label("Function_27_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B5E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B16")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1AE7")

    label("loc_1AE0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1AE7")


    ChrTalk(    #66
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B5B")

    label("loc_1B16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2C")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_1B33")

    label("loc_1B2C")

    TurnDirection(0x106, 0x0, 400)

    label("loc_1B33")


    ChrTalk(    #67
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5B")

    Jump("loc_1CE5")

    label("loc_1B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C62")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA8")

    ChrTalk(    #68
        0x101,
        (
            "#1002F没空磨蹭了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5F")

    label("loc_1BA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE4")

    ChrTalk(    #69
        0x109,
        (
            "#1063F时间似乎无多。\x01",
            "赶紧去西街区那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5F")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C25")

    ChrTalk(    #70
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5F")

    label("loc_1C25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C5F")

    ChrTalk(    #71
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5F")

    Jump("loc_1CE5")

    label("loc_1C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CAA")

    ChrTalk(    #72
        0x101,
        (
            "#1000F……已经这么晚了。\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE5")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE5")

    ChrTalk(    #73
        0x109,
        (
            "#1060F……已经这么晚了啊。\x01",
            "赶快去协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE5")

    OP_59()

    def lambda_1CEC():
        OP_6D(3370, 0, 11000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1CEC)
    Fade(1000)
    SetChrPos(0x0, 3370, 0, 12430, 180)
    SetChrPos(0x1, 3370, 0, 12430, 180)
    SetChrPos(0x2, 3370, 0, 12430, 180)
    SetChrPos(0x143, 3370, 0, 12430, 180)
    OP_0D()
    OP_8C(0x0, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_27_1AB5 end

    def Function_28_1D5C(): pass

    label("Function_28_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E05")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1DBD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D87")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_1D8E")

    label("loc_1D87")

    TurnDirection(0x103, 0x0, 400)

    label("loc_1D8E")


    ChrTalk(    #74
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E02")

    label("loc_1DBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD3")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_1DDA")

    label("loc_1DD3")

    TurnDirection(0x106, 0x0, 400)

    label("loc_1DDA")


    ChrTalk(    #75
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶快去码头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E02")

    Jump("loc_1F8C")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F09")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E4F")

    ChrTalk(    #76
        0x101,
        (
            "#1002F没空磨蹭了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F06")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8B")

    ChrTalk(    #77
        0x109,
        (
            "#1063F时间似乎无多。\x01",
            "赶紧去西街区那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F06")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECC")

    ChrTalk(    #78
        0x103,
        (
            "#022F似乎时间不多了呢。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F06")

    label("loc_1ECC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(    #79
        0x106,
        (
            "#050F没时间浪费了。\x01",
            "赶紧去西街区那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F06")

    Jump("loc_1F8C")

    label("loc_1F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8C")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F51")

    ChrTalk(    #80
        0x101,
        (
            "#1000F……已经这么晚了。\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8C")

    label("loc_1F51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8C")

    ChrTalk(    #81
        0x109,
        (
            "#1060F……已经这么晚了啊。\x01",
            "赶快去协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8C")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_28_1D5C end

    def Function_29_1FAD(): pass

    label("Function_29_1FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2050")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF5")

    ChrTalk(    #82
        0x101,
        (
            "#1000F……已经这么晚了。\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2030")

    label("loc_1FF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2030")

    ChrTalk(    #83
        0x109,
        (
            "#1060F……已经这么晚了啊。\x01",
            "赶快去协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2030")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2050")

    Return()

    # Function_29_1FAD end

    def Function_30_2051(): pass

    label("Function_30_2051")

    EventBegin(0x0)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2070")
    Call(0, 34)

    label("loc_2070")

    RemoveParty(0x42, 0xFF)
    RemoveParty(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_208E")
    AddParty(0x2, 0xF7, 0xFF)
    OP_31(0x2, 0x0, 0x38)
    OP_31(0x2, 0xFE, 0x0)
    Jump("loc_209C")

    label("loc_208E")

    AddParty(0x5, 0xF7, 0xFF)
    OP_31(0x5, 0x0, 0x38)
    OP_31(0x5, 0xFE, 0x0)

    label("loc_209C")

    AddParty(0x8, 0xF8, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    OP_6D(8150, 250, -13250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    Sleep(500)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1F)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0x21)
    Sleep(500)

    def lambda_2171():
        OP_6D(5120, 0, -13430, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2171)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x10)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #84
        0x101,
        (
            "#1002F#6P茶会……\x01",
            "你觉得到底是在哪里？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2248")

    ChrTalk(    #85
        0x106,
        (
            "#053F#2P最可能的是\x01",
            "格兰赛尔城……\x02\x03",

            "#050F但记得有相当数量的\x01",
            "士兵聚集着。\x02\x03",

            "选其他地方比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B3")

    label("loc_2248")


    ChrTalk(    #86
        0x103,
        (
            "#026F#2P最可能的地方\x01",
            "是格兰赛尔城……\x02\x03",

            "#020F不过记得有相当数量的\x01",
            "士兵聚集着吧。\x02\x03",

            "选其他地方比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B3")


    ChrTalk(    #87
        0x109,
        (
            "#1067F嗯～话虽如此\x01",
            "这个城市真宽广啊。\x02\x03",

            "要是没个大体的线索……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -14000, 6000, -18050, 90)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #88
        0x101,
        "#1011F#5P啊……！\x02",
    )

    CloseMessageWindow()
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_2367():
        OP_6D(-1390, 0, -15440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2367)

    def lambda_237F():
        OP_67(0, 12610, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_237F)

    def lambda_2397():
        OP_6B(1940, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2397)

    def lambda_23A7():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23A7)

    def lambda_23B7():
        OP_6E(362, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_23B7)

    def lambda_23C7():

        label("loc_23C7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_23C7")

    QueueWorkItem2(0x109, 0, lambda_23C7)

    def lambda_23D8():

        label("loc_23D8")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_23D8")

    QueueWorkItem2(0xF7, 0, lambda_23D8)
    WaitChrThread(0x101, 0x1)
    OP_8E(0x8, 0x0, 0x7D0, 0xFFFFB1E0, 0x2710, 0x0)
    OP_44(0x101, 0x0)

    def lambda_2406():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2406)

    def lambda_2414():
        OP_6D(4980, 0, -13500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2414)

    def lambda_242C():
        OP_67(0, 11320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_242C)

    def lambda_2444():
        OP_6B(1800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2444)
    OP_44(0x109, 0x0)
    OP_97(0x8, 0x7D0, 0xFFFFC180, 0xFFFD8F00, 0x1770, 0x1)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 225, 400)
    OP_44(0xF7, 0x0)

    def lambda_2482():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2482)

    def lambda_2490():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2490)
    OP_8F(0x8, 0x10CC, 0x12C, 0xFFFFCA18, 0x3E8, 0x0)
    Fade(500)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x101, 1)

    ChrTalk(    #89
        0x101,
        "#1018F#6P基库！\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #90
        0x109,
        "#1064F哇哇，什么东西！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253F")

    ChrTalk(    #91
        0x106,
        "#051F哦哦，来了啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_255C")

    label("loc_253F")


    ChrTalk(    #92
        0x103,
        "#021F呵呵，助手登场呢！\x02",
    )

    CloseMessageWindow()

    label("loc_255C")


    ChrTalk(    #93
        0x8,
        (
            "#310F#2P啾啾！\x02\x03",

            "啾～～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1006F#6P虽、虽然搞不太清楚状况……\x02\x03",

            "它是打算\x01",
            "给我们带路？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        "#311F#2P啾⊙\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x8, 4300, 300, -13800, 225)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x8, 0x80)
    OP_0D()
    OP_22(0x8C, 0x0, 0x64)

    def lambda_2602():
        OP_6D(4980, 2000, -13500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2602)

    def lambda_261A():
        OP_8F(0xFE, 0x1194, 0xFA0, 0xFFFFC950, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_261A)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0x101, 0x3)
    OP_8C(0x8, 270, 400)
    Sleep(300)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)

    def lambda_2655():
        OP_8E(0xFE, 0xFFFFA25E, 0x1770, 0xFFFFB1CC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2655)
    Sleep(500)

    def lambda_2675():

        label("loc_2675")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2675")

    QueueWorkItem2(0x101, 0, lambda_2675)

    def lambda_2686():

        label("loc_2686")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2686")

    QueueWorkItem2(0x109, 0, lambda_2686)

    def lambda_2697():

        label("loc_2697")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2697")

    QueueWorkItem2(0xF7, 0, lambda_2697)

    def lambda_26A8():
        OP_6D(-30650, 0, -19610, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_26A8)

    def lambda_26C0():
        OP_6B(2530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_26C0)

    def lambda_26D0():
        OP_6C(279000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_26D0)
    WaitChrThread(0x8, 0x2)
    OP_44(0x8, 0x1)
    OP_8E(0x8, 0xFFFF737E, 0x1F40, 0xFFFFB1CC, 0x1770, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0xF7, 0x0)
    SetChrPos(0x101, -15970, 0, -20020, 270)
    SetChrPos(0xF7, -15260, 0, -19020, 270)
    SetChrPos(0x109, -15170, 0, -21220, 270)

    def lambda_273C():
        OP_8E(0xFE, 0xFFFF92BE, 0x0, 0xFFFFB1CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_273C)
    Sleep(50)

    def lambda_275C():
        OP_8E(0xFE, 0xFFFF9584, 0x0, 0xFFFFB5B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_275C)
    Sleep(50)

    def lambda_277C():
        OP_8E(0xFE, 0xFFFF95DE, 0x0, 0xFFFFAD1C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_277C)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27CA")

    ChrTalk(    #96
        0x106,
        "#555F#4P西街区方向吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EA")

    label("loc_27CA")


    ChrTalk(    #97
        0x103,
        "#027F#4P西街区方向是吧……\x02",
    )

    CloseMessageWindow()

    label("loc_27EA")


    ChrTalk(    #98
        0x101,
        "#1006F#5P嗯，去看看吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1068F#6P唉～……\x01",
            "你们，可真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    Fade(1000)
    OP_6D(-27270, 0, -19880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -27970, 0, -20020, 270)
    SetChrPos(0x1, -27970, 0, -20020, 270)
    SetChrPos(0x2, -27970, 0, -20020, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x163A)
    OP_A3(0x10F1)
    OP_1B(0x9, 0xFF, 0xFFFF)
    OP_28(0x8E, 0x4, 0x2)
    OP_28(0x8E, 0x4, 0x8)
    OP_28(0x8E, 0x1, 0x1)
    EventEnd(0x0)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    Return()

    # Function_30_2051 end

    def Function_31_28EF(): pass

    label("Function_31_28EF")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)

    def lambda_2916():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2916)
    OP_8E(0xFE, 0xF28, 0x0, 0xFFFFCA5E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_28EF end

    def Function_32_293E(): pass

    label("Function_32_293E")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)

    def lambda_2965():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2965)
    OP_8E(0xFE, 0x1590, 0x28, 0xFFFFC7DE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_32_293E end

    def Function_33_298D(): pass

    label("Function_33_298D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11480, 750, -13010, 270)

    def lambda_29B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29B4)
    OP_8E(0xFE, 0x15AE, 0x0, 0xFFFFCC52, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_33_298D end

    def Function_34_29DC(): pass

    label("Function_34_29DC")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A56"),
        (1, "loc_2A5C"),
        (SWITCH_DEFAULT, "loc_2A62"),
    )


    label("loc_2A56")

    OP_A2(0x1200)
    Jump("loc_2A62")

    label("loc_2A5C")

    OP_A2(0x1201)
    Jump("loc_2A62")

    label("loc_2A62")

    Return()

    # Function_34_29DC end

    def Function_35_2A63(): pass

    label("Function_35_2A63")

    SetPlaceName(0xB9)
    Return()

    # Function_35_2A63 end

    def Function_36_2A67(): pass

    label("Function_36_2A67")

    SetPlaceName(0xB0)
    Return()

    # Function_36_2A67 end

    def Function_37_2A6B(): pass

    label("Function_37_2A6B")

    SetPlaceName(0xB2)
    Return()

    # Function_37_2A6B end

    def Function_38_2A6F(): pass

    label("Function_38_2A6F")

    SetPlaceName(0xAE)
    Return()

    # Function_38_2A6F end

    def Function_39_2A73(): pass

    label("Function_39_2A73")

    SetPlaceName(0xB3)
    Return()

    # Function_39_2A73 end

    SaveToFile()

Try(main)
