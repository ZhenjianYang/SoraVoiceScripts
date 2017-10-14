from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4122   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4122.x',
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
        'Filder',                               # 9
        'Sasha',                                # 10
        'Hardt',                                # 11
        'Passenger',                            # 12
        'Passenger',                            # 13
        'Passenger',                            # 14
        'Bloom',                                # 15
        'Lily',                                 # 16
        'Danton',                               # 17
        'Midee',                                # 18
        'Edel',                                 # 19
        'Kitty',                                # 20
        'Sienna',                               # 21
        'Terell',                               # 22
        'Bloom',                                # 23
        'Agate',                                # 24
        'Scherazard',                           # 25
        'Tita',                                 # 26
        'Major Vander',                         # 27
        'Ambassador Crainagh',                  # 28
        'Ambassador Cochrane',                  # 29
        'Renne',                                # 30
        'Targeting Camera',                     # 31
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT27/CH03570 ._CH',             # 02
        'ED6_DT27/CH03710 ._CH',             # 03
        'ED6_DT27/CH03720 ._CH',             # 04
        'ED6_DT27/CH03510 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01770 ._CH',             # 08
        'ED6_DT07/CH01210 ._CH',             # 09
        'ED6_DT07/CH01120 ._CH',             # 0A
        'ED6_DT07/CH01130 ._CH',             # 0B
        'ED6_DT07/CH01010 ._CH',             # 0C
        'ED6_DT07/CH01013 ._CH',             # 0D
        'ED6_DT07/CH00050 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT27/CH03060 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT27/CH03570P._CP',             # 02
        'ED6_DT27/CH03710P._CP',             # 03
        'ED6_DT27/CH03720P._CP',             # 04
        'ED6_DT27/CH03510P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01770P._CP',             # 08
        'ED6_DT07/CH01210P._CP',             # 09
        'ED6_DT07/CH01120P._CP',             # 0A
        'ED6_DT07/CH01130P._CP',             # 0B
        'ED6_DT07/CH01010P._CP',             # 0C
        'ED6_DT07/CH01013P._CP',             # 0D
        'ED6_DT07/CH00050P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT27/CH03060P._CP',             # 10
    )

    DeclNpc(
        X                   = -1440,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 179,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 1970,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -3140,
        Z                   = 0,
        Y                   = 63640,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -4370,
        Z                   = 0,
        Y                   = 62760,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 4950,
        Z                   = 0,
        Y                   = 60820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -3020,
        Z                   = 0,
        Y                   = 57190,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 3110,
        Z                   = 250,
        Y                   = 60150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8790,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 12170,
        Z                   = 0,
        Y                   = -4050,
        Direction           = 163,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = 10,
        Direction           = 204,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -13690,
        Z                   = 250,
        Y                   = 11270,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -13060,
        Z                   = 0,
        Y                   = 6390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 13590,
        Z                   = 0,
        Y                   = -8540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = -7930,
        Direction           = 200,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 90,
        Z                   = 0,
        Y                   = 63630,
        Direction           = 343,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 90,
        Z                   = 0,
        Y                   = 63630,
        Direction           = 343,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 2900,
        Z                   = 0,
        Y                   = 3330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
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


    DeclActor(
        TriggerX            = 8450,
        TriggerZ            = 0,
        TriggerY            = 8650,
        TriggerRange        = 800,
        ActorX              = 8790,
        ActorZ              = 1500,
        ActorY              = 10500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11970,
        TriggerZ            = 0,
        TriggerY            = -5950,
        TriggerRange        = 800,
        ActorX              = 12170,
        ActorZ              = 1500,
        ActorY              = -4050,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6400,
        TriggerZ            = 0,
        TriggerY            = 9620,
        TriggerRange        = 800,
        ActorX              = -4540,
        ActorZ              = 1500,
        ActorY              = 9850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1370,
        TriggerZ            = 0,
        TriggerY            = 63610,
        TriggerRange        = 800,
        ActorX              = -1440,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1850,
        TriggerZ            = 0,
        TriggerY            = 63640,
        TriggerRange        = 800,
        ActorX              = 1970,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4C6",          # 00, 0
        "Function_1_5D8",          # 01, 1
        "Function_2_669",          # 02, 2
        "Function_3_7E6",          # 03, 3
        "Function_4_80A",          # 04, 4
        "Function_5_80F",          # 05, 5
        "Function_6_E33",          # 06, 6
        "Function_7_E38",          # 07, 7
        "Function_8_124D",         # 08, 8
        "Function_9_1252",         # 09, 9
        "Function_10_1A08",        # 0A, 10
        "Function_11_1EE0",        # 0B, 11
        "Function_12_2173",        # 0C, 12
        "Function_13_24AC",        # 0D, 13
        "Function_14_2883",        # 0E, 14
        "Function_15_2C20",        # 0F, 15
        "Function_16_2C25",        # 10, 16
        "Function_17_34E4",        # 11, 17
        "Function_18_34E9",        # 12, 18
        "Function_19_3DC1",        # 13, 19
        "Function_20_4226",        # 14, 20
        "Function_21_42B8",        # 15, 21
        "Function_22_42F2",        # 16, 22
        "Function_23_4374",        # 17, 23
        "Function_24_4386",        # 18, 24
        "Function_25_44BB",        # 19, 25
        "Function_26_45E9",        # 1A, 26
        "Function_27_470B",        # 1B, 27
        "Function_28_4A7B",        # 1C, 28
        "Function_29_71BC",        # 1D, 29
        "Function_30_7212",        # 1E, 30
        "Function_31_7227",        # 1F, 31
        "Function_32_723C",        # 20, 32
        "Function_33_7A45",        # 21, 33
        "Function_34_7AE0",        # 22, 34
    )


    def Function_0_4C6(): pass

    label("Function_0_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4EF")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, -13690, 250, 11270, 191)
    OP_64(0x2, 0x1)
    SetChrFlags(0x16, 0x80)
    Jump("loc_586")

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_51D")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, -13690, 250, 11270, 191)
    OP_64(0x2, 0x1)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_586")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_56A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_540")
    ClearChrFlags(0x17, 0x80)
    Jump("loc_545")

    label("loc_540")

    ClearChrFlags(0x18, 0x80)

    label("loc_545")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 5430, 0, 1900, 0)
    OP_43(0x1D, 0x0, 0x0, 0x2)

    label("loc_567")

    Jump("loc_586")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_586")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A2"),
        (101, "loc_5A2"),
        (102, "loc_5A2"),
        (103, "loc_5A2"),
        (104, "loc_5BA"),
        (SWITCH_DEFAULT, "loc_5D7"),
    )


    label("loc_5A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B7")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_5B7")

    Jump("loc_5D7")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D4")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_5D4")

    Jump("loc_5D7")

    label("loc_5D7")

    Return()

    # Function_0_4C6 end

    def Function_1_5D8(): pass

    label("Function_1_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4")
    OP_B1("t4122_y")
    Jump("loc_5FD")

    label("loc_5F4")

    OP_B1("t4122_n")

    label("loc_5FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615")
    OP_10(0x6, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x4, 0x0)
    Jump("loc_644")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_628")
    OP_10(0x6, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_644")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_63B")
    OP_10(0x6, 0x0)
    OP_10(0x4, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_644")

    label("loc_63B")

    OP_10(0x6, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x4, 0x1)

    label("loc_644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 59)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 59)

    label("loc_668")

    Return()

    # Function_1_5D8 end

    def Function_2_669(): pass

    label("Function_2_669")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7D0")

    label("loc_68E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7D0")

    label("loc_6A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7D0")

    label("loc_6C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7D0")

    label("loc_6D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7D0")

    label("loc_6F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7D0")

    label("loc_70B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7D0")

    label("loc_724")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7D0")

    label("loc_73D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7D0")

    label("loc_756")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7D0")

    label("loc_76F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7D0")

    label("loc_788")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7D0")

    label("loc_7A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7D0")

    label("loc_7BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7D0")

    label("loc_7E5")

    Return()

    # Function_2_669 end

    def Function_3_7E6(): pass

    label("Function_3_7E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_809")
    OP_8D(0xFE, -11560, -6690, -7260, -10580, 1000)
    Jump("Function_3_7E6")

    label("loc_809")

    Return()

    # Function_3_7E6 end

    def Function_4_80A(): pass

    label("Function_4_80A")

    Call(0, 5)
    Return()

    # Function_4_80A end

    def Function_5_80F(): pass

    label("Function_5_80F")

    TalkBegin(0xF)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    OP_A9(0xD8)
    Jump("loc_842")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_840")
    OP_A9(0xD7)
    Jump("loc_842")

    label("loc_840")

    OP_A9(0xD2)

    label("loc_842")

    TalkEnd(0xF)
    Return()

    label("loc_849")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85A")
    TalkEnd(0xF)
    Return()

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_973")

    ChrTalk(    #0
        0xF,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "Thanks to all the orbal energy going kaput,\x01",
            "the latest edition of the Liberl News is\x01",
            "only sold in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        (
            "Even so, the reporters and editors are incredible\x01",
            "for managing to get an issue out at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xF,
        "I gotta do my part and sell like crazy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A25")

    ChrTalk(    #4
        0xF,
        (
            "Today's all been talk about that crazy\x01",
            "incident ever since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xF,
        (
            "I'm glad they captured the rest of the\x01",
            "Intelligence Division before the signing\x01",
            "ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_B1F")

    ChrTalk(    #6
        0xF,
        (
            "Heya! I've got the latest edition of the\x01",
            "Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        "The feature's about the Ruan mayoral election.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        (
            "I can't read it on the job, but I can at least\x01",
            "check out the headlines. And let me tell you,\x01",
            "you don't wanna miss this one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCB")

    ChrTalk(    #9
        0xF,
        (
            "Seems like checking out the Bose Market\x01",
            "had a real impact on Kitty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        (
            "She said she was going to Bose\x01",
            "again on her next vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        "Could Kitty...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D43")

    ChrTalk(    #12
        0xF,
        (
            "The other day, we went to the Bose Market\x01",
            "to observe on the direction of the manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xF,
        (
            "Man, I was worried! I kept wondering if they'd\x01",
            "out me as someone in the same industry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xF,
        (
            "The manager just directly asked the people\x01",
            "at the stores about their prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xF,
        (
            "Seems like her hearty attitude really endeared\x01",
            "her to the head of the Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_DCA")

    label("loc_D43")


    ChrTalk(    #16
        0xF,
        (
            "It seems like the manager and the head\x01",
            "of the Bose Market really got along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xF,
        (
            "So now they're going to cooperate\x01",
            "and swap info.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCA")

    Jump("loc_E2F")

    label("loc_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E2F")

    ChrTalk(    #18
        0xF,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "The Edel Department Store has everything\x01",
            "from souvenirs to daily goods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2F")

    TalkEnd(0xF)
    Return()

    # Function_5_80F end

    def Function_6_E33(): pass

    label("Function_6_E33")

    Call(0, 7)
    Return()

    # Function_6_E33 end

    def Function_7_E38(): pass

    label("Function_7_E38")

    TalkBegin(0x10)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E55")
    OP_A9(0xD3)
    TalkEnd(0x10)
    Return()

    label("loc_E55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E66")
    TalkEnd(0x10)
    Return()

    label("loc_E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EE9")

    ChrTalk(    #20
        0x10,
        "Our manager's pretty reliable, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "I can see why she says, 'If I were\x01",
            "on a glacier, I could even sell ice.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_FBF")

    ChrTalk(    #22
        0x10,
        (
            "Colonel Richard was very popular with\x01",
            "the citizenry. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "I can understand why the folks in the\x01",
            "Intelligence Division would be willing to\x01",
            "do anything for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "But come on, no tanks, seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_105F")

    ChrTalk(    #25
        0x10,
        (
            "Sounds like Ruan's new mayor has\x01",
            "been decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "That should make all kinds of deals easier,\x01",
            "hopefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "I hope the new mayor works hard.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FB")

    ChrTalk(    #28
        0x10,
        (
            "Oh, yeah, is that weird rumor I heard from\x01",
            "a customer true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "Rumor had it there was a ghost appearing\x01",
            "all over Ruan, or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_10FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_11EA")

    ChrTalk(    #30
        0x10,
        "I hope that Ruan picks its new mayor soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "Ever since the thing with Mayor Dalmore,\x01",
            "distribution with Ruan's been a bit of a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "There's a lot of procedures that need mayoral\x01",
            "approval, so I guess it makes sense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1249")

    label("loc_11EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1249")

    ChrTalk(    #33
        0x10,
        "Welcome. You guys tourists?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "I've got lots of good souvenirs at niiice prices.\x02",
    )

    CloseMessageWindow()

    label("loc_1249")

    TalkEnd(0x10)
    Return()

    # Function_7_E38 end

    def Function_8_124D(): pass

    label("Function_8_124D")

    Call(0, 9)
    Return()

    # Function_8_124D end

    def Function_9_1252(): pass

    label("Function_9_1252")

    TalkBegin(0x11)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126F")
    OP_A9(0xD4)
    TalkEnd(0x11)
    Return()

    label("loc_126F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1280")
    TalkEnd(0x11)
    Return()

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1377")

    ChrTalk(    #35
        0x11,
        (
            "My sister who was heading to Bose\x01",
            "is apparently in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "*siiigh* Thank goodness... She's safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "I-I wasn't worried or anything!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "I'm going to challenge her head on and win\x01",
            "the position of tea sales staff, after all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A04")

    label("loc_1377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_14E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1468")

    ChrTalk(    #39
        0x11,
        (
            "My sister apparently went off to Bose\x01",
            "to study in order to open her own shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "At this rate, she might quit the\x01",
            "department store, she said...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "Sis, please don't leave me behind.\x01",
            "I'm looooooonely...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_14DE")

    label("loc_1468")


    ChrTalk(    #43
        0x11,
        (
            "At this rate, she might quit the department\x01",
            "store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "Sis, please don't leave me behind.\x01",
            "I'm looooooonely...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DE")

    Jump("loc_1A04")

    label("loc_14E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_15AE")

    ChrTalk(    #45
        0x11,
        "Heeheehee... It's come... It's finally come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        (
            "While my sister is on leave\x01",
            "I'm the new tea sales staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "Just you watch! At this rate I'll take the\x01",
            "position right out from under her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A04")

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1665")

    ChrTalk(    #48
        0x11,
        (
            "Lately, my sister's been spending\x01",
            "a lot of time in thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        "Just you watch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x11,
        (
            "While she's spacing out I'll kick her\x01",
            "off of the throne of tea sales staff!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A04")

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E3")

    ChrTalk(    #51
        0x11,
        (
            "Thinking about it, my sister's always\x01",
            "been treated the best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "It was always me who had to get the\x01",
            "paper in the morning because she had\x01",
            "low blood pressure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x11,
        (
            "It was always my job to kill the cockroaches\x01",
            "because she was a coward!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "Why was it always me that got fat when we\x01",
            "ate the same snacks when we're twins?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        "None of these are forgivable!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1865")

    label("loc_17E3")


    ChrTalk(    #56
        0x11,
        "Just you watch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        (
            "At the very least I'm going to make sure you\x01",
            "return the position of tea sales staff you\x01",
            "took from me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1865")

    Jump("loc_1A04")

    label("loc_1868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1981")

    ChrTalk(    #58
        0x11,
        "Er, the golden rule to making the best tea is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "...I always get sleepy when it comes to anything\x01",
            "with the name 'studying' attached to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x11,
        "Ah, no, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        (
            "All this effort is to reclaim the position of tea\x01",
            "sales staff my sister stole from me!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1A04")

    label("loc_1981")


    ChrTalk(    #62
        0x11,
        "Gwaah! I'm NOT gonna fall asleep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "All this effort is to reclaim the position of tea\x01",
            "sales staff my sister stole from me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A04")

    TalkEnd(0x11)
    Return()

    # Function_9_1252 end

    def Function_10_1A08(): pass

    label("Function_10_1A08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B37")

    ChrTalk(    #64
        0xFE,
        (
            "If we're not gonna get anything to sell coming to\x01",
            "us, we'll have to get our stock to sell ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "Sell anything you can at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "After all, our customers surely want products.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Even if there's things we can't do anything about,\x01",
            "we'll do the heck out of what we can do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1C21")

    ChrTalk(    #68
        0xFE,
        (
            "My house is in the West Block, so I heard\x01",
            "crazy loud noises from the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Even I was shocked to hear it was an Intelligence\x01",
            "Division tank, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I'm glad my house wasn't crushed\x01",
            "by something like that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1D05")

    ChrTalk(    #71
        0xFE,
        (
            "I've seen that girl who just left\x01",
            "around quite a bit recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "She seems to be a tourist, but I\x01",
            "wonder where her parents are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "There's a number of kids who get lost\x01",
            "in this store, so I'm a bit worried...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D79")

    ChrTalk(    #74
        0xFE,
        (
            "I'm very sorry, but our store will be\x01",
            "closing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "We eagerly await your future patronage!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1E63")

    ChrTalk(    #76
        0xFE,
        "In this season sales always take a dive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "So I'm definitely not missing out on using a big\x01",
            "event like the signing ceremony to boost our\x01",
            "intake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "All right, we're gonna hold a big ol' pact\x01",
            "signing memorial sale!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1EDC")

    ChrTalk(    #79
        0xFE,
        "Welcome, welcome to the Edel Department Store.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Our store is ever striving to take down\x01",
            "the Bose Market!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDC")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A08 end

    def Function_11_1EE0(): pass

    label("Function_11_1EE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1F54")

    ChrTalk(    #81
        0xFE,
        "I've got some time off starting tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I'll be leaving the tea corner to my\x01",
            "sister Midee.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_1F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(    #83
        0xFE,
        (
            "I learned a lot from getting to see the\x01",
            "Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Not just that, but I've found something\x01",
            "I want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "I can't tell my sister Midee yet, though...\x02",
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_20CA")

    ChrTalk(    #86
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Good customers, would you like some\x01",
            "delicious tea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "If you want to know how to make delicious tea,\x01",
            "I'd be glad to teach you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Please, don't hesitate to ask.\x02",
    )

    CloseMessageWindow()
    Jump("loc_216F")

    label("loc_20CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_216F")

    ChrTalk(    #90
        0xFE,
        (
            "The other day, everyone in the store went\x01",
            "to see the famous Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Everyone in the market was working so hard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "It was touching to see.\x02",
    )

    CloseMessageWindow()

    label("loc_216F")

    TalkEnd(0xFE)
    Return()

    # Function_11_1EE0 end

    def Function_12_2173(): pass

    label("Function_12_2173")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2254")

    ChrTalk(    #93
        0xFE,
        (
            "Lately, we haven't been getting our fish from\x01",
            "Ruan but from the Fisherman's Guild, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I thought they were purely a hobbyist group,\x01",
            "but with orbments dead it seems they're really\x01",
            "stepping up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A8")

    label("loc_2254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_22F6")

    ChrTalk(    #95
        0xFE,
        "The town's kinda noisy. Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Lately I've been so busy with my family that\x01",
            "I haven't paid much attention to current events...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A8")

    label("loc_22F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2374")

    ChrTalk(    #97
        0xFE,
        (
            "I'd like to get some seafood from Ruan.\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Lately, there's not much of it sold even here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A8")

    label("loc_2374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23CB")

    ChrTalk(    #99
        0xFE,
        (
            "Hmm, I'm late in getting in today,\x01",
            "so there's not much good left...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A8")

    label("loc_23CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_241B")

    ChrTalk(    #100
        0xFE,
        (
            "I need to get my family to eat some\x01",
            "vegetables for their health.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A8")

    label("loc_241B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_24A8")

    ChrTalk(    #101
        0xFE,
        (
            "Seems like there've been earthquakes\x01",
            "happening in Zeiss lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I haven't gone in a while, but\x01",
            "are Elmo's hot springs okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A8")

    TalkEnd(0xFE)
    Return()

    # Function_12_2173 end

    def Function_13_24AC(): pass

    label("Function_13_24AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2512")

    ChrTalk(    #103
        0xFE,
        (
            "Forget about pots and plates!\x01",
            "We need to secure food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "This is gettin' serious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_2512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_25F0")

    ChrTalk(    #105
        0xFE,
        (
            "Last night, I saw some of the Royal Guard\x01",
            "running off to the West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I also heard what sounded like a big cannon\x01",
            "from the port. I wonder what that was about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "It was k-kinda violent sounding...\x02",
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_25F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_269F")

    ChrTalk(    #108
        0xFE,
        "Hmm? Seems like you're in a hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Maybe I shouldn't be sayin' this since I'm just\x01",
            "a customer, but take care not to pull the plates\x01",
            "and pots out too fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_269F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2705")

    ChrTalk(    #110
        0xFE,
        "Already evening, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I gotta get home soon or my wife's\x01",
            "gonna chew me out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_2705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2765")

    ChrTalk(    #112
        0xFE,
        (
            "Oh, so this pot's from the Imperial middle ages,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "...It's a good pot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_2765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_287F")

    ChrTalk(    #114
        0xFE,
        (
            "One of the heads of the coup d'etat, Duke Dunan,\x01",
            "seems to be under house arrest by orders of the\x01",
            "queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "A person who's apparently the duke's butler\x01",
            "comes and shops here at the store from time\x01",
            "to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "But for some reason he always just\x01",
            "buys donuts and comics.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287F")

    TalkEnd(0xFE)
    Return()

    # Function_13_24AC end

    def Function_14_2883(): pass

    label("Function_14_2883")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2903")

    ChrTalk(    #117
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I couldn't find any good wife candidates\x01",
            "for my son, ultimately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "How terribly frustrating...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2A14")

    ChrTalk(    #120
        0xFE,
        (
            "I've searched all over for a good girl to\x01",
            "be my son's wife, but I got nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "It's got a lot of people, as you'd expect from\x01",
            "the capital, but they're all such superficial\x01",
            "girls. I don't like any of 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "I guess it might be time to give up here...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B12")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #123
        0xFE,
        "... You. I think I know you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1015F(Er... yeah, we have met.)\x02\x03",

            "(...Who the heck is she again?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I've been looking for a girl for months now,\x01",
            "so I don't remember every girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "I'm not just drawing a blank, all right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2BC2")

    ChrTalk(    #127
        0xFE,
        (
            "I came to the capital to look for\x01",
            "a wife candidate for my son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "If you know any good girls,\x01",
            "introduce them to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "I can't find any really good girls...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2C1C")

    ChrTalk(    #130
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I'm tired from walking around, so\x01",
            "I'm going to take a break here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1C")

    TalkEnd(0xFE)
    Return()

    # Function_14_2883 end

    def Function_15_2C20(): pass

    label("Function_15_2C20")

    Call(0, 16)
    Return()

    # Function_15_2C20 end

    def Function_16_2C25(): pass

    label("Function_16_2C25")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C7F"),
        (1, "loc_34A8"),
        (SWITCH_DEFAULT, "loc_34DD"),
    )


    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D7C")

    ChrTalk(    #132
        0x8,
        (
            "For a while, this place was packed with\x01",
            "people, but thanks to the queen they seem\x01",
            "to have calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "Just a bit ago I heard something\x01",
            "similar happened in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "To think it's this nerve-racking\x01",
            "being unable to use orbments...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_2D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2E0B")

    ChrTalk(    #135
        0x8,
        (
            "Hearing about the Intelligence Division always\x01",
            "puts me on edge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "Thanks to them, our company and\x01",
            "I suffered severe damages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_2E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_2ED0")

    ChrTalk(    #137
        0x8,
        (
            "Oh, seems like the Linde and the factory\x01",
            "ship have come into port on schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "Ahhh, it's so wonderful to be\x01",
            "able to do work on schedule!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        "This is how everything should be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_2ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2F67")

    ChrTalk(    #140
        0x8,
        (
            "I got word that they'll be using the second\x01",
            "lane reserved for the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "I need to get the staff to check the lane\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_2F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_308F")

    ChrTalk(    #142
        0x8,
        "One, two, three...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "Er, that should be all the logs\x01",
            "from the indicated time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        (
            "I was asked by the Bracer Guild\x01",
            "to give them passenger logs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        (
            "They're generally quite helpful to us, so it's\x01",
            "only natural I offer them at least this much\x01",
            "help with their investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_308F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_317E")

    ChrTalk(    #146
        0x8,
        "It was pretty insane after the coup d'etat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "We had to deal with cleaning up after the fact,\x01",
            "and also re-normalize operation of the liners...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "Just remembering day after day of leftover\x01",
            "work brings tears to my eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_317E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3283")

    ChrTalk(    #149
        0x8,
        (
            "Lately, all the airships have been\x01",
            "running according to schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "During the coup d'etat things were messed up\x01",
            "with the coming and going of military ships and\x01",
            "the closing of the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        "I'm finally free of dealing with claimants.\x02",
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_3283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_33C3")

    ChrTalk(    #152
        0x8,
        (
            "One thing I'd wish for right now is for people\x01",
            "asking about the new engine to ask the developers\x01",
            "at the central factory, not the airship company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "The most we did was just store it temporarily\x01",
            "and do a bit of maintenance work on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "It seems like the foreign people don't\x01",
            "quite get that, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_33C3")

    OP_A2(0x0)

    ChrTalk(    #155
        0x8,
        "*sigh* Those people just now were so pushy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "I mean, it IS a sample of the engine going into\x01",
            "the high-speed cruiser Arseille, but sheesh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "I can understand them getting so\x01",
            "worked up, but it's not finished yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A5")

    Jump("loc_34E0")

    label("loc_34A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B9")
    OP_A9(0xD9)
    Jump("loc_34D8")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_34C5")
    OP_A9(0xD1)
    Jump("loc_34D8")

    label("loc_34C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D6")
    OP_A9(0xD0)
    Jump("loc_34D8")

    label("loc_34D6")

    OP_A9(0xCF)

    label("loc_34D8")

    OP_56(0x0)
    Jump("loc_34E0")

    label("loc_34DD")

    Jump("loc_34E0")

    label("loc_34E0")

    TalkEnd(0x8)
    Return()

    # Function_16_2C25 end

    def Function_17_34E4(): pass

    label("Function_17_34E4")

    Call(0, 18)
    Return()

    # Function_17_34E4 end

    def Function_18_34E9(): pass

    label("Function_18_34E9")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3550")

    ChrTalk(    #158
        0x9,
        "At the moment, we are reconsidering all flights.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        "We ask for your understanding.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_3550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_35BE")

    ChrTalk(    #160
        0x9,
        "The Linde just left port a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        (
            "Next will be the west-bound Cecilia\x01",
            "coming into port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_35BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_3640")

    ChrTalk(    #162
        0x9,
        (
            "At the moment, the factory ship\x01",
            "is occupying the second lane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        "Please be careful and do not mistake your lane.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_3640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_36D3")

    ChrTalk(    #164
        0x9,
        "The Linde will be arriving soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x9,
        (
            "Persons boarding are asked to check in at\x01",
            "the counter outside after purchasing their\x01",
            "tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_36D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_376E")

    ChrTalk(    #166
        0x9,
        "A bit ago a silver-haired bracer woman came by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "Apparently she was asking about the threat\x01",
            "letter addressed to the company.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37EA")

    label("loc_376E")


    ChrTalk(    #168
        0x9,
        "A bit ago a red-haired bracer came by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        (
            "Apparently he was asking about the threat\x01",
            "letter addressed to the company.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EA")

    Jump("loc_3DBD")

    label("loc_37ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_38A4")

    ChrTalk(    #170
        0x9,
        (
            "It's true the company's a bit troubled\x01",
            "after receiving that threat letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x9,
        (
            "I hope we don't end up with another situation\x01",
            "that causes trouble for our passengers...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_38A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_38E5")

    ChrTalk(    #172
        0x9,
        "Welcome! Welcome to the Liberl Orbalship Company.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_38E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_3960")

    ChrTalk(    #173
        0x9,
        (
            "Please hand your tickets to the receptionist\x01",
            "immediately outside the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        "You can check in there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DBD")

    label("loc_3960")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x9, 255)
    OP_8C(0x9, 180, 0)
    OP_6D(1800, 0, 64920, 0)
    SetChrPos(0xF7, 2190, 0, 63630, 0)
    SetChrPos(0x101, 1250, 0, 63630, 0)
    OP_0D()

    ChrTalk(    #175
        0x9,
        "#6PWelcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#6PWill you be using our national flights?\x01",
            "Or our international flights?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#6P#1006FEr, two tickets bound for Ruan, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "#6PUnderstood...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "#6POh, pardon me.\x01",
            "You are with the Bracer Guild, yes?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3BD5")

    ChrTalk(    #180
        0x9,
        "#6PAre you Estelle and Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#6P#1004FY-Yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#6PI have already received payment from\x01",
            "Elnan with the capital branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        "#6PHere are your tickets.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #184
        "\x07\x00Received two #1010i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F2, 2)

    ChrTalk(    #185
        0x101,
        "#6P#1011FI see, so Elnan did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x106,
        "#051FNice, Elnan. He's always ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D21")

    label("loc_3BD5")


    ChrTalk(    #187
        0x9,
        "#6PAre you Estelle and Scherazard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#6P#1004FY-Yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "#6PI have already received payment from\x01",
            "Elnan with the capital branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        "#6PHere are your tickets.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #191
        "\x07\x00Received two #1010i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F2, 2)

    ChrTalk(    #192
        0x101,
        "#6P#1011FI see, so Elnan did...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x103,
        (
            "#021FVery nice, Elnan.\x01",
            "Thoughtful as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D21")


    ChrTalk(    #194
        0x9,
        (
            "#6PWell then, please hand your tickets to the\x01",
            "receptionist immediately outside the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "#6PYou can check in for your flight there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1204)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    label("loc_3DBD")

    TalkEnd(0x9)
    Return()

    # Function_18_34E9 end

    def Function_19_3DC1(): pass

    label("Function_19_3DC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E65")

    ChrTalk(    #196
        0xA,
        "Ahh, it's all over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "The tour plan I put everything into's\x01",
            "worth nothing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xA,
        (
            "No one's gonna be traveling in these\x01",
            "circumstances, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3F35")

    ChrTalk(    #199
        0xA,
        (
            "It sure had my heart racing when those\x01",
            "Intelligence Division guys appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "If order is disrupted, it can make the\x01",
            "tourism drop like a rock, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        "I'm glad they were all caught.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_3F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3FEC")

    ChrTalk(    #202
        0xA,
        "Mmm, what should I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        (
            "It seems like the owner of the Anterose\x01",
            "is quite particular about his restaurant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "I can hardly ask for a discount for a tour,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_3FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408F")

    ChrTalk(    #205
        0xA,
        "This is a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "I've got a pretty detailed idea for a Bose tour,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "Adding the Anterose to the list\x01",
            "makes the prices shoot up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_408F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4177")

    ChrTalk(    #208
        0xA,
        (
            "I plan on opening a tour company\x01",
            "together with the airship company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "I proposed Bose for my first stop after visiting\x01",
            "it the other day, and the company approves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        "I'll be deciding the details of the tour now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4222")

    label("loc_4177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4222")

    ChrTalk(    #211
        0xA,
        (
            "The non-aggression pact should be a\x01",
            "big plus for the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "I want to call in all the foreign tourists now\x01",
            "that there's a non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4222")

    TalkEnd(0xFE)
    Return()

    # Function_19_3DC1 end

    def Function_20_4226(): pass

    label("Function_20_4226")

    TalkBegin(0xFE)

    ChrTalk(    #213
        0xFE,
        (
            "Those two just now...\x01",
            "They looked really deadly serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "It seems like they had a fairly high rank,\x01",
            "too. I wonder who they were.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4226 end

    def Function_21_42B8(): pass

    label("Function_21_42B8")

    TalkBegin(0xFE)

    ChrTalk(    #215
        0xFE,
        (
            "Th-That was scary...\x01",
            "Now I can buy my ticket.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_42B8 end

    def Function_22_42F2(): pass

    label("Function_22_42F2")

    TalkBegin(0xFE)

    ChrTalk(    #216
        0xFE,
        (
            "Oh, man. Screaming and fighting in\x01",
            "a place like this. How pathetic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "I wish people could be more well-mannered.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_42F2 end

    def Function_23_4374(): pass

    label("Function_23_4374")

    TalkBegin(0xFE)

    ChrTalk(    #218
        0xFE,
        (
            "仮\x01",
            "仮\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_4374 end

    def Function_24_4386(): pass

    label("Function_24_4386")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_43FD")

    ChrTalk(    #219
        0xFE,
        (
            "#050FIf you're here, does that mean you're\x01",
            "startin' with the embassies?\x02\x03",

            "#051FWell, countin' on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44B7")

    label("loc_43FD")


    ChrTalk(    #220
        0xFE,
        (
            "#052FEstelle, what is it?\x02\x03",

            "#050FI'm just about ta start askin' with the company.\x02\x03",

            "If you're here, does that mean you're\x01",
            "startin' with the embassies?\x02\x03",

            "#051FWell, countin' on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_44B7")

    TalkEnd(0xFE)
    Return()

    # Function_24_4386 end

    def Function_25_44BB(): pass

    label("Function_25_44BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4533")

    ChrTalk(    #221
        0xFE,
        (
            "#020FIf you're here, does that mean you're\x01",
            "starting with the embassies?\x02\x03",

            "Well, we're counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E5")

    label("loc_4533")


    ChrTalk(    #222
        0xFE,
        (
            "#023FOh, what is it?\x02\x03",

            "#020FI was just about to start asking with\x01",
            "the company.\x02\x03",

            "If you're here, does that mean you're\x01",
            "startin' with the embassies?\x02\x03",

            "Well, countin' on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_45E5")

    TalkEnd(0xFE)
    Return()

    # Function_25_44BB end

    def Function_26_45E9(): pass

    label("Function_26_45E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D1, 0)), scpexpr(EXPR_END)), "loc_4624")

    ChrTalk(    #223
        0xFE,
        "#560FWe'll keep shopping here for a bit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4707")

    label("loc_4624")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #224
        0xFE,
        "#560FOh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#1000FTita, take care of Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "#061FYeah, leave it to me.\x02\x03",

            "#560FI've got lotsa places I wanna go with Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        "#1000FJust don't get lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        "#061FOkay! Good luck with your work.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1688)

    label("loc_4707")

    TalkEnd(0xFE)
    Return()

    # Function_26_45E9 end

    def Function_27_470B(): pass

    label("Function_27_470B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 7)), scpexpr(EXPR_END)), "loc_4787")

    ChrTalk(    #229
        0xFE,
        (
            "#260FHmmm... Once we're done shopping\x01",
            "I'd like to go play someplace else, too.\x02\x03",

            "Show me all around, Tita.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A77")

    label("loc_4787")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #230
        0x101,
        "#1001FRenne, so this is where you were?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "#264FHi, Estelle.\x02\x03",

            "#265FHey, which stuffed animal do you like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1011FHmm... I think that rabbit's pretty cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "#260FReally?\x02\x03",

            "#261FWhat a coincidence! I think that\x01",
            "bunny's the cutest, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#1015F...Looking at these stuffed animals\x01",
            "reminds me of Anelace.\x02\x03",

            "I wonder what she's doing now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "#264FAnelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#1000FShe's a bracer like me, but she's a lady\x01",
            "who looooves stuffed animals.\x02\x03",

            "#1001FI'm sure you two would get along, Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "#264FWill I get to meet this lady?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#1000FShe's out of the capital on work right now,\x01",
            "but you might meet her at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "#265FWhen is some point? Tomorrow?\x01",
            "The day after?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#1013FEr... I'm not quite sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#267FAwww.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1687)

    label("loc_4A77")

    TalkEnd(0xFE)
    Return()

    # Function_27_470B end

    def Function_28_4A7B(): pass

    label("Function_28_4A7B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A8E")
    Call(0, 33)

    label("loc_4A8E")

    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1A, 1210, 0, 62900, 266)
    SetChrPos(0x1B, 800, 0, 62000, 270)
    SetChrPos(0x1C, -1180, 0, 62510, 90)
    SetChrPos(0x101, 200, 0, 54480, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-90, -20, 56890, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4B4F")
    SetChrPos(0x106, 1160, 0, 54550, 0)
    Jump("loc_4B60")

    label("loc_4B4F")

    SetChrPos(0x103, 1160, 0, 54550, 0)

    label("loc_4B60")

    FadeToBright(1000, 0)

    def lambda_4B6F():
        OP_8E(0x101, 0x1C2, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B6F)

    def lambda_4B8A():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B8A)
    Sleep(300)

    def lambda_4BA1():
        OP_8E(0xF7, 0x578, 0x0, 0xDBEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_4BA1)

    def lambda_4BBC():
        OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4BBC)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF7, 0x1)
    OP_0D()

    ChrTalk(    #242
        0x101,
        "#6P#1004FHuh? What's...?\x02",
    )

    CloseMessageWindow()

    def lambda_4BF7():
        OP_6D(1040, 0, 63300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4BF7)

    def lambda_4C0F():
        OP_67(0, 6990, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C0F)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    NpcTalk(    #243
        0x1C,
        "Bespectacled Woman",
        (
            "#1P#1112FReally, this is why I cannot stand\x01",
            "the pompous Imperial nobility...\x02\x03",

            "And I thought there were LIMITS to how\x01",
            "unpleasant a single person could be.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #244
        0x1B,
        "Middle-Aged Man",
        (
            "#4P#1101FHah! You took the words\x01",
            "right from my mouth.\x02\x03",

            "Tell me, why does the Republic even\x01",
            "care about the engine provision deal?\x02\x03",

            "I did not think Liberl's internal\x01",
            "politics were your plaything.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #245
        0x1C,
        "Bespectacled Woman",
        (
            "#1P#1111FIt's a matter of national--no,\x01",
            "international--security, of course.\x02\x03",

            "It's only been a decade since\x01",
            "Erebonia attempted\x01",
            "to annex this innocent little country.\x02\x03",

            "#1113FIt is absolutely unacceptable for a half-\x01",
            "barbaric nation like yours to lay their\x01",
            "hands on such cutting-edge technology.\x02\x03",

            "The Republic is a long-standing friend of\x01",
            "Liberl! We won't stand back and allow\x01",
            "something that will threaten its interests.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #246
        0x1B,
        "Middle-Aged Man",
        (
            "#4P#1103FLong-standing friend?!\x02\x03",

            "Some friends you are! You didn't send\x01",
            "them so much as a soldier in the war!\x02\x03",

            "You're just pretending to be allies\x01",
            "when it suits you, while standing back\x01",
            "and doing nothing when it doesn't!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #247
        0x1C,
        "Bespectacled Woman",
        "#1P#1114FWhat did you just--\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1B, 400)

    ChrTalk(    #248
        0x1A,
        (
            "#272F#6PMy Lord Ambassador Crainagh...\x01",
            "may I suggest we leave the matter here?\x02\x03",

            "We do not wish to bother\x01",
            "the other customers.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 0, 400)

    ChrTalk(    #249
        0x1B,
        "#1101FBut, Mueller! We...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1A, 266, 400)

    ChrTalk(    #250
        0x1A,
        (
            "#270F#6PAmbassador Cochrane, may I ask\x01",
            "that you back down as well?\x02\x03",

            "This is a...debate...that could be handled\x01",
            "just as well through the embassies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1C,
        (
            "#1P#1113F...Very well.\x02\x03",

            "I can't say I like hearing that from\x01",
            "a member of the Imperial military.\x02\x03",

            "#1111FStill, far better than hearing it from\x01",
            "that pompous--and gluttonous--member\x01",
            "of the 'nobility,' I suppose.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)

    ChrTalk(    #252
        0x1B,
        "#1103F#4PWHAT DID YOU J--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x1C,
        "#1P#1113FWell, gentlemen, if you'll pardon me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1C, 180, 400)

    def lambda_5320():
        OP_8E(0x1C, 0xFFFFFCE0, 0x0, 0xD5A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_5320)

    def lambda_533B():
        OP_6D(670, 0, 59460, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_533B)

    def lambda_5353():
        OP_67(0, 6990, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_5353)

    def lambda_536B():

        label("loc_536B")

        TurnDirection(0x1B, 0x1C, 0)
        OP_48()
        Jump("loc_536B")

    QueueWorkItem2(0x1B, 1, lambda_536B)

    def lambda_537C():

        label("loc_537C")

        TurnDirection(0x1A, 0x1C, 0)
        OP_48()
        Jump("loc_537C")

    QueueWorkItem2(0x1A, 1, lambda_537C)

    def lambda_538D():

        label("loc_538D")

        TurnDirection(0x101, 0x1C, 0)
        OP_48()
        Jump("loc_538D")

    QueueWorkItem2(0x101, 2, lambda_538D)

    def lambda_539E():

        label("loc_539E")

        TurnDirection(0xF7, 0x1C, 0)
        OP_48()
        Jump("loc_539E")

    QueueWorkItem2(0xF7, 2, lambda_539E)
    Sleep(3500)

    def lambda_53B4():
        OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_53B4)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x1C, 0x1)
    SetChrFlags(0x1C, 0x80)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    WaitChrThread(0x1A, 0x2)
    WaitChrThread(0x1A, 0x3)
    Sleep(1000)

    ChrTalk(    #254
        0x1B,
        (
            "#1101F#6PThat insufferable she-wolf!\x02\x03",

            "This is why commoners with\x01",
            "no history or tradition are--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1B, 400)

    ChrTalk(    #255
        0x1A,
        "#272F#3PMy lord...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1B, 270, 400)
    OP_8C(0x1B, 0, 400)

    ChrTalk(    #256
        0x1B,
        (
            "#1102F#6P...Hrmph, yes, yes.\x02\x03",

            "#1100FI shall return to the embassy. I trust I can\x01",
            "leave the other matter in your hands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x1A,
        "#270F#3PAs you will, my lord.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)
    TurnDirection(0xF7, 0x1B, 400)

    def lambda_5532():

        label("loc_5532")

        TurnDirection(0x1A, 0x1B, 0)
        OP_48()
        Jump("loc_5532")

    QueueWorkItem2(0x1A, 1, lambda_5532)
    OP_43(0x1B, 0x1, 0x0, 0x1D)
    Sleep(1000)

    def lambda_554F():
        OP_6D(1830, 0, 62950, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_554F)

    def lambda_5567():
        OP_67(0, 6150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_5567)
    OP_43(0x101, 0x1, 0x0, 0x1E)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x1F)
    WaitChrThread(0xF7, 0x1)
    OP_44(0x1A, 0x1)

    def lambda_559B():
        TurnDirection(0x101, 0x1A, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_559B)

    def lambda_55A9():
        TurnDirection(0xF7, 0x1A, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55A9)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x1A, 0x2)
    WaitChrThread(0x1A, 0x3)

    ChrTalk(    #258
        0x101,
        "#1011F#2PUm, hiya!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5683")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Olivier Capture Event to Uncleared\x01",      # 0
            "Set Olivier Capture event to Cleared\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_566A"),
        (1, "loc_5672"),
        (SWITCH_DEFAULT, "loc_567A"),
    )


    label("loc_566A")

    OP_28(0x55, 0x3, 0x10)
    Jump("loc_567A")

    label("loc_5672")

    OP_28(0x55, 0x4, 0x10)
    Jump("loc_567A")

    label("loc_567A")

    FadeToBright(300, 0)

    label("loc_5683")

    OP_62(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x55, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571C")

    ChrTalk(    #259
        0x1A,
        (
            "#273F#3PHm? Ah... Estelle, yes?\x02\x03",

            "#277FIt's been some time--since the\x01",
            "Martial Arts Competition, I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5793")

    label("loc_571C")


    ChrTalk(    #260
        0x1A,
        (
            "#273F#3PHm? Ah... Estelle, yes?\x02\x03",

            "#277FIt's been some time--since your, ah,\x01",
            "'help' during the festival, I believe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5793")


    ChrTalk(    #261
        0x101,
        (
            "#1016F#2PHaha! I'm glad you remember.\x02\x03",

            "#1011FThat was one heck of an\x01",
            "argument just now, though.\x02\x03",

            "Who were those two, and why were they\x01",
            "going at each other like a cat and dog?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x1A,
        (
            "#277F#3PThe man was the ambassador of the Erebonian\x01",
            "Empire to Liberl, Lord Davil Crainagh.\x02\x03",

            "The woman would be the ambassador from\x01",
            "the Republic of Calvard, Elsa Cochrane.\x02\x03",

            "They head up their respective\x01",
            "embassies here in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        "#1004F#2POh, I see.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_59D2")

    ChrTalk(    #264
        0x106,
        (
            "#551F#4PAwful damn childish for a\x01",
            "couple of ambassadors.\x02\x03",

            "Can those two really do their jobs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        "#1019F#2PAgate...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A7C")

    label("loc_59D2")


    ChrTalk(    #266
        0x103,
        (
            "#027F#4PSo those are the 'great'\x01",
            "ambassadors, hmm?\x02\x03",

            "How do a pair of whiny children\x01",
            "like those two manage diplomatic\x01",
            "negotiations, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1019F#2PSchera...\x02",
    )

    CloseMessageWindow()

    label("loc_5A7C")


    ChrTalk(    #268
        0x1A,
        (
            "#276F#3PI wish I could disagree, honestly.\x02\x03",

            "#272FTo say that the Empire and the Republic\x01",
            "have always been on 'bad' terms would be\x01",
            "an understatement at the best of times.\x02\x03",

            "And on top of that, those two are like\x01",
            "oil and water on a personal level.\x02\x03",

            "#277FWell... No, the fact that they break into\x01",
            "an argument every time they meet shows\x01",
            "how similar they are, in some ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1016F#2PHaha... I guess I can see that.\x02\x03",

            "#1015FThough, maybe it's 'cause I walked\x01",
            "into the middle of the conversation, but\x01",
            "I couldn't understand, like, half of that.\x02\x03",

            "Something about engine provision\x01",
            "and Liberl's internal politics...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x1A,
        "#270F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#1025F#2PEr, sorry, I guess I shouldn't ask.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1A,
        (
            "#272F#3PNo, I don't mind.\x01",
            "It's not really a secret, anyway.\x02\x03",

            "#277FThe engine in question is actually the\x01",
            "latest from your own central factory.\x02\x03",

            "Once the design is finalized, sample units\x01",
            "are to be provided by your airship company\x01",
            "to the Empire and Republic both. But...\x02\x03",

            "We...er, bumped into Ambassador Cochrane\x01",
            "when we came by to finalize the details of\x01",
            "the deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        (
            "#1000F#2POh, I get it.\x02\x03",

            "#1015FWhy the big argument about\x01",
            "an engine, then?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5F9F")

    ChrTalk(    #274
        0x106,
        (
            "#555F#4PAn orbalship's engine is what determines\x01",
            "what a ship can really do.\x02\x03",

            "Since you can install 'em in\x01",
            "military ships, you usually don't\x01",
            "just hand 'em out like candy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6065")

    label("loc_5F9F")


    ChrTalk(    #275
        0x103,
        (
            "#026F#4PThe capabilities of an orbal engine directly\x01",
            "determine how powerful the ship in question is.\x02\x03",

            "#020FSince such an engine can be installed in a\x01",
            "military ship, I can see why they'd argue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6065")


    ChrTalk(    #276
        0x101,
        (
            "#1002F#2PNow I get it...\x02\x03",

            "#1007FIt'd be a real mess if that engine let\x01",
            "the Imperial Army get all powered up...\x02\x03",

            "#1008FEr, well, I mean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1A,
        (
            "#272F#3PNot at all. It's true.\x02\x03",

            "#277FNormally, sharing such advanced technology with\x01",
            "other countries so freely would be unthinkable,\x01",
            "but this is a part of your queen's plan.\x02\x03",

            "Rather than monopolizing a technological\x01",
            "edge, she wishes to provide it to other\x01",
            "countries to promote multinational peace.\x02\x03",

            "At least, that's her plan as I understand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#1011F#2PI get it... She did mention something\x01",
            "like that a while ago, now that I think\x01",
            "about it.\x02\x03",

            "#1001FIt's pretty incredible that the\x01",
            "queen is willing to try something\x01",
            "like that.\x02\x03",

            "Like, it's not just an ideal, you know?\x01",
            "It's something that could really change\x01",
            "how people negotiate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1A,
        (
            "#272F#3PYes, you have reason to be\x01",
            "proud of your queen, I'd say.\x02\x03",

            "#277F...My apologies, but this conversation\x01",
            "has gone on longer than I'd intended.\x02\x03",

            "You're here for air tickets, yes?\x01",
            "I'll pardon myself here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1004F#2POh, yeah.\x02\x03",

            "#1015FSay, Mueller. About Olivier...\x02\x03",

            "Has he gone back to Erebonia already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x1A,
        "#273F#3PWhat, you've not heard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        (
            "#1007F#2PI haven't really had a chance to see him\x01",
            "since the queen's birthday celebrations,\x01",
            "actually.\x02\x03",

            "I felt kinda bad about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x1A,
        (
            "#277F#3POh, don't worry. That halfwit is continuing\x01",
            "to while away his days here in Liberl.\x02\x03",

            "He said he was going to visit Elmo's\x01",
            "springs, if I remember right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_665C")

    ChrTalk(    #284
        0x101,
        (
            "#1008F#2POkay, then.\x02\x03",

            "#1012FHaha... Yeah, that sounds like\x01",
            "Olivier, all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_669D")

    label("loc_665C")


    ChrTalk(    #285
        0x101,
        "#1008F#2POkay, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x103,
        "#027F#4P...How very like Olivier.\x02",
    )

    CloseMessageWindow()

    label("loc_669D")


    ChrTalk(    #287
        0x1A,
        (
            "#277F#3PShould he ever bother returning to the embassy\x01",
            "like a responsible citizen, unlikely as that is,\x01",
            "I'll let him know you were asking after him.\x02\x03",

            "I'll make sure he at least contacts you\x01",
            "before he returns to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        "#1017F#2PThanks, Mueller.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_67CE")

    ChrTalk(    #289
        0x103,
        "#021F#4PThank you, sir knight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_67CE")

    label("loc_67CE")


    ChrTalk(    #290
        0x1A,
        (
            "#277F#3PHardly. I should thank you for\x01",
            "keeping that lunatic company.\x02\x03",

            "Now, if you'll excuse me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6839():
        OP_6D(670, 0, 59460, 2500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_6839)

    def lambda_6851():
        OP_67(0, 6990, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_6851)

    def lambda_6869():
        OP_8E(0x1A, 0xFFFFFC54, 0x0, 0xEF74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6869)

    def lambda_6884():

        label("loc_6884")

        TurnDirection(0x101, 0x1A, 0)
        OP_48()
        Jump("loc_6884")

    QueueWorkItem2(0x101, 1, lambda_6884)

    def lambda_6895():

        label("loc_6895")

        TurnDirection(0xF7, 0x1A, 0)
        OP_48()
        Jump("loc_6895")

    QueueWorkItem2(0xF7, 1, lambda_6895)
    WaitChrThread(0x1A, 0x1)

    def lambda_68AB():
        OP_8E(0x1A, 0xFFFFFCB8, 0x0, 0xD4E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_68AB)
    Sleep(1900)

    def lambda_68CB():
        OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_68CB)
    Sleep(400)
    WaitChrThread(0x1A, 0x1)
    SetChrFlags(0x1A, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    WaitChrThread(0xF7, 0x2)
    WaitChrThread(0xF7, 0x3)

    def lambda_68FE():
        OP_6D(1360, 0, 61620, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_68FE)

    def lambda_6916():
        OP_67(0, 6990, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6916)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6D10")
    OP_8C(0x106, 280, 500)

    ChrTalk(    #291
        0x106,
        (
            "#555F#4PThat's one hell of a stiff military type\x01",
            "for a friend of that golden-haired guy.\x02\x03",

            "Who is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#1006F#3PMueller's the resident military officer\x01",
            "for the Erebonian embassy, I think.\x02\x03",

            "I've only ever met him a few times myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x106,
        (
            "#552F#4PHrm... Well built and he made sure\x01",
            "to not leave himself open at any\x01",
            "point in our 'chat.'\x02\x03",

            "A well-trained dog of the military...\x01",
            "and hiding some sharp fangs, to boot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#1007F#3PThere you go again...\x02\x03",

            "#1015FHe...does seem like he's\x01",
            "really strong, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x106,
        (
            "#057F#4PTch. I don't trust any Imperials,\x01",
            "and that includes blondie.\x02\x03",

            "It seems like he talked to\x01",
            "Cassius about something...\x02\x03",

            "But who knows what his plan\x01",
            "is, what with staying so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        (
            "#1015F#3PI guess that's a good point.\x02\x03",

            "#1011FAlthough...Olivier may be weird, but\x01",
            "I can't think of him as a bad guy...\x02\x03",

            "Even Mueller doesn't seem all\x01",
            "that...malevolent, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x106,
        (
            "#053F#4PTch. Yeah, whatever.\x02\x03",

            "#050FLet's get over to the counter\x01",
            "and get our tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71B6")

    label("loc_6D10")

    OP_8C(0x103, 280, 500)

    ChrTalk(    #298
        0x103,
        (
            "#021F#4PWhat a serious fellow\x01",
            "for a friend of Olivier's.\x02\x03",

            "#020FHe's obviously an Imperial Army man,\x01",
            "but I wonder what his story is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#1006F#3PMueller's the resident military officer\x01",
            "for the Erebonian embassy, I think.\x02\x03",

            "I've only ever met him a few times myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x103,
        (
            "#027F#4PHmmmm. He's young, but he's got a\x01",
            "strong, manly face--very handsome.\x02\x03",

            "#021FI'd love to share a bottle of wine\x01",
            "or three with him sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1007F#3PHey, let's avoid an international\x01",
            "incident, okay?\x02\x03",

            "#1011FOh, speaking of international disasters,\x01",
            "did you meet up with Olivier after I left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x103,
        (
            "#020F#4PMm-hmm. I saw him a number\x01",
            "of times in the capital.\x02\x03",

            "Come to think of it, he did invite\x01",
            "me to the Elmo springs at one\x01",
            "point, but I had to decline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x101,
        (
            "#1004F#3PWHAAA?!\x02\x03",

            "#1013FYou mean, I, he, he invited you?\x01",
            "Like, INVITED you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x103,
        (
            "#027F#4PWith him, it's impossible to tell.\x02\x03",

            "#021FI was too busy this month to\x01",
            "entertain the idea, anyway.\x02\x03",

            "Normally, I'd have happily abused his\x01",
            "wallet for my lodging costs and kept\x01",
            "him up all night...drinking, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        (
            "#1016F#3PHaha...haaaa... Oh, Olivier, I think\x01",
            "you dodged a bullet, actually...\x02\x03",

            "#1006FAnyway! Let's go get our\x01",
            "tickets at the counter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71B6")

    OP_A2(0x1203)
    EventEnd(0x0)
    Return()

    # Function_28_4A7B end

    def Function_29_71BC(): pass

    label("Function_29_71BC")

    OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xEB3C, 0x7D0, 0x0)

    def lambda_71D6():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0xD57A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_71D6)
    Sleep(2500)

    def lambda_71F6():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_71F6)
    Sleep(400)
    WaitChrThread(0x1B, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_71BC end

    def Function_30_7212(): pass

    label("Function_30_7212")

    OP_8E(0x101, 0x23A, 0x0, 0xEF06, 0x7D0, 0x0)
    Return()

    # Function_30_7212 end

    def Function_31_7227(): pass

    label("Function_31_7227")

    OP_8E(0xF7, 0x5DC, 0x0, 0xED30, 0x7D0, 0x0)
    Return()

    # Function_31_7227 end

    def Function_32_723C(): pass

    label("Function_32_723C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7253")
    Call(0, 33)
    Call(0, 34)

    label("loc_7253")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_726B"),
        (101, "loc_72EF"),
        (102, "loc_7373"),
        (103, "loc_73F7"),
        (SWITCH_DEFAULT, "loc_747B"),
    )


    label("loc_726B")

    SetChrPos(0x101, -9240, 0, 440, 90)
    SetChrPos(0x107, -9330, 0, -480, 90)
    SetChrPos(0xF7, -10150, 0, -550, 90)
    SetChrPos(0xF9, -10150, 0, 520, 90)
    OP_6D(-9640, 0, 0, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_747B")

    label("loc_72EF")

    SetChrPos(0x101, 440, 0, 6410, 180)
    SetChrPos(0x107, -480, 0, 6500, 180)
    SetChrPos(0xF7, 550, 0, 7320, 180)
    SetChrPos(0xF9, -520, 0, 7320, 180)
    OP_6D(0, 0, 6810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_747B")

    label("loc_7373")

    SetChrPos(0x101, 8570, 0, -480, 270)
    SetChrPos(0x107, 8660, 0, 440, 270)
    SetChrPos(0xF7, 9480, 0, 550, 270)
    SetChrPos(0xF9, 9480, 0, -520, 270)
    OP_6D(8970, 0, 0, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_747B")

    label("loc_73F7")

    SetChrPos(0x101, -480, 0, -7240, 0)
    SetChrPos(0x107, 440, 0, -7330, 0)
    SetChrPos(0xF7, -520, 0, -8150, 0)
    SetChrPos(0xF9, 550, 0, -8150, 0)
    OP_6D(0, 0, -7640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_747B")

    label("loc_747B")

    SetChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #306
        0x101,
        "#1004FHey!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_74D3"),
        (101, "loc_7560"),
        (102, "loc_75E2"),
        (103, "loc_7690"),
        (SWITCH_DEFAULT, "loc_771D"),
    )


    label("loc_74D3")

    SetChrPos(0x1D, 4530, 0, -10, 90)

    def lambda_74EA():
        OP_6D(9530, 0, 0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74EA)
    OP_8E(0x1D, 0x253A, 0x0, 0xFFFFFFF6, 0x7D0, 0x0)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    Sleep(1000)
    OP_8E(0x1D, 0x30CA, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    SetChrFlags(0x1D, 0x80)
    Fade(500)
    OP_6D(-9640, 0, 0, 0)
    OP_0D()
    Jump("loc_771D")

    label("loc_7560")

    SetChrPos(0x1D, 0, 0, -3700, 180)

    def lambda_7577():
        OP_6D(0, 0, -8200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7577)
    OP_8E(0x1D, 0x0, 0x0, 0xFFFFDAE4, 0x7D0, 0x0)

    def lambda_75A3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_75A3)
    OP_8E(0x1D, 0x0, 0x0, 0xFFFFD6FC, 0x7D0, 0x0)
    SetChrFlags(0x1D, 0x80)
    Fade(1000)
    OP_6D(0, 0, 6810, 0)
    OP_0D()
    Jump("loc_771D")

    label("loc_75E2")

    SetChrPos(0x1D, -5200, 0, 0, 90)

    def lambda_75F9():
        OP_6D(-10200, 0, 0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75F9)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8E(0x1D, 0xFFFFD31E, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_7651():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7651)
    OP_8E(0x1D, 0xFFFFCF36, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0x1D, 0x80)
    Fade(1000)
    OP_6D(8970, 0, 0, 0)
    OP_0D()
    Jump("loc_771D")

    label("loc_7690")

    SetChrPos(0x1D, 0, 0, 2870, 0)

    def lambda_76A7():
        OP_6D(0, 0, 7370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76A7)
    OP_8E(0x1D, 0x0, 0x0, 0x1CCA, 0x7D0, 0x0)
    Sleep(500)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    Sleep(1000)
    OP_8E(0x1D, 0x0, 0x0, 0x28FA, 0x7D0, 0x0)
    SetChrFlags(0x1D, 0x80)
    Fade(1000)
    OP_6D(0, 0, -7640, 0)
    OP_0D()
    Jump("loc_771D")

    label("loc_771D")

    Sleep(200)

    ChrTalk(    #307
        0x101,
        "#1006FAh-ha! There she is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x107,
        "#065FQuick, we gotta follow her!\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_7780"),
        (101, "loc_7831"),
        (102, "loc_78E2"),
        (103, "loc_7993"),
        (SWITCH_DEFAULT, "loc_7A44"),
    )


    label("loc_7780")


    def lambda_7786():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7786)

    def lambda_779E():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_779E)

    def lambda_77B9():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_77B9)
    Sleep(100)

    def lambda_77D9():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_77D9)

    def lambda_77F4():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_77F4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_7A44")

    label("loc_7831")


    def lambda_7837():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7837)

    def lambda_784F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_784F)

    def lambda_786A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_786A)
    Sleep(100)

    def lambda_788A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_788A)

    def lambda_78A5():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_78A5)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 107, 0, 0)
    IdleLoop()
    Jump("loc_7A44")

    label("loc_78E2")


    def lambda_78E8():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_78E8)

    def lambda_7900():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7900)

    def lambda_791B():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_791B)
    Sleep(100)

    def lambda_793B():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_793B)

    def lambda_7956():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7956)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 108, 0, 0)
    IdleLoop()
    Jump("loc_7A44")

    label("loc_7993")


    def lambda_7999():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7999)

    def lambda_79B1():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79B1)

    def lambda_79CC():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_79CC)
    Sleep(100)

    def lambda_79EC():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_79EC)

    def lambda_7A07():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7A07)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_7A44")

    label("loc_7A44")

    Return()

    # Function_32_723C end

    def Function_33_7A45(): pass

    label("Function_33_7A45")

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
        (0, "loc_7AC1"),
        (1, "loc_7AC7"),
        (SWITCH_DEFAULT, "loc_7ACD"),
    )


    label("loc_7AC1")

    OP_A2(0x1200)
    Jump("loc_7ACD")

    label("loc_7AC7")

    OP_A2(0x1201)
    Jump("loc_7ACD")

    label("loc_7ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7ADB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_7ADF")

    label("loc_7ADB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_7ADF")

    Return()

    # Function_33_7A45 end

    def Function_34_7AE0(): pass

    label("Function_34_7AE0")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7B1F")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_7B39")

    label("loc_7B1F")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_7B39")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_34_7AE0 end

    SaveToFile()

Try(main)
