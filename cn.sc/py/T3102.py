from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '乘客',                                 # 9
        '乘客',                                 # 10
        '女孩子',                               # 11
        '女性客人',                             # 12
        '男孩',                                 # 13
        '乘客',                                 # 14
        '乘客',                                 # 15
        '乘客',                                 # 16
        '受理人吉拉尔',                         # 17
        '巴拉特',                               # 18
        '阿尔丹',                               # 19
        '列曼',                                 # 20
        '鲁特尔',                               # 21
        '诺蒂亚',                               # 22
        '法尔茨',                               # 23
        '雨果',                                 # 24
        '格斯塔夫维修长',                       # 25
        '吉米',                                 # 26
        '赛希莉亚号',                           # 27
        '赛希莉亚号影',                         # 28
        '蔡斯市·工房区',                       # 29
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01140 ._CH',             # 0C
        'ED6_DT07/CH01680 ._CH',             # 0D
        'ED6_DT07/CH02440 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01140P._CP',             # 0C
        'ED6_DT07/CH01680P._CP',             # 0D
        'ED6_DT07/CH02440P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -44890,
        Z                   = -4000,
        Y                   = 146670,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -41630,
        Z                   = 8000,
        Y                   = 123450,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -44830,
        Z                   = -4000,
        Y                   = 141220,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -50230,
        Z                   = 8000,
        Y                   = 121120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -49500,
        Z                   = 8000,
        Y                   = 121470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50910,
        Z                   = 8000,
        Y                   = 121470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -46020,
        Z                   = -4000,
        Y                   = 146670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -39960,
        Z                   = 8000,
        Y                   = 129060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -44890,
        Z                   = -4000,
        Y                   = 140090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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


    DeclActor(
        TriggerX            = -19980,
        TriggerZ            = 8000,
        TriggerY            = 119710,
        TriggerRange        = 400,
        ActorX              = -20110,
        ActorZ              = 9500,
        ActorY              = 121830,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_43E",          # 00, 0
        "Function_1_56E",          # 01, 1
        "Function_2_63A",          # 02, 2
        "Function_3_7B7",          # 03, 3
        "Function_4_7BC",          # 04, 4
        "Function_5_C18",          # 05, 5
        "Function_6_10C8",         # 06, 6
        "Function_7_1490",         # 07, 7
        "Function_8_1546",         # 08, 8
        "Function_9_1801",         # 09, 9
        "Function_10_1887",        # 0A, 10
        "Function_11_18F1",        # 0B, 11
        "Function_12_1A35",        # 0C, 12
        "Function_13_1B0D",        # 0D, 13
        "Function_14_2455",        # 0E, 14
        "Function_15_24A2",        # 0F, 15
        "Function_16_308C",        # 10, 16
        "Function_17_318B",        # 11, 17
        "Function_18_31CF",        # 12, 18
        "Function_19_321C",        # 13, 19
        "Function_20_326E",        # 14, 20
        "Function_21_32C0",        # 15, 21
        "Function_22_3326",        # 16, 22
        "Function_23_338C",        # 17, 23
        "Function_24_33B7",        # 18, 24
        "Function_25_33FD",        # 19, 25
        "Function_26_3443",        # 1A, 26
        "Function_27_3489",        # 1B, 27
        "Function_28_34CF",        # 1C, 28
        "Function_29_3549",        # 1D, 29
        "Function_30_35C3",        # 1E, 30
        "Function_31_363D",        # 1F, 31
        "Function_32_3686",        # 20, 32
        "Function_33_3700",        # 21, 33
        "Function_34_373B",        # 22, 34
        "Function_35_3776",        # 23, 35
        "Function_36_3EC4",        # 24, 36
        "Function_37_45B8",        # 25, 37
        "Function_38_45E6",        # 26, 38
        "Function_39_4614",        # 27, 39
        "Function_40_4656",        # 28, 40
        "Function_41_4698",        # 29, 41
        "Function_42_46DA",        # 2A, 42
        "Function_43_4717",        # 2B, 43
        "Function_44_4EF1",        # 2C, 44
        "Function_45_4F8A",        # 2D, 45
        "Function_46_4FF8",        # 2E, 46
        "Function_47_5051",        # 2F, 47
        "Function_48_50ED",        # 30, 48
    )


    def Function_0_43E(): pass

    label("Function_0_43E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_48E")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, -23200, 8000, 121010, 180)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57460, 4000, 129380, 61)
    OP_8C(0x11, 90, 0)

    label("loc_48E")

    Jump("loc_54A")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    SetChrPos(0x12, -56860, 4000, 129490, 45)
    SetChrPos(0x14, -42830, 8000, 129500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DD")
    ClearChrFlags(0x19, 0x80)

    label("loc_4DD")

    Jump("loc_54A")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_525")
    SetChrPos(0x11, -44890, -4000, 146670, 270)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, -44340, -4000, 151130, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x10)
    Jump("loc_54A")

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_540")
    SetChrPos(0x12, -47490, -4000, 151130, 270)
    Jump("loc_54A")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_54A")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_56D")

    Return()

    # Function_0_43E end

    def Function_1_56E(): pass

    label("Function_1_56E")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x230053)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B4")
    OP_B1("T3102_0")
    OP_6F(0x0, 530)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5B1")
    OP_64(0x0, 0x1)

    label("loc_5B1")

    Jump("loc_639")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E2")
    OP_B1("T3102_1")
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 1001)
    Jump("loc_639")

    label("loc_5E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_60A")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_6F(0x0, 1001)
    Jump("loc_639")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_61D")
    OP_B1("T3102_0")
    Jump("loc_639")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_630")
    OP_B1("T3102_0")
    Jump("loc_639")

    label("loc_630")

    OP_B1("T3102_1")

    label("loc_639")

    Return()

    # Function_1_56E end

    def Function_2_63A(): pass

    label("Function_2_63A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7A1")

    label("loc_65F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7A1")

    label("loc_678")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7A1")

    label("loc_691")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7A1")

    label("loc_6AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7A1")

    label("loc_6C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7A1")

    label("loc_6DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7A1")

    label("loc_6F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7A1")

    label("loc_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7A1")

    label("loc_727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7A1")

    label("loc_740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7A1")

    label("loc_759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7A1")

    label("loc_772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7A1")

    label("loc_78B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7A1")

    label("loc_7B6")

    Return()

    # Function_2_63A end

    def Function_3_7B7(): pass

    label("Function_3_7B7")

    Call(0, 4)
    Return()

    # Function_3_7B7 end

    def Function_4_7BC(): pass

    label("Function_4_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_88E")
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82E")

    ChrTalk(    #0
        0xFE,
        (
            "这里的飞船坪是可动式的，\x01",
            "因此更加危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "说明白一点的话，\x01",
            "其实就是个技术漏洞。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_888")

    label("loc_82E")


    ChrTalk(    #2
        0xFE,
        (
            "这里的飞船坪是可动式的，\x01",
            "因此更加危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "如果是普通的飞船坪，\x01",
            "还可以进行整备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_888")

    TalkEnd(0x10)
    Jump("loc_C17")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_977")
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_925")

    ChrTalk(    #4
        0xFE,
        (
            "导力停止现象的时候\x01",
            "引起了很大骚乱，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "其实根本没有必要\x01",
            "那么吵吵闹闹的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "哈，虽然话是那么说，\x01",
            "但我也一样很惊慌。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_971")

    label("loc_925")


    ChrTalk(    #7
        0xFE,
        (
            "导力停止现象的时候\x01",
            "引起了很大骚乱，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "其实根本没有必要\x01",
            "那么吵闹嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971")

    TalkEnd(0x10)
    Jump("loc_C17")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_992")
    OP_4A(0x10, 255)
    Call(0, 35)
    OP_4B(0x10, 255)
    Jump("loc_C17")

    label("loc_992")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9E8")

    ChrTalk(    #9
        0x10,
        (
            "工事要到雷斯顿要塞\x01",
            "进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "看来果然是关系到\x01",
            "军事机密啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A32")

    label("loc_9E8")


    ChrTalk(    #11
        0x10,
        (
            "『埃尔赛尤』终于\x01",
            "装上了新型的引擎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "工作船现在正在整备中。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A32")

    Jump("loc_C14")

    label("loc_A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AB4")

    ChrTalk(    #13
        0x10,
        (
            "多亏利贝尔通讯的记者\x01",
            "互不侵犯条约的事情终于清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "嗯～不愧是利贝尔通讯，\x01",
            "刊登的文章既详尽又有趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_AB4")


    ChrTalk(    #15
        0x10,
        (
            "最近利贝尔通讯花了很大篇幅\x01",
            "对互不侵犯条约事件进行了报道哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "多亏了杂志上的报道，\x01",
            "我才明白了条约的重要性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        "这次的签字仪式实在是引人关注呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B51")

    Jump("loc_C14")

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BB7")

    ChrTalk(    #18
        0x10,
        (
            "真是的，刚才实在\x01",
            "太危险了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "在危机来临的时候，\x01",
            "人会因恐惧而失去冷静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_BB7")


    ChrTalk(    #20
        0x10,
        "呼～刚才完全慌了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "差一点陷入\x01",
            "混乱之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "呼～不过我还是\x01",
            "很快就镇定下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C14")

    TalkEnd(0x10)

    label("loc_C17")

    Return()

    # Function_4_7BC end

    def Function_5_C18(): pass

    label("Function_5_C18")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_CF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA5")

    ChrTalk(    #23
        0xFE,
        (
            "接下来要检查一下\x01",
            "飞船坪的设施了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "呼～就算检查。\x01",
            "也只是个形式而已吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "不过，至少总比\x01",
            "什么都不做要强。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_CF5")

    label("loc_CA5")


    ChrTalk(    #26
        0xFE,
        (
            "接下来要检查一下\x01",
            "飞船坪的设施了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "呼～就算检查。\x01",
            "也只是个形式而已吧…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF5")

    Jump("loc_10C4")

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAD")

    ChrTalk(    #28
        0xFE,
        (
            "这种现象是在\x01",
            "移动工房船的时候出现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "结果就在拉高到一半时\x01",
            "突然停住不动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "就那样悬在半空，\x01",
            "根本没办法整备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "真是的……\x01",
            "究竟是怎么回事呢，\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_E03")

    label("loc_DAD")


    ChrTalk(    #32
        0xFE,
        (
            "竟然会在移动工房船的时候\x01",
            "出现这种事…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "结果就在拉高到一半时\x01",
            "突然停住不动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E03")

    Jump("loc_10C4")

    label("loc_E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E65")

    ChrTalk(    #34
        0xFE,
        (
            "装载新型引擎的\x01",
            "『埃尔赛尤』啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "啊啊～真想早日瞻仰到\x01",
            "它的雄姿呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA0")

    label("loc_E65")


    ChrTalk(    #36
        0xFE,
        (
            "刚好现在工房船\x01",
            "正要出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "真想赶快过去啊… \x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_EA0")

    Jump("loc_10C4")

    label("loc_EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F08")

    ChrTalk(    #38
        0xFE,
        (
            "新型引擎\x01",
            "终于也进入实装阶段了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "改装工作要加油啊！\x01",
            "我也要继续向女神祈祷！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F48")

    label("loc_F08")


    ChrTalk(    #40
        0xFE,
        "是，已经搬运完毕了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "需要的配件已经\x01",
            "全部准备好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F48")

    Jump("loc_10C4")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_104B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FB2")

    ChrTalk(    #42
        0xFE,
        (
            "那么，接下来就要开始\x01",
            "工房船的出港准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "在维修长回来之前\x01",
            "要全部完成才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1048")

    label("loc_FB2")


    ChrTalk(    #44
        0xFE,
        (
            "那么，马上要进行工房船\x01",
            "的出港准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "为了装配『埃尔赛尤』的引擎，\x01",
            "接下来要去雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "维修长为此也是一大早\x01",
            "就跑去中央工房了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1048")

    Jump("loc_10C4")

    label("loc_104B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_10C4")

    ChrTalk(    #47
        0xFE,
        (
            "地震是我干完工作之后的事情了，\x01",
            "所以物品的检查没出什么乱子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "即使没出现什么问题，\x01",
            "我们也不能松懈精神啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C4")

    TalkEnd(0x11)
    Return()

    # Function_5_C18 end

    def Function_6_10C8(): pass

    label("Function_6_10C8")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_11CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_114C")

    ChrTalk(    #49
        0xFE,
        (
            "那么！拍摄完『赛希莉亚号』\x01",
            "的着陆照片之后就去王都！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "啊啊～『埃尔赛尤』啊……\x01",
            "马上就去，再稍等一会吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C9")

    label("loc_114C")


    ChrTalk(    #51
        0xFE,
        (
            "嗯，工房船的起飞照片\x01",
            "也顺利拍摄到了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "哈～这次的摄影旅行\x01",
            "还真是让人感动又兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "有哭有笑，真是好忙啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_11C9")

    Jump("loc_148C")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_12B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1223")

    ChrTalk(    #54
        0xFE,
        (
            "没想到竟然可以这么近距离地\x01",
            "看到工房船… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "呜呜～活着真好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12B2")

    label("loc_1223")


    ChrTalk(    #56
        0xFE,
        (
            "这就是中央工房所有的\x01",
            "工房船『莱普尼兹号』哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "不但各种设施齐备，\x01",
            "而且还可以进行制品搬运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "它可是有着『飞行的工房』之称号呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_12B2")

    Jump("loc_148C")

    label("loc_12B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12FB")

    ChrTalk(    #59
        0xFE,
        (
            "噢噢～\x01",
            "现在不是感动的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "拍照、拍照～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_137C")

    label("loc_12FB")


    ChrTalk(    #61
        0xFE,
        "噢噢噢！！那、那是！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "那不就是做梦都想看到的\x01",
            "『莱普尼兹号』吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "呜哇哇～～～太壮观了！！\x01",
            "一直保管在地下吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_137C")

    Jump("loc_148C")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_148C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13EC")

    ChrTalk(    #64
        0xFE,
        (
            "现、现在可不是为\x01",
            "地震而吃惊的时候，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "要在下一艘飞船到来之前\x01",
            "准备好拍摄的准备工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148C")

    label("loc_13EC")


    ChrTalk(    #66
        0xFE,
        (
            "呼～呼～\x01",
            "似、似乎还能感觉到摇晃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "啊啊～吓死我了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "不、不过现在不是因\x01",
            "地震而吃惊的时候，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "要在下一艘飞船到来之前\x01",
            "准备好拍摄的准备工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_148C")

    TalkEnd(0x12)
    Return()

    # Function_6_10C8 end

    def Function_7_1490(): pass

    label("Function_7_1490")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14ED")

    ChrTalk(    #70
        0xFE,
        "还真是吓人呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "因为目的地相同，让我\x01",
            "想起了营救博士的那一战呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1542")

    label("loc_14ED")


    ChrTalk(    #72
        0xFE,
        (
            "现在正在进行\x01",
            "工房船的出行准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "好久没有这么大的工作了，\x01",
            "真是好紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1542")

    TalkEnd(0x13)
    Return()

    # Function_7_1490 end

    def Function_8_1546(): pass

    label("Function_8_1546")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FC")

    ChrTalk(    #74
        0xFE,
        (
            "最近利用飞船的\x01",
            "合作多起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "特别是来自帝国和共和国的\x01",
            "合作明显多了起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "能签署正式协议\x01",
            "确实是个好现象啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "不过，也有可能\x01",
            "只是泡沫现象…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1650")

    label("loc_15FC")


    ChrTalk(    #78
        0xFE,
        (
            "最近对飞船的\x01",
            "合作明显多了起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "期待度越高，\x01",
            "希望破灭时的打击也就越大啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1650")

    Jump("loc_17FD")

    label("loc_1653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E5")

    ChrTalk(    #80
        0xFE,
        (
            "现在好像完全无法\x01",
            "驱动导力引擎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "难道飞船以后\x01",
            "再也无法起飞了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "作为相关行业的人员，\x01",
            "没有比这更大的打击了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1731")

    label("loc_16E5")


    ChrTalk(    #83
        0xFE,
        (
            "现在好像完全无法\x01",
            "驱动导力引擎了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "不、不过不会一直\x01",
            "都这样子的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1731")

    Jump("loc_17FD")

    label("loc_1734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_17FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1779")

    ChrTalk(    #85
        0xFE,
        "今天没有风，天气不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "嗯，很适合飞行呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17FD")

    label("loc_1779")


    ChrTalk(    #87
        0xFE,
        (
            "啊，你们也是在等\x01",
            "『赛希莉亚号』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "我要去王都\x01",
            "做一次短期出差。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "嗯，虽然是一次很短的旅行，\x01",
            "不过还是很让人期待呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_17FD")

    TalkEnd(0x14)
    Return()

    # Function_8_1546 end

    def Function_9_1801(): pass

    label("Function_9_1801")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_187F")

    ChrTalk(    #90
        0xFE,
        (
            "地震之后，\x01",
            "温泉又发生异变了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "二者看起来似乎有关联，\x01",
            "但现在没空去管它了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "嗯～～真遗憾。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1883")

    label("loc_187F")

    Call(0, 11)

    label("loc_1883")

    TalkEnd(0x15)
    Return()

    # Function_9_1801 end

    def Function_10_1887(): pass

    label("Function_10_1887")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_18ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_18E9")

    ChrTalk(    #93
        0xFE,
        (
            "似乎原因在于\x01",
            "温泉的源流呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "等编辑部的人回来以后\x01",
            "去那里调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18ED")

    label("loc_18E9")

    Call(0, 11)

    label("loc_18ED")

    TalkEnd(0x16)
    Return()

    # Function_10_1887 end

    def Function_11_18F1(): pass

    label("Function_11_18F1")

    OP_4A(0x15, 255)
    OP_4A(0x16, 255)

    ChrTalk(    #95
        0x15,
        (
            "法尔茨！\x01",
            "亚尔摩村的采访怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x15,
        (
            "不会是泡温泉\x01",
            "泡到忘了正事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x16,
        (
            "啊～没有。\x01",
            "因为出了意外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x16,
        (
            "不知是什么原因，\x01",
            "温泉的水沸腾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x15,
        "温泉沸腾了……真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x16,
        (
            "是的…已经做了\x01",
            "简单的记录。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x16,
        (
            "虽然时间匆忙，\x01",
            "不过这新闻值得报道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x15,
        "好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x15,
        (
            "那么马上整理一下，\x01",
            "归纳出一份报道吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_A2(0x6)
    OP_A2(0x7)
    Return()

    # Function_11_18F1 end

    def Function_12_1A35(): pass

    label("Function_12_1A35")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1AB8")

    ChrTalk(    #104
        0xFE,
        (
            "总之，要带的东西\x01",
            "一定不能忘掉啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "这次要去雷斯顿要塞\x01",
            "工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "要是把东西忘在这里\x01",
            "就没法回来取了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B09")

    label("loc_1AB8")


    ChrTalk(    #107
        0xFE,
        (
            "『ＸＧ－０２』\x01",
            "已经装载好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "其他附带的零件\x01",
            "也不要忘了搬进去啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1B09")

    TalkEnd(0x17)
    Return()

    # Function_12_1A35 end

    def Function_13_1B0D(): pass

    label("Function_13_1B0D")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_207D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1BCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8B")

    ChrTalk(    #109
        0x18,
        (
            "#691F听说水泵已经\x01",
            "修好了呢。\x02\x03",

            "如果可能的话，我也想去\x01",
            "亚尔摩泡泡温泉…\x02\x03",

            "算了，以后再说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1BC8")

    label("loc_1B8B")


    ChrTalk(    #110
        0x18,
        (
            "#690F哎呀呀～虽然船\x01",
            "就在那里…\x02\x03",

            "但却没办法\x01",
            "回收材料啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC8")

    Jump("loc_207A")

    label("loc_1BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_1CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C8A")

    ChrTalk(    #111
        0x18,
        "#691F哦，要找的东西已经找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1001F嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        (
            "#1040F果然普通的办法\x01",
            "还是行不通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x18,
        (
            "#691F哈，不管怎么说，\x01",
            "找到了就好。\x02\x03",

            "水泵的修理工作要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1CCC")

    label("loc_1C8A")


    ChrTalk(    #115
        0x18,
        (
            "#691F哈，不管怎么说，\x01",
            "找到了就好。\x02\x03",

            "水泵的修理工作要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCC")

    Jump("loc_207A")

    label("loc_1CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_END)), "loc_1D2A")

    ChrTalk(    #116
        0x18,
        (
            "#691F内燃引擎应该存放在\x01",
            "雷斯顿要塞中。\x02\x03",

            "抱歉啊～你们自己\x01",
            "去那里问问可以吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207A")

    label("loc_1D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3D")
    Call(0, 43)
    Jump("loc_207A")

    label("loc_1D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1DAE")

    ChrTalk(    #117
        0x18,
        (
            "#691F这样下去的话，\x01",
            "也许以后还会有什么事发生呢。\x02\x03",

            "也许还会需要你们的帮忙，\x01",
            "到那时请一定多关照啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207A")

    label("loc_1DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2025")
    OP_A2(0x2084)
    OP_A2(0x9)

    ChrTalk(    #118
        0x18,
        (
            "#692F啊，我还以为是谁，\x01",
            "这不是艾丝蒂尔吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1000F维修长先生，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x102, 400)

    ChrTalk(    #121
        0x18,
        (
            "#691F噢！这不是约修亚吗。\x02\x03",

            "怎么回事，好像\x01",
            "有很久没见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1016F哈，这个就\x01",
            "说来话长了……\x02\x03",

            "#1000F……那个，维修长先生，\x01",
            "这里的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF9")

    ChrTalk(    #123
        0x107,
        (
            "#063F啊，还是有一些\x01",
            "骚乱的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF9")

    TurnDirection(0x18, 0x101, 400)

    ChrTalk(    #124
        0x18,
        (
            "#690F发生了这样的异变，\x01",
            "确实不得了啊。\x02\x03",

            "总之城里的情况已经算是\x01",
            "稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#1040F是吗……\x02\x03",

            "总算是暂时把\x01",
            "混乱控制住了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x18,
        (
            "#691F啊啊，但是这样的话\x01",
            "也许以后还会有什么事发生呢。\x02\x03",

            "#693F也许会需要你们的帮忙。\x01",
            "到那时请一定多关照啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1001F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#1040F拜托你了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_207A")

    label("loc_2025")


    ChrTalk(    #129
        0x18,
        (
            "#690F这里的飞船坪\x01",
            "是用特殊构造建筑的。\x02\x03",

            "导力无法复员，\x01",
            "船的整备也没办法进行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207A")

    Jump("loc_2451")

    label("loc_207D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_21A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_215B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_20E6")

    ChrTalk(    #130
        0x18,
        (
            "#690F听说连雷斯顿要塞\x01",
            "也发生地震了啊？\x02\x03",

            "要是设备没有被损毁\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215B")

    label("loc_20E6")


    ChrTalk(    #131
        0x18,
        (
            "#690F中央工房刚刚\x01",
            "来联络过了……\x02\x03",

            "雷斯顿要塞也\x01",
            "也发生地震了啊？\x02\x03",

            "呼，『埃尔赛尤』的工事\x01",
            "别出什么意外就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_215B")

    Jump("loc_21A6")

    label("loc_215E")


    ChrTalk(    #132
        0x18,
        (
            "#690F亚尔摩村竟然是震源……\x01",
            "真是搞不懂。\x02\x03",

            "总之，大家要小心行事啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A6")

    Jump("loc_2451")

    label("loc_21A9")


    ChrTalk(    #133
        0x101,
        "#1004F啊！维修长先生！\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x18)
    TurnDirection(0x18, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_222B")

    ChrTalk(    #134
        0x18,
        (
            "#6901F喔喔……\x01",
            "这不是艾丝蒂尔吗！\x02\x03",

            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2265")

    label("loc_222B")


    ChrTalk(    #135
        0x18,
        (
            "#691F喔喔……\x01",
            "这不是艾丝蒂尔吗！\x02\x03",

            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2265")


    ChrTalk(    #136
        0x101,
        (
            "#1006F好久不见，\x01",
            "维修长先生也很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x18,
        (
            "#691F你们现在正在调查地震是吧？\x02\x03",

            "发现了什么线索吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1015F嗯，是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #139
        "\x07\x05将地震源是亚尔摩村告诉给维修长。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #140
        0x18,
        (
            "#692F……真是令人不解啊。\x02\x03",

            "如果要去调查的话\x01",
            "尽早行动比较好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2390")

    ChrTalk(    #141
        0x106,
        "#050F嗯，同感…\x02",
    )

    CloseMessageWindow()
    Jump("loc_23A9")

    label("loc_2390")


    ChrTalk(    #142
        0x103,
        "#026F啊，同感哦……\x02",
    )

    CloseMessageWindow()

    label("loc_23A9")


    ChrTalk(    #143
        0x101,
        (
            "#1002F嗯……\x01",
            "确实应该抓紧时间赶快去。\x02\x03",

            "那么，维修长先生，我们先走了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x107, 400)

    ChrTalk(    #144
        0x18,
        (
            "#691F噢！大家加油吧。\x02\x03",

            "#691F提妲也要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x107,
        "#560F是、是的！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1483)
    OP_A2(0x9)
    ClearChrFlags(0x18, 0x10)

    label("loc_2451")

    TalkEnd(0x18)
    Return()

    # Function_13_1B0D end

    def Function_14_2455(): pass

    label("Function_14_2455")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_249E")

    ChrTalk(    #146
        0xFE,
        (
            "定期船啊，\x01",
            "好久没坐过了，真期待啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "噢噢～快点来吧。\x02",
    )

    CloseMessageWindow()

    label("loc_249E")

    TalkEnd(0x19)
    Return()

    # Function_14_2455 end

    def Function_15_24A2(): pass

    label("Function_15_24A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24B3")
    Call(0, 44)

    label("loc_24B3")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearMapFlags(0x10)
    OP_6D(-33680, -4000, 150830, 0)
    OP_67(0, 14240, -10000, 0)
    OP_6B(8800, 0)
    OP_6C(44000, 0)
    OP_6E(175, 0)
    OP_A1(0x1A, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x1A, -34000, -150, 148000, 0)
    SetChrFlags(0x1A, 0x4)
    OP_A1(0x1B, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x1B, -34000, -10150, 148000, 0)
    SetChrFlags(0x1B, 0x4)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x6, 0x4)
    OP_6F(0x3, 100)
    OP_6F(0x4, 60)
    OP_6F(0x5, 0)
    OP_C8(0x200, 0x46, "C_PLAC08._CH", 0x0, 0x5DC)
    FadeToBright(1500, 0)

    def lambda_2589():
        OP_6C(57000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2589)

    def lambda_2599():
        OP_6B(6800, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2599)
    Call(0, 16)
    Fade(1000)
    OP_6D(-46650, -4000, 144430, 0)
    OP_67(0, 11610, -10000, 0)
    OP_6B(4120, 0)
    OP_6C(314000, 0)
    OP_6E(175, 0)
    OP_6F(0x3, 200)
    OP_6F(0x4, 1)
    OP_6F(0x5, 0)
    OP_0D()
    OP_43(0x8, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x11)
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x11)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x14)
    Sleep(1000)
    OP_43(0xD, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0xF, 0x1, 0x0, 0x16)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x18)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x19)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0x1A)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x1B)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #148
        0x101,
        (
            "#1006F#1P那么，先去一趟\x01",
            "协会吧。\x02\x03",

            "要先和雾香姐打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x104,
        (
            "#033F喔～听名字好像\x01",
            "是位东方的女子啊。\x02\x03",

            "#031F是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1007F#1P又开始了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27E9")

    ChrTalk(    #151
        0x106,
        (
            "#051F#5P嗯，简单说，就是个精明强干的女人。\x02\x03",

            "她可是个比雪拉扎德更厉害的女中豪杰，\x01",
            "想乱来的话先掂量一下吧。\x02\x03",

            "#551F说明白一点，我不想被牵连到，\x01",
            "拜托你别拖累我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A4")

    label("loc_27E9")


    ChrTalk(    #152
        0x103,
        (
            "#027F#5P一言以蔽之，就是个『能干的女人』。\x02\x03",

            "不但处理事务的能力近乎完美，\x01",
            "武术造诣也是达人级的。\x02\x03",

            "#021F虽然是个美人，但她可是丝毫不讲情面的，\x01",
            "如果有什么妄想的话，你可要有所觉悟才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A4")


    ChrTalk(    #153
        0x104,
        (
            "#031F呼呼～听你这么一说，\x01",
            "我对她越来越有兴趣了！\x02\x03",

            "那我们赶快去协会…\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x85, 0x0, 0x64)
    OP_20(0x5DC)

    def lambda_28FE():

        label("loc_28FE")

        OP_7C(0xC8, 0x0, 0x7D0, 0xBB8)
        OP_48()
        Jump("loc_28FE")

    QueueWorkItem2(0x101, 3, lambda_28FE)
    Sleep(500)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_A3(0x0)
    OP_43(0xA, 0x1, 0x0, 0x1D)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0x1F)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x20)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x21)
    Sleep(200)
    OP_43(0xF, 0x1, 0x0, 0x22)
    OP_8C(0x104, 140, 400)
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #154
        0x104,
        (
            "#036F#6P噢噢……！？\x02\x03",

            "这、这个难道就是…\x01",
            "那个雾香小姐的愤怒吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 140, 400)

    ChrTalk(    #155
        0x101,
        "#1019F#5P那、那怎么可能嘛～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)

    ChrTalk(    #156
        0x105,
        "#043F好像……是地震啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xC,
        "#5P救、救命呀～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 184, 400)
    OP_8C(0xF7, 65, 400)

    ChrTalk(    #158
        0xF,
        "#2P要、要掉下去了！\x02",
    )

    CloseMessageWindow()
    OP_4A(0x10, 255)
    SetChrPos(0x10, -45950, 0, 128050, 0)

    ChrTalk(    #159
        0x10,
        (
            "#2P各、各位！\x01",
            "请镇定！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A91():
        OP_6D(-46130, -4000, 138120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A91)

    def lambda_2AA9():
        OP_67(0, 11000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AA9)

    def lambda_2AC1():
        OP_6B(4480, 3000)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2AC1)

    def lambda_2AD1():
        OP_6C(230000, 3000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2AD1)
    OP_8E(0x10, 0xFFFF4BF6, 0xFFFFF34E, 0x213A4, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_2AFA():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2AFA)
    Sleep(100)

    def lambda_2B0D():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B0D)

    def lambda_2B1B():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B1B)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #160
        0x10,
        (
            "#5P这个飞船坪的下层\x01",
            "在设计时就强化了抗震能力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10,
        (
            "#5P这次地震的震级并不高，\x01",
            "大家不用担心！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x85, 0x5A)
    OP_44(0x101, 0x3)

    def lambda_2B98():

        label("loc_2B98")

        OP_7C(0x64, 0x0, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_2B98")

    QueueWorkItem2(0x101, 3, lambda_2B98)
    Sleep(500)
    OP_24(0x85, 0x4B)
    Sleep(500)
    OP_A2(0x0)
    OP_24(0x85, 0x3C)
    OP_44(0x101, 0x3)

    def lambda_2BCC():

        label("loc_2BCC")

        OP_7C(0x32, 0x0, 0x1F4, 0x3E8)
        OP_48()
        Jump("loc_2BCC")

    QueueWorkItem2(0x101, 3, lambda_2BCC)
    Sleep(500)
    OP_44(0xC, 0x1)
    OP_4A(0xC, 255)
    OP_24(0x85, 0x32)
    Sleep(500)

    def lambda_2BFD():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2BFD)
    OP_24(0x85, 0x28)
    OP_44(0x101, 0x3)

    def lambda_2C13():

        label("loc_2C13")

        OP_7C(0x19, 0x0, 0xFA, 0x3E8)
        OP_48()
        Jump("loc_2C13")

    QueueWorkItem2(0x101, 3, lambda_2C13)
    Sleep(500)
    OP_44(0xA, 0x1)
    OP_4A(0xA, 255)
    OP_24(0x85, 0x1E)
    Sleep(500)

    def lambda_2C44():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2C44)
    OP_24(0x85, 0x14)
    OP_44(0x101, 0x3)

    def lambda_2C5A():

        label("loc_2C5A")

        OP_7C(0xC, 0x0, 0x7D, 0x3E8)
        OP_48()
        Jump("loc_2C5A")

    QueueWorkItem2(0x101, 3, lambda_2C5A)
    Sleep(500)
    OP_44(0xB, 0x1)
    OP_4A(0xB, 255)
    OP_24(0x85, 0xA)
    Sleep(500)

    def lambda_2C8B():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2C8B)
    OP_23(0x85)
    OP_44(0x101, 0x3)
    Sleep(500)
    OP_44(0xD, 0x1)
    OP_4A(0xD, 255)

    def lambda_2CAD():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CAD)
    Sleep(500)
    OP_44(0xF, 0x1)
    OP_4A(0xF, 255)

    def lambda_2CC8():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2CC8)
    Sleep(1000)

    ChrTalk(    #162
        0x101,
        "#1025F#2P停、停了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        "#5P已、已经没事了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        (
            "#5P好了，各位。\x01",
            "已经没事了，请不要惊慌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xD,
        (
            "真是的……\x01",
            "好久没遇到地震了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 400)
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #166
        0xA,
        "#5P嘿嘿～还真是刺激啊！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10, 180, 400)

    def lambda_2D9D():
        OP_8E(0xFE, 0xFFFF4C6E, 0x0, 0x1EE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D9D)
    Sleep(400)
    OP_8C(0xB, 180, 400)

    def lambda_2DC4():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DC4)
    Sleep(100)
    OP_8C(0xA, 180, 400)

    def lambda_2DEB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DEB)
    Sleep(200)
    OP_8C(0xC, 180, 400)

    def lambda_2E12():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2E12)
    Sleep(200)
    OP_8C(0xD, 180, 400)

    def lambda_2E39():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E39)
    Sleep(200)
    OP_8C(0xF, 180, 400)

    def lambda_2E60():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E60)
    Sleep(1500)

    def lambda_2E80():
        OP_6D(-46690, -4000, 143590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E80)

    def lambda_2E98():
        OP_67(0, 11000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E98)
    OP_8C(0x101, 45, 400)
    OP_8C(0xF7, 135, 400)
    OP_8C(0x105, 225, 400)
    OP_8C(0x104, 0, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)

    ChrTalk(    #167
        0x101,
        (
            "#1007F呼……吓死人了。\x02\x03",

            "#1019F虽然震得并不算强烈，\x01",
            "但在这种不安全的地方发生摇晃，\x01",
            "还真是危险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        (
            "#045F呵呵，是啊。\x02\x03",

            "#043F不过利贝尔可是\x01",
            "很少发生地震的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x104,
        "#033F#5P哦，是这样吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3012")

    ChrTalk(    #170
        0x106,
        (
            "#053F#2P嗯……\x01",
            "只有过极少的几次。\x02\x03",

            "#050F我们要确认一下受害情况，\x01",
            "赶快到协会去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306B")

    label("loc_3012")


    ChrTalk(    #171
        0x103,
        (
            "#026F#2P嗯……\x01",
            "几乎从来没发生过呢。\x02\x03",

            "#022F我们要确认一下受害情况，\x01",
            "赶快到协会去吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306B")

    OP_4B(0x10, 255)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_24A2 end

    def Function_16_308C(): pass

    label("Function_16_308C")


    def lambda_3092():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3092)

    def lambda_30AD():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFE412, 0x24220, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_30AD)
    WaitChrThread(0x1A, 0x1)

    def lambda_30CD():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD85A, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_30CD)
    WaitChrThread(0x1A, 0x1)

    def lambda_30ED():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_30ED)
    WaitChrThread(0x1A, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x1A, -34000, -11150, 148000, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_6F(0x4, 410)
    OP_70(0x4, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x4)
    OP_44(0x0, 0x1)
    Return()

    # Function_16_308C end

    def Function_17_318B(): pass

    label("Function_17_318B")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4CBE, 0x0, 0x1F4A0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_318B end

    def Function_18_31CF(): pass

    label("Function_18_31CF")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF46F6, 0xFFFFF060, 0x22024, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_18_31CF end

    def Function_19_321C(): pass

    label("Function_19_321C")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF49F8, 0xFFFFF060, 0x21C5A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_19_321C end

    def Function_20_326E(): pass

    label("Function_20_326E")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A70, 0xFFFFF060, 0x220EC, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_20_326E end

    def Function_21_32C0(): pass

    label("Function_21_32C0")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D72, 0xFFFFF060, 0x228F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4F66, 0xFFFFF060, 0x222E0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_21_32C0 end

    def Function_22_3326(): pass

    label("Function_22_3326")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D72, 0xFFFFF060, 0x228F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4FA2, 0xFFFFF060, 0x226C8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_22_3326 end

    def Function_23_338C(): pass

    label("Function_23_338C")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    Return()

    # Function_23_338C end

    def Function_24_33B7(): pass

    label("Function_24_33B7")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0x101, 0xFFFF482C, 0xFFFFF060, 0x23104, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Return()

    # Function_24_33B7 end

    def Function_25_33FD(): pass

    label("Function_25_33FD")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xF7, 0xFFFF48E0, 0xFFFFF060, 0x2353C, 0x7D0, 0x0)
    OP_8C(0xF7, 135, 400)
    Return()

    # Function_25_33FD end

    def Function_26_3443(): pass

    label("Function_26_3443")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0x105, 0xFFFF4D7C, 0xFFFFF060, 0x23410, 0x7D0, 0x0)
    OP_8C(0x105, 270, 400)
    Return()

    # Function_26_3443 end

    def Function_27_3489(): pass

    label("Function_27_3489")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0x104, 0xFFFF4CB4, 0xFFFFF060, 0x22F92, 0x7D0, 0x0)
    OP_8C(0x104, 315, 400)
    Return()

    # Function_27_3489 end

    def Function_28_34CF(): pass

    label("Function_28_34CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3548")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351D")
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    Jump("loc_3545")

    label("loc_351D")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)

    label("loc_3545")

    Jump("Function_28_34CF")

    label("loc_3548")

    Return()

    # Function_28_34CF end

    def Function_29_3549(): pass

    label("Function_29_3549")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35C2")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3597")
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    Jump("loc_35BF")

    label("loc_3597")

    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)

    label("loc_35BF")

    Jump("Function_29_3549")

    label("loc_35C2")

    Return()

    # Function_29_3549 end

    def Function_30_35C3(): pass

    label("Function_30_35C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_363C")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3611")
    OP_90(0xFE, 0x5DC, 0x0, 0x5DC, 0xFA0, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    Jump("loc_3639")

    label("loc_3611")

    OP_90(0xFE, 0x5DC, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)

    label("loc_3639")

    Jump("Function_30_35C3")

    label("loc_363C")

    Return()

    # Function_30_35C3 end

    def Function_31_363D(): pass

    label("Function_31_363D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3685")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 315, 400)
    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    Jump("Function_31_363D")

    label("loc_3685")

    Return()

    # Function_31_363D end

    def Function_32_3686(): pass

    label("Function_32_3686")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36FF")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D4")
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    Jump("loc_36FC")

    label("loc_36D4")

    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)

    label("loc_36FC")

    Jump("Function_32_3686")

    label("loc_36FF")

    Return()

    # Function_32_3686 end

    def Function_33_3700(): pass

    label("Function_33_3700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_373A")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 180, 400)
    Jump("Function_33_3700")

    label("loc_373A")

    Return()

    # Function_33_3700 end

    def Function_34_373B(): pass

    label("Function_34_373B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3775")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Jump("Function_34_373B")

    label("loc_3775")

    Return()

    # Function_34_373B end

    def Function_35_3776(): pass

    label("Function_35_3776")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3796")
    Call(0, 44)
    Call(0, 45)
    FadeToBright(0, 0)

    label("loc_3796")

    Fade(1000)
    SetChrPos(0x101, -19580, 8000, 119820, 0)
    SetChrPos(0xF7, -20630, 8000, 119820, 0)
    SetChrPos(0xF8, -19710, 8000, 118700, 0)
    SetChrPos(0xF9, -20720, 8000, 118640, 0)
    OP_6D(-20180, 8000, 120530, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(194, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6A")
    OP_A2(0x1601)

    ChrTalk(    #172
        0x10,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x10,
        (
            "你们就是要前往格兰赛尔\x01",
            "的游击士们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1011F啊，嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10,
        (
            "雾香小姐已经\x01",
            "支付了船票费用，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        "现在要办乘船手续吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_392E")

    ChrTalk(    #177
        0x106,
        (
            "#050F如果办好了手续，那在船到之前\x01",
            "在这里等着就可以了。\x02\x03",

            "在蔡斯地区的事情\x01",
            "没有事留下了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3995")

    label("loc_392E")


    ChrTalk(    #178
        0x103,
        (
            "#020F如果办好了手续，那在船到之前\x01",
            "在这里等着就可以了。\x02\x03",

            "在蔡斯地区\x01",
            "已经没有什么事情还需要做的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3995")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BA7")

    ChrTalk(    #179
        0x101,
        (
            "#1015F啊，说起来的话……\x02\x03",

            "探测器好像\x01",
            "还没还呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A1B")

    ChrTalk(    #180
        0x107,
        "#560F是『合金探测器』吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Jump("loc_3A8C")

    label("loc_3A1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A52")

    ChrTalk(    #181
        0x104,
        "#030F是『合金探测器』呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Jump("loc_3A8C")

    label("loc_3A52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A8C")

    ChrTalk(    #182
        0x105,
        "#542F就是那个『合金探测器』吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_3A8C")


    ChrTalk(    #183
        0x101,
        (
            "#1006F对对，就是那个。\x02\x03",

            "是在中央工房\x01",
            "一楼的维修柜台\x01",
            "借来的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3B13")

    ChrTalk(    #184
        0x106,
        (
            "#051F工房一楼的维修柜台吗。\x02\x03",

            "好，那我们就快点去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B48")

    label("loc_3B13")


    ChrTalk(    #185
        0x103,
        (
            "#020F工房一楼的维修柜台吗，\x02\x03",

            "那我们就赶快去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B48")


    ChrTalk(    #186
        0x10,
        (
            "那么，等你们的事情办完了\x01",
            "再到这里找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3500, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_3BA7")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C67")

    ChrTalk(    #187
        0x10,
        (
            "那么，等你们的事情办完了\x01",
            "再到这里找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_3C67")

    Jump("loc_3DF5")

    label("loc_3C6A")


    ChrTalk(    #188
        0x10,
        (
            "哦。\x01",
            "要办理乘船手续吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D35")

    ChrTalk(    #189
        0x101,
        (
            "#1015F啊，说起来的话……\x02\x03",

            "合金探测器\x01",
            "还没还呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x10,
        (
            "那么，等你们的事情办完了\x01",
            "再到这里找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_3D35")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF5")

    ChrTalk(    #191
        0x10,
        (
            "那么，等你们的事情办完了\x01",
            "再到这里找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_3DF5")


    ChrTalk(    #192
        0x10,
        "明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x10,
        (
            "那么，就去协会\x01",
            "联络其他的同伴吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #194
        (
            "\x07\x05艾丝蒂尔一行人办理完乘船手续之后\x01",
            "就在原地等待飞船起飞。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x19, 0x80)
    Call(0, 36)
    Return()

    # Function_35_3776 end

    def Function_36_3EC4(): pass

    label("Function_36_3EC4")

    EventBegin(0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EEB")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F15")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F11")
    AddParty(0x4, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F15")

    label("loc_3F11")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_3F15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F3F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3B")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F3F")

    label("loc_3F3B")

    AddParty(0x6, 0xFB, 0xFF)

    label("loc_3F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F69")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F65")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3F69")

    label("loc_3F65")

    AddParty(0x7, 0xFB, 0xFF)

    label("loc_3F69")

    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_6F(0x4, 100)
    OP_6F(0x3, 100)
    SetChrPos(0x101, -46010, -4000, 151140, 14)
    SetChrPos(0xF7, -47050, -4000, 152510, 87)
    SetChrPos(0x107, -47040, -4000, 153400, 87)
    SetChrPos(0x105, -45400, -4000, 151930, 267)
    SetChrPos(0x104, -45280, -4000, 153160, 267)
    SetChrPos(0x108, -46100, -4000, 154080, 177)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, -46990, -4000, 147520, 177)
    SetChrPos(0x9, -46840, -4000, 144960, 357)
    SetChrPos(0xA, -46720, -4000, 146170, 87)
    SetChrPos(0xB, -46700, -4000, 148750, 177)
    SetChrPos(0xC, -46590, -4000, 149930, 177)
    SetChrPos(0xD, -45070, -3800, 144000, 87)
    SetChrPos(0xE, -46280, -4000, 143940, 87)
    OP_6D(-42120, -4000, 150190, 0)
    OP_67(0, 8330, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(62000, 0)
    OP_6E(331, 0)
    SetChrPos(0x1A, -34000, -11150, 148000, 0)
    OP_A1(0x1A, 0x4)
    OP_72(0x4, 0x4)
    SetChrFlags(0x1A, 0x4)
    OP_A1(0x1B, 0x5)
    SetChrPos(0x1B, -34000, -11150, 148000, 0)
    OP_72(0x5, 0x4)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x4, 60)
    OP_71(0x6, 0x4)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(3000)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_43(0xD, 0x1, 0x0, 0x25)
    Sleep(500)
    OP_43(0xE, 0x1, 0x0, 0x26)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x27)
    OP_43(0xA, 0x1, 0x0, 0x27)
    Sleep(600)
    OP_43(0x8, 0x1, 0x0, 0x28)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x29)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x28)
    Sleep(600)
    OP_8C(0x101, 225, 400)
    OP_43(0x101, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_8C(0xF7, 180, 400)
    OP_43(0xF7, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_8C(0x107, 180, 400)
    OP_43(0x107, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_8C(0x105, 225, 400)
    Sleep(1200)
    OP_43(0x105, 0x1, 0x0, 0x2A)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_43(0x104, 0x1, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x108, 0x1, 0x0, 0x2A)
    Sleep(1000)
    OP_0D()
    OP_6D(-33540, -6900, 151660, 0)
    OP_67(0, 600, -10000, 0)
    OP_6B(4360, 0)
    OP_6C(169000, 0)
    OP_6E(425, 0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Sleep(1000)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1000)

    def lambda_42F3():
        OP_67(0, 3030, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42F3)
    FadeToBright(2000, 0)
    OP_0D()
    Fade(500)
    OP_72(0x6, 0x4)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(1000)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0x4, 61)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)
    OP_23(0x75)
    OP_91(0x1A, 0x0, 0x12C, 0x0, 0x12C, 0x0)
    OP_91(0x1A, 0x0, 0x320, 0x0, 0x1F4, 0x0)
    Sleep(2000)

    def lambda_43AC():
        OP_6D(-33490, -6100, 161910, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43AC)

    def lambda_43C4():
        OP_67(0, 3180, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43C4)

    def lambda_43DC():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_43DC)
    OP_94(0x1, 0x1A, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_4401():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4401)
    OP_94(0x1, 0x1A, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_4426():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4426)
    OP_94(0x1, 0x1A, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_444B():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_444B)
    OP_94(0x1, 0x1A, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_4470():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4470)
    FadeToDark(2000, 0, -1)
    OP_94(0x1, 0x1A, 0x0, 0x708, 0x1388, 0x0)

    def lambda_449F():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_449F)
    OP_94(0x1, 0x1A, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_44C4():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_44C4)
    OP_94(0x1, 0x1A, 0x0, 0x898, 0x1B58, 0x0)

    def lambda_44E9():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_44E9)

    def lambda_44FF():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_44FF)
    OP_24(0x77, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_23(0x77)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x1602)
    OP_A2(0x10F2)
    OP_28(0x6C, 0x4, 0x40)
    OP_28(0x6D, 0x4, 0x40)
    OP_28(0x6E, 0x4, 0x40)
    OP_28(0x6F, 0x4, 0x40)
    OP_28(0x70, 0x4, 0x40)
    OP_28(0x71, 0x4, 0x40)
    OP_28(0xA5, 0x4, 0x40)
    OP_28(0xA6, 0x4, 0x40)
    OP_28(0xA7, 0x4, 0x40)
    OP_28(0xA8, 0x4, 0x40)
    NewScene("ED6_DT21/E0001   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_36_3EC4 end

    def Function_37_45B8(): pass

    label("Function_37_45B8")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF7888, 0xFFFFF060, 0x23186, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_37_45B8 end

    def Function_38_45E6(): pass

    label("Function_38_45E6")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF8292, 0xFFFFF060, 0x23186, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_38_45E6 end

    def Function_39_4614(): pass

    label("Function_39_4614")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4BC4, 0xFFFFF060, 0x232EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7EAA, 0xFFFFF060, 0x23186, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_39_4614 end

    def Function_40_4656(): pass

    label("Function_40_4656")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF491C, 0xFFFFF060, 0x2324E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7E46, 0xFFFFF060, 0x2314A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_40_4656 end

    def Function_41_4698(): pass

    label("Function_41_4698")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF491C, 0xFFFFF060, 0x2324E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7CB6, 0xFFFFF060, 0x2314A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_41_4698 end

    def Function_42_46DA(): pass

    label("Function_42_46DA")

    OP_8E(0xFE, 0xFFFF48EA, 0xFFFFF060, 0x24626, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF49A8, 0xFFFFF060, 0x2330C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF793C, 0xFFFFF060, 0x232EE, 0x7D0, 0x0)
    Return()

    # Function_42_46DA end

    def Function_43_4717(): pass

    label("Function_43_4717")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4737")
    Call(0, 44)
    Call(0, 46)
    FadeToBright(0, 0)

    label("loc_4737")

    Fade(1000)
    OP_6D(-38930, 8000, 126550, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3750, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -39260, 8000, 127280, 0)
    SetChrPos(0x102, -40320, 8000, 127230, 0)
    SetChrPos(0xF8, -39030, 8000, 126180, 0)
    SetChrPos(0xF9, -40150, 8000, 126180, 0)
    OP_4A(0x18, 255)
    SetChrSubChip(0x18, 0)
    OP_8C(0x18, 180, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49F6")

    ChrTalk(    #195
        0x18,
        (
            "#692F#6P啊，我还说是谁，\x01",
            "这不是艾丝蒂尔吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1025F#5P维修长先生，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        "#1040F#2P好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x18,
        (
            "#691F#6P噢！这不是约修亚吗。\x02\x03",

            "怎么回事，好像\x01",
            "有很久没见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1016F#5P算了，稍微\x01",
            "说来话长了……\x02\x03",

            "#1015F……嗯，工房长先生那边\x01",
            "现在的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4922")

    ChrTalk(    #200
        0x107,
        (
            "#063F#2P为什么会发生\x01",
            "骚乱的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4922")


    ChrTalk(    #201
        0x18,
        (
            "#691F#6P异常发生的当时\x01",
            "确实不得了啊。\x02\x03",

            "总之城里的情况已经算是\x01",
            "稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        (
            "#1035F#2P是吗……\x02\x03",

            "#1040F总算是从\x01",
            "混乱中摆脱了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x18,
        (
            "#691F#6P啊啊，是啊……\x02\x03",

            "那个暂且不说……\x01",
            "这次来是有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x2084)
    Jump("loc_4B9F")

    label("loc_49F6")


    ChrTalk(    #204
        0x18,
        (
            "#691F#6P噢，是你们吗。\x01",
            "还是和以前一样，总那么忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#1016F#5P啊哈哈……\x01",
            "维修长先生也是一样啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#1040F#2P您辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x18,
        (
            "#690F#6P呵呵，忙虽然是忙，\x01",
            "但特殊情况也没办法……\x02\x03",

            "机械这东西，\x01",
            "一点疏忽也都会要了命，\x02\x03",

            "只能打起精神撑下去啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B1F")

    ChrTalk(    #208
        0x107,
        (
            "#063F#2P那、那确实\x01",
            "很辛苦呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B1F")


    ChrTalk(    #209
        0x101,
        (
            "#1015F#5P嗯～和我\x01",
            "学习棒术时的感觉\x01",
            "应该很相似吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x18,
        (
            "#691F#6P哈，应该差不多吧。\x02\x03",

            "那个暂且不说……\x01",
            "你们这次来有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9F")


    ChrTalk(    #211
        0x102,
        "#1040F#2P是的，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        (
            "\x07\x05向格斯塔夫维修长说明了\x01",
            "要借内燃引擎用的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #213
        0x18,
        (
            "#692F#6P原来如此……\x01",
            "真是个好主意啊。\x02\x03",

            "#690F那东西只能驱动单体机械，\x01",
            "现在已经没什么用了，\x01",
            "可以的话借你们也没问题，可是…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CBA")

    ChrTalk(    #214
        0x106,
        "#052F#2P有什么问题吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D19")

    label("loc_4CBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CE7")

    ChrTalk(    #215
        0x103,
        "#023F#2P有什么问题吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D19")

    label("loc_4CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D19")

    ChrTalk(    #216
        0x108,
        "#073F#2P看起来似乎有些问题啊？\x02",
    )

    CloseMessageWindow()

    label("loc_4D19")


    ChrTalk(    #217
        0x18,
        (
            "#690F#6P这个嘛……\x02\x03",

            "真是不巧，已经\x01",
            "借给王国军了。\x02\x03",

            "就在上次『埃尔赛尤』\x01",
            "改装引擎的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#1015F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DD4")

    ChrTalk(    #219
        0x107,
        (
            "#064F#2P那也就是说，那东西现在\x01",
            "在雷斯顿要塞吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E06")

    label("loc_4DD4")


    ChrTalk(    #220
        0x102,
        (
            "#1044F#2P那么，那东西现在\x01",
            "在雷斯顿要塞对吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E06")


    ChrTalk(    #221
        0x18,
        (
            "#691F#6P啊啊，就是那样。\x02\x03",

            "不好意思，如果一定要借的话，\x01",
            "就只能请你们自己去要了。\x02\x03",

            "像现在这种状态，\x01",
            "连通信器也没办法使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1006F#5P嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        (
            "#1040F#2P嗯，我们会尝试和雷斯顿要塞\x01",
            "那边联络的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x200B)
    OP_28(0xC2, 0x1, 0x8)

    def lambda_4EE2():
        OP_8C(0x18, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4EE2)
    OP_4B(0x18, 255)
    EventEnd(0x0)
    Return()

    # Function_43_4717 end

    def Function_44_4EF1(): pass

    label("Function_44_4EF1")

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
        (0, "loc_4F6B"),
        (1, "loc_4F71"),
        (SWITCH_DEFAULT, "loc_4F77"),
    )


    label("loc_4F6B")

    OP_A2(0x1200)
    Jump("loc_4F77")

    label("loc_4F71")

    OP_A2(0x1201)
    Jump("loc_4F77")

    label("loc_4F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4F85")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4F89")

    label("loc_4F85")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4F89")

    Return()

    # Function_44_4EF1 end

    def Function_45_4F8A(): pass

    label("Function_45_4F8A")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4FC8")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_4FE6")

    label("loc_4FC8")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_4FE6")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_45_4F8A end

    def Function_46_4FF8(): pass

    label("Function_46_4FF8")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_46_4FF8 end

    def Function_47_5051(): pass

    label("Function_47_5051")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #224
        (
            "\x07\x05定期船起降坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　前往卢安市\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #225
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　『利贝尔飞船公社』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_5051 end

    def Function_48_50ED(): pass

    label("Function_48_50ED")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #226
        (
            "\x07\x05　　　飞船坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            " 『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_48_50ED end

    SaveToFile()

Try(main)
