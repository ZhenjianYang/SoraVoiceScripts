from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4102.x',
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
        '鸽子',                                 # 9
        '鸽子',                                 # 10
        '鸽子',                                 # 11
        '鸽子',                                 # 12
        '鸽子',                                 # 13
        '鸽子',                                 # 14
        '鸽子',                                 # 15
        '奈尔',                                 # 16
        '黑衣人',                               # 17
        '黑衣人',                               # 18
        '黑衣人',                               # 19
        '希德中校',                             # 20
        '格斯',                                 # 21
        '观光客',                               # 22
        '观光客',                               # 23
        '士兵达登',                             # 24
        '皮加',                                 # 25
        '科尼嘉',                               # 26
        '诺蒂亚',                               # 27
        '夏妮',                                 # 28
        '目标用摄影机',                         # 29
        '王都格兰赛尔·北街区',                 # 30
        '王都格兰赛尔·南街区',                 # 31
        '王都格兰赛尔·码头',                   # 32
        '',                                     # 33
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01680 ._CH',             # 01
        'ED6_DT07/CH01690 ._CH',             # 02
        'ED6_DT07/CH01730 ._CH',             # 03
        'ED6_DT07/CH01731 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01053 ._CH',             # 06
        'ED6_DT07/CH01153 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT27/CH03460 ._CH',             # 09
        'ED6_DT27/CH03590 ._CH',             # 0A
        'ED6_DT07/CH01020 ._CH',             # 0B
        'ED6_DT07/CH01053 ._CH',             # 0C
        'ED6_DT07/CH01153 ._CH',             # 0D
        'ED6_DT07/CH01640 ._CH',             # 0E
        'ED6_DT07/CH01680 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT26/CH20686 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01680P._CP',             # 01
        'ED6_DT07/CH01690P._CP',             # 02
        'ED6_DT07/CH01730P._CP',             # 03
        'ED6_DT07/CH01731P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01053P._CP',             # 06
        'ED6_DT07/CH01153P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT27/CH03460P._CP',             # 09
        'ED6_DT27/CH03590P._CP',             # 0A
        'ED6_DT07/CH01020P._CP',             # 0B
        'ED6_DT07/CH01053P._CP',             # 0C
        'ED6_DT07/CH01153P._CP',             # 0D
        'ED6_DT07/CH01640P._CP',             # 0E
        'ED6_DT07/CH01680P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT26/CH20686P._CP',             # 12
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
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
        NpcIndex            = 0x101,
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
        NpcIndex            = 0x101,
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
        NpcIndex            = 0x101,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -44500,
        Z                   = 250,
        Y                   = -19980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -58590,
        Z                   = -3250,
        Y                   = -22150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -58070,
        Z                   = -3250,
        Y                   = -23930,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -89010,
        Z                   = 250,
        Y                   = -1030,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -75890,
        Z                   = 0,
        Y                   = -5330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -54960,
        Z                   = -3750,
        Y                   = -30670,
        Direction           = 270,
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
        X                   = -63160,
        Z                   = -3000,
        Y                   = -35170,
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
        X                   = -40940,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
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
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
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
        X                   = -117000,
        Z                   = 0,
        Y                   = -4090,
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
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 49,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 50,
    )


    DeclActor(
        TriggerX            = -72220,
        TriggerZ            = -3180,
        TriggerY            = -15630,
        TriggerRange        = 800,
        ActorX              = -72220,
        ActorZ              = -2000,
        ActorY              = -15630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -76990,
        TriggerZ            = -3500,
        TriggerY            = -30450,
        TriggerRange        = 800,
        ActorX              = -76990,
        ActorZ              = -2500,
        ActorY              = -30450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4EA",          # 00, 0
        "Function_1_585",          # 01, 1
        "Function_2_601",          # 02, 2
        "Function_3_686",          # 03, 3
        "Function_4_713",          # 04, 4
        "Function_5_916",          # 05, 5
        "Function_6_93A",          # 06, 6
        "Function_7_997",          # 07, 7
        "Function_8_A4C",          # 08, 8
        "Function_9_B5A",          # 09, 9
        "Function_10_C4F",         # 0A, 10
        "Function_11_EC8",         # 0B, 11
        "Function_12_FEF",         # 0C, 12
        "Function_13_1018",        # 0D, 13
        "Function_14_109B",        # 0E, 14
        "Function_15_114C",        # 0F, 15
        "Function_16_1177",        # 10, 16
        "Function_17_11A7",        # 11, 17
        "Function_18_121E",        # 12, 18
        "Function_19_129C",        # 13, 19
        "Function_20_12FA",        # 14, 20
        "Function_21_135D",        # 15, 21
        "Function_22_13BB",        # 16, 22
        "Function_23_1419",        # 17, 23
        "Function_24_1477",        # 18, 24
        "Function_25_14D5",        # 19, 25
        "Function_26_1533",        # 1A, 26
        "Function_27_1583",        # 1B, 27
        "Function_28_15D9",        # 1C, 28
        "Function_29_1634",        # 1D, 29
        "Function_30_168F",        # 1E, 30
        "Function_31_16E5",        # 1F, 31
        "Function_32_16FB",        # 20, 32
        "Function_33_193E",        # 21, 33
        "Function_34_199E",        # 22, 34
        "Function_35_19F7",        # 23, 35
        "Function_36_2E8E",        # 24, 36
        "Function_37_2F2F",        # 25, 37
        "Function_38_2F7C",        # 26, 38
        "Function_39_2FBD",        # 27, 39
        "Function_40_364C",        # 28, 40
        "Function_41_36CB",        # 29, 41
        "Function_42_3837",        # 2A, 42
        "Function_43_3995",        # 2B, 43
        "Function_44_3AAB",        # 2C, 44
        "Function_45_3C31",        # 2D, 45
        "Function_46_3C5F",        # 2E, 46
        "Function_47_3CB0",        # 2F, 47
        "Function_48_3E0F",        # 30, 48
        "Function_49_3E13",        # 31, 49
        "Function_50_3E17",        # 32, 50
    )


    def Function_0_4EA(): pass

    label("Function_0_4EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x1F, -89010, 250, -1030, 189)
    OP_43(0x20, 0x0, 0x0, 0x5)

    label("loc_51D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_53F")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_571")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_555")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_571")

    label("loc_555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_571")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 32)

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_584")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_584")

    Return()

    # Function_0_4EA end

    def Function_1_585(): pass

    label("Function_1_585")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x23005D)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8")
    OP_B1("t4102_y")
    Jump("loc_5C1")

    label("loc_5B8")

    OP_B1("t4102_n")

    label("loc_5C1")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_600")
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_1B(0x0, 0x0, 0x29)
    OP_1B(0x2, 0x0, 0x2A)
    OP_1B(0xB, 0x0, 0x2C)
    OP_65(0x1, 0x1)

    label("loc_600")

    Return()

    # Function_1_585 end

    def Function_2_601(): pass

    label("Function_2_601")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_685")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_2_601")

    label("loc_685")

    Return()

    # Function_2_601 end

    def Function_3_686(): pass

    label("Function_3_686")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_712")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_3_686")

    label("loc_712")

    Return()

    # Function_3_686 end

    def Function_4_713(): pass

    label("Function_4_713")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_747")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_915")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DE")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CE")

    def lambda_7B2():

        label("loc_7B2")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_7B2")

    QueueWorkItem2(0xFE, 1, lambda_7B2)
    Jump("loc_7ED")

    label("loc_7CE")


    def lambda_7D4():

        label("loc_7D4")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_7D4")

    QueueWorkItem2(0xFE, 1, lambda_7D4)

    label("loc_7ED")

    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_7FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_834")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82C")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_834")

    label("loc_82C")

    Sleep(15)
    Jump("loc_7FC")

    label("loc_834")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78690, 0, -40, 74)

    label("loc_853")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DB")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D3")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 4)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    Jump("loc_8DB")

    label("loc_8D3")

    Sleep(500)
    Jump("loc_853")

    label("loc_8DB")

    Jump("loc_912")

    label("loc_8DE")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_912")

    def lambda_8FA():
        OP_8D(0xFE, -74920, -1510, -82870, 5610, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FA)

    label("loc_912")

    Jump("loc_747")

    label("loc_915")

    Return()

    # Function_4_713 end

    def Function_5_916(): pass

    label("Function_5_916")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_939")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_5_916")

    label("loc_939")

    Return()

    # Function_5_916 end

    def Function_6_93A(): pass

    label("Function_6_93A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_996")
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFF711C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C52, 0xFFFFF15A, 0xFFFF727A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C0C, 0x0, 0xFFFFEC82, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFFEC00, 0x9C4, 0x0)
    Jump("Function_6_93A")

    label("loc_996")

    Return()

    # Function_6_93A end

    def Function_7_997(): pass

    label("Function_7_997")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9EB")

    ChrTalk(    #0
        0xFE,
        "这前面就是格兰赛尔港了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "不要慌慌张张掉进海里哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2A")

    label("loc_9EB")


    ChrTalk(    #2
        0xFE,
        "这前面就是格兰赛尔港了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "你们也是来观光的吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A2A")

    Jump("loc_A48")

    label("loc_A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A37")
    Jump("loc_A48")

    label("loc_A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_A41")
    Jump("loc_A48")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A48")

    label("loc_A48")

    TalkEnd(0xFE)
    Return()

    # Function_7_997 end

    def Function_8_A4C(): pass

    label("Function_8_A4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AB8")

    ChrTalk(    #4
        0xFE,
        (
            "导力飞艇普及以后\x01",
            "来这里的人就减少了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "外国的大型货船\x01",
            "真是看不腻啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B38")

    label("loc_AB8")


    ChrTalk(    #6
        0xFE,
        (
            "如果去港口，\x01",
            "就可以看到外国船哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "是从亚瑟利亚湾\x01",
            "经卢比诺川而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "这里有很多大型货船，\x01",
            "真是看不腻啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_B38")

    Jump("loc_B56")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_B45")
    Jump("loc_B56")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_B4F")
    Jump("loc_B56")

    label("loc_B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_B56")

    label("loc_B56")

    TalkEnd(0xFE)
    Return()

    # Function_8_A4C end

    def Function_9_B5A(): pass

    label("Function_9_B5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BED")

    ChrTalk(    #9
        0xFE,
        (
            "那边的咖啡店\x01",
            "相当不错哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "特别是黑咖啡，\x01",
            "在市民之间广受好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "不过要我说的话，\x01",
            "最喜欢的还是那家店的气氛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2D")

    label("loc_BED")


    ChrTalk(    #12
        0xFE,
        "呼…………好困啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "早餐就去那家\x01",
            "咖啡店解决吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_C2D")

    Jump("loc_C4B")

    label("loc_C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_C3A")
    Jump("loc_C4B")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_C44")
    Jump("loc_C4B")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_C4B")

    label("loc_C4B")

    TalkEnd(0xFE)
    Return()

    # Function_9_B5A end

    def Function_10_C4F(): pass

    label("Function_10_C4F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_43(0x1D, 0x0, 0x0, 0xB)
    OP_43(0x1E, 0x0, 0x0, 0xB)
    OP_43(0x20, 0x0, 0x0, 0xC)
    OP_43(0x21, 0x0, 0x0, 0xD)
    OP_43(0x22, 0x0, 0x0, 0xE)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_6D(-63000, 0, -30990, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(5010, 0)
    OP_6C(216000, 0)
    OP_6E(309, 0)

    def lambda_D2F():
        OP_6D(-64690, 1150, -9120, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D2F)

    def lambda_D47():
        OP_67(0, 7950, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D47)

    def lambda_D5F():
        OP_6B(5010, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_D5F)

    def lambda_D6F():
        OP_6C(225000, 8000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_D6F)

    def lambda_D7F():
        OP_6E(309, 8000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_D7F)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0xF)
    OP_43(0x1B, 0x0, 0x0, 0x10)
    Sleep(5000)
    Fade(1000)
    OP_6D(-78370, 6150, 15020, 0)
    OP_67(0, 7610, -10000, 0)
    OP_6B(5010, 0)
    OP_6C(0, 0)
    OP_6E(317, 0)
    OP_43(0x109, 0x0, 0x0, 0x11)
    OP_43(0x1B, 0x0, 0x0, 0x12)
    OP_43(0x10, 0x3, 0x0, 0x1A)

    def lambda_E03():
        OP_6D(-78780, 1500, 14220, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E03)

    def lambda_E1B():
        OP_67(0, 3430, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E1B)

    def lambda_E33():
        OP_6B(5010, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E33)

    def lambda_E43():
        OP_6C(0, 7000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_E43)

    def lambda_E53():
        OP_6E(317, 7000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_E53)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    OP_23(0x155)
    Sleep(1000)

    def lambda_E71():
        OP_6D(-78780, 2200, 14220, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E71)

    def lambda_E89():
        OP_67(0, 2990, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E89)

    def lambda_EA1():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_EA1)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4131   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_C4F end

    def Function_11_EC8(): pass

    label("Function_11_EC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FEE")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F04")
    Sleep(1000)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_FEB")

    label("loc_F04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2B")
    Sleep(1300)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_FEB")

    label("loc_F2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F52")
    Sleep(1600)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_FEB")

    label("loc_F52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F79")
    Sleep(1900)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_FEB")

    label("loc_F79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA0")
    Sleep(2200)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_FEB")

    label("loc_FA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
    Sleep(2500)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_FEB")

    label("loc_FC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEB")
    Sleep(2800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    label("loc_FEB")

    Jump("Function_11_EC8")

    label("loc_FEE")

    Return()

    # Function_11_EC8 end

    def Function_12_FEF(): pass

    label("Function_12_FEF")

    OP_8E(0xFE, 0xFFFF281A, 0x0, 0xFFFFE8B8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF29B4, 0xFFFFF15A, 0xFFFF7180, 0x9C4, 0x0)
    Return()

    # Function_12_FEF end

    def Function_13_1018(): pass

    label("Function_13_1018")

    OP_8E(0xFE, 0xFFFF176C, 0xFFFFF15A, 0xFFFF8918, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF0BC8, 0xFFFFF254, 0xFFFF9DE0, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF0786, 0xFFFFF3B2, 0xFFFF9DEA, 0x9C4, 0x0)
    OP_72(0x1005, 0x0)
    ExitThread()
    Sleep(100)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3B)
    OP_73(0x5)
    OP_8E(0xFE, 0xFFFF0024, 0xFFFFF4AC, 0xFFFF9DAE, 0x9C4, 0x0)
    OP_6F(0x5, 59)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_13_1018 end

    def Function_14_109B(): pass

    label("Function_14_109B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1500)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3B)
    OP_73(0x9)

    def lambda_10C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C8)

    def lambda_10DA():
        OP_8E(0xFE, 0xFFFF0A7E, 0xFFFFF15A, 0xFFFF83E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10DA)
    Sleep(200)
    OP_6F(0x9, 59)
    OP_70(0x9, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0xFE, 0x3)
    OP_8E(0xFE, 0xFFFF281A, 0xFFFFF15A, 0xFFFF83FA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF29AA, 0xFFFFF15A, 0xFFFF70EA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF64E2, 0x0, 0xFFFF6FD2, 0x1388, 0x0)
    Return()

    # Function_14_109B end

    def Function_15_114C(): pass

    label("Function_15_114C")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -50890, 0, -3860, 270)
    OP_8E(0xFE, 0xFFFEDAEA, 0x0, 0xFFFFF11E, 0x7D0, 0x0)
    Return()

    # Function_15_114C end

    def Function_16_1177(): pass

    label("Function_16_1177")

    Sleep(300)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -50220, 0, -4380, 270)
    OP_8E(0xFE, 0xFFFEE288, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
    Return()

    # Function_16_1177 end

    def Function_17_11A7(): pass

    label("Function_17_11A7")

    Sleep(2000)
    SetChrPos(0xFE, -79100, 0, 1940, 0)
    OP_8E(0xFE, 0xFFFECC6C, 0x6D6, 0x30A2, 0x7D0, 0x0)
    Sleep(200)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_73(0xC)
    Sleep(200)

    def lambda_11F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11F8)
    OP_8E(0xFE, 0xFFFECB5E, 0x6D6, 0x3872, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_11A7 end

    def Function_18_121E(): pass

    label("Function_18_121E")

    Sleep(2500)
    SetChrPos(0xFE, -79730, 0, 910, 0)
    OP_8E(0xFE, 0xFFFEC9BA, 0x5F0, 0x2AB2, 0x7D0, 0x0)
    Sleep(1000)

    def lambda_1253():
        OP_8E(0xFE, 0xFFFECB4A, 0x6D6, 0x3872, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1253)
    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
    WaitChrThread(0xFE, 0x3)
    OP_6F(0xC, 59)
    OP_70(0xC, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xC)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_121E end

    def Function_19_129C(): pass

    label("Function_19_129C")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_12E4():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFE016, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_12E4)
    Return()

    # Function_19_129C end

    def Function_20_12FA(): pass

    label("Function_20_12FA")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x155, 0x1, 0x32)
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_1347():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFD846, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1347)
    Return()

    # Function_20_12FA end

    def Function_21_135D(): pass

    label("Function_21_135D")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_13A5():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFD076, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_13A5)
    Return()

    # Function_21_135D end

    def Function_22_13BB(): pass

    label("Function_22_13BB")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_1403():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFC8A6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1403)
    Return()

    # Function_22_13BB end

    def Function_23_1419(): pass

    label("Function_23_1419")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_1461():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFC0D6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1461)
    Return()

    # Function_23_1419 end

    def Function_24_1477(): pass

    label("Function_24_1477")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_14BF():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFB906, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_14BF)
    Return()

    # Function_24_1477 end

    def Function_25_14D5(): pass

    label("Function_25_14D5")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, -95400, 18200, -10980, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_22(0x155, 0x1, 0x46)
    OP_43(0xFE, 0x2, 0x0, 0x1F)

    def lambda_151D():
        OP_8F(0xFE, 0xFFFEEB16, 0x5096, 0xFFFFB136, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_151D)
    Return()

    # Function_25_14D5 end

    def Function_26_1533(): pass

    label("Function_26_1533")

    OP_43(0x10, 0x1, 0x0, 0x13)
    Sleep(150)
    OP_43(0x14, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0x12, 0x1, 0x0, 0x15)
    Sleep(150)
    OP_43(0x16, 0x1, 0x0, 0x19)
    Sleep(100)
    OP_43(0x11, 0x1, 0x0, 0x14)
    Sleep(150)
    OP_43(0x15, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x13, 0x1, 0x0, 0x16)
    Return()

    # Function_26_1533 end

    def Function_27_1583(): pass

    label("Function_27_1583")

    SetChrPos(0xFE, -106330, 3290, 5750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x23AA, 0x960)
    OP_98(0x1, 0xFFFF3990, 0x50B4, 0x231E)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_27_1583 end

    def Function_28_15D9(): pass

    label("Function_28_15D9")

    Sleep(100)
    SetChrPos(0xFE, -105330, 2290, 5750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x2792, 0x578)
    OP_98(0x1, 0xFFFF3990, 0x549C, 0x231E)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_28_15D9 end

    def Function_29_1634(): pass

    label("Function_29_1634")

    Sleep(200)
    SetChrPos(0xFE, -108330, 3290, 5750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x2B7A, 0xD48)
    OP_98(0x1, 0xFFFF2DD8, 0x5884, 0x2AEE)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_29_1634 end

    def Function_30_168F(): pass

    label("Function_30_168F")

    SetChrPos(0xFE, -107330, 2590, 6750, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFEC6FE, 0x2792, 0x960)
    OP_98(0x1, 0xFFFF2DD8, 0x549C, 0x2AEE)
    OP_43(0xFE, 0x2, 0x0, 0x1F)
    OP_98(0x2, 0xFE, 0x2134, 0x2)
    Return()

    # Function_30_168F end

    def Function_31_16E5(): pass

    label("Function_31_16E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16FA")
    OP_99(0xFE, 0x0, 0x7, 0x1770)
    Jump("Function_31_16E5")

    label("loc_16FA")

    Return()

    # Function_31_16E5 end

    def Function_32_16FB(): pass

    label("Function_32_16FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-39800, 0, 29500, 0)
    OP_67(0, 3660, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(0, 0)
    OP_6E(322, 0)
    SetChrPos(0x103, -39060, 0, 42500, 180)
    SetChrPos(0x151, -40340, 0, 41520, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x18, -39080, 0, -15580, 0)
    SetChrPos(0x19, -41000, 0, -16860, 0)
    SetChrPos(0x1A, -58700, 0, -3460, 90)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 18)
    SetChrChipByIndex(0x1A, 18)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x23, 0x80)

    def lambda_17DB():
        OP_6B(3140, 2500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17DB)

    def lambda_17EB():
        OP_6E(322, 2500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_17EB)

    def lambda_17FB():
        OP_67(0, 3660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_17FB)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_43(0x151, 0x3, 0x0, 0x21)
    OP_43(0x103, 0x3, 0x0, 0x22)
    WaitChrThread(0x24, 0x1)

    def lambda_1834():
        OP_6D(-39800, 0, -2300, 5000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1834)
    Sleep(3500)
    Fade(1000)
    OP_67(0, 4920, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(24000, 0)
    OP_6E(364, 0)
    Sleep(1500)
    Sleep(900)

    def lambda_188C():
        OP_8E(0xFE, 0xFFFF6064, 0x0, 0xFFFFF27C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_188C)
    Sleep(1100)

    def lambda_18AC():
        OP_8E(0xFE, 0xFFFF6758, 0x0, 0x503C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_18AC)
    Sleep(100)

    def lambda_18CC():
        OP_8E(0xFE, 0xFFFF5FD8, 0x0, 0x5258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_18CC)
    WaitChrThread(0x1A, 0x1)

    def lambda_18EC():
        OP_8E(0xFE, 0xFFFF6384, 0x0, 0xFFFFF59C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_18EC)
    WaitChrThread(0x1A, 0x1)

    def lambda_190C():
        OP_8E(0xFE, 0xFFFF6384, 0x0, 0x599C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_190C)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_16FB end

    def Function_33_193E(): pass

    label("Function_33_193E")


    def lambda_1944():
        OP_8E(0xFE, 0xFFFF626C, 0x0, 0xFFFFF470, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1944)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 270, 500)
    Sleep(500)
    OP_8C(0x151, 180, 500)
    Sleep(500)
    OP_8C(0x151, 0, 500)
    Sleep(200)

    def lambda_1988():
        OP_8E(0xFE, 0xFFFF626C, 0x0, 0xA230, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1988)
    Return()

    # Function_33_193E end

    def Function_34_199E(): pass

    label("Function_34_199E")


    def lambda_19A4():
        OP_8E(0xFE, 0xFFFF676C, 0x0, 0xFFFFF088, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19A4)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    OP_8C(0x103, 270, 500)
    Sleep(500)
    OP_8C(0x103, 0, 500)
    Sleep(300)

    def lambda_19E1():
        OP_8E(0xFE, 0xFFFF676C, 0x0, 0xA604, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19E1)
    Return()

    # Function_34_199E end

    def Function_35_19F7(): pass

    label("Function_35_19F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-63900, -3150, -27000, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(4820, 0)
    OP_6C(230000, 0)
    OP_6E(368, 0)
    SetChrPos(0x103, -79300, -3250, -31120, 90)
    SetChrPos(0x151, -79300, -3250, -30060, 90)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x151, 0x40)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x23, 0x80)

    def lambda_1A97():
        OP_6D(-72900, -3750, -30580, 7000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1A97)

    def lambda_1AAF():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1AAF)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2500)
    OP_70(0xA, 0x3C)
    OP_73(0xA)

    def lambda_1AD8():
        OP_8E(0xFE, 0xFFFEE094, 0xFFFFF254, 0xFFFF8670, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AD8)

    def lambda_1AF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AF3)
    Sleep(200)

    def lambda_1B0A():
        OP_8E(0xFE, 0xFFFEDAF4, 0xFFFFF254, 0xFFFF8A94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1B0A)

    def lambda_1B25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_1B25)
    WaitChrThread(0x24, 0x0)
    Fade(1000)
    OP_6D(-75840, -3500, -30580, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(270000, 0)
    OP_6E(320, 0)
    Sleep(1000)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x151, 0x1)

    ChrTalk(    #14
        0x151,
        "#1650F#2P呼，终于到地面上了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#1646F已经傍晚了啊。\x01",
            "比想像的要花时间呢。\x02\x03",

            "#1642F…………得赶快了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #16
        0x151,
        (
            "#1652F#2P嗯嗯，但是……\x02\x03",

            "#1652F雪拉扎德小姐，没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x103, 0x151, 500)
    Sleep(1000)

    ChrTalk(    #17
        0x103,
        "#1643F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x151,
        (
            "#1656F#2P因为你看起来\x01",
            "脸色不太好……\x02\x03",

            "#1650F是不是有点累了？\x01",
            "要不要先休息一下呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#1647F不、不用啦！\x02\x03",

            "别看我这样，\x01",
            "也是经过相当的锻炼的。\x02\x03",

            "#1644F别小看游击士的体力哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x151,
        (
            "#1653F#2P也、也是。\x01",
            "对不起。\x02",
        )
    )

    Jump("loc_1DA2")

    label("loc_1DA2")

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#1646F……倒是你……\x02\x03",

            "（这家伙，\x01",
            "  紧跟着我的步伐……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)
    OP_8C(0x103, 135, 500)
    Sleep(300)

    ChrTalk(    #22
        0x103,
        "#1643F（………………难道没事吗？）\x02",
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x103,
        (
            "#1642F（这么说来，\x01",
            "  那样逃来逃去居然一口气都不喘……）\x02\x03",

            "#1643F（不，途中好像……\x01",
            "  还跑在我的前面……？？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(600)

    ChrTalk(    #24
        0x151,
        "#1651F#2P#40W？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        "#1644F（呜…………还这么从容吗！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x151,
        (
            "#1650F#2P还是休息一下吧。\x02\x03",

            "#1651F我带了零食哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#1646F不、不用了。\x02\x03",

            "现在还是先考虑去协会避难吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 500)
    Sleep(300)

    ChrTalk(    #28
        0x103,
        (
            "#1646F（虽然发生了很多麻烦，\x01",
            "  但委托内容只是王都的导游……）\x02\x03",

            "#1642F（回到协会委托就结束了。\x01",
            "  …………我赢了！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2059():

        label("loc_2059")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_2059")

    QueueWorkItem2(0x151, 3, lambda_2059)

    def lambda_206A():
        OP_6D(-73840, -3500, -30580, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_206A)

    def lambda_2082():
        OP_8E(0xFE, 0xFFFEE864, 0xFFFFF18C, 0xFFFF8670, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2082)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #29
        0x103,
        "#1644F……好啦，别发呆啦！\x02",
    )

    CloseMessageWindow()
    OP_44(0x151, 0x3)
    OP_62(0x151, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_20DF():
        OP_8E(0xFE, 0xFFFEE2C4, 0xFFFFF254, 0xFFFF8A94, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_20DF)
    WaitChrThread(0x151, 0x1)
    TurnDirection(0x151, 0x103, 500)
    Sleep(100)

    ChrTalk(    #30
        0x151,
        (
            "#1653F#2P我觉得还是\x01",
            "稍微休息一下为好……\x02\x03",

            "真的没问题？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        "#1647F你还真是纠缠不休……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x17, -63000, -3000, -35500, 180)
    ClearChrFlags(0x17, 0x80)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #32
        0x17,
        "怒吼的声音",
        "#2P可恶～！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_220B():
        OP_6D(-66780, -3750, -32460, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_220B)

    def lambda_2223():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2223)
    WaitChrThread(0x24, 0x0)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_70(0x9, 0x3B)
    OP_73(0x9)

    def lambda_2248():
        OP_8E(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF842C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2248)

    def lambda_2263():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2263)
    Sleep(500)

    ChrTalk(    #33
        0x103,
        "#1644F#1P（……快躲起来！）\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0x1)

    NpcTalk(    #34
        0x17,
        "眼神凶恶的男子",
        (
            "#144F那是我熬夜做的啊！\x01",
            "那个老奸巨猾的主编～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22F3():
        OP_8E(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF8C10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_22F3)
    WaitChrThread(0x17, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_2318():
        OP_96(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF842C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2318)

    def lambda_2336():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2336)
    WaitChrThread(0x17, 0x1)

    NpcTalk(    #35
        0x17,
        "眼神凶恶的男子",
        (
            "#145F诺蒂亚那家伙也是，\x01",
            "搞什么啊，真可恶。\x02\x03",

            "说什么『请去找\x01",
            "更热门的好素材』？\x02\x03",

            "#144F这种事\x01",
            "我也知道啊！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23E8():
        OP_8E(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF8C10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_23E8)
    WaitChrThread(0x17, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_240D():
        OP_96(0xFE, 0xFFFF09E8, 0xFFFFF18C, 0xFFFF842C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_240D)

    def lambda_242B():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_242B)
    WaitChrThread(0x17, 0x1)
    OP_59()
    Fade(1000)
    OP_6D(-74140, -3500, -28760, 0)
    OP_67(0, 3800, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(280000, 0)
    OP_6E(320, 0)
    SetChrPos(0x103, -72900, -3500, -28960, 100)
    SetChrPos(0x151, -74120, -3500, -29060, 100)
    Sleep(1000)

    ChrTalk(    #36
        0x151,
        "#1652F（怎、怎么了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#1646F（唔……莫名其妙呢。）\x02\x03",

            "（难不成，\x01",
            "  是什么暗号……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x103,
        (
            "#1643F（不会吧…………\x01",
            "  他也是黑衣人一伙的！？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x151,
        "#1653F（是、是吗？）\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #40
        0x17,
        "怒吼的声音",
        "混帐啊～！！\x02",
    )

    CloseMessageWindow()
    OP_22(0x8E, 0x0, 0x64)

    ChrTalk(    #41
        0x103,
        (
            "#1642F（虽然没有确证，不过……）\x02\x03",

            "（看他那个眼神。\x01",
            "  怎么看都不像是正经人。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x151,
        "#1652F（原来如此……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#1646F（事到如今，\x01",
            "  绝对不能被抓住。）\x02\x03",

            "（要慎重，并且仔细地行动……）\x02\x03",

            "#1642F（哪里有其它的路可走……）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 135, 500)
    Sleep(500)
    OP_8C(0x103, 0, 500)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2706():
        OP_6D(-74240, -3500, -14080, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_2706)

    def lambda_271E():
        OP_67(0, 5960, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_271E)

    def lambda_2736():
        OP_6C(310000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2736)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #44
        0x103,
        (
            "#1643F（那间屋子……\x01",
            "  记得应该是空房……！）\x02\x03",

            "#1644F（…………这边。\x01",
            "  跟我来！）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x103, -73400, -3500, -20900, 0)
    SetChrPos(0x151, -73400, -3500, -24400, 0)

    def lambda_27D9():
        OP_8E(0xFE, 0xFFFEE60C, 0xFFFFF3B2, 0xFFFFC091, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27D9)
    Sleep(50)

    def lambda_27F9():
        OP_8E(0xFE, 0xFFFEE148, 0xFFFFF254, 0xFFFFBE60, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_27F9)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_70(0x11, 0x3C)
    OP_73(0x11)
    OP_8C(0x103, 180, 500)
    Sleep(100)

    def lambda_2852():
        OP_8F(0xFE, 0xFFFEE878, 0xFFFFF3B2, 0xFFFFC091, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2852)
    WaitChrThread(0x103, 0x1)

    def lambda_2872():
        OP_8E(0xFE, 0xFFFEE4CC, 0xFFFFF3B2, 0xFFFFC091, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2872)
    WaitChrThread(0x151, 0x1)

    def lambda_2892():
        OP_8E(0xFE, 0xFFFEE4CC, 0xFFFFF4AC, 0xFFFFC824, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2892)

    def lambda_28AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_28AD)
    WaitChrThread(0x151, 0x1)

    def lambda_28C4():
        OP_8F(0xFE, 0xFFFEE60C, 0xFFFFF3B2, 0xFFFFC091, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28C4)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(500)
    OP_8C(0x103, 270, 500)
    Sleep(800)
    OP_8C(0x103, 180, 500)
    Sleep(500)

    def lambda_2908():
        OP_8F(0xFE, 0xFFFEE60C, 0xFFFFF4AC, 0xFFFFC824, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2908)

    def lambda_2923():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2923)
    WaitChrThread(0x103, 0x1)
    OP_72(0x11, 0x8)
    ExitThread()
    OP_6F(0x11, 30)
    OP_70(0x11, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x11)

    def lambda_2956():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2956)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x24, 0x1)
    SetChrPos(0x17, -54160, -3750, -21840, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x18, -55880, 0, -3100, 180)
    SetChrPos(0x19, -55460, 0, -5260, 0)
    SetChrPos(0x1A, -57020, 0, -5560, 0)
    OP_6D(-54160, -3750, -21840, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(320, 0)
    OP_6A(0x17)
    Sleep(1000)

    def lambda_2A0D():
        OP_6B(2920, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2A0D)
    OP_43(0x17, 0x3, 0x0, 0x24)
    FadeToBright(2000, 0)
    OP_0D()
    #Sleep(500)

    NpcTalk(    #45 op#A
        0x17,
        "眼神凶恶的男子",
        (
            "#142F#32A这么简单就能\x01",
            "弄到内幕的话……\x02",
        )
    )

    Sleep(3600)

    NpcTalk(    #46 op#A
        0x17,
        "眼神凶恶的男子",
        (
            "#144F#29A#3S谁都不用\x01",
            "这么辛苦啦！！\x02",
        )
    )

    Sleep(3200)

    ChrTalk(    #47 op#A
        0x18,
        (
            "#24A#2P你们走下面。\x01",
            "我去上面。\x02",
        )
    )

    Sleep(2800)

    ChrTalk(    #48 op#A
        0x19,
        "#7A#4P好。\x02",
    )

    Sleep(1200)
    OP_8C(0x19, 180, 500)
    Sleep(200)

    def lambda_2B10():
        OP_8E(0xFE, 0xFFFF270C, 0xFFFFF15A, 0xFFFFB17C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2B10)
    Sleep(500)
    OP_43(0x1A, 0x3, 0x0, 0x25)
    OP_8C(0x18, 270, 500)
    Sleep(200)

    def lambda_2B43():
        OP_8E(0xFE, 0xFFFEFF20, 0x0, 0xFFFFF3E4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2B43)
    Sleep(3000)

    NpcTalk(    #49 op#A
        0x17,
        "眼神凶恶的男子",
        (
            "#142F#38A啧……\x01",
            "还得再去拜托雷蒙德吗……\x02",
        )
    )

    Sleep(4300)
    WaitChrThread(0x17, 0x3)

    NpcTalk(    #50
        0x17,
        "眼神凶恶的男子",
        (
            "#145F啊…………\x01",
            "记得那家伙到离宫工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 500)
    Sleep(300)

    NpcTalk(    #51
        0x17,
        "眼神凶恶的男子",
        "#142F可恶，那么远啊。\x02",
    )

    CloseMessageWindow()

    def lambda_2C31():
        OP_8E(0xFE, 0xFFFF6294, 0x0, 0xFFFFAF88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2C31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_END)), "loc_2C9E")

    NpcTalk(    #52 op#A
        0x17,
        "眼神凶恶的男子",
        (
            "#140F#35A……对了，\x01",
            "待会儿还得\x01",
            "把照相机要回来呢。\x02",
        )
    )

    Sleep(4500)

    label("loc_2C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 4)), scpexpr(EXPR_END)), "loc_2CFF")

    NpcTalk(    #53 op#A
        0x17,
        "眼神凶恶的男子",
        (
            "#145F#47A那小鬼，让我多花了\x01",
            "３０００米拉感光结晶回路费……\x02",
        )
    )

    Sleep(5500)

    label("loc_2CFF")

    OP_6A(0xFF)

    NpcTalk(    #54 op#A
        0x17,
        "眼神凶恶的男子",
        (
            "#145F#40A#1P唉，气死人了～……\x01",
            "还是先去补充香烟吧……\x02",
        )
    )

    Sleep(5000)
    Fade(1000)
    OP_6D(-74240, -3500, -14080, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(310000, 0)
    OP_6E(320, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, -73100, -3500, -15300, 0)
    SetChrPos(0x151, -72100, -3500, -15300, 0)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    SetChrPos(0x19, -63040, -3500, -17320, 270)
    SetChrPos(0x1A, -60040, -3500, -17320, 270)
    Sleep(2000)

    def lambda_2DFA():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2DFA)
    Sleep(100)
    OP_43(0x1A, 0x3, 0x0, 0x26)
    Sleep(2000)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x19, 0x1)

    def lambda_2E4F():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFF9980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2E4F)
    WaitChrThread(0x19, 0x1)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T4152   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_35_19F7 end

    def Function_36_2E8E(): pass

    label("Function_36_2E8E")


    def lambda_2E94():
        OP_8E(0xFE, 0xFFFF2C70, 0x0, 0xFFFFE9BC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2E94)
    WaitChrThread(0x17, 0x1)

    def lambda_2EB4():
        OP_8E(0xFE, 0xFFFF33B4, 0x0, 0xFFFFF164, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2EB4)
    WaitChrThread(0x17, 0x1)

    def lambda_2ED4():
        OP_8E(0xFE, 0xFFFF5C18, 0x0, 0xFFFFF164, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2ED4)
    WaitChrThread(0x17, 0x1)

    def lambda_2EF4():
        OP_8E(0xFE, 0xFFFF6294, 0x0, 0xFFFFF7A4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2EF4)
    WaitChrThread(0x17, 0x1)

    def lambda_2F14():
        OP_8E(0xFE, 0xFFFF6294, 0x0, 0xAF0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F14)
    WaitChrThread(0x17, 0x1)
    Return()

    # Function_36_2E8E end

    def Function_37_2F2F(): pass

    label("Function_37_2F2F")

    OP_8C(0x1A, 135, 500)
    Sleep(200)

    def lambda_2F41():
        OP_8E(0xFE, 0xFFFF270C, 0xFFFFF15A, 0xFFFFE534, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F41)
    WaitChrThread(0x1A, 0x1)

    def lambda_2F61():
        OP_8E(0xFE, 0xFFFF270C, 0xFFFFF15A, 0xFFFFB758, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F61)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_37_2F2F end

    def Function_38_2F7C(): pass

    label("Function_38_2F7C")


    def lambda_2F82():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFFBC58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F82)
    WaitChrThread(0x1A, 0x1)

    def lambda_2FA2():
        OP_8E(0xFE, 0xFFFEDFF4, 0xFFFFF254, 0xFFFF9980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2FA2)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_38_2F7C end

    def Function_39_2FBD(): pass

    label("Function_39_2FBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    OP_6D(-60000, -3750, -18720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(296000, 0)
    OP_6E(338, 0)
    SetChrPos(0x103, -71720, -2900, -14320, 180)
    SetChrPos(0x151, -72680, -2900, -14320, 180)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_304E():
        OP_6D(-72640, -3500, -14280, 8000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_304E)

    def lambda_3066():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_3066)

    def lambda_3076():
        OP_6C(335000, 8000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_3076)

    def lambda_3086():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_3086)
    FadeToBright(2000, 0)
    OP_22(0x1C2, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x24, 0x0)
    OP_23(0x1C2)
    OP_70(0x11, 0x3C)
    OP_73(0x11)

    def lambda_30B7():
        OP_8E(0xFE, 0xFFFEE7D8, 0xFFFFF4AC, 0xFFFFC220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30B7)

    def lambda_30D2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_30D2)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(1000)

    def lambda_30F5():
        OP_6D(-75440, -3500, -20580, 4000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_30F5)
    OP_43(0x151, 0x3, 0x0, 0x28)
    Sleep(2000)

    def lambda_3119():
        OP_8F(0xFE, 0xFFFEE7D8, 0xFFFFF254, 0xFFFFBE38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3119)
    WaitChrThread(0x103, 0x1)
    OP_72(0x11, 0x8)
    ExitThread()
    OP_6F(0x11, 30)
    OP_70(0x11, 0x0)
    OP_22(0x7, 0x0, 0x64)

    def lambda_3152():
        OP_8E(0xFE, 0xFFFED9DC, 0xFFFFF254, 0xFFFFB168, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3152)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 60, 500)
    Sleep(300)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #55
        0x103,
        (
            "#1642F………对了，\x01",
            "在格兰赛尔城的什么地方来着？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x151,
        (
            "#1652F行政区域哦。\x02\x03",

            "期限是今天正午之前。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x103, 0x151, 500)
    Sleep(500)

    ChrTalk(    #57
        0x103,
        (
            "#1643F正、正午！？\x01",
            "……今天的！？\x02\x03",

            "#1647F没时间啦！\x01",
            "这种事怎么不早说嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x151,
        (
            "#1654F被继承人死后一个月以内。\x02\x03",

            "#1652F利贝尔的法律\x01",
            "似乎就是这么规定的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        (
            "#1645F啊，这样啊……\x01",
            "我对法律就是头痛啊。\x02\x03",

            "克鲁茨前辈倒是\x01",
            "好像全部都背得下来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x151,
        (
            "#1653F是、是啊……\x02\x03",

            "#1651F呵呵呵……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#1641F啊哈哈哈哈！\x02\x03",

            "#1640F……走吧。\x01",
            "没空绕远路了。\x02\x03",

            "爱娜，你明白吧。\x01",
            "就照刚才商量的办。\x02\x03",

            "绝对要突破那些家伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x151,
        (
            "#1650F………雪拉扎德小姐。\x02\x03",

            "能委托你真是太好了。\x02\x03",

            "你是靠自己双脚\x01",
            "坚强地生活的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#1646F……不是这样啦。\x02\x03",

            "#1640F还有，『雪拉扎德小姐』\x01",
            "这个称呼还是免了吧。\x02\x03",

            "你的发音听起来\x01",
            "总感觉特别长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x151,
        "#1653F是、是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x103,
        (
            "#1640F嗯，\x01",
            "感觉很浪费时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x151,
        (
            "#1650F……………………\x02\x03",

            "#1654F……那么…………\x02\x03",

            "#1652F雪拉扎德，\x01",
            "我重新委托你一件事。\x02\x03",

            "请护送我\x01",
            "到格兰赛尔城吧。\x02",
        )
    )

    Jump("loc_35D3")

    label("loc_35D3")

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        (
            "#1642F我接受了。\x02\x03",

            "#1640F无论如何，\x01",
            "我一定会把你带去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x151,
        "#1651F拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_6F(0x11, 0)
    OP_71(0x11, 0x8)
    ExitThread()
    EventEnd(0x0)
    Return()

    # Function_39_2FBD end

    def Function_40_364C(): pass

    label("Function_40_364C")


    def lambda_3652():
        OP_8E(0xFE, 0xFFFEE418, 0xFFFFF254, 0xFFFFBAA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3652)

    def lambda_366D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_366D)
    WaitChrThread(0x151, 0x1)

    def lambda_3684():
        OP_8E(0xFE, 0xFFFED9DC, 0xFFFFF254, 0xFFFFB168, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3684)
    WaitChrThread(0x151, 0x1)

    def lambda_36A4():
        OP_8E(0xFE, 0xFFFED9DC, 0xFFFFF254, 0xFFFFA7E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_36A4)
    WaitChrThread(0x151, 0x1)
    Sleep(500)
    OP_8C(0x151, 0, 500)
    Return()

    # Function_40_364C end

    def Function_41_36CB(): pass

    label("Function_41_36CB")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3749")
    OP_8C(0x103, 270, 500)
    Sleep(500)
    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0x103, 0, 500)
    Sleep(200)

    ChrTalk(    #69
        0x103,
        (
            "#1640F走这条路就能去北街区。\x02\x03",

            "赶快去格兰赛尔城吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382F")

    label("loc_3749")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #70
        0x151,
        (
            "#1650F雪拉扎德，\x01",
            "要先回一次协会吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #71
        0x103,
        (
            "#1646F不，没那个时间了。\x02\x03",

            "这个时间\x01",
            "克鲁茨前辈应该也不在……\x02\x03",

            "#1640F我们就直接\x01",
            "赶去格兰赛尔城吧。\x02",
        )
    )

    Jump("loc_3817")

    label("loc_3817")

    CloseMessageWindow()
    OP_A2(0x0)
    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)

    label("loc_382F")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_41_36CB end

    def Function_42_3837(): pass

    label("Function_42_3837")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3890")
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #72
        0x103,
        (
            "#1640F这边是码头。\x02\x03",

            "还是不要用船\x01",
            "潜入王城吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3979")

    label("loc_3890")


    ChrTalk(    #73
        0x103,
        "#1643F啊，这边是码头。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #74
        0x151,
        (
            "#1656F嗯嗯。\x02\x03",

            "也可以考虑乘船\x01",
            "潜入格兰赛尔城……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #75
        0x103,
        (
            "#1645F还是不要吧。\x02\x03",

            "就是被警卫射杀了\x01",
            "也没什么好抱怨的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x151,
        "#1650F是、是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3979")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_42_3837 end

    def Function_43_3995(): pass

    label("Function_43_3995")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_39EF")
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #77
        0x103,
        (
            "#1640F这边是地下水路哦。\x02\x03",

            "赶快去格兰赛尔城吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A8F")

    label("loc_39EF")


    ChrTalk(    #78
        0x103,
        "#1642F这边是地下水路吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x151,
        "#1650F锁好像开着……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #80
        0x103,
        (
            "#1645F我说，\x01",
            "没空绕远路了。\x02\x03",

            "#1642F赶快去格兰赛尔城吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3A8F")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_43_3995 end

    def Function_44_3AAB(): pass

    label("Function_44_3AAB")

    EventBegin(0x2)

    def lambda_3AB3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3AB3)
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #81
        0x103,
        (
            "#1640F怎么办？\x01",
            "稍微休息一下吗？\x02",
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
        1,
        (
            "【休息】\x01",        # 0
            "【不用了】\x01",      # 1
        )
    )

    Jump("loc_3B39")

    label("loc_3B39")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B60"),
        (SWITCH_DEFAULT, "loc_3C17"),
    )


    label("loc_3B60")

    OP_20(0xBB8)
    OP_8C(0x103, 0, 500)
    FadeToDark(1000, 0, -1)

    def lambda_3B7C():
        OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B7C)
    OP_43(0x151, 0x3, 0x0, 0x2D)
    OP_0D()
    WaitChrThread(0x103, 0x1)
    OP_44(0x151, 0x3)
    SetChrPos(0x103, -72140, -2900, -14300, 180)
    SetChrPos(0x151, -72140, -2900, -14300, 180)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x50, 0xFC, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    Sleep(1000)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)

    def lambda_3BF7():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF6DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BF7)
    OP_0D()
    WaitChrThread(0x103, 0x1)
    EventEnd(0x2)
    Jump("loc_3C30")

    label("loc_3C17")

    OP_90(0xEE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    EventEnd(0x2)
    Jump("loc_3C30")

    label("loc_3C30")

    Return()

    # Function_44_3AAB end

    def Function_45_3C31(): pass

    label("Function_45_3C31")

    Sleep(200)
    OP_8E(0x151, 0xFFFEE634, 0xFFFFF3B2, 0xFFFFC0E0, 0x3E8, 0x0)
    OP_8E(0x151, 0xFFFEE634, 0xFFFFF3B2, 0xFFFFC4C8, 0x3E8, 0x0)
    Return()

    # Function_45_3C31 end

    def Function_46_3C5F(): pass

    label("Function_46_3C5F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #82
        (
            "\x07\x05　　 待售　　\x01",
            "※可经营饮食店\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_3C5F end

    def Function_47_3CB0(): pass

    label("Function_47_3CB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D1B")
    Sleep(300)
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #83
        0x103,
        (
            "#1640F这边是地下水路。\x02\x03",

            "我们赶快去格兰赛尔城吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC1")

    label("loc_3D1B")


    ChrTalk(    #84
        0x103,
        "#1642F这边是地下水路。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x151,
        "#1650F好像没有上锁……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #86
        0x103,
        (
            "#1645F我说，\x01",
            "现在没有功夫绕路吧。\x02\x03",

            "#1642F赶快去格兰赛尔城吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3DC1")

    TalkEnd(0xFF)
    Jump("loc_3E0E")

    label("loc_3DC7")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #87
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_3E0E")

    Return()

    # Function_47_3CB0 end

    def Function_48_3E0F(): pass

    label("Function_48_3E0F")

    SetPlaceName(0xB8)
    Return()

    # Function_48_3E0F end

    def Function_49_3E13(): pass

    label("Function_49_3E13")

    SetPlaceName(0xB7)
    Return()

    # Function_49_3E13 end

    def Function_50_3E17(): pass

    label("Function_50_3E17")

    SetPlaceName(0xAF)
    Return()

    # Function_50_3E17 end

    SaveToFile()

Try(main)
