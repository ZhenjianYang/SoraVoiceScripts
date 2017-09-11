from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4200.x',
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
        'Private Dan',                          # 9
        'Private Aluts',                        # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Carna',                                # 15
        'Anelace',                              # 16
        'Grant',                                # 17
        'Kurt',                                 # 18
        '1st Lieutenant Schwarz',               # 19
        'Royal Guardsman',                      # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Royal Guardsman',                      # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Cassius',                              # 28
        'Cassius',                              # 29
        'Spectator',                            # 30
        'Spectator',                            # 31
        'Spectator',                            # 32
        'Spectator',                            # 33
        'Spectator',                            # 34
        'Spectator',                            # 35
        'Spectator',                            # 36
        'Spectator',                            # 37
        'Spectator',                            # 38
        'Spectator',                            # 39
        'Spectator',                            # 40
        'Spectator',                            # 41
        'Spectator',                            # 42
        'Spectator',                            # 43
        'Spectator',                            # 44
        'Spectator',                            # 45
        'Spectator',                            # 46
        'Spectator',                            # 47
        'Spectator',                            # 48
        'Spectator',                            # 49
        'Spectator',                            # 50
        'Spectator',                            # 51
        'Spectator',                            # 52
        'Spectator',                            # 53
        'Spectator',                            # 54
        'Spectator',                            # 55
        'Spectator',                            # 56
        'Spectator',                            # 57
        'Spectator',                            # 58
        'Spectator',                            # 59
        'Spectator',                            # 60
        'Spectator',                            # 61
        'Spectator',                            # 62
        'Spectator',                            # 63
        'Spectator',                            # 64
        'Armand',                               # 65
        'Ellie',                                # 66
        'Tourist',                              # 67
        'Tourist',                              # 68
        'Tourist',                              # 69
        'Tourist',                              # 70
        'Grancel - North Block',                # 71
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02470 ._CH',             # 02
        'ED6_DT07/CH01610 ._CH',             # 03
        'ED6_DT07/CH00401 ._CH',             # 04
        'ED6_DT07/CH00421 ._CH',             # 05
        'ED6_DT07/CH00391 ._CH',             # 06
        'ED6_DT07/CH00411 ._CH',             # 07
        'ED6_DT06/CH20114 ._CH',             # 08
        'ED6_DT06/CH20116 ._CH',             # 09
        'ED6_DT07/CH02000 ._CH',             # 0A
        'ED6_DT06/CH20155 ._CH',             # 0B
        'ED6_DT06/CH20156 ._CH',             # 0C
        'ED6_DT06/CH20123 ._CH',             # 0D
        'ED6_DT06/CH20124 ._CH',             # 0E
        'ED6_DT06/CH20125 ._CH',             # 0F
        'ED6_DT07/CH01140 ._CH',             # 10
        'ED6_DT07/CH01150 ._CH',             # 11
        'ED6_DT07/CH01100 ._CH',             # 12
        'ED6_DT07/CH01480 ._CH',             # 13
        'ED6_DT07/CH01050 ._CH',             # 14
        'ED6_DT07/CH01040 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT07/CH01610P._CP',             # 03
        'ED6_DT07/CH00401P._CP',             # 04
        'ED6_DT07/CH00421P._CP',             # 05
        'ED6_DT07/CH00391P._CP',             # 06
        'ED6_DT07/CH00411P._CP',             # 07
        'ED6_DT06/CH20114P._CP',             # 08
        'ED6_DT06/CH20116P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
        'ED6_DT06/CH20155P._CP',             # 0B
        'ED6_DT06/CH20156P._CP',             # 0C
        'ED6_DT06/CH20123P._CP',             # 0D
        'ED6_DT06/CH20124P._CP',             # 0E
        'ED6_DT06/CH20125P._CP',             # 0F
        'ED6_DT07/CH01140P._CP',             # 10
        'ED6_DT07/CH01150P._CP',             # 11
        'ED6_DT07/CH01100P._CP',             # 12
        'ED6_DT07/CH01480P._CP',             # 13
        'ED6_DT07/CH01050P._CP',             # 14
        'ED6_DT07/CH01040P._CP',             # 15
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2660,
        Z                   = 0,
        Y                   = 27180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65550,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1310,
        Z                   = 0,
        Y                   = 26540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131085,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -240,
        Z                   = 0,
        Y                   = 27230,
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
        X                   = 480,
        Z                   = 0,
        Y                   = 26860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1600,
        Z                   = 0,
        Y                   = 26120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65549,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2350,
        Z                   = 0,
        Y                   = 27390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3680,
        Z                   = 0,
        Y                   = 26400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2140,
        Z                   = 0,
        Y                   = 25650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458765,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -520,
        Z                   = 0,
        Y                   = 25640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262158,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 25560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3100,
        Z                   = 0,
        Y                   = 25890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327694,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2260,
        Z                   = 0,
        Y                   = 24940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10,
        Z                   = 0,
        Y                   = 24790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131085,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1370,
        Z                   = 0,
        Y                   = 24770,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262157,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3170,
        Z                   = 0,
        Y                   = 24640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3830,
        Z                   = 0,
        Y                   = 26870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262159,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4590,
        Z                   = 0,
        Y                   = 25090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327695,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2070,
        Z                   = 0,
        Y                   = 24370,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65549,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1570,
        Z                   = 0,
        Y                   = 24240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131085,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3520,
        Z                   = 0,
        Y                   = 24060,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 393229,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 0,
        Y                   = 23340,
        Direction           = 343,
        Unknown2            = 0,
        Unknown3            = 262157,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2820,
        Z                   = 0,
        Y                   = 22600,
        Direction           = 13,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4730,
        Z                   = 0,
        Y                   = 22830,
        Direction           = 353,
        Unknown2            = 0,
        Unknown3            = 262157,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -670,
        Z                   = 0,
        Y                   = 21410,
        Direction           = 12,
        Unknown2            = 0,
        Unknown3            = 327693,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1120,
        Z                   = 0,
        Y                   = 23290,
        Direction           = 2,
        Unknown2            = 0,
        Unknown3            = 327694,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2340,
        Z                   = 0,
        Y                   = 22560,
        Direction           = 359,
        Unknown2            = 0,
        Unknown3            = 65550,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4380,
        Z                   = 0,
        Y                   = 25570,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 262158,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1240,
        Z                   = 0,
        Y                   = 21910,
        Direction           = 357,
        Unknown2            = 0,
        Unknown3            = 393230,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2670,
        Z                   = 0,
        Y                   = 21140,
        Direction           = 358,
        Unknown2            = 0,
        Unknown3            = 458766,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 21580,
        Direction           = 1,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6810,
        Z                   = 0,
        Y                   = 23940,
        Direction           = 46,
        Unknown2            = 0,
        Unknown3            = 393229,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5270,
        Z                   = 0,
        Y                   = 24130,
        Direction           = 36,
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
        X                   = -1790,
        Z                   = 0,
        Y                   = 22220,
        Direction           = 21,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 310,
        Z                   = 0,
        Y                   = 22190,
        Direction           = 13,
        Unknown2            = 0,
        Unknown3            = 196623,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3970,
        Z                   = 0,
        Y                   = 22250,
        Direction           = 349,
        Unknown2            = 0,
        Unknown3            = 131087,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1370,
        Z                   = 0,
        Y                   = 10340,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2340,
        Z                   = 0,
        Y                   = 9870,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3590,
        Z                   = 0,
        Y                   = 14380,
        Direction           = 54,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -2690,
        Z                   = 0,
        Y                   = 13710,
        Direction           = 353,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4310,
        Z                   = 0,
        Y                   = 13350,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4960,
        Z                   = 0,
        Y                   = 3770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -22550,
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
        X                   = -5630,
        Y                   = -1000,
        Z                   = 30090,
        Range               = 6050,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x69BE,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    ScpFunction(
        "Function_0_95A",          # 00, 0
        "Function_1_A78",          # 01, 1
        "Function_2_B83",          # 02, 2
        "Function_3_D00",          # 03, 3
        "Function_4_D72",          # 04, 4
        "Function_5_DE5",          # 05, 5
        "Function_6_175B",         # 06, 6
        "Function_7_1FC6",         # 07, 7
        "Function_8_212A",         # 08, 8
        "Function_9_21EF",         # 09, 9
        "Function_10_2279",        # 0A, 10
        "Function_11_22D4",        # 0B, 11
        "Function_12_2381",        # 0C, 12
        "Function_13_23D3",        # 0D, 13
        "Function_14_423E",        # 0E, 14
        "Function_15_50F3",        # 0F, 15
        "Function_16_55B8",        # 10, 16
        "Function_17_59D2",        # 11, 17
        "Function_18_6C9F",        # 12, 18
        "Function_19_6CB4",        # 13, 19
        "Function_20_6CDA",        # 14, 20
        "Function_21_6D00",        # 15, 21
    )


    def Function_0_95A(): pass

    label("Function_0_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_976")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_984")
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_992")
    OP_A3(0x3FC)
    Event(0, 17)

    label("loc_992")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_9A2"),
        (101, "loc_9A2"),
        (SWITCH_DEFAULT, "loc_9B8"),
    )


    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B5")
    OP_A2(0x60B)
    Event(0, 13)

    label("loc_9B5")

    Jump("loc_9B8")

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_9E0")
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    Jump("loc_A77")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A20")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_A77")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A2A")
    Jump("loc_A77")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A34")
    Jump("loc_A77")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_A3E")
    Jump("loc_A77")

    label("loc_A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_A48")
    Jump("loc_A77")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A52")
    Jump("loc_A77")

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A5C")
    Jump("loc_A77")

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A66")
    Jump("loc_A77")

    label("loc_A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A70")
    Jump("loc_A77")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A77")

    label("loc_A77")

    Return()

    # Function_0_95A end

    def Function_1_A78(): pass

    label("Function_1_A78")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x30060)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABD")
    OP_B1("t4200_y")
    Jump("loc_AC6")

    label("loc_ABD")

    OP_B1("t4200_n")

    label("loc_AC6")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_AE3")
    OP_6F(0x0, 450)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B7D")
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -770, 750, 23720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -520, 750, 42700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_B7D")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_A78 end

    def Function_2_B83(): pass

    label("Function_2_B83")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CEA")

    label("loc_BA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CEA")

    label("loc_BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CEA")

    label("loc_BDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CEA")

    label("loc_BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CEA")

    label("loc_C0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C25")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CEA")

    label("loc_C25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CEA")

    label("loc_C3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C57")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CEA")

    label("loc_C57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C70")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CEA")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C89")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CEA")

    label("loc_C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CEA")

    label("loc_CA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CEA")

    label("loc_CBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CEA")

    label("loc_CD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CFF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CEA")

    label("loc_CFF")

    Return()

    # Function_2_B83 end

    def Function_3_D00(): pass

    label("Function_3_D00")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "Grancel Castle is totally locked\x01",
            "down right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "We're under orders not to allow\x01",
            "ANYONE to pass.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_D00 end

    def Function_4_D72(): pass

    label("Function_4_D72")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "So you're the bracers who won\x01",
            "the tournament, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "The banquet is over. Go back to\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_D72 end

    def Function_5_DE5(): pass

    label("Function_5_DE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(    #4
        0xFE,
        (
            "I never believed Lt. Schwarz\x01",
            "could be a terrorist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "And I'm just as convinced now that\x01",
            "Colonel Richard can't possibly be\x01",
            "the one behind the coup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA8")

    label("loc_E96")

    OP_A2(0x0)

    ChrTalk(    #6
        0xFE,
        (
            "I never believed Lt. Schwarz\x01",
            "could be a terrorist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "And I'm just as convinced now that\x01",
            "Colonel Richard can't possibly be\x01",
            "the one behind the coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I mean, the facts are the facts...but\x01",
            "it just seems so surreal to me. How\x01",
            "could a man like that fall so far?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA8")

    Jump("loc_1757")

    label("loc_FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_FB5")
    Jump("loc_1757")

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_FF3")

    ChrTalk(    #9
        0xFE,
        (
            "So, did you enjoy your look\x01",
            "around the castle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_106E")

    ChrTalk(    #10
        0xFE,
        (
            "Welcome to Her Majesty's fabulous\x01",
            "Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "There should be a guide waiting\x01",
            "for you just inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_106E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_111F")

    ChrTalk(    #12
        0xFE,
        (
            "I wonder what Lt. Schwarz\x01",
            "is doing right now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I've always enjoyed seeing her each\x01",
            "day, even if we did speak little more\x01",
            "than pleasantries to one another.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1268")

    ChrTalk(    #14
        0xFE,
        (
            "Apparently, our security duties in\x01",
            "the city are to be much more rigorous\x01",
            "as of tonight's shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "We've been ordered to step up our\x01",
            "efforts as much as we can, since\x01",
            "the terrorists have yet to be caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Why the hell do we have to go around\x01",
            "wiping the Special Ops' asses?! Let\x01",
            "them clean up their OWN mess!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1306")

    ChrTalk(    #17
        0xFE,
        (
            "The Special Ops team is racking\x01",
            "up the wins at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I wish they'd concentrate on finding\x01",
            "the Royal Guardsmen, though, instead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13D2")

    ChrTalk(    #19
        0xFE,
        (
            "Colonel Richard's barely been\x01",
            "seen outside the castle since\x01",
            "Her Majesty fell ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "...I've heard, too, that the core\x01",
            "of the Intelligence Division has\x01",
            "been moved into the castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B1")

    label("loc_13D2")

    OP_A2(0x0)

    ChrTalk(    #21
        0xFE,
        (
            "Colonel Richard certainly is a\x01",
            "busy man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He's barely been seen outside\x01",
            "the castle since Her Majesty\x01",
            "fell ill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "...I've heard, too, that the core\x01",
            "of the Intelligence Division has\x01",
            "been moved into the castle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B1")

    Jump("loc_1757")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(    #24
        0xFE,
        (
            "I respect Colonel Richard, don't\x01",
            "get me wrong, but those Special\x01",
            "Ops guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "They're good at what they do, but they\x01",
            "make people uncomfortable in the process.\x01",
            "Even the army's creeped out by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_163F")

    ChrTalk(    #26
        0xFE,
        (
            "Colonel Richard is truly an\x01",
            "impressive individual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Thanks to his popularity a large number\x01",
            "of soldiers have requested transfers into\x01",
            "the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_163F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(    #28
        0xFE,
        (
            "I know it sucks that you can't\x01",
            "enter the castle right now...\x01",
            "but cheer up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "There's lots to see in this\x01",
            "city--the castle is just one\x01",
            "of many tourist attractions!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_16FB")


    ChrTalk(    #30
        0xFE,
        "Just a moment, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I'm sorry, but entry to the\x01",
            "castle is strictly prohibited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1757")

    TalkEnd(0xFE)
    Return()

    # Function_5_DE5 end

    def Function_6_175B(): pass

    label("Function_6_175B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1842")

    ChrTalk(    #32
        0xFE,
        (
            "I was shocked when I found out the Intelligence\x01",
            "Division was behind the coup, and they planned\x01",
            "it all out from right inside the castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Still, I'm glad we were at least able\x01",
            "to hold the Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_184C")
    Jump("loc_1FC2")

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_18D5")

    ChrTalk(    #34
        0xFE,
        "So, how was the banquet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I only got to see the food during\x01",
            "my rounds inside. I didn't get to\x01",
            "eat any of it, sadly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_18D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_18F8")

    ChrTalk(    #36
        0xFE,
        "Enjoy your evening!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_18F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1968")

    ChrTalk(    #37
        0xFE,
        (
            "The kitchen supplies were just\x01",
            "unloaded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Looks like it's going to be one\x01",
            "hell of a banquet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A08")

    ChrTalk(    #39
        0xFE,
        (
            "Apparently, our security duties in\x01",
            "the city are to be much more rigorous\x01",
            "from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "We'll be under Captain Amalthea's\x01",
            "orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC8")

    label("loc_1A08")

    OP_A2(0x1)

    ChrTalk(    #41
        0xFE,
        (
            "Apparently, our security duties in\x01",
            "the city are to be much more rigorous\x01",
            "from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "We'll be under Captain Amalthea's\x01",
            "orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Colonel Richard certainly is a\x01",
            "busy man!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC8")

    Jump("loc_1FC2")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1B4F")

    ChrTalk(    #44
        0xFE,
        (
            "We haven't been told much about\x01",
            "Her Majesty's illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "We're just as worried about it\x01",
            "as anyone else, honestly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1BC1")

    ChrTalk(    #46
        0xFE,
        (
            "Round one of the tournament looks\x01",
            "to have just finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I wonder how the Royal Garrison\x01",
            "did?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C79")

    ChrTalk(    #48
        0xFE,
        (
            "Duke Dunan's reputation in the\x01",
            "castle is just as bad as it is\x01",
            "on the outside, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Thank goodness Colonel Richard\x01",
            "is around to buffer his nonsense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5C")

    label("loc_1C79")

    OP_A2(0x1)

    ChrTalk(    #50
        0xFE,
        (
            "Duke Dunan's reputation in the\x01",
            "castle is just as bad as it is\x01",
            "on the outside, I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "All he seems to do is eat, sleep\x01",
            "and fiddle around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Thank goodness Colonel Richard\x01",
            "is around to buffer his nonsense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5C")

    Jump("loc_1FC2")

    label("loc_1D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E42")

    ChrTalk(    #53
        0xFE,
        (
            "Since the tournament is comprised of team\x01",
            "battles this year, there are fewer rounds\x01",
            "than in years past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "The matches are now set to start\x01",
            "in the afternoons, too--again,\x01",
            "very different from years past.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F3E")

    label("loc_1E42")

    OP_A2(0x1)

    ChrTalk(    #55
        0xFE,
        "Well, the preliminaries are over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Since the tournament is comprised of team\x01",
            "battles this year, there are fewer rounds\x01",
            "than in years past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "The matches are now set to start\x01",
            "in the afternoons, too--again,\x01",
            "very different from years past.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3E")

    Jump("loc_1FC2")

    label("loc_1F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1F8D")

    ChrTalk(    #58
        0xFE,
        (
            "You're in the Royal Capital!\x01",
            "Go and enjoy the sights!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1F8D")


    ChrTalk(    #59
        0xFE,
        (
            "Sorry, but the castle is off-\x01",
            "limits right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC2")

    TalkEnd(0xFE)
    Return()

    # Function_6_175B end

    def Function_7_1FC6(): pass

    label("Function_7_1FC6")

    TalkBegin(0xFE)

    ChrTalk(    #60
        0xFE,
        (
            "I was going to propose to my\x01",
            "girlfriend out in front of the\x01",
            "castle gates...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "...when suddenly, the gates opened\x01",
            "up and a bunch of Royal Guardsmen\x01",
            "and bracers flew past us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I thought they'd come to...stop\x01",
            "me from proposing, or something!\x01",
            "Yeah, it's silly, I know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I lost my nerve, though, and STILL\x01",
            "haven't said anything to her...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1FC6 end

    def Function_8_212A(): pass

    label("Function_8_212A")

    TalkBegin(0xFE)

    ChrTalk(    #64
        0xFE,
        (
            "I can't believe something like\x01",
            "that happened while I was standing\x01",
            "RIGHT THERE...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "But I mustn't let myself get so easily\x01",
            "bothered. The climax of our trip is\x01",
            "just around the corner!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_212A end

    def Function_9_21EF(): pass

    label("Function_9_21EF")

    TalkBegin(0xFE)

    ChrTalk(    #66
        0xFE,
        (
            "Everything got all crazy there for a\x01",
            "while, but in the end, I got to see\x01",
            "my grandkid AND Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "Thank the Goddess!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_21EF end

    def Function_10_2279(): pass

    label("Function_10_2279")

    TalkBegin(0xFE)

    ChrTalk(    #68
        0xFE,
        (
            "The princess was so very, very\x01",
            "pretty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "When I saw her, I was all, awww!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_2279 end

    def Function_11_22D4(): pass

    label("Function_11_22D4")

    TalkBegin(0xFE)

    ChrTalk(    #70
        0xFE,
        (
            "So, Her Majesty's illness was all...\x01",
            "some kind of lie?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Dubious though it may be, I'm just\x01",
            "thankful to hear she's all right.\x01",
            "I was quite worried about her!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_22D4 end

    def Function_12_2381(): pass

    label("Function_12_2381")

    TalkBegin(0xFE)

    ChrTalk(    #72
        0xFE,
        "Maybe I'll head into town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "It ought to be pretty wild right\x01",
            "now!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2381 end

    def Function_13_23D3(): pass

    label("Function_13_23D3")

    EventBegin(0x0)
    StopSound(0x186A0, 0x2BF20, 0x3E8)
    OP_6C(30000, 0)

    def lambda_23F1():
        OP_6D(-930, 750, 44710, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23F1)

    def lambda_2409():
        OP_67(0, 4250, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2409)

    def lambda_2421():
        OP_6B(11000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2421)

    def lambda_2431():
        OP_6C(0, 15000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2431)
    Sleep(12000)
    SetChrPos(0x101, -910, 0, 8880, 0)
    SetChrPos(0x102, 1000, 0, 10110, 0)

    def lambda_2468():
        OP_6D(-290, 0, 32350, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2468)

    def lambda_2480():
        OP_6B(7180, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2480)

    def lambda_2490():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2490)

    def lambda_24A0():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24A0)

    def lambda_24BB():
        OP_8E(0xFE, 0x258, 0x0, 0x4808, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24BB)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #74
        0x101,
        (
            "#001FWow...so that's Grancel Castle.\x02\x03",

            "It's gorgeous. I guess it really\x01",
            "is fit for a queen.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #75
        0x102,
        (
            "#010FIt's not just pretty... It's\x01",
            "also really solidly built.\x02\x03",

            "For instance,\x01",
            "look at the main gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#505FYeah, I don't think getting through\x01",
            "there would be an easy task.\x02\x03",

            "Which means, I guess we'll have\x01",
            "to talk to those soldiers there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#010FWell, steel your nerves,\x01",
            "and let's give it a shot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #78
        0x102,
        (
            "#015FOkay, we're just country folk,\x01",
            "here on vacation and checking\x01",
            "out the castle.\x02\x03",

            "And we just thought we'd try\x01",
            "and catch a glimpse of Her\x01",
            "Majesty, since we're here.\x02\x03",

            "#010FDoes that sound okay to you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #79
        0x101,
        (
            "#007FYou know, you're disturbingly\x01",
            "good at coming up with that\x01",
            "kind of stuff.\x02\x03",

            "Not that it doesn't come in\x01",
            "handy, but still...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #80
        0x102,
        (
            "#019FI'll take that as a compliment.\x01",
            "Okay, now smile and act natural.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2826():
        OP_6D(0, 250, 42590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2826)

    def lambda_283E():
        OP_6B(5100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_283E)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x9, 400)
    WaitChrThread(0x101, 0x2)
    SetChrPos(0x101, -850, 0, 25330, 0)
    SetChrPos(0x102, 1090, 0, 22700, 0)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        "Umm... Hello there...\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_28C2():

        label("loc_28C2")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_28C2")

    QueueWorkItem2(0x8, 1, lambda_28C2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_28EA():

        label("loc_28EA")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_28EA")

    QueueWorkItem2(0x9, 1, lambda_28EA)

    def lambda_28FB():
        OP_8E(0xFE, 0x258, 0x0, 0x9290, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28FB)

    def lambda_2916():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0x9290, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2916)
    Sleep(1000)

    ChrTalk(    #82
        0x8,
        "#1PGood afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#2PWelcome to Grancel Castle.\x01",
            "Please state your business.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #84
        0x102,
        (
            "#010F#2POh, we're just getting here\x01",
            "from Rolent. We're taking in\x01",
            "the sights, you might say.\x02\x03",

            "We were wondering if there was\x01",
            "any chance we might get a\x01",
            "tour of the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        "#1PAhh, I get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#1PI'm sorry, but access to\x01",
            "the castle is restricted to\x01",
            "authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "#2PSecurity's been tighter, what\x01",
            "with the terrorism scares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "#2POnce the terrorists are caught,\x01",
            "tours will probably open up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#007FReally...? Dang.\x02\x03",

            "There goes my dream of seeing\x01",
            "the queen in real life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        "#1PWell, not necessarily...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#1PShe always addresses the people from\x01",
            "her terrace during the Birthday \x01",
            "Celebration. You could see her then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "#2PFair warning, though... Her\x01",
            "Majesty hasn't been in the\x01",
            "best of health these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "#2PI don't know if she'll be able to\x01",
            "manage her traditional greeting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#580FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        "#012F#2PHer Majesty is ill?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "#2PYes...\x01",
            "I hear it's because of stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "#2POr maybe from the shock of\x01",
            "learning the Royal Guardsmen were\x01",
            "involved in a terrorist plot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#2PShe hasn't been seen much lately.\x01",
            "I believe she's resting in her\x01",
            "private quarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#002FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#1PDamn the Guardsmen... How could\x01",
            "they just turn traitor like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#1PNever did like those damned\x01",
            "elitist jerks anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #102
        0x9,
        (
            "#2PB-But Lieutenant Schwarz was always\x01",
            "so kind and considerate to everyone.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 800)

    ChrTalk(    #103
        0x9,
        (
            "#2PShe even taught us court etiquette\x01",
            "and how to wield a sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "#2PIt's just hard for me to picture\x01",
            "someone like that as a terrorist.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #105
        0x8,
        "#1PO-Of course it's hard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#1PShe probably left because she\x01",
            "felt responsible for her men's\x01",
            "actions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        "#1PPoor Lieutenant Schwarz...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #108
        0x101,
        (
            "#509F(You don't suppose...)\x02\x03",

            "(...these two had a little crush\x01",
            "on the lieutenant, do you?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        "#019F#2P(Yeah, it seems so.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #110
        0x8,
        "#1PAhem!...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#1PAnyway, yes.\x01",
            "The castle is off limits.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #112
        0x9,
        "#2PSorry, but you can't go inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#007F*sigh*\x01",
            "Well, I guess that's that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#013F#2PI'm just a tad bit worried...\x02\x03",

            "If Her Majesty has taken sick,\x01",
            "who's seeing to her daily affairs\x01",
            "with running the country?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "#2PYes, it's certainly a natural\x01",
            "enough concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "#2PFor now, there's someone acting\x01",
            "as her proxy, on paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#505FHow's that work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        "#1PHa ha. Literally. On paper.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "#1PI can't picture someone like\x01",
            "him ever actually making any\x01",
            "real governmental decisions.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #120
        0x9,
        "#2PHey, watch what you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "#2PThough I'll admit, I would have\x01",
            "thought that the duty would fall\x01",
            "to the princess...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #122
        0x8,
        (
            "#1PAnd you tell me to watch\x01",
            "what *I* say...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD2, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -270, 750, 48420, 180)
    SetChrPos(0xB, 550, 750, 49230, 180)

    ChrTalk(    #123
        0x101,
        "#004FWh-What's that...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 400)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(    #124
        0x8,
        (
            "#1PWhoops...\x01",
            "Speak of the devil...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34BB():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34BB)

    def lambda_34D3():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34D3)

    def lambda_34E3():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34E3)
    Sleep(100)
    TurnDirection(0x8, 0x9, 400)

    def lambda_34FF():
        OP_8F(0xFE, 0xFFFFF6F0, 0x0, 0xA406, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_34FF)
    TurnDirection(0x9, 0x8, 400)

    def lambda_3521():
        OP_8F(0xFE, 0x910, 0x0, 0xA4A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3521)
    OP_6D(-10, 750, 48050, 3000)

    def lambda_354D():

        label("loc_354D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_354D")

    QueueWorkItem2(0x101, 1, lambda_354D)

    def lambda_355E():

        label("loc_355E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_355E")

    QueueWorkItem2(0x102, 1, lambda_355E)
    SetChrPos(0x101, -2130, 0, 39490, 0)
    SetChrPos(0x102, -2130, 0, 37840, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)

    def lambda_35A2():
        OP_8E(0xFE, 0xFFFFFEFC, 0x2EE, 0xAE2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35A2)
    Sleep(500)

    def lambda_35C2():
        OP_8E(0xFE, 0x276, 0x2EE, 0xB090, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_35C2)
    OP_6D(0, 750, 44920, 2000)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xB, 0x1)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #125
        0xA,
        (
            "#222FBah! I've never been\x01",
            "so insulted!\x02\x03",

            "The tournament should have\x01",
            "already begun, and I'M NOT\x01",
            "THERE.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #126
        0xA,
        (
            "#224FPhillip! Why didn't you wake me\x01",
            "sooner! This is all your fault!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #127
        0xB,
        (
            "#722FI am terribly sorry, Your Grace.\x02\x03",

            "But I was merely trying to look after your\x01",
            "mental well-being.\x02\x03",

            "For the last few days you have been in the\x01",
            "banquet hall, drinking and singing...\x02\x03",

            "Consuming exclusively beer and donuts\x01",
            "while reading your morning comics...\x02\x03",

            "I feel that it should come as no surprise that\x01",
            "you overslept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xA,
        (
            "#225FSilence, Phillip! I'm not in the mood\x01",
            "to listen to your chastisements!\x02\x03",

            "As the future king, I can do\x01",
            "what I want, whenever I want!\x02\x03",

            "#224FBah! Time is short! Come on, we\x01",
            "must hurry to the Grand Arena!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    def lambda_38E1():
        OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x6D74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_38E1)
    Sleep(500)

    def lambda_3901():
        OP_8E(0xFE, 0x42E, 0x0, 0x6BF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3901)
    OP_6F(0x0, 450)
    OP_70(0x0, 0x0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(-30, 0, 40870, 5000)

    def lambda_395F():
        OP_8F(0xFE, 0xFFFFFCEA, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_395F)

    def lambda_397A():
        OP_8F(0xFE, 0x3B6, 0x0, 0xA3FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_397A)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_63(0x101)
    OP_63(0x102)
    Sleep(400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #129
        0x101,
        "#509FUhhh...\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFFFAD8, 0x0, 0x96E6, 0x7D0, 0x0)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #130
        0x102,
        "#014F#6PBy any chance, was that...\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #131
        0x8,
        "#4PWe know. Don't even say it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        (
            "#4PThat was His Grace, the duke...\x01",
            "acting proxy for Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#007FWow. Suddenly I fear for\x01",
            "the entire country...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "#4PW-Well, don't worry too much. He\x01",
            "has a very reliable assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x9,
        (
            "#4PAnd it's thanks to him that we\x01",
            "haven't had any major incidents\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_3B74():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B74)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #136
        0x102,
        "#012F#6PDo tell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "#4PHa ha... Colonel Richard, of the\x01",
            "Royal Army Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#4PSince the duke is more of the\x01",
            "playboy sort, the colonel handles\x01",
            "all the government affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#009F(I knew it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#012F#6P(They're pushing harder into\x01",
            "the core of the kingdom than\x01",
            "I'd expected... )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "#4PSo, try not to let this whole\x01",
            "thing get you down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#4PGrancel's got plenty of other\x01",
            "famous places you can check out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #143
        0x9,
        (
            "#4PYeah. You're in the royal city,\x01",
            "after all. Just go at your own pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#008FY-You're right.\x01",
            "We will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#019F#6PThank you both for your kindness.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, -790, 0, 41980, 180)
    SetChrPos(0x9, 950, 0, 41980, 180)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_6D(-170, 0, 24540, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    StopSound(0x0, 0x0, 0x1)
    SetChrPos(0x102, 660, 0, 34050, 18)
    SetChrPos(0x101, -860, 0, 33870, 45)

    def lambda_3EA6():
        OP_8E(0xFE, 0xFFFFFCA4, 0x0, 0x623E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EA6)
    Sleep(300)

    def lambda_3EC6():
        OP_8E(0xFE, 0x294, 0x0, 0x6108, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EC6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    def lambda_3EF0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EF0)
    WaitChrThread(0x102, 0x1)

    def lambda_3F03():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F03)

    ChrTalk(    #146
        0x101,
        (
            "#006F#6PWell, that was...informative.\x02\x03",

            "#007FI can't believe that the duke\x01",
            "is supposed to be acting on\x01",
            "behalf of the queen, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        (
            "#013F#4PThe real power is probably in the\x01",
            "hands of Colonel Richard.\x02\x03",

            "What's more, no one around him\x01",
            "has any clue that he's the one\x01",
            "pulling all the strings.\x02\x03",

            "#012FBeing able to control the\x01",
            "flow of information must be\x01",
            "an extremely useful tool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#007F#6PYou're not supposed to\x01",
            "envy the enemy.\x02\x03",

            "#006FAnd anyway, it looks like the\x01",
            "duke is going to that fighting\x01",
            "tournament.\x02\x03",

            "Can we go, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        (
            "#015F#4PYeah...\x02\x03",

            "#010FIf nothing else, we need to keep\x01",
            "an eye on what he's up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#001F#6PThat settles it, then!\x02\x03",

            "#505F#3PUmm... Which way was it\x01",
            "to the Grand Arena...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        (
            "#010F#4PI believe it's in the East Block.\x02\x03",

            "So, back to the main road,\x01",
            "then east.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x45, 0x1, 0x200)
    OP_28(0x45, 0x1, 0x400)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_13_23D3 end

    def Function_14_423E(): pass

    label("Function_14_423E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_424B")
    Return()

    label("loc_424B")

    EventBegin(0x0)

    def lambda_4253():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4253)

    def lambda_4261():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4261)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #152
        0x108,
        (
            "#073FOh, are we going to the\x01",
            "castle already?\x02\x03",

            "Just to remind you, since we're going\x01",
            "to be staying there after the party,\x01",
            "we won't be able to leave until morning.\x02",
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
            "[Enter Grancel Castle]\x01",      # 0
            "[Not just yet]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_438E"),
        (1, "loc_445C"),
        (SWITCH_DEFAULT, "loc_4490"),
    )


    label("loc_438E")


    ChrTalk(    #153
        0x108,
        (
            "#070FWell, let's show the gatekeeper\x01",
            "our invitations, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#008FUgh... I don't know why\x01",
            "I'm so nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        (
            "#019FProbably because we don't get\x01",
            "invitations to big events like\x01",
            "this very often.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4490")

    label("loc_445C")


    ChrTalk(    #156
        0x108,
        "#070FBack already?\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_4490")


    def lambda_4496():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4496)

    def lambda_44A4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44A4)

    def lambda_44B2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_44B2)

    def lambda_44C0():
        OP_67(0, 5220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44C0)

    def lambda_44D8():
        OP_6E(287, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_44D8)
    OP_6D(110, 0, 41220, 3000)
    SetChrPos(0x101, -620, 0, 32729, 0)
    SetChrPos(0x102, 920, 0, 32590, 0)
    SetChrPos(0x108, 90, 0, 32000, 0)

    def lambda_452C():
        OP_8E(0xFE, 0xFFFFFCFE, 0x0, 0x9B82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_452C)
    Sleep(300)

    def lambda_454C():
        OP_8E(0xFE, 0x4E2, 0x0, 0x9BD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_454C)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #157
        0x8,
        (
            "Hey, this is the castle of Her\x01",
            "Majesty the Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x9,
        (
            "#3PUnless you have official business\x01",
            "here, you need to lea--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        "#3P...Hey.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #160
        0x101,
        "#4P#006FHi there!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #161
        0x102,
        (
            "#010F#4PWe're sorry about the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        "Oh, it's you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        "#3PYou're still staying in town?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#4P#001FYeah, we still have some business\x01",
            "to take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        (
            "#010F#4PWe have a formal invitation, so\x01",
            "by your leave, may we pass?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #166
        0x8,
        "A formal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        "#3P...invitation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x108,
        "#1PReceived directly from His Grace.\x02",
    )

    CloseMessageWindow()

    def lambda_47C5():
        OP_8E(0xFE, 0x12C, 0x0, 0x9862, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_47C5)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #169
        0x8,
        "Wha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x9,
        "#3PIt's a giant!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #171
        0x108,
        (
            "#070F#4PSee? Right here.\x01",
            "Written invitation.\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x108, 0x168, 0x0, 0xA1D6, 0x7D0, 0x0)
    OP_3F(0x371, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #172
        "\x07\x00Handed over \x07\x02Invitation\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x108, 0x12C, 0x0, 0x9E98, 0x7D0, 0x0)

    ChrTalk(    #173
        0x8,
        "Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "#3P'To Zin and his team: In appreciation for\x01",
            "your performance in the competition, you\x01",
            "are cordially invited to a dinner party.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x9,
        (
            "#3POh, okay... You guys were in the\x01",
            "Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "Right, and I heard the winning team\x01",
            "was led by a huge Eastern guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        "So is that you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#4P#502FHee hee... You got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        (
            "#010F#4PWe would greatly appreciate\x01",
            "your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        "#3PMakes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x9,
        (
            "#3PThe head maid told us\x01",
            "you'd be coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#3PYou're missing someone...\x01",
            "What happened to him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x108,
        (
            "#070F#4PIt's kind of impolite, I know,\x01",
            "but it doesn't look like he's\x01",
            "going to be able to make it.\x02\x03",

            "We're the only ones coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "Ahh...\x01",
            "Well, that's a pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        (
            "No matter.\x01",
            "Please, go on in.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BEA():
        OP_6D(70, 750, 44190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BEA)

    def lambda_4C02():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C02)

    def lambda_4C12():
        OP_6E(438, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C12)
    OP_8E(0x9, 0x6E, 0x2EE, 0xADD4, 0x7D0, 0x0)
    OP_8C(0x9, 0, 400)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #186
        0x9,
        (
            "Now entering: Zin and company, victors\x01",
            "of the Martial Arts Competition!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        "Open the gate!\x02",
    )

    CloseMessageWindow()

    def lambda_4CA3():
        OP_6D(70, 3450, 44190, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CA3)

    def lambda_4CBB():
        OP_67(0, 7620, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4CBB)

    def lambda_4CD3():
        OP_8E(0x8, 0xFFFFF704, 0x2EE, 0xAE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CD3)
    OP_8E(0x9, 0x992, 0x2EE, 0xAE38, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #188
        0x101,
        (
            "#004FWow...\x02\x03",

            "It's like the Haken Gate, but there's\x01",
            "something more impressive about\x01",
            "it being part of a castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#010FI'd bet it's more solid, too,\x01",
            "since it's the royal castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x8,
        "#1PThat's part of why it's impregnable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        (
            "#1PEver since the nation was established,\x01",
            "no enemy has ever broken through the\x01",
            "Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#1PThe capital's been ravaged by war\x01",
            "numerous times as a result of mutinies\x01",
            "and insurrections amongst the nobles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x9,
        (
            "#2PBut even then, the castle held the\x01",
            "rebel army at bay and protected the\x01",
            "royal family and the refugees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x9,
        "#2POr so the stories say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#501FWow...\x01",
            "That's pretty neat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x108,
        (
            "#070FVery much the sort of tale one\x01",
            "would expect from a nation\x01",
            "with such history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#1PNow, welcome to Her Majesty's\x01",
            "Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#1PGo right on in. You'll be met by a\x01",
            "welcoming party inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x9,
        "#2PEnjoy your evening.\x02",
    )

    CloseMessageWindow()

    def lambda_5095():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_5095)
    Sleep(100)

    def lambda_50B0():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50B0)
    Sleep(100)

    def lambda_50CB():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_50CB)
    OP_A2(0x638)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T4250   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_423E end

    def Function_15_50F3(): pass

    label("Function_15_50F3")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_6D(70, -1900, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0xC, -790, 0, 41980, 180)
    SetChrPos(0xD, 950, 0, 41980, 180)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(500)

    def lambda_518C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_518C)
    Sleep(200)

    def lambda_519F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_519F)
    OP_6D(70, 2550, 45150, 2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)

    ChrTalk(    #200
        0xC,
        "Wh-What the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xD,
        (
            "Uhh... Aren't we on total lockdown\x01",
            "right now? Why's the gate opening?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_525F():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_525F)
    Sleep(100)

    def lambda_5272():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5272)
    OP_6D(70, -1900, 45200, 1000)

    ChrTalk(    #202
        0xC,
        "#1PWha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xD,
        "#2PImpossible!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-1030, 0, 9000, 0)
    OP_67(0, 9340, -13360, 0)
    OP_6B(1000, 0)
    OP_6C(135000, 0)
    OP_6E(747, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x12, 1730, 0, -280, 0)
    SetChrPos(0x13, 1730, 0, -2790, 180)
    SetChrPos(0x14, 1730, 0, -5480, 180)
    SetChrPos(0x15, 1730, 0, -8070, 180)
    SetChrPos(0x16, 1730, 0, -10050, 180)
    SetChrPos(0xE, 3230, 0, -4350, 0)
    SetChrPos(0x10, 3230, 0, -1480, 0)
    SetChrPos(0x17, -1770, 0, -380, 260)
    SetChrPos(0x18, -1770, 0, -2970, 180)
    SetChrPos(0x19, -1770, 0, -5140, 180)
    SetChrPos(0x1A, -1770, 0, -7650, 180)
    SetChrPos(0xF, -3240, 0, -1470, 360)
    SetChrPos(0x11, -3240, 0, -4130, 360)

    def lambda_541A():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_541A)

    def lambda_5435():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5435)

    def lambda_5450():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5450)

    def lambda_546B():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_546B)

    def lambda_5486():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5486)

    def lambda_54A1():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54A1)

    def lambda_54BC():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_54BC)

    def lambda_54D7():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_54D7)

    def lambda_54F2():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_54F2)

    def lambda_550D():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_550D)

    def lambda_5528():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5528)

    def lambda_5543():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5543)

    def lambda_555E():
        OP_8E(0xFE, 0xFFFFFF06, 0x0, 0x180D8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_555E)

    def lambda_5579():
        OP_6D(-390, 0, 29050, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5579)

    def lambda_5591():
        OP_6C(44000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5591)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_50F3 end

    def Function_16_55B8(): pass

    label("Function_16_55B8")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(50, 4200, 30840, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(61000, 0)
    OP_6E(391, 0)

    def lambda_56D3():
        OP_6D(50, 100, 30840, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_56D3)

    def lambda_56EB():
        OP_6C(50000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_56EB)
    Sleep(5000)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x24, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x26, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x27, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x31, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x32, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x33, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x35, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x38, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x39, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_597B():
        OP_6D(20, 13000, 44770, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_597B)

    def lambda_5993():
        OP_67(0, 3640, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5993)

    def lambda_59AB():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_59AB)
    Sleep(2500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_55B8 end

    def Function_17_59D2(): pass

    label("Function_17_59D2")

    EventBegin(0x0)
    OP_6F(0x0, 450)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x1C, 3420, 0, -7500, 0)
    SetChrPos(0x1B, 2600, 0, -6950, 0)
    SetChrPos(0x101, 3420, 0, -8400, 0)
    SetChrPos(0x102, 4150, 0, -7140, 0)
    SetChrChipByIndex(0x102, 11)
    SetChrChipByIndex(0x1B, 12)
    ClearChrFlags(0x1B, 0x80)
    SetMapFlags(0x1)
    OP_69(0x1C, 0x0)
    OP_6A(0x1C)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_5A82():
        OP_6C(135000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A82)

    def lambda_5A92():
        OP_91(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5A92)
    OP_43(0x101, 0x1, 0x0, 0x12)
    OP_43(0x102, 0x1, 0x0, 0x13)
    OP_43(0x1B, 0x1, 0x0, 0x14)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #204
        0x101,
        (
            "#007FGeez, Dad...\x02\x03",

            "Can't you at least stay with us until\x01",
            "the end of the Birthday Celebration...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x1B,
        (
            "#080FI'm sorry...but there's a war\x01",
            "council starting immediately.\x02\x03",

            "Colonel Richard may be in custody,\x01",
            "but there are plenty of his Special\x01",
            "Ops cohorts still at large.\x02\x03",

            "Captain Amalthea is also hiding\x01",
            "somewhere in the underground ruins.\x02\x03",

            "And if that weren't enough, it\x01",
            "looks like those sky bandits\x01",
            "ran off in all the confusion.\x02\x03",

            "We have to stay on guard so\x01",
            "they don't cause any trouble\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#509FArgh... Those guys are just\x01",
            "a constant pain in the ass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x102,
        (
            "#019FEither way, it leaves a bad\x01",
            "taste in my mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x1B,
        (
            "#082FThe increased security is\x01",
            "just for peace of mind.\x02\x03",

            "The real issue is that we really\x01",
            "don't know the significance of\x01",
            "what happened underground.\x02\x03",

            "We can only guess at what effect\x01",
            "breaking that seal will have.\x02\x03",

            "And what the purpose of\x01",
            "that 'Aureole' is...\x02\x03",

            "That's a puzzle that absolutely\x01",
            "must be solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#505FYeah, I guess you're right.\x02\x03",

            "And it doesn't sound like Colonel\x01",
            "Richard's memory can be trusted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x1B,
        (
            "#085FYes... Just like Kurt, he seems\x01",
            "to have some missing memories.\x02\x03",

            "#082FEven so, the search team was\x01",
            "able to confirm one thing...\x02\x03",

            "We now know where the Black\x01",
            "Orbment came from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#580FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x102,
        "#012FYou know who made it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x1B,
        (
            "#082FNot quite. But we do know who's\x01",
            "responsible for introducing it\x01",
            "to the Intelligence Division.\x02\x03",

            "Commander of the Special Ops:\x01",
            "2nd Lieutenant Lorence Belgar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        "#005F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        "#014FHim...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1B,
        (
            "#085FHe gave it to Richard shortly\x01",
            "after he was recruited for the\x01",
            "Intelligence Division.\x02\x03",

            "And 'coincidentally,' that would be\x01",
            "just about the same time Richard\x01",
            "planned his coup...\x02\x03",

            "#082FWe need to find out everything\x01",
            "about Lorence that we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#003FHuh...\x01",
            "He always did seem strange...\x02\x03",

            "#006FI guess we were lucky that we\x01",
            "actually got a good look at\x01",
            "his face, huh?\x02\x03",

            "If you want, I can try drawing\x01",
            "you a picture of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x1B,
        (
            "#080FThat would be appreciated.\x02\x03",

            "#081FI have to admit, though, that I\x01",
            "don't have the utmost faith in\x01",
            "your artistic skills...\x02\x03",

            "Maybe I should ask Scherazard\x01",
            "or Her Majesty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#009F...That's not nice.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    Fade(1000)
    SetChrChipByIndex(0x1B, 10)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x1B, 0)
    TurnDirection(0x102, 0x101, 0)
    TurnDirection(0x1B, 0x101, 0)
    OP_6C(0, 0)
    OP_6B(2600, 0)
    ClearMapFlags(0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #220
        0x102,
        (
            "#014F#4PEstelle...\x02\x03",

            "You actually saw Lorence's face?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #221
        0x101,
        (
            "#501FWhat, I didn't tell you?\x02\x03",

            "He took his helmet off when we\x01",
            "fought him on the terrace in\x01",
            "the Royal Keep.\x02\x03",

            "He looked around twenty, maybe\x01",
            "older, with ash blond hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        "#514F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#007FHe had some seriously creepy\x01",
            "eyes, too, let me tell you...\x02\x03",

            "#003FBrrrr... They were so cold, but\x01",
            "it was like they were on fire\x01",
            "at the same time.\x02\x03",

            "He told the queen, 'You are hardly\x01",
            "qualified to feel pity for me.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#013F#4PHardly qualified...?\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        "#505FJoshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x1B,
        (
            "#080FYour eyes are looking a little\x01",
            "creepy now too, Joshua! Something\x01",
            "on your mind?\x02\x03",

            "How about you let us handle the\x01",
            "cleanup here, and go have fun\x01",
            "at the festival?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1B, 400)

    ChrTalk(    #227
        0x102,
        (
            "#014F#4PI...\x02\x03",

            "#010FOkay. You're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#001FAwesome. Let's go live it up.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)
    Sleep(400)

    ChrTalk(    #229
        0x101,
        (
            "#006FOh, right. Are we going to be\x01",
            "sleeping at the castle tonight?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x101, 400)

    ChrTalk(    #230
        0x1B,
        (
            "#080FYes. Her Majesty was kind enough\x01",
            "to let me use two of the guest\x01",
            "rooms in the eastern wing.\x02\x03",

            "Joshua and I will be on the\x01",
            "right, you and Schera on\x01",
            "the left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x101,
        "#004FMe and Schera? Together?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x1B,
        (
            "#084FYou don't like that setup?\x02\x03",

            "Okay. How about me and you in\x01",
            "one room, Joshua and Schera in\x01",
            "the other?\x02\x03",

            "#081FJust imagine...all that time for you\x01",
            "to fawn over me, and wait on me, and\x01",
            "tell me how much you missed me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        "#509F...I'll bunk with Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1B,
        (
            "#081FHa ha ha!\x01",
            "I suspected as much.\x02\x03",

            "#080FAll right, then I'll see\x01",
            "you kids tonight.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 0, 400)

    def lambda_6914():

        label("loc_6914")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_6914")

    QueueWorkItem2(0x101, 1, lambda_6914)

    def lambda_6925():

        label("loc_6925")

        TurnDirection(0xFE, 0x1B, 0)
        OP_48()
        Jump("loc_6925")

    QueueWorkItem2(0x102, 1, lambda_6925)
    OP_43(0x1B, 0x1, 0x0, 0x15)
    Sleep(5000)
    SetChrFlags(0x1B, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #235
        0x102,
        (
            "#010F#4PYou know, it wouldn't be a big deal for you\x01",
            "to share a room with him. I mean, it has\x01",
            "been a long time since you last saw him.\x02\x03",

            "Didn't you have a lot of stuff\x01",
            "about your mom that you wanted\x01",
            "to talk to him about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#007FYeah, but...\x02\x03",

            "I don't much like the idea of\x01",
            "you and Schera in the same\x01",
            "room, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x102,
        "#014F#4PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #238
        0x101,
        (
            "#503FNothing! Nothing!\x02\x03",

            "#008FLet's go and look around.\x02\x03",

            "The town's decked out with some\x01",
            "pretty cool festival-exclusive\x01",
            "shops, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        (
            "#010F#4PWell, we certainly can't let THOSE\x01",
            "pass us by now, can we?\x02\x03",

            "And if we get tired, there's a\x01",
            "rest area in the East Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#501FBehind the stores, right?\x02\x03",

            "#001FWe should make that our\x01",
            "last stop, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x0, 0x0)
    OP_6A(0x0)
    OP_92(0x1, 0x0, 0x0, 0x2710, 0x0)
    OP_8C(0x101, 180, 0)
    OP_8C(0x102, 180, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    Sleep(500)
    OP_28(0x4F, 0x1, 0x20)
    OP_28(0x4F, 0x1, 0x40)
    OP_28(0x4F, 0x1, 0x80)
    OP_28(0x4F, 0x1, 0x100)
    OP_28(0x4F, 0x1, 0x200)
    OP_28(0x4F, 0x1, 0x400)
    OP_28(0x4F, 0x1, 0x800)
    OP_28(0x50, 0x4, 0x40)
    OP_28(0x51, 0x4, 0x40)
    ClearMapFlags(0x800)
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_17_59D2 end

    def Function_18_6C9F(): pass

    label("Function_18_6C9F")

    OP_90(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
    Return()

    # Function_18_6C9F end

    def Function_19_6CB4(): pass

    label("Function_19_6CB4")

    OP_90(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    TurnDirection(0x102, 0x1B, 400)
    Return()

    # Function_19_6CB4 end

    def Function_20_6CDA(): pass

    label("Function_20_6CDA")

    OP_90(0xFE, 0xFFFFF272, 0x0, 0x9470, 0x320, 0x0)
    SetChrChipByIndex(0x1B, 10)
    SetChrSubChip(0x1B, 0)
    TurnDirection(0x1B, 0x101, 400)
    Return()

    # Function_20_6CDA end

    def Function_21_6D00(): pass

    label("Function_21_6D00")

    OP_8E(0x1B, 0x46, 0x2EE, 0xAAD2, 0x7D0, 0x0)
    OP_8E(0x1B, 0x190, 0x2EE, 0xBBBC, 0x7D0, 0x0)
    Return()

    # Function_21_6D00 end

    SaveToFile()

Try(main)
