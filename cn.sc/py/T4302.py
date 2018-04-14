from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4302   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4302.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '王都市民',                             # 9
        '王都市民',                             # 10
        '王都市民',                             # 11
        '王都市民',                             # 12
        '王都市民',                             # 13
        '旅行者',                               # 14
        '鸽子',                                 # 15
        '鸽子',                                 # 16
        '杜南公爵',                             # 17
        '管家菲利普',                           # 18
        '王国军士官',                           # 19
        '卫兵',                                 # 20
        '卫兵',                                 # 21
        '王国军士兵',                           # 22
        '王国军士兵',                           # 23
        '王国军士兵',                           # 24
        '王国军士兵',                           # 25
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
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01470 ._CH',             # 03
        'ED6_DT07/CH02140 ._CH',             # 04
        'ED6_DT07/CH02470 ._CH',             # 05
        'ED6_DT07/CH01600 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
        'ED6_DT07/CH00322 ._CH',             # 08
        'ED6_DT07/CH00320 ._CH',             # 09
        'ED6_DT07/CH00321 ._CH',             # 0A
        'ED6_DT07/CH01640 ._CH',             # 0B
        'ED6_DT07/CH01003 ._CH',             # 0C
        'ED6_DT07/CH01150 ._CH',             # 0D
        'ED6_DT07/CH01730 ._CH',             # 0E
        'ED6_DT07/CH01731 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01470P._CP',             # 03
        'ED6_DT07/CH02140P._CP',             # 04
        'ED6_DT07/CH02470P._CP',             # 05
        'ED6_DT07/CH01600P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
        'ED6_DT07/CH00322P._CP',             # 08
        'ED6_DT07/CH00320P._CP',             # 09
        'ED6_DT07/CH00321P._CP',             # 0A
        'ED6_DT07/CH01640P._CP',             # 0B
        'ED6_DT07/CH01003P._CP',             # 0C
        'ED6_DT07/CH01150P._CP',             # 0D
        'ED6_DT07/CH01730P._CP',             # 0E
        'ED6_DT07/CH01731P._CP',             # 0F
    )

    DeclNpc(
        X                   = 7870,
        Z                   = 0,
        Y                   = 39410,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 7190,
        Z                   = 0,
        Y                   = 38470,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 11280,
        Z                   = 20,
        Y                   = 38050,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 11270,
        Z                   = 0,
        Y                   = 36380,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 380,
        Y                   = 27330,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -9500,
        Z                   = 250,
        Y                   = 43800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 13510,
        Z                   = 0,
        Y                   = 37730,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12860,
        Z                   = 0,
        Y                   = 36360,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1960,
        Z                   = 0,
        Y                   = 19780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 1960,
        Z                   = 0,
        Y                   = 19780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8860,
        Z                   = 250,
        Y                   = 42720,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -8860,
        Z                   = 250,
        Y                   = 31000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 1920,
        Z                   = 1000,
        Y                   = 57170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -1920,
        Z                   = 1000,
        Y                   = 57170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    DeclActor(
        TriggerX            = -15850,
        TriggerZ            = 0,
        TriggerY            = 49490,
        TriggerRange        = 1000,
        ActorX              = -15740,
        ActorZ              = -2000,
        ActorY              = 51780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_36E",          # 00, 0
        "Function_1_436",          # 01, 1
        "Function_2_450",          # 02, 2
        "Function_3_5CD",          # 03, 3
        "Function_4_5F1",          # 04, 4
        "Function_5_615",          # 05, 5
        "Function_6_639",          # 06, 6
        "Function_7_65D",          # 07, 7
        "Function_8_706",          # 08, 8
        "Function_9_7AF",          # 09, 9
        "Function_10_963",         # 0A, 10
        "Function_11_B4D",         # 0B, 11
        "Function_12_C24",         # 0C, 12
        "Function_13_D11",         # 0D, 13
        "Function_14_105B",        # 0E, 14
        "Function_15_11E4",        # 0F, 15
        "Function_16_1721",        # 10, 16
        "Function_17_1991",        # 11, 17
        "Function_18_1BC5",        # 12, 18
        "Function_19_1F73",        # 13, 19
        "Function_20_20A5",        # 14, 20
        "Function_21_2188",        # 15, 21
        "Function_22_275E",        # 16, 22
        "Function_23_29BC",        # 17, 23
        "Function_24_29E5",        # 18, 24
        "Function_25_3A4A",        # 19, 25
        "Function_26_3A7F",        # 1A, 26
        "Function_27_3AAC",        # 1B, 27
        "Function_28_3AFC",        # 1C, 28
        "Function_29_3B95",        # 1D, 29
        "Function_30_3C16",        # 1E, 30
    )


    def Function_0_36E(): pass

    label("Function_0_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3D6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_3D6")

    label("loc_3B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3F5")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 22)
    Jump("loc_435")

    label("loc_3F5")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_405"),
        (101, "loc_41D"),
        (SWITCH_DEFAULT, "loc_435"),
    )


    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41A")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_41A")

    Jump("loc_435")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_432")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_432")

    Jump("loc_435")

    label("loc_435")

    Return()

    # Function_0_36E end

    def Function_1_436(): pass

    label("Function_1_436")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8900, 0x230061)
    OP_6F(0x1, 60)
    Return()

    # Function_1_436 end

    def Function_2_450(): pass

    label("Function_2_450")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B7")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5B7")

    label("loc_48E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5B7")

    label("loc_4A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5B7")

    label("loc_4C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5B7")

    label("loc_4D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5B7")

    label("loc_4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5B7")

    label("loc_50B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5B7")

    label("loc_524")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5B7")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5B7")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5B7")

    label("loc_56F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5B7")

    label("loc_588")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5B7")

    label("loc_5A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B7")

    label("loc_5CC")

    Return()

    # Function_2_450 end

    def Function_3_5CD(): pass

    label("Function_3_5CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F0")
    OP_8D(0xFE, 10600, 38120, 11980, 37360, 3000)
    Jump("Function_3_5CD")

    label("loc_5F0")

    Return()

    # Function_3_5CD end

    def Function_4_5F1(): pass

    label("Function_4_5F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_614")
    OP_8D(0xFE, 10270, 36610, 11740, 35690, 3000)
    Jump("Function_4_5F1")

    label("loc_614")

    Return()

    # Function_4_5F1 end

    def Function_5_615(): pass

    label("Function_5_615")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_638")
    OP_8D(0xFE, 12960, 38330, 14560, 37580, 3000)
    Jump("Function_5_615")

    label("loc_638")

    Return()

    # Function_5_615 end

    def Function_6_639(): pass

    label("Function_6_639")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65C")
    OP_8D(0xFE, 12580, 37110, 13800, 35710, 3000)
    Jump("Function_6_639")

    label("loc_65C")

    Return()

    # Function_6_639 end

    def Function_7_65D(): pass

    label("Function_7_65D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_705")
    OP_8E(0xFE, 0x2238, 0xFA, 0xA2A8, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8E(0xFE, 0xD48, 0x0, 0xA2A8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80C, 0x0, 0x9EC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80C, 0x0, 0x82A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEC4, 0x0, 0x7F08, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2238, 0xFA, 0x7F08, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_7_65D")

    label("loc_705")

    Return()

    # Function_7_65D end

    def Function_8_706(): pass

    label("Function_8_706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AE")
    OP_8E(0xFE, 0xFFFFDDC8, 0xFA, 0x7F30, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFF344, 0xFA, 0x7F30, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF86C, 0x0, 0x8458, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF86C, 0x0, 0x9CA4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF3E4, 0x0, 0xA2D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDDC8, 0x0, 0xA2D0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_8_706")

    label("loc_7AE")

    Return()

    # Function_8_706 end

    def Function_9_7AF(): pass

    label("Function_9_7AF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_81F")

    ChrTalk(    #0
        0xFE,
        (
            "现在吃的是\x01",
            "妻子做的三明治,很特别啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "这是利贝尔第一……\x01",
            "不，世界第一美味啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F")

    label("loc_81F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_850")

    ChrTalk(    #2
        0xFE,
        "……孩子们天真烂漫多好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_891")

    label("loc_850")


    ChrTalk(    #3
        0xFE,
        (
            "哎，什么？\x01",
            "穿白裙子的女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "嗯～大概\x01",
            "没见过吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_891")

    Jump("loc_95F")

    label("loc_894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_95F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8EF")

    ChrTalk(    #5
        0xFE,
        (
            "这个离宫只要得到许可，\x01",
            "也能在庭园进餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "真是有点\x01",
            "郊游的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F")

    label("loc_8EF")


    ChrTalk(    #7
        0xFE,
        (
            "这个离宫只要得到许可，\x01",
            "也能在庭园进餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "家庭围在一起\x01",
            "不觉得很适合吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "真是有点\x01",
            "郊游的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_95F")

    TalkEnd(0x8)
    Return()

    # Function_9_7AF end

    def Function_10_963(): pass

    label("Function_10_963")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_9BC")

    ChrTalk(    #10
        0xFE,
        (
            "大家都开怀\x01",
            "大吃就最开心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "呵呵，早起\x01",
            "制作也值得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B49")

    label("loc_9BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A1B")

    ChrTalk(    #12
        0xFE,
        (
            "女孩子是见过不少，\x01",
            "详细的样子就不记得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "对不起，\x01",
            "问问其他人好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_A1B")


    ChrTalk(    #14
        0xFE,
        "……哎，穿白裙子的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "女孩子是见过不少，\x01",
            "详细的样子就不记得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "对不起，\x01",
            "问问其他人好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A8C")

    Jump("loc_B49")

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AE8")

    ChrTalk(    #17
        0xFE,
        (
            "这么漂亮的地方，\x01",
            "没理由不利用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "又不收入场费，\x01",
            "家计也省了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B49")

    label("loc_AE8")


    ChrTalk(    #19
        0xFE,
        (
            "我们家经常\x01",
            "来这个艾尔贝离宫的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "难得女王陛下向市民\x01",
            "开放了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "没理由不利用啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B49")

    TalkEnd(0x9)
    Return()

    # Function_10_963 end

    def Function_11_B4D(): pass

    label("Function_11_B4D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_BAA")

    ChrTalk(    #22
        0xFE,
        (
            "喂，妈妈好不容易\x01",
            "做的三明治哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "为什么要给鸽子\x01",
            "那么多嘛！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_BE7")

    ChrTalk(    #24
        0xFE,
        "仔细听就明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "它们咕噜咕噜\x01",
            "地说话呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_C20")

    ChrTalk(    #26
        0xFE,
        (
            "笨蛋，鸽子叫\x01",
            "从来都是咕噜咕噜\x01",
            "的这还用说吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C20")

    TalkEnd(0xA)
    Return()

    # Function_11_B4D end

    def Function_12_C24(): pass

    label("Function_12_C24")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_C89")

    ChrTalk(    #27
        0xFE,
        (
            "看、看着\x01",
            "鸽子的眼睛，忍不住就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "我说，姐姐\x01",
            "不是也在一起喂吗～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0D")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_CD9")

    ChrTalk(    #29
        0xFE,
        (
            "骗人，我听到的是\x01",
            "啵啵的声音啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "喂食看看，\x01",
            "这次好好听着啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D0D")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_D0D")

    ChrTalk(    #31
        0xFE,
        "对了，姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "鸽子\x01",
            "是啵啵叫的对吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0D")

    TalkEnd(0xB)
    Return()

    # Function_12_C24 end

    def Function_13_D11(): pass

    label("Function_13_D11")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1057")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D79")

    ChrTalk(    #33
        0xFE,
        (
            "好了，从外观来看\x01",
            "也完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "天也晚了，\x01",
            "差不多该回家了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE9")

    label("loc_D79")


    ChrTalk(    #35
        0xFE,
        (
            "好了，从外观来看\x01",
            "也完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "天也晚了，\x01",
            "差不多该回家了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "嗬嗬，今天又是\x01",
            "散了老长的步啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_DE9")

    Jump("loc_1057")

    label("loc_DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E7E")

    ChrTalk(    #38
        0xFE,
        (
            "怎么说，别看我这样，\x01",
            "都活了７０岁以上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "穿白衣服的女孩子\x01",
            "多少看见过一个两个，\x01",
            "但在哪看到的就不记得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "哈哈哈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4E")

    label("loc_E7E")


    ChrTalk(    #41
        0xFE,
        (
            "……有没看见\x01",
            "穿白衣服的女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "这个啊，好像有，\x01",
            "又好像没有似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "怎么说，别看我这样，\x01",
            "都活了７０岁以上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "穿白衣服的女孩子\x01",
            "多少看见过一个两个，\x01",
            "但在哪看到的就不记得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "哈哈哈。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F4E")

    Jump("loc_1057")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1057")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FBE")

    ChrTalk(    #46
        0xFE,
        (
            "我的必杀技\x01",
            "过肩摔想学吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "这样，把前襟\x01",
            "一把抓住……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "……好痛，腰、腰，腰啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1057")

    label("loc_FBE")


    ChrTalk(    #49
        0xFE,
        (
            "离宫附近的草木丛中\x01",
            "传来了恐怖的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "如果是魔兽\x01",
            "就拖出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "哐当～的来一个\x01",
            "必杀技过肩摔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "不知道是不是害怕我\x01",
            "最终还是没现身。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1057")

    TalkEnd(0xC)
    Return()

    # Function_13_D11 end

    def Function_14_105B(): pass

    label("Function_14_105B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_10BE")

    ChrTalk(    #53
        0xFE,
        (
            "艾尔贝离宫本\x01",
            "打算看看就好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "但感觉很舒服，\x01",
            "不知不觉就久坐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E0")

    label("loc_10BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_1108")

    ChrTalk(    #55
        0xFE,
        (
            "……在找穿白裙子\x01",
            "的女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "对不起，\x01",
            "我看来帮不上忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E0")

    label("loc_1108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_11E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_115F")

    ChrTalk(    #57
        0xFE,
        (
            "这里的庭园\x01",
            "完全没有垃圾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "使用这里的人们\x01",
            "看来很懂礼仪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E0")

    label("loc_115F")


    ChrTalk(    #59
        0xFE,
        (
            "哦～虽然简单,\x01",
            "但感觉很不错的庭园嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "树丛和草坪也仔细\x01",
            "修剪过，相当漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "本来以为会更华丽的，\x01",
            "这样的也不坏呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_11E0")

    TalkEnd(0xD)
    Return()

    # Function_14_105B end

    def Function_15_11E4(): pass

    label("Function_15_11E4")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1322")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_127F")

    ChrTalk(    #62
        0xFE,
        (
            "这种混乱之中\x01",
            "能来艾尔贝离宫可真稀奇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "如果想进去，\x01",
            "就尽管通过没关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "现在除了我们卫兵以外\x01",
            "只有职员数名。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1322")

    label("loc_127F")


    ChrTalk(    #65
        0xFE,
        (
            "哎呀，你们\x01",
            "看来好像是游击士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "这种混乱之中\x01",
            "能来艾尔贝离宫可真稀奇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "如果想进去，\x01",
            "就尽管通过没关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "现在除了我们卫兵以外\x01",
            "只有职员数名。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1322")

    Jump("loc_171D")

    label("loc_1325")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_13D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_137D")

    ChrTalk(    #69
        0xFE,
        (
            "希德中校说过\x01",
            "让你们游击士通过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "别客气进去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_137D")


    ChrTalk(    #71
        0xFE,
        "欢迎光临艾尔贝离宫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "希德中校说过\x01",
            "让你们游击士通过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "别客气进去吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_13D5")

    Jump("loc_171D")

    label("loc_13D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1436")

    ChrTalk(    #74
        0xFE,
        (
            "警备本部也平安设置好，\x01",
            "感觉签字仪式也终于快到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "警备也比往常\x01",
            "更加严格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171D")

    label("loc_1436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(    #76
        0xFE,
        (
            "今天来离宫\x01",
            "的人似乎挺多的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "因为签字仪式开始后\x01",
            "普通市民就不能进来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "今天来的人\x01",
            "好像挺多的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171D")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_1564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1505")

    ChrTalk(    #79
        0xFE,
        "穿白裙子的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "到底不可能全部记住\x01",
            "入场的每一个人啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1561")

    label("loc_1505")


    ChrTalk(    #81
        0xFE,
        "穿白裙子的女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "今天人特别多……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "到底不可能全部记住\x01",
            "入场的每一个人啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1561")

    Jump("loc_171D")

    label("loc_1564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_171D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 5)), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(    #84
        0xFE,
        (
            "跑进去的\x01",
            "老人碰到魔兽逃跑时\x01",
            "好像腰痛起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "那个人……不要紧吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_171D")

    label("loc_15C1")


    ChrTalk(    #86
        0xFE,
        "我想问一下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "方才，有个\x01",
            "说是听到可怕\x01",
            "魔兽声音的老人跑进去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "这里入口附近\x01",
            "有发生什么奇怪的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1015F啊啊，一定\x01",
            "是说那只大魔兽吧。\x02\x03",

            "#1000F我们已经打倒它了,\x01",
            "应该没问题了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "哦哦，这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "……这么说来，你们\x01",
            "看来好像是游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "作为搜索和惩治的\x01",
            "先锋真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "感谢你们的协助。\x01",
            "在离宫好好放松吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165D)

    label("loc_171D")

    TalkEnd(0x13)
    Return()

    # Function_15_11E4 end

    def Function_16_1721(): pass

    label("Function_16_1721")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1783")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1780")

    ChrTalk(    #94
        0xFE,
        (
            "虽然事态严重，但离宫里\x01",
            "只有卫兵和相关人员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "不介意就通过吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1780")

    Jump("loc_198D")

    label("loc_1783")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_182B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17CF")

    ChrTalk(    #96
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "来过指示，\x01",
            "你们来了就让放行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1828")

    label("loc_17CF")


    ChrTalk(    #98
        0xFE,
        (
            "你们就是这次配合\x01",
            "搜查的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "上门有指示\x01",
            "你们来了就放行的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1828")

    Jump("loc_198D")

    label("loc_182B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(    #101
        0xFE,
        (
            "艾尔贝离宫在签字仪式当日之前\x01",
            "都是王国军的警备本部。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "再次对市民开放\x01",
            "要到签字仪式的结束后了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198D")

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(    #103
        0xFE,
        (
            "为了迎接条约的签字仪式，\x01",
            "听说格兰赛尔地区\x01",
            "马上就要强化警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "这里对市民开放\x01",
            "也到那时为止。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198D")

    label("loc_190A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_1949")

    ChrTalk(    #105
        0xFE,
        "哎？　女孩子吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "……对不起，\x01",
            "我没有印象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198D")

    label("loc_1949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_198D")

    ChrTalk(    #107
        0xFE,
        (
            "这个艾尔贝离宫，现在\x01",
            "是向市民开放的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "请自由进入。\x02",
    )

    CloseMessageWindow()

    label("loc_198D")

    TalkEnd(0x14)
    Return()

    # Function_16_1721 end

    def Function_17_1991(): pass

    label("Function_17_1991")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1A0B")

    ChrTalk(    #109
        0xFE,
        (
            "导力灯不能使用的夜晚\x01",
            "警备可真恐怖啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "何时会从森林中会跑出\x01",
            "魔兽来袭击也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A89")

    label("loc_1A0B")


    ChrTalk(    #111
        0xFE,
        (
            "这里白天警备时\x01",
            "还没什么不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "导力灯不能使用的\x01",
            "夜晚可真够吓人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "何时会从森林中会跑出\x01",
            "魔兽来袭击也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1A89")

    Jump("loc_1BC1")

    label("loc_1A8C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1AEE")

    ChrTalk(    #114
        0xFE,
        (
            "情报部袭击这里\x01",
            "目的似乎是佯攻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "不过，希德中校\x01",
            "到底是看破了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC1")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1B49")

    ChrTalk(    #116
        0xFE,
        (
            "让公爵呆在这里\x01",
            "也只会妨碍警备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "但是让他回\x01",
            "格兰赛尔没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC1")

    label("loc_1B49")


    ChrTalk(    #118
        0xFE,
        (
            "如你所见杜南公爵的\x01",
            "防备心理似乎解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "让他呆在这里\x01",
            "也只会妨碍警备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "但是让他回\x01",
            "格兰赛尔没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1BC1")

    TalkEnd(0x15)
    Return()

    # Function_17_1991 end

    def Function_18_1BC5(): pass

    label("Function_18_1BC5")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1C30")

    ChrTalk(    #121
        0xFE,
        (
            "部分的通信似乎也恢复了，\x01",
            "但是离宫这里还没收到消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "真是不安……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA9")

    label("loc_1C30")


    ChrTalk(    #123
        0xFE,
        (
            "导力器不能使用了，\x01",
            "今后会变成怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "部分的通信似乎也恢复了，\x01",
            "但是离宫这里还没收到消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "真是不安……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1CA9")

    Jump("loc_1F6F")

    label("loc_1CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1DBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1D52")

    ChrTalk(    #126
        0xFE,
        (
            "没想到，会再次和\x01",
            "特务兵的人作战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "虽然想办法以数量取胜了，\x01",
            "那些家伙可真不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "事关白刃战的技术，\x01",
            "还真是相当了得啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB9")

    label("loc_1D52")


    ChrTalk(    #129
        0xFE,
        (
            "虽然想办法以数量取胜了，\x01",
            "特务兵的人真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "事关白刃战的技术，\x01",
            "还真是相当了得啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1DB9")

    Jump("loc_1F6F")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1E5C")

    ChrTalk(    #131
        0xFE,
        (
            "希德中校和理查德上校\x01",
            "比起来是比较保守……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "但在守护要塞方面可比上校\x01",
            "更加厉害，风评都是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "卡西乌斯准将也相当\x01",
            "看中希德中校吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F6F")

    label("loc_1E5C")


    ChrTalk(    #134
        0xFE,
        (
            "希德中校和理查德上校\x01",
            "比起来是比较保守……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "但在守护要塞方面可比上校\x01",
            "更加厉害，风评都是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "百日战役中，不是有利用关口\x01",
            "将帝国军截断的作战吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "那个时候，战斗最激烈区域\x01",
            "圣海姆门能够防守成功\x01",
            "就是多亏了希德中校哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "卡西乌斯准将也相当\x01",
            "看中希德中校吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1F6F")

    TalkEnd(0x16)
    Return()

    # Function_18_1BC5 end

    def Function_19_1F73(): pass

    label("Function_19_1F73")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1FDC")

    ChrTalk(    #139
        0xFE,
        (
            "这下情报部的余党\x01",
            "也终于全部抓到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "政变事件在真正\x01",
            "意义上解决完毕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_1FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_20A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_202C")

    ChrTalk(    #141
        0xFE,
        "呀～轻松啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "即使是亲卫队也没有\x01",
            "迎接公爵那么空闲啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_202C")


    ChrTalk(    #143
        0xFE,
        "哟，我听说啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "杜南公爵的任性妄为\x01",
            "让我们也经常很头痛的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "要说教、告诫\x01",
            "那公爵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "呀～轻松啦！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_20A1")

    TalkEnd(0x17)
    Return()

    # Function_19_1F73 end

    def Function_20_20A5(): pass

    label("Function_20_20A5")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2108")

    ChrTalk(    #147
        0xFE,
        (
            "最近真是\x01",
            "好天气连续不断啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "签字仪式当天\x01",
            "也有这样的天气就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2184")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2184")

    ChrTalk(    #149
        0xFE,
        (
            "每次都是这样\x01",
            "菲利普先生可真辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "如果没有相当的忍耐力，\x01",
            "可当不了公爵的管家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "那个人真的\x01",
            "是个好人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2184")

    TalkEnd(0x18)
    Return()

    # Function_20_20A5 end

    def Function_21_2188(): pass

    label("Function_21_2188")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_219F")
    Call(0, 28)
    Call(0, 29)

    label("loc_219F")

    OP_6D(680, 1000, 52720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(600, 0)
    OP_C8(0x200, 0x46, "C_PLAC11._CH", 0x1, 0x5DC)
    FadeToBright(1500, 0)
    SetChrPos(0x101, -240, 0, 26720, 10)
    SetChrPos(0xF7, 780, 0, 26810, 10)
    SetChrPos(0xF8, -1170, 0, 26020, 10)
    SetChrPos(0xF9, 1520, 0, 25840, 10)

    def lambda_2244():
        OP_6D(190, 0, 26660, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2244)

    def lambda_225C():
        OP_6E(262, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_225C)

    def lambda_226C():
        OP_6C(348000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_226C)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22AF")

    ChrTalk(    #152
        0x107,
        "#061F哇，好漂亮的地方……！\x02",
    )

    CloseMessageWindow()

    label("loc_22AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232E")

    ChrTalk(    #153
        0x108,
        (
            "#070F艾尔贝离宫……\x01",
            "真奇怪，感觉好怀念啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1006F#5P嗯……\x02\x03",

            "#1015F不过，好像还有普通人\x01",
            "也在里面……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2383")

    label("loc_232E")


    ChrTalk(    #155
        0x101,
        (
            "#1006F#5P艾尔贝离宫……\x01",
            "感觉好怀念啊。\x02\x03",

            "#1015F不过，好像还有普通人\x01",
            "也在里面……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(    #156
        0x105,
        (
            "#040F平时是向\x01",
            "市民开放的。\x02\x03",

            "可以算个稍事\x01",
            "休息的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2482")

    label("loc_23D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242B")

    ChrTalk(    #157
        0x106,
        (
            "#051F平时似乎也是向\x01",
            "一般市民们开放的。\x02\x03",

            "可以算个稍事\x01",
            "休息的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2482")

    label("loc_242B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2482")

    ChrTalk(    #158
        0x103,
        (
            "#020F平时似乎也是向\x01",
            "一般市民开放的呢。\x02\x03",

            "可以算个稍事\x01",
            "休息的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2482")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2543")

    ChrTalk(    #159
        0x104,
        (
            "#035F呼，待在精致的空间\x01",
            "不由得涌出了创作欲望。\x02\x03",

            "#030F这就用我的鲁特琴\x01",
            "让各位更加愉悦吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        (
            "#1007F#5P算了吧你……\x02\x03",

            "#1011F不过，这么一说的确\x01",
            "看起来有很多人全家都来玩呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_2543")


    ChrTalk(    #161
        0x101,
        (
            "#1011F#5P哦～这样啊。\x02\x03",

            "这么一说的确\x01",
            "看起来有很多人全家都来玩呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2624")

    ChrTalk(    #162
        0x108,
        (
            "#070F迷路的孩子啊,\x01",
            "是那种举家同游的客人家\x01",
            "孩子的可能性也很大呢。\x02\x03",

            "总而言之，赶快去找那个\x01",
            "叫雷蒙德的管家大哥啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1006F#5PＯＫ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2758")

    label("loc_2624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C3")

    ChrTalk(    #164
        0x106,
        (
            "#053F迷路的小鬼\x01",
            "是那种举家同游的客人家\x01",
            "孩子的可能性也很大呢。\x02\x03",

            "#050F总而言之，赶快去找那个\x01",
            "叫雷蒙德的管家吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1006F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2758")

    label("loc_26C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2758")

    ChrTalk(    #166
        0x103,
        (
            "#020F迷路的孩子\x01",
            "是那种举家同游的客人家\x01",
            "孩子的可能性也很大呢。\x02\x03",

            "总而言之，赶快去找那个\x01",
            "叫雷蒙德的管家吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#1006F#5P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2758")

    OP_A2(0x160C)
    EventEnd(0x0)
    Return()

    # Function_21_2188 end

    def Function_22_275E(): pass

    label("Function_22_275E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #168
        (
            "\x07\x05第二天早晨，艾丝蒂尔等人\x01",
            "向艾尔贝离宫的希德中校\x01",
            "送交了有关恐吓信的调查报告书。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    SetChrPos(0x13, -7380, 0, 36870, 270)
    SetChrPos(0x14, -11200, 0, 36810, 90)
    SetChrPos(0x15, 9950, 0, 36540, 314)
    SetChrPos(0x16, 6560, 0, 39190, 134)
    SetChrPos(0x17, 7820, 0, 31210, 90)
    SetChrPos(0x18, -8590, 0, 31290, 270)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 8)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x15, 8)
    SetChrSubChip(0x15, 0)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x17, 8)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x18, 8)
    SetChrSubChip(0x18, 0)
    OP_43(0x13, 0x0, 0x0, 0x17)
    Sleep(50)
    OP_43(0x15, 0x0, 0x0, 0x17)
    Sleep(50)
    OP_43(0x14, 0x0, 0x0, 0x17)
    Sleep(50)
    OP_43(0x17, 0x0, 0x0, 0x17)
    Sleep(50)
    OP_43(0x16, 0x0, 0x0, 0x17)
    Sleep(50)
    OP_43(0x18, 0x0, 0x0, 0x17)
    OP_6D(-660, 0, 23220, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(344000, 0)
    OP_6E(409, 0)
    OP_1D(0x11)
    OP_22(0x1C2, 0x0, 0x64)

    def lambda_2951():
        OP_6D(680, 1000, 52720, 7000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2951)

    def lambda_2969():
        OP_67(0, 8000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2969)

    def lambda_2981():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2981)

    def lambda_2991():
        OP_6E(600, 8000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2991)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x13, 0x2)
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_275E end

    def Function_23_29BC(): pass

    label("Function_23_29BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E4")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(1500)
    Jump("Function_23_29BC")

    label("loc_29E4")

    Return()

    # Function_23_29BC end

    def Function_24_29E5(): pass

    label("Function_24_29E5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29F8")
    Call(0, 28)

    label("loc_29F8")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x101, 80, 1000, 59650, 180)
    SetChrPos(0xF7, 80, 1000, 59650, 180)
    SetChrPos(0x107, 80, 1000, 59650, 180)
    SetChrPos(0x12F, 80, 1000, 59650, 180)
    SetChrPos(0x10, -220, 0, 44940, 180)
    SetChrPos(0x11, 560, 0, 45120, 180)
    SetChrPos(0x12, 50, 0, 42800, 0)
    SetChrPos(0x13, -750, 0, 42500, 0)
    SetChrPos(0x14, 750, 0, 42500, 0)
    SetChrChipByIndex(0x13, 11)
    SetChrChipByIndex(0x14, 11)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(580, 1000, 56480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1D)
    OP_73(0x0)

    def lambda_2B3A():
        OP_8E(0xFE, 0x1F4, 0x3E8, 0xD78C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B3A)
    Sleep(600)

    def lambda_2B5A():
        OP_8E(0xFE, 0xFFFFFE0C, 0x3E8, 0xD78C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2B5A)
    Sleep(600)

    def lambda_2B7A():
        OP_8E(0xFE, 0xFFFFFE0C, 0x3E8, 0xDC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2B7A)
    Sleep(600)

    def lambda_2B9A():
        OP_8E(0xFE, 0x1F4, 0x3E8, 0xDC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 0, lambda_2B9A)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #169
        0x101,
        "#1004F#5P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_2BD6():
        OP_6D(470, 0, 44880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BD6)

    def lambda_2BEE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BEE)

    def lambda_2BFE():
        OP_67(0, 8189, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2BFE)
    OP_6B(2450, 3000)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #170
        0x10,
        (
            "#224F#5P怎么回事，这是！？\x02\x03",

            "把拥有第一王位继承权的\x01",
            "杜南·冯·奥赛雷丝\x01",
            "当做无知的白痴来耍弄吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x12,
        "完、完全没有的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x12,
        (
            "其实今天早上，进行了艾尔贝周游道\x01",
            "的魔兽扫荡作战……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x12,
        (
            "因此护卫的数量\x01",
            "这样也足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10,
        (
            "#224F#5P不是这个意思！\x02\x03",

            "对我这样的重要人物\x01",
            "护卫只有３个人实在太无礼了！\x02\x03",

            "至少要准备１０名！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x12,
        "可，可是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x13, 400)
    Sleep(500)

    ChrTalk(    #176
        0x11,
        (
            "#722F#2P阁下……\x01",
            "别说得太过分了吧。\x02\x03",

            "难得陛下\x01",
            "下了许可。\x02\x03",

            "仅此\x01",
            "就应该觉得万幸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x10,
        (
            "#222F#5P住口，菲利普！\x02\x03",

            "说到底处分这事\x01",
            "就不当至极。\x02\x03",

            "那么亲卫队全员\x01",
            "出迎也是应该的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#4P嗯，亲卫队全员\x01",
            "到底是来不了……\x02\x03",

            "可以的话我们\x01",
            "陪你一起可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2E98():
        OP_6D(-70, 0, 46500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E98)

    def lambda_2EB0():
        OP_67(0, 8050, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2EB0)

    def lambda_2EC8():
        OP_6E(300, 4000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_2EC8)

    def lambda_2ED8():
        OP_8E(0xFE, 0xB4, 0x0, 0xB586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ED8)
    Sleep(100)

    def lambda_2EF8():
        TurnDirection(0x10, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2EF8)

    def lambda_2F06():
        TurnDirection(0x11, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F06)

    def lambda_2F14():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xB66C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2F14)
    Sleep(50)

    def lambda_2F34():
        OP_8E(0xFE, 0xC8, 0xFA, 0xBA54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_2F34)
    Sleep(100)

    def lambda_2F54():
        OP_8E(0xFE, 0xFFFFFC7C, 0xFA, 0xBA54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2F54)
    WaitChrThread(0x101, 0x2)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #179
        0x10,
        "#226F#6P你、你们是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x11,
        "#721F#4P哦哦，各位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1007F真是的……\x01",
            "公爵先生也是一点都没变呢。\x02\x03",

            "#1019F说话太任性\x01",
            "让大家为难可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x10,
        (
            "#226F#6P别、别随便\x01",
            "乱叫什么公爵先生！\x02\x03",

            "为什么你们\x01",
            "会在这种地方！？\x02\x03",

            "不是已经禁止\x01",
            "民间人士进入了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1006F只是有东西要交给\x01",
            "这里的警备责任人啦。\x02\x03",

            "那，公爵先生你们\x01",
            "现在要去散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10,
        (
            "#220F#6P哼、哼。\x01",
            "听了可别吓坏了……\x02\x03",

            "#221F把束缚我的无理规定\x01",
            "终于解除了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1004F无理规定解除了……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_317B")

    ChrTalk(    #186
        0x106,
        (
            "#052F#5P难不成\x01",
            "是禁足处分解除了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A4")

    label("loc_317B")


    ChrTalk(    #187
        0x103,
        (
            "#023F#5P难不成\x01",
            "是禁足处分解除了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A4")


    ChrTalk(    #188
        0x11,
        (
            "#720F#4P是的，今天早晨\x01",
            "收到了陛下的联络。\x02\x03",

            "说要离开离宫，\x01",
            "返回格兰赛尔城。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_322B")

    ChrTalk(    #189
        0x106,
        (
            "#051F#5P哎呀哎呀……\x01",
            "真是老好人的婆婆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3250")

    label("loc_322B")


    ChrTalk(    #190
        0x103,
        (
            "#027F#5P哎呀呀……\x01",
            "相当简单呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3250")


    ChrTalk(    #191
        0x101,
        (
            "#1011F哦～不过\x01",
            "也好吧。\x02\x03",

            "#1001F不要再次被利用\x01",
            "要好好把持住自己哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x10,
        "#223F#6P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        (
            "#1006F嗯～还是要把生活态度\x01",
            "重新端正一下比较好吧？\x02\x03",

            "公爵先生啊\x01",
            "实在是自由散漫惯了呢。\x02\x03",

            "推荐你做点运动哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12F, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xF7)
    OP_63(0x10)
    OP_63(0x11)
    OP_63(0x107)
    OP_63(0x12F)
    OP_63(0x12)
    OP_63(0x13)
    OP_63(0x14)

    ChrTalk(    #194
        0x101,
        (
            "#1015F咦？\x01",
            "我说了什么奇怪的话？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x11,
        (
            "#720F#4P不……正如艾丝蒂尔大人\x01",
            "说的一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(500)

    ChrTalk(    #196
        0x11,
        (
            "#722F#2P如果阁下自己\x01",
            "把持得住，也不会被\x01",
            "理查德上校所利用……\x02\x03",

            "我菲利普，希望\x01",
            "就此再度进言……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10,
        "#226F#6P哎，说教够了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 600)

    ChrTalk(    #198
        0x10,
        (
            "#224F#5P够了，这个地方\x01",
            "我一秒钟也不想再待了！\x02\x03",

            "赶紧去王都！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x12,
        "#2P哦哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#1004F啊？\x01",
            "不用陪同吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 600)

    ChrTalk(    #201
        0x10,
        (
            "#224F#6P不要！\x02\x03",

            "走了！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x1, 0x0, 0x1B)
    Sleep(50)
    OP_43(0x13, 0x1, 0x0, 0x19)
    OP_43(0x14, 0x1, 0x0, 0x1A)

    def lambda_3563():

        label("loc_3563")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_3563")

    QueueWorkItem2(0x11, 2, lambda_3563)
    OP_8C(0x10, 180, 600)
    OP_8E(0x10, 0xFFFFFF24, 0x0, 0x88B8, 0xBB8, 0x0)
    OP_44(0x11, 0x2)
    OP_8C(0x11, 270, 400)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #202
        0x11,
        (
            "#720F艾丝蒂尔小姐，每次\x01",
            "都麻烦您真是感激不尽。\x02\x03",

            "该如何感谢才好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#1016F啊哈哈，不用啦。\x02\x03",

            "#1006F不过，菲利普先生\x01",
            "偶尔也得好好训训他。\x02\x03",

            "就是因为没人训他\x01",
            "才变成那样不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x11,
        "#721F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#1006F我想他本性也不坏,\x01",
            "只要有心还是能改过的啦。\x02\x03",

            "需要的就是一个契机吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x11,
        (
            "#722F艾丝蒂尔小姐……\x02\x03",

            "您的话，我菲利普，\x01",
            "将铭刻在心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x10,
        (
            "#5P菲利普！\x01",
            "在干什么！\x02\x03",

            "再磨磨蹭蹭\x01",
            "我就丢下你不管了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)
    OP_8C(0x11, 180, 600)

    ChrTalk(    #208
        0x11,
        "#721F#5P是、是，这就来。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)
    OP_8C(0x11, 0, 600)

    ChrTalk(    #209
        0x11,
        (
            "#720F那么各位……\x01",
            "我就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)
    OP_8C(0x11, 180, 600)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    def lambda_37AF():
        OP_6D(-370, 0, 43300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37AF)
    OP_8E(0x11, 0xFFFFFF24, 0x0, 0x88B8, 0xBB8, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(500)
    OP_6D(-600, 250, 47270, 1600)

    ChrTalk(    #210
        0x101,
        (
            "#1015F嗯～虽然觉得还是\x01",
            "陪着一起会比较好啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3875")

    ChrTalk(    #211
        0x106,
        (
            "#051F……怎么说呢。\x02\x03",

            "说实话，你这种地方\x01",
            "还真是学不来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38AD")

    label("loc_3875")


    ChrTalk(    #212
        0x103,
        (
            "#021F……艾丝蒂尔你啊。\x02\x03",

            "不愧是流着\x01",
            "老师的血液呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AD")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #213
        0x101,
        "#1004F#2P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x107,
        (
            "#067F嘿嘿嘿……\x01",
            "还是姐姐厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x12F,
        (
            "#268F虽然初次见面\x01",
            "就有这种感觉……\x02\x03",

            "艾丝蒂尔啊，真是个\x01",
            "大好人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #216
        0x101,
        "#1015F#6P好人……为什么？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_39BA")

    ChrTalk(    #217
        0x106,
        (
            "#051F啊～不懂的话\x01",
            "就保持这样好了。\x02\x03",

            "总之回王都去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F6")

    label("loc_39BA")


    ChrTalk(    #218
        0x103,
        (
            "#027F呵呵，不懂的话\x01",
            "就保持这样好了。\x02\x03",

            "总之回王都去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F6")

    OP_A2(0x162C)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)
    SetChrPos(0x13, -1960, 0, 19780, 180)
    SetChrPos(0x14, 1960, 0, 19780, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    EventEnd(0x0)
    Return()

    # Function_24_29E5 end

    def Function_25_3A4A(): pass

    label("Function_25_3A4A")

    OP_8F(0xFE, 0xFFFFF916, 0x0, 0xA690, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 500)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0x9088, 0x9C4, 0x0)
    Return()

    # Function_25_3A4A end

    def Function_26_3A7F(): pass

    label("Function_26_3A7F")

    Sleep(1000)
    OP_8C(0xFE, 270, 500)
    Sleep(1500)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0x30C, 0x0, 0x9088, 0x9C4, 0x0)
    Return()

    # Function_26_3A7F end

    def Function_27_3AAC(): pass

    label("Function_27_3AAC")

    OP_8F(0xFE, 0x14, 0x0, 0xA2A8, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 500)
    OP_8F(0xFE, 0x2B2, 0x0, 0xA2A8, 0x9C4, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFFF24, 0x0, 0x8CA0, 0x9C4, 0x0)
    Return()

    # Function_27_3AAC end

    def Function_28_3AFC(): pass

    label("Function_28_3AFC")

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
        (0, "loc_3B76"),
        (1, "loc_3B7C"),
        (SWITCH_DEFAULT, "loc_3B82"),
    )


    label("loc_3B76")

    OP_A2(0x1200)
    Jump("loc_3B82")

    label("loc_3B7C")

    OP_A2(0x1201)
    Jump("loc_3B82")

    label("loc_3B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3B90")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3B94")

    label("loc_3B90")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3B94")

    Return()

    # Function_28_3AFC end

    def Function_29_3B95(): pass

    label("Function_29_3B95")

    ClearMapFlags(0x1)
    OP_6D(-11230, 0, -25420, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3BD8")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_3BF6")

    label("loc_3BD8")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_3BF6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_29_3B95 end

    def Function_30_3C16(): pass

    label("Function_30_3C16")

    EventBegin(0x1)

    ChrTalk(    #219
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #220
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF2")

    def lambda_3C8D():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3C8D)

    def lambda_3C9D():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3C9D)
    WaitChrThread(0x1, 0x1)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0x2F, 0xFFFFC216, 0x0, 0xC152, 0x0, 0xFFFFC284, 0xFFFFFAEC, 0xCA44)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3D01")

    label("loc_3CF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D01")
    EventEnd(0x1)

    label("loc_3D01")

    Return()

    # Function_30_3C16 end

    SaveToFile()

Try(main)
