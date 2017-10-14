from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4130   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4130.x',
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
        'Nial',                                 # 9
        'Editor-In-Chief',                      # 10
        'Noticia',                              # 11
        'Faults',                               # 12
        'Dorothy',                              # 13
        'Sariah',                               # 14
        'Baral',                                # 15
        'Connor',                               # 16
        'Novel',                                # 17
        'Cready',                               # 18
        'Spencer',                              # 19
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01023 ._CH',             # 01
        'ED6_DT07/CH01100 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01213 ._CH',             # 05
        'ED6_DT07/CH02070 ._CH',             # 06
        'ED6_DT07/CH01540 ._CH',             # 07
        'ED6_DT06/CH20021 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01023P._CP',             # 01
        'ED6_DT07/CH01100P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01213P._CP',             # 05
        'ED6_DT07/CH02070P._CP',             # 06
        'ED6_DT07/CH01540P._CP',             # 07
        'ED6_DT06/CH20021P._CP',             # 08
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -54100,
        Z                   = 200,
        Y                   = 61000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -55730,
        Z                   = 250,
        Y                   = 119940,
        Direction           = 181,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -59030,
        Z                   = 100,
        Y                   = 59540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -56890,
        Z                   = 0,
        Y                   = 63750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -56630,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 65800,
        Z                   = 100,
        Y                   = -3410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 66540,
        Z                   = 750,
        Y                   = -4140,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1703944,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -56840,
        TriggerZ            = 0,
        TriggerY            = 3500,
        TriggerRange        = 400,
        ActorX              = -56630,
        ActorZ              = 1500,
        ActorY              = 5500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_306",          # 00, 0
        "Function_1_4EE",          # 01, 1
        "Function_2_5E1",          # 02, 2
        "Function_3_75E",          # 03, 3
        "Function_4_1223",         # 04, 4
        "Function_5_1D4B",         # 05, 5
        "Function_6_1D50",         # 06, 6
        "Function_7_290F",         # 07, 7
        "Function_8_2914",         # 08, 8
        "Function_9_3504",         # 09, 9
        "Function_10_3E42",        # 0A, 10
        "Function_11_436D",        # 0B, 11
        "Function_12_487A",        # 0C, 12
        "Function_13_4D3E",        # 0D, 13
        "Function_14_501A",        # 0E, 14
        "Function_15_501F",        # 0F, 15
        "Function_16_53FA",        # 10, 16
        "Function_17_58C1",        # 11, 17
        "Function_18_7424",        # 12, 18
        "Function_19_78DA",        # 13, 19
        "Function_20_7975",        # 14, 20
        "Function_21_79EE",        # 15, 21
        "Function_22_7C25",        # 16, 22
        "Function_23_7D0D",        # 17, 23
        "Function_24_8337",        # 18, 24
        "Function_25_83EF",        # 19, 25
    )


    def Function_0_306(): pass

    label("Function_0_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3C2")
    SetChrChipByIndex(0x9, 1)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, -56260, 0, 60900, 270)
    OP_43(0x9, 0x0, 0x6, 0x2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -55850, 0, 63410, 90)
    SetChrChipByIndex(0xA, 5)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0xA, -61660, 0, 59440, 72)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrChipByIndex(0xB, 9)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x10)
    SetChrPos(0xB, -59900, 0, 59400, 71)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrPos(0x8, -58470, 0, 62920, 117)
    SetChrPos(0xC, -59920, 0, 62910, 134)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4CA")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3F3")
    SetChrChipByIndex(0xA, 5)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0xA, -56250, 0, 61030, 80)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jump("loc_4CA")

    label("loc_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_43F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -64450, 0, 60580, 1)
    SetChrChipByIndex(0xA, 5)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0xA, -57850, 0, 61830, 263)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jump("loc_4CA")

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -59010, 0, 121400, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D")
    SetChrFlags(0x8, 0x10)

    label("loc_46D")

    SetChrChipByIndex(0xA, 5)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0xA, -56570, 0, 64660, 1)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jump("loc_4CA")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4A1")
    Jump("loc_4CA")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4CA")
    SetChrPos(0xA, -56250, 0, 61090, 103)
    SetChrChipByIndex(0xA, 5)
    SetChrFlags(0xA, 0x10)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4ED")

    Return()

    # Function_0_306 end

    def Function_1_4EE(): pass

    label("Function_1_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
    OP_B1("t4130_y")
    Jump("loc_513")

    label("loc_50A")

    OP_B1("t4130_n")

    label("loc_513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_END)), "loc_51F")
    SetChrFlags(0x10, 0x80)

    label("loc_51F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_585")
    OP_D2(0x700A2, 0x700A6, 0x1)
    OP_D2(0x700C9, 0x700CD, 0x5)
    OP_D2(0x700BA, 0x700BE, 0x9)
    Jump("loc_5E0")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_599")
    OP_D2(0x700C9, 0x700CD, 0x5)
    Jump("loc_5E0")

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5AD")
    OP_D2(0x700C9, 0x700CD, 0x5)
    Jump("loc_5E0")

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C5")
    OP_D2(0x700C9, 0x700CD, 0x5)
    Jump("loc_5E0")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5CF")
    Jump("loc_5E0")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5E0")
    OP_D2(0x700C9, 0x700CD, 0x5)

    label("loc_5E0")

    Return()

    # Function_1_4EE end

    def Function_2_5E1(): pass

    label("Function_2_5E1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_606")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_748")

    label("loc_606")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_748")

    label("loc_61F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_638")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_748")

    label("loc_638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_748")

    label("loc_651")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_748")

    label("loc_66A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_748")

    label("loc_683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_748")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_748")

    label("loc_6B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_748")

    label("loc_6CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_748")

    label("loc_6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_748")

    label("loc_700")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_719")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_748")

    label("loc_719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_748")

    label("loc_732")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_748")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_748")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_748")

    label("loc_75D")

    Return()

    # Function_2_5E1 end

    def Function_3_75E(): pass

    label("Function_3_75E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABA")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #0
        0x101,
        "#1001FNial!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#143FOh, hey, Estelle...\x02\x03",

            "And Joshua... Been quite a while,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1040FIt has, indeed.\x02\x03",

            "You're as busy as always, Nial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#140FYeah, I told the editor the same thing,\x01",
            "but somethin' like this ain't gonna stop\x01",
            "my pen.\x02\x03",

            "That's just how companies want it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1015FBut what do you plan on doing without\x01",
            "being able to use orbments?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 300)

    ChrTalk(    #5
        0x8,
        (
            "#145FYeah, that's the problem.\x02\x03",

            "With things as they are, we can't even\x01",
            "use Dorothy's camera.\x02\x03",

            "#141FWell, I got some ideas, though.\x02\x03",

            "After this I'm gonna meet with Queen\x01",
            "Alicia and have her listen to 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1001FSounds like you're working pretty hard.\x01",
            "Kind of a relief.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 300)

    ChrTalk(    #7
        0x8,
        (
            "#141FSo...Joshua.\x02\x03",

            "I gotta admit, I wanna interview you real bad.\x01",
            "I'll put that off for now, though.\x02\x03",

            "#147FStill, you be ready for my pen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1054FHaha... Go easy on me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D7)
    Jump("loc_B50")

    label("loc_ABA")


    ChrTalk(    #9
        0x8,
        (
            "#140FI've got a mountain of problems and things\x01",
            "to do, but I can't afford to space out.\x02\x03",

            "For a journalist, the first thing to do\x01",
            "is take action.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B50")

    Jump("loc_121F")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E65")

    ChrTalk(    #10
        0x8,
        (
            "#145F*yaaawn* Geez...\x02\x03",

            "#140FIt's a damn waste. I couldn't write a decent\x01",
            "article on that giant mechanical doll thing\x01",
            "thanks to those army restrictions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1015FLt. Colonel Cid gagged you, did he?\x02\x03",

            "#1000FWell, if people knew somethin' like that\x01",
            "had appeared, they'd probably panic.\x02\x03",

            "I'm sure Cid was worried about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#140FYeah, well...\x02\x03",

            "#142FBut, the Liberl News ain't a mouthpiece for\x01",
            "the military.\x02\x03",

            "Our mission is ultimately to report information\x01",
            "correctly from a neutral position.\x02\x03",

            "Knowing something and not tellin'\x01",
            "it is a lie, basically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1015FW-Well, maybe so, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#145FWell, this time I'll give in. This time.\x02\x03",

            "#140FNow, then, Dorothy should be gettin'\x01",
            "back soon...\x02\x03",

            "Not sure if she'll make it in time for\x01",
            "your departure, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1666)
    Jump("loc_ED3")

    label("loc_E65")


    ChrTalk(    #15
        0x8,
        (
            "#140FDorothy should be gettin' back soon, but...\x02\x03",

            "Not sure if she'll make it in time for\x01",
            "your departure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED3")

    Jump("loc_121F")

    label("loc_ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_117A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1077")

    ChrTalk(    #16
        0x8,
        (
            "#143FYou wanna know if I've seen Renne?\x02\x03",

            "#140FThe girl who was at dinner last\x01",
            "night at the bar, you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1011FYeah, yeah, have you seen her around?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#140FSorry, I ain't left the building today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1015FDarn...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_1048")

    ChrTalk(    #20
        0x8,
        (
            "#140FWell, try askin' someone else.\x02\x03",

            "#141FThe guy runnin' that cafe we went\x01",
            "to's a pretty good source of info.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1071")

    label("loc_1048")


    ChrTalk(    #21
        0x8,
        "#140FWell, try askin' someone else.\x02",
    )

    CloseMessageWindow()

    label("loc_1071")

    OP_A2(0x2)
    Jump("loc_1177")

    label("loc_1077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_111F")

    ChrTalk(    #22
        0x8,
        (
            "#140FSorry, but if you're looking for a lost\x01",
            "kid, you'll need to ask someone else.\x02\x03",

            "The guy runnin' that cafe we went\x01",
            "to's a pretty good source of info.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1177")

    label("loc_111F")


    ChrTalk(    #23
        0x8,
        (
            "#140FSorry, but if you're looking for a lost\x01",
            "kid, you'll need to ask someone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1177")

    Jump("loc_121F")

    label("loc_117A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_1207")

    ChrTalk(    #24
        0x8,
        (
            "#140FI spent all day walkin' around,\x01",
            "but I got a big load of nothin'.\x02\x03",

            "I hope Dorothy managed to find something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120B")

    label("loc_1207")

    Call(0, 17)

    label("loc_120B")

    Jump("loc_121F")

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1218")
    Jump("loc_121F")

    label("loc_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_121F")

    label("loc_121F")

    TalkEnd(0x8)
    Return()

    # Function_3_75E end

    def Function_4_1223(): pass

    label("Function_4_1223")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12DE")

    ChrTalk(    #25
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I don't think of this situation\x01",
            "as a threat at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "If anything, this is exactly when the true worth\x01",
            "of the Liberl News Service will be tested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_12DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_13E1")

    ChrTalk(    #28
        0xFE,
        (
            "Hey, sounds like you had a late night last night,\x01",
            "but thanks for helping with Nial's coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "He just went out with Dorothy a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "They said they were going to poke around town and\x01",
            "do a little digging about last night's incident\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_13E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_14D0")

    ChrTalk(    #31
        0xFE,
        (
            "Gives me gray hairs just thinking about Dorothy\x01",
            "out on her own, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "She does do a good job, whatever else\x01",
            "you might say about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "There's been a lot of side trips, but results\x01",
            "are what matter in this business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D47")

    label("loc_14D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_16BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1647")

    ChrTalk(    #34
        0xFE,
        (
            "A reporter can't get good information\x01",
            "without jumping into someone's pocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "However, a reporter also has to distance\x01",
            "themselves from the subject as much as\x01",
            "possible when writing their article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Not just interview subjects and cases,\x01",
            "but sometimes you have to even\x01",
            "look at yourself from the outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "A true journalist finds the truth.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_16B9")

    label("loc_1647")


    ChrTalk(    #38
        0xFE,
        (
            "A reporter must even be able to look\x01",
            "at themselves from the outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "A true journalist finds the truth.\x02",
    )

    CloseMessageWindow()

    label("loc_16B9")

    Jump("loc_1D47")

    label("loc_16BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_178C")

    ChrTalk(    #40
        0xFE,
        "Oh, Estelle, Nial just got back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1000FAh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "Yeah, he's upstairs in the reference room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Haha, that expression's one he wears\x01",
            "when he didn't get a scoop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AF")

    label("loc_178C")


    ChrTalk(    #44
        0xFE,
        "Oh, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1001FHeya, Chief, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "What do you need today, hmm?\x01",
            "Business with Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1000FYeah, got some questions on some\x01",
            "guild business.\x02\x03",

            "Is he back from Ruan yet?\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Yep, he should be in the office.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Think I saw him go up to the reference room.\x02",
    )

    CloseMessageWindow()

    label("loc_18AF")

    OP_A2(0x1664)
    Jump("loc_1903")

    label("loc_18B5")


    ChrTalk(    #50
        0xFE,
        (
            "If you're looking for Nial, he should\x01",
            "be in the upstairs reference room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1903")

    Jump("loc_1D47")

    label("loc_1906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6D")

    ChrTalk(    #51
        0xFE,
        "Oh, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1001FHeya, Chief, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "What do you need today, hmm?\x01",
            "Business with Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1000FYeah, got some questions on some\x01",
            "guild business.\x02\x03",

            "Is he back from Ruan yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Yeah, he's back, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I think he stepped outside to do some coverage.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1015FAh, figures.\x01",
            "He always does seem pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Well, that's our job after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Don't know where he is, but I heard\x01",
            "he'll be back by the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1006FOkay, got it. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        "#040FIt seems we should start somewhere else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x108,
        (
            "#070FYes, this can probably be the last place\x01",
            "we visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1680)
    Jump("loc_1BCF")

    label("loc_1B6D")


    ChrTalk(    #63
        0xFE,
        "Nial's out at the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Don't know where he is, but I heard\x01",
            "he'll be back by evening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCF")

    Jump("loc_1D47")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC9")

    ChrTalk(    #65
        0xFE,
        "[Ruan's New Mayor Decided!]... Huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Kinda tame coming from Nial,\x01",
            "but it's not bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "All right. Too bad for Noticia, but this looks\x01",
            "like it'll be our next headline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1000F(Looks like they're in a meeting...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1D47")

    label("loc_1CC9")


    ChrTalk(    #69
        0xFE,
        "[Ruan's New Mayor Decided!]... Huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "All right. Too bad for Noticia, but this looks\x01",
            "like it'll be our next headline.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D47")

    TalkEnd(0x9)
    Return()

    # Function_4_1223 end

    def Function_5_1D4B(): pass

    label("Function_5_1D4B")

    Call(0, 6)
    Return()

    # Function_5_1D4B end

    def Function_6_1D50(): pass

    label("Function_6_1D50")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Curry of Dreams] - 900 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DCD")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_1DCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EA7")
    SubMira(900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #71
        "\x06Ate #2CCurry of Dreams#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x640)
    OP_31(0x1, 0xFD, 0x640)
    OP_31(0x2, 0xFD, 0x640)
    OP_31(0x3, 0xFD, 0x640)
    OP_31(0x4, 0xFD, 0x640)
    OP_31(0x5, 0xFD, 0x640)
    OP_31(0x6, 0xFD, 0x640)
    OP_31(0x7, 0xFD, 0x640)
    OP_31(0x8, 0xFD, 0x640)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E99")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_1E68")
    Jump("loc_1E99")

    label("loc_1E68")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #72
        "\x06Learned [#2CCurry of Dreams#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_1E99")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1ECF")

    label("loc_1EA7")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #73
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1ECF")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_1EE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EFB")
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    label("loc_1EFB")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Collected all of Gambler Jack\x01",               # 0
            "Have not collected all of Gambler Jack\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F8C"),
        (1, "loc_1FD5"),
        (SWITCH_DEFAULT, "loc_201E"),
    )


    label("loc_1F8C")

    OP_3E(0x23A, 1)
    OP_3E(0x23B, 1)
    OP_3E(0x23C, 1)
    OP_3E(0x23D, 1)
    OP_3E(0x23E, 1)
    OP_3E(0x23F, 1)
    OP_3E(0x240, 1)
    OP_3E(0x241, 1)
    OP_3E(0x242, 1)
    OP_3E(0x243, 1)
    OP_3E(0x244, 1)
    OP_3E(0x245, 1)
    OP_3E(0x246, 1)
    OP_3E(0x247, 1)
    Jump("loc_201E")

    label("loc_1FD5")

    OP_3F(0x23A, 1)
    OP_3F(0x23B, 1)
    OP_3F(0x23C, 1)
    OP_3F(0x23D, 1)
    OP_3F(0x23E, 1)
    OP_3F(0x23F, 1)
    OP_3F(0x240, 1)
    OP_3F(0x241, 1)
    OP_3F(0x242, 1)
    OP_3F(0x243, 1)
    OP_3F(0x244, 1)
    OP_3F(0x245, 1)
    OP_3F(0x246, 1)
    OP_3F(0x247, 1)
    Jump("loc_201E")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x23A, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x23B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23E, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23F, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x240, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x241, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x242, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x243, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x244, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x245, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x246, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x247, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_209B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2093")
    OP_A2(0x10C3)
    Call(0, 21)
    TalkEnd(0xE)
    Return()

    label("loc_2093")

    Call(0, 22)
    TalkEnd(0xE)
    Return()

    label("loc_209B")


    ChrTalk(    #74
        0xE,
        (
            "Cooking without orbments is rough,\x01",
            "but I like that rustic feel when you use fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "Even the coffee seems a little tastier when\x01",
            "prepared this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "Might be good to do it with wood and\x01",
            "charcoal fires from now on, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2226")

    ChrTalk(    #77
        0xE,
        (
            "I thought the harbor district seemed kinda\x01",
            "loud. Guess something bad happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xE,
        (
            "But, if things can stay calm from here on,\x01",
            "then all's well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_24CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 3)), scpexpr(EXPR_END)), "loc_22E7")

    ChrTalk(    #79
        0xE,
        (
            "A little girl drank a Cafe au Lait, then\x01",
            "asked me an odd question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "I think it was... 'Do you know where they\x01",
            "sell the sweets that disappear if you\x01",
            "leave them alone?'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24C9")

    label("loc_22E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_22F5")
    Call(0, 18)
    Jump("loc_24C9")

    label("loc_22F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")

    ChrTalk(    #81
        0xE,
        (
            "When I worked at the castle, I always took\x01",
            "boats from Ruan for my international trips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        "After all, we didn't have airships back then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xE,
        (
            "They can't move as fast as airships,\x01",
            "but boats are nice in their own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        (
            "Time passes more slowly...\x01",
            "That's how things used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xE,
        (
            "Ever since airships appeared, people have\x01",
            "become quite the restless animal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_24C9")

    label("loc_2470")


    ChrTalk(    #86
        0xE,
        "Haha, thinking this proves I'm getting old.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xE,
        "Well, just gotta go with the flow.\x02",
    )

    CloseMessageWindow()

    label("loc_24C9")

    Jump("loc_28FD")

    label("loc_24CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25D1")

    ChrTalk(    #88
        0xE,
        (
            "Lately, the Liberl News folk have\x01",
            "been running all around the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "Given these hectic times, it's probably because\x01",
            "there's a lot to talk about nowadays...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        (
            "I sure hope they bring in good news\x01",
            "at least as much as the other stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28FD")

    label("loc_25D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_27FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2711")

    ChrTalk(    #91
        0xE,
        (
            "With rebuilding the Royal Army and preparing for\x01",
            "the signing ceremony, it seems like government\x01",
            "officials sure are busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "Conversely, peaceful life's returned for\x01",
            "the citizens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        (
            "Really reminds me that I'm no longer in the\x01",
            "royal service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xE,
        "Mind, I feel bad for my former coworkers.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_27FA")

    label("loc_2711")


    ChrTalk(    #95
        0xE,
        (
            "With rebuilding the Royal Army and preparing for\x01",
            "the signing ceremony, it seems like government\x01",
            "officials sure are busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xE,
        (
            "I feel bad for my former coworkers, but it\x01",
            "really reminds me that I'm no longer in the\x01",
            "royal service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FA")

    Jump("loc_28FD")

    label("loc_27FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_28FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B4")

    ChrTalk(    #97
        0xE,
        "Hey, I know that face.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        (
            "You're the bracer lady who's a friend of Nial's,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        (
            "Welcome to Baral Coffee House, known\x01",
            "for its coffee and rice curry!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_28FD")

    label("loc_28B4")


    ChrTalk(    #100
        0xE,
        (
            "Welcome to Baral Coffee House, known\x01",
            "for its coffee and rice curry!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290B")
    OP_A2(0x0)
    Jump("loc_290B")

    label("loc_290B")

    TalkEnd(0xE)
    Return()

    # Function_6_1D50 end

    def Function_7_290F(): pass

    label("Function_7_290F")

    Call(0, 8)
    Return()

    # Function_7_290F end

    def Function_8_2914(): pass

    label("Function_8_2914")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Seafood Hotpot] - 1600 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2991")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCA)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_2991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A69")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #101
        "\x06Ate #2CSeafood Hotpot#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x9C4)
    OP_31(0x1, 0xFD, 0x9C4)
    OP_31(0x2, 0xFD, 0x9C4)
    OP_31(0x3, 0xFD, 0x9C4)
    OP_31(0x4, 0xFD, 0x9C4)
    OP_31(0x5, 0xFD, 0x9C4)
    OP_31(0x6, 0xFD, 0x9C4)
    OP_31(0x7, 0xFD, 0x9C4)
    OP_31(0x8, 0xFD, 0x9C4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_2A2B")
    Jump("loc_2A5B")

    label("loc_2A2B")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x06Learned [#2CSeafood Hotpot#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_2A5B")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_2A91")

    label("loc_2A69")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #103
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_2A91")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x11)
    Return()

    label("loc_2AA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ABD")
    FadeToBright(300, 0)
    TalkEnd(0x11)
    Return()

    label("loc_2ABD")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B9D")

    ChrTalk(    #104
        0x11,
        (
            "Phew! It took a bit, but I think I'm getting used\x01",
            "to this cooking with fire thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "If the people from the Fishermen's Group hadn't\x01",
            "taught me, I'd probably be closed for business\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_2B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2CA1")

    ChrTalk(    #106
        0x11,
        (
            "Apparently there was a fight between the\x01",
            "Intelligence Division and the Royal Army\x01",
            "in the harbor block yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        (
            "Word is, all the Intelligence Division people\x01",
            "were arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x11,
        (
            "To show up just in the nick of time...\x01",
            "That's Julia for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_2CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E09")

    ChrTalk(    #109
        0x11,
        (
            "Yesterday I went over to the cafe in the\x01",
            "West Block to have their curry rice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        (
            "That perfect level of spiciness is as\x01",
            "addictive as the rumors say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "The coffee was good too.\x01",
            "I was very satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        (
            "A shop banking on its bitterness and\x01",
            "its spiciness... A very fresh idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        (
            "Makes sense, since the owner's so\x01",
            "well traveled.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2E8D")

    label("loc_2E09")


    ChrTalk(    #114
        0x11,
        (
            "A shop banking on its bitterness and\x01",
            "its spiciness... A very fresh idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        (
            "Makes sense, since the owner's so\x01",
            "well traveled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8D")

    Jump("loc_3500")

    label("loc_2E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7C")

    ChrTalk(    #116
        0x11,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        "You guys sure were having fun last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x11,
        (
            "To see people enjoying things that much sure makes\x01",
            "me happy to be the one running the store.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12F, 400)

    ChrTalk(    #119
        0x11,
        "I hope you'll all come back and dine again.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_300D")

    label("loc_2F7C")


    ChrTalk(    #120
        0x11,
        "You guys sure were having fun last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        (
            "To see people enjoying things that much sure makes\x01",
            "me happy to be the one running the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300D")

    Jump("loc_3500")

    label("loc_3010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3084")

    ChrTalk(    #122
        0x11,
        (
            "Now, then, it's just about evening so\x01",
            "I'm gonna start getting busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        "Gonna do my best today!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_3084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333F")

    ChrTalk(    #124
        0x11,
        "Welcome! Welcome to the Sunnybell Inn!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x104, 400)

    ChrTalk(    #125
        0x11,
        "Hmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x11,
        (
            "Are you Olivier, the guy I asked to\x01",
            "perform on the piano a while back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x104,
        "#031FHa ha, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        (
            "It's been a while.\x01",
            "What're you doing here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x104,
        (
            "#034FOhh, say not such cruel words.\x02\x03",

            "#035FThe bittersweet few days I spent here with you...\x02\x03",

            "To a lonely traveling performer, they were\x01",
            "truly a single ray of light illuminating an\x01",
            "eternal dark.\x02\x03",

            "#030FSo, unable to forget you, I have returned like a\x01",
            "migrating bird seeking the warmth of the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        "Heh heh, same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x11,
        (
            "If you don't have anything else to do, I wonder\x01",
            "if I could ask you to play the piano again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x104,
        "#031FHa ha, but of course!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3394")

    label("loc_333F")

    TurnDirection(0x11, 0x104, 400)

    ChrTalk(    #133
        0x11,
        (
            "Olivier, if you're lacking anything to do,\x01",
            "mind giving the piano a spin?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3394")

    Jump("loc_3500")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_348A")

    ChrTalk(    #134
        0x11,
        (
            "There's still a lot of people who are thinking\x01",
            "about Colonel Richard, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x11,
        (
            "The colonel comes up a lot in people's\x01",
            "conversations even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x11,
        (
            "Certainly he did something bad, but\x01",
            "that just shows how much charm he had.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3500")

    label("loc_348A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3500")

    ChrTalk(    #137
        0x11,
        "Maybe it's because the signing ceremony's close...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x11,
        "Lately, I see a lot of foreigners in the store...\x02",
    )

    CloseMessageWindow()

    label("loc_3500")

    TalkEnd(0x11)
    Return()

    # Function_8_2914 end

    def Function_9_3504(): pass

    label("Function_9_3504")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3602")

    ChrTalk(    #139
        0xFE,
        (
            "The surface of the meat is roasted perfectly,\x01",
            "and smells wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Direct heat cooking's different than normal,\x01",
            "but kinda nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Seems like it's hard to control the fire, though.\x01",
            "Cready was having a rough time of it at first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3E")

    label("loc_3602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_37FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375D")

    ChrTalk(    #142
        0xFE,
        (
            "So the remnants of the Intelligence Division\x01",
            "were hiding in the harbor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I know Kanone tried to flee, but the Royal Guard\x01",
            "eventually managed to capture her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "That'd mean all the Intelligence Division heads\x01",
            "have been caught, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I swear, everything I hear ends up making Colonel\x01",
            "Richard look even worse...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_37FC")

    label("loc_375D")


    ChrTalk(    #146
        0xFE,
        (
            "So the remnants of the Intelligence Division\x01",
            "were hiding in the harbor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I swear, everything I hear ends up making Colonel\x01",
            "Richard look even worse...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FC")

    Jump("loc_3E3E")

    label("loc_37FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_39A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3932")

    ChrTalk(    #148
        0xFE,
        (
            "Yesterday, I had some of the ice cream sold\x01",
            "in the East Block for the first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "Man, it was good. I can see why Princess\x01",
            "Klaudia would sneak out to get some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "Still, I've never much liked cold food.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "I eat slowly, so it always melts away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Makes me kinda sad...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_39A6")

    label("loc_3932")


    ChrTalk(    #153
        0xFE,
        "Still, I've never much liked cold food.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "I eat slowly, so it always melts away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "Makes me kinda sad...\x02",
    )

    CloseMessageWindow()

    label("loc_39A6")

    Jump("loc_3E3E")

    label("loc_39A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_39CD")

    ChrTalk(    #156
        0xFE,
        "What to eat today...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E3E")

    label("loc_39CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AB2")

    ChrTalk(    #157
        0xFE,
        (
            "Colonel Richard's second in command, that\x01",
            "lady captain, is apparently still on the run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "Who was she... Canno? Kanan? Kanone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Apparently she was Julia's rival in the\x01",
            "Royal Guard during officer school.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3E")

    label("loc_3AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BBF")

    ChrTalk(    #160
        0xFE,
        "Just between you and me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "I've petitioned the queen and asked\x01",
            "her to pardon Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "It's been a while since the coup, and\x01",
            "I've thought about it a lot, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "I just can't believe that the colonel is\x01",
            "just some villain.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3C48")

    label("loc_3BBF")


    ChrTalk(    #164
        0xFE,
        (
            "I've petitioned the queen and asked\x01",
            "her to pardon Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I just can't believe that the colonel is\x01",
            "just some villain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C48")

    Jump("loc_3E3E")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3D47")

    ChrTalk(    #166
        0xFE,
        (
            "Apparently Colonel Richard, the one behind\x01",
            "the coup d'etat, is being imprisoned at\x01",
            "Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "...I wonder what's going to happen\x01",
            "to the colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "If he's behind a coup d'etat, I can't\x01",
            "believe things will go easy for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3E")

    label("loc_3D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3E3E")

    ChrTalk(    #169
        0xFE,
        (
            "During the coup d'etat, a lot of officials\x01",
            "and servants got kicked out of the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "Now, those people are all busy back at work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Cleaning up after such an event's hard, though,\x01",
            "so things won't go back to normal right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3E")

    TalkEnd(0xFE)
    Return()

    # Function_9_3504 end

    def Function_10_3E42(): pass

    label("Function_10_3E42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3F1F")

    ChrTalk(    #172
        0xFE,
        (
            "The cafe owner makes it all sound so carefree,\x01",
            "but this is a big problem for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "After all, with no orbments, I can't read\x01",
            "at night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Candle light makes me feel like\x01",
            "I'm just hurting my eyes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_3F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3FDF")

    ChrTalk(    #175
        0xFE,
        "Wh-What was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I saw a giant metal...doll thing fly off\x01",
            "during last night's mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "I bet the Liberl News has the details.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "I've gotta pick up the next edition!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_3FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_END)), "loc_4076")

    ChrTalk(    #179
        0xFE,
        (
            "Today's the release of the new\x01",
            "edition of the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Time to run out and pick up a copy to\x01",
            "soak up the latest events.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_417D")

    label("loc_4076")


    ChrTalk(    #181
        0xFE,
        "Huh... Was the Liberl News out today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "The Liberl News is the Liberl News Magazine,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "Whew! Finished my book.\x01",
            "Time to go shopping!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "Here, you can have it.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #185
        "\x07\x00Received #574i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23E, 1)
    OP_A2(0x10B9)

    label("loc_417D")

    Jump("loc_4369")

    label("loc_4180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41EB")

    ChrTalk(    #186
        0xFE,
        "Oh! It's already evening...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "Getting lost in a good book really makes\x01",
            "the time fly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_41EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_42AF")

    ChrTalk(    #188
        0xFE,
        (
            "The date of the signing for the non-aggression\x01",
            "pact Queen Alicia's been promoting is approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "As a citizen of Liberl, I can certainly\x01",
            "understand the ideal behind the pact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_42AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4369")

    ChrTalk(    #190
        0xFE,
        "The Air-Letten shop wasn't bad, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Yeah, this cafe really is the best place\x01",
            "to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "If I get sleepy, I can just get some coffee.\x01",
            "It's peeeerfect for reading.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4369")

    TalkEnd(0xFE)
    Return()

    # Function_10_3E42 end

    def Function_11_436D(): pass

    label("Function_11_436D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_43FF")

    ChrTalk(    #193
        0xFE,
        "Yeah, yeah, the Editor-In-Chief has it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "All right, even if I have to write it by hand,\x01",
            "we are putting out the Liberl News!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_43FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_449A")

    ChrTalk(    #195
        0xFE,
        "You're those bracer friends of Nial's, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Next time you get some kind of scoop that\x01",
            "might turn into a good article, give it to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_449A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_456B")

    ChrTalk(    #197
        0xFE,
        (
            "Hmm, don't really have any decisive\x01",
            "scoop for our next edition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Seems like Nial's following up\x01",
            "on the threat letters, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Isn't there some kinda juicy case rollin'\x01",
            "around somewhere?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_456B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_4642")

    ChrTalk(    #200
        0xFE,
        (
            "Next edition I'll write up a better article\x01",
            "than Nial!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "But I wonder what was wrong...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "I thought I'd written it pretty well from the\x01",
            "perspective of how those affected by the\x01",
            "earthquake feel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_4642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_475E")

    ChrTalk(    #203
        0xFE,
        (
            "The Imperial ambassador and the Republic\x01",
            "ambassador... I've interviewed both of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "They're pretty weird, if you ask me.\x01",
            "They never talk about the important things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "Especially Ambassador Crainagh of the Empire.\x01",
            "His comments were absolutely unprintable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_475E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_483B")

    ChrTalk(    #206
        0xFE,
        (
            "If I'll be writing the article about the signing\x01",
            "ceremony, I guess I should go cover things\x01",
            "at the villa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "The weather's just about perfect, so I bet a walk\x01",
            "along the Erbe Scenic Route would be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4876")

    label("loc_483B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4876")

    ChrTalk(    #208
        0xFE,
        (
            "Ahhh, Nial takes top posting this time,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4876")

    TalkEnd(0xFE)
    Return()

    # Function_11_436D end

    def Function_12_487A(): pass

    label("Function_12_487A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_496E")

    ChrTalk(    #209
        0xFE,
        (
            "I thought so during the coup d'etat,\x01",
            "but being pushed in a corner only\x01",
            "makes things more exciting, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "Maybe I'll write up an article about simple\x01",
            "recipes you can do even without orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "All right, let's do this!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D3A")

    label("loc_496E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4A22")

    ChrTalk(    #212
        0xFE,
        (
            "Just before it went to the presses,\x01",
            "we changed out the top article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "Uuuugh, I had to help adjust the printing press...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "Well, not that that's anything new.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D3A")

    label("loc_4A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4AB7")

    ChrTalk(    #215
        0xFE,
        (
            "Hmm, who should we work with\x01",
            "on our next special edition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "Actually, I don't think we've had a special\x01",
            "about Ruan's casino yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3A")

    label("loc_4AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_4AF8")

    ChrTalk(    #217
        0xFE,
        (
            "Now, then, today I'm gonna drink, eat,\x01",
            "and sleep!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3A")

    label("loc_4AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B86")

    ChrTalk(    #218
        0xFE,
        "Finally sent it off to press.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "Gonna get something delicious to eat at the\x01",
            "cafe and regain some of my fighting spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3A")

    label("loc_4B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4C91")

    ChrTalk(    #220
        0xFE,
        (
            "I run the culture column, so I don't have a super\x01",
            "tight schedule like some of the people above me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "But, the flip side of that is I get used hard to\x01",
            "help out with other things, so it's not easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "If anything, I'm so busy it's kinda depressing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D3A")

    label("loc_4C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4D3A")

    ChrTalk(    #223
        0xFE,
        (
            "Ultimately, we don't really know the reason\x01",
            "why Elmo's hot springs were boiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "The Editor-In-Chief told me it was a real\x01",
            "half-assed article... *sigh*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3A")

    TalkEnd(0xFE)
    Return()

    # Function_12_487A end

    def Function_13_4D3E(): pass

    label("Function_13_4D3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8A")
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #225
        0xC,
        "#153FAhhh, Joshuuuuua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#1040FHey, Dorothy. Been a whole\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #227
        0xC,
        "#151FYou really came back. Good for you, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#1008FY-Yeah, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xC,
        (
            "#156FI'd love to get a memorial shot...\x02\x03",

            "But, my camera isn't working.\x02\x03",

            "*siiiiiiigh* It really messes with my groove.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#1001FAhaha, I guess your camera's pretty\x01",
            "important to you, Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xC,
        (
            "#150FOf course it is!\x01",
            "It's my claim to fame, ya know.\x02\x03",

            "#151FI wanna be able to take loooots of pictures\x01",
            "of that cute little floaty island soon. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x102,
        (
            "#1054FHaha, ah... you're the same as always,\x01",
            "Dorothy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20F2)
    Jump("loc_5016")

    label("loc_4F8A")


    ChrTalk(    #233
        0xC,
        (
            "#150FThe Editor-In-Chief seems really cool today.\x02\x03",

            "I can hardly believe he's the same guy\x01",
            "people always call that old sly fox. Heehee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5016")

    TalkEnd(0xFE)
    Return()

    # Function_13_4D3E end

    def Function_14_501A(): pass

    label("Function_14_501A")

    Call(0, 15)
    Return()

    # Function_14_501A end

    def Function_15_501F(): pass

    label("Function_15_501F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_50BA")

    ChrTalk(    #234
        0xD,
        (
            "Seems like the Editor-In-Chief's got\x01",
            "something to say to the staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xD,
        (
            "They're upstairs in the editorial room--\x01",
            "all of them, for once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F6")

    label("loc_50BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_514D")

    ChrTalk(    #236
        0xD,
        (
            "Seems like there was a big\x01",
            "case over at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xD,
        (
            "Apparently the reporters have been running\x01",
            "all over since late last night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F6")

    label("loc_514D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_51E2")

    ChrTalk(    #238
        0xD,
        (
            "I wonder if Dorothy's doing a good\x01",
            "job wherever she got sent off to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xD,
        (
            "I'm not Nial, but I still can't\x01",
            "help but worry about her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F6")

    label("loc_51E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_520E")

    ChrTalk(    #240
        0xD,
        "On your way back? Good work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53F6")

    label("loc_520E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52DC")

    ChrTalk(    #241
        0xD,
        (
            "Now, then, the time's come around,\x01",
            "so I'm gonna call it a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xD,
        (
            "The reporters are always here late.\x01",
            "Must be hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xD,
        (
            "I always feel a little bad for leaving\x01",
            "before them every day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F6")

    label("loc_52DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5372")

    ChrTalk(    #244
        0xD,
        "Welcome to the Liberl News Service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xD,
        (
            "If you have business with the reporters,\x01",
            "please go to the editorial room on the\x01",
            "second floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53F6")

    label("loc_5372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_53F6")

    ChrTalk(    #246
        0xD,
        "Welcome to the Liberl News Service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        (
            "The first floor here is reception,\x01",
            "and the second floor is our\x01",
            "editorial room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53F6")

    TalkEnd(0xD)
    Return()

    # Function_15_501F end

    def Function_16_53FA(): pass

    label("Function_16_53FA")

    EventBegin(0x0)
    OP_6D(-59650, 0, 61820, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -63630, 0, 66440, 90)
    SetChrPos(0x102, -63630, 0, 66440, 90)
    SetChrPos(0xF8, -63630, 0, 66440, 90)
    SetChrPos(0xF9, -63630, 0, 66440, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)

    def lambda_54AF():
        OP_6D(-57880, 0, 61180, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54AF)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(300)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)

    ChrTalk(    #248
        0x9,
        (
            "#4POrbal energy's stopped, and it's not just light\x01",
            "and heat that's a problem, but communication\x01",
            "is difficult as well.\x02\x03",

            "However, I don't think that you lot are the\x01",
            "sort of journalists to be deterred by small\x01",
            "stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xA,
        "#5POf course not! We have a job to do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x9,
        (
            "#4PExactly. Many of the citizens now have\x01",
            "no access to information and are trapped\x01",
            "by anxiety and fear.\x02\x03",

            "This is EXACTLY the time for us to provide\x01",
            "accurate information and contribute to society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        (
            "#140F#6PYou ain't gotta tell me twice...\x02\x03",

            "That's exactly the reason us journalists exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xC,
        (
            "#156F#6PBut, but, Nial.\x02\x03",

            "It'll be hard to get an article without\x01",
            "even orbal cameras working, ya know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "#4PDorothy is right, most of our\x01",
            "equipment doesn't work.\x02\x03",

            "However, to use that as a reason to abandon the\x01",
            "duty of mass media is the utmost of unacceptable.\x02\x03",

            "Everyone, I don't care what you do, do anything\x01",
            "you can come up with to get our next edition out\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_69(0x0, 0x7D0)
    OP_A2(0x20EF)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    EventEnd(0x0)
    Return()

    # Function_16_53FA end

    def Function_17_58C1(): pass

    label("Function_17_58C1")

    EventBegin(0x0)
    Fade(1000)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x101, -59120, 0, 122980, 180)
    SetChrPos(0x105, -60010, 0, 123340, 180)
    SetChrPos(0x104, -58800, 0, 124220, 180)
    SetChrPos(0x108, -60490, 0, 124220, 180)
    OP_6D(-58080, 0, 123630, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    OP_0D()

    ChrTalk(    #254
        0x101,
        (
            "#1011F#6PThere he is!\x02\x03",

            "#1001FHeeey, Nial! Hellooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x8,
        "#142F#5PWho in the hell...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #256
        0x8,
        (
            "#141FWell, whaddya know! You guys!\x01",
            "How ya doin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x105,
        "#048F#6PGood day, Nial.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x104,
        "#031F#6PHeh, pardon our intrusion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x8,
        (
            "#143FOh, it's that bard guy and...\x01",
            "Erm, Your Highness!\x01",
            "Er, good day to you, yeah!\x02\x03",

            "You even have Zin the Immovable\x01",
            "of Calvard with you! You got kind of\x01",
            "a gang going here, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1016F#6PHaha... A lot of stuff's happened\x01",
            "since we met last.\x02\x03",

            "#1006FHow'd your coverage of the election\x01",
            "in Ruan go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x8,
        (
            "#141FDamn well, that's how! Got the article\x01",
            "done, thanks in part to you guys.\x02\x03",

            "Speakin' of, what brings you by today?\x01",
            "Got a hot scoop for your old buddy Nial?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1025F#6PWell, actually, we're the ones who'd\x01",
            "like to know something.\x02\x03",

            "We heard the Liberl News received a\x01",
            "threatening letter...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #263
        0x8,
        (
            "#143FYou guys're investigating that thing?\x02\x03",

            "I figured the military woulda been taking\x01",
            "care of that one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#1006F#6PWe're working on request from\x01",
            "the military, actually.\x02\x03",

            "So, do you know anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x8,
        (
            "#145FWell, I just got back to the capital,\x01",
            "so I don't know much.\x02\x03",

            "To be honest, I'd like to hear what\x01",
            "YOU guys know, if anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#1019F#6PThat's real helpful, Nial.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x104,
        (
            "#030F#6PCome now, you're a newsman,\x01",
            "a hound for a good story.\x02\x03",

            "Surely you must have a clue as\x01",
            "to who our villain is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x8,
        "#142FTsk... I don't have time for this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x105,
        (
            "#045F#6PUm, that's a bit impolite, you two.\x02\x03",

            "#043FNial? I know this is a lot to ask...\x02\x03",

            "But, please, if you know anything at all,\x01",
            "share it with us. Please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x8,
        (
            "#143FWhoa, hey, Your Highness!\x01",
            "You don't need to lower your\x01",
            "head to ME!\x02\x03",

            "#145FFor cryin'... Fine, fine.\x02\x03",

            "#140FOkay, so, this is off the record, but...\x01",
            "we ain't the only ones who got a letter.\x01",
            "Not even close.\x02\x03",

            "Leiston Fortress got one...\x02\x03",

            "Then the cathedral, the airship company,\x01",
            "the Hotel Roenbaum...\x02\x03",

            "And then both embassies, Grancel Castle,\x01",
            "AND the Erbe Royal Villa all got one too!\x02\x03",

            "There were nine letters in total.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x108, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #271
        0x8,
        "#143FHuh? Somethin' wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_63(0x105)
    OP_63(0x104)
    OP_63(0x108)

    ChrTalk(    #272
        0x101,
        (
            "#1007F#6PEr. Nial.\x02\x03",

            "We heard that from the military already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#143FWHAT?!\x02\x03",

            "#145FDAMN IT! That was my\x01",
            "big scoop for the day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x108,
        (
            "#073F#6PDoesn't look like we're going to\x01",
            "get much out of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        "#1007F#6PYeah, time to move on, I think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "#144FNow you wait just one second, missy!\x02\x03",

            "You keep talkin' like that and Nial Burns,\x01",
            "star reporter for the Liberl News, is gonna\x01",
            "have a name worth a pile of crap!\x02\x03",

            "#141FAll right, all right.\x01",
            "Lemme let you in on my take of this whole\x01",
            "mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        "#1015F#6PWell, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x104,
        (
            "#035F#6PHeh. You may want to be brief,\x01",
            "Mr. Burns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x8,
        (
            "#142F...Fine. Listen up.\x02\x03",

            "Here's the short of it. My gut tells me\x01",
            "this is some kind of huge prank.\x01",
            "The threats aren't real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        "#1025F#6PWe'd thought of that, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x108,
        (
            "#070F#6PYou sound awfully sure, though.\x01",
            "Mind telling us why you're so convinced?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x8,
        (
            "#140FOkay, trick is, I've covered terrorist threats\x01",
            "like this before, right? But with this...there's\x01",
            "no reality to the threat.\x02\x03",

            "Threats only work and have power if they\x01",
            "describe, or at least imply, something nasty\x01",
            "that's gonna happen, see?\x02\x03",

            "These letters have exactly NONE of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x104,
        (
            "#030F#6PMr. Burns does have a point.\x02\x03",

            "'Disaster will be visited upon you' does not\x01",
            "offer much in the way of a specific terror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x8,
        (
            "#141FExactly.\x02\x03",

            "I've got a hunch this isn't about stopping\x01",
            "the signing ceremony at all.\x02\x03",

            "This is more about gettin' people worked\x01",
            "up over a threat, and then sittin' back\x01",
            "and watchin' the fireworks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#1004F#6PI see... That's kind of a good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x105,
        (
            "#047F#6PThere is some sense behind it.\x02\x03",

            "#542FI'm still bothered by the fact that so\x01",
            "many letters were sent, though...\x02\x03",

            "And each and every one was sent to a place\x01",
            "involved with the ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x108,
        (
            "#074F#6PYes. For a prank, whoever did this seems\x01",
            "to know a lot about what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#145FThat does seem kinda true...\x01",
            "on the surface.\x02\x03",

            "#141FThink about it, though. All that info would be\x01",
            "pretty easy to find with a little digging.\x01",
            "Hell, I knew about those places, weeks ago.\x02\x03",

            "Anyway, I'm gonna be workin' this on the\x01",
            "assumption that it's a prank.\x02\x03",

            "Maybe you guys should stick to your\x01",
            "guns about it being a real threat, and we can\x01",
            "compare notes later, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#1006F#6PYeah, good idea!\x02\x03",

            "#1001FThanks, Nial. That actually helped a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x8,
        (
            "#141FDarn right it did.\x02\x03",

            "Just stop by if you want to swap stories.\x02\x03",

            "I'll be sittin' around here until the\x01",
            "pact's signed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1011F#6POkay!\x02\x03",

            "#1004FOh, speaking of 'sitting around here'...\x01",
            "I don't see Dorothy anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x8,
        (
            "#143FAhh, right.\x01",
            "She's off working the Bose region.\x02\x03",

            "I sent her to snag some photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        "#1015F#6PWhat, for a special of some kind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#141FYeah, related to the Royal Army.\x02\x03",

            "You remember that old fort the\x01",
            "sky bandits were using as a base,\x01",
            "right? The one you guys busted.\x02\x03",

            "The army decided those rats had\x01",
            "the right idea, and have claimed and\x01",
            "repurposed it as a training facility.\x02\x03",

            "They're runnin' airship pilot training\x01",
            "out of there now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1006F#6POh, okay. Neat!\x02\x03",

            "So she went off to get coverage\x01",
            "of the base, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x8,
        (
            "#145FThat's the idea, yeah.\x02\x03",

            "I was a little worried about sendin'\x01",
            "her out on her own, but...gotta do it\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1016F#6PDorothy out on her own, huh?\x01",
            "Scary...\x02\x03",

            "#1004FOh! Wait. Duh! Speaking of girls out on\x01",
            "their own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x8,
        "#143FUh, what's up?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #299
        "\x07\x05Estelle explained the situation with Renne's parents.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #300
        0x8,
        (
            "#142FHarold Hayworth, a trader from Crossbell...\x02\x03",

            "Hmm... Never heard of the guy.\x02\x03",

            "Pretty sure he's never been in our classifieds...\x01",
            "or our 'wanted' column, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        "#1007F#6PFigures...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x8,
        (
            "#141FBut hey. This is part of the job, right?\x02\x03",

            "If you guys are totally stuck, I'll help you out.\x02\x03",

            "We can put 'em up in the classifieds, if you\x01",
            "want. I even have a few people in Crossbell\x01",
            "I could poke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x101,
        (
            "#1001F#6PThanks, Nial!\x02\x03",

            "#1008FHaha... You're way more reliable\x01",
            "than I thought you'd be.\x02\x03",

            "I think I need to upgrade my opinion\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x8,
        (
            "#147FHa! 'Course you do!\x02\x03",

            "#144FWait a minute... Whaddya mean?\x01",
            "Was I not reliable before?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        "#1016F#6PAhaha... Just kidding.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_721E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as chose Agate as teammate in Ch. 1\x01",           # 0
            "Set as chose Scherazard as teammate in Ch. 1\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7212"),
        (1, "loc_7218"),
        (SWITCH_DEFAULT, "loc_721E"),
    )


    label("loc_7212")

    OP_A2(0x1201)
    Jump("loc_721E")

    label("loc_7218")

    OP_A3(0x1200)
    Jump("loc_721E")

    label("loc_721E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7286")

    ChrTalk(    #306
        0x108,
        (
            "#070F#6PAll right! Let's get back to the\x01",
            "guildhouse, then.\x02\x03",

            "Agate should be back by now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72E9")

    label("loc_7286")


    ChrTalk(    #307
        0x108,
        (
            "#070F#6PAll right! Let's get back to the\x01",
            "guildhouse, then.\x02\x03",

            "Scherazard should be back by now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E9")


    ChrTalk(    #308
        0x104,
        "#031F#6PHopefully, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x105,
        "#048F#6PThank you again, Nial.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x8,
        "#141FEh, it was no big. Come by again any time.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-59640, 0, 123290, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_8C(0x8, 90, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x0, -59640, 0, 123290, 90)
    SetChrPos(0x1, -59640, 0, 123290, 90)
    SetChrPos(0x2, -59640, 0, 123290, 90)
    SetChrPos(0x3, -59640, 0, 123290, 90)
    Sleep(500)
    FadeToBright(1000, 0)
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x1628)
    OP_28(0x8B, 0x2, 0x1000)
    OP_28(0x8B, 0x1, 0x2000)
    OP_28(0x8B, 0x1, 0x4000)
    EventEnd(0x0)
    Return()

    # Function_17_58C1 end

    def Function_18_7424(): pass

    label("Function_18_7424")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7444")
    Call(0, 19)
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_7444")

    Fade(1000)
    SetChrPos(0x101, 61220, 0, 550, 0)
    SetChrPos(0x107, 60230, 0, 550, 0)
    SetChrPos(0xF7, 60630, 0, -480, 0)
    SetChrPos(0xF9, 61610, 0, -550, 0)
    OP_8C(0xE, 180, 0)
    SetChrSubChip(0xE, 0)
    OP_6D(61320, 0, 1590, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #311
        0x101,
        "#1015F#6PSay, barkeep. What're your specials?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xE,
        "#6POur best special's our coffee, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xE,
        (
            "#6POur most popular item is our dark-roasted\x01",
            "dragon bean blend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xE,
        "#6POur spice-heavy curry is also real popular!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#1006F#6PSpicy curry and bitter coffee, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x107,
        "#061FIt's a bitter, spicy, delicious store! ♪\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7663")

    ChrTalk(    #317
        0x106,
        (
            "#051F#2PHey, has a little girl in a white dress\x01",
            "been by?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76AA")

    label("loc_7663")


    ChrTalk(    #318
        0x103,
        (
            "#020F#2PPardon, but have you seen a\x01",
            "little girl in a white dress?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76AA")


    ChrTalk(    #319
        0xE,
        "#6PYeah, she was in here not too long ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xE,
        (
            "#6PShe ordered a Cafe au Lait and seemed\x01",
            "to love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xE,
        (
            "#6PCome to think, she did ask me a very\x01",
            "strange question, though...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7790")

    ChrTalk(    #322
        0x108,
        "#073FAnd what would that be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_77B3")

    label("loc_7790")


    ChrTalk(    #323
        0x105,
        "#044FWhat would that be, sir?\x02",
    )

    CloseMessageWindow()

    label("loc_77B3")


    ChrTalk(    #324
        0xE,
        (
            "#6PWhat was it, now...? 'Do you know where\x01",
            "they sell the sweets that disappear if you\x01",
            "leave them alone,' I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        (
            "#1006F#6PHuh. 'Sweets that disappear if you leave\x01",
            "them alone'...\x02\x03",

            "Okay, wrote that down!\x02\x03",

            "I think we're tightening the noose!\x01",
            "I might know what this one is...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1633)
    OP_28(0x8C, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_18_7424 end

    def Function_19_78DA(): pass

    label("Function_19_78DA")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_7956"),
        (1, "loc_795C"),
        (SWITCH_DEFAULT, "loc_7962"),
    )


    label("loc_7956")

    OP_A2(0x1200)
    Jump("loc_7962")

    label("loc_795C")

    OP_A2(0x1201)
    Jump("loc_7962")

    label("loc_7962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7970")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_7974")

    label("loc_7970")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_7974")

    Return()

    # Function_19_78DA end

    def Function_20_7975(): pass

    label("Function_20_7975")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_79B4")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_79CE")

    label("loc_79B4")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_79CE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_7975 end

    def Function_21_79EE(): pass

    label("Function_21_79EE")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 60480, 0, 540, 0)
    SetChrPos(0x102, 61400, 0, 540, 0)
    SetChrPos(0xF8, 60480, 0, -800, 0)
    SetChrPos(0xF9, 61400, 0, -800, 0)
    OP_0D()

    ChrTalk(    #326
        0xE,
        "Oh! Why, I know that series.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xE,
        (
            "Is that Gambler Jack, the series popular in the\x01",
            "harbor area that I've heard so much about,\x01",
            "perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x101,
        "#1004FAh, these novels?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xE,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xE,
        (
            "It's a drama about a gambler with\x01",
            "a curious fate, set in the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xE,
        "I've been wanting to read it for a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        "#1015F(I do owe him a bit...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Hand Over Books\x01",      # 0
            "Don't\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BFE")
    Call(0, 23)
    Jump("loc_7C22")

    label("loc_7BFE")


    ChrTalk(    #333
        0x101,
        "#1016F(Nah, I don't think so.)\x02",
    )

    CloseMessageWindow()

    label("loc_7C22")

    EventEnd(0x0)
    Return()

    # Function_21_79EE end

    def Function_22_7C25(): pass

    label("Function_22_7C25")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 60480, 0, 540, 0)
    SetChrPos(0x102, 61400, 0, 540, 0)
    SetChrPos(0xF8, 60480, 0, -800, 0)
    SetChrPos(0xF9, 61400, 0, -800, 0)
    OP_0D()

    ChrTalk(    #334
        0xE,
        "Oh, what is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Hand Over Books\x01",      # 0
            "Don't\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CE6")
    Call(0, 23)
    Jump("loc_7D0A")

    label("loc_7CE6")


    ChrTalk(    #335
        0x101,
        "#1016F(Nah, I don't think so.)\x02",
    )

    CloseMessageWindow()

    label("loc_7D0A")

    EventEnd(0x0)
    Return()

    # Function_22_7C25 end

    def Function_23_7D0D(): pass

    label("Function_23_7D0D")


    ChrTalk(    #336
        0x101,
        (
            "#1001FAll right, here you go.\x01",
            "It's all yours, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xE,
        "Oh, that isn't why I mentioned it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1000FDon't worry about it.\x02\x03",

            "It's thanks for the great curry and\x01",
            "coffee before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xE,
        "That's very kind of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xE,
        "I'd be happy to take them.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #341
        "Handed over all of #2CGambler Jack#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3F(0x23A, 1)
    OP_3F(0x23B, 1)
    OP_3F(0x23C, 1)
    OP_3F(0x23D, 1)
    OP_3F(0x23E, 1)
    OP_3F(0x23F, 1)
    OP_3F(0x240, 1)
    OP_3F(0x241, 1)
    OP_3F(0x242, 1)
    OP_3F(0x243, 1)
    OP_3F(0x244, 1)
    OP_3F(0x245, 1)
    OP_3F(0x246, 1)
    OP_3F(0x247, 1)
    OP_0D()

    ChrTalk(    #342
        0xE,
        (
            "You have my thanks. I'm looking forward\x01",
            "to reading them little by little over the\x01",
            "coming nights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xE,
        (
            "Oh, And as a token from my side,\x01",
            "allow me to offer you this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #344
        "\x07\x00Received #1047i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x417, 1)
    OP_0D()

    ChrTalk(    #345
        0x102,
        "#1044FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xE,
        (
            "When I was still a diplomat,\x01",
            "I picked this up in Arteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1015FArteria... That's where the headquarters\x01",
            "of the Septian Church is, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xE,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xE,
        (
            "In the distant past, back during the Zemurian era,\x01",
            "things were made with this metal, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x102,
        (
            "#1044FThe Zemurian era? It must be incredibly old.\x01",
            "Certainly, I've never seen this alloy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xE,
        "Haha, I don't know how true it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xE,
        (
            "Incidentally, apparently the techniques\x01",
            "to mold that metal have long been lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1018FHuh, thinking about it, that\x01",
            "makes it pretty incredible.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 7)), scpexpr(EXPR_END)), "loc_82BC")

    ChrTalk(    #354
        0x102,
        (
            "#1040FI believe we traded books with you\x01",
            "for a weapon before, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xE,
        "Haha, I remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xE,
        (
            "This isn't anything that incredible this\x01",
            "time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x101,
        "#1001FNo, we're still grateful for it. Seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8333")

    label("loc_82BC")


    ChrTalk(    #358
        0xE,
        (
            "Haha, it isn't anything that incredible,\x01",
            "but perhaps it'll be a good luck charm\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1001FYeah, thanks!\x02",
    )

    CloseMessageWindow()

    label("loc_8333")

    OP_A2(0x10C4)
    Return()

    # Function_23_7D0D end

    def Function_24_8337(): pass

    label("Function_24_8337")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #360
        (
            "\x07\x05The Baral Coffee House's specialty!\x01",
            "[Curry of Dreams] - 900 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #361
        (
            "\x07\x05Try our hot curry, cooked to perfection\x01",
            "with our secret spices!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_8337 end

    def Function_25_83EF(): pass

    label("Function_25_83EF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #362
        (
            "\x07\x05- Menu -\x01",
            "Mocking Pie           400 mira\x01",
            "Tomatrio Sandwich    1400 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #363
        (
            "\x07\x05- Chef's Recommendations -\x01",
            "Seafood Hotpot     1200 mira\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_83EF end

    SaveToFile()

Try(main)
