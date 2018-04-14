from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0010   ._SN',
        MapName             = 'event',
        Location            = 'E0010.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        '古兰托机长',                           # 9
        '乘务员迪蒙',                           # 10
        '乘务员卡尔托斯',                       # 11
        '乘务员卡拉莉丝',                       # 12
        '乘务员波嘉',                           # 13
        '罗伊德',                               # 14
        '雪拉扎德',                             # 15
        '阿加特',                               # 16
        '修女萝萨',                             # 17
        '菲利奥',                               # 18
        '拉科舒',                               # 19
        '西蒙',                                 # 20
        '巴雷尔',                               # 21
        '奥维德',                               # 22
        '乘客',                                 # 23
        '乘客',                                 # 24
        '乘客',                                 # 25
        '乘客',                                 # 26
        '乘客',                                 # 27
        '乘客',                                 # 28
        '登克',                                 # 29
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
        'ED6_DT07/CH01443 ._CH',             # 00
        'ED6_DT07/CH01290 ._CH',             # 01
        'ED6_DT07/CH01293 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01290 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH00023 ._CH',             # 06
        'ED6_DT07/CH00053 ._CH',             # 07
        'ED6_DT07/CH01410 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01030 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01143 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH01013 ._CH',             # 0E
        'ED6_DT07/CH01213 ._CH',             # 0F
        'ED6_DT07/CH01103 ._CH',             # 10
        'ED6_DT07/CH01133 ._CH',             # 11
        'ED6_DT07/CH01490 ._CH',             # 12
        'ED6_DT07/CH01043 ._CH',             # 13
        'ED6_DT07/CH01450 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH01443P._CP',             # 00
        'ED6_DT07/CH01290P._CP',             # 01
        'ED6_DT07/CH01293P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01290P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH00023P._CP',             # 06
        'ED6_DT07/CH00053P._CP',             # 07
        'ED6_DT07/CH01410P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01030P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01143P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH01013P._CP',             # 0E
        'ED6_DT07/CH01213P._CP',             # 0F
        'ED6_DT07/CH01103P._CP',             # 10
        'ED6_DT07/CH01133P._CP',             # 11
        'ED6_DT07/CH01490P._CP',             # 12
        'ED6_DT07/CH01043P._CP',             # 13
        'ED6_DT07/CH01450P._CP',             # 14
    )

    DeclNpc(
        X                   = 59020,
        Z                   = -600,
        Y                   = 49310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 60800,
        Z                   = -2000,
        Y                   = 53360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 59190,
        Z                   = -1950,
        Y                   = 54200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 88840,
        Z                   = 0,
        Y                   = 47400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 85950,
        Z                   = 0,
        Y                   = 9240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 115970,
        Z                   = 0,
        Y                   = 11300,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 117330,
        Z                   = 200,
        Y                   = 1160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 117330,
        Z                   = 200,
        Y                   = 1160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 89500,
        Z                   = 0,
        Y                   = 9050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 91250,
        Z                   = 0,
        Y                   = 44510,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 91250,
        Z                   = 0,
        Y                   = 45520,
        Direction           = 120,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 57200,
        Z                   = 0,
        Y                   = -1850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 117490,
        Z                   = 100,
        Y                   = 5290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 89340,
        Z                   = -1000,
        Y                   = 52850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 89270,
        Z                   = 200,
        Y                   = -3230,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 85350,
        Z                   = 150,
        Y                   = -1370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 117490,
        Z                   = 100,
        Y                   = 7300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 89270,
        Z                   = 150,
        Y                   = 430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 88030,
        Z                   = 0,
        Y                   = 430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 113400,
        Z                   = 100,
        Y                   = -630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 31990,
        Z                   = 0,
        Y                   = 5410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_4A7",          # 01, 1
        "Function_2_4CD",          # 02, 2
        "Function_3_64A",          # 03, 3
        "Function_4_BC4",          # 04, 4
        "Function_5_C85",          # 05, 5
        "Function_6_D61",          # 06, 6
        "Function_7_EB9",          # 07, 7
        "Function_8_F65",          # 08, 8
        "Function_9_102F",         # 09, 9
        "Function_10_12BE",        # 0A, 10
        "Function_11_13DE",        # 0B, 11
        "Function_12_149D",        # 0C, 12
        "Function_13_150D",        # 0D, 13
        "Function_14_1B2B",        # 0E, 14
        "Function_15_1E94",        # 0F, 15
        "Function_16_1F50",        # 10, 16
        "Function_17_1FD2",        # 11, 17
        "Function_18_20A4",        # 12, 18
        "Function_19_2169",        # 13, 19
        "Function_20_224F",        # 14, 20
        "Function_21_22FA",        # 15, 21
        "Function_22_23FE",        # 16, 22
        "Function_23_25D0",        # 17, 23
        "Function_24_26D3",        # 18, 24
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_422"),
        (102, "loc_422"),
        (103, "loc_422"),
        (104, "loc_422"),
        (105, "loc_422"),
        (106, "loc_422"),
        (107, "loc_422"),
        (109, "loc_422"),
        (110, "loc_422"),
        (115, "loc_422"),
        (SWITCH_DEFAULT, "loc_4A6"),
    )


    label("loc_422")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 7)), scpexpr(EXPR_END)), "loc_43D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 0)), scpexpr(EXPR_END)), "loc_44E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 1)), scpexpr(EXPR_END)), "loc_45F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 2)), scpexpr(EXPR_END)), "loc_470")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 3)), scpexpr(EXPR_END)), "loc_481")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 5)), scpexpr(EXPR_END)), "loc_492")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_492")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A3")
    Event(0, 24)

    label("loc_4A3")

    Jump("loc_4A6")

    label("loc_4A6")

    Return()

    # Function_0_3F2 end

    def Function_1_4A7(): pass

    label("Function_1_4A7")

    OP_22(0x7A, 0x1, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4BB")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_4C0")

    label("loc_4BB")

    ClearChrFlags(0xF, 0x80)

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 1)), scpexpr(EXPR_END)), "loc_4CC")
    ClearChrFlags(0xD, 0x10)

    label("loc_4CC")

    Return()

    # Function_1_4A7 end

    def Function_2_4CD(): pass

    label("Function_2_4CD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_634")

    label("loc_4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_634")

    label("loc_50B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_634")

    label("loc_524")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_634")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_634")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_634")

    label("loc_56F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_634")

    label("loc_588")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_634")

    label("loc_5A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_634")

    label("loc_5BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_634")

    label("loc_5D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_634")

    label("loc_5EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_605")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_634")

    label("loc_605")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_634")

    label("loc_61E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_634")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_634")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_649")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_634")

    label("loc_649")

    Return()

    # Function_2_4CD end

    def Function_3_64A(): pass

    label("Function_3_64A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 7)), scpexpr(EXPR_END)), "loc_81C")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_681")
    SetChrSubChip(0xFE, 1)
    Jump("loc_6A7")

    label("loc_681")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A2")
    SetChrSubChip(0xFE, 2)
    Jump("loc_6A7")

    label("loc_6A2")

    SetChrSubChip(0xFE, 0)

    label("loc_6A7")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_71A")

    ChrTalk(    #0
        0xFE,
        "能找到父亲可真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "虽然时间已经所剩无几，\x01",
            "不过抵达前好好享受一下空中旅行吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_819")

    label("loc_71A")

    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "……话说回来，\x01",
            "你们找到自己父亲了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1000F啊，嗯。\x01",
            "总算是回来了。\x02\x03",

            "#1007F……真的是在最后关头呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "是吗，这实在是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "这些话我只在这里说，\x01",
            "其实我也稍微有点担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "毕竟他突然提出\x01",
            "要下船的要求嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1008F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_819")

    Jump("loc_BBB")

    label("loc_81C")

    OP_A2(0x1207)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    SetChrSubChip(0xFE, 1)
    Jump("loc_87C")

    label("loc_856")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_877")
    SetChrSubChip(0xFE, 2)
    Jump("loc_87C")

    label("loc_877")

    SetChrSubChip(0xFE, 0)

    label("loc_87C")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #8
        0xFE,
        "来操舵室有什么事吗？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #9
        0xFE,
        (
            "啊，你难道是\x01",
            "解决那起空贼事件的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1011F啊，好久不见了，船长先生。\x02\x03",

            "还记得上次见面是在空贼团的要塞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "哎呀，果然是这么回事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "对了对了，\x01",
            "我好像还没有正式向你们道过谢吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "我在这里代表本船的全体成员，\x01",
            "再次向你表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1008F啊哈哈，太客气了。\x01",
            "我们只是尽我们的义务而已。\x02\x03",

            "#1000F不过，感觉真不可思议呢。\x02\x03",

            "之前在废坑发现的林德号……\x01",
            "现在居然能够像这个样子来搭乘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "虽然维修花费了比较多的时间，\x01",
            "不过基本上已经恢复了原貌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "如果它知道你们也坐在上面，\x01",
            "这条船肯定也会加倍努力的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(600)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0x101,
        "#1004F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "哈哈，\x01",
            "看来它听到我们的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "照现在这个风速的话，\x01",
            "我想应该很快就会抵达卢安的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "虽然有点依依不舍，但至少到抵达前\x01",
            "好好享受一下空中旅行吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1001F嗯，我们就不客气了。\x02",
    )

    CloseMessageWindow()

    label("loc_BBB")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_64A end

    def Function_4_BC4(): pass

    label("Function_4_BC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C26")

    ChrTalk(    #22
        0xFE,
        "呼，海风不强真是帮了大忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "看来今天不必过份使用导力引擎\x01",
            "就可以顺利飞行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C81")

    label("loc_C26")

    OP_A2(0x1)

    ChrTalk(    #24
        0xFE,
        (
            "高度保持不变，\x01",
            "推力固定在６０％。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "直到飞至卢比诺川上空之前，\x01",
            "维持现在的航线。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C81")

    TalkEnd(0xFE)
    Return()

    # Function_4_BC4 end

    def Function_5_C85(): pass

    label("Function_5_C85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CF2")

    ChrTalk(    #26
        0xFE,
        (
            "各位乘客～再过一会儿\x01",
            "就可以看见一条巨大的河流了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "那就是王国最大的河流——\x01",
            "卢比诺川。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5D")

    label("loc_CF2")

    OP_A2(0x3)

    ChrTalk(    #28
        0xFE,
        (
            "各位乘客～\x01",
            "右手边看到的是瓦雷利亚湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "遗憾的是雾比较大，\x01",
            "不过湖的大致形状应该还是能够看见的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5D")

    TalkEnd(0xFE)
    Return()

    # Function_5_C85 end

    def Function_6_D61(): pass

    label("Function_6_D61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DE4")

    ChrTalk(    #30
        0xFE,
        (
            "我结束了在大圣堂的工作，\x01",
            "正准备返回柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "我们那边的教区长是个我行我素的人，\x01",
            "真不知道这段时间教会怎样了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB5")

    label("loc_DE4")

    OP_A2(0x4)

    ChrTalk(    #32
        0xFE,
        (
            "我结束了在大圣堂的工作，\x01",
            "正准备返回柏斯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "那里没有我的话实在是很让人担心，\x01",
            "结果在王都整个人都心不在焉的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "虽然是反方向航行的船，\x01",
            "但想都没想就了上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "啊啊，\x01",
            "主日学校顺利结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB5")

    TalkEnd(0xFE)
    Return()

    # Function_6_D61 end

    def Function_7_EB9(): pass

    label("Function_7_EB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_EE9")

    ChrTalk(    #36
        0xFE,
        (
            "这，这次……\x01",
            "可别再出事了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F61")

    label("loc_EE9")

    OP_A2(0x7)

    ChrTalk(    #37
        0xFE,
        (
            "话说回来，这次是我\x01",
            "第二次搭乘定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "上次被卷进了\x01",
            "那个空贼团的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "拜、拜托这次\x01",
            "可别再出事了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F61")

    TalkEnd(0xFE)
    Return()

    # Function_7_EB9 end

    def Function_8_F65(): pass

    label("Function_8_F65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 2)), scpexpr(EXPR_END)), "loc_FD0")

    ChrTalk(    #40
        0xFE,
        (
            "这次的货物几乎都是\x01",
            "在蔡斯装载的导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "虽然不知为什么，\x01",
            "不过最近的物流还挺繁忙的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102B")

    label("loc_FD0")

    OP_A2(0x120A)

    ChrTalk(    #42
        0xFE,
        (
            "这里是储货仓。\x01",
            "不是乘客该来的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "摇摇晃晃地走来走去\x01",
            "会撞到头的，小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102B")

    TalkEnd(0xFE)
    Return()

    # Function_8_F65 end

    def Function_9_102F(): pass

    label("Function_9_102F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_109C")

    ChrTalk(    #44
        0xFE,
        (
            "唔～要把玛诺利亚周边\x01",
            "全部食材都重新检视一遍……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "还是需要做个列表\x01",
            "有计划地调查才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_109C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "◇完成『狩猎蘑菇』或『探索的护卫』\x01",        # 0
            "◇未完成『狩猎蘑菇』或『探索的护卫』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112B")
    OP_28(0x5, 0x4, 0x10)

    label("loc_112B")

    OP_A2(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_122E")

    ChrTalk(    #46
        0xFE,
        (
            "唔唔～……\x01",
            "…………嗯嗯嗯嗯嗯……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#1019F（这，这个人是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "下、下一笔生意\x01",
            "无论如何都必须谈成功……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "现在还是先\x01",
            "把当地的食材重新检视一遍吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "呼，是啊。\x01",
            "回到初学者的心态\x01",
            "开始地道的调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_122E")


    ChrTalk(    #51
        0xFE,
        (
            "唔唔～下次商谈\x01",
            "无论如何都必须成功……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "现在还是先\x01",
            "把当地的食材重新检视一遍吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "呼，是啊。\x01",
            "回到初学者的心态\x01",
            "开始地道的调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BA")

    TalkEnd(0xFE)
    Return()

    # Function_9_102F end

    def Function_10_12BE(): pass

    label("Function_10_12BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1344")

    ChrTalk(    #54
        0xFE,
        (
            "呼～刚回到柏斯\x01",
            "马上又要掉头去蔡斯啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "米拉诺小姐安排的行程\x01",
            "总是那么紧迫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "不过，这样倒也\x01",
            "不会浪费时间……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_1344")

    OP_A2(0x6)

    ChrTalk(    #57
        0xFE,
        (
            "呼～才刚回到柏斯，\x01",
            "马上又要掉头去蔡斯啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "和帝国的互不侵犯条约要是顺利签署，\x01",
            "导力器的出口量也会增加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "得趁现在去蔡斯\x01",
            "多进一些现货。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DA")

    TalkEnd(0xFE)
    Return()

    # Function_10_12BE end

    def Function_11_13DE(): pass

    label("Function_11_13DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1459")

    ChrTalk(    #60
        0xFE,
        (
            "不过，最近这个人\x01",
            "确实很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "也有在努力工作……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "……呼，这样就马上\x01",
            "变得宽容也是我的弱点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1499")

    label("loc_1459")

    OP_A2(0x5)

    ChrTalk(    #63
        0xFE,
        "什么叫『偶尔』啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "不是好不容易\x01",
            "才刚刚找到工作吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1499")

    TalkEnd(0xFE)
    Return()

    # Function_11_13DE end

    def Function_12_149D(): pass

    label("Function_12_149D")

    TalkBegin(0xFE)

    ChrTalk(    #65
        0xFE,
        (
            "听说卢安的娱乐场\x01",
            "又重新装修要开张了呢。\x01",
            "于是我就马上从王都赶来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "人生也需要\x01",
            "偶然放松一下嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_149D end

    def Function_13_150D(): pass

    label("Function_13_150D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 1)), scpexpr(EXPR_END)), "loc_15EA")

    ChrTalk(    #67
        0xFE,
        (
            "提到卢安肯定就要联想到海边垂钓了，\x01",
            "不过其它地方也有不少优质的钓鱼场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "市内流淌的卢比诺川，\x01",
            "还有以瀑布闻名的艾尔·雷登，\x01",
            "在钓鱼爱好者之间都是很有名的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "如果有机会去的话，\x01",
            "务必要带上钓竿哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B27")

    label("loc_15EA")

    OP_A2(0x1209)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 115920, 0, 10120, 0)
    OP_69(0x101, 0x0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #70
        0xFE,
        "哟哟，瓦雷利亚湖啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "在那广阔的湖中某处，\x01",
            "对……有那传说中的鱼王。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1016F#2P（一点都没变呢～～）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "嗯……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)

    ChrTalk(    #74
        0xFE,
        "啊，还以为是谁呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1000F#2P罗伊德先生，好久不见。\x02\x03",

            "又要去挑战瓦雷利亚湖的\x01",
            "鱼王了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "不，这次\x01",
            "预定去卢安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "听说市内也有可以轻松享受的\x01",
            "钓鱼点呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1016F#2P真是热心啊～\x02\x03",

            "虽然确实很有趣，不过我\x01",
            "应该还没有那么入迷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "哎呀……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "唔～那可真是遗憾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "以前在湖畔的旅馆我可是见识过，\x01",
            "你的钓鱼天赋实在是相当出色啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0xFE,
        (
            "……对了。\x01",
            "这个给你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1000F#2P？？？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #84
        "\x07\x00得到了\x1F\x0E\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x07\x00得到了\x1F\x4F\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20E, 1)
    OP_3E(0x24F, 1)

    ChrTalk(    #86
        0x101,
        "#1015F#2P这是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "初级者用的钓竿\x01",
            "和写下钓鱼记录的手册。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "毕竟我们『钓公师团』\x01",
            "是以普及钓鱼文化为目的\x01",
            "而进行活动的团体嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "对有素质的年轻人\x01",
            "应该赠予这样的道具的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "话说回来…\x01",
            "你也要去卢安吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1000F#2P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "嗯，那就尽快\x01",
            "甩甩钓竿试试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "卢安可是\x01",
            "有很多钓场的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1011F#2P啊啊～是吗。\x02\x03",

            "这么说来确实是个\x01",
            "有很多水边的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "刚才我也说了…\x01",
            "市内也有钓鱼点，\x01",
            "先在那边练习练习吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "总之一开始还是轻轻松松\x01",
            "享受就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1001F#2P嗯，谢谢。\x01",
            "我一定试试看的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "希望你有朝一日也能\x01",
            "加入『钓公师团』啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "那么，祝旅途顺利。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 45, 400)
    EventEnd(0x0)

    label("loc_1B27")

    TalkEnd(0xFE)
    Return()

    # Function_13_150D end

    def Function_14_1B2B(): pass

    label("Function_14_1B2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 0)), scpexpr(EXPR_END)), "loc_1B94")

    ChrTalk(    #100
        0xFE,
        (
            "话说回来，游击士\x01",
            "总是忙忙碌碌的，真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "不过，多亏你们的努力\x01",
            "才能维持和平呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E90")

    label("loc_1B94")

    OP_A2(0x1208)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_4A(0xFE, 255)

    ChrTalk(    #102
        0xFE,
        "哎呀…………？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #103
        0xFE,
        (
            "请问，客人是\x01",
            "游击士协会的人，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1000F嗯，是啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "呀，果然没错。\x01",
            "真高兴能再次相见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "还记得吗？\x01",
            "我在空贼团事件的时候\x01",
            "承蒙你们相救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1004F啊，是和船长先生在一起的人吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "嗯嗯，我是客室乘务员\x01",
            "卡拉莉丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "全体乘务员都由衷地\x01",
            "感谢你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "能像现在这样重新营业，\x01",
            "也是多亏游击士们的活跃表现啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1008F啊哈哈，太客气了。\x02\x03",

            "#1000F被当作人质的乘务员们\x01",
            "都平安回到工作岗位了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "嗯嗯，大家都比以往\x01",
            "更加努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1006F是吗，太好了……\x02\x03",

            "大家都回到\x01",
            "平常的生活了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "对了，今天是来旅行？\x01",
            "还是工作呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1016F嘿嘿，很可惜是工作。\x02\x03",

            "今后因为公事要使用定期船\x01",
            "的机会似乎变多了呢。\x02\x03",

            "以后再乘坐的话\x01",
            "就要麻烦你们关照了哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "是，期待你们的光临。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)

    label("loc_1E90")

    TalkEnd(0xFE)
    Return()

    # Function_14_1B2B end

    def Function_15_1E94(): pass

    label("Function_15_1E94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1EF5")

    ChrTalk(    #117
        0xFE,
        (
            "推力确定设定为６０％。\x01",
            "导力驱动器固定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "好，照这状况\x01",
            "可以准时到达卢安吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4C")

    label("loc_1EF5")

    OP_A2(0x2)

    ChrTalk(    #119
        0xFE,
        (
            "高度良好。\x01",
            "推进力变更为６０％。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "直到飞至卢比诺川上空之前，\x01",
            "维持现在方向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4C")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E94 end

    def Function_16_1F50(): pass

    label("Function_16_1F50")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0xFE,
        (
            "我们年轻的时候\x01",
            "可要辛苦地在各个街道上徒步旅行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "这个世界真是\x01",
            "变得越来越方便了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "这也多亏了女王陛下。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_16_1F50 end

    def Function_17_1FD2(): pass

    label("Function_17_1FD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_202C")

    ChrTalk(    #124
        0xFE,
        (
            "代表港口的人物，\x01",
            "还有推进旅游业的实业家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "究竟谁会在选举中获胜呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_209B")

    label("loc_202C")

    OP_A2(0x9)

    ChrTalk(    #126
        0xFE,
        (
            "卢安正在\x01",
            "进行市长选举呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "港口的负责人和酒店的老板\x01",
            "似乎都是候选人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "究竟谁会在选举中获胜呢。\x02",
    )

    CloseMessageWindow()

    label("loc_209B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_17_1FD2 end

    def Function_18_20A4(): pass

    label("Function_18_20A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_20DA")

    ChrTalk(    #129
        0xFE,
        (
            "那个戴尔蒙市长事件\x01",
            "真是令人震惊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2165")

    label("loc_20DA")

    OP_A2(0xA)

    ChrTalk(    #130
        0xFE,
        "呼，接下来是卢安吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "说到卢安市…\x01",
            "戴尔蒙市长被捕一事\x01",
            "可真是冲击性的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "事件之后市民们\x01",
            "似乎也相当动摇，\x01",
            "这也难怪吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2165")

    TalkEnd(0xFE)
    Return()

    # Function_18_20A4 end

    def Function_19_2169(): pass

    label("Function_19_2169")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(    #133
        0xFE,
        (
            "虽说是空贼团，\x01",
            "但要是没有飞船也就不足为惧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "利贝尔通讯上\x01",
            "也写着危险性很低呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2246")

    label("loc_21D0")

    OP_A2(0xB)

    ChrTalk(    #135
        0xFE,
        (
            "真是的，爷爷\x01",
            "担心过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "虽说是空贼团，\x01",
            "但他们已经没有飞船了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "利贝尔通讯上\x01",
            "也写着危险性很低呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2246")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_19_2169 end

    def Function_20_224F(): pass

    label("Function_20_224F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_22A7")

    ChrTalk(    #138
        0xFE,
        (
            "虽然空贼团逃亡到国外\x01",
            "的可能性似乎很高……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "……但还是有点不安啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F6")

    label("loc_22A7")

    OP_A2(0xC)

    ChrTalk(    #140
        0xFE,
        (
            "说起来，空贼团一党\x01",
            "好像还没被逮捕吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "难道…\x01",
            "还会再来袭击我们吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F6")

    TalkEnd(0xFE)
    Return()

    # Function_20_224F end

    def Function_21_22FA(): pass

    label("Function_21_22FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_236B")

    ChrTalk(    #142
        0xFE,
        (
            "毕竟在利贝尔王国以外，\x01",
            "飞船还是特殊的交通工具嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "像这样市民能平常地\x01",
            "搭乘真是令人惊讶啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F5")

    label("loc_236B")

    OP_A2(0xD)

    ChrTalk(    #144
        0xFE,
        (
            "呼……\x01",
            "利贝尔王国果然好厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "在我的故乡共和国，\x01",
            "飞船还是特殊的交通工具呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "像这样子市民能平常地\x01",
            "搭乘真是令人惊讶啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F5")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_21_22FA end

    def Function_22_23FE(): pass

    label("Function_22_23FE")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_242E")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2454")

    label("loc_242E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_244F")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2454")

    label("loc_244F")

    SetChrSubChip(0xFE, 0)

    label("loc_2454")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 5)), scpexpr(EXPR_END)), "loc_24D3")

    ChrTalk(    #147
        0xFE,
        (
            "#020F艾丝蒂尔，散步倒无所谓，\x01",
            "可别忘了我们要在卢安下船哦。\x02\x03",

            "着陆前会有广播提醒的，\x01",
            "一定要回座位哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C7")

    label("loc_24D3")

    OP_A2(0x120D)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #148
        0xFE,
        (
            "#020F哎呀，艾丝蒂尔。\x01",
            "散完步了吗？\x02\x03",

            "离到达\x01",
            "还有一段时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#1015F嗯，说得也是。\x02\x03",

            "#1011F那就再稍微\x01",
            "走走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "#020F散步倒无所谓，\x01",
            "可别忘了在卢安下船哦。\x02\x03",

            "着陆前会有广播提醒的，\x01",
            "一定要回座位哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1006F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_25C7")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_22_23FE end

    def Function_23_25D0(): pass

    label("Function_23_25D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 5)), scpexpr(EXPR_END)), "loc_2646")
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #152
        0xFE,
        "#053F……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)

    ChrTalk(    #153
        0x101,
        (
            "#1015F（睡得这么熟\x01",
            "也够值得尊敬了。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_26D2")

    label("loc_2646")

    OP_A2(0x120D)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #154
        0xFE,
        "#053F……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #155
        0x101,
        "#1019F（已、已经睡熟了……）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_26D2")

    Return()

    # Function_23_25D0 end

    def Function_24_26D3(): pass

    label("Function_24_26D3")

    EventBegin(0x0)
    OP_0D()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #156
        "\x07\x05……久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #157
        (
            "\x07\x05本船即将\x01",
            "抵达卢安市。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #158
        (
            "\x07\x05着陆时会有少许摇晃，\x01",
            "请尽快回到座位上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #159
        0x101,
        (
            "#1004F啊，不好。\x01",
            "要早点回座位才行。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_26D3 end

    SaveToFile()

Try(main)
