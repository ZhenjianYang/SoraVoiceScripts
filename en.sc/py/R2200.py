from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2200.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        'Matron Theresa',                       # 9
        'Clem',                                 # 10
        'Polly',                                # 11
        'Mary',                                 # 12
        'Daniel',                               # 13
        'Kurt',                                 # 14
        'Anelace',                              # 15
        'Grant',                                # 16
        'Carna',                                # 17
        'Royal Army Soldier',                   # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Steel Cougar',                         # 21
        'Steel Cougar',                         # 22
        'Steel Cougar',                         # 23
        'Steel Cougar',                         # 24
        'Steel Cougar',                         # 25
        'Steel Cougar',                         # 26
        'Steel Cougar',                         # 27
        'Steel Cougar',                         # 28
        'Steel Cougar',                         # 29
        'Steel Cougar',                         # 30
        'Targeting Camera',                     # 31
        'Target',                               # 32
        'Target',                               # 33
        'Target',                               # 34
        'Target',                               # 35
        'Manoria Village',                      # 36
        'Mercia Orphanage',                     # 37
        'Ruan',                                 # 38
        '',                                     # 39
        '',                                     # 40
        '',                                     # 41
        '',                                     # 42
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
        'ED6_DT29/CH12100 ._CH',             # 00
        'ED6_DT29/CH12101 ._CH',             # 01
        'ED6_DT29/CH12150 ._CH',             # 02
        'ED6_DT29/CH12151 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02590 ._CH',             # 05
        'ED6_DT07/CH02500 ._CH',             # 06
        'ED6_DT07/CH02630 ._CH',             # 07
        'ED6_DT07/CH02640 ._CH',             # 08
        'ED6_DT07/CH00412 ._CH',             # 09
        'ED6_DT07/CH00420 ._CH',             # 0A
        'ED6_DT07/CH00390 ._CH',             # 0B
        'ED6_DT07/CH00400 ._CH',             # 0C
        'ED6_DT07/CH00320 ._CH',             # 0D
        'ED6_DT29/CH12330 ._CH',             # 0E
        'ED6_DT07/CH00411 ._CH',             # 0F
        'ED6_DT07/CH00412 ._CH',             # 10
        'ED6_DT07/CH00415 ._CH',             # 11
        'ED6_DT07/CH00416 ._CH',             # 12
        'ED6_DT07/CH00421 ._CH',             # 13
        'ED6_DT07/CH00422 ._CH',             # 14
        'ED6_DT07/CH00391 ._CH',             # 15
        'ED6_DT07/CH00392 ._CH',             # 16
        'ED6_DT07/CH00401 ._CH',             # 17
        'ED6_DT07/CH00321 ._CH',             # 18
        'ED6_DT07/CH00326 ._CH',             # 19
        'ED6_DT29/CH12331 ._CH',             # 1A
        'ED6_DT29/CH12333 ._CH',             # 1B
        'ED6_DT07/CH00321 ._CH',             # 1C
        'ED6_DT07/CH01640 ._CH',             # 1D
        'ED6_DT07/CH01620 ._CH',             # 1E
        'ED6_DT07/CH01630 ._CH',             # 1F
        'ED6_DT07/CH01260 ._CH',             # 20
        'ED6_DT07/CH01240 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT29/CH12100P._CP',             # 00
        'ED6_DT29/CH12101P._CP',             # 01
        'ED6_DT29/CH12150P._CP',             # 02
        'ED6_DT29/CH12151P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02590P._CP',             # 05
        'ED6_DT07/CH02500P._CP',             # 06
        'ED6_DT07/CH02630P._CP',             # 07
        'ED6_DT07/CH02640P._CP',             # 08
        'ED6_DT07/CH00412P._CP',             # 09
        'ED6_DT07/CH00420P._CP',             # 0A
        'ED6_DT07/CH00390P._CP',             # 0B
        'ED6_DT07/CH00400P._CP',             # 0C
        'ED6_DT07/CH00320P._CP',             # 0D
        'ED6_DT29/CH12330P._CP',             # 0E
        'ED6_DT07/CH00411P._CP',             # 0F
        'ED6_DT07/CH00412P._CP',             # 10
        'ED6_DT07/CH00415P._CP',             # 11
        'ED6_DT07/CH00416P._CP',             # 12
        'ED6_DT07/CH00421P._CP',             # 13
        'ED6_DT07/CH00422P._CP',             # 14
        'ED6_DT07/CH00391P._CP',             # 15
        'ED6_DT07/CH00392P._CP',             # 16
        'ED6_DT07/CH00401P._CP',             # 17
        'ED6_DT07/CH00321P._CP',             # 18
        'ED6_DT07/CH00326P._CP',             # 19
        'ED6_DT29/CH12331P._CP',             # 1A
        'ED6_DT29/CH12333P._CP',             # 1B
        'ED6_DT07/CH00321P._CP',             # 1C
        'ED6_DT07/CH01640P._CP',             # 1D
        'ED6_DT07/CH01620P._CP',             # 1E
        'ED6_DT07/CH01630P._CP',             # 1F
        'ED6_DT07/CH01260P._CP',             # 20
        'ED6_DT07/CH01240P._CP',             # 21
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
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
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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


    DeclMonster(
        X                   = -96260,
        Z                   = -1950,
        Y                   = 27960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x184,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104740,
        Z                   = -5970,
        Y                   = 11000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81100,
        Z                   = -5870,
        Y                   = 13330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88220,
        Z                   = -5960,
        Y                   = 9810,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x18F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77980,
        TriggerZ            = -6870,
        TriggerY            = -11780,
        TriggerRange        = 1000,
        ActorX              = -77540,
        ActorZ              = -6730,
        ActorY              = -11140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 49,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_67A",          # 00, 0
        "Function_1_6D9",          # 01, 1
        "Function_2_72D",          # 02, 2
        "Function_3_8AA",          # 03, 3
        "Function_4_A37",          # 04, 4
        "Function_5_BD1",          # 05, 5
        "Function_6_1258",         # 06, 6
        "Function_7_1714",         # 07, 7
        "Function_8_3296",         # 08, 8
        "Function_9_32DF",         # 09, 9
        "Function_10_32F9",        # 0A, 10
        "Function_11_3313",        # 0B, 11
        "Function_12_332D",        # 0C, 12
        "Function_13_3347",        # 0D, 13
        "Function_14_3361",        # 0E, 14
        "Function_15_337B",        # 0F, 15
        "Function_16_33EE",        # 10, 16
        "Function_17_3461",        # 11, 17
        "Function_18_34D4",        # 12, 18
        "Function_19_3547",        # 13, 19
        "Function_20_35AF",        # 14, 20
        "Function_21_3617",        # 15, 21
        "Function_22_3636",        # 16, 22
        "Function_23_3655",        # 17, 23
        "Function_24_3674",        # 18, 24
        "Function_25_368D",        # 19, 25
        "Function_26_375A",        # 1A, 26
        "Function_27_3820",        # 1B, 27
        "Function_28_38E6",        # 1C, 28
        "Function_29_39AC",        # 1D, 29
        "Function_30_3A0D",        # 1E, 30
        "Function_31_3A75",        # 1F, 31
        "Function_32_3AD1",        # 20, 32
        "Function_33_3B12",        # 21, 33
        "Function_34_3B7A",        # 22, 34
        "Function_35_3BE2",        # 23, 35
        "Function_36_3C4A",        # 24, 36
        "Function_37_3E23",        # 25, 37
        "Function_38_4005",        # 26, 38
        "Function_39_4092",        # 27, 39
        "Function_40_42C8",        # 28, 40
        "Function_41_434C",        # 29, 41
        "Function_42_4372",        # 2A, 42
        "Function_43_4398",        # 2B, 43
        "Function_44_43BE",        # 2C, 44
        "Function_45_4416",        # 2D, 45
        "Function_46_445A",        # 2E, 46
        "Function_47_449E",        # 2F, 47
        "Function_48_4536",        # 30, 48
        "Function_49_4580",        # 31, 49
    )


    def Function_0_67A(): pass

    label("Function_0_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_690")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_6D8")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6AF")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_6D8")

    label("loc_6AF")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_6BB"),
        (SWITCH_DEFAULT, "loc_6D8"),
    )


    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_6D5")

    Jump("loc_6D8")

    label("loc_6D8")

    Return()

    # Function_0_67A end

    def Function_1_6D9(): pass

    label("Function_1_6D9")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x230026)
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x186A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C")
    OP_6F(0x0, 0)
    Jump("loc_713")

    label("loc_70C")

    OP_6F(0x0, 60)

    label("loc_713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725")
    OP_6F(0x1, 0)
    Jump("loc_72C")

    label("loc_725")

    OP_6F(0x1, 60)

    label("loc_72C")

    Return()

    # Function_1_6D9 end

    def Function_2_72D(): pass

    label("Function_2_72D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_894")

    label("loc_752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_894")

    label("loc_76B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_784")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_894")

    label("loc_784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_894")

    label("loc_79D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_894")

    label("loc_7B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_894")

    label("loc_7CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_894")

    label("loc_7E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_894")

    label("loc_801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_894")

    label("loc_81A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_894")

    label("loc_833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_894")

    label("loc_84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_865")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_894")

    label("loc_865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_894")

    label("loc_87E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_894")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_894")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_894")

    label("loc_8A9")

    Return()

    # Function_2_72D end

    def Function_3_8AA(): pass

    label("Function_3_8AA")

    OP_EA(0x2, 0xE0, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_982")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_91B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF8\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1302)
    Jump("loc_97F")

    label("loc_91B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF8\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF8\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_97F")

    Jump("loc_A29")

    label("loc_982")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You nearly tear the top of the chest of its\x01",
            "hinges in your excitement to open it. Your face\x01",
            "falls as you realize there's nothing inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A29")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8AA end

    def Function_4_A37(): pass

    label("Function_4_A37")

    OP_EA(0x2, 0xE1, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x260, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_AA8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1303)
    Jump("loc_B0C")

    label("loc_AA8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_B0C")

    Jump("loc_BC3")

    label("loc_B0F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05This chest is holding a beauty pageant with all its\x01",
            "other treasure chest friends. But beauty on the\x01",
            "outside can't save how empty it is on the inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BC3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A37 end

    def Function_5_BD1(): pass

    label("Function_5_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE2")
    Call(0, 47)

    label("loc_BE2")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -28930, -1990, 68170, 180)
    SetChrPos(0xF7, -27890, -2009, 67540, 180)
    ClearMapFlags(0x1)
    OP_6D(-28090, -2060, 66510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_C5D():
        OP_6D(-28100, -2000, 63110, 2800)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C5D)

    def lambda_C75():
        OP_67(0, 9500, -10000, 2800)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_C75)

    def lambda_C8D():
        OP_8E(0xFE, 0xFFFF930E, 0x0, 0xF708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_C8D)

    def lambda_CA8():
        OP_8E(0xFE, 0xFFFF8EFE, 0x0, 0xF7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CA8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xF7, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F85")
    OP_8C(0x106, 270, 400)

    ChrTalk(    #6
        0x106,
        (
            "#051F#4PThe Matron still blows me away.\x01",
            "I was impressed with her before,\x01",
            "but...man.\x02\x03",

            "I can't help but feel humbled by women like\x01",
            "that, y'know? The queen's the same way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #7
        0x101,
        (
            "#1016F#3PHaha! You too, huh, Agate?\x02\x03",

            "#1017FYeah... She kinda reminds me\x01",
            "of Mom, that way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        (
            "#052F#4POh, yeah, the old man's wife.\x02\x03",

            "#552FShe died during the war, didn't she...?\x02\x03",

            "...Hrm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1004F#3PAgate? Something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x106,
        (
            "#552F#4PNah. Just...\x02\x03",

            "Women are strong, y'know?\x01",
            "Stronger than you'd think...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        "#1015F#3PWhat's this all of a sudden?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        (
            "#053F#4PAh, let it go. I'm...rambling.\x01",
            "Or something...\x02\x03",

            "#050FC'mon. Let's go collect the kids\x01",
            "from Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1252")

    label("loc_F85")

    OP_8C(0x103, 270, 400)

    ChrTalk(    #13
        0x103,
        (
            "#021F#4PMy, she's a wonderful person.\x02\x03",

            "Something about her reminds me of\x01",
            "Lena. Quite a few things, actually.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #14
        0x101,
        (
            "#1017F#3PYou thought so too, Schera?\x02\x03",

            "She reminds me a bit of Mom, too,\x01",
            "but more than anyone she reminds\x01",
            "me of the queen.\x02\x03",

            "She... I dunno...just warms your heart,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020F#4PIt's the compassionate heart of\x01",
            "a mature woman, really.\x02\x03",

            "#026F*sigh* I feel a bit inadequate on\x01",
            "that score in comparison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1006F#3PHey, you do a pretty good job\x01",
            "at it, too, Schera.\x02\x03",

            "I mean, if you want to be better at it,\x01",
            "maybe cutting back on the booze\x01",
            "would help a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#025F#4POuch...\x01",
            "Right for the jugular, there, Estelle.\x02\x03",

            "#020FAnyway. Let's get to Manoria and\x01",
            "collect the kids, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1252")

    OP_A2(0x1217)
    EventEnd(0x0)
    Return()

    # Function_5_BD1 end

    def Function_6_1258(): pass

    label("Function_6_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1269")
    Call(0, 47)

    label("loc_1269")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -27520, -1970, 67560, 197)
    SetChrPos(0xF7, -28770, -2040, 67850, 173)
    SetChrPos(0x109, -28090, -2000, 66790, 186)
    OP_6D(-27790, -1950, 68340, 0)
    OP_67(0, 10060, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_12F0():
        OP_6D(-28370, -1950, 60060, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_12F0)

    def lambda_1308():
        OP_67(0, 10060, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1308)

    def lambda_1320():
        OP_8E(0xFE, 0xFFFF90F2, 0xFFFFF844, 0xE5C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1320)
    Sleep(500)

    def lambda_1340():
        OP_8E(0xFE, 0xFFFF934A, 0xFFFFF84E, 0xEC0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1340)
    Sleep(200)

    def lambda_1360():
        OP_8E(0xFE, 0xFFFF8DA0, 0xFFFFF844, 0xED3A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1360)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF7, 0x2)

    ChrTalk(    #18
        0x109,
        (
            "#1061FMaaaaan, those kids are energetic!\x02\x03",

            "#1062FGotta wonder, though, whether or not\x01",
            "their matron qualifies for sainthood.\x02\x03",

            "'Cause every single one of them was\x01",
            "among the most polite, wonderful kids\x01",
            "I've ever met!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1006FYeah, Matron Theresa's amazing.\x02\x03",

            "There's actually another...\x01",
            "er, girl, who helps out here too...\x02\x03",

            "She's busy with her school exams and\x01",
            "couldn't get out here today, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        (
            "#1062FHmm... Okay.\x02\x03",

            "#1060FAnyway, I'm headin' back\x01",
            "to Ruan for a bit.\x02\x03",

            "What about you guys?\x01",
            "Wanna come with?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_161D")

    ChrTalk(    #21
        0x106,
        (
            "#051F#3PWell, we've asked everything\x01",
            "we need to over here.\x02\x03",

            "And the road's always better with\x01",
            "company. Let's head out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C5")

    label("loc_161D")


    ChrTalk(    #22
        0x103,
        (
            "#021F#3PHmm. Well, we've nothing left\x01",
            "to investigate here...\x02\x03",

            "And, as they say, 'the journey is\x01",
            "more important than the destination,'\x01",
            "so, certainly. Let's be off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C5")


    ChrTalk(    #23
        0x101,
        (
            "#1006FIt's decided, then.\x02\x03",

            "Off we go to Ruan! Let's go!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x121A)
    OP_28(0x82, 0x2, 0x100)
    OP_28(0x82, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_6_1258 end

    def Function_7_1714(): pass

    label("Function_7_1714")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-45040, -2090, 25310, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(4610, 0)
    OP_6C(48000, 0)
    OP_6E(339, 0)
    SetChrPos(0x8, -35650, -2000, 30000, 90)
    SetChrPos(0x9, -36610, -2000, 30450, 90)
    SetChrPos(0xB, -36680, -2000, 29000, 90)
    SetChrPos(0xC, -37600, -2000, 30100, 90)
    SetChrPos(0xA, -37620, -2000, 29000, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0x11, -32070, -1990, 32290, 135)
    SetChrPos(0x12, -31520, -2000, 31180, 135)
    SetChrPos(0x13, -32080, -2000, 29670, 135)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    LoadEffect(0x0, "map\\\\mp008_00.eff")
    LoadEffect(0x1, "Craft\\\\cr000_00.eff")
    LoadEffect(0x2, "monster\\\\msc0290.eff")
    LoadEffect(0x3, "monster\\\\msc0100.eff")
    LoadEffect(0x4, "battle\\\\btgun00.eff")
    LoadEffect(0x5, "map\\\\mp003_00.eff")
    LoadEffect(0x6, "scraft\\\\sc000_11.eff")

    def lambda_18DE():
        OP_6D(-24600, -2000, 30160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18DE)
    OP_C8(0x200, 0x46, "C_PLAC18._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(-10080, -2000, 30010, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(1540, 0)
    OP_6C(72000, 0)
    OP_6E(562, 0)
    OP_43(0x14, 0x0, 0x0, 0x18)
    Sleep(150)
    OP_43(0xB, 0x3, 0x0, 0x28)
    OP_0D()

    def lambda_1970():
        OP_6D(-16810, -2000, 29970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1970)

    def lambda_1988():
        OP_67(0, 6040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1988)

    def lambda_19A0():
        OP_6B(1400, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19A0)

    def lambda_19B0():
        OP_6C(59000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19B0)
    WaitChrThread(0x14, 0x0)
    OP_44(0xB, 0x3)
    OP_23(0x13F)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-34180, -2000, 31670, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(33000, 0)
    OP_6E(378, 0)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x15)
    Sleep(100)
    OP_43(0x12, 0x0, 0x0, 0x16)
    Sleep(100)
    OP_43(0x13, 0x0, 0x0, 0x17)
    WaitChrThread(0x12, 0x0)

    def lambda_1A3D():
        OP_8F(0xFE, 0xFFFF7ED2, 0xFFFFF83A, 0x7E22, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1A3D)
    Sleep(100)

    def lambda_1A5D():
        OP_8F(0xFE, 0xFFFF7EC8, 0xFFFFF830, 0x73E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1A5D)
    Sleep(100)

    def lambda_1A7D():
        OP_8F(0xFE, 0xFFFF80F8, 0xFFFFF830, 0x79CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1A7D)

    ChrTalk(    #24
        0x12,
        "#6PNgh! Still chasing us, are they...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#6PJust a little further and we can meet up\x01",
            "with the Manoria Garrison...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x13,
        (
            "#6PDon't stop now! We MUST see\x01",
            "these people safely there!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x11, 0x1, 0x0, 0x21)
    Sleep(100)
    OP_43(0x12, 0x1, 0x0, 0x22)
    Sleep(100)
    OP_43(0x13, 0x1, 0x0, 0x23)
    Sleep(1000)

    ChrTalk(    #27
        0xB,
        "#1901F#5PM-Matron Theresaaaa...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(    #28
        0x8,
        (
            "#754F#2PDon't worry, Mary... We'll be fine.\x02\x03",

            "#750FI won't let them lay a finger on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #29
        0xA,
        (
            "#1733F#5PWe're in a loooot of trouble,\x01",
            "aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "#752F#2P#3SOh, no!\x02",
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x2)
    OP_43(0x17, 0x3, 0x0, 0x2)
    SetChrPos(0x14, -58610, -1700, 17850, 90)
    SetChrPos(0x15, -61080, -1700, 19330, 90)
    SetChrPos(0x16, -59760, -1700, 15360, 90)
    SetChrPos(0x17, -62900, -1700, 16980, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x14, 0x800)
    SetChrFlags(0x15, 0x800)
    SetChrFlags(0x16, 0x800)
    SetChrFlags(0x17, 0x800)

    def lambda_1CFE():
        OP_6D(-60930, -2000, 17930, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CFE)

    def lambda_1D16():
        OP_67(0, 4890, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D16)

    def lambda_1D2E():
        OP_6B(2250, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D2E)

    def lambda_1D3E():
        OP_6C(299000, 4000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1D3E)

    def lambda_1D4E():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1D4E)

    def lambda_1D5E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D5E)
    Sleep(80)

    def lambda_1D71():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D71)
    Sleep(50)

    def lambda_1D84():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D84)
    OP_8E(0x8, 0xFFFF7414, 0xFFFFF830, 0x6EF0, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFF6B22, 0xFFFFF830, 0x6C3E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFF68D4, 0xFFFFF830, 0x7030, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Fade(500)
    OP_6D(-36180, -2000, 31670, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(33000, 0)
    OP_6E(378, 0)
    OP_44(0x11, 0x1)
    OP_44(0x13, 0x1)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x11, 13)
    SetChrChipByIndex(0x13, 13)
    OP_8C(0x11, 270, 0)
    OP_8C(0x13, 270, 0)
    OP_8C(0x14, 90, 0)
    OP_8C(0x15, 90, 0)
    OP_8C(0x16, 90, 0)
    OP_8C(0x17, 90, 0)
    ClearChrFlags(0x14, 0x800)
    ClearChrFlags(0x15, 0x800)
    ClearChrFlags(0x16, 0x800)
    ClearChrFlags(0x17, 0x800)
    OP_0D()

    ChrTalk(    #31
        0x13,
        "#2PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        "#4PFrom the opposite side?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #33
        0xC,
        "#1723F#2PWaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#776F#2POkay, you jerks!\x01",
            "I guess I gotta--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "#755F#5PNO, CLEM! Get back here!\x02\x03",

            "#757F(Oh, Aidios...please, save us,\x01",
            "your powerless children...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_44(0x12, 0x1)
    OP_6D(-58200, -2000, 18040, 0)
    OP_67(0, 4530, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(255000, 0)
    OP_6E(371, 0)

    def lambda_1FB9():
        OP_6D(-51550, -2000, 22170, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FB9)
    OP_43(0xB, 0x3, 0x0, 0x28)
    OP_43(0x14, 0x0, 0x0, 0x19)
    Sleep(200)
    OP_43(0x15, 0x0, 0x0, 0x1A)
    Sleep(250)
    OP_43(0x16, 0x0, 0x0, 0x1B)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0x1C)
    Sleep(1000)
    OP_20(0x3E8)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_1D(0x2C)
    Sleep(500)
    Fade(500)
    OP_6D(-49530, -2000, 23670, 0)
    OP_67(0, 6880, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(20000, 0)
    OP_6E(355, 0)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xE, -50890, 300, 35800, 225)
    SetChrPos(0xD, -50890, 300, 35800, 225)
    SetChrPos(0xF, -50890, 300, 35800, 225)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xF, 0x40)
    OP_43(0xF, 0x1, 0x0, 0x24)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x25)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x27)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)

    def lambda_20FC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_20FC)

    def lambda_210A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_210A)
    Sleep(1000)

    def lambda_211D():
        OP_6D(-57190, -2000, 18670, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_211D)
    OP_7D(0x0, 0xE, 0x32, 0x1F4)
    OP_7D(0x0, 0xD, 0x32, 0x1F4)
    OP_7D(0x0, 0xF, 0x32, 0x1F4)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 20)

    def lambda_2157():
        OP_99(0xFE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2157)

    def lambda_2167():
        OP_99(0xFE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2167)

    def lambda_2177():
        OP_99(0xFE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2177)

    def lambda_2187():
        OP_8F(0xFE, 0xFFFF1EE2, 0xFFFFF830, 0x47EA, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2187)

    def lambda_21A2():
        OP_8F(0xFE, 0xFFFF225C, 0xFFFFF830, 0x45A6, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_21A2)

    def lambda_21BD():
        OP_8F(0xFE, 0xFFFF1EF6, 0xFFFFF830, 0x4CCC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_21BD)
    OP_22(0x9B, 0x0, 0x64)
    Sleep(100)
    OP_44(0x17, 0x3)
    SetChrChipByIndex(0x17, 27)
    SetChrSubChip(0x17, 0)
    WaitChrThread(0xE, 0x2)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xF, 0x2)
    OP_7D(0x1, 0xE, 0x0, 0x0)
    OP_7D(0x1, 0xD, 0x0, 0x0)
    OP_7D(0x1, 0xF, 0x0, 0x0)
    PlayEffect(0x3, 0x0, 0x17, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    SetChrFlags(0x17, 0x80)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-37000, -2000, 30060, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(24000, 0)
    OP_6E(282, 0)
    SetChrPos(0x11, -35550, -2000, 30860, 270)
    SetChrPos(0x12, -34880, -2000, 29770, 270)
    SetChrPos(0x13, -34710, -2000, 28220, 270)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x11, 29)
    SetChrChipByIndex(0x12, 29)
    SetChrChipByIndex(0x13, 29)
    OP_8C(0x12, 270, 0)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xF, 0x20)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 30)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 31)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 32)

    def lambda_2329():
        OP_8E(0xFE, 0xFFFF5E84, 0xFFFFF830, 0x6B6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2329)
    OP_0D()
    SetMapFlags(0x10)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)

    def lambda_2366():
        OP_8E(0xFE, 0xFFFF5ACE, 0xFFFFF830, 0x6E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2366)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_242C():
        OP_8E(0xFE, 0xFFFF5E02, 0xFFFFF830, 0x65A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_242C)
    WaitChrThread(0xD, 0x1)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)

    ChrTalk(    #36
        0x11,
        "#4PWho're you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "#774F#4PHey, they're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#1714F#4PBracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xF,
        "#821F#5PHeh! Sorry to keep ya waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        "#811F#5PEveryone okay? Nobody hurt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        "#1720F#4PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        "#1732F#4PWe're fiiiiine!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, -44820, 0, 51380, 135)

    NpcTalk(    #43
        0x10,
        "Woman's Voice",
        "Haha! Good to see we made it.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrPos(0x10, -48280, 0, 36210, 135)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 33)

    def lambda_259C():
        OP_6D(-40770, -2000, 33410, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_259C)

    def lambda_25B4():
        OP_67(0, 3940, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25B4)

    def lambda_25CC():
        OP_6B(2880, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25CC)

    def lambda_25DC():
        OP_6C(327000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_25DC)

    def lambda_25EC():
        OP_6E(367, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_25EC)

    def lambda_25FC():
        OP_8E(0xFE, 0xFFFF59E8, 0x0, 0x8016, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_25FC)

    def lambda_2617():

        label("loc_2617")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2617")

    QueueWorkItem2(0x8, 1, lambda_2617)

    def lambda_2628():

        label("loc_2628")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2628")

    QueueWorkItem2(0x9, 1, lambda_2628)

    def lambda_2639():

        label("loc_2639")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2639")

    QueueWorkItem2(0xC, 1, lambda_2639)

    def lambda_264A():

        label("loc_264A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_264A")

    QueueWorkItem2(0x11, 1, lambda_264A)

    def lambda_265B():

        label("loc_265B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_265B")

    QueueWorkItem2(0xF, 1, lambda_265B)
    Sleep(100)

    def lambda_2671():

        label("loc_2671")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2671")

    QueueWorkItem2(0xB, 1, lambda_2671)

    def lambda_2682():

        label("loc_2682")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2682")

    QueueWorkItem2(0xA, 1, lambda_2682)

    def lambda_2693():

        label("loc_2693")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2693")

    QueueWorkItem2(0x12, 1, lambda_2693)

    def lambda_26A4():

        label("loc_26A4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26A4")

    QueueWorkItem2(0xE, 1, lambda_26A4)
    Sleep(100)

    def lambda_26BA():

        label("loc_26BA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26BA")

    QueueWorkItem2(0x13, 1, lambda_26BA)

    def lambda_26CB():

        label("loc_26CB")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_26CB")

    QueueWorkItem2(0xD, 1, lambda_26CB)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x10, 0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0xD, 0x1)
    Sleep(500)

    ChrTalk(    #44
        0x8,
        "#753F#5PCarna!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#831F#6PSorry to meet you again\x01",
            "like this, Matron Theresa!\x02\x03",

            "You're evacuating to Manoria, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#750F#5PYes, the good soldiers\x01",
            "here were escorting us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27CD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27CD)
    Sleep(100)

    def lambda_27E0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_27E0)
    Sleep(100)

    def lambda_27F3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_27F3)
    Sleep(400)

    ChrTalk(    #47
        0xD,
        (
            "#842F#5PYou there, soldiers!\x01",
            "We shall hold them here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "#816F#5PYeah! You guys hurry and\x01",
            "get the kids to Manoria!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#2PY-You have our thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x13,
        "#2PEveryone! Follow us!\x02",
    )

    CloseMessageWindow()

    def lambda_28BC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28BC)
    Sleep(80)

    def lambda_28CF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28CF)

    def lambda_28DD():

        label("loc_28DD")

        OP_8C(0xFE, 90, 400)
        OP_48()
        Jump("loc_28DD")

    QueueWorkItem2(0xB, 1, lambda_28DD)
    Sleep(80)

    def lambda_28F3():

        label("loc_28F3")

        OP_8C(0xFE, 90, 400)
        OP_48()
        Jump("loc_28F3")

    QueueWorkItem2(0xA, 1, lambda_28F3)
    Sleep(50)

    def lambda_2909():

        label("loc_2909")

        OP_8C(0xFE, 90, 400)
        OP_48()
        Jump("loc_2909")

    QueueWorkItem2(0xC, 1, lambda_2909)
    Sleep(400)

    ChrTalk(    #51
        0x9,
        "#770F#5POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        "#1731F#5PComiiiiing!\x02",
    )

    CloseMessageWindow()
    OP_43(0x13, 0x1, 0x0, 0x2E)
    OP_43(0x12, 0x1, 0x0, 0x2D)
    Sleep(100)
    OP_43(0xD, 0x1, 0x0, 0x2B)

    def lambda_2966():

        label("loc_2966")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2966")

    QueueWorkItem2(0x10, 3, lambda_2966)
    Sleep(200)
    OP_43(0xF, 0x1, 0x0, 0x29)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x2A)

    def lambda_298F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_298F)

    def lambda_299D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_299D)

    def lambda_29AB():

        label("loc_29AB")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_29AB")

    QueueWorkItem2(0x8, 1, lambda_29AB)

    def lambda_29BC():

        label("loc_29BC")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_29BC")

    QueueWorkItem2(0x9, 1, lambda_29BC)

    def lambda_29CD():

        label("loc_29CD")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_29CD")

    QueueWorkItem2(0xC, 1, lambda_29CD)

    def lambda_29DE():

        label("loc_29DE")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_29DE")

    QueueWorkItem2(0xB, 1, lambda_29DE)

    def lambda_29EF():

        label("loc_29EF")

        OP_8C(0xFE, 270, 400)
        OP_48()
        Jump("loc_29EF")

    QueueWorkItem2(0xA, 1, lambda_29EF)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x13, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xA, 0x1)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 24)

    def lambda_2A2D():
        OP_8E(0xFE, 0xFFFF33A0, 0xFFFFF830, 0x5442, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A2D)
    Sleep(50)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x13, 24)

    def lambda_2A57():
        OP_8E(0xFE, 0xFFFF2D56, 0xFFFFF84E, 0x5ADC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2A57)
    Sleep(100)

    def lambda_2A77():
        OP_8E(0xFE, 0xFFFF3684, 0xFFFFF830, 0x5906, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A77)

    def lambda_2A92():
        OP_6D(-39740, -1500, 29550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A92)

    def lambda_2AAA():
        OP_67(0, 5590, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AAA)

    def lambda_2AC2():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AC2)

    def lambda_2AD2():
        OP_6C(306000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AD2)

    def lambda_2AE2():
        OP_6E(367, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AE2)
    Sleep(100)

    def lambda_2AF7():
        OP_8E(0xFE, 0xFFFF3C6A, 0xFFFFF830, 0x56EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2AF7)
    Sleep(50)

    def lambda_2B17():
        OP_8E(0xFE, 0xFFFF3738, 0xFFFFF830, 0x5FC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B17)
    Sleep(100)

    def lambda_2B37():
        OP_8E(0xFE, 0xFFFF3C6A, 0xFFFFF830, 0x56EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2B37)

    def lambda_2B52():
        OP_8E(0xFE, 0xFFFF3738, 0xFFFFF830, 0x5FC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B52)
    Sleep(100)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 24)

    def lambda_2B7C():
        OP_8E(0xFE, 0xFFFF3B8E, 0xFFFFF830, 0x5C26, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B7C)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0xF, 0x3)
    OP_44(0x10, 0x3)
    OP_44(0xE, 0x3)
    OP_44(0xD, 0x3)
    OP_8C(0xD, 45, 400)

    def lambda_2BE0():
        OP_8E(0xFE, 0xFFFF696A, 0xFFFFF830, 0x6D6A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2BE0)
    Sleep(100)
    OP_8C(0x10, 135, 400)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2C0C():
        OP_96(0xFE, 0xFFFF6794, 0xFFFFF830, 0x73BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2C0C)
    Sleep(100)
    WaitChrThread(0xD, 0x0)
    OP_8C(0xD, 90, 400)
    WaitChrThread(0x10, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2C45():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2C45)
    Sleep(100)

    def lambda_2C58():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2C58)
    Sleep(100)
    OP_8C(0xE, 90, 400)
    Fade(1000)
    OP_6D(-16780, -2000, 30390, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(89000, 0)
    OP_6E(349, 0)

    def lambda_2CB4():
        OP_6C(53000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2CB4)
    OP_43(0x14, 0x0, 0x0, 0xF)
    Sleep(200)
    OP_43(0xB, 0x3, 0x0, 0x28)
    Sleep(200)
    OP_43(0x15, 0x0, 0x0, 0x10)
    Sleep(400)
    OP_43(0x16, 0x0, 0x0, 0x11)
    Sleep(400)
    OP_43(0x17, 0x0, 0x0, 0x12)
    Sleep(400)
    OP_43(0x18, 0x0, 0x0, 0x13)
    Sleep(400)
    OP_43(0x19, 0x0, 0x0, 0x14)
    WaitChrThread(0x19, 0x0)
    OP_44(0xB, 0x3)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    SetChrPos(0xD, -37670, -2000, 29370, 90)
    SetChrPos(0xF, -39320, -2000, 30070, 90)
    SetChrPos(0xE, -39100, -2000, 27880, 90)
    SetChrPos(0x10, -41230, -2000, 28610, 90)
    SetChrChipByIndex(0xD, 9)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xF, 11)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xE, 10)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)

    def lambda_2D92():
        OP_6D(-37540, -2000, 29550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D92)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #53
        0xF,
        (
            "#825F#1PAlllrighty. Looks like we've got\x01",
            "our work cut out for us, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        "#835F#5PWe still have to do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        (
            "#816F#2PDon't worry, this is nothing!\x02\x03",

            "Compared to what Estelle and\x01",
            "everyone have to deal with at\x01",
            "those towers, this is a picnic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "#840F#6PIndeed!\x02\x03",

            "All we can do is do our best\x01",
            "here so they can fight without\x01",
            "worrying for their loved ones.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0xD,
        "#843F#6PBy my arts--become hard as steel!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 18)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    PlayEffect(0x1, 0x0, 0xD, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0xD, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x2, 0xE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x3, 0xF, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x2, 0x4, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x4, 0x2)
    Sleep(500)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #58
        0xD,
        "#846F#6PCome, everyone! For Liberl!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #59
        0xE,
        "#815F#1KWoo!\x02",
    )


    ChrTalk(    #60
        0xF,
        "#822F#1K#1PHell yeah!\x02",
    )


    ChrTalk(    #61
        0x10,
        "#832F#1K#3PLet's go!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()

    def lambda_3153():
        OP_6D(-26760, -2000, 31240, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3153)

    def lambda_316B():
        OP_6B(2390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_316B)
    FadeToDark(2000, 0, -1)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 15)

    def lambda_318F():
        OP_8F(0xFE, 0xFFFF8DFA, 0xFFFFF830, 0x7A08, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_318F)
    Sleep(100)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 19)

    def lambda_31B9():
        OP_8F(0xFE, 0xFFFF897C, 0xFFFFF830, 0x7454, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_31B9)
    Sleep(50)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 21)

    def lambda_31E3():
        OP_8F(0xFE, 0xFFFF87D8, 0xFFFFF830, 0x7CA6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_31E3)
    Sleep(100)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 23)

    def lambda_320D():
        OP_8F(0xFE, 0xFFFF8404, 0xFFFFF830, 0x771A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_320D)
    OP_43(0x14, 0x1, 0x0, 0x8)
    OP_43(0xB, 0x3, 0x0, 0x28)
    OP_A2(0x0)
    Sleep(100)
    OP_0D()
    OP_20(0x7D0)
    Sleep(200)
    OP_24(0x1C8, 0x5A)
    Sleep(200)
    OP_24(0x1C8, 0x50)
    Sleep(200)
    OP_24(0x1C8, 0x46)
    Sleep(200)
    OP_24(0x1C8, 0x3C)
    Sleep(200)
    OP_24(0x1C8, 0x32)
    Sleep(200)
    OP_24(0x1C8, 0x28)
    Sleep(200)
    OP_24(0x1C8, 0x1E)
    Sleep(200)
    OP_23(0x1C8)
    OP_21()
    OP_A2(0x1E2F)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1714 end

    def Function_8_3296(): pass

    label("Function_8_3296")

    Sleep(500)
    OP_43(0x14, 0x0, 0x0, 0x9)
    Sleep(200)
    OP_43(0x15, 0x0, 0x0, 0xA)
    Sleep(200)
    OP_43(0x16, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0xC)
    Sleep(200)
    OP_43(0x18, 0x0, 0x0, 0xD)
    Sleep(200)
    OP_43(0x19, 0x0, 0x0, 0xE)
    Return()

    # Function_8_3296 end

    def Function_9_32DF(): pass

    label("Function_9_32DF")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_9_32DF end

    def Function_10_32F9(): pass

    label("Function_10_32F9")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_10_32F9 end

    def Function_11_3313(): pass

    label("Function_11_3313")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_11_3313 end

    def Function_12_332D(): pass

    label("Function_12_332D")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_12_332D end

    def Function_13_3347(): pass

    label("Function_13_3347")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_13_3347 end

    def Function_14_3361(): pass

    label("Function_14_3361")

    SetChrChipByIndex(0xFE, 26)
    OP_90(0xFE, 0xFFFFEC78, 0xFFFFFF38, 0x1F4, 0x1388, 0x0)
    Return()

    # Function_14_3361 end

    def Function_15_337B(): pass

    label("Function_15_337B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFB302, 0xFFFFF92A, 0x79F4, 0x1770, 0x0)
    SetChrPos(0xFE, -19710, -1600, 31220, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_15_337B end

    def Function_16_33EE(): pass

    label("Function_16_33EE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFAF6A, 0xFFFFF92A, 0x7094, 0x1770, 0x0)
    SetChrPos(0xFE, -20630, -1600, 28820, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_16_33EE end

    def Function_17_3461(): pass

    label("Function_17_3461")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFBBFE, 0xFFFFF92A, 0x6E46, 0x1770, 0x0)
    SetChrPos(0xFE, -17410, -1600, 28230, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_17_3461 end

    def Function_18_34D4(): pass

    label("Function_18_34D4")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC07C, 0xFFFFF92A, 0x7738, 0x1770, 0x0)
    SetChrPos(0xFE, -16260, -1600, 30520, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_18_34D4 end

    def Function_19_3547(): pass

    label("Function_19_3547")

    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC9E6, 0xFFFFF92A, 0x72F6, 0x1770, 0x0)
    SetChrPos(0xFE, -13850, -1600, 29430, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_19_3547 end

    def Function_20_35AF(): pass

    label("Function_20_35AF")

    SetChrPos(0xFE, -2790, -1750, 30120, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFD760, 0xFFFFF92A, 0x7404, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFD31E, 0xFFFFF92A, 0x713E, 0x1770, 0x0)
    SetChrPos(0xFE, -11490, -1600, 28990, 270)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_20_35AF end

    def Function_21_3617(): pass

    label("Function_21_3617")

    SetChrChipByIndex(0xFE, 28)
    OP_8F(0xFE, 0xFFFF7ED2, 0xFFFFF830, 0x7E22, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_21_3617 end

    def Function_22_3636(): pass

    label("Function_22_3636")

    SetChrChipByIndex(0xFE, 28)
    OP_8F(0xFE, 0xFFFF80F8, 0xFFFFF830, 0x79CC, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_22_3636 end

    def Function_23_3655(): pass

    label("Function_23_3655")

    SetChrChipByIndex(0xFE, 28)
    OP_8F(0xFE, 0xFFFF7EC8, 0xFFFFF830, 0x73E6, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    Return()

    # Function_23_3655 end

    def Function_24_3674(): pass

    label("Function_24_3674")

    OP_43(0x14, 0x1, 0x0, 0x1D)
    Sleep(600)
    OP_43(0x15, 0x1, 0x0, 0x1E)
    WaitChrThread(0x15, 0x1)
    Return()

    # Function_24_3674 end

    def Function_25_368D(): pass

    label("Function_25_368D")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF2BF8, 0xFFFFF95C, 0x4E3E, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF3EEA, 0xFFFFF95C, 0x5C62, 0x1770, 0x0)
    SetChrPos(0xFE, -49430, -1500, 23650, 45)
    OP_44(0xFE, 0x3)
    OP_44(0xB, 0x3)
    OP_23(0x13F)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x14, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_25_368D end

    def Function_26_375A(): pass

    label("Function_26_375A")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF2324, 0xFFFFF95C, 0x4E48, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF336E, 0xFFFFF95C, 0x5D3E, 0x1770, 0x0)
    SetChrPos(0xFE, -52370, -1500, 23870, 45)
    OP_44(0xFE, 0x3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x15, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_26_375A end

    def Function_27_3820(): pass

    label("Function_27_3820")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF2CC0, 0xFFFFF95C, 0x454C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF39F4, 0xFFFFF95C, 0x4F38, 0x1770, 0x0)
    SetChrPos(0xFE, -50700, -1500, 20280, 45)
    OP_44(0xFE, 0x3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x16, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_27_3820 end

    def Function_28_38E6(): pass

    label("Function_28_38E6")

    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFF1E56, 0xFFFFF95C, 0x4632, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFF2B76, 0xFFFFF95C, 0x4F4C, 0x1770, 0x0)
    SetChrPos(0xFE, -54410, -1500, 20300, 45)
    OP_44(0xFE, 0x3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0x17, 3000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 14)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_28_38E6 end

    def Function_29_39AC(): pass

    label("Function_29_39AC")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFD396, 0xFFFFF92A, 0x74F4, 0x1770, 0x0)
    OP_8F(0xFE, 0xFFFFBCEE, 0xFFFFF92A, 0x771A, 0x1770, 0x0)
    SetChrPos(0xFE, -17170, -1600, 30490, 270)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_29_39AC end

    def Function_30_3A0D(): pass

    label("Function_30_3A0D")

    OP_43(0xFE, 0x3, 0x0, 0x2)
    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFD396, 0xFFFFF92A, 0x74F4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFBB86, 0xFFFFF92A, 0x6B6C, 0x1770, 0x0)
    SetChrPos(0xFE, -17530, -1600, 27500, 270)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_30_3A0D end

    def Function_31_3A75(): pass

    label("Function_31_3A75")

    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFD396, 0xFFFFF92A, 0x74F4, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFC50E, 0xFFFFF92A, 0x6EC8, 0x1770, 0x0)
    SetChrPos(0xFE, -15090, -1600, 28360, 270)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_31_3A75 end

    def Function_32_3AD1(): pass

    label("Function_32_3AD1")

    SetChrPos(0xFE, 6670, -1750, 29940, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 26)
    OP_8F(0xFE, 0xFFFFCA40, 0xFFFFF92A, 0x759E, 0x1388, 0x0)
    SetChrPos(0xFE, -13760, -1600, 30110, 270)
    Return()

    # Function_32_3AD1 end

    def Function_33_3B12(): pass

    label("Function_33_3B12")

    SetChrChipByIndex(0xFE, 25)

    label("loc_3B17")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B79")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x50)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(550)
    Jump("loc_3B17")

    label("loc_3B79")

    Return()

    # Function_33_3B12 end

    def Function_34_3B7A(): pass

    label("Function_34_3B7A")

    SetChrChipByIndex(0xFE, 25)

    label("loc_3B7F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BE1")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x50)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(600)
    Jump("loc_3B7F")

    label("loc_3BE1")

    Return()

    # Function_34_3B7A end

    def Function_35_3BE2(): pass

    label("Function_35_3BE2")

    SetChrChipByIndex(0xFE, 25)

    label("loc_3BE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C49")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x50)
    PlayEffect(0x4, 0xFF, 0xFE, 0, 900, 1100, -45, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(500)
    Jump("loc_3BE7")

    label("loc_3C49")

    Return()

    # Function_35_3BE2 end

    def Function_36_3C4A(): pass

    label("Function_36_3C4A")

    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFF4F20, 0xFFFFF830, 0x5D8E, 0x4B0, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 225, 400)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x4)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFF4052, 0xFFFFF830, 0x51E0, 0x1770, 0x0)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 22)

    def lambda_3CAA():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CAA)
    Sleep(300)
    PlayEffect(0x6, 0xFF, 0x16, 0, 800, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_44(0x16, 0x3)
    SetChrChipByIndex(0x16, 27)
    SetChrSubChip(0x16, 0)

    def lambda_3D13():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3D13)
    Sleep(300)

    def lambda_3D32():
        OP_96(0xFE, 0xFFFF4052, 0xFFFFF830, 0x51E0, 0xBB8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D32)

    def lambda_3D50():
        OP_99(0xFE, 0x7, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D50)
    OP_44(0x16, 0x1)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x800)
    OP_99(0xFE, 0x0, 0x4, 0xDAC)
    WaitChrThread(0xFE, 0x3)
    PlayEffect(0x6, 0xFF, 0x16, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_3DC2():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3DC2)

    def lambda_3DDC():
        OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3DDC)
    OP_94(0x1, 0x16, 0x0, 0xFFFFE0C0, 0x5DC0, 0x0)
    OP_44(0x16, 0x1)
    OP_22(0x20B, 0x0, 0x64)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0xFE, 0x800)
    OP_99(0xFE, 0x4, 0x7, 0x9C4)
    SetChrSubChip(0xFE, 1)
    Return()

    # Function_36_3C4A end

    def Function_37_3E23(): pass

    label("Function_37_3E23")

    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFF506A, 0xFFFFF830, 0x64FA, 0x44C, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 225, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 19)
    OP_8E(0xFE, 0xFFFF43A4, 0xFFFFF830, 0x5D5C, 0x1770, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 20)

    def lambda_3E79():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E79)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x6, 0xFF, 0x14, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x14, 0x3)
    SetChrChipByIndex(0x14, 27)
    SetChrSubChip(0x14, 0)

    def lambda_3EE2():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3EE2)
    WaitChrThread(0xFE, 0x2)

    def lambda_3F01():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F01)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0x14, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_44(0x14, 0x1)
    WaitChrThread(0xFE, 0x2)
    SetChrChipByIndex(0x14, 14)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0xFE, 1)

    def lambda_3F74():
        OP_96(0xFE, 0xFFFF43A4, 0xFFFFF830, 0x5D5C, 0xFA0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3F74)
    WaitChrThread(0xFE, 0x3)

    def lambda_3F97():
        OP_99(0xE, 0x1, 0x4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F97)
    OP_43(0x14, 0x3, 0x0, 0x26)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x2)

    def lambda_3FB8():
        OP_96(0xFE, 0xFFFF4548, 0xFFFFF830, 0x5E88, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3FB8)
    SetChrSubChip(0xFE, 1)
    OP_99(0xFE, 0x0, 0x7, 0xFA0)
    OP_99(0xFE, 0x0, 0x7, 0xFA0)
    ClearChrFlags(0xFE, 0x2)
    WaitChrThread(0xFE, 0x3)
    SetChrSubChip(0xFE, 0)

    def lambda_3FFC():
        TurnDirection(0xFE, 0x17, 0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_3FFC)
    Return()

    # Function_37_3E23 end

    def Function_38_4005(): pass

    label("Function_38_4005")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    PlayEffect(0x6, 0xFF, 0x14, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 27)
    SetChrSubChip(0x14, 0)

    def lambda_4060():
        OP_94(0x1, 0x14, 0x0, 0xFFFFEC78, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4060)

    def lambda_4076():
        OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4076)
    WaitChrThread(0x14, 0x0)
    OP_22(0x20B, 0x0, 0x64)
    SetChrFlags(0x14, 0x80)
    Return()

    # Function_38_4005 end

    def Function_39_4092(): pass

    label("Function_39_4092")

    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xFE, 0xFFFF455C, 0xFFFFF830, 0x6824, 0x3E8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0xFE, 225, 400)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0xFFFF3882, 0xFFFFF830, 0x5FAA, 0x1770, 0x0)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 16)

    def lambda_40F2():
        OP_99(0xFE, 0x0, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40F2)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0x15, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_44(0x15, 0x3)
    SetChrChipByIndex(0x15, 27)
    SetChrSubChip(0x15, 0)

    def lambda_415B():
        OP_9E(0xFE, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_415B)

    def lambda_4175():
        OP_99(0xFE, 0x0, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4175)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0x15, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_41DA():
        OP_96(0xFE, 0xFFFF4098, 0xFFFFF830, 0x66BC, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_41DA)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xFE, 1)
    WaitChrThread(0xFE, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)

    def lambda_4211():
        OP_8F(0xFE, 0xFFFF3832, 0xFFFFF830, 0x5FAA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4211)
    SetChrChipByIndex(0xD, 16)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x3, 0xBB8)
    WaitChrThread(0xFE, 0x3)
    PlayEffect(0x6, 0xFF, 0x15, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_428A():
        OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_428A)
    OP_94(0x1, 0x15, 0x0, 0xFFFFE890, 0x5DC0, 0x0)
    SetChrFlags(0x15, 0x80)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    OP_22(0x20B, 0x0, 0x64)
    ClearChrFlags(0x15, 0x20)
    OP_99(0xFE, 0x4, 0x7, 0x9C4)
    Return()

    # Function_39_4092 end

    def Function_40_42C8(): pass

    label("Function_40_42C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E7")
    OP_22(0x13F, 0x0, 0x4B)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x4B)
    Sleep(300)
    Jump("Function_40_42C8")

    label("loc_42E7")

    OP_22(0x13F, 0x0, 0x41)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x41)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x37)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x37)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x2D)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x2D)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x23)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x23)
    Sleep(300)
    OP_22(0x13F, 0x0, 0x19)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x19)
    Sleep(300)
    Return()

    # Function_40_42C8 end

    def Function_41_434C(): pass

    label("Function_41_434C")

    OP_8E(0xFE, 0xFFFF5FA6, 0xFFFFF830, 0x792C, 0xBB8, 0x0)

    def lambda_4366():

        label("loc_4366")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4366")

    QueueWorkItem2(0xFE, 3, lambda_4366)
    Return()

    # Function_41_434C end

    def Function_42_4372(): pass

    label("Function_42_4372")

    OP_8E(0xFE, 0xFFFF5D08, 0xFFFFF830, 0x75EE, 0xBB8, 0x0)

    def lambda_438C():

        label("loc_438C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_438C")

    QueueWorkItem2(0xFE, 3, lambda_438C)
    Return()

    # Function_42_4372 end

    def Function_43_4398(): pass

    label("Function_43_4398")

    OP_8E(0xFE, 0xFFFF680C, 0xFFFFF827, 0x60C2, 0xBB8, 0x0)

    def lambda_43B2():

        label("loc_43B2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_43B2")

    QueueWorkItem2(0xFE, 3, lambda_43B2)
    Return()

    # Function_43_4398 end

    def Function_44_43BE(): pass

    label("Function_44_43BE")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF6C1C, 0xFFFFF880, 0x7A9E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF678A, 0xFFFFF830, 0x7602, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF644C, 0xFFFFF830, 0x7008, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_44_43BE end

    def Function_45_4416(): pass

    label("Function_45_4416")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF7568, 0xFFFFF830, 0x6AF4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF67B2, 0xFFFFF830, 0x68C4, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_45_4416 end

    def Function_46_445A(): pass

    label("Function_46_445A")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFF67B2, 0xFFFFF830, 0x68C4, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF61D6, 0xFFFFF830, 0x6FEA, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 13)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_46_445A end

    def Function_47_449E(): pass

    label("Function_47_449E")

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
        (0, "loc_4517"),
        (1, "loc_451D"),
        (SWITCH_DEFAULT, "loc_4523"),
    )


    label("loc_4517")

    OP_A2(0x1200)
    Jump("loc_4523")

    label("loc_451D")

    OP_A2(0x1201)
    Jump("loc_4523")

    label("loc_4523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4531")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4535")

    label("loc_4531")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4535")

    Return()

    # Function_47_449E end

    def Function_48_4536(): pass

    label("Function_48_4536")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #62
        "\x07\x05North: Mercia Orphanage\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_48_4536 end

    def Function_49_4580(): pass

    label("Function_49_4580")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #63
        (
            "\x07\x05East: City of Ruan - 238 selge\x01",
            "West: Manoria Village - 74 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_4580 end

    SaveToFile()

Try(main)
