from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2521   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2521.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2521   ._SN',
            'ED6_DT01/T2521_1 ._SN',
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
        'Mickey',                               # 9
        'Dennis',                               # 10
        'Jill',                                 # 11
        'Hans',                                 # 12
        'Joshua',                               # 13
        'Deborah',                              # 14
        'Captain Amalthea',                     # 15
        'Rex',                                  # 16
        'Carla',                                # 17
        'Lucia',                                # 18
        'Professor Alba',                       # 19
        'Seagaro',                              # 20
        'Edel',                                 # 21
        'Logic',                                # 22
        'CH22000',                              # 23
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
        'ED6_DT07/CH01080 ._CH',             # 00
        'ED6_DT07/CH01360 ._CH',             # 01
        'ED6_DT07/CH02390 ._CH',             # 02
        'ED6_DT07/CH02550 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH02103 ._CH',             # 06
        'ED6_DT07/CH01023 ._CH',             # 07
        'ED6_DT07/CH01033 ._CH',             # 08
        'ED6_DT07/CH01070 ._CH',             # 09
        'ED6_DT07/CH02050 ._CH',             # 0A
        'ED6_DT07/CH01043 ._CH',             # 0B
        'ED6_DT07/CH01213 ._CH',             # 0C
        'ED6_DT07/CH01080 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
        'ED6_DT07/CH00013 ._CH',             # 0F
        'ED6_DT07/CH02553 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01080P._CP',             # 00
        'ED6_DT07/CH01360P._CP',             # 01
        'ED6_DT07/CH02390P._CP',             # 02
        'ED6_DT07/CH02550P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH02103P._CP',             # 06
        'ED6_DT07/CH01023P._CP',             # 07
        'ED6_DT07/CH01033P._CP',             # 08
        'ED6_DT07/CH01070P._CP',             # 09
        'ED6_DT07/CH02050P._CP',             # 0A
        'ED6_DT07/CH01043P._CP',             # 0B
        'ED6_DT07/CH01213P._CP',             # 0C
        'ED6_DT07/CH01080P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
        'ED6_DT07/CH00013P._CP',             # 0F
        'ED6_DT07/CH02553P._CP',             # 10
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -31200,
        Z                   = 0,
        Y                   = 52500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28700,
        Z                   = 0,
        Y                   = 55100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 29600,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 29600,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -4970,
        Z                   = 250,
        Y                   = -4830,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 250,
        Y                   = -1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -3000,
        Z                   = 250,
        Y                   = 300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 550,
        Z                   = 0,
        Y                   = -2060,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4120,
        Z                   = 0,
        Y                   = 2470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 3960,
        Z                   = 100,
        Y                   = -5890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 100,
        Y                   = -4200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -31470,
        Z                   = 0,
        Y                   = 58630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -31350,
        Z                   = 330,
        Y                   = 23900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835022,
        ChipIndex           = 0xE,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 2130,
        Y                   = 0,
        Z                   = 42010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )


    DeclActor(
        TriggerX            = 3340,
        TriggerZ            = 0,
        TriggerY            = 3110,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31350,
        TriggerZ            = 330,
        TriggerY            = 23900,
        TriggerRange        = 500,
        ActorX              = -31350,
        ActorZ              = 500,
        ActorY              = 23900,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2920,
        TriggerZ            = 0,
        TriggerY            = 49990,
        TriggerRange        = 800,
        ActorX              = 2920,
        ActorZ              = 1000,
        ActorY              = 49990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31560,
        TriggerZ            = 0,
        TriggerY            = 59430,
        TriggerRange        = 800,
        ActorX              = -31560,
        ActorZ              = 1000,
        ActorY              = 59430,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = 53550,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = 53550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_446",          # 00, 0
        "Function_1_5BD",          # 01, 1
        "Function_2_680",          # 02, 2
        "Function_3_7FD",          # 03, 3
        "Function_4_821",          # 04, 4
        "Function_5_B1C",          # 05, 5
        "Function_6_D14",          # 06, 6
        "Function_7_F4D",          # 07, 7
        "Function_8_1613",         # 08, 8
        "Function_9_1BAB",         # 09, 9
        "Function_10_217E",        # 0A, 10
        "Function_11_28DC",        # 0B, 11
        "Function_12_28E1",        # 0C, 12
        "Function_13_2FDA",        # 0D, 13
        "Function_14_31B3",        # 0E, 14
        "Function_15_322A",        # 0F, 15
        "Function_16_325D",        # 10, 16
        "Function_17_329D",        # 11, 17
        "Function_18_3A43",        # 12, 18
        "Function_19_3AA8",        # 13, 19
        "Function_20_3B0D",        # 14, 20
        "Function_21_3B82",        # 15, 21
        "Function_22_3B86",        # 16, 22
        "Function_23_3B8A",        # 17, 23
        "Function_24_3B8E",        # 18, 24
    )


    def Function_0_446(): pass

    label("Function_0_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_455")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_5BC")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_45F")
    Jump("loc_5BC")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_49F")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 250, 0, -1810, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 280, 0, -3490, 0)
    Jump("loc_5BC")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4FB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -28900, 0, 22980, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_5BC")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_588")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_563")
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 16)
    SetChrSubChip(0xB, 0)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -1800, 250, -1090, 270)
    SetChrPos(0xB, -3030, 250, 290, 180)
    Jump("loc_585")

    label("loc_563")

    SetChrPos(0xB, 3610, 0, 50080, 0)
    SetChrPos(0xC, 3610, 0, 50080, 0)

    label("loc_585")

    Jump("loc_5BC")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_597")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_5BC")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_5A1")
    Jump("loc_5BC")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_5AB")
    Jump("loc_5BC")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_5B5")
    Jump("loc_5BC")

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_5BC")

    label("loc_5BC")

    Return()

    # Function_0_446 end

    def Function_1_5BD(): pass

    label("Function_1_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DE")
    OP_B1("t2521_y")
    Jump("loc_5E7")

    label("loc_5DE")

    OP_B1("t2521_n")

    label("loc_5E7")

    OP_64(0x1, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_5FE")
    OP_65(0x1, 0x1)

    label("loc_5FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_612")
    OP_64(0x1, 0x1)
    SetChrFlags(0x16, 0x80)

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_62D")

    label("loc_629")

    OP_64(0x2, 0x1)

    label("loc_62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_66A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x400)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_666")
    Jump("loc_66A")

    label("loc_666")

    OP_65(0x3, 0x1)

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67F")

    Return()

    # Function_1_5BD end

    def Function_2_680(): pass

    label("Function_2_680")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7E7")

    label("loc_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7E7")

    label("loc_6BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7E7")

    label("loc_6D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7E7")

    label("loc_6F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7E7")

    label("loc_709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_722")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7E7")

    label("loc_722")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7E7")

    label("loc_73B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7E7")

    label("loc_754")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7E7")

    label("loc_76D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_786")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7E7")

    label("loc_786")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7E7")

    label("loc_79F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7E7")

    label("loc_7B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7E7")

    label("loc_7D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7E7")

    label("loc_7FC")

    Return()

    # Function_2_680 end

    def Function_3_7FD(): pass

    label("Function_3_7FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_820")
    OP_8D(0xFE, -590, -1050, 1740, -4800, 3000)
    Jump("Function_3_7FD")

    label("loc_820")

    Return()

    # Function_3_7FD end

    def Function_4_821(): pass

    label("Function_4_821")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(    #0
        0xFE,
        "Ahhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Ahhh, it's finally over. I think\x01",
            "I'm going to go home and get\x01",
            "some rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B18")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_9A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "I don't want to have anything\x01",
            "to do with the campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd rather just spend the\x01",
            "time relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Why should I have to get\x01",
            "roped into this crap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A6")

    label("loc_944")


    ChrTalk(    #5
        0xFE,
        (
            "I'd rather just spend the\x01",
            "time relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Why should I have to get\x01",
            "roped into this crap?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A6")

    Jump("loc_B18")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3C")
    OP_A2(0x0)

    ChrTalk(    #7
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Ah, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Class is dull and the student\x01",
            "council president is annoying,\x01",
            "so I'm just killing time here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9D")

    label("loc_A3C")


    ChrTalk(    #10
        0xFE,
        (
            "Class is dull and the student\x01",
            "council president is annoying,\x01",
            "so I'm just killing time here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9D")

    Jump("loc_B18")

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_B18")

    ChrTalk(    #11
        0xFE,
        (
            "Setting up for the campus festival\x01",
            "is such a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Let the people that want to be\x01",
            "involved work on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B18")

    TalkEnd(0x8)
    Return()

    # Function_4_821 end

    def Function_5_B1C(): pass

    label("Function_5_B1C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    OP_A2(0x1)

    ChrTalk(    #13
        0xFE,
        "Why do you say that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "She already has two very\x01",
            "fine suitors.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 800)

    ChrTalk(    #15
        0xFE,
        (
            "Huh...h-how long have you\x01",
            "been standing there?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #16
        0xFE,
        (
            "P-Please, don't make this out to\x01",
            "be something that it's not. I was\x01",
            "just reciting lines from the play.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    Jump("loc_CA5")

    label("loc_C58")


    ChrTalk(    #17
        0xFE,
        (
            "I just don't want to make any\x01",
            "mistakes and look foolish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "*grumble*\x02",
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_D10")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_D10")

    ChrTalk(    #19
        0xFE,
        "*grumble grumble*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Wh-What do you want? Please don't\x01",
            "interrupt me. I'm trying to study.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D10")

    TalkEnd(0x9)
    Return()

    # Function_5_B1C end

    def Function_6_D14(): pass

    label("Function_6_D14")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E23")
    OP_A2(0x2)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #21
        0xFE,
        (
            "#640FHi, Kloe. Have the kids from\x01",
            "the orphanage gotten here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        "#040FYes. All present and accounted for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "#640FGood. Hopefully, they'll be able to\x01",
            "forget about all this nastiness,\x01",
            "at least for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        "#040FIndeed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E85")

    label("loc_E23")


    ChrTalk(    #25
        0xFE,
        (
            "#640FI'd like to help the kids forget\x01",
            "about all this nastiness, at\x01",
            "least for a little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E85")

    Jump("loc_F49")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_F49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F11")
    OP_A2(0x2)

    ChrTalk(    #26
        0xFE,
        (
            "#640FOkay, that should do it.\x01",
            "There's our projected budget.\x02\x03",

            "We should be okay, since\x01",
            "it's not that much.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_F49")

    label("loc_F11")


    ChrTalk(    #27
        0xFE,
        (
            "#640FOh, what's up, you three?\x01",
            "Are you having fun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F49")

    TalkEnd(0xA)
    Return()

    # Function_6_D14 end

    def Function_7_F4D(): pass

    label("Function_7_F4D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_108F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF4")
    OP_A2(0x3)

    ChrTalk(    #28
        0xFE,
        (
            "#733FOh...Kloe and Estelle...\x02\x03",

            "#730FSo what's so important that Joshua\x01",
            "actually thought it was okay to\x01",
            "leave two cute girls on their own?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108C")

    label("loc_FF4")


    ChrTalk(    #29
        0xFE,
        (
            "#730FOnce the play starts up,\x01",
            "everyone will be locked out\x01",
            "of this building for a while.\x02\x03",

            "It's to keep anyone from coming\x01",
            "in and stealing anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108C")

    Jump("loc_160F")

    label("loc_108F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_10F7")

    ChrTalk(    #30
        0xFE,
        (
            "#730FThe documents are all set to go.\x02\x03",

            "Now we just need to get the\x01",
            "dean to approve them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160F")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 2)), scpexpr(EXPR_END)), "loc_1604")

    ChrTalk(    #31
        0xFE,
        (
            "#730FWhat...?\x02\x03",

            "You ready to order some food?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Order food]\x01",        # 0
            "[Not just yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_119D"),
        (0, "loc_11E0"),
        (SWITCH_DEFAULT, "loc_1601"),
    )


    label("loc_119D")


    ChrTalk(    #32
        0xFE,
        (
            "#730FWhen you're done with your\x01",
            "errands, give me a holler.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1601")

    label("loc_11E0")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-1640, 0, -1220, 0)
    SetChrPos(0x101, -1160, 0, -1960, 315)
    SetChrPos(0x105, -1530, 0, -3000, 0)
    SetChrPos(0x13B, -2250, 0, -2380, 0)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #33
        0x13B,
        (
            "#645F#3POh, man. My stomach cries\x01",
            "out for nourishment!\x02\x03",

            "Finishing up the play and having to\x01",
            "run hither and yon like a madman\x01",
            "really works up an appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        (
            "#048FHa ha... But that all ends after\x01",
            "today, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x13B,
        (
            "#644F#3PYou're right. I've gotta get motivated!\x02\x03",

            "Got the new job to deal with\x01",
            "and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        "#733FWait, what? What new job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x13B,
        (
            "#640F#3PYeah, I'll tell you about it later.\x02\x03",

            "#641FLet's go out there and stir things\x01",
            "up! We're going to make this\x01",
            "festival a huge success!\x02\x03",

            "I'll be counting on you, Estelle.\x01",
            "You too, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 0)
    Sleep(300)

    ChrTalk(    #38
        0x101,
        "#006FOh, I'm all over it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        "#019FWe'll do our absolute best.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()

    AnonymousTalk(    #40
        "\x07\x05That evening, everyone spent a rather busy hour in the cafeteria...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #41
        (
            "\x07\x05At the end, they all raised a toast (with soft drinks) to the success of the\x01",
            "play.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #42
        (
            "\x07\x05Afterward, they returned to the dorm and went to bed early, in order to be\x01",
            "prepared for the busy day ahead.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #43
        "\x07\x05And on the day of the festival...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x431)
    OP_A2(0x3FA)
    RemoveParty(0x3A, 0xFF)
    NewScene("ED6_DT01/T2523   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_1601")

    label("loc_1601")

    Jump("loc_160F")

    label("loc_1604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_160F")
    Call(0, 9)

    label("loc_160F")

    TalkEnd(0xB)
    Return()

    # Function_7_F4D end

    def Function_8_1613(): pass

    label("Function_8_1613")

    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1638")
    SetChrSubChip(0xC, 2)
    Jump("loc_1669")

    label("loc_1638")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_164E")
    SetChrSubChip(0xC, 1)
    Jump("loc_1669")

    label("loc_164E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1664")
    SetChrSubChip(0xC, 0)
    Jump("loc_1669")

    label("loc_1664")

    SetChrSubChip(0xC, 2)

    label("loc_1669")

    OP_8C(0xC, 270, 0)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 2)), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(    #44
        0xC,
        (
            "#010FDid you want to order something\x01",
            "to eat?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Order food]\x01",        # 0
            "[Not just yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_171B"),
        (0, "loc_176A"),
        (SWITCH_DEFAULT, "loc_1B99"),
    )


    label("loc_171B")


    ChrTalk(    #45
        0xC,
        (
            "#010FI'm going to go sit down. Just\x01",
            "let me know when you're done.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    Jump("loc_1B99")

    label("loc_176A")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-1640, 0, -1220, 0)
    SetChrPos(0x101, -1160, 0, -1960, 315)
    SetChrPos(0x105, -1530, 0, -3000, 0)
    SetChrPos(0x13B, -2250, 0, -2380, 0)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #46
        0x13B,
        (
            "#645F#3POh, man. My stomach cries\x01",
            "out for nourishment!\x02\x03",

            "Finishing up the play and having to\x01",
            "run hither and yon like a madman\x01",
            "really works up an appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x105,
        (
            "#048FHa ha...but that all ends after\x01",
            "today, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x13B,
        (
            "#644F#3PYou're right. I've gotta get motivated!\x02\x03",

            "Got the new job to deal with\x01",
            "and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        "#733FWait, what? What new job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x13B,
        (
            "#640F#3PYeah, I'll tell you about it later.\x02\x03",

            "#641FLet's go out there and stir things\x01",
            "up! We're going to make this\x01",
            "festival a huge success!\x02\x03",

            "I'll be counting on you, Estelle.\x01",
            "You too, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 0)
    Sleep(300)

    ChrTalk(    #51
        0x101,
        "#006FOh, I'm all over it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        "#019FWe'll do our absolute best.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()

    AnonymousTalk(    #53
        (
            "\x07\x05That evening, everyone spent a rather\x01",
            "busy hour in the cafeteria...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #54
        (
            "\x07\x05At the end, they all raised a toast (with\x01",
            "soft drinks) to the success of the play.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x05Afterward, they returned to the dorm\x01",
            "and went to bed early, in order to\x01",
            "be prepared for the busy day ahead.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #56
        "\x07\x05And on the day of the festival...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    OP_A2(0x431)
    OP_A2(0x3FA)
    RemoveParty(0x3A, 0xFF)
    NewScene("ED6_DT01/T2523   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_1B99")

    label("loc_1B99")

    Jump("loc_1BA7")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_1BA7")
    Call(0, 9)

    label("loc_1BA7")

    TalkEnd(0xC)
    Return()

    # Function_8_1613 end

    def Function_9_1BAB(): pass

    label("Function_9_1BAB")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-1640, 0, -1220, 0)
    SetChrPos(0x101, -1160, 0, -1960, 315)
    SetChrPos(0x105, -1530, 0, -3000, 0)
    SetChrPos(0x13B, -2250, 0, -2380, 0)
    SetChrSubChip(0xC, 1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 1)), scpexpr(EXPR_END)), "loc_1C23")

    ChrTalk(    #57
        0x101,
        "#503FUm...we're here...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C46")

    label("loc_1C23")


    ChrTalk(    #58
        0x101,
        "#001FHeeeyyyy! ♪ We're here!\x02",
    )

    CloseMessageWindow()

    label("loc_1C46")


    ChrTalk(    #59
        0x13B,
        "#641F#6PWhew...thanks everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xC,
        "#010FThank you, Jill.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "#730FHey, we've been waiting for you.\x02\x03",

            "NOW are you ready to order\x01",
            "some food?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Order food]\x01",        # 0
            "[Not just yet]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1D45"),
        (0, "loc_1D99"),
        (SWITCH_DEFAULT, "loc_217D"),
    )


    label("loc_1D45")


    ChrTalk(    #62
        0xC,
        (
            "#010FI'm going to go sit down. Just\x01",
            "let me know when you're done.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    OP_A2(0x44A)
    EventEnd(0x0)
    Jump("loc_217D")

    label("loc_1D99")


    ChrTalk(    #63
        0x13B,
        (
            "#645F#6POh, man. My stomach cries\x01",
            "out for nourishment!\x02\x03",

            "Finishing up the play and having to\x01",
            "run hither and yon like a madman\x01",
            "really works up an appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        (
            "#048FHa ha...but that all ends after\x01",
            "today, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x13B,
        (
            "#644F#6PYou're right. I've gotta get motivated!\x02\x03",

            "Got the new job to deal with\x01",
            "and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xB,
        "#733FWait, what? What new job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x13B,
        (
            "#640F#6PYeah, I'll tell you about it later.\x02\x03",

            "#641FLet's go out there and stir things\x01",
            "up! We're going to make this\x01",
            "festival a huge success!\x02\x03",

            "I'll be counting on you, Estelle.\x01",
            "You too, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 0)
    Sleep(300)

    ChrTalk(    #68
        0x101,
        "#006FOh, I'm all over it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xC,
        "#019FWe'll do our absolute best.\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()

    AnonymousTalk(    #70
        (
            "\x07\x05That evening, everyone spent a rather\x01",
            "busy hour in the cafeteria...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #71
        (
            "\x07\x05At the end, they all raised a toast (with\x01",
            "soft drinks) to the success of the play.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        (
            "\x07\x05Afterward, they returned to the dorm\x01",
            "and went to bed early, in order to\x01",
            "be prepared for the busy day ahead.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        "\x07\x05And on the day of the festival...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMapFlags(0x100000)
    OP_22(0xD, 0x0, 0x64)
    OP_A2(0x431)
    OP_28(0x3D, 0x1, 0x800)
    OP_A2(0x3FA)
    RemoveParty(0x3A, 0xFF)
    NewScene("ED6_DT01/T2523   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_217D")

    label("loc_217D")

    Return()

    # Function_9_1BAB end

    def Function_10_217E(): pass

    label("Function_10_217E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285C")
    OP_A2(0x449)
    EventBegin(0x0)

    NpcTalk(    #74
        0xB,
        "Hans's Voice",
        (
            "#4PMs. Wiola is so damn hot.\x02\x03",

            "Plus she's really up-front about things\x01",
            "and seems low-maintenance, which\x01",
            "always scores big points with me.\x02\x03",

            "On the other hand, I don't get the\x01",
            "feeling that there's a beating heart\x01",
            "under Ms. Millia's chilly exterior.\x02\x03",

            "But man, there's something \x01",
            "about a woman wearing a pair\x01",
            "of glasses that suits her...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0xC,
        "Joshua's Voice",
        (
            "#3PWell, far be it for me to challenge\x01",
            "a strongly-held opinion...\x02\x03",

            "But wouldn't that also apply\x01",
            "to Jill?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0xB,
        "Hans's Voice",
        (
            "#4PI-It's not just about the glasses.\x02\x03",

            "Mature women just have this\x01",
            "glamour to them!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0xC,
        "Joshua's Voice",
        (
            "#3PHa ha...feeling a little anxious,\x01",
            "are we?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0xB,
        "Hans's Voice",
        "#4PNever in my life!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)

    ChrTalk(    #79
        0x101,
        (
            "#007F(Didn't they say they were\x01",
            "going to their seats? What's\x01",
            "this all about?)\x02\x03",

            "(Boys can be so hopeless sometimes.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x105,
        (
            "#045F(Well, Joshua's in on this\x01",
            "conversation, too...)\x02\x03",

            "(I'm kind of surprised.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0xB,
        "Hans's Voice",
        (
            "#4PSo...how far have you gone\x01",
            "with Estelle?\x02\x03",

            "I KNOW you're not going to\x01",
            "tell me you haven't done\x01",
            "anything with her.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0xC,
        "Joshua's Voice",
        (
            "#3PSorry to disappoint you, but you\x01",
            "have an overactive imagination.\x02\x03",

            "What am I supposed to say?\x01",
            "Not that it would be any\x01",
            "of your business, mind you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #83
        0xB,
        "Hans's Voice",
        (
            "#4PHuh...you don't say. I just\x01",
            "figured you two would make\x01",
            "a good couple.\x02\x03",

            "So if you've given up on that,\x01",
            "what's your plan of attack\x01",
            "on Kloe?\x02\x03",

            "You might have to practice, but if\x01",
            "you'd straighten up a little, you\x01",
            "could be a good match for her.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0xC,
        "Joshua's Voice",
        (
            "#3PAnd what's that supposed\x01",
            "to mean...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x105)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #85
        0x101,
        (
            "#503F(You wanna get out of here and\x01",
            "go on to the dean's office?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #86
        0x105,
        (
            "#542F(Y-Yes...we need to meet\x01",
            "up with Jill. )\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_28DB")

    label("loc_285C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AC")

    ChrTalk(    #87
        0x101,
        (
            "#503F(We need to meet up with Jill\x01",
            "in the dean's office.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D9")

    label("loc_28AC")


    ChrTalk(    #88
        0x105,
        "#540F(U-Umm...I don't want to intrude.)\x02",
    )

    CloseMessageWindow()

    label("loc_28D9")

    EventEnd(0x1)

    label("loc_28DB")

    Return()

    # Function_10_217E end

    def Function_11_28DC(): pass

    label("Function_11_28DC")

    Call(0, 12)
    Return()

    # Function_11_28DC end

    def Function_12_28E1(): pass

    label("Function_12_28E1")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                          # 0
            "Shop\x01",                          # 1
            "[Jenis Lunch] - 500 mira\x01",      # 2
            "Leave\x01",                         # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295A")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x30)
    OP_56(0x0)
    TalkEnd(0xD)
    Return()

    label("loc_295A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A60")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A26")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #89
        "\x06\x07\x00Ate \x07\x02Jenis Lunch\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_29EB")
    Jump("loc_2A18")

    label("loc_29EB")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #90
        "\x06\x07\x00Learned '\x07\x02Jenis Lunch\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_2A18")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_2A4E")

    label("loc_2A26")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #91
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_2A4E")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xD)
    Return()

    label("loc_2A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7A")
    FadeToBright(300, 0)
    TalkEnd(0xD)
    Return()

    label("loc_2A7A")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2AB4")

    ChrTalk(    #92
        0xD,
        (
            "Hey there!\x01",
            "What can I do for you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_2C15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCC")
    OP_A2(0x4)

    ChrTalk(    #93
        0xD,
        (
            "I got to see the play earlier.\x01",
            "You folks did a really great job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "To thank you for all your hard work on\x01",
            "it, please, take this. It's not much,\x01",
            "but you might find some use for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xD,
        "On the house.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC9")
    OP_A2(0x452)
    OP_3E(0x384, 1)

    AnonymousTalk(    #96
        "\x07\x00Received \x07\x02Firefly Fungus\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2BC9")

    Jump("loc_2C12")

    label("loc_2BCC")


    ChrTalk(    #97
        0xD,
        (
            "I got to see the play earlier.\x01",
            "You folks did a really great job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C12")

    Jump("loc_2FD6")

    label("loc_2C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2C78")

    ChrTalk(    #98
        0xD,
        "You folks are in the play, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "I'm planning to go see it.\x01",
            "I hope it's good!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2CD4")

    ChrTalk(    #100
        0xD,
        (
            "The place is open today as a\x01",
            "rest area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        "Still got the same food though!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2D6E")

    ChrTalk(    #102
        0xD,
        (
            "I'll bet you've been so involved\x01",
            "with setting up that you haven't\x01",
            "been eating so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "Kids like you need to make\x01",
            "sure you eat right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2DF7")

    ChrTalk(    #104
        0xD,
        "So, how's the festival setup going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        (
            "You need to keep your strength\x01",
            "up, so big servings all around.\x01",
            "Come by any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2E6F")

    ChrTalk(    #106
        0xD,
        "Well, now...classes are almost over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "I should get flooded with hungry\x01",
            "young students here, shortly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2EE6")

    ChrTalk(    #108
        0xD,
        (
            "Well, if it isn't Kloe. I thought\x01",
            "you'd be in class still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xD,
        (
            "I'm sorry, hon, but we're not\x01",
            "open yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_2F60")

    ChrTalk(    #110
        0xD,
        (
            "Oh, aren't you thinking of\x01",
            "enrolling here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "Well, you don't have to be a\x01",
            "student to eat here, sweetie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD6")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2FD6")

    ChrTalk(    #112
        0xD,
        (
            "What'll you have to eat for your\x01",
            "little field trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        (
            "If you're hungry, you don't have\x01",
            "to be shy here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD6")

    TalkEnd(0xD)
    Return()

    # Function_12_28E1 end

    def Function_13_2FDA(): pass

    label("Function_13_2FDA")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310C")
    OP_A2(0x5)

    ChrTalk(    #114
        0x101,
        (
            "#501F(Huh...where have I seen\x01",
            "her before?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#010F(I believe she was with Colonel\x01",
            "Richard in the sky bandit hideout.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "#181FHa ha...the Colonel often spoke\x01",
            "of coming to visit...\x02\x03",

            "He still has his hands full\x01",
            "at the moment, though.\x02\x03",

            "I'm sure he'll be free to drop by\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AF")

    label("loc_310C")


    ChrTalk(    #117
        0xFE,
        (
            "#181FHa ha...the Colonel often spoke\x01",
            "of coming to visit...\x02\x03",

            "He still has his hands full\x01",
            "at the moment, though.\x02\x03",

            "I'm sure he'll be free to drop by\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AF")

    TalkEnd(0xE)
    Return()

    # Function_13_2FDA end

    def Function_14_31B3(): pass

    label("Function_14_31B3")

    TalkBegin(0xF)

    ChrTalk(    #118
        0xFE,
        (
            "My wife and I moved to Manoria\x01",
            "years ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "...but this is our first time visiting\x01",
            "the royal academy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_14_31B3 end

    def Function_15_322A(): pass

    label("Function_15_322A")

    TalkBegin(0x10)

    ChrTalk(    #120
        0xFE,
        (
            "I'm amazed that the campus\x01",
            "is so busy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_15_322A end

    def Function_16_325D(): pass

    label("Function_16_325D")

    TalkBegin(0x11)

    ChrTalk(    #121
        0xFE,
        (
            "Heehee... I came here with Clem\x01",
            "and the other kids.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_16_325D end

    def Function_17_329D(): pass

    label("Function_17_329D")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391C")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 4710, 0, 1390, 0)
    SetChrPos(0x105, 3350, 0, 1120, 0)
    SetChrPos(0x102, 3900, 0, 320, 0)
    OP_6D(4270, 0, 2180, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_8C(0xFE, 180, 0)
    OP_4A(0xFE, 255)
    OP_0D()
    OP_A2(0x459)

    ChrTalk(    #122
        0x101,
        (
            "#004F...Huh?\x02\x03",

            "Professor Alba, is that you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "#130FWell! Estelle and Joshua.\x02\x03",

            "This is a pleasant surprise.\x01",
            "I trust you're doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#010FWere you invited here for\x01",
            "the festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "#130FSadly, no. I'm here on\x01",
            "other business.\x02\x03",

            "I've come to investigate a\x01",
            "new discovery within the\x01",
            "Sapphirl Tower.\x02\x03",

            "I was hoping that the academy\x01",
            "could provide me with some\x01",
            "useful materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#506FWow, you're really dedicated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "#130FHa ha... Well, I have to be. Research\x01",
            "hasn't made me wealthy, so I'm\x01",
            "fueled by pure enthusiasm.\x02\x03",

            "#132FOn a related note, the academy's curriculum is\x01",
            "divided into a few courses, isn't it?\x02\x03",

            "Will there be any exhibitions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x105,
        (
            "#040FYes, although of the three courses available\x01",
            "to study here only the social studies class\x01",
            "will have an exhibition.\x02\x03",

            "The students are displaying the results of an\x01",
            "independent research project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "#130FI see. I recall my own\x01",
            "days as a student.\x02\x03",

            "So, where is this research\x01",
            "publication made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#505FOhhh, okay. This must be your\x01",
            "first time at the academy, right?\x02\x03",

            "Huh...let's see. \x01",
            "How to explain...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x105,
        (
            "#045FIndeed. The campus is fairly\x01",
            "littered with buildings.\x02\x03",

            "#040FIf you'd like, we can just take\x01",
            "you there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "#131FThat WOULD be helpful...\x02\x03",

            "...but I'd hate to spoil your\x01",
            "fun here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#001FOh, it's fine. We're not doing\x01",
            "anything major right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "#130FI see. Well, in that case, I would greatly\x01",
            "appreciate you showing me to the exhibition\x01",
            "hall, whenever you have time.\x02\x03",

            "I'll be waiting for you right\x01",
            "here in the cafeteria.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_4B(0xFE, 255)
    EventEnd(0x0)
    Jump("loc_3A3F")

    label("loc_391C")


    ChrTalk(    #135
        0xFE,
        (
            "#130FMy...the students here\x01",
            "are fortunate.\x02\x03",

            "I certainly wish my own meals\x01",
            "only cost this much.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Continue looking around campus]\x01",                     # 0
            "[Take the professor to the social studies room]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A22"),
        (1, "loc_3A25"),
        (SWITCH_DEFAULT, "loc_3A3F"),
    )


    label("loc_3A22")

    Jump("loc_3A3F")

    label("loc_3A25")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2520   ._SN", 123, 0, 0)
    IdleLoop()
    Jump("loc_3A3F")

    label("loc_3A3F")

    TalkEnd(0x12)
    Return()

    # Function_17_329D end

    def Function_18_3A43(): pass

    label("Function_18_3A43")

    TalkBegin(0x13)

    ChrTalk(    #136
        0xFE,
        (
            "Wow... The school's really shaping\x01",
            "up lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I've only ever been to Sunday\x01",
            "School.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_18_3A43 end

    def Function_19_3AA8(): pass

    label("Function_19_3AA8")

    TalkBegin(0x14)

    ChrTalk(    #138
        0xFE,
        (
            "I've always heard stories about how\x01",
            "I should visit the royal academy if\x01",
            "I ever traveled.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_19_3AA8 end

    def Function_20_3B0D(): pass

    label("Function_20_3B0D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #139
        (
            "\x07\x05       Student Council Office\x01\x01",
            "  Students and faculty only, please\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_3B0D end

    def Function_21_3B82(): pass

    label("Function_21_3B82")

    SetPlaceName(0x71)
    Return()

    # Function_21_3B82 end

    def Function_22_3B86(): pass

    label("Function_22_3B86")

    SetPlaceName(0x72)
    Return()

    # Function_22_3B86 end

    def Function_23_3B8A(): pass

    label("Function_23_3B8A")

    SetPlaceName(0x75)
    Return()

    # Function_23_3B8A end

    def Function_24_3B8E(): pass

    label("Function_24_3B8E")

    SetPlaceName(0x70)
    Return()

    # Function_24_3B8E end

    SaveToFile()

Try(main)
