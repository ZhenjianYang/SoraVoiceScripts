from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Knowles',                              # 9
        'Cosimo',                               # 10
        'Monika',                               # 11
        'Bruno',                                # 12
        'Elise',                                # 13
        'Vince',                                # 14
        'ｴｽｶﾚｰﾀｽﾚｯﾄﾞ',               # 15
        'Kilika',                               # 16
        'Stain',                                # 17
        'Randall',                              # 18
        'Wong',                                 # 19
        'Haulage Vehicle',                      # 20
        'Igor',                                 # 21
        'Zeiss - Factory Block',                # 22
        'Tratt Plains Road',                    # 23
        'Ritter Roadway',                       # 24
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
        "Function_7_1AC5",         # 07, 7
        "Function_8_1C37",         # 08, 8
        "Function_9_1F18",         # 09, 9
        "Function_10_2919",        # 0A, 10
        "Function_11_31C7",        # 0B, 11
        "Function_12_366A",        # 0C, 12
        "Function_13_38CA",        # 0D, 13
        "Function_14_3AED",        # 0E, 14
        "Function_15_4054",        # 0F, 15
        "Function_16_4367",        # 10, 16
        "Function_17_481C",        # 11, 17
        "Function_18_48AA",        # 12, 18
        "Function_19_48D3",        # 13, 19
        "Function_20_48E5",        # 14, 20
        "Function_21_4E77",        # 15, 21
        "Function_22_5172",        # 16, 22
        "Function_23_55D0",        # 17, 23
        "Function_24_55F1",        # 18, 24
        "Function_25_5626",        # 19, 25
        "Function_26_565B",        # 1A, 26
        "Function_27_56BF",        # 1B, 27
        "Function_28_56F5",        # 1C, 28
        "Function_29_5893",        # 1D, 29
        "Function_30_5A31",        # 1E, 30
        "Function_31_5AC9",        # 1F, 31
        "Function_32_5EEC",        # 20, 32
        "Function_33_5EF0",        # 21, 33
        "Function_34_5EF4",        # 22, 34
        "Function_35_5EF8",        # 23, 35
        "Function_36_5EFC",        # 24, 36
        "Function_37_5F00",        # 25, 37
        "Function_38_5F04",        # 26, 38
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Met Wong in previous game\x01",               # 0
            "Did not meet Wong in previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CB6"),
        (1, "loc_CBC"),
        (SWITCH_DEFAULT, "loc_CC2"),
    )


    label("loc_CB6")

    OP_A2(0x9)
    Jump("loc_CC2")

    label("loc_CBC")

    OP_A3(0x9)
    Jump("loc_CC2")

    label("loc_CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_109B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")

    ChrTalk(    #0
        0xFE,
        "*sigh* What a mess...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_END)), "loc_D2A")

    ChrTalk(    #1
        0x101,
        (
            "#1011FOh, it's Wong.\x02\x03",

            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_D2A")


    ChrTalk(    #2
        0x101,
        (
            "#1015FHuh?\x02\x03",

            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D49")

    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        "Well, the vehicle I was escorting broke down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "I'm a bit at a loss for what to do.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        (
            "#1019FUgh...\x02\x03",

            "Of all the places to break down...\x01",
            "It just HAD to be in the middle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1048FIt's definitely going to block the\x01",
            "road like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E89")

    ChrTalk(    #7
        0x107,
        "#561FY-Yeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_ED1")

    label("loc_E89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB2")

    ChrTalk(    #8
        0x106,
        "#551F...Seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_ED1")

    label("loc_EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED1")

    ChrTalk(    #9
        0x103,
        "#025F*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_ED1")


    ChrTalk(    #10
        0xFE,
        "Y-You think so too, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "*sigh* It'll be a pain, but I guess I've\x01",
            "gotta get it to the side of the road...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0xA)
    OP_A2(0x20CA)
    Jump("loc_1098")

    label("loc_F5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_END)), "loc_FF3")

    ChrTalk(    #12
        0xFE,
        (
            "I didn't think the truck would\x01",
            "just stop here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "*sigh* It'll be a pain, but I guess I've\x01",
            "gotta get it to the side of the road...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1098")

    label("loc_FF3")


    ChrTalk(    #14
        0xFE,
        (
            "The vehicle I was escorting broke down\x01",
            "right in the middle of everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "*sigh* It'll be a pain, but I guess I've\x01",
            "gotta get it to the side of the road...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1098")

    Jump("loc_1AC1")

    label("loc_109B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_12EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1179")

    ChrTalk(    #16
        0xFE,
        (
            "In a bit, I'll be escorting another\x01",
            "freight vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Orbment exports are as steady as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I hear Bruno complaining sometimes that\x01",
            "he's so busy he can hardly stand it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E7")

    label("loc_1179")


    ChrTalk(    #19
        0xFE,
        (
            "In a bit, I'll be escorting another\x01",
            "freight vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Lately there've been a lot of dangerous\x01",
            "monsters on the roads, so this kinda job\x01",
            "has gotten pretty stressful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Anyway, before I head off I'm gonna\x01",
            "get something to eat over at the Forgel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "After all, a round trip escort mission\x01",
            "can take a long time, especially the\x01",
            "way things are these days.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_12E7")

    Jump("loc_1359")

    label("loc_12EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1359")

    ChrTalk(    #23
        0xFE,
        "I'm gonna take on as many jobs as I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Leave the grunt work to me if anything\x01",
            "big comes up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1359")

    Jump("loc_13E7")

    label("loc_135C")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #25
        0xFE,
        (
            "Sorry for the trouble, but I hope you'll\x01",
            "help out around here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Let's both work together and\x01",
            "do our best, hey?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E7")

    Jump("loc_1AC1")

    label("loc_13EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_160F")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152D")

    ChrTalk(    #27
        0xFE,
        "Hey, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Do you remember me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1001FOf course!\x02\x03",

            "You're Wong, with the Zeiss branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Haha, thanks. Glad we got to meet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Looks like you managed to get\x01",
            "promoted to a full bracer, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Congrats. With your skills I expected\x01",
            "nothing less.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160C")

    label("loc_152D")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #33
        0xFE,
        "Oh, hey, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1004FHuh...?\x02\x03",

            "#1018FAh, I was wondering who it was.\x01",
            "Hey, Wong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Looks like you managed to get\x01",
            "promoted to a full bracer, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Congrats. With your skills I expected\x01",
            "nothing less.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160C")

    Jump("loc_17A7")

    label("loc_160F")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #37
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "Aren't you Estelle, that recently promoted senior?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1004FUh, yeah, that's me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "Ah, 'scuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "I'm Wong. I'm with the Zeiss branch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1000FAh, I see.\x02\x03",

            "I'm Estelle Bright. Nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Yeah, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "I've heard about your work here and there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "After all the successes you've had, it's\x01",
            "only natural you're a full bracer already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A7")


    ChrTalk(    #46
        0x101,
        (
            "#1008FAhaha, thank you.\x02\x03",

            "But, I'm still in training.\x01",
            "I've got a lot to learn still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Never forget the attitude of a\x01",
            "beginner, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Pretty admirable sentiment.\x01",
            "I hope I can follow your example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Incidentally, did you know Gundolf\x01",
            "is out on a job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1011FAh, yeah, I heard from Jean.\x02\x03",

            "We came to Zeiss in part to help\x01",
            "pitch in while he's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Ah, got'cha. Thanks, that'll be a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Sorry for the trouble, but I hope you'll\x01",
            "help out around here for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_19F9")
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #53
        0xFE,
        (
            "Agate, looking forward to working\x01",
            "with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x106,
        "#051FYeah, same here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A58")

    label("loc_19F9")

    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #55
        0xFE,
        (
            "Scherazard, looking forward to working\x01",
            "with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        "#020FYes, same here.\x02",
    )

    CloseMessageWindow()

    label("loc_1A58")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #57
        0xFE,
        "I'll help out as best I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Well, then, let's all work\x01",
            "together and do our best.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1427)
    OP_A2(0xA)

    label("loc_1AC1")

    TalkEnd(0x12)
    Return()

    # Function_6_C30 end

    def Function_7_1AC5(): pass

    label("Function_7_1AC5")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1B43")

    ChrTalk(    #59
        0xFE,
        (
            "Lately my granddaughter's been going\x01",
            "in and out of the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "Makes me worry a bit, it does.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C33")

    label("loc_1B43")


    ChrTalk(    #61
        0xFE,
        (
            "From the looks of it there's\x01",
            "no real damage to the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Well, I'm sure that small shaker didn't\x01",
            "do much to the central factory, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "The only real damage is people using the\x01",
            "earthquake as an excuse to skip work.\x01",
            "Hmph.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1C33")

    TalkEnd(0x11)
    Return()

    # Function_7_1AC5 end

    def Function_8_1C37(): pass

    label("Function_8_1C37")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D31")

    ChrTalk(    #64
        0xFE,
        (
            "The phenomenon that occurred here before\x01",
            "is now happening nation-wide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I doubt anything can face this crisis save\x01",
            "the minds in the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Anyway, I hope they resume their\x01",
            "research as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1DDA")

    label("loc_1D31")


    ChrTalk(    #67
        0xFE,
        (
            "Russell is absent, but we have\x01",
            "many other capable staff members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "With the full power of the central factory on\x01",
            "the case, I'm sure we can overcome this threat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDA")

    Jump("loc_1F14")

    label("loc_1DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1E70")

    ChrTalk(    #69
        0xFE,
        "I run a weapon shop in Zeiss city boundaries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It's across the street from the Bracer Guild,\x01",
            "so if you have the chance stop by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F14")

    label("loc_1E70")


    ChrTalk(    #71
        0xFE,
        (
            "There don't seem to be any aftershocks,\x01",
            "so I bet my store's okay, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Still, earthquakes, how rare. We certainly\x01",
            "don't get many of those in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1F14")

    TalkEnd(0x10)
    Return()

    # Function_8_1C37 end

    def Function_9_1F18(): pass

    label("Function_9_1F18")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_240F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2143")
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)
    Sleep(400)

    ChrTalk(    #73
        0xFE,
        "Ah, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Seems like things are getting pretty\x01",
            "crazy, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x107,
        "#063FYeah... Are you okay, Knowles?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "My store's goin' okay, so I'm managing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "What about you, Tita? I bet things are\x01",
            "crazy with the professor, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x107,
        (
            "#562FY-Yeah, kinda of, but for Grandpa,\x01",
            "well...\x02\x03",

            "#562FIt's times like these that he can\x01",
            "really go all out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Huh, wow. I guess that's \x01",
            "Russell for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "The ideas of the people in the central factory\x01",
            "are a little bit different than most people.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x20C9)
    Jump("loc_240C")

    label("loc_2143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D7")

    ChrTalk(    #81
        0xFE,
        "To go all out at a time like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "That's Russell for you.\x01",
            "It's exactly what you'd expect from\x01",
            "the pride of Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240C")

    label("loc_21D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_232B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A5")

    ChrTalk(    #83
        0xFE,
        (
            "The fish and fruit I've got for\x01",
            "now is still fresh, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "Almost all shipping was done by airship.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "If this continues forever, what's gonna\x01",
            "happen to the city, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2328")

    label("loc_22A5")


    ChrTalk(    #86
        0xFE,
        (
            "Fish and fruit and stuff is almost\x01",
            "all shipped by airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "If this continues, what's gonna\x01",
            "happen to the city, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2328")

    Jump("loc_240C")

    label("loc_232B")


    ChrTalk(    #88
        0xFE,
        (
            "I thought the people in the central factory\x01",
            "would solve this one pretty quick, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "But, it seems like they haven't\x01",
            "yet found the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Everyone's having a tough time, so\x01",
            "I wish they'd work a little harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240C")

    Jump("loc_2915")

    label("loc_240F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_245C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2455")

    ChrTalk(    #91
        0xFE,
        "Phew! Man, there's lots of different customers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_2455")

    Call(0, 13)

    label("loc_2459")

    Jump("loc_2915")

    label("loc_245C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_24F4")

    ChrTalk(    #92
        0xFE,
        "I'd better hurry up and put all the fruit back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "*sigh* I wish the professor would hurry\x01",
            "up and get rid of these earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2641")

    label("loc_24F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2503")
    Call(0, 12)
    Jump("loc_2641")

    label("loc_2503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25B2")

    ChrTalk(    #94
        0xFE,
        (
            "Hmm, piling stuff up too high will make\x01",
            "a real mess if another earthquake comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I'm sure I'll end up chasing apples\x01",
            "across the street if I'm not careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2641")

    label("loc_25B2")


    ChrTalk(    #96
        0xFE,
        "I'm putting all the fruit back where it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Piling up colorful stuff like this looks really\x01",
            "attractive to prospective customers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2641")

    Jump("loc_2915")

    label("loc_2644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_26ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 2)), scpexpr(EXPR_END)), "loc_26E6")

    ChrTalk(    #98
        0xFE,
        (
            "Now, then, next I need to put\x01",
            "my fruit back where it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "*sigh* I wish the professor would hurry\x01",
            "up and get rid of these earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EA")

    label("loc_26E6")

    Call(0, 12)

    label("loc_26EA")

    Jump("loc_2915")

    label("loc_26ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_27FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_276A")

    ChrTalk(    #100
        0xFE,
        (
            "I finally finished putting my wares\x01",
            "back where they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "But what if another earthquake happens?\x02",
    )

    CloseMessageWindow()
    Jump("loc_27F9")

    label("loc_276A")


    ChrTalk(    #102
        0xFE,
        (
            "Phew! Finally got some stuff back where\x01",
            "it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Ah, everything's back as it should.\x01",
            "Mm-hmm. Looks perfect, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_27F9")

    Jump("loc_2915")

    label("loc_27FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2894")

    ChrTalk(    #104
        0xFE,
        (
            "Anyway, I need to put my goods\x01",
            "back where they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Things are such a mess now that it's\x01",
            "embarrassing for customers to see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2915")

    label("loc_2894")


    ChrTalk(    #106
        0xFE,
        (
            "Awww, crap! My perfect display of\x01",
            "goods is all messed up now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Thanks a LOT, earthquake!\x01",
            "I'm not gonna forget this!!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2915")

    TalkEnd(0x8)
    Return()

    # Function_9_1F18 end

    def Function_10_2919(): pass

    label("Function_10_2919")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3A")

    ChrTalk(    #108
        0xFE,
        (
            "We can't use orbal lights, so night\x01",
            "sure seems to come fast lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "It certainly may be inconvenient,\x01",
            "but it's better for your health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Wake with the rising of the sun,\x01",
            "and rest with the setting of it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "Everyone lived that way when I was young.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2ACB")

    label("loc_2A3A")


    ChrTalk(    #112
        0xFE,
        (
            "We can't use orbal lights, so night\x01",
            "sure seems to come fast lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "It certainly may be inconvenient,\x01",
            "but it's better for your health.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACB")

    Jump("loc_31C3")

    label("loc_2ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B83")

    ChrTalk(    #114
        0xFE,
        "For even the elevators to stop...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I doubt the orbal factory\x01",
            "is working at all, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "If we can't make any orbments,\x01",
            "what will happen to Zeiss?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2BFC")

    label("loc_2B83")


    ChrTalk(    #117
        0xFE,
        (
            "Orbment production is this city's\x01",
            "bread and butter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "And yet no one thought something\x01",
            "like this would happen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFC")

    Jump("loc_31C3")

    label("loc_2BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2C8D")

    ChrTalk(    #119
        0xFE,
        (
            "Apparently there was a safety\x01",
            "notification at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Really, right up until the end those\x01",
            "earthquakes made no sense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D51")

    ChrTalk(    #121
        0xFE,
        (
            "Apparently Randall's grandchild has\x01",
            "joined the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "That's as good a bit of news as when we heard\x01",
            "the new model engine was completed.\x01",
            "He must be very proud.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E88")

    label("loc_2D51")


    ChrTalk(    #123
        0xFE,
        (
            "Apparently Randall's grandchild has\x01",
            "joined the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "That's as good a bit of news as when we heard\x01",
            "the new model engine was completed.\x01",
            "He must be very proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I'd be glad for all the youngsters\x01",
            "to join the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "In the times coming, it'll be technology\x01",
            "that moves the world.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2E88")

    Jump("loc_31C3")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F22")

    ChrTalk(    #127
        0xFE,
        (
            "Actually, even in the earth, there's\x01",
            "power like orbal energy flowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Fascinating, huh?\x01",
            "Nature truly is a mysterious thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3085")

    label("loc_2F22")


    ChrTalk(    #129
        0xFE,
        "It's not exactly common knowledge, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Actually, even in the earth, there's\x01",
            "power like orbal energy flowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "It's a phenomenon caused by power flowing\x01",
            "through veins of septium ore, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "The scale is absolutely different,\x01",
            "but the basic concept is the same\x01",
            "as the quartz in an orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "Nature truly is a mysterious thing.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3085")

    Jump("loc_31C3")

    label("loc_3088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_31C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3118")

    ChrTalk(    #134
        0xFE,
        (
            "It seems the city clock is\x01",
            "still right on point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "It's been forty years since it was built,\x01",
            "too. What a sturdy clock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_3118")


    ChrTalk(    #136
        0xFE,
        (
            "It seems the city clock is\x01",
            "still right on point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "It's been forty years since it was built,\x01",
            "too. What a sturdy clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "Ho ho, almost like Russell himself.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_31C3")

    TalkEnd(0x9)
    Return()

    # Function_10_2919 end

    def Function_11_31C7(): pass

    label("Function_11_31C7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_324C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3245")

    ChrTalk(    #139
        0xFE,
        (
            "To know just at a glance...\x01",
            "He's like a pro or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "Ahaha, I'm glad I asked for his help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3249")

    label("loc_3245")

    Call(0, 13)

    label("loc_3249")

    Jump("loc_3666")

    label("loc_324C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3390")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_32E8")

    ChrTalk(    #141
        0xFE,
        (
            "I decided to buy the item on the\x01",
            "far right, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "All the apples I picked out like\x01",
            "that have been sour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "Hmm, I wonder why.\x02",
    )

    CloseMessageWindow()
    Jump("loc_338D")

    label("loc_32E8")


    ChrTalk(    #144
        0xFE,
        (
            "I've come to accept that I just plain\x01",
            "suck at shopping for food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "It all just looks the same to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "*sigh* Maybe I should just ask the store owner.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_338D")

    Jump("loc_3666")

    label("loc_3390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_341E")

    ChrTalk(    #147
        0xFE,
        (
            "My father told me to go buy\x01",
            "'what looks delicious.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "*sigh* I wonder which apples are\x01",
            "supposed to 'look delicious.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_350E")

    label("loc_341E")


    ChrTalk(    #149
        0xFE,
        (
            "I came shopping at my father's request,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "All my father said was to go buy\x01",
            "'what looks delicious.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "Don't you think that's a ridiculous order?\x01",
            "How the heck am I supposed to know\x01",
            "which is the good stuff and what's not?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_350E")

    Jump("loc_3666")

    label("loc_3511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_3666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_35B3")

    ChrTalk(    #152
        0xFE,
        (
            "I'd like to look at the canned goods,\x01",
            "but the shop owner won't show me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "He said he's adjusting them.\x01",
            "What the heck is there to adjust?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3666")

    label("loc_35B3")


    ChrTalk(    #154
        0xFE,
        (
            "I came to buy some canned goods,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Apparently they're being 'adjusted,'\x01",
            "and I can't look at them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "What the heck is there to 'adjust'\x01",
            "about canned goods...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3666")

    TalkEnd(0xA)
    Return()

    # Function_11_31C7 end

    def Function_12_366A(): pass

    label("Function_12_366A")

    TurnDirection(0x8, 0x107, 0)

    ChrTalk(    #157
        0xFE,
        "Ah, hey, Tita. Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Seems you've got a bunch of people with you.\x01",
            "Are they the professor's assistants, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x107,
        (
            "#067FN-No, not exactly, but they are\x01",
            "helping with some research.\x02\x03",

            "#560FAre you helping out, Knowles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Yeah, just finished picking up some stuff\x01",
            "that got knocked over by the earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "But, if the professor's researching 'em,\x01",
            "then I'm sure these earthquakes'll be\x01",
            "solved no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Hope you got a new invention up your\x01",
            "sleeves to deal with these earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "Wishin' you luck with it, Tita! See you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x107,
        "#061FYeah, see you at Sunday School.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x1432)
    Return()

    # Function_12_366A end

    def Function_13_38CA(): pass

    label("Function_13_38CA")

    OP_4A(0x8, 255)
    OP_4A(0xA, 255)

    ChrTalk(    #165
        0xA,
        (
            "Uh, um... I'm sorry to bother\x01",
            "you while you're working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "Do you, um, have any 'delicious-looking'\x01",
            "apples here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        "Delicious-looking apples?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "So, like, ones with good color and shine,\x01",
            "you mean?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)

    ChrTalk(    #169
        0x8,
        (
            "...How about that one?\x01",
            "I'd say it looks pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "Wooow, incredible.\x01",
            "You can tell just by looking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "Man, pros like you are on a different\x01",
            "level or something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)

    ChrTalk(    #172
        0x8,
        (
            "I-I don't think there's any\x01",
            "reason to be so impressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "I just kind of picked one that seemed\x01",
            "okay, is all.\x02",
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

    # Function_13_38CA end

    def Function_14_3AED(): pass

    label("Function_14_3AED")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BD0")

    ChrTalk(    #174
        0xFE,
        (
            "It's great that we all managed to get the\x01",
            "freight vehicle to the side of the road, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "Like I thought, there's nothin' wrong with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "What a pain. I've got deliveries to do now,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3C2D")

    label("loc_3BD0")


    ChrTalk(    #177
        0xFE,
        "What a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "It's been looked over, but there's\x01",
            "nothin' obviously wrong with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2D")

    Jump("loc_4050")

    label("loc_3C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9C")

    ChrTalk(    #179
        0xFE,
        (
            "The agreement is he's gonna check\x01",
            "my freight vehicle next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "...Don't butt in.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3CD6")

    label("loc_3C9C")


    ChrTalk(    #181
        0xFE,
        (
            "Next up is my freight vehicle's turn.\x01",
            "Don't butt in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD6")

    Jump("loc_4050")

    label("loc_3CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3D4E")

    ChrTalk(    #182
        0xFE,
        (
            "*pheeew*\x01",
            "Next delivery's to the capital, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "Guess I gotta ask Wong for an escort AGAIN.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DE4")

    label("loc_3D4E")


    ChrTalk(    #184
        0xFE,
        (
            "Chief Murdock said there ain't\x01",
            "gonna be no more earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Apparently whatever's been goin' on\x01",
            "is just a natural rhythm. Or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3DE4")

    Jump("loc_4050")

    label("loc_3DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3E74")

    ChrTalk(    #186
        0xFE,
        (
            "Really, I ain't got time to sit and think about\x01",
            "earthquakes no matter how rare they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "All right, back to work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3ED6")

    label("loc_3E74")


    ChrTalk(    #188
        0xFE,
        "Man, oh, man, am I BUSY.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "As always, people're willin' to\x01",
            "fight over Zeiss' orbments.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3ED6")

    Jump("loc_4050")

    label("loc_3ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_4050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3F52")

    ChrTalk(    #190
        0xFE,
        (
            "Well, there wasn't any real damage,\x01",
            "so thankfully everything's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "All right, back to work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4050")

    label("loc_3F52")


    ChrTalk(    #192
        0xFE,
        (
            "It shook a bit, but seems like\x01",
            "it's settled now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "When I went to the Wolf Fort a bit ago\x01",
            "there was a tiny little ol' earthquake.\x01",
            "Didn't do anythin' but jiggle my mid-section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "That one was a smaller earthquake\x01",
            "than this just now, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4050")

    TalkEnd(0xB)
    Return()

    # Function_14_3AED end

    def Function_15_4054(): pass

    label("Function_15_4054")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_41FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_40FE")

    ChrTalk(    #195
        0xFE,
        (
            "The central factory made an\x01",
            "announcement, but it sounds like the\x01",
            "earthquakes are over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "I'm relieved. All that worrying was\x01",
            "pretty draining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FB")

    label("loc_40FE")


    ChrTalk(    #197
        0xFE,
        (
            "I just heard from my husband, but apparently there\x01",
            "aren't going to be any more earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Just as I was planning on safeguarding the\x01",
            "flower beds to prepare for earthquakes,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "I'm relieved. All that worrying was\x01",
            "pretty draining.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_41FB")

    Jump("loc_4363")

    label("loc_41FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_4363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_428C")

    ChrTalk(    #200
        0xFE,
        (
            "Since I have the chance, I'd like\x01",
            "to reposition the flower beds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Yeah, that's good.\x01",
            "Later I'll go see the flowers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4363")

    label("loc_428C")


    ChrTalk(    #202
        0xFE,
        (
            "Phew! All done.\x01",
            "The flower beds are safe now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "There might be another, so I'd like to\x01",
            "set them up so they won't collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "But if I'm going to do that, I might \x01",
            "as well change their position. Hmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4363")

    TalkEnd(0xC)
    Return()

    # Function_15_4054 end

    def Function_16_4367(): pass

    label("Function_16_4367")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_45E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453A")

    ChrTalk(    #205
        0xFE,
        (
            "Apparently all the trouble with the orbments\x01",
            "is because of the Orbal Shutdown Phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "What the heck is causing it, though?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44DC")
    TurnDirection(0xD, 0x107, 400)

    ChrTalk(    #207
        0xFE,
        "Tita, does the professor have any ideas?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x107,
        (
            "#064FHuh...?!\x02\x03",

            "#067FU-Umm... Apparently he's still thinking it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "Well, I guess this is gonna keep up\x01",
            "for a while, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4534")

    label("loc_44DC")


    ChrTalk(    #211
        0xFE,
        (
            "As long as we don't know that, a solution\x01",
            "will be hard to come up with, I imagine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4534")

    OP_A2(0x5)
    Jump("loc_45DD")

    label("loc_453A")


    ChrTalk(    #212
        0xFE,
        (
            "Without a doubt, this problem with the orbments\x01",
            "is because of the Orbal Shutdown Phenomenon,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "Still, the scale of the phenomenon is far too big.\x02",
    )

    CloseMessageWindow()

    label("loc_45DD")

    Jump("loc_4818")

    label("loc_45E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4672")

    ChrTalk(    #214
        0xFE,
        (
            "Perhaps we should consider preparations\x01",
            "for earthquakes in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "Right now we're far too defenseless,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4711")

    label("loc_4672")


    ChrTalk(    #216
        0xFE,
        (
            "Apparently a declaration of safety was\x01",
            "put out under Chief Murdock's name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "Anyway, we're just glad there was no\x01",
            "real damage from the earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4711")

    Jump("loc_4818")

    label("loc_4714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_4818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_47B7")

    ChrTalk(    #218
        0xFE,
        (
            "To move the very earth... That must require\x01",
            "a truly absurd amount of energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "The central factory's Capel might\x01",
            "be able to calculate it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4818")

    label("loc_47B7")


    ChrTalk(    #220
        0xFE,
        "So that was an earthquake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "First time I've ever felt one.\x01",
            "What incredible energy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4818")

    TalkEnd(0xD)
    Return()

    # Function_16_4367 end

    def Function_17_481C(): pass

    label("Function_17_481C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #222
        (
            "\x07\x05[First Orbally-Powered Clock]\x01",
            "Made in year 1162 of the Septian Calendar,\x01",
            "by Zeissian manufacturers.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_17_481C end

    def Function_18_48AA(): pass

    label("Function_18_48AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48D2")
    OP_28(0x6C, 0x1, 0x4)
    Call(1, 0)
    TalkEnd(0xFF)

    label("loc_48D2")

    Return()

    # Function_18_48AA end

    def Function_19_48D3(): pass

    label("Function_19_48D3")

    OP_28(0x6C, 0x1, 0x10)
    Call(1, 1)
    OP_64(0x1, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_19_48D3 end

    def Function_20_48E5(): pass

    label("Function_20_48E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4AFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_496A")

    ChrTalk(    #223
        0x101,
        (
            "#1007FWithout the crest there\x01",
            "it just doesn't feel right.\x02\x03",

            "#1002FWe really need to get our sign back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF7")

    label("loc_496A")

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
        "#1002FAh, so this is where the problem is.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4A88")

    ChrTalk(    #225
        0x106,
        (
            "#052FLooks like he just lifted the damn thing.\x02\x03",

            "#551FBastard thinks he's clever, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEF")

    label("loc_4A88")


    ChrTalk(    #226
        0x103,
        (
            "#025FAmazing. It looks like he just lifted\x01",
            "the crest portion.\x02\x03",

            "Really, what a dexterous person...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEF")

    OP_28(0x6C, 0x1, 0x1000)
    EventEnd(0x0)

    label("loc_4AF7")

    Jump("loc_4E73")

    label("loc_4AFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_4BEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4B6C")

    ChrTalk(    #227
        0x101,
        (
            "#1015FHmm... I wonder what happened.\x02\x03",

            "We should ask Kilika when we've\x01",
            "got some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE7")

    label("loc_4B6C")


    ChrTalk(    #228
        0x101,
        (
            "#1015FI wonder if something happened at the guild.\x02\x03",

            "Maybe we should check the request\x01",
            "board when we've got some time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE7")

    Jump("loc_4E73")

    label("loc_4BEA")

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
            "#1004FHuh?\x02\x03",

            "The sign here...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4D0A")

    ChrTalk(    #230
        0x106,
        (
            "#053FOh, yeah, there was somethin' about the sign.\x02\x03",

            "#050FWe should check with Kilika later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D81")

    label("loc_4D0A")


    ChrTalk(    #231
        0x103,
        (
            "#022FOh, yes, there was something about the sign.\x02\x03",

            "#020FIf you're curious, why don't you\x01",
            "check with Kilika later?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D81")


    ChrTalk(    #232
        0x101,
        "#1015FYeah, will do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E6B")

    label("loc_4D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4DD5")

    ChrTalk(    #233
        0x106,
        (
            "#555FWhat the heck?\x02\x03",

            "The crest is gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E01")

    label("loc_4DD5")


    ChrTalk(    #234
        0x103,
        "#023FWhat on...? The crest is missing.\x02",
    )

    CloseMessageWindow()

    label("loc_4E01")


    ChrTalk(    #235
        0x101,
        (
            "#1015FMaybe something happened at the guild.\x02\x03",

            "If we get some time, we might\x01",
            "want to check the board.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6B")

    OP_28(0x6C, 0x1, 0x1000)
    EventEnd(0x0)

    label("loc_4E73")

    TalkEnd(0xFF)
    Return()

    # Function_20_48E5 end

    def Function_21_4E77(): pass

    label("Function_21_4E77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_4FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F4D")

    ChrTalk(    #236
        0xFE,
        (
            "There doesn't seem to be\x01",
            "anything wrong with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "It's just not working because of the\x01",
            "Orbal Shutdown Phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Hate to say it to Bruno, but he's\x01",
            "just gonna have to give up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4FC8")

    label("loc_4F4D")


    ChrTalk(    #239
        0xFE,
        (
            "It's just not working because of the\x01",
            "Orbal Shutdown Phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "Sorry, but there's nothing we can\x01",
            "do about it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC8")

    Jump("loc_516E")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_516E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F4")

    ChrTalk(    #241
        0xFE,
        (
            "I looked over it just in case,\x01",
            "but this isn't a breakdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "Apparently something like that Orbal Shutdown\x01",
            "Phenomenon thingy that happened before is in\x01",
            "effect here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Orbments stopping in their tracks, islands\x01",
            "floating in the sky... Just what the heck is\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_516E")

    label("loc_50F4")


    ChrTalk(    #244
        0xFE,
        "There's no fault anywhere in the escalator.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "This has gotta be that Orbal Shutdown\x01",
            "Phenomenon thing from before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_516E")

    TalkEnd(0xFE)
    Return()

    # Function_21_4E77 end

    def Function_22_5172(): pass

    label("Function_22_5172")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5185")
    Call(0, 30)

    label("loc_5185")

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
            "\x07\x05Please form your party. You may choose two other\x01",
            "members aside from the mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_52FA")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_530F")

    label("loc_52FA")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_530F")

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
            "#1011FOkay...next stop, Grancel!\x02\x03",

            "We'll head to the dock once\x01",
            "everyone's ready.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_54F8")

    ChrTalk(    #248
        0x106,
        (
            "#051FGiven that it's the military--which,\x01",
            "y'know, means your dad--calling,\x01",
            "we might wanna hurry.\x02\x03",

            "Still, if we got any jobs left\x01",
            "or shopping to do, we can take\x01",
            "care of that, I bet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55B3")

    label("loc_54F8")


    ChrTalk(    #249
        0x103,
        (
            "#020FThis is a request from the military,\x01",
            "so I don't think we should dawdle\x01",
            "too long.\x02\x03",

            "We should have time to finish any\x01",
            "stray jobs, or stray shopping, before\x01",
            "we have to go, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55B3")


    ChrTalk(    #250
        0x101,
        "#1006FOff we go!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_22_5172 end

    def Function_23_55D0(): pass

    label("Function_23_55D0")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x698C, 0x0, 0xEA74, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_23_55D0 end

    def Function_24_55F1(): pass

    label("Function_24_55F1")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x69AA, 0x0, 0xF690, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6CFC, 0x0, 0xEE48, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_24_55F1 end

    def Function_25_5626(): pass

    label("Function_25_5626")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x69AA, 0x0, 0xF690, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6630, 0x0, 0xEE48, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_25_5626 end

    def Function_26_565B(): pass

    label("Function_26_565B")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x698C, 0x0, 0xF7E4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_72(0xC, 0x800)
    OP_6F(0xC, 29)
    OP_70(0xC, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xC)
    OP_71(0xC, 0x800)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x698C, 0x0, 0xF258, 0x7D0, 0x0)
    Return()

    # Function_26_565B end

    def Function_27_56BF(): pass

    label("Function_27_56BF")

    OP_72(0x10, 0x20)
    OP_72(0xE, 0x20)

    label("loc_56C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56F4")
    OP_6F(0x10, 40)
    OP_70(0x10, 0x0)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x28)
    OP_73(0x10)
    Jump("loc_56C9")

    label("loc_56F4")

    Return()

    # Function_27_56BF end

    def Function_28_56F5(): pass

    label("Function_28_56F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5892")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577E")

    ChrTalk(    #251
        0x101,
        (
            "#1000FBefore we leave town, we need to\x01",
            "talk to Tita and the professor...\x02\x03",

            "Let's stop by Russell's factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5877")

    label("loc_577E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5803")

    ChrTalk(    #252
        0x106,
        (
            "#050FWe're gonna say hello to Tita and the\x01",
            "old man before we leave town, right?\x02\x03",

            "Let's get over to Russell's factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5877")

    label("loc_5803")


    ChrTalk(    #253
        0x103,
        (
            "#020FBefore we leave town, weren't we going to\x01",
            "go meet Tita and Russell?\x02\x03",

            "Let's go to the professor's factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5877")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5892")

    Return()

    # Function_28_56F5 end

    def Function_29_5893(): pass

    label("Function_29_5893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A30")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591C")

    ChrTalk(    #254
        0x101,
        (
            "#1000FBefore we leave town, we need to\x01",
            "talk to Tita and the professor...\x02\x03",

            "Let's stop by Russell's factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A15")

    label("loc_591C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_59A1")

    ChrTalk(    #255
        0x106,
        (
            "#050FWe're gonna say hello to Tita and the\x01",
            "old man before we leave town, right?\x02\x03",

            "Let's get over to Russell's factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A15")

    label("loc_59A1")


    ChrTalk(    #256
        0x103,
        (
            "#020FBefore we leave town, weren't we going to\x01",
            "go meet Tita and Russell?\x02\x03",

            "Let's go to the professor's factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A15")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5A30")

    Return()

    # Function_29_5893 end

    def Function_30_5A31(): pass

    label("Function_30_5A31")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5AAA"),
        (1, "loc_5AB0"),
        (SWITCH_DEFAULT, "loc_5AB6"),
    )


    label("loc_5AAA")

    OP_A2(0x1200)
    Jump("loc_5AB6")

    label("loc_5AB0")

    OP_A2(0x1201)
    Jump("loc_5AB6")

    label("loc_5AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5AC4")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5AC8")

    label("loc_5AC4")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5AC8")

    Return()

    # Function_30_5A31 end

    def Function_31_5AC9(): pass

    label("Function_31_5AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DC3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5B3A")

    ChrTalk(    #257
        0x101,
        (
            "#1000FTita and the professor are over\x01",
            "at their house.\x02\x03",

            "Let's get going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB4")

    label("loc_5B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5BF7")

    ChrTalk(    #258
        0x101,
        "#1011FUp this way is the central factory, huh.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #259
        0x103,
        "#020FFirst let's go check in at the professor's place.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #260
        0x101,
        "#1000FYeah, it's in the southwest part of town.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5CB1")

    ChrTalk(    #261
        0x101,
        "#1011FUp this way is the central factory, huh.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #262
        0x106,
        "#051FFirst let's go check in at the professor's place.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x106, 400)

    ChrTalk(    #263
        0x101,
        "#1000FYeah, it's in the southwest part of town.\x02",
    )

    CloseMessageWindow()

    label("loc_5CB1")

    OP_A2(0x6)

    label("loc_5CB4")

    Jump("loc_5DA8")

    label("loc_5CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5D39")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #264
        0x103,
        (
            "#020FGoing this way will take us to the\x01",
            "central factory.\x02\x03",

            "First let's go check in at the professor's place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DA8")

    label("loc_5D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5DA8")
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #265
        0x106,
        (
            "#050FThis way goes to the central factory.\x02\x03",

            "First let's go check in at the old man's place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA8")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EEB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2D")

    ChrTalk(    #266
        0x101,
        (
            "#1000FTita and the professor are over\x01",
            "at their house.\x02\x03",

            "Let's get going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED0")

    label("loc_5E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5E84")

    ChrTalk(    #267
        0x103,
        (
            "#020FTita and Russell should be at home.\x02\x03",

            "Let's go offer our greetings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED0")

    label("loc_5E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5ED0")
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #268
        0x106,
        (
            "#050FTita and the old man are at home.\x02\x03",

            "Let's go say hi.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED0")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5EEB")

    Return()

    # Function_31_5AC9 end

    def Function_32_5EEC(): pass

    label("Function_32_5EEC")

    SetPlaceName(0x7D)
    Return()

    # Function_32_5EEC end

    def Function_33_5EF0(): pass

    label("Function_33_5EF0")

    SetPlaceName(0x7F)
    Return()

    # Function_33_5EF0 end

    def Function_34_5EF4(): pass

    label("Function_34_5EF4")

    SetPlaceName(0x82)
    Return()

    # Function_34_5EF4 end

    def Function_35_5EF8(): pass

    label("Function_35_5EF8")

    SetPlaceName(0x7C)
    Return()

    # Function_35_5EF8 end

    def Function_36_5EFC(): pass

    label("Function_36_5EFC")

    SetPlaceName(0x7A)
    Return()

    # Function_36_5EFC end

    def Function_37_5F00(): pass

    label("Function_37_5F00")

    SetPlaceName(0x7B)
    Return()

    # Function_37_5F00 end

    def Function_38_5F04(): pass

    label("Function_38_5F04")

    SetPlaceName(0x80)
    Return()

    # Function_38_5F04 end

    SaveToFile()

Try(main)
