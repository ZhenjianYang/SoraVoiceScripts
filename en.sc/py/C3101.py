from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C3101   ._SN',
            'ED6_DT21/C3101_1 ._SN',
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
        'Cassius',                              # 9
        'Captain Schwarz',                      # 10
        'General Morgan',                       # 11
        'Lt. Col. Cid',                         # 12
        'Maintenance Chief Gustav',             # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Soldier',                              # 22
        'Soldier',                              # 23
        'Soldier',                              # 24
        'Soldier',                              # 25
        'Soldier',                              # 26
        'Soldier',                              # 27
        'Soldier',                              # 28
        'Soldier',                              # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Royal Guardsman',                      # 32
        'Royal Guardsman',                      # 33
        'Royal Guardsman',                      # 34
        'Royal Guardsman',                      # 35
        'Officer',                              # 36
        'Target Camera',                        # 37
        'Warrant Officer Belc',                 # 38
        'Soldier',                              # 39
        'Soldier',                              # 40
        'Soldier',                              # 41
        'Soldier',                              # 42
        'Soldier',                              # 43
        'Soldier',                              # 44
        'Soldier',                              # 45
        'Soldier',                              # 46
        'Soldier',                              # 47
        'Soldier',                              # 48
        'Soldier',                              # 49
        'Soldier',                              # 50
        'Soldier',                              # 51
        'Soldier',                              # 52
        'Soldier',                              # 53
        'Soldier',                              # 54
        'Soldier',                              # 55
        'Soldier',                              # 56
        'Soldier',                              # 57
        'Soldier',                              # 58
        'Soldier',                              # 59
        'Soldier',                              # 60
        'Soldier',                              # 61
        'Soldier',                              # 62
        'Soldier',                              # 63
        'Soldier',                              # 64
        'Soldier',                              # 65
        'Soldier',                              # 66
        'Soldier',                              # 67
        'Soldier',                              # 68
        'Soldier',                              # 69
        'Soldier',                              # 70
        'Officer',                              # 71
        'Officer',                              # 72
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH03580 ._CH',             # 01
        'ED6_DT07/CH02080 ._CH',             # 02
        'ED6_DT27/CH03590 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01300 ._CH',             # 05
        'ED6_DT07/CH01320 ._CH',             # 06
        'ED6_DT27/CH04580 ._CH',             # 07
        'ED6_DT07/CH01600 ._CH',             # 08
        'ED6_DT07/CH00322 ._CH',             # 09
        'ED6_DT07/CH00321 ._CH',             # 0A
        'ED6_DT27/CH04000 ._CH',             # 0B
        'ED6_DT27/CH04004 ._CH',             # 0C
        'ED6_DT07/CH00120 ._CH',             # 0D
        'ED6_DT07/CH00124 ._CH',             # 0E
        'ED6_DT07/CH00130 ._CH',             # 0F
        'ED6_DT07/CH00134 ._CH',             # 10
        'ED6_DT07/CH00140 ._CH',             # 11
        'ED6_DT07/CH00144 ._CH',             # 12
        'ED6_DT07/CH00150 ._CH',             # 13
        'ED6_DT07/CH00154 ._CH',             # 14
        'ED6_DT07/CH00320 ._CH',             # 15
        'ED6_DT07/CH00324 ._CH',             # 16
        'ED6_DT07/CH00330 ._CH',             # 17
        'ED6_DT07/CH00334 ._CH',             # 18
        'ED6_DT07/CH00137 ._CH',             # 19
        'ED6_DT26/CH20290 ._CH',             # 1A
        'ED6_DT26/CH20307 ._CH',             # 1B
        'ED6_DT26/CH20296 ._CH',             # 1C
        'ED6_DT26/CH20297 ._CH',             # 1D
        'ED6_DT07/CH01640 ._CH',             # 1E
        'ED6_DT07/CH00331 ._CH',             # 1F
        'ED6_DT27/CH04590 ._CH',             # 20
        'ED6_DT27/CH04594 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
        'ED6_DT07/CH02080P._CP',             # 02
        'ED6_DT27/CH03590P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01300P._CP',             # 05
        'ED6_DT07/CH01320P._CP',             # 06
        'ED6_DT27/CH04580P._CP',             # 07
        'ED6_DT07/CH01600P._CP',             # 08
        'ED6_DT07/CH00322P._CP',             # 09
        'ED6_DT07/CH00321P._CP',             # 0A
        'ED6_DT27/CH04000P._CP',             # 0B
        'ED6_DT27/CH04004P._CP',             # 0C
        'ED6_DT07/CH00120P._CP',             # 0D
        'ED6_DT07/CH00124P._CP',             # 0E
        'ED6_DT07/CH00130P._CP',             # 0F
        'ED6_DT07/CH00134P._CP',             # 10
        'ED6_DT07/CH00140P._CP',             # 11
        'ED6_DT07/CH00144P._CP',             # 12
        'ED6_DT07/CH00150P._CP',             # 13
        'ED6_DT07/CH00154P._CP',             # 14
        'ED6_DT07/CH00320P._CP',             # 15
        'ED6_DT07/CH00324P._CP',             # 16
        'ED6_DT07/CH00330P._CP',             # 17
        'ED6_DT07/CH00334P._CP',             # 18
        'ED6_DT07/CH00137P._CP',             # 19
        'ED6_DT26/CH20290P._CP',             # 1A
        'ED6_DT26/CH20307P._CP',             # 1B
        'ED6_DT26/CH20296P._CP',             # 1C
        'ED6_DT26/CH20297P._CP',             # 1D
        'ED6_DT07/CH01640P._CP',             # 1E
        'ED6_DT07/CH00331P._CP',             # 1F
        'ED6_DT27/CH04590P._CP',             # 20
        'ED6_DT27/CH04594P._CP',             # 21
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_9BA",          # 00, 0
        "Function_1_9FE",          # 01, 1
        "Function_2_9FF",          # 02, 2
        "Function_3_D97",          # 03, 3
        "Function_4_DBC",          # 04, 4
        "Function_5_DE4",          # 05, 5
        "Function_6_E1E",          # 06, 6
        "Function_7_E5D",          # 07, 7
        "Function_8_E9C",          # 08, 8
        "Function_9_ECA",          # 09, 9
        "Function_10_F09",         # 0A, 10
        "Function_11_F48",         # 0B, 11
        "Function_12_597D",        # 0C, 12
        "Function_13_6D2D",        # 0D, 13
        "Function_14_6D58",        # 0E, 14
        "Function_15_6D83",        # 0F, 15
        "Function_16_6DA7",        # 10, 16
        "Function_17_6DD2",        # 11, 17
        "Function_18_6DEC",        # 12, 18
        "Function_19_6E06",        # 13, 19
        "Function_20_6E20",        # 14, 20
        "Function_21_6E3A",        # 15, 21
        "Function_22_6E7E",        # 16, 22
        "Function_23_6EC2",        # 17, 23
        "Function_24_6EE9",        # 18, 24
        "Function_25_6F10",        # 19, 25
        "Function_26_6F37",        # 1A, 26
    )


    def Function_0_9BA(): pass

    label("Function_0_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_9D0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_9FD")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_9EF")
    OP_A3(0x10F1)
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_9FD")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_9FD")
    OP_A3(0x10F2)
    Event(1, 0)

    label("loc_9FD")

    Return()

    # Function_0_9BA end

    def Function_1_9FE(): pass

    label("Function_1_9FE")

    Return()

    # Function_1_9FE end

    def Function_2_9FF(): pass

    label("Function_2_9FF")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x23, -850, 0, 30150, 180)
    SetChrPos(0xD, -2850, 0, 28150, 90)
    SetChrPos(0xE, 1250, 0, 28150, 270)
    SetChrPos(0xF, -2850, 0, 26150, 90)
    SetChrPos(0x10, 1250, 0, 26150, 270)
    SetChrPos(0x11, -2850, 0, 24150, 90)
    SetChrPos(0x12, 1250, 0, 24150, 270)
    SetChrChipByIndex(0xD, 9)
    SetChrChipByIndex(0xE, 9)
    SetChrChipByIndex(0xF, 9)
    SetChrChipByIndex(0x10, 9)
    SetChrChipByIndex(0x11, 9)
    SetChrChipByIndex(0x12, 9)
    OP_6D(-980, 0, 27500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_43(0xD, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0xE, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x11, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x10, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_43(0x12, 0x1, 0x0, 0x4)
    FadeToBright(2000, 0)
    Sleep(3500)
    OP_22(0x85, 0x0, 0x64)

    def lambda_B66():

        label("loc_B66")

        OP_7C(0xC8, 0x0, 0x7D0, 0xBB8)
        OP_48()
        Jump("loc_B66")

    QueueWorkItem2(0x101, 3, lambda_B66)
    Sleep(500)
    OP_A2(0x0)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0xD,
        "Wh-What the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        "We're under attack!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xD, 0x1, 0x0, 0x5)
    OP_43(0xE, 0x1, 0x0, 0x6)
    OP_43(0xF, 0x1, 0x0, 0x7)
    OP_43(0x10, 0x1, 0x0, 0x8)
    OP_43(0x11, 0x1, 0x0, 0x9)
    OP_43(0x12, 0x1, 0x0, 0xA)
    OP_43(0x23, 0x1, 0x0, 0x3)
    Sleep(1000)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #2
        0x23,
        "#6PCALM DOWN! It's just an earthquake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x23,
        "#6PHOLD your lines! Stay in position!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_9FF end

    def Function_3_D97(): pass

    label("Function_3_D97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBB")
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    Jump("Function_3_D97")

    label("loc_DBB")

    Return()

    # Function_3_D97 end

    def Function_4_DBC(): pass

    label("Function_4_DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE3")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(1500)
    Jump("Function_4_DBC")

    label("loc_DE3")

    Return()

    # Function_4_DBC end

    def Function_5_DE4(): pass

    label("Function_5_DE4")

    SetChrChipByIndex(0xFE, 10)

    label("loc_DE9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E1D")
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x1004, 0x0)
    OP_90(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0x1068, 0x0)
    Jump("loc_DE9")

    label("loc_E1D")

    Return()

    # Function_5_DE4 end

    def Function_6_E1E(): pass

    label("Function_6_E1E")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_E28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5C")
    OP_90(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFFCE0, 0x1068, 0x0)
    OP_90(0xFE, 0x320, 0x0, 0x320, 0x10CC, 0x0)
    Jump("loc_E28")

    label("loc_E5C")

    Return()

    # Function_6_E1E end

    def Function_7_E5D(): pass

    label("Function_7_E5D")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_E67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E9B")
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0xED8, 0x0)
    OP_90(0xFE, 0x3E8, 0x0, 0x0, 0xF3C, 0x0)
    Jump("loc_E67")

    label("loc_E9B")

    Return()

    # Function_7_E5D end

    def Function_8_E9C(): pass

    label("Function_8_E9C")

    SetChrChipByIndex(0xFE, 10)

    label("loc_EA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC9")
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 180, 400)
    Jump("loc_EA1")

    label("loc_EC9")

    Return()

    # Function_8_E9C end

    def Function_9_ECA(): pass

    label("Function_9_ECA")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_ED4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F08")
    OP_90(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0xFA0, 0x0)
    OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x1004, 0x0)
    Jump("loc_ED4")

    label("loc_F08")

    Return()

    # Function_9_ECA end

    def Function_10_F09(): pass

    label("Function_10_F09")

    SetChrChipByIndex(0xFE, 10)
    Sleep(50)

    label("loc_F13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F47")
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x1068, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x10CC, 0x0)
    Jump("loc_F13")

    label("loc_F47")

    Return()

    # Function_10_F09 end

    def Function_11_F48(): pass

    label("Function_11_F48")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x8, -2300, 0, 17510, 0)
    SetChrPos(0x9, -2300, 0, 24240, 180)
    SetChrPos(0xA, -4980, 0, 20880, 90)
    SetChrPos(0xD, -12080, 0, 15010, 90)
    SetChrPos(0xE, -12900, 0, 16840, 90)
    SetChrPos(0xF, -13490, 0, 18730, 90)
    SetChrPos(0x10, -14010, 0, 15710, 90)
    SetChrPos(0x11, -14670, 0, 17570, 90)
    SetChrPos(0x12, -15200, 0, 19820, 90)
    SetChrPos(0x1D, -13510, 0, 22660, 90)
    SetChrPos(0x1E, -12880, 0, 24340, 90)
    SetChrPos(0x1F, -11920, 0, 26130, 90)
    SetChrPos(0x20, -15170, 0, 22090, 90)
    SetChrPos(0x21, -14580, 0, 23690, 90)
    SetChrPos(0x22, -13960, 0, 25780, 90)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 6)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    OP_6D(-16450, 0, 14000, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(247000, 0)
    OP_6E(316, 0)
    FadeToBright(1000, 0)

    def lambda_1121():
        OP_6D(-16450, 0, 28000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1121)

    def lambda_1139():
        OP_6C(310000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1139)
    WaitChrThread(0x8, 0x1)

    def lambda_114E():
        OP_6D(-2680, 0, 21130, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_114E)

    def lambda_1166():
        OP_67(0, 4810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1166)

    def lambda_117E():
        OP_6B(2760, 4500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_117E)

    def lambda_118E():
        OP_6C(296000, 4500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_118E)

    def lambda_119E():
        OP_6E(443, 4500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_119E)
    WaitChrThread(0x9, 0x1)
    Fade(500)
    OP_6D(-5790, 0, 20930, 0)
    OP_67(0, 4810, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(271000, 0)
    OP_6E(443, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0xA,
        "#163F#5PCombatants, at the ready!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #5
        0xA,
        "#162F#5P#4SAnd...BEGIN!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_51(0x24, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12B4():
        OP_8F(0xFE, 0xFFFFD3B4, 0x0, 0x5190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_12B4)
    OP_DB()
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x40)

    def lambda_12E4():
        OP_6D(-2710, 0, 25430, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12E4)

    def lambda_12FC():
        OP_6B(1740, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12FC)

    def lambda_130C():
        OP_6C(336000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_130C)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #6 op#A op#5
        0x9,
        "#177F#6P#8AHiiiiiiiiiYAH!\x05\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_135E():
        OP_6D(-3520, 0, 18740, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_135E)

    def lambda_1376():
        OP_6B(1840, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1376)

    def lambda_1386():
        OP_6C(296000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1386)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_13A0():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x5140, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_13A0)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)

    def lambda_13D4():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x4A4C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_13D4)

    def lambda_13EF():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13EF)

    def lambda_13FF():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x433A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_13FF)
    WaitChrThread(0x9, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    def lambda_1467():
        OP_6C(278000, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1467)

    def lambda_1477():
        OP_6B(2040, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1477)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_1491():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x544C, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1491)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    Sleep(200)

    def lambda_14C8():
        OP_6D(-3520, 0, 18250, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14C8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_14F3():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x4F10, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_14F3)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 9)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 7)

    def lambda_1527():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x49E8, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1527)

    def lambda_1542():
        OP_99(0xFE, 0x9, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1542)

    def lambda_1552():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x420E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1552)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    def lambda_15B5():
        OP_6D(-3520, 0, 15920, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15B5)

    def lambda_15CD():
        OP_6C(226000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15CD)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 7)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 2)

    def lambda_15FF():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x4600, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_15FF)

    def lambda_161A():
        OP_99(0xFE, 0x7, 0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_161A)

    def lambda_162A():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x3EEE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_162A)
    OP_23(0xD6)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    def lambda_1690():
        OP_6D(-3520, 0, 16120, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1690)

    def lambda_16A8():
        OP_6B(1840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16A8)

    def lambda_16B8():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16B8)

    def lambda_16D2():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16D2)

    def lambda_16EC():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x40B0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_16EC)
    Sleep(150)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 7)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)

    def lambda_1747():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x3E6C, 0x190, 0x4E20)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1747)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_176F():
        OP_99(0xFE, 0x6, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_176F)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_17D1():
        OP_6D(-2750, 0, 20070, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17D1)

    def lambda_17E9():
        OP_6C(192000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17E9)

    def lambda_17F9():
        OP_67(0, 7000, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17F9)

    def lambda_1811():
        OP_6B(1840, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1811)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_182B():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x56EA, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_182B)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_185D():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5D98, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_185D)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    Sleep(1000)

    def lambda_1894():
        OP_6D(-2470, 0, 19840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1894)

    def lambda_18AC():
        OP_6C(184000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18AC)

    def lambda_18BC():
        OP_67(0, 3850, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18BC)

    def lambda_18D4():
        OP_6B(1720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_18D4)
    Sleep(200)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    Sleep(200)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_191F():
        OP_6D(-2280, 0, 18410, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_191F)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_1941():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x46D2, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1941)
    Sleep(200)
    SetChrPos(0x9, -2300, 0, 23960, 180)

    def lambda_1972():
        OP_8E(0xFE, 0xFFFFF704, 0x0, 0x46D2, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1972)
    OP_6D(-2250, 0, 22320, 0)
    OP_67(0, 3850, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(1000, 0)
    OP_6E(443, 0)

    def lambda_19CA():
        OP_6D(-2250, 0, 19120, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19CA)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 0)

    def lambda_19F1():
        OP_8F(0xFE, 0xFFFFF704, 0x0, 0x427C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_19F1)

    def lambda_1A0C():
        OP_99(0xFE, 0x0, 0x1, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A0C)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 45, 0)

    def lambda_1A2D():
        OP_8F(0xFE, 0xFFFFF43E, 0x0, 0x3D40, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A2D)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 2)
    OP_8C(0x9, 225, 0)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1A89():
        OP_6D(-3820, 0, 16950, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A89)

    def lambda_1AA1():
        OP_6C(315000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AA1)

    def lambda_1AB1():
        OP_8F(0xFE, 0xFFFFF5C4, 0x0, 0x3FC9, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1AB1)

    def lambda_1ACC():
        OP_99(0xFE, 0x2, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1ACC)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    OP_8C(0x8, 0, 0)

    def lambda_1AED():
        OP_8F(0xFE, 0xFFFFF682, 0x0, 0x39F8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1AED)
    Sleep(200)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_1B2A():
        OP_6D(-3120, 0, 16810, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B2A)

    def lambda_1B42():
        OP_67(0, 4680, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B42)

    def lambda_1B5A():
        OP_6B(2200, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B5A)
    OP_8C(0x9, 0, 1000)
    OP_8C(0x9, 90, 1000)

    def lambda_1B78():
        OP_8C(0xFE, 180, 1000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1B78)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_1B90():
        OP_96(0xFE, 0xFFFFF81C, 0x0, 0x4CEA, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B90)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_1BD1():
        OP_8F(0xFE, 0xFFFFF81C, 0x0, 0x3278, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1BD1)

    def lambda_1BEC():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BEC)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(600)

    def lambda_1C38():
        OP_6D(-3120, 0, 19040, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C38)

    def lambda_1C50():
        OP_6C(270000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C50)

    def lambda_1C60():
        OP_6B(1820, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C60)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_8C(0x9, 90, 1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1C8A():
        OP_8C(0xFE, 0, 1000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1C8A)

    def lambda_1C98():
        OP_8F(0xFE, 0xFFFFF81C, 0x0, 0x3E94, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1C98)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_1CD1():
        OP_8F(0xFE, 0xFFFFF81C, 0x0, 0x4484, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1CD1)

    def lambda_1CEC():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CEC)
    Sleep(100)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 5)

    def lambda_1D0B():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x4CEA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1D0B)
    WaitChrThread(0x9, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_1D6E():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D6E)
    Sleep(600)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1D92():
        OP_6D(-3120, 0, 15960, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D92)

    def lambda_1DAA():
        OP_6C(235000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DAA)

    def lambda_1DBA():
        OP_6B(2240, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DBA)
    TurnDirection(0x8, 0x9, 0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1DEE():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x4916, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1DEE)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 5)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x209, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_1E35():
        OP_8F(0xFE, 0xFFFFF880, 0x0, 0x366A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1E35)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)

    def lambda_1E69():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E69)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #7
        0x9,
        "#172F#1PAgh!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x8,
        (
            "#1126F#2PJulia! Your attacks are too predictable!\x02\x03",

            "With a rapier, you should be able\x01",
            "to overwhelm me with moves only\x01",
            "possible with a light blade!\x02\x03",

            "Remember what I taught you,\x01",
            "and come at me again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#173F#1PSir...\x02\x03",

            "#177FYes, sir!\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    Fade(250)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    OP_0D()

    def lambda_1FB4():
        OP_6D(-3120, 0, 12880, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FB4)

    def lambda_1FCC():
        OP_6B(1940, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FCC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_1FE6():
        OP_6D(-2360, 0, 19240, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FE6)

    def lambda_1FFE():
        OP_6C(322000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FFE)

    def lambda_200E():
        OP_6B(2440, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_200E)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_2030():

        label("loc_2030")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2030")

    QueueWorkItem2(0x9, 3, lambda_2030)

    def lambda_2041():
        OP_96(0xFE, 0xBFE, 0x0, 0x48BC, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2041)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2069():
        OP_96(0xFE, 0xFFFFF880, 0x0, 0x5A82, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2069)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2091():
        OP_96(0xFE, 0xFFFFE4DA, 0x0, 0x48BC, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2091)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_44(0x9, 0x3)
    Fade(500)
    OP_8C(0x9, 79, 0)
    OP_6D(-7350, 0, 21010, 0)
    OP_67(0, 2370, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(304000, 0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    Sleep(400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_2127():
        OP_6D(-5290, 0, 21010, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2127)

    def lambda_213F():
        OP_8F(0xFE, 0xFFFFEF20, 0x0, 0x48BC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_213F)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_2169():
        OP_8F(0xFE, 0xFFFFF39E, 0x0, 0x48BC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2169)

    def lambda_2184():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2184)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 349, 0)

    def lambda_21A5():
        OP_8F(0xFE, 0xFFFFFCA4, 0x0, 0x46F0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_21A5)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    def lambda_21E2():
        OP_6D(-4680, 0, 19770, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21E2)

    def lambda_21FA():
        OP_67(0, 4800, -10000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21FA)

    def lambda_2212():

        label("loc_2212")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2212")

    QueueWorkItem2(0x8, 3, lambda_2212)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_222D():
        OP_96(0xFE, 0xFFFFEA0C, 0x0, 0x48BC, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_222D)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_44(0x8, 0x3)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)

    def lambda_226D():
        OP_6D(-4690, 0, 18490, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_226D)

    def lambda_2285():
        OP_6C(270000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2285)

    def lambda_2295():
        OP_67(0, 3680, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2295)
    OP_7D(0x0, 0x9, 0x32, 0xC8)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_22BF():

        label("loc_22BF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22BF")

    QueueWorkItem2(0x9, 3, lambda_22BF)

    def lambda_22D0():
        OP_8F(0xFE, 0xFFFFF24A, 0x0, 0x5190, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_22D0)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 2)

    def lambda_2314():
        OP_96(0xFE, 0xFFFFF862, 0x0, 0x4B5A, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2314)
    OP_8C(0x9, 214, 2000)
    OP_8C(0x9, 304, 2000)
    OP_8C(0x9, 34, 2000)
    OP_8C(0x9, 124, 2000)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 3)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 7)
    OP_8C(0x8, 315, 0)

    def lambda_23A8():
        OP_8F(0xFE, 0x17C, 0x0, 0x4484, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_23A8)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_23E0():
        OP_96(0xFE, 0xFFFFF218, 0x0, 0x4F88, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_23E0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)

    def lambda_2412():
        OP_6D(-370, 0, 16280, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2412)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_243C():
        OP_96(0xFE, 0x1068, 0x0, 0x39E4, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_243C)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2495():
        OP_6D(-2090, 0, 18000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2495)

    def lambda_24AD():
        OP_6C(258000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24AD)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_24C7():
        OP_8F(0xFE, 0x780, 0x0, 0x4006, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_24C7)

    def lambda_24E2():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24E2)

    def lambda_24F2():
        OP_8C(0xFE, 306, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_24F2)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_2514():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2514)

    def lambda_2522():
        OP_96(0xFE, 0xFFFFF3F8, 0x0, 0x4EC0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2522)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    WaitChrThread(0x8, 0x0)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x8, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2586():
        OP_6D(-3700, 0, 19950, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2586)

    def lambda_259E():
        OP_6C(282000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_259E)

    def lambda_25AE():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25AE)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0xC8)

    def lambda_25D0():

        label("loc_25D0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_25D0")

    QueueWorkItem2(0x9, 3, lambda_25D0)

    def lambda_25E1():
        OP_8F(0xFE, 0xFFFFFBBE, 0x0, 0x48BC, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_25E1)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)

    def lambda_260B():
        OP_6D(-5530, 0, 18670, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_260B)

    def lambda_2623():
        OP_96(0xFE, 0xFFFFF02E, 0x0, 0x3FF2, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2623)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    OP_44(0x9, 0x3)
    OP_7D(0x1, 0x9, 0x0, 0x0)

    def lambda_2657():
        OP_6D(-4720, 0, 20630, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2657)

    def lambda_266F():
        OP_67(0, 3060, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_266F)

    def lambda_2687():
        OP_6C(258000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2687)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 12)

    def lambda_26A1():
        OP_96(0xFE, 0xFFFFF3B2, 0x0, 0x49FC, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_26A1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0x9, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 1)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 2)
    OP_8C(0x8, 213, 0)

    def lambda_2743():
        OP_8F(0xFE, 0xFFFFF86C, 0x0, 0x5870, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2743)

    def lambda_275E():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_275E)
    WaitChrThread(0x8, 0x0)
    Sleep(200)

    def lambda_2782():
        OP_6D(-3540, 0, 21820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2782)

    def lambda_279A():
        OP_67(0, 4059, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_279A)

    def lambda_27B2():
        OP_6C(234000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27B2)

    def lambda_27C2():
        OP_6B(2400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_27C2)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_27DC():
        OP_96(0xFE, 0xFFFFFCFE, 0x0, 0x65FE, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_27DC)

    def lambda_27FA():
        OP_8C(0xFE, 189, 200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27FA)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(200)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #10
        0x8,
        (
            "#1125F#2PGood, that's better.\x02\x03",

            "#1122FAnd now...my turn!\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_8C(0x9, 9, 0)
    OP_8C(0x8, 189, 0)

    def lambda_28B1():
        OP_6D(-2150, 0, 25310, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28B1)

    def lambda_28C9():
        OP_67(0, 3360, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28C9)

    def lambda_28E1():
        OP_6B(1800, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28E1)
    Fade(250)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 8)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_291E():
        OP_6D(-5080, 0, 19800, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_291E)

    def lambda_2936():
        OP_6C(270000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2936)

    def lambda_2946():
        OP_6B(2200, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2946)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)
    SetChrFlags(0x8, 0x4)

    def lambda_2965():
        OP_96(0xFE, 0xFFFFF3B2, 0xC8, 0x4F38, 0x960, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2965)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA3, 0x0, 0x64)
    Sleep(250)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)

    def lambda_29A2():
        OP_99(0xFE, 0x4, 0x5, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29A2)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 2)

    def lambda_29FB():
        OP_9E(0xFE, 0xA, 0x0, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29FB)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_2A23():
        OP_6D(-5080, 0, 23430, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A23)

    def lambda_2A3B():
        OP_67(0, 4360, -10000, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A3B)

    def lambda_2A53():
        OP_6C(315000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A53)

    def lambda_2A63():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4808, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2A63)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    ClearChrFlags(0x8, 0x4)

    def lambda_2A8D():
        OP_96(0xFE, 0xFFFFF3B2, 0x0, 0x5D02, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2A8D)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(200)

    def lambda_2ACF():
        OP_6D(-4860, 0, 20850, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2ACF)

    def lambda_2AE7():
        OP_6B(1960, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AE7)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_2B0A():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x52BC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2B0A)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_2B43():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4DF8, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2B43)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)

    def lambda_2BA2():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x45CE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2BA2)

    def lambda_2BBD():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BBD)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_2BF4():
        OP_6D(-4860, 0, 19860, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2BF4)

    def lambda_2C0C():
        OP_6B(1760, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C0C)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_2C2F():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4A6A, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2C2F)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)

    def lambda_2C8E():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x4240, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2C8E)

    def lambda_2CA9():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2CA9)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(150)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_2CEA():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x3C64, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2CEA)
    WaitChrThread(0x8, 0x0)
    Sleep(50)

    def lambda_2D12():
        OP_6D(-4860, 0, 18870, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D12)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_2D34():
        OP_8F(0xFE, 0xFFFFF3B2, 0x0, 0x46DC, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D34)
    OP_22(0x84, 0x0, 0x64)
    Sleep(300)

    def lambda_2D59():
        OP_6D(-4860, 0, 17620, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D59)

    def lambda_2D71():
        OP_6B(2060, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D71)

    def lambda_2D81():
        OP_67(0, 3360, -10000, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D81)

    def lambda_2D99():
        OP_6C(304000, 200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D99)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    OP_7D(0x0, 0x8, 0x14, 0xC8)
    OP_8C(0x8, 259, 0)

    def lambda_2DC2():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x4204, 0x190, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DC2)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 2)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_8C(0x8, 214, 800)
    OP_8C(0x8, 169, 800)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)

    def lambda_2E1E():
        OP_6D(-7640, 0, 14240, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E1E)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_2E7A():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x328C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2E7A)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2EA2():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x2738, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2EA2)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_2ECA():
        OP_96(0xFE, 0xFFFFE7C8, 0x0, 0x4FD8, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2ECA)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_2F28():
        OP_8F(0xFE, 0xFFFFE7C8, 0x0, 0x2F94, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2F28)
    Sleep(200)
    SetChrPos(0x8, -6200, 0, 20440, 180)

    def lambda_2F59():
        OP_8F(0xFE, 0xFFFFE7C8, 0x0, 0x2F94, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2F59)
    Fade(500)
    OP_6D(-7500, 0, 12160, 0)
    OP_6C(220000, 0)
    OP_6E(443, 0)

    def lambda_2F9C():
        OP_6D(-7460, 0, 9900, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F9C)

    def lambda_2FB4():
        OP_6B(1800, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FB4)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 11)
    WaitChrThread(0x8, 0x0)

    def lambda_2FE1():
        OP_6D(-7460, 0, 10900, 200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FE1)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 10)

    def lambda_3003():
        OP_8F(0xFE, 0xFFFFE7C8, 0x0, 0x2B84, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3003)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    OP_7D(0x0, 0x8, 0x14, 0xC8)

    def lambda_3030():
        OP_8F(0xFE, 0xFFFFE408, 0x0, 0x35B6, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3030)
    WaitChrThread(0x8, 0x0)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_22(0x84, 0x0, 0x64)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_306B():
        OP_6D(-5960, 0, 10310, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_306B)

    def lambda_3083():
        OP_6B(2060, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3083)

    def lambda_3093():
        OP_67(0, 4360, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3093)

    def lambda_30AB():
        OP_6C(110000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_30AB)

    def lambda_30BB():
        OP_8F(0xFE, 0xFFFFDFE4, 0x0, 0x2A30, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_30BB)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 2)

    def lambda_30E0():
        OP_8C(0xFE, 245, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_30E0)
    OP_8C(0x8, 90, 1500)
    OP_8C(0x8, 0, 1500)
    OP_8C(0x8, 270, 1500)
    OP_8C(0x8, 180, 1500)
    OP_8C(0x8, 90, 1500)
    OP_8C(0x8, 66, 1500)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)

    def lambda_3183():
        OP_96(0xFE, 0xFFFFFE5C, 0x0, 0x3458, 0x960, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3183)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_31B1():
        OP_6D(-1220, 0, 8000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31B1)

    def lambda_31C9():
        OP_67(0, 3400, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31C9)

    def lambda_31E1():
        OP_6C(154000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31E1)

    def lambda_31F1():
        OP_6B(2320, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31F1)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_320B():
        OP_96(0xFE, 0xFFFFFE5C, 0x0, 0x3458, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_320B)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)

    def lambda_3248():
        OP_99(0xFE, 0x4, 0x5, 0x708)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3248)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)

    def lambda_3265():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3265)
    OP_22(0x209, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Sleep(200)
    WaitChrThread(0x9, 0x0)

    def lambda_32A2():
        OP_6D(-2640, 0, 11340, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_32A2)

    def lambda_32BA():
        OP_67(0, 6180, -10000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32BA)

    def lambda_32D2():
        OP_6C(130000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32D2)

    def lambda_32E2():
        OP_96(0xFE, 0xD0C, 0x0, 0x3480, 0x7D0, 0x2328)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_32E2)

    def lambda_3300():
        OP_96(0xFE, 0xFFFFDF44, 0x0, 0x2C74, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3300)
    Sleep(100)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3342():
        OP_6D(-710, 0, 11560, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3342)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_3364():
        OP_96(0xFE, 0xFFFFEBA6, 0x0, 0x2E72, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3364)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)

    def lambda_33AB():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_33AB)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x3)
    OP_DC()

    ChrTalk(    #11
        0x9,
        "#175F#3PUgh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    OP_0D()

    ChrTalk(    #12
        0x8,
        (
            "#1127F#2PDefense is the same way!\x02\x03",

            "Build an image of the flow of battle in\x01",
            "your mind, offense and defense, and\x01",
            "use it to predict a foe's movements!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        "#178F#3PSir!\x02",
    )

    CloseMessageWindow()
    OP_DB()

    def lambda_34BE():
        OP_6D(1340, 0, 10040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34BE)

    def lambda_34D6():
        OP_67(0, 2660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D6)
    Sleep(500)

    ChrTalk(    #14 op#A op#5
        0x9,
        "#177F#3P#3S#15AHii-YAAAAAAH!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_3567():

        label("loc_3567")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3567")

    QueueWorkItem2(0x9, 3, lambda_3567)

    def lambda_3578():
        OP_96(0xFE, 0x67C, 0x0, 0x3F01, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3578)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_35A0():
        OP_8F(0xFE, 0xFFFFF77C, 0x0, 0x358E, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_35A0)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_35C5():
        OP_96(0xFE, 0xFFFFFD3A, 0x0, 0x2530, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_35C5)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_44(0x9, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3602():
        OP_6D(-2540, 0, 11300, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3602)

    def lambda_361A():
        OP_67(0, 4420, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_361A)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 12)

    def lambda_363C():
        OP_96(0xFE, 0xFFFFF218, 0x0, 0x2954, 0x640, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_363C)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 0)
    Sleep(200)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_3683():

        label("loc_3683")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3683")

    QueueWorkItem2(0x8, 3, lambda_3683)

    def lambda_3694():
        OP_96(0xFE, 0xFFFFEACA, 0x0, 0x3DFE, 0x258, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3694)
    WaitChrThread(0x9, 0x0)
    OP_22(0x84, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 1)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_36F3():
        OP_6D(-5430, 0, 14290, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_36F3)

    def lambda_370B():
        OP_6C(190000, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_370B)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)

    def lambda_3725():
        OP_96(0xFE, 0xFFFFEA02, 0x0, 0x4C36, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3725)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    Sleep(100)
    OP_44(0x8, 0x3)

    def lambda_3760():
        OP_6D(-6870, 0, 16030, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3760)

    def lambda_3778():
        OP_67(0, 3360, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3778)

    def lambda_3790():
        OP_6C(238000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3790)

    def lambda_37A0():
        OP_6B(2180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37A0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)
    TurnDirection(0x9, 0x8, 0)

    def lambda_37C9():
        OP_8F(0xFE, 0xFFFFED7C, 0x0, 0x3ECF, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_37C9)
    Sleep(100)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(200)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3809():
        OP_8F(0xFE, 0xFFFFEB38, 0x0, 0x4736, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3809)
    WaitChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_388A():
        OP_6D(-6250, 0, 15120, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_388A)

    def lambda_38A2():
        OP_6B(1980, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38A2)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    Sleep(400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_38CA():
        OP_8F(0xFE, 0xFFFFEC82, 0x0, 0x431C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_38CA)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)

    def lambda_38EF():
        OP_8F(0xFE, 0xFFFFF038, 0x0, 0x3B9C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_38EF)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_3957():
        OP_6D(-5360, 0, 13720, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3957)

    def lambda_396F():
        OP_6C(236000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_396F)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_399C():
        OP_96(0xFE, 0xFFFFF650, 0x0, 0x2C10, 0x258, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_399C)
    Sleep(400)

    def lambda_39BF():
        OP_8F(0xFE, 0xFFFFEE44, 0x0, 0x3F48, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_39BF)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 1)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 5)

    def lambda_39F8():
        OP_8F(0xFE, 0xFFFFF36C, 0x0, 0x32E6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_39F8)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_3A60():
        OP_6B(1780, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A60)

    def lambda_3A70():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A70)

    def lambda_3A8A():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A8A)
    WaitChrThread(0x101, 0x0)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_3B18():
        OP_6D(-3420, 0, 13940, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B18)

    def lambda_3B30():
        OP_67(0, 6500, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B30)

    def lambda_3B48():
        OP_6C(148000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B48)

    def lambda_3B58():
        OP_6B(2180, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B58)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 2)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 3)
    OP_43(0x8, 0x3, 0x0, 0xD)

    def lambda_3B83():
        OP_96(0xFE, 0xFFFFECC8, 0x0, 0x2B84, 0x4B0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3B83)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x9, 0x3, 0x0, 0xE)

    def lambda_3BB3():
        OP_96(0xFE, 0xFFFFF542, 0x0, 0x4862, 0x4B0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3BB3)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    Sleep(200)

    def lambda_3C1F():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3C1F)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3C47():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3C47)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)

    def lambda_3C77():
        OP_6D(-3810, 0, 12730, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C77)

    def lambda_3C8F():
        OP_67(0, 4600, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C8F)

    def lambda_3CA7():

        label("loc_3CA7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3CA7")

    QueueWorkItem2(0x9, 3, lambda_3CA7)

    def lambda_3CB8():

        label("loc_3CB8")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_3CB8")

    QueueWorkItem2(0x8, 3, lambda_3CB8)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3CD3():
        OP_96(0xFE, 0xFFFFF164, 0x0, 0x3B38, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3CD3)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3CFB():
        OP_6C(204000, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CFB)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3D15():
        OP_96(0xFE, 0xFFFFF7A4, 0x0, 0x2E40, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3D15)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_3D47():
        OP_96(0xFE, 0xFFFFFA2E, 0x0, 0x3A34, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3D47)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3D6F():
        OP_6C(122000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D6F)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3D89():
        OP_96(0xFE, 0xFFFFEFE8, 0x0, 0x367E, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3D89)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3DB1():
        OP_6D(-3690, 0, 10320, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DB1)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 5)

    def lambda_3DD3():
        OP_96(0xFE, 0xFFFFE994, 0x0, 0x3D40, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3DD3)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 8)

    def lambda_3E05():
        OP_96(0xFE, 0xFFFFE1A6, 0x0, 0x3340, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3E05)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 7)
    OP_44(0x9, 0x3)
    OP_44(0x8, 0x3)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3E55():
        OP_6D(-400, 0, 8240, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E55)

    def lambda_3E6D():
        OP_67(0, 3300, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E6D)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_3E8F():
        OP_8F(0xFE, 0xFFFFF9CA, 0x0, 0x231E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3E8F)

    def lambda_3EAA():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3EAA)
    Sleep(100)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 2)
    OP_8C(0x8, 205, 0)

    def lambda_3ED0():
        OP_8F(0xFE, 0xFFFFF0CE, 0x0, 0x319C, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3ED0)

    def lambda_3EEB():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3EEB)
    PlayEffect(0x0, 0xFF, 0x8, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3F60():
        OP_6D(-1000, 0, 11820, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F60)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_3F82():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3F82)
    OP_43(0x9, 0x3, 0x0, 0x10)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)

    def lambda_3FB6():
        OP_8F(0xFE, 0xFFFFE6A6, 0x0, 0x3EEE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3FB6)

    def lambda_3FD1():
        OP_99(0xFE, 0x4, 0x6, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3FD1)
    Sleep(50)
    OP_22(0x84, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    OP_8C(0x8, 257, 0)

    def lambda_3FFC():
        OP_96(0xFE, 0xFFFFFF38, 0x0, 0x3584, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3FFC)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    def lambda_403C():
        OP_6D(-1000, 0, 13940, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_403C)

    def lambda_4054():
        OP_6C(118000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4054)
    SetChrChipByIndex(0x9, 28)
    SetChrSubChip(0x9, 4)

    def lambda_406E():
        OP_96(0xFE, 0xFFFFF236, 0x0, 0x4A4C, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_406E)
    OP_43(0x9, 0x3, 0x0, 0xE)
    WaitChrThread(0x9, 0x3)
    OP_8C(0x9, 147, 0)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 3)
    Sleep(50)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)
    OP_43(0x8, 0x3, 0x0, 0xF)
    Sleep(200)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)

    def lambda_40DC():
        OP_6D(1360, 0, 15090, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40DC)

    def lambda_40F4():
        OP_6C(64000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40F4)

    def lambda_4104():
        OP_6B(1780, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4104)

    def lambda_4114():
        OP_8F(0xFE, 0xFFFFFC4A, 0x190, 0x396C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_4114)
    WaitChrThread(0x9, 0x0)

    def lambda_4134():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_4134)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 5)
    OP_22(0x209, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 6)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)

    def lambda_4175():
        OP_6D(-1170, 0, 17520, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4175)

    def lambda_418D():
        OP_67(0, 4340, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_418D)

    def lambda_41A5():
        OP_6B(2240, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41A5)

    def lambda_41B5():
        OP_6C(45000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_41B5)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 4)
    OP_43(0x8, 0x3, 0x0, 0xF)
    ClearChrFlags(0x9, 0x4)

    def lambda_41DB():
        OP_96(0xFE, 0xFFFFEC64, 0x0, 0x4C86, 0x4B0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_41DB)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)
    WaitChrThread(0x9, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)

    def lambda_4232():
        OP_9E(0xFE, 0xA, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4232)
    Sleep(200)

    def lambda_4251():
        OP_6D(-1660, 0, 17640, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4251)

    def lambda_4269():
        OP_6C(80000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4269)
    Fade(250)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 8)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_4293():
        OP_6D(-4760, 0, 21530, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4293)

    def lambda_42AB():
        OP_6B(1800, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42AB)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)
    OP_7D(0x0, 0x8, 0xA, 0x1F4)

    def lambda_42D6():
        OP_96(0xFE, 0xFFFFE110, 0x0, 0x59C4, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_42D6)
    Sleep(100)
    OP_22(0x9B, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 3)
    WaitChrThread(0x8, 0x0)

    def lambda_434C():
        OP_9E(0xFE, 0x1E, 0x0, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_434C)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    def lambda_437C():
        OP_6D(-5050, 0, 21050, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_437C)

    def lambda_4394():
        OP_6B(2160, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4394)

    def lambda_43A4():
        OP_6C(8000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43A4)

    def lambda_43B4():
        OP_8C(0xFE, 35, 400)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_43B4)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 3)
    OP_7D(0x0, 0x8, 0x32, 0xC8)

    def lambda_43D4():
        OP_96(0xFE, 0xFFFFE304, 0x0, 0x3F0C, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_43D4)
    WaitChrThread(0x9, 0x3)

    def lambda_43F7():
        OP_8C(0xFE, 305, 400)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_43F7)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x8, 0x0, 0x0)

    def lambda_4417():
        OP_6D(-3930, 0, 22440, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4417)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 6)

    def lambda_4442():
        OP_8F(0xFE, 0xFFFFE8AE, 0x0, 0x4704, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_4442)
    OP_8C(0x8, 270, 1000)
    OP_8C(0x8, 180, 1000)
    OP_8C(0x8, 90, 1000)
    TurnDirection(0x8, 0x9, 1000)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x9, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x8, 26)
    SetChrSubChip(0x8, 7)
    TurnDirection(0x9, 0x8, 0)

    def lambda_44D2():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x578, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_44D2)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 0x0)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 4)
    Sleep(400)

    def lambda_451F():
        OP_6D(-2680, 0, 21130, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_451F)

    def lambda_4537():
        OP_6B(1820, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4537)

    def lambda_4547():
        OP_6C(296000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4547)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 9)

    def lambda_4561():

        label("loc_4561")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4561")

    QueueWorkItem2(0x8, 3, lambda_4561)

    def lambda_4572():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_4572)

    def lambda_4590():

        label("loc_4590")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4590")

    QueueWorkItem2(0x9, 3, lambda_4590)
    WaitChrThread(0x8, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_44(0x8, 0x3)
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_DC()

    ChrTalk(    #15
        0xA,
        "#163F#6PEnough! I call the match.\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_45FE():
        OP_67(0, 4810, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45FE)

    def lambda_4616():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4616)
    OP_22(0xBF, 0x0, 0x64)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x40)

    ChrTalk(    #16
        0x9,
        "#175F#4PHaah... Haah... Haaaah...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 27)
    SetChrSubChip(0x8, 6)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x8,
        (
            "#1125F#6PHeh! Not a whit less than I expected.\x02\x03",

            "#1120FI only taught you the barest of\x01",
            "basics all those years ago...\x02\x03",

            "...but you've come far on your\x01",
            "own, Julia. Well done.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x9,
        (
            "#171F#4PNo, sir...\x02\x03",

            "My performance was shameful...\x01",
            "I...haah...could not best you...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFEC8C, 0x0, 0x5190, 0xDAC, 0x0)

    ChrTalk(    #19
        0xA,
        (
            "#165F#6PDon't disparage yourself, Schwarz.\x01",
            "That was a fairly impressive display.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        "#175F#4PBut, General--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "#163F#6PRemember who you're fighting,\x01",
            "Captain.\x02\x03",

            "I've yet to meet a man--or woman--who can\x01",
            "match blades with Cassius without having their\x01",
            "sword swept from their hand in a few strokes.\x02\x03",

            "#165FYou did very well for yourself. I see why Cassius\x01",
            "and Her Majesty place such stock in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#173F#4PTh-Thank you, sir...\x02\x03",

            "#176FStill, a chance to practice like\x01",
            "this doesn't come up very often.\x02\x03",

            "#172FI'd like to continue until I'm truly\x01",
            "unable to fight, if you don't mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "#164F#6PHa-ha-ha-ha! Good!\x02\x03",

            "#165FWell, Cassius? Up for risking a skewering\x01",
            "again? She may well manage it this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#1125F#6PWell, I'd be humbled to\x01",
            "get poked down a peg...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 12950, 0, 21590, 270)
    SetChrPos(0xC, 13170, 0, 22870, 270)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    TurnDirection(0x8, 0xB, 400)
    Sleep(500)

    ChrTalk(    #25
        0x8,
        "#1120F#6PBut I believe we have a visitor.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)

    def lambda_4B79():
        OP_6D(6670, 0, 21130, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4B79)

    def lambda_4B91():
        TurnDirection(0x9, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4B91)

    def lambda_4B9F():

        label("loc_4B9F")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_4B9F")

    QueueWorkItem2(0x8, 1, lambda_4B9F)
    WaitChrThread(0x9, 0x2)
    Sleep(500)

    def lambda_4BBA():

        label("loc_4BBA")

        TurnDirection(0x9, 0xB, 400)
        OP_48()
        Jump("loc_4BBA")

    QueueWorkItem2(0x9, 1, lambda_4BBA)

    def lambda_4BCB():
        OP_8E(0xFE, 0x226, 0x0, 0x4D44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4BCB)
    Sleep(500)

    def lambda_4BEB():
        OP_8E(0xFE, 0x5E6, 0x0, 0x5302, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4BEB)
    OP_69(0x24, 0x1388)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xC, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)

    ChrTalk(    #26
        0xC,
        (
            "#692FHah! Dang if that wasn't one heck\x01",
            "of a show!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        "#703FWell fought, both of you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 400)
    Sleep(300)

    ChrTalk(    #28
        0xB,
        (
            "#701F#5PCaptain Schwarz.\x01",
            "That was very impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        "#171FLieutenant Colonel Cid!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xC, 400)
    Sleep(300)

    ChrTalk(    #30
        0x9,
        "#173FAnd the man with you is...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 400)
    Sleep(300)

    ChrTalk(    #31
        0xC,
        (
            "#691F#5PMaintenance Chief Gustav, ma'am.\x01",
            "The central factory sent me over.\x02\x03",

            "#693FNice to meet you, Captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#173FOh! Pardon me.\x02\x03",

            "#176FI am Captain Julia Schwarz, company\x01",
            "commander of the Royal Guard.\x02\x03",

            "#170FIt's a pleasure to meet you,\x01",
            "Mr. Gustav.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#165F#6PHm. It seems that WILL be\x01",
            "all for today, then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E5B():
        OP_6D(-6760, 0, 19100, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4E5B)
    OP_8C(0x8, 302, 400)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #34
        0x8,
        (
            "#1120F#5PAll right, lads, show's over.\x02\x03",

            "Back to your posts!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EC0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4EC0)
    Sleep(50)

    def lambda_4ED3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4ED3)

    def lambda_4EE1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4EE1)
    Sleep(50)

    def lambda_4EF4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4EF4)

    def lambda_4F02():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4F02)
    Sleep(50)

    def lambda_4F15():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4F15)

    def lambda_4F23():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F23)
    Sleep(50)

    def lambda_4F36():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4F36)

    def lambda_4F44():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F44)
    Sleep(50)

    def lambda_4F57():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4F57)

    def lambda_4F65():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F65)
    Sleep(50)

    def lambda_4F78():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F78)
    Sleep(500)
    SetMessageWindowPos(140, 120, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #35
        "\x07\x00#5SSir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x8, 0x0, 0x0, 0x15)
    OP_43(0x8, 0x1, 0x0, 0x16)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)

    def lambda_4FDF():
        OP_69(0xFE, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4FDF)
    TurnDirection(0x8, 0x9, 400)
    WaitChrThread(0x24, 0x1)

    ChrTalk(    #36
        0xC,
        (
            "#691F#5PSo, mind showin' me to the\x01",
            "Arseille's engine room?\x02\x03",

            "I'd like to get an idea of how\x01",
            "we're going to attack this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "#171FCertainly. Follow me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    Sleep(500)

    ChrTalk(    #38
        0x9,
        (
            "#176FYou'll have to excuse me,\x01",
            "General Morgan, General Bright.\x02\x03",

            "#171FGeneral, thank you very much\x01",
            "for your guidance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#1121F#6PHah! Not at all! These old bones\x01",
            "needed a workout anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#165F#6PCaptain, Mr. Gustav.\x01",
            "Take care with the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#172FSir!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)
    Sleep(300)

    ChrTalk(    #42
        0xC,
        (
            "#691FNo worries, General!\x01",
            "The Arseille's like my baby.\x01",
            "I won't let her down.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_520F():

        label("loc_520F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_520F")

    QueueWorkItem2(0x8, 3, lambda_520F)

    def lambda_5220():

        label("loc_5220")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_5220")

    QueueWorkItem2(0xB, 3, lambda_5220)
    OP_8C(0x9, 70, 400)

    def lambda_5238():
        OP_6D(-1480, 0, 22850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5238)

    def lambda_5250():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5250)
    OP_8C(0xC, 70, 400)

    def lambda_5272():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5272)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xC, 0x1)
    Sleep(500)

    def lambda_529C():
        OP_6D(-3450, 0, 20710, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_529C)

    def lambda_52B4():
        OP_6C(308000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_52B4)

    def lambda_52C4():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_52C4)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_44(0x8, 0x3)
    OP_44(0xB, 0x3)

    ChrTalk(    #43
        0xB,
        (
            "#701F#5PCaptain Schwarz has gotten quite\x01",
            "impressive.\x02\x03",

            "I swear she's even better\x01",
            "than when I saw her last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#1125F#5PYes. She's come a long way, very quickly.\x02\x03",

            "#1120FEven now, she's only a step or two below you\x01",
            "and Richard, Colonel. And she can only grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#164F#6PIndeed! Watching youth on display like\x01",
            "that gives me back a bit of my old drive!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 148, 400)
    Sleep(300)

    ChrTalk(    #46
        0xA,
        (
            "#165F#6PCassius, how about it? I'LL give you a\x01",
            "skewering later, if you're up for it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54B7():
        OP_8C(0xFE, 344, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54B7)

    def lambda_54C5():
        OP_8C(0xFE, 267, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_54C5)
    WaitChrThread(0x8, 0x1)
    Sleep(300)

    ChrTalk(    #47
        0x8,
        (
            "#1123F#5PEr, Morgan.\x02\x03",

            "I'm not sure it'd be the\x01",
            "best idea at your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        "#160F#6PMmmmrrrrgh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#1120F#5PBesides, I heard you did quite well\x01",
            "for yourself at last year's tournament\x01",
            "in Grancel.\x02\x03",

            "You have to let the young folks\x01",
            "have their moment occasionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "#163F#6PHmph! Why do you think I gave you\x01",
            "command?\x02\x03",

            "#165FIf you can say that, how about you stop\x01",
            "complaining and do your job, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#1123F#5POuch. Put my foot right into\x01",
            "THAT hornet's nest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        "#701F#2PHaha!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)
    Sleep(300)

    ChrTalk(    #53
        0xA,
        (
            "#161F#6PSpeaking of a hornet's nest...\x01",
            "Lieutenant Colonel, I believe you'll\x01",
            "be assigned to the guard patrol?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "#701F#2PYes, sir. I'll be leaving at noon.\x02\x03",

            "I'll be using three companies\x01",
            "and two patrol ships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "#165F#6PI'll be at the signing ceremony itself,\x01",
            "but I won't be free until then.\x02\x03",

            "You're in charge of the defense\x01",
            "of Grancel until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "#703F#2PLeave it to me, sir.\x02\x03",

            "#701FI'll be sure to work well with the Bracer\x01",
            "Guild to make sure that nothing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#161F#6PMmmm.\x02\x03",

            "#163FI don't like it...but I suppose\x01",
            "we've little choice but to lean\x01",
            "on those civilians this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#1120F#5PHeh. Warming up to the guild\x01",
            "a little, Morgan?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    SetMapFlags(0x10)
    Return()

    # Function_11_F48 end

    def Function_12_597D(): pass

    label("Function_12_597D")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x8, -2300, 0, 17510, 0)
    SetChrPos(0x9, -2300, 0, 24240, 180)
    SetChrPos(0xA, -4300, 0, 20880, 90)
    SetChrPos(0xD, -12080, 0, 15010, 90)
    SetChrPos(0xE, -12900, 0, 16840, 90)
    SetChrPos(0xF, -13490, 0, 18730, 90)
    SetChrPos(0x10, -14010, 0, 15710, 90)
    SetChrPos(0x11, -14670, 0, 17570, 90)
    SetChrPos(0x12, -15200, 0, 19820, 90)
    SetChrPos(0x1D, -13510, 0, 22660, 90)
    SetChrPos(0x1E, -12880, 0, 24340, 90)
    SetChrPos(0x1F, -11920, 0, 26130, 90)
    SetChrPos(0x20, -15170, 0, 22090, 90)
    SetChrPos(0x21, -14580, 0, 23690, 90)
    SetChrPos(0x22, -13960, 0, 25780, 90)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_6D(-16450, 0, 14000, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(247000, 0)
    OP_6E(316, 0)
    FadeToBright(1000, 0)

    def lambda_5B1F():
        OP_6D(-16450, 0, 28000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B1F)

    def lambda_5B37():
        OP_6C(310000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5B37)
    WaitChrThread(0x8, 0x1)

    def lambda_5B4C():
        OP_6D(-2680, 0, 21130, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B4C)

    def lambda_5B64():
        OP_67(0, 4810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5B64)

    def lambda_5B7C():
        OP_6B(2760, 4500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5B7C)

    def lambda_5B8C():
        OP_6C(296000, 4500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5B8C)

    def lambda_5B9C():
        OP_6E(443, 4500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5B9C)
    WaitChrThread(0x9, 0x1)
    Sleep(1000)

    ChrTalk(    #59
        0xA,
        (
            "#160F#4P両者、構え！\x02\x03",

            "#3S始めいっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x24, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #60
        0x9,
        "#170F#6P──やあああああッ！\x02",
    )

    CloseMessageWindow()

    def lambda_5C40():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C40)

    def lambda_5C5E():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5C5E)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_5C86():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C86)

    def lambda_5CA4():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5CA4)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #61
        0x9,
        "#170F#6Pくっ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#1120F#6Pどうした！？\x01",
            "動きが直線的すぎるぞ！\x02\x03",

            "細剣だからこそ可能な\x01",
            "攻めの流れが作れるはずだ！\x02\x03",

            "教えたことを思い出せ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "#170F#6Pハッ……\x02\x03",

            "……はいッ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D81():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D81)

    def lambda_5D9F():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D9F)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_5DC7():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5DC7)

    def lambda_5DE5():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DE5)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #64
        0x8,
        (
            "#1120F#6Pそれでいい……\x02\x03",

            "では、こちらからも行くぞ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E46():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5E46)

    def lambda_5E64():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5E64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_5E8C():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5E8C)

    def lambda_5EAA():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5EAA)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)

    ChrTalk(    #65
        0x9,
        "#170F#6Pくうっ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#1120F#6P守りも基本は同じだ！\x02\x03",

            "相手の動きを取り込みつつ\x01",
            "攻守の流れをイメージしろ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#170F#6Pはい！\x02\x03",

            "ハアアアアアアッ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F6A():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4F9C, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5F6A)

    def lambda_5F88():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5384, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F88)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_5FB0():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x4466, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5FB0)

    def lambda_5FCE():
        OP_96(0xFE, 0xFFFFF704, 0x0, 0x5EB0, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5FCE)
    WaitChrThread(0x8, 0x1)
    Sleep(1000)
    OP_22(0xBF, 0x0, 0x64)
    Sleep(6000)

    ChrTalk(    #68
        0x9,
        "#170F#6Pはあっ、はあっ、はあっ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#1120F#6Pふふ、さすがだな。\x02\x03",

            "昔、お前に教えたのは\x01",
            "ほんの基礎だけだったが……\x02\x03",

            "よくぞ独力でここまで鍛えた。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x9, 1)
    OP_0D()

    ChrTalk(    #70
        0x9,
        (
            "#170F#6Pい……いえ……\x02\x03",

            "まだまだ未熟です……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0xFFFFF362, 0x0, 0x5190, 0xBB8, 0x0)
    Sleep(1000)
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #71
        0xA,
        (
            "#160F#4Pうむ、そこまでだ。\x02\x03",

            "なかなか良い仕合だったぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        "#170F#6P将軍、ですが……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#160F#4P正直、おぬしがここまで\x01",
            "やるとは思いもしなかった。\x02\x03",

            "相当な使い手であっても\x01",
            "カシウス相手なら数合ほどで\x01",
            "剣を弾かれてしまっただろう。\x02\x03",

            "若手最強と言われるのも肯ける。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "#170F#6Pきょ、恐縮です……\x02\x03",

            "ですが滅多にない機会……\x02\x03",

            "できれば叩きのめされるまで\x01",
            "お付き合い願えないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#160F#4Pフハハハハ！\x01",
            "なかなか頼もしいな。\x02\x03",

            "さて、どうするカシウス？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#1120F#6Pふふ、付き合って\x01",
            "やりたいのは山々ですが……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 12950, 0, 21590, 270)
    SetChrPos(0xC, 13170, 0, 22870, 270)
    TurnDirection(0x8, 0xB, 400)
    Sleep(1000)

    ChrTalk(    #77
        0x8,
        "#1120F#6Pどうやらお客人のようですな。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0xB, 400)
    Sleep(1000)

    def lambda_638C():

        label("loc_638C")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_638C")

    QueueWorkItem2(0x8, 1, lambda_638C)
    OP_6D(6670, 0, 21130, 2000)

    def lambda_63AE():
        OP_8E(0xFE, 0x226, 0x0, 0x4D44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_63AE)
    Sleep(300)

    def lambda_63CE():
        OP_8E(0xFE, 0x262, 0x0, 0x55B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_63CE)
    OP_69(0x24, 0x1388)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xC, 0x1)
    Sleep(1000)
    OP_44(0x8, 0x1)

    ChrTalk(    #78
        0xC,
        (
            "#690Fは～、こりゃあ\x01",
            "凄いモンを見ちまったなァ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "#700F２人ともお疲れさまでした。\x02\x03",

            "シュバルツ大尉。\x01",
            "本当に見事だったよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#170Fシード中佐……\x02\x03",

            "それにそちらの方は……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xC,
        (
            "#690F中央工房から派遣された\x01",
            "グスタフっていう者だ。\x02\x03",

            "よろしく頼むぜ、隊長さん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "#170Fこ、これは失礼した。\x02\x03",

            "王室親衛隊、中隊長。\x01",
            "ユリア・シュバルツ大尉です。\x02\x03",

            "こちらこそよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#160Fふむ、どうやら\x01",
            "これでお開きのようだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65AE():
        OP_6D(-6760, 0, 19100, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_65AE)
    OP_8C(0x8, 302, 400)
    Sleep(2000)

    ChrTalk(    #84
        0x8,
        (
            "#1120F#3Pみんな、余興はおしまいだ。\x02\x03",

            "それぞれの持ち場に戻ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("兵士たち")

    AnonymousTalk(    #85
        "\x07\x00#4Sイエス・サー！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0xD, 0x1, 0x0, 0x11)
    OP_43(0x10, 0x1, 0x0, 0x12)
    OP_43(0x1F, 0x1, 0x0, 0x13)
    OP_43(0x22, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xE, 0x1, 0x0, 0x11)
    OP_43(0x11, 0x1, 0x0, 0x12)
    OP_43(0x1E, 0x1, 0x0, 0x13)
    OP_43(0x21, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xF, 0x1, 0x0, 0x11)
    OP_43(0x12, 0x1, 0x0, 0x12)
    OP_43(0x1D, 0x1, 0x0, 0x13)
    OP_43(0x20, 0x1, 0x0, 0x14)
    OP_69(0x24, 0x3E8)
    Sleep(1000)
    TurnDirection(0x8, 0xB, 400)
    Sleep(1000)

    ChrTalk(    #86
        0xC,
        (
            "#690Fさてと、早速で悪いが\x01",
            "機関部を見せてくれるか？\x02\x03",

            "できれば今日中に\x01",
            "目処をつけちまいたいからな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        "#170Fええ、了解しました。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    Sleep(1000)

    ChrTalk(    #88
        0x9,
        (
            "#170Fそれでは失礼します！\x02\x03",

            "准将、指南していただき\x01",
            "ありがとうございました！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 343, 400)
    Sleep(1000)

    ChrTalk(    #89
        0x8,
        (
            "#1120Fなんのなんの。\x01",
            "こちらも良い運動になった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "#160F整備長、大尉。\x01",
            "アルセイユを頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "#170Fは！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        "#690Fどんとお任せあれ。\x02",
    )

    CloseMessageWindow()

    def lambda_6856():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6856)
    Sleep(1000)

    def lambda_6876():
        OP_8E(0xFE, 0x3DF4, 0x0, 0x5BC2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6876)
    Sleep(2000)

    def lambda_6896():
        OP_6D(-2510, 0, 20260, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6896)

    def lambda_68AE():
        OP_6C(308000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_68AE)

    def lambda_68BE():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_68BE)
    WaitChrThread(0xB, 0x1)
    Sleep(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)

    ChrTalk(    #93
        0xB,
        (
            "#700Fふふ……\x01",
            "さすがですね、彼女は。\x02\x03",

            "これから更に伸びそうです。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#1120Fああ、そうだな。\x02\x03",

            "お前やリシャールの域まで\x01",
            "あと１、２歩といった所だろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 148, 400)
    Sleep(1000)

    ChrTalk(    #95
        0xA,
        (
            "#160Fふむ、ああいう若者を見ると\x01",
            "老体にも湧き立つものがあるな。\x02\x03",

            "カシウス、後で付き合わんか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#1120F将軍……\x02\x03",

            "さすがにお年を考えた方が\x01",
            "よろしいんじゃありませんか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        "#160Fむむっ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#1120F聞けば去年の武術大会では\x01",
            "かなり大暴れしたそうですな？\x02\x03",

            "少しは若い者に花を持たせて\x01",
            "やらなくてはいかんでしょう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "#160Fふん、だからこそ\x01",
            "お前に司令の座を委ねたのだ。\x02\x03",

            "そこまで言ったからには\x01",
            "文句を言わずに勤めてもらうぞ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        "#1120Fおっと、ヤブ蛇でしたか。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        "#700Fふふ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "#160Fそうだ、シード中佐。\x01",
            "今日には出発するそうだな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "#700Fはい、正午には。\x02\x03",

            "軍用艇２隻をもって\x01",
            "３個中隊を率いる予定です。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "#160F調印式にはワシも参加するが\x01",
            "それまでは身動きがとれん。\x02\x03",

            "王都の守りは頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        (
            "#700Fよろしくお任せ下さい。\x02\x03",

            "遊撃士協会と協力して\x01",
            "事に当たらせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "#160Fう、うむ……\x02\x03",

            "あまり愉快ではないが\x01",
            "今回ばかりは仕方なかろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#1120Fふふ、将軍のギルド嫌いも\x01",
            "徐々に治りつつあるようですな。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_597D end

    def Function_13_6D2D(): pass

    label("Function_13_6D2D")

    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    TurnDirection(0xFE, 0x9, 1000)
    Return()

    # Function_13_6D2D end

    def Function_14_6D58(): pass

    label("Function_14_6D58")

    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 270, 1000)
    TurnDirection(0xFE, 0x8, 1000)
    Return()

    # Function_14_6D58 end

    def Function_15_6D83(): pass

    label("Function_15_6D83")

    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    TurnDirection(0xFE, 0x9, 1000)
    Return()

    # Function_15_6D83 end

    def Function_16_6DA7(): pass

    label("Function_16_6DA7")

    OP_8C(0xFE, 90, 1400)
    OP_8C(0xFE, 0, 1400)
    OP_8C(0xFE, 270, 1400)
    OP_8C(0xFE, 180, 1400)
    OP_8C(0xFE, 90, 1400)
    TurnDirection(0xFE, 0x8, 1400)
    Return()

    # Function_16_6DA7 end

    def Function_17_6DD2(): pass

    label("Function_17_6DD2")

    OP_8E(0xFE, 0x1C2, 0x0, 0x1982, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_6DD2 end

    def Function_18_6DEC(): pass

    label("Function_18_6DEC")

    OP_8E(0xFE, 0xFFFF437C, 0x0, 0x42CC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_6DEC end

    def Function_19_6E06(): pass

    label("Function_19_6E06")

    OP_8E(0xFE, 0xFFFFFD80, 0x0, 0x8980, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_6E06 end

    def Function_20_6E20(): pass

    label("Function_20_6E20")

    OP_8E(0xFE, 0xFFFF81AC, 0x0, 0xFCC5, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_6E20 end

    def Function_21_6E3A(): pass

    label("Function_21_6E3A")

    OP_43(0xF, 0x1, 0x0, 0x17)
    Sleep(600)
    OP_43(0x10, 0x1, 0x0, 0x18)
    Sleep(200)
    OP_43(0x12, 0x1, 0x0, 0x18)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(400)
    OP_43(0x11, 0x1, 0x0, 0x18)
    Sleep(600)
    OP_43(0xD, 0x1, 0x0, 0x17)
    Return()

    # Function_21_6E3A end

    def Function_22_6E7E(): pass

    label("Function_22_6E7E")

    OP_43(0x21, 0x1, 0x0, 0x1A)
    Sleep(200)
    OP_43(0x1D, 0x1, 0x0, 0x19)
    Sleep(600)
    OP_43(0x20, 0x1, 0x0, 0x1A)
    Sleep(600)
    OP_43(0x1F, 0x1, 0x0, 0x19)
    Sleep(400)
    OP_43(0x1E, 0x1, 0x0, 0x19)
    Sleep(200)
    OP_43(0x22, 0x1, 0x0, 0x1A)
    Return()

    # Function_22_6E7E end

    def Function_23_6EC2(): pass

    label("Function_23_6EC2")

    OP_8B(0xFE, 0x1C2, 0x1982, 0x190)
    OP_8E(0xFE, 0x1C2, 0x0, 0x1982, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_6EC2 end

    def Function_24_6EE9(): pass

    label("Function_24_6EE9")

    OP_8B(0xFE, 0xFFFF437C, 0x42CC, 0x190)
    OP_8E(0xFE, 0xFFFF437C, 0x0, 0x42CC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_6EE9 end

    def Function_25_6F10(): pass

    label("Function_25_6F10")

    OP_8B(0xFE, 0xFFFFFD80, 0x8980, 0x190)
    OP_8E(0xFE, 0xFFFFFD80, 0x0, 0x8980, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_6F10 end

    def Function_26_6F37(): pass

    label("Function_26_6F37")

    OP_8B(0xFE, 0xFFFF81AC, 0xFCC5, 0x190)
    OP_8E(0xFE, 0xFFFF81AC, 0x0, 0xFCC5, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_6F37 end

    SaveToFile()

Try(main)
