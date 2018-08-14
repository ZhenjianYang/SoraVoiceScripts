from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4100   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4100.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '爱娜',                                 # 9
        '搬家公司职员',                         # 10
        '搬家公司职员',                         # 11
        '嘉瑟',                                 # 12
        '伯登',                                 # 13
        '拉塔娜',                               # 14
        '托朗老人',                             # 15
        '帕菲',                                 # 16
        '娜娜',                                 # 17
        '乌兰',                                 # 18
        '侬娜',                                 # 19
        '蒂库',                                 # 20
        '拉尔斯',                               # 21
        '托伊',                                 # 22
        '拜舍尔',                               # 23
        '伊鲁妮婆婆',                           # 24
        '王都格兰赛尔·北街区',                 # 25
        '庭院大道方向',                         # 26
        '王都格兰赛尔·东街区',                 # 27
        '王都格兰赛尔·西街区',                 # 28
        '黑衣人',                               # 29
        '黑衣人',                               # 30
        '黑衣人',                               # 31
        '黑衣人',                               # 32
        '箱子',                                 # 33
        '目标用摄影机',                         # 34
        '',                                     # 35
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
        'ED6_DT07/CH02710 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01200 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01100 ._CH',             # 05
        'ED6_DT07/CH02730 ._CH',             # 06
        'ED6_DT07/CH02740 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
        'ED6_DT07/CH01050 ._CH',             # 09
        'ED6_DT07/CH01160 ._CH',             # 0A
        'ED6_DT07/CH01470 ._CH',             # 0B
        'ED6_DT07/CH01060 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT07/CH01460 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT27/CH03460 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02710P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01200P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01100P._CP',             # 05
        'ED6_DT07/CH02730P._CP',             # 06
        'ED6_DT07/CH02740P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
        'ED6_DT07/CH01050P._CP',             # 09
        'ED6_DT07/CH01160P._CP',             # 0A
        'ED6_DT07/CH01470P._CP',             # 0B
        'ED6_DT07/CH01060P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT07/CH01460P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT27/CH03460P._CP',             # 10
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
        X                   = 7930,
        Z                   = 250,
        Y                   = -26470,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8400,
        Z                   = 250,
        Y                   = -30150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3670,
        Z                   = 0,
        Y                   = -43050,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 5760,
        Z                   = 0,
        Y                   = -46060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 1930,
        Z                   = 0,
        Y                   = -50840,
        Direction           = 270,
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
        X                   = 690,
        Z                   = 0,
        Y                   = -50920,
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
        X                   = 5870,
        Z                   = 0,
        Y                   = -38230,
        Direction           = 270,
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
        X                   = 5550,
        Z                   = 0,
        Y                   = -54380,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -840,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 710,
        Z                   = 0,
        Y                   = -50090,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -90,
        Z                   = 0,
        Y                   = -51500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 92000,
        Z                   = 300,
        Y                   = 61850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 7800,
        Z                   = 0,
        Y                   = -530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE4,
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


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = -65600,
        Range               = 2000,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -25000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -10280,
        Y                   = 0,
        Z                   = -11040,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = -14940,
        Y                   = 0,
        Z                   = -15750,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = -10290,
        Y                   = 0,
        Z                   = -30020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 9240,
        Y                   = 0,
        Z                   = -13010,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )

    DeclEvent(
        X                   = 15900,
        Y                   = 0,
        Z                   = 6330,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 40,
    )


    ScpFunction(
        "Function_0_552",          # 00, 0
        "Function_1_711",          # 01, 1
        "Function_2_7CB",          # 02, 2
        "Function_3_948",          # 03, 3
        "Function_4_96C",          # 04, 4
        "Function_5_9C9",          # 05, 5
        "Function_6_A56",          # 06, 6
        "Function_7_AC5",          # 07, 7
        "Function_8_B34",          # 08, 8
        "Function_9_B58",          # 09, 9
        "Function_10_BAA",         # 0A, 10
        "Function_11_C13",         # 0B, 11
        "Function_12_DC2",         # 0C, 12
        "Function_13_1050",        # 0D, 13
        "Function_14_1223",        # 0E, 14
        "Function_15_13EF",        # 0F, 15
        "Function_16_154D",        # 10, 16
        "Function_17_1552",        # 11, 17
        "Function_18_1719",        # 12, 18
        "Function_19_17D2",        # 13, 19
        "Function_20_19D0",        # 14, 20
        "Function_21_1BBD",        # 15, 21
        "Function_22_1D31",        # 16, 22
        "Function_23_1D80",        # 17, 23
        "Function_24_1E4C",        # 18, 24
        "Function_25_1E92",        # 19, 25
        "Function_26_2601",        # 1A, 26
        "Function_27_2A71",        # 1B, 27
        "Function_28_2CB4",        # 1C, 28
        "Function_29_2CFC",        # 1D, 29
        "Function_30_2D44",        # 1E, 30
        "Function_31_2D8C",        # 1F, 31
        "Function_32_2DD4",        # 20, 32
        "Function_33_3658",        # 21, 33
        "Function_34_3934",        # 22, 34
        "Function_35_3C3F",        # 23, 35
        "Function_36_3C7A",        # 24, 36
        "Function_37_3C7E",        # 25, 37
        "Function_38_3C82",        # 26, 38
        "Function_39_3C86",        # 27, 39
        "Function_40_3C8A",        # 28, 40
    )


    def Function_0_552(): pass

    label("Function_0_552")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x18, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_59F")
    Jump("loc_6A9")

    label("loc_59F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_624")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x24, 960, 0, -65800, 315)
    SetChrPos(0x25, -960, 0, -65800, 45)
    SetChrPos(0x26, 960, 0, -64099, 225)
    SetChrPos(0x27, -960, 0, -64099, 135)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x27, 0x0, 0x0, 0x2)
    OP_43(0x24, 0x3, 0x0, 0xA)
    Jump("loc_6A9")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_6A9")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_6A9")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x24, 0, 0, -64099, 180)
    SetChrPos(0x25, -1000, 0, -65800, 45)
    SetChrPos(0x26, 1000, 0, -65800, 315)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x24, 0x3, 0x0, 0x9)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 7140, 250, -23020, 135)

    label("loc_6A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_6D4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_6FD")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_6EA")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_6FD")

    label("loc_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_6FD")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_710")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_710")

    Return()

    # Function_0_552 end

    def Function_1_711(): pass

    label("Function_1_711")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDBDE0, 0x23005B)
    OP_B1("T4100_n")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AE")
    OP_71(0x411, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_76B")
    Jump("loc_7AE")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_77F")
    OP_1B(0x9, 0x0, 0x21)
    OP_B2(0x1, 0x0, 0x80)
    Jump("loc_7AE")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_789")
    Jump("loc_7AE")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7AE")
    OP_1B(0xB, 0x0, 0x1C)
    OP_1B(0xC, 0x0, 0x1D)
    OP_1B(0xD, 0x0, 0x1E)
    OP_1B(0xE, 0x0, 0x1F)
    OP_1B(0x9, 0x0, 0x21)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_7AE")

    SoundDistance(0x1CB, 0x32, 0x0, 0xFFFF4BCE, 0x7D0, 0x3A98, 0x64, 0x0)
    Return()

    # Function_1_711 end

    def Function_2_7CB(): pass

    label("Function_2_7CB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_932")

    label("loc_7F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_809")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_932")

    label("loc_809")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_932")

    label("loc_822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_932")

    label("loc_83B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_932")

    label("loc_854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_932")

    label("loc_86D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_886")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_932")

    label("loc_886")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_932")

    label("loc_89F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_932")

    label("loc_8B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_932")

    label("loc_8D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_932")

    label("loc_8EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_903")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_932")

    label("loc_903")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_932")

    label("loc_91C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_932")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_947")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_932")

    label("loc_947")

    Return()

    # Function_2_7CB end

    def Function_3_948(): pass

    label("Function_3_948")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96B")
    OP_8D(0xFE, 3700, -42040, 10110, -50100, 2000)
    Jump("Function_3_948")

    label("loc_96B")

    Return()

    # Function_3_948 end

    def Function_4_96C(): pass

    label("Function_4_96C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C8")
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0xFFFF6E24, 0x8FC, 0x0)
    OP_8E(0xFE, 0x9CE, 0x0, 0x2166, 0x8FC, 0x0)
    OP_8E(0xFE, 0xFFFFF7EA, 0x0, 0x2166, 0x8FC, 0x0)
    Jump("Function_4_96C")

    label("loc_9C8")

    Return()

    # Function_4_96C end

    def Function_5_9C9(): pass

    label("Function_5_9C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A55")
    OP_8E(0xFE, 0xDC0, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0xFFFF6532, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF29A, 0x0, 0x2990, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDC0, 0x0, 0x2990, 0x7D0, 0x0)
    Jump("Function_5_9C9")

    label("loc_A55")

    Return()

    # Function_5_9C9 end

    def Function_6_A56(): pass

    label("Function_6_A56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC4")
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
    Jump("Function_6_A56")

    label("loc_AC4")

    Return()

    # Function_6_A56 end

    def Function_7_AC5(): pass

    label("Function_7_AC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B33")
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
    Jump("Function_7_AC5")

    label("loc_B33")

    Return()

    # Function_7_AC5 end

    def Function_8_B34(): pass

    label("Function_8_B34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B57")
    OP_8D(0xFE, -9540, -8220, -7490, -4270, 2000)
    Jump("Function_8_B34")

    label("loc_B57")

    Return()

    # Function_8_B34 end

    def Function_9_B58(): pass

    label("Function_9_B58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA9")
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x26, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jump("Function_9_B58")

    label("loc_BA9")

    Return()

    # Function_9_B58 end

    def Function_10_BAA(): pass

    label("Function_10_BAA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C12")
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x26, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x27, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jump("Function_10_BAA")

    label("loc_C12")

    Return()

    # Function_10_BAA end

    def Function_11_C13(): pass

    label("Function_11_C13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_DBE")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_CF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C9C")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #0
        0xFE,
        "嗯～这里是南街区……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "顺着这条道直走就是北街区，\x01",
            "再前面就是格兰赛尔城……对吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 0)
    Jump("loc_CF0")

    label("loc_C9C")


    ChrTalk(    #2
        0xFE,
        (
            "嗯～首先要在格兰赛尔城\x01",
            "办理居住转移的手续……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "然后就得找工作了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_CF0")

    Jump("loc_DBE")

    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_CFD")
    Jump("loc_DBE")

    label("loc_CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_DBE")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D65")

    ChrTalk(    #4
        0xFE,
        (
            "我才刚从\x01",
            "乡下过来。\x02",
        )
    )

    Jump("loc_D38")

    label("loc_D38")

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "好，\x01",
            "要找到工作努力干活～！\x02",
        )
    )

    Jump("loc_D61")

    label("loc_D61")

    CloseMessageWindow()
    Jump("loc_DB7")

    label("loc_D65")


    ChrTalk(    #6
        0xFE,
        (
            "我、我才刚从\x01",
            "乡下过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "王都好大啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "好、好像很容易迷路。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_DB7")

    OP_8C(0xFE, 135, 0)

    label("loc_DBE")

    TalkEnd(0xFE)
    Return()

    # Function_11_C13 end

    def Function_12_DC2(): pass

    label("Function_12_DC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_DCF")
    Jump("loc_104C")

    label("loc_DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_E70")

    ChrTalk(    #9
        0xFE,
        (
            "北街区大概可以称为\x01",
            "高级住宅区吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "虽然的确没有\x01",
            "郊外的宅邸那么大，\x01",
            "但都是些豪华的房子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "那大概就是\x01",
            "格兰赛尔市民的憧憬吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2B")

    label("loc_E70")


    ChrTalk(    #12
        0xFE,
        "格兰赛尔是个很大的城市吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "南街区就像你看到的这样，\x01",
            "东街区有百货店和大竞技场，\x01",
            "西街区有大圣堂和格兰赛尔港。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "北街区则有\x01",
            "利贝尔最大的旅馆，\x01",
            "而且离格兰赛尔城很近呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F2B")

    Jump("loc_104C")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_F38")
    Jump("loc_104C")

    label("loc_F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_104C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FC8")

    ChrTalk(    #15
        0xFE,
        (
            "都把女儿的名字\x01",
            "当店名使了，\x01",
            "是不是本来就打算给她继承的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "而且她似乎干得\x01",
            "并不比她老爸差。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "这也是遗传吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_104C")

    label("loc_FC8")


    ChrTalk(    #18
        0xFE,
        (
            "之前百货店的老板换了，\x01",
            "你知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "那家店，\x01",
            "据说由女儿继承了。\x02",
        )
    )

    Jump("loc_101F")

    label("loc_101F")

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "虽然还很年轻，\x01",
            "但似乎相当能干呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_104C")

    TalkEnd(0xFE)
    Return()

    # Function_12_DC2 end

    def Function_13_1050(): pass

    label("Function_13_1050")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_105D")
    Jump("loc_121F")

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_10B0")

    ChrTalk(    #21
        0xFE,
        "是叫什么名字的鱼来着……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "嗯，好像是『什么鲶』吧？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_113D")

    label("loc_10B0")


    ChrTalk(    #23
        0xFE,
        (
            "刚才和那边\x01",
            "正在搬东西的人聊了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "唔，是钓公师团的人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "居然说帝国大使\x01",
            "长着像鱼一样的脸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "……这是夸奖吗？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_113D")

    Jump("loc_121F")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_114A")
    Jump("loc_121F")

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_11C3")

    ChrTalk(    #27
        0xFE,
        (
            "之前我见到帝国的大使了。\x01",
            "他一直带着一副不高兴的表情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "帝国的人\x01",
            "都是那样的吗。\x02",
        )
    )

    Jump("loc_11BF")

    label("loc_11BF")

    CloseMessageWindow()
    Jump("loc_121F")

    label("loc_11C3")


    ChrTalk(    #29
        0xFE,
        "之前我见到帝国的大使了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "我国和帝国之间发生过很多事，\x01",
            "感觉真是有点复杂呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_121F")

    TalkEnd(0xFE)
    Return()

    # Function_13_1050 end

    def Function_14_1223(): pass

    label("Function_14_1223")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1230")
    Jump("loc_13EB")

    label("loc_1230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_132D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_12B8")

    ChrTalk(    #31
        0xFE,
        (
            "据说那位霍尔登先生\x01",
            "已经去世了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "在我们那一代\x01",
            "他可是时代的宠儿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "听到这消息，\x01",
            "真是感觉自己老了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132A")

    label("loc_12B8")


    ChrTalk(    #34
        0xFE,
        "读了利贝尔通讯真是大吃一惊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "据说那位霍尔登先生\x01",
            "已经去世了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "哎呀呀，我也上年纪了呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_132A")

    Jump("loc_13EB")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1337")
    Jump("loc_13EB")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_13EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_139C")

    ChrTalk(    #37
        0xFE,
        (
            "利贝尔通讯出版社\x01",
            "就在西街区呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "对格兰赛尔市民来说\x01",
            "是很熟悉的媒体了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EB")

    label("loc_139C")


    ChrTalk(    #39
        0xFE,
        (
            "啊啊，\x01",
            "今天是利贝尔通讯的发售日呢。\x02",
        )
    )

    Jump("loc_13CF")

    label("loc_13CF")

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "稍后要去买才行。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_13EB")

    TalkEnd(0xFE)
    Return()

    # Function_14_1223 end

    def Function_15_13EF(): pass

    label("Function_15_13EF")

    TalkBegin(0xFE)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1404")
    Jump("loc_1541")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1481")

    ChrTalk(    #41
        0x18,
        "不过啊～…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x18,
        (
            "大姐头正在工作，\x01",
            "想不想去偷看一下？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x17,
        "啊，也许吧～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x17,
        "现在去吗？　去吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1541")

    label("loc_1481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_148B")
    Jump("loc_1541")

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1541")

    ChrTalk(    #45
        0x17,
        (
            "大姐她啊～，\x01",
            "在百货店工作呢～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x17,
        "什么～？　艾德尔百货店？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x17,
        (
            "感觉真是\x01",
            "难以接近啊～。\x02",
        )
    )

    Jump("loc_1503")

    label("loc_1503")

    CloseMessageWindow()

    ChrTalk(    #48
        0x18,
        "啊～，那不好啦～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x18,
        (
            "因为啊～，\x01",
            "会被爸妈发现吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1541")

    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    TalkEnd(0xFE)
    Return()

    # Function_15_13EF end

    def Function_16_154D(): pass

    label("Function_16_154D")

    Call(0, 15)
    Return()

    # Function_16_154D end

    def Function_17_1552(): pass

    label("Function_17_1552")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_155F")
    Jump("loc_1715")

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_15DB")

    ChrTalk(    #50
        0xFE,
        (
            "因为觉得稀奇，\x01",
            "所以乘了好多次飞艇，\x01",
            "这样不好吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "可是，说到利贝尔，\x01",
            "就不得不提到飞艇公社吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1664")

    label("loc_15DB")


    ChrTalk(    #52
        0xFE,
        (
            "我从卡尔瓦德艺术学院毕业以后\x01",
            "就在大陆上到处旅行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "本着增长见识的打算。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "但是钱用光之后，\x01",
            "就被困在这个国家了～。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1664")

    Jump("loc_1715")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1671")
    Jump("loc_1715")

    label("loc_1671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_16CC")

    ChrTalk(    #55
        0xFE,
        (
            "来来，别客气，\x01",
            "尽管来看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "就当是助人为乐，\x01",
            "来买点东西吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1715")

    label("loc_16CC")


    ChrTalk(    #57
        0xFE,
        (
            "呀，欢迎光临。\x01",
            "要买糖果吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "来来，别客气，\x01",
            "尽管来看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1715")

    TalkEnd(0xFE)
    Return()

    # Function_17_1552 end

    def Function_18_1719(): pass

    label("Function_18_1719")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1726")
    Jump("loc_17CE")

    label("loc_1726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1730")
    Jump("loc_17CE")

    label("loc_1730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_173A")
    Jump("loc_17CE")

    label("loc_173A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_17CE")
    OP_8C(0x1E, 135, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1788")

    ChrTalk(    #59
        0xFE,
        "这里就是钓公师团吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "我也能入团吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_17CE")

    label("loc_1788")


    ChrTalk(    #61
        0xFE,
        "这、这里就是钓公师团吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "到底怎么做\x01",
            "才能入团呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_17CE")

    TalkEnd(0xFE)
    Return()

    # Function_18_1719 end

    def Function_19_17D2(): pass

    label("Function_19_17D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_17DF")
    Jump("loc_19CC")

    label("loc_17DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_187C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1832")

    ChrTalk(    #63
        0xFE,
        "这个箱子，真是重得过分啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "…………是故意整人的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1879")

    label("loc_1832")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #65
        0xFE,
        "好啦好啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "好、好重。\x01",
            "到底装了什么啊，这里面？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_1879")

    Jump("loc_19CC")

    label("loc_187C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1886")
    Jump("loc_19CC")

    label("loc_1886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_19CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1917")

    ChrTalk(    #67
        0xFE,
        "啊，搬东西好麻烦啊～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "要不要再去申请个委托呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x103,
        (
            "#1645F你们啊，这是本职工作吧？\x02\x03",

            "#1645F别偷懒，好好干啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19CC")

    label("loc_1917")


    ChrTalk(    #70
        0xFE,
        (
            "呀，\x01",
            "这不是刚才的游击士吗？\x02",
        )
    )

    Jump("loc_193F")

    label("loc_193F")

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "能不能帮个忙？\x01",
            "帮帮忙啦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#1646F我的工作\x01",
            "就是把东西搬下来而已吧。\x02\x03",

            "委托已经完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "怎么这样～……\x01",
            "好冷淡啊～。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_19CC")

    TalkEnd(0xFE)
    Return()

    # Function_19_17D2 end

    def Function_20_19D0(): pass

    label("Function_20_19D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_19DD")
    Jump("loc_1BB9")

    label("loc_19DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1A46")

    ChrTalk(    #74
        0xFE,
        "现在有点人手不足啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "怎样，要不要来我们这里？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        "#1646F……没兴趣啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ACE")

    label("loc_1A46")


    ChrTalk(    #77
        0xFE,
        "要转职就来我们这里哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "现在我们正人手不足呢。\x01",
            "热烈欢迎！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        (
            "#1646F我们游击士协会才人手不足呢。\x02\x03",

            "这种劝诱我拒绝。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_1ACE")

    Jump("loc_1BB9")

    label("loc_1AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1ADB")
    Jump("loc_1BB9")

    label("loc_1ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1B54")

    ChrTalk(    #80
        0xFE,
        "哟，游击士小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "也给我们的年轻人\x01",
            "增加点动力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        (
            "#1642F……别把这种事情\x01",
            "推给我啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB9")

    label("loc_1B54")


    ChrTalk(    #83
        0xFE,
        (
            "哟，\x01",
            "这不是游击士小姐吗。\x02",
        )
    )

    Jump("loc_1B7A")

    label("loc_1B7A")

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "你啊，很有毅力嘛。\x01",
            "真是佩服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x103,
        "#1640F多谢了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_1BB9")

    TalkEnd(0xFE)
    Return()

    # Function_20_19D0 end

    def Function_21_1BBD(): pass

    label("Function_21_1BBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -5720, 0, -36280, 270)
    OP_43(0x13, 0x0, 0x0, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 5760, 0, -46060, 270)
    OP_43(0x14, 0x0, 0x0, 0x3)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -2070, 0, -5120, 180)
    OP_43(0x15, 0x0, 0x0, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 3520, 0, 10640, 180)
    OP_43(0x16, 0x0, 0x0, 0x5)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    OP_43(0x1E, 0x0, 0x0, 0x17)
    OP_43(0x1F, 0x0, 0x0, 0x18)
    OP_6D(0, -3750, -42620, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3590, 0)
    OP_6C(0, 0)
    OP_6E(590, 0)

    def lambda_1CA7():
        OP_6D(0, -5750, 630, 9000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1CA7)

    def lambda_1CBF():
        OP_67(0, 10940, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1CBF)

    def lambda_1CD7():
        OP_6B(3500, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1CD7)

    def lambda_1CE7():
        OP_6C(0, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1CE7)

    def lambda_1CF7():
        OP_6E(590, 9000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1CF7)
    OP_43(0x1B, 0x0, 0x0, 0x16)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_21_1BBD end

    def Function_22_1D31(): pass

    label("Function_22_1D31")

    Sleep(500)
    OP_62(0x1B, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x1B)
    OP_62(0x1C, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    OP_62(0x1D, 0x0, 1600, 0x0, 0x1, 0xC8, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    OP_63(0x1D)
    Return()

    # Function_22_1D31 end

    def Function_23_1D80(): pass

    label("Function_23_1D80")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 11280, 750, -25090, 270)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3B)
    OP_23(0x6)
    OP_73(0x6)
    OP_8E(0xFE, 0x1FC2, 0xFA, 0xFFFF9F0C, 0x7D0, 0x0)
    OP_6F(0x6, 59)
    OP_70(0x6, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x2026, 0xFA, 0xFFFFCD9C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x256C, 0x1F4, 0xFFFFCD88, 0x7D0, 0x0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    OP_8E(0xFE, 0x2CD8, 0x2EE, 0xFFFFCD9C, 0x7D0, 0x0)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_23_1D80 end

    def Function_24_1E4C(): pass

    label("Function_24_1E4C")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -11710, 0, -19530, 90)
    OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0xFFFFB3B6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x1CB6, 0x7D0, 0x0)
    Return()

    # Function_24_1E4C end

    def Function_25_1E92(): pass

    label("Function_25_1E92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, -14500, 750, -2340, 90)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x00#40W五年前――#20W\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(1650, 5600, -50220, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(339000, 0)
    OP_6E(511, 0)
    OP_1D(0xE)
    FadeToBright(2000, 0)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x7D0)

    def lambda_1F5F():
        OP_6D(-9650, 4500, -5440, 10000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_1F5F)

    def lambda_1F77():
        OP_67(0, 6200, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1F77)

    def lambda_1F8F():
        OP_6B(3100, 10000)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_1F8F)

    def lambda_1F9F():
        OP_6C(311000, 10000)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_1F9F)

    def lambda_1FAF():
        OP_6E(511, 10000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FAF)
    WaitChrThread(0x29, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-14800, 250, -900, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(311000, 0)
    OP_6E(262, 0)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    Sleep(1000)
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_70(0x4, 0x3B)
    OP_73(0x4)

    def lambda_2028():
        OP_6D(-10820, 250, -1900, 2300)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_2028)

    def lambda_2040():
        OP_6C(322000, 2300)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_2040)

    def lambda_2050():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2050)

    def lambda_2062():
        OP_8E(0xFE, 0xFFFFD828, 0xFA, 0xFFFFF574, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2062)
    Sleep(1500)
    OP_72(0x4, 0x8)
    ExitThread()
    OP_6F(0x4, 59)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x4, 0x0)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #87
        0x103,
        (
            "#1645F呼，\x01",
            "这么大的地方送货也不轻松啊。\x02\x03",

            "唔～下一个是…………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)
    Sleep(300)
    OP_22(0x12, 0x0, 0x5A)
    Sleep(500)

    ChrTalk(    #88
        0x103,
        (
            "#1643F呃，艾尔贝离宫！？\x01",
            "要去那么远的地方啊？\x02\x03",

            "#1645F呜……大城市\x01",
            "就是这点讨厌啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 140, 500)
    Sleep(300)

    def lambda_2182():
        OP_8E(0xFE, 0xFFFFEACA, 0x0, 0xFFFFDDA0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2182)
    WaitChrThread(0x103, 0x1)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_A1(0x28, 0x1F)
    SetChrPos(0x28, 7400, 250, -25740, 0)
    SetChrPos(0x16, 5860, 0, -19380, 0)
    SetChrPos(0x15, -2000, 0, -22540, 0)

    def lambda_21E2():
        OP_8E(0xFE, 0x16BC, 0x0, 0xFFFFE250, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_21E2)
    Sleep(100)

    def lambda_2202():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0xFFFFCC0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2202)
    Fade(1000)
    OP_6D(4480, 0, -13440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x11, 7780, 250, -24540, 180)
    SetChrPos(0x12, 8480, 250, -25940, 270)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 59)
    SetChrPos(0x103, 4480, 0, -2140, 180)

    def lambda_22A9():
        OP_8E(0xFE, 0x1180, 0x0, 0xFFFF955C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22A9)
    Sleep(1000)

    def lambda_22C9():
        OP_6D(5780, 0, -25540, 4000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_22C9)

    def lambda_22E1():
        OP_67(0, 6860, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_22E1)

    def lambda_22F9():
        OP_6B(3080, 4000)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_22F9)

    def lambda_2309():
        OP_6C(30000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_2309)
    Sleep(3800)

    def lambda_231E():

        label("loc_231E")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_231E")

    QueueWorkItem2(0x11, 2, lambda_231E)

    def lambda_232F():

        label("loc_232F")

        TurnDirection(0xFE, 0x103, 0)
        OP_48()
        Jump("loc_232F")

    QueueWorkItem2(0x12, 2, lambda_232F)

    ChrTalk(    #89
        0x11,
        (
            "呀，\x01",
            "这不是刚才的游击士吗。\x02",
        )
    )

    Jump("loc_2367")

    label("loc_2367")

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x29, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2840, 0, -37340, 0)

    def lambda_238E():
        OP_8E(0xFE, 0xB18, 0x0, 0xFFFFBFC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_238E)
    Sleep(300)

    def lambda_23AE():
        OP_6D(7780, 0, -24520, 1500)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_23AE)

    def lambda_23C6():
        OP_67(0, 5900, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_23C6)
    TurnDirection(0x103, 0x12, 500)
    WaitChrThread(0x29, 0x0)
    OP_44(0x16, 0xFF)
    OP_44(0x15, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x80)
    Sleep(300)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #90
        0x11,
        (
            "多亏你帮忙了。\x01",
            "你还真有力气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x12,
        (
            "#2P怎样，要不要来我们这里。\x01",
            "如果是你的话随时欢迎哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        (
            "#1646F……抱歉，我没兴趣。\x02\x03",

            "#1642F我还有急事呢。\x01",
            "再见了！\x02",
        )
    )

    Jump("loc_24C9")

    label("loc_24C9")

    CloseMessageWindow()
    OP_8C(0x103, 180, 500)
    Sleep(200)

    def lambda_24DC():
        OP_8E(0xFE, 0x1180, 0x0, 0xFFFF6E4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_24DC)
    Sleep(2000)
    WaitChrThread(0x10, 0x1)
    SetChrPos(0x10, 8460, 250, -13000, 90)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_2524():
        OP_6D(11060, 750, -13000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_2524)

    def lambda_253C():
        OP_67(0, 6760, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_253C)

    def lambda_2554():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_2554)

    def lambda_2564():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_2564)
    WaitChrThread(0x29, 0x1)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    def lambda_2586():
        OP_8E(0xFE, 0x2580, 0x1F4, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2586)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #93
        0x10,
        "女性",
        "#1650F那个…………\x02",
    )

    Jump("loc_25D8")

    label("loc_25D8")

    CloseMessageWindow()

    def lambda_25DF():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_25DF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_1E92 end

    def Function_26_2601(): pass

    label("Function_26_2601")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, 11500, 750, -13000, 270)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 11500, 750, -13000, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(8920, 500, -12780, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1, 0x8)
    ExitThread()
    OP_22(0x6, 0x0, 0x64)
    OP_70(0x1, 0x3B)
    OP_73(0x1)

    def lambda_26B9():
        OP_8E(0xFE, 0x1B30, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_26B9)

    def lambda_26D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_26D4)
    Sleep(2000)

    def lambda_26EB():
        OP_8E(0xFE, 0x25E4, 0x1F4, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26EB)

    def lambda_2706():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2706)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 400)
    Sleep(500)
    OP_6F(0x1, 59)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    Sleep(500)

    ChrTalk(    #94
        0x103,
        (
            "#1645F（……唉，\x01",
            "  为什么我要当这家伙的保镖……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10,
        (
            "#1653F对不起。\x01",
            "还是给你添麻烦了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)
    Sleep(300)

    def lambda_27CC():
        OP_8E(0xFE, 0x2134, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27CC)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #96
        0x103,
        (
            "#1646F#2P没事啦，真是的。\x02\x03",

            "（啊啊啊，\x01",
            "  这种做作的口气\x01",
            "  真是听了就烦人……）\x02\x03",

            "#1642F那么？　你要去哪里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "#1654F对了……\x02\x03",

            "保险起见，\x01",
            "先去艾德尔百货店买点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x103,
        "#1643F#2P……保险起见？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "#1650F艾德尔百货店在东街区。\x01",
            "没弄错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        (
            "#1648F#2P没错。\x02\x03",

            "（啊啊，\x01",
            "  真是烦人啊……！）\x02",
        )
    )

    Jump("loc_2961")

    label("loc_2961")

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    AddParty(0x50, 0xFF, 0xFF)
    SetChrPos(0x151, 7180, 250, -13000, 90)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x8)
    ExitThread()
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_A2(0x2F4A)
    OP_1B(0xB, 0x0, 0x1C)
    OP_1B(0xC, 0x0, 0x1D)
    OP_1B(0xD, 0x0, 0x1E)
    OP_1B(0xE, 0x0, 0x1F)
    OP_1B(0x9, 0x0, 0x21)
    OP_B2(0x1, 0x0, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x24, 0, 0, -64099, 180)
    SetChrPos(0x25, -1000, 0, -65800, 45)
    SetChrPos(0x26, 1000, 0, -65800, 315)
    OP_43(0x24, 0x0, 0x0, 0x2)
    OP_43(0x25, 0x0, 0x0, 0x2)
    OP_43(0x26, 0x0, 0x0, 0x2)
    OP_43(0x24, 0x3, 0x0, 0x9)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 7140, 250, -23020, 135)
    OP_41(0x2, 0x0, 0xFF)
    OP_31(0x2, 0x10, 0xA)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x2, 0x5, 0x0)
    OP_35(0x2, 0xFFFF)
    OP_34(0x2, 0xFFFF)
    OP_35(0x2, 0x0)
    OP_37(0x2, 0x7F, 0x0)
    OP_37(0x2, 0x7F, 0x0)
    OP_BB(0x2, 0x6, 0x0)
    OP_41(0x2, 0x44E, 0xFF)
    OP_41(0x2, 0x63F, 0xFF)
    OP_41(0x2, 0x7F, 0xFF)
    OP_3E(0x203, 3)
    EventEnd(0x0)
    Return()

    # Function_26_2601 end

    def Function_27_2A71(): pass

    label("Function_27_2A71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, 11500, 750, -13000, 270)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x151, 11500, 750, -13000, 270)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x151, 0x40)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(8920, 500, -12780, 0)
    OP_67(0, 8540, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1, 0x8)
    ExitThread()
    OP_22(0x6, 0x0, 0x64)
    OP_70(0x1, 0x3B)
    OP_73(0x1)

    def lambda_2B24():
        OP_8E(0xFE, 0x1BBC, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B24)

    def lambda_2B3F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2B3F)
    Sleep(1500)

    def lambda_2B56():
        OP_8E(0xFE, 0x2134, 0xFA, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2B56)

    def lambda_2B71():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_2B71)
    Sleep(1000)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #101
        0x103,
        (
            "#1646F好了…………\x02\x03",

            "#1641F赶快解决吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x151,
        (
            "\x07\x00#1650F#2P那个，雪拉扎德小姐。\x01",
            "『老师』是指……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(300)

    ChrTalk(    #103
        0x103,
        (
            "#1645F啊～\x01",
            "你别多管闲事。\x02\x03",

            "好啦，要去酒店对吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x151,
        "#1650F#2P嗯、嗯嗯…………\x02",
    )

    CloseMessageWindow()
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    ClearChrFlags(0x151, 0x40)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x8)
    ExitThread()
    EventEnd(0x0)
    Return()

    # Function_27_2A71 end

    def Function_28_2CB4(): pass

    label("Function_28_2CB4")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, -8800, 250, 13160, 180)
    SetChrPos(0x151, -8800, 250, 13160, 180)
    OP_6D(-8800, 250, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_28_2CB4 end

    def Function_29_2CFC(): pass

    label("Function_29_2CFC")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, -3600, 0, 13160, 180)
    SetChrPos(0x151, -3600, 0, 13160, 180)
    OP_6D(-3600, 0, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_29_2CFC end

    def Function_30_2D44(): pass

    label("Function_30_2D44")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, 8800, 250, 13160, 180)
    SetChrPos(0x151, 8800, 250, 13160, 180)
    OP_6D(8800, 250, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_30_2D44 end

    def Function_31_2D8C(): pass

    label("Function_31_2D8C")

    EventBegin(0x2)
    Call(0, 32)
    OP_59()
    Fade(1000)
    SetChrPos(0x103, 3600, 0, 13160, 180)
    SetChrPos(0x151, 3600, 0, 13160, 180)
    OP_6D(3600, 0, 9000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_31_2D8C end

    def Function_32_2DD4(): pass

    label("Function_32_2DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2DDE")
    Jump("loc_3657")

    label("loc_2DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_2DE8")
    Jump("loc_3657")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2DF2")
    Jump("loc_3657")

    label("loc_2DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_3657")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_302D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2F02")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #105
        0x151,
        (
            "#1650F#6P从这边走\x01",
            "好像绕远路了。\x02\x03",

            "#1651F我们从协会前面的路\x01",
            "往右拐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x103,
        (
            "#1646F#6P…………………………\x02\x03",

            "（刚才明明还说是\x01",
            "  第一次来王都，\x01",
            "  这不是很了解情况吗…………）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302A")

    label("loc_2F02")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #107
        0x151,
        (
            "#1653F#6P……雪拉扎德小姐，\x01",
            "艾德尔百货店\x01",
            "不在这边哦。\x02\x03",

            "记得是在东街区，\x01",
            "我们应该从协会前面的路往右拐。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #108
        0x103,
        "#1642F#6P从这条路也能走啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x151,
        (
            "#1654F#6P…………但是……\x02\x03",

            "#1651F会绕远路的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        "#1646F#6P…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_302A")

    Jump("loc_3657")

    label("loc_302D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3246")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3121")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #111
        0x151,
        (
            "#1650F从这边走\x01",
            "好像绕远路了。\x02\x03",

            "#1651F我们从协会前面的路\x01",
            "往右拐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#1646F#4P…………………………\x02\x03",

            "（刚才明明还说是\x01",
            "  第一次来王都，\x01",
            "  这不是很了解情况吗…………）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3243")

    label("loc_3121")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #113
        0x151,
        (
            "#1653F……雪拉扎德小姐，\x01",
            "艾德尔百货店\x01",
            "不在这边哦。\x02\x03",

            "记得是在东街区，\x01",
            "我们应该从协会前面的路往右拐。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #114
        0x103,
        "#1642F#4P从这条路也能走啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x151,
        (
            "#1654F…………但是……\x02\x03",

            "#1651F会绕远路的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        "#1646F#4P…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3243")

    Jump("loc_3657")

    label("loc_3246")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_345F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_333A")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #117
        0x151,
        (
            "#1650F从这边走\x01",
            "好像绕远路了。\x02\x03",

            "#1651F我们从协会前面的路\x01",
            "往右拐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#1646F#3P…………………………\x02\x03",

            "（刚才明明还说是\x01",
            "  第一次来王都，\x01",
            "  这不是很了解情况吗…………）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345C")

    label("loc_333A")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #119
        0x151,
        (
            "#1653F……雪拉扎德小姐，\x01",
            "艾德尔百货店\x01",
            "不在这边哦。\x02\x03",

            "记得是在东街区，\x01",
            "我们应该从协会前面的路往右拐。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #120
        0x103,
        "#1642F#3P从这条路也能走啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x151,
        (
            "#1654F…………但是……\x02\x03",

            "#1651F会绕远路的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        "#1646F#3P…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_345C")

    Jump("loc_3657")

    label("loc_345F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_353B")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #123
        0x151,
        (
            "#1650F从这边走\x01",
            "好像绕远路了。\x02\x03",

            "#1651F我们从协会前面的路\x01",
            "往右拐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#1646F…………………………\x02\x03",

            "（刚才明明还说是\x01",
            "  第一次来王都，\x01",
            "  这不是很了解情况吗…………）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3657")

    label("loc_353B")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #125
        0x151,
        (
            "#1653F……雪拉扎德小姐，\x01",
            "艾德尔百货店\x01",
            "不在这边哦。\x02\x03",

            "记得是在东街区，\x01",
            "我们应该从协会前面的路往右拐。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #126
        0x103,
        "#1642F从这条路也能走啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x151,
        (
            "#1654F…………但是……\x02\x03",

            "#1651F会绕远路的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#1646F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3657")

    Return()

    # Function_32_2DD4 end

    def Function_33_3658(): pass

    label("Function_33_3658")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_3664")
    Jump("loc_3918")

    label("loc_3664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_37D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3727")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #129
        0x151,
        (
            "#1656F雪拉扎德小姐，\x01",
            "不是这边哦。\x02\x03",

            "#1650F应该是往回走一点，\x01",
            "再往左拐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x103,
        (
            "#1648F（从刚才起就是这个样子。）\x02\x03",

            "（啊啊，好烦人……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_3727")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #131
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "不是这边哦。\x02\x03",

            "#1650F酒店在北街区哦。\x02\x03",

            "应该是往回走一点，\x01",
            "再往左拐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        "#1642F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_37D2")

    Jump("loc_3918")

    label("loc_37D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_37DF")
    Jump("loc_3918")

    label("loc_37DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_3918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3852")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #133
        0x151,
        "#1651F雪拉扎德小姐，方向走反了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x103,
        "#1646F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3918")

    label("loc_3852")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #135
        0x151,
        (
            "#1653F……雪拉扎德小姐，\x01",
            "这边是西街区哦。\x02\x03",

            "艾德尔百货店\x01",
            "在东街区………\x02\x03",

            "#1651F……方向走反了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #136
        0x103,
        (
            "#1646F……只、只是\x01",
            "一时搞错而已啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3918")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_33_3658 end

    def Function_34_3934(): pass

    label("Function_34_3934")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_3940")
    Jump("loc_3BF9")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_3A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A01")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #137
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "你去哪边？\x02\x03",

            "这边可是通向王都外面哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        (
            "#1646F（啊啊，好烦人……）\x02\x03",

            "#1647F（这大小姐\x01",
            "  每件事都自以为是！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A80")

    label("loc_3A01")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #139
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "你去哪边？\x02\x03",

            "这边可是王都外面哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        "#1646F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3A80")

    Jump("loc_3BF9")

    label("loc_3A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_3A8D")
    Jump("loc_3BF9")

    label("loc_3A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_3BF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B2A")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #141
        0x151,
        (
            "#1650F艾德尔百货店在东街区，\x01",
            "所以要走协会前面的路再往右……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #142
        0x103,
        (
            "#1642F我知道啦。\x01",
            "真是烦人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BF9")

    label("loc_3B2A")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #143
        0x151,
        (
            "#1652F……雪拉扎德小姐………#1600W \x01",
            "#20W#1651F这边是格兰赛尔外面哦？\x02\x03",

            "艾德尔百货店在东街区，\x01",
            "所以要走协会前面的路再往右拐才对。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x151, 500)
    Sleep(200)

    ChrTalk(    #144
        0x103,
        "#1642F我、我知道啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3BF9")

    OP_59()
    Fade(1000)
    SetChrPos(0x103, 0, 0, -58800, 0)
    SetChrPos(0x151, 0, 0, -58800, 0)
    OP_6D(0, 0, -58800, 0)
    Sleep(1000)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_3934 end

    def Function_35_3C3F(): pass

    label("Function_35_3C3F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #145
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    SetMapFlags(0x2000000)
    Return()

    # Function_35_3C3F end

    def Function_36_3C7A(): pass

    label("Function_36_3C7A")

    SetPlaceName(0xB9)
    Return()

    # Function_36_3C7A end

    def Function_37_3C7E(): pass

    label("Function_37_3C7E")

    SetPlaceName(0xB0)
    Return()

    # Function_37_3C7E end

    def Function_38_3C82(): pass

    label("Function_38_3C82")

    SetPlaceName(0xB2)
    Return()

    # Function_38_3C82 end

    def Function_39_3C86(): pass

    label("Function_39_3C86")

    SetPlaceName(0xAE)
    Return()

    # Function_39_3C86 end

    def Function_40_3C8A(): pass

    label("Function_40_3C8A")

    SetPlaceName(0xB3)
    Return()

    # Function_40_3C8A end

    SaveToFile()

Try(main)
