from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '提妲',                                 # 9
        '玲',                                   # 10
        '管家雷蒙德',                           # 11
        '西莫鲁',                               # 12
        '王都市民',                             # 13
        '王都市民',                             # 14
        '旅行者',                               # 15
        '旅行者',                               # 16
        '王国军士兵',                           # 17
        '王国军士兵',                           # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '王国军士兵',                           # 21
        '王国军士兵',                           # 22
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
        'ED6_DT07/CH00060 ._CH',             # 00
        'ED6_DT27/CH03510 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01350 ._CH',             # 04
        'ED6_DT26/CH20291 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01140 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
        'ED6_DT27/CH03510P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01350P._CP',             # 04
        'ED6_DT26/CH20291P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01140P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
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
        X                   = -19780,
        Z                   = 1000,
        Y                   = 29190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -19840,
        Z                   = 1000,
        Y                   = 27860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2270,
        Z                   = 250,
        Y                   = 13100,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -2670,
        Z                   = 360,
        Y                   = 14060,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4700,
        Z                   = 250,
        Y                   = 18020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4700,
        Z                   = 250,
        Y                   = 17020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2960,
        Z                   = 1000,
        Y                   = 37310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2960,
        Z                   = 1000,
        Y                   = 37310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -350,
        Z                   = 250,
        Y                   = 12110,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -19000,
        Z                   = 1000,
        Y                   = -7160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 19000,
        Z                   = 1000,
        Y                   = -7160,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20860,
        Z                   = 1000,
        Y                   = 31020,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    DeclEvent(
        X                   = 21800,
        Y                   = 1000,
        Z                   = 33960,
        Range               = 21000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x7CD8,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 9000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 9000,
        ActorZ              = 0,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = -9000,
        ActorZ              = 0,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13400,
        TriggerZ            = 0,
        TriggerY            = 27000,
        TriggerRange        = 800,
        ActorX              = 13400,
        ActorZ              = 0,
        ActorY              = 27000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13400,
        TriggerZ            = 0,
        TriggerY            = 21000,
        TriggerRange        = 800,
        ActorX              = 13400,
        ActorZ              = 0,
        ActorY              = 21000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13400,
        TriggerZ            = 0,
        TriggerY            = 11000,
        TriggerRange        = 800,
        ActorX              = 13400,
        ActorZ              = 0,
        ActorY              = 11000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13400,
        TriggerZ            = 0,
        TriggerY            = 5000,
        TriggerRange        = 800,
        ActorX              = 13400,
        ActorZ              = 0,
        ActorY              = 5000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13400,
        TriggerZ            = 0,
        TriggerY            = 27000,
        TriggerRange        = 800,
        ActorX              = -13400,
        ActorZ              = 0,
        ActorY              = 27000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13400,
        TriggerZ            = 0,
        TriggerY            = 21000,
        TriggerRange        = 800,
        ActorX              = -13400,
        ActorZ              = 0,
        ActorY              = 21000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13400,
        TriggerZ            = 0,
        TriggerY            = 11000,
        TriggerRange        = 800,
        ActorX              = -13400,
        ActorZ              = 0,
        ActorY              = 11000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13400,
        TriggerZ            = 0,
        TriggerY            = 5000,
        TriggerRange        = 800,
        ActorX              = -13400,
        ActorZ              = 0,
        ActorY              = 5000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22170,
        TriggerZ            = 1000,
        TriggerY            = 29080,
        TriggerRange        = 800,
        ActorX              = -22170,
        ActorZ              = 1500,
        ActorY              = 29080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_46E",          # 00, 0
        "Function_1_578",          # 01, 1
        "Function_2_607",          # 02, 2
        "Function_3_784",          # 03, 3
        "Function_4_7A8",          # 04, 4
        "Function_5_845",          # 05, 5
        "Function_6_8E2",          # 06, 6
        "Function_7_937",          # 07, 7
        "Function_8_9CC",          # 08, 8
        "Function_9_B1E",          # 09, 9
        "Function_10_BEA",         # 0A, 10
        "Function_11_C92",         # 0B, 11
        "Function_12_D23",         # 0C, 12
        "Function_13_F4C",         # 0D, 13
        "Function_14_1103",        # 0E, 14
        "Function_15_1252",        # 0F, 15
        "Function_16_13A3",        # 10, 16
        "Function_17_14E2",        # 11, 17
        "Function_18_1584",        # 12, 18
        "Function_19_164F",        # 13, 19
        "Function_20_1697",        # 14, 20
        "Function_21_1827",        # 15, 21
        "Function_22_2187",        # 16, 22
        "Function_23_21B9",        # 17, 23
        "Function_24_21EB",        # 18, 24
        "Function_25_2231",        # 19, 25
        "Function_26_228D",        # 1A, 26
        "Function_27_23D4",        # 1B, 27
        "Function_28_23FB",        # 1C, 28
        "Function_29_243D",        # 1D, 29
        "Function_30_246B",        # 1E, 30
        "Function_31_2D5B",        # 1F, 31
        "Function_32_2DAD",        # 20, 32
        "Function_33_2E1D",        # 21, 33
        "Function_34_2EB6",        # 22, 34
    )


    def Function_0_46E(): pass

    label("Function_0_46E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_50B")

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_4DC")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_50B")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_4F0")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Jump("loc_50B")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_END)), "loc_4FA")
    Jump("loc_50B")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_50B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_521")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_577")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_537")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_577")

    label("loc_537")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_547"),
        (106, "loc_55F"),
        (SWITCH_DEFAULT, "loc_577"),
    )


    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_55C")

    Jump("loc_577")

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_574")
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_574")

    Jump("loc_577")

    label("loc_577")

    Return()

    # Function_0_46E end

    def Function_1_578(): pass

    label("Function_1_578")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230062)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_END)), "loc_598")
    OP_64(0xA, 0x1)
    Jump("loc_59D")

    label("loc_598")

    OP_72(0x3, 0x10)

    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_5CC")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)

    label("loc_5CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EA")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    Jump("loc_606")

    label("loc_5EA")

    SoundDistance(0x1CB, 0xFFFFFF7E, 0xFA, 0x3E1C, 0x7D0, 0x61A8, 0x64, 0x0)

    label("loc_606")

    Return()

    # Function_1_578 end

    def Function_2_607(): pass

    label("Function_2_607")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_76E")

    label("loc_62C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_645")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_76E")

    label("loc_645")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_76E")

    label("loc_65E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_76E")

    label("loc_677")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_76E")

    label("loc_690")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_76E")

    label("loc_6A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C2")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_76E")

    label("loc_6C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_76E")

    label("loc_6DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_76E")

    label("loc_6F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_76E")

    label("loc_70D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_726")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_76E")

    label("loc_726")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_76E")

    label("loc_73F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_758")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_76E")

    label("loc_758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_76E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_783")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_76E")

    label("loc_783")

    Return()

    # Function_2_607 end

    def Function_3_784(): pass

    label("Function_3_784")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A7")
    OP_8D(0xFE, -4370, 20680, 4760, 11150, 2000)
    Jump("Function_3_784")

    label("loc_7A7")

    Return()

    # Function_3_784 end

    def Function_4_7A8(): pass

    label("Function_4_7A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_844")
    OP_8E(0xFE, 0xFFFFB5C8, 0x3E8, 0xFFFFE408, 0x7D0, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFB5C8, 0x3E8, 0x84D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFBA78, 0x3E8, 0x891C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDCD8, 0x3E8, 0x891C, 0x7D0, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFFBA78, 0x3E8, 0x891C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB5C8, 0x3E8, 0x84D0, 0x7D0, 0x0)
    Jump("Function_4_7A8")

    label("loc_844")

    Return()

    # Function_4_7A8 end

    def Function_5_845(): pass

    label("Function_5_845")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E1")
    OP_8E(0xFE, 0x4A38, 0x3E8, 0xFFFFE408, 0x7D0, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x4A38, 0x3E8, 0x84D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4588, 0x3E8, 0x891C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2328, 0x3E8, 0x891C, 0x7D0, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x4588, 0x3E8, 0x891C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4A38, 0x3E8, 0x84D0, 0x7D0, 0x0)
    Jump("Function_5_845")

    label("loc_8E1")

    Return()

    # Function_5_845 end

    def Function_6_8E2(): pass

    label("Function_6_8E2")

    TalkBegin(0xA)

    ChrTalk(    #0
        0xFE,
        (
            "总、总之，只有镇定下来\x01",
            "仔细寻找了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "那孩子可能\x01",
            "有什么理由也不一定。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_6_8E2 end

    def Function_7_937(): pass

    label("Function_7_937")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_97B")

    ChrTalk(    #2
        0xFE,
        (
            "那孩子一定在\x01",
            "离宫中的某处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "请一定要找到～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C8")

    label("loc_97B")


    ChrTalk(    #4
        0xFE,
        (
            "啊～真是的，那孩子\x01",
            "就像捉弄人似的消失了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "绝对不能原谅～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_9C8")

    TalkEnd(0xB)
    Return()

    # Function_7_937 end

    def Function_8_9CC(): pass

    label("Function_8_9CC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #6
        0xFE,
        (
            "呼，凝视着喷泉\x01",
            "心就不可思议地平静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "水真是有各种各样的效果啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1A")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A7E")

    ChrTalk(    #8
        0xFE,
        "穿白裙子的女孩吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "我见过这样的孩子\x01",
            "在这附近玩呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1A")

    label("loc_A7E")


    ChrTalk(    #10
        0xFE,
        (
            "……哦？\x01",
            "穿白裙子的女孩吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "这么说来，好像有见过\x01",
            "在这附近玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1004F知道去哪儿了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "嗯……抱歉，\x01",
            "记不起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1007F……是吗。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B1A")

    TalkEnd(0xC)
    Return()

    # Function_8_9CC end

    def Function_9_B1E(): pass

    label("Function_9_B1E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_B7A")

    ChrTalk(    #15
        0xFE,
        (
            "能让飞船飞起来，\x01",
            "让喷泉喷出水来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "导力真是不可思议啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE6")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_BE6")

    ChrTalk(    #17
        0xFE,
        (
            "对了，这喷泉\x01",
            "也是导力驱动的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "世界上，各种各样的东西\x01",
            "都是靠导力驱动的\x01",
            "老爸是这么说的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE6")

    TalkEnd(0xD)
    Return()

    # Function_9_B1E end

    def Function_10_BEA(): pass

    label("Function_10_BEA")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_C1B")

    ChrTalk(    #19
        0xFE,
        "公主！　我对你……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8E")

    label("loc_C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_C8E")

    ChrTalk(    #20
        0xFE,
        "嗯～原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "确实这个离宫\x01",
            "是相当适合王室的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "只是待在这里\x01",
            "就感觉自己也成了王子一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8E")

    TalkEnd(0xE)
    Return()

    # Function_10_BEA end

    def Function_11_C92(): pass

    label("Function_11_C92")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_CCE")

    ChrTalk(    #23
        0xFE,
        (
            "不行，王子！\x01",
            "下人们会看见的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1F")

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_D1F")

    ChrTalk(    #24
        0xFE,
        (
            "呵呵，他真是\x01",
            "个浪漫主义者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "他要是王子殿下\x01",
            "那我就是公主殿下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1F")

    TalkEnd(0xF)
    Return()

    # Function_11_C92 end

    def Function_12_D23(): pass

    label("Function_12_D23")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DA3")

    ChrTalk(    #26
        0xFE,
        (
            "听说签字仪式上\x01",
            "会有国内外许多媒体到场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "呼呼呼，我的初次杂志亮相\x01",
            "说不定就近在咫尺了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E52")

    label("loc_DA3")


    ChrTalk(    #28
        0xFE,
        (
            "听说签字仪式上\x01",
            "会有国内外许多媒体到场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "看来报道阵容已经得到批准\x01",
            "使用照相机拍摄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "……我的杂志初次亮相难道近在咫尺了！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_E52")

    Jump("loc_F48")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EC2")

    ChrTalk(    #32
        0xFE,
        (
            "不仅是原精锐部队，\x01",
            "情报部还有白刃战的专家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "如果在市区发生战斗，\x01",
            "绝对不能轻视哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F48")

    label("loc_EC2")


    ChrTalk(    #34
        0xFE,
        (
            "万一要与情报部作战，\x01",
            "必须提高警惕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不仅是原精锐部队，\x01",
            "他们还有白刃战的专家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "如果在市区发生战斗，\x01",
            "绝对不能轻视哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F48")

    TalkEnd(0x10)
    Return()

    # Function_12_D23 end

    def Function_13_F4C(): pass

    label("Function_13_F4C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(    #37
        0xFE,
        (
            "从诞辰庆典开始\x01",
            "事件持续不断\x01",
            "到底是令人紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "只希望签字仪式\x01",
            "能平安结束就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1041")

    label("loc_FC7")


    ChrTalk(    #39
        0xFE,
        "签字仪式也近在眼前了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "从诞辰庆典开始\x01",
            "事件持续不断\x01",
            "到底是令人紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "只希望签字仪式\x01",
            "能平安结束就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1041")

    Jump("loc_10FF")

    label("loc_1044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1094")

    ChrTalk(    #42
        0xFE,
        (
            "能借助各位游击士的力量\x01",
            "可真令人放心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "一起努力吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10FF")

    label("loc_1094")


    ChrTalk(    #44
        0xFE,
        (
            "听说今后要和\x01",
            "游击士协会配合工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "能借助各位游击士的力量\x01",
            "可真令人放心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "一起努力吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_10FF")

    TalkEnd(0x11)
    Return()

    # Function_13_F4C end

    def Function_14_1103(): pass

    label("Function_14_1103")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(    #47
        0xFE,
        (
            "如你所见，\x01",
            "连喷泉都停了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "真是连平常的景色\x01",
            "也有导力器渗透其中啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1167")

    Jump("loc_124E")

    label("loc_116A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_11E0")

    ChrTalk(    #49
        0xFE,
        (
            "多亏希德中校的指挥\x01",
            "袭击似乎没有造成多大损害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "作为佯攻的特务兵\x01",
            "也真是找错了对象啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124E")

    label("loc_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_124E")

    ChrTalk(    #51
        0xFE,
        "现在还没什么异常。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "只是，刚才副队长从通讯室\x01",
            "慌慌张张跑了出去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "……可得做好心理准备啊。\x02",
    )

    CloseMessageWindow()

    label("loc_124E")

    TalkEnd(0x12)
    Return()

    # Function_14_1103 end

    def Function_15_1252(): pass

    label("Function_15_1252")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12D1")

    ChrTalk(    #54
        0xFE,
        (
            "虽然从这里看不见，\x01",
            "听说瓦雷利亚湖上出现了\x01",
            "不可思议的物体不是吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "连协会，\x01",
            "也不知道其真面目吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D1")

    Jump("loc_139F")

    label("loc_12D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1336")

    ChrTalk(    #56
        0xFE,
        (
            "刚才爱尔莎大使\x01",
            "和共和国议员来访了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "看来是来熟悉会场\x01",
            "和洽谈来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139F")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_139F")

    ChrTalk(    #58
        0xFE,
        (
            "这么说来，共和国的\x01",
            "议员们都住在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "似乎是为了签字仪式的准备和视察，\x01",
            "提前来到现场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139F")

    TalkEnd(0x13)
    Return()

    # Function_15_1252 end

    def Function_16_13A3(): pass

    label("Function_16_13A3")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_143E")

    ChrTalk(    #60
        0xFE,
        (
            "和守护哈肯门的时候\x01",
            "相比，这里还很平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "那边怎么说都经常\x01",
            "受到帝国的威胁嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "待在那城堡里的话，晚上\x01",
            "可是能睡得很香呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143E")

    Jump("loc_14DE")

    label("loc_1441")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_14AF")

    ChrTalk(    #63
        0xFE,
        (
            "余党的事件结束后\x01",
            "感觉真是转眼间的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "竟然能那么快解决，\x01",
            "他们也真有点可怜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DE")

    label("loc_14AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_14DE")

    ChrTalk(    #65
        0xFE,
        "抱歉我正在巡逻。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "不要妨碍我。\x02",
    )

    CloseMessageWindow()

    label("loc_14DE")

    TalkEnd(0x14)
    Return()

    # Function_16_13A3 end

    def Function_17_14E2(): pass

    label("Function_17_14E2")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1580")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1533")

    ChrTalk(    #67
        0xFE,
        "这个房间是通信室。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "现在贝尔克副队长在里面哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1580")

    label("loc_1533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1580")

    ChrTalk(    #69
        0xFE,
        (
            "这个房间现在\x01",
            "是作为通信室来使用的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "无关人员\x01",
            "是不能进去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1580")

    TalkEnd(0x15)
    Return()

    # Function_17_14E2 end

    def Function_18_1584(): pass

    label("Function_18_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1591")
    Return()

    label("loc_1591")

    EventBegin(0x2)
    OP_4A(0x15, 255)
    TurnDirection(0x15, 0x0, 0)
    TurnDirection(0x0, 0x15, 0)
    TurnDirection(0x1, 0x15, 0)
    TurnDirection(0x2, 0x15, 0)
    TurnDirection(0x3, 0x15, 0)

    ChrTalk(    #71
        0x15,
        "这个房间是通信室。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x15,
        "请不要随便进去。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x15, 20860, 1000, 31020, 270)
    SetChrPos(0x0, 20020, 1000, 32960, 270)
    SetChrPos(0x1, 20020, 1000, 32960, 270)
    SetChrPos(0x2, 20020, 1000, 32960, 270)
    SetChrPos(0x3, 20020, 1000, 32960, 270)
    OP_0D()
    OP_4B(0x15, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_18_1584 end

    def Function_19_164F(): pass

    label("Function_19_164F")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #73
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_19_164F end

    def Function_20_1697(): pass

    label("Function_20_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E0")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #74
        "\x07\x05长椅周围没有任何人。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #75
        0x101,
        (
            "#1015F长椅和树丛的\x01",
            "缝隙里也没有吗……\x02\x03",

            "#1004F啊，难不成\x01",
            "在树丛里面！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1761")

    ChrTalk(    #76
        0x107,
        (
            "#067F简、简直是\x01",
            "真正的猫啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1761")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1796")

    ChrTalk(    #77
        0x106,
        (
            "#552F喂喂……\x01",
            "又不是真正的猫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_1796")


    ChrTalk(    #78
        0x103,
        (
            "#524F真是的……\x01",
            "又不是真正的猫。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BC")


    ChrTalk(    #79
        0x101,
        "#1016F还是不行？\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_A2(0x1611)
    OP_28(0x89, 0x1, 0x40)
    Jump("loc_1826")

    label("loc_17E0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05长椅周围没有任何人。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1826")

    Return()

    # Function_20_1697 end

    def Function_21_1827(): pass

    label("Function_21_1827")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_183E")
    Call(0, 33)
    Call(0, 34)

    label("loc_183E")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-19850, 1000, 2930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x5, 0x10)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1D)
    OP_73(0x5)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C2E")
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #81
        0x101,
        (
            "#1005F真是的……\x01",
            "什么嘛，那个公爵！\x02\x03",

            "抬高自己\x01",
            "还贬低科洛丝！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AAB")

    ChrTalk(    #82
        0x106,
        (
            "#053F哎，别那么冲动嘛。\x02\x03",

            "#050F我倒觉得那公爵说的\x01",
            "也有一番道理。\x02\x03",

            "站在高处的人\x01",
            "是不能显示出迷惘的。\x02\x03",

            "必须时时向周围的人\x01",
            "展现自己的正确。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1026F但是，科洛丝……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        (
            "#051F啊啊，是啊。\x02\x03",

            "就算那个公爵不说\x01",
            "公主肯定明白的。\x02\x03",

            "现在我们只要守护着\x01",
            "公主找到答案就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1025F啊……\x01",
            "嗯……明白了。\x02\x03",

            "#1006F好！\x01",
            "寻找迷路的孩子，再度开始吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x106,
        "#051F哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2B")

    label("loc_1AAB")


    ChrTalk(    #87
        0x103,
        (
            "#026F哎，别那么冲动嘛。\x02\x03",

            "#020F那公爵先生，意外的\x01",
            "也会说点正经话嘛。\x02\x03",

            "站在高处的人\x01",
            "是不能显示出迷惘的。\x02\x03",

            "必须时时向周围的人\x01",
            "展现自己的正确引导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1026F但是，科洛丝……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        (
            "#021F嗯嗯，是啊。\x02\x03",

            "#027F就算公爵先生不说\x01",
            "公主殿下应该也明白的。\x02\x03",

            "现在只要守护着公主殿下\x01",
            "等她找到答案就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1025F啊……\x01",
            "嗯……明白了。\x02\x03",

            "#1006F好！\x01",
            "寻找迷路的孩子，再度开始吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        "#021F哎哎。\x02",
    )

    CloseMessageWindow()

    label("loc_1C2B")

    Jump("loc_217C")

    label("loc_1C2E")

    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x18)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6A")
    OP_43(0x104, 0x1, 0x0, 0x19)
    Jump("loc_1C97")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C82")
    OP_43(0x107, 0x1, 0x0, 0x19)
    Jump("loc_1C97")

    label("loc_1C82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C97")
    OP_43(0x108, 0x1, 0x0, 0x19)

    label("loc_1C97")

    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #92
        0x101,
        (
            "#1005F真是的……\x01",
            "什么嘛，那个公爵！\x02\x03",

            "抬高自己\x01",
            "还贬低科洛丝！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x105,
        (
            "#047F不，叔叔的责难\x01",
            "要我说也是当然。\x02\x03",

            "身为王族的义务……\x01",
            "这确实是存在的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1002F但、但是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0C")

    ChrTalk(    #95
        0x104,
        (
            "#030F唔，知名度吗……\x02\x03",

            "#035F历史上，几乎默默无闻地\x01",
            "坐在君主之位上\x01",
            "却留下了伟大业绩的人也不少。\x02\x03",

            "埃雷波尼亚也有过因为内乱\x01",
            "使得有力的皇子们相继死去\x01",
            "而最后，无名的皇子继承了皇位……\x02\x03",

            "那位皇子，日后成为了被称为中兴之祖的\x01",
            "伟大皇帝。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 187, 400)

    ChrTalk(    #96
        0x105,
        "#040F#2P是说德莱凯尔斯大帝吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x104,
        (
            "#031F呼，知道的真清楚。\x02\x03",

            "#030F所以我想公主殿下\x01",
            "您无需多虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x105,
        (
            "#045F#2P呵呵，或许吧。\x02\x03",

            "#049F但我的心理准备\x01",
            "正如叔叔所说的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1026F科洛丝……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 127, 400)
    Jump("loc_20E3")

    label("loc_1F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2068")

    ChrTalk(    #100
        0x108,
        (
            "#074F嗯，共和国是通过选举\x01",
            "来选出大总统的嘛。\x02\x03",

            "虽说这是王族的义务,\x01",
            "你只不过还没完全进入角色……\x02\x03",

            "#070F但是，那个公爵阁下的情况，\x01",
            "倒是坏的知名度高涨了。\x02\x03",

            "认为他比你\x01",
            "更适合当下任国王的人\x01",
            "整个利贝尔都找不到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 187, 400)
    Sleep(400)

    ChrTalk(    #101
        0x105,
        (
            "#043F#2P这……\x01",
            "或许是吧。\x02\x03",

            "#049F但我的心理准备\x01",
            "正如叔叔所说的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1026F科洛丝……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 127, 400)
    Sleep(400)
    Jump("loc_20E3")

    label("loc_2068")


    ChrTalk(    #103
        0x105,
        (
            "#049F即使不谈这义务……\x02\x03",

            "但我的心理准备\x01",
            "正如叔叔所说的一样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20CD")

    ChrTalk(    #104
        0x107,
        "#063F科洛丝……\x02",
    )

    CloseMessageWindow()

    label("loc_20CD")


    ChrTalk(    #105
        0x101,
        "#1026F科洛丝……\x02",
    )

    CloseMessageWindow()

    label("loc_20E3")


    ChrTalk(    #106
        0x105,
        (
            "#542F我能在这里\x01",
            "遇见叔叔真是太好了。\x02\x03",

            "让我重新注意到了\x01",
            "自己不足的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1025F是哦……\x02\x03",

            "#1006F好！\x01",
            "寻找迷路的孩子，重新开始吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x105,
        "#041F好。\x02",
    )

    CloseMessageWindow()

    label("loc_217C")

    OP_A2(0x1614)
    OP_71(0x5, 0x10)
    EventEnd(0x0)
    Return()

    # Function_21_1827 end

    def Function_22_2187(): pass

    label("Function_22_2187")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFB79E, 0x3E8, 0x99C, 0x7D0, 0x0)
    OP_8C(0xFE, 296, 400)
    Return()

    # Function_22_2187 end

    def Function_23_21B9(): pass

    label("Function_23_21B9")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFB384, 0x3E8, 0xC26, 0x7D0, 0x0)
    OP_8C(0xFE, 127, 400)
    Return()

    # Function_23_21B9 end

    def Function_24_21EB(): pass

    label("Function_24_21EB")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFABF0, 0x3E8, 0xAE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB406, 0x3E8, 0x672, 0x7D0, 0x0)
    OP_8C(0xFE, 29, 400)
    Return()

    # Function_24_21EB end

    def Function_25_2231(): pass

    label("Function_25_2231")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFABF0, 0x3E8, 0xAE6, 0x7D0, 0x0)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB014, 0x3E8, 0x94C, 0x7D0, 0x0)
    OP_8C(0xFE, 101, 400)
    Return()

    # Function_25_2231 end

    def Function_26_228D(): pass

    label("Function_26_228D")

    EventBegin(0x0)
    OP_11(0x9E, 0xFF, 0xFF, 0x88B8, 0x47C70, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x9, 2710, 250, 13190, 45)
    SetChrPos(0x8, 1030, 250, 12140, 90)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    SetChrPos(0x10, 19000, 1000, 16000, 360)
    SetChrPos(0x11, -1190, 1000, 33830, 360)
    SetChrPos(0x12, 19000, 1000, 17500, 360)
    SetChrPos(0x13, -2690, 1000, 33830, 360)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x13, 2)
    SetChrSubChip(0x13, 0)
    OP_6D(4920, 0, 22470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4910, 0)
    OP_6C(43000, 0)
    OP_6E(350, 0)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    OP_43(0x8, 0x1, 0x0, 0x1B)
    OP_43(0x10, 0x1, 0x0, 0x1C)
    OP_43(0x11, 0x1, 0x0, 0x1D)
    OP_43(0x12, 0x1, 0x0, 0x1C)
    OP_43(0x13, 0x1, 0x0, 0x1D)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4312   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_26_228D end

    def Function_27_23D4(): pass

    label("Function_27_23D4")

    ClearChrFlags(0xFE, 0x80)

    label("loc_23D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23FA")
    OP_97(0xFE, 0xFFFFFFCE, 0x3E9E, 0xFFFEA070, 0x1770, 0x1)
    Jump("loc_23D9")

    label("loc_23FA")

    Return()

    # Function_27_23D4 end

    def Function_28_23FB(): pass

    label("Function_28_23FB")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4A38, 0x3E8, 0x8BF6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB636, 0x3E8, 0x8BF6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB636, 0x3E8, 0xFFFFF45C, 0x7D0, 0x0)
    Return()

    # Function_28_23FB end

    def Function_29_243D(): pass

    label("Function_29_243D")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x49CA, 0x3E8, 0x8426, 0x7D0, 0x0)
    OP_8E(0xFE, 0x49CA, 0x3E8, 0xFFFFF45C, 0x7D0, 0x0)
    Return()

    # Function_29_243D end

    def Function_30_246B(): pass

    label("Function_30_246B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_247E")
    Call(0, 33)

    label("loc_247E")

    AddParty(0x6, 0xF8, 0xFF)
    AddParty(0x2E, 0xFF, 0xFF)
    OP_6D(370, 1000, 42730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrPos(0x107, 0, 0, 24820, 360)
    SetChrPos(0x12F, 0, 0, 24820, 360)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1D)
    OP_73(0x0)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1F)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(3000)

    def lambda_252D():
        OP_6D(460, 1000, 34360, 3000)
        ExitThread()

    QueueWorkItem(0x12F, 0, lambda_252D)

    def lambda_2545():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_2545)
    WaitChrThread(0x12F, 0x0)
    WaitChrThread(0x12F, 0x1)

    NpcTalk(    #109
        0x12F,
        "少女的声音",
        "#5P啊，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    def lambda_2581():
        OP_8E(0xFE, 0x3B6, 0x3E8, 0x80C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_2581)
    Sleep(500)

    def lambda_25A1():
        OP_8E(0xFE, 0xFFFFFF38, 0x3E8, 0x80C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_25A1)
    WaitChrThread(0x12F, 0x1)
    WaitChrThread(0x107, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25F7")

    ChrTalk(    #110
        0x107,
        (
            "#560F#6P姐姐，阿加特哥哥。\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2620")

    label("loc_25F7")


    ChrTalk(    #111
        0x107,
        (
            "#560F#6P姐姐、雪拉姐。\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2620")


    ChrTalk(    #112
        0x12F,
        (
            "#260F嗯，这么快\x01",
            "就结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1006F我不是说了吗？\x01",
            "只是交调查的报告书而已。\x02\x03",

            "乖乖在协会\x01",
            "等着不就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x12F,
        (
            "#262F呀，好过分！\x02\x03",

            "玲只是想和艾丝蒂尔\x01",
            "在一起……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x107, 400)

    ChrTalk(    #115
        0x12F,
        (
            "#262F#5P喏，提妲也\x01",
            "说点什么啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)

    ChrTalk(    #116
        0x107,
        (
            "#064F#6P我，我？\x02\x03",

            "#067F嗯～想和姐姐们\x01",
            "在一起是没错……\x02\x03",

            "但这是工作，不能\x01",
            "太任性嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x12F,
        "#269F#5P哼～是吗。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12F, 0, 400)
    Sleep(500)

    ChrTalk(    #118
        0x12F,
        (
            "#263F#5P那么艾丝蒂尔\x01",
            "就归玲了哦。\x02\x03",

            "因为提妲太不合群了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x107,
        (
            "#065F#6P啊呜……\x01",
            "玲好过分啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1016F#5P好啦好啦，不准吵架。\x02\x03",

            "提妲是姐姐\x01",
            "要稍微大度点嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #121
        0x107,
        (
            "#562F#6P但，但是但是……\x02\x03",

            "不知什么时候开始\x01",
            "就叫得那么亲密……\x02\x03",

            "#063F姐姐……\x01",
            "你不要我了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1016F真是的～那种事\x01",
            "怎么可能嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x107, 0x40)
    OP_8F(0x101, 0xFFFFFF4C, 0x3E8, 0x82D2, 0x7D0, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 5)
    SetChrSubChip(0x107, 0)
    OP_99(0x107, 0x0, 0x2, 0x3E8)
    Sleep(500)
    TurnDirection(0x12F, 0x107, 400)
    OP_62(0x12F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x101,
        (
            "#1006F#5P喂喂，怎么了～？\x02\x03",

            "摆出那张脸\x01",
            "我会抱紧你的哦～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x107,
        (
            "#067F#6P啊，真是的。\x01",
            "姐姐你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x12F,
        (
            "#1301F#5P啊啊！\x01",
            "提妲，太狡猾了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29DD")

    ChrTalk(    #126
        0x106,
        (
            "#053F#5P哎呀呀。\x01",
            "真受不了。\x02\x03",

            "#051F别说这个了……\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2E")

    label("loc_29DD")


    ChrTalk(    #127
        0x103,
        (
            "#021F#5P艾丝蒂尔啊\x01",
            "真是受欢迎啊。\x02\x03",

            "#020F这个暂且不提……\x01",
            "要赶快返回协会了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2E")


    ChrTalk(    #128
        0x101,
        "#1004F#5P啊，是哦。\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0x2, 0x0, 0x3E8)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)

    def lambda_2A65():
        OP_8F(0xFE, 0x172, 0x3E8, 0x858E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A65)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #129
        0x107,
        (
            "#064F#6P嗯……\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2AEC")

    ChrTalk(    #130
        0x106,
        (
            "#555F#5P啊啊……\x02\x03",

            "似乎柏斯地区\x01",
            "出现特务兵的余党了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B29")

    label("loc_2AEC")


    ChrTalk(    #131
        0x103,
        (
            "#022F#5P嗯嗯……\x02\x03",

            "似乎柏斯地区\x01",
            "似乎出现特务兵的余党了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B29")

    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0x101,
        (
            "#1002F嗯，虽然还不清楚\x01",
            "详细情况……\x02\x03",

            "不管怎么说协会\x01",
            "应该会收到情报的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#065F#6P那、那确实\x01",
            "要赶快回去才行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12F, 0, 400)

    ChrTalk(    #134
        0x12F,
        (
            "#262F唔～马上\x01",
            "就说起玲不懂的话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1016F啊哈哈，抱歉抱歉。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C40")

    ChrTalk(    #136
        0x106,
        (
            "#051F#5P总之有要事\x01",
            "要赶快回协会就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6B")

    label("loc_2C40")


    ChrTalk(    #137
        0x103,
        (
            "#020F#1P总之有要事\x01",
            "要赶快回协会才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6B")


    ChrTalk(    #138
        0x12F,
        (
            "#264F哎呀，是吗。\x02\x03",

            "#263F真可惜，有这么多\x01",
            "士兵在，本想玩玩\x01",
            "捉迷藏也不错的。\x02\x03",

            "#265F能藏的地方，就这附近\x01",
            "所有的森林怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)

    ChrTalk(    #139
        0x107,
        (
            "#067F#6P呜哎～……\x01",
            "好积极啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1016F这、这还是\x01",
            "饶了我吧……\x02\x03",

            "#1006F那么就马上\x01",
            "返回王都吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x162B)
    EventEnd(0x0)
    Return()

    # Function_30_246B end

    def Function_31_2D5B(): pass

    label("Function_31_2D5B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 1000, 43500, 180)
    OP_8E(0xFE, 0x17C, 0x3E8, 0x9934, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xF7, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x172, 0x3E8, 0x858E, 0x7D0, 0x0)
    Return()

    # Function_31_2D5B end

    def Function_32_2DAD(): pass

    label("Function_32_2DAD")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 1000, 43500, 180)
    OP_8E(0xFE, 0x0, 0x3E8, 0xA154, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_6F(0x0, 29)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFFE3E, 0x3E8, 0x88B8, 0x7D0, 0x0)
    Return()

    # Function_32_2DAD end

    def Function_33_2E1D(): pass

    label("Function_33_2E1D")

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
        (0, "loc_2E97"),
        (1, "loc_2E9D"),
        (SWITCH_DEFAULT, "loc_2EA3"),
    )


    label("loc_2E97")

    OP_A2(0x1200)
    Jump("loc_2EA3")

    label("loc_2E9D")

    OP_A2(0x1201)
    Jump("loc_2EA3")

    label("loc_2EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2EB1")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2EB5")

    label("loc_2EB1")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2EB5")

    Return()

    # Function_33_2E1D end

    def Function_34_2EB6(): pass

    label("Function_34_2EB6")

    ClearMapFlags(0x1)
    OP_6D(-23520, 1000, -41440, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2EF9")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_2F17")

    label("loc_2EF9")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_2F17")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_34_2EB6 end

    SaveToFile()

Try(main)
