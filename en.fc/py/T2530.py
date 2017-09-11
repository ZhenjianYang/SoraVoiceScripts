from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2530   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2530.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Dean Collins',                         # 9
        'Jill',                                 # 10
        'Fauna',                                # 11
        'Mr. Ratio',                            # 12
        'Ms. Wiola',                            # 13
        'Ms. Millia',                           # 14
        'Mr. Effort',                           # 15
        'Rhody',                                # 16
        'Kaden',                                # 17
        'Alice',                                # 18
        'Taylor',                               # 19
        'Purity',                               # 20
        'Logic',                                # 21
        'Roy',                                  # 22
        'Thelma',                               # 23
        'Patrick',                              # 24
        'Gerome',                               # 25
        'Nikita',                               # 26
        'Mayor Dalmore',                        # 27
        'CH22000',                              # 28
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
        'ED6_DT07/CH02600 ._CH',             # 00
        'ED6_DT07/CH02390 ._CH',             # 01
        'ED6_DT07/CH02490 ._CH',             # 02
        'ED6_DT07/CH01660 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01430 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01360 ._CH',             # 07
        'ED6_DT07/CH01580 ._CH',             # 08
        'ED6_DT07/CH01590 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01090 ._CH',             # 0B
        'ED6_DT07/CH01080 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
        'ED6_DT07/CH01663 ._CH',             # 0E
        'ED6_DT07/CH01213 ._CH',             # 0F
        'ED6_DT07/CH01433 ._CH',             # 10
        'ED6_DT07/CH01463 ._CH',             # 11
        'ED6_DT07/CH02603 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02600P._CP',             # 00
        'ED6_DT07/CH02390P._CP',             # 01
        'ED6_DT07/CH02490P._CP',             # 02
        'ED6_DT07/CH01660P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01430P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01360P._CP',             # 07
        'ED6_DT07/CH01580P._CP',             # 08
        'ED6_DT07/CH01590P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01090P._CP',             # 0B
        'ED6_DT07/CH01080P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
        'ED6_DT07/CH01663P._CP',             # 0E
        'ED6_DT07/CH01213P._CP',             # 0F
        'ED6_DT07/CH01433P._CP',             # 10
        'ED6_DT07/CH01463P._CP',             # 11
        'ED6_DT07/CH02603P._CP',             # 12
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 30700,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 270,
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
        X                   = 41400,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 87700,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 84400,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 3100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2800,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 90,
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
        X                   = -700,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 2000,
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
        X                   = -3100,
        Z                   = 0,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -2900,
        Z                   = 0,
        Y                   = 30000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -2600,
        Z                   = 0,
        Y                   = 30800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -6200,
        Z                   = 0,
        Y                   = 35300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 86000,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 86600,
        Z                   = 0,
        Y                   = 32700,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 84800,
        Z                   = 0,
        Y                   = 33200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        X                   = 85590,
        Z                   = 700,
        Y                   = 3050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835021,
        ChipIndex           = 0xD,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 51000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 35,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )


    DeclActor(
        TriggerX            = 85590,
        TriggerZ            = 700,
        TriggerY            = 3400,
        TriggerRange        = 1000,
        ActorX              = 85590,
        ActorZ              = 1000,
        ActorY              = 3050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 48200,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 48200,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31580,
        TriggerZ            = 0,
        TriggerY            = 1450,
        TriggerRange        = 800,
        ActorX              = 31580,
        ActorZ              = 1000,
        ActorY              = 1450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57380,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 57380,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31630,
        TriggerZ            = 0,
        TriggerY            = 31460,
        TriggerRange        = 800,
        ActorX              = 31630,
        ActorZ              = 1000,
        ActorY              = 31460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3420,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 3420,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3570,
        TriggerZ            = 0,
        TriggerY            = 34450,
        TriggerRange        = 800,
        ActorX              = 3570,
        ActorZ              = 1200,
        ActorY              = 34450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 790,
        TriggerZ            = 0,
        TriggerY            = 35530,
        TriggerRange        = 800,
        ActorX              = 790,
        ActorZ              = 1200,
        ActorY              = 35530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5010,
        TriggerZ            = 0,
        TriggerY            = 29180,
        TriggerRange        = 800,
        ActorX              = -5010,
        ActorZ              = 1200,
        ActorY              = 29180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1970,
        TriggerZ            = 0,
        TriggerY            = 30780,
        TriggerRange        = 800,
        ActorX              = -1970,
        ActorZ              = 1200,
        ActorY              = 30780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41160,
        TriggerZ            = 0,
        TriggerY            = 6230,
        TriggerRange        = 400,
        ActorX              = 41400,
        ActorZ              = 1500,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_612",          # 00, 0
        "Function_1_9F1",          # 01, 1
        "Function_2_A43",          # 02, 2
        "Function_3_BC0",          # 03, 3
        "Function_4_1478",         # 04, 4
        "Function_5_147D",         # 05, 5
        "Function_6_1E5C",         # 06, 6
        "Function_7_223D",         # 07, 7
        "Function_8_25CD",         # 08, 8
        "Function_9_2B34",         # 09, 9
        "Function_10_2F66",        # 0A, 10
        "Function_11_3163",        # 0B, 11
        "Function_12_3590",        # 0C, 12
        "Function_13_3848",        # 0D, 13
        "Function_14_3ADE",        # 0E, 14
        "Function_15_3B71",        # 0F, 15
        "Function_16_4313",        # 10, 16
        "Function_17_4723",        # 11, 17
        "Function_18_47B3",        # 12, 18
        "Function_19_4825",        # 13, 19
        "Function_20_4A1E",        # 14, 20
        "Function_21_4C35",        # 15, 21
        "Function_22_51DF",        # 16, 22
        "Function_23_5247",        # 17, 23
        "Function_24_52BE",        # 18, 24
        "Function_25_5324",        # 19, 25
        "Function_26_53A0",        # 1A, 26
        "Function_27_5410",        # 1B, 27
        "Function_28_547B",        # 1C, 28
        "Function_29_54CF",        # 1D, 29
        "Function_30_552F",        # 1E, 30
        "Function_31_55B1",        # 1F, 31
        "Function_32_5608",        # 20, 32
        "Function_33_5667",        # 21, 33
        "Function_34_566B",        # 22, 34
        "Function_35_566F",        # 23, 35
        "Function_36_5673",        # 24, 36
        "Function_37_5677",        # 25, 37
    )


    def Function_0_612(): pass

    label("Function_0_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_668")
    SetChrPos(0xB, 5320, 250, 2110, 270)
    SetChrPos(0xC, 5300, 250, 32080, 267)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xF, 400, 0, 0, 90)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_9C1")

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_6AE")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    Jump("loc_9C1")

    label("loc_6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_740")
    SetChrPos(0xB, 1710, 0, 4970, 180)
    SetChrPos(0xC, -6910, 0, 33220, 90)
    SetChrPos(0xD, 95370, 250, 34220, 225)
    SetChrPos(0x8, 43470, 0, 5280, 225)
    SetChrPos(0x10, -7060, 0, 1680, 90)
    SetChrPos(0x11, 920, 0, -1500, 0)
    SetChrPos(0x12, -1590, 0, 34700, 0)
    SetChrPos(0x14, 1300, 0, 28510, 90)
    Jump("loc_9C1")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_7C4")
    SetChrPos(0xB, 1710, 0, 4970, 180)
    SetChrPos(0xC, -6910, 0, 33220, 90)
    SetChrPos(0xD, 95370, 250, 34220, 225)
    SetChrPos(0x8, 42940, 0, 1070, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, -7060, 0, 1680, 90)
    SetChrPos(0x11, 920, 0, -1500, 0)
    SetChrFlags(0x14, 0x80)
    Jump("loc_9C1")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_887")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x10, -5200, 0, 2050, 0)
    SetChrPos(0x11, 4500, 250, 4019, 270)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    SetChrChipByIndex(0xD, 16)
    SetChrPos(0xD, 84450, 250, 2790, 90)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    OP_44(0xD, 0xFF)
    SetChrChipByIndex(0xB, 14)
    SetChrPos(0xB, 84450, 250, 1030, 90)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 18)
    Jump("loc_9C1")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_8BB")
    SetChrPos(0xC, 5300, 250, 32080, 267)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_8F7")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_938")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_97E")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jump("loc_9C1")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_9C1")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_9C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_9D1")
    SetChrFlags(0x1B, 0x80)

    label("loc_9D1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (114, "loc_9DD"),
        (SWITCH_DEFAULT, "loc_9F0"),
    )


    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9ED")
    Event(0, 21)

    label("loc_9ED")

    Jump("loc_9F0")

    label("loc_9F0")

    Return()

    # Function_0_612 end

    def Function_1_9F1(): pass

    label("Function_1_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A12")
    OP_B1("t2530_y")
    Jump("loc_A1B")

    label("loc_A12")

    OP_B1("t2530_n")

    label("loc_A1B")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_A2E")
    OP_65(0x0, 0x1)

    label("loc_A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_A42")
    OP_64(0x0, 0x1)
    SetChrFlags(0x1B, 0x80)

    label("loc_A42")

    Return()

    # Function_1_9F1 end

    def Function_2_A43(): pass

    label("Function_2_A43")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BAA")

    label("loc_A68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BAA")

    label("loc_A81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BAA")

    label("loc_A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BAA")

    label("loc_AB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BAA")

    label("loc_ACC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BAA")

    label("loc_AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BAA")

    label("loc_AFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B17")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BAA")

    label("loc_B17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BAA")

    label("loc_B30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B49")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BAA")

    label("loc_B49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BAA")

    label("loc_B62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BAA")

    label("loc_B7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B94")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BAA")

    label("loc_B94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BAA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BAA")

    label("loc_BBF")

    Return()

    # Function_2_A43 end

    def Function_3_BC0(): pass

    label("Function_3_BC0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9F")
    OP_A2(0x0)

    ChrTalk(    #0
        0xFE,
        (
            "#780FAh, hello there.\x02\x03",

            "First of all, I'd like to say how\x01",
            "relieved I am that the criminals\x01",
            "have been caught.\x02\x03",

            "I'll be waiting for when you turn\x01",
            "your investigations toward your\x01",
            "academic pursuits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_C9F")


    ChrTalk(    #1
        0xFE,
        (
            "#780FThank goodness that the\x01",
            "attackers have been arrested.\x02\x03",

            "I'll be waiting for when you turn\x01",
            "your investigations toward your\x01",
            "academic pursuits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D35")

    Jump("loc_1474")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "#780FAh, you're here.\x02\x03",

            "I heard about Matron Theresa\x01",
            "and the children.\x02\x03",

            "They certainly didn't deserve this.\x02\x03",

            "What words are there to describe\x01",
            "such a thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4B")

    label("loc_DED")


    ChrTalk(    #3
        0xFE,
        (
            "#780FI heard about Matron Theresa\x01",
            "and her children.\x02\x03",

            "They certainly didn't deserve this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4B")

    Jump("loc_1474")

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F54")
    OP_A2(0x0)

    ChrTalk(    #4
        0xFE,
        (
            "#780FWell, we certainly are in\x01",
            "your debt this time...\x02\x03",

            "The play was magnificent. Joshua's\x01",
            "portrayal of Princess Cecilia was\x01",
            "particularly memorable.\x02\x03",

            "I hope that you'll be able to come\x01",
            "to the campus again, hopefully to\x01",
            "stay for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE7")

    label("loc_F54")


    ChrTalk(    #5
        0xFE,
        (
            "#780FWell, we certainly are in\x01",
            "your debt this time...\x02\x03",

            "I hope that you'll be able to come\x01",
            "to the campus again, hopefully to\x01",
            "stay for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE7")

    Jump("loc_1474")

    label("loc_FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109A")
    OP_A2(0x0)

    ChrTalk(    #6
        0xFE,
        (
            "#780FAh, hello there. Everything's been\x01",
            "quite a big success.\x02\x03",

            "I'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FC")

    label("loc_109A")


    ChrTalk(    #7
        0xFE,
        (
            "#780FI'm looking forward to seeing the\x01",
            "play. I expect it will be a big hit\x01",
            "for the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    Jump("loc_1474")

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1208")
    OP_A2(0x0)

    ChrTalk(    #8
        0xFE,
        (
            "#780FI've not seen you since last year's\x01",
            "Royal Council, Mayor Dalmore.\x02\x03",

            "Has much changed since then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x1A,
        (
            "#660FAs you can see, I'm feeling\x01",
            "quite well. You look to be in\x01",
            "good health, also.\x02\x03",

            "I expect that today will be\x01",
            "quite enjoyable.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    Jump("loc_12BF")

    label("loc_1208")


    ChrTalk(    #10
        0xFE,
        (
            "#780FI'd like to get your input on some\x01",
            "of the school's affairs, if you have\x01",
            "the time.\x02\x03",

            "Though we may be chartered by\x01",
            "the monarchy, it's still important\x01",
            "to hear the local views.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BF")

    Jump("loc_1474")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 0)), scpexpr(EXPR_END)), "loc_137A")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12EB")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1306")

    label("loc_12EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1301")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1306")

    label("loc_1301")

    SetChrSubChip(0xFE, 2)

    label("loc_1306")

    OP_8C(0xFE, 180, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #11
        0x8,
        (
            "#780FHa ha. I'd hate to get in the\x01",
            "way of your fun tomorrow.\x02\x03",

            "I hope you enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    Jump("loc_1474")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1474")

    ChrTalk(    #12
        0xFE,
        (
            "#780FDon't worry, I'll make sure you have a place\x01",
            "to stay. And I'm greatly looking forward to\x01",
            "your...erm...'transformation'...\x02\x03",

            "There's also a cafeteria on campus, which\x01",
            "you may use at your leisure. Just relax,\x01",
            "and work hard on the play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1474")

    TalkEnd(0x8)
    Return()

    # Function_3_BC0 end

    def Function_4_1478(): pass

    label("Function_4_1478")

    Call(0, 5)
    Return()

    # Function_4_1478 end

    def Function_5_147D(): pass

    label("Function_5_147D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1501")
    OP_A2(0x1)

    ChrTalk(    #13
        0xA,
        "Hmm? Did someone need me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "Classes just ended, so the students\x01",
            "should be milling about any moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1520")

    label("loc_1501")


    ChrTalk(    #15
        0xA,
        "Hmm? Did someone need me?\x02",
    )

    CloseMessageWindow()

    label("loc_1520")

    Jump("loc_1E58")

    label("loc_1523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_15B3")

    ChrTalk(    #16
        0xA,
        (
            "Ha ha...the festival was a\x01",
            "huge success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "I always worry that the people\x01",
            "with children will lose track of\x01",
            "them in the crowd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_16D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167B")
    OP_A2(0x1)

    ChrTalk(    #18
        0xA,
        (
            "Success! This is possibly our\x01",
            "best turnout yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "Though I do always worry that the people\x01",
            "with children will lose track of them in\x01",
            "the crowd. But so far...no fatalities!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D5")

    label("loc_167B")


    ChrTalk(    #20
        0xA,
        "Is someone looking for them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "I can call for them on the campus\x01",
            "P.A. if need be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D5")

    Jump("loc_1E58")

    label("loc_16D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_184B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E7")
    OP_A2(0x1)

    ChrTalk(    #22
        0xA,
        (
            "The event will be held on the\x01",
            "grounds and in the main building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "There's a play scheduled to be held\x01",
            "in the auditorium, this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "The Student Council has set up the\x01",
            "cafeteria as the rest area, so please,\x01",
            "feel free to relax there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1848")

    label("loc_17E7")


    ChrTalk(    #25
        0xA,
        (
            "In order to help prevent crime,\x01",
            "the dorms are locked down for\x01",
            "the duration of the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1848")

    Jump("loc_1E58")

    label("loc_184B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CE")
    OP_A2(0x1)

    ChrTalk(    #26
        0xA,
        "Have you finished getting ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "It looks like we'll have more\x01",
            "attendees tomorrow than\x01",
            "ever before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_18CE")


    ChrTalk(    #28
        0xA,
        (
            "Have you finished getting ready?\x01",
            "Tomorrow isn't far away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190D")

    Jump("loc_1E58")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")
    OP_A2(0x1)

    ChrTalk(    #29
        0xA,
        (
            "Ha ha...even with classes done,\x01",
            "it's still extremely busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        "It's almost festival time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "I hope all of the students are\x01",
            "trying their hardest for this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0A")

    label("loc_19CA")


    ChrTalk(    #32
        0xA,
        (
            "Ha ha...even with classes done,\x01",
            "it's still extremely busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0A")

    Jump("loc_1E58")

    label("loc_1A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_1B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1B")
    OP_A2(0x1)

    ChrTalk(    #33
        0xA,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#040FPardon me, Fauna...I just got back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        "Ha ha, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x105,
        (
            "#040FOh, all right. I'll go and see\x01",
            "him now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B84")

    label("loc_1B1B")


    ChrTalk(    #39
        0xA,
        (
            "If you're looking for the dean,\x01",
            "he just went to his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        "He's been quite worried about you.\x02",
    )

    CloseMessageWindow()

    label("loc_1B84")

    Jump("loc_1E58")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5F")
    OP_A2(0x1)

    ChrTalk(    #41
        0xA,
        (
            "Hello, Kloe. Are you already done\x01",
            "with your off-campus errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#040FOh, not yet...\x02\x03",

            "I'm sorry, but I still have some\x01",
            "errands left to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "That's fine. Just take care\x01",
            "of yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1C5F")


    ChrTalk(    #44
        0xA,
        "Take care of yourself, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_1C81")

    Jump("loc_1E58")

    label("loc_1C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_1D03")

    ChrTalk(    #45
        0xA,
        "Oh, did you want a guided tour?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "I'm terribly sorry, but I can't\x01",
            "show you around while class\x01",
            "is in session.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E07")
    OP_A2(0x1)

    ChrTalk(    #47
        0xA,
        (
            "Oh, hello, Kloe. Are you back\x01",
            "to stay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#040FNo...I'm just showing some folks\x01",
            "around on the way to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "I see...well, since this is your\x01",
            "vacation, make sure you let\x01",
            "your hair down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x105,
        "#040FI will...thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1E07")


    ChrTalk(    #51
        0xA,
        (
            "Since this is your vacation,\x01",
            "make sure you let your hair\x01",
            "down and have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E58")

    TalkEnd(0xA)
    Return()

    # Function_5_147D end

    def Function_6_1E5C(): pass

    label("Function_6_1E5C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1EAD")

    ChrTalk(    #52
        0xFE,
        (
            "Class may be over, but I still\x01",
            "get questions from my students.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2239")

    label("loc_1EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_1F22")

    ChrTalk(    #53
        0xFE,
        (
            "Hmm...my class has done a\x01",
            "fine job on the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "They really put a lot of work\x01",
            "into this set.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2239")

    label("loc_1F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_1F98")

    ChrTalk(    #55
        0xFE,
        (
            "The lead roles will be played\x01",
            "by students, will they not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Everyone's even more active\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2239")

    label("loc_1F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_218A")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FC1")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1FF2")

    label("loc_1FC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FD7")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1FF2")

    label("loc_1FD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FED")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1FF2")

    label("loc_1FED")

    SetChrSubChip(0xFE, 1)

    label("loc_1FF2")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CE")
    OP_A2(0x2)

    ChrTalk(    #57
        0xFE,
        (
            "You kids came from Rolent,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "I'm actually from there, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Speaking of which, my parents will\x01",
            "be visiting to attend the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "It's good that they were invited.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2182")

    label("loc_20CE")


    ChrTalk(    #61
        0xFE,
        (
            "Ah, yes...I had a chance to\x01",
            "watch the rehearsals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Such dedication from all the actors! I'm\x01",
            "quite looking forward to the performance.\x01",
            "The, uh, princess is something else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2182")

    SetChrSubChip(0xFE, 0)
    Jump("loc_2239")

    label("loc_218A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2239")

    ChrTalk(    #63
        0xFE,
        (
            "With the festival coming up, the\x01",
            "kids practically vibrate in their\x01",
            "seats when class is almost out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Ha ha...but I suppose there's\x01",
            "nothing to be done about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2239")

    TalkEnd(0xB)
    Return()

    # Function_6_1E5C end

    def Function_7_223D(): pass

    label("Function_7_223D")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_22D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A0")
    OP_A2(0x3)

    ChrTalk(    #65
        0xFE,
        "Let's see...this problem here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "How do you do it?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    Jump("loc_22D2")

    label("loc_22A0")


    ChrTalk(    #68
        0xFE,
        (
            "Wow, the students here are\x01",
            "really dedicated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D2")

    Jump("loc_25C9")

    label("loc_22D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2340")

    ChrTalk(    #69
        0xFE,
        "This afternoon is the big play.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Good thing you two seem like\x01",
            "the really reliable sort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C9")

    label("loc_2340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F5")
    OP_A2(0x3)

    ChrTalk(    #71
        0xFE,
        "Hmm...my class is fairly low-key...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "To be honest, I think the research\x01",
            "periodical is pretty plain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "But it's okay. I'm just glad we\x01",
            "have readers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2424")

    label("loc_23F5")


    ChrTalk(    #74
        0xFE,
        "I don't want to lose to Millia's class...\x02",
    )

    CloseMessageWindow()

    label("loc_2424")

    Jump("loc_25C9")

    label("loc_2427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_25C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2581")
    OP_A2(0x3)

    ChrTalk(    #75
        0xFE,
        "Oh, hello, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#040FHello, Ms. Wiola.\x02\x03",

            "I'm sorry I missed your class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Ha ha...you don't need to worry\x01",
            "about that, dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "You did have important business\x01",
            "to attend to, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "If you stop by the faculty lounge later,\x01",
            "I can give you a printout of the\x01",
            "work you missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x105,
        "#040FYes, ma'am. I will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25C9")

    label("loc_2581")


    ChrTalk(    #81
        0xFE,
        (
            "Now, then...I suppose I should get\x01",
            "started on grading these tests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C9")

    TalkEnd(0xC)
    Return()

    # Function_7_223D end

    def Function_8_25CD(): pass

    label("Function_8_25CD")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(    #82
        0xFE,
        (
            "I've been put in charge of writing\x01",
            "up the entrance examinations\x01",
            "for this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Ha ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "I look forward to the challenge.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B30")

    label("loc_2662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F1")
    OP_A2(0x4)

    ChrTalk(    #85
        0xFE,
        (
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2751")

    label("loc_26F1")


    ChrTalk(    #87
        0xFE,
        (
            "The students in that class are\x01",
            "impressive...though the same\x01",
            "can't be said for the teacher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2751")

    Jump("loc_2B30")

    label("loc_2754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_27D8")

    ChrTalk(    #88
        0xFE,
        (
            "Why is my class doing fortune-\x01",
            "telling and games, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Wiola's kids are doing something\x01",
            "far more direct.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B30")

    label("loc_27D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2944")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2801")
    SetChrSubChip(0xFE, 1)
    Jump("loc_2832")

    label("loc_2801")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2817")
    SetChrSubChip(0xFE, 0)
    Jump("loc_2832")

    label("loc_2817")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_282D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_2832")

    label("loc_282D")

    SetChrSubChip(0xFE, 1)

    label("loc_2832")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EC")
    OP_A2(0x4)

    ChrTalk(    #90
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I'll do my best to keep my criticisms\x01",
            "to myself...as valid as they may be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293C")

    label("loc_28EC")


    ChrTalk(    #92
        0xFE,
        (
            "Well, the students will show\x01",
            "everyone the fruits of their\x01",
            "labors tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293C")

    SetChrSubChip(0xFE, 0)
    Jump("loc_2B30")

    label("loc_2944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_2B30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A66")
    OP_A2(0x4)

    ChrTalk(    #93
        0xFE,
        (
            "Everyone tends to slack off in\x01",
            "the lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I suppose all the instruction in\x01",
            "the world can't change that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha... Ahem!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B30")

    label("loc_2A66")


    ChrTalk(    #96
        0xFE,
        (
            "Everyone tends to slack off in the\x01",
            "lead-up to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Perhaps tomorrow, I'll give the kids a pop quiz.\x01",
            "And just to show them...it will NOT be multiple\x01",
            "choice! Mwa ha ha ha...ha... Ahem!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B30")

    TalkEnd(0xD)
    Return()

    # Function_8_25CD end

    def Function_9_2B34(): pass

    label("Function_9_2B34")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2BB5")

    ChrTalk(    #98
        0xFE,
        "I should make my rounds, soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "The students are generally\x01",
            "well-behaved enough to not\x01",
            "require me to hover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F62")

    label("loc_2BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_2D22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2C5C")

    ChrTalk(    #100
        0xFE,
        (
            "Ah, thanks for everything you\x01",
            "did yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I don't really have anything\x01",
            "I need to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'm just staying here,\x01",
            "in case I'm needed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D1F")

    label("loc_2C5C")


    ChrTalk(    #103
        0xFE,
        (
            "I heard some students talking\x01",
            "yesterday about having seen\x01",
            "monsters in the old building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I'll be making sure everything is\x01",
            "locked up tight before my rounds,\x01",
            "just to be on the safe side.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1F")

    Jump("loc_2F62")

    label("loc_2D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E1A")
    OP_A2(0x5)

    ChrTalk(    #105
        0xFE,
        (
            "There are three major courses\x01",
            "offered at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC2")

    label("loc_2E1A")


    ChrTalk(    #108
        0xFE,
        (
            "All of them are important,\x01",
            "but I'm personally in charge\x01",
            "of physical education.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "There are no classes at the\x01",
            "moment. Perfect time to get\x01",
            "the papers sorted out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC2")

    Jump("loc_2F62")

    label("loc_2EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F38")
    OP_A2(0x5)

    ChrTalk(    #110
        0xFE,
        "Hey, aren't you students?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Class is in session. You'll need\x01",
            "a pass to go off-campus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F62")

    label("loc_2F38")


    ChrTalk(    #112
        0xFE,
        "You'll need a pass to go off-campus.\x02",
    )

    CloseMessageWindow()

    label("loc_2F62")

    TalkEnd(0xE)
    Return()

    # Function_9_2B34 end

    def Function_10_2F66(): pass

    label("Function_10_2F66")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FEB")
    OP_A2(0x6)

    ChrTalk(    #113
        0xFE,
        (
            "Ahhh...finally, classes are done\x01",
            "for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3025")

    label("loc_2FEB")


    ChrTalk(    #115
        0xFE,
        (
            "Afternoon classes always make\x01",
            "me want to take a nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3025")

    Jump("loc_315F")

    label("loc_3028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_315F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DC")
    OP_A2(0x6)

    ChrTalk(    #116
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "Yep, I'm feeling good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_315F")

    label("loc_30DC")


    ChrTalk(    #119
        0xFE,
        (
            "I've been involved in the club's\x01",
            "food stand the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I didn't have a chance to get\x01",
            "involved in the class project.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315F")

    TalkEnd(0xF)
    Return()

    # Function_10_2F66 end

    def Function_11_3163(): pass

    label("Function_11_3163")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_31C6")

    ChrTalk(    #121
        0xFE,
        "Okay, time for the club activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "I've GOT to finish this painting today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_31C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_325C")

    ChrTalk(    #123
        0xFE,
        (
            "Since I'm working on the coffee house,\x01",
            "I've got to push myself! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "This is pretty tough...\x02",
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3328")

    ChrTalk(    #125
        0xFE,
        (
            "Whew...I'm not sure how, but I\x01",
            "managed to finish up in time.\x01",
            "Musta been the 36 lattes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Ugh...staying up all night has left\x01",
            "me completely drained. Or is that\x01",
            "the caffeine withdrawal?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_3328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_342F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D6")
    OP_A2(0x7)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #127
        0xFE,
        (
            "Whoa! What the hell?!\x01",
            "This is a cappuccino...\x01",
            "I ordered an espresso! Nooooo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I'll never finish up in time\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342C")

    label("loc_33D6")


    ChrTalk(    #129
        0xFE,
        "Hmm...maybe if I work all night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Ahhh...that should give me\x01",
            "plenty of time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342C")

    Jump("loc_358C")

    label("loc_342F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_358C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3555")
    OP_A2(0x7)

    ChrTalk(    #131
        0xFE,
        (
            "Hmm-hmm-hmmmmm... ♪\x01",
            "They've got an awful lot of coffee... ♪\x01",
            "An awful lot of coffee... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I'm making outfits to wear at\x01",
            "the food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I've got to really throw myself\x01",
            "into this! And to do that...\x01",
            "I NEED MORE COFFEEEEEE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "I love making stuff like this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_3555")


    ChrTalk(    #135
        0xFE,
        (
            "I've got to make decorations for\x01",
            "the room, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358C")

    TalkEnd(0x10)
    Return()

    # Function_11_3163 end

    def Function_12_3590(): pass

    label("Function_12_3590")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_35D5")

    ChrTalk(    #136
        0xFE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I'd be glad to show you to\x01",
            "your seats.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3844")

    label("loc_35D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3630")

    ChrTalk(    #138
        0xFE,
        "Hee hee...isn't this a cute outfit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Kaden's been making a lot of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3844")

    label("loc_3630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_370A")

    ChrTalk(    #140
        0xFE,
        (
            "He thought we had more time than we actually\x01",
            "do. Thankfully, with enough coffee in him, we\x01",
            "can still make the deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "So worry not, we'll be ready!\x01",
            "I want this to be the cutest\x01",
            "little place ever!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3844")

    label("loc_370A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_3844")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CE")
    OP_A2(0x8)

    ChrTalk(    #142
        0xFE,
        (
            "Kaden's really good with his hands,\x01",
            "and if you give him a little coffee,\x01",
            "then he can do just about anything! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Maybe I can get him to make\x01",
            "some stuffed dolls next...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3844")

    label("loc_37CE")


    ChrTalk(    #144
        0xFE,
        (
            "Despite the fact that he's appearing\x01",
            "in the play, he still managed to find\x01",
            "the time to make maid outfits for us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3844")

    TalkEnd(0x11)
    Return()

    # Function_12_3590 end

    def Function_13_3848(): pass

    label("Function_13_3848")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_397F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392D")
    OP_A2(0x9)

    ChrTalk(    #145
        0xFE,
        (
            "I didn't really understand the\x01",
            "lesson in my last class...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Umm...I thought maybe I should\x01",
            "ask some questions, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Ms. Millia always goes straight to\x01",
            "the faculty lounge once class is over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_397C")

    label("loc_392D")


    ChrTalk(    #148
        0xFE,
        (
            "Ms. Millia always goes straight to\x01",
            "the faculty lounge once class is over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397C")

    Jump("loc_3ADA")

    label("loc_397F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A79")
    OP_A2(0x9)

    ChrTalk(    #149
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "My class is doing either a tea house or a\x01",
            "haunted house. Not sure which, though,\x01",
            "frankly I think there's cross-over potential.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADA")

    label("loc_3A79")


    ChrTalk(    #152
        0xFE,
        (
            "Everyone in the social studies\x01",
            "class is working on the research\x01",
            "periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "Oh, wow...\x02",
    )

    CloseMessageWindow()

    label("loc_3ADA")

    TalkEnd(0x12)
    Return()

    # Function_13_3848 end

    def Function_14_3ADE(): pass

    label("Function_14_3ADE")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3B12")

    ChrTalk(    #154
        0xFE,
        "Welcome to the Fontana Tea House.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B6D")

    label("loc_3B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_3B6D")

    ChrTalk(    #155
        0xFE,
        (
            "I'm kind of embarrassed to be\x01",
            "dressed like this, but it is for\x01",
            "the festival...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B6D")

    TalkEnd(0x13)
    Return()

    # Function_14_3ADE end

    def Function_15_3B71(): pass

    label("Function_15_3B71")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3BAD")

    ChrTalk(    #156
        0xFE,
        (
            "Hmm...today's lesson was\x01",
            "very worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_430F")

    label("loc_3BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_3D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9A")
    OP_A2(0xB)

    ChrTalk(    #157
        0xFE,
        (
            "I understand the need to enjoy oneself,\x01",
            "but at the end of the day, I still need to\x01",
            "hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "That's especially true when\x01",
            "you're a senior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "Getting good grades is paramount.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D28")

    label("loc_3C9A")


    ChrTalk(    #160
        0xFE,
        (
            "I understand the need to engage in outside\x01",
            "activities, but at the end of the day, I still\x01",
            "need to hand in my research results, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D28")

    Jump("loc_430F")

    label("loc_3D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4159")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3EC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E92")
    OP_A2(0xB)

    ChrTalk(    #161
        0xFE,
        (
            "My social studies class has been using various\x01",
            "economic indicators to predict future trends\x01",
            "and we'll be displaying the results here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "We also have a collection of materials\x01",
            "summarising the history and development of this\x01",
            "region in a simple, easy to read format.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3E92")


    ChrTalk(    #164
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC3")

    Jump("loc_4156")

    label("loc_3EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4034")
    OP_A2(0xB)

    ChrTalk(    #165
        0xFE,
        (
            "My social studies class will be\x01",
            "researching various economic\x01",
            "indicators to predict future trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "Reviewing the history and growth\x01",
            "of Ruan should provide useful\x01",
            "data for this project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "If any details are missing, you just\x01",
            "have to go with what makes the most\x01",
            "sense from the data available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4156")

    label("loc_4034")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_4125")

    ChrTalk(    #169
        0xFE,
        (
            "It may push me past deadline, but I'd\x01",
            "love to get my hands on a copy of 'Ruan\x01",
            "Economics.' Very useful data in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "If you should happen to see any\x01",
            "of the volumes, would you please\x01",
            "return them to the reference room?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4156")

    label("loc_4125")


    ChrTalk(    #171
        0xFE,
        (
            "If you're interested,\x01",
            "come and take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4156")

    Jump("loc_430F")

    label("loc_4159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4163")
    Jump("loc_430F")

    label("loc_4163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_430F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42ED")
    OP_A2(0xB)

    ChrTalk(    #172
        0xFE,
        (
            "Hello, Kloe.\x01",
            "So, you've come back to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "The preparations for the class\x01",
            "program appear to be coming\x01",
            "along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "How fares the play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "I'm told the casting has not yet\x01",
            "been finalized, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x105,
        (
            "#040FHa ha. That was done some\x01",
            "time ago, Logic.\x02\x03",

            "It's going to be great.\x01",
            "I hope you'll enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Ah, yes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "Then I wish you the best of luck.\x02",
    )

    CloseMessageWindow()
    Jump("loc_430F")

    label("loc_42ED")


    ChrTalk(    #179
        0xFE,
        "I wish you the best of luck.\x02",
    )

    CloseMessageWindow()

    label("loc_430F")

    TalkEnd(0x14)
    Return()

    # Function_15_3B71 end

    def Function_16_4313(): pass

    label("Function_16_4313")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_43C0")

    ChrTalk(    #180
        0xFE,
        (
            "Rumor has it the queen's birthday\x01",
            "celebration is going to feature the\x01",
            "biggest competition yet this year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I'd love for my Fencing Club\x01",
            "to participate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471F")

    label("loc_43C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_44EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4478")
    OP_A2(0xC)

    ChrTalk(    #182
        0xFE,
        (
            "I'm too busy with classes to do\x01",
            "much with the club, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "We've been switching off who's\x01",
            "supervising the club shop, so \x01",
            "I was thinking of checking in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44EB")

    label("loc_4478")


    ChrTalk(    #184
        0xFE,
        (
            "In my case, there's a lot of people\x01",
            "to watch and the more enthusiastic\x01",
            "ones have some pretty sharp questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44EB")

    Jump("loc_471F")

    label("loc_44EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_4618")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A3")
    OP_A2(0xC)

    ChrTalk(    #185
        0xFE,
        (
            "I'm an exchange student from the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "I've been busy with this year's\x01",
            "research periodical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "It's eaten up most of my time, actually.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4615")

    label("loc_45A3")


    ChrTalk(    #188
        0xFE,
        (
            "I'm an exchange student from the\x01",
            "Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I've been busy with this year's\x01",
            "research periodical.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4615")

    Jump("loc_471F")

    label("loc_4618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_471F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B3")
    OP_A2(0xC)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #190
        0xFE,
        "Oh, hi, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "The class has finished up most\x01",
            "of its setup duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "Logic is still at work in the\x01",
            "reference room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471F")

    label("loc_46B3")


    ChrTalk(    #193
        0xFE,
        (
            "The class has finished up most\x01",
            "of its setup duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Logic is still at work in the\x01",
            "reference room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471F")

    TalkEnd(0x15)
    Return()

    # Function_16_4313 end

    def Function_17_4723(): pass

    label("Function_17_4723")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_478B")
    OP_A2(0xD)

    ChrTalk(    #195
        0xFE,
        "Logic is such a perfectionist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Personally, I think we've gotten\x01",
            "plenty done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47AF")

    label("loc_478B")


    ChrTalk(    #197
        0xFE,
        "Logic is such a perfectionist.\x02",
    )

    CloseMessageWindow()

    label("loc_47AF")

    TalkEnd(0x16)
    Return()

    # Function_17_4723 end

    def Function_18_47B3(): pass

    label("Function_18_47B3")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4821")

    ChrTalk(    #198
        0xFE,
        (
            "These two must be childhood\x01",
            "friends. They both live in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "Ha ha...I'm kind of envious.\x02",
    )

    CloseMessageWindow()

    label("loc_4821")

    TalkEnd(0x17)
    Return()

    # Function_18_47B3 end

    def Function_19_4825(): pass

    label("Function_19_4825")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FD")
    TalkBegin(0x19)
    OP_A2(0xF)
    OP_A2(0x10)

    ChrTalk(    #200
        0x18,
        "Hey, Nikita.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #201
        0x18,
        "Don't you think this is good enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x18,
        (
            "I can put the finishing touches on\x01",
            "tomorrow when everyone'll be\x01",
            "around to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x19,
        (
            "Man, you never get tired of passing\x01",
            "work off on other people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x19,
        (
            "Everyone else still has work\x01",
            "to do, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x19,
        (
            "There's no telling if anyone else\x01",
            "will even have time to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x18,
        "Well, I guess you're probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x18,
        "Man, I'm hungry.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x10)
    ClearChrFlags(0x18, 0x10)
    TalkEnd(0x19)
    Jump("loc_4A1A")

    label("loc_49FD")


    ChrTalk(    #208
        0xFE,
        "*sigh* Man, I'm hungry.\x02",
    )

    CloseMessageWindow()

    label("loc_4A1A")

    TalkEnd(0x18)
    Return()

    # Function_19_4825 end

    def Function_20_4A1E(): pass

    label("Function_20_4A1E")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_4C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF6")
    TalkBegin(0x18)
    OP_A2(0xF)
    OP_A2(0x10)

    ChrTalk(    #209
        0x18,
        "Hey, Nikita.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #210
        0x18,
        "Don't you think this is good enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x18,
        (
            "I can put the finishing touches on\x01",
            "tomorrow when everyone'll be\x01",
            "around to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x19,
        (
            "Man, you never get tired of passing\x01",
            "work off on other people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x19,
        (
            "Everyone else still has work\x01",
            "to do, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x19,
        (
            "There's no telling if anyone else\x01",
            "will even have time to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x18,
        "Well, I guess you're probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x18,
        "Man, I'm hungry.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x10)
    ClearChrFlags(0x18, 0x10)
    TalkEnd(0x18)
    Jump("loc_4C31")

    label("loc_4BF6")


    ChrTalk(    #217
        0xFE,
        (
            "So what now? How are we supposed\x01",
            "to be ready in time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C31")

    TalkEnd(0x19)
    Return()

    # Function_20_4A1E end

    def Function_21_4C35(): pass

    label("Function_21_4C35")

    AddParty(0x3A, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(116200, 0, 4240, 0)
    SetChrPos(0x101, 116870, 0, -3740, 0)
    SetChrPos(0x105, 116870, 0, -3740, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x13B, 115990, 0, 2740, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #218
        0x13B,
        (
            "#643F#4PHey... That's a great idea!\x02\x03",

            "#641FThat's our dean.\x01",
            "Always level-headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x8,
        (
            "#781FHa ha ha. You flatter me.\x02\x03",

            "#780FThen, I assume I can entrust\x01",
            "the list to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x13B,
        "#644F#4PYes, sir! I'll take care of it!\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #221
        0x101,
        "#1PExcuse us...!\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_4DC0():
        OP_6D(117520, 0, 2870, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4DC0)

    def lambda_4DD8():
        OP_8E(0xFE, 0x1CAF2, 0x0, 0x5B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DD8)

    def lambda_4DF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DF3)
    Sleep(700)

    def lambda_4E0A():
        OP_8E(0xFE, 0x1C75A, 0x0, 0x1CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4E0A)

    def lambda_4E25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_4E25)
    OP_8C(0x13B, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 315, 0)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #222
        0x105,
        (
            "#044FOh, we're sorry...\x01",
            "Are we interrupting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        (
            "#781FNo, no. We were just finishing up.\x02\x03",

            "Actually...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x8, 400)

    ChrTalk(    #224
        0x13B,
        (
            "#646FDean! Don't say anything!\x02\x03",

            "You'll spoil the fun tomorrow!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(    #225
        0x101,
        (
            "#008F#2PUh, what? You're acting all\x01",
            "suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x105,
        (
            "#045FSo, what are you plotting this\x01",
            "time, Jill?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(    #227
        0x13B,
        (
            "#649FHeh heh heh... You'll have to\x01",
            "wait until tomorrow to find out.\x02\x03",

            "#640FAnyway, what's up? Do you\x01",
            "need me for something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x105,
        "#040FYes, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #229
        (
            "\x07\x05Kloe explained that an evening feast had been planned for the next day in\x01",
            "anticipation of the play's success.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #230
        0x13B,
        (
            "#640FOh, that sounds fine.\x02\x03",

            "#641FI'm just hoping and praying that\x01",
            "the festival is a big success.\x02\x03",

            "Let's give it all we've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x8,
        (
            "#780FHa ha. Barring any major complications,\x01",
            "I think tomorrow will go just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x105,
        "#040FYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#501F#2PC'mon, Jill. Let's go to the\x01",
            "cafeteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x13B,
        "#644FOkay.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x448)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_21_4C35 end

    def Function_22_51DF(): pass

    label("Function_22_51DF")

    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x1B, 0x80)
    OP_64(0x0, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #235
        "\x07\x00Found \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33E, 1)
    OP_28(0x27, 0x1, 0x80)
    TalkEnd(0xFF)
    Return()

    # Function_22_51DF end

    def Function_23_5247(): pass

    label("Function_23_5247")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #236
        (
            "\x07\x05Ahead: Dean's Room, Faculty Lounge\x01\x01",
            "* Academy personnel ONLY, please\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_23_5247 end

    def Function_24_52BE(): pass

    label("Function_24_52BE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #237
        (
            "\x07\x05Humanities Refreshment Booth\x01",
            "     Fontana Tea House\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_52BE end

    def Function_25_5324(): pass

    label("Function_25_5324")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #238
        (
            "\x07\x05          KEEP OUR HALLWAYS QUIET\x01",
            " \x01",
            "                    --Student Council\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_5324 end

    def Function_26_53A0(): pass

    label("Function_26_53A0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #239
        (
            "\x07\x05Natural Sciences Demonstration\x01",
            "'Quartz Circuits & Orbal Arts'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_53A0 end

    def Function_27_5410(): pass

    label("Function_27_5410")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #240
        (
            "\x07\x05Social Studies Demonstration\x01",
            "'Ruanian History & Economy'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_5410 end

    def Function_28_547B(): pass

    label("Function_28_547B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #241
        "\x07\x05Welcome to the Fontana Tea House!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_547B end

    def Function_29_54CF(): pass

    label("Function_29_54CF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #242
        (
            "\x07\x05It summarizes the trends in\x01",
            "orbal arts usage.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_29_54CF end

    def Function_30_552F(): pass

    label("Function_30_552F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #243
        (
            "\x07\x05It has a graph, depicting changes in the\x01",
            "tourist industry's annual growth rate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_30_552F end

    def Function_31_55B1(): pass

    label("Function_31_55B1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #244
        "\x07\x05It lists the most important exports.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_31_55B1 end

    def Function_32_5608(): pass

    label("Function_32_5608")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #245
        (
            "\x07\x05It concerns population growth and\x01",
            "migration.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_32_5608 end

    def Function_33_5667(): pass

    label("Function_33_5667")

    SetPlaceName(0x6F)
    Return()

    # Function_33_5667 end

    def Function_34_566B(): pass

    label("Function_34_566B")

    SetPlaceName(0x5E)
    Return()

    # Function_34_566B end

    def Function_35_566F(): pass

    label("Function_35_566F")

    SetPlaceName(0x6E)
    Return()

    # Function_35_566F end

    def Function_36_5673(): pass

    label("Function_36_5673")

    SetPlaceName(0x74)
    Return()

    # Function_36_5673 end

    def Function_37_5677(): pass

    label("Function_37_5677")

    SetPlaceName(0x73)
    Return()

    # Function_37_5677 end

    SaveToFile()

Try(main)
