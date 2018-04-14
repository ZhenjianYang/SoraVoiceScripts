from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '奈尔',                                 # 9
        '总编',                                 # 10
        '诺蒂亚',                               # 11
        '法尔茨',                               # 12
        '朵洛希',                               # 13
        '莎莉亚',                               # 14
        '巴拉尔',                               # 15
        '科尼嘉',                               # 16
        '小说',                                 # 17
        '科蕾蒂',                               # 18
        '彭萨',                                 # 19
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
        "Function_4_F23",          # 04, 4
        "Function_5_16FE",         # 05, 5
        "Function_6_1703",         # 06, 6
        "Function_7_1FAF",         # 07, 7
        "Function_8_1FB4",         # 08, 8
        "Function_9_2791",         # 09, 9
        "Function_10_2D56",        # 0A, 10
        "Function_11_3109",        # 0B, 11
        "Function_12_33CA",        # 0C, 12
        "Function_13_368E",        # 0D, 13
        "Function_14_38B8",        # 0E, 14
        "Function_15_38BD",        # 0F, 15
        "Function_16_3B32",        # 10, 16
        "Function_17_3E67",        # 11, 17
        "Function_18_506E",        # 12, 18
        "Function_19_53DD",        # 13, 19
        "Function_20_5479",        # 14, 20
        "Function_21_54F2",        # 15, 21
        "Function_22_56D1",        # 16, 22
        "Function_23_57B0",        # 17, 23
        "Function_24_5C14",        # 18, 24
        "Function_25_5CA2",        # 19, 25
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E7")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #0
        0x101,
        "#1001F奈尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#143F哟，是艾丝蒂尔啊……\x02\x03",

            "还有约修亚……\x01",
            "一起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1040F嗯，好久不见。\x02\x03",

            "奈尔先生你们\x01",
            "还是看上去很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#140F嗯，总编也说过，\x01",
            "就这点程度的劳累\x01",
            "是不会让我们放下笔杆的。\x02\x03",

            "我们才不会随了结社的心愿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1015F不过导力器都不能用了，\x01",
            "你们接下来准备怎么办？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 300)

    ChrTalk(    #5
        0x8,
        (
            "#145F嗯，问题就在这儿。\x02\x03",

            "现在朵洛希的\x01",
            "照相机也不能用了。\x02\x03",

            "#141F不过我们也不是束手无策。\x02\x03",

            "接下来我准备晋见艾莉茜雅\x01",
            "女王，和她商量一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1001F哟，真努力……\x01",
            "感觉放心了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 300)

    ChrTalk(    #7
        0x8,
        (
            "#141F那么，约修亚。\x02\x03",

            "我有不可斗量的\x01",
            "问题要采访你，\x01",
            "不过先要推迟一下。\x02\x03",

            "#147F你就洗干净脖子等着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1054F哈哈……请手下留情。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D7)
    Jump("loc_A3C")

    label("loc_9E7")


    ChrTalk(    #9
        0x8,
        (
            "#140F要做的事和要解决问题有很多，\x01",
            "不能呆在这里发呆了。\x02\x03",

            "记者就是要\x01",
            "行动优先的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3C")

    Jump("loc_F1F")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4A")

    ChrTalk(    #10
        0x8,
        (
            "#145F哇～真没办法……\x02\x03",

            "#140F……因为军队的管制\x01",
            "所以没法清清楚楚地在报上\x01",
            "报导那个巨大机器人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1015F好像是希德中校说的吧？\x02\x03",

            "#1000F不过，如果大众知道出现了\x01",
            "那种东西一定会引发骚动的。\x02\x03",

            "中校应该也是\x01",
            "顾虑到了这一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#140F大概吧……\x02\x03",

            "#142F可利贝尔通讯不是\x01",
            "政府的御用杂志。\x02\x03",

            "我们的使命终究是\x01",
            "中立地发布信息。\x02\x03",

            "明知有又不公开的行为\x01",
            "也能算是撒谎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1015F可、可能\x01",
            "也有点道理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#145F算了，这次就算我输了。\x02\x03",

            "#140F好，朵洛希那家伙\x01",
            "也该回来了……\x02\x03",

            "能不能赶上你们出发倒是\x01",
            "有点不得而知。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1666)
    Jump("loc_C97")

    label("loc_C4A")


    ChrTalk(    #15
        0x8,
        (
            "#140F朵洛希那家伙\x01",
            "也该回来了……\x02\x03",

            "能不能赶上你们出发倒是\x01",
            "有点不得而知。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C97")

    Jump("loc_F1F")

    label("loc_C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_E99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD")

    ChrTalk(    #16
        0x8,
        (
            "#143F……你问我有没有看见玲？\x02\x03",

            "#140F就是昨天在酒馆\x01",
            "一起吃饭的女孩子？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1011F对对，你在这附近\x01",
            "有没有见过她？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#140F抱歉，不巧的是我今天\x01",
            "一直没离开杂志社。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1015F哦，这样啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_DD4")

    ChrTalk(    #20
        0x8,
        (
            "#140F那你们可以去问问其他人。\x02\x03",

            "#141F上次我请你们去的咖啡馆\x01",
            "主人也是个相当有实力的情报通。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF7")

    label("loc_DD4")


    ChrTalk(    #21
        0x8,
        "#140F那你们可以去问问其他人。\x02",
    )

    CloseMessageWindow()

    label("loc_DF7")

    OP_A2(0x2)
    Jump("loc_E96")

    label("loc_DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_E6A")

    ChrTalk(    #22
        0x8,
        (
            "#140F抱歉，找迷路的孩子\x01",
            "请去问其他人。\x02\x03",

            "上次我请你们去的咖啡馆\x01",
            "主人也是个相当有实力的情报通。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E96")

    label("loc_E6A")


    ChrTalk(    #23
        0x8,
        (
            "#140F抱歉，找迷路的孩子\x01",
            "请去问其他人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E96")

    Jump("loc_F1F")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_F07")

    ChrTalk(    #24
        0x8,
        (
            "#140F今天跑了一天，也没\x01",
            "找到什么不错的新闻线索。\x02\x03",

            "希望朵洛希那家伙\x01",
            "能抓到些什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0B")

    label("loc_F07")

    Call(0, 17)

    label("loc_F0B")

    Jump("loc_F1F")

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_F18")
    Jump("loc_F1F")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_F1F")

    label("loc_F1F")

    TalkEnd(0x8)
    Return()

    # Function_3_75E end

    def Function_4_F23(): pass

    label("Function_4_F23")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F9A")

    ChrTalk(    #25
        0xFE,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "我不觉得现在是\x01",
            "危机时刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "倒不如说是利贝尔通讯社的\x01",
            "真正的价值正在受到考验。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FA")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1024")

    ChrTalk(    #28
        0xFE,
        (
            "哟，昨天那么晚\x01",
            "你们还在配合\x01",
            "奈尔的采访啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "他和刚才回来的\x01",
            "朵洛希一起出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "说是要去城里收集\x01",
            "昨天的事件的消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FA")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_10C5")

    ChrTalk(    #31
        0xFE,
        (
            "让朵洛希一个人去采访\x01",
            "确实令人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "不管怎么样，还是希望能认真顺利地\x01",
            "完成工作回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "虽然途中可能会受到耽搁，\x01",
            "不过这买卖看重的是结果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FA")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_11EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119D")

    ChrTalk(    #34
        0xFE,
        (
            "……记者如果不死缠烂打\x01",
            "就无法获得好的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "但是，在写报道的时候必须\x01",
            "尽量远离对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "不用说采访对方和事件了，\x01",
            "有时候甚至不能从外侧\x01",
            "审视自我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "只有发现真实的人\x01",
            "才是真正的记者。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_11E7")

    label("loc_119D")


    ChrTalk(    #38
        0xFE,
        (
            "记者甚至不能从外侧\x01",
            "审视自我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "只有发现真实的人\x01",
            "才是真正的记者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E7")

    Jump("loc_16FA")

    label("loc_11EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1393")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1378")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_128F")

    ChrTalk(    #40
        0xFE,
        (
            "哟，艾丝蒂尔，\x01",
            "奈尔刚才回来了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1000F啊，真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "嗯，他在资料室。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "哈哈，瞧他那张脸就知道\x01",
            "他没找到什么好的材料了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1372")

    label("loc_128F")


    ChrTalk(    #44
        0xFE,
        "哎呀，这不是艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1001F总编先生，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "今天是怎么了。\x01",
            "莫非是找奈尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1000F嗯，因为协会的工作\x01",
            "有点事想问问他。\x02\x03",

            "他已经从卢安\x01",
            "回来了吗？\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "嗯，他应该正好在。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "刚才我还看见\x01",
            "他上了资料室。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1372")

    OP_A2(0x1664)
    Jump("loc_1390")

    label("loc_1378")


    ChrTalk(    #50
        0xFE,
        "奈尔应该在资料室。\x02",
    )

    CloseMessageWindow()

    label("loc_1390")

    Jump("loc_16FA")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_15AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1564")

    ChrTalk(    #51
        0xFE,
        "哎呀，这不是艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1001F总编先生，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "今天是怎么了。\x01",
            "莫非是找奈尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1000F嗯，因为协会的工作\x01",
            "有点事想问问他。\x02\x03",

            "他已经从卢安\x01",
            "回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "嗯，回来是回来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "不过我记得他又去\x01",
            "外面采访了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1015F是吗？可以想象\x01",
            "他仍然是那么忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "嗯，也是工作原因。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "虽然不知道他在哪里，\x01",
            "不过我听说他傍晚前会回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        (
            "#040F看来先去其他地方\x01",
            "会比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x108,
        (
            "#070F是啊，这里就\x01",
            "放放吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1680)
    Jump("loc_15AB")

    label("loc_1564")


    ChrTalk(    #63
        0xFE,
        "奈尔出去了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "虽然不知道他在哪里，\x01",
            "不过我听说他傍晚前会回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AB")

    Jump("loc_16FA")

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_16FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168A")

    ChrTalk(    #65
        0xFE,
        (
            "『卢安市的新市长\x01",
            "　终于确定！』……了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "奈尔写这种文章可能会觉得闷，\x01",
            "不过写得还不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "好，虽然有点对不起诺蒂亚，\x01",
            "不过还是把这作为下一期的头条吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1000F（他们看来在讨论呢……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_16FA")

    label("loc_168A")


    ChrTalk(    #69
        0xFE,
        (
            "『卢安市的新市长\x01",
            "　终于确定！』……了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "好，虽然有点对不起诺蒂亚，\x01",
            "不过还是把这作为下一期的头条吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FA")

    TalkEnd(0x9)
    Return()

    # Function_4_F23 end

    def Function_5_16FE(): pass

    label("Function_5_16FE")

    Call(0, 6)
    Return()

    # Function_5_16FE end

    def Function_6_1703(): pass

    label("Function_6_1703")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                               # 0
            "买东西\x01",                             # 1
            "招牌菜『完熟咖喱饭』　900米拉\x01",      # 2
            "离开\x01",                               # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1782")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_1782")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1857")
    SubMira(900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #71
        "\x06\x07\x02完熟咖喱饭\x07\x00已经品尝过了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1849")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_181F")
    Jump("loc_1849")

    label("loc_181F")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #72
        "\x06\x07\x02完熟咖喱饭\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_1849")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_187D")

    label("loc_1857")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #73
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_187D")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_188F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18A9")
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    label("loc_18A9")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇集齐了全部『牌技师杰克』】\x01",      # 0
            "【◇没集齐全部『牌技师杰克』】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1933"),
        (1, "loc_197C"),
        (SWITCH_DEFAULT, "loc_19C5"),
    )


    label("loc_1933")

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
    Jump("loc_19C5")

    label("loc_197C")

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
    Jump("loc_19C5")

    label("loc_19C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x23A, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x23B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23E, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23F, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x240, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x241, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x242, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x243, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x244, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x245, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x246, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x247, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3A")
    OP_A2(0x10C3)
    Call(0, 21)
    TalkEnd(0xE)
    Return()

    label("loc_1A3A")

    Call(0, 22)
    TalkEnd(0xE)
    Return()

    label("loc_1A42")


    ChrTalk(    #74
        0xE,
        (
            "不用导力器做饭虽然麻烦，\x01",
            "不过别有一番风味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "同样是煮出来的咖啡，\x01",
            "却感觉这样更加好喝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "以后也可以考虑用\x01",
            "炭火或者柴来煮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9D")

    label("loc_1ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B32")

    ChrTalk(    #77
        0xE,
        (
            "我想港口怎么这么吵，\x01",
            "原来是发生了大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xE,
        (
            "不过今后的夜晚会变得安静，\x01",
            "不是也挺好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9D")

    label("loc_1B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 3)), scpexpr(EXPR_END)), "loc_1BA1")

    ChrTalk(    #79
        0xE,
        (
            "女孩子喝着奶咖，\x01",
            "问了我一个奇怪的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "她问『没人管就会消失的点心\x01",
            "在哪儿有卖？』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDD")

    label("loc_1BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_1BAF")
    Call(0, 18)
    Jump("loc_1CDD")

    label("loc_1BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(    #81
        0xE,
        (
            "在城里工作的时候，\x01",
            "每次去外国出差\x01",
            "都是在卢安坐的船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        (
            "那时候还没有\x01",
            "定期船呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xE,
        (
            "船自然没飞船\x01",
            "移动得快，\x01",
            "不过也有它的长处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        (
            "慢慢地花时间前进……\x01",
            "人类本就是这样的生物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xE,
        (
            "飞船出现之后人变得\x01",
            "越来越忙碌了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1CDD")

    label("loc_1C9C")


    ChrTalk(    #86
        0xE,
        (
            "哈哈，我会这么想\x01",
            "说明我是老了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xE,
        "算了，当我自言自语吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1CDD")

    Jump("loc_1F9D")

    label("loc_1CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D73")

    ChrTalk(    #88
        0xE,
        (
            "最近，利贝尔通讯的那帮人\x01",
            "好像在利贝尔中上窜下跳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "现在这当口，话题\x01",
            "应该是很多吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        (
            "希望他们能尽量\x01",
            "带来一些好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9D")

    label("loc_1D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1EDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E48")

    ChrTalk(    #91
        0xE,
        (
            "王国军的重建和签字仪\x01",
            "式的准备使军人和官员们\x01",
            "都看上去很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "对市民来说平静的\x01",
            "生活反而回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        (
            "我渐渐感觉到自己\x01",
            "是从仕官生活中解放出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xE,
        "虽然对以前的同事有点不好意思。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1EDC")

    label("loc_1E48")


    ChrTalk(    #95
        0xE,
        (
            "王国军的重建和签字仪\x01",
            "式的准备使军人和官员们\x01",
            "都看上去很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xE,
        (
            "虽然对以前的同事有点不好意思，\x01",
            "但我渐渐感觉到自己\x01",
            "是从仕官生活中解放出来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDC")

    Jump("loc_1F9D")

    label("loc_1EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F66")

    ChrTalk(    #97
        0xE,
        "哟，我好像见过你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        (
            "你是奈尔认识的\x01",
            "游击士小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        (
            "咖啡和咖喱饭\x01",
            "欢迎来到王都的特色咖啡厅『巴拉尔』！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1F9D")

    label("loc_1F66")


    ChrTalk(    #100
        0xE,
        (
            "咖啡和咖喱饭\x01",
            "欢迎来到王都的特色咖啡厅『巴拉尔』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAB")
    OP_A2(0x0)
    Jump("loc_1FAB")

    label("loc_1FAB")

    TalkEnd(0xE)
    Return()

    # Function_6_1703 end

    def Function_7_1FAF(): pass

    label("Function_7_1FAF")

    Call(0, 8)
    Return()

    # Function_7_1FAF end

    def Function_8_1FB4(): pass

    label("Function_8_1FB4")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                            # 0
            "买东西\x01",                          # 1
            "招牌菜『热海汁』　1200米拉\x01",      # 2
            "离开\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2030")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCA)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_2030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2135")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20FD")
    SubMira(1200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #101
        "\x06\x07\x02热海汁\x07\x00已经品尝过了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_20C9")
    Jump("loc_20EF")

    label("loc_20C9")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x06\x07\x02热海汁\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_20EF")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_2123")

    label("loc_20FD")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #103
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_2123")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x11)
    Return()

    label("loc_2135")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214F")
    FadeToBright(300, 0)
    TalkEnd(0x11)
    Return()

    label("loc_214F")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21BB")

    ChrTalk(    #104
        0x11,
        (
            "呼，总算习惯了\x01",
            "用火来做饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "是钓公师团的人们\x01",
            "告诉我的，\x01",
            "大概是暂停营业了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278D")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2248")

    ChrTalk(    #106
        0x11,
        (
            "昨天在西街区情报部好像\x01",
            "和王国军发生了战斗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x11,
        (
            "情报部的人好像\x01",
            "尽数被亲卫队逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x11,
        (
            "能够恰好赶到，\x01",
            "真不愧是尤莉亚上尉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278D")

    label("loc_2248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_236A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2321")

    ChrTalk(    #109
        0x11,
        (
            "我昨天去西街区的\x01",
            "咖啡馆吃了\x01",
            "咖喱饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        (
            "那种绝妙的调味掌控\x01",
            "真如传说中那般会让人上瘾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "咖啡也很好喝，\x01",
            "真令人满意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        (
            "特色是又苦又辣的店……\x01",
            "构思也挺新颖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        (
            "主人不愧是\x01",
            "海归派。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2367")

    label("loc_2321")


    ChrTalk(    #114
        0x11,
        (
            "特色是又苦又辣的店……\x01",
            "构思也挺新颖的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        (
            "主人不愧是\x01",
            "海归派。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2367")

    Jump("loc_278D")

    label("loc_236A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_244A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FB")

    ChrTalk(    #116
        0x11,
        "欢迎！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        (
            "各位，昨晚都\x01",
            "尽兴了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x11,
        (
            "你们能那么开心，\x01",
            "作为店方的我们也很荣幸。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12F, 400)

    ChrTalk(    #119
        0x11,
        (
            "姐姐你们也请\x01",
            "再来吃饭。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2447")

    label("loc_23FB")


    ChrTalk(    #120
        0x11,
        (
            "各位，昨晚都\x01",
            "尽兴了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        (
            "你们能那么开心，\x01",
            "作为店方的我们也很荣幸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2447")

    Jump("loc_278D")

    label("loc_244A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2497")

    ChrTalk(    #122
        0x11,
        (
            "那么，接下来就是晚饭时间了，\x01",
            "要忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        "今天也要努力！\x02",
    )

    CloseMessageWindow()
    Jump("loc_278D")

    label("loc_2497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_26AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2673")

    ChrTalk(    #124
        0x11,
        (
            "欢迎！\x01",
            "欢迎来到『阳光铃铛』。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x104, 400)

    ChrTalk(    #125
        0x11,
        "咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x11,
        (
            "难道你就是我以前点播\x01",
            "钢琴演奏的奥利维尔先生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x104,
        "#031F哈哈，正是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        (
            "好久没见了啊！\x01",
            "今天到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x104,
        (
            "#034F啊，请不要说\x01",
            "庸俗的话。\x02\x03",

            "#035F在这家店里和你共同度过的\x01",
            "模糊、甜蜜又痛苦的每一天……\x02\x03",

            "对孤独旅行的演奏家来说，\x01",
            "你简直是暗夜里的明灯。\x02\x03",

            "#030F我就是那无法忘记你，\x01",
            "追寻着阳光\x01",
            "返回的小鸟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        "呵呵，你还是老样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x11,
        (
            "你看来很闲，能不能请你\x01",
            "再演奏一曲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x104,
        "#031F哈哈，当然！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_26A7")

    label("loc_2673")

    TurnDirection(0x11, 0x104, 400)

    ChrTalk(    #133
        0x11,
        (
            "奥利维尔先生，你有空\x01",
            "我就再请你弹钢琴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A7")

    Jump("loc_278D")

    label("loc_26AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2735")

    ChrTalk(    #134
        0x11,
        (
            "现在还有很多人\x01",
            "喜欢理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x11,
        (
            "在客人的会话中\x01",
            "也经常冒出上校的话题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x11,
        (
            "说明他虽然做了错事，\x01",
            "不过还是个有魅力的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278D")

    label("loc_2735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_278D")

    ChrTalk(    #137
        0x11,
        "可能是快到签字仪式了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x11,
        (
            "最近，在这家店里也能\x01",
            "看见星星点点的外国人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278D")

    TalkEnd(0x11)
    Return()

    # Function_8_1FB4 end

    def Function_9_2791(): pass

    label("Function_9_2791")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2817")

    ChrTalk(    #139
        0xFE,
        (
            "肉的表面烤得松脆，\x01",
            "非常香。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "生烤菜挺有特色的，\x01",
            "也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "好像火候挺难把握的，\x01",
            "科蕾蒂小姐看来也挺不容易的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D0")

    ChrTalk(    #142
        0xFE,
        (
            "情报部的余党之前\x01",
            "似乎潜伏在港口？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "逃亡的凯诺娜上尉\x01",
            "据说也被亲卫队逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "情报部的所有人\x01",
            "都被逮捕了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "这样的话理查德上校的罪\x01",
            "不会再加重吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2922")

    label("loc_28D0")


    ChrTalk(    #146
        0xFE,
        (
            "情报部的余党之前\x01",
            "似乎潜伏在港口？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "这样的话理查德上校的罪\x01",
            "不会再加重吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2922")

    Jump("loc_2D52")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A09")

    ChrTalk(    #148
        0xFE,
        (
            "昨天我第一次吃了\x01",
            "东街区卖的冰淇淋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "不愧是科洛蒂娅公主，居然\x01",
            "会出城来买冰淇淋吃啊，\x01",
            "确实很美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "只不过我这个人本就\x01",
            "不适应吃冰的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "吃的节奏一慢\x01",
            "冰就不断地化掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "有点郁闷啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2A63")

    label("loc_2A09")


    ChrTalk(    #153
        0xFE,
        (
            "我本来就不适应\x01",
            "吃冰的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "吃的节奏一慢\x01",
            "冰就不断地化掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "有点郁闷啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2A63")

    Jump("loc_2D52")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2A8A")

    ChrTalk(    #156
        0xFE,
        "唔～今天吃什么呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B3B")

    ChrTalk(    #157
        0xFE,
        (
            "曾是理查德上校的女部下的\x01",
            "一名上尉似乎钻了个空子，\x01",
            "现在都还在逃亡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "我记得她叫……凯、凯、凯诺娜上尉？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "好像在士官学校时\x01",
            "和尤莉亚小姐就是竞争对手哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD9")

    ChrTalk(    #160
        0xFE,
        "请不要外传……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "其实我写了信请求宽大\x01",
            "处理理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "过了那么久，\x01",
            "我也想了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "我实在不认为那位上校\x01",
            "只是个坏蛋。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2C2B")

    label("loc_2BD9")


    ChrTalk(    #164
        0xFE,
        (
            "其实我写了信请求宽大\x01",
            "处理理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "我实在不认为那位上校\x01",
            "只是个坏蛋。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2B")

    Jump("loc_2D52")

    label("loc_2C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2CBC")

    ChrTalk(    #166
        0xFE,
        (
            "政变的幕后黑手\x01",
            "理查德上校\x01",
            "好像被关在雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "……上校接下来会\x01",
            "怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "作为政变的罪犯，\x01",
            "是不可能简单脱罪的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D52")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2D52")

    ChrTalk(    #169
        0xFE,
        (
            "政变的时候\x01",
            "很多的城里官员和佣人\x01",
            "都被公爵放了假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "现在那些人好像\x01",
            "也在忙碌地工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "事件的善后很麻烦，\x01",
            "应该是没法很快\x01",
            "复原的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D52")

    TalkEnd(0xFE)
    Return()

    # Function_9_2791 end

    def Function_10_2D56(): pass

    label("Function_10_2D56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DD2")

    ChrTalk(    #172
        0xFE,
        (
            "虽然主人说得悠闲，\x01",
            "不过我很着急！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "因为没了导力器\x01",
            "晚上都不能读书啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "靠蜡烛的话\x01",
            "眼睛会坏掉的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3105")

    label("loc_2DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2E70")

    ChrTalk(    #175
        0xFE,
        "那、那究竟是什么东西啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "在昨天的骚动中我看见有台\x01",
            "巨大的机器人飞走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "利贝尔通讯有可能会\x01",
            "登载详细情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "下一期我一定要买！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3105")

    label("loc_2E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_END)), "loc_2EBE")

    ChrTalk(    #179
        0xFE,
        "今天利贝尔通讯的最新一期出了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "赶紧去买来\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9C")

    label("loc_2EBE")


    ChrTalk(    #181
        0xFE,
        (
            "咦……今天是\x01",
            "利贝尔通讯的发售日？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "利贝尔通讯当然是\x01",
            "指利贝尔通讯啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "这本书也读完了，\x01",
            "我赶紧去买吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "对了，这本书送给你吧。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #185
        "\x07\x00得到了\x1F\x3E\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23E, 1)
    OP_A2(0x10B9)

    label("loc_2F9C")

    Jump("loc_3105")

    label("loc_2F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3003")

    ChrTalk(    #186
        0xFE,
        (
            "哟，不知不觉已经\x01",
            "到了傍晚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "沉浸于书中的世界里的话\x01",
            "一转眼时间就过去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3105")

    label("loc_3003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3083")

    ChrTalk(    #188
        0xFE,
        (
            "由艾莉茜雅女王倡导的互不侵犯\x01",
            "条约的签署也马上就要进行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "作为利贝尔国民的一员,\x01",
            "我也想了解一下\x01",
            "条约的概要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3105")

    label("loc_3083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3105")

    ChrTalk(    #190
        0xFE,
        (
            "艾尔·雷登那家店\x01",
            "虽然也不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "不过还是这家店\x01",
            "最能让我放松下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "困了还能喝咖啡，\x01",
            "是个正合适读书的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3105")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D56 end

    def Function_11_3109(): pass

    label("Function_11_3109")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_315F")

    ChrTalk(    #193
        0xFE,
        "嗯嗯，总编说得没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "好～就算是手写也要\x01",
            "把利贝尔通讯给弄出来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_315F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_31B5")

    ChrTalk(    #195
        0xFE,
        (
            "你们就是奈尔\x01",
            "认识的游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "下次有什么新闻线索\x01",
            "也要留点给我哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_31B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3215")

    ChrTalk(    #197
        0xFE,
        "下一期没什么好的素材\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "恐吓信那边也有\x01",
            "奈尔在追查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "怎么就不\x01",
            "出点事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_3215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_3291")

    ChrTalk(    #200
        0xFE,
        (
            "下一期我一定要写出\x01",
            "胜过奈尔的报道来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "可是，到底是哪儿不对呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "我是以地震受害者的\x01",
            "心情来写完的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_3291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_332C")

    ChrTalk(    #203
        0xFE,
        (
            "帝国大使和共和国大使……\x01",
            "两边我都采访了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "两个人都是老奸巨猾的，\x01",
            "重要的事都没说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "尤其是帝国的达维尔大使的\x01",
            "回答根本就没法登。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_332C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_339A")

    ChrTalk(    #206
        0xFE,
        (
            "要写签字仪式的报道\x01",
            "看来还是得去离宫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "天气也不错，要是去艾尔贝\x01",
            "周游道散步心情一定不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_339A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_33C6")

    ChrTalk(    #208
        0xFE,
        (
            "啊～这次的头条\x01",
            "被奈尔给抢了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C6")

    TalkEnd(0xFE)
    Return()

    # Function_11_3109 end

    def Function_12_33CA(): pass

    label("Function_12_33CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3458")

    ChrTalk(    #209
        0xFE,
        (
            "政变的时候也是的，\x01",
            "越是受压迫，\x01",
            "大家就反而更有热情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "我来写点就算没有导力器\x01",
            "也能轻松烹调的菜吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "好～就这么办～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_3458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_34C0")

    ChrTalk(    #212
        0xFE,
        (
            "在即将截稿之前\x01",
            "新闻被换了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "唔～我也被拉来\x01",
            "帮忙校对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "不过我也习以为常了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_34C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3519")

    ChrTalk(    #215
        0xFE,
        "唔～下一期的特辑做什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "对了，卢安的游戏吧\x01",
            "还没被拿来做过特辑呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_3519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_3541")

    ChrTalk(    #217
        0xFE,
        "今天要吃饱喝足睡大觉～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_3541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(    #218
        0xFE,
        "截稿终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "在咖啡馆或者酒馆打个牙祭\x01",
            "好好养精蓄锐一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_3596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3631")

    ChrTalk(    #220
        0xFE,
        (
            "因为我负责文化栏，\x01",
            "所以不用像前辈们那样\x01",
            "日程排得满满的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "但是也因为这点常被各处叫去\x01",
            "帮忙，我也不轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "或者说我反而比他们更忙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_368A")

    label("loc_3631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_368A")

    ChrTalk(    #223
        0xFE,
        (
            "结果还是不清楚亚尔摩\x01",
            "温泉沸腾的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "被总编批评成半吊子\x01",
            "新闻了，唔……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368A")

    TalkEnd(0xFE)
    Return()

    # Function_12_33CA end

    def Function_13_368E(): pass

    label("Function_13_368E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3855")
    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #225
        0xC,
        "#153F啊～是约修亚～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#1040F朵洛希小姐，好久不见。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #227
        0xC,
        (
            "#151F你真的回来了。\x01",
            "小艾，太好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#1008F是、是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xC,
        (
            "#151F来张纪念照……\x02\x03",

            "虽然心里这么想，\x01",
            "#156F不过照相机没法用啊～\x02\x03",

            "唉～\x01",
            "总觉得现在很不正常～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#1001F哈哈，对朵洛希来说\x01",
            "照相机果然是很重要的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xC,
        (
            "#150F那是自然！\x01",
            "我就这点特长呢。\x02\x03",

            "#151F真想马上去\x01",
            "给湖里冒出来的可爱贝壳\x01",
            "拍几张照片啊～㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x102,
        (
            "#1054F哈哈，怎么说才好……\x01",
            "你真是一点都没变啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20F2)
    Jump("loc_38B4")

    label("loc_3855")


    ChrTalk(    #233
        0xC,
        (
            "#150F今天的总编先生不知\x01",
            "为什么，看上去很帅～\x02\x03",

            "实在想象不出他平时\x01",
            "为什么会被大家叫作狸猫～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B4")

    TalkEnd(0xFE)
    Return()

    # Function_13_368E end

    def Function_14_38B8(): pass

    label("Function_14_38B8")

    Call(0, 15)
    Return()

    # Function_14_38B8 end

    def Function_15_38BD(): pass

    label("Function_15_38BD")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_391C")

    ChrTalk(    #234
        0xD,
        (
            "今天总编好像有话\x01",
            "和记者们说哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xD,
        (
            "现在正好在编辑部\x01",
            "开着少见的全体会议呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2E")

    label("loc_391C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_396D")

    ChrTalk(    #236
        0xD,
        "据说港口发生了大事件。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xD,
        (
            "记者们从昨晚开始\x01",
            "好像就在通宵奔波哦，\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2E")

    label("loc_396D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_39DD")

    ChrTalk(    #238
        0xD,
        (
            "朵洛希不知道有没有\x01",
            "在出差地好好工作呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xD,
        (
            "她虽然不是奈尔先生，\x01",
            "不过我总会不知不觉担心起来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2E")

    label("loc_39DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_END)), "loc_3A02")

    ChrTalk(    #240
        0xD,
        (
            "要回去了吗？\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2E")

    label("loc_3A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A8F")

    ChrTalk(    #241
        0xD,
        (
            "那么，时间也到了，\x01",
            "我也要下班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xD,
        (
            "记者们平时都要工作到\x01",
            "很晚，真不容易……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xD,
        (
            "每天我都会早下班，\x01",
            "感觉有点不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2E")

    label("loc_3A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3AE2")

    ChrTalk(    #244
        0xD,
        "欢迎来到利贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xD,
        (
            "如果找记者们有事的话\x01",
            "请上二楼的编辑部。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2E")

    label("loc_3AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3B2E")

    ChrTalk(    #246
        0xD,
        "欢迎来到利贝尔通讯社。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        (
            "这里的一楼是接待处，\x01",
            "二楼是编辑部。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2E")

    TalkEnd(0xD)
    Return()

    # Function_15_38BD end

    def Function_16_3B32(): pass

    label("Function_16_3B32")

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

    def lambda_3BE7():
        OP_6D(-57880, 0, 61180, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BE7)
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
            "#2P……导力停止以后，照明和暖气\x01",
            "自不必说，通讯也完全无法使用。\x02\x03",

            "可是，我不认为像你们\x01",
            "这样的记者会\x01",
            "被打垮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xA,
        (
            "#6P当然了，我们有\x01",
            "我们的任务！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x9,
        (
            "#2P对，市民们中有很多得\x01",
            "不到信息而在不安中\x01",
            "度日的人。\x02\x03",

            "正因为现状如此，\x01",
            "我们更应该传递正确的信息，\x01",
            "为社会做贡献。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        (
            "#140F#5P这还用说……\x02\x03",

            "这本就是我们记者的\x01",
            "存在意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xC,
        (
            "#156F#6P不过，奈尔前辈～\x02\x03",

            "导力照相机不能用的话\x01",
            "采访可不会顺利哦～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "#2P如朵洛希所述，\x01",
            "大半的器材都不能用。\x02\x03",

            "可是如果别人说我们以\x01",
            "此为理由而放弃媒体的使命\x01",
            "我可不甘心。\x02\x03",

            "各自发挥创意，\x01",
            "一定要想办法保持发行。\x02",
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

    # Function_16_3B32 end

    def Function_17_3E67(): pass

    label("Function_17_3E67")

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
            "#1011F#5P啊，找到了。\x02\x03",

            "#1001F喂～奈尔。\x01",
            "你好～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x8,
        "#142F#5P嗯……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #256
        0x8,
        (
            "#141F怎么了怎么了！\x01",
            "是你们啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x105,
        "#048F#5P你好，奈尔先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x104,
        "#031F#5P呵呵，我们要打扰你们一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x8,
        (
            "#143F啊～连公主殿下、演奏家\x01",
            "和『不动金』也在啊？\x02\x03",

            "相当热闹啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1016F#5P嘿嘿……\x01",
            "后来又发生了不少事。\x02\x03",

            "#1006F奈尔，你采访市长的事\x01",
            "还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x8,
        (
            "#141F呵呵，那还用问？\x02\x03",

            "那么你们今天有什么事？\x01",
            "有什么好的新闻线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1025F#5P不，确切地说是\x01",
            "我们要来问你。\x02\x03",

            "关于寄到这里的恐吓信\x01",
            "想要打听一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #263
        0x8,
        (
            "#143F怎么？你们也在\x01",
            "调查这事儿？\x02\x03",

            "我还以为王国军\x01",
            "在调查呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        (
            "#1006F#5P嗯，我们是接受军方的\x01",
            "委托在帮忙调查的……\x02\x03",

            "你有什么消息吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x8,
        (
            "#145F唔～我也是\x01",
            "刚回王都，\x01",
            "没得到什么重要消息。\x02\x03",

            "倒是还要问问\x01",
            "你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#1019F#5P你真是靠不住啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x104,
        (
            "#030F#5P你也算是媒体的人吧。\x02\x03",

            "对罪犯的身份\x01",
            "就没一点头绪？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x8,
        "#142F唔……你们真没礼貌。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x105,
        (
            "#045F#5P你们两个太没礼貌了。\x02\x03",

            "#043F那个，奈尔先生，\x01",
            "我知道这有点强人所难。\x02\x03",

            "你能不能告诉我们一点\x01",
            "哪怕是细小的线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x8,
        (
            "#143F等、等等，公主殿下！\x01",
            "请别对我这么客气！\x02\x03",

            "#145F真是的……拿你们没办法。\x02\x03",

            "#140F内部消息……\x01",
            "恐吓信好像不只是\x01",
            "寄到了这里。\x02\x03",

            "先是雷斯顿要塞……\x02\x03",

            "然后是大圣堂、飞船公社\x01",
            "和罗恩鲍姆酒店……\x02\x03",

            "接着是帝国和共和国的大使馆\x01",
            "以及格兰赛尔城堡、艾尔贝离宫……\x02\x03",

            "好像一共寄了９个地方。\x02",
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
        "#143F嗯，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_63(0x105)
    OP_63(0x104)
    OP_63(0x108)

    ChrTalk(    #272
        0x101,
        (
            "#1007F#5P那个奈尔……\x02\x03",

            "这情报军队早就\x01",
            "给过我们了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x8,
        (
            "#143F什么～！？\x02\x03",

            "#145F我、我这可是刚到手的\x01",
            "最新资料啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x108,
        "#073F#5P这听不听都一样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        (
            "#1007F#5P嗯，我们还是\x01",
            "去找别人吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "#144F你们给我等等～！\x02\x03",

            "竟被小看到这种程度，\x01",
            "利贝尔通讯头号实力派记者\x01",
            "奈尔·班兹的名声可要受损了。\x02\x03",

            "#141F好吧……\x01",
            "就把到目前为止我的\x01",
            "推理说给你们听听吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        "#1015F#5P哟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x104,
        "#035F#5P呵呵，那就请你长话短说吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x8,
        (
            "#142F唔……你们给我听好了。\x02\x03",

            "我认为这次的案件\x01",
            "是恶作剧型的犯罪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1025F#5P嗯～这我也不是\x01",
            "没假设过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x108,
        (
            "#070F#5P能不能说说你这么\x01",
            "确定这一点的理由？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x8,
        (
            "#140F以记者的经验来看……\x01",
            "那份恐吓信没有真实性。\x02\x03",

            "本来恐吓信也该包含有\x01",
            "具体且符合现实的要求，\x01",
            "这样才有意义。\x02\x03",

            "但是，那份恐吓信却并非如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x104,
        (
            "#030F#5P呼，确实有点道理。\x02\x03",

            "只是说『会发生灾难』的话\x01",
            "有关人士根本无法应对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x8,
        (
            "#141F就是这么回事。\x02\x03",

            "实在无法相信这信真的\x01",
            "想要妨碍条约。\x02\x03",

            "虽然不知道是谁，不过\x01",
            "那个人看来很高兴把时局搞乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#1004F#5P原、原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x105,
        (
            "#047F#5P有点道理。\x02\x03",

            "#542F只不过，恐吓信寄了９个地方\x01",
            "很令人在意……\x02\x03",

            "而且每一处都是与\x01",
            "条约是有关联的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x108,
        (
            "#074F#5P确实，如果只是恶作剧的话\x01",
            "又似乎太了解内情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#145F嗯～被你这么一说……\x02\x03",

            "#141F不过这些情况只要愿意，\x01",
            "调查一下就行。\x02\x03",

            "总之我现在在以恶作剧为前提\x01",
            "收集着信息。\x02\x03",

            "你们可以从别的\x01",
            "角度尝试调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#1006F#5P嗯，是啊。\x02\x03",

            "#1001F谢谢你，奈尔。\x01",
            "你的意见很重要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x8,
        (
            "#141F哼哼，不假吧？\x02\x03",

            "反正查到些什么\x01",
            "我们就彼此交换情报。\x02\x03",

            "我在互不侵犯条约缔结前\x01",
            "也准备留在王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1011F#5P哦，这样啊。\x02\x03",

            "#1004F对了，说起来的话……\x01",
            "朵洛希在干什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x8,
        (
            "#143F哦，那家伙在\x01",
            "柏斯地区出差。\x02\x03",

            "我想让她去\x01",
            "拍点照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        "#1015F#5P特辑？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#141F王国军相关的特辑。\x02\x03",

            "不是有座空贼使用过的\x01",
            "中世纪的城堡吗？\x02\x03",

            "现在那里成了王国军的\x01",
            "训练基地。\x02\x03",

            "好像在进行飞船的\x01",
            "操纵训练什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1006F#5P哦，是吗？\x02\x03",

            "那么她是去\x01",
            "那座基地采访了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x8,
        (
            "#145F算是吧。\x02\x03",

            "虽然目前交给她一个人\x01",
            "还有点令人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1016F#5P嗯……\x01",
            "确实无法否定啊。\x02\x03",

            "#1004F啊，对了。\x01",
            "还有一件事想\x01",
            "问问奈尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x8,
        "#143F嗯？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #299
        "\x07\x05向奈尔询问了关于玲双亲的情况。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #300
        0x8,
        (
            "#142F克洛斯贝尔的贸易商\x01",
            "哈罗德·海瓦斯……\x02\x03",

            "唔，没听说过。\x02\x03",

            "也不记得我们的杂志\x01",
            "有登他们的寻人启事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        "#1007F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x8,
        (
            "#141F算了，给你们免费服务一次。\x02\x03",

            "如果实在找不到的话\x01",
            "我也来帮忙吧。\x02\x03",

            "我可以帮你们刊登寻人启事，\x01",
            "或者去问问\x01",
            "我在克洛斯贝尔的熟人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x101,
        (
            "#1001F#5P谢谢你，奈尔。\x02\x03",

            "#1008F嘿嘿，感觉今天\x01",
            "你比平时来得可靠。\x02\x03",

            "我对你都有点刮目相看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x8,
        (
            "#147F是吧是吧？\x02\x03",

            "#144F等等，难道说我平时\x01",
            "就不可靠吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        (
            "#1016F#5P讨厌～\x01",
            "这是一种修辞啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EB6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第１章选了阿加特作为同伴】\x01",        # 0
            "【◇在第１章选了雪拉扎德作为同伴】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4EAA"),
        (1, "loc_4EB0"),
        (SWITCH_DEFAULT, "loc_4EB6"),
    )


    label("loc_4EAA")

    OP_A2(0x1201)
    Jump("loc_4EB6")

    label("loc_4EB0")

    OP_A3(0x1200)
    Jump("loc_4EB6")

    label("loc_4EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4F08")

    ChrTalk(    #306
        0x108,
        (
            "#070F#5P好，那么我们\x01",
            "回协会吧？\x02\x03",

            "阿加特那家伙也\x01",
            "应该已经回去了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F4C")

    label("loc_4F08")


    ChrTalk(    #307
        0x108,
        (
            "#070F#5P好，那么我们\x01",
            "回协会吧？\x02\x03",

            "雪拉扎德也\x01",
            "应该已经回去了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4C")


    ChrTalk(    #308
        0x104,
        "#031F#5P嗯，是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x105,
        (
            "#048F#5P奈尔先生。\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x8,
        (
            "#141F没什么的啦。\x01",
            "请再来哦。\x02",
        )
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

    # Function_17_3E67 end

    def Function_18_506E(): pass

    label("Function_18_506E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_508E")
    Call(0, 19)
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_508E")

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
        (
            "#1015F#6P我说老板啊，\x01",
            "这里的招牌菜是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xE,
        (
            "#5P那当然是\x01",
            "咖啡了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xE,
        (
            "#5P那可是混和了龙豆，用玻璃壶\x01",
            "沏的我们最为自豪的上品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xE,
        (
            "#5P还有大量使用了香料的\x01",
            "咖喱饭也相当受欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#1006F#6P辣咖喱、苦咖啡……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x107,
        "#061F这就是所谓的『又辣又苦又美味的店』啊⊙\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_526B")

    ChrTalk(    #317
        0x106,
        (
            "#051F请问，有没有一个穿\x01",
            "白色礼服的小姑娘来过？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529F")

    label("loc_526B")


    ChrTalk(    #318
        0x103,
        (
            "#020F请问，有没有一个穿\x01",
            "白色礼服的女孩子来过？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529F")


    ChrTalk(    #319
        0xE,
        "#5P嗯，刚才来过的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xE,
        (
            "#5P点了咖啡牛奶，\x01",
            "喝得津津有味的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xE,
        (
            "#5P对了，她还问了我\x01",
            "一个奇怪的问题……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5332")

    ChrTalk(    #322
        0x108,
        "#073F什么问题？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5349")

    label("loc_5332")


    ChrTalk(    #323
        0x105,
        "#044F是什么问题？\x02",
    )

    CloseMessageWindow()

    label("loc_5349")


    ChrTalk(    #324
        0xE,
        (
            "#5P『没人管就会消失的点心\x01",
            "在哪儿有卖？』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        (
            "#1006F#6P『没人管就会消失的点心』……\x02\x03",

            "……好，我记下了。\x02\x03",

            "唔～感觉快要\x01",
            "追上她了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1633)
    OP_28(0x8C, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_18_506E end

    def Function_19_53DD(): pass

    label("Function_19_53DD")

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
        (0, "loc_545A"),
        (1, "loc_5460"),
        (SWITCH_DEFAULT, "loc_5466"),
    )


    label("loc_545A")

    OP_A2(0x1200)
    Jump("loc_5466")

    label("loc_5460")

    OP_A2(0x1201)
    Jump("loc_5466")

    label("loc_5466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5474")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5478")

    label("loc_5474")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5478")

    Return()

    # Function_19_53DD end

    def Function_20_5479(): pass

    label("Function_20_5479")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_54B8")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_54D2")

    label("loc_54B8")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_54D2")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_5479 end

    def Function_21_54F2(): pass

    label("Function_21_54F2")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 60480, 0, 540, 0)
    SetChrPos(0x102, 61400, 0, 540, 0)
    SetChrPos(0xF8, 60480, 0, -800, 0)
    SetChrPos(0xF9, 61400, 0, -800, 0)
    OP_0D()

    ChrTalk(    #326
        0xE,
        "哟……这本书是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xE,
        (
            "应该是流行于街头巷尾的\x01",
            "传说中的《牌技师杰克》吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x101,
        "#1004F啊，你是说这本小说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xE,
        (
            "以共和国为舞台，\x01",
            "背负了不幸命运的\x01",
            "牌技师们的故事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xE,
        (
            "嗯嗯，真吸引人。\x01",
            "我很早就想读它了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        (
            "#1015F（唔～我也受了不少\x01",
            "　老板的关照……)\x02",
        )
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
            "【给店主小说】\x01",      # 0
            "【不给】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B2")
    Call(0, 23)
    Jump("loc_56CE")

    label("loc_56B2")


    ChrTalk(    #333
        0x101,
        "#1016F（还是算了吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_56CE")

    EventEnd(0x0)
    Return()

    # Function_21_54F2 end

    def Function_22_56D1(): pass

    label("Function_22_56D1")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 60480, 0, 540, 0)
    SetChrPos(0x102, 61400, 0, 540, 0)
    SetChrPos(0xF8, 60480, 0, -800, 0)
    SetChrPos(0xF9, 61400, 0, -800, 0)
    OP_0D()

    ChrTalk(    #334
        0xE,
        "咦，你这是？\x02",
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
            "【给店主小说】\x01",      # 0
            "【不给】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5791")
    Call(0, 23)
    Jump("loc_57AD")

    label("loc_5791")


    ChrTalk(    #335
        0x101,
        "#1016F（还是算了吧。）\x02",
    )

    CloseMessageWindow()

    label("loc_57AD")

    EventEnd(0x0)
    Return()

    # Function_22_56D1 end

    def Function_23_57B0(): pass

    label("Function_23_57B0")


    ChrTalk(    #336
        0x101,
        (
            "#1001F喏，给你。\x01",
            "就送给老板吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xE,
        (
            "啊，我不是为了要书\x01",
            "才跟你们说这些的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1000F请别介意。\x02\x03",

            "这就当\x01",
            "美味咖喱和咖啡的回礼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xE,
        (
            "你能这么说\x01",
            "我真高兴…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xE,
        (
            "这样的话\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #341
        "\x07\x02牌技师杰克\x07\x00交给了店主。\x02",
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
            "谢谢，我会每晚\x01",
            "一点点地读的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xE,
        (
            "对了……\x01",
            "这点不成敬意的东西\x01",
            "请收下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #344
        "\x1F\x17\x04\x07\x00收下了。\x02",
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
        "#1044F这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xE,
        (
            "这是我还在当外交官的时候，\x01",
            "在亚尔特利亚得到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1015F亚尔特利亚应该是\x01",
            "七耀教会的总部吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xE,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xE,
        (
            "这好像是用很久以前的塞姆里亚时代\x01",
            "出产的金属制成的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x102,
        (
            "#1044F塞姆里亚时代的？\x01",
            "确实从没见过这样的金属……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xE,
        (
            "哈哈，我也不知道\x01",
            "是真是假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xE,
        (
            "顺带一提，加工此物的技术\x01",
            "据说已经完全失传了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1018F哟，这么看来，\x01",
            "还挺有传奇色彩的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 7)), scpexpr(EXPR_END)), "loc_5BBF")

    ChrTalk(    #354
        0x102,
        (
            "#1040F记得以前老板也拿武器\x01",
            "来跟我换过书吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xE,
        "哈哈，我还记得。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xE,
        (
            "不过这次不是什么了不起的东西，\x01",
            "不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x101,
        "#1001F不不，我会好好珍惜它的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C10")

    label("loc_5BBF")


    ChrTalk(    #358
        0xE,
        (
            "哈哈，这也不算什么，\x01",
            "你就当作是护身符吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1001F嗯，我会好好珍惜它的。\x02",
    )

    CloseMessageWindow()

    label("loc_5C10")

    OP_A2(0x10C4)
    Return()

    # Function_23_57B0 end

    def Function_24_5C14(): pass

    label("Function_24_5C14")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #360
        (
            "\x07\x05巴拉尔咖啡厅的名菜！\x01",
            "『完熟咖喱饭』 ９００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #361
        (
            "\x07\x05请一定要品尝用秘传香料\x01",
            "特制的辛辣咖喱。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_5C14 end

    def Function_25_5CA2(): pass

    label("Function_25_5CA2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #362
        (
            "\x07\x05～　目录　～\x01",
            "仿手工制派　４００米拉\x01",
            "苦西红柿三明治　１４００米拉\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #363
        (
            "\x07\x05～ 本店招牌菜　～\x01",
            "热海汁　１２００米拉\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_5CA2 end

    SaveToFile()

Try(main)
