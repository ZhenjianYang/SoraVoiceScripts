from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4103.x',
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
        '黑衣人',                               # 9
        '黑衣人',                               # 10
        '黑衣人',                               # 11
        '黑衣人',                               # 12
        '黑衣人',                               # 13
        '黑衣人',                               # 14
        '黑衣人',                               # 15
        '黑衣人',                               # 16
        '黑衣人',                               # 17
        '黑衣人',                               # 18
        '克鲁茨',                               # 19
        '冈多夫',                               # 20
        '猫',                                   # 21
        '奈尔',                                 # 22
        '朵洛希',                               # 23
        '诺雅尔',                               # 24
        '维基奥',                               # 25
        '巴鲁托',                               # 26
        '箱子',                                 # 27
        '女性',                                 # 28
        '女性',                                 # 29
        '女性',                                 # 30
        '卡兰大主教',                           # 31
        '穆拉少校',                             # 32
        '王都格兰赛尔·西街区',                 # 33
        '格兰赛尔城',                           # 34
        '王都格兰赛尔·东街区',                 # 35
        '王都格兰赛尔·南街区',                 # 36
        '目标用照相机',                         # 37
        '',                                     # 38
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
        'ED6_DT27/CH03460 ._CH',             # 00
        'ED6_DT07/CH01620 ._CH',             # 01
        'ED6_DT26/CH20682 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH02720 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT26/CH20618 ._CH',             # 09
        'ED6_DT27/CH04230 ._CH',             # 0A
        'ED6_DT27/CH04232 ._CH',             # 0B
        'ED6_DT27/CH04234 ._CH',             # 0C
        'ED6_DT27/CH04231 ._CH',             # 0D
        'ED6_DT27/CH04464 ._CH',             # 0E
        'ED6_DT27/CH04463 ._CH',             # 0F
        'ED6_DT07/CH01410 ._CH',             # 10
        'ED6_DT07/CH01400 ._CH',             # 11
        'ED6_DT27/CH03570 ._CH',             # 12
        'ED6_DT07/CH01030 ._CH',             # 13
        'ED6_DT07/CH01130 ._CH',             # 14
        'ED6_DT07/CH01170 ._CH',             # 15
        'ED6_DT26/CH20686 ._CH',             # 16
        'ED6_DT26/CH20681 ._CH',             # 17
        'ED6_DT27/CH04462 ._CH',             # 18
        'ED6_DT27/CH04460 ._CH',             # 19
        'ED6_DT27/CH04461 ._CH',             # 1A
        'ED6_DT26/CH20680 ._CH',             # 1B
        'ED6_DT27/CH03420 ._CH',             # 1C
        'ED6_DT26/CH20684 ._CH',             # 1D
        'ED6_DT26/CH20684 ._CH',             # 1E
        'ED6_DT07/CH00410 ._CH',             # 1F
        'ED6_DT07/CH00411 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT27/CH03460P._CP',             # 00
        'ED6_DT07/CH01620P._CP',             # 01
        'ED6_DT26/CH20682P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH02720P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT26/CH20618P._CP',             # 09
        'ED6_DT27/CH04230P._CP',             # 0A
        'ED6_DT27/CH04232P._CP',             # 0B
        'ED6_DT27/CH04234P._CP',             # 0C
        'ED6_DT27/CH04231P._CP',             # 0D
        'ED6_DT27/CH04464P._CP',             # 0E
        'ED6_DT27/CH04463P._CP',             # 0F
        'ED6_DT07/CH01410P._CP',             # 10
        'ED6_DT07/CH01400P._CP',             # 11
        'ED6_DT27/CH03570P._CP',             # 12
        'ED6_DT07/CH01030P._CP',             # 13
        'ED6_DT07/CH01130P._CP',             # 14
        'ED6_DT07/CH01170P._CP',             # 15
        'ED6_DT26/CH20686P._CP',             # 16
        'ED6_DT26/CH20681P._CP',             # 17
        'ED6_DT27/CH04462P._CP',             # 18
        'ED6_DT27/CH04460P._CP',             # 19
        'ED6_DT27/CH04461P._CP',             # 1A
        'ED6_DT26/CH20680P._CP',             # 1B
        'ED6_DT27/CH03420P._CP',             # 1C
        'ED6_DT26/CH20684P._CP',             # 1D
        'ED6_DT26/CH20684P._CP',             # 1E
        'ED6_DT07/CH00410P._CP',             # 1F
        'ED6_DT07/CH00411P._CP',             # 20
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = -3000,
        Y                   = 0,
        Z                   = 70200,
        Range               = 2000,
        Unknown_10          = 0x1D4C,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 3000,
        Y                   = 0,
        Z                   = 70200,
        Range               = 2000,
        Unknown_10          = 0x1D4C,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 16560,
        Y                   = 0,
        Z                   = 70500,
        Range               = 18000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xD6D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = -35600,
        Y                   = 0,
        Z                   = 54000,
        Range               = -33600,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xB1BC,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )


    ScpFunction(
        "Function_0_5F2",          # 00, 0
        "Function_1_74B",          # 01, 1
        "Function_2_7D7",          # 02, 2
        "Function_3_7ED",          # 03, 3
        "Function_4_833",          # 04, 4
        "Function_5_A6C",          # 05, 5
        "Function_6_AC6",          # 06, 6
        "Function_7_B5D",          # 07, 7
        "Function_8_C64",          # 08, 8
        "Function_9_C88",          # 09, 9
        "Function_10_DA5",         # 0A, 10
        "Function_11_E6B",         # 0B, 11
        "Function_12_F98",         # 0C, 12
        "Function_13_172D",        # 0D, 13
        "Function_14_2262",        # 0E, 14
        "Function_15_2294",        # 0F, 15
        "Function_16_2301",        # 10, 16
        "Function_17_2332",        # 11, 17
        "Function_18_2CF9",        # 12, 18
        "Function_19_2D60",        # 13, 19
        "Function_20_2DDF",        # 14, 20
        "Function_21_417A",        # 15, 21
        "Function_22_4BB1",        # 16, 22
        "Function_23_4BD9",        # 17, 23
        "Function_24_4C0B",        # 18, 24
        "Function_25_4C62",        # 19, 25
        "Function_26_4CA5",        # 1A, 26
        "Function_27_4CBE",        # 1B, 27
        "Function_28_4CDC",        # 1C, 28
        "Function_29_4DCC",        # 1D, 29
        "Function_30_4EBC",        # 1E, 30
        "Function_31_4FAC",        # 1F, 31
        "Function_32_509C",        # 20, 32
        "Function_33_5924",        # 21, 33
        "Function_34_5989",        # 22, 34
        "Function_35_5A1C",        # 23, 35
        "Function_36_6B0C",        # 24, 36
        "Function_37_6B10",        # 25, 37
        "Function_38_6B58",        # 26, 38
        "Function_39_6BBE",        # 27, 39
    )


    def Function_0_5F2(): pass

    label("Function_0_5F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_6EC")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x10, -4660, 0, 68440, 180)
    SetChrPos(0x11, -1500, 0, 68440, 180)
    SetChrPos(0x12, -3080, 0, 68080, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x13, 4660, 0, 68440, 180)
    SetChrPos(0x14, 1500, 0, 68440, 180)
    SetChrPos(0x15, 3080, 0, 68080, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 27400, 0, 65260, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 27400, 0, 63660, 270)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 25020, 0, 64500, 90)
    Jump("loc_707")

    label("loc_6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_6F6")
    Jump("loc_707")

    label("loc_6F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_700")
    Jump("loc_707")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_707")

    label("loc_707")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_72B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_72B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_74A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_74A")

    Return()

    # Function_0_5F2 end

    def Function_1_74B(): pass

    label("Function_1_74B")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_772")

    OP_B1("T4103_n")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    OP_B2(0x0, 0x4, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7D6")
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_B2(0x1, 0x3, 0x80)
    OP_B2(0x1, 0x4, 0x80)
    OP_1B(0x0, 0x0, 0x1C)
    OP_1B(0x1, 0x0, 0x1D)
    OP_1B(0x2, 0x0, 0x1F)
    OP_1B(0x3, 0x0, 0x1E)

    label("loc_7D6")

    Return()

    # Function_1_74B end

    def Function_2_7D7(): pass

    label("Function_2_7D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7EC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7D7")

    label("loc_7EC")

    Return()

    # Function_2_7D7 end

    def Function_3_7ED(): pass

    label("Function_3_7ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_832")
    SetChrPos(0xFE, 31870, 0, 62180, 270)
    OP_8E(0xFE, 0x1324, 0x0, 0xF2E4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1324, 0x0, 0x40CE, 0x7D0, 0x0)
    Jump("Function_3_7ED")

    label("loc_832")

    Return()

    # Function_3_7ED end

    def Function_4_833(): pass

    label("Function_4_833")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6B")
    SetChrPos(0xFE, -40860, 0, 28340, 0)
    OP_8E(0xFE, 0xFFFF6064, 0x0, 0xBAE0, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF624E, 0x0, 0xC422, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFF9F48, 0xFA, 0xF1F4, 0x2328, 0x0)
    OP_8C(0xFE, 0, 800)
    Sleep(400)
    OP_8E(0xFE, 0xFFFFA33A, 0xFA, 0xE9DE, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFA33A, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFE674, 0x0, 0xC5F8, 0x2328, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xCED6, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFECDC, 0x0, 0xF276, 0x2328, 0x0)
    OP_8E(0xFE, 0xFFFFF16E, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x3070, 0x0, 0xFD84, 0x2328, 0x0)
    OP_8E(0xFE, 0x37F0, 0x0, 0xF604, 0x2328, 0x0)
    OP_8E(0xFE, 0x9B8C, 0x0, 0xF604, 0x2328, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 39650, 0, 62210, 90)
    OP_8E(0xFE, 0x67A2, 0x0, 0xF302, 0x2328, 0x0)
    OP_8E(0xFE, 0x56B8, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2A9E, 0xFA, 0xE60A, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xDC00, 0x2328, 0x0)
    OP_8E(0xFE, 0x2288, 0xFA, 0xC030, 0x2328, 0x0)
    OP_8E(0xFE, 0x2BE8, 0xFA, 0xB6D0, 0x2328, 0x0)
    OP_8E(0xFE, 0x402E, 0xFA, 0xB6D0, 0x2328, 0x0)
    Sleep(400)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x8E12, 0x2328, 0x0)
    OP_8E(0xFE, 0x1EF0, 0xFA, 0x1F04, 0x2328, 0x0)
    Sleep(2000)
    Jump("Function_4_833")

    label("loc_A6B")

    Return()

    # Function_4_833 end

    def Function_5_A6C(): pass

    label("Function_5_A6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC5")
    SetChrPos(0xFE, -4340, 0, 16160, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0xBD74, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6866, 0x0, 0x6B58, 0x9C4, 0x0)
    Jump("Function_5_A6C")

    label("loc_AC5")

    Return()

    # Function_5_A6C end

    def Function_6_AC6(): pass

    label("Function_6_AC6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5C")
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0x5528, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xC300, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF47A, 0x0, 0xF94C, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_6_AC6")

    label("loc_B5C")

    Return()

    # Function_6_AC6 end

    def Function_7_B5D(): pass

    label("Function_7_B5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C63")
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF65E6, 0x0, 0xBBE4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0x9592, 0x9C4, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFF64BA, 0x0, 0xB644, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF676C, 0x0, 0xC1E8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFA68C, 0x0, 0xC0F8, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFE2F0, 0x0, 0xC0F8, 0x9C4, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_7_B5D")

    label("loc_C63")

    Return()

    # Function_7_B5D end

    def Function_8_C64(): pass

    label("Function_8_C64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C87")
    OP_8D(0xFE, 8130, 41700, 5710, 43100, 2000)
    Jump("Function_8_C64")

    label("loc_C87")

    Return()

    # Function_8_C64 end

    def Function_9_C88(): pass

    label("Function_9_C88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D0E")

    ChrTalk(    #0
        0xFE,
        (
            "要说王都第一的景点，\x01",
            "就是格兰赛尔城的空中庭院了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "不过最近好像\x01",
            "不向游客开放了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "怎么回事呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D83")

    label("loc_D0E")


    ChrTalk(    #3
        0xFE,
        (
            "要说王都第一的景点，\x01",
            "就是格兰赛尔城的空中庭院了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "虽然王都有很多名胜，\x01",
            "不过只有这里绝对不能错过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_D83")

    Jump("loc_DA1")

    label("loc_D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_D90")
    Jump("loc_DA1")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_D9A")
    Jump("loc_DA1")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_DA1")

    label("loc_DA1")

    TalkEnd(0xFE)
    Return()

    # Function_9_C88 end

    def Function_10_DA5(): pass

    label("Function_10_DA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E03")

    ChrTalk(    #5
        0xFE,
        (
            "之前看到许多\x01",
            "穿着黑衣服的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "连戴着的眼镜\x01",
            "都是黑色的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E49")

    label("loc_E03")


    ChrTalk(    #7
        0xFE,
        (
            "啊啊，好忙，好忙。\x01",
            "整天跑来跑去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "喂，让开让开～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_E49")

    Jump("loc_E67")

    label("loc_E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_E56")
    Jump("loc_E67")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_E60")
    Jump("loc_E67")

    label("loc_E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_E67")

    label("loc_E67")

    TalkEnd(0xFE)
    Return()

    # Function_10_DA5 end

    def Function_11_E6B(): pass

    label("Function_11_E6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EE5")

    ChrTalk(    #9
        0xFE,
        (
            "听说常驻武官阿温格先生\x01",
            "要回国一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "他好像因为工作很忙的缘故，\x01",
            "很少有回国的机会……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F76")

    label("loc_EE5")


    ChrTalk(    #11
        0xFE,
        (
            "对了，\x01",
            "听说阿温格先生要回国一段时间。\x02",
        )
    )

    Jump("loc_F1A")

    label("loc_F1A")

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "他是摩尔根将军的儿子，\x01",
            "在外国担任常驻武官。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "是不是有什么\x01",
            "重要的案件呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_F76")

    Jump("loc_F94")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_F83")
    Jump("loc_F94")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_F8D")
    Jump("loc_F94")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_F94")

    label("loc_F94")

    TalkEnd(0xFE)
    Return()

    # Function_11_E6B end

    def Function_12_F98(): pass

    label("Function_12_F98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(21960, 250, 46140, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(58000, 0)
    OP_6E(330, 0)
    SetChrPos(0x151, 8900, 250, 26340, 0)
    SetChrPos(0x103, 8900, 250, 24140, 0)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_1033():
        OP_6D(11260, 250, 39200, 5000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1033)

    def lambda_104B():
        OP_8E(0xFE, 0x22C4, 0xFA, 0xBCAC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_104B)
    OP_43(0x151, 0x3, 0x0, 0xE)

    def lambda_106D():
        OP_8E(0xFE, 0x22C4, 0x0, 0xABE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_106D)
    WaitChrThread(0x2C, 0x0)
    Sleep(1000)

    def lambda_1092():
        OP_6D(9920, 250, 46880, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1092)

    def lambda_10AA():
        OP_6B(3500, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_10AA)

    def lambda_10BA():
        OP_6C(35000, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_10BA)

    def lambda_10CA():
        OP_6E(266, 7000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_10CA)
    WaitChrThread(0x2C, 0x0)
    WaitChrThread(0x103, 0x1)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x103,
        (
            "#1643F慢、慢着……？\x02\x03",

            "你说酒店，就是这里？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x151, 0x3)

    ChrTalk(    #15
        0x151,
        "#1652F嗯嗯，是的……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 4500, 0, 67380, 180)
    SetChrPos(0x16, 2400, 0, 67380, 180)
    OP_59()

    def lambda_1191():
        OP_6D(6440, 0, 58060, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1191)

    def lambda_11A9():
        OP_67(0, 3620, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_11A9)

    def lambda_11C1():
        OP_6B(3700, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_11C1)

    def lambda_11D1():
        OP_6C(0, 2500)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_11D1)

    def lambda_11E1():
        OP_6E(276, 2500)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_11E1)
    WaitChrThread(0x2C, 0x0)
    Sleep(500)

    def lambda_11FB():
        OP_8F(0xFE, 0x274C, 0xFA, 0xBF40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_11FB)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #16
        0x151,
        (
            "#1652F（对格兰赛尔城的\x01",
            "  警戒果然森严啊。）\x02\x03",

            "#1656F（唔，最好的进城路线是……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(11340, 250, 49020, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(3490, 0)
    OP_6C(35000, 0)
    OP_6E(267, 0)
    SetChrPos(0x151, 10460, 250, 48960, 0)
    Sleep(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    def lambda_12EA():
        OP_8E(0xFE, 0x28DC, 0x0, 0xB4DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12EA)
    WaitChrThread(0x103, 0x1)

    def lambda_130A():
        OP_8E(0xFE, 0x28DC, 0x0, 0xB860, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_130A)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #17
        0x103,
        (
            "#1648F#4P…………………………\x02\x03",

            "这前面就是格兰赛尔城了。\x01",
            "怎么办？要参观吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(    #18
        0x151,
        (
            "#1654F#5P…………是、是啊。\x02\x03",

            "嗯～…………\x01",
            "……嗯嗯…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#1646F#4P（……差不多该露出马脚了吧。）\x02\x03",

            "#1648F（说来听听吧。）\x02\x03",

            "（拉着我\x01",
            "  到处团团转的理由！）\x02",
        )
    )

    Jump("loc_1462")

    label("loc_1462")

    CloseMessageWindow()

    def lambda_1469():
        OP_6D(15540, 0, 46880, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1469)
    WaitChrThread(0x2C, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 20500, 750, 44000, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #20
        0x10,
        "男人的声音",
        "#3P啧，真受不了啊。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x10,
        "男人的声音",
        (
            "#3P我到外面去\x01",
            "稍微换换空气。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(21160, 250, 44340, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(82000, 0)
    OP_6E(266, 0)
    Sleep(500)
    OP_20(0x7D0)
    OP_70(0x4, 0x3B)
    OP_73(0x4)

    def lambda_155B():
        OP_6D(13640, 250, 46420, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_155B)

    def lambda_1573():
        OP_8E(0xFE, 0x3B24, 0xFA, 0xABE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1573)

    def lambda_158E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_158E)
    WaitChrThread(0x10, 0x1)

    def lambda_15A5():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_15A5)

    def lambda_15B3():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_15B3)

    def lambda_15C1():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_15C1)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x10,
        "#3S找、找到了！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#1643F什、什么？\x01",
            "……怎么了！？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x10, 0)
    Sleep(300)

    ChrTalk(    #24
        0x10,
        "#3S给我老实点！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_16D1():
        OP_6B(2340, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_16D1)
    SetChrChipByIndex(0x10, 26)
    SetChrSubChip(0x10, 0)

    def lambda_16EB():
        OP_8E(0xFE, 0x2FA8, 0xFA, 0xB694, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16EB)
    Sleep(500)
    OP_44(0x2C, 0xFF)
    OP_44(0x10, 0xFF)
    Battle(0x3AC, 0x0, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    Return()

    # Function_12_F98 end

    def Function_13_172D(): pass

    label("Function_13_172D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_6D(13240, 250, 46040, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(60000, 0)
    OP_6E(266, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 13640, 250, 44740, 270)
    SetChrPos(0x103, 10920, 250, 44860, 90)
    SetChrPos(0x151, 12940, 250, 46860, 180)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)

    def lambda_17C8():
        OP_6B(3340, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_17C8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x2C, 0x0)

    ChrTalk(    #25
        0x103,
        (
            "#1645F呼、呼……\x02\x03",

            "#1642F怎、怎么回事，这家伙。\x01",
            "有受过战斗训练啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(500)
    OP_8C(0x151, 315, 500)
    Sleep(300)

    def lambda_1867():
        OP_8E(0xFE, 0x2A30, 0xFA, 0xBE8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1867)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 0, 500)
    Sleep(500)

    ChrTalk(    #26
        0x151,
        (
            "#1652F#5P（看来还没被发现。）\x02\x03",

            "#1654F（不过这样下去只是时间问题……\x01",
            "  有没有什么好办法……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(300)

    ChrTalk(    #27
        0x103,
        (
            "#1644F我说你啊，\x01",
            "给我说明一下吧。\x02\x03",

            "这个黑衣男人是怎么回事啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x151,
        "#1654F#5P（一旦让军队警戒起来就麻烦了……）\x02",
    )

    CloseMessageWindow()

    def lambda_1998():
        OP_8E(0xFE, 0x2AA8, 0xFA, 0xB324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1998)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #29
        0x103,
        "#1644F#120W#4S你·听·到·了·吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(    #30
        0x151,
        "#1652F#5P嘘——！　安静点！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 20500, 750, 44500, 270)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 20500, 750, 43500, 270)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #31
        0x11,
        "男人的声音",
        (
            "#3P果然在住宿登记里\x01",
            "也没能找到呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AA2():
        OP_6D(14840, 250, 46040, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1AA2)
    OP_62(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1ADE():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_1ADE)

    def lambda_1AEC():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AEC)
    WaitChrThread(0x2C, 0x0)

    NpcTalk(    #32
        0x12,
        "男人的声音",
        "#3P啧…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #33
        0x12,
        "男人的声音",
        (
            "#3P本以为\x01",
            "娇生惯养的大小姐\x01",
            "一定会住酒店的……\x02",
        )
    )

    Jump("loc_1B69")

    label("loc_1B69")

    CloseMessageWindow()

    NpcTalk(    #34
        0x11,
        "男人的声音",
        (
            "#3P没办法了。\x01",
            "去街上……\x02",
        )
    )

    CloseMessageWindow()
    OP_70(0x4, 0x3B)
    OP_73(0x4)

    def lambda_1BA9():
        OP_8E(0xFE, 0x4470, 0xFA, 0xADD4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BA9)

    def lambda_1BC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1BC4)
    Sleep(250)

    def lambda_1BDB():
        OP_8E(0xFE, 0x459C, 0xFA, 0xA924, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1BDB)

    def lambda_1BF6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1BF6)
    Sleep(500)

    ChrTalk(    #35
        0x11,
        "#3P找找………吗………？？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(200)
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(    #36 op#A
        0x11,
        "#3S#19A找、找到了！！\x02",
    )

    CloseMessageWindow()
    OP_7C(0x0, 0x96, 0xBB8, 0x64)
    #Sleep(2156)

    ChrTalk(    #37 op#A
        0x12,
        "#3S#4P#16A就是这家伙，快抓起来！\x02",
    )
    CloseMessageWindow()

    OP_7C(0x0, 0x96, 0xBB8, 0x64)
    #Sleep(1700)

    ChrTalk(    #38
        0x151,
        "#1653F#4S不，大声喊的话……\x02",
    )

    OP_7C(0x0, 0xDC, 0xBB8, 0x64)
    Sleep(200)
    OP_56(0x1)
    OP_59()
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, 4500, 0, 68380, 180)
    SetChrPos(0x14, 2000, 0, 68380, 180)

    def lambda_1D2D():
        OP_6D(4960, 0, 68860, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_1D2D)
    WaitChrThread(0x2C, 0x0)

    def lambda_1D4A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1D4A)
    Sleep(100)

    def lambda_1D5D():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1D5D)
    Sleep(300)

    ChrTalk(    #39
        0x13,
        "#2P喂，听到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14,
        "啊啊，从那个方向来的！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x13, 0)

    def lambda_1DB9():
        OP_8E(0xFE, 0x1194, 0x0, 0xBCFC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1DB9)
    Sleep(100)
    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0x14, 0)

    def lambda_1DE3():
        OP_8E(0xFE, 0x7D0, 0x0, 0xBCFC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DE3)
    Sleep(1000)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x1)
    Fade(500)
    OP_6D(6280, 0, 44480, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(35000, 0)
    OP_6E(266, 0)
    SetChrPos(0x103, 6760, 0, 43740, 90)
    SetChrPos(0x151, 4000, 0, 42440, 90)
    SetChrPos(0x11, 10140, 0, 45600, 270)
    SetChrPos(0x12, 10400, 0, 43360, 270)
    SetChrPos(0x13, 6200, 0, 58500, 180)
    SetChrPos(0x14, 3940, 0, 59000, 180)
    Sleep(500)
    OP_43(0x151, 0x3, 0x0, 0xF)

    def lambda_1EC3():
        OP_8E(0xFE, 0x23B4, 0x0, 0xB220, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1EC3)
    Sleep(200)

    def lambda_1EE3():
        OP_8E(0xFE, 0x251C, 0x0, 0xA960, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1EE3)
    Sleep(400)

    def lambda_1F03():
        OP_8F(0xFE, 0x1680, 0x0, 0xAADC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F03)
    WaitChrThread(0x103, 0x1)

    def lambda_1F23():
        OP_8E(0xFE, 0x1838, 0x0, 0xBAA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1F23)
    Sleep(100)

    def lambda_1F43():
        OP_8E(0xFE, 0xF64, 0x0, 0xB860, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F43)
    WaitChrThread(0x13, 0x1)
    SetChrChipByIndex(0x13, 0)
    SetChrSubChip(0x13, 0)
    WaitChrThread(0x14, 0x1)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 0)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x103, 0x3, 0x0, 0x10)
    Sleep(1500)

    ChrTalk(    #41
        0x103,
        (
            "#1643F#3S什么！？　什么！？\x01",
            "喂！　这是怎么了！？#2S\x02\x03",

            "#1644F#3S我说委托人，\x01",
            "快点给我说明啊！！#2S\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x3)

    ChrTalk(    #42
        0x151,
        "#1652F那个，雪拉扎德小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43 op#A
        0x151,
        "#3S#28A#1P总而言之快逃吧～！#2S\x02",
    )


    def lambda_2067():
        OP_8E(0xFE, 0xFA0, 0x0, 0x6F68, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2067)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(3000)
    OP_8C(0x103, 180, 500)
    Sleep(100)

    ChrTalk(    #44 op#A
        0x103,
        (
            "#1644F#3S#8A啊啊！？#2S\x02",

            "#3S#20A等、等一下啊！！#2S\x02",
        )
    )


    def lambda_20E9():

        label("loc_20E9")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_20E9")

    QueueWorkItem2(0x11, 2, lambda_20E9)

    def lambda_20FA():

        label("loc_20FA")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_20FA")

    QueueWorkItem2(0x12, 2, lambda_20FA)

    def lambda_210B():

        label("loc_210B")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_210B")

    QueueWorkItem2(0x13, 2, lambda_210B)

    def lambda_211C():

        label("loc_211C")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_211C")

    QueueWorkItem2(0x14, 2, lambda_211C)

    def lambda_212D():
        OP_8E(0xFE, 0x1680, 0x0, 0x7044, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_212D)
    Sleep(500)
    OP_44(0x13, 0x2)
    OP_8C(0x13, 180, 0)
    SetChrChipByIndex(0x13, 22)
    SetChrSubChip(0x13, 0)

    def lambda_2162():
        OP_8E(0xFE, 0x1838, 0x0, 0x6C84, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2162)
    Sleep(100)
    OP_44(0x12, 0x2)
    OP_8C(0x12, 180, 0)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)

    def lambda_2197():
        OP_8E(0xFE, 0x251C, 0x0, 0x5B40, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2197)
    Sleep(50)
    OP_44(0x14, 0x2)
    OP_8C(0x14, 180, 0)
    SetChrChipByIndex(0x14, 22)
    SetChrSubChip(0x14, 0)

    def lambda_21CC():
        OP_8E(0xFE, 0xF64, 0x0, 0x6A40, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_21CC)
    Sleep(100)
    OP_44(0x11, 0x2)
    OP_8C(0x11, 180, 0)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)

    def lambda_2201():
        OP_8E(0xFE, 0x23B4, 0x0, 0x6400, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2201)
    Sleep(3000)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x151, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_172D end

    def Function_14_2262(): pass

    label("Function_14_2262")

    WaitChrThread(0x151, 0x1)

    def lambda_226D():
        OP_8E(0xFE, 0x28DC, 0xFA, 0xBF40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_226D)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 0, 500)
    Sleep(400)
    Return()

    # Function_14_2262 end

    def Function_15_2294(): pass

    label("Function_15_2294")


    ChrTalk(    #45 op#A
        0x13,
        (
            "#4P#23A哦，找到了！\x01",
            "那就是目标！\x02",
        )
    )

    Sleep(2500)
    OP_56(0x0)
    OP_59()

    ChrTalk(    #46 op#A
        0x14,
        (
            "#4P#23A那个金发的女孩。\x01",
            "快把她抓起来！\x02",
        )
    )

    Sleep(2700)
    OP_56(0x0)
    OP_59()
    Return()

    # Function_15_2294 end

    def Function_16_2301(): pass

    label("Function_16_2301")

    OP_8C(0x103, 0, 500)
    Sleep(600)
    OP_8C(0x103, 90, 500)
    Sleep(600)
    OP_8C(0x103, 0, 500)
    Sleep(600)
    OP_8C(0x103, 90, 500)
    Sleep(600)
    Return()

    # Function_16_2301 end

    def Function_17_2332(): pass

    label("Function_17_2332")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_6D(-3000, 0, 69580, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(0, 0)
    OP_6E(244, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x10, -3950, 0, 69340, 135)
    SetChrPos(0x11, -2050, 0, 69340, 225)
    SetChrPos(0x12, -3000, 0, 68080, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x13, 4660, 0, 68440, 180)
    SetChrPos(0x14, 1500, 0, 68440, 180)
    SetChrPos(0x15, 3080, 0, 68080, 180)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, -13180, 3000, 60360, 90)
    SetChrPos(0x151, -13180, 3000, 59060, 90)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    SoundLoad(372)
    SoundLoad(402)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24E4")
    Call(0, 32)

    def lambda_2482():
        OP_6D(-3000, 0, 69580, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2482)

    def lambda_249A():
        OP_67(0, 7500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_249A)

    def lambda_24B2():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_24B2)

    def lambda_24C2():
        OP_6B(3280, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_24C2)

    def lambda_24D2():
        OP_6E(244, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_24D2)
    WaitChrThread(0x2C, 0x0)
    Jump("loc_24EE")

    label("loc_24E4")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_24EE")

    Sleep(500)
    OP_20(0xBB8)

    def lambda_24FE():
        OP_6D(-3000, 0, 68000, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_24FE)

    def lambda_2516():
        OP_67(0, 4160, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2516)

    def lambda_252E():
        OP_6B(4220, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_252E)
    Sleep(3000)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    OP_A1(0x22, 0x8)
    SetChrPos(0x22, -3000, 0, 57440, 0)
    OP_72(0x408, 0x0)
    ExitThread()

    def lambda_2569():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xE574, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2569)
    OP_22(0x174, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    Sleep(500)

    def lambda_2593():
        OP_8F(0xFE, 0xFFFFF470, 0x0, 0xE574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2593)
    WaitChrThread(0x22, 0x1)

    def lambda_25B3():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xE574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_25B3)
    WaitChrThread(0x22, 0x1)

    def lambda_25D3():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xE574, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_25D3)
    WaitChrThread(0x22, 0x1)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0x13)
    OP_22(0x174, 0x0, 0x64)

    def lambda_2604():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEA88, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2604)
    WaitChrThread(0x22, 0x1)
    Sleep(500)

    def lambda_2629():
        OP_8F(0xFE, 0xFFFFF470, 0x0, 0xEA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2629)
    WaitChrThread(0x22, 0x1)

    def lambda_2649():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xEA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2649)
    WaitChrThread(0x22, 0x1)

    def lambda_2669():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2669)
    WaitChrThread(0x22, 0x1)
    Sleep(500)
    OP_22(0x174, 0x0, 0x64)

    def lambda_2693():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2693)
    WaitChrThread(0x22, 0x1)
    Sleep(500)

    def lambda_26B8():
        OP_8F(0xFE, 0xFFFFF470, 0x0, 0xEF9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_26B8)
    WaitChrThread(0x22, 0x1)

    def lambda_26D8():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xEF9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_26D8)
    WaitChrThread(0x22, 0x1)

    def lambda_26F8():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEF9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_26F8)
    WaitChrThread(0x22, 0x1)
    Sleep(500)
    Sleep(300)

    ChrTalk(    #47
        0x10,
        "……哼，来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        "今天就是最后一天了……\x02",
    )

    CloseMessageWindow()

    def lambda_2760():
        OP_6D(-3000, 0, 67000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2760)

    def lambda_2778():
        OP_6B(3820, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2778)

    def lambda_2788():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0x104DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2788)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x2C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x40)
    SetChrPos(0x1C, -3000, 0, 61340, 0)
    OP_22(0x192, 0x0, 0x64)

    NpcTalk(    #49
        0x1C,
        "叫声",
        "#6P喵～。\x02",
    )

    Jump("loc_27F0")

    label("loc_27F0")

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(70)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_284B():
        OP_8F(0xFE, 0xFFFFF45C, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_284B)
    WaitChrThread(0x22, 0x1)

    def lambda_286B():
        OP_8F(0xFE, 0xFFFFF420, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_286B)
    WaitChrThread(0x22, 0x1)

    def lambda_288B():
        OP_8F(0xFE, 0xFFFFF448, 0x0, 0xEF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_288B)
    WaitChrThread(0x22, 0x1)
    OP_22(0x16E, 0x0, 0x50)
    Sleep(500)

    def lambda_28B5():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xFB2C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_28B5)
    WaitChrThread(0x1C, 0x1)
    OP_22(0x192, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #50
        0x12,
        "#5P喂喂，是猫啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "……不，等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "说不定\x01",
            "还藏在里面。\x02",
        )
    )

    Jump("loc_2988")

    label("loc_2988")

    CloseMessageWindow()
    OP_59()

    def lambda_2990():
        OP_6D(-2009, 0, 64700, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2990)

    def lambda_29A8():
        OP_6B(3700, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_29A8)

    def lambda_29B8():
        OP_67(0, 4600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_29B8)

    def lambda_29D0():
        OP_6C(30000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_29D0)

    def lambda_29E0():
        OP_8E(0xFE, 0xFFFFEE3A, 0x0, 0xF3AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_29E0)
    Sleep(150)

    def lambda_2A00():
        OP_8E(0xFE, 0xFFFFFA56, 0x0, 0xF794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2A00)
    Sleep(600)

    def lambda_2A20():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xF794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A20)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2A52():
        OP_8E(0xFE, 0x2760, 0x0, 0xFB2C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2A52)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 225, 500)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 135, 500)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #53
        0x10,
        "喂，别大意啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        "#1P我知道。\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_2AC0():
        OP_6D(-6780, 250, 66570, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2AC0)
    Sleep(500)

    def lambda_2ADD():
        OP_67(0, 4550, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2ADD)

    def lambda_2AF5():
        OP_6C(344000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_2AF5)

    def lambda_2B05():
        OP_6B(1720, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_2B05)

    def lambda_2B15():
        OP_6E(536, 1000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2B15)
    OP_7D(0x0, 0x103, 0x1E, 0x96)
    OP_43(0x103, 0x3, 0x0, 0x12)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x151, 29)
    SetChrSubChip(0x151, 2)
    OP_7D(0x0, 0x151, 0x1E, 0x96)

    def lambda_2B50():
        OP_96(0xFE, 0xFFFFDFBC, 0xFA, 0xFFEF, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2B50)
    WaitChrThread(0x151, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x151, 0x0, 0x0)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    Sleep(100)

    def lambda_2B8F():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2B8F)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    TurnDirection(0x10, 0x103, 500)
    Sleep(100)
    OP_1D(0x35)
    Sleep(200)

    ChrTalk(    #55
        0x10,
        "#3S啊啊，这些家伙！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_2C01():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C01)
    Sleep(50)

    def lambda_2C14():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C14)
    Sleep(100)

    ChrTalk(    #56
        0x103,
        "#1644F#3S#1P太迟啦！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2C6A():
        OP_6B(1520, 500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2C6A)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 13)
    SetChrSubChip(0x103, 0)

    def lambda_2C89():
        OP_8F(0xFE, 0xFFFFEFE8, 0xFA, 0xF6E0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C89)

    def lambda_2CA4():
        OP_8F(0xFE, 0xFFFFEBB0, 0xFA, 0xF6E0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2CA4)
    Sleep(300)
    OP_44(0x2C, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x151, 0xFF)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x151, 0x4)
    Battle(0x3AE, 0x0, 0x2, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 20)
    Return()

    # Function_17_2332 end

    def Function_18_2CF9(): pass

    label("Function_18_2CF9")

    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x103, 13)
    SetChrSubChip(0x103, 2)

    def lambda_2D0E():
        OP_96(0xFE, 0xFFFFE430, 0xFA, 0xFE88, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D0E)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 12)
    SetChrSubChip(0x103, 3)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x103, 0x0, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x103, 10)
    SetChrSubChip(0x103, 0)

    def lambda_2D57():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D57)
    Return()

    # Function_18_2CF9 end

    def Function_19_2D60(): pass

    label("Function_19_2D60")

    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)

    def lambda_2DAB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2DAB)
    Sleep(200)

    def lambda_2DBE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2DBE)
    Sleep(150)

    def lambda_2DD1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2DD1)
    Sleep(500)
    Return()

    # Function_19_2D60 end

    def Function_20_2DDF(): pass

    label("Function_20_2DDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x56)
    OP_6D(-3400, 0, 63380, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(35000, 0)
    OP_6E(244, 0)
    ClearMapFlags(0x10)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    SetChrPos(0x22, -1680, 0, 59140, 0)
    OP_A1(0x22, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    SetChrFlags(0x1E, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x10, -2880, 0, 62740, 270)
    SetChrPos(0x11, -2040, 0, 65099, 270)
    SetChrPos(0x12, -1480, 0, 61240, 270)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 3)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0x11, 3)
    SetChrChipByIndex(0x12, 14)
    SetChrSubChip(0x12, 3)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrPos(0x103, -4920, 0, 63180, 90)
    SetChrPos(0x151, -5060, 0, 61700, 90)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    SetChrFlags(0x1C, 0x80)
    SoundLoad(132)
    SoundLoad(521)
    LoadEffect(0x0, "battle\\\\damage5.eff")

    def lambda_2F50():
        OP_6B(3300, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2F50)
    FadeToBright(1000, 0)
    Sleep(1000)

    def lambda_2F6E():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2F6E)
    Sleep(1000)

    ChrTalk(    #57
        0x10,
        "可、可恶！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(100)

    ChrTalk(    #58
        0x103,
        "#1644F#1P爱娜，趁现在！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(100)

    ChrTalk(    #59
        0x151,
        "#1652F嗯嗯！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrPos(0x13, -4019, 250, 76600, 180)
    SetChrPos(0x14, -1880, 250, 76600, 180)

    def lambda_302E():
        OP_8E(0xFE, 0xFFFFF04D, 0xFA, 0x113C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_302E)

    def lambda_3049():
        OP_6D(-3720, 0, 68980, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3049)
    OP_8C(0x103, 0, 600)
    Sleep(50)

    def lambda_306D():
        OP_8F(0xFE, 0xFFFFF100, 0x0, 0x10554, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_306D)
    Sleep(200)
    OP_43(0x14, 0x3, 0x0, 0x16)

    def lambda_3094():
        OP_8E(0xFE, 0xFFFFED90, 0x0, 0xFF14, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3094)
    WaitChrThread(0x103, 0x1)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x151, 0x1)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x103,
        "#1647F唔…………增援吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x151,
        "#1656F怎么会……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x3)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 4240, 0, 66760, 270)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x16, -5840, 0, 52800, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x17, -4059, 0, 51940, 0)

    def lambda_3186():
        OP_6D(-3360, 0, 65740, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3186)

    def lambda_319E():
        OP_6B(3620, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_319E)

    def lambda_31AE():
        OP_67(0, 5470, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_31AE)

    def lambda_31C6():
        OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0x104C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_31C6)

    def lambda_31E1():
        OP_8E(0xFE, 0xFFFFE930, 0x0, 0xEBC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_31E1)

    def lambda_31FC():
        OP_8E(0xFE, 0xFFFFF025, 0x0, 0xE9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_31FC)
    OP_43(0x103, 0x3, 0x0, 0x17)
    OP_43(0x151, 0x3, 0x0, 0x18)
    Sleep(1500)

    def lambda_322A():
        OP_8F(0xFE, 0xFFFFF7CC, 0x0, 0x10C48, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_322A)
    Sleep(1000)

    def lambda_324A():
        OP_8F(0xFE, 0xFFFFEED0, 0x0, 0x10E28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_324A)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(1000)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrChipByIndex(0x18, 28)
    SetChrSubChip(0x18, 0)
    SetChrPos(0x18, -2420, 0, 75240, 0)

    NpcTalk(    #62
        0x18,
        "男人的声音",
        "#4P……终于出现了啊。\x02",
    )

    CloseMessageWindow()

    def lambda_32C5():
        OP_6D(-3480, 0, 68000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_32C5)

    def lambda_32DD():
        OP_8E(0xFE, 0xFFFFF68C, 0x0, 0x11620, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32DD)
    Sleep(200)

    def lambda_32FD():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_32FD)
    Sleep(100)

    def lambda_3310():
        OP_8C(0xFE, 40, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3310)
    Sleep(100)

    def lambda_3323():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3323)
    WaitChrThread(0x18, 0x1)
    Sleep(300)
    WaitChrThread(0x2C, 0x0)

    NpcTalk(    #63
        0x18,
        "黑衣人头目",
        "#4P喂，还站着干什么。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #64
        0x18,
        "黑衣人头目",
        (
            "#4P雇主还在等着。\x01",
            "赶快带过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x18, 0, 500)
    Sleep(200)

    def lambda_33AE():
        OP_6D(-3360, 0, 65740, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_33AE)

    def lambda_33C6():
        OP_8E(0xFE, 0xFFFFF68C, 0x0, 0x125E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_33C6)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x2C, 0x0)

    def lambda_33EB():
        OP_8C(0xFE, 230, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_33EB)
    Sleep(50)

    def lambda_33FE():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_33FE)
    Sleep(50)

    def lambda_3411():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3411)
    Sleep(500)

    def lambda_3424():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_3424)

    def lambda_3432():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3432)
    Sleep(100)

    def lambda_3451():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3451)
    Sleep(100)
    Fade(200)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_347F():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_347F)
    Sleep(100)
    Fade(200)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    Fade(200)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)

    def lambda_34C1():
        OP_8C(0xFE, 315, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_34C1)
    Sleep(200)

    def lambda_34D4():
        OP_8F(0xFE, 0xFFFFE340, 0xFA, 0xF870, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_34D4)
    Sleep(300)

    def lambda_34F4():
        OP_8F(0xFE, 0xFFFFE78C, 0x0, 0xFC94, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34F4)
    Sleep(200)
    TurnDirection(0x13, 0x103, 400)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x151, 0x1)

    def lambda_3525():
        OP_8E(0xFE, 0xFFFFF5B0, 0x0, 0xFE4B, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3525)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #65
        0x11,
        (
            "…………你们……\x01",
            "别欺人太甚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        "以为这样就了事了？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #67
        0x11,
        "先杀了你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "……这边的大小姐\x01",
            "就暂时留着一条命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "让本人来写遗嘱，\x01",
            "和伪造比起来\x01",
            "还是要省事多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        (
            "#1646F…………………………\x02\x03",

            "#1648F会有……这么简单吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x11,
        "哼，嘴巴倒挺硬的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#1642F（………………爱娜……）\x02\x03",

            "（……还能跑吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x151,
        "#1652F（嗯、嗯嗯…………）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#1646F（我来拖住\x01",
            "  这些家伙。）\x02\x03",

            "（……你快跑！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x151,
        (
            "#1653F（咦……………………）\x02\x03",

            "#1652F（这、这样不行啊！\x01",
            "  这么多对手，\x01",
            "  雪拉扎德…………）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        "呼呼，求饶完毕了？\x02",
    )

    CloseMessageWindow()

    def lambda_37D2():
        OP_8E(0xFE, 0xFFFFEA48, 0x0, 0xFC94, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37D2)
    Sleep(200)

    def lambda_37F2():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_37F2)

    def lambda_3800():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3800)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #77
        0x103,
        (
            "#1644F你还有要做的事情。\x01",
            "而我也是！\x02\x03",

            "我们彼此……\x01",
            "都要去做自己该做的事情。\x02\x03",

            "#1641F……没关系，我不会死的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "你们在\x01",
            "胡说八道什么呢……\x02",
        )
    )

    Jump("loc_38BF")

    label("loc_38BF")

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_38CF():
        OP_6B(3260, 400)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_38CF)
    OP_43(0x103, 0x3, 0x0, 0x19)
    Sleep(500)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x11, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)

    def lambda_392F():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_392F)

    def lambda_3949():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xFE4B, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3949)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 14)
    SetChrSubChip(0x11, 3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #79
        0x11,
        "唔……出手好重……！？\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x10)

    ChrTalk(    #80
        0x12,
        "混、混帐……！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x15, 25)
    SetChrSubChip(0x15, 0)
    Sleep(100)
    Fade(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x13, 25)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x16, 25)
    SetChrSubChip(0x16, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(70)
    Fade(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 25)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x17, 25)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x10, 25)
    SetChrSubChip(0x10, 0)
    Sleep(100)

    ChrTalk(    #81
        0x103,
        "#1642F快走，爱娜！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #82
        0x151,
        "#1652F但、但是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x103,
        "#1644F#3S快走啊！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 13280, 0, 65040, 270)
    OP_20(0xBB8)

    NpcTalk(    #84
        0x1A,
        "青年的声音",
        (
            "看来你陷入困境了啊，\x01",
            "雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_3C26():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3C26)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)

    def lambda_3C3E():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3C3E)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 0)

    def lambda_3C56():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3C56)
    SetChrChipByIndex(0x13, 0)
    SetChrSubChip(0x13, 0)

    def lambda_3C6E():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3C6E)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 0)

    def lambda_3C86():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3C86)
    SetChrChipByIndex(0x15, 0)
    SetChrSubChip(0x15, 0)

    def lambda_3C9E():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3C9E)
    SetChrChipByIndex(0x16, 0)
    SetChrSubChip(0x16, 0)

    def lambda_3CB6():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3CB6)
    SetChrChipByIndex(0x17, 0)
    SetChrSubChip(0x17, 0)

    def lambda_3CCE():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3CCE)
    Sleep(300)

    ChrTalk(    #85
        0x103,
        "#1643F啊……………………\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3D07():
        OP_8E(0xFE, 0x2C10, 0x0, 0xFE10, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_3D07)

    def lambda_3D22():
        OP_6D(11520, 0, 65040, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3D22)

    def lambda_3D3A():
        OP_67(0, 4040, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3D3A)

    def lambda_3D52():
        OP_6B(3500, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_3D52)

    def lambda_3D62():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_3D62)
    WaitChrThread(0x2C, 0x0)
    Sleep(300)
    SetChrPos(0x11, -900, 0, 65040, 90)
    SetChrPos(0x10, -2880, 0, 63240, 90)
    SetChrPos(0x12, -1480, 0, 61740, 45)
    SetChrPos(0x16, -5840, 0, 61060, 45)
    SetChrPos(0x17, -4059, 0, 60140, 45)
    SetChrPos(0x13, -4700, 0, 68980, 135)
    SetChrPos(0x14, -2400, 0, 68500, 135)
    SetChrPos(0x15, -900, 0, 66760, 90)

    ChrTalk(    #86
        0x11,
        "#5P你、你是什么人！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, -5560, 0, 65040, 90)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)

    ChrTalk(    #87
        0x103,
        (
            "#1643F#5P克、克鲁茨前辈…………\x02\x03",

            "为什么会在这里……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E8B():
        OP_6D(2860, 0, 65040, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3E8B)

    def lambda_3EA3():
        OP_67(0, 5400, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3EA3)

    def lambda_3EBB():
        OP_6B(3760, 4000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_3EBB)

    def lambda_3ECB():
        OP_8E(0xFE, 0x1194, 0x0, 0xFE10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3ECB)
    WaitChrThread(0x1A, 0x1)
    WaitChrThread(0x2C, 0x0)

    ChrTalk(    #88
        0x1A,
        (
            "#840F#5P哎呀呀，我可是王都支部所属的啊？\x01",
            "在这里不是理所当然的吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        "#1643F#5P那、那倒没错…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x1A,
        (
            "#840F#5P……雪拉扎德，\x01",
            "看来你找到该做的事了啊。\x02\x03",

            "#842F不过，\x01",
            "轻视自己生命的行为可不值得赞赏哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        "#1642F是、是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x1A,
        (
            "#843F#5P对游击士来说虽然不是错误的判断，\x01",
            "不过你也要多注意一下周围的情况。\x02\x03",

            "你似乎有极端厌恶\x01",
            "向他人求助的倾向……\x02\x03",

            "#840F既然现在我出现在这里，\x01",
            "你该做的事是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #93
        0x103,
        (
            "#1646F………………前辈。\x02\x03",

            "#1644F这里就拜托了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x33)
    Fade(500)

    def lambda_4108():
        OP_6D(3300, 0, 65040, 100)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_4108)

    def lambda_4120():
        OP_6B(3400, 100)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4120)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1A, 31)
    SetChrSubChip(0x1A, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #94
        0x1A,
        "#843F#5P―――明白―――――\x02",
    )

    CloseMessageWindow()
    Battle(0x2710, 0x30000B, 0x0, 0x0, 0xFF)
    Call(0, 21)
    Return()

    # Function_20_2DDF end

    def Function_21_417A(): pass

    label("Function_21_417A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x33)
    OP_82(0x82, 0x0)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_6D(-2240, 0, 65600, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(244, 0)
    SetMapFlags(0x10)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    SetChrPos(0x22, -1520, 0, 58740, 0)
    OP_A1(0x22, 0x8)
    OP_72(0x408, 0x0)
    ExitThread()
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x10, -1840, 0, 66660, 90)
    SetChrPos(0x11, -1700, 0, 64500, 90)
    SetChrPos(0x12, -2660, 0, 68480, 135)
    SetChrPos(0x13, 1360, 0, 68480, 180)
    SetChrPos(0x16, 60, 250, 61100, 0)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x16, 9)
    SetChrSubChip(0x16, 0)
    SetChrPos(0x14, -5140, 0, 61740, 45)
    SetChrPos(0x15, -2220, 0, 62900, 45)
    SetChrPos(0x17, -1400, 0, 61340, 45)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 840, 0, 66460, 225)
    SetChrChipByIndex(0x1A, 31)
    SetChrSubChip(0x1A, 0)
    SetChrPos(0x103, -4540, 0, 66200, 90)
    SetChrPos(0x151, -4600, 0, 64400, 90)

    def lambda_436F():
        OP_6B(3760, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_436F)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_439F():
        OP_8F(0xFE, 0xFFFFF830, 0x0, 0xED44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_439F)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_43D1():
        OP_8F(0xFE, 0xFFFFEAC0, 0x0, 0xF000, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_43D1)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4403():
        OP_8F(0xFE, 0xFFFFF36C, 0x0, 0xF1CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4403)
    OP_0D()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #95
        0x103,
        "#1644F#1P快走吧，爱娜！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #96
        0x151,
        "#1652F嗯，好的！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 600)
    Sleep(100)

    def lambda_4484():
        OP_8E(0xFE, 0xFFFFEF34, 0x0, 0x12674, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4484)
    Sleep(100)

    def lambda_44A4():
        OP_8E(0xFE, 0xFFFFEED0, 0x0, 0x1228C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_44A4)
    Sleep(400)
    OP_8C(0x14, 0, 500)
    Sleep(200)

    ChrTalk(    #97
        0x14,
        "啊啊，那些家伙！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 45, 500)
    Sleep(200)

    ChrTalk(    #98
        0x14,
        (
            "一半留下来解决这个人。\x01",
            "其余的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4527():
        OP_6D(-1900, 0, 63560, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_4527)

    def lambda_453F():
        OP_6C(36000, 1000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_453F)
    WaitChrThread(0x2C, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrPos(0x1B, -4000, 0, 51040, 0)
    OP_22(0x209, 0x0, 0x64)

    NpcTalk(    #99 op#A
        0x19,
        "黑衣人的哀嚎",
        "#3S#1P#10A呜哇！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x8)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x19, -5200, 0, 53660, 180)
    SetChrChipByIndex(0x19, 15)
    SetChrSubChip(0x19, 0)

    def lambda_45DC():
        OP_96(0xFE, 0xFFFFEBB0, 0x0, 0xDF0C, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_45DC)
    WaitChrThread(0x19, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    OP_8C(0x19, 0, 0)
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    Sleep(1000)
    OP_22(0x209, 0x0, 0x64)

    NpcTalk(    #100 op#A
        0x18,
        "黑衣人的哀嚎",
        "#3S#1P#10A呜哦哦哦！？\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8)
    SetChrFlags(0x18, 0x40)
    SetChrPos(0x18, -3100, 0, 54060, 180)
    SetChrChipByIndex(0x18, 15)
    SetChrSubChip(0x18, 0)

    def lambda_4688():
        OP_96(0xFE, 0xFFFFF3E4, 0x0, 0xE31C, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4688)
    WaitChrThread(0x18, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    OP_8C(0x18, 45, 0)
    SetChrChipByIndex(0x18, 9)
    SetChrSubChip(0x18, 0)
    Sleep(800)

    NpcTalk(    #101
        0x1B,
        "男性的声音",
        (
            "#1P抱歉，克鲁茨。\x01",
            "我来迟了点。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_46FD():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_46FD)
    Sleep(50)

    def lambda_4710():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_4710)
    Sleep(50)

    def lambda_4723():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4723)
    Sleep(500)
    Fade(1000)
    OP_6D(-3560, 0, 50340, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(145000, 0)
    OP_6E(324, 0)
    SetChrPos(0x10, -1840, 0, 65660, 90)
    SetChrPos(0x11, -1700, 0, 63500, 180)
    SetChrPos(0x12, -6330, 0, 48660, 315)
    SetChrPos(0x13, -2460, 0, 47180, 220)
    SetChrFlags(0x12, 0x800)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x16, -260, 250, 60700, 90)
    SetChrPos(0x14, -5440, 0, 59940, 180)
    SetChrPos(0x15, -3220, 0, 60400, 180)
    SetChrPos(0x17, -2000, 0, 59240, 180)
    SetChrPos(0x18, -2700, 0, 56540, 45)
    SetChrPos(0x19, -5660, 0, 56200, 0)
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x22, -1520, 0, 57740, 0)
    SetChrPos(0x1A, 840, 0, 65459, 225)
    SetChrPos(0x1B, -4000, 0, 50840, 0)

    def lambda_486A():
        OP_6D(-2780, 0, 58340, 3500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_486A)

    def lambda_4882():
        OP_6C(132000, 3500)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4882)

    def lambda_4892():
        OP_6B(2600, 3500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4892)

    def lambda_48A2():
        OP_8E(0xFE, 0xFFFFF060, 0x0, 0xDCC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_48A2)
    Sleep(1000)
    SetChrChipByIndex(0x1A, 32)
    SetChrSubChip(0x1A, 0)

    def lambda_48CC():
        OP_8E(0xFE, 0xFFFFF060, 0x0, 0xFB2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_48CC)
    Sleep(500)

    def lambda_48EC():
        OP_8F(0xFE, 0xFFFFEAC0, 0x0, 0xEC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_48EC)
    Sleep(200)

    def lambda_490C():
        OP_8F(0xFE, 0xFFFFF36C, 0x0, 0xEDE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_490C)
    Sleep(200)

    def lambda_492C():
        OP_8F(0xFE, 0xFFFFF830, 0x0, 0xE95C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_492C)
    WaitChrThread(0x1A, 0x1)
    TurnDirection(0x1A, 0x1B, 500)
    SetChrChipByIndex(0x1A, 31)
    SetChrSubChip(0x1A, 0)
    Sleep(200)

    ChrTalk(    #102
        0x1A,
        (
            "#840F没事，\x01",
            "这边也解决得差不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x1B,
        (
            "哎呀呀，\x01",
            "你还是那么麻利。\x02",
        )
    )

    Jump("loc_49BC")

    label("loc_49BC")

    CloseMessageWindow()

    ChrTalk(    #104
        0x1B,
        (
            "话说回来…………\x01",
            "那个逞强的女孩终于低头了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x1B,
        (
            "在蔡斯支部的时候，\x01",
            "那脾气可是犟得\x01",
            "不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x1A,
        (
            "#841F哈哈…………\x01",
            "她本来就很适合当游击士。\x02\x03",

            "#840F只不过是迷失了\x01",
            "最重要的东西而已。\x02\x03",

            "只要有点契机\x01",
            "就能够察觉了。\x02\x03",

            "然后就会变得坚强起来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x1B,
        "真羡慕年轻人啊……\x02",
    )

    CloseMessageWindow()
    OP_43(0x14, 0x3, 0x0, 0x1A)
    OP_43(0x17, 0x3, 0x0, 0x1B)
    Sleep(500)
    OP_8C(0x15, 345, 500)
    Sleep(300)

    ChrTalk(    #108
        0x14,
        "怎、怎么还这么悠闲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x14,
        "#3S宰了你们！！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    Sleep(200)
    SetChrChipByIndex(0x17, 25)
    SetChrSubChip(0x17, 0)
    Sleep(50)
    SetChrChipByIndex(0x15, 25)
    SetChrSubChip(0x15, 0)
    Sleep(50)
    SetChrChipByIndex(0x14, 25)
    SetChrSubChip(0x14, 0)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_417A end

    def Function_22_4BB1(): pass

    label("Function_22_4BB1")


    def lambda_4BB7():
        OP_8E(0xFE, 0xFFFFF8A8, 0xFA, 0x113C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4BB7)
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x103, 500)
    Return()

    # Function_22_4BB1 end

    def Function_23_4BD9(): pass

    label("Function_23_4BD9")

    Sleep(300)
    OP_8C(0x103, 90, 500)
    Sleep(1000)

    def lambda_4BF0():
        OP_8F(0xFE, 0xFFFFEB10, 0x0, 0xFF8C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BF0)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_23_4BD9 end

    def Function_24_4C0B(): pass

    label("Function_24_4C0B")

    Sleep(500)
    OP_8C(0x151, 180, 500)
    Sleep(300)

    def lambda_4C22():
        OP_8E(0xFE, 0xFFFFED90, 0x0, 0xF424, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4C22)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    def lambda_4C47():
        OP_8F(0xFE, 0xFFFFEAAC, 0x0, 0xFADC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4C47)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_24_4C0B end

    def Function_25_4C62(): pass

    label("Function_25_4C62")


    ChrTalk(    #110 op#A
        0x103,
        "#1644F#3S#5A喝！！\x02",
    )

    Sleep(200)
    SetChrChipByIndex(0x103, 11)
    SetChrSubChip(0x103, 0)

    def lambda_4C95():
        OP_99(0xFE, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C95)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_25_4C62 end

    def Function_26_4CA5(): pass

    label("Function_26_4CA5")

    OP_8C(0x14, 30, 600)
    Sleep(300)
    OP_8C(0x14, 165, 600)
    Sleep(300)
    Return()

    # Function_26_4CA5 end

    def Function_27_4CBE(): pass

    label("Function_27_4CBE")

    Sleep(150)
    OP_8C(0x17, 345, 600)
    Sleep(500)
    OP_8C(0x17, 210, 600)
    Sleep(300)
    Return()

    # Function_27_4CBE end

    def Function_28_4CDC(): pass

    label("Function_28_4CDC")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4D3F")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #111
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "直接冲进\x01",
            "格兰赛尔城！\x02",
        )
    )

    Jump("loc_4D3B")

    label("loc_4D3B")

    CloseMessageWindow()
    Jump("loc_4D9B")

    label("loc_4D3F")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #112
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "赶快前往\x01",
            "格兰赛尔城吧！\x02",
        )
    )

    Jump("loc_4D97")

    label("loc_4D97")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4D9B")

    OP_59()
    Fade(500)
    SetChrPos(0x103, -8900, 0, 19840, 0)
    SetChrPos(0x151, -8900, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_28_4CDC end

    def Function_29_4DCC(): pass

    label("Function_29_4DCC")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4E2F")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #113
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "直接冲进\x01",
            "格兰赛尔城！\x02",
        )
    )

    Jump("loc_4E2B")

    label("loc_4E2B")

    CloseMessageWindow()
    Jump("loc_4E8B")

    label("loc_4E2F")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #114
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "赶快前往\x01",
            "格兰赛尔城吧！\x02",
        )
    )

    Jump("loc_4E87")

    label("loc_4E87")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4E8B")

    OP_59()
    Fade(500)
    SetChrPos(0x103, -3600, 0, 19840, 0)
    SetChrPos(0x151, -3600, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_29_4DCC end

    def Function_30_4EBC(): pass

    label("Function_30_4EBC")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F1F")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #115
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "直接冲进\x01",
            "格兰赛尔城！\x02",
        )
    )

    Jump("loc_4F1B")

    label("loc_4F1B")

    CloseMessageWindow()
    Jump("loc_4F7B")

    label("loc_4F1F")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #116
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "赶快前往\x01",
            "格兰赛尔城吧！\x02",
        )
    )

    Jump("loc_4F77")

    label("loc_4F77")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4F7B")

    OP_59()
    Fade(500)
    SetChrPos(0x103, 3600, 0, 19840, 0)
    SetChrPos(0x151, 3600, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_30_4EBC end

    def Function_31_4FAC(): pass

    label("Function_31_4FAC")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_500F")
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #117
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "直接冲进\x01",
            "格兰赛尔城！\x02",
        )
    )

    Jump("loc_500B")

    label("loc_500B")

    CloseMessageWindow()
    Jump("loc_506B")

    label("loc_500F")

    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #118
        0x103,
        (
            "#1642F已经没时间了。\x02\x03",

            "赶快前往\x01",
            "格兰赛尔城吧！\x02",
        )
    )

    Jump("loc_5067")

    label("loc_5067")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_506B")

    OP_59()
    Fade(500)
    SetChrPos(0x103, 8900, 0, 19840, 0)
    SetChrPos(0x151, 8900, 0, 19840, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_31_4FAC end

    def Function_32_509C(): pass

    label("Function_32_509C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 0)), scpexpr(EXPR_END)), "loc_54DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_52EE")

    def lambda_50B0():
        OP_6D(27200, 0, 65239, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_50B0)

    def lambda_50C8():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_50C8)

    def lambda_50E0():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_50E0)

    def lambda_50F0():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_50F0)
    WaitChrThread(0x2C, 0x0)
    Sleep(500)
    LoadEffect(0x3, "map\\\\mp032_00.eff")

    def lambda_511E():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFDE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_511E)
    WaitChrThread(0x1E, 0x1)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_5182():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5182)
    WaitChrThread(0x1E, 0x1)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_51E6():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFBF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_51E6)
    WaitChrThread(0x1E, 0x1)

    NpcTalk(    #119
        0x1E,
        "长雀斑的少女",
        "#1661F哦哦～，表情不错～⊙\x02",
    )

    CloseMessageWindow()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #120
        0x16,
        "哭出来吧……！！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Jump("loc_54D8")

    label("loc_52EE")


    def lambda_52F4():
        OP_6D(27200, 0, 65239, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_52F4)

    def lambda_530C():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_530C)

    def lambda_5324():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_5324)

    def lambda_5334():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_5334)
    WaitChrThread(0x2C, 0x0)
    Sleep(500)

    NpcTalk(    #121
        0x1E,
        "长雀斑的少女",
        "#1660F那就不客气了……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1E, 23)
    SetChrSubChip(0x1E, 0)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x1E, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #122
        0x16,
        (
            "这个小鬼……\x01",
            "我要揍你啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x17,
        "喂，不要离开岗位哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x17,
        (
            "听说担任护卫的家伙\x01",
            "似乎很有本事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        "不可大意啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x16,
        "知、知道啦……\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x1)

    label("loc_54D8")

    Jump("loc_5923")

    label("loc_54DB")

    OP_6D(27200, 0, 65239, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1E, 15020, 0, 64500, 90)

    def lambda_552F():
        OP_8F(0xFE, 0x61BC, 0x0, 0xFBF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_552F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x1E, 0x1)
    Sleep(300)

    NpcTalk(    #127
        0x1E,
        "长雀斑的少女",
        (
            "#1662F呜哇，纯黑的衣服……！\x02\x03",

            "好可爱哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x1E, 0x3, 0x0, 0x22)

    def lambda_55AE():

        label("loc_55AE")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_55AE")

    QueueWorkItem2(0x16, 0, lambda_55AE)

    def lambda_55BF():

        label("loc_55BF")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_55BF")

    QueueWorkItem2(0x17, 0, lambda_55BF)
    Sleep(1000)

    ChrTalk(    #128
        0x16,
        "你、你干什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x17,
        "别捣乱，走开！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x17,
        "快走快走！！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #131
        0x1E,
        "长雀斑的少女",
        (
            "#1661F穿的都一样呢～。\x01",
            "是制服吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x16,
        "这小鬼搞什么啊……！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 32740, 0, 62540, 270)

    def lambda_5698():
        OP_8E(0xFE, 0x607C, 0x0, 0xF44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5698)
    Sleep(2000)

    NpcTalk(    #133
        0x1D,
        "眼神凶恶的男子",
        (
            "#145F呜呜呜，头痛……\x01",
            "果然喝多了吗……\x02\x03",

            "#142F啊——…………\x01",
            "好像忘了什么东西……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1D, 0x1)
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x1E, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x1D)

    NpcTalk(    #134
        0x1D,
        "眼神凶恶的男子",
        (
            "#145F#4P……不行，想不起来。\x02\x03",

            "大概不是什么大不了的事吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57C3():
        OP_8E(0xFE, 0x490C, 0x0, 0xF44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_57C3)
    Sleep(2000)
    OP_44(0x1E, 0x2)
    OP_44(0x1E, 0x3)

    def lambda_57EB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_57EB)
    OP_8F(0x1E, 0x61BC, 0x0, 0xFBF4, 0x7D0, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    Fade(250)
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    OP_8C(0x16, 270, 0)
    OP_8C(0x17, 270, 0)
    Sleep(250)

    NpcTalk(    #135
        0x1E,
        "长雀斑的少女",
        "#1660F能拍张照片吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x16,
        "能才有鬼啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x16,
        "喂，把这家伙扔出去！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x17,
        (
            "不行，\x01",
            "现在不能离开岗位。\x02",
        )
    )

    Jump("loc_58C6")

    label("loc_58C6")

    CloseMessageWindow()

    ChrTalk(    #139
        0x17,
        "喂，小鬼，算你运气好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x17,
        (
            "我们今天很忙。\x01",
            "到那边随便玩去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x1D, 0xFF)
    SetChrFlags(0x1D, 0x80)
    OP_A2(0x2F58)

    label("loc_5923")

    Return()

    # Function_32_509C end

    def Function_33_5924(): pass

    label("Function_33_5924")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5988")

    def lambda_5933():
        OP_8E(0xFE, 0x68BA, 0x0, 0xFD3E, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_5933)
    WaitChrThread(0x1E, 0x0)
    OP_8C(0x1E, 45, 500)
    Sleep(1500)

    def lambda_595F():
        OP_8E(0xFE, 0x6964, 0x0, 0xFA63, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_595F)
    WaitChrThread(0x1E, 0x0)
    OP_8C(0x1E, 135, 500)
    Sleep(1800)
    Jump("Function_33_5924")

    label("loc_5988")

    Return()

    # Function_33_5924 end

    def Function_34_5989(): pass

    label("Function_34_5989")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A1B")

    def lambda_5998():

        label("loc_5998")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_5998")

    QueueWorkItem2(0x1E, 2, lambda_5998)
    OP_8F(0x1E, 0x661C, 0x0, 0xFEB0, 0x5DC, 0x0)
    Sleep(800)
    OP_8F(0x1E, 0x68D8, 0x0, 0xFBF4, 0x5DC, 0x0)
    Sleep(800)

    def lambda_59DB():

        label("loc_59DB")

        TurnDirection(0xFE, 0x17, 500)
        OP_48()
        Jump("loc_59DB")

    QueueWorkItem2(0x1E, 2, lambda_59DB)
    OP_8F(0x1E, 0x661C, 0x0, 0xF938, 0x5DC, 0x0)
    Sleep(800)
    OP_8F(0x1E, 0x68D8, 0x0, 0xFBF4, 0x5DC, 0x0)
    Sleep(800)
    Jump("Function_34_5989")

    label("loc_5A1B")

    Return()

    # Function_34_5989 end

    def Function_35_5A1C(): pass

    label("Function_35_5A1C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-2940, 0, 52140, 0)
    OP_67(0, 9380, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, -3900, 0, 56200, 180)
    SetChrChipByIndex(0x10E, 16)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, -3900, 0, 57200, 180)

    def lambda_5A9C():
        OP_8E(0xFE, 0xFFFFF0C4, 0x0, 0xC1C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_5A9C)
    Sleep(50)

    def lambda_5ABC():
        OP_8E(0xFE, 0xFFFFF0C4, 0x0, 0xC79C, 0x578, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5ABC)

    def lambda_5AD7():
        OP_67(0, 6380, -10000, 4600)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_5AD7)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #141
        0x10E,
        "修女艾伦",
        "#5P呼………………\x02",
    )

    Jump("loc_5B2F")

    label("loc_5B2F")

    CloseMessageWindow()

    ChrTalk(    #142
        0x26,
        (
            "……尤莉亚小姐，\x01",
            "进行得似乎很顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #143
        0x10E,
        "修女艾伦",
        "#5P嗯、嗯嗯…………\x02",
    )

    Jump("loc_5B96")

    label("loc_5B96")

    CloseMessageWindow()
    TurnDirection(0x26, 0x10E, 500)
    Sleep(300)

    NpcTalk(    #144
        0x10E,
        "修女艾伦",
        (
            "#5P又给卡兰大主教您\x01",
            "添麻烦了。\x02",
        )
    )

    Jump("loc_5BE2")

    label("loc_5BE2")

    CloseMessageWindow()

    ChrTalk(    #145
        0x26,
        "哈哈，不用在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x26,
        (
            "不过你也够辛苦的。\x01",
            "看她们那狂热的样子……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, -23400, 0, 50100, 90)
    Fade(1000)
    OP_6D(-14740, 0, 50100, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(270000, 0)

    def lambda_5C8C():
        OP_8E(0xFE, 0xFFFFC9B4, 0x0, 0xC3B4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_5C8C)
    WaitChrThread(0x27, 0x1)
    SetChrPos(0x26, -5900, 0, 49600, 0)
    SetChrPos(0x10E, -5900, 0, 50980, 180)
    OP_62(0x27, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #147
        0x27,
        "#270F#5P嗯………………？\x02",
    )

    CloseMessageWindow()

    def lambda_5D0A():
        OP_6D(-7120, 0, 51280, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_5D0A)

    def lambda_5D22():
        OP_67(0, 6900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_5D22)

    def lambda_5D3A():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_5D3A)

    def lambda_5D4A():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_5D4A)

    def lambda_5D5A():
        OP_8E(0xFE, 0xFFFFE1EC, 0x0, 0xC3B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_5D5A)
    WaitChrThread(0x27, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5DA8():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x10E, 2, lambda_5DA8)
    Sleep(150)
    OP_8C(0x26, 270, 500)
    Sleep(300)

    NpcTalk(    #148
        0x10E,
        "修女艾伦",
        "（穆……穆拉少校！？）\x02",
    )

    Jump("loc_5DF8")

    label("loc_5DF8")

    CloseMessageWindow()

    def lambda_5DFF():
        OP_8F(0xFE, 0xFFFFEBEC, 0x0, 0xC47C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5DFF)
    Sleep(300)

    def lambda_5E1F():
        OP_8F(0xFE, 0xFFFFE8F4, 0x0, 0xC3B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_5E1F)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #149
        0x10E,
        "修女艾伦",
        "（为、为什么会在这种地方……）\x02",
    )

    Jump("loc_5E7D")

    label("loc_5E7D")

    CloseMessageWindow()

    NpcTalk(    #150
        0x10E,
        "修女艾伦",
        (
            "（我记得他应该\x01",
            "  已经离开利贝尔了啊……！？）\x02",
        )
    )

    Jump("loc_5ECC")

    label("loc_5ECC")

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x27)
    Sleep(500)

    ChrTalk(    #151
        0x27,
        (
            "#277F#5P…………真是失礼了。\x02\x03",

            "#278F没想到尤莉亚上尉\x01",
            "还兼任修女啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #152
        0x10E,
        "修女艾伦",
        "咦咦………………！？\x02",
    )

    Jump("loc_5FA5")

    label("loc_5FA5")

    OP_7C(0x0, 0x96, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10E, 0, 500)
    Sleep(600)

    NpcTalk(    #153
        0x10E,
        "修女艾伦",
        (
            "啊、啊、啊…………\x01",
            "……不，这是因为………\x02",
        )
    )

    Jump("loc_6012")

    label("loc_6012")

    CloseMessageWindow()

    ChrTalk(    #154
        0x27,
        (
            "#272F#5P其实是因为那个赖皮蛋\x01",
            "还留下了一堆残局要收拾……\x02\x03",

            "所以在那之后，\x01",
            "我又得来利贝尔一趟了。\x02\x03",

            "#277F还没机会\x01",
            "和上尉打声招呼呢。\x02\x03",

            "#278F啊啊………………\x02\x03",

            "#275F……现在是不是称呼您为\x01",
            "修女尤莉亚比较合适呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x10E, 0x27, 500)
    Sleep(300)

    NpcTalk(    #155
        0x10E,
        "修女尤莉亚",
        "少、少校…………！\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #156
        0x26,
        "#6P唔………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x10E, 500)
    Sleep(300)

    ChrTalk(    #157
        0x26,
        (
            "#5P尤莉亚小姐，\x01",
            "看来没必要对这位先生隐瞒呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x26,
        (
            "#5P我还要准备下午的弥撒，\x01",
            "就此先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_61F2():

        label("loc_61F2")

        TurnDirection(0xFE, 0x26, 500)
        OP_48()
        Jump("loc_61F2")

    QueueWorkItem2(0x10E, 2, lambda_61F2)

    def lambda_6203():

        label("loc_6203")

        TurnDirection(0xFE, 0x26, 500)
        OP_48()
        Jump("loc_6203")

    QueueWorkItem2(0x27, 2, lambda_6203)
    OP_43(0x26, 0x3, 0x0, 0x25)
    Sleep(400)

    NpcTalk(    #159 op#A op#5
        0x10E,
        "修女尤莉亚",
        "#20A啊，大主教…………！？\x05\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x27, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    OP_63(0x27)
    Sleep(500)
    OP_44(0x10E, 0x2)
    OP_44(0x27, 0x2)

    ChrTalk(    #160
        0x27,
        (
            "#276F#11P……那位就是有名的\x01",
            "卡兰大主教吗。\x02\x03",

            "#272F嗯，\x01",
            "是不是应该打个招呼呢。\x02",
        )
    )

    Jump("loc_62F3")

    label("loc_62F3")

    CloseMessageWindow()

    def lambda_62FA():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0xC418, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_62FA)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)

    NpcTalk(    #161
        0x10E,
        "修女尤莉亚",
        "#4P……那、那个少校。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x10E, 400)
    Sleep(500)

    NpcTalk(    #162
        0x10E,
        "修女尤莉亚",
        (
            "#4P其实，\x01",
            "这是有原因的……\x02",
        )
    )

    Jump("loc_638C")

    label("loc_638C")

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x23, -5700, 0, 63140, 180)
    SetChrPos(0x25, -4640, 0, 62420, 180)
    SetChrPos(0x24, -4840, 0, 63800, 180)

    NpcTalk(    #163
        0x23,
        "女性的声音",
        (
            "啊～啊，\x01",
            "我也差不多该回去了……\x02",
        )
    )

    Jump("loc_6410")

    label("loc_6410")

    CloseMessageWindow()

    NpcTalk(    #164
        0x24,
        "女性的声音",
        (
            "哪怕一眼也好，\x01",
            "真想看看尤莉亚大人威风凛凛的样子……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #165
        0x25,
        "少女的声音",
        "啊啊，尤莉亚大人……㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10E, 0, 500)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrPos(0x23, -3000, 0, 76060, 180)
    SetChrPos(0x24, -3700, 0, 76980, 180)
    SetChrPos(0x25, -2300, 0, 76980, 180)

    def lambda_64F6():
        OP_6D(-3000, 0, 68980, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_64F6)

    def lambda_650E():
        OP_67(0, 6900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_650E)

    def lambda_6526():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_6526)

    def lambda_6536():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_6536)
    Sleep(2000)

    def lambda_654B():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0xDE94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_654B)
    Sleep(50)

    def lambda_656B():
        OP_8E(0xFE, 0xFFFFF18C, 0x0, 0xDE94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_656B)
    Sleep(50)

    def lambda_658B():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xDAFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_658B)
    Sleep(3000)
    SetChrPos(0x27, -7700, 0, 49900, 0)
    Fade(1000)
    OP_6D(-7120, 0, 51280, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_44(0x23, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x25, 0xFF)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(800)
    OP_8C(0x27, 90, 500)
    Sleep(1000)

    def lambda_662E():
        OP_8F(0xFE, 0xFFFFE890, 0x0, 0xC15C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_662E)
    WaitChrThread(0x10E, 0x1)
    OP_63(0x10E)
    Sleep(200)

    NpcTalk(    #166
        0x10E,
        "修女尤莉亚",
        (
            "#6P（……呜…………\x01",
            "  那些女孩们\x01",
            "  已经回来了吗…………！）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #167
        0x10E,
        "修女尤莉亚",
        (
            "#6P（在这里被看见就万事休矣……\x01",
            "  有什么办法………吗…！？）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1700)
    OP_63(0x27)
    Sleep(500)

    ChrTalk(    #168
        0x27,
        (
            "#276F#5P……上尉，\x01",
            "可以的话，让在下帮你打掩护吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10E, 270, 500)
    Sleep(300)

    NpcTalk(    #169
        0x10E,
        "修女尤莉亚",
        "#4P咦…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x27,
        (
            "#272F#5P虽然不大清楚内情，\x01",
            "但你似乎遇到了麻烦。\x02\x03",

            "#277F这种时候，\x01",
            "堂堂正正一点\x01",
            "反而不会被看穿吧。\x02\x03",

            "不介意的话，\x01",
            "我护送你到安全的地方去吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #171
        0x10E,
        "修女尤莉亚",
        "#4P穆拉少校…………\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x23, -5700, 0, 63140, 180)
    SetChrPos(0x24, -4640, 0, 62420, 180)
    SetChrPos(0x25, -4840, 0, 63800, 180)

    NpcTalk(    #172
        0x23,
        "女性的声音",
        "唉，尤莉亚大人真是的………㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10E, 0, 500)
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x10E, 270, 500)
    Sleep(300)

    NpcTalk(    #173
        0x10E,
        "修女尤莉亚",
        (
            "#4P那、那就拜托\x01",
            "您帮忙了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x27,
        "#277F#5P……明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_6961():

        label("loc_6961")

        TurnDirection(0xFE, 0x27, 500)
        OP_48()
        Jump("loc_6961")

    QueueWorkItem2(0x10E, 2, lambda_6961)
    OP_43(0x27, 0x3, 0x0, 0x26)
    Sleep(200)
    OP_43(0x10E, 0x3, 0x0, 0x27)
    Sleep(3000)
    SetChrPos(0x23, -3000, 0, 70060, 180)
    SetChrPos(0x24, -3700, 0, 70980, 180)
    SetChrPos(0x25, -2300, 0, 70980, 180)

    def lambda_69BD():
        OP_8E(0xFE, 0xFFFFF448, 0x0, 0xB3EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_69BD)
    Sleep(50)

    def lambda_69DD():
        OP_8E(0xFE, 0xFFFFF18C, 0x0, 0xF71C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_69DD)
    Sleep(50)

    def lambda_69FD():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0xB784, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_69FD)
    Fade(1000)
    OP_6D(-3040, 0, 63960, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x24, 0x1)
    OP_62(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_6A7B():

        label("loc_6A7B")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_6A7B")

    QueueWorkItem2(0x24, 2, lambda_6A7B)

    ChrTalk(    #175 op#A op#5
        0x24,
        "#15A#6P哎呀…………？\x05\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x3)
    OP_44(0x24, 0x2)

    ChrTalk(    #176
        0x24,
        "#6P……是错觉吧，嗯。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x24, 180, 400)

    def lambda_6ADF():
        OP_8E(0xFE, 0xFFFFF18C, 0x0, 0xB590, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6ADF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_5A1C end

    def Function_36_6B0C(): pass

    label("Function_36_6B0C")

    SetPlaceName(0xB4)
    Return()

    # Function_36_6B0C end

    def Function_37_6B10(): pass

    label("Function_37_6B10")

    OP_8C(0x26, 225, 500)

    def lambda_6B1D():
        OP_8E(0xFE, 0xFFFFE570, 0x0, 0xBF68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6B1D)
    WaitChrThread(0x26, 0x1)

    def lambda_6B3D():
        OP_8E(0xFE, 0xFFFFBCD0, 0x0, 0xBF68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6B3D)
    WaitChrThread(0x26, 0x1)
    Return()

    # Function_37_6B10 end

    def Function_38_6B58(): pass

    label("Function_38_6B58")


    def lambda_6B5E():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0xC2EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6B5E)
    WaitChrThread(0x27, 0x1)
    Sleep(400)

    def lambda_6B83():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6B83)
    WaitChrThread(0x27, 0x1)

    def lambda_6BA3():
        OP_8E(0xFE, 0x2328, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6BA3)
    WaitChrThread(0x27, 0x1)
    Return()

    # Function_38_6B58 end

    def Function_39_6BBE(): pass

    label("Function_39_6BBE")


    def lambda_6BC4():
        OP_8F(0xFE, 0xFFFFE890, 0x0, 0xBFCC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_6BC4)
    WaitChrThread(0x10E, 0x1)
    OP_44(0x10E, 0x2)
    Sleep(400)
    Sleep(400)

    def lambda_6BF2():
        OP_8E(0xFE, 0xFFFFE890, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_6BF2)
    WaitChrThread(0x10E, 0x1)

    def lambda_6C12():
        OP_8E(0xFE, 0x2328, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_6C12)
    WaitChrThread(0x10E, 0x1)
    Return()

    # Function_39_6BBE end

    SaveToFile()

Try(main)
