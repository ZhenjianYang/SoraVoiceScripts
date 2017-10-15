from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5403   ._SN',
        MapName             = 'Other',
        Location            = 'C5403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '',                                     # 9
        'Gilbert',                              # 10
        'Riot Arms',                            # 11
        'Riot Arms',                            # 12
        'ポートシーカー',                       # 13
        'ヴォーグル570（青）',                  # 14
        'ヴォーグル235（赤）',                  # 15
        'ポートシーカー',                       # 16
        'ポートシーカー',                       # 17
        'ヴォーグル570（青）',                  # 18
        'ヴォーグル235（赤）',                  # 19
        'ポートシーカー',                       # 20
        'レオールガンイージ',                   # 21
        'レオールガンイージ',                   # 22
        'レオールガンイージ',                   # 23
        'レオールガンイージ',                   # 24
        'ポートシーカー',                       # 25
        'ヴォーグル570（青）',                  # 26
        'ヴォーグル235（赤）',                  # 27
        'ポートシーカー',                       # 28
        'ポートシーカー',                       # 29
        'ヴォーグル570（青）',                  # 30
        'ヴォーグル235（赤）',                  # 31
        'ポートシーカー',                       # 32
        'レオールガンイージ',                   # 33
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12350 ._CH',             # 02
        'ED6_DT29/CH12351 ._CH',             # 03
        'ED6_DT26/CH20255 ._CH',             # 04
        'ED6_DT26/CH20255 ._CH',             # 05
        'ED6_DT29/CH12310 ._CH',             # 06
        'ED6_DT29/CH12310 ._CH',             # 07
        'ED6_DT29/CH12320 ._CH',             # 08
        'ED6_DT29/CH12321 ._CH',             # 09
        'ED6_DT27/CH03750 ._CH',             # 0A
        'ED6_DT29/CH12530 ._CH',             # 0B
        'ED6_DT29/CH12531 ._CH',             # 0C
        'ED6_DT26/CH20501 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12350P._CP',             # 02
        'ED6_DT29/CH12351P._CP',             # 03
        'ED6_DT26/CH20255P._CP',             # 04
        'ED6_DT26/CH20255P._CP',             # 05
        'ED6_DT29/CH12310P._CP',             # 06
        'ED6_DT29/CH12310P._CP',             # 07
        'ED6_DT29/CH12320P._CP',             # 08
        'ED6_DT29/CH12321P._CP',             # 09
        'ED6_DT27/CH03750P._CP',             # 0A
        'ED6_DT29/CH12530P._CP',             # 0B
        'ED6_DT29/CH12531P._CP',             # 0C
        'ED6_DT26/CH20501P._CP',             # 0D
    )

    DeclNpc(
        X                   = 35060,
        Z                   = 2000,
        Y                   = -35010,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x185,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 34000,
        Z                   = 1000,
        Y                   = -76880,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = -27100,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = 27210,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32040,
        Z                   = 1000,
        Y                   = 116120,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34140,
        Z                   = 1000,
        Y                   = 116640,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -87240,
        Z                   = 0,
        Y                   = 27500,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86970,
        Z                   = 0,
        Y                   = -24730,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33900,
        Z                   = 1000,
        Y                   = -75690,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -830,
        Z                   = 0,
        Y                   = -16890,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -940,
        Z                   = 0,
        Y                   = 8910,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1050,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -910,
        Z                   = 0,
        Y                   = -28570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x426,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34000,
        Z                   = 1000,
        Y                   = -76880,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = -27100,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82050,
        Z                   = 0,
        Y                   = 27210,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32040,
        Z                   = 1000,
        Y                   = 116120,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -34140,
        Z                   = 1000,
        Y                   = 116640,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -87240,
        Z                   = 0,
        Y                   = 27500,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86970,
        Z                   = 0,
        Y                   = -24730,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -33900,
        Z                   = 1000,
        Y                   = -75690,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1050,
        Z                   = 0,
        Y                   = 23020,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = -1000,
        Z                   = 82020,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -6200,
        Y                   = -1000,
        Z                   = -27740,
        Range               = 4700,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF978C,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -5910,
        Y                   = -1000,
        Z                   = 31010,
        Range               = 3950,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x695A,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -5690,
        Y                   = -1000,
        Z                   = -32460,
        Range               = 4110,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF6E2E,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 80120,
        Y                   = -1000,
        Z                   = -36990,
        Range               = 84020,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF6000,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 80070,
        Y                   = -1000,
        Z                   = 8600,
        Range               = 83680,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x12AC,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = -127880,
        Y                   = -1000,
        Z                   = 10750,
        Range               = -124230,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1AFE,
        Unknown_18          = 0x0,
        Unknown_1C          = 33,
    )

    DeclEvent(
        X                   = -88820,
        Y                   = -1000,
        Z                   = 10590,
        Range               = -84910,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1B6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )


    DeclActor(
        TriggerX            = -42690,
        TriggerZ            = 0,
        TriggerY            = -31970,
        TriggerRange        = 1000,
        ActorX              = -42030,
        ActorZ              = 0,
        ActorY              = -31970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35680,
        TriggerZ            = 0,
        TriggerY            = -35010,
        TriggerRange        = 1000,
        ActorX              = 35060,
        ActorZ              = 0,
        ActorY              = -35010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3580,
        TriggerZ            = 0,
        TriggerY            = 79630,
        TriggerRange        = 1000,
        ActorX              = 3580,
        ActorZ              = 1000,
        ActorY              = 79630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41170,
        TriggerZ            = 0,
        TriggerY            = 60740,
        TriggerRange        = 1000,
        ActorX              = 41740,
        ActorZ              = 1000,
        ActorY              = 60890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41200,
        TriggerZ            = 0,
        TriggerY            = 59640,
        TriggerRange        = 1000,
        ActorX              = 41740,
        ActorZ              = 1000,
        ActorY              = 59710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41220,
        TriggerZ            = 0,
        TriggerY            = 58190,
        TriggerRange        = 1000,
        ActorX              = 41930,
        ActorZ              = 1000,
        ActorY              = 58370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41190,
        TriggerZ            = 0,
        TriggerY            = 56900,
        TriggerRange        = 1000,
        ActorX              = 42060,
        ActorZ              = 1000,
        ActorY              = 57120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38140,
        TriggerZ            = 0,
        TriggerY            = 62850,
        TriggerRange        = 1000,
        ActorX              = 38130,
        ActorZ              = 1000,
        ActorY              = 63510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38390,
        TriggerZ            = 0,
        TriggerY            = 55260,
        TriggerRange        = 1000,
        ActorX              = 38380,
        ActorZ              = 1000,
        ActorY              = 54650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41600,
        TriggerZ            = 0,
        TriggerY            = 15510,
        TriggerRange        = 1000,
        ActorX              = 42260,
        ActorZ              = 0,
        ActorY              = 15480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41600,
        TriggerZ            = 0,
        TriggerY            = 12030,
        TriggerRange        = 1000,
        ActorX              = 42210,
        ActorZ              = 0,
        ActorY              = 11950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41590,
        TriggerZ            = 0,
        TriggerY            = 8540,
        TriggerRange        = 1000,
        ActorX              = 42300,
        ActorZ              = 0,
        ActorY              = 8510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43620,
        TriggerZ            = 0,
        TriggerY            = 17790,
        TriggerRange        = 1000,
        ActorX              = -43660,
        ActorZ              = 0,
        ActorY              = 18410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39950,
        TriggerZ            = 0,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -39990,
        ActorZ              = 0,
        ActorY              = 18410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36240,
        TriggerZ            = 0,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -36280,
        ActorZ              = 0,
        ActorY              = 18510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4960,
        TriggerZ            = 0,
        TriggerY            = 77000,
        TriggerRange        = 1000,
        ActorX              = 4960,
        ActorZ              = 1000,
        ActorY              = 77000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_726",          # 00, 0
        "Function_1_758",          # 01, 1
        "Function_2_B5E",          # 02, 2
        "Function_3_B74",          # 03, 3
        "Function_4_CC9",          # 04, 4
        "Function_5_EBC",          # 05, 5
        "Function_6_1005",         # 06, 6
        "Function_7_112C",         # 07, 7
        "Function_8_129C",         # 08, 8
        "Function_9_13E1",         # 09, 9
        "Function_10_151C",        # 0A, 10
        "Function_11_1648",        # 0B, 11
        "Function_12_17D0",        # 0C, 12
        "Function_13_18F9",        # 0D, 13
        "Function_14_1A68",        # 0E, 14
        "Function_15_1BC6",        # 0F, 15
        "Function_16_1D30",        # 10, 16
        "Function_17_1EBF",        # 11, 17
        "Function_18_1ED8",        # 12, 18
        "Function_19_1EEE",        # 13, 19
        "Function_20_31C2",        # 14, 20
        "Function_21_3C7E",        # 15, 21
        "Function_22_3C94",        # 16, 22
        "Function_23_3CAA",        # 17, 23
        "Function_24_3CC8",        # 18, 24
        "Function_25_3CFD",        # 19, 25
        "Function_26_3D12",        # 1A, 26
        "Function_27_3D98",        # 1B, 27
        "Function_28_3FBA",        # 1C, 28
        "Function_29_420C",        # 1D, 29
        "Function_30_424D",        # 1E, 30
        "Function_31_428E",        # 1F, 31
        "Function_32_42CF",        # 20, 32
        "Function_33_4310",        # 21, 33
        "Function_34_4351",        # 22, 34
        "Function_35_4392",        # 23, 35
        "Function_36_4423",        # 24, 36
        "Function_37_4449",        # 25, 37
    )


    def Function_0_726(): pass

    label("Function_0_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_END)), "loc_757")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1950, 0, -22900, 180)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 5)

    label("loc_757")

    Return()

    # Function_0_726 end

    def Function_1_758(): pass

    label("Function_1_758")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_788")
    OP_6F(0x24, 0)
    Jump("loc_78F")

    label("loc_788")

    OP_6F(0x24, 60)

    label("loc_78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A1")
    OP_6F(0x25, 0)
    Jump("loc_7A8")

    label("loc_7A1")

    OP_6F(0x25, 60)

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BA")
    OP_6F(0x29, 0)
    Jump("loc_7C1")

    label("loc_7BA")

    OP_6F(0x29, 60)

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D3")
    OP_6F(0x2A, 0)
    Jump("loc_7DA")

    label("loc_7D3")

    OP_6F(0x2A, 60)

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EC")
    OP_6F(0x2B, 0)
    Jump("loc_7F3")

    label("loc_7EC")

    OP_6F(0x2B, 60)

    label("loc_7F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_805")
    OP_6F(0x2C, 0)
    Jump("loc_80C")

    label("loc_805")

    OP_6F(0x2C, 60)

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81E")
    OP_6F(0x2D, 0)
    Jump("loc_825")

    label("loc_81E")

    OP_6F(0x2D, 60)

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_837")
    OP_6F(0x2E, 0)
    Jump("loc_83E")

    label("loc_837")

    OP_6F(0x2E, 60)

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850")
    OP_6F(0x2F, 0)
    Jump("loc_857")

    label("loc_850")

    OP_6F(0x2F, 60)

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_869")
    OP_6F(0x30, 0)
    Jump("loc_870")

    label("loc_869")

    OP_6F(0x30, 60)

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_882")
    OP_6F(0x31, 0)
    Jump("loc_889")

    label("loc_882")

    OP_6F(0x31, 60)

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89B")
    OP_6F(0x32, 0)
    Jump("loc_8A2")

    label("loc_89B")

    OP_6F(0x32, 60)

    label("loc_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4")
    OP_6F(0x33, 0)
    Jump("loc_8BB")

    label("loc_8B4")

    OP_6F(0x33, 60)

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CD")
    OP_6F(0x34, 0)
    Jump("loc_8D4")

    label("loc_8CD")

    OP_6F(0x34, 60)

    label("loc_8D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_929")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 3580, 1200, 79630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_929")

    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AB")
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
    SetChrFlags(0x17, 0x80)
    Jump("loc_9D8")

    label("loc_9AB")

    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)

    label("loc_9D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6C")
    OP_72(0x17, 0x10)
    OP_6F(0x2, 100)
    OP_6F(0x4, 100)
    OP_6F(0x5, 100)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 80500, -1000, -37650, 84000, 2000, -40350)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_BE(0x5, 0x1, 0x2, 0x64, 0x0, 0x2, -88290, 0, 10370, -85540, 2000, 7640)
    SetChrFlags(0x17, 0x80)
    Jump("loc_A6C")

    label("loc_A6C")

    Call(0, 28)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x434), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5D")
    OP_D2(0x2703A8, 0x2703B2, 0xE)
    OP_D2(0x2703AC, 0x2703B6, 0xF)
    OP_D2(0x2703AE, 0x2703B8, 0x10)
    OP_D2(0x26020B, 0x260210, 0x11)
    OP_D2(0x290216, 0x29021A, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270130, 0x270140, 0x14)
    OP_D2(0x702B4, 0x702BB, 0x15)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_B02"),
        (3, "loc_B0F"),
        (4, "loc_B1C"),
        (5, "loc_B29"),
        (6, "loc_B36"),
        (7, "loc_B43"),
        (8, "loc_B50"),
        (SWITCH_DEFAULT, "loc_B5D"),
    )


    label("loc_B02")

    OP_D2(0x701D0, 0x701DC, 0x16)
    Jump("loc_B5D")

    label("loc_B0F")

    OP_D2(0x701E8, 0x701F4, 0x16)
    Jump("loc_B5D")

    label("loc_B1C")

    OP_D2(0x27036E, 0x27037B, 0x16)
    Jump("loc_B5D")

    label("loc_B29")

    OP_D2(0x70218, 0x70224, 0x16)
    Jump("loc_B5D")

    label("loc_B36")

    OP_D2(0x70230, 0x7023C, 0x16)
    Jump("loc_B5D")

    label("loc_B43")

    OP_D2(0x70248, 0x70254, 0x16)
    Jump("loc_B5D")

    label("loc_B50")

    OP_D2(0x270176, 0x270183, 0x16)
    Jump("loc_B5D")

    label("loc_B5D")

    Return()

    # Function_1_758 end

    def Function_2_B5E(): pass

    label("Function_2_B5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B73")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_B5E")

    label("loc_B73")

    Return()

    # Function_2_B5E end

    def Function_3_B74(): pass

    label("Function_3_B74")

    OP_EA(0x2, 0x63, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x185, 1)"), scpexpr(EXPR_END)), "loc_BE5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x85\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D36)
    Jump("loc_C49")

    label("loc_BE5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x85\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x85\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_C49")

    Jump("loc_CBB")

    label("loc_C4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Were you hoping somebody would come along\x01",
            "and put in MORE stuff for you to take?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CBB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B74 end

    def Function_4_CC9(): pass

    label("Function_4_CC9")

    OP_EA(0x2, 0x64, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E64")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB3")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D20():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D20)

    def lambda_D3B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D3B)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #3
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x42C, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D8E"),
        (2, "loc_DA0"),
        (1, "loc_DB0"),
        (SWITCH_DEFAULT, "loc_DB3"),
    )


    label("loc_D8E")

    OP_A2(0x1D38)
    OP_6F(0x25, 60)
    Sleep(500)
    Jump("loc_DB3")

    label("loc_DA0")

    OP_6F(0x25, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DB0")

    OP_B4(0x0)
    Return()

    label("loc_DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19, 1)"), scpexpr(EXPR_END)), "loc_DFF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        "Found \x1F\x19\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D37)
    Jump("loc_E61")

    label("loc_DFF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        (
            "Found \x1F\x19\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x19\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_E61")

    Jump("loc_EAE")

    label("loc_E64")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05Wear good shoes and you'll never see de feet.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EAE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CC9 end

    def Function_5_EBC(): pass

    label("Function_5_EBC")

    OP_EA(0x2, 0x65, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F94")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_F2D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3D)
    Jump("loc_F91")

    label("loc_F2D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_F91")

    Jump("loc_FF7")

    label("loc_F94")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Someone's robbed this chest blind. Not to\x01",
            "worry. You're on the case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FF7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_EBC end

    def Function_6_1005(): pass

    label("Function_6_1005")

    OP_EA(0x2, 0x66, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x166, 1)"), scpexpr(EXPR_END)), "loc_1076")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x66\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3E)
    Jump("loc_10DA")

    label("loc_1076")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x66\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x66\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_10DA")

    Jump("loc_111E")

    label("loc_10DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05You find only a bleak, empty void.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_111E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1005 end

    def Function_7_112C(): pass

    label("Function_7_112C")

    OP_EA(0x2, 0x67, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1204")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_119D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3F)
    Jump("loc_1201")

    label("loc_119D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_1201")

    Jump("loc_128E")

    label("loc_1204")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05You open the chest, eyes wild with avarice.\x01",
            "Your face falls as you realize you've already\x01",
            "taken everything.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_128E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_112C end

    def Function_8_129C(): pass

    label("Function_8_129C")

    OP_EA(0x2, 0x68, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1374")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_130D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D40)
    Jump("loc_1371")

    label("loc_130D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_1371")

    Jump("loc_13D3")

    label("loc_1374")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05A single tumbleweed rolls from one side of the\x01",
            "chest to another.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13D3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_129C end

    def Function_9_13E1(): pass

    label("Function_9_13E1")

    OP_EA(0x2, 0x69, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1452")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D41)
    Jump("loc_14B6")

    label("loc_1452")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2D, 60)
    OP_70(0x2D, 0x0)

    label("loc_14B6")

    Jump("loc_150E")

    label("loc_14B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05This empty chest is a monument to your\x01",
            "reckless greed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_150E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_13E1 end

    def Function_10_151C(): pass

    label("Function_10_151C")

    OP_EA(0x2, 0x6A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1613")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x1E)
    OP_73(0x2E)
    OP_6F(0x2E, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D42)
    Jump("loc_1636")

    label("loc_1613")


    AnonymousTalk(    #23
        "\x07\x05Space for rent. -Management\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1636")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_151C end

    def Function_11_1648(): pass

    label("Function_11_1648")

    OP_EA(0x2, 0x6B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1720")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_16B9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D43)
    Jump("loc_171D")

    label("loc_16B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_171D")

    Jump("loc_17C2")

    label("loc_1720")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x05They all look the same to you now. Every one\x01",
            "of them, so helpless, so vulnerable--a mere\x01",
            "target for you and your insatiable hunger.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_17C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1648 end

    def Function_12_17D0(): pass

    label("Function_12_17D0")

    OP_EA(0x2, 0x6C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x30, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x170, 1)"), scpexpr(EXPR_END)), "loc_1841")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "Found \x1F\x70\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D44)
    Jump("loc_18A5")

    label("loc_1841")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "Found \x1F\x70\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x70\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x30, 60)
    OP_70(0x30, 0x0)

    label("loc_18A5")

    Jump("loc_18EB")

    label("loc_18A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05This chest is as empty as your soul.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_18EB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_17D0 end

    def Function_13_18F9(): pass

    label("Function_13_18F9")

    OP_EA(0x2, 0x6D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x31, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_196A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D46)
    Jump("loc_19CE")

    label("loc_196A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x31, 60)
    OP_70(0x31, 0x0)

    label("loc_19CE")

    Jump("loc_1A5A")

    label("loc_19D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x07\x05You see a single tear roll down its treasure chest\x01",
            "cheek. Wait a second... Chests don't have tear\x01",
            "ducts...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1A5A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_18F9 end

    def Function_14_1A68(): pass

    label("Function_14_1A68")

    OP_EA(0x2, 0x6E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B40")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x32, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_1AD9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D47)
    Jump("loc_1B3D")

    label("loc_1AD9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x32, 60)
    OP_70(0x32, 0x0)

    label("loc_1B3D")

    Jump("loc_1BB8")

    label("loc_1B40")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x07\x05You kick the chest open, but all you get for your\x01",
            "talented footwork is a stubbed toe. Ow.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1BB8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1A68 end

    def Function_15_1BC6(): pass

    label("Function_15_1BC6")

    OP_EA(0x2, 0x6F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x33, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_1C37")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D48)
    Jump("loc_1C9B")

    label("loc_1C37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x33, 60)
    OP_70(0x33, 0x0)

    label("loc_1C9B")

    Jump("loc_1D22")

    label("loc_1C9E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05You look under the chest, hoping to find the\x01",
            "keys to a BRAND NEW AIRSHIP! ...You don't find\x01",
            "anything.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1D22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1BC6 end

    def Function_16_1D30(): pass

    label("Function_16_1D30")

    OP_EA(0x2, 0x70, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E08")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x34, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_1DA1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        "Found \x1F\x05\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D49)
    Jump("loc_1E05")

    label("loc_1DA1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "Found \x1F\x05\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x05\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x34, 60)
    OP_70(0x34, 0x0)

    label("loc_1E05")

    Jump("loc_1EB1")

    label("loc_1E08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "\x07\x05As you reach into the chest, the lid suddenly\x01",
            "snaps down! IT'S EATING YOU ALIVE. ...Kidding!\x01",
            "Oh, you should've seen the look on your face!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1EB1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_1D30 end

    def Function_17_1EBF(): pass

    label("Function_17_1EBF")

    OP_A3(0x1C81)
    OP_A3(0x1C82)
    OP_A3(0x1C83)
    OP_A3(0x1C84)
    OP_A2(0x1C85)
    OP_A3(0x1C86)
    OP_A3(0x1C87)
    OP_A3(0x1C88)
    Return()

    # Function_17_1EBF end

    def Function_18_1ED8(): pass

    label("Function_18_1ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EE5")
    Return()

    label("loc_1EE5")

    Call(0, 19)
    Call(0, 20)
    Return()

    # Function_18_1ED8 end

    def Function_19_1EEE(): pass

    label("Function_19_1EEE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F13")
    Call(0, 26)
    Call(0, 35)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_1F13")

    OP_43(0xF9, 0x3, 0x0, 0x25)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB2")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FF0")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD9")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1FF0")

    label("loc_1FD9")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1FF0")

    Sleep(1000)

    def lambda_1FFB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FFB)
    Sleep(50)

    def lambda_200E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_200E)
    Sleep(50)

    def lambda_2021():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2021)
    Sleep(50)
    OP_8C(0xF9, 180, 400)
    SetChrFlags(0x20, 0x80)
    Fade(500)
    OP_6D(150, 0, -28510, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    SetChrPos(0x101, -1540, 0, -27810, 180)
    SetChrPos(0x102, -120, 0, -27830, 180)
    SetChrPos(0x10B, -1860, 0, -29380, 180)
    SetChrPos(0xF9, -350, 0, -29430, 180)
    SetChrPos(0x9, -950, 0, -12970, 180)
    OP_E5(0x9, 0x0, 0x0)
    OP_0D()

    ChrTalk(    #42
        0x10B,
        "#216F#5PWhat the?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1020F#6PWhat is this?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #44
        0x9,
        "Young Man's Voice",
        "#4PHeh heh. Finally caught you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BD")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21FB")

    label("loc_21BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E4")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21FB")

    label("loc_21E4")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_21FB")

    Sleep(1000)

    def lambda_2206():
        OP_6D(-10, 0, -23700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2206)

    def lambda_221E():
        OP_67(0, 4680, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_221E)

    def lambda_2236():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2236)

    def lambda_2246():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2246)

    def lambda_2256():
        OP_6E(357, 3000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_2256)
    WaitChrThread(0xF9, 0x3)
    ClearChrFlags(0x9, 0x80)

    def lambda_2270():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xFFFFB3A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2270)

    def lambda_228B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_228B)
    Sleep(50)

    def lambda_229E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_229E)
    Sleep(80)

    def lambda_22B1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_22B1)
    Sleep(70)

    def lambda_22C4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_22C4)
    WaitChrThread(0x9, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)
    OP_E5(0x9, 0x0, 0x1)

    ChrTalk(    #45
        0x101,
        "#1005F#2PGILBERT?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_233E")

    ChrTalk(    #46
        0x105,
        "#1164F#2PGilbert? From the academy?\x02",
    )

    CloseMessageWindow()

    label("loc_233E")


    ChrTalk(    #47
        0x102,
        "#1042F#2PSo they DID bring you along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#1226F#6PWell, well, well. I'd wondered what manner\x01",
            "of fools would dare to attempt storming the\x01",
            "Glorious.\x02\x03",

            "#1221FI had an inkling it might be you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10B,
        (
            "#213F#2PHuh? Hey...\x02\x03",

            "Do you guys know this dude?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2644")

    ChrTalk(    #50
        0x105,
        (
            "#1163F#2PYes... He's an alumnus of the\x01",
            "royal academy, but he...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as completed Royal Academy Rescue\x01",      # 0
            "Set as didn't complete\x01",                     # 1
            "No change\x01",                                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2520"),
        (1, "loc_2526"),
        (SWITCH_DEFAULT, "loc_252C"),
    )


    label("loc_2520")

    OP_A2(0x202F)
    Jump("loc_252C")

    label("loc_2526")

    OP_A3(0x202F)
    Jump("loc_252C")

    label("loc_252C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_25DB")

    ChrTalk(    #51
        0x101,
        (
            "#1007F#2PHe's not much of an 'alumnus' after\x01",
            "ATTACKING it, Kloe.\x02\x03",

            "#1019FWe first met--and arrested--his dumb butt\x01",
            "when he was a flunky of Ruan's corrupt mayor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2641")

    label("loc_25DB")


    ChrTalk(    #52
        0x101,
        (
            "#1019F#2PWe first met--and arrested--his dumb butt\x01",
            "when he was a flunky of Ruan's corrupt mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2641")

    Jump("loc_26D2")

    label("loc_2644")


    ChrTalk(    #53
        0x101,
        (
            "#1007F#2PYou could sorta say that, maybe.\x02\x03",

            "#1019FWe first met--and arrested--his dumb butt\x01",
            "when he was a flunky of Ruan's corrupt mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D2")


    ChrTalk(    #54
        0x102,
        (
            "#1035F#2PHe escaped during the coup and\x01",
            "apparently joined Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10B,
        (
            "#211F#2PHahaha, right! I thought so!\x02\x03",

            "#210FYou were that guy locked up\x01",
            "with us in Leiston, right?\x02\x03",

            "I remember him because he kept bawling\x01",
            "and going on and on saying 'I'm innocent!'\x01",
            "and stuff. 'Wah wah wah' all the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #56
        0x9,
        "#1224F#6PWHAT?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284A")

    ChrTalk(    #57
        0x105,
        "#1164FOh, my.\x02",
    )

    CloseMessageWindow()

    label("loc_284A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2883")

    ChrTalk(    #58
        0x107,
        "#067FAww, we made him feel bad again!\x02",
    )

    CloseMessageWindow()

    label("loc_2883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28CA")

    ChrTalk(    #59
        0x104,
        (
            "#031FHa ha ha! The shocking truth,\x01",
            "brutal as it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28F3")

    ChrTalk(    #60
        0x103,
        "#025FAlways pathetic.\x02",
    )

    CloseMessageWindow()

    label("loc_28F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2921")

    ChrTalk(    #61
        0x106,
        "#053FWhat a piece of work.\x02",
    )

    CloseMessageWindow()

    label("loc_2921")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29D8")

    ChrTalk(    #62
        0x109,
        (
            "#1068F#2PUh, hey now, young lady...\x02\x03",

            "#1066FIt's polite to pretend you didn't see that\x01",
            "kinda thing, y'know? Even if it does make\x01",
            "great material for pokin' fun...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4E")

    label("loc_29D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A4E")

    ChrTalk(    #63
        0x108,
        (
            "#075F#2PHey, c'mon now, Miss Josette.\x02\x03",

            "#070FIt's polite to ignore a man's behavior\x01",
            "at his weakest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4E")


    ChrTalk(    #64
        0x101,
        (
            "#1025F#2PUm, riiight...\x02\x03",

            "#1016FAnyway, nothing to let bother you, y'know?\x02\x03",

            "It's part of, uh, life! Having to grow from\x01",
            "pathetic moments like that, I mean.\x02\x03",

            "#1013FThough, uh, given the uniform, I dunno\x01",
            "how much he actually grew...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x102,
        (
            "#1048F#2P... Estelle, that's not exactly a\x01",
            "comforting follow-up.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(300)

    ChrTalk(    #66
        0x9,
        (
            "#1222F#6PD-Damn you... How much of a fool\x01",
            "do you intend to play me for?!\x02\x03",

            "#1226FBut...no matter. It just confirms I have\x01",
            "no reasons to show you mercy.\x02\x03",

            "#1225FYou face now the power of the NEW Gilbert!\x01",
            "TREEEMBLE!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 16)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -990, 800, 49890, 180)
    OP_43(0xA, 0x0, 0x0, 0x15)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)

    def lambda_2CE4():
        OP_69(0xA, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CE4)

    def lambda_2CF2():
        OP_67(0, 2000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CF2)

    def lambda_2D0A():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D0A)

    def lambda_2D1A():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D1A)

    def lambda_2D2A():
        OP_6E(380, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D2A)
    WaitChrThread(0x101, 0x0)
    SetChrPos(0x9, -10, 0, -19000, 180)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x101, -7820, 0, -30050, 0)
    Sleep(500)
    OP_22(0x193, 0x0, 0x64)
    Sleep(900)
    OP_43(0x9, 0x3, 0x0, 0x18)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 12)

    def lambda_2D94():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2D94)

    def lambda_2DA6():
        OP_8F(0xFE, 0xFFFFF79A, 0x320, 0xFFFFFFE2, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DA6)
    Sleep(1200)
    Fade(500)
    OP_69(0xA, 0x0)
    OP_6A(0xA)
    OP_67(0, 2500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(24000, 0)
    OP_6E(380, 0)

    def lambda_2E01():
        OP_67(0, 3000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E01)

    def lambda_2E19():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E19)

    def lambda_2E29():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2E29)
    WaitChrThread(0xA, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_6A(0xFF)
    OP_44(0x9, 0x3)
    OP_23(0x13F)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_2E59():
        OP_96(0xFE, 0xFFFFF79A, 0xFA0, 0xFFFFD9A4, 0x1388, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E59)
    Sleep(100)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2150, 800, -19000, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    WaitChrThread(0xA, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_2ED6():
        OP_96(0xFE, 0xFFFFF79A, 0x320, 0xFFFFB5C8, 0x7D0, 0x1F40)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2ED6)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 11)
    OP_44(0xA, 0x0)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x1388, 0x1F4)
    Sleep(500)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_22(0x193, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #67
        0x101,
        "#1020F#1PAaaah!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(400, 0, -22850, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(44000, 0)
    OP_6E(380, 0)
    SetChrPos(0x101, -1540, 0, -27810, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 20)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10B, 21)
    SetChrSubChip(0x10B, 0)
    SetChrChipByIndex(0xF9, 22)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #68
        0x10B,
        "#216F#2PWh-Wh-What the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1020F#2PMechanical...lions?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#1042F#2PIt's not something I recognize...\x01",
            "I take it this must be a new model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#1221F#6PIndeed! Lion-model attack archaism, the Riot Arms!\x02\x03",

            "Cower! Beg for life! It ends here!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x193, 0x0, 0x64)
    Sleep(1200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_30F8():
        OP_6D(-210, 0, -25930, 700)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30F8)

    def lambda_3110():
        OP_67(0, 6180, -10000, 700)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3110)

    def lambda_3128():
        OP_6B(2020, 700)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3128)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 12)
    OP_43(0xA, 0x0, 0x0, 0x15)
    OP_43(0xA, 0x3, 0x0, 0x19)
    OP_8F(0xA, 0xFFFFFC04, 0x320, 0xFFFFA79A, 0x2710, 0x0)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_3169():
        OP_96(0xFE, 0xFFFFFCA4, 0x0, 0xFFFF92A0, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3169)
    OP_44(0xA, 0x0)
    SetChrChipByIndex(0xA, 18)

    def lambda_3190():
        OP_99(0xFE, 0x0, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3190)
    WaitChrThread(0x101, 0x1)
    OP_44(0xA, 0xFF)
    Battle(0x434, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_31BC"),
        (SWITCH_DEFAULT, "loc_31C1"),
    )


    label("loc_31BC")

    OP_B4(0x0)
    Jump("loc_31C1")

    label("loc_31C1")

    Return()

    # Function_19_1EEE end

    def Function_20_31C2(): pass

    label("Function_20_31C2")

    OP_EA(0xB, 0x0, 0x0, 0x0)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0xA, 0x0)
    OP_44(0xA, 0x1)
    OP_44(0xA, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_6D(-480, 0, -22740, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2170, 0, -25140, 0)
    SetChrPos(0x102, -910, 0, -25200, 0)
    SetChrPos(0x10B, -2630, 0, -26440, 0)
    SetChrPos(0xF9, -1200, 0, -26530, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1620, 0, -22000, 180)
    SetChrChipByIndex(0x9, 15)
    SetChrSubChip(0x9, 3)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10B, 65535)
    SetChrChipByIndex(0xF9, 65535)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #72
        0x9,
        (
            "#1224F#6PImpossible...\x02\x03",

            "Even as a new man, I can't win...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1015F#2PEr... Can I point something out?\x02\x03",

            "That lion thingy WAS actually pretty tough.\x01",
            "But, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10B,
        (
            "#413F#2PThat doesn't mean you've gotten\x01",
            "any stronger at all, does it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "#1224F#6PNo...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3408")

    ChrTalk(    #76
        0x105,
        (
            "#1165FYes, the 'new man' idea may\x01",
            "have been a little premature.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_3408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3457")

    ChrTalk(    #77
        0x107,
        (
            "#067FI'm, um, not really sure about\x01",
            "how 'new' you are...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_3457")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34DE")

    ChrTalk(    #78
        0x109,
        (
            "#1068FYeah, callin' yourself 'new' mighta\x01",
            "been a bit much.\x02\x03",

            "#1060FThis's what they call over-advertising,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_34DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3584")

    ChrTalk(    #79
        0x103,
        (
            "#025FYes, calling yourself a 'new man'\x01",
            "was a bit excessive.\x02\x03",

            "#524FFor future reference, most women don't\x01",
            "go for men who put on airs, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_3584")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35F0")

    ChrTalk(    #80
        0x104,
        (
            "#035FA new man, hmm?\x02\x03",

            "#037FEven pretension such as that can\x01",
            "be captivating, at times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_35F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_366E")

    ChrTalk(    #81
        0x106,
        (
            "#551FTch. What's 'new' about this?\x02\x03",

            "#555FNew or not, if you're a man, fight\x01",
            "with your own damn muscles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_366E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36F7")

    ChrTalk(    #82
        0x108,
        (
            "#074FTrue enough. You haven't changed\x01",
            "enough to call yourself a new man.\x02\x03",

            "#070FDrop the attitude and maybe we'll see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F7")


    ChrTalk(    #83
        0x9,
        "#1228F#6P...Blorf.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrPos(0x9, -1950, 0, -22900, 180)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #84
        0x101,
        "#1004F#2PAh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10B,
        "#213F#2POh.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3790")

    ChrTalk(    #86
        0x105,
        "#1164FOh, my!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_3790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B6")

    ChrTalk(    #87
        0x107,
        "#065FWaaa-aaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_37B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37DA")

    ChrTalk(    #88
        0x109,
        "#1064FAw man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_37DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3801")

    ChrTalk(    #89
        0x103,
        "#023FGoodness...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_3801")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3823")

    ChrTalk(    #90
        0x104,
        "#033FMy my.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_3823")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3842")

    ChrTalk(    #91
        0x106,
        "#052FUh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_3842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3861")

    ChrTalk(    #92
        0x108,
        "#073FHuh...\x02",
    )

    CloseMessageWindow()

    label("loc_3861")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C8")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38FC")

    label("loc_38C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38EA")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_38FC")

    label("loc_38EA")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_38FC")

    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0x10B)
    OP_63(0xF9)
    Sleep(500)

    def lambda_3918():
        OP_6D(-1450, 0, -25300, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3918)

    def lambda_3930():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3930)
    Sleep(50)

    def lambda_3943():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3943)
    Sleep(50)

    def lambda_3956():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_3956)
    Sleep(50)

    def lambda_3969():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3969)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #93
        0x101,
        "#1016F#6PWelllllll...better get to those cells, huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39EA")

    ChrTalk(    #94
        0x105,
        "#1165FQu-Quite...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_39EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A1D")

    ChrTalk(    #95
        0x107,
        "#067FUm, yeah! We should go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_3A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A57")

    ChrTalk(    #96
        0x109,
        "#1066FHaha, yeeeah... Uh, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_3A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A7F")

    ChrTalk(    #97
        0x103,
        "#021FA good idea!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_3A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AAA")

    ChrTalk(    #98
        0x104,
        "#031FA capital idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ACC")

    ChrTalk(    #99
        0x106,
        "#551F*sigh*\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AEC")

    label("loc_3ACC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AEC")

    ChrTalk(    #100
        0x108,
        "#070FIndeed!\x02",
    )

    CloseMessageWindow()

    label("loc_3AEC")


    ChrTalk(    #101
        0x10B,
        "#211F#6PYeah, c'mon! We need to save my brothers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        "#1052F#6P(I can't help but feel sorry for the guy...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1410, 0, -25050, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1410, 0, -25050, 0)
    SetChrPos(0x1, -1410, 0, -25050, 0)
    SetChrPos(0x2, -1410, 0, -25050, 0)
    SetChrPos(0x3, -1410, 0, -25050, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_71(0x17, 0x10)
    OP_6F(0x2, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_BE(0x2, 0x1, 0x0, 0x0, 0x0, 0x2, 0, 0, 0, 0, 0, 0)
    OP_BE(0x4, 0x1, 0x0, 0x0, 0x0, 0x2, 0, 0, 0, 0, 0, 0)
    OP_BE(0x5, 0x1, 0x0, 0x0, 0x0, 0x2, 0, 0, 0, 0, 0, 0)
    OP_A2(0x2227)
    EventEnd(0x0)
    Return()

    # Function_20_31C2 end

    def Function_21_3C7E(): pass

    label("Function_21_3C7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C93")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_21_3C7E")

    label("loc_3C93")

    Return()

    # Function_21_3C7E end

    def Function_22_3C94(): pass

    label("Function_22_3C94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CA9")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_22_3C94")

    label("loc_3CA9")

    Return()

    # Function_22_3C94 end

    def Function_23_3CAA(): pass

    label("Function_23_3CAA")

    SetChrChipByIndex(0xFE, 18)
    OP_22(0x195, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_23_3CAA end

    def Function_24_3CC8(): pass

    label("Function_24_3CC8")

    OP_22(0x13F, 0x0, 0x46)
    Sleep(400)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(400)
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(400)

    label("loc_3CE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CFC")
    OP_22(0x13F, 0x0, 0x64)
    Sleep(400)
    Jump("loc_3CE6")

    label("loc_3CFC")

    Return()

    # Function_24_3CC8 end

    def Function_25_3CFD(): pass

    label("Function_25_3CFD")

    OP_22(0x13F, 0x0, 0x64)
    Sleep(400)
    OP_22(0x13F, 0x0, 0x64)
    Sleep(400)
    Return()

    # Function_25_3CFD end

    def Function_26_3D12(): pass

    label("Function_26_3D12")

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
        (0, "loc_3D8B"),
        (1, "loc_3D91"),
        (SWITCH_DEFAULT, "loc_3D97"),
    )


    label("loc_3D8B")

    OP_A2(0x1200)
    Jump("loc_3D97")

    label("loc_3D91")

    OP_A2(0x1201)
    Jump("loc_3D97")

    label("loc_3D97")

    Return()

    # Function_26_3D12 end

    def Function_27_3D98(): pass

    label("Function_27_3D98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DFE")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #103
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3FB9")

    label("loc_3DFE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #104
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 3580, 1000, 79630, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x28, 0)
    OP_70(0x28, 0x32)
    OP_73(0x28)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 3580, 1000, 79630, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 3580, 1000, 79630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x28, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3F9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FB8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3FB8")

    Return()

    label("loc_3FB9")

    Return()

    # Function_27_3D98 end

    def Function_28_3FBA(): pass

    label("Function_28_3FBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_40EB")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x2)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_71(0x1, 0x2)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_71(0x2, 0x2)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x2)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_6F(0x4, 0)
    OP_71(0x4, 0x2)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 0)
    OP_71(0x5, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40EA")
    OP_72(0x17, 0x10)
    OP_6F(0x2, 100)
    OP_6F(0x4, 100)
    OP_6F(0x5, 100)
    OP_72(0x2, 0x2)
    OP_72(0x4, 0x2)
    OP_72(0x5, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 80500, -1000, -37650, 84000, 2000, -40350)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_BE(0x5, 0x1, 0x2, 0x64, 0x0, 0x2, -88290, 0, 10370, -85540, 2000, 7640)
    SetChrFlags(0x17, 0x80)

    label("loc_40EA")

    Return()

    label("loc_40EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 4)), scpexpr(EXPR_END)), "loc_411B")
    OP_6F(0x0, 100)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -5310, -1000, 30410, 3470, 2000, 27560)

    label("loc_411B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 5)), scpexpr(EXPR_END)), "loc_414B")
    OP_6F(0x1, 100)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -5210, -1000, -36500, 3470, 2000, -33500)

    label("loc_414B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 6)), scpexpr(EXPR_END)), "loc_417B")
    OP_6F(0x2, 100)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, 80500, -1000, -37650, 84000, 2000, -40350)

    label("loc_417B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 7)), scpexpr(EXPR_END)), "loc_41AB")
    OP_6F(0x3, 100)
    OP_BE(0x3, 0x1, 0x2, 0x64, 0x0, 0x2, 80690, -1000, 8260, 83470, 2000, 5400)

    label("loc_41AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 0)), scpexpr(EXPR_END)), "loc_41DB")
    OP_6F(0x4, 100)
    OP_BE(0x4, 0x1, 0x2, 0x64, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)

    label("loc_41DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 1)), scpexpr(EXPR_END)), "loc_420B")
    OP_6F(0x5, 100)
    OP_BE(0x5, 0x1, 0x2, 0x64, 0x0, 0x2, -88290, 0, 10370, -85540, 2000, 7640)

    label("loc_420B")

    Return()

    # Function_28_3FBA end

    def Function_29_420C(): pass

    label("Function_29_420C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4219")
    Return()

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 4)), scpexpr(EXPR_END)), "loc_4221")
    Return()

    label("loc_4221")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x0)
    OP_A2(0x1C94)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_29_420C end

    def Function_30_424D(): pass

    label("Function_30_424D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_425A")
    Return()

    label("loc_425A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 5)), scpexpr(EXPR_END)), "loc_4262")
    Return()

    label("loc_4262")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x1C95)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_30_424D end

    def Function_31_428E(): pass

    label("Function_31_428E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_429B")
    Return()

    label("loc_429B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 6)), scpexpr(EXPR_END)), "loc_42A3")
    Return()

    label("loc_42A3")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x1C96)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_31_428E end

    def Function_32_42CF(): pass

    label("Function_32_42CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_42DC")
    Return()

    label("loc_42DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 7)), scpexpr(EXPR_END)), "loc_42E4")
    Return()

    label("loc_42E4")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x3)
    OP_A2(0x1C97)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_32_42CF end

    def Function_33_4310(): pass

    label("Function_33_4310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_431D")
    Return()

    label("loc_431D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 0)), scpexpr(EXPR_END)), "loc_4325")
    Return()

    label("loc_4325")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x1C98)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_33_4310 end

    def Function_34_4351(): pass

    label("Function_34_4351")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_435E")
    Return()

    label("loc_435E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x393, 1)), scpexpr(EXPR_END)), "loc_4366")
    Return()

    label("loc_4366")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(1500)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x1C99)
    Call(0, 28)
    EventEnd(0x3)
    Return()

    # Function_34_4351 end

    def Function_35_4392(): pass

    label("Function_35_4392")

    FadeToDark(0, 0, -1)
    OP_6D(-27650, 0, -3680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xA, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_35_4392 end

    def Function_36_4423(): pass

    label("Function_36_4423")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240131, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_36_4423 end

    def Function_37_4449(): pass

    label("Function_37_4449")

    OP_D2(0x2703A8, 0x2703B2, 0xE)
    OP_D2(0x2703AE, 0x2703B8, 0x10)
    OP_D2(0x290216, 0x29021A, 0x12)
    OP_D2(0x270110, 0x270120, 0x13)
    OP_D2(0x270130, 0x270140, 0x14)
    OP_D2(0x702B4, 0x702BB, 0x15)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_44AA"),
        (3, "loc_44B7"),
        (4, "loc_44C4"),
        (5, "loc_44D1"),
        (6, "loc_44DE"),
        (7, "loc_44EB"),
        (8, "loc_44F8"),
        (SWITCH_DEFAULT, "loc_4505"),
    )


    label("loc_44AA")

    OP_D2(0x701D0, 0x701DC, 0x16)
    Jump("loc_4505")

    label("loc_44B7")

    OP_D2(0x701E8, 0x701F4, 0x16)
    Jump("loc_4505")

    label("loc_44C4")

    OP_D2(0x27036E, 0x27037B, 0x16)
    Jump("loc_4505")

    label("loc_44D1")

    OP_D2(0x70218, 0x70224, 0x16)
    Jump("loc_4505")

    label("loc_44DE")

    OP_D2(0x70230, 0x7023C, 0x16)
    Jump("loc_4505")

    label("loc_44EB")

    OP_D2(0x70248, 0x70254, 0x16)
    Jump("loc_4505")

    label("loc_44F8")

    OP_D2(0x270176, 0x270183, 0x16)
    Jump("loc_4505")

    label("loc_4505")

    Return()

    # Function_37_4449 end

    SaveToFile()

Try(main)
