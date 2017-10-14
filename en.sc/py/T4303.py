from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Tita',                                 # 9
        'Renne',                                # 10
        'Chamberlain Raymond',                  # 11
        'Simone',                               # 12
        'Capital Citizen',                      # 13
        'Capital Citizen',                      # 14
        'Traveler',                             # 15
        'Traveler',                             # 16
        'Royal Army Soldier',                   # 17
        'Royal Army Soldier',                   # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Royal Army Soldier',                   # 21
        'Royal Army Soldier',                   # 22
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
        "Function_7_969",          # 07, 7
        "Function_8_A41",          # 08, 8
        "Function_9_C0D",          # 09, 9
        "Function_10_D05",         # 0A, 10
        "Function_11_DD3",         # 0B, 11
        "Function_12_E9B",         # 0C, 12
        "Function_13_12A0",        # 0D, 13
        "Function_14_1578",        # 0E, 14
        "Function_15_177D",        # 0F, 15
        "Function_16_1985",        # 10, 16
        "Function_17_1B57",        # 11, 17
        "Function_18_1C4E",        # 12, 18
        "Function_19_1D4C",        # 13, 19
        "Function_20_1D9D",        # 14, 20
        "Function_21_1F94",        # 15, 21
        "Function_22_2E27",        # 16, 22
        "Function_23_2E59",        # 17, 23
        "Function_24_2E8B",        # 18, 24
        "Function_25_2ED1",        # 19, 25
        "Function_26_2F37",        # 1A, 26
        "Function_27_308A",        # 1B, 27
        "Function_28_30B1",        # 1C, 28
        "Function_29_30F3",        # 1D, 29
        "Function_30_3121",        # 1E, 30
        "Function_31_3D5B",        # 1F, 31
        "Function_32_3DAD",        # 20, 32
        "Function_33_3E27",        # 21, 33
        "Function_34_3EBF",        # 22, 34
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
            "N-Now, now. All we can do is calm\x01",
            "down and search carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "That girl might have some reasons of her\x01",
            "own for hiding.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_6_8E2 end

    def Function_7_969(): pass

    label("Function_7_969")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9C0")

    ChrTalk(    #2
        0xFE,
        "I'm sure that girl's somewhere in the villa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Pleeease find her!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3D")

    label("loc_9C0")


    ChrTalk(    #4
        0xFE,
        (
            "*sigh* That girl disappears, but it's\x01",
            "like she's trying to tease me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "I'm not letting her get away with it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    ClearChrFlags(0xB, 0x10)

    label("loc_A3D")

    TalkEnd(0xB)
    Return()

    # Function_7_969 end

    def Function_8_A41(): pass

    label("Function_8_A41")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_AB4")

    ChrTalk(    #6
        0xFE,
        (
            "Phew! Gazing at this fountain calms me\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Water truly has many effects.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B1C")

    ChrTalk(    #8
        0xFE,
        "A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I think I saw a girl like that playing\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_B1C")


    ChrTalk(    #10
        0xFE,
        "...Oh? A girl wearing a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Now that you mention it, I think I saw\x01",
            "someone like that playing around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1004FDo you know where she went?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Hmm... I'm sorry, I don't quite remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1007F...Darn it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C09")

    TalkEnd(0xC)
    Return()

    # Function_8_A41 end

    def Function_9_C0D(): pass

    label("Function_9_C0D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_C84")

    ChrTalk(    #15
        0xFE,
        (
            "It flies airships, it makes water flow \x01",
            "from fountains...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Orbal energy is very odd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D01")

    label("loc_C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_D01")

    ChrTalk(    #17
        0xFE,
        (
            "Hey, does this fountain run on orbal\x01",
            "energy, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Dad said lots of things run on orbal\x01",
            "energy in the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D01")

    TalkEnd(0xD)
    Return()

    # Function_9_C0D end

    def Function_10_D05(): pass

    label("Function_10_D05")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(    #19
        0xFE,
        "Princess! For you, I'd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DCF")

    label("loc_D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_DCF")

    ChrTalk(    #20
        0xFE,
        "Hmm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "This villa certainly feels worthy\x01",
            "of royalty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Just being here makes me feel like\x01",
            "I've become a prince myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCF")

    TalkEnd(0xE)
    Return()

    # Function_10_D05 end

    def Function_11_DD3(): pass

    label("Function_11_DD3")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_E23")

    ChrTalk(    #23
        0xFE,
        "We mustn't, my prince! The servants are watching!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E97")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E97")

    ChrTalk(    #24
        0xFE,
        "Heehee, oh, he's such a romanticist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "If he is a prince, then I suppose\x01",
            "that makes me the princess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E97")

    TalkEnd(0xF)
    Return()

    # Function_11_DD3 end

    def Function_12_E9B(): pass

    label("Function_12_E9B")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F57")

    ChrTalk(    #26
        0xFE,
        (
            "I'm sure media from all over the\x01",
            "continent will be flooding the place\x01",
            "during the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Heh heh, perhaps my magazine debut\x01",
            "draws near!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1053")

    label("loc_F57")


    ChrTalk(    #28
        0xFE,
        (
            "I'm sure media from all over the\x01",
            "continent will be flooding the place\x01",
            "during the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "It seems like the press corps have\x01",
            "permission to take photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "...Could it finally be time to make my\x01",
            "debut in the magazines?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1053")

    Jump("loc_129C")

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_129C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1157")

    ChrTalk(    #32
        0xFE,
        (
            "They're not just a former elite squad, you know.\x01",
            "The Intelligence Division's also a bunch\x01",
            "of hand-to-hand combat professionals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Maybe I could take them in a fight\x01",
            "within the city, but I wouldn't dare\x01",
            "underestimate them otherwise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129C")

    label("loc_1157")


    ChrTalk(    #34
        0xFE,
        (
            "I'd need to give a fight against the\x01",
            "Intelligence Division everything I got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "They're not just a former elite squad, you know.\x01",
            "The Intelligence Division's also a bunch\x01",
            "of hand-to-hand combat professionals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Maybe I could take them in a fight\x01",
            "within the city, but I wouldn't dare\x01",
            "underestimate them otherwise.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_129C")

    TalkEnd(0x10)
    Return()

    # Function_12_E9B end

    def Function_13_12A0(): pass

    label("Function_13_12A0")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1369")

    ChrTalk(    #37
        0xFE,
        (
            "There's been a lot of incidents since the\x01",
            "Birthday Celebration, so I can't help but\x01",
            "be nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "All I can do is pray the ceremony\x01",
            "ends with nothing happening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F")

    label("loc_1369")


    ChrTalk(    #39
        0xFE,
        "The signing ceremony's not far away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "There's been a lot of incidents since the\x01",
            "Birthday Celebration, so I can't help but\x01",
            "be nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "All I can do is pray the ceremony\x01",
            "ends with nothing happening.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_143F")

    Jump("loc_1574")

    label("loc_1442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14BD")

    ChrTalk(    #42
        0xFE,
        "It's a relief to have you bracers assisting us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Let's give this everything we've got.\x01",
            "Together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1574")

    label("loc_14BD")


    ChrTalk(    #44
        0xFE,
        (
            "I heard we're going to be working with\x01",
            "the Bracer Guild from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "It's a relief to have you bracers assisting us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Let's give this everything we've got.\x01",
            "Together.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1574")

    TalkEnd(0x11)
    Return()

    # Function_13_12A0 end

    def Function_14_1578(): pass

    label("Function_14_1578")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1611")

    ChrTalk(    #47
        0xFE,
        "As you can see, even the fountain's stopped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Orbments really have sort of worked themselves\x01",
            "into all parts of life, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1611")

    Jump("loc_1779")

    label("loc_1614")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_16CC")

    ChrTalk(    #49
        0xFE,
        (
            "Thanks to Colonel Cid's command,\x01",
            "we suffered very little damage from\x01",
            "the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "The Special Ops who were acting as\x01",
            "the feint picked the wrong enemy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1779")

    label("loc_16CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1779")

    ChrTalk(    #51
        0xFE,
        "Nothing out of the ordinary here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "However, the sub commander just ran\x01",
            "off from the communications room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "...Looks like I'd best be ready for the worst.\x02",
    )

    CloseMessageWindow()

    label("loc_1779")

    TalkEnd(0x12)
    Return()

    # Function_14_1578 end

    def Function_15_177D(): pass

    label("Function_15_177D")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1839")

    ChrTalk(    #54
        0xFE,
        (
            "You can't see it from here, but we've\x01",
            "received reports of a mysterious object\x01",
            "appearing above Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Does the guild know anything about what it is?\x02",
    )

    CloseMessageWindow()

    label("loc_1839")

    Jump("loc_1981")

    label("loc_183C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_18CC")

    ChrTalk(    #56
        0xFE,
        (
            "Right now, there's a Republican senator\x01",
            "visiting Ambassador Cochrane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "He's here to examine the site in advance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1981")

    label("loc_18CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1981")

    ChrTalk(    #58
        0xFE,
        (
            "That reminds me, apparently there's a Republican\x01",
            "senator or something staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "He arrived here early to prepare for\x01",
            "the signing ceremony and observe the site.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1981")

    TalkEnd(0x13)
    Return()

    # Function_15_177D end

    def Function_16_1985(): pass

    label("Function_16_1985")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A68")

    ChrTalk(    #60
        0xFE,
        (
            "Compared to guarding Haken Gate,\x01",
            "this is pretty relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I mean, that place is constantly\x01",
            "under threat from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "If I was in that fort, I wouldn't be able to\x01",
            "sleep soundly at night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A68")

    Jump("loc_1B53")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B06")

    ChrTalk(    #63
        0xFE,
        (
            "That business with the leftover Intelligence\x01",
            "guys ended rather quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "To get mopped up so quickly...\x01",
            "I almost pity them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B53")

    label("loc_1B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1B53")

    ChrTalk(    #65
        0xFE,
        "Sorry, but I'm on patrol right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "Please don't bother me.\x02",
    )

    CloseMessageWindow()

    label("loc_1B53")

    TalkEnd(0x14)
    Return()

    # Function_16_1985 end

    def Function_17_1B57(): pass

    label("Function_17_1B57")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1BD0")

    ChrTalk(    #67
        0xFE,
        "This room is the communications room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "Right now, Warrant Officer Belc is in the room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C4A")

    label("loc_1BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1C4A")

    ChrTalk(    #69
        0xFE,
        (
            "Currently, this area is being used\x01",
            "as a communications room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "I can't let unaffiliated personnel through.\x02",
    )

    CloseMessageWindow()

    label("loc_1C4A")

    TalkEnd(0x15)
    Return()

    # Function_17_1B57 end

    def Function_18_1C4E(): pass

    label("Function_18_1C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C5B")
    Return()

    label("loc_1C5B")

    EventBegin(0x2)
    OP_4A(0x15, 255)
    TurnDirection(0x15, 0x0, 0)
    TurnDirection(0x0, 0x15, 0)
    TurnDirection(0x1, 0x15, 0)
    TurnDirection(0x2, 0x15, 0)
    TurnDirection(0x3, 0x15, 0)

    ChrTalk(    #71
        0x15,
        "This room is the communications room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x15,
        "Please refrain from entering without permission.\x02",
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

    # Function_18_1C4E end

    def Function_19_1D4C(): pass

    label("Function_19_1D4C")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #73
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_19_1D4C end

    def Function_20_1D9D(): pass

    label("Function_20_1D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F43")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #74
        "\x07\x05There's no one near the bench.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #75
        0x101,
        (
            "#1015FShe's not behind the bench or\x01",
            "the planter...\x02\x03",

            "#1004FHey, maybe she's IN the planter!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAE")

    ChrTalk(    #76
        0x107,
        (
            "#067FShe'd have to be as small as a\x01",
            "cat to fit in there, Estelle...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F15")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE8")

    ChrTalk(    #77
        0x106,
        "#552FOh, c'mon, she not a damn cat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F15")

    label("loc_1EE8")


    ChrTalk(    #78
        0x103,
        "#524FShe's not actually a cat, Estelle.\x02",
    )

    CloseMessageWindow()

    label("loc_1F15")


    ChrTalk(    #79
        0x101,
        "#1016FYeah, I guess not...\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_A2(0x1611)
    OP_28(0x89, 0x1, 0x40)
    Jump("loc_1F93")

    label("loc_1F43")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #80
        "\x07\x05There's no one near the bench.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1F93")

    Return()

    # Function_20_1D9D end

    def Function_21_1F94(): pass

    label("Function_21_1F94")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FAB")
    Call(0, 33)
    Call(0, 34)

    label("loc_1FAB")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25B2")
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
            "#1005FRrrrrrrrrrgh, I'm fighting the urge to\x01",
            "STRANGLE that guy!\x02\x03",

            "He's all acting like he's the most\x01",
            "innocent person in the world while\x01",
            "insulting Kloe at the same time!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2327")

    ChrTalk(    #82
        0x106,
        (
            "#053FHey, chill a bit, okay?\x02\x03",

            "#050FYou ask me, he does kind of\x01",
            "have a point.\x02\x03",

            "People who're leaders can't ever\x01",
            "show their confusion to others.\x02\x03",

            "They need to at least LOOK like\x01",
            "they think they know what they're\x01",
            "doing all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1026FBut, Kloe is--!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        (
            "#051FHey, you don't need to tell me.\x02\x03",

            "She knows even without that guy\x01",
            "sayin' a word, I'm sure.\x02\x03",

            "Just let her find her own answer.\x01",
            "It'll work out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1025FYeah... Maybe you're right.\x02\x03",

            "#1006FOkay! Let's get back to finding\x01",
            "our lost girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x106,
        "#051FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25AF")

    label("loc_2327")


    ChrTalk(    #87
        0x103,
        (
            "#026FThere's no need to get so worked up,\x01",
            "Estelle.\x02\x03",

            "#020FAs much as I hate to admit it, Duke\x01",
            "Dunan was approaching something\x01",
            "like a point...I think.\x02\x03",

            "People who must stand above others--\x01",
            "people who lead--can't afford to show\x01",
            "hesitation.\x02\x03",

            "They can never let their doubts show\x01",
            "and must always display an air of\x01",
            "confidence in the eyes of their people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1026FBut, Kloe is--!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        (
            "#021FI know, honey.\x02\x03",

            "#027FKloe knows what she needs to,\x01",
            "regardless of what that man may\x01",
            "say.\x02\x03",

            "We just need to give her time to\x01",
            "find her own answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1025FYeah... Maybe you're right.\x02\x03",

            "#1006FOkay! Let's get back to finding\x01",
            "our lost girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        "#021FAfter you.\x02",
    )

    CloseMessageWindow()

    label("loc_25AF")

    Jump("loc_2E1C")

    label("loc_25B2")

    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x18)
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25EE")
    OP_43(0x104, 0x1, 0x0, 0x19)
    Jump("loc_261B")

    label("loc_25EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2606")
    OP_43(0x107, 0x1, 0x0, 0x19)
    Jump("loc_261B")

    label("loc_2606")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_261B")
    OP_43(0x108, 0x1, 0x0, 0x19)

    label("loc_261B")

    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #92
        0x101,
        (
            "#1005FRrrrrrrrrrgh, I'm fighting the urge to\x01",
            "STRANGLE that guy!\x02\x03",

            "He's all acting like he's the most\x01",
            "innocent person in the world while\x01",
            "insulting Kloe at the same time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x105,
        (
            "#047FNo, his criticism was fairly reasonable,\x01",
            "I think.\x02\x03",

            "His concept of 'nobility' is perhaps\x01",
            "outdated, but he is correct about the\x01",
            "qualities one must possess to lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1002FBut, wait...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5D")

    ChrTalk(    #95
        0x104,
        (
            "#030FI'm not sure I agree with fame being a\x01",
            "prerequisite for rightful inheritance.\x02\x03",

            "#035FCountless rulers in days past were unknown\x01",
            "upon their ascent, and still they performed\x01",
            "great works during their respective reigns.\x02\x03",

            "Erebonia had one such man. After the deaths\x01",
            "of all potential heirs due to civil war, one\x01",
            "unsung hero took the throne in their stead. \x02\x03",

            "That man is now hailed as the emperor who\x01",
            "returned Erebonia to its former glory.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 187, 400)

    ChrTalk(    #96
        0x105,
        "#040F#4PThat was Emperor Dreichels, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x104,
        (
            "#031FThe very same.\x02\x03",

            "#030FMy point is thus: you have nothing\x01",
            "to worry about, Princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x105,
        (
            "#045F#4PHaha. Maybe...\x02\x03",

            "#049FHe still has a point about my\x01",
            "readiness, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1026F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 127, 400)
    Jump("loc_2D27")

    label("loc_2A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C8C")

    ChrTalk(    #100
        0x108,
        (
            "#074FHmmm. Well, Calvard chooses\x01",
            "its leaders with elections, and our\x01",
            "'nobility' was overthrown ages ago.\x02\x03",

            "So I can't say I've got a full grasp\x01",
            "of the concept of nobility, or anything\x01",
            "along those lines.\x02\x03",

            "#070FFrom my perspective, the duke is\x01",
            "'famous,' sure...but it's just infamy.\x02\x03",

            "I can't imagine there's a single man,\x01",
            "woman, or child in Liberl who thinks\x01",
            "he's the superior choice next to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 187, 400)
    Sleep(400)

    ChrTalk(    #101
        0x105,
        (
            "#043F#4PI...suppose that's true, really.\x02\x03",

            "#049FHe still has a point about my\x01",
            "readiness, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1026F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 127, 400)
    Sleep(400)
    Jump("loc_2D27")

    label("loc_2C8C")


    ChrTalk(    #103
        0x105,
        (
            "#049FPutting duty aside...\x02\x03",

            "I fear he's correct about my\x01",
            "readiness to be the next queen.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D13")

    ChrTalk(    #104
        0x107,
        "#063FHe's still mean!\x02",
    )

    CloseMessageWindow()

    label("loc_2D13")


    ChrTalk(    #105
        0x101,
        "#1026FStill...\x02",
    )

    CloseMessageWindow()

    label("loc_2D27")


    ChrTalk(    #106
        0x105,
        (
            "#542FTo tell you the truth, I'm glad we\x01",
            "met him here.\x02\x03",

            "I think I've gained a new sense\x01",
            "of what I'm lacking. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1025FWell, I'm glad you got something\x01",
            "positive out of it.\x02\x03",

            "#1006FAnyway! Shall we find us a lost girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x105,
        "#041FYes, let's!\x02",
    )

    CloseMessageWindow()

    label("loc_2E1C")

    OP_A2(0x1614)
    OP_71(0x5, 0x10)
    EventEnd(0x0)
    Return()

    # Function_21_1F94 end

    def Function_22_2E27(): pass

    label("Function_22_2E27")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFB79E, 0x3E8, 0x99C, 0x7D0, 0x0)
    OP_8C(0xFE, 296, 400)
    Return()

    # Function_22_2E27 end

    def Function_23_2E59(): pass

    label("Function_23_2E59")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFB384, 0x3E8, 0xC26, 0x7D0, 0x0)
    OP_8C(0xFE, 127, 400)
    Return()

    # Function_23_2E59 end

    def Function_24_2E8B(): pass

    label("Function_24_2E8B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFABF0, 0x3E8, 0xAE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB406, 0x3E8, 0x672, 0x7D0, 0x0)
    OP_8C(0xFE, 29, 400)
    Return()

    # Function_24_2E8B end

    def Function_25_2ED1(): pass

    label("Function_25_2ED1")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -22550, 1000, 3180, 90)
    OP_8E(0xFE, 0xFFFFABF0, 0x3E8, 0xAE6, 0x7D0, 0x0)
    OP_72(0x5, 0x800)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFB014, 0x3E8, 0x94C, 0x7D0, 0x0)
    OP_8C(0xFE, 101, 400)
    OP_71(0x5, 0x800)
    Return()

    # Function_25_2ED1 end

    def Function_26_2F37(): pass

    label("Function_26_2F37")

    EventBegin(0x0)
    OP_DB()
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
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4312   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_26_2F37 end

    def Function_27_308A(): pass

    label("Function_27_308A")

    ClearChrFlags(0xFE, 0x80)

    label("loc_308F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B0")
    OP_97(0xFE, 0xFFFFFFCE, 0x3E9E, 0xFFFEA070, 0x1770, 0x1)
    Jump("loc_308F")

    label("loc_30B0")

    Return()

    # Function_27_308A end

    def Function_28_30B1(): pass

    label("Function_28_30B1")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4A38, 0x3E8, 0x8BF6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB636, 0x3E8, 0x8BF6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB636, 0x3E8, 0xFFFFF45C, 0x7D0, 0x0)
    Return()

    # Function_28_30B1 end

    def Function_29_30F3(): pass

    label("Function_29_30F3")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x49CA, 0x3E8, 0x8426, 0x7D0, 0x0)
    OP_8E(0xFE, 0x49CA, 0x3E8, 0xFFFFF45C, 0x7D0, 0x0)
    Return()

    # Function_29_30F3 end

    def Function_30_3121(): pass

    label("Function_30_3121")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3134")
    Call(0, 33)

    label("loc_3134")

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

    def lambda_31E3():
        OP_6D(460, 1000, 34360, 3000)
        ExitThread()

    QueueWorkItem(0x12F, 0, lambda_31E3)

    def lambda_31FB():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_31FB)
    WaitChrThread(0x12F, 0x0)
    WaitChrThread(0x12F, 0x1)

    NpcTalk(    #109
        0x12F,
        "Girl's Voice",
        "#5PEstelle!\x02",
    )

    CloseMessageWindow()

    def lambda_3233():
        OP_8E(0xFE, 0x3B6, 0x3E8, 0x80C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_3233)
    Sleep(500)

    def lambda_3253():
        OP_8E(0xFE, 0xFFFFFF38, 0x3E8, 0x80C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3253)
    WaitChrThread(0x12F, 0x1)
    WaitChrThread(0x107, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_32A7")

    ChrTalk(    #110
        0x107,
        "#560F#2PEstelle, Agate, are you done?\x02",
    )

    CloseMessageWindow()
    Jump("loc_32D3")

    label("loc_32A7")


    ChrTalk(    #111
        0x107,
        "#560F#2PEstelle, Schera, are you done?\x02",
    )

    CloseMessageWindow()

    label("loc_32D3")


    ChrTalk(    #112
        0x12F,
        "#260FThat was kind of quick, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1006FDidn't I tell you? We just needed\x01",
            "to turn in a report.\x02\x03",

            "You could've just waited at the\x01",
            "guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x12F,
        (
            "#262FAww, that's mean!\x02\x03",

            "I just wanna stay with you,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x107, 400)

    ChrTalk(    #115
        0x12F,
        "#262FTitaaaa, say something to her!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)

    ChrTalk(    #116
        0x107,
        (
            "#064F#5PM-Me?\x02\x03",

            "#067FWell, I do wanna stay with Estelle\x01",
            "all the time, but...\x02\x03",

            "She has work to do, so I don't\x01",
            "want to be selfish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x12F,
        "#269FHmph! Fine, then!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12F, 0, 400)
    Sleep(500)

    ChrTalk(    #118
        0x12F,
        (
            "#263F#4PIn that case, I'll just have to\x01",
            "run off with Estelle myself.\x02\x03",

            "You don't get to play, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x107,
        "#065F#5PAwww! Renne, you're so mean!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1016F#6PHahaha... C'mon, you two, don't fight.\x02\x03",

            "Tita, you're the older girl here, so let it\x01",
            "slide, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)

    ChrTalk(    #121
        0x107,
        (
            "#562F#2PBut, but...\x02\x03",

            "You two seem really close\x01",
            "all of a sudden!\x02\x03",

            "#063FI'm...not annoying, am I...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1016FOhh, c'mon, sweetie, like I could\x01",
            "ever stop loving you!\x02",
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
            "#1006F#5PWeeell, Tita?\x02\x03",

            "You keep making that saaad,\x01",
            "looonely face, and I'm just gonna\x01",
            "have to hug you alllll up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x107,
        "#067F#2PAaaaah! Stop, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x12F,
        "#1301FHeeey! Tita, pity hugs are cheating!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3814")

    ChrTalk(    #126
        0x106,
        (
            "#053F#6PFor the love of... I'm not gonna\x01",
            "even try to keep up with this anymore.\x02\x03",

            "#051FIf you kids are done, how about we\x01",
            "get back to the guildhouse?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CC")

    label("loc_3814")


    ChrTalk(    #127
        0x103,
        (
            "#021F#6PYou get much more popular with\x01",
            "the ladies, Estelle, and Olivier might\x01",
            "get jealous.\x02\x03",

            "#020FWith that out of the way, though,\x01",
            "we really need to hurry back to the\x01",
            "guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CC")


    ChrTalk(    #128
        0x101,
        "#1004F#5POh, yeah, we should.\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0x2, 0x0, 0x3E8)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)

    def lambda_390D():
        OP_8F(0xFE, 0x172, 0x3E8, 0x858E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_390D)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #129
        0x107,
        "#064F#2PHuh? Did something happen?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_39AA")

    ChrTalk(    #130
        0x106,
        (
            "#555F#6PYeah...\x02\x03",

            "Some of the old Intelligence goons\x01",
            "showed up in Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A06")

    label("loc_39AA")


    ChrTalk(    #131
        0x103,
        (
            "#022F#6PI'm afraid so.\x02\x03",

            "Remnants of the Intelligence Division\x01",
            "have been found in Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A06")

    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #132
        0x107,
        "#065F#2PThat's awful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1002FYeah, but we're still a bit fuzzy on\x01",
            "the details.\x02\x03",

            "Elnan can hopefully tell us more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x107,
        "#062F#2PWe really need to hurry back, then!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12F, 0, 400)

    ChrTalk(    #135
        0x12F,
        (
            "#262FArrgh! This isn't fair, you guys.\x01",
            "I don't know what you're talking\x01",
            "about at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#1016FAh-haha, sorry, Renne.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3BBE")

    ChrTalk(    #137
        0x106,
        (
            "#051F#6PBasically, some serious stuff has\x01",
            "come up, so we need to get back\x01",
            "to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_3BBE")


    ChrTalk(    #138
        0x103,
        (
            "#020F#6PBasically, something very important\x01",
            "has happened, so we need to go back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C14")


    ChrTalk(    #139
        0x12F,
        (
            "#264FOh! Well, that was easy.\x02\x03",

            "#263FToo bad. It'd be fun to play hide\x01",
            "and seek with all these soldiers.\x02\x03",

            "#265FWe could use the whole forest as a\x01",
            "hiding place! That'd be fun, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)

    ChrTalk(    #140
        0x107,
        "#067F#5PUmmm... That might be...fun, yeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1016FLet's not do that and say we did.\x02\x03",

            "#1006FOkay! You guys ready to go?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x162B)
    EventEnd(0x0)
    Return()

    # Function_30_3121 end

    def Function_31_3D5B(): pass

    label("Function_31_3D5B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 1000, 43500, 180)
    OP_8E(0xFE, 0x17C, 0x3E8, 0x9934, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xF7, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x172, 0x3E8, 0x858E, 0x7D0, 0x0)
    Return()

    # Function_31_3D5B end

    def Function_32_3DAD(): pass

    label("Function_32_3DAD")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 1000, 43500, 180)
    OP_8E(0xFE, 0x0, 0x3E8, 0xA154, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 29)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFFE3E, 0x3E8, 0x88B8, 0x7D0, 0x0)
    Return()

    # Function_32_3DAD end

    def Function_33_3E27(): pass

    label("Function_33_3E27")

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
        (0, "loc_3EA0"),
        (1, "loc_3EA6"),
        (SWITCH_DEFAULT, "loc_3EAC"),
    )


    label("loc_3EA0")

    OP_A2(0x1200)
    Jump("loc_3EAC")

    label("loc_3EA6")

    OP_A2(0x1201)
    Jump("loc_3EAC")

    label("loc_3EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3EBA")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3EBE")

    label("loc_3EBA")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3EBE")

    Return()

    # Function_33_3E27 end

    def Function_34_3EBF(): pass

    label("Function_34_3EBF")

    ClearMapFlags(0x1)
    OP_6D(-23520, 1000, -41440, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F02")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_3F20")

    label("loc_3F02")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_3F20")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_34_3EBF end

    SaveToFile()

Try(main)
