from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3120   ._SN',
            'ED6_DT21/T3120_1 ._SN',
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
        '雾香',                                 # 9
        '拉赛尔博士',                           # 10
        '提妲',                                 # 11
        '测量仪',                               # 12
        '测量仪',                               # 13
        '测量仪',                               # 14
        '奥利维尔',                             # 15
        '科洛丝',                               # 16
        '玛多克工房长',                         # 17
        '金',                                   # 18
        '埃尔文',                               # 19
        '耶鲁克',                               # 20
        '艾妲',                                 # 21
        '呆呆',                                 # 22
        '王',                                   # 23
        '雪拉扎德',                             # 24
        '阿加特',                               # 25
        '吉米',                                 # 26
        '莫妮卡',                               # 27
        '临时',                                 # 28
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00033 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT07/CH02620 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01030 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH00023 ._CH',             # 0F
        'ED6_DT07/CH00053 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT07/CH00073 ._CH',             # 12
        'ED6_DT07/CH01040 ._CH',             # 13
        'ED6_DT07/CH02490 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00033P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT07/CH02620P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01030P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH00023P._CP',             # 0F
        'ED6_DT07/CH00053P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT07/CH00073P._CP',             # 12
        'ED6_DT07/CH01040P._CP',             # 13
        'ED6_DT07/CH02490P._CP',             # 14
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1E6,
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
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 1000,
        Y                   = 53000,
        Direction           = 183,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 52970,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 172,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 52390,
        Z                   = 0,
        Y                   = 53790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55570,
        Z                   = 0,
        Y                   = 51740,
        Direction           = 63,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 25480,
        Z                   = 0,
        Y                   = -3020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = -3440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40,
        Z                   = 1000,
        Y                   = 50980,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -50,
        Y                   = 0,
        Z                   = -7200,
        Range               = 3010,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE98A,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_482",          # 00, 0
        "Function_1_771",          # 01, 1
        "Function_2_7BA",          # 02, 2
        "Function_3_861",          # 03, 3
        "Function_4_8B2",          # 04, 4
        "Function_5_8B7",          # 05, 5
        "Function_6_FC0",          # 06, 6
        "Function_7_1368",         # 07, 7
        "Function_8_190E",         # 08, 8
        "Function_9_1913",         # 09, 9
        "Function_10_2117",        # 0A, 10
        "Function_11_3C24",        # 0B, 11
        "Function_12_445C",        # 0C, 12
        "Function_13_460B",        # 0D, 13
        "Function_14_57F4",        # 0E, 14
        "Function_15_5810",        # 0F, 15
        "Function_16_582C",        # 10, 16
        "Function_17_5848",        # 11, 17
        "Function_18_5864",        # 12, 18
        "Function_19_5894",        # 13, 19
        "Function_20_7B30",        # 14, 20
        "Function_21_7B9D",        # 15, 21
        "Function_22_7C0A",        # 16, 22
        "Function_23_7C77",        # 17, 23
        "Function_24_7CDA",        # 18, 24
        "Function_25_A17B",        # 19, 25
        "Function_26_A40C",        # 1A, 26
        "Function_27_BF81",        # 1B, 27
        "Function_28_BFB1",        # 1C, 28
        "Function_29_BFE1",        # 1D, 29
        "Function_30_C011",        # 1E, 30
        "Function_31_C041",        # 1F, 31
        "Function_32_C86F",        # 20, 32
        "Function_33_C8A0",        # 21, 33
        "Function_34_C8DA",        # 22, 34
        "Function_35_C914",        # 23, 35
        "Function_36_C94E",        # 24, 36
        "Function_37_C988",        # 25, 37
        "Function_38_CF84",        # 26, 38
        "Function_39_D01D",        # 27, 39
        "Function_40_D083",        # 28, 40
    )


    def Function_0_482(): pass

    label("Function_0_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AD")
    OP_A3(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6")
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 23530, 200, -2100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 18)
    OP_A2(0x9)

    label("loc_4D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_508")
    SetChrPos(0xE, 23530, 200, -2100, 0)
    OP_A2(0xA)
    Jump("loc_51C")

    label("loc_508")

    SetChrPos(0xE, 23530, 200, 400, 180)
    OP_A3(0xA)

    label("loc_51C")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 6)
    OP_A2(0x9)

    label("loc_529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C")
    SetChrFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B")
    SetChrPos(0xF, 23530, 200, -2100, 0)
    OP_A2(0xB)
    Jump("loc_56F")

    label("loc_55B")

    SetChrPos(0xF, 23530, 200, 400, 180)
    OP_A3(0xB)

    label("loc_56F")

    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 7)
    OP_A2(0x9)

    label("loc_57C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 23530, 200, 400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 17)
    OP_A2(0x9)

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5C1")
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_601")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_5DC")
    SetChrPos(0x16, 61080, 2000, 2170, 0)
    Jump("loc_601")

    label("loc_5DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5F0")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_601")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_601")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_601")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_643")
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x17, 23550, 200, 420, 180)

    label("loc_643")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrChipByIndex(0x18, 16)
    SetChrPos(0x18, 26270, 200, -480, 90)

    label("loc_670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69D")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 17)
    SetChrPos(0xA, 28530, 200, -570, 270)

    label("loc_69D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6CA")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 18)
    SetChrPos(0x11, 23550, 200, -2170, 0)

    label("loc_6CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6E0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_770")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6FF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_770")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_71E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_770")

    label("loc_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_734")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(1, 13)
    Jump("loc_770")

    label("loc_734")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_740"),
        (SWITCH_DEFAULT, "loc_770"),
    )


    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_758")
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_76D")

    label("loc_758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D")
    SetMapFlags(0x10000000)
    Event(0, 19)

    label("loc_76D")

    Jump("loc_770")

    label("loc_770")

    Return()

    # Function_0_482 end

    def Function_1_771(): pass

    label("Function_1_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 4)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B9")
    OP_44(0x15, 0x0)
    SetChrFlags(0x15, 0x10)
    OP_51(0x15, 0x1, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B9")

    Return()

    # Function_1_771 end

    def Function_2_7BA(): pass

    label("Function_2_7BA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_7EB"),
        (1, "loc_7F7"),
        (2, "loc_803"),
        (3, "loc_80F"),
        (4, "loc_81B"),
        (5, "loc_827"),
        (6, "loc_833"),
        (SWITCH_DEFAULT, "loc_83F"),
    )


    label("loc_7EB")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_84B")

    label("loc_7F7")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_84B")

    label("loc_803")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_84B")

    label("loc_80F")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_84B")

    label("loc_81B")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_84B")

    label("loc_827")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_84B")

    label("loc_833")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_84B")

    label("loc_83F")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_84B")

    label("loc_84B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_860")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_84B")

    label("loc_860")

    Return()

    # Function_2_7BA end

    def Function_3_861(): pass

    label("Function_3_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_88E")

    label("loc_868")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88B")
    OP_8D(0xFE, 58120, 52460, 56040, 51120, 3000)
    Jump("loc_868")

    label("loc_88B")

    Jump("loc_8B1")

    label("loc_88E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B1")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("loc_88E")

    label("loc_8B1")

    Return()

    # Function_3_861 end

    def Function_4_8B2(): pass

    label("Function_4_8B2")

    Call(0, 5)
    Return()

    # Function_4_8B2 end

    def Function_5_8B7(): pass

    label("Function_5_8B7")

    TalkBegin(0x12)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    OP_A9(0x9E)
    Jump("loc_8DE")

    label("loc_8DC")

    OP_A9(0x98)

    label("loc_8DE")

    TalkEnd(0x12)
    Return()

    label("loc_8E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F6")
    TalkEnd(0x12)
    Return()

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E9")

    ChrTalk(    #0
        0x12,
        (
            "不久前中央工房的人\x01",
            "来买油灯的灯油呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        (
            "那里原本装设的全是导力灯，\x01",
            "这下可就麻烦了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x12,
        (
            "多亏他们制造了夜视眼镜，\x01",
            "戴上之后就可以通过漆黑的卡鲁迪亚隧道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12,
        (
            "拐弯抹角的话就不多说了，\x01",
            "总之我就是在推销而已啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A67")

    label("loc_9E9")


    ChrTalk(    #4
        0x12,
        (
            "卡鲁迪亚隧道现在一团漆黑，\x01",
            "想走那里的话一定要买夜视眼镜才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x12,
        (
            "这是中央工房的特制产品，\x01",
            "戴上之后可以在黑暗中看东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A67")

    Jump("loc_FBC")

    label("loc_A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4B")

    ChrTalk(    #6
        0x12,
        (
            "呀，欢迎。\x01",
            "欢迎光临贝尔杂货店～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "大家好像遇到了麻烦吧，\x01",
            "从早上开始客人就一直不断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x12,
        (
            "听说卡鲁迪亚隧道现在漆黑一团，\x01",
            "不过只要戴上这眼镜就ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "要是想去卢安的话\x01",
            "这个东西是一定要买的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_BF4")

    label("loc_B4B")


    ChrTalk(    #10
        0x12,
        (
            "大家好像遇到了什么麻烦，\x01",
            "从早上开始客人就一直不断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "听说卡鲁迪亚隧道现在漆黑一团，\x01",
            "不过只要戴上这眼镜就ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        (
            "要是想去卢安的话\x01",
            "这个东西是一定要买的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF4")

    Jump("loc_FBC")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C4A")

    ChrTalk(    #13
        0x12,
        "听说地震不会再来了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        "中央工房发表的声明是不会骗人的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAF")

    label("loc_C4A")


    ChrTalk(    #15
        0x12,
        (
            "啊，你好。\x01",
            "欢迎光临贝尔杂货店～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "听说已经不会再有地震了，\x01",
            "这样的话就可以放心去买东西了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CAF")

    Jump("loc_FBC")

    label("loc_CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D3E")

    ChrTalk(    #17
        0x12,
        (
            "我老婆去礼拜堂\x01",
            "找药去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "不过今天怎么回来这么晚啊。\x01",
            "难道还有其他别的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "每次去都是很快\x01",
            "就回来了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEF")

    label("loc_D3E")


    ChrTalk(    #20
        0x12,
        (
            "我老婆\x01",
            "经常去礼拜堂呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        (
            "她一直有肩酸的毛病，\x01",
            "所以要去找教区长领取药品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "不过，说起来的话……\x01",
            "今天回来得好像比平时晚不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "每次去都是很快\x01",
            "就回来了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DEF")

    Jump("loc_FBC")

    label("loc_DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_F03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E68")

    ChrTalk(    #24
        0x12,
        (
            "工房遭遇袭击的事件\x01",
            "到现在我仿佛还历历在目呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        (
            "那次的事件\x01",
            "在当时可是改变了我们\x01",
            "的想法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F00")

    label("loc_E68")


    ChrTalk(    #26
        0x12,
        (
            "以前我和妻子经常会因为经营方针的不和\x01",
            "而产生冲突矛盾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        (
            "但工房遭到袭击后\x01",
            "我们就再也没吵过架。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "我们今后的目标是要经营\x01",
            "两个人共同的店铺。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F00")

    Jump("loc_FBC")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F67")

    ChrTalk(    #29
        0x12,
        "我们这里的东西可以说是应有尽有。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "不管食材还是日用品，\x01",
            "你想找的都能找到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_F67")


    ChrTalk(    #31
        0x12,
        (
            "呀，欢迎。\x01",
            "欢迎光临贝尔杂货店～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        (
            "我是不会输给地震的，\x01",
            "今天也要照常营业！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FBC")

    TalkEnd(0x12)
    Return()

    # Function_5_8B7 end

    def Function_6_FC0(): pass

    label("Function_6_FC0")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_10C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1065")

    ChrTalk(    #33
        0xFE,
        (
            "导力器无法运转了，\x01",
            "家务事也变得很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "要是再不去拿治疗肩膀的药\x01",
            "可就快撑不下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "呼，真想去亚尔摩温泉\x01",
            "好好泡个热水澡啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_10BD")

    label("loc_1065")


    ChrTalk(    #36
        0xFE,
        (
            "家务活真是累人，\x01",
            "肩膀都快疼死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "再不早点去礼拜堂拿药的话\x01",
            "可就要撑不下去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BD")

    Jump("loc_1364")

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1199")

    ChrTalk(    #38
        0xFE,
        (
            "很多平时不常用的东西最近卖得很好，\x01",
            "让我赚了不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "不过，那也就意味着\x01",
            "大家遇到了什么困难吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "要是一直这样下去的话\x01",
            "我这里也就不是杂货店了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "希望中央工房的人\x01",
            "能早点解决危机。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_11F5")

    label("loc_1199")


    ChrTalk(    #42
        0xFE,
        (
            "要是一直这样下去的话\x01",
            "我这里也就不是杂货店了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "希望中央工房的人\x01",
            "能早点解决危机。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F5")

    Jump("loc_1364")

    label("loc_11F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_124A")

    ChrTalk(    #44
        0xFE,
        "听说地震已经不会再来了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "果然在礼拜堂祈祷\x01",
            "是有用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128D")

    label("loc_124A")


    ChrTalk(    #46
        0xFE,
        "听说地震已经不会再来了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "呵呵呵，祈祷也是有用的啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_128D")

    Jump("loc_1364")

    label("loc_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12FD")

    ChrTalk(    #48
        0xFE,
        (
            "接下来还要去找教区长\x01",
            "拿治疗肩膀的药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "希望地震别再来了，\x01",
            "我今天也有虔诚地祈祷呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1364")

    label("loc_12FD")


    ChrTalk(    #50
        0xFE,
        "希望地震别再来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "总觉得地震还会再来，\x01",
            "实在安心不下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "今天还是继续\x01",
            "祈祷比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1364")

    TalkEnd(0x14)
    Return()

    # Function_6_FC0 end

    def Function_7_1368(): pass

    label("Function_7_1368")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14CD")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #53
        0xFE,
        "嘿～提妲姐姐～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "现在的情况\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x107,
        (
            "#063F嗯～抱歉…\x02\x03",

            "姐姐我们\x01",
            "现在还在调查中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "哎～是吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        (
            "#060F嗯，所以请再\x01",
            "稍等一下。\x02\x03",

            "姐姐我们一定\x01",
            "会让一切都恢复原样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "嗯～～我明白了。\x01",
            "一言为定哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "那好吧～\x01",
            "到时还要一起\x01",
            "玩上次的游戏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x107,
        (
            "#067F嗯、嗯，没问题。\x01",
            "（到、到底是什么游戏呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20C1)
    Jump("loc_1656")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151C")

    ChrTalk(    #61
        0xFE,
        (
            "那……下次还要\x01",
            "一起玩以前的\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "游戏哦，\x01",
            "提妲姐姐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1656")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_155C")

    ChrTalk(    #63
        0xFE,
        (
            "妈妈的肩膀\x01",
            "又开始疼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "是因为太\x01",
            "劳累了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1656")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(    #65
        0xFE,
        (
            "哎～看啊看啊～\x01",
            "是新游戏呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "我想出来的……\x01",
            "嘿～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    Sleep(500)

    ChrTalk(    #67
        0xFE,
        "冲啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "砰………………………！！\x02",
    )

    CloseMessageWindow()
    OP_44(0xFE, 0x0)
    SetChrFlags(0xFE, 0x10)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x13)
    OP_A2(0x2)
    Jump("loc_1656")

    label("loc_1601")


    ChrTalk(    #69
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "……………………………………\x01",
            "（在干什么啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1656")

    Jump("loc_190A")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16B4")

    ChrTalk(    #71
        0xFE,
        (
            "啊～可是这样的话\x01",
            "会让哥哥生气的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "……嗯，果然还是\x01",
            "不应该来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E5")

    label("loc_16B4")


    ChrTalk(    #73
        0xFE,
        "哎？还是没有地震吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "我还很期待呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_16E5")

    Jump("loc_190A")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_177E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1738")

    ChrTalk(    #75
        0xFE,
        (
            "嗯～今天\x01",
            "妈妈回来得好晚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "平时这时候都已经回来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_177B")

    label("loc_1738")


    ChrTalk(    #77
        0xFE,
        (
            "嗯～今天\x01",
            "妈妈回来得好晚啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "为什么到\x01",
            "现在还不回来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_177B")

    Jump("loc_190A")

    label("loc_177E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_189A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17D8")

    ChrTalk(    #79
        0xFE,
        (
            "啊～地震快点\x01",
            "来吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17AB():
        OP_9E(0xFE, 0x1E, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_17AB)

    ChrTalk(    #80
        0xFE,
        "哇～～来了来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1893")

    label("loc_17D8")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #81
        0xFE,
        "啊～提妲姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "地震来了～地震来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        (
            "#064F地震来了？\x02\x03",

            "是在假装地震吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "是呀～～\x02",
    )

    CloseMessageWindow()

    def lambda_185A():
        OP_9E(0xFE, 0x1E, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_185A)

    ChrTalk(    #85
        0xFE,
        "轰隆隆隆～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "哇～是地震！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1893")

    OP_44(0xFE, 0x1)
    Jump("loc_190A")

    label("loc_189A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_18D8")

    ChrTalk(    #87
        0xFE,
        (
            "妈妈\x01",
            "去礼拜堂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "好像是去找教区长\x01",
            "拿药。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(    #89
        0xFE,
        (
            "我在玩地震\x01",
            "的游戏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "要一起玩吗？\x02",
    )

    CloseMessageWindow()

    label("loc_190A")

    TalkEnd(0x15)
    Return()

    # Function_7_1368 end

    def Function_8_190E(): pass

    label("Function_8_190E")

    Call(0, 9)
    Return()

    # Function_8_190E end

    def Function_9_1913(): pass

    label("Function_9_1913")

    TalkBegin(0x13)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1941")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1938")
    OP_A9(0xA9)
    Jump("loc_193A")

    label("loc_1938")

    OP_A9(0x97)

    label("loc_193A")

    TalkEnd(0x13)
    Return()

    label("loc_1941")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1952")
    TalkEnd(0x13)
    Return()

    label("loc_1952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EA")

    ChrTalk(    #91
        0x13,
        (
            "我的店本来是以贩卖枪类武器\x01",
            "为主的，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x13,
        (
            "这次也进了不少\x01",
            "近战型的武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x13,
        (
            "虽然不想这样……\x01",
            "但现在这种情况也没办法。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1A4A")

    label("loc_19EA")


    ChrTalk(    #94
        0x13,
        (
            "枪炮类的武器无法使用，\x01",
            "只能进些近战武器了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x13,
        (
            "虽然不想这样……\x01",
            "但现在这种情况也没办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4A")

    Jump("loc_2113")

    label("loc_1A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B36")

    ChrTalk(    #96
        0x13,
        (
            "真没办法啊……\x01",
            "本来我们是主营业导力炮的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x13,
        (
            "因为最近的这一系列异变\x01",
            "销售量直线下降，已经严重赤字了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "中央工房的那些家伙\x01",
            "到底在做什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x13,
        (
            "我们的生活已经严重受影响了，\x01",
            "研究者们还是危机意识不足啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1BA0")

    label("loc_1B36")


    ChrTalk(    #100
        0x13,
        (
            "中央工房的那些家伙\x01",
            "到底在做什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x13,
        (
            "理论研究等东西都无所谓，\x01",
            "现在最关键的是要调查出异变的原因。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA0")

    Jump("loc_2113")

    label("loc_1BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1D4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(    #102
        0x13,
        (
            "帝国莱恩福尔特社和\x01",
            "共和国的乌尔努社……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x13,
        (
            "这两家是目前最大的\x01",
            "导力枪制造商。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x13,
        (
            "当然了！我们蔡斯中央工房\x01",
            "的技术力也是不会输给他们的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x13,
        (
            "总有一天会让ＺＣＦ的标志\x01",
            "变成世界最强的象征。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_1C76")


    ChrTalk(    #106
        0x13,
        (
            "说起来的话，再过不久\x01",
            "就是互不侵犯条约的签字仪式了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x13,
        (
            "我们和帝国的枪械制造社\x01",
            "也都有往来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x13,
        (
            "哟，帝国的莱恩福尔特社，\x01",
            "你们应该也听说过吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x13,
        (
            "嗯，那里并不只是生产枪械，\x01",
            "连战车也都有制造。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D47")

    Jump("loc_2113")

    label("loc_1D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1DCB")

    ChrTalk(    #110
        0x13,
        (
            "虽然还在开发中，但斯坦因先生\x01",
            "可是很重视的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x13,
        (
            "如果遇到技术高超的专业人士，\x01",
            "一定可以学到有用的枪械知识。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E94")

    label("loc_1DCB")


    ChrTalk(    #112
        0x13,
        (
            "不久前斯坦因先生给我看了\x01",
            "开发中的新型枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x13,
        (
            "那种型号很罕见，\x01",
            "我非常喜欢呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x13,
        (
            "经过足够的测试之后\x01",
            "相信一定很快就能流行起来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x13,
        (
            "斯坦因先生对它也是赞美有加。\x01",
            "一定可以学到有用的枪械知识。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1E94")

    Jump("loc_2113")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1EEF")

    ChrTalk(    #116
        0x13,
        (
            "斯坦因先生虽然技术高超\x01",
            "但却不太好相处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x13,
        "真是苦了技术员们啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F89")

    label("loc_1EEF")


    ChrTalk(    #118
        0x13,
        (
            "这家店的主人\x01",
            "就是斯坦因先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x13,
        (
            "虽然他有些倔强，\x01",
            "但对武器的见解还是很强的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x13,
        (
            "总之是个技术高超\x01",
            "却不太好相处的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x13,
        "真是苦了技术员们啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1F89")

    Jump("loc_2113")

    label("loc_1F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2048")

    ChrTalk(    #122
        0x13,
        (
            "虽然被地震吓了一跳，\x01",
            "但是我并不在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x13,
        (
            "所谓的地震，本来就是周期性的\x01",
            "普通自然现象而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x13,
        (
            "我们作为受过良好教育的工房都市居民，\x01",
            "遇到这种情况时自然应该保持冷静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_2048")


    ChrTalk(    #125
        0x13,
        (
            "哟，欢迎光临。\x01",
            "欢迎光临斯坦因武器店，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x13,
        (
            "虽然被地震吓了一跳，\x01",
            "但是我并不在意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x13,
        (
            "那只是再普通不过的\x01",
            "自然现象而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x13,
        (
            "我们作为受过良好教育的工房都市居民，\x01",
            "遇到这种情况时自然应该保持冷静。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2113")

    TalkEnd(0x13)
    Return()

    # Function_9_1913 end

    def Function_10_2117(): pass

    label("Function_10_2117")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_286D")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(2920, 0, 700, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(315000, 0)
    OP_6E(332, 0)
    SetChrPos(0x101, 4360, 0, -720, 0)
    SetChrPos(0x102, 3220, 0, -700, 0)
    SetChrPos(0xF8, 4600, 0, -1800, 0)
    SetChrPos(0xF9, 3230, 0, -1800, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_END)), "loc_22F4")

    ChrTalk(    #129
        0x8,
        (
            "#790F你们还是和以前一样忙，\x01",
            "整天到处跑啊。\x02\x03",

            "啊，温泉的水泵\x01",
            "已经修好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1001F#4P嗯，已经修好了……\x02\x03",

            "#1015F……嗯，总之先来\x01",
            "做个正式的报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        "#1040F#1P那么，先做个报告吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #132
        (
            "\x07\x05将亚尔摩温泉的水泵\x01",
            "已经修理好的情况做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #133
        0x8,
        (
            "#790F呵呵，看来比想象中的\x01",
            "还麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240C")

    label("loc_22F4")


    ChrTalk(    #134
        0x8,
        (
            "#790F听工房长说过了，\x01",
            "好像很忙的样子呢。\x02\x03",

            "发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1011F#4P啊，是啊是啊。\x01",
            "要报告一下才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#1035F#1P嗯嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #137
        (
            "\x07\x05将亚尔摩温泉的水泵\x01",
            "已经修理好的情况做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #138
        0x8,
        (
            "#790F呼呼～原来如此。\x02\x03",

            "果然是游击士\x01",
            "要做的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240C")


    ChrTalk(    #139
        0x101,
        (
            "#1015F#4P嗯，在这种非常时期\x01",
            "似乎有点过于悠闲了呢……\x02\x03",

            "#1002F不过，遇到有困难的人\x01",
            "总没有办法坐视不管。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24CA")

    ChrTalk(    #140
        0x108,
        (
            "#070F啊啊，那也正是\x01",
            "游击士的精神啊，\x02\x03",

            "我认为这是正确的判断。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256A")

    label("loc_24CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_251D")

    ChrTalk(    #141
        0x106,
        (
            "#051F啊啊～那也正是\x01",
            "游击士的精神啦。\x02\x03",

            "我认为这是正确的判断。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256A")

    label("loc_251D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256A")

    ChrTalk(    #142
        0x103,
        (
            "#020F嗯，那也正是游击士的精神啊。\x02\x03",

            "我认为这是正确的判断。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256A")


    ChrTalk(    #143
        0x8,
        (
            "#792F协会规章第二项……\x01",
            "以保护市民为原则。\x02\x03",

            "以那种精神来判定的话，\x01",
            "你们的决断自然是正确的。\x02\x03",

            "#791F你们做的很好，\x01",
            "很值得自豪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1008F#4P嘿嘿嘿，谢谢啦。\x02\x03",

            "被雾香小姐这么一说，\x01",
            "一下子就有自信了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#1040F#1P……报告就这么多。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC2, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_2666")
    OP_A2(0x10)
    Jump("loc_2669")

    label("loc_2666")

    OP_A3(0x10)

    label("loc_2669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2723")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇地方任务未报告（QF_REPORT不成立）】\x01",        # 0
            "【◇在其他支部报告完毕（QF_REPORT成立）】\x01",      # 1
            "【◇不变更】\x01",                                   # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2717"),
        (1, "loc_271D"),
        (SWITCH_DEFAULT, "loc_2723"),
    )


    label("loc_2717")

    OP_A3(0x10)
    Jump("loc_2723")

    label("loc_271D")

    OP_A2(0x10)
    Jump("loc_2723")

    label("loc_2723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D2")

    ChrTalk(    #146
        0x8,
        (
            "#790F那么，接下来我们\x01",
            "马上就会去核查。\x02\x03",

            "要想收取报酬的话，\x01",
            "请重新选择『报告』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#1011F#4P在领取报酬的时候\x01",
            "再来报告就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        "#790F嗯，那就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2864")

    label("loc_27D2")


    ChrTalk(    #149
        0x8,
        (
            "#790F核查已经结束了，\x01",
            "这件事也算是告一段落。\x02\x03",

            "那么，各位今后\x01",
            "也要小心行事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1006F#4P嗯，了解。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        (
            "#1040F#1P是的……\x01",
            "那就先失礼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2864")

    OP_A2(0x20C7)
    EventEnd(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_286D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28D9")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "报告\x01",            # 1
            "有关招牌板\x01",      # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_29E8")

    label("loc_28D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2982")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2944")

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "报告\x01",            # 1
            "呼叫同伴\x01",        # 2
            "向要塞询问\x01",      # 3
            "离开\x01",            # 4
        )
    )

    Jump("loc_2967")

    label("loc_2944")


    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "报告\x01",            # 1
            "向要塞询问\x01",      # 2
            "离开\x01",            # 3
        )
    )


    label("loc_2967")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_29E1")

    label("loc_2982")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29DD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "报告\x01",          # 1
            "呼叫同伴\x01",      # 2
            "离开\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_29E1")

    label("loc_29DD")

    Call(6, 5)

    label("loc_29E1")

    Jump("loc_29E8")

    label("loc_29E4")

    Call(6, 5)

    label("loc_29E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BBF")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x85, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x85, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AAB")

    ChrTalk(    #152
        0x8,
        (
            "#790F辛苦了。\x02\x03",

            "之前一系列调查的报酬\x01",
            "已经给你们准备好了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_AF(0x9A, 0x85)
    Sleep(100)
    OP_28(0x86, 0x4, 0x20)
    OP_28(0x87, 0x4, 0x20)

    ChrTalk(    #153
        0x8,
        (
            "#790F去亚尔摩村之前\x01",
            "最好先好好整备一下装备。\x02\x03",

            "总之，请小心行事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB6")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B12")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x9A)

    ChrTalk(    #154
        0x8,
        (
            "#790F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB6")

    label("loc_2B12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x9A)"), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(    #155
        0x8,
        (
            "#790F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB6")

    label("loc_2B67")


    ChrTalk(    #156
        0x8,
        (
            "#790F啊，现在\x01",
            "好像没有可以报告的工作吧。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB6")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_2BBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_2BF8")
    Call(1, 12)
    Jump("loc_2C0F")

    label("loc_2BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0B")
    Call(1, 9)
    Jump("loc_2C0F")

    label("loc_2C0B")

    Call(1, 10)

    label("loc_2C0F")

    TalkEnd(0x8)
    Jump("loc_2CEF")

    label("loc_2C15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CBF")

    ChrTalk(    #157
        0x8,
        (
            "#790F要呼叫同伴吗。\x02\x03",

            "了解。\x01",
            "马上就和他们进行联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #158
        (
            "\x07\x05联络各支部，\x01",
            "集合了待命人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    TalkEnd(0x8)
    Jump("loc_2CEF")

    label("loc_2CBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CE6")
    Call(0, 37)
    TalkEnd(0x8)
    Jump("loc_2CE9")

    label("loc_2CE6")

    TalkEnd(0x8)

    label("loc_2CE9")

    Jump("loc_2CEF")

    label("loc_2CEC")

    TalkEnd(0x8)

    label("loc_2CEF")

    Return()

    label("loc_2CF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D25")
    Call(0, 37)
    TalkEnd(0x8)
    Return()

    label("loc_2D25")

    TalkEnd(0x8)
    Return()

    label("loc_2D2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3D")
    TalkEnd(0x8)
    Return()

    label("loc_2D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2DDC")

    ChrTalk(    #159
        0x8,
        (
            "#790F水泵的修理辛苦你们了。\x02\x03",

            "虽然是平凡的小事，\x01",
            "但对游击士来说却也是重要的任务哦。\x02\x03",

            "用心解决市民的每个困难，\x01",
            "身为游击士，应该把这句话牢记在心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C20")

    label("loc_2DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F84")

    ChrTalk(    #160
        0x8,
        "#790F内燃引擎已经拿到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1006F嗯，总算是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x102,
        (
            "#1040F顺利借到了。\x02\x03",

            "警备艇上的各位士兵\x01",
            "好像也没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "#790F是吗，那可是好消息。\x02\x03",

            "要塞那边就由我来\x01",
            "通知就可以了。\x02\x03",

            "你们就继续去忙\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1040F明白。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F16")

    ChrTalk(    #165
        0x107,
        (
            "#560F是、是的！\x01",
            "那么～我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2F16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3E")

    ChrTalk(    #166
        0x106,
        "#051F嗯，我们走。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F65")

    label("loc_2F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F65")

    ChrTalk(    #167
        0x108,
        "#070F嗯，那就走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2F65")


    ChrTalk(    #168
        0x8,
        "#790F一定要小心哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2FDD")

    label("loc_2F84")


    ChrTalk(    #169
        0x8,
        (
            "#790F警备艇的事情\x01",
            "让我来报告给他们就可以了。\x02\x03",

            "你们就继续去忙\x01",
            "你们继续忙自己的事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FDD")

    Jump("loc_3212")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_END)), "loc_3063")

    ChrTalk(    #170
        0x8,
        (
            "#790F听说内燃引擎被装载在迫降在\x01",
            "托兰特平原的警备艇上。\x02\x03",

            "你们也只有去托兰特平原搜索一下，\x01",
            "和他们的负责人交涉一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_3063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_END)), "loc_3212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_END)), "loc_30D9")

    ChrTalk(    #171
        0x8,
        (
            "#790F从刚才的联络来看，\x01",
            "似乎不用马上就出发。\x02\x03",

            "如果你们以后正好路过王都的话\x01",
            "顺便去看看就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_30D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3196")

    ChrTalk(    #172
        0x8,
        (
            "#790F因为在雷斯顿要塞附近，\x01",
            "所以治安方面应该不成问题。\x02\x03",

            "就检查一下告示板，\x01",
            "之后确认一下中央工房和\x01",
            "亚尔摩温泉的状况就可以了。\x02\x03",

            "现在联系困难，\x01",
            "也许会遇到什么麻烦也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3212")

    label("loc_3196")


    ChrTalk(    #173
        0x8,
        (
            "#790F就检查一下告示板，\x01",
            "之后确认一下中央工房和\x01",
            "亚尔摩温泉的状况就可以了。\x02\x03",

            "现在联系困难，\x01",
            "也许会遇到什么麻烦也说不定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3212")

    Jump("loc_3C20")

    label("loc_3215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_36B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_327F")

    ChrTalk(    #174
        0x8,
        (
            "#790F有关古代遗物，\x01",
            "目前还有很多未解之处。\x02\x03",

            "希望从这次的发现中\x01",
            "可以找到什么线索……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B6")

    label("loc_327F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3360")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3312")

    ChrTalk(    #175
        0x8,
        (
            "#790F今后他们很有可能\x01",
            "会再次出现，\x02\x03",

            "即使到了王都也要小心行动啊。\x02\x03",

            "愿女神保佑诸位。\x01",
            "请一路小心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_335D")

    label("loc_3312")


    ChrTalk(    #176
        0x8,
        (
            "#790F王都的艾南先生\x01",
            "就由我来联络吧。\x02\x03",

            "愿女神保佑诸位。\x01",
            "请一路小心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335D")

    Jump("loc_36B6")

    label("loc_3360")


    ChrTalk(    #177
        0x8,
        (
            "#792F说起来的话，已经注意到了吗？\x02\x03",

            "协会的招牌板……\x01",
            "已经顺利找回了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #178
        0x101,
        "#1004F那块招牌板已经找到了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #179
        0x8,
        (
            "#790F是中央工房的菲小姐\x01",
            "帮忙找到的。\x02\x03",

            "不知是怎么回事，\x01",
            "竟然被人运送到了地下仓库\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1020F地、地下仓库～！？\x02\x03",

            "#1007F为什么会在那里……\x01",
            "这……有什么缘由吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_34EF")

    ChrTalk(    #181
        0x106,
        (
            "#551F大概是那家伙干的吧。\x02\x03",

            "虽然不知道他是怎么做到的，\x01",
            "但手段真是很厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_352F")

    label("loc_34EF")


    ChrTalk(    #182
        0x103,
        (
            "#025F嗯嗯，肯定是那个人\x01",
            "干的好事吧，\x02\x03",

            "真是个不得了的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352F")


    ChrTalk(    #183
        0x8,
        (
            "#792F事情就是这样，\x01",
            "所以那个委托也就撤消了。\x02\x03",

            "没有凭自己的实力夺回来，\x01",
            "总觉得有些遗憾呢……\x02\x03",

            "#790F今后他们很有可能\x01",
            "会再次出现，\x02\x03",

            "即使到了王都也要小心行动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3600")

    ChrTalk(    #184
        0x104,
        "#030F呼，这样也不错啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3640")

    label("loc_3600")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3626")

    ChrTalk(    #185
        0x107,
        "#062F是、是的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3640")

    label("loc_3626")


    ChrTalk(    #186
        0x101,
        "#1002F嗯……明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_3640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3665")

    ChrTalk(    #187
        0x106,
        "#050F啊啊，会小心的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_367C")

    label("loc_3665")


    ChrTalk(    #188
        0x103,
        "#020F嗯，了解啦。\x02",
    )

    CloseMessageWindow()

    label("loc_367C")


    ChrTalk(    #189
        0x8,
        (
            "#790F那么，愿女神守护诸位。\x02\x03",

            "请一路小心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_28(0x6C, 0x1, 0x4000)

    label("loc_36B6")

    Jump("loc_3C20")

    label("loc_36B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_373A")

    ChrTalk(    #190
        0x8,
        (
            "#790F那么，招牌板的搜查工作\x01",
            "也就一起交给你们了。\x02\x03",

            "并不是什么太紧急的任务，和地震的调查\x01",
            "相比起来就显得无关紧要了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C20")

    label("loc_373A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_38D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_379B")

    ChrTalk(    #191
        0x8,
        (
            "#790F竟然敢对雷斯顿要塞下手，\x01",
            "看来对手不是等闲之辈。\x02\x03",

            "你们一定不能大意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D6")

    label("loc_379B")


    ChrTalk(    #192
        0x8,
        (
            "#790F我听说了，\x01",
            "你们要去亚尔摩村对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        "#1016F啊，消息还是那么灵通～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x8,
        (
            "#790F海泽尔和我联系过了哦。\x02\x03",

            "竟然敢对雷斯顿要塞下手，\x01",
            "看来对手不是等闲之辈。\x02\x03",

            "……一定不要大意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3872")

    ChrTalk(    #195
        0x106,
        "#050F哈，那当然。\x02",
    )

    CloseMessageWindow()
    Jump("loc_388B")

    label("loc_3872")


    ChrTalk(    #196
        0x103,
        "#022F嗯嗯～明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_388B")


    ChrTalk(    #197
        0x8,
        (
            "#790F嗯，那就不用多说了。\x01",
            "好了，快去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1002F嗯，我们走了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_38D6")

    Jump("loc_3C20")

    label("loc_38D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3946")

    ChrTalk(    #199
        0x8,
        (
            "#790F测量仪已经设置完毕的话，\x01",
            "接下来就请去中央工房吧。\x02\x03",

            "我想博士应该在５层的\x01",
            "演算室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C20")

    label("loc_3946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_39CE")

    ChrTalk(    #200
        0x8,
        (
            "#790F测量仪的设置场所是\x01",
            "隧道中部、平原北部外围、\x01",
            "雷斯顿要塞前三个地方。\x02\x03",

            "必要的联络已经做过了，\x01",
            "请你们直接去现场调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C20")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A3C")

    ChrTalk(    #201
        0x8,
        (
            "#790F地震的调查\x01",
            "并不是紧急性的工作哦。\x02\x03",

            "一边完成告示板上的委托\x01",
            "一边抽空进行调查就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE0")

    label("loc_3A3C")


    ChrTalk(    #202
        0x8,
        (
            "#790F你们先去沃尔费堡垒\x01",
            "进行调查吧。\x02\x03",

            "蔡斯市内的情报收集工作\x01",
            "已经拜托过工房长先生了。\x01",
            "即使不去管也没关系。\x02\x03",

            "一边完成告示板上的委托\x01",
            "一边抽空进行调查就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3AE0")

    Jump("loc_3C20")

    label("loc_3AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_3C20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3B57")

    ChrTalk(    #203
        0x8,
        (
            "#790F地震的调查工作并不是很急，\x01",
            "慢慢进行也没关系的。\x02\x03",

            "先去拉赛尔工房\x01",
            "和博士他们打个招呼如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C20")

    label("loc_3B57")


    ChrTalk(    #204
        0x8,
        (
            "#790F你们先去沃尔费堡垒\x01",
            "进行调查吧。\x02\x03",

            "蔡斯市内的情报收集工作\x01",
            "已经拜托过工房长先生了。\x01",
            "即使不去管也没关系。\x02\x03",

            "一边完成告示板上的委托\x01",
            "慢慢进行也没关系哦。\x02\x03",

            "先去拉赛尔工房\x01",
            "和博士他们打个招呼如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3C20")

    TalkEnd(0x8)
    Return()

    # Function_10_2117 end

    def Function_11_3C24(): pass

    label("Function_11_3C24")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_3C31")
    OP_A2(0x5)

    label("loc_3C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CA7")
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
        (0, "loc_3C9B"),
        (1, "loc_3CA1"),
        (SWITCH_DEFAULT, "loc_3CA7"),
    )


    label("loc_3C9B")

    OP_A2(0x5)
    Jump("loc_3CA7")

    label("loc_3CA1")

    OP_A3(0x5)
    Jump("loc_3CA7")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3D1D")

    ChrTalk(    #205
        0xFE,
        (
            "冈多夫好像\x01",
            "马上就要回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "这种人手不足的情况\x01",
            "究竟要持续到什么时候呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D96")

    label("loc_3D1D")


    ChrTalk(    #207
        0xFE,
        (
            "前去王都的冈多夫\x01",
            "马上就要回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "终于快要卸下担子了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "不过这里的人手不足问题\x01",
            "究竟要持续到什么时候呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3D96")

    Jump("loc_3EC1")

    label("loc_3D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3DFA")

    ChrTalk(    #210
        0xFE,
        (
            "等修好之后\x01",
            "还要继续进行护卫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "导力器的输出工作\x01",
            "还是和以前一样顺利啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E51")

    label("loc_3DFA")


    ChrTalk(    #212
        0xFE,
        (
            "等修好之后\x01",
            "还要继续进行护卫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "最近出现了很多危险的魔兽，\x01",
            "也真是伤脑筋呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3E51")

    Jump("loc_3EC1")

    label("loc_3E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_3EC1")

    ChrTalk(    #214
        0xFE,
        (
            "可能的话，我也想\x01",
            "自己挑选工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "以后你们要是接到什么重要调查的话\x01",
            "也分配一些简单任务给我吧，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC1")

    Jump("loc_3F06")

    label("loc_3EC4")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #216
        0xFE,
        (
            "不好意思，\x01",
            "很想帮到你们一些忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "大家一起加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_3F06")

    Jump("loc_4458")

    label("loc_3F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_40C8")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4015")

    ChrTalk(    #218
        0xFE,
        "呀，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "还记得我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1001F当然记得啦！\x02\x03",

            "你不是蔡斯支部\x01",
            "的王吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "哈哈，谢谢，竟然还记得我。\x01",
            "能再次相遇真是高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "你终于顺利晋升为\x01",
            "正游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "恭喜！\x01",
            "凭你的实力，这也是理所当然的结果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40C5")

    label("loc_4015")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #224
        0xFE,
        "啊，这不是艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#1004F咦……？\x02\x03",

            "#1018F啊，我还说是谁，\x01",
            "这不是王吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "你终于顺利晋升为\x01",
            "正游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "恭喜！\x01",
            "凭你的实力，这也是理所当然的结果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C5")

    Jump("loc_4210")

    label("loc_40C8")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #228
        0xFE,
        "…………哎呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "你不就是…\x01",
            "最近才转正的艾丝蒂尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        "#1004F哎哎，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "啊，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "我是王。\x01",
            "蔡斯地区的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1000F啊～是吗。\x02\x03",

            "我是艾丝蒂尔·布莱特。\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "啊啊，请多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "你们的事情\x01",
            "我也早有耳闻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "真是立了大功啊，\x01",
            "升为正游击士也是理所当然的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4210")


    ChrTalk(    #237
        0x101,
        (
            "#1008F嘿嘿，谢谢夸奖。\x02\x03",

            "我们也还差得远呢，\x01",
            "还需要不断努力进步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "嗯…保持上进心，永不懈怠吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "这种谦虚的态度\x01",
            "我也要多多学习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "对了，冈多夫\x01",
            "出去办事了，你们知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "从嘉恩那里听说了。\x02\x03",

            "我们就是为了增援\x01",
            "才特意来蔡斯的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "是这样吗。\x01",
            "谢啦，真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "真是不好意思，\x01",
            "很想帮到你们一些忙。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_43C4")
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #244
        0xFE,
        (
            "阿加特前辈也一样……\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x106,
        "#051F哪里，也请你们多关照了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_441B")

    label("loc_43C4")

    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #246
        0xFE,
        (
            "雪拉扎德前辈也一样，\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x103,
        "#020F哪里的话，互相关照吧。\x02",
    )

    CloseMessageWindow()

    label("loc_441B")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #248
        0xFE,
        "我也竭尽全力哟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "那么，大家都加油吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1427)
    OP_A2(0x6)

    label("loc_4458")

    TalkEnd(0x16)
    Return()

    # Function_11_3C24 end

    def Function_12_445C(): pass

    label("Function_12_445C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_451E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D8")

    ChrTalk(    #250
        0xFE,
        (
            "好久没看见这个了，\x01",
            "油灯其实也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "虽然亮度不能和\x01",
            "导力灯相比……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "可是却很温暖呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_451B")

    label("loc_44D8")


    ChrTalk(    #253
        0xFE,
        (
            "好久没看见这个了，\x01",
            "油灯其实也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "让人感觉很温暖呢。\x02",
    )

    CloseMessageWindow()

    label("loc_451B")

    Jump("loc_4607")

    label("loc_451E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BF")

    ChrTalk(    #255
        0xFE,
        (
            "今天是为了购买油灯\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "买这种东西果然\x01",
            "简单多了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "买水果和面包的时候\x01",
            "总是给我提『买看起来好吃的』\x01",
            "这种含糊不清的要求。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_4607")

    label("loc_45BF")


    ChrTalk(    #258
        0xFE,
        (
            "今天是为了购买油灯\x01",
            "而过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "果然还是买工业制品\x01",
            "简单多了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4607")

    TalkEnd(0xFE)
    Return()

    # Function_12_445C end

    def Function_13_460B(): pass

    label("Function_13_460B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_461C")
    Call(0, 38)

    label("loc_461C")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 5230, 0, 2029, 0)
    SetChrPos(0x101, 2240, 0, -5100, 0)
    SetChrPos(0xF7, 1230, 0, -5230, 0)
    SetChrPos(0x105, 2170, 0, -6120, 0)
    SetChrPos(0x104, 1010, 0, -6200, 0)
    OP_6D(5230, 0, 2029, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    OP_6D(2240, 0, -5100, 0)
    OP_69(0x8, 0x0)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #260
        0x8,
        (
            "#792F嗯，中央工房\x01",
            "没有受到损害……\x02\x03",

            "#791F市区也没出什么大事，\x01",
            "可以放心了。\x02\x03",

            "嗯，有关那件事\x01",
            "就拜托你们了。\x02\x03",

            "那么先这样。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(800)

    ChrTalk(    #261
        0x8,
        (
            "#792F呵呵……\x01",
            "来得还真是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47E4():
        OP_6D(2450, 0, -1640, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47E4)

    def lambda_47FC():
        OP_67(0, 6000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_47FC)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4972")

    ChrTalk(    #262
        0x8,
        (
            "#791F#2P你们终于到了啊。\x01",
            "艾丝蒂尔，阿加特。\x02\x03",

            "在飞船坪那里吓了一跳吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        (
            "#1016F#6P啊、啊哈哈……\x01",
            "好久不见啦，雾香姐。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48B0():
        OP_6D(3350, 0, 330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48B0)

    def lambda_48C8():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_48C8)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(250)
    OP_43(0x8, 0x1, 0x0, 0x12)
    Sleep(250)
    OP_43(0xF7, 0x1, 0x0, 0xF)
    Sleep(250)
    OP_43(0x105, 0x1, 0x0, 0x10)
    Sleep(250)
    OP_43(0x104, 0x1, 0x0, 0x11)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #264
        0x106,
        (
            "#051F#6P哼，还是和从前一样，\x01",
            "什么事情都能料到啊……\x02\x03",

            "算啦，总之请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB8")

    label("loc_4972")


    ChrTalk(    #265
        0x8,
        (
            "#791F#2P你们终于到了啊。\x01",
            "艾丝蒂尔，雪拉扎德。\x02\x03",

            "在飞船坪那里吓了一跳吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        (
            "#1016F#6P啊、啊哈哈……\x01",
            "好久不见啦，雾香姐。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49F7():
        OP_6D(3550, 0, 330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49F7)

    def lambda_4A0F():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4A0F)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(250)
    OP_43(0x8, 0x1, 0x0, 0x12)
    Sleep(250)
    OP_43(0xF7, 0x1, 0x0, 0xF)
    Sleep(250)
    OP_43(0x105, 0x1, 0x0, 0x10)
    Sleep(250)
    OP_43(0x104, 0x1, 0x0, 0x11)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #267
        0x103,
        (
            "#021F#6P呵呵，还是和以前一样，\x01",
            "什么都被你料到了啊。\x02\x03",

            "#020F雾香。\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB8")


    ChrTalk(    #268
        0x8,
        (
            "#791F你们能来也是帮我大忙了。\x02\x03",

            "嗯，站在那边的两位就是\x01",
            "公主殿下和奥利维尔先生了吧。\x02\x03",

            "我叫雾香。\x01",
            "是蔡斯支部的负责人。\x02\x03",

            "以后还请多多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x105,
        (
            "#048F#6P是的，彼此彼此。\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #270
        0x104,
        (
            "#037F#6P呼，真是比想象中\x01",
            "更美丽的佳人啊。\x02\x03",

            "请允许我奥利维尔为你\x01",
            "献上一首即兴之曲吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x8,
        (
            "#791F听嘉恩说，你们已经是\x01",
            "正式的协力者了对吧？\x02\x03",

            "协力者同游击士一样，\x01",
            "可以自由使用楼上的休息室。\x02\x03",

            "也可以在那里进行约见会谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x105,
        "#041F#6P是，我们知道了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #273
        0x104,
        "#036F#6P啊～我的即兴之曲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x8,
        (
            "#792F想弹奏鲁特琴的话\x01",
            "可以去楼上的休息室。\x02\x03",

            "但请在常识的范围内进行演奏。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #275
        0x104,
        "#034F#6P呜……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#1016F#6P（比起雪拉姐…\x01",
            "真是一点情面也不留啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4DCC")

    ChrTalk(    #277
        0x106,
        (
            "#551F#6P哈，那么……\x02\x03",

            "#051F还是快点把工作的状况\x01",
            "说给我们听听吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E1F")

    label("loc_4DCC")


    ChrTalk(    #278
        0x103,
        (
            "#021F#6P好啦，这个笨蛋\x01",
            "就不用管他了……\x02\x03",

            "#020F还是先把工作的情况\x01",
            "告诉我们吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E1F")


    ChrTalk(    #279
        0x8,
        (
            "#792F告示板上确实是积攒了不少委托，\x01",
            "不过都不是什么太紧急的工作。\x02\x03",

            "凭你们的能力\x01",
            "很容易就可以解决了……\x02\x03",

            "#790F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1004F#6P？？？\x02\x03",

            "你怎么了？雾香姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x8,
        (
            "#791F这个不是普通的委托，\x01",
            "而是协会的直接请求……\x02\x03",

            "希望你们可以对『结社』\x01",
            "展开调查。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4FB1")

    ChrTalk(    #282
        0x106,
        "#057F#6P什么……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FCD")

    label("loc_4FB1")


    ChrTalk(    #283
        0x103,
        "#022F#6P怎么回事……？\x02",
    )

    CloseMessageWindow()

    label("loc_4FCD")


    ChrTalk(    #284
        0x101,
        "#1002F#6P还、还真是单刀直入啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x105,
        (
            "#043F#6P那个……\x01",
            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x8,
        (
            "#790F想让你们调查的事，\x02\x03",

            "就是刚才发生的『地震』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        (
            "#1015F#6P调查地震？\x02\x03",

            "是去向大家询问\x01",
            "受害程度吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#792F那当然也包括在内……\x02\x03",

            "其实在３天前，沃尔费堡垒\x01",
            "也发生过同样的地震。\x02\x03",

            "时间好像在１０秒左右，\x01",
            "听说没有出现什么受害状况。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5144")

    ChrTalk(    #289
        0x106,
        (
            "#552F#6P原来如此……\x01",
            "和刚才的地震和相似啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5175")

    label("loc_5144")


    ChrTalk(    #290
        0x103,
        (
            "#522F#6P原来如此……\x01",
            "和刚才的地震很相似呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5175")


    ChrTalk(    #291
        0x8,
        (
            "#790F奇怪的现象还有一个。\x02\x03",

            "在沃尔费堡垒发生地震的时候，\x01",
            "蔡斯市却完全没有任何摇晃。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #292
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x104,
        (
            "#032F#6P嗯，那真是很奇怪。\x02\x03",

            "从地图上看，沃尔费堡垒\x01",
            "离这里并不算远。\x02\x03",

            "那里如果发生了地震，这边\x01",
            "多少也应该能感觉到摇晃才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#790F也有可能是因为震级较低，\x01",
            "所以没有注意到。\x02\x03",

            "#792F只是，嗯……\x01",
            "可能是直觉的判断吧，\x02\x03",

            "我总有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1007F#6P我明白你的意思了……\x02\x03",

            "#1002F幽灵事件也是如此，\x01",
            "这种奇异的现象我也是很在意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_53A5")

    ChrTalk(    #296
        0x106,
        (
            "#051F#6P好！我们接受了。\x02\x03",

            "那就先在蔡斯市和沃尔费堡垒\x01",
            "两个地方进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5402")

    label("loc_53A5")


    ChrTalk(    #297
        0x103,
        (
            "#020F#6P嗯，那我们就接受委托了。\x02\x03",

            "只要在蔡斯市和沃尔费堡垒\x01",
            "两个地方进行调查就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5402")


    ChrTalk(    #298
        0x8,
        (
            "#791F那就拜托了。\x02\x03",

            "市内的情报你们可以\x01",
            "找玛多克工房长帮忙，\x01",
            "也许他那里已经有足够的情报了。\x02\x03",

            "如果是那样的话，你们\x01",
            "就可以省下不少力气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#1006F#6P原来如此……\x02\x03",

            "也就是说，沃尔费堡垒\x01",
            "是必须要去调查的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x8,
        (
            "#792F嗯，不过这也只是我个人比较在意而已，\x01",
            "也不用把它当成紧急性的委托。\x02\x03",

            "一边完成告示板上的委托，\x01",
            "一边抽空去进行就可以了。\x02\x03",

            "#791F另外……\x01",
            "你们也有想去拜会的朋友吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1008F#6P啊……嗯！\x02\x03",

            "有关新型『福音』的事情\x01",
            "我们也要去通知给博士和提妲才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x105,
        (
            "#542F#6P是啊……\x01",
            "先去看看他们也好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x104,
        (
            "#030F#6P呼～既然如此，协会的工作\x01",
            "就先暂放一边吧。\x02\x03",

            "#031F为了和提妲再会，\x01",
            "我们马上就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_56D0")

    def lambda_5666():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5666)

    def lambda_5674():
        TurnDirection(0x105, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5674)
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #304
        0x106,
        (
            "#551F#5P你这家伙\x01",
            "有什么好激动的……\x02\x03",

            "#050F好啦，这就去拉赛尔工房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5740")

    label("loc_56D0")


    def lambda_56D6():
        TurnDirection(0x103, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_56D6)

    def lambda_56E4():
        TurnDirection(0x105, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56E4)
    OP_8C(0x101, 186, 400)

    ChrTalk(    #305
        0x101,
        (
            "#1007F#5P提妲和你\x01",
            "又没有什么关系……\x02\x03",

            "#1006F好啦。\x01",
            "去一趟拉赛尔工房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5740")

    OP_A2(0x1408)
    OP_28(0x85, 0x4, 0x2)
    OP_28(0x85, 0x4, 0x8)
    OP_28(0x85, 0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_6D(2550, 0, -2610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2550, 0, -2610, 180)
    SetChrPos(0xF7, 2550, 0, -2610, 180)
    SetChrPos(0x105, 2550, 0, -2610, 180)
    SetChrPos(0x104, 2550, 0, -2610, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_13_460B end

    def Function_14_57F4(): pass

    label("Function_14_57F4")

    OP_8E(0xFE, 0x1086, 0x0, 0xFFFFFD3A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_57F4 end

    def Function_15_5810(): pass

    label("Function_15_5810")

    OP_8E(0xFE, 0xC6C, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_5810 end

    def Function_16_582C(): pass

    label("Function_16_582C")

    OP_8E(0xFE, 0x10CC, 0x0, 0xFFFFF862, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_582C end

    def Function_17_5848(): pass

    label("Function_17_5848")

    OP_8E(0xFE, 0xD34, 0x0, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_5848 end

    def Function_18_5864(): pass

    label("Function_18_5864")

    OP_8E(0x8, 0x1482, 0x0, 0x532, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    Return()

    # Function_18_5864 end

    def Function_19_5894(): pass

    label("Function_19_5894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A5")
    Call(0, 38)

    label("loc_58A5")

    OP_31(0x6, 0x0, 0x28)
    OP_31(0x6, 0xFE, 0x0)
    OP_41(0x6, 0xBC, 0xFF)
    OP_41(0x6, 0xFF, 0xFF)
    OP_41(0x6, 0x120, 0xFF)
    OP_41(0x6, 0x2C9, 0x0)
    OP_41(0x6, 0x25F, 0x2)
    OP_41(0x6, 0x2D1, 0x3)
    OP_35(0x6, 0x0)
    OP_35(0x6, 0x8C)
    OP_BB(0x6, 0x6, 0x104)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrPos(0xB, 2770, 1050, 100, 0)
    SetChrPos(0xC, 3770, 1050, 100, 0)
    SetChrPos(0xD, 4770, 1050, 100, 0)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_A1(0xB, 0x1)
    OP_A1(0xC, 0x2)
    OP_A1(0xD, 0x3)
    SetChrPos(0x9, 3400, 0, -790, 0)
    SetChrPos(0xA, 4460, 0, -720, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(1770, 0, -2950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x1, 0x0, 0x14)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0x16)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #306
        0x101,
        (
            "#1004F#5P啊……\x01",
            "怎么了，二位。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_8C(0xA, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5A85")

    ChrTalk(    #307
        0xA,
        (
            "#061F#2P啊……\x01",
            "姐姐，还有阿加特哥哥！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AA8")

    label("loc_5A85")


    ChrTalk(    #308
        0xA,
        (
            "#061F#2P啊……\x01",
            "艾丝蒂尔姐姐！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AA8")


    ChrTalk(    #309
        0x9,
        (
            "#101F#2P喔喔～回来得\x01",
            "还真是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5AD7():
        OP_6D(3520, 0, -260, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5AD7)

    def lambda_5AEF():
        OP_6D(3520, 0, -260, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_5AEF)

    def lambda_5B07():
        OP_8E(0xFE, 0x1112, 0x0, 0xFFFFF916, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B07)
    Sleep(200)

    def lambda_5B27():
        OP_8E(0xFE, 0xD02, 0x0, 0xFFFFF7CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5B27)
    Sleep(300)

    def lambda_5B47():
        OP_8E(0xFE, 0x11D0, 0x0, 0xFFFFF4CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B47)
    Sleep(200)

    def lambda_5B67():
        OP_8E(0xFE, 0xDC0, 0x0, 0xFFFFF380, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B67)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 0, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 0, 400)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xA, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5C59")

    ChrTalk(    #310
        0x106,
        (
            "#051F#3P地震的调查已经完成了，\x01",
            "我们就回来了……\x02\x03",

            "嗯？那堆破烂是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x9,
        (
            "#104F#5P说破烂可太失礼了啊。\x02\x03",

            "#100F这个就是之前我说的那个\x01",
            "『好东西』了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF8")

    label("loc_5C59")


    ChrTalk(    #312
        0x101,
        (
            "#1011F#6P地震的调查已经完成了，\x01",
            "我们正要回来报告……\x02\x03",

            "嗯？那些机械是做什么的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        (
            "#101F#5P呵呵呵，\x01",
            "问的好。\x02\x03",

            "#100F这个就是之前我说的那个\x01",
            "『好东西』了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF8")


    ChrTalk(    #314
        0x8,
        (
            "#792F嗯，时间紧迫，有关那个的说明\x01",
            "还请稍后再说吧……\x02\x03",

            "#791F听说你们连圣海姆门\x01",
            "也一起调查过了对吧。\x02\x03",

            "那么就和沃尔费堡垒的调查\x01",
            "一起做个报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#1002F#6P嗯，是这样的……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E43")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在蔡斯看过瓦鲁特的情报】\x01",          # 0
            "【◇没有在蔡斯看过瓦鲁特的情报】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5E37"),
        (1, "loc_5E3D"),
        (SWITCH_DEFAULT, "loc_5E43"),
    )


    label("loc_5E37")

    OP_A2(0x1480)
    Jump("loc_5E43")

    label("loc_5E3D")

    OP_A3(0x1480)
    Jump("loc_5E43")

    label("loc_5E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_606D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #316
        (
            "\x07\x05将沃尔费堡垒和圣海姆门\x01",
            "的调查结果报告给雾香。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #317
        0x9,
        (
            "#104F#5P原来如此……\x01",
            "地震的规模似乎开始扩大了。\x02\x03",

            "#102F看来事态比想象中的更加严重呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xA,
        (
            "#063F#2P嗯，是啊……\x02\x03",

            "如果蔡斯市内\x01",
            "再发生更大地震的话，\x01",
            "那可就不得了了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x8,
        (
            "#792F还有在两个地震地点都\x01",
            "被目击到的墨镜男子……\x02\x03",

            "#790F和在蔡斯市内被目击到的那个人\x01",
            "像是同一个人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x101,
        (
            "#1002F#6P是吗……\x01",
            "果然也出现在市内了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x8,
        (
            "#790F嗯，玛多克工房长\x01",
            "帮忙收集了市内的情报。\x02\x03",

            "那个男人为『结社』一员\x01",
            "的可能性相当的高。\x02\x03",

            "因此各位今后一定要\x01",
            "全力协助博士的实验才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_620C")

    label("loc_606D")

    OP_2B(0x85, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #322
        (
            "\x07\x05将沃尔费堡垒、圣海姆门\x01",
            "以及蔡斯市内的调查结果做了报告。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #323
        0x9,
        (
            "#104F#5P原来如此……\x01",
            "地震的规模似乎开始扩大了。\x02\x03",

            "#102F看来事态比想象中的更加严重呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xA,
        (
            "#063F#2P嗯……\x02\x03",

            "如果蔡斯市内\x01",
            "再发生更大地震的话，\x01",
            "那可就不得了了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x8,
        (
            "#792F还有，在全部事发场所中都\x01",
            "被目击到的墨镜男子……\x02\x03",

            "#790F那个男人为『结社』一员\x01",
            "的可能性相当的高。\x02\x03",

            "因此各位今后一定要\x01",
            "全力协助博士的实验才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_620C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6241")

    ChrTalk(    #326
        0x106,
        (
            "#052F#3P实验……\x01",
            "是要使用这个装置吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6284")

    label("loc_6241")


    ChrTalk(    #327
        0x103,
        (
            "#027F#3P原来如此……\x02\x03",

            "所谓的实验，就是要使用\x01",
            "这个装置进行吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6284")


    ChrTalk(    #328
        0x9,
        (
            "#101F#5P嗯，正是。\x02\x03",

            "#100F这个是我在数年前\x01",
            "开发的『七耀脉测量仪』。\x02\x03",

            "将它设置在地面\x01",
            "就可以对『七耀脉』的流动\x01",
            "进行实时的感知和测定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x101,
        (
            "#1016F#6P哎哎……\x02\x03",

            "#1008F虽然这个名词已经听过好几次了，\x01",
            "不过……『七耀脉』究竟是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xA,
        (
            "#560F#2P那个啊，是存在于地下深处的\x01",
            "巨大的七耀石矿脉。\x02\x03",

            "它蕴藏的巨大能源可以对大地\x01",
            "造成一定的影响。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6438")

    ChrTalk(    #331
        0x104,
        (
            "#035F#3P『地脉』、『灵脉』等说法\x01",
            "都是它的别称呢。\x02\x03",

            "#030F在东方好像是把它称作『龙脉』吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6495")

    label("loc_6438")


    ChrTalk(    #332
        0x103,
        (
            "#020F#3P『地脉』、『灵脉』等说法\x01",
            "好像也都是指它呢。\x02\x03",

            "在东方，好像是把它称作『龙脉』吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6495")


    ChrTalk(    #333
        0x8,
        (
            "#791F啊，你知道的还真清楚呢。\x02\x03",

            "在很久以前的东方，人们都将都市建造\x01",
            "在传说有龙脉流经的地方呢。\x02\x03",

            "大概是想把大地的能源\x01",
            "用于国家的建设吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        (
            "#1011F#6P嘿嘿～原来是这样啊。\x01",
            "又上了一课呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x105,
        (
            "#043F#6P那么，使用这装置的话\x01",
            "就可以阻止地震的发生了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x9,
        (
            "#104F#5P不，它只能探测七耀脉的流动，\x01",
            "并不能真正阻止地震的发生。\x02\x03",

            "#100F但是，在塞姆里亚大陆中\x01",
            "流传着这种说法：地震是由于七耀脉\x01",
            "的流动造成地壳歪曲而引发的。\x02\x03",

            "所以，只要调查七耀脉的流动情况，\x01",
            "也许就能发现什么有用的线索了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x105,
        (
            "#047F#6P原来如此……\x02\x03",

            "#040F那么，在下次地震发生之前\x01",
            "要尽快将它们设置好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6707")

    ChrTalk(    #338
        0x106,
        (
            "#051F#3P装置共有３个，\x01",
            "也就是说要分别放置在３个地方了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673E")

    label("loc_6707")


    ChrTalk(    #339
        0x103,
        (
            "#020F#3P装置共有３个，\x01",
            "是要分别设置在３处场所吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_673E")


    ChrTalk(    #340
        0x9,
        "#102F#5P嗯，把地图给我看看。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    def lambda_676D():
        TurnDirection(0xA, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_676D)
    TurnDirection(0x101, 0x9, 400)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS134._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS204._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS205._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS206._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("拉赛尔博士")

    AnonymousTalk(    #341
        (
            "\x07\x00#104F要设置的场所共有３处，\x01",
            "都在蔡斯地区。\x02\x03",

            "#100F首先是托兰特平原北部外围\x01",
            "的一处巨石堆积的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("拉赛尔博士")

    AnonymousTalk(    #342
        (
            "\x07\x00#104F然后是卡鲁迪亚隧道的中间地带，\x01",
            "大概就是从蔡斯方向出发，遇到的第一座桥那里。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("拉赛尔博士")

    AnonymousTalk(    #343
        "\x07\x00#100F最后是雷斯顿要塞前。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("拉赛尔博士")

    AnonymousTalk(    #344
        (
            "\x07\x00#101F──希望你们能将装置\x01",
            "设置在以上３个地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #345
        0x101,
        (
            "#1006F#6P嗯……\x01",
            "我们记住了。\x02\x03",

            "不过，设置测量仪…\x01",
            "只需要将它放在那里就可以了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x9,
        (
            "#102F#5P不，没那么简单。\x02\x03",

            "必须要将测定用的勘测针以正确的角度\x01",
            "刺入地面，\x01",
            "另外天线也需要手动设置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x104,
        (
            "#030F#6P天线是导力通讯\x01",
            "的装置吧。\x02\x03",

            "作用是要将勘测出的情报\x01",
            "发送出去，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x9,
        (
            "#101F#5P喔，判断力很敏锐嘛。\x02\x03",

            "#100F嗯，外设的天线会把测定出来的数值\x01",
            "传送到演算导力器『卡佩尔』中，\x01",
            "用以解析七耀脉的流动情况。\x02\x03",

            "卡佩尔会对３个地方的情况\x01",
            "进行实时分析，\x01",
            "因此应该可以得出正确的结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        (
            "#1007F#6P嗯～似乎是很厉害的实验呢。\x02\x03",

            "#1011F那么，拉赛尔博士也要\x01",
            "和我们同行，去进行装置的设置吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x9,
        (
            "#100F#5P不，我还要进行『卡佩尔』\x01",
            "的调整工作，实在没有空闲。\x02\x03",

            "那件工作就让提妲替我去做吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #351
        0xA,
        (
            "#067F#2P嘿嘿嘿……\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6F01")

    ChrTalk(    #352
        0x101,
        (
            "#1006F#6P是吗。\x01",
            "有提妲帮忙的话比一百人还要管用呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #353
        0x101,
        (
            "#1019F#6P……阿加特。\x01",
            "你没什么要说的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #354
        0x106,
        (
            "#053F#1P没办法了……\x02\x03",

            "#051F只是你可不能总\x01",
            "陶醉在机械的世界里啊，\x02\x03",

            "要是还像以前那样动不动就发呆，\x01",
            "也许被魔兽吃掉了还不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xA,
        (
            "#562F#2P呜呜……\x01",
            "阿加特哥哥又欺负人了……\x02\x03",

            "#560F可是～就算真的出现那种情况\x01",
            "你也会保护我的对不对？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x106,
        "#551F#1P……真是的，这小鬼头。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x101,
        (
            "#1001F#6P哈哈哈～\x01",
            "阿加特果然还是败了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FBB")

    label("loc_6F01")


    ChrTalk(    #358
        0x101,
        (
            "#1006F#6P是吗。\x01",
            "有提妲帮忙的话比一百人还要管用呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #359
        0x101,
        "#1011F#6P雪拉姐，可以吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #360
        0x103,
        (
            "#021F#1P呵呵，那当然啦。\x02\x03",

            "#526F请多关照了，小提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xA,
        "#061F#2P是的，雪拉姐。\x02",
    )

    CloseMessageWindow()

    label("loc_6FBB")

    OP_44(0x101, 0xFF)
    OP_8C(0x101, 315, 400)
    OP_8C(0xF7, 0, 400)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #362
        0x9,
        (
            "#100F#5P那么，我这就开始\x01",
            "进行『卡佩尔』的输入调整了。\x02\x03",

            "你们把全部的测量仪设置完毕后\x01",
            "就来中央工房的演算室找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        "#1018F#6P嗯，明白了！\x02",
    )

    CloseMessageWindow()

    def lambda_706B():

        label("loc_706B")

        TurnDirection(0xA, 0x9, 400)
        OP_48()
        Jump("loc_706B")

    QueueWorkItem2(0xA, 3, lambda_706B)

    ChrTalk(    #364
        0xA,
        "#560F#2P爷爷也要加油啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 225, 400)

    def lambda_70A1():
        OP_6D(1600, 0, -4670, 3000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_70A1)

    def lambda_70B9():

        label("loc_70B9")

        TurnDirection(0x101, 0x9, 400)
        OP_48()
        Jump("loc_70B9")

    QueueWorkItem2(0x101, 3, lambda_70B9)

    def lambda_70CA():

        label("loc_70CA")

        TurnDirection(0xF7, 0x9, 400)
        OP_48()
        Jump("loc_70CA")

    QueueWorkItem2(0xF7, 3, lambda_70CA)

    def lambda_70DB():

        label("loc_70DB")

        TurnDirection(0x105, 0x9, 400)
        OP_48()
        Jump("loc_70DB")

    QueueWorkItem2(0x105, 3, lambda_70DB)

    def lambda_70EC():

        label("loc_70EC")

        TurnDirection(0x104, 0x9, 400)
        OP_48()
        Jump("loc_70EC")

    QueueWorkItem2(0x104, 3, lambda_70EC)
    OP_8E(0x9, 0x5A0, 0x0, 0xFFFFF966, 0x9C4, 0x0)
    OP_8E(0x9, 0x5F0, 0x0, 0xFFFFE750, 0x9C4, 0x0)
    OP_8E(0x9, 0x5DC, 0xFFFFFE0C, 0xFFFFE3F4, 0x9C4, 0x0)
    SetChrFlags(0x9, 0x4)

    def lambda_713E():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_713E)
    OP_8E(0x9, 0x618, 0xFFFFFE0C, 0xFFFFDFC6, 0x9C4, 0x0)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x9, 0x3)
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x3)
    OP_44(0x105, 0x3)
    OP_44(0x104, 0x3)
    OP_44(0xA, 0x3)
    Sleep(500)

    def lambda_7187():
        OP_6D(3500, 0, -505, 1500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7187)

    def lambda_719F():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_719F)

    def lambda_71AD():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71AD)

    def lambda_71BB():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71BB)

    def lambda_71C9():
        OP_8C(0xA, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_71C9)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x9, 0x3)

    ChrTalk(    #365
        0x101,
        (
            "#1006F#6P一定要在下次地震发生之前\x01",
            "将全部测量仪设置好……\x02\x03",

            "我们马上出发吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_72A4")

    ChrTalk(    #366
        0x106,
        (
            "#052F#5P哦，等一下……\x02\x03",

            "#051F要一起行动的话\x01",
            "人数似乎太多了啊。\x02\x03",

            "在这里决定一下行动队员\x01",
            "再决定比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7315")

    label("loc_72A4")


    ChrTalk(    #367
        0x103,
        (
            "#023F#5P啊，请稍等一下。\x02\x03",

            "#020F这么多人一起行动的话\x01",
            "似乎有些不便哦。\x02\x03",

            "在这里决定一下行动队员\x01",
            "和待机队员吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7315")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #368
        (
            "\x07\x05※可以参加战斗的同行队员\x01",
            "　最多只能有４位。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #369
        (
            "※今后，队伍成员超过４人的时候，\x01",
            "　就需要在全部成员中\x01",
            "　选出同行的角色。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x1F4)
    Sleep(500)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_73DD")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_73EE")

    label("loc_73DD")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_73EE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    OP_6D(2310, 0, -620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF7, 3200, 0, -1260, 270)
    SetChrPos(0x101, 4240, 0, -1160, 270)
    SetChrPos(0x107, 4290, 0, -2310, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A3")
    SetChrPos(0xE, 1680, 0, -1990, 90)
    SetChrPos(0x105, 3020, 0, -2400, 270)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_74CA")

    label("loc_74A3")

    SetChrPos(0xF, 1680, 0, -1990, 90)
    SetChrPos(0x104, 3020, 0, -2400, 270)
    ClearChrFlags(0xF, 0x80)

    label("loc_74CA")

    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7638")

    ChrTalk(    #370
        0xE,
        (
            "#035F#5P呼～那么我暂且就在\x01",
            "２楼优雅地休息一会吧。\x02\x03",

            "#030F需要我这个天才帮忙的时候\x01",
            "随时可以过来找我哟。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_7560():

        label("loc_7560")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_7560")

    QueueWorkItem2(0x101, 3, lambda_7560)

    def lambda_7571():

        label("loc_7571")

        TurnDirection(0xF7, 0xE, 400)
        OP_48()
        Jump("loc_7571")

    QueueWorkItem2(0xF7, 3, lambda_7571)

    def lambda_7582():

        label("loc_7582")

        TurnDirection(0x105, 0xE, 400)
        OP_48()
        Jump("loc_7582")

    QueueWorkItem2(0x105, 3, lambda_7582)

    def lambda_7593():

        label("loc_7593")

        TurnDirection(0x107, 0xE, 400)
        OP_48()
        Jump("loc_7593")

    QueueWorkItem2(0x107, 3, lambda_7593)
    OP_8C(0xE, 315, 500)

    def lambda_75AB():
        OP_6D(1550, 0, 430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_75AB)
    SetChrFlags(0xE, 0x4)
    OP_8E(0xE, 0xFFFFF8D0, 0x0, 0x51E, 0x9C4, 0x0)
    OP_8E(0xE, 0xFFFFF858, 0x0, 0x992, 0x9C4, 0x0)
    OP_8C(0xE, 90, 500)
    ClearChrFlags(0xE, 0x4)
    OP_8E(0xE, 0x9C4, 0x8CA, 0xAAA, 0x9C4, 0x0)

    def lambda_7610():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_7610)
    OP_8E(0xE, 0xFA0, 0xDAC, 0x99C, 0x9C4, 0x0)
    SetChrFlags(0xE, 0x80)
    Jump("loc_7769")

    label("loc_7638")


    ChrTalk(    #371
        0xF,
        (
            "#040F#5P明白了。\x01",
            "我先在２楼待命。\x02\x03",

            "#041F需要我出力的时候\x01",
            "随时可以过来找我。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_7694():

        label("loc_7694")

        TurnDirection(0x101, 0xF, 400)
        OP_48()
        Jump("loc_7694")

    QueueWorkItem2(0x101, 3, lambda_7694)

    def lambda_76A5():

        label("loc_76A5")

        TurnDirection(0xF7, 0xF, 400)
        OP_48()
        Jump("loc_76A5")

    QueueWorkItem2(0xF7, 3, lambda_76A5)

    def lambda_76B6():

        label("loc_76B6")

        TurnDirection(0x104, 0xF, 400)
        OP_48()
        Jump("loc_76B6")

    QueueWorkItem2(0x104, 3, lambda_76B6)

    def lambda_76C7():

        label("loc_76C7")

        TurnDirection(0x107, 0xF, 400)
        OP_48()
        Jump("loc_76C7")

    QueueWorkItem2(0x107, 3, lambda_76C7)
    OP_8C(0xF, 315, 500)

    def lambda_76DF():
        OP_6D(1550, 0, 430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76DF)
    SetChrFlags(0xF, 0x4)
    OP_8E(0xF, 0xFFFFF8D0, 0x0, 0x51E, 0x9C4, 0x0)
    OP_8E(0xF, 0xFFFFF858, 0x0, 0x992, 0x9C4, 0x0)
    OP_8C(0xF, 90, 500)
    ClearChrFlags(0xF, 0x4)
    OP_8E(0xF, 0x9C4, 0x8CA, 0xAAA, 0x9C4, 0x0)

    def lambda_7744():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7744)
    OP_8E(0xF, 0xFA0, 0xDAC, 0x99C, 0x9C4, 0x0)
    SetChrFlags(0xF, 0x80)

    label("loc_7769")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #372
        (
            "\x07\x05※不在队伍中的成员\x01",
            "　会在协会的２楼待命。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #373
        (
            "※通过对话，即可\x01",
            "　随时更改\x01",
            "　队伍内的成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_77F0():
        OP_6D(3500, 0, -505, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77F0)
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0x107, 0x3)

    def lambda_7818():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7818)

    def lambda_7826():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7826)

    def lambda_7834():
        OP_8C(0x107, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7834)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #374
        0x101,
        (
            "#1006F#6P嗯，这就ＯＫ了。\x02\x03",

            "#1015F嗯…测量仪需要设置在\x01",
            "隧道途中、平原北部、\x01",
            "雷斯顿要塞３个地方哦。\x02\x03",

            "哎～以什么顺序\x01",
            "来设置比较好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x8,
        (
            "#791F那就随便你们了。\x02\x03",

            "雷斯顿要塞那边\x01",
            "我会和他们联络。\x02\x03",

            "到时你们只要把情况和门卫说一下，\x01",
            "他应该就会允许你们在那里设置了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x101,
        "#1006F#6P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_7970():
        OP_8C(0xF7, 135, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7970)
    OP_8C(0x101, 270, 400)
    OP_8C(0x107, 315, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_79DD")

    ChrTalk(    #377
        0x106,
        (
            "#051F#5P好，那我们马上出发吧。\x02\x03",

            "提妲。\x01",
            "要跟上我们哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x107,
        "#061F#6P好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A4C")

    label("loc_79DD")


    ChrTalk(    #379
        0x103,
        (
            "#020F#5P那么……\x01",
            "我们这就出发吧。\x02\x03",

            "#021F小提妲。\x01",
            "接下来就要看你的表现了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x107,
        "#560F#6P我、我会加油的！\x02",
    )

    CloseMessageWindow()

    label("loc_7A4C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1417)
    OP_28(0x87, 0x4, 0x2)
    OP_28(0x87, 0x4, 0x8)
    OP_28(0x87, 0x1, 0x1)
    OP_28(0x87, 0x1, 0x2)
    OP_28(0x87, 0x1, 0x4)
    OP_28(0x87, 0x1, 0x8)
    OP_4B(0x8, 255)
    OP_6D(3170, 0, -2350, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 3170, 0, -2350, 180)
    SetChrPos(0x1, 3170, 0, -2350, 180)
    SetChrPos(0x2, 3170, 0, -2350, 180)
    SetChrPos(0x3, 3170, 0, -2350, 180)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_19_5894 end

    def Function_20_7B30(): pass

    label("Function_20_7B30")

    SetChrFlags(0x101, 0x4)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 1480, -500, -8360, 0)
    ClearChrFlags(0x101, 0x80)

    def lambda_7B5C():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B5C)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_8E(0x101, 0x974, 0x0, 0xFFFFED18, 0x7D0, 0x0)
    OP_8C(0x101, 0, 0)
    Return()

    # Function_20_7B30 end

    def Function_21_7B9D(): pass

    label("Function_21_7B9D")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF7, 1480, -500, -8360, 0)
    ClearChrFlags(0xF7, 0x80)

    def lambda_7BC9():
        OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_7BC9)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xF7, 0x550, 0x0, 0xFFFFEC82, 0x7D0, 0x0)
    OP_8C(0xF7, 0, 0)
    Return()

    # Function_21_7B9D end

    def Function_22_7C0A(): pass

    label("Function_22_7C0A")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, 1480, -500, -8360, 0)
    ClearChrFlags(0x105, 0x80)

    def lambda_7C36():
        OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C36)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0x105, 0x8DE, 0x0, 0xFFFFE89A, 0x7D0, 0x0)
    OP_8C(0x105, 0, 0)
    Return()

    # Function_22_7C0A end

    def Function_23_7C77(): pass

    label("Function_23_7C77")

    OP_9F(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, 1480, -500, -8360, 0)
    ClearChrFlags(0x104, 0x80)

    def lambda_7C9E():
        OP_9F(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7C9E)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    OP_8E(0x104, 0x438, 0x0, 0xFFFFE7DC, 0x7D0, 0x0)
    OP_8C(0x104, 0, 0)
    Return()

    # Function_23_7C77 end

    def Function_24_7CDA(): pass

    label("Function_24_7CDA")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CF6")
    Call(0, 38)
    Call(0, 39)

    label("loc_7CF6")

    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0E")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_7D12")

    label("loc_7D0E")

    AddParty(0x3, 0xFA, 0xFF)

    label("loc_7D12")

    OP_6D(2340, 0, -5820, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 3120, 0, -700, 0)
    SetChrPos(0x101, 4170, 0, -700, 315)
    SetChrPos(0x104, 2450, 0, -1620, 0)
    SetChrPos(0xF7, 3600, 0, -1920, 0)
    SetChrPos(0x105, 4720, 0, -1960, 0)
    SetChrPos(0x107, 4190, 0, -3140, 0)
    SetChrPos(0x9, 3140, 0, -2970, 0)
    SetChrPos(0x10, 2029, 0, -2710, 0)
    FadeToBright(1000, 0)

    def lambda_7DF5():
        OP_6D(2660, 0, -300, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DF5)

    def lambda_7E0D():
        OP_67(0, 8000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E0D)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #381
        0x8,
        (
            "#792F是吗……\x02\x03",

            "那个戴墨镜的男人\x01",
            "果然就是瓦鲁特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x11,
        (
            "#073F#6P啊啊──哎？\x02\x03",

            "难道你早就\x01",
            "已经猜到了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x8,
        (
            "#791F嗯，听过服装和体型的描述后\x01",
            "我就基本确定是他了。\x02\x03",

            "#792F你这次还是太大意了啊。\x02\x03",

            "怎么可以就这样任由他\x01",
            "把『福音』带走？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x11,
        (
            "#075F#6P没办法……\x01",
            "我也没想到那东西\x01",
            "会这么重要啊。\x02\x03",

            "#072F而且连事情经过都不说\x01",
            "就直接催我快去亚尔摩村\x01",
            "的人不正是你吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x8,
        (
            "#791F嗯，这也算是我的判断失误。\x02\x03",

            "本以为这种状况就算不做说明\x01",
            "你自己也能判断清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x11,
        "#075F#6P呼……你还是这么不可爱。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x8,
        (
            "#792F不管怎么说，\x01",
            "地震的调查总算是解决了。\x02\x03",

            "#790F把调查的报酬\x01",
            "给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x85, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8085")
    OP_AF(0x9A, 0x85)
    Sleep(100)
    OP_28(0x86, 0x4, 0x10)
    OP_28(0x86, 0x4, 0x20)
    OP_28(0x87, 0x4, 0x10)
    OP_28(0x87, 0x4, 0x20)

    label("loc_8085")

    OP_28(0x88, 0x4, 0x10)
    OP_AF(0x9A, 0x88)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #388
        0x101,
        (
            "#1006F#6P谢谢雾香姐。\x02\x03",

            "#1015F不过…你们和那个墨镜男\x01",
            "在以前就认识的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #389
        0x11,
        (
            "#074F#5P嗯，这个啊…\x01",
            "要怎么说才好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#791F简单的说，\x01",
            "我和金，还有瓦鲁特…\x02\x03",

            "曾经都是同门修行的弟子……\x02\x03",

            "其中他最年长，\x01",
            "也就是大师兄。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_81C0")

    ChrTalk(    #391
        0x106,
        (
            "#052F#6P同门师兄弟啊……\x01",
            "也就是武术上的前辈吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F7")

    label("loc_81C0")


    ChrTalk(    #392
        0x103,
        (
            "#023F#6P同门师兄弟……\x01",
            "那也就是武术上的前辈了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F7")

    OP_8C(0x11, 135, 400)

    ChrTalk(    #393
        0x11,
        (
            "#070F#5P嗯，正确的说，\x01",
            "雾香她并不是弟子，\x02\x03",

            "而是龙牙师父的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x8,
        (
            "#792F我的事情就没必要提了。\x02\x03",

            "#790F总之那个男人曾经是\x01",
            "『泰斗流』门下的弟子。\x02\x03",

            "在6年前离开道场后\x01",
            "就被『噬身之蛇』看中。\x02\x03",

            "#792F之后就加入了那个组织。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x11,
        "#572F#5P雾香……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8377")

    ChrTalk(    #396
        0x106,
        (
            "#053F#6P说到这里我就完全明白了。\x02\x03",

            "#552F话说回来，他使用的武术好像是\x01",
            "和你们一样的『泰斗流』功夫啊……\x02\x03",

            "强得简直像个妖怪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83F3")

    label("loc_8377")


    ChrTalk(    #397
        0x103,
        (
            "#026F#6P说到这里我就完全明白了。\x02\x03",

            "#020F话说回来，他好像和你们一样，\x01",
            "用的也是『泰斗流』的武术……\x02\x03",

            "真是好厉害的功夫啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F3")


    ChrTalk(    #398
        0x11,
        (
            "#074F#5P他的身手比在道场时\x01",
            "又精进了很多。\x02\x03",

            "#072F可以说是达人级别的武者了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x8,
        (
            "#792F确实是个非常危险的男人啊。\x02\x03",

            "#791F不过现在看来，再发生地震\x01",
            "的可能性应该已经很低了。\x02\x03",

            "稍微放松一下警备也无所谓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x10,
        (
            "#801F#6P啊啊，说的对。\x01",
            "我这就去通知市民和职员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x9,
        (
            "#104F#6P不过，他们再次使用了\x01",
            "『福音』啊。\x02\x03",

            "而且还连同让七耀脉活性化的\x01",
            "装置一起使用……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8555():
        OP_6D(2660, 0, -1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8555)

    def lambda_856D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_856D)

    def lambda_857B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_857B)
    Sleep(50)

    def lambda_858E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_858E)

    def lambda_859C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_859C)
    Sleep(50)

    def lambda_85AF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_85AF)

    def lambda_85BD():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_85BD)
    Sleep(50)

    def lambda_85D0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_85D0)
    Sleep(300)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8744")

    ChrTalk(    #402
        0x104,
        (
            "#030F#5P联系学院地下的投影\x01",
            "装置一起分析的话……\x02\x03",

            "看来他们已经得到了可以大幅度提高\x01",
            "导力器性能的技术了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x9,
        (
            "#102F#6P嗯……确实如此。\x02\x03",

            "空间投影装置也好，\x01",
            "七耀脉的活性化装置也好，\x01",
            "都不是绝对无法实现的技术。\x02\x03",

            "但加上『福音』的影响后就可以产生\x01",
            "以当今的导力技术无法解释的现象。\x02\x03",

            "不仅是我，其他任何一家\x01",
            "技术工房恐怕也都不能解释这些现象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8896")

    label("loc_8744")


    ChrTalk(    #404
        0x105,
        (
            "#042F#2P连同学院地下的投影装置\x01",
            "一起分析的话……\x02\x03",

            "看来他们已经得到了可以大幅度提高\x01",
            "导力器性能的技术了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x9,
        (
            "#102F#6P嗯……应该没错。\x02\x03",

            "空间投影装置也好，\x01",
            "七耀脉的活性化装置也好，\x01",
            "都不是绝对无法实现的技术。\x02\x03",

            "但加上『福音』的影响后就可以产生\x01",
            "以当今的导力技术无法解释的现象。\x02\x03",

            "不仅是我，其它任何一家\x01",
            "技术工房恐怕也都不能解释这些现象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8896")


    ChrTalk(    #406
        0x10,
        (
            "#803F#5P是啊……\x02\x03",

            "共和国的乌尔努社，\x01",
            "帝国的莱恩福尔特社……\x02\x03",

            "#800F甚至是研发了战术导力器的\x01",
            "爱普斯泰恩财团也都无法做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        (
            "#1002F#2P这么说的话…结社的\x01",
            "技术力实在是太惊人了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x9,
        (
            "#100F#6P嗯，大概他们之中\x01",
            "有个这方面的天才吧。\x02\x03",

            "#101F嗯嗯……\x01",
            "我也不能输给他们啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x107,
        "#065F#6P爷、爷爷……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x10,
        (
            "#803F#5P呼，真没办法……\x02\x03",

            "#800F新型引擎总算\x01",
            "也完工了……\x02\x03",

            "中央工房今后就将解析『福音』\x01",
            "作为最优先的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x9,
        "#101F#6P哇哈哈，那当然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x101,
        (
            "#1006F#2P确实，如果能参透『福音』\x01",
            "的奥秘的话就帮大忙了……\x02\x03",

            "不知道他们今后还会以怎样的\x01",
            "方式来使用『福音』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8B28")

    ChrTalk(    #413
        0x106,
        (
            "#053F#5P而且那些家伙都在说\x01",
            "什么『实验』。\x02\x03",

            "#050F既然有２次的话，再出现第３次也不奇怪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7E")

    label("loc_8B28")


    ChrTalk(    #414
        0x103,
        (
            "#026F#5P而且那些家伙都在说\x01",
            "什么『实验』。\x02\x03",

            "#022F有２次的话，就难保不会有第３次。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B7E")


    ChrTalk(    #415
        0x8,
        (
            "#792F『福音』的分析工作\x01",
            "就拜托博士他们了……\x02\x03",

            "#790F而你们也差不多该\x01",
            "向下一个地方进发了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8BE4():
        OP_6D(2660, 0, -300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BE4)

    def lambda_8BFC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8BFC)

    def lambda_8C0A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C0A)
    Sleep(50)

    def lambda_8C1D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C1D)

    def lambda_8C2B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C2B)
    Sleep(50)

    def lambda_8C3E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8C3E)

    def lambda_8C4C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8C4C)
    Sleep(50)

    def lambda_8C5F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8C5F)
    Sleep(500)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #416
        0x101,
        (
            "#1006F#6P嗯，是啊。\x02\x03",

            "虽然没有抓到犯人，\x01",
            "但总算把地震的事情解决了。\x02\x03",

            "接下来我们要去哪里好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x8,
        (
            "#791F王都支部正好刚发来了\x01",
            "支援请求。\x02\x03",

            "王国军\x01",
            "好像有什么正式的委托啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        (
            "#1004F#6P王国军……\x01",
            "难道是老爸的委托吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x8,
        (
            "#791F详情我也不清楚。\x02\x03",

            "不过那边还特意指名\x01",
            "让你们去，\x01",
            "大概是和结社有关的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x101,
        "#1015F#6P确实如此啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8DEF")

    ChrTalk(    #421
        0x106,
        (
            "#051F#6P嘿……\x01",
            "那就过去看看好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E1E")

    label("loc_8DEF")


    ChrTalk(    #422
        0x103,
        (
            "#027F#6P呵呵……\x01",
            "那就只有先过去看看了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E1E")

    OP_8C(0x11, 135, 400)

    ChrTalk(    #423
        0x11,
        (
            "#071F#5P好，那就这么决定了。\x02\x03",

            "把蔡斯的事情全做完以后\x01",
            "就乘坐定期船去王都吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #424
        0x101,
        (
            "#1001F ＯＫ……\x02\x03",

            "#1004F啊，难道\x01",
            "金先生也要和我们一起行动吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x11,
        (
            "#070F#5P喂～那是当然的啊，不然你以为\x01",
            "我是为了什么才会特意赶回来的。\x02\x03",

            "瓦鲁特的事情我不能坐视不管，\x01",
            "而且你不是还在寻找约修亚吗？\x02\x03",

            "我当然要尽力帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x101,
        "#1017F金先生……谢谢你。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9087")

    ChrTalk(    #427
        0x106,
        (
            "#053F#6P说心里话，你能\x01",
            "帮忙实在是太好了啊。\x02\x03",

            "#050F我这次算是彻底\x01",
            "惨败给那个戴墨镜的混蛋了……\x02\x03",

            "可以的话请你指点我几招吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x11,
        (
            "#071F#5P哈哈，你这么说话未免\x01",
            "太谦虚了。\x02\x03",

            "#070F原来的豪气跑到哪里去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x106,
        (
            "#552F#6P哼，我早已不是连你的\x01",
            "实力都不清楚的呆小子了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9187")

    label("loc_9087")


    ChrTalk(    #430
        0x103,
        (
            "#021F#6P呵呵，金先生一个人\x01",
            "可是比一百个人还要可靠的强援啊。\x02\x03",

            "#027F我这次算是彻底\x01",
            "被那个戴墨镜的男人打败了……\x02\x03",

            "可以的话请你来指教我一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x11,
        (
            "#070F#5P嗯，这个没问题。\x02\x03",

            "那家伙的招式比较特殊，\x01",
            "到时我把应对方法告诉你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x103,
        "#021F#6P嗯，那就拜托了。\x02",
    )

    CloseMessageWindow()

    label("loc_9187")

    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_93D9")

    ChrTalk(    #433
        0x107,
        (
            "#062F#6P姐姐，阿加特哥哥。\x02\x03",

            "我也……\x01",
            "我也和你们一起去可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_9224():
        OP_6D(2660, 0, -1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9224)

    def lambda_923C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_923C)

    def lambda_924A():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_924A)
    Sleep(50)

    def lambda_925D():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_925D)

    def lambda_926B():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_926B)
    Sleep(50)

    def lambda_927E():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_927E)

    def lambda_928C():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_928C)
    Sleep(50)

    def lambda_929F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_929F)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #434
        0x101,
        "#1004F#2P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x106,
        "#055F#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x107,
        (
            "#561F#6P嗯…我想他们以后也许还会\x01",
            "继续使用『福音』之类的\x01",
            "奇怪装置。\x02\x03",

            "到了那个时候…\x01",
            "我应该可以帮上一点忙……\x02\x03",

            "#062F所以…请你们带上我吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        "#1003F#2P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x106,
        "#053F#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 400)
    Sleep(300)

    ChrTalk(    #439
        0x106,
        "#050F#5P老爷子的意见如何？\x02",
    )

    CloseMessageWindow()
    Jump("loc_95FB")

    label("loc_93D9")


    ChrTalk(    #440
        0x107,
        (
            "#062F#6P艾丝蒂尔姐姐、雪拉姐姐。\x02\x03",

            "我也……\x01",
            "我也和你们一起去可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_945B():
        OP_6D(2660, 0, -1300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_945B)

    def lambda_9473():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9473)

    def lambda_9481():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9481)
    Sleep(50)

    def lambda_9494():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9494)

    def lambda_94A2():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_94A2)
    Sleep(50)

    def lambda_94B5():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_94B5)

    def lambda_94C3():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_94C3)
    Sleep(50)

    def lambda_94D6():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_94D6)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #441
        0x101,
        "#1004F#2P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x103,
        "#023F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x107,
        (
            "#561F#6P嗯…我想他们以后也许还会\x01",
            "继续使用『福音』之类的\x01",
            "奇怪装置。\x02\x03",

            "到了那个时候…\x01",
            "我应该可以帮上一点忙……\x02\x03",

            "#062F所以…请你们带上我吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x101,
        "#1003F#2P可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x103,
        "#026F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)
    Sleep(300)

    ChrTalk(    #446
        0x103,
        "#020F#5P博士的意见如何呢？\x02",
    )

    CloseMessageWindow()

    label("loc_95FB")


    ChrTalk(    #447
        0x9,
        (
            "#104F#6P嗯…作为爷爷\x01",
            "我自然是不愿意孙女去犯险……\x02\x03",

            "#100F不过提妲这孩子也很顽固，\x01",
            "还是尽量顺从她的心意比较好。\x02\x03",

            "所以呢，我就不反对了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #448
        0x107,
        "#560F#6P爷爷……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x9,
        (
            "#100F#6P结社拥有着超乎我们\x01",
            "想象的技术力。\x02\x03",

            "所以在今后的调查中\x01",
            "提妲一定可以派得上用场，\x02\x03",

            "#101F你们收下她肯定是不吃亏的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x10,
        (
            "#805F#5P真是的…这口气怎么像是\x01",
            "在兜售新产品一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x101,
        (
            "#1007F#2P嗯，有提妲的帮忙\x01",
            "虽然很好……\x02\x03",

            "#1003F但如果以后再出现墨镜男子\x01",
            "那样危险的家伙……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9BCE")

    ChrTalk(    #452
        0x106,
        (
            "#552F#5P……………………………\x02\x03",

            "#053F不……这样也好。\x02\x03",

            "您的孙女，\x01",
            "就先交给我照顾吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 315, 400)

    ChrTalk(    #453
        0x107,
        "#064F#6P哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x9,
        "#103F#6P喔哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0x101,
        (
            "#1004F#2P这、这到底是什么了！？\x02\x03",

            "本以为你一定会\x01",
            "坚决反对的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x106,
        (
            "#053F#5P单从地震事件就可以看出，\x01",
            "『结社』的行为完全没有顾及到\x01",
            "民间人士的生命安全。\x02\x03",

            "这就意味着，不管在什么地方\x01",
            "也都不能保证绝对的安全。\x02\x03",

            "#051F所以还不如遵照她本人的意愿，\x01",
            "顺便也还能帮我们一点忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x107,
        "#560F#6P阿加特哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x9,
        (
            "#100F#6P原来如此……\x01",
            "这种想法倒也没有错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x104,
        (
            "#035F#5P嘿嘿嘿～你是希望把她留在身边\x01",
            "保护，不然放不下心吧。\x02\x03",

            "#037F原来是这样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x106, 270, 600)

    ChrTalk(    #460
        0x106,
        "#055F#4P什、什么啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x101,
        "#1006F#2P啊，好像脸红了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x107,
        (
            "#560F#6P那个那个……\x01",
            "那个…真的是这样吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 135, 400)

    ChrTalk(    #463
        0x106,
        (
            "#551F#5P这种话你还要当真啊……\x02\x03",

            "#555F事先听好！保护好自己\x01",
            "是最基本的原则。\x02\x03",

            "不要再一看到机械就不顾\x01",
            "周围的情况了，明白了没有？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x107,
        "#067F#6P嘿嘿……我一定会小心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x11,
        (
            "#071F#5P哈哈……\x01",
            "能达成共识就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x105,
        (
            "#048F哈哈，看来\x01",
            "大家的意见统一了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E5F")

    label("loc_9BCE")

    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #467
        0x105,
        (
            "#043F#4P啊啊，话虽如此……\x02\x03",

            "但从地震事件来看的话，\x01",
            "『结社』的行为已经严重\x01",
            "威胁到了民众的安全。\x02\x03",

            "因此即使留在这里\x01",
            "也未必可以保证完全没有危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x101,
        "#1004F#2P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #469
        0x103,
        (
            "#027F#5P也许和我们一起行动\x01",
            "反而会更安全一点……\x02\x03",

            "那么说的话也没错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x105,
        "#542F#4P是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0x107,
        "#064F#6P科洛丝姐姐…雪拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        (
            "#1007F#2P啊啊！！好了啦，我知道了。\x02\x03",

            "#1005F其实我不是也……\x01",
            "不想和提妲分别吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x107,
        "#560F#6P艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x101,
        (
            "#1013F哎#2P……嗯……\x02\x03",

            "#1016F就是那样啦，\x01",
            "以后多多关照啊，提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x107,
        "#067F#6P嗯！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x11,
        (
            "#071F#5P哈哈……\x01",
            "能达成共识就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x104,
        (
            "#031F#5P呵呵，看来大家\x01",
            "已经统一意见了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E3F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9E3F)
    Sleep(50)

    def lambda_9E52():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E52)
    Sleep(50)

    label("loc_9E5F")

    OP_8C(0x107, 270, 400)
    OP_8C(0x9, 90, 400)

    ChrTalk(    #478
        0x9,
        (
            "#100F#5P提妲啊，\x01",
            "旅途中一定要多加小心。\x02\x03",

            "#101F在你努力的时候\x01",
            "爷爷也会把『福音』之谜\x01",
            "解明给你看的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x107,
        "#061F#6P嗯……那就等着您的好消息了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x10,
        (
            "#801F#5P博士就放心交给我吧。\x02\x03",

            "我会好好监视他，\x01",
            "避免引起什么事故的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "那就拜托您啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x9,
        (
            "#104F#5P真是的……\x01",
            "不管到哪里都这么失礼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x8,
        "#792F呵呵……\x02",
    )

    CloseMessageWindow()

    def lambda_9FB5():
        OP_6D(2660, 0, -300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FB5)

    def lambda_9FCD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9FCD)

    def lambda_9FDB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FDB)
    Sleep(50)

    def lambda_9FEE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9FEE)

    def lambda_9FFC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FFC)
    Sleep(50)

    def lambda_A00F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A00F)

    def lambda_A01D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A01D)
    Sleep(50)

    def lambda_A030():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A030)

    def lambda_A03E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A03E)
    Sleep(200)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #484
        0x8,
        (
            "#791F王都的艾南那里\x01",
            "就由我来联络吧。\x02\x03",

            "愿女神保佑诸位。\x01",
            "请一路小心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x3F5, 1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0BE")
    RemoveParty(0x4, 0xFF)
    Jump("loc_A0C1")

    label("loc_A0BE")

    RemoveParty(0x3, 0xFF)

    label("loc_A0C1")

    Sleep(1000)
    OP_AD(0x2400AF, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1484)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x124), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A142")
    ShowSaveMenu()

    label("loc_A142")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    OP_20(0xBB8)
    Sleep(2000)
    OP_21()
    OP_A3(0x1484)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/C3108   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_7CDA end

    def Function_25_A17B(): pass

    label("Function_25_A17B")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(4430, 0, 3750, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(327000, 0)
    OP_6E(272, 0)
    SetChrPos(0x8, 5380, 0, 2500, 270)
    OP_4A(0x8, 255)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #485
        0x8,
        (
            "#792F……原来如此。\x01",
            "大致状况我已经明白了\x02\x03",

            "#791F军队的守备队\x01",
            "之前也已经开始行动了。\x02\x03",

            "现在的战况已经基本稳定，\x01",
            "不需要协会的援助了。\x02\x03",

            "#790F…………………………………\x02\x03",

            "#792F……是吗，接下来\x01",
            "要去的是『红莲之塔』吗。\x02\x03",

            "#791F明白了……祝大家好运。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #486
        0x8,
        (
            "#792F……还是和以前一样\x01",
            "什么事都憋不住，\x02\x03",

            "#791F真的是一点也没变啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #487
        0x8,
        (
            "#790F#5P好了……\x02\x03",

            "这样的话\x01",
            "接下来我也有的忙了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10FF)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_A17B end

    def Function_26_A40C(): pass

    label("Function_26_A40C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A423")
    Call(0, 38)
    Call(0, 40)

    label("loc_A423")

    OP_4A(0x8, 255)
    SetChrPos(0x8, 3380, 0, 2350, 0)
    OP_6D(2880, 0, 2070, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(310, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4DD")

    ChrTalk(    #488
        0x8,
        (
            "#792F#5P哎呀……\x01",
            "比我预想中来得要早啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A541")

    label("loc_A4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A516")

    ChrTalk(    #489
        0x8,
        (
            "#792F#5P呵……\x01",
            "比我预想的慢了好多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A541")

    label("loc_A516")


    ChrTalk(    #490
        0x8,
        (
            "#792F#5P呵呵……\x01",
            "你们来的正是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A541")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A73A")

    ChrTalk(    #491
        0x108,
        "#2P喔～你……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrPos(0x101, 1770, 0, -6100, 0)
    SetChrPos(0x102, 1770, 0, -6100, 0)
    SetChrPos(0xF8, 1770, 0, -6100, 0)
    SetChrPos(0xF9, 1770, 0, -6100, 0)

    def lambda_A5B1():
        OP_6D(2800, 0, 750, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5B1)

    def lambda_A5C9():
        OP_67(0, 6190, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A5C9)

    def lambda_A5E1():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A5E1)

    def lambda_A5F1():
        OP_6E(311, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A5F1)
    OP_43(0x101, 0x1, 0x0, 0x1B)
    OP_8C(0x8, 180, 400)
    OP_43(0x102, 0x1, 0x0, 0x1C)

    def lambda_A616():
        OP_8E(0xFE, 0xDAC, 0x0, 0x4B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A616)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x1D)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x1E)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #492
        0x108,
        (
            "#075F#6P为什么你知道\x01",
            "我们会来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x8,
        (
            "#791F这次导力停止现象\x01",
            "的原因就是那座浮游都市吧？\x02\x03",

            "如今一切导力设施都已经瘫痪，\x01",
            "你们要想确认各地情况的话当然\x01",
            "也就只能徒步巡视各地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x108,
        "#072F#6P嗯嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        "#1016F#6P啊哈哈，确实是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A934")

    label("loc_A73A")


    ChrTalk(    #496
        0x101,
        "#2P呵呵，不愧是雾香姐……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrPos(0x101, 1590, 0, -8119, 0)
    SetChrPos(0x102, 1590, 0, -8119, 0)
    SetChrPos(0xF8, 1590, 0, -8119, 0)
    SetChrPos(0xF9, 1590, 0, -8119, 0)

    def lambda_A7A8():
        OP_6D(2800, 0, 750, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7A8)

    def lambda_A7C0():
        OP_67(0, 6190, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A7C0)

    def lambda_A7D8():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A7D8)

    def lambda_A7E8():
        OP_6E(311, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A7E8)
    OP_43(0x101, 0x1, 0x0, 0x1B)
    OP_8C(0x8, 180, 400)
    OP_43(0x102, 0x1, 0x0, 0x1C)

    def lambda_A80D():
        OP_8E(0xFE, 0xDAC, 0x0, 0x4B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A80D)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x1D)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x1E)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #497
        0x101,
        (
            "#1008F#6P你已经猜想到\x01",
            "我们会来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x8,
        (
            "#791F这次导力停止现象\x01",
            "的原因就是那座浮游都市吧？\x02\x03",

            "如今一切导力设施都已经瘫痪，\x01",
            "你们要想确认各地情况的话当然\x01",
            "也就只能徒步巡视各地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x101,
        "#1016F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x102,
        "#1040F#6P确实是这样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A934")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A96C")

    ChrTalk(    #501
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "不愧是雾香姐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9E3")

    label("loc_A96C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9AA")

    ChrTalk(    #502
        0x106,
        (
            "#051F#6P嘿……\x01",
            "真是位可靠的女中豪杰啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9E3")

    label("loc_A9AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9E3")

    ChrTalk(    #503
        0x103,
        (
            "#021F#6P呵呵……\x01",
            "真是个可以靠的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9E3")


    ChrTalk(    #504
        0x8,
        (
            "#792F嗯，这里的情况\x01",
            "正如你们想象中的一样。\x02\x03",

            "#790F作为利贝尔王国\x01",
            "最先进的导力都市，\x01",
            "这里的混乱情况也是倍加严重。\x02\x03",

            "虽然玛多克工房长努力\x01",
            "做了各种补救对策，\x01",
            "但仍然无法平息市民们的不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x101,
        (
            "#1015F#6P这样啊……\x01",
            "工房长现在怎么样了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB08")

    ChrTalk(    #506
        0x107,
        (
            "#063F#6P要是我们可以\x01",
            "帮的上他的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB3E")

    label("loc_AB08")


    ChrTalk(    #507
        0x102,
        (
            "#1043F#6P要是有什么需要的话，\x01",
            "我们可以去帮他……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3E")


    ChrTalk(    #508
        0x8,
        (
            "#792F嗯，有空的话就去\x01",
            "顺便看看也好。\x02\x03",

            "#790F另外……\x01",
            "还有一个问题就是卡鲁迪亚隧道了。\x02\x03",

            "由于照明系统的消失，\x01",
            "现在想从那里通行就变得十分困难。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACE3")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇通过卡鲁迪亚隧道而来到蔡斯】\x01",                # 0
            "【◇曾进入过卡鲁迪亚隧道的艾尔·雷登一侧】\x01",      # 1
            "【◇曾进入过卡鲁迪亚隧道的蔡斯一侧】\x01",            # 2
            "【◇没有进入卡鲁迪亚隧道】\x01",                      # 3
            "【◇不变更】\x01",                                    # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ACBF"),
        (1, "loc_ACC8"),
        (2, "loc_ACD1"),
        (3, "loc_ACDA"),
        (SWITCH_DEFAULT, "loc_ACE3"),
    )


    label("loc_ACBF")

    OP_A2(0x2081)
    OP_A2(0x2082)
    Jump("loc_ACE3")

    label("loc_ACC8")

    OP_A2(0x2081)
    OP_A3(0x2082)
    Jump("loc_ACE3")

    label("loc_ACD1")

    OP_A3(0x2081)
    OP_A2(0x2082)
    Jump("loc_ACE3")

    label("loc_ACDA")

    OP_A3(0x2081)
    OP_A3(0x2082)
    Jump("loc_ACE3")

    label("loc_ACE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD5D")

    ChrTalk(    #509
        0x101,
        (
            "#1007F#6P嗯……\x02\x03",

            "我们就是通过那里\x01",
            "来到蔡斯的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x102,
        (
            "#1042F#6P那里的可视范围十分狭小，\x01",
            "确实非常危险呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE33")

    label("loc_AD5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ADD1")

    ChrTalk(    #511
        0x101,
        (
            "#1007F#6P嗯……\x01",
            "我们也去那里看过了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x102,
        (
            "#1042F#6P那里的可视范围十分狭小，\x01",
            "状况确实非常危险呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE33")

    label("loc_ADD1")


    ChrTalk(    #513
        0x101,
        (
            "#1007F#6P那个地方确实不能\x01",
            "没有照明系统啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x102,
        (
            "#1042F#6P如果失去了照明系统\x01",
            "那就太危险了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE33")


    ChrTalk(    #515
        0x8,
        (
            "#792F还有啊……\x02\x03",

            "#790F听说亚尔摩村的水泵装置坏掉了，\x01",
            "现在温泉已经不能使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0x101,
        "#1015F#6P这样啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AED9")

    ChrTalk(    #517
        0x107,
        (
            "#561F#6P那毛婆婆一定会\x01",
            "很烦恼呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEFF")

    label("loc_AED9")


    ChrTalk(    #518
        0x102,
        (
            "#1043F#6P那毛婆婆肯定\x01",
            "很沮丧吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEFF")


    ChrTalk(    #519
        0x8,
        (
            "#792F……大概吧。\x02\x03",

            "#790F那么也把你们的事情\x01",
            "说给我听听吧，\x02\x03",

            "在『红莲之塔』分别以后\x01",
            "到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF96")

    ChrTalk(    #520
        0x108,
        "#072F#6P啊啊，其实……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFB3")

    label("loc_AF96")


    ChrTalk(    #521
        0x101,
        "#1002F#6P嗯，其实呢……\x02",
    )

    CloseMessageWindow()

    label("loc_AFB3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #522
        (
            "\x07\x05艾丝蒂尔告诉雾香\x01",
            "『浮游都市』出现了的缘由以及\x01",
            "说明了关于『零力场发生器』的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #523
        0x8,
        (
            "#792F原来是这样。\x01",
            "那个果然就是『辉之环』……\x02\x03",

            "#790F在『四轮之塔』被他们占据时，\x01",
            "这种事态就注定要发生了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0CC")

    ChrTalk(    #524
        0x108,
        "#074F#6P啊啊……确实是这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0EF")

    label("loc_B0CC")


    ChrTalk(    #525
        0x102,
        "#1035F#6P是啊……确实是那样。\x02",
    )

    CloseMessageWindow()

    label("loc_B0EF")


    ChrTalk(    #526
        0x101,
        (
            "#1003F#6P那么说的话\x01",
            "我们费那么大力气到那四座塔里战斗\x01",
            "根本就是毫无意义的嘛……\x02\x03",

            "#1007F真是气死人了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x8,
        (
            "#792F已经过去的事情，\x01",
            "再后悔也没有意义啊。\x02\x03",

            "#791F而且你们在塔内\x01",
            "新发现的一些事情\x01",
            "似乎也很有意义。\x02\x03",

            "现在最重要的是从中找出有用的信息\x01",
            "留至以后活用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0x101,
        "#1025F#6P雾香姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0x8,
        (
            "#791F……那么你们就尽快\x01",
            "把通讯器修好可以吗？\x02\x03",

            "这也是为了迎来光明的未来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2A1")

    ChrTalk(    #530
        0x108,
        (
            "#075F#6P啊……\x02\x03",

            "#072F光顾着聊天，\x01",
            "把正事都给忘了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B412")

    ChrTalk(    #531
        0x101,
        "#1016F#6P啊哈哈……明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #532
        0x101,
        (
            "#1006F#2P那么，提妲。\x01",
            "这里就拜托你了哦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #533
        0x107,
        "#061F#6P嗯，交给我吧⊙\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 16)
    SetChrPos(0x107, 5350, 0, 2490, 270)
    OP_8C(0x8, 90, 0)
    OP_8C(0x101, 0, 0)
    OP_6D(3430, 0, 2620, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #534
        0x107,
        "#560F……嗯，这样就完成了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #535
        "\x07\x05提妲打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_B546")

    label("loc_B412")


    ChrTalk(    #536
        0x101,
        "#1016F#6P啊哈哈……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0x102,
        (
            "#1040F#6P那我马上就开始\x01",
            "设置『零力场发生器』。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 16)
    SetChrPos(0x102, 5350, 0, 2490, 270)
    OP_8C(0x8, 90, 0)
    OP_6D(3430, 0, 2620, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #538
        0x102,
        "#1035F……这样就可以了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #539
        "\x07\x05约修亚打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_B546")

    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #540
        0x8,
        (
            "#791F#5P……真不愧是拉赛尔博士。\x01",
            "能发明出这么好的东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)

    def lambda_B5FD():
        OP_6D(2850, 0, 1670, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B5FD)

    def lambda_B615():
        OP_67(0, 6270, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B615)

    def lambda_B62D():
        OP_6E(325, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B62D)

    def lambda_B63D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B63D)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B662")
    OP_8C(0x107, 180, 400)
    Jump("loc_B669")

    label("loc_B662")

    OP_8C(0x102, 180, 400)

    label("loc_B669")

    WaitChrThread(0x101, 0x0)

    ChrTalk(    #541
        0x8,
        (
            "#791F#2P你们大家也辛苦了，\x01",
            "这下真是帮了大忙了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B743")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇恢复全部的通讯器】\x01",        # 0
            "【◇只恢复这里的通讯器】\x01",      # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B731"),
        (1, "loc_B73A"),
        (SWITCH_DEFAULT, "loc_B743"),
    )


    label("loc_B731")

    OP_A2(0x2001)
    OP_A2(0x2003)
    Jump("loc_B743")

    label("loc_B73A")

    OP_A3(0x2001)
    OP_A3(0x2003)
    Jump("loc_B743")

    label("loc_B743")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9A5")

    ChrTalk(    #542
        0x101,
        "#1016F#6P嘿嘿，不用客气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x108,
        (
            "#071F#6P哈哈，怎么了。\x01",
            "你以前可没这么直白啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x8,
        (
            "#792F#2P这真是遗憾啊。\x02\x03",

            "#791F我倒是觉得应该没有\x01",
            "比我更直白的人了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B914")

    ChrTalk(    #545
        0x108,
        (
            "#075F#6P与其说是直白，\x01",
            "倒不如说是毫不客气。\x02\x03",

            "#070F好了，这样一来，\x01",
            "所有支部的通信器就都修好了。\x02\x03",

            "确认各地的状况\x01",
            "进行执行任务的报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)

    ChrTalk(    #546
        0x8,
        (
            "#790F#2P真是辛苦大家了啊。\x02\x03",

            "如此一来，\x01",
            "我们就可以迅速作出各种应对策略了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0x108,
        "#070F还有其他事情要帮忙吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9A2")

    label("loc_B914")


    ChrTalk(    #548
        0x108,
        (
            "#075F#6P用不着\x01",
            "那么客气啦。\x02\x03",

            "#070F嗯，接下来准备照这个样子，\x01",
            "把其他几个协会的通讯器也\x01",
            "给修理好……\x02\x03",

            "不过，这里没有其他需要帮忙的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9A2")

    Jump("loc_BD13")

    label("loc_B9A5")


    ChrTalk(    #549
        0x101,
        "#1016F#6P嘿嘿，不用客气。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F4")

    ChrTalk(    #550
        0x102,
        "#1040F#6P能帮上忙就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA19")

    label("loc_B9F4")


    ChrTalk(    #551
        0x102,
        "#1040F#2P能帮上忙就比什么都好。\x02",
    )

    CloseMessageWindow()

    label("loc_BA19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBD4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA94")

    ChrTalk(    #552
        0x103,
        (
            "#020F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么现在就将各地的任务\x01",
            "做个总结报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB05")

    label("loc_BA94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB05")

    ChrTalk(    #553
        0x106,
        (
            "#051F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，结合各地的状况\x01",
            "那就进行任务的汇报吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB05")

    OP_59()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)

    ChrTalk(    #554
        0x8,
        (
            "#791F#2P真是辛苦大家了。\x02\x03",

            "这样一来\x01",
            "这样我们就可以迅速作出各种应对策略了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBA4")

    ChrTalk(    #555
        0x103,
        "#020F还有其他事情要帮忙吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBD1")

    label("loc_BBA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBD1")

    ChrTalk(    #556
        0x106,
        "#051F还有什么要帮忙的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_BBD1")

    Jump("loc_BD13")

    label("loc_BBD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC3F")

    ChrTalk(    #557
        0x103,
        (
            "#020F#6P嗯，准备继续\x01",
            "把其他协会的通讯器\x01",
            "也修好…\x02\x03",

            "不过，这里没有其他事情要帮忙了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD13")

    label("loc_BC3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCAA")

    ChrTalk(    #558
        0x106,
        (
            "#051F#6P嗯，准备继续\x01",
            "把其他协会的通讯器\x01",
            "也修好…\x02\x03",

            "不过，这里没有其他事情要帮忙了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD13")

    label("loc_BCAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD13")

    ChrTalk(    #559
        0x107,
        (
            "#560F这个嘛，准备继续\x01",
            "把其他协会的通讯器\x01",
            "也修好…\x02\x03",

            "不过，这里没有其他事情要帮忙了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD13")


    ChrTalk(    #560
        0x8,
        (
            "#791F#2P雷斯顿要塞就在附近，\x01",
            "治安方面应该没什么问题，不过…\x01",
            "你们还是看看告示板上的委托吧。\x02\x03",

            "如果有时间的话\x01",
            "去中央工房和亚尔摩温泉看看吧，\x01",
            "确认一下那里的状况就可以了。\x02\x03",

            "那里好像有什么麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x101,
        "#1006F#6P嗯，知道啦！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE18")

    ChrTalk(    #562
        0x102,
        "#1040F#6P明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE2F")

    label("loc_BE18")


    ChrTalk(    #563
        0x102,
        "#1040F#2P明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_BE2F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #564
        (
            "\x07\x05※因为通讯器已经修好了，可以呼叫在其他支部待命的同伴，\x01",
            "  将他们召集来蔡斯支部。\x01",
            "　想呼叫的时候请在接待处选择『呼叫同伴』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_4B(0x8, 255)
    OP_A2(0x2005)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BEDE")
    OP_A2(0x2091)
    Jump("loc_BEE1")

    label("loc_BEDE")

    OP_A3(0x2091)

    label("loc_BEE1")

    OP_28(0x9B, 0x2, 0x10)
    OP_28(0x9B, 0x1, 0x20)
    OP_6D(2510, 0, -2680, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2510, 0, -2680, 180)
    SetChrPos(0x1, 2510, 0, -2680, 180)
    SetChrPos(0x2, 2510, 0, -2680, 180)
    SetChrPos(0x3, 2510, 0, -2680, 180)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_26_A40C end

    def Function_27_BF81(): pass

    label("Function_27_BF81")

    OP_8E(0xFE, 0xF3C, 0x0, 0xFFFFF268, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10EA, 0x0, 0xFFFFFD44, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_BF81 end

    def Function_28_BFB1(): pass

    label("Function_28_BFB1")

    OP_8E(0xFE, 0xA5A, 0x0, 0xFFFFF38A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD02, 0x0, 0xFFFFFD44, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_BFB1 end

    def Function_29_BFE1(): pass

    label("Function_29_BFE1")

    OP_8E(0xFE, 0xF3C, 0x0, 0xFFFFF268, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10EA, 0x0, 0xFFFFF8F8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_29_BFE1 end

    def Function_30_C011(): pass

    label("Function_30_C011")

    OP_8E(0xFE, 0xA5A, 0x0, 0xFFFFF38A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD02, 0x0, 0xFFFFF8F8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_30_C011 end

    def Function_31_C041(): pass

    label("Function_31_C041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C05B")
    Return()

    label("loc_C05B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C07B")
    Call(0, 38)
    Call(0, 40)
    FadeToBright(0, 0)

    label("loc_C07B")

    OP_22(0xC3, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)

    ChrTalk(    #565
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_C0F9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C0F9)

    def lambda_C107():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C107)
    Sleep(100)

    def lambda_C11A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C11A)
    OP_8C(0x3, 0, 400)

    ChrTalk(    #566
        0x8,
        "#791F#3P这么快就有联络了呢。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(3970, 0, 2180, 0)
    OP_67(0, 6980, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    SetChrPos(0x101, 1770, 0, -6100, 0)
    SetChrPos(0x102, 1770, 0, -6100, 0)
    SetChrPos(0xF8, 1770, 0, -6100, 0)
    SetChrPos(0xF9, 1770, 0, -6100, 0)
    OP_8E(0x8, 0x14E6, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0x14E6, 0x0, 0x9BA, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(700)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_43(0x101, 0x0, 0x0, 0x20)

    ChrTalk(    #567
        0x8,
        (
            "#792F这里是游击士协会\x01",
            "蔡斯支部……\x02\x03",

            "#791F……啊啊，是你吗。\x02\x03",

            "这边的通讯也是刚刚才修复好。\x02\x03",

            "……嗯嗯，是啊。\x01",
            "他们正好就在这里。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF9, 0x1)

    def lambda_C2EA():
        OP_6D(3720, 0, 1230, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2EA)

    def lambda_C302():
        OP_67(0, 6580, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C302)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #568
        0x101,
        "#1004F#6P（找我们的……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0x102,
        "#1044F#6P（好像有话要说。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0x8,
        (
            "#792F……嗯……嗯。\x02\x03",

            "………………………………………\x02\x03",

            "#791F……明白了。\x01",
            "我会转告给他们的。\x02\x03",

            "关于这边的状况\x01",
            "以后有机会再联络吧。\x02\x03",

            "#792F……是啊。\x01",
            "只有互相加油了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C449")

    ChrTalk(    #571
        0x108,
        (
            "#073F#6P雾香，\x01",
            "是哪里的联络？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C473")

    label("loc_C449")


    ChrTalk(    #572
        0x101,
        (
            "#1015F#6P雾香姐姐，\x01",
            "是哪里来的联络？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C473")


    def lambda_C479():
        OP_6D(3080, 0, 500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C479)
    OP_8E(0x8, 0x14B4, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #573
        0x8,
        (
            "#791F是王都支部的艾南先生。\x02\x03",

            "好像是艾莉茜娅女王\x01",
            "有事情要和你们说，\x02\x03",

            "如果到格兰赛尔附近来的话，\x01",
            "希望你们去王城一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #574
        0x101,
        "#1004F#6P女王陛下！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C598")

    ChrTalk(    #575
        0x103,
        (
            "#023F#6P这真让人惊讶……\x01",
            "到底是什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C617")

    label("loc_C598")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5D9")

    ChrTalk(    #576
        0x106,
        (
            "#052F#6P真是让人吃惊啊……\x01",
            "到底有什么事呢?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C617")

    label("loc_C5D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C617")

    ChrTalk(    #577
        0x108,
        (
            "#073F#6P那真是让人吃惊啊。\x01",
            "到底有什么事呢?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C617")


    ChrTalk(    #578
        0x8,
        (
            "#792F我没有具体问。\x02\x03",

            "#790F不过似乎是在通信器中\x01",
            "难以说清楚的事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #579
        0x101,
        (
            "#1015F#6P通信中无法说清楚的事……\x02\x03",

            "#1026F是吗，导力通讯\x01",
            "存在被人监听的危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #580
        0x102,
        (
            "#1042F#6P看来是\x01",
            "比较机密的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0x8,
        (
            "#792F不过倒是没要求你们马上就去，\x01",
            "看样子并不是什么急事，\x02\x03",

            "#791F路过王都的时候顺便去看看就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #582
        0x101,
        "#1006F#6P这样的啊……知道了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C793")

    ChrTalk(    #583
        0x108,
        "#070F#6P嗯，那就过去一趟吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7B2")

    label("loc_C793")


    ChrTalk(    #584
        0x102,
        "#1040F#6P赶快过去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_C7B2")

    OP_A2(0x2006)
    OP_28(0x9B, 0x1, 0x100)
    OP_28(0x9B, 0x1, 0x200)
    OP_28(0x9B, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_6D(2510, 0, -2680, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2510, 0, -2680, 180)
    SetChrPos(0x1, 2510, 0, -2680, 180)
    SetChrPos(0x2, 2510, 0, -2680, 180)
    SetChrPos(0x3, 2510, 0, -2680, 180)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_31_C041 end

    def Function_32_C86F(): pass

    label("Function_32_C86F")

    OP_43(0x101, 0x1, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x1C)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x0, 0x1D)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x1E)
    WaitChrThread(0xF9, 0x1)
    Return()

    # Function_32_C86F end

    def Function_33_C8A0(): pass

    label("Function_33_C8A0")

    OP_8E(0xFE, 0x636, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC12, 0x0, 0xFFFFFD44, 0x7D0, 0x0)

    def lambda_C8CE():

        label("loc_C8CE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C8CE")

    QueueWorkItem2(0xFE, 2, lambda_C8CE)
    Return()

    # Function_33_C8A0 end

    def Function_34_C8DA(): pass

    label("Function_34_C8DA")

    OP_8E(0xFE, 0x9E2, 0x0, 0xFFFFEE26, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF0A, 0x0, 0xFFFFFD44, 0x7D0, 0x0)

    def lambda_C908():

        label("loc_C908")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C908")

    QueueWorkItem2(0xFE, 2, lambda_C908)
    Return()

    # Function_34_C8DA end

    def Function_35_C914(): pass

    label("Function_35_C914")

    OP_8E(0xFE, 0x636, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x91A, 0x0, 0xFFFFFAD8, 0x7D0, 0x0)

    def lambda_C942():

        label("loc_C942")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C942")

    QueueWorkItem2(0xFE, 2, lambda_C942)
    Return()

    # Function_35_C914 end

    def Function_36_C94E(): pass

    label("Function_36_C94E")

    OP_8E(0xFE, 0x9E2, 0x0, 0xFFFFEE26, 0x7D0, 0x0)
    OP_8E(0xFE, 0x122A, 0x0, 0xFFFFFC68, 0x7D0, 0x0)

    def lambda_C97C():

        label("loc_C97C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C97C")

    QueueWorkItem2(0xFE, 2, lambda_C97C)
    Return()

    # Function_36_C94E end

    def Function_37_C988(): pass

    label("Function_37_C988")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9A8")
    Call(0, 38)
    Call(0, 40)
    FadeToBright(0, 0)

    label("loc_C9A8")

    Fade(1000)
    OP_6D(2920, 0, 700, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(315000, 0)
    OP_6E(332, 0)
    SetChrPos(0x101, 4360, 0, -720, 0)
    SetChrPos(0x102, 3220, 0, -700, 0)
    SetChrPos(0xF8, 4600, 0, -1800, 0)
    SetChrPos(0xF9, 3230, 0, -1800, 0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    OP_0D()

    ChrTalk(    #585
        0x8,
        (
            "#790F#2P啊……\x01",
            "发生什么事了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x101,
        "#1002F#6P嗯，其实呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #587
        (
            "\x07\x05将内燃引擎的事情告诉了雾香，\x01",
            "并拜托雾香帮忙和雷斯顿要塞\x01",
            "进行联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #588
        0x8,
        (
            "#791F#2P呵呵，这也是我们\x01",
            "游击士应该做的工作啊。\x02\x03",

            "要塞的通信器应该也已经恢复了，\x01",
            "现在就和他们联络看看吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB61():
        OP_6D(3670, 0, 1500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB61)
    OP_8E(0x8, 0x14E6, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0x14E6, 0x0, 0x9BA, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x1)
    OP_22(0x83, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(    #589
        0x8,
        (
            "#792F……………………………\x02\x03",

            "#790F您好，这里是游击士协会\x01",
            "的蔡斯支部──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #590
        0x8,
        (
            "#792F──是这样啊。\x02\x03",

            "#791F我知道了，\x01",
            "这就转告他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)

    def lambda_CC9E():
        OP_6D(2920, 0, 700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC9E)
    OP_8E(0x8, 0x14B4, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    Sleep(700)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #591
        0x8,
        (
            "#792F#2P──现在要塞里\x01",
            "也没有『内燃引擎』了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0x101,
        "#1020F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0x102,
        "#1044F#6P这是怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0x8,
        (
            "#790F#2P他们准备将它那东西返还给中央工房，\x01",
            "就使用一艘警备艇进行运送。\x02\x03",

            "但那艘警备艇却因为导力停止现象\x01",
            "而紧急迫降在托兰特平原道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE26")

    ChrTalk(    #596
        0x108,
        "#070F#6P原来如此，事情是那样吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE91")

    label("loc_CE26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE5D")

    ChrTalk(    #597
        0x103,
        "#027F#6P原来如此，事情是那样呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE91")

    label("loc_CE5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE91")

    ChrTalk(    #598
        0x106,
        "#051F#6P原来如此，事情是那样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_CE91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CEE3")

    ChrTalk(    #599
        0x107,
        (
            "#560F#6P那么说的话，只要去找\x01",
            "那艘警备艇上的士兵就可以了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF1D")

    label("loc_CEE3")


    ChrTalk(    #600
        0x102,
        (
            "#1040F#6P这样的话，去拜托\x01",
            "警备艇的负责人不就行了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF1D")


    ChrTalk(    #601
        0x8,
        (
            "#792F#2P嗯，没错。\x02\x03",

            "#791F警备艇应该降落在\x01",
            "托兰特平原道一带了，\x01",
            "你们去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x200C)
    OP_28(0xC2, 0x1, 0x10)
    OP_28(0xC2, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_37_C988 end

    def Function_38_CF84(): pass

    label("Function_38_CF84")

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
        (0, "loc_CFFE"),
        (1, "loc_D004"),
        (SWITCH_DEFAULT, "loc_D00A"),
    )


    label("loc_CFFE")

    OP_A2(0x1200)
    Jump("loc_D00A")

    label("loc_D004")

    OP_A2(0x1201)
    Jump("loc_D00A")

    label("loc_D00A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D018")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_D01C")

    label("loc_D018")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_D01C")

    Return()

    # Function_38_CF84 end

    def Function_39_D01D(): pass

    label("Function_39_D01D")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D057")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_D071")

    label("loc_D057")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_D071")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_39_D01D end

    def Function_40_D083(): pass

    label("Function_40_D083")

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

    # Function_40_D083 end

    SaveToFile()

Try(main)
