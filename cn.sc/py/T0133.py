from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0133   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0133.x',
        MapIndex            = 10,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0133_1 ._SN',
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
        '潘杜老人',                             # 9
        '士兵斯科特',                           # 10
        '士兵哈罗德',                           # 11
        '士兵拉科斯',                           # 12
        '士兵霍帕',                             # 13
        '士兵安托斯',                           # 14
        '士兵多明戈',                           # 15
        '士兵迈尔斯',                           # 16
        '士兵马克斯',                           # 17
        '戴恩副队长',                           # 18
        '阿斯顿队长',                           # 19
        '基蒂',                                 # 20
        '鲁克',                                 # 21
        '帕特',                                 # 22
        '克露莎',                               # 23
        '艾娅莉',                               # 24
        '阿鲁姆',                               # 25
        '胡里奥',                               # 26
        '利吉',                                 # 27
        '商人',                                 # 28
        '旅行者',                               # 29
        '旅行者',                               # 30
        '鸽子',                                 # 31
        '鸽子',                                 # 32
        '鸽子',                                 # 33
        '鸽子',                                 # 34
        '鸽子',                                 # 35
        '梅尔达斯',                             # 36
        '安敦',                                 # 37
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
        'ED6_DT07/CH01250 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
        'ED6_DT07/CH01770 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH01160 ._CH',             # 05
        'ED6_DT07/CH01060 ._CH',             # 06
        'ED6_DT07/CH01070 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
        'ED6_DT07/CH01760 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
        'ED6_DT07/CH01220 ._CH',             # 0D
        'ED6_DT07/CH01230 ._CH',             # 0E
        'ED6_DT07/CH01730 ._CH',             # 0F
        'ED6_DT07/CH01731 ._CH',             # 10
        'ED6_DT07/CH01000 ._CH',             # 11
        'ED6_DT07/CH01040 ._CH',             # 12
        'ED6_DT07/CH01044 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01250P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
        'ED6_DT07/CH01770P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH01160P._CP',             # 05
        'ED6_DT07/CH01060P._CP',             # 06
        'ED6_DT07/CH01070P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
        'ED6_DT07/CH01760P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
        'ED6_DT07/CH01220P._CP',             # 0D
        'ED6_DT07/CH01230P._CP',             # 0E
        'ED6_DT07/CH01730P._CP',             # 0F
        'ED6_DT07/CH01731P._CP',             # 10
        'ED6_DT07/CH01000P._CP',             # 11
        'ED6_DT07/CH01040P._CP',             # 12
        'ED6_DT07/CH01044P._CP',             # 13
    )

    DeclNpc(
        X                   = 3275,
        Z                   = 0,
        Y                   = 2522,
        Direction           = 180,
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
        X                   = 19740,
        Z                   = 0,
        Y                   = 42720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 19740,
        Z                   = 0,
        Y                   = 38120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46620,
        Z                   = 0,
        Y                   = 12420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51800,
        Z                   = 0,
        Y                   = 12420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26440,
        Z                   = 0,
        Y                   = 70940,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29720,
        Z                   = 0,
        Y                   = 70940,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57650,
        Z                   = 0,
        Y                   = 70870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40910,
        Z                   = 0,
        Y                   = 14450,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51560,
        Z                   = 0,
        Y                   = 45820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51560,
        Z                   = 0,
        Y                   = 47080,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 46300,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49120,
        Z                   = 0,
        Y                   = 48300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49870,
        Z                   = 0,
        Y                   = 50090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 30420,
        Z                   = 0,
        Y                   = 40090,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 32700,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 31830,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51830,
        Z                   = 0,
        Y                   = 35210,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59490,
        Z                   = 0,
        Y                   = 44360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 60290,
        Z                   = 0,
        Y                   = 42390,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 60630,
        Z                   = 0,
        Y                   = 41060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 59130,
        Z                   = 0,
        Y                   = 41140,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x145,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3290,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 55210,
        Z                   = 10300,
        Y                   = 44150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )


    DeclActor(
        TriggerX            = -300,
        TriggerZ            = 0,
        TriggerY            = 4140,
        TriggerRange        = 800,
        ActorX              = -300,
        ActorZ              = 1000,
        ActorY              = 4140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53450,
        TriggerZ            = 10300,
        TriggerY            = 47970,
        TriggerRange        = 800,
        ActorX              = 53450,
        ActorZ              = 10000,
        ActorY              = 47970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51520,
        TriggerZ            = 10300,
        TriggerY            = 46970,
        TriggerRange        = 1700,
        ActorX              = 51520,
        ActorZ              = 11300,
        ActorY              = 46970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_556",          # 00, 0
        "Function_1_6B0",          # 01, 1
        "Function_2_76F",          # 02, 2
        "Function_3_8EC",          # 03, 3
        "Function_4_93F",          # 04, 4
        "Function_5_992",          # 05, 5
        "Function_6_9B6",          # 06, 6
        "Function_7_AF7",          # 07, 7
        "Function_8_BFC",          # 08, 8
        "Function_9_C42",          # 09, 9
        "Function_10_117A",        # 0A, 10
        "Function_11_1342",        # 0B, 11
        "Function_12_15B2",        # 0C, 12
        "Function_13_16D0",        # 0D, 13
        "Function_14_16FE",        # 0E, 14
        "Function_15_1708",        # 0F, 15
    )


    def Function_0_556(): pass

    label("Function_0_556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5B1")
    SetChrPos(0x8, 55710, 10300, 47580, 270)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 54840, 10300, 46250, 270)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599")
    Jump("loc_5AE")

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9")
    SetChrFlags(0x19, 0x80)
    Jump("loc_5AE")

    label("loc_5A9")

    SetChrFlags(0x19, 0x80)

    label("loc_5AE")

    Jump("loc_6AF")

    label("loc_5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_5D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D0")
    ClearChrFlags(0x24, 0x80)

    label("loc_5D0")

    Jump("loc_6AF")

    label("loc_5D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_61E")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_6AF")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_670")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_66D")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_66D")

    Jump("loc_6AF")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_69B")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_698")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)

    label("loc_698")

    Jump("loc_6AF")

    label("loc_69B")

    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)

    label("loc_6AF")

    Return()

    # Function_0_556 end

    def Function_1_6B0(): pass

    label("Function_1_6B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_6E7")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_6FC")

    label("loc_6E7")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_6FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_714")
    OP_B1("t0133_n")
    Jump("loc_751")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_748")
    OP_B1("t0133_y")
    OP_11(0xDB, 0xB7, 0xFF, 0x0, 0xFF78, 0x0)
    Jump("loc_751")

    label("loc_748")

    OP_B1("t0133_n")

    label("loc_751")

    Jump("loc_762")

    label("loc_754")

    OP_B1("t0133_n")
    ClearMapFlags(0x10)

    label("loc_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E")
    OP_64(0x2, 0x1)

    label("loc_76E")

    Return()

    # Function_1_6B0 end

    def Function_2_76F(): pass

    label("Function_2_76F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_794")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8D6")

    label("loc_794")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8D6")

    label("loc_7AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8D6")

    label("loc_7C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8D6")

    label("loc_7DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8D6")

    label("loc_7F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_811")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8D6")

    label("loc_811")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8D6")

    label("loc_82A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_843")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8D6")

    label("loc_843")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8D6")

    label("loc_85C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8D6")

    label("loc_875")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8D6")

    label("loc_88E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8D6")

    label("loc_8A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8D6")

    label("loc_8C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8D6")

    label("loc_8EB")

    Return()

    # Function_2_76F end

    def Function_3_8EC(): pass

    label("Function_3_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93E")
    OP_8D(0xFE, 48000, 49500, 50500, 50500, 3000)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    TurnDirection(0xFE, 0x14, 400)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93B")

    Jump("Function_3_8EC")

    label("loc_93E")

    Return()

    # Function_3_8EC end

    def Function_4_93F(): pass

    label("Function_4_93F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_991")
    OP_8D(0xFE, 48000, 49000, 50500, 48000, 3000)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98E")
    TurnDirection(0xFE, 0x15, 400)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_98E")

    Jump("Function_4_93F")

    label("loc_991")

    Return()

    # Function_4_93F end

    def Function_5_992(): pass

    label("Function_5_992")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B5")
    OP_8D(0xFE, 25948, 43568, 37838, 41060, 3000)
    Jump("Function_5_992")

    label("loc_9B5")

    Return()

    # Function_5_992 end

    def Function_6_9B6(): pass

    label("Function_6_9B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF6")
    OP_8E(0xFE, 0xE132, 0x0, 0x114D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBD7E, 0x0, 0x114D6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xBD7E, 0x0, 0xA10E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFA8C, 0x0, 0xA10E, 0x7D0, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFA8C, 0x0, 0x48EE, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFA8C, 0x0, 0x38EA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC60C, 0x0, 0x38EA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xC60C, 0x0, 0xA10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE6B4, 0x0, 0xA10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE6B4, 0x0, 0xCAF8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE132, 0x0, 0xCAF8, 0x7D0, 0x0)
    Jump("Function_6_9B6")

    label("loc_AF6")

    Return()

    # Function_6_9B6 end

    def Function_7_AF7(): pass

    label("Function_7_AF7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFB")
    OP_8E(0xFE, 0x9FCE, 0x0, 0x3872, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7620, 0x0, 0x3872, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7620, 0x0, 0x9C5E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x9C5E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x1098C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6E6E, 0x0, 0x1098C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x1098C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x3872, 0x7D0, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Jump("Function_7_AF7")

    label("loc_BFB")

    Return()

    # Function_7_AF7 end

    def Function_8_BFC(): pass

    label("Function_8_BFC")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8D(0xFE, 51380, 38050, 58760, 42200, 0)

    label("loc_C1E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C41")
    OP_8D(0xFE, 51380, 38050, 58760, 42200, 1500)
    Jump("loc_C1E")

    label("loc_C41")

    Return()

    # Function_8_BFC end

    def Function_9_C42(): pass

    label("Function_9_C42")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5B")
    Call(0, 11)
    Jump("loc_D5B")

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CA3")

    ChrTalk(    #0
        0xFE,
        (
            "你们难得\x01",
            "回来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "别总是工作，\x01",
            "偶尔也要享受一下啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5B")

    label("loc_CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF4")

    ChrTalk(    #2
        0xFE,
        (
            "导力器瘫痪的理由\x01",
            "现在还不能确定…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "真是的……\x01",
            "但真是头疼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5B")

    label("loc_CF4")


    ChrTalk(    #4
        0xFE,
        (
            "那个跟岛一样的东西\x01",
            "出现在天空的同时，\x01",
            "时钟就停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "似乎不是偶然啊。\x01",
            "肯定有什么关联吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5B")

    Jump("loc_1176")

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DDC")

    ChrTalk(    #6
        0xFE,
        (
            "那个料理我\x01",
            "还是记得很清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "呵呵，去问问城里的\x01",
            "婆婆们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "在我们那个年代，\x01",
            "几乎谁都会做呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECD")

    label("loc_DDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E07")
    Call(1, 0)
    Jump("loc_ECD")

    label("loc_E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E59")

    ChrTalk(    #9
        0xFE,
        (
            "鲁克那小子\x01",
            "似乎也恢复健康了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "玩闹时的叫喊声\x01",
            "在这里都能听到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECD")

    label("loc_E59")


    ChrTalk(    #11
        0xFE,
        (
            "鲁克那小子\x01",
            "似乎也恢复健康了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "玩闹时的叫喊声\x01",
            "在这里都能听到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "哈哈，洛连特还是适合\x01",
            "灿烂的阳光啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_ECD")

    Jump("loc_1176")

    label("loc_ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F55")

    ChrTalk(    #14
        0xFE,
        (
            "和帝国的互不侵犯条约顺利签订，\x01",
            "对利贝尔来说也是一个里程碑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "对『百日战役』的牺牲者\x01",
            "也算是一个交代和缅怀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE7")

    label("loc_F55")


    ChrTalk(    #16
        0xFE,
        (
            "说起来的话，今天\x01",
            "好像就是互不侵犯条约的签字仪式啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "利贝尔也要踏出\x01",
            "崭新的一步了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "对『百日战役』的牺牲者\x01",
            "也算是一个交代和缅怀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FE7")

    Jump("loc_1176")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_10BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(    #19
        0xFE,
        (
            "嗯，钟楼的钟声\x01",
            "听起来很不舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "这些……那些都\x01",
            "一定是因为这次的浓雾吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B9")

    label("loc_104D")


    ChrTalk(    #21
        0xFE,
        (
            "今天早上也是\x01",
            "一片浓雾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "是心理问题吗，总觉得钟声\x01",
            "也变得很不对劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "听起来似乎\x01",
            "很不舒服。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10B9")

    Jump("loc_1176")

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1176")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(    #24
        0xFE,
        (
            "今天也没问题了，\x01",
            "希望能永远和平啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "战争永远都是\x01",
            "我们不希望看见的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1176")

    label("loc_111B")


    ChrTalk(    #26
        0xFE,
        "嗯…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "今天也没问题了，\x01",
            "希望能永远和平啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "战争永远都是\x01",
            "我们不希望看见的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1176")

    TalkEnd(0x8)
    Return()

    # Function_9_C42 end

    def Function_10_117A(): pass

    label("Function_10_117A")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118C")
    Call(0, 11)
    Jump("loc_133E")

    label("loc_118C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_11E3")

    ChrTalk(    #29
        0xFE,
        (
            "可是导力器\x01",
            "为什么会突然停止呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #30
        0xFE,
        (
            "果然是因为那座岛\x01",
            "的缘故吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133E")

    label("loc_11E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1240")

    ChrTalk(    #31
        0xFE,
        (
            "导力器为什么会突然瘫痪呢，\x01",
            "谁也想不出理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "果然是因为天上\x01",
            "那座岛屿吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133E")

    label("loc_1240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")

    ChrTalk(    #33
        0xFE,
        (
            "最近一直在这钟楼上\x01",
            "眺望那座岛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "那么大的东西能漂浮在空中，\x01",
            "真让人不敢相信啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "导力器瘫痪也是\x01",
            "因为它的缘故吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "那么想的话，\x01",
            "总有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_133E")

    label("loc_12F0")


    ChrTalk(    #37
        0xFE,
        (
            "导力器瘫痪的时候也是\x01",
            "那座岛出现的时候…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "说实话，总有种\x01",
            "不好的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133E")

    TalkEnd(0x23)
    Return()

    # Function_10_117A end

    def Function_11_1342(): pass

    label("Function_11_1342")

    OP_4A(0x23, 255)
    OP_4A(0x8, 255)
    TurnDirection(0x23, 0x101, 400)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #39
        0x23,
        "哦，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x102, 400)

    ChrTalk(    #40
        0x23,
        (
            "啊，怎么回事，\x01",
            "约修亚也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "呼呼，\x01",
            "有一阵没见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1040F您两位\x01",
            "还和以前一样，没什么变化啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x23,
        "这里还是老样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x23,
        (
            "城中有很多老机械，\x01",
            "工作总是很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "现在就在检查\x01",
            "钟楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "时钟的时针不动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1004F啊，说起来的话，\x01",
            "这座钟的时针…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#1035F……是导力式的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x23,
        (
            "啊啊，城里的导力器\x01",
            "全都不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x23,
        (
            "啊，不知道有没有用，\x01",
            "我打算给时钟加些油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "你们也是难得\x01",
            "回来一次啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "不要总想着工作，\x01",
            "偶尔也要放松一下。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #53
        0x102,
        "#1040F呵呵，说的是啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #54
        0x101,
        (
            "#1001F嗯，闲下来的话\x01",
            "会休息一下的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2099)
    OP_8C(0x23, 180, 0)
    OP_8C(0x8, 135, 0)
    OP_4B(0x23, 255)
    OP_4B(0x8, 255)
    OP_A2(0x1)
    OP_A2(0x3)
    Return()

    # Function_11_1342 end

    def Function_12_15B2(): pass

    label("Function_12_15B2")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_166C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1655")

    ChrTalk(    #55
        0xFE,
        "女神啊，拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "请一定让游击士们\x01",
            "把药的材料收集全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1669")

    label("loc_1655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1669")
    Call(1, 4)
    Jump("loc_1669")

    label("loc_1669")

    Jump("loc_16CC")

    label("loc_166C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_168F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_1688")
    Call(1, 2)
    Jump("loc_168C")

    label("loc_1688")

    Call(1, 1)

    label("loc_168C")

    Jump("loc_16CC")

    label("loc_168F")


    ChrTalk(    #57
        0xFE,
        "女神啊，拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "让我顺利接近那位\x01",
            "美丽的姐姐吧…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CC")

    TalkEnd(0x24)
    Return()

    # Function_12_15B2 end

    def Function_13_16D0(): pass

    label("Function_13_16D0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400D1, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_13_16D0 end

    def Function_14_16FE(): pass

    label("Function_14_16FE")

    NewScene("ED6_DT21/T0133   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_14_16FE end

    def Function_15_1708(): pass

    label("Function_15_1708")

    NewScene("ED6_DT21/T0133   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1708 end

    SaveToFile()

Try(main)
