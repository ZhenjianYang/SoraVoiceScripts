from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0100.x',
        MapIndex            = 14,
        MapDefaultBGM       = "ed60030",
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
        'Miner Miles',                          # 9
        'Miner Landan',                         # 10
        'Miner-in-Training',                    # 11
        'Miner Bones',                          # 12
        'Miner Trent',                          # 13
        'Miner Pierre',                         # 14
        'Miner Heinrich',                       # 15
        'Mine Chief Gaton',                     # 16
        'Fiend',                                # 17
        'Fiend',                                # 18
        'Fiend',                                # 19
        'Fiend',                                # 20
        'Fiend',                                # 21
        'Fiend',                                # 22
        'Target Camera',                        # 23
        'カニキャンサー',                       # 24
        'カニキャンサー',                       # 25
        'カニキャンサー',                       # 26
        'カニキャンサー',                       # 27
    )

    DeclEntryPoint(
        Unknown_00              = 25000,
        Unknown_04              = 0,
        Unknown_08              = 9000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 14,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 25000,
        Unknown_04              = 0,
        Unknown_08              = 9000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 14,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10000 ._CH',             # 00
        'ED6_DT09/CH10001 ._CH',             # 01
        'ED6_DT09/CH10050 ._CH',             # 02
        'ED6_DT09/CH10051 ._CH',             # 03
        'ED6_DT07/CH01500 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
        'ED6_DT07/CH00100 ._CH',             # 06
        'ED6_DT07/CH00110 ._CH',             # 07
        'ED6_DT06/CH20034 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT09/CH10000P._CP',             # 00
        'ED6_DT09/CH10001P._CP',             # 01
        'ED6_DT09/CH10050P._CP',             # 02
        'ED6_DT09/CH10051P._CP',             # 03
        'ED6_DT07/CH01500P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
        'ED6_DT07/CH00100P._CP',             # 06
        'ED6_DT07/CH00110P._CP',             # 07
        'ED6_DT06/CH20034P._CP',             # 08
    )

    DeclNpc(
        X                   = 22500,
        Z                   = 1000,
        Y                   = 65840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 96890,
        Z                   = 1000,
        Y                   = 91220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 130850,
        Z                   = 1000,
        Y                   = 13900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 126070,
        Z                   = 500,
        Y                   = 13270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 83580,
        Z                   = 1000,
        Y                   = 33130,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 83760,
        Z                   = 1000,
        Y                   = 31300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 84600,
        Z                   = 0,
        Y                   = 14100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 114000,
        Z                   = -500,
        Y                   = 80000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 108000,
        Z                   = 0,
        Y                   = 54000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x58,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 109000,
        Z                   = 0,
        Y                   = 35000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105000,
        Z                   = 0,
        Y                   = 16000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 129,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x57,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 104400,
        Y                   = -1000,
        Z                   = 68900,
        Range               = 109400,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFF14,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = 92200,
        Y                   = -1000,
        Z                   = 63230,
        Range               = 4000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 90100,
        Y                   = -1000,
        Z                   = 72400,
        Range               = 97800,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x10F4A,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 123500,
        Y                   = -1000,
        Z                   = 27100,
        Range               = 132000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x7E2B,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 126240,
        Y                   = -1000,
        Z                   = 15000,
        Range               = 131400,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2A94,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 92900,
        Y                   = -1000,
        Z                   = 33340,
        Range               = 97970,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5762,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 84730,
        Y                   = 1000,
        Z                   = 31370,
        Range               = 88770,
        Unknown_10          = 0xFFFFFF9C,
        Unknown_14          = 0x8444,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )


    DeclActor(
        TriggerX            = 14000,
        TriggerZ            = 1000,
        TriggerY            = 31800,
        TriggerRange        = 1000,
        ActorX              = 14000,
        ActorZ              = 1000,
        ActorY              = 31800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16000,
        TriggerZ            = 1000,
        TriggerY            = 32000,
        TriggerRange        = 1500,
        ActorX              = 16000,
        ActorZ              = 1000,
        ActorY              = 32000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35000,
        TriggerZ            = 1000,
        TriggerY            = 59500,
        TriggerRange        = 1500,
        ActorX              = 35000,
        ActorZ              = 1000,
        ActorY              = 59500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50500,
        TriggerZ            = 1000,
        TriggerY            = 50000,
        TriggerRange        = 1500,
        ActorX              = 50500,
        ActorZ              = 1000,
        ActorY              = 50000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54000,
        TriggerZ            = 500,
        TriggerY            = 58200,
        TriggerRange        = 600,
        ActorX              = 54000,
        ActorZ              = 500,
        ActorY              = 58200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 129000,
        TriggerZ            = 500,
        TriggerY            = 78200,
        TriggerRange        = 600,
        ActorX              = 129000,
        ActorZ              = 500,
        ActorY              = 78200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 104800,
        TriggerZ            = 0,
        TriggerY            = 39740,
        TriggerRange        = 1000,
        ActorX              = 104800,
        ActorZ              = 1000,
        ActorY              = 39740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_562",          # 00, 0
        "Function_1_629",          # 01, 1
        "Function_2_710",          # 02, 2
        "Function_3_88D",          # 03, 3
        "Function_4_88E",          # 04, 4
        "Function_5_99C",          # 05, 5
        "Function_6_C8F",          # 06, 6
        "Function_7_E8F",          # 07, 7
        "Function_8_11AC",         # 08, 8
        "Function_9_145A",         # 09, 9
        "Function_10_2AC3",        # 0A, 10
        "Function_11_2B46",        # 0B, 11
        "Function_12_2B58",        # 0C, 12
        "Function_13_2B62",        # 0D, 13
        "Function_14_2F7A",        # 0E, 14
        "Function_15_3ADF",        # 0F, 15
        "Function_16_4114",        # 10, 16
        "Function_17_429D",        # 11, 17
        "Function_18_47DE",        # 12, 18
        "Function_19_47F0",        # 13, 19
        "Function_20_49ED",        # 14, 20
        "Function_21_4A10",        # 15, 21
        "Function_22_4B81",        # 16, 22
        "Function_23_4E80",        # 17, 23
        "Function_24_4EBD",        # 18, 24
        "Function_25_4FF6",        # 19, 25
        "Function_26_53F5",        # 1A, 26
        "Function_27_541E",        # 1B, 27
        "Function_28_5C6A",        # 1C, 28
        "Function_29_5C80",        # 1D, 29
        "Function_30_6593",        # 1E, 30
        "Function_31_6847",        # 1F, 31
        "Function_32_69B1",        # 20, 32
        "Function_33_6B14",        # 21, 33
        "Function_34_6B5F",        # 22, 34
    )


    def Function_0_562(): pass

    label("Function_0_562")

    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_594"),
        (100, "loc_59B"),
        (101, "loc_59E"),
        (SWITCH_DEFAULT, "loc_5A1"),
    )


    label("loc_594")

    Event(0, 15)
    Jump("loc_5A1")

    label("loc_59B")

    Jump("loc_5A1")

    label("loc_59E")

    Jump("loc_5A1")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_5FD")
    SetChrPos(0xF, 14160, 0, 12750, 225)
    SetChrPos(0xB, 39350, 0, 26280, 0)
    SetChrPos(0xC, 24110, -40, 15950, 0)
    SetChrPos(0xD, 10800, 0, 29530, 0)
    SetChrPos(0xE, 54240, 0, 53990, 0)

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_61F")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)

    label("loc_61F")

    OP_A2(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    Return()

    # Function_0_562 end

    def Function_1_629(): pass

    label("Function_1_629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_63A")
    OP_6F(0x0, 0)
    Jump("loc_659")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_64B")
    OP_6F(0x0, 330)
    Jump("loc_659")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_659")
    OP_6F(0x0, 900)

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_66A")
    OP_6F(0x3, 25)
    Jump("loc_671")

    label("loc_66A")

    OP_6F(0x3, 0)

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C6")
    LoadEffect(0x0, "map\\\\mp002_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 1000)

    label("loc_6C6")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_629 end

    def Function_2_710(): pass

    label("Function_2_710")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_877")

    label("loc_735")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_877")

    label("loc_74E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_767")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_877")

    label("loc_767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_877")

    label("loc_780")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_877")

    label("loc_799")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_877")

    label("loc_7B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CB")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_877")

    label("loc_7CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E4")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_877")

    label("loc_7E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FD")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_877")

    label("loc_7FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_816")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_877")

    label("loc_816")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_877")

    label("loc_82F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_848")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_877")

    label("loc_848")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_877")

    label("loc_861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_877")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_877")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_877")

    label("loc_88C")

    Return()

    # Function_2_710 end

    def Function_3_88D(): pass

    label("Function_3_88D")

    Return()

    # Function_3_88D end

    def Function_4_88E(): pass

    label("Function_4_88E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933")
    OP_A2(0x5)

    ChrTalk(    #0
        0xA,
        (
            "Eeek! Y-You scared me there\x01",
            "for a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "So, you're looking for the mine\x01",
            "chief, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "I'm sure he's somewhere across\x01",
            "the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_998")

    label("loc_933")


    ChrTalk(    #3
        0xA,
        (
            "So, you're looking for the mine\x01",
            "chief, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "I'm sure he's somewhere across\x01",
            "the bridge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_998")

    TalkEnd(0xA)
    Return()

    # Function_4_88E end

    def Function_5_99C(): pass

    label("Function_5_99C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A24")

    ChrTalk(    #5
        0xB,
        (
            "We sealed off the hole to the\x01",
            "monster's nest with a load of\x01",
            "explosives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "Now I just hope we can get back\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A9B")

    ChrTalk(    #7
        0xB,
        "I can't find Trent anywhere...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xB,
        (
            "I bet he's skipped out on work again\x01",
            "to grab a bite back in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(    #9
        0xB,
        (
            "The mine chief hasn't been home\x01",
            "in like, forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "No doubt his family's been anxiously waiting for\x01",
            "him to step through the front door. I wonder if\x01",
            "it's okay for him to stay here so long like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_BF5")

    ChrTalk(    #11
        0xB,
        (
            "Since we won't be able to mine anything\x01",
            "below for a while, it looks like we're\x01",
            "stuck digging up what we can here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_BF5")


    ChrTalk(    #12
        0xB,
        (
            "It looks like Trent was cutting\x01",
            "work again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "I can't believe he's still pulling the\x01",
            "same stunts after that last earful\x01",
            "he got from the boss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8B")

    TalkEnd(0xB)
    Return()

    # Function_5_99C end

    def Function_6_C8F(): pass

    label("Function_6_C8F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_CC4")

    ChrTalk(    #14
        0xC,
        "Think like I'm eating in Rolent...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_CF6")

    ChrTalk(    #15
        0xC,
        "Think like I'm eating in Rolent...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_D7D")

    ChrTalk(    #16
        0xC,
        (
            "I can't go on any longer with this\x01",
            "empty stomach... I'll die...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "As soon as I'm done here, I'm\x01",
            "sneaking off to eat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_E0A")

    ChrTalk(    #18
        0xC,
        (
            "All those monsters...\x01",
            "What a horrible experience that was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        (
            "And when it was all over...my\x01",
            "stomach started growling again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8B")

    label("loc_E0A")


    ChrTalk(    #20
        0xC,
        (
            "Oh, man... I ate a ton of food,\x01",
            "but now I'm hungry again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        (
            "Maybe I ought to try sneaking off\x01",
            "to town for lunch again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8B")

    TalkEnd(0xC)
    Return()

    # Function_6_C8F end

    def Function_7_E8F(): pass

    label("Function_7_E8F")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_F52")

    ChrTalk(    #22
        0xD,
        (
            "Whew, with this job now out of\x01",
            "the way, I think I'd better take\x01",
            "some time to visit the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        (
            "I haven't been there to pray in a\x01",
            "while because I've been so busy\x01",
            "with work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_FBF")

    ChrTalk(    #24
        0xD,
        (
            "It looks like the mine chief intends\x01",
            "to seal up the monsters' nest hole\x01",
            "with some explosives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_107D")

    ChrTalk(    #25
        0xD,
        (
            "Before the cave-in, we struck several\x01",
            "new veins, so there IS something left\x01",
            "to be mined...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xD,
        (
            "But if we can't get into the lower\x01",
            "stratum soon, we'll be out of stuff\x01",
            "to dig.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_111B")

    ChrTalk(    #27
        0xD,
        (
            "Whew, for a minute there,\x01",
            "I thought I was a goner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        (
            "Once I get back to town, I'd better\x01",
            "head to the chapel and give thanks\x01",
            "to the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_111B")


    ChrTalk(    #29
        0xD,
        (
            "The reason why we've been able to\x01",
            "work like we have is due to the grace\x01",
            "of the Goddess herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        "We'd best remember to give thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_11A8")

    TalkEnd(0xD)
    Return()

    # Function_7_E8F end

    def Function_8_11AC(): pass

    label("Function_8_11AC")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_123A")

    ChrTalk(    #31
        0xE,
        "You still can't use the elevator.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "The monster scare has settled\x01",
            "down, but I've decided to watch\x01",
            "and wait just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_123A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_12EC")

    ChrTalk(    #33
        0xE,
        (
            "Sealing up the nest hole is good\x01",
            "and all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xE,
        (
            "Somebody still has to go down\x01",
            "there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "Somebody is going to be stuck\x01",
            "with task of doing it, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_1387")

    ChrTalk(    #36
        0xE,
        (
            "There are still monsters crawling\x01",
            "around down below.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "I'd sure like to see them exterminated\x01",
            "or sealed back in wherever they came\x01",
            "from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_140B")

    ChrTalk(    #38
        0xE,
        (
            "The lower stratum will be sealed\x01",
            "off for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        (
            "There are monsters everywhere,\x01",
            "and it's incredibly dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1456")

    label("loc_140B")


    ChrTalk(    #40
        0xE,
        (
            "You said you're looking for the mine\x01",
            "chief? He was here a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1456")

    TalkEnd(0xE)
    Return()

    # Function_8_11AC end

    def Function_9_145A(): pass

    label("Function_9_145A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_148E")

    ChrTalk(    #41
        0xF,
        "They should be at home in Rolent.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_148E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(    #42
        0xF,
        (
            "It looks like our only option is to seal\x01",
            "up the monsters' den.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "There are enough of them down there,\x01",
            "it'd be a tough job even for bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_15BC")

    ChrTalk(    #44
        0xF,
        (
            "The new guy that took off back during\x01",
            "the cave-in still hasn't returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xF,
        (
            "It's not surprising after an experience\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_1652")

    ChrTalk(    #46
        0xF,
        (
            "I sincerely apologize for getting you\x01",
            "all wrapped up in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xF,
        (
            "But it's strange. The bedrock shouldn't\x01",
            "have been weak like that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABF")

    label("loc_1652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABF")
    OP_A2(0x242)
    OP_28(0x3, 0x1, 0x40)
    OP_28(0x3, 0x1, 0x80)
    ClearMapFlags(0x1)
    Fade(1000)
    EventBegin(0x0)
    AddParty(0x32, 0xFF)
    SetChrFlags(0x133, 0x80)
    SetChrPos(0x102, 85400, 0, 12650, 0)
    SetChrPos(0x101, 84250, 0, 12500, 0)
    OP_6C(315000, 0)
    TurnDirection(0xF, 0x101, 0)
    SetChrSubChip(0xF, 0)
    OP_6D(84460, 0, 13210, 1000)
    OP_0D()

    ChrTalk(    #48
        0xF,
        (
            "#2PHeaven and earth!\x01",
            "What are two kids like you\x01",
            "doing down here in the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#000FYou're the mine chief, right?\x01",
            "Boy, am I glad to see you. We've been\x01",
            "searching all over this dank place for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#010FWe're with the Bracer Guild,\x01",
            "and we've come today on behalf\x01",
            "of Mayor Klaus.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #51
        "\x07\x00Handed over the \x07\x02Mayor's Referral\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x321, 1)

    ChrTalk(    #52
        0xF,
        (
            "#2PHmmm, I see...\x01",
            "So you kids are bracers, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        (
            "#2PThat's quite a feat for being\x01",
            "so young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#506FTee hee. It's not that big of\x01",
            "a deal.\x02\x03",

            "#006FBy the way...you're supposed to\x01",
            "have some sort of crystal for us,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        "#2POh right, give me a second.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xF,
        (
            "#2PThis little baby is something\x01",
            "you don't see every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        (
            "#2PWhich is why I've been keeping it\x01",
            "as close to myself as possible.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        "\x07\x05The mine chief pulls a large-grain crystal from his breast-pocket.\x07\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x80, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0xF, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CloseMessageWindow()
    Sleep(1500)

    ChrTalk(    #59
        0x101,
        "#004FWow...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x101,
        (
            "#001FI've never seen a crystal THIS\x01",
            "big before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#014FThat is impressive...\x01",
            "There seems to be light swirling\x01",
            "around inside, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xF,
        (
            "#2PIt's one of several types of septium.\x01",
            "Specifically, it's an esmelas crystal\x01",
            "which is endowed with the power of wind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xF,
        (
            "#2PFor a gem of this size, you're\x01",
            "looking at a hefty price tag. I'm\x01",
            "talking about a small fortune here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xF,
        (
            "#2PMake ABSOLUTELY sure that this\x01",
            "gets to the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#002FR-Roger that...\x02",
    )

    CloseMessageWindow()
    OP_92(0xF, 0x101, 0x3E8, 0x3E8, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrChipByIndex(0x101, 8)
    OP_82(0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #66
        "\x07\x00Received \x07\x02Septium Crystal\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x323, 1)
    OP_8F(0xF, 0x14A78, 0x0, 0x3714, 0x3E8, 0x0)
    OP_6D(84250, -500, 12500, 1000)

    ChrTalk(    #67
        0x101,
        (
            "#008FIt's soooo...beautiful...\x02\x03",

            "It feels like I'm carrying a little\x01",
            "fairy in my hand...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_69(0x101, 0x3E8)
    OP_6A(0x101)
    SetMapFlags(0x1)
    OP_97(0x101, 0x1491A, 0x29FE, 0xFFFF15A0, 0x7D0, 0x1)

    def lambda_1DF7():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DF7)
    OP_97(0x101, 0x1491A, 0x29FE, 0xFFFF8AD0, 0xBB8, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFA81C0, 0xFA0, 0x1)
    OP_A2(0x2)
    OP_43(0x101, 0x1, 0x0, 0xA)

    ChrTalk(    #68
        0x101,
        (
            "#001FThis is super fun!\x02\x03",

            "#001FCheck this out, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    OP_6D(84000, 0, 13440, 2000)

    ChrTalk(    #69
        0x102,
        (
            "#015F#2PThat's nice and all, but...\x02\x03",

            "#010FHow about you stop horsing around?\x01",
            "If you drop it we could be in some\x01",
            "real trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    OP_A6(0x1)

    ChrTalk(    #70
        0x101,
        "#007FFine, you big killjoy.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x1491A, 0x0, 0x30D4, 0x5DC, 0x0)
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x102, 0x101, 0)
    Sleep(1000)
    OP_82(0x0, 0x2)
    SetChrChipByIndex(0x101, 65535)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #71
        "\x07\x05Estelle put the crystal away in her pocket.\x07\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)

    ChrTalk(    #72
        0x101,
        "#006FWell, I guess that's that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(    #73
        0x101,
        (
            "#006FWe'll get out of your hair now,\x01",
            "Mr. Gaton, but don't worry, we'll\x01",
            "make sure this gets to the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xF,
        "#2PI'm counting on you kids.\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1100)
    OP_8C(0xF, 135, 400)

    ChrTalk(    #75
        0xF,
        "#2PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#000FWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xF,
        "#2PThat's odd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xF,
        (
            "#2PThe airflow down here suddenly\x01",
            "shifted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#004FThe airflow...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#012F#2P(This scent. It's...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_43(0x101, 0x1, 0x0, 0xD)
    OP_22(0x85, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0xF,
        "#2PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#504FAhhhhh?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 180, 400)
    OP_8C(0x101, 315, 400)
    OP_8C(0x101, 45, 400)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #83
        0x102,
        "#012F#2P...\x02",
    )

    CloseMessageWindow()
    OP_A3(0x3)
    OP_24(0x85, 0x5A)
    Sleep(200)
    OP_24(0x85, 0x50)
    Sleep(200)
    OP_24(0x85, 0x46)
    Sleep(200)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    Sleep(200)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #84
        0x101,
        (
            "#007FIs... Is it over?\x02\x03",

            "#002FWas that an earthquake just now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #85
        0xF,
        (
            "#2PNo...it seems that there's been a\x01",
            "cave-in somewhere within the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xF,
        (
            "#2PI wonder if one of the miners hit a\x01",
            "patch of loose ground. I'd better\x01",
            "check on the extent of the damage...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, 92200, 0, 10100, 0)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x102, 7)
    OP_8C(0x102, 135, 800)

    ChrTalk(    #87
        0x102,
        "#016FLook out, Estelle!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 800)

    ChrTalk(    #88
        0x101,
        "#004FWha...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 6)

    def lambda_23FF():
        OP_6D(91250, 0, 7500, 2600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23FF)

    def lambda_2417():
        OP_6B(2000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2417)
    OP_8E(0x10, 0x158EC, 0x0, 0x2904, 0x1B58, 0x0)
    OP_92(0x10, 0x101, 0x7D0, 0x2710, 0x0)
    OP_44(0x101, 0xFF)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2460"),
        (SWITCH_DEFAULT, "loc_2465"),
    )


    label("loc_2460")

    OP_B4(0x0)
    Jump("loc_2465")

    label("loc_2465")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    SetChrFlags(0x10, 0x80)
    OP_6B(2800, 0)
    OP_6D(84460, 0, 13210, 0)
    SetChrPos(0x101, 85400, 0, 12650, 0)
    SetChrPos(0x102, 86100, -500, 13380, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0xF, 0x101, 0)
    TurnDirection(0x101, 0xF, 0)
    TurnDirection(0x102, 0xF, 0)
    OP_0D()

    ChrTalk(    #89
        0x101,
        (
            "#580FWh-Why are there...\x02\x03",

            "Do you usually have problems\x01",
            "with monsters like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        (
            "#1PNo, this is the first time we've\x01",
            "ever had anything like this\x01",
            "happen down here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xF,
        (
            "#1PMonsters have a predisposition\x01",
            "which attracts them to the glow\x01",
            "of septium...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xF,
        (
            "#1P...so we've had a lot of them wander\x01",
            "into the mine in the past, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#012FJudging from the situation...\x02\x03",

            "It may be that the recent cave-in\x01",
            "opened up a hole connected to a\x01",
            "den of monsters.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #94
        0x101,
        "#005FD-Did you say a den of monsters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xF,
        "#1PIt's not inconceivable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xF,
        (
            "#1PBut, this is no time to be standing\x01",
            "around thinking about it. I've got to\x01",
            "get the other workers out of here!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(    #97
        0x101,
        (
            "#002FIf that's the case, then how about\x01",
            "letting us help you out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xF,
        "#1PYou're kidding, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#006FMonster extermination is right\x01",
            "up our alley and besides,\x01",
            "every minute counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        (
            "#1PYou're right...some extra help\x01",
            "would be much appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#012FSo how many miners are we\x01",
            "looking at in all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        (
            "#1PThere should only be four others\x01",
            "working here in the lower tunnels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#005FGot it! Now let's go find them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xF,
        (
            "#1PSorry about all this...\x01",
            "Oh right, take these and\x01",
            "use them if you need to.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #105
        "\x07\x00Received \x07\x02Tear Balm\x07\x00 x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x1F5, 2)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    LoadEffect(0x0, "map\\\\mp002_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x11, 85530, 1000, 32350, 270)
    SetChrPos(0x12, 128360, 1000, 12900, 180)
    SetChrPos(0x13, 92200, 0, 63230, 225)
    SetChrPos(0x14, 92600, 0, 62100, 270)
    SetChrPos(0x15, 90800, 0, 63630, 180)
    OP_8C(0xA, 225, 0)
    OP_8C(0xB, 225, 0)
    OP_8C(0xD, 225, 0)
    OP_8C(0xD, 90, 0)
    OP_8C(0xE, 90, 0)
    SetChrFlags(0xF, 0x40)

    def lambda_2A9F():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2A9F)
    EventEnd(0x0)
    ClearChrFlags(0x133, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)

    label("loc_2ABF")

    TalkEnd(0xF)
    Return()

    # Function_9_145A end

    def Function_10_2AC3(): pass

    label("Function_10_2AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2AE2")
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEA070, 0xFA0, 0x1)
    Jump("Function_10_2AC3")

    label("loc_2AE2")

    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEA070, 0xFA0, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEC780, 0xBB8, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFEEE90, 0x7D0, 0x1)
    OP_97(0x101, 0x1462C, 0x29FE, 0xFFFF8AD0, 0x3E8, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)
    OP_A2(0x1)
    Return()

    # Function_10_2AC3 end

    def Function_11_2B46(): pass

    label("Function_11_2B46")

    OP_6D(91250, 0, 7500, 2600)
    Return()

    # Function_11_2B46 end

    def Function_12_2B58(): pass

    label("Function_12_2B58")

    OP_6B(200, 1500)
    Return()

    # Function_12_2B58 end

    def Function_13_2B62(): pass

    label("Function_13_2B62")

    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)

    label("loc_2C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C5A")
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 400, 13440, 20)
    Jump("loc_2C2E")

    label("loc_2C5A")

    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 300, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 200, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    OP_6D(84000, 100, 13440, 20)
    OP_6D(84000, 0, 13440, 20)
    Return()

    # Function_13_2B62 end

    def Function_14_2F7A(): pass

    label("Function_14_2F7A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_308A")

    ChrTalk(    #106
        0x8,
        (
            "The mine chief went to the lower\x01",
            "tunnels and sealed up that monster\x01",
            "hole with explosives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "We'd probably just have gotten in\x01",
            "his way if we had gone along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "That's just like Mine Chief Gaton.\x01",
            "There's not another miner alive\x01",
            "who's as manly as him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3118")

    ChrTalk(    #109
        0x8,
        (
            "Whew, we've mined just about everything\x01",
            "we can out of this place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "I sure want to get back to work\x01",
            "in the lower stratum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_31D9")

    ChrTalk(    #111
        0x8,
        (
            "It's unbelievable to think that the new\x01",
            "lodes we just found would be followed\x01",
            "by a cave-in. Such terrible luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "I hope we can get back down to\x01",
            "the lower levels before long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_31D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_3261")

    ChrTalk(    #113
        0x8,
        (
            "I was so surprised when I felt\x01",
            "that rumble from below.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "I'm just glad that the mine chief\x01",
            "and everyone else is safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377A")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0x23E)

    ChrTalk(    #115
        0x8,
        (
            "Great Aidios! What are you kids\x01",
            "doing down here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "Are you friends with someone who\x01",
            "works here in the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#000FNot exactly. We've come to see\x01",
            "the mine chief at the request of\x01",
            "the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "Oh, so you're here about the crystal,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "Well, if you're looking for the boss,\x01",
            "he should be in the tunnels below.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "If you use the elevator at the end of\x01",
            "the tracks on the opposite side of\x01",
            "the mine, you can get down there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A7")

    ChrTalk(    #121
        0x101,
        (
            "#004FThe end of the tracks on the opposite\x01",
            "side of the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "When you were riding in the mine cart,\x01",
            "you noticed a place along the way where\x01",
            "the track diverges, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "If you follow that other line,\x01",
            "you'll reach the elevator. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "In order to get there, you'll have to go\x01",
            "back to where you came from and flip\x01",
            "the lever to activate the track switch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3775")

    label("loc_35A7")

    OP_A2(0x23F)
    OP_28(0x3, 0x1, 0x20)

    ChrTalk(    #125
        0x101,
        (
            "#002FWe found the elevator, but we didn't\x01",
            "know how to make it run.\x02\x03",

            "#002FDo you know how to operate it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "Well, that's an easy problem to fix.\x01",
            "All you need is a key to activate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "But...since you don't have one of\x01",
            "your own, I'll help you out by\x01",
            "lending you mine.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #128
        "\x07\x00Borrowed \x07\x02Elevator Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x322, 1)

    ChrTalk(    #129
        0x101,
        (
            "#001FMuch appreciated. Once our business\x01",
            "here is finished we'll make sure to\x01",
            "return it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3775")

    EventEnd(0x1)
    Jump("loc_3ADB")

    label("loc_377A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3921")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0x23F)
    OP_28(0x3, 0x1, 0x20)

    ChrTalk(    #130
        0x8,
        (
            "What's that, you say?\x01",
            "The elevator wouldn't work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "Ah, I see what the problem is.\x01",
            "You need the key to activate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        (
            "But...since you don't have one of\x01",
            "your own, I'll help you out by\x01",
            "lending you mine.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #133
        "\x07\x00Borrowed \x07\x02Elevator Key\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x322, 1)

    ChrTalk(    #134
        0x101,
        (
            "#001FMuch appreciated. Once our business\x01",
            "here is finished we'll make sure to\x01",
            "return it.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_3ADB")

    label("loc_3921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_END)), "loc_39B1")

    ChrTalk(    #135
        0x8,
        (
            "If you insert that key, you should\x01",
            "be able to use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "You can return it when you're done\x01",
            "with your business here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_39B1")


    ChrTalk(    #137
        0x8,
        (
            "When you were riding in the mine cart,\x01",
            "you noticed a place along the way where\x01",
            "the track diverges, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "If you follow that other line,\x01",
            "you'll reach the elevator. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "In order to get there, you'll have to go\x01",
            "back to where you came from and flip\x01",
            "the lever to activate the track switch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADB")

    TalkEnd(0x8)
    Return()

    # Function_14_2F7A end

    def Function_15_3ADF(): pass

    label("Function_15_3ADF")

    EventBegin(0x0)
    SetChrPos(0xF, 27100, -500, 13125, 180)
    SetChrPos(0x101, 26230, 0, 10530, 0)
    SetChrPos(0x102, 27600, 0, 10640, 0)
    SetChrPos(0xB, 39350, 0, 26280, 0)
    SetChrPos(0xC, 24110, -40, 15950, 0)
    SetChrPos(0xD, 10800, 0, 29530, 0)
    SetChrPos(0xE, 54240, 0, 53990, 0)
    OP_3F(0x322, 1)
    OP_4A(0xF, 0)
    ClearMapFlags(0x1)
    OP_69(0x101, 0x0)

    ChrTalk(    #140
        0xF,
        (
            "I apologize for getting you involved\x01",
            "in more than your fair share of work\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xF,
        (
            "I'll get in touch with the guild a\x01",
            "little later on and make sure you\x01",
            "two are compensated fairly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#000FDon't sweat it. We just did what\x01",
            "anyone would have done in our\x01",
            "position.\x02\x03",

            "#000FAnd besides, it's all a part of our\x01",
            "training to become full-fledged\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        (
            "#010F#5PBy the way, what do you intend\x01",
            "to do about the lower tunnels?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xF,
        (
            "I don't know, but we'll figure out\x01",
            "some way to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xF,
        (
            "There's always the option of sealing off\x01",
            "the monster den with some explosives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xF,
        (
            "As a heads up, I may ask the guild for help\x01",
            "if we run into any other serious trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#006FSure, you can count on us.\x02\x03",

            "#006FAnd we'll make sure this crystal\x01",
            "gets to the mayor as intended.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #148
        0x102,
        (
            "#010FYou did make sure that you didn't\x01",
            "drop it...right, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #149
        0x101,
        (
            "#007FHow rude. I'm not that careless.\x02\x03",

            "#007FLook, it's right...\x02\x03",

            "#007F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #150
        0x102,
        "#018FY-You didn't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xF,
        "Y-You lost it?!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_22(0x80, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x101, 8)
    OP_8C(0x101, 180, 500)
    OP_8C(0x101, 270, 500)
    OP_8C(0x101, 0, 500)
    OP_8C(0x101, 90, 500)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #152
        0x101,
        (
            "#001FPsych! I've got it right here!\x02\x03",

            "#001FLet's go make that delivery,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    OP_82(0x0, 0x2)
    OP_84(0x0)
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #153
        0x102,
        "#017FYou are unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xF,
        (
            "Young lady, those are the kind of\x01",
            "words that'll give an old man like\x01",
            "me a heart attack...\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x400000)
    OP_4B(0xF, 0)
    EventEnd(0x0)
    Return()

    # Function_15_3ADF end

    def Function_16_4114(): pass

    label("Function_16_4114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_429C")
    SetMapFlags(0x8000000)
    OP_A2(0x24A)
    OP_A2(0x24D)
    OP_62(0x133, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrPos(0xA, 90000, 0, 61740, 90)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    TurnDirection(0x133, 0xA, 0)
    EventBegin(0x0)

    ChrTalk(    #155
        0xA,
        "Ahhhhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xA,
        (
            "Things weren't supposed to go like this...\x01",
            "I don't wanna die!\x01",
            "I haven't even had a girlfriend yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        "Heeeeelp!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4235")
    Jump("loc_4295")

    label("loc_4235")


    ChrTalk(    #158
        0x133,
        (
            "What?! We've still got another one\x01",
            "down here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#002FWe'd better hurry and rescue him!\x02",
    )

    CloseMessageWindow()

    label("loc_4295")

    EventEnd(0x1)
    ClearMapFlags(0x8000000)

    label("loc_429C")

    Return()

    # Function_16_4114 end

    def Function_17_429D(): pass

    label("Function_17_429D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47DD")
    EventBegin(0x0)
    TurnDirection(0x0, 0x13, 0)
    TurnDirection(0x1, 0x13, 0)
    TurnDirection(0x2, 0x13, 0)
    OP_A2(0x24B)
    SetChrFlags(0xA, 0x40)
    OP_A3(0x9)
    TurnDirection(0x13, 0x101, 800)
    OP_43(0x13, 0x1, 0x0, 0x12)
    TurnDirection(0x15, 0x101, 800)
    OP_43(0x15, 0x1, 0x0, 0x12)
    TurnDirection(0x14, 0x101, 800)
    OP_43(0x14, 0x1, 0x0, 0x12)
    OP_A6(0x9)
    OP_44(0x13, 0xFF)
    OP_44(0x15, 0xFF)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4319"),
        (SWITCH_DEFAULT, "loc_431E"),
    )


    label("loc_4319")

    OP_B4(0x0)
    Jump("loc_431E")

    label("loc_431E")

    EventBegin(0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    SetChrPos(0x133, 91310, 0, 62810, 225)
    SetChrPos(0x102, 91630, 0, 64090, 225)
    SetChrPos(0x101, 92380, 0, 62140, 270)
    OP_6D(91000, 0, 62560, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0xA, 45, 0)
    OP_44(0xA, 0xFF)
    Sleep(1000)

    ChrTalk(    #160
        0xA,
        "#3POh man, you kids saved my skin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#006F#2PDon't worry, you're safe now.\x02\x03",

            "#006FA handful of monsters are no\x01",
            "match for the likes of a bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 600)

    ChrTalk(    #162
        0xA,
        "#3PDid you say b-b-bracers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        (
            "#3PWhat are you doing in a place\x01",
            "like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x133,
        (
            "#4PBy the soot on my boots, you're...\x01",
            "the new recruit from yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x133,
        (
            "#4PWhy on earth are you digging\x01",
            "down here in the lower tunnels?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x133, 600)

    ChrTalk(    #166
        0xA,
        "#3PI, uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "#3PI was hoping to get a glimpse of\x01",
            "how all you veteran miners work\x01",
            "down here... Yeah, that's it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "#3P...when suddenly the wall collapsed\x01",
            "and a flood of monsters came in from\x01",
            "the other side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x133,
        (
            "#4PSo we've got ourselves a veritable\x01",
            "nest of monsters now, huh? It looks\x01",
            "like you guessed right, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        "#012FSo it seems...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "#3PThe area up ahead is dangerous.\x01",
            "It's swarming with monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        "#3PA-Anyway, I'm outta here!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xA, 0x2, 0x0, 0x14)
    OP_8E(0xA, 0x17598, 0x0, 0xF03C, 0x36B0, 0x0)
    OP_8E(0xA, 0x1ACA2, 0x0, 0x11044, 0x36B0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    ChrTalk(    #173
        0x101,
        (
            "#000F#1PWould ya look at him run...\x01",
            "He must've been really scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x102,
        "#010F#3PI bet...\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_44(0xA, 0xFF)

    label("loc_47DD")

    Return()

    # Function_17_429D end

    def Function_18_47DE(): pass

    label("Function_18_47DE")

    OP_92(0xFE, 0x0, 0x262, 0x1388, 0x0)
    OP_A2(0x9)
    Return()

    # Function_18_47DE end

    def Function_19_47F0(): pass

    label("Function_19_47F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_END)), "loc_49EC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496D")
    OP_A2(0x4)
    TurnDirection(0x133, 0x0, 400)

    ChrTalk(    #175
        0x133,
        (
            "Hey, where are you going?\x01",
            "That way leads to the monster den.\x02\x03",

            "The bedrock is also still unstable,\x01",
            "so how about we do ourselves a\x01",
            "favor and keep away from there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492A")
    TurnDirection(0x101, 0x133, 400)

    ChrTalk(    #176
        0x101,
        (
            "#002FIt certainly doesn't look that\x01",
            "safe either.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #177
        0x102,
        "#012FAll right, let's turn back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_496A")

    label("loc_492A")


    def lambda_4930():
        TurnDirection(0x101, 0x133, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4930)
    TurnDirection(0x102, 0x133, 400)

    ChrTalk(    #178
        0x102,
        "#012FYou're right, let's turn around.\x02",
    )

    CloseMessageWindow()

    label("loc_496A")

    Jump("loc_49D1")

    label("loc_496D")


    ChrTalk(    #179
        0x133,
        (
            "That way leads to the monster den.\x01",
            "How about we do ourselves a favor\x01",
            "and keep away from there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D1")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_49EC")

    Return()

    # Function_19_47F0 end

    def Function_20_49ED(): pass

    label("Function_20_49ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A0F")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    TurnDirection(0x2, 0xFE, 0)
    OP_48()
    Jump("Function_20_49ED")

    label("loc_4A0F")

    Return()

    # Function_20_49ED end

    def Function_21_4A10(): pass

    label("Function_21_4A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B80")
    SetMapFlags(0x8000000)
    OP_A2(0x244)
    SetChrPos(0xB, 130840, 1000, 15040, 270)
    SetChrPos(0xC, 130850, 1000, 13860, 270)
    OP_62(0x133, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0xB, 0)
    TurnDirection(0x133, 0xB, 0)
    EventBegin(0x0)

    ChrTalk(    #180
        0xB,
        "D-Don't come any closer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xB,
        (
            "I'm not trying to brag, but I'm\x01",
            "all muscle, so I wouldn't make\x01",
            "a tasty meal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xC,
        (
            "M-Me too!\x01",
            "I'm not delicious, either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xC,
        (
            "All this flab would be terrible\x01",
            "for a monster's health!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    ClearMapFlags(0x8000000)

    label("loc_4B80")

    Return()

    # Function_21_4A10 end

    def Function_22_4B81(): pass

    label("Function_22_4B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E7F")
    OP_A2(0x245)
    EventBegin(0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x1, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    TurnDirection(0x12, 0x101, 500)
    Sleep(200)
    OP_92(0x12, 0x0, 0x1F4, 0x1B58, 0x0)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4BE4"),
        (SWITCH_DEFAULT, "loc_4BE9"),
    )


    label("loc_4BE4")

    OP_B4(0x0)
    Jump("loc_4BE9")

    label("loc_4BE9")

    EventBegin(0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrPos(0x133, 129000, 1000, 12980, 45)
    SetChrPos(0x102, 126780, 1000, 11750, 45)
    SetChrPos(0x101, 127660, 1000, 11490, 45)
    OP_6D(128919, 1000, 12950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    TurnDirection(0xB, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #184
        0x101,
        "#000FYou're safe now, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xB,
        (
            "Th-Thank you for coming when\x01",
            "you did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xC,
        (
            "Oh man, for a minute there, I\x01",
            "thought I'd never be able to sit\x01",
            "down for another meal again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x133,
        (
            "#3PThis is no time to feel relieved!\x01",
            "We need to evacuate this place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x133,
        (
            "#3PAny more lollygagging and you're\x01",
            "going to be sitting in the belly of\x01",
            "one of these monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xB,
        "Y-Yes boss!\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x17)
    Sleep(300)

    ChrTalk(    #190
        0xC,
        "W-Wait for me!\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xC, 0x2, 0x0, 0x14)
    OP_8E(0xC, 0x1EBAE, 0x1F4, 0x3138, 0x1770, 0x0)
    OP_8E(0xC, 0x1DE84, 0xFA, 0x4010, 0x1B58, 0x0)
    OP_8E(0xC, 0x1F07C, 0x0, 0x620C, 0x1F40, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    EventEnd(0x0)
    OP_44(0xC, 0xFF)

    label("loc_4E7F")

    Return()

    # Function_22_4B81 end

    def Function_23_4E80(): pass

    label("Function_23_4E80")

    OP_8E(0xB, 0x1EBAE, 0x1F4, 0x3138, 0x1770, 0x0)
    OP_8E(0xB, 0x1DE84, 0xFA, 0x4010, 0x1B58, 0x0)
    OP_8E(0xB, 0x1F07C, 0x0, 0x620C, 0x1F40, 0x0)
    Return()

    # Function_23_4E80 end

    def Function_24_4EBD(): pass

    label("Function_24_4EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FF5")
    SetMapFlags(0x8000000)
    OP_A2(0x247)
    OP_62(0x133, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xD, 0)
    TurnDirection(0x102, 0xD, 0)
    TurnDirection(0x133, 0xD, 0)
    EventBegin(0x0)

    ChrTalk(    #191
        0xD,
        (
            "Oh, Aidios, who art in heaven...\x01",
            "extend to us thy saving hand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xE,
        "H-Hey, idiot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xE,
        (
            "If you've got time to pray to the\x01",
            "Goddess, then how about helping\x01",
            "me take care of these creatures!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    ClearMapFlags(0x8000000)

    label("loc_4FF5")

    Return()

    # Function_24_4EBD end

    def Function_25_4FF6(): pass

    label("Function_25_4FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F4")
    OP_A2(0x248)
    EventBegin(0x0)
    TurnDirection(0x0, 0x11, 0)
    TurnDirection(0x1, 0x11, 0)
    TurnDirection(0x2, 0x11, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    TurnDirection(0x11, 0x101, 500)
    Sleep(200)
    OP_92(0x11, 0x0, 0x1F4, 0x1B58, 0x0)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5059"),
        (SWITCH_DEFAULT, "loc_505E"),
    )


    label("loc_5059")

    OP_B4(0x0)
    Jump("loc_505E")

    label("loc_505E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x133, 86770, -500, 30250, 315)
    SetChrPos(0x102, 87730, 0, 28260, 315)
    SetChrPos(0x101, 88160, 0, 29600, 315)
    OP_6D(84700, -290, 30790, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    TurnDirection(0xD, 0x101, 0)
    TurnDirection(0xE, 0x101, 0)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    Sleep(1000)

    ChrTalk(    #194
        0x102,
        "#010FIs everyone all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xD,
        "W-We are now...thanks to you kids.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xD,
        (
            "This must also be the divine work\x01",
            "of Aidios.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #197
        0xE,
        "What a religious nut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xE,
        (
            "If this was really the work of the Goddess,\x01",
            "then she wouldn't have allowed us to get\x01",
            "into this mess in the first place.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #199
        0xD,
        (
            "It's because of unbelievers like you\x01",
            "that unfortunate accidents like this\x01",
            "happen!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #200
        0xE,
        (
            "How about you try and say that\x01",
            "again, buddy?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x133, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #201
        0x133,
        (
            "Is this really the time or place\x01",
            "for that kind of nonsense?!\x01",
            "Now get out of here!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x133, 600)
    TurnDirection(0xE, 0x133, 600)

    ChrTalk(    #202
        0xD,
        "R-Right away, boss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xE,
        "You be careful too, boss!\x02",
    )

    CloseMessageWindow()
    OP_43(0xE, 0x1, 0x0, 0x1A)
    Sleep(500)
    OP_43(0xD, 0x2, 0x0, 0x14)
    OP_8E(0xD, 0x14DFC, 0x3E8, 0x7FBC, 0x1770, 0x0)
    OP_8E(0xD, 0x17FFC, 0x0, 0x69DC, 0x1770, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    EventEnd(0x0)
    OP_44(0xD, 0xFF)

    label("loc_53F4")

    Return()

    # Function_25_4FF6 end

    def Function_26_53F5(): pass

    label("Function_26_53F5")

    OP_8E(0xE, 0x14DFC, 0x3E8, 0x7FBC, 0x1770, 0x0)
    OP_8E(0xE, 0x17FFC, 0x0, 0x69DC, 0x1770, 0x0)
    Return()

    # Function_26_53F5 end

    def Function_27_541E(): pass

    label("Function_27_541E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_END)), "loc_546E")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #204
        "\x07\x05The elevator is locked down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Jump("loc_5C69")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4C")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_END)), "loc_5704")
    Fade(1000)
    SetChrPos(0x0, 53590, 50, 57020, 0)
    SetChrPos(0x1, 54570, 50, 57080, 0)
    OP_6D(53780, 50, 58370, 1000)
    OP_A2(0x241)

    ChrTalk(    #205
        0x102,
        (
            "#010FEstelle, try using that key we\x01",
            "just borrowed.\x02\x03",

            "#010FWe should be able to get the\x01",
            "elevator working this time.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #206
        "\x07\x05Estelle used the Elevator Key.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #207
        0x102,
        (
            "#010FIt looks like we can use the\x01",
            "elevator now.\x02\x03",

            "#010FHow about we head down into\x01",
            "the lower tunnels?\x02",
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
            "[Use elevator]\x01",            # 0
            "[Don't use elevator]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5654")
    Sleep(300)
    EventEnd(0x0)
    Return()

    label("loc_5654")

    Fade(1000)
    SetChrPos(0x0, 53590, 50, 57020, 0)
    SetChrPos(0x1, 54570, 50, 57080, 0)
    OP_6D(54090, 50, 57700, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_6F(0x1, 120)
    Fade(1000)
    OP_6D(129000, 0, 76700, 0)
    SetChrPos(0x0, 128580, 8000, 77050, 180)
    SetChrPos(0x1, 129560, 8000, 77060, 180)
    OP_6F(0x2, 360)
    Sleep(120)
    OP_70(0x2, 0xF0)
    OP_73(0x2)
    EventEnd(0x0)
    OP_6F(0x2, 240)
    Return()

    label("loc_5704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_591F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D6")
    Fade(1000)
    SetChrPos(0x101, 53800, 50, 57690, 0)
    SetChrPos(0x102, 54180, 50, 56280, 0)
    OP_6D(53780, 50, 58370, 1000)

    ChrTalk(    #208
        0x101,
        (
            "#002FThis is the elevator we're supposed\x01",
            "to use to reach the lower tunnels,\x01",
            "right?\x02\x03",

            "#002FWhy doesn't it work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        "#012FLet me have a look.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_57EA():

        label("loc_57EA")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_57EA")

    QueueWorkItem2(0x101, 1, lambda_57EA)
    OP_8F(0x101, 0xD08E, 0x32, 0xDEE4, 0x7D0, 0x0)
    OP_8E(0x102, 0xD336, 0x32, 0xE15A, 0x7D0, 0x0)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #210
        0x102,
        (
            "#012FThere's orbal energy running through it,\x01",
            "but it appears to be mechanically locked. \x02\x03",

            "#012FMaybe we should ask someone\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    EventEnd(0x0)
    Jump("loc_591C")

    label("loc_58D6")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #211
        "\x07\x05The elevator is locked down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)

    label("loc_591C")

    Jump("loc_5B40")

    label("loc_591F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF8")
    Fade(1000)
    SetChrPos(0x101, 53800, 50, 57690, 0)
    SetChrPos(0x102, 54180, 50, 56280, 0)
    OP_6D(53780, 50, 58370, 1000)

    ChrTalk(    #212
        0x101,
        (
            "#505FThis is the elevator we're supposed\x01",
            "to use to reach the lower tunnels,\x01",
            "right?\x02\x03",

            "#505FWhy doesn't it work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x102,
        "#010FLet me have a look.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_59FD():

        label("loc_59FD")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_59FD")

    QueueWorkItem2(0x101, 1, lambda_59FD)
    OP_8F(0x101, 0xD08E, 0x32, 0xDEE4, 0x7D0, 0x0)
    OP_8E(0x102, 0xD336, 0x32, 0xE15A, 0x7D0, 0x0)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #214
        0x102,
        (
            "#015FThere's orbal energy running through it,\x01",
            "but it appears to be mechanically locked. \x02\x03",

            "#010FMaybe we should go back and\x01",
            "ask that miner about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    EventEnd(0x0)
    Jump("loc_5B40")

    label("loc_5AF8")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #215
        "\x07\x05The elevator is locked down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)

    label("loc_5B40")

    OP_A2(0x240)
    OP_28(0x3, 0x1, 0x10)
    Jump("loc_5C69")

    label("loc_5B4C")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use elevator]\x01",            # 0
            "[Don't use elevator]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BBE")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_5BBE")

    Fade(1000)
    SetChrPos(0x0, 53590, 50, 57020, 0)
    SetChrPos(0x1, 54570, 50, 57080, 0)
    OP_6D(54090, 50, 57700, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x1, 0x78)
    OP_73(0x1)
    OP_6F(0x1, 120)
    Fade(1000)
    OP_6D(129000, 0, 76700, 0)
    SetChrPos(0x0, 128580, 8000, 77050, 180)
    SetChrPos(0x1, 129560, 8000, 77060, 180)
    OP_6F(0x2, 360)
    Sleep(120)
    OP_70(0x2, 0xF0)
    OP_73(0x2)
    EventEnd(0x0)
    OP_6F(0x2, 240)
    Return()

    label("loc_5C69")

    Return()

    # Function_27_541E end

    def Function_28_5C6A(): pass

    label("Function_28_5C6A")

    OP_92(0x0, 0x1, 0x0, 0xBB8, 0x0)
    TurnDirection(0x0, 0x1, 0)
    Return()

    # Function_28_5C6A end

    def Function_29_5C80(): pass

    label("Function_29_5C80")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D85")
    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)
    TurnDirection(0x0, 0x2, 400)
    TurnDirection(0x1, 0x2, 400)
    TurnDirection(0x2, 0x0, 400)

    ChrTalk(    #216
        0x133,
        (
            "I'm sorry...but there are still\x01",
            "others who need rescuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x133,
        (
            "Can I get you to lend me a hand\x01",
            "for a bit longer?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EEF")
    OP_A2(0x24D)
    SetChrPos(0xA, 90000, 0, 61740, 90)

    ChrTalk(    #218
        0xA,
        (
            "Ahhhhh! Things weren't supposed\x01",
            "to go like this... I don't wanna die!\x01",
            "I haven't even had a girlfriend yet!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    TurnDirection(0x133, 0xA, 0)

    ChrTalk(    #219
        0xA,
        "Heeeeelp!\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)

    ChrTalk(    #220
        0x133,
        (
            "What?! We've still got another\x01",
            "one down here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#002FWe'd better hurry and rescue him!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FC5")

    label("loc_5EEF")

    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)
    TurnDirection(0x101, 0x133, 0)
    TurnDirection(0x102, 0x133, 0)
    TurnDirection(0x133, 0x101, 0)

    ChrTalk(    #222
        0x133,
        (
            "I'm sorry...but there are still others\x01",
            "who need rescuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x133,
        (
            "Can I get you to lend me a hand\x01",
            "for a bit longer?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FC5")

    EventEnd(0x1)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_5FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D4")
    ClearMapFlags(0x1)
    OP_51(0x16, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x133, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x16, 0x320)
    TurnDirection(0x101, 0x133, 0)
    TurnDirection(0x102, 0x133, 0)
    TurnDirection(0x133, 0x101, 0)

    ChrTalk(    #224
        0x101,
        "#000FDid we find everybody?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x133,
        "Yes, that should be everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        (
            "#010FAll right, then let's get out of\x01",
            "here ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x133, 129070, 50, 76680, 0)
    Jump("loc_614B")

    label("loc_60D4")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use elevator]\x01",            # 0
            "[Don't use elevator]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6146")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_6146")

    Fade(1000)

    label("loc_614B")

    SetChrPos(0x0, 128440, 50, 77690, 0)
    SetChrPos(0x1, 129410, 50, 77690, 0)
    OP_6D(129020, 50, 77590, 1000)
    Sleep(120)
    OP_22(0x66, 0x0, 0x64)
    OP_70(0x2, 0x168)
    OP_73(0x2)
    OP_6F(0x2, 360)
    Fade(1000)
    OP_6F(0x1, 120)
    Sleep(120)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62A5")
    SetChrPos(0xD, 51560, 0, 55100, 0)
    SetChrPos(0xE, 51880, 0, 53800, 0)
    SetChrPos(0x9, 53210, 0, 54100, 0)
    SetChrPos(0x8, 55190, 0, 54000, 0)
    SetChrPos(0xB, 55250, 0, 51960, 0)
    SetChrPos(0xC, 56100, 0, 52360, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x133, 0x8)
    ClearChrFlags(0x133, 0x80)
    ClearChrFlags(0x133, 0x4)
    SetChrBattleFlags(0x133, 0x20)
    OP_89(0x133, 54000, 0, 56400, 180)
    TurnDirection(0xD, 0x133, 0)
    TurnDirection(0xE, 0x133, 0)
    TurnDirection(0xC, 0x133, 0)
    TurnDirection(0xB, 0x133, 0)
    TurnDirection(0x9, 0x133, 0)
    TurnDirection(0x8, 0x133, 0)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)

    label("loc_62A5")

    OP_6D(54110, 50, 57680, 0)
    SetChrPos(0x0, 53380, -6000, 57690, 180)
    SetChrPos(0x1, 54620, -6000, 57470, 180)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_6F(0x1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6586")

    def lambda_62FB():
        OP_6D(54030, 0, 55920, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62FB)
    OP_8E(0x133, 0xD41C, 0x0, 0xD714, 0xFA0, 0x0)
    OP_A2(0x24E)
    OP_28(0x3, 0x1, 0x100)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #227
        0x8,
        "Are you all right, boss?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xB,
        "I'm sure glad you're safe!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x101, 400)

    ChrTalk(    #229
        0x133,
        "You can thank these kids for that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x9, 400)

    ChrTalk(    #230
        0x133,
        (
            "By the way, is everyone accounted\x01",
            "for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        "Yep, everyone's here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x9,
        (
            "Well, except for the new guy who\x01",
            "took off like a bat out of hell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x9,
        (
            "The poor guy must have wet\x01",
            "himself scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x133,
        (
            "I see... Well, I hope he doesn't\x01",
            "give up on being a miner after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x133,
        (
            "Anyway, there's a high possibility\x01",
            "that there are monsters still in the\x01",
            "lower tunnels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x133,
        (
            "Until we can confirm that it's safe,\x01",
            "I don't want anyone using the elevator,\x01",
            "you hear me?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x32, 0xFF)
    ClearMapFlags(0x8000000)
    NewScene("ED6_DT01/R0303   ._SN", 3, 0, 0)
    IdleLoop()

    label("loc_6586")

    ClearMapFlags(0x400000)
    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_29_5C80 end

    def Function_30_6593(): pass

    label("Function_30_6593")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6656")
    OP_6D(15980, 0, 32049, 1000)
    OP_A2(0x23D)

    ChrTalk(    #237
        0x101,
        (
            "#000FCheck it out. It's a mine cart.\x01",
            "Do you think it's powered by\x01",
            "orbments, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#010FLooks that way to me. How about we\x01",
            "get in and see where it takes us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6656")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride mine cart\x01",            # 0
            "Don't ride mine cart\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66C3")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_66C3")

    SetMapFlags(0x1)
    Fade(500)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 15900, 400, 32299, 0)
    SetChrPos(0x1, 15900, 400, 32299, 0)
    SetChrPos(0x2, 15900, 400, 32299, 0)
    SetChrPos(0x3, 15900, 400, 32299, 0)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BA")
    OP_A3(0x6)
    OP_A2(0x7)
    OP_A3(0x8)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14A)
    OP_73(0x0)
    OP_6F(0x0, 330)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 34200, 100, 61400, 315)
    SetChrPos(0x1, 34200, 100, 61400, 315)
    SetChrPos(0x2, 34200, 100, 61400, 315)
    SetChrPos(0x3, 34200, 100, 61400, 315)
    Jump("loc_683F")

    label("loc_67BA")

    OP_A3(0x6)
    OP_A3(0x7)
    OP_A2(0x8)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x384)
    OP_73(0x0)
    OP_6F(0x0, 900)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 50500, 0, 51900, 45)
    SetChrPos(0x1, 50500, 0, 51900, 45)
    SetChrPos(0x2, 50500, 0, 51900, 45)
    SetChrPos(0x3, 50500, 0, 51900, 45)

    label("loc_683F")

    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_30_6593 end

    def Function_31_6847(): pass

    label("Function_31_6847")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride mine cart\x01",            # 0
            "Don't ride mine cart\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68B6")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_68B6")

    OP_A2(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    SetMapFlags(0x1)
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 34800, 400, 59200, 225)
    SetChrPos(0x1, 34800, 400, 59200, 225)
    SetChrPos(0x2, 34800, 400, 59200, 225)
    SetChrPos(0x3, 34800, 400, 59200, 225)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    OP_6F(0x0, 330)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_6F(0x0, 0)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x0, 16000, 50, 29700, 180)
    SetChrPos(0x1, 16000, 50, 29700, 180)
    SetChrPos(0x2, 16000, 50, 29700, 180)
    SetChrPos(0x3, 16000, 50, 29700, 180)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_31_6847 end

    def Function_32_69B1(): pass

    label("Function_32_69B1")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Ride mine cart\x01",            # 0
            "Don't ride mine cart\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A20")
    Sleep(300)
    EventEnd(0x1)
    Return()

    label("loc_6A20")

    OP_A2(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    SetMapFlags(0x1)
    Fade(500)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrPos(0x0, 50200, 400, 49900, 270)
    SetChrPos(0x1, 50200, 400, 49900, 270)
    SetChrPos(0x2, 50200, 400, 49900, 270)
    SetChrPos(0x3, 50200, 400, 49900, 270)
    Sleep(500)
    OP_22(0x65, 0x0, 0x64)
    OP_6F(0x0, 900)
    OP_70(0x0, 0x1F4)
    OP_73(0x0)
    OP_6F(0x0, 500)
    Sleep(500)
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrPos(0x0, 16000, 50, 29700, 180)
    SetChrPos(0x1, 16000, 50, 29700, 180)
    SetChrPos(0x2, 16000, 50, 29700, 180)
    SetChrPos(0x3, 16000, 50, 29700, 180)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_32_69B1 end

    def Function_33_6B14(): pass

    label("Function_33_6B14")

    SetMapFlags(0x80)
    Sleep(30)
    OP_22(0x64, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B42")
    OP_70(0x3, 0x19)
    OP_73(0x3)
    OP_6F(0x3, 25)
    OP_A2(0x0)
    Jump("loc_6B56")

    label("loc_6B42")

    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_6F(0x3, 0)
    OP_A3(0x0)

    label("loc_6B56")

    OP_73(0x3)
    ClearMapFlags(0x80)
    Return()

    # Function_33_6B14 end

    def Function_34_6B5F(): pass

    label("Function_34_6B5F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #239
        "\x07\x05There is an orbment charging station.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D75")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 104880, 1000, 39790, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x33, 0)
    OP_70(0x33, 0x32)
    OP_73(0x33)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 106750, 0, 39530, 285)
    SetChrPos(0x1, 106750, 0, 39530, 285)
    SetChrPos(0x2, 106750, 0, 39530, 285)
    SetChrPos(0x3, 106750, 0, 39530, 285)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 104880, 1000, 39790, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x33, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_6D75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D8F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_6D8F")

    Return()

    # Function_34_6B5F end

    SaveToFile()

Try(main)
