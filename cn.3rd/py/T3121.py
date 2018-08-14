from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3121   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '导力装甲',                             # 9
        '阿加特',                               # 10
        '提妲',                                 # 11
        '艾莉卡',                               # 12
        '丹',                                   # 13
        '拉赛尔博士',                           # 14
        '加鲁诺',                               # 15
        '工作人员',                             # 16
        '箱',                                   # 17
        '箱',                                   # 18
        '桶罐',                                 # 19
        '桶罐',                                 # 20
        '桶罐',                                 # 21
        '桶罐',                                 # 22
        '桶罐',                                 # 23
        '桶罐',                                 # 24
        '桶罐',                                 # 25
        '桶罐',                                 # 26
        '面板',                                 # 27
        '面板',                                 # 28
        '目标用照相机',                         # 29
        '',                                     # 30
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
        'ED6_DT26/CH20601 ._CH',             # 00
        'ED6_DT27/CH04220 ._CH',             # 01
        'ED6_DT27/CH04221 ._CH',             # 02
        'ED6_DT27/CH04222 ._CH',             # 03
        'ED6_DT27/CH04223 ._CH',             # 04
        'ED6_DT06/CH20053 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT27/CH03970 ._CH',             # 07
        'ED6_DT27/CH03980 ._CH',             # 08
        'ED6_DT07/CH02020 ._CH',             # 09
        'ED6_DT07/CH02620 ._CH',             # 0A
        'ED6_DT07/CH01190 ._CH',             # 0B
        'ED6_DT07/CH01450 ._CH',             # 0C
        'ED6_DT07/CH00065 ._CH',             # 0D
        'ED6_DT06/CH20137 ._CH',             # 0E
        'ED6_DT07/CH00150 ._CH',             # 0F
        'ED6_DT07/CH00151 ._CH',             # 10
        'ED6_DT07/CH00153 ._CH',             # 11
        'ED6_DT07/CH00159 ._CH',             # 12
        'ED6_DT07/CH00064 ._CH',             # 13
        'ED6_DT27/CH04221 ._CH',             # 14
        'ED6_DT06/CH20104 ._CH',             # 15
        'ED6_DT07/CH00061 ._CH',             # 16
        'ED6_DT07/CH00154 ._CH',             # 17
        'ED6_DT07/CH00159 ._CH',             # 18
        'ED6_DT07/CH00151 ._CH',             # 19
        'ED6_DT07/CH00152 ._CH',             # 1A
        'ED6_DT06/CH20061 ._CH',             # 1B
        'ED6_DT26/CH20750 ._CH',             # 1C
        'ED6_DT26/CH20646 ._CH',             # 1D
        'ED6_DT26/CH20647 ._CH',             # 1E
        'ED6_DT26/CH20648 ._CH',             # 1F
        'ED6_DT26/CH20649 ._CH',             # 20
        'ED6_DT26/CH20755 ._CH',             # 21
        'ED6_DT26/CH20756 ._CH',             # 22
        'ED6_DT26/CH20695 ._CH',             # 23
        'ED6_DT26/CH20626 ._CH',             # 24
        'ED6_DT07/CH00054 ._CH',             # 25
        'ED6_DT07/CH00063 ._CH',             # 26
        'ED6_DT26/CH20697 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT26/CH20601P._CP',             # 00
        'ED6_DT27/CH04220P._CP',             # 01
        'ED6_DT27/CH04221P._CP',             # 02
        'ED6_DT27/CH04222P._CP',             # 03
        'ED6_DT27/CH04223P._CP',             # 04
        'ED6_DT06/CH20053P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT27/CH03970P._CP',             # 07
        'ED6_DT27/CH03980P._CP',             # 08
        'ED6_DT07/CH02020P._CP',             # 09
        'ED6_DT07/CH02620P._CP',             # 0A
        'ED6_DT07/CH01190P._CP',             # 0B
        'ED6_DT07/CH01450P._CP',             # 0C
        'ED6_DT07/CH00065P._CP',             # 0D
        'ED6_DT06/CH20137P._CP',             # 0E
        'ED6_DT07/CH00150P._CP',             # 0F
        'ED6_DT07/CH00151P._CP',             # 10
        'ED6_DT07/CH00153P._CP',             # 11
        'ED6_DT07/CH00159P._CP',             # 12
        'ED6_DT07/CH00064P._CP',             # 13
        'ED6_DT27/CH04221P._CP',             # 14
        'ED6_DT06/CH20104P._CP',             # 15
        'ED6_DT07/CH00061P._CP',             # 16
        'ED6_DT07/CH00154P._CP',             # 17
        'ED6_DT07/CH00159P._CP',             # 18
        'ED6_DT07/CH00151P._CP',             # 19
        'ED6_DT07/CH00152P._CP',             # 1A
        'ED6_DT06/CH20061P._CP',             # 1B
        'ED6_DT26/CH20750P._CP',             # 1C
        'ED6_DT26/CH20646P._CP',             # 1D
        'ED6_DT26/CH20647P._CP',             # 1E
        'ED6_DT26/CH20648P._CP',             # 1F
        'ED6_DT26/CH20649P._CP',             # 20
        'ED6_DT26/CH20755P._CP',             # 21
        'ED6_DT26/CH20756P._CP',             # 22
        'ED6_DT26/CH20695P._CP',             # 23
        'ED6_DT26/CH20626P._CP',             # 24
        'ED6_DT07/CH00054P._CP',             # 25
        'ED6_DT07/CH00063P._CP',             # 26
        'ED6_DT26/CH20697P._CP',             # 27
    )

    DeclNpc(
        X                   = 7000,
        Z                   = 800,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1D5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        "Function_0_48A",          # 00, 0
        "Function_1_61D",          # 01, 1
        "Function_2_672",          # 02, 2
        "Function_3_70E",          # 03, 3
        "Function_4_786",          # 04, 4
        "Function_5_2CF7",         # 05, 5
        "Function_6_2D13",         # 06, 6
        "Function_7_2D5A",         # 07, 7
        "Function_8_2DA8",         # 08, 8
        "Function_9_42E9",         # 09, 9
        "Function_10_4338",        # 0A, 10
        "Function_11_4421",        # 0B, 11
        "Function_12_44B6",        # 0C, 12
        "Function_13_48F5",        # 0D, 13
        "Function_14_5348",        # 0E, 14
        "Function_15_539E",        # 0F, 15
        "Function_16_5419",        # 10, 16
        "Function_17_5429",        # 11, 17
        "Function_18_5B1B",        # 12, 18
        "Function_19_5B69",        # 13, 19
        "Function_20_5BB0",        # 14, 20
        "Function_21_5E6F",        # 15, 21
        "Function_22_5F90",        # 16, 22
        "Function_23_6FF1",        # 17, 23
        "Function_24_7008",        # 18, 24
        "Function_25_7031",        # 19, 25
        "Function_26_7071",        # 1A, 26
        "Function_27_7099",        # 1B, 27
        "Function_28_847E",        # 1C, 28
        "Function_29_84C6",        # 1D, 29
        "Function_30_850E",        # 1E, 30
        "Function_31_9393",        # 1F, 31
        "Function_32_93D3",        # 20, 32
        "Function_33_93FC",        # 21, 33
        "Function_34_AD84",        # 22, 34
        "Function_35_AE64",        # 23, 35
        "Function_36_C56F",        # 24, 36
        "Function_37_C5AC",        # 25, 37
        "Function_38_C62D",        # 26, 38
        "Function_39_C684",        # 27, 39
        "Function_40_C711",        # 28, 40
        "Function_41_C7C4",        # 29, 41
        "Function_42_C883",        # 2A, 42
        "Function_43_C95B",        # 2B, 43
        "Function_44_C9AB",        # 2C, 44
        "Function_45_CA84",        # 2D, 45
        "Function_46_CB17",        # 2E, 46
        "Function_47_CBE9",        # 2F, 47
        "Function_48_CC39",        # 30, 48
        "Function_49_CC47",        # 31, 49
        "Function_50_CCA6",        # 32, 50
        "Function_51_CCE8",        # 33, 51
        "Function_52_CD3E",        # 34, 52
        "Function_53_CD9D",        # 35, 53
        "Function_54_CDD0",        # 36, 54
        "Function_55_CE12",        # 37, 55
        "Function_56_CE59",        # 38, 56
        "Function_57_CE8D",        # 39, 57
        "Function_58_CEF6",        # 3A, 58
        "Function_59_CF64",        # 3B, 59
        "Function_60_CFAA",        # 3C, 60
        "Function_61_CFF8",        # 3D, 61
        "Function_62_D00D",        # 3E, 62
        "Function_63_D027",        # 3F, 63
        "Function_64_D046",        # 40, 64
    )


    def Function_0_48A(): pass

    label("Function_0_48A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")

    label("loc_496")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_END)), "loc_4CC")
    OP_A3(0x250B)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_4EC")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_515")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_53E")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_567")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_590")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_5B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_5D5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 30)

    label("loc_5D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_600")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 35)
    Jump("loc_61C")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_61C")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 33)

    label("loc_61C")

    Return()

    # Function_0_48A end

    def Function_1_61D(): pass

    label("Function_1_61D")

    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    Return()

    # Function_1_61D end

    def Function_2_672(): pass

    label("Function_2_672")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697")
    OP_99(0xFE, 0x0, 0x5, 0x672)
    Jump("loc_6F8")

    label("loc_697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")
    OP_99(0xFE, 0x1, 0x5, 0x640)
    Jump("loc_6F8")

    label("loc_6B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C9")
    OP_99(0xFE, 0x2, 0x5, 0x60E)
    Jump("loc_6F8")

    label("loc_6C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    OP_99(0xFE, 0x3, 0x5, 0x5DC)
    Jump("loc_6F8")

    label("loc_6E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x4, 0x5, 0x5AA)

    label("loc_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_99(0xFE, 0x0, 0x5, 0x5DC)
    Jump("loc_6F8")

    label("loc_70D")

    Return()

    # Function_2_672 end

    def Function_3_70E(): pass

    label("Function_3_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    Call(0, 27)

    label("loc_71F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730")
    Call(0, 22)

    label("loc_730")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_741")
    Call(0, 17)

    label("loc_741")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    Call(0, 13)

    label("loc_752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763")
    Call(0, 12)

    label("loc_763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_774")
    Call(0, 8)

    label("loc_774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785")
    Call(0, 4)

    label("loc_785")

    Return()

    # Function_3_70E end

    def Function_4_786(): pass

    label("Function_4_786")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x98)
    OP_6D(3260, 0, 7460, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 29)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1100, 800, 8000, 180)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x20)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13760, 0, -1400, 90)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x106, 1260, 0, 3000, 0)
    OP_6F(0x8, 60)
    OP_6F(0x9, 60)
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_72(0x1009, 0x0)
    ExitThread()
    LoadEffect(0x1, "map\\mp009_00.eff")
    LoadEffect(0x3, "Scraft\\sc000_31.eff")
    LoadEffect(0x0, "monster\\ms04220b.eff")
    LoadEffect(0x2, "monster\\ms04220.eff")
    PlayEffect(0x0, 0x6, 0x10, 1000, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0x10, -1000, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x10, 500, 700, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x10, -500, 700, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x3DC, 0x1, 0x50)

    def lambda_9D5():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9D5)
    ClearMapFlags(0x10)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x106,
        (
            "#054F提妲，没事吗！？\x02\x03",

            "动作停止了！\x01",
            "赶快下来！！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x10,
        "提妲",
        (
            "#065F但、但是……\x02\x03",

            "腰带挂住了……\x02",
        )
    )

    Jump("loc_A80")

    label("loc_A80")

    CloseMessageWindow()

    ChrTalk(    #2
        0x106,
        "#550F啧…………\x02",
    )

    CloseMessageWindow()

    def lambda_AA3():
        OP_6D(2640, 0, 9800, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_AA3)

    def lambda_ABB():
        OP_67(0, 4120, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_ABB)

    def lambda_AD3():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_AD3)
    SetChrFlags(0x106, 0x1000)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 25)

    def lambda_AF2():

        label("loc_AF2")

        TurnDirection(0xFE, 0x10, 600)
        OP_48()
        Jump("loc_AF2")

    QueueWorkItem2(0x106, 2, lambda_AF2)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_B08():
        OP_96(0xFE, 0xFFFFF72C, 0x0, 0x116C, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B08)
    WaitChrThread(0x106, 0x1)
    OP_44(0x106, 0x2)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_B34():
        OP_97(0xFE, 0x44C, 0x2008, 0x9C40, 0x1F40, 0x2)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B34)
    WaitChrThread(0x106, 0x1)
    Sleep(100)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 26)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_B69():
        OP_96(0xFE, 0xFFFFFBC8, 0x0, 0x1F54, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B69)

    def lambda_B87():
        OP_99(0xFE, 0x2, 0x6, 0x384)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B87)
    Sleep(600)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    SetChrFlags(0x10, 0x20)

    def lambda_BAB():
        OP_8F(0xFE, 0x640, 0x320, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BAB)
    PlayEffect(0x1, 0xFF, 0x106, 1200, 1000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x10, 0x2)

    def lambda_C10():
        OP_9E(0xFE, 0x19, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_C10)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 65535)
    ClearChrFlags(0x106, 0x1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    def lambda_C57():
        OP_8F(0xFE, 0xFFFFFFD8, 0x0, 0x1F7C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C57)
    WaitChrThread(0x106, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x106, 0x4)

    def lambda_C81():
        OP_96(0xFE, 0x410, 0x514, 0x1D74, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C81)
    WaitChrThread(0x106, 0x1)
    OP_22(0x8F, 0x0, 0x64)
    Fade(1000)
    SetChrChipByIndex(0x10, 32)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x106, 28)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x20)
    SetChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x1)
    OP_0D()
    SetChrPos(0x13, 2540, 0, -5440, 0)
    OP_99(0x106, 0x0, 0x3, 0x3E8)
    Sleep(100)

    def lambda_CF6():
        OP_6D(3700, 0, 5920, 1200)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_CF6)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_D13():
        OP_96(0xFE, 0x67C, 0x0, 0xBE0, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_D13)
    SetChrSubChip(0x106, 4)
    Sleep(500)

    def lambda_D3B():
        OP_99(0xFE, 0x5, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_D3B)
    WaitChrThread(0x106, 0x1)
    SetChrFlags(0x106, 0x1)
    ClearChrFlags(0x106, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_D5F():
        OP_8F(0xFE, 0x730, 0x0, 0xFFFFFA10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D5F)
    Sleep(400)

    ChrTalk(    #3
        0x13,
        "#1833F#6P提妲，太好……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    ClearChrFlags(0x10, 0x20)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_22(0x17E, 0x0, 0x64)
    SetChrSubChip(0x106, 8)
    SetChrPos(0x106, 1600, 0, 4380, 180)
    SetChrPos(0x13, 1600, 0, -1520, 0)
    OP_6D(1600, 0, 7500, 0)
    OP_67(0, 4120, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_E25():
        OP_9E(0xFE, 0x19, 0x0, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E25)
    OP_0D()
    Sleep(1500)
    Fade(1200)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_62(0x106, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 30)

    def lambda_E9B():
        OP_99(0xFE, 0x0, 0x2, 0x258)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E9B)
    OP_22(0x116, 0x0, 0x64)
    WaitChrThread(0x10, 0x2)
    SetChrFlags(0x10, 0x20)

    def lambda_EBA():
        OP_6B(2200, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_EBA)

    def lambda_ECA():
        OP_8F(0xFE, 0x640, 0x320, 0x1310, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_ECA)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_20(0x7D0)
    FadeToDark(2000, 16777215, -1)
    Sleep(50)
    SetChrSubChip(0x10, 3)
    Sleep(50)
    OP_24(0x17E, 0x50)
    Sleep(100)
    OP_24(0x17E, 0x3C)
    Sleep(100)
    OP_24(0x17E, 0x28)
    Sleep(100)
    OP_24(0x17E, 0x14)
    OP_0D()
    OP_23(0x17E)
    Sleep(300)
    OP_22(0xF5, 0x0, 0x64)
    Sleep(4000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10, 4)
    OP_6D(200, 0, -6340, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -620, -100, -6760, 270)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x800)
    SetChrFlags(0x106, 0x4)
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x13, 1600, 0, -2520, 225)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 160, 0, 2820, 180)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_43(0x14, 0x0, 0x0, 0x7)

    def lambda_FF3():
        OP_6D(4040, 0, 4740, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_FF3)

    def lambda_100B():
        OP_67(0, 3620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_100B)

    def lambda_1023():
        OP_6B(3180, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_1023)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #4
        0x12,
        (
            "#068F#40W……………………！\x02\x03",

            "#064F咦、咦……？\x02",
        )
    )

    CloseMessageWindow()
    Fade(800)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    OP_0D()
    OP_8C(0x12, 270, 300)
    Sleep(800)
    OP_8C(0x12, 135, 300)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(500)

    def lambda_10AC():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_10AC)
    Sleep(500)
    OP_22(0x17E, 0x0, 0x64)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x12, 45, 500)
    Sleep(200)
    Fade(1500)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 0)
    OP_8C(0x10, 225, 0)
    Sleep(300)

    ChrTalk(    #5 op#A
        0x13,
        "#8A#4P#3S提妲……！#2S\x02",
    )

    OP_0D()
    Sleep(300)

    def lambda_114B():
        OP_8F(0xFE, 0x1CC, 0x0, 0x578, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_114B)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 30)

    def lambda_1179():
        OP_99(0xFE, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1179)
    WaitChrThread(0x10, 0x2)
    Fade(300)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x800)
    OP_6D(3220, -100, 7120, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(64000, 0)
    OP_6E(262, 0)

    def lambda_11E0():
        OP_6D(2250, -100, 8070, 800)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_11E0)

    def lambda_11F8():
        OP_6C(18000, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_11F8)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x8)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 34)
    SetChrSubChip(0x14, 7)
    SetChrPos(0x14, -9000, 0, 4980, 90)

    def lambda_1232():
        OP_96(0xFE, 0x0, 0x0, 0x1374, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1232)
    Sleep(400)

    def lambda_1255():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1255)

    ChrTalk(    #6 op#A op#5
        0x14,
        "#8A#3S#5P喝……！！#2S\x05\x02",
    )

    WaitChrThread(0x14, 0x1)

    def lambda_128D():

        label("loc_128D")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_128D")

    QueueWorkItem2(0x12, 2, lambda_128D)

    def lambda_129E():

        label("loc_129E")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_129E")

    QueueWorkItem2(0x13, 2, lambda_129E)
    OP_23(0x17E)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    SetChrFlags(0x10, 0x20)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 31)

    def lambda_12CB():
        OP_8F(0xFE, 0x11F8, 0x320, 0x1310, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12CB)
    PlayEffect(0x1, 0xFF, 0x14, 2000, 1000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)

    def lambda_132C():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_132C)
    WaitChrThread(0x10, 0x1)
    Sleep(200)

    def lambda_1350():
        OP_6D(-670, -100, 8140, 400)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1350)

    def lambda_1368():
        OP_6C(323000, 400)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1368)
    OP_8C(0x10, 270, 500)
    SetChrSubChip(0x14, 7)
    SetChrFlags(0x14, 0x4)

    def lambda_1389():
        OP_96(0xFE, 0xC94, 0x0, 0x1374, 0x9C4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1389)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #7 op#A op#5
        0x14,
        "#10A#3S#1P嘿……！！#2S\x05\x02",
    )

    Sleep(100)

    def lambda_13DA():
        OP_99(0xFE, 0x7, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_13DA)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    PlayEffect(0x1, 0xFF, 0x14, 2000, 500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_143F():
        OP_8F(0xFE, 0x15E0, 0x320, 0x1310, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_143F)

    def lambda_145A():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_145A)
    Sleep(1000)
    Sleep(300)
    Fade(500)
    OP_6D(9000, 200, 8390, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0x3D3, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(500)
    OP_23(0x3DC)
    OP_22(0xF5, 0x0, 0x50)
    SetChrChipByIndex(0x10, 32)
    SetChrSubChip(0x10, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1520():
        OP_6D(9000, -100, 8390, 300)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1520)
    OP_0D()
    OP_20(0x7D0)
    Sleep(1000)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    OP_82(0x6, 0x2)
    Sleep(1500)

    ChrTalk(    #8
        0x14,
        "#1464F呼，赶上了吗……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 8)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x14, 0x4)
    OP_0D()
    Sleep(300)

    def lambda_159F():
        OP_6D(-1600, -100, 5800, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_159F)

    def lambda_15B7():
        OP_67(0, 3780, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_15B7)

    def lambda_15CF():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_15CF)

    def lambda_15DF():
        OP_6C(320000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_15DF)

    def lambda_15EF():
        OP_6E(239, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_15EF)
    OP_8C(0x14, 180, 500)

    def lambda_1606():
        OP_8E(0xFE, 0x9D8, 0x0, 0x910, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1606)
    WaitChrThread(0x14, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x13, 0x2)

    def lambda_162E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_162E)
    OP_8C(0x14, 270, 400)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #9
        0x14,
        "#1462F#12P大家，都没受伤吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x13,
        (
            "#1453F#5P嗯嗯，我和提妲没事……\x02\x03",

            "但是………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16BB():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_16BB)
    Sleep(300)
    TurnDirection(0x14, 0x106, 300)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)

    def lambda_16F1():
        TurnDirection(0xFE, 0x106, 600)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_16F1)
    Sleep(500)

    ChrTalk(    #11
        0x12,
        "#065F#11P啊…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(2180, 0, -720, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #12
        0x12,
        "#566F#3S阿加特大哥哥！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_17AA():
        OP_6D(160, 0, -5900, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_17AA)

    def lambda_17C2():
        OP_67(0, 5680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17C2)

    def lambda_17DA():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_17DA)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)

    def lambda_17F4():
        OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0x820, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17F4)
    WaitChrThread(0x12, 0x1)

    def lambda_1814():
        OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0xFFFFE9BC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1814)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    Sleep(300)

    ChrTalk(    #13
        0x12,
        (
            "#567F#5P……阿加特大哥哥！\x01",
            "#3S………阿加特大哥哥！！#2S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x106,
        "#4P#40W…………………………\x02",
    )

    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    OP_0D()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #15
        0x12,
        (
            "#069F#5P#40W………………呜……\x02\x03",

            "怎、怎么会……\x01",
            "因为我……\x02\x03",

            "都怪我………\x01",
            "……阿加特大哥哥……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x106,
        "#4P#40W…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_196A():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_196A)

    ChrTalk(    #17
        0x12,
        (
            "#562F#5P#40W对……对、对不起…………\x02\x03",

            "……我总是\x01",
            "任性妄为……\x01",
            "给阿加特大哥哥添麻烦……\x02\x03",

            "#069F每次都是这样……\x01",
            "才让阿加特大哥哥，碰到这种事……\x02\x03",

            "都是……\x01",
            "因为我太任性……\x02\x03",

            "说、说什么\x01",
            "想接近玲……\x02",
        )
    )

    Jump("loc_1A6A")

    label("loc_1A6A")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #18
        0x12,
        (
            "#567F#5P明明什么也做不到……\x01",
            "却想要实现无法实现的愿望！\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1ACB():
        OP_9E(0xFE, 0x5, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1ACB)
    Sleep(1000)

    ChrTalk(    #19
        0x12,
        (
            "#562F#5P#40W我不想\x01",
            "变成这样的……\x02\x03",

            "我不希望\x01",
            "发生这种事的……\x02\x03",

            "#069F但是……但是………！\x02",
        )
    )

    Jump("loc_1B61")

    label("loc_1B61")

    CloseMessageWindow()
    WaitChrThread(0x24, 0x2)

    def lambda_1B6D():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1B6D)
    Sleep(1000)

    ChrTalk(    #20
        0x106,
        "#056F#4P……呜…………\x02",
    )

    CloseMessageWindow()

    def lambda_1BAF():
        OP_99(0xFE, 0x0, 0x1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1BAF)
    WaitChrThread(0x106, 0x2)
    Sleep(300)

    ChrTalk(    #21
        0x106,
        (
            "#552F#4P吵……吵死了……\x02\x03",

            "脑袋里哐哐地响。\x01",
            "别那么大声叫喊啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x64, 1400, 0x2, 0x7, 0x64, 0x1)
    Sleep(800)
    Fade(100)
    SetChrChipByIndex(0x12, 36)
    SetChrSubChip(0x12, 1)
    Sleep(300)

    ChrTalk(    #22
        0x12,
        (
            "#565F#5P#40W啊………………\x02\x03",

            "阿……阿加特……大哥哥……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        (
            "#057F#4P哼，\x01",
            "我怎么可能这么容易倒下……\x02\x03",

            "#056F………………好痛…………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)

    def lambda_1CF6():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_1CF6)

    def lambda_1D10():
        OP_99(0xFE, 0x1, 0x4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1D10)
    WaitChrThread(0x106, 0x2)
    OP_44(0x106, 0x3)
    Sleep(300)
    OP_43(0x14, 0x0, 0x0, 0x5)
    SetChrPos(0x15, -60, 0, 2700, 180)
    SetChrPos(0x10, 4600, 800, 4880, 225)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)

    ChrTalk(    #24
        0x106,
        (
            "#551F#4P真是的……\x01",
            "力量真大啊……\x02\x03",

            "还好用重剑\x01",
            "挡住了斩击……\x02\x03",

            "#556F嘿，要是正面挨一下，\x01",
            "现在早就上西天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        (
            "#069F#5P#40W……呜………………\x01",
            "…………呜…………\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x106, 6)
    Sleep(200)
    OP_62(0x106, 0xFA, 1750, 0x28, 0x2B, 0x64, 0x2)
    Sleep(500)

    ChrTalk(    #26
        0x106,
        (
            "#055F#4P都、都说\x01",
            "没什么大碍啦！\x02\x03",

            "别在那抽抽嗒嗒的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        (
            "#562F#5P#40W但、但是都怪我……\x02\x03",

            "#069F呜哇…………\x01",
            "阿加特大哥哥对不起……！\x02\x03",

            "我、我…………\x02\x03",

            "……我……\x01",
            "再也不做这种事了………\x02\x03",

            "所、所以…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#053F#4P…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x106,
        (
            "#054F#4P#3S这种程度\x01",
            "你就想放弃吗！！#2S\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x64, 1400, 0x2, 0x7, 0x64, 0x1)
    Sleep(1000)

    ChrTalk(    #30
        0x12,
        "#065F#5P#40W……咦………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        (
            "#057F#4P别这么简单放弃啊。\x02\x03",

            "你不是想\x01",
            "接近那个叫玲的小鬼吗。\x02\x03",

            "那个胡作非为的小丫头，\x01",
            "你不是想更了解她吗。\x02\x03",

            "#053F……别放弃啊。\x02",
        )
    )

    Jump("loc_20A5")

    label("loc_20A5")

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        "#063F#5P#40W阿加特……大哥哥……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x106, 4)
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrSubChip(0x106, 7)
    Sleep(1500)

    ChrTalk(    #33
        0x106,
        (
            "#053F#4P……我呢，提妲。\x01",
            "曾经度过了颓废的十年。\x02\x03",

            "真的是相当颓废的十年，\x01",
            "但是我从来\x01",
            "没有舍弃过这个。\x02\x03",

            "绝对不会舍弃的。\x02\x03",

            "#051F………………只要这样就好。\x02\x03",

            "正因为如此，\x01",
            "我现在才会成为游击士。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0xC8, 1600, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)
    SetChrSubChip(0x106, 4)
    Sleep(500)

    ChrTalk(    #34
        0x106,
        (
            "#053F#4P就是因为\x01",
            "有无论如何也无法舍弃的东西。\x02\x03",

            "无论怎样努力忘却，\x01",
            "也永远忘不了的东西。\x02\x03",

            "#556F………………提妲。\x02\x03",

            "你不是……\x01",
            "也找到了这样的东西吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #35
        0x12,
        (
            "#064F#5P#40W………啊…………………\x02\x03",

            "#062F（没错…………………）\x02\x03",

            "（……我…………\x01",
            "  我还是……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x64, 1400, 0x18, 0x1B, 0xFA, 0x2)
    Sleep(2500)

    ChrTalk(    #36
        0x12,
        (
            "#561F#5P……那、那个，\x01",
            "阿加特大哥哥…………\x02\x03",

            "#062F我、我……不会放弃！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x106, 6)
    OP_0D()
    Sleep(300)

    ChrTalk(    #37
        0x12,
        (
            "#062F#5P现在我不能\x01",
            "一直哭个不停了……\x02\x03",

            "因为我已经决定\x01",
            "要做自己力所能及的事。\x02\x03",

            "就像阿加特大哥哥是游击士一样，\x01",
            "我也算是一个研究人员！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#556F#4P…………………………\x02\x03",

            "#053F……是吗……………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x106, 0x20)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x106, 0x800)
    ClearChrFlags(0x106, 0x4)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x106, -580, 0, -6740, 0)
    OP_0D()
    OP_8C(0x106, 0, 400)
    Sleep(300)

    ChrTalk(    #39
        0x12,
        (
            "#064F#5P………………？？？\x02\x03",

            "阿加特大哥哥……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        (
            "#556F#4P……没什么啦。\x01",
            "你这小鬼…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2567():
        OP_6D(160, 0, -5200, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_2567)
    OP_8E(0x106, 0xFFFFFE34, 0x0, 0xFFFFE778, 0x3E8, 0x0)
    OP_8C(0x106, 315, 400)
    WaitChrThread(0x24, 0x0)
    OP_22(0x8F, 0x0, 0x64)
    Fade(1000)
    SetChrChipByIndex(0x106, 35)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0x106, 0x2)
    SetChrPos(0x106, -530, 0, -6010, 225)
    SetChrFlags(0x12, 0x8)
    OP_0D()
    Sleep(500)
    Sleep(500)
    OP_20(0x0)
    OP_22(0xF0, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    Sleep(2000)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0xFA, 2000, 0x2, 0x7, 0x64, 0x1)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    SetChrFlags(0x10, 0x800)
    OP_8C(0x10, 280, 0)

    def lambda_264C():
        OP_6D(1920, 0, -800, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_264C)

    def lambda_2664():
        OP_67(0, 4300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2664)

    def lambda_267C():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_267C)
    Sleep(500)
    SetChrPos(0x106, -460, 0, -6280, 315)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x12, 0x8)

    def lambda_26B6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_26B6)
    WaitChrThread(0x24, 0x0)
    Fade(500)
    OP_C4(0x1, 0x400)
    OP_0D()
    Sleep(1000)

    def lambda_26DA():

        label("loc_26DA")

        TurnDirection(0xFE, 0x106, 500)
        OP_48()
        Jump("loc_26DA")

    QueueWorkItem2(0x12, 2, lambda_26DA)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_26FD():
        OP_8E(0xFE, 0x244, 0x0, 0xFFFFE9BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_26FD)
    WaitChrThread(0x106, 0x1)
    OP_44(0x12, 0x2)

    def lambda_2721():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2721)
    Sleep(150)
    OP_8C(0x12, 0, 500)
    Sleep(300)

    ChrTalk(    #41
        0x106,
        (
            "#055F你、你们怎么回事啊。\x01",
            "一直站在那里……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14)
    OP_63(0x13)
    OP_63(0x15)
    Sleep(500)

    ChrTalk(    #42
        0x13,
        (
            "#1457F唉……………………\x02\x03",

            "#1453F哎呀呀，\x01",
            "这下可没办法了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x15,
        (
            "#104F所以我不是说过了吗。\x02\x03",

            "这个红毛啊，\x01",
            "虽然笨拙别扭迟钝性格又差……\x02\x03",

            "#100F但还是有优点的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13,
        (
            "#1457F虽然还在准备中……\x02\x03",

            "#1832F不过，看来要立刻实行\x01",
            "红毛『实验』第二阶段了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #45
        0x106,
        "#055F喂，你说什么呢……？\x02",
    )

    CloseMessageWindow()

    def lambda_28E5():
        OP_6D(2250, 0, -2600, 2500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_28E5)

    def lambda_28FD():

        label("loc_28FD")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_28FD")

    QueueWorkItem2(0x12, 2, lambda_28FD)

    def lambda_290E():
        OP_8E(0xFE, 0x244, 0x0, 0xFFFFF218, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_290E)
    WaitChrThread(0x14, 0x1)
    OP_44(0x12, 0x2)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #46
        0x14,
        (
            "#1460F#5P我对你刮目相看了，阿加特。\x02\x03",

            "你按照我们的约定，\x01",
            "让提妲平安无事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x106,
        "#052F哦、哦…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x14,
        "#1461F#5P傍晚的时候来我们家吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#055F啊…………？\x02\x03",

            "不，一开始不是已经\x01",
            "约好要去吃晚饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14,
        "#1465F#5P#40W…………我们很欢迎您哦？\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_2A79():
        OP_8F(0xFE, 0x244, 0x0, 0xFFFFE890, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2A79)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    ChrTalk(    #51
        0x106,
        (
            "#055F（为、为什么\x01",
            "  突然开始说敬语了……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x106, 500)
    Sleep(300)

    ChrTalk(    #52
        0x12,
        (
            "#560F#6P啊，阿加特大哥哥……！\x02\x03",

            "#561F那个……\x01",
            "刚才真是谢谢你了。\x02\x03",

            "我又被你\x01",
            "保护了一次……\x02",
        )
    )

    Jump("loc_2B5A")

    label("loc_2B5A")

    CloseMessageWindow()
    TurnDirection(0x106, 0x12, 500)
    Sleep(300)

    ChrTalk(    #53
        0x106,
        (
            "#055F#11P这种事怎样都无所谓啦！\x02\x03",

            "#551F话、话说回来提妲，\x01",
            "不好意思今晚的晚饭就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        (
            "#560F#6P嗯，\x01",
            "是蘑菇山菜火锅和全海草汤。\x02\x03",

            "#066F爸爸妈妈\x01",
            "看来也对阿加特大哥哥\x01",
            "有所了解了……\x02\x03",

            "#067F嘿嘿，\x01",
            "今天大家就一起吃火锅吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x106,
        (
            "#556F#11P#40W是、是啊，哈哈哈……\x02\x03",

            "#551F怎么这么开心啊，喂……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    Sleep(2000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_786 end

    def Function_5_2CF7(): pass

    label("Function_5_2CF7")

    OP_8E(0xFE, 0x5C8, 0x0, 0x578, 0x3E8, 0x0)
    OP_8C(0x14, 180, 400)
    Return()

    # Function_5_2CF7 end

    def Function_6_2D13(): pass

    label("Function_6_2D13")

    OP_24(0x3DC, 0x46)
    Sleep(200)
    OP_24(0x3DC, 0x3C)
    Sleep(200)
    OP_24(0x3DC, 0x32)
    Sleep(200)
    OP_24(0x3DC, 0x28)
    Sleep(200)
    OP_24(0x3DC, 0x1E)
    Sleep(200)
    OP_24(0x3DC, 0x14)
    Sleep(200)
    OP_24(0x3DC, 0xA)
    Sleep(200)
    OP_24(0x3DC, 0x0)
    OP_23(0x3DC)
    Return()

    # Function_6_2D13 end

    def Function_7_2D5A(): pass

    label("Function_7_2D5A")

    OP_22(0x3DC, 0x1, 0x0)
    Sleep(100)
    OP_24(0x3DC, 0xA)
    Sleep(100)
    OP_24(0x3DC, 0x14)
    Sleep(100)
    OP_24(0x3DC, 0x1E)
    Sleep(100)
    OP_24(0x3DC, 0x28)
    Sleep(100)
    OP_24(0x3DC, 0x32)
    Sleep(100)
    OP_24(0x3DC, 0x3C)
    Sleep(100)
    OP_24(0x3DC, 0x46)
    Sleep(100)
    OP_24(0x3DC, 0x50)
    Return()

    # Function_7_2D5A end

    def Function_8_2DA8(): pass

    label("Function_8_2DA8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x57)
    OP_31(0x5, 0xFC, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    LoadEffect(0x0, "monster\\ms04220b.eff")
    LoadEffect(0x1, "monster\\ms30109a.eff")
    LoadEffect(0x2, "monster\\ms04220.eff")
    OP_6D(7160, 0, 1720, 0)
    OP_67(0, 5980, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 4100, 800, 1000, 90)
    SetChrPos(0x106, 8119, 0, 1000, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6140, 0, -5220, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13760, 0, -1400, 90)
    OP_A1(0x18, 0x8)
    SetChrPos(0x18, 4600, 0, 8950, 0)
    OP_A1(0x19, 0x9)
    SetChrPos(0x19, 3200, 0, 8950, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2EFA"),
        (0, "loc_2F07"),
        (SWITCH_DEFAULT, "loc_2F14"),
    )


    label("loc_2EFA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F14")

    label("loc_2F07")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F14")

    label("loc_2F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆赢了\x01",      # 0
            "◆输了\x01",      # 1
        )
    )

    Jump("loc_2F4E")

    label("loc_2F4E")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_2F5F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2F70"),
        (0, "loc_2F7D"),
        (SWITCH_DEFAULT, "loc_2F8A"),
    )


    label("loc_2F70")

    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 3)
    Jump("loc_2F8A")

    label("loc_2F7D")

    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)
    Jump("loc_2F8A")

    label("loc_2F8A")


    def lambda_2F90():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2F90)
    FadeToBright(2000, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2FB5"),
        (0, "loc_3284"),
        (SWITCH_DEFAULT, "loc_3589"),
    )


    label("loc_2FB5")


    ChrTalk(    #56
        0x12,
        (
            "#065F啊，阿加特大哥哥！\x01",
            "你没事吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x106,
        (
            "#053F#11P啊啊，\x01",
            "这点小事没什么啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()

    def lambda_3031():
        OP_6D(9160, 0, 1720, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_3031)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #58
        0x13,
        (
            "#1833F#1P呼呼……㈱\x02\x03",

            "#1831F呼呼呼呼……㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 500)
    Sleep(300)

    ChrTalk(    #59
        0x13,
        (
            "#1458F#3P感觉怎么样？\x01",
            "阿加特·科洛斯纳……\x02\x03",

            "这就是我导力装甲的力量！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #60
        0x13,
        "#1834F#3P#3S知·道·厉·害·了·吧！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    Sleep(300)

    def lambda_3144():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_3144)

    def lambda_3154():
        OP_67(0, 4980, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_3154)

    def lambda_316C():
        OP_8E(0xFE, 0x1FB7, 0x0, 0xFFFFFC40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_316C)
    Sleep(600)

    def lambda_318C():
        OP_8E(0xFE, 0x17FC, 0x0, 0xFFFFFC40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_318C)

    ChrTalk(    #61
        0x106,
        (
            "#555F#5P操纵的人\x01",
            "不是提妲吗……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x106, 500)
    Sleep(300)

    ChrTalk(    #62
        0x14,
        (
            "#1461F#6P哈哈哈……\x02\x03",

            "#1460F总而言之，\x01",
            "这次比赛是导力装甲的胜利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x13,
        (
            "#1832F#12P啧…………\x01",
            "这就结束了啊……\x02\x03",

            "好无聊，好无聊啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3589")

    label("loc_3284")


    ChrTalk(    #64
        0x106,
        (
            "#051F#11P……哼。\x01",
            "嗯，也就这样了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()

    def lambda_32CF():
        OP_6D(9160, 0, 1720, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_32CF)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #65
        0x13,
        "#1830F#1P唔、唔唔唔唔唔…………！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 500)
    Sleep(300)

    ChrTalk(    #66
        0x13,
        (
            "#1459F#1P……阿加特·科洛斯纳。\x02\x03",

            "你刚才，犯规了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    Sleep(300)

    ChrTalk(    #67
        0x106,
        (
            "#052F#5P犯、犯规？\x02\x03",

            "我哪有犯规啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33AF():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_33AF)

    def lambda_33BF():
        OP_67(0, 4980, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_33BF)

    def lambda_33D7():
        OP_8E(0xFE, 0x1FB7, 0x0, 0xFFFFFC40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_33D7)
    WaitChrThread(0x13, 0x1)
    Sleep(300)

    ChrTalk(    #68
        0x13,
        "#1830F#12P不，你就是犯规了。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #69
        0x13,
        (
            "#1830F#3S#12P你用了什么\x01",
            "看不见的力量吧！！#2S\x02",
        )
    )

    OP_7C(0x0, 0x190, 0xFA0, 0x64)
    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #70
        0x106,
        "#055F#5P哪、哪有那种东西啊！\x02",
    )

    CloseMessageWindow()

    def lambda_34B5():
        OP_8E(0xFE, 0x17FC, 0x0, 0xFFFFFC40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_34B5)
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x106, 500)
    Sleep(300)

    ChrTalk(    #71
        0x14,
        (
            "#1461F#6P哈哈哈……\x02\x03",

            "#1460F总而言之，\x01",
            "这次比赛是阿加特的胜利。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 90, 500)
    Sleep(300)

    ChrTalk(    #72
        0x13,
        (
            "#1830F#3S#5P瞪～！！#2S\x02\x03",

            "#1832F（嘀嘀咕咕，嘀嘀咕咕）……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3589")

    label("loc_3589")

    TurnDirection(0x106, 0x14, 500)
    Sleep(300)

    ChrTalk(    #73
        0x106,
        (
            "#053F#5P……喂，\x01",
            "实验就到此为止了吧。\x02\x03",

            "我就当是\x01",
            "委托完成了啊。\x02",
        )
    )

    Jump("loc_35F2")

    label("loc_35F2")

    CloseMessageWindow()
    Sleep(500)
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(    #74
        0x13,
        (
            "#1457F#11P………丹。\x01",
            "这么说来昨天……\x02\x03",

            "#1450F你不是说\x01",
            "想和这红毛小子\x01",
            "交个手看看吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    ChrTalk(    #75
        0x14,
        (
            "#1463F#6P……咦？\x02\x03",

            "#1464F啊啊……没错。\x02\x03",

            "#1465F他的事情，\x01",
            "我也从卡西乌斯先生\x01",
            "那儿听说了一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        "#052F#5P……什………！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x13, 500)
    Sleep(300)

    ChrTalk(    #77
        0x106,
        "#551F#5P（好像有种不详的预感……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x13,
        (
            "#1458F#11P呼呼……那就决定了。\x02\x03",

            "#1456F来吧，\x01",
            "赶快把武器拿出来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x14,
        (
            "#1463F#6P唔，\x01",
            "但是我觉得也不必现在就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x13,
        "#1834F#11P来吧，赶快赶快……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x14,
        (
            "#1464F#6P……知道啦。\x02\x03",

            "#1460F那么，这里就交给你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 270, 500)

    def lambda_3858():
        OP_8E(0xFE, 0xFFFFF04D, 0x0, 0xFFFFFC40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3858)
    WaitChrThread(0x14, 0x1)
    SetChrFlags(0x14, 0x8)
    TurnDirection(0x13, 0x106, 400)
    Sleep(300)

    ChrTalk(    #82
        0x13,
        (
            "#1456F#12P……话说在前头，\x01",
            "虽说丹是因为受伤才引退的，\x01",
            "不过他可是很强的哦。\x02\x03",

            "怎么说也是十年前\x01",
            "对卡西乌斯先生\x01",
            "做过棒术基础指导的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #83
        0x106,
        "#052F#5P#3S什……！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #84
        0x13,
        (
            "#1458F#12P不过，卡西乌斯先生\x01",
            "似乎是在那之后自己将棒术练到极致的。\x02\x03",

            "#1833F………即使如此，\x01",
            "他有多少实力你该知道了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        (
            "#051F#5P哼，\x01",
            "听了这种话我也不会退缩的……\x02\x03",

            "#055F……不过慢着！\x01",
            "实验已经结束了吧！？\x02\x03",

            "为什么突然\x01",
            "变成这样啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x13,
        (
            "#1459F#12P……还没呢！\x02\x03",

            "#1454F……啊啊，对了对了，\x01",
            "还要检查提妲的身体才行。\x02\x03",

            "#1835F万一要是\x01",
            "有个什么擦伤……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    Sleep(300)

    ChrTalk(    #87
        0x13,
        (
            "#1451F#11P提妲，\x01",
            "下来吧～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        "#063F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    def lambda_3B77():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3B77)
    Sleep(500)

    ChrTalk(    #89
        0x13,
        (
            "#1454F#11P提妲……？\x01",
            "怎么了？\x02",
        )
    )

    Jump("loc_3BB9")

    label("loc_3BB9")

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        (
            "#067F嗯，\x01",
            "好像出了奇怪的错误……\x02\x03",

            "#065F咦、咦…………？\x02",
        )
    )

    Jump("loc_3C0A")

    label("loc_3C0A")

    CloseMessageWindow()
    OP_21()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x10, 0x2, 0x0, 0x9)
    OP_43(0x10, 0x1, 0x0, 0xA)
    Sleep(1000)
    OP_62(0x12, 0x1C2, 2300, 0x28, 0x2B, 0x96, 0x2)

    ChrTalk(    #91
        0x12,
        "#065F怎、怎么回事啊？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x15,
        "#102F#1P唔，糟糕！！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x98)
    Sleep(500)
    OP_22(0x17E, 0x0, 0x64)
    OP_43(0x12, 0x3, 0x0, 0xB)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0xC8, 0x0)

    ChrTalk(    #93
        0x13,
        (
            "#1454F#11P这、这是……\x02\x03",

            "#1459F不好……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3D08():
        OP_8E(0xFE, 0x206C, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3D08)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 90, 500)
    Sleep(200)
    OP_22(0x2BB, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #94
        0x13,
        (
            "#1830F#6P啧…………\x01",
            "无法接受命令……！\x02\x03",

            "提妲，\x01",
            "先把系统关闭！\x02",
        )
    )

    Jump("loc_3DF7")

    label("loc_3DF7")

    CloseMessageWindow()

    ChrTalk(    #95
        0x12,
        (
            "#065F但、但是……\x02\x03",

            "它好像\x01",
            "不听使唤了……\x02",
        )
    )

    Jump("loc_3E3C")

    label("loc_3E3C")

    CloseMessageWindow()
    OP_8C(0x106, 180, 600)
    Sleep(500)
    OP_8C(0x106, 270, 600)
    Sleep(500)
    OP_8C(0x106, 180, 600)
    Sleep(300)

    ChrTalk(    #96
        0x106,
        (
            "#055F#5P喂、喂……\x01",
            "怎么回事！？\x02\x03",

            "#054F说清楚些，让我也能听懂！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    ChrTalk(    #97
        0x12,
        "#065F呃呃……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #98
        0x12,
        "#068F#3S哇啊……！？#2S\x02",
    )

    CloseMessageWindow()

    def lambda_3EFF():
        OP_6D(6200, 0, 10160, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_3EFF)

    def lambda_3F17():
        OP_67(0, 4820, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_3F17)

    def lambda_3F2F():
        OP_6B(3100, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_3F2F)
    OP_44(0x12, 0x3)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x1)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 0, 500)
    OP_82(0x7, 0x0)
    OP_44(0x10, 0x2)
    OP_22(0x187, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_3F74():
        OP_8E(0xFE, 0x1004, 0x320, 0x2008, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3F74)
    WaitChrThread(0x12, 0x1)
    OP_23(0x187)
    OP_70(0x8, 0x3C)
    OP_70(0x9, 0x3C)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_44(0x10, 0x3)
    OP_43(0x10, 0x2, 0x0, 0x9)

    def lambda_3FBA():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3FBA)
    OP_7C(0x1C2, 0x1C2, 0xBB8, 0x1F4)
    OP_22(0x1FE, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(300)
    OP_23(0x17E)
    Sleep(1000)

    def lambda_3FFC():
        OP_6D(6000, 0, 8240, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_3FFC)

    def lambda_4014():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4014)

    def lambda_4024():
        OP_8E(0xFE, 0x10A4, 0x0, 0x10F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4024)
    OP_22(0x17E, 0x0, 0x64)
    Sleep(100)
    OP_23(0x17E)
    Sleep(300)
    OP_22(0x17E, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x12, 500)
    Sleep(300)

    ChrTalk(    #99
        0x106,
        (
            "#054F…………提妲！！\x02\x03",

            "这家伙，失控了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        "#065F#5P阿加特大哥哥，那个……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #101
        0x12,
        "#068F#5P#3S快逃啊！！#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_59()
    OP_8C(0x12, 180, 700)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)

    def lambda_411E():
        OP_9E(0xFE, 0x19, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_411E)

    def lambda_4138():

        label("loc_4138")

        OP_7C(0x32, 0x32, 0xBB8, 0x7D0)
        OP_48()
        Jump("loc_4138")

    QueueWorkItem2(0x12, 3, lambda_4138)
    Sleep(300)

    ChrTalk(    #102
        0x106,
        "#550F#12P……啧…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x106)
    OP_22(0xD5, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    Sleep(500)

    def lambda_4198():
        OP_6D(5940, 0, 7020, 800)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_4198)

    def lambda_41B0():
        OP_67(0, 3660, -10000, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_41B0)

    def lambda_41C8():
        OP_6B(2540, 800)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_41C8)

    def lambda_41D8():
        OP_6C(36000, 800)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_41D8)

    def lambda_41E8():
        OP_6E(312, 800)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_41E8)
    SetChrChipByIndex(0x106, 18)
    SetChrSubChip(0x106, 0)

    def lambda_4202():
        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_4202)

    def lambda_4212():
        OP_96(0xFE, 0x10A4, 0x0, 0x514, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4212)
    WaitChrThread(0x106, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x7, 0x0)
    OP_44(0x10, 0x2)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)
    OP_22(0x187, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_4272():
        OP_8E(0xFE, 0x1004, 0x320, 0xC80, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4272)

    def lambda_428D():
        OP_6D(5940, 0, 4019, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_428D)

    def lambda_42A5():
        OP_6B(1900, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_42A5)
    Sleep(400)
    OP_44(0x12, 0xFF)
    OP_44(0x10, 0xFF)
    OP_23(0x187)
    OP_44(0x24, 0xFF)
    Battle(0x3B9, 0x300003, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_2DA8 end

    def Function_9_42E9(): pass

    label("Function_9_42E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4337")
    PlayEffect(0x1, 0x7, 0x12, 0, 500, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_22(0x29, 0x0, 0x50)
    OP_83(0x7, 0x2)
    Sleep(1000)
    Jump("Function_9_42E9")

    label("loc_4337")

    Return()

    # Function_9_42E9 end

    def Function_10_4338(): pass

    label("Function_10_4338")

    Sleep(2000)
    PlayEffect(0x0, 0x6, 0x12, 1000, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    PlayEffect(0x0, 0x5, 0x12, -1000, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x0, 0x4, 0x12, 500, 1000, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x0, 0x3, 0x12, -500, 1000, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_4338 end

    def Function_11_4421(): pass

    label("Function_11_4421")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44AB")

    def lambda_4430():
        OP_7C(0x32, 0x32, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4430)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)

    def lambda_4452():
        OP_9E(0xFE, 0x0, 0x28, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4452)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4475")
    Jump("loc_44AB")

    label("loc_4475")

    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)

    def lambda_4485():
        OP_9E(0xFE, 0x28, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4485)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_44A8")
    Jump("loc_44AB")

    label("loc_44A8")

    Jump("Function_11_4421")

    label("loc_44AB")

    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_4421 end

    def Function_12_44B6(): pass

    label("Function_12_44B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "monster\\ms04220.eff")
    OP_6D(-660, 0, 1260, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -900, 800, 1000, 180)
    SetChrPos(0x106, -2620, 0, 1000, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -2000, 0, -1120, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #103
        0x14,
        (
            "#1464F#12P最后为了观察综合能力，\x01",
            "准备进行模拟战斗。\x02\x03",

            "#1462F双方，各就各位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x12,
        "#062F#5P是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        "#053F#5P是是。\x02",
    )

    CloseMessageWindow()

    def lambda_463A():
        OP_6D(-2000, 0, 1860, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_463A)

    def lambda_4652():
        OP_67(0, 5540, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4652)

    def lambda_466A():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_466A)

    def lambda_467A():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_467A)

    def lambda_468A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_468A)
    OP_8C(0x12, 90, 200)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)
    OP_22(0x187, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_46BA():
        OP_8E(0xFE, 0x578, 0x320, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_46BA)

    def lambda_46D5():
        OP_8E(0xFE, 0xFFFFEAE8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_46D5)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_23(0x187)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)

    def lambda_470B():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_470B)
    WaitChrThread(0x106, 0x1)

    def lambda_471E():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_471E)
    Sleep(500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #106
        0x13,
        (
            "#1457F……我想你应该知道，\x01",
            "你只能瞄准导力装甲。\x02\x03",

            "#1457F要是敢伤提妲一根汗毛\x02\x01",

            "#1459F……………………就是立即处死。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x106,
        (
            "#551F#5P…………我都说过\x01",
            "知道啦。\x02",
        )
    )

    Jump("loc_480A")

    label("loc_480A")

    CloseMessageWindow()

    ChrTalk(    #108
        0x14,
        "#1462F……准备好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#053F#5P啊啊…………\x02\x03",

            "#051F#3S随时奉陪！！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_41(0x5, 0x0, 0xFF)
    OP_31(0x5, 0x10, 0x5A)
    OP_31(0x5, 0x5, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_35(0x5, 0xFFFF)
    OP_34(0x5, 0xFFFF)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x101)
    OP_37(0x5, 0x7F, 0x0)
    OP_37(0x5, 0x7F, 0x2)
    OP_41(0x5, 0x3E8, 0xFF)
    OP_34(0x5, 0x82)
    OP_34(0x5, 0x83)
    OP_34(0x5, 0x57)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0xA)
    OP_3E(0x207, 10)
    OP_3E(0x1F3, 10)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3B8, 0x300003, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_44B6 end

    def Function_13_48F5(): pass

    label("Function_13_48F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "monster\\ms04220.eff")
    OP_72(0x414, 0x0)
    ExitThread()
    OP_72(0x417, 0x0)
    ExitThread()
    OP_72(0x418, 0x0)
    ExitThread()
    OP_72(0x419, 0x0)
    ExitThread()
    OP_72(0x41A, 0x0)
    ExitThread()
    OP_72(0x41B, 0x0)
    ExitThread()
    OP_72(0x41C, 0x0)
    ExitThread()
    OP_72(0x41D, 0x0)
    ExitThread()
    OP_72(0x41E, 0x0)
    ExitThread()
    OP_72(0x41F, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x216, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_6D(-5460, 0, -1060, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(45000, 0)
    OP_6E(448, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -11640, 800, 840, 135)
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x106, -11140, 0, -2100, 45)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -9060, 0, -1000, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 90)
    OP_A1(0x1A, 0x18)
    OP_A1(0x1B, 0x19)
    OP_A1(0x1C, 0x1A)
    OP_A1(0x1D, 0x1B)
    OP_A1(0x1E, 0x1C)
    OP_A1(0x1F, 0x1D)
    OP_A1(0x20, 0x1E)
    OP_A1(0x21, 0x1F)
    SetChrPos(0x1C, -4000, 0, -6600, 0)
    SetChrPos(0x1A, -4000, 0, -5400, 0)
    SetChrPos(0x1E, -5300, 0, -5400, 0)
    SetChrPos(0x20, -5300, 0, -6600, 0)
    SetChrPos(0x1D, -4000, 0, 3400, 0)
    SetChrPos(0x1B, -4000, 0, 4600, 0)
    SetChrPos(0x1F, -5300, 0, 4600, 0)
    SetChrPos(0x21, -5300, 0, 3400, 0)
    OP_A1(0x22, 0x14)
    OP_A1(0x23, 0x17)
    SetChrPos(0x22, -4300, 0, -6000, 0)
    SetChrPos(0x23, -4300, 0, 4000, 0)

    def lambda_4B2F():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4B2F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x24, 0x2)
    Sleep(500)
    Fade(1000)
    OP_6D(-7700, 0, -1000, 0)
    OP_67(0, 6780, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(90000, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #110
        0x106,
        "#052F#12P喂，这是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x14,
        (
            "#1460F#5P下一项实验是精密控制测试。\x02\x03",

            "将四种颜色的桶罐，\x01",
            "分别放到对应颜色的砖块上。\x02\x03",

            "#1461F这比看起来要困难，\x01",
            "你可不要大意哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x106,
        (
            "#053F#12P………………………………\x02\x03",

            "#552F（要是这个输了，\x01",
            "  一定会被他们说\x01",
            "  『身为人类还这么笨』之类的话……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x14,
        "#1460F#5P那么就开始吧。       \x02",
    )

    CloseMessageWindow()

    def lambda_4D06():
        OP_6D(-5700, 0, -1000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_4D06)
    OP_43(0x12, 0x3, 0x0, 0xE)
    OP_8C(0x106, 135, 500)

    def lambda_4D2C():
        OP_8E(0xFE, 0xFFFFE37C, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4D2C)
    Sleep(1000)

    def lambda_4D4C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4D4C)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 90, 500)
    WaitChrThread(0x12, 0x3)
    Sleep(1000)

    ChrTalk(    #114
        0x14,
        "#1462F#3S……开始！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-3040, 0, -1000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(90000, 0)
    OP_6E(430, 0)
    SetChrPos(0x21, -1660, 0, 7000, 0)
    SetChrPos(0x1D, -7560, 0, 7000, 0)
    SetChrPos(0x1B, -7560, 0, 5260, 0)
    SetChrPos(0x1F, -4000, 0, 3400, 0)
    SetChrPos(0x20, -1660, 0, -3000, 0)
    SetChrPos(0x1E, -1660, 0, -9000, 0)
    SetChrPos(0x1A, -7560, 0, -9000, 0)
    SetChrPos(0x1C, -5300, 0, -5400, 0)
    SetChrPos(0x106, -5240, 0, -6020, 315)
    SetChrPos(0x12, -5600, 800, 7000, 180)

    def lambda_4E96():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFF1DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4E96)

    def lambda_4EB1():
        OP_8F(0xFE, 0xFFFFE278, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4EB1)
    OP_43(0x12, 0x3, 0x0, 0xF)
    OP_43(0x1C, 0x3, 0x0, 0x10)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x1C, 0x1)
    Sleep(500)

    def lambda_4EF3():
        OP_8F(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFEFE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4EF3)
    WaitChrThread(0x106, 0x1)
    Sleep(300)

    ChrTalk(    #115
        0x106,
        "#051F#11P哼，小菜一碟……\x02",
    )

    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x12, 0x3)
    Fade(500)
    OP_6D(0, 0, -40, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(90000, 0)
    OP_6E(284, 0)
    SetChrPos(0x13, 7000, 0, -5000, 90)
    SetChrPos(0x106, -8000, 0, -1660, 90)
    SetChrPos(0x14, -8960, 0, -400, 90)
    OP_0D()
    Sleep(300)

    ChrTalk(    #116
        0x13,
        "#1454F#6P哎呀，不错的数据嘛。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 315, 400)

    def lambda_4FF0():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFF9E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4FF0)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 315, 400)

    ChrTalk(    #117
        0x13,
        (
            "#1451F#11P提妲，干得好。\x01",
            "操纵也越来越熟练了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x12,
        (
            "#067F#6P嘿嘿……\x02\x03",

            "#560F不过我想，\x01",
            "这应该是爸爸的功劳吧。\x02\x03",

            "传动器的微调\x01",
            "做得非常完美，\x01",
            "所以操作起来才能得心应手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x13,
        (
            "#1451F#11P呵呵，是啊……\x02\x03",

            "丹做这些事\x01",
            "实在是很能干呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x12,
        (
            "#067F#6P嗯，这个手臂的所有动作\x01",
            "似乎都有加速度控制……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 90, 400)
    Sleep(300)

    ChrTalk(    #121
        0x106,
        "#551F……喂，无视我吗。\x02",
    )

    CloseMessageWindow()

    def lambda_5199():
        OP_6D(-3340, 0, -1000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_5199)

    def lambda_51B1():
        OP_67(0, 4540, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_51B1)

    def lambda_51C9():
        OP_6B(2980, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_51C9)
    WaitChrThread(0x24, 0x0)
    OP_8C(0x14, 135, 400)
    Sleep(300)

    ChrTalk(    #122
        0x14,
        (
            "#1460F#6P哈哈，\x01",
            "实验的目的纯粹是收集数据嘛。\x02\x03",

            "#1464F不过…………\x02\x03",

            "#1465F…………接下来就不一样了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    Sleep(300)

    ChrTalk(    #123
        0x13,
        (
            "#1458F#12P呼呼呼呼呼…………\x02\x03",

            "#1835F来吧，现在才是正式开始呢！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x106, 0x4)
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_48F5 end

    def Function_14_5348(): pass

    label("Function_14_5348")

    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_22(0x187, 0x0, 0x64)
    OP_8C(0x12, 45, 400)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_536B():
        OP_8E(0xFE, 0xFFFFE2B4, 0x320, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_536B)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_8C(0x12, 90, 400)
    OP_23(0x187)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    Return()

    # Function_14_5348 end

    def Function_15_539E(): pass

    label("Function_15_539E")

    OP_43(0x10, 0x3, 0x0, 0x13)
    OP_22(0x187, 0x1, 0x3C)

    def lambda_53B0():
        OP_8E(0xFE, 0xFFFFEA20, 0x320, 0x10A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_53B0)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 135, 400)

    def lambda_53D7():
        OP_8E(0xFE, 0xFFFFF358, 0x320, 0x744, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_53D7)

    def lambda_53F2():
        OP_8F(0xFE, 0xFFFFF984, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_53F2)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_23(0x187)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_15_539E end

    def Function_16_5419(): pass

    label("Function_16_5419")

    OP_22(0x174, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x174, 0x0, 0x64)
    Return()

    # Function_16_5419 end

    def Function_17_5429(): pass

    label("Function_17_5429")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_72(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x216, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_6D(-4460, 0, -1060, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(90000, 0)
    OP_6E(448, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -9960, 800, -200, 90)
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x106, -9960, 0, -1960, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -6560, 0, -1100, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 90)
    LoadEffect(0x0, "map\\mp021_00.eff")
    LoadEffect(0x1, "map\\mp065_01.eff")
    LoadEffect(0x2, "monster\\ms04220.eff")
    ClearMapFlags(0x10)

    def lambda_557C():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_557C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x24, 0x2)
    Sleep(500)
    Fade(1000)
    OP_6D(-8700, 0, 200, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #124
        0x14,
        (
            "#1460F第一项实验是行走测试。\x01",
            "要绕实验场外圈三周。\x02\x03",

            "#1460F途中还有障碍物，\x01",
            "要小心哦。\x02\x03",

            "阿加特，准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x106,
        (
            "#053F#6P……啊啊，赶快开始吧。\x02\x03",

            "#555F我姑且也算是来处理工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x14,
        (
            "#1461F呵呵，那倒是。\x02\x03",

            "#1460F那么各就各位。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x12)
    Sleep(400)

    def lambda_570A():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_570A)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 500)
    Sleep(1000)

    ChrTalk(    #127
        0x14,
        "#1462F#3S#40W预备，#1720W #40W开始！#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x14)
    OP_43(0x106, 0x3, 0x0, 0x15)
    Sleep(1000)
    Fade(500)
    OP_6D(-4500, 0, -6200, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(1500)
    Fade(300)
    OP_6D(2250, 0, 3010, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    Sleep(2000)

    def lambda_5811():
        OP_6D(1880, 0, 5150, 500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_5811)

    def lambda_5829():
        OP_6B(2840, 500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5829)

    def lambda_5839():
        OP_6C(325000, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5839)
    Sleep(1300)
    Fade(300)
    OP_6D(-9090, 0, 620, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x12, 0x3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-8700, 0, -200, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x106, 37)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x12, -8960, 800, -3400, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #128
        0x106,
        (
            "#551F#5P呼、呼…………\x02\x03",

            "#055F喂，刚才那是怎么回事！？\x01",
            "怎么跳起来了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x12,
        (
            "#562F对、对不起\x01",
            "阿加特大哥哥……\x02\x03",

            "不过，\x01",
            "是妈妈说最后\x01",
            "要跳起来到终点…………\x02",
        )
    )

    Jump("loc_59BE")

    label("loc_59BE")

    CloseMessageWindow()

    ChrTalk(    #130
        0x13,
        "#1456F呃……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x106,
        "#555F#5P（那家伙………）\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    OP_8C(0x106, 90, 400)
    Sleep(300)

    ChrTalk(    #132
        0x14,
        (
            "#1461F#11P阿加特，\x01",
            "跳跃并不算犯规哦。\x02\x03",

            "因为收集跳跃时的数据\x01",
            "也是在计划内的。\x02\x03",

            "#1465F这次应该……\x01",
            "算是你大意了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        "#552F#6P哼…………\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x106, 0x4)
    OP_71(0x415, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    SetMapFlags(0x10)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_5429 end

    def Function_18_5B1B(): pass

    label("Function_18_5B1B")

    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 45, 400)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_5B39():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B39)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_8C(0x12, 180, 400)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    Return()

    # Function_18_5B1B end

    def Function_19_5B69(): pass

    label("Function_19_5B69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BAF")
    PlayEffect(0x2, 0x3, 0x12, 0, -400, -400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Jump("Function_19_5B69")

    label("loc_5BAF")

    Return()

    # Function_19_5B69 end

    def Function_20_5BB0(): pass

    label("Function_20_5BB0")

    OP_43(0x10, 0x3, 0x0, 0x13)
    OP_22(0x187, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)

    def lambda_5BCC():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5BCC)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 90, 500)

    def lambda_5BF3():
        OP_8E(0xFE, 0xFFFFF6F0, 0x320, 0xFFFFE700, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5BF3)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 45, 400)

    def lambda_5C1A():
        OP_8E(0xFE, 0xA78, 0x320, 0xFFFFFA88, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C1A)
    WaitChrThread(0x12, 0x1)

    def lambda_5C3A():
        OP_8E(0xFE, 0xA78, 0x320, 0xFDB, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C3A)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 400)
    OP_44(0x10, 0x3)
    OP_7C(0x64, 0x64, 0xBB8, 0x1F4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x114, 0x0, 0x46)
    PlayEffect(0x1, 0x1, 0x12, -400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x12, 400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_5CF3():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFDB, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5CF3)
    WaitChrThread(0x12, 0x1)
    OP_23(0x187)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_8C(0x12, 180, 0)
    PlayEffect(0x1, 0x1, 0x12, -400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x12, 400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xEE, 0x0, 0x64)

    def lambda_5D95():
        OP_96(0xFE, 0xFFFFDD00, 0x320, 0xFFFFEED0, 0x3E8, 0x157C)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D95)
    WaitChrThread(0x12, 0x1)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_22(0xEC, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_5DF4():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5DF4)
    Sleep(300)

    def lambda_5E14():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E14)
    Sleep(300)

    def lambda_5E34():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E34)
    Sleep(300)

    def lambda_5E54():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E54)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_20_5BB0 end

    def Function_21_5E6F(): pass

    label("Function_21_5E6F")


    def lambda_5E75():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0xFFFFE534, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5E75)
    WaitChrThread(0x106, 0x1)

    def lambda_5E95():
        OP_8E(0xFE, 0xFFFFDD14, 0x0, 0xFFFFDE18, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5E95)
    WaitChrThread(0x106, 0x1)

    def lambda_5EB5():
        OP_8E(0xFE, 0xFFFFF920, 0x0, 0xFFFFDE18, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5EB5)
    WaitChrThread(0x106, 0x1)

    def lambda_5ED5():
        OP_8E(0xFE, 0x12D4, 0x0, 0xFFFFF7CC, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5ED5)
    WaitChrThread(0x106, 0x1)

    def lambda_5EF5():
        OP_8E(0xFE, 0x12D4, 0x0, 0x120C, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5EF5)
    WaitChrThread(0x106, 0x1)

    def lambda_5F15():
        OP_8E(0xFE, 0xA64, 0x0, 0x1A40, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5F15)
    WaitChrThread(0x106, 0x1)

    def lambda_5F35():
        OP_8E(0xFE, 0xFFFFDE18, 0x0, 0x1A40, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5F35)
    WaitChrThread(0x106, 0x1)

    def lambda_5F55():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0x10CC, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5F55)
    WaitChrThread(0x106, 0x1)

    def lambda_5F75():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0xFFFFFF38, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5F75)
    WaitChrThread(0x106, 0x1)
    Return()

    # Function_21_5E6F end

    def Function_22_5F90(): pass

    label("Function_22_5F90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(8420, 0, 1220, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 7000, 800, 1000, 270)
    SetChrPos(0x106, 5100, 0, -1400, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6200, 0, -1400, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5100, 0, 1000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 100)
    OP_1D(0x57)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #134
        0x13,
        (
            "#1450F#6P提妲，怎样？\x02\x03",

            "能顺利操作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x12,
        (
            "#560F#11P嗯，没问题。\x01",
            "我练习了好多遍……\x02\x03",

            "随时都能启动哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x15,
        (
            "#100F#3P显示系统启动。\x02\x03",

            "数据连接无异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x14,
        "#1464F#12P……准备就绪了呢。\x02",
    )

    CloseMessageWindow()

    def lambda_615E():
        OP_6D(7300, 0, 260, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_615E)

    def lambda_6176():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6176)

    def lambda_6186():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6186)
    Sleep(150)
    TurnDirection(0x106, 0x14, 500)
    Sleep(300)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #138
        0x14,
        (
            "#1460F#11P……那么阿加特，\x01",
            "现在开始导力装甲Ver.0.5的\x01",
            "动作实验。\x02\x03",

            "做好心理准备了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x106,
        (
            "#053F#6P……啊啊，交给我吧。\x02\x03",

            "#051F既然来到这里，\x01",
            "就不会躲也不会藏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x14,
        (
            "#1462F#11P那么首先，\x01",
            "希望你答应我一件事情。\x02\x03",

            "#1464F实验最后，\x01",
            "会进行你和导力装甲的\x01",
            "模拟战斗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x13,
        (
            "#1452F#5P但若是敢伤到\x01",
            "提妲一根汗毛……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x106, 500)
    Sleep(300)

    ChrTalk(    #142
        0x13,
        (
            "#1458F#5P我就会把你\x01",
            "送到女神身边去……！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x14,
        (
            "#1461F#11P哈哈哈……\x02\x03",

            "#1465F说极端一点\x01",
            "就是这样了。\x02\x03",

            "一定要保证\x01",
            "不能受伤哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x106,
        (
            "#551F#6P……我知道。\x01",
            "这根本不用说啦。\x02\x03",

            "#050F虽然不会手下留情，\x01",
            "但也没打算伤人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x14,
        (
            "#1464F#11P…………这就够了。\x02\x03",

            "#1460F那么首先……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6467():

        label("loc_6467")

        TurnDirection(0xFE, 0x106, 500)
        OP_48()
        Jump("loc_6467")

    QueueWorkItem2(0x14, 2, lambda_6467)

    def lambda_6478():
        OP_8F(0xFE, 0x13EC, 0x0, 0xFFFFFD6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6478)
    WaitChrThread(0x14, 0x1)
    Sleep(300)
    OP_22(0xA, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x106, 0x1E, 0x0, 0x12C, 0xBB8)
    Sleep(1000)

    def lambda_64CC():
        OP_8F(0xFE, 0x10CC, 0x0, 0xFFFFFA88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_64CC)
    WaitChrThread(0x14, 0x1)
    Sleep(300)
    OP_22(0xA, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x106, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(1000)

    def lambda_6520():
        OP_8F(0xFE, 0x13EC, 0x0, 0xFFFFF7A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6520)
    WaitChrThread(0x14, 0x1)
    Sleep(300)
    OP_22(0xA, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x106, 0x1E, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #146
        (
            "\x07\x05丹在阿加特身体上\x01",
            "装满了小小的结晶回路。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #147
        0x106,
        "#055F#5P干、干什么……\x02",
    )

    CloseMessageWindow()

    def lambda_65E8():
        OP_8F(0xFE, 0x1A2C, 0x0, 0xFFFFFA88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_65E8)
    WaitChrThread(0x14, 0x1)
    OP_44(0x14, 0x2)
    Sleep(300)

    ChrTalk(    #148
        0x14,
        (
            "#1465F#11P在实验中，\x01",
            "要实时获取你的身体数据。\x02\x03",

            "这架试作机的基本运动性能\x01",
            "大概和现在的你同等，或是稍稍胜出。\x02\x03",

            "#1461F作性能比较不是正合适吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x106,
        (
            "#555F#6P呜…………\x02\x03",

            "#552F实际上是\x01",
            "故意整人的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x14,
        (
            "#1461F#11P哈哈，你想太多了。\x02\x03",

            "#1460F…………好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6742():

        label("loc_6742")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_6742")

    QueueWorkItem2(0x14, 2, lambda_6742)
    Sleep(200)

    def lambda_6758():

        label("loc_6758")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_6758")

    QueueWorkItem2(0x106, 2, lambda_6758)
    Sleep(500)

    ChrTalk(    #151
        0x14,
        (
            "#1460F#12P那么艾莉卡，\x01",
            "拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #152
        0x13,
        "#1834F#11P好，开始吧！\x02",
    )

    CloseMessageWindow()
    OP_59()
    LoadEffect(0x0, "map\\mp310_00.eff")

    def lambda_67DF():
        OP_6D(1560, 0, 1840, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_67DF)

    def lambda_67F7():
        OP_67(0, 4840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_67F7)

    def lambda_680F():
        OP_8F(0xFE, 0xE74, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_680F)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x24, 0x0)
    Sleep(500)

    ChrTalk(    #153 op#A op#5
        0x13,
        "#20A#3S呼呜呜呜呜…………#2S\x05\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    Sleep(2000)

    ChrTalk(    #154 op#A op#5
        0x13,
        "#15A#3S嗨……！#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_68A7():
        OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_68A7)
    WaitChrThread(0x13, 0x1)
    Sleep(800)
    OP_8C(0x13, 180, 0)

    def lambda_68D3():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xBB8, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_68D3)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #155 op#A op#5
        0x13,
        "#15A#3S呜呀……！#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_6927():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x1388, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6927)
    WaitChrThread(0x13, 0x1)
    Sleep(500)

    ChrTalk(    #156 op#A op#5
        0x13,
        "#20A#3S喝———！！#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_97(0x13, 0xFFFFFE0C, 0xBB8, 0xFFFD40E0, 0x1B58, 0x1)
    OP_97(0x13, 0xFFFFFE0C, 0xFFFFFC18, 0x2BF20, 0x1B58, 0x1)
    Sleep(500)

    ChrTalk(    #157 op#A op#5
        0x13,
        "#15A#3S哈———！！#2\x05\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x64)

    def lambda_69E4():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFC18, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_69E4)
    WaitChrThread(0x13, 0x1)

    def lambda_6A07():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6A07)
    WaitChrThread(0x13, 0x1)
    Sleep(600)

    ChrTalk(    #158 op#A op#5
        0x13,
        "#20A#3S呼呀呀……#2\x05\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    OP_43(0x13, 0x3, 0x0, 0x18)

    def lambda_6A67():
        OP_8E(0xFE, 0xFFFFEF98, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6A67)
    WaitChrThread(0x13, 0x1)
    OP_44(0x13, 0x3)
    OP_8C(0x13, 270, 0)
    Sleep(500)

    def lambda_6A97():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6A97)
    WaitChrThread(0x13, 0x1)
    Sleep(200)
    PlayEffect(0x0, 0x0, 0x13, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_6AF9():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6AF9)

    ChrTalk(    #159 op#A op#5
        0x13,
        "#20A#3S哦哦哦哦哦……！！#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x1F4)
    Sleep(3000)
    OP_44(0x106, 0xFF)
    OP_8C(0x106, 270, 0)

    def lambda_6B5C():
        OP_6D(4860, 0, 1840, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6B5C)
    WaitChrThread(0x24, 0x0)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #160
        0x106,
        "#055F#11P那，那是什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        (
            "#1460F#11P艾莉卡的『成功歌谣』。\x01",
            "重大实验之前她一定要来一次的。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #162
        0x13,
        (
            "#1834F#11P#3S呼哈哈！\x01",
            "气势饱满！！#2S\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_82(0x0, 0x2)
    CloseMessageWindow()
    SetChrPos(0x15, 11680, 0, -2340, 270)

    def lambda_6C67():

        label("loc_6C67")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_6C67")

    QueueWorkItem2(0x15, 2, lambda_6C67)

    def lambda_6C78():

        label("loc_6C78")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_6C78")

    QueueWorkItem2(0x106, 2, lambda_6C78)

    def lambda_6C89():
        OP_6D(10200, 0, -3140, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6C89)

    def lambda_6CA1():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_6CA1)

    def lambda_6CB1():
        OP_8E(0xFE, 0x1F04, 0x0, 0xFFFFEC78, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6CB1)
    Sleep(500)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6CE3():
        OP_8F(0xFE, 0x161C, 0x0, 0xFFFFFCA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_6CE3)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 90, 500)
    OP_44(0x106, 0x2)
    OP_44(0x14, 0x2)
    OP_44(0x15, 0x2)
    Sleep(300)
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x17)

    ChrTalk(    #163
        0x13,
        (
            "#1457F#12P噼啪啪……！\x02\x03",

            "#1457F噼啪啪啪啪！！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #164
        0x13,
        "#1834F#12P好，设置完毕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        (
            "#067F#11P妈、妈妈……\x01",
            "还在做这个啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x15,
        (
            "#104F#5P哼，不过是迷信罢了。\x02\x03",

            "#101F从统计数据上来看，\x01",
            "成功率还不是没什么变化～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x15,
        (
            "#101F#1P怎么样，\x01",
            "程序管理就由我代替……\x02",
        )
    )


    def lambda_6E6A():
        OP_8E(0xFE, 0x2698, 0x0, 0xFFFFF6DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E6A)
    WaitChrThread(0x15, 0x1)

    def lambda_6E8A():
        OP_8E(0xFE, 0x20D0, 0x0, 0xFFFFF13C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E8A)
    WaitChrThread(0x15, 0x1)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #168 op#A
        0x13,
        "#1830F#15A#3S喝呀～！！#2S\x02",
    )


    def lambda_6ED6():
        OP_8E(0xFE, 0x1F04, 0x0, 0xFFFFEF34, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6ED6)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #169 op#A
        0x15,
        "#103F#10A#3S#1P呜哦……！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x8E, 0x0, 0x64)
    OP_43(0x15, 0x3, 0x0, 0x19)
    WaitChrThread(0x15, 0x3)
    Sleep(1500)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x14, 270, 500)
    Sleep(300)

    ChrTalk(    #170
        0x14,
        (
            "#1465F#5P……她现在很兴奋，\x01",
            "你可别刺激她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x106,
        "#551F#6P（真、真不是一般的累啊……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 9)
    SetChrSubChip(0x15, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_5F90 end

    def Function_23_6FF1(): pass

    label("Function_23_6FF1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7007")
    OP_22(0x2BB, 0x0, 0x50)
    Sleep(500)
    Jump("Function_23_6FF1")

    label("loc_7007")

    Return()

    # Function_23_6FF1 end

    def Function_24_7008(): pass

    label("Function_24_7008")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7030")
    OP_8C(0x13, 270, 1000)
    OP_8C(0x13, 180, 1000)
    OP_8C(0x13, 90, 1000)
    OP_8C(0x13, 0, 1000)
    Jump("Function_24_7008")

    label("loc_7030")

    Return()

    # Function_24_7008 end

    def Function_25_7031(): pass

    label("Function_25_7031")


    def lambda_7037():
        OP_96(0xFE, 0x2774, 0x0, 0xFFFFF7E0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7037)
    OP_43(0x15, 0x2, 0x0, 0x20)
    WaitChrThread(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_8C(0x15, 225, 0)
    SetChrChipByIndex(0x15, 21)
    SetChrSubChip(0x15, 0)
    Return()

    # Function_25_7031 end

    def Function_26_7071(): pass

    label("Function_26_7071")


    def lambda_7077():
        OP_8E(0xFE, 0x1C34, 0x0, 0xFFFFFBA0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7077)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 0, 500)
    Return()

    # Function_26_7071 end

    def Function_27_7099(): pass

    label("Function_27_7099")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-8400, 0, 9140, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5100, 0, 1000, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 7000, 800, 1000, 270)
    SetChrPos(0x106, -9000, 0, 12000, 180)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)

    def lambda_7185():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1AF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7185)
    Sleep(2000)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    Sleep(300)
    OP_8C(0x106, 270, 500)
    Sleep(600)
    OP_8C(0x106, 180, 500)
    Sleep(500)

    ChrTalk(    #172
        0x106,
        "#552F#5P这里是…………？\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 135, 500)
    Sleep(200)

    ChrTalk(    #173
        0x106,
        (
            "#055F#6P那、那就是\x01",
            "导力装甲吗……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7259():
        OP_6D(6400, 0, 1000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7259)

    def lambda_7271():
        OP_6C(90000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7271)
    WaitChrThread(0x24, 0x0)
    Sleep(500)

    ChrTalk(    #174
        0x12,
        (
            "#061F#6P嗯，\x01",
            "脚部附近的检查也完毕了。\x02\x03",

            "#560F要不要\x01",
            "再确认一次\x01",
            "程序的流程呢。\x02\x03",

            "妈妈他们\x01",
            "也不知道跑哪儿去了……\x02",
        )
    )

    Jump("loc_7318")

    label("loc_7318")

    CloseMessageWindow()

    def lambda_731F():
        OP_8E(0xFE, 0x13EC, 0x0, 0xFFFFF7CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_731F)
    WaitChrThread(0x12, 0x1)

    def lambda_733F():
        OP_8E(0xFE, 0x1E78, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_733F)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 90, 400)
    Sleep(300)
    OP_62(0x12, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x106, -3800, 0, 1000, 90)

    def lambda_7398():
        OP_8E(0xFE, 0x898, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7398)
    WaitChrThread(0x106, 0x1)
    Sleep(300)

    ChrTalk(    #175
        0x106,
        (
            "#055F我还以为\x01",
            "一定是导力炮什么的……\x02\x03",

            "真亏你们\x01",
            "能做出这种东西来啊。\x02",
        )
    )

    Jump("loc_7419")

    label("loc_7419")

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x12, 315, 500)

    ChrTalk(    #176
        0x12,
        (
            "#064F#1P阿、阿加特大哥哥！？\x02\x03",

            "为什么你会在这里……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #177
        0x12,
        (
            "#065F#1P难、难不成\x01",
            "是妈妈！？\x02\x03",

            "是妈妈\x01",
            "叫你来的吗……\x02",
        )
    )

    Jump("loc_74FE")

    label("loc_74FE")

    CloseMessageWindow()

    def lambda_7505():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_7505)

    def lambda_7513():
        OP_6D(4700, 0, 400, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7513)

    def lambda_752B():
        OP_67(0, 5820, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_752B)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)

    def lambda_754D():
        OP_8E(0xFE, 0xCF8, 0x0, 0xFFFFFF74, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_754D)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    Sleep(500)

    ChrTalk(    #178
        0x12,
        (
            "#562F#11P对、对不起……\x02\x03",

            "爸爸和妈妈\x01",
            "好像误会了\x01",
            "阿加特大哥哥的事。\x02\x03",

            "#063F昨天开始我就一直在解释，\x01",
            "但他们完全不听我的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x106,
        (
            "#551F#6P啊，不是那样的。\x01",
            "……………别担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x12,
        "#064F#11P咦…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x106,
        (
            "#552F#6P那个，怎么说呢……\x02\x03",

            "听说你成为了正式的技师，\x01",
            "正在努力呢。\x02\x03",

            "#051F嗯，所以今天过来陪陪你\x01",
            "就算表示支持了。\x02\x03",

            "协助导力装甲实验……\x01",
            "姑且也算是正式的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x12,
        (
            "#565F#11P…………………………\x02\x03",

            "#067F嘿、嘿嘿嘿嘿…………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xD)
    Sleep(500)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_778C():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_778C)
    Sleep(150)
    OP_8C(0x106, 90, 500)
    Sleep(300)

    ChrTalk(    #183
        0x12,
        (
            "#061F#12P那个那个，\x01",
            "我来说明一下这个导力装甲吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x0, 0x0, 0x1A)

    def lambda_77EF():
        OP_6D(9620, 0, 250, 4500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_77EF)

    ChrTalk(    #184
        0x12,
        (
            "#061F#12P这个试作机的\x01",
            "最大特征是载人型的\x01",
            "人型导力兵器…………\x02\x03",

            "#060F啊，\x01",
            "不过这个开发方针还没有决定。\x02\x03",

            "嗯，\x01",
            "还有要最大限度\x01",
            "实现机体性能这一点也还……\x02\x03",

            "#560F啊，阿加特大哥哥。\x01",
            "你过来这边一下。\x02",
        )
    )

    Jump("loc_78ED")

    label("loc_78ED")

    CloseMessageWindow()

    ChrTalk(    #185
        0x106,
        "#052F#5P哦，哦…………\x02",
    )

    CloseMessageWindow()

    def lambda_7917():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7917)

    def lambda_7927():
        OP_8E(0xFE, 0x1770, 0x0, 0xFFFFFBA0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7927)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 0, 500)
    Sleep(300)

    def lambda_7953():

        label("loc_7953")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_7953")

    QueueWorkItem2(0x12, 2, lambda_7953)

    def lambda_7964():
        OP_8F(0xFE, 0x1D5B, 0x0, 0xFFFFFCC7, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7964)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #186
        0x12,
        (
            "#560F#12P还有，\x01",
            "这个新的步行系统虽然能大幅提高\x01",
            "双足型导力人形兵器的机动性能…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_79E9():
        OP_8F(0xFE, 0x1E82, 0x0, 0xFFFFFDEE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_79E9)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #187
        0x12,
        (
            "#560F#12P但由于必须将普通的双足步行系统\x01",
            "精密的姿势控制与重心控制单元\x01",
            "相互合并……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A6C():
        OP_8F(0xFE, 0x1FA9, 0x0, 0xFFFFFF15, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7A6C)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #188
        0x12,
        (
            "#061F#12P所以会大量消耗\x01",
            "系统整体的能源。\x01",
            "为了消除这个……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7AD7():
        OP_8F(0xFE, 0x20D0, 0x0, 0x3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7AD7)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8400, 0, 2600, 180)
    WaitChrThread(0x12, 0x0)

    def lambda_7B17():
        OP_8F(0xFE, 0x20D0, 0x0, 0x618, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7B17)
    WaitChrThread(0x12, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_7B3C():
        OP_96(0xFE, 0x2094, 0x0, 0x3C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7B3C)
    WaitChrThread(0x12, 0x1)

    def lambda_7B5F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_7B5F)
    OP_44(0x12, 0x2)
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x12, 0, 500)
    Sleep(300)

    ChrTalk(    #189
        0x12,
        "#064F#12P咦、咦…………？\x02",
    )

    CloseMessageWindow()

    def lambda_7BBF():

        label("loc_7BBF")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_7BBF")

    QueueWorkItem2(0x12, 2, lambda_7BBF)

    def lambda_7BD0():

        label("loc_7BD0")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_7BD0")

    QueueWorkItem2(0x106, 2, lambda_7BD0)

    def lambda_7BE1():
        OP_8F(0xFE, 0x20D0, 0x0, 0xFFFFFB50, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7BE1)

    def lambda_7BFC():
        OP_8F(0xFE, 0x20D0, 0x0, 0x3C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7BFC)
    WaitChrThread(0x13, 0x1)
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #190
        0x106,
        (
            "#055F#6P什……！？\x01",
            "你、你是……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x12,
        (
            "#065F#12P妈……妈妈！？\x01",
            "你什么时候来的！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CD5():
        OP_8E(0xFE, 0x1D9C, 0x0, 0xFFFFFBDC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7CD5)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #192
        0x13,
        (
            "#1456F#11P阿加特·科洛斯纳……\x01",
            "感谢你协助实验。\x02\x03",

            "终于打算低头认罪，\x01",
            "来向我忏悔了吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x106,
        (
            "#555F#6P又、又在\x01",
            "说些乱七八糟、\x01",
            "莫名其妙的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x13,
        (
            "#1451F#11P你刚才\x01",
            "靠近了提妲吧。\x02\x03",

            "没错吧，\x01",
            "靠近了吧！？\x02\x03",

            "#1835F我已经抓到决定性的证据了！！\x02",
        )
    )

    Jump("loc_7E20")

    label("loc_7E20")

    CloseMessageWindow()

    ChrTalk(    #195
        0x106,
        "#055F#6P别用这种眼神了行吗……\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0x2)
    OP_44(0x106, 0x2)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 14300, 4000, 100, 270)
    SetChrPos(0x14, 14300, 4000, 1200, 270)

    NpcTalk(    #196
        0x15,
        "老人的声音",
        (
            "#12P虽然机械盲\x01",
            "始终是机械盲……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #197
        0x15,
        "老人声音",
        (
            "#12P不过就算如此，\x01",
            "不是也很有趣吗？\x02",
        )
    )

    Jump("loc_7EFB")

    label("loc_7EFB")

    CloseMessageWindow()

    NpcTalk(    #198
        0x14,
        "男性的声音",
        "#3P是啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #199
        0x14,
        "男性的声音",
        (
            "#3P虽然暂时还\x01",
            "值得商榷……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F57():
        OP_6D(10260, 3000, -660, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7F57)

    def lambda_7F6F():
        OP_67(0, 2640, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7F6F)

    def lambda_7F87():
        OP_6B(3540, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_7F87)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #200
        0x14,
        (
            "#1460F#6P不过即使是跟不上的话题，\x01",
            "也不会不分青红皂白地否定，\x01",
            "这点或许值得好评。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #201
        0x106,
        (
            "#055F#5P你、你们\x01",
            "为什么会在那里……！？\x02\x03",

            "话说，丹，\x01",
            "你不是在房顶上吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x14,
        (
            "#1465F#12P……我没说过吗。\x02\x03",

            "#1461F我会来观看『实验』的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#551F#5P（完、完全看不透\x01",
            "  这家伙在想什么……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x13,
        (
            "#1830F#11P……阿加特·科洛斯纳！？\x01",
            "不要无视我！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(8780, 0, 20, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    SetChrPos(0x15, 15200, 0, 7300, 180)
    SetChrPos(0x14, 15200, 0, 7300, 180)
    OP_43(0x15, 0x3, 0x0, 0x1C)
    Sleep(1000)
    OP_43(0x14, 0x3, 0x0, 0x1D)

    def lambda_81AC():
        OP_8E(0xFE, 0x19B4, 0x0, 0xFFFFFBDC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_81AC)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_81E3():
        OP_8F(0xFE, 0x1450, 0x0, 0xFFFFFBA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_81E3)
    WaitChrThread(0x106, 0x1)

    def lambda_8203():
        OP_8F(0xFE, 0x1D9C, 0x0, 0xFFFFFBDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8203)
    WaitChrThread(0x15, 0x3)
    Sleep(300)

    ChrTalk(    #205
        0x15,
        (
            "#101F#11P算了，按照计划，\x01",
            "人也都到齐了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x3)

    ChrTalk(    #206
        0x14,
        "#1460F#11P差不多该开始了吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 0)
    OP_8C(0x12, 95, 500)
    Sleep(600)
    OP_8C(0x12, 135, 500)
    OP_8C(0x12, 270, 500)
    Sleep(300)

    ChrTalk(    #207
        0x12,
        (
            "#064F#11P…………哎……？？\x02\x03",

            "最终检查\x01",
            "都已经结束了啊……？\x02",
        )
    )

    Jump("loc_8304")

    label("loc_8304")

    CloseMessageWindow()
    OP_8C(0x13, 90, 500)
    Sleep(300)

    ChrTalk(    #208
        0x13,
        (
            "#1451F#5P你干得不错，提妲。\x02\x03",

            "#1834F终于要开始『实验』了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    ChrTalk(    #209
        0x15,
        "#101F#11P哦呵呵呵呵！\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    ChrTalk(    #210
        0x14,
        "#1461F#11P哈哈哈哈哈……\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    ChrTalk(    #211
        0x13,
        "#1451F#5P#3S哦～呵·呵·呵！！#2S\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x106,
        "#551F#6P怎么了，这一家子………？\x02",
    )

    CloseMessageWindow()

    def lambda_8458():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_8458)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_7099 end

    def Function_28_847E(): pass

    label("Function_28_847E")


    def lambda_8484():
        OP_8E(0xFE, 0x3B60, 0x0, 0xF3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8484)
    WaitChrThread(0x15, 0x1)

    def lambda_84A4():
        OP_8E(0xFE, 0x23F0, 0x0, 0xFFFFF7CC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_84A4)
    WaitChrThread(0x15, 0x1)
    OP_8C(0x15, 270, 500)
    Return()

    # Function_28_847E end

    def Function_29_84C6(): pass

    label("Function_29_84C6")


    def lambda_84CC():
        OP_8E(0xFE, 0x3B60, 0x0, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_84CC)
    WaitChrThread(0x14, 0x1)

    def lambda_84EC():
        OP_8E(0xFE, 0x2710, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_84EC)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 270, 500)
    Return()

    # Function_29_84C6 end

    def Function_30_850E(): pass

    label("Function_30_850E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(8100, 500, 2240, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -9000, 0, 14600, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 7020, 2000, 980, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5300, 0, 1400, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -4600, 0, 3260, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -9000, 0, 12000, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 7000, 800, 1000, 270)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0x14,
        (
            "#1460F交换作业就到这里吧。\x02\x03",

            "虽然这款机枪是新型的，\x01",
            "但还是需要进行调试……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x13,
        (
            "#1458F#6P不过这样一来\x01",
            "武装强化也算完成了。\x02\x03",

            "多亏了之前的通宵工作，\x01",
            "使导力装甲的机动性能\x01",
            "提升了１６％……\x02\x03",

            "#1456F呼呼呼，\x01",
            "在目前这个阶段，先收集一次数据吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x14,
        (
            "#1464F一般来说，最开始\x01",
            "只要进行基本的动作测试……\x02\x03",

            "#1465F不过多亏提妲帮忙，\x01",
            "这家伙作为试作机\x01",
            "完成度已经很高了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 180, 500)

    def lambda_8792():
        OP_96(0xFE, 0x1B6C, 0x0, 0xFFFFFD1C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8792)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x14, 0x4)
    TurnDirection(0x14, 0x13, 400)
    Sleep(300)

    ChrTalk(    #216
        0x14,
        (
            "#1461F#11P顺便进行一些\x01",
            "简单的战斗吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x13,
        (
            "#1457F#6P…………当然了。\x02\x03",

            "#1835F毕竟难得有个\x01",
            "牺牲品在这里……！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)

    def lambda_8865():
        OP_6D(5900, 0, 1920, 3500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_8865)

    def lambda_887D():
        OP_67(0, 5700, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_887D)

    def lambda_8895():
        OP_8F(0xFE, 0x794, 0x0, 0x104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8895)

    def lambda_88B0():
        OP_8C(0x14, 270, 300)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_88B0)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #218
        0x12,
        (
            "#560F#6P啊…………\x01",
            "爸爸，妈妈。\x02\x03",

            "那个……嗯……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8906():
        OP_8F(0xFE, 0x139C, 0x0, 0x78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8906)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 270, 500)
    Sleep(300)

    ChrTalk(    #219
        0x14,
        (
            "#1460F#11P哟，提妲，\x01",
            "今天睡得好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x12,
        (
            "#060F#6P嗯、嗯，没问题。\x01",
            "睡得很香，精神很好呢。\x02\x03",

            "#063F但、但是……那个………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x13,
        (
            "#1456F#5P被这个导力装甲\x01",
            "彻底修理一番之后\x01",
            "趴在地上的红毛……\x02\x03",

            "#1831F啊啊，简直近在眼前………㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #222
        0x12,
        (
            "#065F#6P妈、妈妈！\x02\x03",

            "我都说了，\x01",
            "阿加特大哥哥不是坏人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x14,
        (
            "#1461F#11P啊哈哈……\x01",
            "不用介意，提妲。\x02\x03",

            "#1465F别看艾莉卡表面上\x01",
            "一副得理不饶人的口气……\x02\x03",

            "但她其实是为了确认\x01",
            "阿加特接近提妲的\x01",
            "目的。\x02",
        )
    )

    Jump("loc_8B34")

    label("loc_8B34")

    CloseMessageWindow()

    ChrTalk(    #224
        0x12,
        "#065F#6P嗯、嗯…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #225
        0x12,
        (
            "#561F#6P（唉…………\x01",
            "  果然，我觉得\x01",
            "  爸爸也误会了……）\x02\x03",

            "#062F那个，我再说一次哦。\x02\x03",

            "阿加特大哥哥虽然不好相处，\x01",
            "又嫌麻烦，说话用词\x01",
            "也有点粗鲁……\x02\x03",

            "但其实他是个温柔的好人哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x13)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #226
        0x14,
        (
            "#1463F#11P是、是吗。\x02\x03",

            "#1464F这样我也\x01",
            "有点担心起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x12,
        (
            "#065F#6P……咦咦！？\x01",
            "为、为什么…………？\x02\x03",

            "我都解释了好多遍了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #228
        0x13,
        (
            "#1457F#5P…………差不多\x01",
            "该进行准备了吧。\x02\x03",

            "#1452F丹，最终调整交给你了。\x01",
            "我稍微出去一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 500)
    Sleep(300)

    ChrTalk(    #229
        0x14,
        "#1462F#12P……这就要走了吗，艾莉卡。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x13,
        (
            "#1457F#5P………………嗯嗯。\x02\x03",

            "听到这里，\x01",
            "我再也不能沉默下去了。\x02\x03",

            "#1835F罪人，就必须死……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E4C():

        label("loc_8E4C")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_8E4C")

    QueueWorkItem2(0x12, 2, lambda_8E4C)

    def lambda_8E5D():

        label("loc_8E5D")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_8E5D")

    QueueWorkItem2(0x14, 2, lambda_8E5D)

    def lambda_8E6E():
        OP_8E(0xFE, 0xFFFFE610, 0x0, 0x578, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8E6E)
    Sleep(500)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #231
        0x12,
        (
            "#065F#5P咦咦…………！？\x02\x03",

            "妈、妈妈！？\x01",
            "你去哪里……？\x02\x03",

            "……等、等等啊！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_8F1B():
        OP_8E(0xFE, 0xFFFFE9F8, 0x0, 0x104, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8F1B)
    WaitChrThread(0x12, 0x1)
    Fade(1000)
    OP_6D(-9000, 0, 10480, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_44(0x12, 0x2)
    OP_44(0x14, 0x2)
    SetChrPos(0x13, 480, 0, 1780, 225)
    SetChrPos(0x12, 480, 0, 1780, 225)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)

    def lambda_8FCD():
        OP_6D(-7260, 0, 8680, 3500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_8FCD)

    def lambda_8FE5():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_8FE5)

    def lambda_8FF5():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8FF5)
    Sleep(100)

    def lambda_9015():
        OP_8E(0xFE, 0xFFFFF394, 0x0, 0x6F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9015)
    WaitChrThread(0x13, 0x1)

    def lambda_9035():
        OP_8E(0xFE, 0xFFFFDECC, 0x0, 0x1BBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9035)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    ChrTalk(    #232 op#A
        0x15,
        "#103F#10A#5P#3S哇……！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_43(0x15, 0x3, 0x0, 0x1F)

    def lambda_909A():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_909A)
    WaitChrThread(0x13, 0x1)

    def lambda_90BA():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_90BA)
    WaitChrThread(0x13, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_90ED():
        OP_8E(0xFE, 0xFFFFF394, 0x0, 0x6F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_90ED)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x13, 0x8)

    def lambda_9112():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9112)
    Sleep(600)

    ChrTalk(    #233 op#A
        0x12,
        "#068F#10A#6P#3S妈妈！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    WaitChrThread(0x12, 0x1)

    def lambda_916E():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_916E)
    Sleep(100)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #234
        0x15,
        "#102F#11P怎、怎么了……\x02",
    )

    CloseMessageWindow()

    def lambda_91E2():
        OP_6D(-5590, 0, 8720, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_91E2)
    SetChrPos(0x14, -2100, 0, 1900, 315)

    def lambda_920B():
        OP_8E(0xFE, 0xFFFFE638, 0x0, 0x1900, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_920B)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x14, 0x2)
    OP_8C(0x14, 0, 500)
    Sleep(300)

    ChrTalk(    #235
        0x14,
        (
            "#1460F#12P没受伤吗，\x01",
            "岳父。\x02",
        )
    )

    Jump("loc_9266")

    label("loc_9266")

    CloseMessageWindow()

    ChrTalk(    #236
        0x15,
        "#104F#5P啊，没什么。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x15, 9)
    SetChrSubChip(0x15, 0)
    Sleep(500)
    OP_8C(0x15, 180, 400)
    Sleep(300)

    ChrTalk(    #237
        0x15,
        (
            "#102F#5P着什么急呢，\x01",
            "艾莉卡那家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x14,
        (
            "#1461F#12P哈哈哈…………\x02\x03",

            "……要开始了呢。#1000W \x01",
            "#20W那个『实验』……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #239
        0x15,
        "#104F#5P你也真是溺爱孩子啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_850E end

    def Function_31_9393(): pass

    label("Function_31_9393")


    def lambda_9399():
        OP_96(0xFE, 0xFFFFE570, 0x0, 0x1DB0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9399)
    OP_43(0x15, 0x2, 0x0, 0x20)
    WaitChrThread(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_8C(0x15, 270, 0)
    SetChrChipByIndex(0x15, 21)
    SetChrSubChip(0x15, 0)
    Return()

    # Function_31_9393 end

    def Function_32_93D3(): pass

    label("Function_32_93D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93FB")
    OP_8C(0x15, 270, 1000)
    OP_8C(0x15, 0, 1000)
    OP_8C(0x15, 90, 1000)
    OP_8C(0x15, 180, 1000)
    Jump("Function_32_93D3")

    label("loc_93FB")

    Return()

    # Function_32_93D3 end

    def Function_33_93FC(): pass

    label("Function_33_93FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(8520, 0, 2460, 0)
    OP_67(0, 4140, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -1300, 0, -3240, 0)
    SetChrPos(0x107, -9000, 0, 11940, 180)
    OP_72(0x12, 0x0)
    ExitThread()
    OP_72(0x412, 0x0)
    ExitThread()
    OP_72(0x13, 0x0)
    ExitThread()
    OP_72(0x413, 0x0)
    ExitThread()
    OP_A1(0x18, 0x8)
    SetChrPos(0x18, 2400, 0, 2700, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14, 0x3, 0x0, 0x22)

    def lambda_94B1():
        OP_6D(-2820, 0, 740, 10000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_94B1)

    def lambda_94C9():
        OP_6C(24000, 10000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_94C9)

    def lambda_94D9():
        OP_67(0, 5100, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_94D9)

    def lambda_94F1():
        OP_6E(502, 10000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_94F1)
    OP_C8(0x200, 0x46, "C_PLAC40._CH", 0x1, 0xBB8)
    WaitChrThread(0x24, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-7220, 0, 10500, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 2400, 0, 1000, 90)
    OP_0D()
    Sleep(300)
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_22(0x6D, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)

    def lambda_9598():
        OP_6D(-7220, 0, 9000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_9598)

    def lambda_95B0():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1C84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_95B0)
    WaitChrThread(0x107, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x107, 90, 500)
    Sleep(800)
    OP_8C(0x107, 220, 500)
    Sleep(800)
    OP_8C(0x107, 135, 500)
    Sleep(300)

    def lambda_960C():
        OP_6D(-800, 0, 3020, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_960C)

    def lambda_9624():
        OP_6C(70000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9624)

    def lambda_9634():
        OP_8E(0xFE, 0xFFFFE8F4, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9634)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x14, 500)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #240
        0x107,
        "#560F#5P……爸爸！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x107, 500)
    Sleep(300)

    ChrTalk(    #241
        0x14,
        (
            "#1463F提妲？\x02\x03",

            "#1460F啊，稍微等等。\x01",
            "我这就去你那边。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 180, 400)

    def lambda_96EB():
        OP_8E(0xFE, 0x960, 0x0, 0xFFFFF31C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_96EB)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x14, 0xFF)
    SetChrSubChip(0x14, 0)
    OP_6F(0x7, 0)
    OP_6D(600, 400, 1830, 0)
    OP_67(0, 4460, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x107, 0x1)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x107, -800, 400, 380, 270)
    SetChrChipByIndex(0x107, 38)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x14, 0x800)
    ClearChrFlags(0x14, 0x1)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, -700, 300, 1500, 270)
    SetChrChipByIndex(0x14, 39)
    SetChrSubChip(0x14, 0)
    Sleep(1000)

    def lambda_97B2():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_97B2)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x107, 0x0)
    Sleep(500)

    ChrTalk(    #242
        0x14,
        (
            "#1465F#5P是吗……\x02\x03",

            "艾莉卡不让你\x01",
            "参加开发啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x107,
        (
            "#063F#12P嗯…………\x02\x03",

            "妈妈说的话我都懂，\x01",
            "也完全无法反驳……\x02\x03",

            "#561F但是，好不甘心…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x14,
        (
            "#1464F#5P……艾莉卡\x01",
            "和岳父不一样，\x01",
            "有自己明确的研究思想。\x02\x03",

            "不是一时心血来潮，\x01",
            "而是根据明确的动机而行动……\x02\x03",

            "#1465F特别是这次，\x01",
            "关系到利贝尔的国防大事。\x02\x03",

            "的确，\x01",
            "提妲的话还比不上啊……\x02",
        )
    )

    Jump("loc_9964")

    label("loc_9964")

    CloseMessageWindow()

    ChrTalk(    #245
        0x107,
        (
            "#063F#12P……………………\x02\x03",

            "#062F但是我，\x01",
            "想好好面对玲啊！\x02\x03",

            "虽然我、我说的话\x01",
            "可能是出于孩子气！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x14, 1)
    Sleep(500)

    ChrTalk(    #246
        0x14,
        (
            "#1462F#5P提妲……\x02\x03",

            "#1462F（这么认真的表情\x01",
            "  我好像还是头一次见到……）\x02\x03",

            "#1464F我并不认为\x01",
            "提妲的话是孩子气哦。\x02\x03",

            "但是，说到底那和导力装甲的\x01",
            "开发还是没有关系啊。\x02\x03",

            "#1464F即使有导力装甲，\x01",
            "你也很难\x01",
            "面对那孩子吧……\x02",
        )
    )

    Jump("loc_9AF2")

    label("loc_9AF2")

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #247
        0x14,
        (
            "#1462F#5P…………提妲，\x01",
            "要直面一个人\x01",
            "是非常困难的事情。\x02\x03",

            "也许，\x01",
            "比提妲所想象的还要难很多哦。\x02\x03",

            "#1465F虽然提妲是善良的孩子，\x01",
            "但有些事并不是光凭善良\x01",
            "就能明白的啊……\x02",
        )
    )

    Jump("loc_9BD7")

    label("loc_9BD7")

    CloseMessageWindow()

    ChrTalk(    #248
        0x107,
        "#063F#12P嗯…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #249
        0x107,
        (
            "#562F#12P#40W果然，\x01",
            "我还是没办法\x01",
            "和玲对话吗……\x02\x03",

            "我又是\x01",
            "什么也做不到……\x02",
        )
    )

    Jump("loc_9C7B")

    label("loc_9C7B")

    CloseMessageWindow()

    ChrTalk(    #250
        0x14,
        (
            "#1462F#5P…………………………\x02\x03",

            "#1462F刚才提妲\x01",
            "去和艾莉卡交涉，\x01",
            "结果反而被说服了吧？\x02\x03",

            "那是因为艾莉卡\x01",
            "拥有强烈的信念。\x02\x03",

            "#1464F如果那孩子有着深重的过去，\x01",
            "提妲就要有比她\x01",
            "更强的信念才行。\x02\x03",

            "否则的话，\x01",
            "彼此就不能了解对方的真意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x107,
        (
            "#561F#12P…………这么说来\x01",
            "阿加特大哥哥也说过……\x02\x03",

            "#062F……『吵架就是看气势！』\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #252
        0x14,
        (
            "#1460F#5P不、不，说是气势有点………\x02\x03",

            "#1464F（…………阿加特…………\x01",
            "  你也挺令人不安呢……）\x02\x03",

            "#1465F嗯…………\x01",
            "这种情况下该说是觉悟吧。\x02\x03",

            "要直面那个孩子\x01",
            "表露彼此心声的觉悟……\x02\x03",

            "说起来容易，\x01",
            "做起来难哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #253
        0x107,
        (
            "#063F#12P……的确，\x01",
            "玲是『结社』的人，\x01",
            "帕蒂尔·玛蒂尔也非常强……\x02\x03",

            "#063F我又没有艾丝蒂尔姐姐\x01",
            "那样的力量……\x02\x03",

            "我说的话，\x01",
            "可能都无法传达给她……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #254
        0x107,
        (
            "#062F#12P…………但是，\x01",
            "我还是无法放任\x01",
            "玲或者帕蒂尔·玛蒂尔不管！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x107, 0x1)

    def lambda_A025():
        OP_96(0xFE, 0xFFFFF8F8, 0x0, 0x17C, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A025)
    WaitChrThread(0x107, 0x1)
    ClearChrFlags(0x107, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_A052():
        OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x17C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A052)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 400)
    Fade(500)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, -800, 200, 1500, 270)
    SetChrPos(0x107, -4400, 0, 380, 90)
    OP_6D(-800, 0, 1500, 0)
    OP_67(0, 3740, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13, -9330, 0, 8610, 135)

    def lambda_A0F3():
        OP_8E(0xFE, 0xFFFFEED0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A0F3)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x14, 500)
    Sleep(500)

    def lambda_A11F():
        OP_6B(3000, 20000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_A11F)

    ChrTalk(    #255
        0x107,
        (
            "#062F#6P那、那个，爸爸。\x02\x03",

            "虽然玲是『结社』的人，\x01",
            "她也可能确实\x01",
            "做过一些坏事……\x02\x03",

            "但是我也曾经\x01",
            "和她一起去逛过街，\x01",
            "所以我明白的。\x02\x03",

            "#563F玲其实很善良的。\x01",
            "那不是什么演技，\x01",
            "是发自内心的表现。\x02\x03",

            "在店里看到可爱的项链时，\x01",
            "两个人都忍不住\x01",
            "开心大笑起来……\x02\x03",

            "#066F我摔倒的时候\x01",
            "她一边说着真没办法\x01",
            "一边伸手帮我……\x02\x03",

            "玲真的是好孩子。\x01",
            "我现在还认为她是我的朋友。\x02\x03",

            "#561F…………但是，\x01",
            "玲和帕蒂尔·玛蒂尔都离我太远，\x01",
            "那个时候我完全无法触及……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #256
        0x107,
        (
            "#062F#6P但是……\x01",
            "现在却有可能接近了。\x02\x03",

            "只要有导力装甲，\x01",
            "说不定我就能看到\x01",
            "玲所看到的东西……\x02\x03",

            "玲说不定也能敞开心扉\x01",
            "和我对话……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #257
        0x107,
        (
            "#566F#6P……所以，所以…………\x01",
            "我想参加这个计划！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(300)
    Fade(250)
    SetChrPos(0x14, -2300, 0, 1500, 270)
    SetChrChipByIndex(0x14, 8)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x1)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #258
        0x14,
        (
            "#1465F#5P（是吗…………\x01",
            "  提妲已经……）\x02\x03",

            "#1464F………………………………\x02\x03",

            "……艾莉卡，你怎么看？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x107,
        "#064F#6P咦…………！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)

    def lambda_A50A():
        OP_6D(-2800, 0, 4000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_A50A)

    def lambda_A522():
        OP_8F(0xFE, 0xFFFFE214, 0x0, 0x1900, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A522)
    Sleep(500)

    def lambda_A542():

        label("loc_A542")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_A542")

    QueueWorkItem2(0x107, 2, lambda_A542)

    def lambda_A553():

        label("loc_A553")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_A553")

    QueueWorkItem2(0x14, 2, lambda_A553)
    WaitChrThread(0x24, 0x0)
    WaitChrThread(0x13, 0x1)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #260
        0x107,
        (
            "#065F妈……妈妈！？\x02\x03",

            "从什么时候开始听的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x13,
        "#1450F……只有最后那里。\x02",
    )

    CloseMessageWindow()

    def lambda_A5E4():
        OP_6D(-2000, 0, 3200, 2500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_A5E4)

    def lambda_A5FC():
        OP_67(0, 3800, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A5FC)

    def lambda_A614():
        OP_6C(60000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_A614)

    def lambda_A624():
        OP_6B(2900, 2500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_A624)

    def lambda_A634():
        OP_6E(267, 2500)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_A634)

    def lambda_A644():
        OP_8E(0xFE, 0xFFFFEED0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A644)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x107, 500)
    Sleep(300)

    ChrTalk(    #262
        0x13,
        "#1452F#5P提妲，我可以问你一个问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x107,
        (
            "#062F#12P嗯、嗯。\x01",
            "…………是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x13,
        (
            "#1452F#5P如果那个叫玲的女孩\x01",
            "并没有把提妲\x01",
            "当成自己的朋友……\x02\x03",

            "你打算怎么办？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #265
        0x107,
        (
            "#066F#12P…………什么……\x02\x03",

            "什么也不会改变的，妈妈。\x02\x03",

            "#563F因为我已经决定\x01",
            "要和玲联系在一起了。\x02\x03",

            "虽然我\x01",
            "也许不能追上她，\x01",
            "然后说服她……\x02\x03",

            "但是，\x01",
            "了解玛蒂尔·帕蒂尔的事情，\x01",
            "给导力装甲计划帮忙………\x02\x03",

            "#560F这样的事情，\x01",
            "我还是能做得到的。\x02\x03",

            "用这种形式，\x01",
            "我也能和玲有所联系。\x02\x03",

            "#062F………………我想这么做。#1800W \x01",
            "#20W这就是我的心情。\x02",
        )
    )

    Jump("loc_A8DF")

    label("loc_A8DF")

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #266
        0x13,
        (
            "#1457F#5P…………是吗。\x02\x03",

            "那，好吧。\x01",
            "虽然还稍显天真……\x02\x03",

            "#1450F但看来你确实有\x01",
            "参加计划的理由。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #267
        0x107,
        "#064F#12P咦…………！？\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x75)
    OP_8C(0x13, 280, 400)
    Sleep(300)

    ChrTalk(    #268
        0x13,
        (
            "#1458F#5P好啦你们两个，\x01",
            "别磨磨蹭蹭的！\x02\x03",

            "#1834F……丹！\x01",
            "我要修改设计图纸，\x01",
            "麻烦你检查一下！！\x02\x03",

            "……提妲！！\x01",
            "我们开始\x01",
            "试作结晶回路！！\x02",
        )
    )

    Jump("loc_AA75")

    label("loc_AA75")

    CloseMessageWindow()

    ChrTalk(    #269
        0x107,
        (
            "#560F#12P……妈妈，这么说……\x02\x03",

            "我能参加\x01",
            "开发计划了……？\x02",
        )
    )

    Jump("loc_AACD")

    label("loc_AACD")

    CloseMessageWindow()

    ChrTalk(    #270
        0x13,
        (
            "#1458F#5P……这孩子，\x01",
            "干嘛一副那么高兴的样子。\x02\x03",

            "#1456F既然参加\x01",
            "就要给我努力工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x107,
        (
            "#067F#12P嗯、嗯…………\x02\x03",

            "交给我吧，妈妈！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x14,
        "#1461F#11P那么，走吧。\x02",
    )

    CloseMessageWindow()

    def lambda_AB9B():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_AB9B)
    OP_8C(0x13, 280, 600)

    def lambda_ABB2():
        OP_8E(0xFE, 0xFFFFDC74, 0x0, 0x1630, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_ABB2)
    Sleep(150)
    OP_44(0x107, 0x2)

    def lambda_ABD6():
        OP_8E(0xFE, 0xFFFFDBD4, 0x0, 0x11F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_ABD6)
    Sleep(200)
    OP_44(0x14, 0x2)

    def lambda_ABFA():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ABFA)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0x24, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #273
        (
            "\x07\x00#40W──就这样，\x01",
            "提妲参加了导力装甲计划。\x02\x03",

            "曾经多次出入的中央工房成为了工作场所，\x01",
            "也增添了一份新的紧张感。\x02\x03",

            "提妲作为一位技师\x01",
            "与众多大人一起努力工作着。\x02\x03",

            "特别是艾莉卡要求十分严格，\x01",
            "从来不留情面……\x02\x03",

            "但这种严厉\x01",
            "对于提妲来说也是值得高兴的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #274
        "\x07\x00――就这样过了两星期。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_93FC end

    def Function_34_AD84(): pass

    label("Function_34_AD84")


    def lambda_AD8A():
        OP_8E(0xFE, 0x960, 0x0, 0xFFFFF358, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AD8A)
    WaitChrThread(0x14, 0x1)

    def lambda_ADAA():
        OP_8E(0xFE, 0x960, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ADAA)
    WaitChrThread(0x14, 0x1)

    def lambda_ADCA():
        OP_8E(0xFE, 0xCE4, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ADCA)
    WaitChrThread(0x14, 0x1)
    Sleep(2000)
    OP_8C(0x14, 315, 400)

    def lambda_ADF6():
        OP_8E(0xFE, 0x960, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ADF6)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 0, 400)
    Sleep(2000)

    def lambda_AE22():
        OP_8F(0xFE, 0x960, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AE22)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 90, 400)

    def lambda_AE49():
        OP_8E(0xFE, 0xCE4, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AE49)
    WaitChrThread(0x14, 0x1)
    Return()

    # Function_34_AD84 end

    def Function_35_AE64(): pass

    label("Function_35_AE64")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x15, -9000, 0, 11940, 180)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 3200, 0, 1000, 90)
    SetChrPos(0x10, 7000, 800, 61000, 270)
    SetChrFlags(0x10, 0x2000)
    SetChrPos(0x14, -1700, 0, 160, 0)
    SetChrPos(0x107, -2100, 0, 1680, 90)
    SetChrChipByIndex(0x107, 36)
    SetChrSubChip(0x107, 0)
    OP_72(0x13, 0x0)
    ExitThread()
    OP_72(0x413, 0x0)
    ExitThread()
    OP_A1(0x18, 0x8)
    SetChrPos(0x18, -3100, 0, 6500, 0)
    OP_6D(8800, 0, 61000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(8680, 0, 62620, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_6D(8480, 0, 59120, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    Sleep(300)
    FadeToBright(0, 0)
    OP_22(0xF0, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_6D(9400, 0, 61000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(300)
    FadeToBright(0, 0)
    OP_22(0xF0, 0x0, 0x64)
    Sleep(1600)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(2000)
    ClearChrFlags(0x10, 0x2000)
    SetChrPos(0x10, 7000, 800, 1000, 270)
    OP_6D(9400, 0, 1000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    def lambda_B0EF():
        OP_6D(7400, 0, 1000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B0EF)

    def lambda_B107():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_B107)

    def lambda_B11F():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_B11F)

    def lambda_B12F():
        OP_6E(268, 3000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_B12F)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #275
        0x13,
        "#1456F#4S#300W　完　成　。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xD)
    Sleep(500)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #276
        0x13,
        "#1455F#5P好，进入启动实验吧！\x02",
    )

    CloseMessageWindow()

    def lambda_B1AE():
        OP_6D(1200, 0, 1840, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B1AE)

    def lambda_B1C6():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_B1C6)
    WaitChrThread(0x24, 0x0)
    OP_8C(0x14, 90, 400)
    Sleep(300)

    ChrTalk(    #277
        0x14,
        (
            "#1464F#6P艾、艾莉卡。\x01",
            "稍微休息一下吧……\x02\x03",

            "#1465F都不眠不休地工作了三天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x107,
        (
            "#562F#6P妈、妈妈……\x01",
            "为什么你这么有精神啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B27D():
        OP_6D(440, 0, 2410, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B27D)

    def lambda_B295():
        OP_67(0, 5210, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_B295)

    def lambda_B2AD():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_B2AD)

    def lambda_B2BD():
        OP_8E(0xFE, 0x168, 0x0, 0x3E8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B2BD)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #279
        0x13,
        (
            "#1459F#11P你们两个真是的，\x01",
            "怎么这么没精打采啊！\x02\x03",

            "开发的精髓\x01",
            "现在才要开始啊！\x02\x03",

            "#1455F……特别是提妲！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)
    Sleep(150)

    ChrTalk(    #280
        0x107,
        "#065F#6P哎、哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x13,
        (
            "#1456F#11P这次试作机的坐席很小，\x01",
            "只有你才能乘坐。\x02\x03",

            "实验中也要给我\x01",
            "努力到最后哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x107,
        (
            "#063F#6P嗯、嗯。我知道……\x02\x03",

            "#561F但是，\x01",
            "就稍微让我睡会儿吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 0)
    Sleep(500)
    OP_62(0x107, 0x64, 1500, 0x1C, 0x21, 0x12C, 0x0)
    Sleep(2500)

    def lambda_B46C():
        OP_6D(-140, 0, 2470, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B46C)

    def lambda_B484():

        label("loc_B484")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_B484")

    QueueWorkItem2(0x14, 2, lambda_B484)
    Sleep(500)

    def lambda_B49A():
        OP_8F(0xFE, 0xFFFFFD08, 0x0, 0x690, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B49A)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x107, 500)
    Sleep(300)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #283
        0x13,
        (
            "#1833F#11P唉，真没办法呢。\x02\x03",

            "这种状态要是出错也麻烦，\x01",
            "启动实验还是推到明天吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x14,
        (
            "#1460F#12P我觉得提妲干得很好。\x02\x03",

            "即使是熟练的技术人员，\x01",
            "通常都跟不上\x01",
            "艾莉卡的步调呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 225, 400)
    Sleep(300)

    ChrTalk(    #285
        0x13,
        (
            "#1832F#5P哎呀～，真没礼貌。\x02\x03",

            "我可不是\x01",
            "只有体力的白痴哦。\x02",
        )
    )

    Jump("loc_B5F1")

    label("loc_B5F1")

    CloseMessageWindow()
    OP_8C(0x13, 90, 500)
    Sleep(300)
    OP_22(0x12, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #286
        0x13,
        (
            "#1458F#5P嗯嗯…………\x02\x03",

            "２８日星期五，\x01",
            "启动实验……。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107)
    Sleep(300)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x64, 1500, 0x2, 0x7, 0xC8, 0x1)
    Sleep(300)
    OP_95(0x107, 0x0, 0x12C, 0x0, 0x12C, 0xBB8)
    Sleep(300)

    ChrTalk(    #287
        0x107,
        "#561F#6P嗯、嗯嗯嗯…………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x107, 1)
    Sleep(300)

    ChrTalk(    #288
        0x107,
        (
            "#560F#6P妈、妈妈……\x01",
            "难不成，明天是星期五！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x107, 500)
    Sleep(300)

    ChrTalk(    #289
        0x13,
        (
            "#1454F#11P嗯、嗯嗯。\x01",
            "是没错……？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_0D()

    ChrTalk(    #290
        0x107,
        "#067F#6P糟糕，得准备做饭啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_B7B7():

        label("loc_B7B7")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_B7B7")

    QueueWorkItem2(0x13, 2, lambda_B7B7)
    OP_8C(0x107, 315, 500)

    def lambda_B7CF():
        OP_8E(0xFE, 0xFFFFE6B0, 0x0, 0x17D4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B7CF)
    Sleep(1000)
    Fade(1000)
    OP_44(0x107, 0x1)
    SetChrPos(0x107, -2000, 0, 1680, 315)
    OP_6D(-8000, 0, 9000, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(14000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)

    def lambda_B866():
        OP_6D(-6500, 0, 8020, 4000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B866)
    OP_43(0x15, 0x3, 0x0, 0x25)
    Sleep(500)

    ChrTalk(    #291 op#A op#5
        0x15,
        (
            "#100F#1P#35A#5P卡佩尔的\x01",
            "模拟实验\x01",
            "已经完成了。\x02\x03\x05",

            "#40A呵呵，\x01",
            "预定的性能应该都达标了……\x02\x03\x05",

            "#103F#30A哦，提妲，\x01",
            "怎么了？\x05\x02",
        )
    )

    Jump("loc_B92B")

    label("loc_B92B")

    CloseMessageWindow()
    WaitChrThread(0x15, 0x3)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #292
        0x107,
        (
            "#061F#12P啊，爷爷。\x02\x03",

            "明天是月底的星期五啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x15,
        (
            "#101F#5P啊啊，是吗……\x02\x03",

            "是阿加特那家伙\x01",
            "要来的日子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x107,
        (
            "#067F#12P嗯，今天之内\x01",
            "得把料理的材料都准备好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x15,
        (
            "#104F#5P是吗，\x01",
            "那我想要吃的是……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF0, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    OP_1F(0x0, 0x0)
    Sleep(2000)
    SetChrPos(0x13, -1500, 0, 980, 300)
    SetChrPos(0x14, -2420, 0, -160, 300)

    def lambda_BA6A():
        OP_6D(-3240, 0, 3740, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_BA6A)

    def lambda_BA82():
        OP_67(0, 4500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BA82)

    def lambda_BA9A():
        OP_6C(352000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_BA9A)
    WaitChrThread(0x24, 0x0)
    Sleep(1000)

    ChrTalk(    #296
        0x13,
        "#1451F#12P阿加特……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_C4(0x1, 0x400)
    OP_0D()
    Sleep(1000)
    OP_1F(0x64, 0xBB8)

    def lambda_BAEE():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_BAEE)
    Sleep(1000)

    ChrTalk(    #297
        0x14,
        (
            "#1463F#12P嗯……\x02\x03",

            "我听到『月底的星期五』\x01",
            "什么的……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x2)
    OP_44(0x14, 0x2)

    def lambda_BB5C():
        OP_6D(-5600, 0, 6920, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_BB5C)

    def lambda_BB74():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BB74)

    def lambda_BB84():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BB84)
    Sleep(400)

    def lambda_BBA4():
        OP_8E(0xFE, 0xFFFFEB60, 0x0, 0xCBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BBA4)
    Sleep(500)
    TurnDirection(0x107, 0x13, 500)
    WaitChrThread(0x14, 0x1)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #298
        0x107,
        (
            "#064F#5P……啊，对了。\x02\x03",

            "爸爸妈妈还是第一次\x01",
            "见阿加特大哥哥吧。\x02\x03",

            "#061F嘿嘿，\x01",
            "阿加特大哥哥每个月会来家里一次哦。\x02\x03",

            "然后呢…………\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x0, 0x0, 0x24)

    ChrTalk(    #299
        0x13,
        (
            "#1451F#12P#130W『阿加特大哥哥来家里的日子』……#20W\x02\x03",

            "呼呼，\x01",
            "正好是启动实验的日子呢。\x02\x03",

            "#1831F……他运气真好。\x01",
            "#3S啊哈哈哈哈哈！！#2S\x02",
        )
    )

    Jump("loc_BD32")

    label("loc_BD32")

    CloseMessageWindow()
    OP_44(0x13, 0x0)

    ChrTalk(    #300
        0x107,
        (
            "#064F#5P嗯…………？？\x02\x03",

            "……妈妈？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x14,
        (
            "#1465F#6P啊，提妲。\x01",
            "其实，艾莉卡……那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 45, 400)

    def lambda_BDB3():
        OP_6D(-5000, 0, 7300, 2500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_BDB3)

    def lambda_BDCB():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_BDCB)

    def lambda_BDDB():
        OP_8E(0xFE, 0xFFFFF1B4, 0x0, 0x1694, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BDDB)

    def lambda_BDF6():

        label("loc_BDF6")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_BDF6")

    QueueWorkItem2(0x107, 2, lambda_BDF6)

    def lambda_BE07():

        label("loc_BE07")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_BE07")

    QueueWorkItem2(0x15, 2, lambda_BE07)
    Sleep(500)

    def lambda_BE1D():

        label("loc_BE1D")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_BE1D")

    QueueWorkItem2(0x14, 2, lambda_BE1D)
    WaitChrThread(0x13, 0x1)
    OP_44(0x107, 0x2)
    OP_44(0x15, 0x2)

    def lambda_BE3B():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_BE3B)
    Sleep(300)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13)
    Sleep(500)

    def lambda_BE6D():
        OP_8F(0xFE, 0xFFFFEFFC, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BE6D)
    WaitChrThread(0x13, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_BE96():
        OP_6B(2900, 100)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_BE96)

    def lambda_BEA6():
        OP_8F(0xFE, 0xFFFFF1B4, 0x0, 0x1694, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BEA6)
    WaitChrThread(0x13, 0x1)
    OP_22(0x154, 0x0, 0x64)
    OP_22(0x11A, 0x0, 0x64)
    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    OP_70(0x8, 0x3C)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(70)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #302
        0x13,
        (
            "#1458F#5P…………丹？\x01",
            "我想到好主意了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(    #303
        0x13,
        (
            "#1451F#11P这次的实验\x01",
            "要使用活祭品。\x02\x03",

            "呼呼呼…………\x01",
            "既然要来我们家玩。\x02\x03",

            "那当然要求他\x01",
            "有相当的人格才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 500)
    Sleep(300)

    ChrTalk(    #304
        0x13,
        "#1835F#2P#3S阿加特·科洛斯纳！！#2S\x02",
    )

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6B(2820, 0)
    Sleep(500)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x107, 0x2)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 135, 500)
    Sleep(600)
    OP_8C(0x107, 90, 500)
    Sleep(300)

    ChrTalk(    #305
        0x107,
        "#065F#5P嗯……嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x14,
        (
            "#1463F#6P艾、艾莉卡。\x02\x03",

            "也就是说，\x01",
            "你要让阿加特帮忙实验……\x01",
            "……是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x15,
        (
            "#104F啊，那个，艾莉卡。\x02\x03",

            "阿加特那家伙\x01",
            "是个机械盲……\x02\x03",

            "帮忙什么的\x01",
            "应该做不到吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x13,
        (
            "#1458F#11P…………帮忙？\x02\x03",

            "哼，太便宜他了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C1C2():
        OP_6D(-3900, 0, 7600, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_C1C2)

    def lambda_C1DA():
        OP_67(0, 4550, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_C1DA)

    def lambda_C1F2():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_C1F2)

    def lambda_C202():
        OP_6C(35000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_C202)
    TurnDirection(0x13, 0x107, 500)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #309
        0x13,
        (
            "#1834F#11P#3S我要他在这个实验里，\x01",
            "献上自己的人生！！\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #310
        0x107,
        "#065F#3S#6P咦咦～～～！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #311
        0x14,
        (
            "#1461F#6P啊、啊哈哈……\x01",
            "太夸张了……\x02\x03",

            "#1465F不过，\x01",
            "让他帮忙也不算过分吧。\x02\x03",

            "我也想……\x01",
            "和他好好谈一次。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 135, 500)
    Sleep(300)

    ChrTalk(    #312
        0x107,
        "#065F#5P连、连爸爸也！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x13,
        (
            "#1458F#11P就这么定了。\x02\x03",

            "明天一定\x01",
            "是个好日子……\x02",
        )
    )

    Jump("loc_C3AE")

    label("loc_C3AE")

    CloseMessageWindow()

    ChrTalk(    #314
        0x107,
        "#065F#5P哎、哎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 90, 500)
    Sleep(600)
    OP_8C(0x107, 135, 500)
    Sleep(600)
    OP_8C(0x107, 90, 500)
    Sleep(300)

    ChrTalk(    #315
        0x107,
        (
            "#065F#6P（难、难不成……）\x02\x03",

            "（对阿加特大哥哥\x01",
            "  误会了什么……？？）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C461():
        OP_6B(3300, 4000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_C461)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x24, 0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #316
        "\x07\x00Episode『导力装甲开发计划/前篇』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C55F")
    Sleep(1000)
    OP_28(0x1, 0x4, 0x10)
    OP_28(0x1, 0x4, 0x20)
    OP_3E(0x153, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #317
        "\x07\x00得到了\x1F\x53\x01\x07\x00。\x02",
    )

    Jump("loc_C528")

    label("loc_C528")

    CloseMessageWindow()
    AddMira(3000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #318
        "\x07\x00得到了\x07\x02３０００米拉\x07\x00。\x02",
    )

    Jump("loc_C553")

    label("loc_C553")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_C55F")

    OP_C2(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_AE64 end

    def Function_36_C56F(): pass

    label("Function_36_C56F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5AB")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_36_C56F")

    label("loc_C5AB")

    Return()

    # Function_36_C56F end

    def Function_37_C5AC(): pass

    label("Function_37_C5AC")


    def lambda_C5B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_C5B2)

    def lambda_C5C4():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x2198, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C5C4)
    WaitChrThread(0x15, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_C5F7():
        OP_8E(0xFE, 0xFFFFE304, 0x0, 0x1B6C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C5F7)
    WaitChrThread(0x15, 0x1)

    def lambda_C617():
        OP_8E(0xFE, 0xFFFFE6B0, 0x0, 0x17D4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_C617)
    Return()

    # Function_37_C5AC end

    def Function_38_C62D(): pass

    label("Function_38_C62D")

    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_C64C():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C64C)

    def lambda_C667():

        label("loc_C667")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_C667")

    QueueWorkItem2(0xFE, 3, lambda_C667)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_38_C62D end

    def Function_39_C684(): pass

    label("Function_39_C684")

    SetChrChipByIndex(0x12, 2)
    SetChrFlags(0xFE, 0x2)

    def lambda_C694():

        label("loc_C694")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_C694")

    QueueWorkItem2(0xFE, 2, lambda_C694)

    def lambda_C6A7():

        label("loc_C6A7")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_C6A7")

    QueueWorkItem2(0xFE, 3, lambda_C6A7)
    OP_22(0xED, 0x0, 0x64)

    def lambda_C6C9():
        OP_8F(0xFE, 0xFFFFF362, 0x320, 0x244, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C6C9)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x2)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)

    def lambda_C6FC():

        label("loc_C6FC")

        OP_99(0xFE, 0x0, 0x5, 0x9C4)
        OP_48()
        Jump("loc_C6FC")

    QueueWorkItem2(0x12, 3, lambda_C6FC)
    OP_8C(0xFE, 90, 500)
    Return()

    # Function_39_C684 end

    def Function_40_C711(): pass

    label("Function_40_C711")

    OP_44(0xFE, 0x3)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_C727():
        OP_96(0xFE, 0x56E, 0x0, 0xDD4, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C727)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_C76F():
        OP_96(0xFE, 0x1432, 0x0, 0x65E, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C76F)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x1AA4, 0x0, 0x316, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_40_C711 end

    def Function_41_C7C4(): pass

    label("Function_41_C7C4")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_C7E7():
        OP_8F(0xFE, 0xFFFFF33A, 0x320, 0x2094, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C7E7)

    def lambda_C802():

        label("loc_C802")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_C802")

    QueueWorkItem2(0xFE, 3, lambda_C802)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_7C(0x190, 0x190, 0xBB8, 0x64)
    OP_22(0x1FE, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x64)
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 0)
    OP_70(0x8, 0x3C)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x2009, 0x0)
    ExitThread()
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3C)
    Return()

    # Function_41_C7C4 end

    def Function_42_C883(): pass

    label("Function_42_C883")

    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_C8A2():
        OP_91(0xFE, 0x3E8, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C8A2)

    def lambda_C8BD():

        label("loc_C8BD")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_C8BD")

    QueueWorkItem2(0xFE, 3, lambda_C8BD)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x2)

    def lambda_C8E9():

        label("loc_C8E9")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_C8E9")

    QueueWorkItem2(0xFE, 2, lambda_C8E9)

    def lambda_C8FC():

        label("loc_C8FC")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_C8FC")

    QueueWorkItem2(0xFE, 3, lambda_C8FC)
    OP_22(0xED, 0x0, 0x64)
    OP_97(0xFE, 0xFFFFF600, 0x4E2, 0xFFFE7960, 0x1388, 0x1)
    OP_44(0x12, 0x2)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)

    def lambda_C946():

        label("loc_C946")

        OP_99(0xFE, 0x0, 0x5, 0x9C4)
        OP_48()
        Jump("loc_C946")

    QueueWorkItem2(0x12, 3, lambda_C946)
    OP_8C(0xFE, 0, 500)
    Return()

    # Function_42_C883 end

    def Function_43_C95B(): pass

    label("Function_43_C95B")

    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 180, 0)

    def lambda_C96D():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xEF6, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C96D)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_43_C95B end

    def Function_44_C9AB(): pass

    label("Function_44_C9AB")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_C9CE():
        OP_8F(0xFE, 0xFFFFE1B0, 0x320, 0x5C8, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C9CE)

    def lambda_C9E9():

        label("loc_C9E9")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_C9E9")

    QueueWorkItem2(0xFE, 3, lambda_C9E9)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_7C(0x190, 0x190, 0xBB8, 0x64)
    OP_22(0x1FE, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x64)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_6F(0xB, 0)
    OP_70(0xB, 0x3C)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_72(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3C)
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Return()

    # Function_44_C9AB end

    def Function_45_CA84(): pass

    label("Function_45_CA84")

    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x64, 0x0, 0x114E, 0x1B58, 0x0)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_CAAD():
        OP_96(0xFE, 0xFFFFF5F6, 0x0, 0x3D4, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CAAD)

    def lambda_CACB():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CACB)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)

    def lambda_CAE3():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_CAE3)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_45_CA84 end

    def Function_46_CB17(): pass

    label("Function_46_CB17")

    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x11A8, 0x1B58, 0x0)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_CB40():
        OP_96(0xFE, 0xFFFFF786, 0x0, 0x690, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CB40)

    def lambda_CB5E():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CB5E)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_CB8F():
        OP_96(0xFE, 0xFFFFFE48, 0x0, 0xFFFFFA38, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CB8F)

    def lambda_CBAD():
        OP_8C(0xFE, 45, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CBAD)
    SetChrSubChip(0xFE, 2)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_CB17 end

    def Function_47_CBE9(): pass

    label("Function_47_CBE9")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    ClearChrFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xFFFFF8A8, 0x0, 0x168A, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x20)
    OP_8C(0xFE, 135, 400)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_47_CBE9 end

    def Function_48_CC39(): pass

    label("Function_48_CC39")

    OP_22(0x35A, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x35A)
    Return()

    # Function_48_CC39 end

    def Function_49_CC47(): pass

    label("Function_49_CC47")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_CC6A():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CC6A)

    def lambda_CC85():

        label("loc_CC85")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_CC85")

    QueueWorkItem2(0xFE, 3, lambda_CC85)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    Return()

    # Function_49_CC47 end

    def Function_50_CCA6(): pass

    label("Function_50_CCA6")

    OP_22(0xCB, 0x0, 0x64)

    def lambda_CCB1():
        OP_96(0xFE, 0xFFFFF0B0, 0x0, 0x802, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CCB1)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_50_CCA6 end

    def Function_51_CCE8(): pass

    label("Function_51_CCE8")

    SetChrFlags(0x12, 0x800)

    def lambda_CCF3():
        OP_91(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CCF3)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_23(0x1A0)
    SetChrChipByIndex(0x12, 3)
    SetChrSubChip(0x12, 0)

    def lambda_CD24():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_CD24)
    Sleep(200)
    OP_22(0xEE, 0x0, 0x64)
    WaitChrThread(0x12, 0x2)
    Return()

    # Function_51_CCE8 end

    def Function_52_CD3E(): pass

    label("Function_52_CD3E")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_CD61():
        OP_91(0xFE, 0xFFFFE890, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CD61)

    def lambda_CD7C():

        label("loc_CD7C")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_CD7C")

    QueueWorkItem2(0xFE, 3, lambda_CD7C)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    Return()

    # Function_52_CD3E end

    def Function_53_CD9D(): pass

    label("Function_53_CD9D")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 16)
    OP_8F(0xFE, 0xFFFFF844, 0x0, 0x3F2, 0xFA0, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_53_CD9D end

    def Function_54_CDD0(): pass

    label("Function_54_CDD0")

    OP_22(0xCB, 0x0, 0x64)

    def lambda_CDDB():
        OP_96(0xFE, 0xFFFFF254, 0x0, 0x3F2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CDDB)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_54_CDD0 end

    def Function_55_CE12(): pass

    label("Function_55_CE12")

    OP_22(0xCB, 0x0, 0x64)

    def lambda_CE1D():
        OP_96(0xFE, 0xFFFFF844, 0x0, 0x3F2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE1D)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_55_CE12 end

    def Function_56_CE59(): pass

    label("Function_56_CE59")

    OP_22(0x92, 0x0, 0x64)
    OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0x2710)
    OP_23(0x92)
    OP_22(0x9D, 0x0, 0x64)

    def lambda_CE7F():

        label("loc_CE7F")

        OP_99(0xFE, 0x0, 0x5, 0x5DC)
        OP_48()
        Jump("loc_CE7F")

    QueueWorkItem2(0xFE, 3, lambda_CE7F)
    Return()

    # Function_56_CE59 end

    def Function_57_CE8D(): pass

    label("Function_57_CE8D")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x2436, 0x0, 0xFFFFFB96, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3A70, 0x0, 0x1086, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3A84, 0x0, 0x22A6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3142, 0x0, 0x21E8, 0xBB8, 0x0)
    SetChrPos(0xFE, 14300, 4000, 760, 270)
    Return()

    # Function_57_CE8D end

    def Function_58_CEF6(): pass

    label("Function_58_CEF6")

    Sleep(300)
    OP_8C(0xFE, 45, 400)
    OP_8E(0xFE, 0x1022, 0x0, 0xE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3976, 0x0, 0xDA2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3A84, 0x0, 0x22A6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3142, 0x0, 0x21E8, 0xBB8, 0x0)
    SetChrPos(0xFE, 15380, 4000, 2130, 270)
    Return()

    # Function_58_CEF6 end

    def Function_59_CF64(): pass

    label("Function_59_CF64")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -8990, 0, 11860, 180)
    OP_8E(0xFE, 0xFFFFDD64, 0x0, 0x25BC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDA4E, 0x0, 0x20EE, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_59_CF64 end

    def Function_60_CFAA(): pass

    label("Function_60_CFAA")

    Sleep(600)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8990, 0, 11860, 180)
    OP_8E(0xFE, 0xFFFFDD64, 0x0, 0x25BC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDF6C, 0x0, 0x1FD6, 0x7D0, 0x0)
    Return()

    # Function_60_CFAA end

    def Function_61_CFF8(): pass

    label("Function_61_CFF8")

    OP_8E(0xFE, 0xC76, 0x0, 0x6FE, 0x1388, 0x0)
    Return()

    # Function_61_CFF8 end

    def Function_62_D00D(): pass

    label("Function_62_D00D")

    Sleep(400)
    OP_8E(0xFE, 0xF46, 0x0, 0x410, 0x1388, 0x0)
    Return()

    # Function_62_D00D end

    def Function_63_D027(): pass

    label("Function_63_D027")

    Sleep(400)
    Sleep(400)
    OP_8E(0xFE, 0xD7A, 0x0, 0xFFFFFF56, 0x1388, 0x0)
    Return()

    # Function_63_D027 end

    def Function_64_D046(): pass

    label("Function_64_D046")

    Sleep(400)
    Sleep(400)
    Sleep(400)
    OP_8E(0xFE, 0x1536, 0x0, 0x3AC, 0x1388, 0x0)
    Return()

    # Function_64_D046 end

    SaveToFile()

Try(main)
