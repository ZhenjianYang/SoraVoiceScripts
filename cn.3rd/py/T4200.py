from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '士兵丹',                               # 9
        '士兵阿尔兹',                           # 10
        '黑衣人首领',                           # 11
        '黑衣人',                               # 12
        '黑衣人',                               # 13
        '绅士模样的男人',                       # 14
        '中队长',                               # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
        '士兵',                                 # 19
        '目标用照相机',                         # 20
        '游客',                                 # 21
        '游客',                                 # 22
        '游客',                                 # 23
        '游客',                                 # 24
        '游客',                                 # 25
        '女性',                                 # 26
        '女性',                                 # 27
        '女性',                                 # 28
        '女性',                                 # 29
        '女性',                                 # 30
        '女性',                                 # 31
        '女性',                                 # 32
        '女性',                                 # 33
        '女性',                                 # 34
        '女性',                                 # 35
        '女性',                                 # 36
        '女性',                                 # 37
        '女性',                                 # 38
        '女性',                                 # 39
        '卡兰大主教',                           # 40
        '临时',                                 # 41
        '',                                     # 42
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01600 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT27/CH03460 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT27/CH04230 ._CH',             # 09
        'ED6_DT26/CH20618 ._CH',             # 0A
        'ED6_DT26/CH20419 ._CH',             # 0B
        'ED6_DT07/CH01410 ._CH',             # 0C
        'ED6_DT07/CH01400 ._CH',             # 0D
        'ED6_DT07/CH01030 ._CH',             # 0E
        'ED6_DT07/CH01130 ._CH',             # 0F
        'ED6_DT07/CH01230 ._CH',             # 10
        'ED6_DT07/CH01170 ._CH',             # 11
        'ED6_DT07/CH01070 ._CH',             # 12
        'ED6_DT07/CH01350 ._CH',             # 13
        'ED6_DT07/CH00323 ._CH',             # 14
        'ED6_DT27/CH03420 ._CH',             # 15
        'ED6_DT27/CH04462 ._CH',             # 16
        'ED6_DT27/CH04460 ._CH',             # 17
        'ED6_DT27/CH04461 ._CH',             # 18
        'ED6_DT26/CH20613 ._CH',             # 19
        'ED6_DT26/CH20683 ._CH',             # 1A
        'ED6_DT26/CH20690 ._CH',             # 1B
        'ED6_DT27/CH03231 ._CH',             # 1C
        'ED6_DT26/CH20684 ._CH',             # 1D
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01600P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT27/CH03460P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT27/CH04230P._CP',             # 09
        'ED6_DT26/CH20618P._CP',             # 0A
        'ED6_DT26/CH20419P._CP',             # 0B
        'ED6_DT07/CH01410P._CP',             # 0C
        'ED6_DT07/CH01400P._CP',             # 0D
        'ED6_DT07/CH01030P._CP',             # 0E
        'ED6_DT07/CH01130P._CP',             # 0F
        'ED6_DT07/CH01230P._CP',             # 10
        'ED6_DT07/CH01170P._CP',             # 11
        'ED6_DT07/CH01070P._CP',             # 12
        'ED6_DT07/CH01350P._CP',             # 13
        'ED6_DT07/CH00323P._CP',             # 14
        'ED6_DT27/CH03420P._CP',             # 15
        'ED6_DT27/CH04462P._CP',             # 16
        'ED6_DT27/CH04460P._CP',             # 17
        'ED6_DT27/CH04461P._CP',             # 18
        'ED6_DT26/CH20613P._CP',             # 19
        'ED6_DT26/CH20683P._CP',             # 1A
        'ED6_DT26/CH20690P._CP',             # 1B
        'ED6_DT27/CH03231P._CP',             # 1C
        'ED6_DT26/CH20684P._CP',             # 1D
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
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
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
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

    DeclNpc(
        X                   = 6640,
        Z                   = 0,
        Y                   = 24120,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = 2060,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8130,
        Z                   = 0,
        Y                   = 11800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 6210,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 12840,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC8,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_5BA",          # 00, 0
        "Function_1_649",          # 01, 1
        "Function_2_66A",          # 02, 2
        "Function_3_7E7",          # 03, 3
        "Function_4_80B",          # 04, 4
        "Function_5_82F",          # 05, 5
        "Function_6_949",          # 06, 6
        "Function_7_A70",          # 07, 7
        "Function_8_17F2",         # 08, 8
        "Function_9_1B41",         # 09, 9
        "Function_10_1E51",        # 0A, 10
        "Function_11_1E79",        # 0B, 11
        "Function_12_1EA1",        # 0C, 12
        "Function_13_1EC9",        # 0D, 13
        "Function_14_1F36",        # 0E, 14
        "Function_15_1FDC",        # 0F, 15
        "Function_16_2972",        # 10, 16
        "Function_17_2A76",        # 11, 17
        "Function_18_3370",        # 12, 18
        "Function_19_33A8",        # 13, 19
        "Function_20_33E0",        # 14, 20
        "Function_21_4745",        # 15, 21
        "Function_22_47ED",        # 16, 22
        "Function_23_4875",        # 17, 23
        "Function_24_48FD",        # 18, 24
        "Function_25_4965",        # 19, 25
        "Function_26_4A06",        # 1A, 26
    )


    def Function_0_5BA(): pass

    label("Function_0_5BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_5DC")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_5EF")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_5EF")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_5EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 17)

    label("loc_60D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_635")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_648")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_648")

    Return()

    # Function_0_5BA end

    def Function_1_649(): pass

    label("Function_1_649")

    OP_B1("T4200_n")
    OP_72(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_649 end

    def Function_2_66A(): pass

    label("Function_2_66A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7D1")

    label("loc_68F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7D1")

    label("loc_6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7D1")

    label("loc_6C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7D1")

    label("loc_6DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7D1")

    label("loc_6F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7D1")

    label("loc_70C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_725")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7D1")

    label("loc_725")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7D1")

    label("loc_73E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7D1")

    label("loc_757")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7D1")

    label("loc_770")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_789")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7D1")

    label("loc_789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A2")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7D1")

    label("loc_7A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7D1")

    label("loc_7BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7D1")

    label("loc_7E6")

    Return()

    # Function_2_66A end

    def Function_3_7E7(): pass

    label("Function_3_7E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_80A")
    OP_8D(0xFE, 2620, 2600, -590, 3530, 2000)
    Jump("Function_3_7E7")

    label("loc_80A")

    Return()

    # Function_3_7E7 end

    def Function_4_80B(): pass

    label("Function_4_80B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82E")
    OP_8D(0xFE, -1730, 10700, -4110, 14100, 2000)
    Jump("Function_4_80B")

    label("loc_82E")

    Return()

    # Function_4_80B end

    def Function_5_82F(): pass

    label("Function_5_82F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    OP_6D(-1020, 3250, -890, 0)
    OP_67(0, 9510, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(45000, 0)
    OP_6E(455, 0)

    def lambda_8A6():
        OP_6D(-1020, 3250, 37010, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8A6)

    def lambda_8BE():
        OP_67(0, 4330, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8BE)

    def lambda_8D6():
        OP_6B(3320, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8D6)

    def lambda_8E6():
        OP_6C(33000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8E6)

    def lambda_8F6():
        OP_6E(455, 8000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_8F6)
    OP_43(0x1E, 0x0, 0x0, 0x6)
    OP_43(0x1F, 0x0, 0x0, 0x6)
    OP_62(0x1C, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_82F end

    def Function_6_949(): pass

    label("Function_6_949")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6F")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_985")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_985")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC")
    Sleep(1300)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_9AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D3")
    Sleep(1600)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_9D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    Sleep(1900)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_9FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21")
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_A21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A48")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_A6C")

    label("loc_A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6C")
    Sleep(2800)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_A6C")

    Jump("Function_6_949")

    label("loc_A6F")

    Return()

    # Function_6_949 end

    def Function_7_A70(): pass

    label("Function_7_A70")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1300, 250, 42740, 0)
    OP_67(0, 6060, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 450)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -1300, 0, 28300, 180)
    SetChrPos(0x11, 1300, 0, 28700, 180)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    LoadEffect(0x0, "map\\\\mp012_00.eff")
    SoundLoad(228)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x21, 390, 0, 27650, 45)
    SetChrPos(0x22, -1260, 0, 27080, 0)
    SetChrPos(0x23, -500, 0, 26260, 0)
    SetChrPos(0x24, 940, 0, 26760, 0)
    SetChrPos(0x25, 1880, 0, 26230, 0)
    SetChrPos(0x26, -2040, 0, 25530, 0)
    SetChrPos(0x27, 240, 0, 25280, 0)
    SetChrPos(0x28, -2880, 0, 26700, 45)
    SetChrPos(0x29, 1370, 0, 24890, 0)
    SetChrPos(0x2A, 2320, 0, 27300, 315)
    SetChrPos(0x2B, -3270, 0, 25200, 45)
    SetChrPos(0x2C, -1760, 0, 24490, 0)
    SetChrPos(0x2D, 180, 0, 24020, 0)
    SetChrPos(0x2E, 2860, 0, 25120, 315)
    SetChrPos(0x10E, 0, 750, 51200, 180)
    FadeToBright(2000, 0)

    def lambda_C6F():
        OP_8E(0xFE, 0x0, 0x2EE, 0xACA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_C6F)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #0
        0x10E,
        "尤莉亚上尉",
        (
            "#170F#5P好了，\x01",
            "虽然接受了休假安排……\x02\x03",

            "#176F…………不过，\x01",
            "真是好久没休过假了。\x01",
            "该干什么好呢……\x02\x03",

            "去逛街……买装备……\x01",
            "……还是回房间\x01",
            "看看书呢…………\x02\x03",

            "#175F不，\x01",
            "休假应该过得更有意义一点……\x02",
        )
    )

    Jump("loc_D7E")

    label("loc_D7E")

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #1
        0x10E,
        "尤莉亚上尉",
        (
            "#179F#5P……对了，\x01",
            "好久没有悠闲地逛逛周游道了。\x02\x03",

            "#170F干脆就走远一点，\x01",
            "沿着街道散散步\x01",
            "似乎也不错……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E27():
        OP_8E(0xFE, 0x0, 0x0, 0x940C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_E27)
    WaitChrThread(0x10E, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x1388)

    def lambda_E68():
        OP_6D(1160, 0, 27600, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_E68)

    def lambda_E80():
        OP_67(0, 5340, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_E80)

    def lambda_E98():
        OP_6B(3280, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_E98)

    def lambda_EA8():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_EA8)
    WaitChrThread(0x1B, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x21,
        (
            "#4P听说尤莉亚大人回格兰赛尔了，\x01",
            "这是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x22,
        (
            "#4P尤莉亚大人……\x01",
            "尤莉亚大人在哪里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#1P好、好了好了……\x01",
            "请别推啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        (
            "#1P各位，\x01",
            "请镇定、镇定……\x02",
        )
    )

    Jump("loc_F80")

    label("loc_F80")

    CloseMessageWindow()
    SetChrPos(0x10E, 120, 0, 37400, 180)

    def lambda_F98():
        OP_8E(0xFE, 0x78, 0x0, 0x78DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_F98)
    WaitChrThread(0x10E, 0x1)

    NpcTalk(    #6
        0x10E,
        "尤莉亚上尉",
        "#173F这、这骚动是…………！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)

    def lambda_1025():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1025)

    def lambda_1033():
        TurnDirection(0xFE, 0x10E, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1033)
    WaitChrThread(0x10, 0x2)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #7
        0x10,
        (
            "上、上尉…………！？\x02\x03",

            "怎么偏偏在这时候出来……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        "#2P危险，请退下！！\x02",
    )

    CloseMessageWindow()
    OP_4A(0x21, 255)
    OP_8C(0x21, 0, 500)
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    NpcTalk(    #9
        0x21,
        "尖叫声",
        "#4P啊，是尤莉亚大人！\x02",
    )

    Jump("loc_111F")

    label("loc_111F")

    CloseMessageWindow()
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    OP_4A(0x2C, 255)
    OP_4A(0x2D, 255)
    OP_4A(0x2E, 255)

    NpcTalk(    #10
        0x22,
        "尖叫声",
        "#4P咦……！？\x02",
    )

    Jump("loc_117C")

    label("loc_117C")

    CloseMessageWindow()
    OP_1D(0x52)
    Sleep(500)
    OP_43(0x21, 0x0, 0x0, 0x8)
    OP_43(0x21, 0x3, 0x0, 0xA)
    Sleep(500)

    NpcTalk(    #11
        0x23,
        "尖叫声",
        "#4P呀——，是真人啊——！！\x02",
    )

    Jump("loc_11CD")

    label("loc_11CD")

    CloseMessageWindow()
    OP_8C(0x10E, 225, 600)
    Sleep(600)
    OP_8C(0x10E, 135, 600)
    Sleep(600)
    OP_8C(0x10E, 180, 600)
    Sleep(300)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #12
        0x10E,
        "尤莉亚上尉",
        "#172F怎、怎么回事…………！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x23,
        "尖叫声",
        "#3S#4P尤莉亚大人――――！！#2S\x02",
    )

    Jump("loc_1273")

    label("loc_1273")

    CloseMessageWindow()
    OP_44(0x21, 0x0)
    Sleep(100)

    def lambda_1283():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1283)

    def lambda_1291():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1291)

    def lambda_129F():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_129F)

    def lambda_12B9():
        OP_8F(0xFE, 0xFFFFFAEC, 0x0, 0x7148, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12B9)

    def lambda_12D4():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_12D4)

    def lambda_12EE():
        OP_8F(0xFE, 0x514, 0x0, 0x72D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12EE)

    def lambda_1309():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_1309)

    def lambda_131E():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_131E)

    def lambda_1333():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1333)
    Sleep(50)

    def lambda_134D():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_134D)

    def lambda_1362():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1362)

    def lambda_1377():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1377)
    Sleep(50)

    def lambda_1391():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1391)

    def lambda_13A6():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_13A6)

    def lambda_13BB():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_13BB)
    Sleep(50)

    def lambda_13D5():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_13D5)

    def lambda_13EA():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_13EA)

    def lambda_13FF():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_13FF)
    Sleep(50)

    def lambda_1419():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_1419)

    def lambda_142E():
        OP_92(0xFE, 0x10E, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_142E)
    Sleep(100)
    OP_44(0x21, 0x2)
    OP_44(0x22, 0x2)
    OP_44(0x23, 0x2)
    Sleep(100)
    OP_44(0x24, 0x2)
    OP_44(0x25, 0x2)
    OP_44(0x26, 0x2)
    Sleep(100)
    OP_44(0x27, 0x2)
    OP_44(0x28, 0x2)
    OP_44(0x29, 0x2)
    Sleep(100)
    OP_44(0x2A, 0x2)
    OP_44(0x2B, 0x2)
    OP_44(0x2C, 0x2)
    Sleep(100)
    OP_44(0x2D, 0x2)
    OP_44(0x2E, 0x2)
    OP_43(0x21, 0x0, 0x0, 0x8)

    NpcTalk(    #14
        0x10E,
        "尤莉亚上尉",
        "#174F……呜…………！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x30, 120, 0, 31300, 0)
    OP_8C(0x10E, 0, 500)

    def lambda_14E2():
        OP_6D(1160, 0, 32600, 1500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_14E2)
    OP_62(0x30, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_150C():
        OP_8E(0xFE, 0x78, 0x2EE, 0xBCAC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_150C)

    def lambda_1527():
        OP_8E(0xFE, 0x78, 0x2EE, 0xBB44, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1527)
    Sleep(1500)

    NpcTalk(    #15
        0x23,
        "尖叫声",
        "#3S#4P等一下～！　尤莉亚大人～#2S㈱\x02",
    )

    Jump("loc_157F")

    label("loc_157F")

    CloseMessageWindow()
    OP_43(0x21, 0x3, 0x0, 0xB)

    NpcTalk(    #16
        0x22,
        "尖叫声",
        "#3S#4P不要走呀――！！#2S\x02",
    )

    Jump("loc_15BB")

    label("loc_15BB")

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0xD)
    Sleep(150)
    OP_22(0xAF, 0x0, 0x64)
    OP_43(0x21, 0x3, 0x0, 0xC)

    def lambda_15DA():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_15DA)

    def lambda_15F5():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_15F5)
    Sleep(50)

    def lambda_1615():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1615)

    def lambda_1630():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_1630)
    Sleep(50)

    def lambda_1650():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_1650)

    def lambda_166B():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_166B)
    Sleep(100)
    OP_43(0x11, 0x3, 0x0, 0xE)
    Sleep(150)

    def lambda_1697():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_1697)
    Sleep(50)

    def lambda_16B7():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_16B7)

    def lambda_16D2():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_16D2)
    Sleep(50)

    def lambda_16F2():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_16F2)

    def lambda_170D():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_170D)
    Sleep(50)

    def lambda_172D():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_172D)

    def lambda_1748():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_1748)

    def lambda_1763():
        OP_90(0xFE, 0x0, 0x0, 0x7530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_1763)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_43(0x21, 0x0, 0x0, 0x9)
    OP_0D()
    OP_20(0x1388)
    OP_24(0x85, 0x5A)
    Sleep(500)
    OP_24(0x85, 0x50)
    Sleep(500)
    OP_24(0x85, 0x46)
    Sleep(400)
    OP_24(0x85, 0x3C)
    Sleep(300)
    OP_24(0x85, 0x32)
    Sleep(300)
    OP_24(0x85, 0x28)
    Sleep(300)
    OP_24(0x85, 0x1E)
    Sleep(300)
    OP_24(0x85, 0x14)
    Sleep(300)
    OP_23(0x85)
    Sleep(800)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_A70 end

    def Function_8_17F2(): pass

    label("Function_8_17F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B40")
    OP_62(0x27, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1834():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1834)
    Sleep(200)
    OP_62(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_188A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_188A)
    Sleep(300)
    OP_62(0x24, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_18E0():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_18E0)
    Sleep(200)
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1936():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1936)
    Sleep(400)

    def lambda_1959():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1959)
    OP_62(0x2C, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_19AA():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_19AA)
    Sleep(300)
    OP_62(0x2A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1A00():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1A00)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1A56():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1A56)
    Sleep(300)
    OP_62(0x2B, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1AAC():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1AAC)
    Sleep(400)

    def lambda_1ACF():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1ACF)
    OP_62(0x2D, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1B20():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_1B20)
    Sleep(400)
    Jump("Function_8_17F2")

    label("loc_1B40")

    Return()

    # Function_8_17F2 end

    def Function_9_1B41(): pass

    label("Function_9_1B41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E50")
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1B6C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1B6C)
    Sleep(200)
    OP_62(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1BBD():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_1BBD)
    Sleep(300)
    OP_62(0x24, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1C0E():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_1C0E)
    Sleep(200)
    OP_62(0x28, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1C5F():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1C5F)
    Sleep(400)

    def lambda_1C82():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1C82)
    OP_62(0x2C, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x2E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1CCE():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1CCE)
    Sleep(300)
    OP_62(0x2A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1D1F():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1D1F)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1D70():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1D70)
    Sleep(300)
    OP_62(0x2B, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1DC1():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1DC1)
    Sleep(400)

    def lambda_1DE4():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1DE4)
    OP_62(0x2D, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    def lambda_1E30():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_1E30)
    Sleep(400)
    Jump("Function_9_1B41")

    label("loc_1E50")

    Return()

    # Function_9_1B41 end

    def Function_10_1E51(): pass

    label("Function_10_1E51")

    OP_22(0x85, 0x1, 0x50)

    label("loc_1E56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E78")
    OP_7C(0x0, 0x78, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_1E56")

    label("loc_1E78")

    Return()

    # Function_10_1E51 end

    def Function_11_1E79(): pass

    label("Function_11_1E79")

    OP_22(0x85, 0x1, 0x50)

    label("loc_1E7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EA0")
    OP_7C(0x0, 0xB4, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_1E7E")

    label("loc_1EA0")

    Return()

    # Function_11_1E79 end

    def Function_12_1EA1(): pass

    label("Function_12_1EA1")

    OP_22(0x85, 0x1, 0x64)

    label("loc_1EA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EC8")
    OP_7C(0x0, 0xF0, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("loc_1EA6")

    label("loc_1EC8")

    Return()

    # Function_12_1EA1 end

    def Function_13_1EC9(): pass

    label("Function_13_1EC9")

    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(    #17 op#A
        0x10,
        "#10A#3S#1P哇！？#2S\x02",
    )

    Sleep(200)
    SetChrChipByIndex(0x10, 20)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x4)

    def lambda_1F07():
        OP_96(0xFE, 0xFFFFF510, 0xFFFFFE70, 0x7C60, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F07)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 0, 0)
    SetChrChipByIndex(0x10, 11)
    SetChrSubChip(0x10, 0)
    Return()

    # Function_13_1EC9 end

    def Function_14_1F36(): pass

    label("Function_14_1F36")

    OP_22(0x7D, 0x0, 0x64)

    ChrTalk(    #18 op#A
        0x11,
        "#10A#3S#5P呜……！？#2S\x02",
    )

    Sleep(200)
    OP_8C(0x11, 270, 0)
    SetChrChipByIndex(0x11, 20)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x4)

    def lambda_1F7F():
        OP_96(0xFE, 0x1900, 0xFFFFF448, 0x7E90, 0x5DC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F7F)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_22(0xE4, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 6400, -3000, 32400, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_14_1F36 end

    def Function_15_1FDC(): pass

    label("Function_15_1FDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1220, 0, 42880, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -1660, 0, 41680, 180)
    SetChrPos(0x11, 1660, 0, 41680, 180)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x21, 690, 0, 40650, 0)
    SetChrPos(0x22, -960, 0, 40480, 0)
    SetChrPos(0x23, -200, 0, 39560, 0)
    SetChrPos(0x24, 1240, 0, 39760, 0)
    SetChrPos(0x25, 2180, 0, 39230, 0)
    SetChrPos(0x26, -1740, 0, 38830, 0)
    SetChrPos(0x27, 540, 0, 38280, 0)
    SetChrPos(0x28, -2580, 0, 40000, 45)
    SetChrPos(0x29, 1670, 0, 37890, 0)
    SetChrPos(0x2A, 2620, 0, 40300, 315)
    SetChrPos(0x2B, -2970, 0, 38500, 45)
    SetChrPos(0x2C, -1460, 0, 37790, 0)
    SetChrPos(0x2D, -180, 0, 37020, 0)
    SetChrPos(0x2E, 3160, 0, 38120, 315)
    SetChrPos(0x10E, 340, 750, 51700, 180)
    SetChrChipByIndex(0x10E, 12)
    SetChrSubChip(0x10E, 0)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, 0, 750, 51200, 180)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #19
        0x10,
        "#1P好、好了～，各位——！\x02",
    )

    OP_9E(0x10, 0x1E, 0x0, 0x1F4, 0xBB8)
    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#1P请退后一点……！\x02",
    )

    CloseMessageWindow()
    OP_9E(0x10, 0x1E, 0x0, 0x12C, 0xBB8)
    Sleep(800)

    ChrTalk(    #21
        0x11,
        (
            "#1P请、请大家\x01",
            "冷静一下～……\x02",
        )
    )

    OP_9E(0x11, 0x1E, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    OP_70(0x0, 0x1C2)
    Sleep(800)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_22D1():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_22D1)

    def lambda_22EF():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22EF)
    Sleep(600)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x2A, 255)
    OP_4A(0x2B, 255)
    OP_4A(0x2C, 255)
    OP_4A(0x2D, 255)
    OP_4A(0x2E, 255)

    def lambda_234A():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_234A)
    OP_8C(0x11, 0, 500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x21, 0x0, 0x0, 0x8)
    Sleep(1000)

    NpcTalk(    #22
        0x21,
        "尖叫声",
        "#4P呀，一定是尤莉亚大人！\x02",
    )

    Jump("loc_23BD")

    label("loc_23BD")

    CloseMessageWindow()

    NpcTalk(    #23
        0x22,
        "尖叫声",
        "#4P尤莉亚大人，看这边～！！\x02",
    )

    Jump("loc_23F4")

    label("loc_23F4")

    CloseMessageWindow()

    def lambda_23FB():
        OP_6D(0, 0, 43900, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_23FB)

    def lambda_2413():
        OP_67(0, 5800, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2413)

    def lambda_242B():
        OP_6B(3260, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_242B)

    def lambda_243B():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_243B)

    def lambda_244B():

        label("loc_244B")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_244B")

    QueueWorkItem2(0x10, 2, lambda_244B)

    def lambda_245C():

        label("loc_245C")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_245C")

    QueueWorkItem2(0x11, 2, lambda_245C)

    def lambda_246D():

        label("loc_246D")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_246D")

    QueueWorkItem2(0x21, 2, lambda_246D)

    def lambda_247E():

        label("loc_247E")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_247E")

    QueueWorkItem2(0x22, 2, lambda_247E)

    def lambda_248F():

        label("loc_248F")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_248F")

    QueueWorkItem2(0x23, 2, lambda_248F)

    def lambda_24A0():

        label("loc_24A0")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24A0")

    QueueWorkItem2(0x24, 2, lambda_24A0)

    def lambda_24B1():

        label("loc_24B1")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24B1")

    QueueWorkItem2(0x25, 2, lambda_24B1)

    def lambda_24C2():

        label("loc_24C2")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24C2")

    QueueWorkItem2(0x26, 2, lambda_24C2)

    def lambda_24D3():

        label("loc_24D3")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24D3")

    QueueWorkItem2(0x27, 2, lambda_24D3)

    def lambda_24E4():

        label("loc_24E4")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24E4")

    QueueWorkItem2(0x28, 2, lambda_24E4)

    def lambda_24F5():

        label("loc_24F5")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_24F5")

    QueueWorkItem2(0x29, 2, lambda_24F5)

    def lambda_2506():

        label("loc_2506")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2506")

    QueueWorkItem2(0x2A, 2, lambda_2506)

    def lambda_2517():

        label("loc_2517")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2517")

    QueueWorkItem2(0x2B, 2, lambda_2517)

    def lambda_2528():

        label("loc_2528")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2528")

    QueueWorkItem2(0x2C, 2, lambda_2528)

    def lambda_2539():

        label("loc_2539")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_2539")

    QueueWorkItem2(0x2D, 2, lambda_2539)

    def lambda_254A():

        label("loc_254A")

        TurnDirection(0xFE, 0x2F, 500)
        OP_48()
        Jump("loc_254A")

    QueueWorkItem2(0x2E, 2, lambda_254A)

    def lambda_255B():
        OP_8E(0xFE, 0x0, 0x2EE, 0xACD0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_255B)
    Sleep(50)

    def lambda_257B():
        OP_8E(0xFE, 0x154, 0x2EE, 0xAEC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_257B)
    WaitChrThread(0x2F, 0x1)
    OP_44(0x21, 0x0)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x29, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x22,
        "咦………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x21,
        (
            "怎么，\x01",
            "是大主教大人和修女啊……\x02",
        )
    )

    Jump("loc_26F2")

    label("loc_26F2")

    CloseMessageWindow()

    ChrTalk(    #26
        0x2F,
        (
            "喂喂，你们。\x01",
            "快让路。\x02",
        )
    )

    Jump("loc_2720")

    label("loc_2720")

    CloseMessageWindow()

    NpcTalk(    #27
        0x10E,
        "修女艾伦",
        "………………（鞠躬）。\x02",
    )

    Jump("loc_2758")

    label("loc_2758")

    CloseMessageWindow()

    def lambda_275F():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_275F)

    def lambda_277A():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_277A)
    Sleep(50)

    def lambda_279A():
        OP_91(0xFE, 0x320, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_279A)

    def lambda_27B5():
        OP_91(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_27B5)
    Sleep(50)

    def lambda_27D5():
        OP_91(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_27D5)

    def lambda_27F0():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_27F0)

    def lambda_280B():
        OP_91(0xFE, 0x190, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_280B)
    Sleep(50)

    def lambda_282B():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_282B)

    def lambda_2846():
        OP_91(0xFE, 0x190, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2846)
    Sleep(50)

    def lambda_2866():
        OP_91(0xFE, 0xC8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_2866)

    def lambda_2881():
        OP_91(0xFE, 0xC8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_2881)

    def lambda_289C():
        OP_91(0xFE, 0xFFFFFF9C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_289C)

    def lambda_28B7():
        OP_8E(0xFE, 0x0, 0x0, 0x85C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_28B7)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_28E9():
        OP_8E(0xFE, 0x154, 0x0, 0x87B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_28E9)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1FDC end

    def Function_16_2972(): pass

    label("Function_16_2972")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -2090, 0, 42000, 180)
    SetChrPos(0x11, 2440, 0, 42000, 180)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x1C2, 0x0, 0x64)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 450)

    def lambda_29F0():
        OP_6E(496, 9000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_29F0)
    OP_6D(3500, 100, 49020, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(37000, 0)
    OP_6E(496, 0)

    def lambda_2A3D():
        OP_6B(3330, 5000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_2A3D)
    FadeToBright(2000, 0)
    OP_0D()
    OP_23(0x1C2)
    WaitChrThread(0x1B, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2972 end

    def Function_17_2A76(): pass

    label("Function_17_2A76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(0, 3540, 26420, 0)
    OP_67(0, 2660, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 760, 0, 28520, 180)
    SetChrPos(0x13, -2280, 0, 30400, 180)
    SetChrPos(0x14, 2280, 0, 30400, 180)
    SetChrPos(0x15, -760, 0, 28520, 180)
    SetChrPos(0x103, -1400, 0, 18240, 0)
    SetChrPos(0x151, 0, 0, 18300, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #28
        0x12,
        "#2P好慢啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        "#2P那些家伙，在干什么……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 135, 400)
    Sleep(300)

    ChrTalk(    #30
        0x15,
        "#1P哎，别那么着急嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x15,
        (
            "#1P本来就不必\x01",
            "特意去把她抓起来嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x15,
        (
            "#1P只要就这样下去\x01",
            "等正午的钟声响过……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 225, 400)
    Sleep(300)

    ChrTalk(    #33
        0x12,
        "#2P但、但是呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x12,
        (
            "#2P如果遗嘱就这么无效了，\x01",
            "遗产可是要平分哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "#2P我们拿的份也会减少。\x01",
            "我可不想这样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x15,
        "#1P还有很多手段。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x15,
        (
            "#1P对手不过是个小丫头。\x01",
            "……对吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x151,
        "声音",
        "#5P啊……………………\x02",
    )

    Jump("loc_2D44")

    label("loc_2D44")

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2DB6():
        OP_6D(0, 0, 25920, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_2DB6)

    def lambda_2DCE():
        OP_67(0, 3880, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2DCE)

    def lambda_2DE6():
        OP_6B(3460, 2500)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_2DE6)

    def lambda_2DF6():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DF6)
    Sleep(100)

    def lambda_2E09():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2E09)
    WaitChrThread(0x1B, 0x0)
    Sleep(500)

    def lambda_2E21():
        OP_8E(0xFE, 0x0, 0x0, 0x5398, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2E21)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #39
        0x151,
        (
            "#1653F#12P…………伯父……？\x02\x03",

            "#1656F………为什么…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x15,
        (
            "哎呀，爱娜，\x01",
            "你怎么到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x15,
        "都跟你说外面很危险了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x15,
        "……不要一个人到处乱走哦？\x02",
    )

    CloseMessageWindow()

    def lambda_2F05():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0x4FD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F05)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #43
        0x103,
        (
            "#1644F#6P………………喂，大叔。\x01",
            "你看不到我在这儿吗？\x02\x03",

            "爱娜可不是独自一人啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x15,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x15,
        "……真碍事啊，你这家伙。\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x13, 0)
    Sleep(100)
    OP_7D(0x0, 0x103, 0xA, 0xC8)

    def lambda_2FF8():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0x52BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FF8)
    WaitChrThread(0x103, 0x1)
    OP_7D(0x1, 0x103, 0x0, 0x0)

    def lambda_3020():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3020)
    OP_43(0x103, 0x3, 0x0, 0x12)
    Sleep(10)
    OP_43(0x151, 0x3, 0x0, 0x13)
    OP_22(0x1F7, 0x0, 0x64)
    SetChrSubChip(0x13, 1)
    Sleep(100)
    SetChrSubChip(0x13, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -1400, 0, 20440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    SetChrSubChip(0x13, 1)
    Sleep(100)
    SetChrSubChip(0x13, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0, 0, 21400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    Sleep(1000)

    ChrTalk(    #46
        0x103,
        (
            "#1647F#6P（唔…………\x01",
            "  连爱娜都想杀吗！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x15,
        "#5P啊啊，真遗憾。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13, 500)
    Sleep(300)

    ChrTalk(    #48
        0x15,
        "#5P……你是不是不擅长射击？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 0)
    Sleep(100)
    TurnDirection(0x13, 0x15, 500)
    Sleep(300)

    ChrTalk(    #49
        0x13,
        "抱、抱歉。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_31C9():
        OP_8F(0xFE, 0x0, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_31C9)
    Sleep(500)

    def lambda_31E9():
        OP_8F(0xFE, 0xFFFFFC40, 0x0, 0x4BF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_31E9)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #50
        0x151,
        "#1654F#12P……雪拉扎德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        "#1642F#6P…………什么事，爱娜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x151,
        (
            "#1654F#12P……够了。\x02\x03",

            "#1652F没时间了，\x01",
            "我们强行突破吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 9)
    SetChrSubChip(0x103, 0)
    Sleep(250)

    ChrTalk(    #53
        0x103,
        "#1640F#6P…………明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x15,
        (
            "来……\x01",
            "回家吧，爱娜。\x02",
        )
    )

    Jump("loc_330B")

    label("loc_330B")

    CloseMessageWindow()
    Sleep(300)
    Fade(600)
    TurnDirection(0x15, 0x151, 300)
    OP_0D()
    Sleep(300)
    OP_8C(0x13, 180, 500)
    Sleep(400)

    ChrTalk(    #55
        0x15,
        "……大家都在等你呢。\x02",
    )

    CloseMessageWindow()
    Battle(0x3AF, 0x0, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 20)
    Return()

    # Function_17_2A76 end

    def Function_18_3370(): pass

    label("Function_18_3370")

    SetChrChipByIndex(0x103, 28)
    SetChrSubChip(0x103, 2)

    def lambda_3380():
        OP_96(0xFE, 0xFFFFFC40, 0x0, 0x48D0, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3380)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    Return()

    # Function_18_3370 end

    def Function_19_33A8(): pass

    label("Function_19_33A8")

    SetChrChipByIndex(0x151, 29)
    SetChrSubChip(0x151, 2)

    def lambda_33B8():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4A9C, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_33B8)
    WaitChrThread(0x151, 0x1)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    Return()

    # Function_19_33A8 end

    def Function_20_33E0(): pass

    label("Function_20_33E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0xE)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_6D(480, 0, 29600, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x12, 0x800)
    SetChrFlags(0x13, 0x800)
    SetChrFlags(0x14, 0x800)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x12, -2120, -200, 27400, 225)
    SetChrPos(0x13, -2080, 0, 30400, 270)
    SetChrPos(0x14, 2500, 0, 30260, 180)
    SetChrPos(0x15, 0, 0, 30200, 180)
    SetChrPos(0x103, -320, 0, 26220, 0)
    SetChrPos(0x151, 1340, 0, 26760, 0)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3501"),
        (SWITCH_DEFAULT, "loc_350E"),
    )


    label("loc_3501")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_351B")

    label("loc_350E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_351B")

    label("loc_351B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3560")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆打倒了绅士\x01",      # 0
            "◆没打倒绅士\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_3560")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3571"),
        (1, "loc_3585"),
        (SWITCH_DEFAULT, "loc_3588"),
    )


    label("loc_3571")

    OP_8C(0x15, 0, 0)
    SetChrChipByIndex(0x15, 26)
    SetChrSubChip(0x15, 0)
    Jump("loc_3588")

    label("loc_3585")

    Jump("loc_3588")

    label("loc_3588")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3599"),
        (0, "loc_3B27"),
        (SWITCH_DEFAULT, "loc_3D01"),
    )


    label("loc_3599")


    def lambda_359F():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_359F)
    FadeToBright(1000, 0)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x15, 90, 500)
    Sleep(500)
    OP_8C(0x15, 270, 500)
    Sleep(500)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x15, 90, 500)
    Sleep(500)
    OP_8C(0x15, 270, 500)
    Sleep(500)

    ChrTalk(    #56
        0x15,
        "怎、怎么会这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x15,
        (
            "我还特意花了高价\x01",
            "雇来这些家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x15,
        (
            "这可是毁约啊。\x01",
            "呜、呜呜……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x15, 90, 500)
    Sleep(500)
    OP_8C(0x15, 270, 500)
    Sleep(500)

    ChrTalk(    #59
        0x103,
        (
            "#1646F……真丢人啊。\x02\x03",

            "#1642F给你一招狠的\x01",
            "作为见面礼吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36F4():
        OP_8E(0xFE, 0xFFFFFEC0, 0x0, 0x6BE4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36F4)
    WaitChrThread(0x103, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 9)
    SetChrSubChip(0x103, 0)
    Sleep(250)
    OP_8C(0x15, 180, 500)
    Sleep(200)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_374B():
        OP_8F(0xFE, 0x0, 0x0, 0x7A6C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_374B)
    Sleep(300)

    ChrTalk(    #60
        0x15,
        "你、你是什么人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x15,
        "竟然这么粗暴……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x15,
        "知、知不知道什么是教养啊！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x1)

    ChrTalk(    #63
        0x103,
        "#1648F…………唔………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x151,
        "#1654F……那个，伯父……\x02",
    )

    CloseMessageWindow()

    def lambda_3821():
        OP_8E(0xFE, 0x410, 0x0, 0x6EC8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3821)
    WaitChrThread(0x151, 0x1)

    def lambda_3841():
        OP_8E(0xFE, 0x0, 0x0, 0x7300, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3841)
    WaitChrThread(0x151, 0x1)
    TurnDirection(0x151, 0x15, 500)
    Fade(250)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    Sleep(300)

    ChrTalk(    #65
        0x151,
        (
            "#1656F我本来并不想要\x01",
            "土地或财产之类的东西。\x02\x03",

            "我并不是为了那种东西\x01",
            "才这么执着的。\x02\x03",

            "#1654F…………但是……\x02\x03",

            "#1652F我决不能让一米拉\x01",
            "落到你这种人的手中。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3933():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_3933)

    def lambda_3943():
        OP_8E(0xFE, 0x0, 0x0, 0x774C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3943)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #66 op#A op#5
        0x151,
        "#1652F#6P#3S#17A……对不起了！#2S\x05\x02",
    )

    SetChrChipByIndex(0x151, 27)
    SetChrSubChip(0x151, 0)
    Sleep(800)

    def lambda_39A0():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_39A0)
    Sleep(600)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
    OP_22(0x8E, 0x0, 0x64)
    SetChrFlags(0x15, 0x4)

    def lambda_39D0():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_39D0)

    def lambda_39EA():
        OP_95(0xFE, 0xFFFFFF9C, 0xFFFFFF9C, 0x514, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_39EA)
    WaitChrThread(0x15, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x15, 26)
    SetChrSubChip(0x15, 0)
    OP_8C(0x15, 0, 0)
    Sleep(1000)

    def lambda_3A28():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3A28)
    Sleep(200)
    OP_62(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x103,
        (
            "#1645F呜哇，好像很痛…………\x02\x03",

            "之前我就在想了，\x01",
            "你真的是千金小姐？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    Sleep(100)
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #68
        0x151,
        (
            "#1651F好过分啊。\x02\x03",

            "雪拉扎德才是，\x01",
            "总是用粗鲁的语气跟我说话吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D01")

    label("loc_3B27")


    def lambda_3B2D():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_3B2D)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1B, 0x0)

    ChrTalk(    #69
        0x151,
        "#1652F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#1642F……真是令人火大的老头。\x01",
            "要再揍一拳吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x151,
        (
            "#1654F不用了，放了他吧。\x01",
            "反正都解决了……\x02\x03",

            "#1656F他本来也不是坏人。\x02\x03",

            "只是因为我继承了财产，\x01",
            "才起了歹心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#1646F…………是这样吗。\x01",
            "你是不是太心软了？\x02\x03",

            "#1642F这家伙，可是想杀死你的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x151,
        (
            "#1650F万一不行的话，就由我来揍他。\x02\x03",

            "#1651F……用这个包包。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        "#1645F那、那好像很痛呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D01")

    label("loc_3D01")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 450)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x16, 0, 750, 44100, 180)
    SetChrPos(0x17, 1700, 750, 45000, 180)
    SetChrPos(0x18, -1700, 750, 45000, 180)
    SetChrPos(0x19, 1700, 750, 46420, 180)
    SetChrPos(0x1A, -1700, 750, 46420, 180)

    NpcTalk(    #75
        0x16,
        "声音",
        (
            "你们几个，\x01",
            "在这里干什么！\x02",
        )
    )

    Jump("loc_3DC5")

    label("loc_3DC5")

    CloseMessageWindow()

    def lambda_3DCC():
        OP_6D(480, 0, 42200, 1500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_3DCC)

    def lambda_3DE4():
        OP_6B(3400, 1500)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3DE4)
    WaitChrThread(0x1B, 0x0)
    SetChrPos(0x103, -680, 0, 28940, 0)
    SetChrPos(0x151, 700, 0, 29340, 0)
    SetChrPos(0x15, -500, 0, 27040, 180)
    SetChrPos(0x12, 1460, 0, 27120, 225)
    SetChrPos(0x13, -2540, 0, 26100, 180)
    SetChrPos(0x14, -900, -400, 24780, 90)
    SetChrChipByIndex(0x12, 10)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x14, 25)
    SetChrSubChip(0x14, 0)
    Sleep(500)

    def lambda_3E78():
        OP_6D(780, 0, 30200, 3000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_3E78)

    def lambda_3E90():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3E90)

    def lambda_3EA8():
        OP_6B(3320, 3000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_3EA8)

    def lambda_3EB8():
        OP_8E(0xFE, 0x0, 0x0, 0x7D3C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3EB8)
    Sleep(50)

    def lambda_3ED8():
        OP_8E(0xFE, 0x6A4, 0x0, 0x8124, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3ED8)

    def lambda_3EF3():
        OP_8E(0xFE, 0xFFFFF95C, 0x0, 0x8124, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3EF3)
    Sleep(50)

    def lambda_3F13():
        OP_8E(0xFE, 0x6A4, 0x0, 0x8700, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3F13)

    def lambda_3F2E():
        OP_8E(0xFE, 0xFFFFF95C, 0x0, 0x8700, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3F2E)
    WaitChrThread(0x16, 0x1)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x17,
        "到、到底发生了什么事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x16,
        (
            "就、就是说你！\x01",
            "放下武器！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_401B():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0x7300, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_401B)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #78
        0x103,
        "#1642F……我是游击士协会的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x16,
        (
            "什么！？\x01",
            "竟然是……游击士？\x02",
        )
    )

    Jump("loc_4098")

    label("loc_4098")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05雪拉扎德出示了准游击士徽章。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #81
        0x16,
        (
            "唔、唔……\x01",
            "…………确实没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x16,
        (
            "但是，\x01",
            "游击士又在这里干什么！？\x02",
        )
    )

    Jump("loc_413B")

    label("loc_413B")

    CloseMessageWindow()

    ChrTalk(    #83
        0x16,
        (
            "虽然陛下承认你们的存在，\x01",
            "但竟然在王城前引起如此骚乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#1646F这些家伙很可能在王都\x01",
            "犯下了严重的罪行。\x02\x03",

            "为了王都治安和民众的安全，\x01",
            "我只是让他们睡着了而已。\x02\x03",

            "#1642F……能麻烦你们\x01",
            "把他们逮捕起来吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x16,
        "唔、唔唔…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x16,
        "…………没办法了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "本来应该连你们\x01",
            "也一起拘捕的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 0, 600)
    Sleep(300)

    ChrTalk(    #88
        0x16,
        "喂！\x02",
    )

    Jump("loc_42B0")

    label("loc_42B0")

    CloseMessageWindow()
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("士兵们")

    AnonymousTalk(    #89
        "\x07\x00#3S是……！\x02",
    )

    Jump("loc_42E2")

    label("loc_42E2")

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_43(0x17, 0x3, 0x0, 0x17)
    OP_43(0x18, 0x3, 0x0, 0x15)
    OP_43(0x19, 0x3, 0x0, 0x18)
    OP_43(0x1A, 0x3, 0x0, 0x16)
    Sleep(1000)
    OP_8C(0x16, 180, 500)
    Sleep(300)

    ChrTalk(    #90
        0x16,
        (
            "喂，游击士。\x01",
            "这次就放过你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x16,
        (
            "只不过要给我记住一点。\x01",
            "守护王都的是我们王都警卫队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x16,
        (
            "以后再多管闲事\x01",
            "就算是游击士也饶不了你们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        (
            "#1640F啊，对了。\x02\x03",

            "城里还有些残党，\x01",
            "能不能也麻烦你们处理？\x02\x03",

            "#1641F虽然有我的前辈们出马，\x01",
            "应该已经搞定了就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x16,
        "唔、唔……\x02",
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x19)

    def lambda_4478():

        label("loc_4478")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_4478")

    QueueWorkItem2(0x17, 3, lambda_4478)

    def lambda_4489():

        label("loc_4489")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_4489")

    QueueWorkItem2(0x18, 3, lambda_4489)
    Sleep(100)

    ChrTalk(    #95 op#A
        0x16,
        "#15A……你们两个，快去！\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #96
        0x17,
        "#11P是、是！\x02",
    )


    ChrTalk(    #97
        0x18,
        "#1P是、是！\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_44F6():

        label("loc_44F6")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_44F6")

    QueueWorkItem2(0x103, 3, lambda_44F6)

    def lambda_4507():

        label("loc_4507")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_4507")

    QueueWorkItem2(0x151, 3, lambda_4507)
    WaitChrThread(0x16, 0x3)
    OP_44(0x17, 0x3)

    def lambda_4521():
        OP_8F(0xFE, 0x3AC, 0x0, 0x3AF2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4521)
    Sleep(100)
    OP_44(0x18, 0x3)

    def lambda_4545():
        OP_8F(0xFE, 0xFFFFF5BA, 0x0, 0x36BA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4545)
    Sleep(1000)
    OP_44(0x103, 0x3)
    OP_44(0x151, 0x3)
    OP_44(0x17, 0x3)
    OP_44(0x18, 0x3)
    Sleep(800)

    ChrTalk(    #98
        0x103,
        (
            "#1645F呼………………\x01",
            "真是不擅长跟军人打交道啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x151)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x103, 0x151, 400)
    Sleep(200)

    ChrTalk(    #99
        0x103,
        "#1643F………………什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x151,
        (
            "#1650F#2P……游击士的徽章，\x01",
            "看来挺有威力的……\x02\x03",

            "感觉很酷呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #101
        0x103,
        (
            "#1646F我、我也是\x01",
            "第一次这样使用啦！\x02\x03",

            "#1642F好了，已经没时间了。\x01",
            "爱娜，我们快跑吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x151,
        "#1651F#2P好！\x02",
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x1A)
    Sleep(50)
    OP_8C(0x151, 0, 500)

    def lambda_471B():
        OP_8E(0xFE, 0x2BC, 0x0, 0x99AC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_471B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T4212   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_33E0 end

    def Function_21_4745(): pass

    label("Function_21_4745")


    def lambda_474B():
        OP_8E(0xFE, 0xFFFFF894, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_474B)
    WaitChrThread(0x18, 0x1)

    def lambda_476B():
        OP_8E(0xFE, 0xFFFFF5EC, 0x0, 0x6DD8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_476B)
    WaitChrThread(0x18, 0x1)

    def lambda_478B():
        OP_8E(0xFE, 0xFFFFEFDE, 0x0, 0x670C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_478B)
    WaitChrThread(0x18, 0x1)

    def lambda_47AB():
        OP_8E(0xFE, 0xFFFFF02E, 0x0, 0x5FDC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_47AB)
    WaitChrThread(0x18, 0x1)

    def lambda_47CB():
        OP_8E(0xFE, 0xFFFFF5BA, 0x0, 0x5DCA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_47CB)
    WaitChrThread(0x18, 0x1)
    TurnDirection(0x18, 0x14, 500)
    Return()

    # Function_21_4745 end

    def Function_22_47ED(): pass

    label("Function_22_47ED")


    def lambda_47F3():
        OP_8E(0xFE, 0xFFFFF894, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_47F3)
    WaitChrThread(0x1A, 0x1)

    def lambda_4813():
        OP_8E(0xFE, 0xFFFFF5EC, 0x0, 0x6DD8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4813)
    WaitChrThread(0x1A, 0x1)

    def lambda_4833():
        OP_8E(0xFE, 0xFFFFEFDE, 0x0, 0x670C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4833)
    WaitChrThread(0x1A, 0x1)

    def lambda_4853():
        OP_8E(0xFE, 0xFFFFF362, 0x0, 0x670C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4853)
    WaitChrThread(0x1A, 0x1)
    TurnDirection(0x1A, 0x13, 500)
    Return()

    # Function_22_47ED end

    def Function_23_4875(): pass

    label("Function_23_4875")


    def lambda_487B():
        OP_8E(0xFE, 0x76C, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_487B)
    WaitChrThread(0x17, 0x1)

    def lambda_489B():
        OP_8E(0xFE, 0xB40, 0x0, 0x6BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_489B)
    WaitChrThread(0x17, 0x1)

    def lambda_48BB():
        OP_8E(0xFE, 0x820, 0x0, 0x64DC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_48BB)
    WaitChrThread(0x17, 0x1)

    def lambda_48DB():
        OP_8E(0xFE, 0x3AC, 0x0, 0x6202, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_48DB)
    WaitChrThread(0x17, 0x1)
    TurnDirection(0x17, 0x14, 500)
    Return()

    # Function_23_4875 end

    def Function_24_48FD(): pass

    label("Function_24_48FD")


    def lambda_4903():
        OP_8E(0xFE, 0x76C, 0x0, 0x76F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4903)
    WaitChrThread(0x19, 0x1)

    def lambda_4923():
        OP_8E(0xFE, 0xB40, 0x0, 0x6BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4923)
    WaitChrThread(0x19, 0x1)

    def lambda_4943():
        OP_8E(0xFE, 0x8C0, 0x0, 0x6928, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4943)
    WaitChrThread(0x19, 0x1)
    TurnDirection(0x19, 0x12, 500)
    Return()

    # Function_24_48FD end

    def Function_25_4965(): pass

    label("Function_25_4965")


    def lambda_496B():
        OP_8E(0xFE, 0xFFFFF754, 0x0, 0x74F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_496B)
    WaitChrThread(0x16, 0x1)

    def lambda_498B():
        OP_8E(0xFE, 0xFFFFF6FA, 0x0, 0x6F40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_498B)
    WaitChrThread(0x16, 0x1)

    def lambda_49AB():
        OP_8E(0xFE, 0xFFFFED40, 0x0, 0x64F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_49AB)
    WaitChrThread(0x16, 0x1)

    def lambda_49CB():
        OP_8E(0xFE, 0xFFFFED40, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_49CB)
    WaitChrThread(0x16, 0x1)

    def lambda_49EB():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_49EB)
    WaitChrThread(0x16, 0x1)
    Return()

    # Function_25_4965 end

    def Function_26_4A06(): pass

    label("Function_26_4A06")

    OP_8C(0x103, 0, 500)

    def lambda_4A13():
        OP_8E(0xFE, 0xFFFFFD58, 0x0, 0x981C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A13)
    Return()

    # Function_26_4A06 end

    SaveToFile()

Try(main)
