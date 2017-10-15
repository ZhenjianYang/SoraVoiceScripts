from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Melvin',                               # 9
        'Hardt',                                # 10
        'Kuper',                                # 11
        'Benoit',                               # 12
        'Harg',                                 # 13
        'Brenda',                               # 14
        'Belden',                               # 15
        'Rocco',                                # 16
        'Portos',                               # 17
        'Jabu',                                 # 18
        'Picaro',                               # 19
        'Gasoline',                             # 20
        'Gasoline',                             # 21
        'Gasoline',                             # 22
        'Citizen',                              # 23
        'Citizen',                              # 24
        'Citizen',                              # 25
        'Citizen',                              # 26
        'Citizen',                              # 27
        'Citizen',                              # 28
        'Citizen',                              # 29
        'Citizen',                              # 30
        'Citizen',                              # 31
        'Citizen',                              # 32
        'Citizen',                              # 33
        'Middle-Aged Man',                      # 34
        'Murray',                               # 35
        'Lloyd',                                # 36
        'Boat',                                 # 37
        'Targeting Camera',                     # 38
        'Aurian Causeway',                      # 39
        'Ruan - North Block',                   # 40
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
        'ED6_DT07/CH01760 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01110 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH00472 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01080 ._CH',             # 0A
        'ED6_DT07/CH01050 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH01680 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01190 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01390 ._CH',             # 14
        'ED6_DT07/CH02530 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH01760P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01110P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH00472P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01080P._CP',             # 0A
        'ED6_DT07/CH01050P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH01680P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01190P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01390P._CP',             # 14
        'ED6_DT07/CH02530P._CP',             # 15
    )

    DeclNpc(
        X                   = 31640,
        Z                   = 0,
        Y                   = 10890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 30790,
        Z                   = 0,
        Y                   = 9980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 54040,
        Z                   = 0,
        Y                   = 25560,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 19700,
        Z                   = 0,
        Y                   = 28620,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 35750,
        Z                   = 0,
        Y                   = 25180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 75930,
        Z                   = 0,
        Y                   = 10740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 41000,
        Z                   = 1050,
        Y                   = 21010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 59750,
        Z                   = 0,
        Y                   = 6040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32140,
        Z                   = 0,
        Y                   = 6240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 51030,
        Z                   = 0,
        Y                   = 25340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 27010,
        Z                   = 0,
        Y                   = 11360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966088,
        ChipIndex           = 0x8,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966088,
        ChipIndex           = 0x8,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966088,
        ChipIndex           = 0x8,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xA0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 70000,
        Y                   = 0,
        Z                   = -2100,
        Range               = 76500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFFBB4,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 17690,
        Y                   = 2000,
        Z                   = 7750,
        Range               = 16040,
        Unknown_10          = 0xFFFFF8F8,
        Unknown_14          = 0x1036,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 54040,
        Y                   = -1000,
        Z                   = 25560,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 35750,
        Y                   = -1000,
        Z                   = 25180,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 26200,
        Y                   = -2000,
        Z                   = 14000,
        Range               = 31900,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x3E80,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )


    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 9400,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 9400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31960,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 31960,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23540,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 23540,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 77600,
        TriggerZ            = 0,
        TriggerY            = 12330,
        TriggerRange        = 800,
        ActorX              = 77900,
        ActorZ              = 1000,
        ActorY              = 12330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1270,
        TriggerZ            = 0,
        TriggerY            = 29530,
        TriggerRange        = 1000,
        ActorX              = -1300,
        ActorZ              = -2000,
        ActorY              = 34150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6EE",          # 00, 0
        "Function_1_964",          # 01, 1
        "Function_2_A05",          # 02, 2
        "Function_3_B82",          # 03, 3
        "Function_4_BA2",          # 04, 4
        "Function_5_D45",          # 05, 5
        "Function_6_E22",          # 06, 6
        "Function_7_F65",          # 07, 7
        "Function_8_15C0",         # 08, 8
        "Function_9_1DC1",         # 09, 9
        "Function_10_24FF",        # 0A, 10
        "Function_11_2AC9",        # 0B, 11
        "Function_12_2C2E",        # 0C, 12
        "Function_13_2EAF",        # 0D, 13
        "Function_14_2F47",        # 0E, 14
        "Function_15_2FBB",        # 0F, 15
        "Function_16_382C",        # 10, 16
        "Function_17_3A94",        # 11, 17
        "Function_18_3CC3",        # 12, 18
        "Function_19_3D12",        # 13, 19
        "Function_20_4065",        # 14, 20
        "Function_21_4F8C",        # 15, 21
        "Function_22_573E",        # 16, 22
        "Function_23_69B3",        # 17, 23
        "Function_24_7387",        # 18, 24
        "Function_25_741F",        # 19, 25
        "Function_26_7478",        # 1A, 26
        "Function_27_747F",        # 1B, 27
        "Function_28_751E",        # 1C, 28
        "Function_29_7FE8",        # 1D, 29
        "Function_30_8035",        # 1E, 30
        "Function_31_815D",        # 1F, 31
        "Function_32_8161",        # 20, 32
    )


    def Function_0_6EE(): pass

    label("Function_0_6EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9")
    SetChrPos(0x16, 18790, -1800, 11600, 0)
    SetChrPos(0x17, 17990, -1800, 11600, 90)
    SetChrPos(0x18, 17220, -1800, 11420, 90)
    SetChrPos(0x19, 16490, -1800, 11290, 90)
    SetChrPos(0x1A, 15770, -1800, 11470, 90)
    SetChrPos(0x1B, 15050, -1800, 11610, 90)
    SetChrPos(0x1C, 14440, -1800, 10960, 45)
    SetChrPos(0x1D, 14560, -1800, 10210, 0)
    SetChrPos(0x1E, 14410, -1800, 9520, 0)
    SetChrPos(0x1F, 14460, -1800, 8730, 0)
    SetChrPos(0x20, 14350, -1800, 7960, 0)
    SetChrPos(0x21, 14470, -1800, 7260, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0xA, 22700, -1800, 20620, 180)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xD, 40940, 1050, 21050, 200)
    SetChrPos(0x10, 24760, 0, 24750, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_894")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 31330, 0, 20020, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x10)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xF, 54610, 0, 24160, 270)
    SetChrChipByIndex(0xF, 21)

    label("loc_894")

    SetChrPos(0xC, 3800, -1800, 23920, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B6")
    SetChrFlags(0xC, 0x10)

    label("loc_8B6")

    Jump("loc_950")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_8E5")
    OP_43(0xF, 0x1, 0x0, 0x3)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E2")
    ClearChrFlags(0xA, 0x80)

    label("loc_8E2")

    Jump("loc_950")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_91B")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xB, 17990, 0, 1680, 180)
    SetChrPos(0xA, 50910, 0, 23310, 288)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_950")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_944")
    SetChrPos(0xB, 15930, -1800, 25220, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_950")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_950")
    ClearChrFlags(0xA, 0x80)

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_963")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_963")

    Return()

    # Function_0_6EE end

    def Function_1_964(): pass

    label("Function_1_964")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x230048)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987")
    OP_64(0x4, 0x1)

    label("loc_987")

    OP_72(0x16, 0x10)
    OP_6F(0x16, 60)
    OP_72(0x12, 0x10)
    OP_72(0x14, 0x10)
    OP_72(0x15, 0x10)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF")
    OP_6F(0x11, 1500)
    OP_72(0x21, 0x2)
    OP_71(0x22, 0x4)
    OP_64(0x3, 0x1)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)

    label("loc_9FF")

    OP_1C(0x13, 0x0, 0x1A)
    Return()

    # Function_1_964 end

    def Function_2_A05(): pass

    label("Function_2_A05")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B6C")

    label("loc_A2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B6C")

    label("loc_A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B6C")

    label("loc_A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B6C")

    label("loc_A75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B6C")

    label("loc_A8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B6C")

    label("loc_AA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B6C")

    label("loc_AC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B6C")

    label("loc_AD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B6C")

    label("loc_AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B6C")

    label("loc_B0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B24")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B6C")

    label("loc_B24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B6C")

    label("loc_B3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B56")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B6C")

    label("loc_B56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B81")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B6C")

    label("loc_B81")

    Return()

    # Function_2_A05 end

    def Function_3_B82(): pass

    label("Function_3_B82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA1")
    OP_99(0xFE, 0x1, 0x7, 0xBB8)
    SetChrSubChip(0xFE, 0)
    Sleep(250)
    Jump("Function_3_B82")

    label("loc_BA1")

    Return()

    # Function_3_B82 end

    def Function_4_BA2(): pass

    label("Function_4_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD4")

    label("loc_BAE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BD1")
    OP_8D(0xFE, 48840, 21930, 53280, 24890, 2000)
    Jump("loc_BAE")

    label("loc_BD1")

    Jump("loc_D44")

    label("loc_BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BED")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D2F")

    label("loc_BED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C06")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D2F")

    label("loc_C06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D2F")

    label("loc_C1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C38")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D2F")

    label("loc_C38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C51")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D2F")

    label("loc_C51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D2F")

    label("loc_C6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C83")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D2F")

    label("loc_C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D2F")

    label("loc_C9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D2F")

    label("loc_CB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCE")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D2F")

    label("loc_CCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D2F")

    label("loc_CE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D00")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D2F")

    label("loc_D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D19")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D2F")

    label("loc_D19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D44")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D2F")

    label("loc_D44")

    Return()

    # Function_4_BA2 end

    def Function_5_D45(): pass

    label("Function_5_D45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_DCD")

    ChrTalk(    #0
        0xFE,
        (
            "#1761FOur guys slack off the second\x01",
            "you take your eyes off 'em.\x02\x03",

            "So I'm pumpin' 'em up as I make\x01",
            "my scheduled rounds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1E")

    label("loc_DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DEE")

    ChrTalk(    #1
        0xFE,
        "#1767FHmph! Hmph!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1E")

    label("loc_DEE")

    OP_A2(0x7)

    ChrTalk(    #2
        0xFE,
        (
            "#1767FHmph! Hmph!\x02\x03",

            "#1766FNot enough...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1E")

    TalkEnd(0xFE)
    Return()

    # Function_5_D45 end

    def Function_6_E22(): pass

    label("Function_6_E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_EBC")

    ChrTalk(    #3
        0xFE,
        (
            "In this case, there's no choice, so I guess\x01",
            "that part-time job's okay, but, maaan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Working at my dad's office is gonna\x01",
            "be kinda...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F61")

    label("loc_EBC")

    OP_A2(0x6)

    ChrTalk(    #5
        0xFE,
        (
            "I went looking for work in the North Block,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "World's a hard place now, huh. The only\x01",
            "places hirin' are basically part-time jobs\x01",
            "for the election.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F61")

    TalkEnd(0xFE)
    Return()

    # Function_6_E22 end

    def Function_7_F65(): pass

    label("Function_7_F65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_107A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1017")

    ChrTalk(    #7
        0xFE,
        "The ferry port's busier than it used to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Not too long ago, every house had\x01",
            "at least one boat of their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Not everyone rode the ferry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1077")

    label("loc_1017")


    ChrTalk(    #10
        0xFE,
        "The ferry port's busier than it used to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Really, just standing there is so tiring.\x02",
    )

    CloseMessageWindow()

    label("loc_1077")

    Jump("loc_15BC")

    label("loc_107A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114E")

    ChrTalk(    #12
        0xFE,
        (
            "To be unable to cross the bridge is\x01",
            "like returning to the old days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "The ships from the ferry port are free,\x01",
            "but they're so inconvenient...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I've gotten too used to easy living.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_11E3")

    label("loc_114E")


    ChrTalk(    #15
        0xFE,
        (
            "To be unable to cross the bridge is\x01",
            "like returning to the old days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "The ships from the ferry port are free,\x01",
            "but they're so inconvenient...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E3")

    Jump("loc_15BC")

    label("loc_11E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1368")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1282")

    ChrTalk(    #17
        0xFE,
        (
            "There used to be a lot more energy here, too.\x01",
            "You'd see stands and little stalls all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "I suppose we'll never see that again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1365")

    label("loc_1282")

    OP_A2(0x5)

    ChrTalk(    #19
        0xFE,
        (
            "There used to be a lot more energy here, too.\x01",
            "You'd see stands and little stalls all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "The kids in the harbor are all working\x01",
            "hard for this election, it seems, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I suppose we'll never see that again.\x02",
    )

    CloseMessageWindow()

    label("loc_1365")

    Jump("loc_15BC")

    label("loc_1368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_13B2")

    ChrTalk(    #22
        0xFE,
        (
            "Young people should have at\x01",
            "least that much spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145F")

    label("loc_13B2")

    OP_A2(0x5)

    ChrTalk(    #23
        0xFE,
        (
            "Oh, that fuss a bit ago was\x01",
            "quite the show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Fights like that happen pretty\x01",
            "often where sailors gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Young people should have at\x01",
            "least that much spirit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145F")

    Jump("loc_15BC")

    label("loc_1462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14DE")

    ChrTalk(    #26
        0xFE,
        "The famous Dalmore family has fallen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Perhaps this is what they call\x01",
            "a turning point in the ages.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BC")

    label("loc_14DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_154D")

    ChrTalk(    #28
        0xFE,
        (
            "If you're looking for Norman's house,\x01",
            "it's right over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(    #29
        0xFE,
        "It's that house there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BC")

    label("loc_154D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_15BC")

    ChrTalk(    #30
        0xFE,
        "Both of them are quite the man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I'm sure the person who took their\x01",
            "pictures was very skilled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BC")

    TalkEnd(0xFE)
    Return()

    # Function_7_F65 end

    def Function_8_15C0(): pass

    label("Function_8_15C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D6")
    Call(0, 20)
    Jump("loc_1DBD")

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1649")

    ChrTalk(    #32
        0xFE,
        (
            "If you need gasoline again,\x01",
            "come by any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "That oil's too flammable to use in lamps.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_1649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1717")

    ChrTalk(    #34
        0xFE,
        (
            "Still, it'll be pretty bad if we don't\x01",
            "get any ships in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "We've got a limit to what we've\x01",
            "got in the warehouses right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "...I, I don't wanna think\x01",
            "about the future too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1796")

    label("loc_1717")


    ChrTalk(    #37
        0xFE,
        (
            "It'll be pretty bad if we don't get\x01",
            "any ships in soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "...Well, let's try not to worry about\x01",
            "the future to much yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1796")

    Jump("loc_1DBD")

    label("loc_1799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_180C")

    ChrTalk(    #39
        0xFE,
        (
            "If you need gasoline again,\x01",
            "come by any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "That oil's too flammable to use in lamps.\x02",
    )

    CloseMessageWindow()
    Jump("loc_197D")

    label("loc_180C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(    #41
        0xFE,
        (
            "Phew! It's been a while since I had\x01",
            "to do any real manual labor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "It's pretty tiring moving that much cargo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Well, with the crane not working,\x01",
            "not much we can do about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_197D")

    label("loc_18D4")


    ChrTalk(    #44
        0xFE,
        (
            "Sweet Aidios, it's been a long time since\x01",
            "we did work using 100% manpower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Well, we normally use the crane for\x01",
            "this kind of thing. Sure miss havin'\x01",
            "use of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197D")

    Jump("loc_1DBD")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A1E")

    ChrTalk(    #46
        0xFE,
        (
            "Callin' all voters! Vote for mayoral\x01",
            "candidate Portos, please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Vote for Portos, who will breathe new\x01",
            "life into the harbor, please!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF6")

    label("loc_1A1E")

    OP_A2(0x4)

    ChrTalk(    #48
        0xFE,
        (
            "Portos has kept the harbor goin'\x01",
            "for many years, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "If he becomes mayor, I'm sure he'll\x01",
            "support the harbor with all his power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "*pheeew* I'll take a quick break\x01",
            "and then get back to yelling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF6")

    Jump("loc_1DBD")

    label("loc_1AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1B63")

    ChrTalk(    #51
        0xFE,
        "Maybe I should've watched from farther away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "That cut a few years off my life.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C0B")

    label("loc_1B63")

    OP_A2(0x4)

    ChrTalk(    #53
        0xFE,
        (
            "I went to go see what the onlookers were\x01",
            "making a fuss about and almost got wrapped\x01",
            "up in that mess. Freaked me out, I tell ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Phew! That was a surprise.\x02",
    )

    CloseMessageWindow()

    label("loc_1C0B")

    Jump("loc_1DBD")

    label("loc_1C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C83")

    ChrTalk(    #55
        0xFE,
        "Can't slack off too much or Benoit will get mad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "He's a scary one when he gets angry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D00")

    label("loc_1C83")

    OP_A2(0x4)

    ChrTalk(    #57
        0xFE,
        "Ohh, it's about time for the next boat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Finding time with my job to go out and\x01",
            "do election work is pretty hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D00")

    Jump("loc_1DBD")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1D57")
    OP_A3(0x4)

    ChrTalk(    #59
        0xFE,
        "Portos! Vote for Portos, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "Vooooote for Portos!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1D57")

    OP_A2(0x4)

    ChrTalk(    #61
        0xFE,
        "Hmm, no one's passing through here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Maybe I should head to the other\x01",
            "side of the bridge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBD")

    TalkEnd(0xFE)
    Return()

    # Function_8_15C0 end

    def Function_9_1DC1(): pass

    label("Function_9_1DC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1E46")

    ChrTalk(    #63
        0xFE,
        "Seems like the Ravens are up to something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Did they finally come to their senses\x01",
            "in this emergency situation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24FB")

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1EEC")

    ChrTalk(    #65
        0xFE,
        (
            "Seems like the new mayor's finally\x01",
            "shown his true character. Hmph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Ultimately, he was all talk, and without\x01",
            "the boss he can't do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FED")

    label("loc_1EEC")


    ChrTalk(    #67
        0xFE,
        (
            "Thanks to the boss' orders, we've at least\x01",
            "got daily goods in the warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "If we run out of fuel or food,\x01",
            "we're really done for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Still, what is that new mayor doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "The one who's givin' orders in the\x01",
            "harbor is all our boss Portos!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FED")

    Jump("loc_24FB")

    label("loc_1FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_22D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_216E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_209A")

    ChrTalk(    #71
        0xFE,
        (
            "Kuper apparently went to apologize\x01",
            "over that uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "He was sure as heck fannin' the flames,\x01",
            "but there's fault on both sides.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_216B")

    label("loc_209A")

    OP_A2(0x3)

    ChrTalk(    #73
        0xFE,
        (
            "Kuper apparently went to apologize\x01",
            "over that uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "He was sure as heck fannin' the flames,\x01",
            "but there's fault on both sides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Well, the one who sent him to apologize\x01",
            "was boss Portos, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216B")

    Jump("loc_22D1")

    label("loc_216E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2200")

    ChrTalk(    #76
        0xFE,
        (
            "Kuper apparently went to apologize\x01",
            "over that uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "He was sure as heck fannin' the flames,\x01",
            "but there's fault on both sides.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D1")

    label("loc_2200")

    OP_A2(0x3)

    ChrTalk(    #78
        0xFE,
        (
            "Kuper apparently went to apologize\x01",
            "over that uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "He was sure as heck fannin' the flames,\x01",
            "but there's fault on both sides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Well, the one who sent him to apologize\x01",
            "was boss Portos, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D1")

    Jump("loc_24FB")

    label("loc_22D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2360")

    ChrTalk(    #81
        0xFE,
        "Why is that whole ghost thing our fault?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "What nonsense.\x01",
            "Think about what yer sayin', damn it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Tch, ticks me off...\x02",
    )

    CloseMessageWindow()
    Jump("loc_24FB")

    label("loc_2360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2480")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_23D2")

    ChrTalk(    #84
        0xFE,
        "I want Portos to be the mayor too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "After all, ain't many people as popular as him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_247D")

    label("loc_23D2")

    OP_A2(0x3)

    ChrTalk(    #86
        0xFE,
        (
            "I don't mind you helpin' with the election,\x01",
            "but mind workin' a bit more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "I mean, is there a point to yellin' here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "The only ones listenin' is the gulls.\x02",
    )

    CloseMessageWindow()

    label("loc_247D")

    Jump("loc_24FB")

    label("loc_2480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_24FB")

    ChrTalk(    #89
        0xFE,
        (
            "Boss Portos is busy with the election\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I'm takin' over runnin' the harbor\x01",
            "in his place for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FB")

    TalkEnd(0xFE)
    Return()

    # Function_9_1DC1 end

    def Function_10_24FF(): pass

    label("Function_10_24FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EF")

    ChrTalk(    #91
        0xFE,
        (
            "The boss apparently intends\x01",
            "to work with Mayor Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "That's boss Portos for you.\x01",
            "He's a pretty generous guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "The fact that he lost the election is more and\x01",
            "more regrettable every time I look back...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2670")

    label("loc_25EF")


    ChrTalk(    #94
        0xFE,
        (
            "The boss apparently intends\x01",
            "to work with Mayor Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Well, it's a crisis right now, so\x01",
            "we all need to come together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2670")

    Jump("loc_2AC5")

    label("loc_2673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_270B")

    ChrTalk(    #96
        0xFE,
        (
            "With the crane not working, all\x01",
            "we can rely on is our arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I wish that damn new mayor would come\x01",
            "down and help us carry the cargo.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC5")

    label("loc_270B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2793")

    ChrTalk(    #98
        0xFE,
        (
            "However, it's about time both\x01",
            "camps reconciled already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "At this rate, there's gonna be another happenin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27F2")

    label("loc_2793")

    OP_A2(0x2)

    ChrTalk(    #100
        0xFE,
        (
            "Hey, bracers.\x01",
            "Thanks for your help back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "I almost got pinned as a criminal.\x02",
    )

    CloseMessageWindow()

    label("loc_27F2")

    Jump("loc_2AC5")

    label("loc_27F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_286D")

    ChrTalk(    #102
        0xFE,
        (
            "Oh, hey, bracers.\x01",
            "Good work at the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Well, one way or another,\x01",
            "it's best we know the truth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC5")

    label("loc_286D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_29EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28F2")

    ChrTalk(    #104
        0xFE,
        (
            "Those guys tried to make the ghost\x01",
            "thing out to be our fault!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Ahh, just thinkin' back on it ticks me off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29E8")

    label("loc_28F2")

    OP_A2(0x2)

    ChrTalk(    #106
        0xFE,
        (
            "Boss Portos told me to go\x01",
            "apologize to Norman, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "I don't see why I've gotta go apologize even\x01",
            "though they're the ones accusin' us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Well, I guess insulting his son\x01",
            "WAS kind of a low blow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Hmm, I just can't accept it.\x02",
    )

    CloseMessageWindow()

    label("loc_29E8")

    Jump("loc_2AC5")

    label("loc_29EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A36")

    ChrTalk(    #110
        0xFE,
        (
            "Man of the sea, Portos! Vote\x01",
            "in the election for Portoooos!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC5")

    label("loc_2A36")

    OP_A2(0x2)

    ChrTalk(    #111
        0xFE,
        (
            "Man of the sea, Portos! Vote\x01",
            "in the election for Portoooos!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Portos will protect your harbor!\x01",
            "Vote for the man of the sea, Portos!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC5")

    TalkEnd(0xFE)
    Return()

    # Function_10_24FF end

    def Function_11_2AC9(): pass

    label("Function_11_2AC9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B60")

    ChrTalk(    #113
        0x9,
        "So this is the problematic warehouse block.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "To develop as a tourist hub we'll need\x01",
            "to do something about this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2A")

    label("loc_2B60")

    OP_A2(0x1)

    ChrTalk(    #115
        0x9,
        (
            "So this is the problematic warehouse block.\x01",
            "Seems like it attracts 'rats' of all sorts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "I asked for an escort since I heard\x01",
            "it was dangerous, but perhaps that was\x01",
            "a bit of an exaggeration?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2A")

    TalkEnd(0xFE)
    Return()

    # Function_11_2AC9 end

    def Function_12_2C2E(): pass

    label("Function_12_2C2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEF")

    ChrTalk(    #117
        0xFE,
        "Heeey, good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I was just reporting to the mayor's mansion\x01",
            "about the case at the academy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I'm gonna take a break here before\x01",
            "I head back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2D98")

    label("loc_2CEF")


    ChrTalk(    #120
        0xFE,
        (
            "I was just reporting to the mayor's mansion\x01",
            "about the case at the academy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Apparently you guys took care of everything\x01",
            "no prob. Great work as always, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D98")

    Jump("loc_2EAB")

    label("loc_2D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2DA5")
    Jump("loc_2EAB")

    label("loc_2DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E56")

    ChrTalk(    #122
        0xFE,
        (
            "Didn't think I'd end up escorting\x01",
            "someone INSIDE the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I feel kind of responsible as a local bracer,\x01",
            "like Ruan is a dangerous place suddenly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EAB")

    label("loc_2E56")

    OP_A2(0x0)

    ChrTalk(    #124
        0xFE,
        "Ah, good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I'm escorting a merchant who's\x01",
            "come to inspect the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAB")

    TalkEnd(0xFE)
    Return()

    # Function_12_2C2E end

    def Function_13_2EAF(): pass

    label("Function_13_2EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2EBA")
    Return()

    label("loc_2EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2ED9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2ED5")
    Jump("loc_2ED6")

    label("loc_2ED5")

    Return()

    label("loc_2ED6")

    Jump("loc_2EFA")

    label("loc_2ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2EE4")
    Return()

    label("loc_2EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EF3")
    Return()

    label("loc_2EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2EFA")

    label("loc_2EFA")

    OP_4A(0xA, 0)

    ChrTalk(    #126 op#A
        0xA,
        (
            "#4AMayoral candidate Portos!\x01",
            "Please, your vote for Portos!\x02",
        )
    )

    Sleep(2000)
    OP_4B(0xA, 0)
    Return()

    # Function_13_2EAF end

    def Function_14_2F47(): pass

    label("Function_14_2F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F52")
    Return()

    label("loc_2F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2F5C")
    Jump("loc_2F85")

    label("loc_2F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2F67")
    Return()

    label("loc_2F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F75")
    Jump("loc_2F85")

    label("loc_2F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F85")
    Return()

    label("loc_2F85")

    OP_4A(0xC, 0)

    ChrTalk(    #127 op#A
        0xC,
        "#4APortos! Vote for Portos, please!\x02",
    )

    Sleep(2000)
    OP_4B(0xC, 0)
    Return()

    # Function_14_2F47 end

    def Function_15_2FBB(): pass

    label("Function_15_2FBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_302D")

    ChrTalk(    #128
        0xFE,
        "Hey. Did you find what you're looking for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "It seems you're in a hurry, but be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3828")

    label("loc_302D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3393")
    OP_8C(0xFE, 225, 0)
    OP_4A(0xFE, 255)
    EventBegin(0x0)
    Fade(500)
    OP_6D(25350, 0, 25220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 26090, 0, 25080, 270)
    SetChrPos(0x102, 26250, 0, 24080, 270)
    SetChrPos(0xF8, 27170, 0, 24990, 270)
    SetChrPos(0xF9, 27360, 0, 23940, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #130
        0x101,
        "#1025F#4PUm, pardon us.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #131
        0xFE,
        "#6PCan I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        "#1040F#2PYes. Do you have a moment?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #133
        (
            "\x07\x05Estelle explained the situation and showed\x01",
            "Portos the letter from the Factory Chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #134
        0xFE,
        (
            "#6PIt's true I'm responsible\x01",
            "for the harbor block, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "#6PYou'd be better off asking Harg about this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#1015F#4PHarg?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "#6PYes, he's responsible for freight handling\x01",
            "in our harbor at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "#6PHe should be on the other side\x01",
            "of this embankment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1006F#4PAll right. He's not too far, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#1040F#2PLet's go talk to him.\x02\x03",

            "Thank you for your assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "#6PAh, be careful. Don't run off\x01",
            "and fall into the sea.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20D5)
    EventEnd(0x0)
    Jump("loc_3403")

    label("loc_3393")


    ChrTalk(    #142
        0xFE,
        (
            "You should ask Harg about\x01",
            "what you're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "He should be on the other side\x01",
            "of this embankment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3403")

    Jump("loc_3828")

    label("loc_3406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_35D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3547")

    ChrTalk(    #144
        0xFE,
        (
            "I have a good relationship with the\x01",
            "new mayor, Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "We may have competed in the election,\x01",
            "but we both love our hometown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "As long as we can cooperate, I'm sure\x01",
            "we can build a future for the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Of course, before that, we need to do\x01",
            "something about this situation, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_35CE")

    label("loc_3547")


    ChrTalk(    #148
        0xFE,
        (
            "I have a good relationship with the\x01",
            "new mayor, Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "To overcome this situation, more than\x01",
            "anything, we need to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35CE")

    Jump("loc_3828")

    label("loc_35D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3784")

    ChrTalk(    #150
        0xFE,
        (
            "I talked with Mayor Norman, and for the\x01",
            "moment we've decided to store general\x01",
            "goods in our warehouses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "This should allow us to make sure the\x01",
            "citizens get food supplies and basic\x01",
            "needs stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "It seems there's a great deal of criticism\x01",
            "being put on the new mayor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "Both the mayor and I want to protect Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I intend to work with him and continue\x01",
            "to support the lives of our citizens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3828")

    label("loc_3784")


    ChrTalk(    #155
        0xFE,
        (
            "Anyway, we've decided to collect\x01",
            "general goods in our warehouses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "This should allow us to make sure the\x01",
            "citizens get food supplies and basic\x01",
            "needs stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3828")

    TalkEnd(0xFE)
    Return()

    # Function_15_2FBB end

    def Function_16_382C(): pass

    label("Function_16_382C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E4")

    ChrTalk(    #157
        0xFE,
        (
            "I thought no one was lookin', so\x01",
            "I took a little breather, ya know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "Just then, Rocco came by on patrol.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "Man, lately he's been workin' real hard.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_392D")

    label("loc_38E4")


    ChrTalk(    #160
        0xFE,
        "What happened to that guy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "Lately he's been workin' real hard.\x02",
    )

    CloseMessageWindow()

    label("loc_392D")

    Jump("loc_3A90")

    label("loc_3930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3A90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A16")

    ChrTalk(    #162
        0xFE,
        (
            "The bridge's stuck up, so\x01",
            "you can't cross this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "There's ferries by the warehouses, so if you're\x01",
            "headin' to the North Block best ya use those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "Lately our members have been\x01",
            "workin' as guides.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3A90")

    label("loc_3A16")


    ChrTalk(    #165
        0xFE,
        (
            "Use the ferry if you're headin'\x01",
            "to the North Block, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "The sign of a guide is this kickin' red bandana!\x02",
    )

    CloseMessageWindow()

    label("loc_3A90")

    TalkEnd(0xFE)
    Return()

    # Function_16_382C end

    def Function_17_3A94(): pass

    label("Function_17_3A94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B56")

    ChrTalk(    #167
        0xFE,
        "Lately, the people in town are real nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "A girl I don't even know said thanks a bit ago...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Guess the Goddess really must be\x01",
            "watching from somewhere, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_3BC9")

    label("loc_3B56")


    ChrTalk(    #170
        0xFE,
        "Lately, the people in town are real nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Guess the Goddess really must be\x01",
            "watching from somewhere, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC9")

    Jump("loc_3CBF")

    label("loc_3BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C39")

    ChrTalk(    #172
        0xFE,
        (
            "Boats headed to the North Block\x01",
            "are departing from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "Please wait in line.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_3CBF")

    label("loc_3C39")


    ChrTalk(    #174
        0xFE,
        (
            "Boats headed to the North Block\x01",
            "are departing from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "The mayor treated us to it, so we\x01",
            "gotta use it or it'd be a waste.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBF")

    TalkEnd(0xFE)
    Return()

    # Function_17_3A94 end

    def Function_18_3CC3(): pass

    label("Function_18_3CC3")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #176
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_3CC3 end

    def Function_19_3D12(): pass

    label("Function_19_3D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4064")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_3EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3DEE")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #177
        0x106,
        (
            "#050FWe still haven't asked Belden about \x01",
            "the ghost.\x02\x03",

            "We can leave town after that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #178
        0x101,
        (
            "#1007FAh, right.\x02\x03",

            "#1006FIt was the house to the right of\x01",
            "the mayor's mansion, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EB3")

    label("loc_3DEE")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #179
        0x103,
        (
            "#020FWe still haven't asked that kid\x01",
            "about the ghost.\x02\x03",

            "Let's leave the town after that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #180
        0x101,
        (
            "#1007FAh, right.\x02\x03",

            "#1006FIt was the house to the right of\x01",
            "the mayor's mansion, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB3")

    Jump("loc_4049")

    label("loc_3EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F83")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #181
        0x106,
        (
            "#050FWe still haven't asked the Ravens\x01",
            "about the ghost.\x02\x03",

            "We can leave town after that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #182
        0x101,
        (
            "#1007FAh, that's right.\x02\x03",

            "#1006FWe need to go to the warehouses\x01",
            "in the harbor block.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4049")

    label("loc_3F83")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #183
        0x103,
        (
            "#020FWe still haven't asked the Ravens\x01",
            "about the ghost.\x02\x03",

            "Let's leave the town after that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #184
        0x101,
        (
            "#1007FAh, that's right.\x02\x03",

            "#1006FWe need to go to the warehouses\x01",
            "in the harbor block.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4049")

    OP_90(0x0, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4064")

    Return()

    # Function_19_3D12 end

    def Function_20_4065(): pass

    label("Function_20_4065")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408A")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_408A")

    Fade(1000)
    OP_6D(4330, -1800, 24700, 0)
    OP_67(0, 6230, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(282, 0)
    SetChrPos(0x101, 5170, -1800, 23340, 270)
    SetChrPos(0x102, 5260, -1800, 24300, 270)
    SetChrPos(0xF8, 6400, -1800, 22950, 270)
    SetChrPos(0xF9, 6380, -1800, 24230, 270)
    OP_4A(0xC, 255)
    OP_0D()

    ChrTalk(    #185
        0x101,
        "#1011F#6PUmm, may I have a moment?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #186
        0xC,
        "#6PWhat is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #187
        (
            "\x07\x05Estelle explained the situation and showed Harg the\x01",
            "letter from the Factory Chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #188
        0xC,
        (
            "#6PGasoline...? Yeah, we got some.\x02\x03",

            "I was just about to send it to Zeiss when\x01",
            "all this happened, so we're securing it in\x01",
            "the warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#1006F#6PGreat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x102,
        "#1040F#4PCould we take it from here, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        (
            "#6PI don't mind, but there's a lot of it,\x01",
            "ya know?\x02\x03",

            "I really don't think you could carry all of it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_437C")

    ChrTalk(    #192
        0x103,
        (
            "#026F#4PHmmm...\x02\x03",

            "#020FFor now, how about as much as we\x01",
            "could carry? That should be enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4435")

    label("loc_437C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43DE")

    ChrTalk(    #193
        0x106,
        (
            "#053F#4PGood point...\x02\x03",

            "#051FFor now, let's just carry whatever we can take.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4435")

    label("loc_43DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4435")

    ChrTalk(    #194
        0x108,
        (
            "#074F#4PTrue...\x02\x03",

            "#070FLet's just take whatever we can lift for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4435")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_6F(0x15, 60)
    SetChrPos(0x13, 24000, 1000, 4010, 315)
    SetChrPos(0x14, 23300, 1000, 4010, 315)
    SetChrPos(0x15, 22600, 1000, 4010, 315)
    OP_A1(0x13, 0x27)
    OP_72(0x27, 0x4)
    OP_A1(0x14, 0x28)
    OP_72(0x28, 0x4)
    OP_A1(0x15, 0x29)
    OP_72(0x29, 0x4)
    OP_6D(24300, 500, 4860, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23900, 0, 6280, 180)
    SetChrPos(0x102, 22750, 0, 6280, 180)
    SetChrPos(0xF8, 22200, 0, 7500, 180)
    SetChrPos(0xF9, 23870, 0, 7500, 180)
    SetChrPos(0xC, 23300, 250, 4960, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_8C(0xC, 0, 400)

    ChrTalk(    #195
        0xC,
        "#4PHmm... This enough?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45C3")

    ChrTalk(    #196
        0x107,
        (
            "#560F#5PYes, that should be enough to\x01",
            "keep them for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45FA")

    label("loc_45C3")


    ChrTalk(    #197
        0x102,
        "#1040F#5PYeah, that should be enough for the job.\x02",
    )

    CloseMessageWindow()

    label("loc_45FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463A")

    ChrTalk(    #198
        0x108,
        "#071F#5PWell, this much is easy to carry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4700")

    label("loc_463A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4682")

    ChrTalk(    #199
        0x106,
        "#051F#5PThis much shouldn't be a problem to haul.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4700")

    label("loc_4682")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4700")

    ChrTalk(    #200
        0x103,
        (
            "#524F#5P*sigh* We shouldn't have any problem\x01",
            "lugging this around, but I foresee sore\x01",
            "muscles in my future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4700")

    Sleep(200)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #201
        "\x07\x00Received #1036i x 3.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x40C, 3)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    Sleep(500)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x0)
    OP_73(0x15)
    SetChrPos(0xC, 23290, 1000, 3980, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #202
        0xC,
        (
            "#4PWell, if ya need anything\x01",
            "else come on by again.\x02\x03",

            "Well, hopefully this whole mess will\x01",
            "be sorted before that, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#1007F#5PYeah, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x102,
        "#1040F#5PSorry for the trouble.\x02",
    )

    CloseMessageWindow()

    def lambda_4868():

        label("loc_4868")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4868")

    QueueWorkItem2(0x101, 1, lambda_4868)

    def lambda_4879():

        label("loc_4879")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_4879")

    QueueWorkItem2(0x102, 1, lambda_4879)

    def lambda_488A():

        label("loc_488A")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_488A")

    QueueWorkItem2(0xF8, 1, lambda_488A)

    def lambda_489B():

        label("loc_489B")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_489B")

    QueueWorkItem2(0xF9, 1, lambda_489B)

    def lambda_48AC():
        OP_6D(26650, 0, 7870, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48AC)
    OP_8E(0xC, 0x6F54, 0x0, 0x1ED2, 0xBB8, 0x0)
    OP_8E(0xC, 0x6F54, 0x14A, 0x43DA, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(24210, 0, 5890, 1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B19")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as got Combustion Engine\x01",                                                                          # 0
            "Set as no Combustion Engine, but Kilika said to inquire at the Fortress\x01",                               # 1
            "Set as no Combustion Engine, but talked to Samuel about Combustion Engine\x01",                             # 2
            "Set as no Combustion Engine and have not asked at Fortress, but have talked to Maintenance Chief\x01",      # 3
            "Set as no Combustion Engine, have not asked Fortress, have not talked to Maintenance Chief\x01",            # 4
            "No Change\x01",                                                                                             # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4AD7"),
        (1, "loc_4ADD"),
        (2, "loc_4AEC"),
        (3, "loc_4AFB"),
        (4, "loc_4B0A"),
        (SWITCH_DEFAULT, "loc_4B19"),
    )


    label("loc_4AD7")

    OP_A2(0x200F)
    Jump("loc_4B19")

    label("loc_4ADD")

    OP_A3(0x200F)
    OP_A2(0x200B)
    OP_A2(0x200C)
    OP_A3(0x200E)
    Jump("loc_4B19")

    label("loc_4AEC")

    OP_A3(0x200F)
    OP_A2(0x200B)
    OP_A3(0x200C)
    OP_A2(0x200E)
    Jump("loc_4B19")

    label("loc_4AFB")

    OP_A3(0x200F)
    OP_A2(0x200B)
    OP_A3(0x200C)
    OP_A3(0x200E)
    Jump("loc_4B19")

    label("loc_4B0A")

    OP_A3(0x200F)
    OP_A3(0x200B)
    OP_A3(0x200C)
    OP_A3(0x200E)
    Jump("loc_4B19")

    label("loc_4B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_4D22")
    OP_28(0xC2, 0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C0C")

    def lambda_4B3A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4B3A)
    Sleep(100)

    def lambda_4B4D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4B4D)
    Sleep(100)

    def lambda_4B60():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B60)
    Sleep(100)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #205
        0x101,
        (
            "#1006F#7PNow, then...\x01",
            "That's the fuel taken care of.\x02\x03",

            "Shall we get back to Elmo and\x01",
            "upgrade the pump?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #206
        0x107,
        "#061FYup, I'm ready whenever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D1F")

    label("loc_4C0C")


    def lambda_4C12():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4C12)
    Sleep(100)

    def lambda_4C25():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4C25)
    Sleep(100)

    def lambda_4C38():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C38)
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #207
        0x101,
        (
            "#1006F#6PNow, then...\x01",
            "That's the fuel taken care of.\x02\x03",

            "#1015FWe can't really upgrade the pump\x01",
            "without Tita, though, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#1040F#4PRight.\x02\x03",

            "Let's return to the guild for the\x01",
            "moment and meet up with Tita.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1F")

    Jump("loc_4F63")

    label("loc_4D22")


    def lambda_4D28():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4D28)
    Sleep(100)

    def lambda_4D3B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4D3B)
    Sleep(100)

    def lambda_4D4E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D4E)
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #209
        0x101,
        (
            "#1006F#6POkay, that's the gasoline checked off.\x02\x03",

            "#1015FNow we just need the engine, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E56")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #210
        0x102,
        (
            "#1040F#4PIt seems the ship that landed in\x01",
            "the Tratt Plains was carrying it.\x02\x03",

            "Let's try there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1006F#6PYeah, got it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F63")

    label("loc_4E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_END)), "loc_4EE9")

    ChrTalk(    #212
        0x102,
        (
            "#1035F#4PIt seems it was lent out to the Royal Army.\x02\x03",

            "#1040FWe'll have to inquire at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        "#1006F#6PI see, got it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F63")

    label("loc_4EE9")


    ChrTalk(    #214
        0x102,
        (
            "#1040F#4PAs I recall, Gustav was in charge of that.\x02\x03",

            "Let's go to the Zeiss Landing Port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#1006F#6PYeah, got it.\x02",
    )

    CloseMessageWindow()

    label("loc_4F63")

    OP_A2(0x2011)
    OP_A2(0xB)
    OP_28(0xC2, 0x1, 0x800)
    SetChrPos(0xC, 3800, -1800, 23920, 270)
    ClearChrFlags(0xC, 0x10)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_20_4065 end

    def Function_21_4F8C(): pass

    label("Function_21_4F8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FAE")
    Call(0, 24)
    Call(0, 25)

    label("loc_4FAE")

    OP_D2(0x270003, 0x270007, 0x16)
    OP_D2(0x270013, 0x270017, 0x17)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_4FDB"),
        (5, "loc_4FE8"),
        (6, "loc_4FF5"),
        (7, "loc_5002"),
        (SWITCH_DEFAULT, "loc_500F"),
    )


    label("loc_4FDB")

    OP_D2(0x70023, 0x7002B, 0x18)
    Jump("loc_500F")

    label("loc_4FE8")

    OP_D2(0x70053, 0x7005B, 0x18)
    Jump("loc_500F")

    label("loc_4FF5")

    OP_D2(0x70063, 0x7006B, 0x18)
    Jump("loc_500F")

    label("loc_5002")

    OP_D2(0x70073, 0x7007B, 0x18)
    Jump("loc_500F")

    label("loc_500F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_5028"),
        (5, "loc_5035"),
        (6, "loc_5042"),
        (7, "loc_504F"),
        (SWITCH_DEFAULT, "loc_505C"),
    )


    label("loc_5028")

    OP_D2(0x70023, 0x7002B, 0x19)
    Jump("loc_505C")

    label("loc_5035")

    OP_D2(0x70053, 0x7005B, 0x19)
    Jump("loc_505C")

    label("loc_5042")

    OP_D2(0x70063, 0x7006B, 0x19)
    Jump("loc_505C")

    label("loc_504F")

    OP_D2(0x70073, 0x7007B, 0x19)
    Jump("loc_505C")

    label("loc_505C")

    SetChrChipByIndex(0x101, 22)
    SetChrChipByIndex(0x102, 23)
    SetChrChipByIndex(0xF8, 24)
    SetChrChipByIndex(0xF9, 25)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    PlayEffect(0x0, 0x0, 0x24, 0, -100, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2A, 0x4)
    OP_71(0x2A, 0x2)
    OP_71(0x2A, 0x40)
    OP_71(0x2A, 0x20)
    OP_B0(0x2A, 0x1E)
    OP_6F(0x2A, 1)
    OP_70(0x2A, 0xF0)
    OP_A1(0x24, 0x2A)
    SetChrFlags(0x24, 0x40)
    SetChrPos(0x24, 4000, -2900, 14170, 180)
    OP_8C(0x24, 90, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)
    OP_48()
    OP_8C(0x24, 270, 0)
    OP_89(0x101, 4900, -2800, 13940, 90)
    OP_89(0x102, 4900, -2800, 14580, 90)
    OP_89(0xF8, 3550, -2800, 14580, 90)
    OP_89(0xF9, 3550, -2800, 13940, 90)
    OP_89(0x22, 2900, -3000, 13800, 180)
    SetChrBattleFlags(0x22, 0x20)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_48()
    OP_6D(15100, -1800, 13700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_5231():

        label("loc_5231")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5231")

    QueueWorkItem2(0x16, 1, lambda_5231)

    def lambda_5242():

        label("loc_5242")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5242")

    QueueWorkItem2(0x17, 1, lambda_5242)

    def lambda_5253():

        label("loc_5253")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5253")

    QueueWorkItem2(0x18, 1, lambda_5253)

    def lambda_5264():

        label("loc_5264")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5264")

    QueueWorkItem2(0x19, 1, lambda_5264)

    def lambda_5275():

        label("loc_5275")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5275")

    QueueWorkItem2(0x1A, 1, lambda_5275)

    def lambda_5286():

        label("loc_5286")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5286")

    QueueWorkItem2(0x1B, 1, lambda_5286)

    def lambda_5297():

        label("loc_5297")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_5297")

    QueueWorkItem2(0x1C, 1, lambda_5297)

    def lambda_52A8():

        label("loc_52A8")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_52A8")

    QueueWorkItem2(0x1D, 1, lambda_52A8)

    def lambda_52B9():

        label("loc_52B9")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_52B9")

    QueueWorkItem2(0x1E, 1, lambda_52B9)

    def lambda_52CA():

        label("loc_52CA")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_52CA")

    QueueWorkItem2(0x1F, 1, lambda_52CA)

    def lambda_52DB():

        label("loc_52DB")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_52DB")

    QueueWorkItem2(0x20, 1, lambda_52DB)

    def lambda_52EC():

        label("loc_52EC")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_52EC")

    QueueWorkItem2(0x21, 1, lambda_52EC)

    def lambda_52FD():
        OP_8F(0xFE, 0x4650, 0xFFFFF4AC, 0x375A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_52FD)

    def lambda_5318():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5318)

    def lambda_5333():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5333)

    def lambda_534E():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_534E)

    def lambda_5369():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5369)

    def lambda_5384():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5384)
    Sleep(2000)

    def lambda_53A4():
        OP_6D(17380, -1800, 13360, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_53A4)
    Sleep(4000)

    def lambda_53C1():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x375A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_53C1)

    def lambda_53DC():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_53DC)

    def lambda_53F7():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53F7)

    def lambda_5412():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5412)

    def lambda_542D():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_542D)

    def lambda_5448():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5448)
    Sleep(2000)

    def lambda_5468():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x375A, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5468)

    def lambda_5483():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_5483)

    def lambda_549E():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_549E)

    def lambda_54B9():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54B9)

    def lambda_54D4():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_54D4)

    def lambda_54EF():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_54EF)
    WaitChrThread(0x24, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_82(0x0, 0x2)
    OP_44(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x24, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0x0, 18420, 0, 6280, 90)
    SetChrPos(0x1, 18420, 0, 6280, 90)
    SetChrPos(0x2, 18420, 0, 6280, 90)
    SetChrPos(0x3, 18420, 0, 6280, 90)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0xF8, 0x1)
    SetChrFlags(0xF9, 0x1)
    ClearChrFlags(0x22, 0x20)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0xF8, 0x20)
    ClearChrFlags(0xF9, 0x20)
    OP_6D(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x2A, 0x4)
    SetChrFlags(0x22, 0x80)
    SetChrPos(0x16, 18790, -1800, 11600, 0)
    SetChrPos(0x17, 17990, -1800, 11600, 90)
    SetChrPos(0x18, 17220, -1800, 11420, 90)
    SetChrPos(0x19, 16490, -1800, 11290, 90)
    SetChrPos(0x1A, 15770, -1800, 11470, 90)
    SetChrPos(0x1B, 15050, -1800, 11610, 90)
    SetChrPos(0x1C, 14440, -1800, 10960, 45)
    SetChrPos(0x1D, 14560, -1800, 10210, 0)
    SetChrPos(0x1E, 14410, -1800, 9520, 0)
    SetChrPos(0x1F, 14460, -1800, 8730, 0)
    SetChrPos(0x20, 14350, -1800, 7960, 0)
    SetChrPos(0x21, 14470, -1800, 7260, 0)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x1F, 255)
    OP_4B(0x20, 255)
    OP_4B(0x21, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_DC()
    EventEnd(0x0)
    Return()

    # Function_21_4F8C end

    def Function_22_573E(): pass

    label("Function_22_573E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_574B")
    Return()

    label("loc_574B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 5)), scpexpr(EXPR_END)), "loc_5757")
    Call(0, 23)
    Return()

    label("loc_5757")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5777")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_5777")

    OP_A2(0x2035)
    Fade(1000)
    SetChrPos(0x101, 16260, -1300, 6720, 310)
    SetChrPos(0x102, 16260, -1300, 5650, 310)
    SetChrPos(0xF8, 17170, -550, 6760, 310)
    SetChrPos(0xF9, 17240, -550, 5550, 310)
    OP_6D(17120, -1300, 7040, 0)
    OP_67(0, 4230, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(134000, 0)
    OP_6E(481, 0)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5967")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as stopped by Jean's place (Ruan Branch phone fixed)\x01",                  # 0
            "Set as not yet stopped by Jean's place (Ruan Branch phone not fixed)\x01",      # 1
            "No change\x01",                                                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5908"),
        (1, "loc_590E"),
        (SWITCH_DEFAULT, "loc_5914"),
    )


    label("loc_5908")

    OP_A2(0x2001)
    Jump("loc_5914")

    label("loc_590E")

    OP_A3(0x2001)
    Jump("loc_5914")

    label("loc_5914")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_END)), "loc_592F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_592F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_5940")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_END)), "loc_5951")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5964")
    OP_A2(0x2091)
    Jump("loc_5967")

    label("loc_5964")

    OP_A3(0x2091)

    label("loc_5967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFB")

    ChrTalk(    #216
        0x101,
        "#1004F#6PWhat's all this about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x102,
        (
            "#1042F#4PSomething seems to be causing\x01",
            "a lot of confusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_59F1():
        OP_6D(17090, -1800, 5230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_59F1)
    TurnDirection(0x21, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #218
        0x21,
        (
            "#4PYou kids looking to cross\x01",
            "over to the other side?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(16700, -1050, 7050, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1630, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_0D()

    def lambda_5A97():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A97)
    Sleep(100)

    def lambda_5AAA():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5AAA)
    Sleep(100)

    def lambda_5ABD():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5ABD)
    Sleep(100)
    OP_8C(0xF9, 270, 400)

    ChrTalk(    #219
        0x101,
        "#1004F#4PHuh? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x21,
        (
            "#5PWhat do I...?\x02\x03",

            "Don't you know the Langland Bridge isn't\x01",
            "working and stuck raised right now?\x02\x03",

            "Thanks to that, we've got to use\x01",
            "boats to get across the river now.\x02\x03",

            "And this is the dock we're using!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1007F#4PThe bridge is stuck?\x01",
            "Oh, man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        (
            "#1043F#2PWell, that's...inconvenient,\x01",
            "to say the least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x21,
        (
            "#5PNo kidding it's inconvenient.\x01",
            "Frankly, I don't think the city\x01",
            "can take much more of this.\x02\x03",

            "At the direction of the mayor,\x01",
            "rides are free.\x02\x03",

            "But...thanks to that, we end\x01",
            "up backed up half an hour.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4B")

    label("loc_5CFB")


    ChrTalk(    #224
        0x101,
        "#1004F#6POh, this must be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x102,
        "#1042F#4PThis must be the ferry Jean mentioned.\x02",
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5D6F():
        OP_6D(17090, -1800, 5230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5D6F)
    TurnDirection(0x21, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #226
        0x21,
        (
            "#4PYou kids looking to cross\x01",
            "over to the other side?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(16700, -1050, 7050, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1630, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_0D()

    def lambda_5E15():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E15)
    Sleep(100)

    def lambda_5E28():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E28)
    Sleep(100)

    def lambda_5E3B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5E3B)
    Sleep(100)
    OP_8C(0xF9, 270, 400)

    ChrTalk(    #227
        0x101,
        (
            "#1025F#4PEr, yes! We'd like to, but, um...\x02\x03",

            "How much does it cost, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x21,
        (
            "#5PNo fare, miss, by order of the mayor.\x02\x03",

            "The wait's going to be about\x01",
            "half an hour or so, though.\x02\x03",

            "This whole thing's been murder\x01",
            "on the residents, let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F87")

    ChrTalk(    #229
        0x107,
        "#065F#4PAwwww! That's almost forever!\x02",
    )

    CloseMessageWindow()
    Jump("loc_600E")

    label("loc_5F87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FC6")

    ChrTalk(    #230
        0x103,
        "#025F#4PThat...would be a bit of a wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_600E")

    label("loc_5FC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_600E")

    ChrTalk(    #231
        0x106,
        (
            "#052F#4PThat's a bit more of a wait\x01",
            "than I expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_600E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6069")

    ChrTalk(    #232
        0x108,
        (
            "#074F#4PIt has to go there and back.\x01",
            "There's not much anyone can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_613E")

    label("loc_6069")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60D2")

    ChrTalk(    #233
        0x106,
        (
            "#053F#4PIt's gotta get passengers on both sides\x01",
            "of the river. Not much you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_613E")

    label("loc_60D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_613E")

    ChrTalk(    #234
        0x103,
        (
            "#025F#4PWell, considering it has to ferry\x01",
            "both ways, there's not much for it,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_613E")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #235
        0x102,
        (
            "#1042F#2PWell, how about it, Estelle?\x01",
            "Shall we cross over?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #236
        0x101,
        "#1015F#6PUm...\x02",
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
            "Cross to the North Side\x01",      # 0
            "Waiting is Evil!\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6374")

    ChrTalk(    #237
        0x101,
        (
            "#1025F#6PNo, not yet, I think.\x02\x03",

            "There's still some stuff we've\x01",
            "got to do over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        (
            "#1040F#2PAll right, then.\x01",
            "Let's get out of the way.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 18420, 0, 6280, 90)
    SetChrPos(0x1, 18420, 0, 6280, 90)
    SetChrPos(0x2, 18420, 0, 6280, 90)
    SetChrPos(0x3, 18420, 0, 6280, 90)
    OP_69(0x0, 0x0)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x1F, 255)
    OP_4B(0x20, 255)
    OP_4B(0x21, 255)
    OP_8C(0x21, 0, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_6374")

    OP_A2(0x2036)

    ChrTalk(    #239
        0x101,
        (
            "#1007F#6PDoesn't look like there's any\x01",
            "other way across, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        "#1040F#2PLet's get in line, then.\x02",
    )

    CloseMessageWindow()
    OP_DB()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(15520, -1550, 8870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1A, 18790, -1800, 11600, 0)
    SetChrPos(0x1B, 17990, -1800, 11600, 90)
    SetChrPos(0x1C, 17220, -1800, 11420, 90)
    SetChrPos(0x1D, 16490, -1800, 11290, 90)
    SetChrPos(0x1E, 15770, -1800, 11470, 90)
    SetChrPos(0x1F, 15050, -1800, 11610, 90)
    SetChrPos(0x20, 14440, -1800, 10960, 45)
    SetChrPos(0x21, 14560, -1800, 10210, 0)
    SetChrPos(0x101, 14410, -1800, 9520, 0)
    SetChrPos(0x102, 14460, -1800, 8730, 0)
    SetChrPos(0xF8, 14350, -1800, 7960, 0)
    SetChrPos(0xF9, 14470, -1800, 7260, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(14870, -1800, 11420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1E, 18790, -1800, 11600, 0)
    SetChrPos(0x1F, 17990, -1800, 11600, 90)
    SetChrPos(0x20, 17220, -1800, 11420, 90)
    SetChrPos(0x21, 16490, -1800, 11290, 90)
    SetChrPos(0x101, 15770, -1800, 11470, 90)
    SetChrPos(0x102, 15050, -1800, 11610, 90)
    SetChrPos(0xF8, 14440, -1800, 10960, 45)
    SetChrPos(0xF9, 14560, -1800, 10210, 0)
    SetChrPos(0x18, 14410, -1800, 9520, 0)
    SetChrPos(0x16, 14460, -1800, 8730, 0)
    SetChrPos(0x19, 14350, -1800, 7960, 0)
    SetChrPos(0x17, 14470, -1800, 7260, 0)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(17470, -1800, 11460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 18790, -1800, 11600, 0)
    SetChrPos(0x102, 17990, -1800, 11600, 90)
    SetChrPos(0xF8, 17220, -1800, 11420, 90)
    SetChrPos(0xF9, 16490, -1800, 11290, 90)
    SetChrPos(0x18, 15770, -1800, 11470, 90)
    SetChrPos(0x16, 15050, -1800, 11610, 90)
    SetChrPos(0x19, 14440, -1800, 10960, 45)
    SetChrPos(0x17, 14560, -1800, 10210, 0)
    SetChrPos(0x1A, 14410, -1800, 9520, 0)
    SetChrPos(0x1C, 14460, -1800, 8730, 0)
    SetChrPos(0x1B, 14350, -1800, 7960, 0)
    SetChrPos(0x1D, 14470, -1800, 7260, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(18450, -1800, 12450, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(135000, 0)
    OP_6E(381, 0)
    SetChrPos(0x101, 19290, -1800, 11600, 0)
    SetChrPos(0x102, 18490, -1800, 11600, 0)
    SetChrPos(0xF8, 17720, -1800, 11420, 0)
    SetChrPos(0xF9, 16990, -1800, 11290, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0x24, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2A, 0x4)
    OP_72(0x2A, 0x2)
    OP_71(0x2A, 0x400)
    OP_71(0x2A, 0x40)
    OP_71(0x2A, 0x20)
    OP_B0(0x2A, 0x1E)
    OP_6F(0x2A, 1)
    OP_70(0x2A, 0xF0)
    OP_A1(0x24, 0x2A)
    SetChrFlags(0x24, 0x40)
    SetChrPos(0x24, 18170, -2900, 14170, 90)
    OP_8C(0x24, 90, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    ClearChrBattleFlags(0x22, 0x20)
    SetChrPos(0x22, 19600, -3000, 14300, 180)
    OP_48()
    FadeToBright(1000, 0)
    OP_0D()
    OP_DC()

    ChrTalk(    #241
        0x22,
        (
            "#6PSorry for the wait.\x01",
            "It's your turn next.\x02\x03",

            "Onto the boat, now, come on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        "#1006F#4POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        "#1040F#4PThank you.\x02",
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2100   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_22_573E end

    def Function_23_69B3(): pass

    label("Function_23_69B3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69D3")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_69D3")

    Fade(1000)
    SetChrPos(0x101, 16260, -1300, 6720, 270)
    SetChrPos(0x102, 16260, -1300, 5650, 270)
    SetChrPos(0xF8, 17170, -550, 6760, 270)
    SetChrPos(0xF9, 17240, -550, 5550, 270)
    OP_6D(16700, -1050, 7050, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(1640, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AEA")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #244
        0x102,
        (
            "#1042FWell, how about it, Estelle?\x01",
            "Shall we cross over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        "#1015F#6PUm...\x02",
    )

    CloseMessageWindow()

    label("loc_6AEA")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cross to the North Side\x01",      # 0
            "Waiting is Evil!\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF4")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #246
        0x101,
        (
            "#1025F#6PNo, not yet, I think.\x02\x03",

            "There's still some stuff we've\x01",
            "got to do over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x102,
        (
            "#1040FAll right, then.\x01",
            "Let's get out of the way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 18420, 0, 6280, 90)
    SetChrPos(0x1, 18420, 0, 6280, 90)
    SetChrPos(0x2, 18420, 0, 6280, 90)
    SetChrPos(0x3, 18420, 0, 6280, 90)
    OP_69(0x0, 0x0)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x1F, 255)
    OP_4B(0x20, 255)
    OP_4B(0x21, 255)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_6CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D42")
    TurnDirection(0x101, 0x102, 400)
    Sleep(700)

    ChrTalk(    #248
        0x101,
        (
            "#1007F#6PDoesn't look like there's any\x01",
            "other way across, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x102,
        "#1040F#2PLet's get in line, then.\x02",
    )

    CloseMessageWindow()

    label("loc_6D42")

    OP_DB()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(15520, -1550, 8870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1A, 18790, -1800, 11600, 0)
    SetChrPos(0x1B, 17990, -1800, 11600, 90)
    SetChrPos(0x1C, 17220, -1800, 11420, 90)
    SetChrPos(0x1D, 16490, -1800, 11290, 90)
    SetChrPos(0x1E, 15770, -1800, 11470, 90)
    SetChrPos(0x1F, 15050, -1800, 11610, 90)
    SetChrPos(0x20, 14440, -1800, 10960, 45)
    SetChrPos(0x21, 14560, -1800, 10210, 0)
    SetChrPos(0x101, 14410, -1800, 9520, 0)
    SetChrPos(0x102, 14460, -1800, 8730, 0)
    SetChrPos(0xF8, 14350, -1800, 7960, 0)
    SetChrPos(0xF9, 14470, -1800, 7260, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(14870, -1800, 11420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1E, 18790, -1800, 11600, 0)
    SetChrPos(0x1F, 17990, -1800, 11600, 90)
    SetChrPos(0x20, 17220, -1800, 11420, 90)
    SetChrPos(0x21, 16490, -1800, 11290, 90)
    SetChrPos(0x101, 15770, -1800, 11470, 90)
    SetChrPos(0x102, 15050, -1800, 11610, 90)
    SetChrPos(0xF8, 14440, -1800, 10960, 45)
    SetChrPos(0xF9, 14560, -1800, 10210, 0)
    SetChrPos(0x18, 14410, -1800, 9520, 0)
    SetChrPos(0x16, 14460, -1800, 8730, 0)
    SetChrPos(0x19, 14350, -1800, 7960, 0)
    SetChrPos(0x17, 14470, -1800, 7260, 0)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(17470, -1800, 11460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 18790, -1800, 11600, 0)
    SetChrPos(0x102, 17990, -1800, 11600, 90)
    SetChrPos(0xF8, 17220, -1800, 11420, 90)
    SetChrPos(0xF9, 16490, -1800, 11290, 90)
    SetChrPos(0x18, 15770, -1800, 11470, 90)
    SetChrPos(0x16, 15050, -1800, 11610, 90)
    SetChrPos(0x19, 14440, -1800, 10960, 45)
    SetChrPos(0x17, 14560, -1800, 10210, 0)
    SetChrPos(0x1A, 14410, -1800, 9520, 0)
    SetChrPos(0x1C, 14460, -1800, 8730, 0)
    SetChrPos(0x1B, 14350, -1800, 7960, 0)
    SetChrPos(0x1D, 14470, -1800, 7260, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(18450, -1800, 12450, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(135000, 0)
    OP_6E(381, 0)
    SetChrPos(0x101, 19290, -1800, 11600, 0)
    SetChrPos(0x102, 18490, -1800, 11600, 0)
    SetChrPos(0xF8, 17720, -1800, 11420, 0)
    SetChrPos(0xF9, 16990, -1800, 11290, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0x24, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2A, 0x4)
    OP_72(0x2A, 0x2)
    OP_71(0x2A, 0x400)
    OP_71(0x2A, 0x40)
    OP_71(0x2A, 0x20)
    OP_B0(0x2A, 0x1E)
    OP_6F(0x2A, 1)
    OP_70(0x2A, 0xF0)
    OP_A1(0x24, 0x2A)
    SetChrFlags(0x24, 0x40)
    SetChrPos(0x24, 18170, -2900, 14170, 90)
    OP_8C(0x24, 90, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    ClearChrBattleFlags(0x22, 0x20)
    SetChrPos(0x22, 19600, -3000, 14200, 180)
    OP_48()
    FadeToBright(1000, 0)
    OP_0D()
    OP_DC()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72FC")
    OP_A2(0x2036)

    ChrTalk(    #250
        0x22,
        (
            "#6PSorry for the wait.\x01",
            "It's your turn next.\x02\x03",

            "Onto the boat, now, come on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        "#1006F#7POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x102,
        "#1040F#7PThank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7362")

    label("loc_72FC")


    ChrTalk(    #253
        0x22,
        (
            "#6PAll right, your turn.\x02\x03",

            "There's a line forming behind ya,\x01",
            "so please hurry and get on the boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7362")

    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2100   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_23_69B3 end

    def Function_24_7387(): pass

    label("Function_24_7387")

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
        (0, "loc_7400"),
        (1, "loc_7406"),
        (SWITCH_DEFAULT, "loc_740C"),
    )


    label("loc_7400")

    OP_A2(0x1200)
    Jump("loc_740C")

    label("loc_7406")

    OP_A2(0x1201)
    Jump("loc_740C")

    label("loc_740C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_741A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_741E")

    label("loc_741A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_741E")

    Return()

    # Function_24_7387 end

    def Function_25_741F(): pass

    label("Function_25_741F")

    ClearMapFlags(0x1)
    OP_6D(122280, 0, 24310, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_25_741F end

    def Function_26_7478(): pass

    label("Function_26_7478")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_26_7478 end

    def Function_27_747F(): pass

    label("Function_27_747F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #254
        (
            "\x07\x05《Ruan Mayoral Election》※ Make sure to go to the voting site\x01",
            "on voting day! -Election Management Committee\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_747F end

    def Function_28_751E(): pass

    label("Function_28_751E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_752B")
    Return()

    label("loc_752B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7547")
    Call(0, 24)
    FadeToBright(0, 0)

    label("loc_7547")

    Fade(1000)
    SetChrPos(0x101, 29960, 1050, 15670, 180)
    SetChrPos(0xF7, 29070, 900, 16290, 180)
    SetChrPos(0x23, 24000, 0, 8780, 90)
    ClearChrFlags(0x23, 0x80)

    def lambda_758A():

        label("loc_758A")

        OP_69(0x25, 0x0)
        OP_48()
        Jump("loc_758A")

    QueueWorkItem2(0x25, 1, lambda_758A)
    OP_43(0x25, 0x2, 0x0, 0x1D)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    def lambda_75CE():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75CE)
    Sleep(200)

    def lambda_75E9():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_75E9)

    def lambda_75FF():
        OP_8E(0xFE, 0x72C4, 0x0, 0x224C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_75FF)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #255
        0x101,
        (
            "#1004FAh...?!\x02\x03",

            "Is that you, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 0x1)
    OP_44(0x25, 0x1)
    OP_44(0x25, 0x2)
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x23, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #256
        0x23,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x23, 0, 400)

    def lambda_76AE():
        OP_8E(0xFE, 0x7332, 0x280, 0x33A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_76AE)
    OP_6D(29180, 1050, 14710, 2000)

    ChrTalk(    #257
        0x23,
        "How about it? Already tried out your rod?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1015FNo, not yet.\x02\x03",

            "I had some places I needed to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x23,
        "I see, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x23,
        "Well, then, want to check out a spot nearby?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x23,
        "I know a really great location.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #262
        0x101,
        "#1018FReally?! Yes, please!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7839")

    ChrTalk(    #263
        0x106,
        (
            "#552F...Hey, weren't we gonna ask\x01",
            "the Ravens about the ghost?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7883")

    label("loc_7839")


    ChrTalk(    #264
        0x103,
        (
            "#023FAhem! Weren't we going to ask those\x01",
            "Raven kids about the ghost?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7883")

    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(1000)

    ChrTalk(    #265
        0x101,
        (
            "#1008FO-Of course! Of course we were.\x02\x03",

            "But, we can make a short stop, right...?\x01",
            "Pleeeeeease?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7943")

    ChrTalk(    #266
        0x106,
        (
            "#551F*sigh* Fine.\x01",
            "Hurry up and get it over with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7981")

    label("loc_7943")


    ChrTalk(    #267
        0x103,
        (
            "#021FGuess there's no stopping you.\x01",
            "Very well, let's go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7981")


    ChrTalk(    #268
        0x23,
        (
            "Haha, no worries.\x01",
            "It won't take that much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x23,
        "Let me show you. Follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x23, 400)

    ChrTalk(    #270
        0x101,
        "#1001FYeah!!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(19780, 0, 26480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(96000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1690, 0, 29190, 0)
    SetChrPos(0xF7, -880, 0, 28060, 0)
    SetChrPos(0x23, -310, 0, 29250, 0)

    def lambda_7A76():
        OP_6D(-980, 0, 29260, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7A76)

    def lambda_7A8E():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7A8E)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Sleep(400)

    ChrTalk(    #271
        0x101,
        "#1011FThis is the spot you were talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x23,
        "Yeah, look at the surface of the water.\x02",
    )

    CloseMessageWindow()
    OP_6D(-1300, -2000, 34150, 2000)

    ChrTalk(    #273
        0x23,
        "#1PSee, there's a ripple in the water, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x23,
        "#1PThat's a sign that you can pull up fish here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x23,
        (
            "#1PYou should be able to find them in\x01",
            "most bodies of water, so be sure to\x01",
            "keep an eye out on your travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#1006F#1POkay. So basically, just pay attention\x01",
            "to the surface of the water. Got it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-980, 0, 29260, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    TurnDirection(0x101, 0x23, 0)
    TurnDirection(0x23, 0x101, 0)
    OP_0D()

    ChrTalk(    #277
        0x23,
        "Now, enough about how to find fishing spots...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x23,
        "Next, let me give you this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #279
        "\x07\x00Received #987i x 5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3DB, 5)

    ChrTalk(    #280
        0x23,
        "This is bait for fishing, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x23,
        (
            "It's not sold in stores, so you'll\x01",
            "have to find it on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x23,
        (
            "They're dropped by monsters, though,\x01",
            "so a bracer like you shouldn't have\x01",
            "any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        "#1018FAh, that's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x23,
        "Aaaaand that's about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x23,
        (
            "You'll just have to find out\x01",
            "the rest by trying stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x101,
        (
            "#1006FYeah, got it.\x01",
            "Thanks for all the help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x23,
        (
            "No, no. My pleasure. It's all part of being\x01",
            "a member of the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x23,
        (
            "Well, then, catch you later.\x01",
            "I expect great results!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F39():

        label("loc_7F39")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_7F39")

    QueueWorkItem2(0x101, 1, lambda_7F39)

    def lambda_7F4A():

        label("loc_7F4A")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_7F4A")

    QueueWorkItem2(0xF7, 1, lambda_7F4A)

    def lambda_7F5B():
        OP_69(0x101, 0x5DC)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_7F5B)
    SetChrFlags(0x23, 0x40)
    OP_8E(0x23, 0x96, 0x0, 0x6DB0, 0x7D0, 0x0)
    OP_8E(0x23, 0xA96, 0x0, 0x6DB0, 0x7D0, 0x0)
    OP_8E(0x23, 0xDCA, 0x0, 0x70F8, 0x7D0, 0x0)
    OP_8E(0x23, 0x14B4, 0x0, 0x7148, 0x7D0, 0x0)
    OP_8E(0x23, 0x173E, 0xFFFFF8F8, 0x6298, 0x7D0, 0x0)
    SetChrFlags(0x23, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    WaitChrThread(0x25, 0x1)
    OP_65(0x4, 0x1)
    OP_A2(0x1242)
    EventEnd(0x0)
    Return()

    # Function_28_751E end

    def Function_29_7FE8(): pass

    label("Function_29_7FE8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8034")
    OP_51(0x25, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_29_7FE8")

    label("loc_8034")

    Return()

    # Function_29_7FE8 end

    def Function_30_8035(): pass

    label("Function_30_8035")

    EventBegin(0x1)

    ChrTalk(    #289
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_8061():
        OP_6D(-1300, 0, 34150, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8061)

    def lambda_8079():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8079)

    def lambda_8089():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_8089)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #290
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814D")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0x18, 0xFFFFFC22, 0x0, 0x738C, 0x0, 0xFFFFFAEC, 0xFFFFF448, 0x8566)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_815C")

    label("loc_814D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_815C")
    EventEnd(0x1)

    label("loc_815C")

    Return()

    # Function_30_8035 end

    def Function_31_815D(): pass

    label("Function_31_815D")

    SetPlaceName(0x69)
    Return()

    # Function_31_815D end

    def Function_32_8161(): pass

    label("Function_32_8161")

    SetPlaceName(0x52)
    Return()

    # Function_32_8161 end

    SaveToFile()

Try(main)
