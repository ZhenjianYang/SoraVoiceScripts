from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3100_1 ._SN',
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
        '库诺',                                 # 9
        '科奇莫爷爷',                           # 10
        '莫妮卡',                               # 11
        '布鲁诺',                               # 12
        '阿利瑟',                               # 13
        '温丝',                                 # 14
        '自动扶梯',                             # 15
        '雾香',                                 # 16
        '斯坦因',                               # 17
        '兰达老人',                             # 18
        '王',                                   # 19
        '运输车',                               # 20
        '伊格尔',                               # 21
        '蔡斯市·工房区',                       # 22
        '托兰特平原道方向',                     # 23
        '利塔街道方向',                         # 24
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
        'ED6_DT07/CH01060 ._CH',             # 00
        'ED6_DT07/CH01100 ._CH',             # 01
        'ED6_DT07/CH02490 ._CH',             # 02
        'ED6_DT07/CH01530 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01470 ._CH',             # 05
        'ED6_DT07/CH02610 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
        'ED6_DT07/CH01000 ._CH',             # 08
        'ED6_DT07/CH01760 ._CH',             # 09
        'ED6_DT07/CH01250 ._CH',             # 0A
        'ED6_DT26/CH20311 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01060P._CP',             # 00
        'ED6_DT07/CH01100P._CP',             # 01
        'ED6_DT07/CH02490P._CP',             # 02
        'ED6_DT07/CH01530P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01470P._CP',             # 05
        'ED6_DT07/CH02610P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
        'ED6_DT07/CH01000P._CP',             # 08
        'ED6_DT07/CH01760P._CP',             # 09
        'ED6_DT07/CH01250P._CP',             # 0A
        'ED6_DT26/CH20311P._CP',             # 0B
    )

    DeclNpc(
        X                   = 38920,
        Z                   = 0,
        Y                   = 69060,
        Direction           = 90,
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
        X                   = 37980,
        Z                   = 0,
        Y                   = 77980,
        Direction           = 315,
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
        X                   = 38350,
        Z                   = 0,
        Y                   = 64680,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 36810,
        Z                   = 0,
        Y                   = 45690,
        Direction           = 0,
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
        X                   = 14780,
        Z                   = 3500,
        Y                   = 72610,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 16640,
        Z                   = 3500,
        Y                   = 73500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 28770,
        Z                   = 0,
        Y                   = 61520,
        Direction           = 45,
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
        X                   = 20010,
        Z                   = 0,
        Y                   = 60550,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 42470,
        Z                   = 0,
        Y                   = 55580,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 42250,
        Z                   = 0,
        Y                   = 54550,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 58280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -17220,
        Z                   = 8000,
        Y                   = 59000,
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
        X                   = 81330,
        Z                   = 0,
        Y                   = 53110,
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
        X                   = 42990,
        Z                   = 0,
        Y                   = 104270,
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
        X                   = 39780,
        Y                   = 0,
        Z                   = 90710,
        Range               = 46240,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x16544,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 69760,
        Y                   = 0,
        Z                   = 48040,
        Range               = 70360,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xE20E,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 7780,
        Y                   = -1000,
        Z                   = 63930,
        Range               = 6420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xEA1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 6420,
        Y                   = -1000,
        Z                   = 58250,
        Range               = 7860,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xD5D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 43700,
        Y                   = 0,
        Z                   = 63080,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 40200,
        Y                   = 0,
        Z                   = 66870,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 52230,
        Y                   = 0,
        Z                   = 54590,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 51500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 47450,
        Y                   = 450,
        Z                   = 48500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 59950,
        Y                   = 0,
        Z                   = 25220,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 36000,
        Y                   = 0,
        Z                   = 54740,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = 27020,
        Y                   = 0,
        Z                   = 63460,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = 23130,
        Y                   = 0,
        Z                   = 82450,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 64030,
        Y                   = 0,
        Z                   = 69550,
        Range               = 1200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )


    DeclActor(
        TriggerX            = 33000,
        TriggerZ            = 500,
        TriggerY            = 85510,
        TriggerRange        = 800,
        ActorX              = 33000,
        ActorZ              = 1500,
        ActorY              = 85510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 56700,
        TriggerZ            = 0,
        TriggerY            = 48320,
        TriggerRange        = 1000,
        ActorX              = 56700,
        ActorZ              = 1000,
        ActorY              = 48320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30800,
        TriggerZ            = 0,
        TriggerY            = 63150,
        TriggerRange        = 1000,
        ActorX              = 30800,
        ActorZ              = 3000,
        ActorY              = 63150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35000,
        TriggerZ            = 500,
        TriggerY            = 87990,
        TriggerRange        = 800,
        ActorX              = 33610,
        ActorZ              = 1850,
        ActorY              = 87900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_55A",          # 00, 0
        "Function_1_71F",          # 01, 1
        "Function_2_85B",          # 02, 2
        "Function_3_9D8",          # 03, 3
        "Function_4_BE8",          # 04, 4
        "Function_5_C0C",          # 05, 5
        "Function_6_C30",          # 06, 6
        "Function_7_16E3",         # 07, 7
        "Function_8_17CF",         # 08, 8
        "Function_9_19B6",         # 09, 9
        "Function_10_2055",        # 0A, 10
        "Function_11_2643",        # 0B, 11
        "Function_12_2934",        # 0C, 12
        "Function_13_2A92",        # 0D, 13
        "Function_14_2C12",        # 0E, 14
        "Function_15_2F94",        # 0F, 15
        "Function_16_3162",        # 10, 16
        "Function_17_347F",        # 11, 17
        "Function_18_34E7",        # 12, 18
        "Function_19_3510",        # 13, 19
        "Function_20_3522",        # 14, 20
        "Function_21_3A06",        # 15, 21
        "Function_22_3BC0",        # 16, 22
        "Function_23_3F65",        # 17, 23
        "Function_24_3F86",        # 18, 24
        "Function_25_3FBB",        # 19, 25
        "Function_26_3FF0",        # 1A, 26
        "Function_27_404A",        # 1B, 27
        "Function_28_4080",        # 1C, 28
        "Function_29_419E",        # 1D, 29
        "Function_30_42BC",        # 1E, 30
        "Function_31_4355",        # 1F, 31
        "Function_32_4691",        # 20, 32
        "Function_33_4695",        # 21, 33
        "Function_34_4699",        # 22, 34
        "Function_35_469D",        # 23, 35
        "Function_36_46A1",        # 24, 36
        "Function_37_46A5",        # 25, 37
        "Function_38_46A9",        # 26, 38
    )


    def Function_0_55A(): pass

    label("Function_0_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5FC")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x9, 12790, 0, 61820, 265)
    OP_43(0x9, 0x0, 0x0, 0x2)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5B9")
    SetChrPos(0xB, 18190, 0, 57240, 120)
    SetChrPos(0x14, 20310, 0, 56290, 180)
    SetChrFlags(0xD, 0x80)
    Jump("loc_5F9")

    label("loc_5B9")

    SetChrPos(0xB, 8520, 0, 59530, 185)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x12, 33570, 0, 57740, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4")
    SetChrFlags(0x12, 0x10)

    label("loc_5F4")

    SetChrFlags(0xD, 0x80)

    label("loc_5F9")

    Jump("loc_6D8")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_64A")
    SetChrPos(0x8, 41870, 0, 61820, 270)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, 40930, 0, 61820, 90)
    SetChrFlags(0xA, 0x10)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrPos(0x9, 34530, 0, 75930, 270)
    Jump("loc_6D8")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_69D")
    SetChrPos(0x8, 41870, 0, 61820, 0)
    SetChrPos(0xA, 45950, 0, 61990, 0)
    SetChrFlags(0xB, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrPos(0x9, 34530, 0, 75930, 270)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_6D8")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_6CE")
    SetChrPos(0xA, 45950, 0, 61990, 0)
    OP_43(0x9, 0x0, 0x0, 0x3)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_6D8")

    label("loc_6CE")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_705")
    OP_28(0x88, 0x1, 0x10)
    OP_28(0x88, 0x1, 0x20)
    OP_28(0x88, 0x1, 0x40)
    OP_28(0x6C, 0x4, 0x40)
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 22)
    Jump("loc_71E")

    label("loc_705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_71E")
    OP_28(0x6C, 0x1, 0x20)
    OP_28(0x6C, 0x4, 0x10)
    OP_A3(0x10F1)
    Event(1, 2)

    label("loc_71E")

    Return()

    # Function_0_55A end

    def Function_1_71F(): pass

    label("Function_1_71F")

    OP_16(0x2, 0xFA0, 0xFFFE94B8, 0xFFFEF278, 0x230051)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79E")
    OP_72(0xE, 0x8)
    OP_72(0x10, 0x8)
    OP_76(0xFF, 0x25, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_77E")
    OP_A1(0x13, 0x11)
    SetChrPos(0x13, 20000, 0, 55180, 270)
    Jump("loc_79B")

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_79B")
    OP_A1(0x13, 0x11)
    SetChrPos(0x13, 32590, 0, 59100, 90)

    label("loc_79B")

    Jump("loc_7CF")

    label("loc_79E")

    OP_43(0xE, 0x0, 0x0, 0x1B)
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    SoundDistance(0xA0, 0x1CC, 0xADC, 0xE63C, 0x2710, 0x7530, 0x64, 0x0)

    label("loc_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E0")
    OP_71(0x11, 0x4)

    label("loc_7E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_800")
    OP_71(0x1, 0x4)
    OP_72(0x15, 0x4)
    Jump("loc_80E")

    label("loc_800")

    OP_72(0x1, 0x4)
    OP_71(0x15, 0x4)
    OP_64(0x2, 0x1)

    label("loc_80E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82C")
    OP_71(0x16, 0x4)
    OP_64(0x3, 0x1)
    Jump("loc_83B")

    label("loc_82C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83B")
    OP_64(0x3, 0x1)

    label("loc_83B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85A")
    OP_64(0x1, 0x1)

    label("loc_85A")

    Return()

    # Function_1_71F end

    def Function_2_85B(): pass

    label("Function_2_85B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_9C2")

    label("loc_880")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_899")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_9C2")

    label("loc_899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_9C2")

    label("loc_8B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_9C2")

    label("loc_8CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_9C2")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_9C2")

    label("loc_8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_916")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_9C2")

    label("loc_916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_9C2")

    label("loc_92F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_9C2")

    label("loc_948")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_9C2")

    label("loc_961")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_9C2")

    label("loc_97A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_9C2")

    label("loc_993")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_9C2")

    label("loc_9AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_9C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_9C2")

    label("loc_9D7")

    Return()

    # Function_2_85B end

    def Function_3_9D8(): pass

    label("Function_3_9D8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9F9"),
        (1, "loc_A17"),
        (2, "loc_A35"),
        (SWITCH_DEFAULT, "loc_A8F"),
    )


    label("loc_9F9")

    SetChrPos(0x9, 34000, 0, 71810, 90)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8F")

    label("loc_A17")

    SetChrPos(0x9, 10000, 0, 71120, 90)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8F")

    label("loc_A35")

    SetChrPos(0x9, 21000, 0, 69900, 357)
    OP_8E(0xFE, 0x5208, 0x0, 0x12322, 0x7D0, 0x0)
    OP_8E(0xFE, 0x506E, 0x0, 0x1262E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4DD0, 0x0, 0x128E0, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8F")

    label("loc_A8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEB")
    OP_8E(0xFE, 0x84D0, 0x0, 0x12124, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8070, 0x0, 0x1264C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7CBA, 0x0, 0x128E0, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3E")
    OP_8E(0xFE, 0x2D82, 0x0, 0x128E0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2940, 0x0, 0x1266A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2710, 0x0, 0x12214, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B91")
    OP_8E(0xFE, 0x2710, 0x0, 0xF352, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2AA8, 0x0, 0xF064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2F62, 0x0, 0xEC54, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE4")
    OP_8E(0xFE, 0x803E, 0x0, 0xEC54, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8444, 0x0, 0xEFF6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x84D0, 0x0, 0xF488, 0x7D0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BE4")

    Jump("loc_A8F")

    label("loc_BE7")

    Return()

    # Function_3_9D8 end

    def Function_4_BE8(): pass

    label("Function_4_BE8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0B")
    OP_8D(0xFE, 17690, 58310, 20560, 61470, 1000)
    Jump("Function_4_BE8")

    label("loc_C0B")

    Return()

    # Function_4_BE8 end

    def Function_5_C0C(): pass

    label("Function_5_C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C2F")
    OP_8D(0xFE, 40220, 54770, 45110, 57860, 1000)
    Jump("Function_5_C0C")

    label("loc_C2F")

    Return()

    # Function_5_C0C end

    def Function_6_C30(): pass

    label("Function_6_C30")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_C3D")
    OP_A2(0x9)

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在前作中与王相识】\x01",      # 0
            "【◇在前作中不认识王】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CA7"),
        (1, "loc_CAD"),
        (SWITCH_DEFAULT, "loc_CB3"),
    )


    label("loc_CA7")

    OP_A2(0x9)
    Jump("loc_CB3")

    label("loc_CAD")

    OP_A3(0x9)
    Jump("loc_CB3")

    label("loc_CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED5")

    ChrTalk(    #0
        0xFE,
        "呼，来了吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_END)), "loc_D1D")

    ChrTalk(    #1
        0x101,
        (
            "#1011F啊，这不是王吗！\x02\x03",

            "你怎么会在这里？\x01",
            "到底怎么了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3F")

    label("loc_D1D")


    ChrTalk(    #2
        0x101,
        (
            "#1015F？？？\x02\x03",

            "到底怎么了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3F")

    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        (
            "啊啊，护卫的搬运车\x01",
            "忽然停住不动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "真让人头疼啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        (
            "#1019F嗯、嗯……\x02\x03",

            "却偏偏\x01",
            "在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1048F这样的话就会\x01",
            "严重妨碍通行了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E28")

    ChrTalk(    #7
        0x107,
        "#561F……真是的啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_E28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E50")

    ChrTalk(    #8
        0x106,
        "#551F……真的呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7B")

    label("loc_E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(    #9
        0x103,
        "#025F……哎呀呀，是呢。\x02",
    )

    CloseMessageWindow()

    label("loc_E7B")


    ChrTalk(    #10
        0xFE,
        "确、确实啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "呼，虽然很麻烦，\x01",
            "但不想办法把它挪走的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0xA)
    OP_A2(0x20CA)
    Jump("loc_F8F")

    label("loc_ED5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_END)), "loc_F31")

    ChrTalk(    #12
        0xFE,
        (
            "搬运车竟然在\x01",
            "这种地方不动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "虽然很麻烦，\x01",
            "但不想办法把它挪走的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8F")

    label("loc_F31")


    ChrTalk(    #14
        0xFE,
        (
            "护卫的搬运车\x01",
            "竟然停在这种地方不动了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "呼，虽然很麻烦，\x01",
            "但不想办法把它挪走的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8F")

    Jump("loc_16DF")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_10EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1031")

    ChrTalk(    #16
        0xFE,
        (
            "等修好之后\x01",
            "还要继续进行护卫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "导力器的输出工作\x01",
            "还是和以前一样顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "已经快忙不过来了，\x01",
            "布鲁诺偏偏还不在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EC")

    label("loc_1031")


    ChrTalk(    #19
        0xFE,
        (
            "等修好之后\x01",
            "还要继续进行护卫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "最近出现了很多危险的魔兽，\x01",
            "这种工作也变得很麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "那么…在出发之前\x01",
            "先去『福格尔酒馆』吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "做往返护卫的任务\x01",
            "真是很花时间啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_10EC")

    Jump("loc_115C")

    label("loc_10EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_115C")

    ChrTalk(    #23
        0xFE,
        (
            "可能的话，我也想\x01",
            "自己挑选工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "以后你们要是接到什么重要调查的话\x01",
            "也分配一些简单任务给我吧，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115C")

    Jump("loc_11A1")

    label("loc_115F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #25
        0xFE,
        (
            "不好意思，\x01",
            "很想帮到你们一些忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "大家一起加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_11A1")

    Jump("loc_16DF")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1363")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B0")

    ChrTalk(    #27
        0xFE,
        "呀，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "还记得我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1001F当然记得啦！\x02\x03",

            "你不是蔡斯支部\x01",
            "的王吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "哈哈，谢谢，竟然还记得我。\x01",
            "能再次相遇真是高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "你终于顺利晋升为\x01",
            "正游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "恭喜！\x01",
            "凭你的实力，这也是理所当然的结果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1360")

    label("loc_12B0")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #33
        0xFE,
        "啊，这不是艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1004F咦……？\x02\x03",

            "#1018F啊，我还说是谁，\x01",
            "这不是王吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "你终于顺利晋升为\x01",
            "正游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "恭喜！\x01",
            "凭你的实力，这也是理所当然的结果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1360")

    Jump("loc_14AB")

    label("loc_1363")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #37
        0xFE,
        "…………哎呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "你不就是…\x01",
            "最近才转正的艾丝蒂尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1004F哎哎，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "啊，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "我是王。\x01",
            "蔡斯地区的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1000F啊～是吗。\x02\x03",

            "我是艾丝蒂尔·布莱特。\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "啊啊，请多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "你们的事情\x01",
            "我也早有耳闻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "真是立了大功啊，\x01",
            "升为正游击士也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14AB")


    ChrTalk(    #46
        0x101,
        (
            "#1008F嘿嘿，谢谢夸奖。\x02\x03",

            "我们也还差得远呢，\x01",
            "还需要不断努力进步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "嗯…保持上进心，永不懈怠吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "这种谦虚的态度\x01",
            "我也要多多学习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "对了，冈多夫\x01",
            "出去办事了，你们知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "从嘉恩那里听说了。\x02\x03",

            "我们就是为了增援\x01",
            "才特意来蔡斯的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "是这样吗。\x01",
            "谢啦，真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "真是不好意思，\x01",
            "很想帮到你们一些忙。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_165B")
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #53
        0xFE,
        (
            "阿加特前辈也是，\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x106,
        "#051F哪里，也请你们多关照了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A2")

    label("loc_165B")

    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #55
        0xFE,
        (
            "雪拉扎德也\x01",
            "请多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        "#020F哪里的话，互相关照吧。\x02",
    )

    CloseMessageWindow()

    label("loc_16A2")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #57
        0xFE,
        "我也竭尽全力哟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "那么，大家都加油吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1427)
    OP_A2(0xA)

    label("loc_16DF")

    TalkEnd(0x12)
    Return()

    # Function_6_C30 end

    def Function_7_16E3(): pass

    label("Function_7_16E3")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1733")

    ChrTalk(    #59
        0xFE,
        (
            "最近我的孙女\x01",
            "也一直频繁出入中央工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "真让人放心不下啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17CB")

    label("loc_1733")


    ChrTalk(    #61
        0xFE,
        (
            "嗯，不过看起来\x01",
            "城里也没有发生太大的事故。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "算啦，这种程度的摇晃\x01",
            "应该还不至于影响到中央工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "因为地震事件，\x01",
            "出现了接连不断的受害事件。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_17CB")

    TalkEnd(0x11)
    Return()

    # Function_7_16E3 end

    def Function_8_17CF(): pass

    label("Function_8_17CF")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1878")

    ChrTalk(    #64
        0xFE,
        (
            "再这样下去的话\x01",
            "整个王国也都会被波及吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "想顺利解决这次危机的话\x01",
            "就只有靠中央工房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "不管怎样，总之希望能尽快\x01",
            "重新开始研究活动啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_18E0")

    label("loc_1878")


    ChrTalk(    #67
        0xFE,
        (
            "虽然拉赛尔博士不在，\x01",
            "但你们也是很优秀能干的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "只要发挥出中央工房的力量\x01",
            "就一定可以解决危机的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E0")

    Jump("loc_19B2")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1945")

    ChrTalk(    #69
        0xFE,
        (
            "我在蔡斯市内\x01",
            "经营武器店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "就是游击士协会对面的那家店，\x01",
            "有机会的话多来光顾吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19B2")

    label("loc_1945")


    ChrTalk(    #71
        0xFE,
        (
            "嗯，好像没有余震了，\x01",
            "店应该不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "不过真奇怪，竟然会有地震。\x01",
            "利贝尔可是很少发生地震的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_19B2")

    TalkEnd(0x10)
    Return()

    # Function_8_17CF end

    def Function_9_19B6(): pass

    label("Function_9_19B6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B57")
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)
    Sleep(400)

    ChrTalk(    #73
        0xFE,
        "啊～提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "好像发生了什么\x01",
            "大事的样子哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x107,
        (
            "#063F嗯……\x01",
            "库诺不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "店里的生意一直很好，\x01",
            "当然不要紧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "倒是提妲你啊…\x01",
            "最近博士很头疼吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x107,
        (
            "#562F嗯、嗯…爷爷他\x01",
            "最近确实一直都很为难，不过……\x02\x03",

            "#562F爷爷越在这种时候就越有干劲，\x01",
            "一定不会放弃的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "嘿嘿～好厉害啊。\x01",
            "真不愧是拉赛尔博士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "中央工房的人\x01",
            "果然就是不一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x20C9)
    Jump("loc_1D42")

    label("loc_1B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BC6")

    ChrTalk(    #81
        0xFE,
        (
            "在这种危机的情况下\x01",
            "仍然还这么泰然自若……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "真不愧是拉赛尔博士啊。\x01",
            "期待他的成果！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D42")

    label("loc_1BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C58")

    ChrTalk(    #83
        0xFE,
        (
            "现在的鱼和水果还都是\x01",
            "很新鲜的货，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "大部分的商品\x01",
            "都是用定期船运来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "要是一直这样的话\x01",
            "这里可就惨了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1CAC")

    label("loc_1C58")


    ChrTalk(    #86
        0xFE,
        (
            "鱼和水果几乎都是用\x01",
            "定期船来运送的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "如果一直这么下去的话\x01",
            "这里可就惨了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAC")

    Jump("loc_1D42")

    label("loc_1CAF")


    ChrTalk(    #88
        0xFE,
        (
            "如果是中央工房的人\x01",
            "应该可以很快找出原因才对啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "但是不知为何，\x01",
            "到现在好像也没有任何头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "现在大家都很困扰，\x01",
            "还要更加努力才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D42")

    Jump("loc_2051")

    label("loc_1D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D6F")

    ChrTalk(    #91
        0xFE,
        (
            "呼，客人\x01",
            "太多了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D73")

    label("loc_1D6F")

    Call(0, 13)

    label("loc_1D73")

    Jump("loc_2051")

    label("loc_1D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1E7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1DD7")

    ChrTalk(    #92
        0xFE,
        (
            "要赶快把水果\x01",
            "摆放好才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "啊啊～～真希望博士\x01",
            "能早点把地震事件平息啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7C")

    label("loc_1DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE6")
    Call(0, 12)
    Jump("loc_1E7C")

    label("loc_1DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E3C")

    ChrTalk(    #94
        0xFE,
        (
            "嗯…堆太高的话\x01",
            "一有地震就不得了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "到时苹果也许会滚得\x01",
            "满街都是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E7C")

    label("loc_1E3C")


    ChrTalk(    #96
        0xFE,
        "已经把水果摆放好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "这样摆放的话\x01",
            "看起来很漂亮啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1E7C")

    Jump("loc_2051")

    label("loc_1E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 2)), scpexpr(EXPR_END)), "loc_1EE6")

    ChrTalk(    #98
        0xFE,
        (
            "那么，要赶快把商品\x01",
            "摆好才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "啊啊～～真希望博士\x01",
            "能早点把地震事件平息啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEA")

    label("loc_1EE6")

    Call(0, 12)

    label("loc_1EEA")

    Jump("loc_2051")

    label("loc_1EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F4C")

    ChrTalk(    #100
        0xFE,
        (
            "终于把商品重新\x01",
            "摆放好了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "但如果再出现\x01",
            "一次地震的话该如何是好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F94")

    label("loc_1F4C")


    ChrTalk(    #102
        0xFE,
        (
            "呼～终于把桔子\x01",
            "摆放好了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "呼呼～这下就和原来一样完美了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1F94")

    Jump("loc_2051")

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FFA")

    ChrTalk(    #104
        0xFE,
        (
            "必须要赶快把\x01",
            "商品重新摆好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "这种乱七八糟的丢人样子\x01",
            "可不能给客人看见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2051")

    label("loc_1FFA")


    ChrTalk(    #106
        0xFE,
        (
            "可恶！！花好大力气\x01",
            "才弄好的展柜全都震坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "可恶的地震～\x01",
            "不可原谅啊～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2051")

    TalkEnd(0x8)
    Return()

    # Function_9_19B6 end

    def Function_10_2055(): pass

    label("Function_10_2055")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_219E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2129")

    ChrTalk(    #108
        0xFE,
        (
            "导力灯现在不能用了，\x01",
            "好像每天很早就天黑了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "虽然确实很不方便，不过\x01",
            "从健康角度来考虑的话好像也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "日出时起床，\x01",
            "日落时睡觉，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "我们年轻的时候\x01",
            "就一直是这样的作息时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_219B")

    label("loc_2129")


    ChrTalk(    #112
        0xFE,
        (
            "导力灯现在不能用了，\x01",
            "好像每天很早就天黑了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "虽然确实很不方便，不过\x01",
            "从健康角度来考虑的话好像也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219B")

    Jump("loc_263F")

    label("loc_219E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2226")

    ChrTalk(    #114
        0xFE,
        (
            "连电梯\x01",
            "也不能用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "看来导力工厂也\x01",
            "完全失去机能了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "要是不能制造导力器的话，\x01",
            "蔡斯可怎么办啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2270")

    label("loc_2226")


    ChrTalk(    #117
        0xFE,
        (
            "导力器产业可是\x01",
            "这城市的生命线啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "可是……\x01",
            "竟然发生了这种事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2270")

    Jump("loc_263F")

    label("loc_2273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_22CB")

    ChrTalk(    #119
        0xFE,
        (
            "不知在什么时候\x01",
            "放出了安全宣言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "哎呀，到最后\x01",
            "也是毫无来由的地震啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263F")

    label("loc_22CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_23F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2334")

    ChrTalk(    #121
        0xFE,
        (
            "兰达的孙女\x01",
            "好像也进中央工房了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "这是和完成了新型引擎\x01",
            "同样值得高兴的消息啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F5")

    label("loc_2334")


    ChrTalk(    #123
        0xFE,
        (
            "兰达的孙女\x01",
            "好像也进中央工房了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "这是和完成了新型引擎\x01",
            "同样值得高兴的消息啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "现在的年轻人都\x01",
            "想进入中央工房工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "在当今的时代，\x01",
            "技术力已经变成推动世界发展的最大动力了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_23F5")

    Jump("loc_263F")

    label("loc_23F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2465")

    ChrTalk(    #127
        0xFE,
        (
            "其实在这片大地上\x01",
            "除了导力之外也还有其他的力量呢，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "大自然确实是\x01",
            "非常神秘的存在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2544")

    label("loc_2465")


    ChrTalk(    #129
        0xFE,
        "虽然很多东西并不为人所知……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "其实在这片大地上\x01",
            "但也确实是存在的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "像这次七耀石的矿脉上\x01",
            "流动着力量波纹的现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "虽然在规模上有些不同，\x01",
            "但和结晶回路是一个原理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "嗯，大自然真的是\x01",
            "不可思议的存在啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2544")

    Jump("loc_263F")

    label("loc_2547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_263F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25B4")

    ChrTalk(    #134
        0xFE,
        (
            "嗯，街上的时钟\x01",
            "好像一点也没有慢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "已经是４０年前制造的东西了，\x01",
            "竟然还这么结实。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263F")

    label("loc_25B4")


    ChrTalk(    #136
        0xFE,
        (
            "嗯，街上的时钟\x01",
            "好像一点也没有慢啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "已经是４０年前制造的东西了，\x01",
            "竟然还这么结实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "哈哈哈～简直就像拉赛尔那个老头子一样。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_263F")

    TalkEnd(0x9)
    Return()

    # Function_10_2055 end

    def Function_11_2643(): pass

    label("Function_11_2643")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_26AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26A6")

    ChrTalk(    #139
        0xFE,
        (
            "竟然一眼就看出来了，\x01",
            "果然是职业的啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "呵呵呵，和你商量算是找对人了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_26AA")

    label("loc_26A6")

    Call(0, 13)

    label("loc_26AA")

    Jump("loc_2930")

    label("loc_26AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2718")

    ChrTalk(    #141
        0xFE,
        (
            "也买过最右边的，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "买来的苹果\x01",
            "全部都是酸的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "倒霉～为什么会这样呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2796")

    label("loc_2718")


    ChrTalk(    #144
        0xFE,
        (
            "虽然稍微有点经验了，\x01",
            "但还是觉得买食物很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "看起来的话\x01",
            "哪个也都是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "哈，还是决定\x01",
            "听听店员的意见吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2796")

    Jump("loc_2930")

    label("loc_2799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_286B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2802")

    ChrTalk(    #147
        0xFE,
        (
            "爸爸让我来买\x01",
            "『看起来就好吃的』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "可是，『看起来就好吃』\x01",
            "的苹果究竟是哪个呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2868")

    label("loc_2802")


    ChrTalk(    #149
        0xFE,
        (
            "爸爸让我来买东西，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "他只说让我买\x01",
            "『看起来好吃的』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "那种说法\x01",
            "会有谁能懂啊…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2868")

    Jump("loc_2930")

    label("loc_286B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28C8")

    ChrTalk(    #152
        0xFE,
        (
            "想买罐头，\x01",
            "但是现在买不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "说是休整中……\x01",
            "不过到底在休整什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2930")

    label("loc_28C8")


    ChrTalk(    #154
        0xFE,
        (
            "今天本来是来买罐头的，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "说是在休整中，\x01",
            "暂时不能买。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "休整中……\x01",
            "在休整什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2930")

    TalkEnd(0xA)
    Return()

    # Function_11_2643 end

    def Function_12_2934(): pass

    label("Function_12_2934")

    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #157
        0xFE,
        (
            "啊～提妲。\x01",
            "欢迎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "好多人啊，\x01",
            "他们都是博士的助手吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x107,
        (
            "#067F喔～虽然不是，\x01",
            "但也算是帮忙研究工作的。\x02\x03",

            "#560F库诺也在帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "嗯，要赶快把被地震弄乱\x01",
            "的商品重新摆放好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "不知道博士对地震的研究\x01",
            "现在怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "希望他能早点发明出一个\x01",
            "能控制地震的好东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "提妲也要\x01",
            "努力帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x107,
        "#061F嗯！在主日学校再见吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x1432)
    Return()

    # Function_12_2934 end

    def Function_13_2A92(): pass

    label("Function_13_2A92")

    OP_4A(0x8, 255)
    OP_4A(0xA, 255)

    ChrTalk(    #165
        0xA,
        (
            "啊……那个……\x01",
            "抱歉，打扰你工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "这家店里有没有卖\x01",
            "『看起来很好吃』的苹果？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        "看起来好吃的苹果？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "嗯……那就是颜色好看\x01",
            "的苹果了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)

    ChrTalk(    #169
        0x8,
        (
            "……那个如何？\x01",
            "看起来应该很好吃的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "哇，厉害。\x01",
            "一眼就能看出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        "啊啊！专业的果然就是不一样。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)

    ChrTalk(    #172
        0x8,
        (
            "不、不是什么\x01",
            "值得佩服的大事吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "只不过是代选了\x01",
            "一下而已啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0xA, 255)
    OP_A2(0x0)
    OP_A2(0x2)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    Return()

    # Function_13_2A92 end

    def Function_14_2C12(): pass

    label("Function_14_2C12")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2CFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC1")

    ChrTalk(    #174
        0xFE,
        (
            "叫大家帮忙一起把搬运车\x01",
            "推到路边自然最好，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "正如我预想的一样，\x01",
            "车子并没有任何异常状况啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "真是没办法。\x01",
            "车上的东西还要急着运送……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2CF8")

    label("loc_2CC1")


    ChrTalk(    #177
        0xFE,
        "真伤脑筋……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "可不管怎么检查\x01",
            "也发现不了问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF8")

    Jump("loc_2F90")

    label("loc_2CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4B")

    ChrTalk(    #179
        0xFE,
        (
            "接下来我也要\x01",
            "检查搬运车了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "……好不容易等到了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2D7A")

    label("loc_2D4B")


    ChrTalk(    #181
        0xFE,
        (
            "接下来轮到我的搬运车了。\x01",
            "终于轮到我了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7A")

    Jump("loc_2F90")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2DD1")

    ChrTalk(    #182
        0xFE,
        "呼～下一站是王都了么，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "看来这次又要委托王\x01",
            "进行护卫了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E30")

    label("loc_2DD1")


    ChrTalk(    #184
        0xFE,
        (
            "已经不会再有地震了，\x01",
            "玛多克工房长亲口说过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "这样下去的话\x01",
            "简直就是大自然的惩罚啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2E30")

    Jump("loc_2F90")

    label("loc_2E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E7D")

    ChrTalk(    #186
        0xFE,
        (
            "没时间因为地震之类的\x01",
            "东西惊叹了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "赶快工作吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EBF")

    label("loc_2E7D")


    ChrTalk(    #188
        0xFE,
        "呼～还是这么忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "蔡斯的导力器\x01",
            "还是和以前一样受好评。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2EBF")

    Jump("loc_2F90")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F18")

    ChrTalk(    #190
        0xFE,
        (
            "呼～没有太大的受害情况\x01",
            "就算是万幸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "喔，还是赶快工作吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2F18")


    ChrTalk(    #192
        0xFE,
        (
            "虽然有些摇晃，\x01",
            "不过现在已经停止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "之前去沃尔费堡垒的时候\x01",
            "也遇到小地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "震动比最近的地震\x01",
            "还要小。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2F90")

    TalkEnd(0xB)
    Return()

    # Function_14_2C12 end

    def Function_15_2F94(): pass

    label("Function_15_2F94")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3081")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2FF7")

    ChrTalk(    #195
        0xFE,
        (
            "中央工房好像已经做了发表，\x01",
            "说今后不会再有地震了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "总算是松了口气啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_2FF7")


    ChrTalk(    #197
        0xFE,
        (
            "虽然听老公说过了，\x01",
            "但真的不会再发生了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "本来为了保护花坛\x01",
            "还特意想了很多防震对策呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "呼，不管怎么说，总算松了口气。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_307E")

    Jump("loc_315E")

    label("loc_3081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_315E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_30EA")

    ChrTalk(    #200
        0xFE,
        (
            "这是个难得的机会，\x01",
            "正想改变花坛的放置位置呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "嗯，那好。\x01",
            "一会儿就去看看花吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_315E")

    label("loc_30EA")


    ChrTalk(    #202
        0xFE,
        (
            "呼，还好。\x01",
            "花坛总算没事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "地震也许还会再来，\x01",
            "不能让它们被震倒啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "嗯……不过\x01",
            "该怎么摆放才好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_315E")

    TalkEnd(0xC)
    Return()

    # Function_15_2F94 end

    def Function_16_3162(): pass

    label("Function_16_3162")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BC")

    ChrTalk(    #205
        0xFE,
        (
            "现在发生的这些\x01",
            "好像是导力停止现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "不过，究竟是什么原因\x01",
            "引发了这种现象呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_327F")
    TurnDirection(0xD, 0x107, 400)

    ChrTalk(    #207
        0xFE,
        (
            "……提妲。\x01",
            "博士需要什么指示吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x107,
        (
            "#064F哎……！？\x02\x03",

            "#067F嗯、嗯……\x01",
            "好像还在苦恼中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "那么说的话，\x01",
            "这种状况还要持续一阵了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B6")

    label("loc_327F")


    ChrTalk(    #211
        0xFE,
        (
            "如果不能找到原因，\x01",
            "想解决这次的事情可就很困难了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B6")

    OP_A2(0x5)
    Jump("loc_3300")

    label("loc_32BC")


    ChrTalk(    #212
        0xFE,
        (
            "我想这次的现象\x01",
            "正是导力停止现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "不过规模实在\x01",
            "也太大了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3300")

    Jump("loc_347B")

    label("loc_3303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_33D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_336C")

    ChrTalk(    #214
        0xFE,
        (
            "看来今后也要做好\x01",
            "地震的预防工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "以前我们对这种事\x01",
            "根本就没有任何预防措施。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33CD")

    label("loc_336C")


    ChrTalk(    #216
        0xFE,
        (
            "玛多克工房长已经\x01",
            "发出安全宣言了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "不管怎样，地震没造成\x01",
            "人员伤亡就是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_33CD")

    Jump("loc_347B")

    label("loc_33D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_347B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_343B")

    ChrTalk(    #218
        0xFE,
        (
            "控制大地震动…\x01",
            "真是可怕的能源啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "用中央工房的『卡佩尔』\x01",
            "说不定可以计算出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_347B")

    label("loc_343B")


    ChrTalk(    #220
        0xFE,
        "那就是地震吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "我还是第一次体验到，\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_347B")

    TalkEnd(0xD)
    Return()

    # Function_16_3162 end

    def Function_17_347F(): pass

    label("Function_17_347F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #222
        (
            "\x07\x05『导力式时钟第１号机』\x01",
            "　七耀日历１１６２年·蔡斯技术工房制造\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_17_347F end

    def Function_18_34E7(): pass

    label("Function_18_34E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350F")
    OP_28(0x6C, 0x1, 0x4)
    Call(1, 0)
    TalkEnd(0xFF)

    label("loc_350F")

    Return()

    # Function_18_34E7 end

    def Function_19_3510(): pass

    label("Function_19_3510")

    OP_28(0x6C, 0x1, 0x10)
    Call(1, 1)
    OP_64(0x1, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_19_3510 end

    def Function_20_3522(): pass

    label("Function_20_3522")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_36E5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3593")

    ChrTalk(    #223
        0x101,
        (
            "#1007F嗯～纹章的部分没有了，\x01",
            "情况果然很糟糕呢。\x02\x03",

            "#1002F不早点把招牌板找回来的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E2")

    label("loc_3593")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(28590, 0, 63210, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 28590, 0, 63210, 81)
    SetChrPos(0xF7, 28200, 0, 62550, 90)
    SetChrPos(0xF8, 27430, 0, 63190, 90)
    SetChrPos(0xF9, 27170, 0, 62250, 90)
    OP_0D()

    ChrTalk(    #224
        0x101,
        "#1002F#1P啊，这就是那个招牌板了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3695")

    ChrTalk(    #225
        0x106,
        (
            "#052F#1P可是…\x01",
            "究竟是怎么盗走的呢。\x02\x03",

            "#551F真是个不得了的家伙呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_3695")


    ChrTalk(    #226
        0x103,
        (
            "#025F#1P看来纹章部分\x01",
            "已经被人盗走了呢。\x02\x03",

            "那家伙的手段真是厉害。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DA")

    OP_28(0x6C, 0x1, 0x1000)
    EventEnd(0x0)

    label("loc_36E2")

    Jump("loc_3A02")

    label("loc_36E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3753")

    ChrTalk(    #227
        0x101,
        (
            "#1015F嗯……\x01",
            "要怎么做好呢。\x02\x03",

            "如果手上没什么别的事的话，\x01",
            "不如去问问雾香小姐吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AF")

    label("loc_3753")


    ChrTalk(    #228
        0x101,
        (
            "#1015F竟然连协会都会\x01",
            "遇到这种事件吗。\x02\x03",

            "要是手上没其他事的话，\x01",
            "还是去确认一下这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AF")

    Jump("loc_3A02")

    label("loc_37B2")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(28590, 0, 63210, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 28590, 0, 63210, 81)
    SetChrPos(0xF7, 28200, 0, 62550, 90)
    SetChrPos(0xF8, 27430, 0, 63190, 90)
    SetChrPos(0xF9, 27170, 0, 62250, 90)
    OP_0D()

    ChrTalk(    #229
        0x101,
        (
            "#1004F啊？\x02\x03",

            "这里的招牌板……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3933")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_38BC")

    ChrTalk(    #230
        0x106,
        (
            "#053F是啊，招牌板\x01",
            "竟然变成这个样子了。\x02\x03",

            "#050F稍后去和雾香确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3918")

    label("loc_38BC")


    ChrTalk(    #231
        0x103,
        (
            "#022F说起来的话，招牌板\x01",
            "居然变成这样了啊。\x02\x03",

            "#020F如果在意的话，\x01",
            "稍后去问问雾香小姐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3918")


    ChrTalk(    #232
        0x101,
        "#1015F嗯……了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39FA")

    label("loc_3933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_396C")

    ChrTalk(    #233
        0x106,
        (
            "#555F这是怎么回事？\x02\x03",

            "中间部分被挖去了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_396C")


    ChrTalk(    #234
        0x103,
        (
            "#023F什么啊！？这个。\x01",
            "中心部分竟然被挖掉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399E")


    ChrTalk(    #235
        0x101,
        (
            "#1015F嗯…也许协会里\x01",
            "发生什么事了吧。\x02\x03",

            "要是手上没其他事的话，\x01",
            "还是去确认一下这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FA")

    OP_28(0x6C, 0x1, 0x1000)
    EventEnd(0x0)

    label("loc_3A02")

    TalkEnd(0xFF)
    Return()

    # Function_20_3522 end

    def Function_21_3A06(): pass

    label("Function_21_3A06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A93")

    ChrTalk(    #236
        0xFE,
        (
            "嗯，这个也没有\x01",
            "发现任何异常啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "无法运转\x01",
            "是因为导力停止现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "虽然有点对不起布鲁诺，\x01",
            "但也只有放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_3AD9")

    label("loc_3A93")


    ChrTalk(    #239
        0xFE,
        (
            "无法运转\x01",
            "是因为导力停止现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "抱歉啊，这个\x01",
            "但也只有放弃了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD9")

    Jump("loc_3BBC")

    label("loc_3ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3BBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B76")

    ChrTalk(    #241
        0xFE,
        (
            "已经检查过了，\x01",
            "但根本不是故障原因。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "似乎和以前那次导力停止现象\x01",
            "是同样性质的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "还有浮在湖上的岛…\x01",
            "究竟发生什么了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_3BBC")

    label("loc_3B76")


    ChrTalk(    #244
        0xFE,
        (
            "自动扶梯\x01",
            "没有任何故障，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "这就是和上次一样的\x01",
            "导力停止现象啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BBC")

    TalkEnd(0xFE)
    Return()

    # Function_21_3A06 end

    def Function_22_3BC0(): pass

    label("Function_22_3BC0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BD3")
    Call(0, 30)

    label("loc_3BD3")

    OP_31(0x7, 0x0, 0x36)
    OP_31(0x7, 0xFE, 0x0)
    OP_41(0x7, 0x0, 0xFF)
    OP_41(0x7, 0xDA, 0xFF)
    OP_41(0x7, 0x100, 0xFF)
    OP_41(0x7, 0x121, 0xFF)
    OP_41(0x7, 0x263, 0x0)
    OP_41(0x7, 0x258, 0x1)
    OP_41(0x7, 0x2C8, 0x2)
    OP_41(0x7, 0x281, 0x5)
    OP_41(0x7, 0x272, 0x6)
    OP_35(0x7, 0x0)
    OP_BB(0x7, 0x6, 0x10A)
    OP_6D(25720, 0, 5470, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(0, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #246
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3D27")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_3D3C")

    label("loc_3D27")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_3D3C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrPos(0x101, 27020, 0, 65640, 180)
    SetChrPos(0xF7, 27020, 0, 65640, 180)
    SetChrPos(0xF8, 27020, 0, 65640, 180)
    SetChrPos(0xF9, 27020, 0, 65640, 180)
    OP_4A(0x9, 255)
    OP_6D(27420, 0, 61770, 0)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x1D)
    OP_73(0xC)
    OP_43(0x101, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x19)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x1A)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #247
        0x101,
        (
            "#1011F#6P那么……\x01",
            "接下来要去王都格兰赛尔了。\x02\x03",

            "准备完毕后\x01",
            "就马上去飞船坪吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3ED5")

    ChrTalk(    #248
        0x106,
        (
            "#051F#5P既然是军队的直接委托，\x01",
            "我们最好尽快过去。\x02\x03",

            "不过，要是还有委托没完成的话，\x01",
            "先解决之后再去也可以。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F45")

    label("loc_3ED5")


    ChrTalk(    #249
        0x103,
        (
            "#020F#5P既然是军队的委托，\x01",
            "我们还是尽快过去比较好。\x02\x03",

            "不过，要是还有委托没完成的话，\x01",
            "先解决掉再去也来得及。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F45")


    ChrTalk(    #250
        0x101,
        "#1006F#6P嗯，明白。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_22_3BC0 end

    def Function_23_3F65(): pass

    label("Function_23_3F65")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x698C, 0x0, 0xEA74, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_3F65 end

    def Function_24_3F86(): pass

    label("Function_24_3F86")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x69AA, 0x0, 0xF690, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6CFC, 0x0, 0xEE48, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_24_3F86 end

    def Function_25_3FBB(): pass

    label("Function_25_3FBB")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x69AA, 0x0, 0xF690, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6630, 0x0, 0xEE48, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_25_3FBB end

    def Function_26_3FF0(): pass

    label("Function_26_3FF0")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x698C, 0x0, 0xF7E4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_6F(0xC, 29)
    OP_70(0xC, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xC)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x698C, 0x0, 0xF258, 0x7D0, 0x0)
    Return()

    # Function_26_3FF0 end

    def Function_27_404A(): pass

    label("Function_27_404A")

    OP_72(0x10, 0x20)
    OP_72(0xE, 0x20)

    label("loc_4054")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_407F")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_4054")

    label("loc_407F")

    Return()

    # Function_27_404A end

    def Function_28_4080(): pass

    label("Function_28_4080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40EA")

    ChrTalk(    #251
        0x101,
        (
            "#1000F出城之前还是先去同\x01",
            "提妲和博士打个招呼比较好……\x02\x03",

            "去一趟拉赛尔工房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4182")

    label("loc_40EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4138")

    ChrTalk(    #252
        0x106,
        (
            "#050F出城之前还是先去通知\x01",
            "提妲和老爷爷一声吧？\x02\x03",

            "赶快去工房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4182")

    label("loc_4138")


    ChrTalk(    #253
        0x103,
        (
            "#020F出城之前最好先去同\x01",
            "提妲还有博士打个招呼，\x02\x03",

            "这就去博士的工房吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4182")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_419D")

    Return()

    # Function_28_4080 end

    def Function_29_419E(): pass

    label("Function_29_419E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42BB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4208")

    ChrTalk(    #254
        0x101,
        (
            "#1000F出城之前还是先去同\x01",
            "提妲和博士打个招呼比较好……\x02\x03",

            "去一趟拉赛尔工房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A0")

    label("loc_4208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4256")

    ChrTalk(    #255
        0x106,
        (
            "#050F出城之前还是先去通知\x01",
            "提妲和老爷爷一声吧？\x02\x03",

            "赶快去工房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A0")

    label("loc_4256")


    ChrTalk(    #256
        0x103,
        (
            "#020F出城之前最好先去同\x01",
            "提妲还有博士打个招呼，\x02\x03",

            "这就去博士的工房吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A0")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_42BB")

    Return()

    # Function_29_419E end

    def Function_30_42BC(): pass

    label("Function_30_42BC")

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
        (0, "loc_4336"),
        (1, "loc_433C"),
        (SWITCH_DEFAULT, "loc_4342"),
    )


    label("loc_4336")

    OP_A2(0x1200)
    Jump("loc_4342")

    label("loc_433C")

    OP_A2(0x1201)
    Jump("loc_4342")

    label("loc_4342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4350")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4354")

    label("loc_4350")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4354")

    Return()

    # Function_30_42BC end

    def Function_31_4355(): pass

    label("Function_31_4355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4583")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_43B2")

    ChrTalk(    #257
        0x101,
        (
            "#1000F提妲和博士\x01",
            "应该在拉赛尔工房里，\x02\x03",

            "赶快过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44D2")

    label("loc_43B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4442")

    ChrTalk(    #258
        0x101,
        "#1011F……从这里上去就是中央工房了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #259
        0x103,
        (
            "#020F先去拉赛尔工房\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #260
        0x101,
        "#1000F嗯，拉赛尔工房应该在城的西南角。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44CF")

    label("loc_4442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_44CF")

    ChrTalk(    #261
        0x101,
        "#1011F……从这里上去就是中央工房了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #262
        0x106,
        (
            "#051F先去拉赛尔工房\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x106, 400)

    ChrTalk(    #263
        0x101,
        "#1000F嗯，拉赛尔工房应该在城的西南角。\x02",
    )

    CloseMessageWindow()

    label("loc_44CF")

    OP_A2(0x6)

    label("loc_44D2")

    Jump("loc_4568")

    label("loc_44D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4522")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #264
        0x103,
        (
            "#020F这边是中央工房的方向哦。\x02\x03",

            "先去拉赛尔工房\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4568")

    label("loc_4522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4568")
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #265
        0x106,
        (
            "#050F那边就是中央工房了。\x02\x03",

            "先去拉赛尔工房\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4568")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4690")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D9")

    ChrTalk(    #266
        0x101,
        (
            "#1000F提妲和博士\x01",
            "应该在拉赛尔工房里，\x02\x03",

            "赶快过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4675")

    label("loc_45D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4623")

    ChrTalk(    #267
        0x103,
        (
            "#020F提妲和博士应该在\x01",
            "拉赛尔工房里，\x02\x03",

            "赶快过去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4675")

    label("loc_4623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4675")
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #268
        0x106,
        (
            "#050F提妲和老爷爷现在应该在\x01",
            "拉赛尔工房，\x02\x03",

            "赶快过去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4675")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4690")

    Return()

    # Function_31_4355 end

    def Function_32_4691(): pass

    label("Function_32_4691")

    SetPlaceName(0x7D)
    Return()

    # Function_32_4691 end

    def Function_33_4695(): pass

    label("Function_33_4695")

    SetPlaceName(0x7F)
    Return()

    # Function_33_4695 end

    def Function_34_4699(): pass

    label("Function_34_4699")

    SetPlaceName(0x82)
    Return()

    # Function_34_4699 end

    def Function_35_469D(): pass

    label("Function_35_469D")

    SetPlaceName(0x7C)
    Return()

    # Function_35_469D end

    def Function_36_46A1(): pass

    label("Function_36_46A1")

    SetPlaceName(0x7A)
    Return()

    # Function_36_46A1 end

    def Function_37_46A5(): pass

    label("Function_37_46A5")

    SetPlaceName(0x7B)
    Return()

    # Function_37_46A5 end

    def Function_38_46A9(): pass

    label("Function_38_46A9")

    SetPlaceName(0x80)
    Return()

    # Function_38_46A9 end

    SaveToFile()

Try(main)
