from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4403   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Military Dog',                         # 9
        'Military Dog',                         # 10
        'Military Dog',                         # 11
        'Kanone',                               # 12
        'Duke Dunan',                           # 13
        'Scherazard',                           # 14
        'Agate',                                # 15
        'Olivier',                              # 16
        'Kloe',                                 # 17
        'Tita',                                 # 18
        'Zin',                                  # 19
        'Anelace',                              # 20
        'Renne',                                # 21
        'Lt. Colonel Cid',                      # 22
        'Butler Phillip',                       # 23
        'Nial',                                 # 24
        "Renne's Father",                       # 25
        "Renne's Mother",                       # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Royal Guardsman',                      # 32
        'Royal Guardsman',                      # 33
        'Royal Guardsman',                      # 34
        'Soldier',                              # 35
        'Soldier',                              # 36
        'Soldier',                              # 37
        'Soldier',                              # 38
        'Soldier',                              # 39
        'Soldier',                              # 40
        'Soldier',                              # 41
        'Soldier',                              # 42
        'Soldier',                              # 43
        'Soldier',                              # 44
        'Special Ops Soldier',                  # 45
        'Special Ops Soldier',                  # 46
        'Special Ops Soldier',                  # 47
        "Orbal Tank 'Orgueille'",               # 48
        'Howitzer',                             # 49
        'Howitzer',                             # 50
        'Howitzer',                             # 51
        'Pater-Mater',                          # 52
        'Grancel - West Block',                 # 53
        'Grancel - N Warehouse District',       # 54
        'アタックドーベン',                     # 55
        'アタックドーベン',                     # 56
        'アタックドーベン',                     # 57
        'アタックドーベン',                     # 58
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
        'ED6_DT27/CH04512 ._CH',             # 00
        'ED6_DT27/CH03120 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00050 ._CH',             # 04
        'ED6_DT07/CH00030 ._CH',             # 05
        'ED6_DT07/CH00040 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT27/CH03090 ._CH',             # 09
        'ED6_DT26/CH20287 ._CH',             # 0A
        'ED6_DT27/CH03590 ._CH',             # 0B
        'ED6_DT07/CH02470 ._CH',             # 0C
        'ED6_DT07/CH02060 ._CH',             # 0D
        'ED6_DT26/CH20303 ._CH',             # 0E
        'ED6_DT26/CH20308 ._CH',             # 0F
        'ED6_DT07/CH01320 ._CH',             # 10
        'ED6_DT07/CH01650 ._CH',             # 11
        'ED6_DT07/CH00341 ._CH',             # 12
        'ED6_DT27/CH04586 ._CH',             # 13
        'ED6_DT27/CH04584 ._CH',             # 14
        'ED6_DT26/CH20309 ._CH',             # 15
        'ED6_DT27/CH04580 ._CH',             # 16
        'ED6_DT27/CH04120 ._CH',             # 17
        'ED6_DT07/CH00440 ._CH',             # 18
        'ED6_DT07/CH00341 ._CH',             # 19
        'ED6_DT07/CH00441 ._CH',             # 1A
        'ED6_DT27/CH04124 ._CH',             # 1B
        'ED6_DT06/CH20042 ._CH',             # 1C
        'ED6_DT26/CH20447 ._CH',             # 1D
        'ED6_DT09/CH10060 ._CH',             # 1E
        'ED6_DT09/CH10061 ._CH',             # 1F
        'ED6_DT27/CH04000 ._CH',             # 20
        'ED6_DT07/CH00150 ._CH',             # 21
        'ED6_DT07/CH00120 ._CH',             # 22
        'ED6_DT27/CH04080 ._CH',             # 23
        'ED6_DT26/CH20293 ._CH',             # 24
        'ED6_DT26/CH20294 ._CH',             # 25
        'ED6_DT26/CH20302 ._CH',             # 26
        'ED6_DT27/CH04001 ._CH',             # 27
        'ED6_DT07/CH00151 ._CH',             # 28
        'ED6_DT07/CH00121 ._CH',             # 29
        'ED6_DT27/CH04081 ._CH',             # 2A
        'ED6_DT27/CH04581 ._CH',             # 2B
        'ED6_DT27/CH04121 ._CH',             # 2C
        'ED6_DT26/CH20286 ._CH',             # 2D
        'ED6_DT27/CH04511 ._CH',             # 2E
        'ED6_DT27/CH04516 ._CH',             # 2F
        'ED6_DT07/CH00340 ._CH',             # 30
    )

    AddCharChipPat(
        'ED6_DT27/CH04512P._CP',             # 00
        'ED6_DT27/CH03120P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00050P._CP',             # 04
        'ED6_DT07/CH00030P._CP',             # 05
        'ED6_DT07/CH00040P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT27/CH03090P._CP',             # 09
        'ED6_DT26/CH20287P._CP',             # 0A
        'ED6_DT27/CH03590P._CP',             # 0B
        'ED6_DT07/CH02470P._CP',             # 0C
        'ED6_DT07/CH02060P._CP',             # 0D
        'ED6_DT26/CH20303P._CP',             # 0E
        'ED6_DT26/CH20308P._CP',             # 0F
        'ED6_DT07/CH01320P._CP',             # 10
        'ED6_DT07/CH01650P._CP',             # 11
        'ED6_DT07/CH00341P._CP',             # 12
        'ED6_DT27/CH04586P._CP',             # 13
        'ED6_DT27/CH04584P._CP',             # 14
        'ED6_DT26/CH20309P._CP',             # 15
        'ED6_DT27/CH04580P._CP',             # 16
        'ED6_DT27/CH04120P._CP',             # 17
        'ED6_DT07/CH00440P._CP',             # 18
        'ED6_DT07/CH00341P._CP',             # 19
        'ED6_DT07/CH00441P._CP',             # 1A
        'ED6_DT27/CH04124P._CP',             # 1B
        'ED6_DT06/CH20042P._CP',             # 1C
        'ED6_DT26/CH20447P._CP',             # 1D
        'ED6_DT09/CH10060P._CP',             # 1E
        'ED6_DT09/CH10061P._CP',             # 1F
        'ED6_DT27/CH04000P._CP',             # 20
        'ED6_DT07/CH00150P._CP',             # 21
        'ED6_DT07/CH00120P._CP',             # 22
        'ED6_DT27/CH04080P._CP',             # 23
        'ED6_DT26/CH20293P._CP',             # 24
        'ED6_DT26/CH20294P._CP',             # 25
        'ED6_DT26/CH20302P._CP',             # 26
        'ED6_DT27/CH04001P._CP',             # 27
        'ED6_DT07/CH00151P._CP',             # 28
        'ED6_DT07/CH00121P._CP',             # 29
        'ED6_DT27/CH04081P._CP',             # 2A
        'ED6_DT27/CH04581P._CP',             # 2B
        'ED6_DT27/CH04121P._CP',             # 2C
        'ED6_DT26/CH20286P._CP',             # 2D
        'ED6_DT27/CH04511P._CP',             # 2E
        'ED6_DT27/CH04516P._CP',             # 2F
        'ED6_DT07/CH00340P._CP',             # 30
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
        Unknown3            = 45,
        ChipIndex           = 0x2D,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        NpcIndex            = 0x189,
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
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 60310,
        Z                   = 0,
        Y                   = -1230,
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
        X                   = -9950,
        Z                   = 0,
        Y                   = 71270,
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
        X                   = 9400,
        Z                   = 0,
        Y                   = -1180,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15030,
        Z                   = 0,
        Y                   = -9320,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -11830,
        Z                   = 0,
        Y                   = 6760,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24660,
        Z                   = 0,
        Y                   = -820,
        Unknown_0C          = 180,
        Unknown_0E          = 30,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 27000,
        Y                   = -2000,
        Z                   = -11000,
        Range               = 29500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x251C,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -18200,
        Y                   = -2000,
        Z                   = 32700,
        Range               = -6000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x878C,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    ScpFunction(
        "Function_0_8A2",          # 00, 0
        "Function_1_8DF",          # 01, 1
        "Function_2_9A4",          # 02, 2
        "Function_3_9BA",          # 03, 3
        "Function_4_9CB",          # 04, 4
        "Function_5_D1A",          # 05, 5
        "Function_6_F3D",          # 06, 6
        "Function_7_F66",          # 07, 7
        "Function_8_F8F",          # 08, 8
        "Function_9_FB8",          # 09, 9
        "Function_10_FEE",         # 0A, 10
        "Function_11_1024",        # 0B, 11
        "Function_12_105A",        # 0C, 12
        "Function_13_1092",        # 0D, 13
        "Function_14_10CA",        # 0E, 14
        "Function_15_10F6",        # 0F, 15
        "Function_16_1389",        # 10, 16
        "Function_17_1396",        # 11, 17
        "Function_18_4137",        # 12, 18
        "Function_19_4283",        # 13, 19
        "Function_20_42C2",        # 14, 20
        "Function_21_4302",        # 15, 21
        "Function_22_43D3",        # 16, 22
        "Function_23_4C56",        # 17, 23
        "Function_24_8454",        # 18, 24
        "Function_25_848A",        # 19, 25
        "Function_26_84DF",        # 1A, 26
        "Function_27_853E",        # 1B, 27
        "Function_28_8593",        # 1C, 28
        "Function_29_85AF",        # 1D, 29
        "Function_30_85CB",        # 1E, 30
        "Function_31_8602",        # 1F, 31
        "Function_32_8639",        # 20, 32
        "Function_33_867C",        # 21, 33
        "Function_34_86BF",        # 22, 34
        "Function_35_86E2",        # 23, 35
        "Function_36_86F8",        # 24, 36
        "Function_37_8718",        # 25, 37
        "Function_38_873C",        # 26, 38
        "Function_39_87DC",        # 27, 39
        "Function_40_8802",        # 28, 40
        "Function_41_8828",        # 29, 41
        "Function_42_8853",        # 2A, 42
        "Function_43_887E",        # 2B, 43
        "Function_44_88A9",        # 2C, 44
        "Function_45_88D4",        # 2D, 45
        "Function_46_88FF",        # 2E, 46
        "Function_47_8920",        # 2F, 47
        "Function_48_894B",        # 30, 48
        "Function_49_8976",        # 31, 49
        "Function_50_89A1",        # 32, 50
        "Function_51_89CC",        # 33, 51
        "Function_52_89F7",        # 34, 52
        "Function_53_8A22",        # 35, 53
        "Function_54_8A4D",        # 36, 54
        "Function_55_8A78",        # 37, 55
        "Function_56_8AA3",        # 38, 56
        "Function_57_8ACE",        # 39, 57
        "Function_58_8AF9",        # 3A, 58
        "Function_59_8DFF",        # 3B, 59
        "Function_60_8E97",        # 3C, 60
    )


    def Function_0_8A2(): pass

    label("Function_0_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C2")
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_8DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_8DE")

    Return()

    # Function_0_8A2 end

    def Function_1_8DF(): pass

    label("Function_1_8DF")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_1C(0x2, 0x0, 0x3C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x45E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98E")
    OP_D2(0x2702EA, 0x2702F4, 0x31)
    OP_D2(0x2702EB, 0x2702F5, 0x32)
    OP_D2(0x702EF, 0x702F6, 0x33)
    OP_D2(0x70021, 0x70029, 0x35)
    OP_D2(0x70051, 0x70059, 0x36)
    OP_D2(0x70031, 0x70039, 0x37)
    OP_D2(0x70041, 0x70049, 0x38)
    OP_D2(0x70061, 0x70069, 0x39)
    OP_D2(0x70071, 0x70079, 0x3A)
    OP_D2(0x270091, 0x270095, 0x3B)

    label("loc_98E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x44E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A3")

    Return()

    # Function_1_8DF end

    def Function_2_9A4(): pass

    label("Function_2_9A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_9A4")

    label("loc_9B9")

    Return()

    # Function_2_9A4 end

    def Function_3_9BA(): pass

    label("Function_3_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_END)), "loc_9C2")
    Return()

    label("loc_9C2")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_9BA end

    def Function_4_9CB(): pass

    label("Function_4_9CB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E7")
    Call(0, 59)
    FadeToBright(0, 0)

    label("loc_9E7")

    Fade(1000)
    SetChrPos(0x101, 28170, 0, -970, 270)
    SetChrPos(0xF7, 28170, 0, 530, 270)
    SetChrPos(0x109, 29480, 0, -250, 270)
    OP_6D(28120, 0, -40, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(1850, 0)
    OP_6C(315000, 0)
    OP_6E(357, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7E")

    ChrTalk(    #0
        0x106,
        "#052FHell!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8C")

    label("loc_A7E")


    ChrTalk(    #1
        0x103,
        "#023FAh!\x02",
    )

    CloseMessageWindow()

    label("loc_A8C")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 8490, 0, -970, 90)
    SetChrPos(0x9, 8380, 0, 530, 90)
    SetChrPos(0xA, 6950, 0, -250, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_20(0x7D0)
    OP_6D(20000, 0, -550, 2000)
    OP_43(0x8, 0x1, 0x0, 0x6)
    Sleep(100)
    OP_43(0x9, 0x1, 0x0, 0x7)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x8)

    def lambda_B1E():
        OP_6D(25120, 0, 240, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1E)

    def lambda_B36():
        OP_67(0, 9180, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B36)

    def lambda_B4E():
        OP_6B(1990, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B4E)

    def lambda_B5E():
        OP_6E(385, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B5E)
    OP_1D(0x35)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xA, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB7")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_BC1")

    label("loc_BB7")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_BC1")

    OP_0D()
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x109,
        (
            "#1061F#2PAh, heeey, nice puppies...\x01",
            "Gooooood puppies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1005F#5PIntelligence Division attack dogs!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7F")

    ChrTalk(    #4
        0x106,
        "#054F#2PHere they come!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C9F")

    label("loc_C7F")


    ChrTalk(    #5
        0x103,
        "#024F#2PDefend yourselves!\x02",
    )

    CloseMessageWindow()

    label("loc_C9F")

    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(50)
    OP_43(0x9, 0x1, 0x0, 0xA)
    Sleep(50)
    OP_43(0xA, 0x1, 0x0, 0xB)

    def lambda_CC4():
        OP_6D(26990, 0, 1000, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CC4)

    def lambda_CDC():
        OP_6B(1600, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CDC)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    Battle(0x45B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_D14"),
        (SWITCH_DEFAULT, "loc_D19"),
    )


    label("loc_D14")

    OP_B4(0x0)
    Jump("loc_D19")

    label("loc_D19")

    Return()

    # Function_4_9CB end

    def Function_5_D1A(): pass

    label("Function_5_D1A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_6D(28240, 0, -280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 28170, 0, -970, 270)
    SetChrPos(0xF7, 28170, 0, 530, 270)
    SetChrPos(0x109, 29480, 0, -250, 270)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x109, 65535)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(100)
    OP_43(0xF7, 0x1, 0x0, 0xD)
    Sleep(100)
    OP_43(0x109, 0x1, 0x0, 0xE)
    WaitChrThread(0x109, 0x1)
    OP_0D()

    ChrTalk(    #6
        0x109,
        (
            "#1068FWellll, didn't expect we'd be visiting\x01",
            "the kennel club tonight.\x02\x03",

            "#1060FI think it's safe to say we've found\x01",
            "our 'tea party,' though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1002F#3PSeems like it! Now where are they...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(    #8
        0x106,
        "#050F#6PRight, let's keep an eye out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F1D")

    label("loc_EE6")


    ChrTalk(    #9
        0x103,
        "#022F#6PLet's proceed carefully and deliberately.\x02",
    )

    CloseMessageWindow()

    label("loc_F1D")

    OP_A2(0x163B)
    OP_28(0x8E, 0x1, 0x2)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_D1A end

    def Function_6_F3D(): pass

    label("Function_6_F3D")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5604, 0x0, 0xFFFFFC72, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_F3D end

    def Function_7_F66(): pass

    label("Function_7_F66")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x565E, 0x0, 0x398, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_F66 end

    def Function_8_F8F(): pass

    label("Function_8_F8F")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x50B4, 0x0, 0x1D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_F8F end

    def Function_9_FB8(): pass

    label("Function_9_FB8")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5D5C, 0x0, 0xFFFFFBFA, 0x1770, 0x0)
    OP_96(0xFE, 0x6B1C, 0x0, 0xFFFFFC22, 0x5DC, 0x1F40)
    Return()

    # Function_9_FB8 end

    def Function_10_FEE(): pass

    label("Function_10_FEE")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5D52, 0x0, 0x23A, 0x1770, 0x0)
    OP_96(0xFE, 0x6A72, 0x0, 0x1B8, 0x5DC, 0x1F40)
    Return()

    # Function_10_FEE end

    def Function_11_1024(): pass

    label("Function_11_1024")

    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x5870, 0x0, 0x0, 0x1770, 0x0)
    OP_96(0xFE, 0x6568, 0x0, 0xFFFFFFCE, 0x5DC, 0x1F40)
    Return()

    # Function_11_1024 end

    def Function_12_105A(): pass

    label("Function_12_105A")

    OP_8C(0xFE, 315, 400)
    Sleep(1000)
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 315, 400)
    Sleep(1000)
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_105A end

    def Function_13_1092(): pass

    label("Function_13_1092")

    OP_8C(0xFE, 360, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 360, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_13_1092 end

    def Function_14_10CA(): pass

    label("Function_14_10CA")

    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_14_10CA end

    def Function_15_10F6(): pass

    label("Function_15_10F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1388")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1247")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B4")

    ChrTalk(    #10
        0x106,
        "#052FHold up, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 400)

    ChrTalk(    #11
        0x106,
        (
            "#552FI can hear people inside\x01",
            "this building.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #12
        0x101,
        (
            "#1002FYou're right...\x01",
            "I guess we should check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1244")

    label("loc_11B4")


    ChrTalk(    #13
        0x103,
        "#023FWait, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #14
        0x103,
        (
            "#022FI hear people inside\x01",
            "this building.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #15
        0x101,
        (
            "#1002FYou're right...\x01",
            "I guess we should check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1244")

    Jump("loc_136D")

    label("loc_1247")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E0")

    ChrTalk(    #16
        0x101,
        "#1004FWait a sec!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1002FI can hear people inside\x01",
            "this building.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 400)

    ChrTalk(    #18
        0x106,
        (
            "#552FHmm... \x01",
            "Guess we better check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136D")

    label("loc_12E0")


    ChrTalk(    #19
        0x101,
        "#1004FWait a sec!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #20
        0x101,
        (
            "#1002FI can hear people inside\x01",
            "this building.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #21
        0x103,
        (
            "#022FMy, my... \x01",
            "I guess we should check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1388")

    Return()

    # Function_15_10F6 end

    def Function_16_1389(): pass

    label("Function_16_1389")

    Call(0, 17)
    Call(0, 22)
    Call(0, 23)
    Return()

    # Function_16_1389 end

    def Function_17_1396(): pass

    label("Function_17_1396")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B4")
    Call(0, 59)

    label("loc_13B4")

    AddParty(0xE, 0xF9, 0xFF)
    LoadEffect(0x0, "monster\\ms30600d.eff")
    LoadEffect(0x1, "monster\\ms30600b.eff")
    LoadEffect(0x2, "monster\\ms30600a.eff")
    LoadEffect(0x3, "battle\\\\btbomb00.eff")
    PlayEffect(0x0, 0x1, 0x2F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x2F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x2F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x2F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x2F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x2F, 0x80)
    OP_72(0x5, 0x4)
    OP_A1(0x2F, 0x5)
    SetChrPos(0x2F, -11220, 0, 51980, 180)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xB, -12500, 2000, 51890, 180)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_A1(0x30, 0x0)
    OP_A1(0x31, 0x1)
    OP_A1(0x32, 0x3)
    SetChrPos(0x30, 1540, 0, 3700, 90)
    SetChrPos(0x31, 1190, 0, -2000, 90)
    SetChrPos(0x32, -1450, 0, 8080, 45)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    OP_89(0x1A, 1540, 750, 3700, 270)
    OP_89(0x1B, 1190, 750, -2000, 270)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x10F, 4290, 0, 380, 270)
    SetChrPos(0x1C, 5510, 0, -1750, 270)
    SetChrPos(0x1D, 5700, 0, 520, 270)
    SetChrPos(0x1E, 5710, 0, -3450, 270)
    SetChrPos(0x1F, 5630, 0, 1960, 270)
    SetChrPos(0x20, 7090, 0, -1780, 270)
    SetChrPos(0x21, 7090, 0, -120, 270)

    def lambda_16F3():

        label("loc_16F3")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_16F3")

    QueueWorkItem2(0x2F, 3, lambda_16F3)
    OP_22(0x10F, 0x0, 0x64)
    OP_22(0x110, 0x0, 0x64)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    OP_6D(-11130, 0, 7550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)

    def lambda_1769():

        label("loc_1769")

        OP_69(0x2F, 0x0)
        OP_48()
        Jump("loc_1769")

    QueueWorkItem2(0x2F, 2, lambda_1769)
    FadeToBright(2000, 0)

    def lambda_1783():
        OP_8F(0xFE, 0xFFFFD42C, 0x0, 0xC94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_1783)

    def lambda_179E():
        OP_8F(0xFE, 0xFFFFCF2C, 0x7D0, 0x9D1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_179E)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 371)
    OP_70(0x5, 0x186)
    OP_73(0x5)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)

    def lambda_17E8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_17E8)

    def lambda_17FA():
        OP_8F(0xFE, 0xFFFFCF2C, 0x8FC, 0xC94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17FA)
    Sleep(2000)

    def lambda_181A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_181A)
    WaitChrThread(0xB, 0x2)

    ChrTalk(    #22 op#A op#5
        0xB,
        (
            "#1181F#6P#30AExcellent.\x01",
            "We've managed to give them the\x01",
            "slip.\x02\x03",

            "#1181F#6P#38ANow, if we can just capture\x01",
            "Grancel Castle and the queen--\x05\x02",
        )
    )

    Sleep(7700)
    PlayEffect(0x3, 0xFF, 0xFF, -11910, 0, -720, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x3E4CCCCD, 0xC8, 0x7D0, 0x64)
    Sleep(300)
    PlayEffect(0x3, 0xFF, 0xFF, -9980, 0, -1310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x3E4CCCCD, 0xC8, 0x7D0, 0x64)
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x2F, 0x1)
    OP_23(0x110)
    OP_44(0x2F, 0x3)
    OP_44(0xB, 0x1)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_20(0x0)
    Sleep(1000)

    def lambda_198A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_198A)
    WaitChrThread(0xB, 0x2)
    OP_DC()

    ChrTalk(    #23
        0xB,
        "#1185F#6PWhat?!\x02",
    )

    CloseMessageWindow()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xA)
    OP_73(0x3)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xA)
    OP_73(0x4)

    NpcTalk(    #24
        0x10F,
        "Woman's Voice",
        "Looks like I made it in time, then.\x02",
    )

    CloseMessageWindow()
    OP_44(0x2F, 0x2)
    OP_1D(0x74)
    Sleep(500)

    def lambda_1A17():
        OP_6D(-6040, 0, 4270, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A17)

    def lambda_1A2F():
        OP_67(0, 4190, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A2F)

    def lambda_1A47():
        OP_6B(9600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A47)

    def lambda_1A57():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A57)

    def lambda_1A67():
        OP_6E(156, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A67)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    Sleep(500)

    ChrTalk(    #25
        0xB,
        (
            "#1185FThe Royal Guard!\x02\x03",

            "And...I knew it! JULIA SCHWARZ!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        (
            "#176F#2PIt's been a while...'Captain' Amalthea.\x02\x03",

            "#178FI wouldn't have imagined we'd be facing\x01",
            "one another down in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "#1185FHow... Why are you here?!\x02\x03",

            "Weren't you training at Leiston Fortress?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        (
            "#170F#2PWe received an emergency aid\x01",
            "request from Lieutenant Colonel Cid.\x02\x03",

            "He seemed a bit concerned that\x01",
            "someone was going to cause trouble\x01",
            "in Grancel. Imagine that.\x02\x03",

            "So we came flying, as it were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "#1187FHmph. And I thought he was as useful\x01",
            "as a broken watch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10F,
        (
            "#170F#2PLieutentant Colonel Cid is from Brigadier General Bright's\x01",
            "former squad--the same as the former\x01",
            "Colonel Richard.\x02\x03",

            "It's your mistake for underestimating him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#1183FIt seems it was.\x02\x03",

            "#1180FSo, gentlemen.\x01",
            "What do you think you're doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10F,
        "#173F#2PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        (
            "#1181FUnless I'm mistaken, those are the orbal\x01",
            "cannons from the Arseille, yes?\x02\x03",

            "Do you really intend to fight the Orgueille\x01",
            "with those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        (
            "#178F#2PFight to defeat you...perhaps not.\x01",
            "But we can certainly slow you down.\x02\x03",

            "The colonel's battalion will be arriving\x01",
            "momentarily.\x02\x03",

            "Surrender now, for the sake of your men,\x01",
            "if not your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        "#1181FHahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #36
        0xB,
        "#1188F#3SHahahahaha!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#178F#2PJust WHAT is so funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "#1320FOh, Julia, you really haven't changed a bit.\x02\x03",

            "Straight as an arrow, cold as midwinter,\x01",
            "not a hint of fear. Just like at school...\x02\x03",

            "I know we fought like cats at basically\x01",
            "every opportunity, but...\x02\x03",

            "I always admired you on some level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#175F#2PI...could say many of the same things\x01",
            "about you...Kanone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "#1183FHowever.\x02\x03",

            "#1182FIf you intend to stand in the way\x01",
            "of my rescue of Colonel Richard,\x01",
            "I will show you no mercy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        "#173F#2P*gasp*\x02",
    )

    CloseMessageWindow()
    OP_22(0xE6, 0x0, 0x64)
    OP_8F(0xB, 0xFFFFCF2C, 0x7D0, 0xC94, 0xFA0, 0x0)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 391)
    OP_70(0x5, 0x19A)
    OP_73(0x5)
    SetChrFlags(0xB, 0x80)
    OP_B0(0x5, 0x5)
    OP_6F(0x5, 251)
    OP_70(0x5, 0x104)
    OP_22(0x111, 0x0, 0x64)

    ChrTalk(    #42
        0x10F,
        (
            "#176F#2PSo be it.\x02\x03",

            "#172FCannons one and two! Prepare to fire!\x01",
            "We are stopping them here!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("Soldiers")

    AnonymousTalk(    #43
        "\x07\x00#3SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    LoadEffect(0x3, "map\\\\mp063_00.eff")
    LoadEffect(0x4, "map\\\\mp015_00.eff")
    LoadEffect(0x5, "map\\\\mp007_00.eff")
    LoadEffect(0x7, "map\\\\mp007_01.eff")
    PlayEffect(0x3, 0x2, 0xFF, -2070, 1500, 3480, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x355, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x3, 0x7, 0xFF, -2420, 1500, -2230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x355, 0x0, 0x64)
    OP_B0(0x5, 0x5)
    OP_6F(0x5, 261)
    OP_70(0x5, 0x108)
    OP_73(0x5)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 264)
    OP_70(0x5, 0x10C)
    OP_73(0x5)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 268)
    OP_70(0x5, 0x10E)
    OP_73(0x5)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 411)
    OP_70(0x5, 0x1AE)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 19)
    SetChrSubChip(0x10F, 0)
    Sleep(500)
    OP_99(0x10F, 0x0, 0x1, 0x5DC)

    ChrTalk(    #44
        0x10F,
        "#177F#2P#3SFIRE!\x02",
    )

    CloseMessageWindow()
    OP_20(0x0)
    Play3DEffect(0x5, 0x0, 0x5, "Frame68__gospel__1_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_22(0x90, 0x0, 0x64)
    Play3DEffect(0x7, 0x1, 0x5, "Frame68__gospel__1_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    OP_22(0x91, 0x0, 0x64)

    def lambda_241A():
        OP_67(0, 6190, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_241A)

    def lambda_2432():
        OP_6B(12600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2432)
    PlayEffect(0x4, 0xFF, 0xFF, -11100, 2650, 2870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_23(0x10F)
    OP_1D(0x5C)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    OP_82(0x6, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x7, 0x2)
    OP_7B()
    Sleep(150)
    OP_79(0x2, 0x2)
    OP_7B()
    Sleep(150)
    OP_79(0x3, 0x2)
    OP_7B()
    Sleep(100)
    OP_6F(0x3, 0)
    OP_7B()
    Sleep(150)
    OP_6F(0x4, 0)
    OP_7B()
    Sleep(150)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(100)
    OP_79(0x5, 0x2)
    OP_7B()
    Sleep(250)
    OP_6F(0x0, 1)
    OP_7B()
    Sleep(150)
    OP_6F(0x1, 1)
    OP_7B()
    Sleep(200)
    OP_79(0xC, 0x2)
    OP_7B()
    Sleep(100)
    OP_79(0xD, 0x2)
    OP_7B()
    Sleep(150)
    OP_79(0x1, 0x2)
    OP_79(0x0, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    Fade(500)
    OP_7B()
    OP_0D()
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    Sleep(500)

    ChrTalk(    #45
        0x10F,
        "#173F#2PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1A,
        (
            "#2PNo good, ma'am!\x01",
            "The cannons are inoperable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        (
            "#177F#2PThe Orbal Shutdown Phenomenon!\x01",
            "Blast it!\x02\x03",

            "But that will mean their tank is--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x10F, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x2F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0x4, 0x2F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x5, 0x2F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x6, 0x2F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_26ED():

        label("loc_26ED")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_26ED")

    QueueWorkItem2(0x2F, 3, lambda_26ED)
    PlayEffect(0x0, 0x1, 0x2F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x5, 0xF)
    Sleep(300)
    OP_22(0x110, 0x0, 0x64)
    OP_8C(0x2F, 90, 50)
    OP_23(0x110)
    OP_44(0x2F, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    ChrTalk(    #48
        0x10F,
        "#173F#2PWHAT?! How is it still moving?!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    LoadEffect(0x3, "scraft\\sc003_12.eff")
    LoadEffect(0x4, "battle\\btbomb00.eff")
    OP_0D()

    def lambda_27F3():
        OP_67(0, 4190, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27F3)

    def lambda_280B():
        OP_6B(9600, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_280B)
    StopSound(0x186A0, 0x2BF20, 0x1770)
    OP_43(0x2F, 0x1, 0x0, 0x12)
    WaitChrThread(0x2F, 0x1)
    LoadEffect(0x3, "monster\\ms30602a.eff")
    LoadEffect(0x4, "monster\\ms30602b.eff")
    OP_72(0x5, 0x20)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 121)
    OP_70(0x5, 0x91)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0x5)
    OP_22(0x3E0, 0x0, 0x64)
    OP_73(0x1)
    Sleep(200)
    Sleep(300)
    Sleep(500)
    PlayEffect(0x3, 0xFF, 0x2F, 0, 2200, 3500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_28CD():
        OP_8F(0xFE, 0xFFFFD044, 0x0, 0xC94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_28CD)
    OP_6F(0x5, 161)
    OP_70(0x5, 0xBE)
    OP_22(0x3E1, 0x0, 0x64)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0xBB8, 0xBB8, 0x1388, 0xC8)
    PlayEffect(0x4, 0xFF, 0xFF, 290, 0, 3540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_6F(0x0, 2)
    OP_70(0x0, 0x3C)
    Sleep(50)

    def lambda_295E():
        OP_96(0x1A, 0x852, 0x0, 0x1900, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_295E)
    SetChrChipByIndex(0x1A, 21)
    SetChrSubChip(0x1A, 3)
    WaitChrThread(0x1A, 0x1)
    SetChrFlags(0x1A, 0x2)
    SetChrChipByIndex(0x1A, 29)
    SetChrSubChip(0x1A, 0)
    OP_73(0x0)
    Sleep(200)
    OP_73(0x1)
    Sleep(200)

    ChrTalk(    #49
        0x10F,
        "#177F#2PWha...!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x3, "monster\\msc0311.eff")
    LoadEffect(0x4, "map\\\\mp003_00.eff")
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 191)
    OP_70(0x5, 0xD2)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0x5)
    OP_6F(0x5, 101)
    OP_70(0x5, 0x78)
    OP_73(0x5)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x3, 0x7, 0x2F, 500, 3000, 2300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 4019, 0, -1270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 6310, 0, 580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 6820, 0, 1440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    ChrTalk(    #50 op#A op#5
        0x1F,
        "#10A#2PWhoa!\x05\x02",
    )

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 7720, 0, -1790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 4030, 0, 1650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 7690, 0, 210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 5160, 0, -4490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x4, 0xFF, 0xFF, 6820, 0, -3850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x7, 0x0)
    SetChrChipByIndex(0x10F, 20)
    SetChrChipByIndex(0x1C, 21)
    SetChrChipByIndex(0x1D, 21)
    SetChrChipByIndex(0x1E, 21)
    SetChrChipByIndex(0x1F, 21)
    SetChrChipByIndex(0x20, 21)
    SetChrChipByIndex(0x21, 21)
    SetChrSubChip(0x10F, 0)
    SetChrSubChip(0x1C, 0)
    SetChrSubChip(0x1D, 0)
    SetChrSubChip(0x1E, 0)
    SetChrSubChip(0x1F, 0)
    SetChrSubChip(0x20, 0)
    SetChrSubChip(0x21, 0)

    def lambda_2CBD():
        OP_99(0x1E, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2CBD)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(50)

    def lambda_2CD7():
        OP_99(0x1F, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2CD7)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(100)

    def lambda_2CF1():
        OP_99(0x1C, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2CF1)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(50)

    def lambda_2D0B():
        OP_99(0x20, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2D0B)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(50)

    def lambda_2D25():
        OP_99(0x1D, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2D25)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(100)

    def lambda_2D3F():
        OP_99(0x21, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2D3F)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(200)

    def lambda_2D59():
        OP_99(0x10F, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2D59)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 271)
    OP_70(0x5, 0x122)
    OP_73(0x5)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -12290, 2000, 1850, 90)
    ClearChrFlags(0xB, 0x80)

    def lambda_2DAE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2DAE)
    OP_8F(0xB, 0xFFFFCFFE, 0x9C4, 0x73A, 0x7D0, 0x0)
    Sleep(1000)

    ChrTalk(    #51
        0xB,
        (
            "#1181F#6PA unit capable of stopping all local orbal\x01",
            "devices dead, and yet remains fully\x01",
            "functional itself.\x02\x03",

            "Oh, my goodness, this is even better than\x01",
            "I'd imagined... We're truly unstoppable\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        (
            "#175F#2PDamn it, Kanone!\x02\x03",

            "Where on earth did you get a Gospel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        (
            "#1181F#6PHeh. Let's just say a concerned citizen\x01",
            "donated it to the cause.\x02\x03",

            "All I have to do in return is agree to help\x01",
            "with an 'experiment' of some sort.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-11440, 0, 35260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    ClearMapFlags(0x10)
    SetChrPos(0x101, -11270, 0, 40480, 180)
    SetChrPos(0xF7, -10400, 0, 41140, 180)
    SetChrPos(0x109, -12300, 0, 41220, 180)

    def lambda_3009():
        OP_8E(0xFE, 0xFFFFD42C, 0x0, 0x8598, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3009)
    Sleep(100)

    def lambda_3029():
        OP_8E(0xFE, 0xFFFFD760, 0x0, 0x8944, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3029)
    Sleep(100)

    def lambda_3049():
        OP_8E(0xFE, 0xFFFFCFF4, 0x0, 0x8994, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3049)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3096")

    ChrTalk(    #54
        0x106,
        "#055F#4PWhat the HELL?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BB")

    label("loc_3096")


    ChrTalk(    #55
        0x103,
        "#023F#4PWHAT in the name of...?\x02",
    )

    CloseMessageWindow()

    label("loc_30BB")


    ChrTalk(    #56
        0x101,
        (
            "#1020F#6POuroboros' Gospel experiment...!\x02\x03",

            "Oh, man, I did NOT expect it to turn out\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x109,
        (
            "#1067F#6PErgh. This is bad.\x02\x03",

            "We can't use arts or anything orbal while\x01",
            "that thing is lumberin' around.\x02\x03",

            "#1065FTime to use my trump card, I think.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 400)
    Sleep(100)
    TurnDirection(0xF7, 0x109, 400)

    ChrTalk(    #58
        0x101,
        "#1004F#6PWhat d'you--\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3376")

    ChrTalk(    #59
        0x109,
        (
            "#1063F#6PEstelle, Agate.\x02\x03",

            "If what I'm about to do succeeds, it'll\x01",
            "stop that Gospel for a short time.\x01",
            "I think. Maybe.\x02\x03",

            "I need you to use the chance to disable\x01",
            "that tank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x106,
        "#052FWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1002F#6PWait, you can DO that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x109,
        (
            "#1066F#6PI give it about even odds of either working or,\x01",
            "uh, gettin' us all killed. Messily.\x02\x03",

            "So a couple of prayers from you two wouldn't\x01",
            "hurt, yeah?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3505")

    label("loc_3376")


    ChrTalk(    #63
        0x109,
        (
            "#1063F#6PEstelle, Schera.\x02\x03",

            "If what I'm about to do succeeds, it'll\x01",
            "stop that Gospel for a short time.\x01",
            "I think. Maybe.\x02\x03",

            "I need you to use the chance to disable\x01",
            "that tank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x103,
        "#023FYou must be joking!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1002F#6PWait, you can DO that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        (
            "#1066F#6PI give it about even odds of either working or,\x01",
            "uh, gettin' us all killed. Messily.\x02\x03",

            "So a couple of prayers from you two wouldn't\x01",
            "hurt, yeah?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3505")

    Sleep(250)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 36)
    SetChrSubChip(0x109, 8)
    OP_0D()
    Sleep(500)

    def lambda_3525():
        OP_6D(-12300, 0, 35220, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3525)

    def lambda_353D():
        OP_6E(246, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_353D)
    OP_99(0x109, 0x8, 0xB, 0x5DC)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x109, 0x2000)
    OP_D7(0x1, 15000, 265)
    OP_99(0x109, 0xB, 0xF, 0x5DC)
    OP_43(0x109, 0x0, 0x0, 0x23)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        "#1004F#6PWait... That's the...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        (
            "#1065FYep. The 'Chronos Rod.'\x02\x03",

            "#1063FMayor Dalmore's forbidden artifact!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_360C():

        label("loc_360C")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_360C")

    QueueWorkItem2(0x101, 3, lambda_360C)

    def lambda_361D():

        label("loc_361D")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_361D")

    QueueWorkItem2(0xF7, 1, lambda_361D)

    def lambda_362E():
        OP_6D(-13800, 0, 3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_362E)

    def lambda_3646():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3646)

    def lambda_365E():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_365E)

    def lambda_366E():
        OP_6C(200000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_366E)

    def lambda_367E():
        OP_6E(402, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_367E)
    OP_44(0x109, 0x0)
    ClearChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 37)
    SetChrSubChip(0x109, 0)
    OP_8E(0x109, 0xFFFFD3FA, 0x0, 0x2C7E, 0x1770, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_36C3():
        OP_6D(-14370, 0, -1260, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36C3)

    def lambda_36DB():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_36DB)

    ChrTalk(    #69 op#A op#5
        0x109,
        "#1069F#5P#3S#8AHere we goooooooo!\x05\x02",
    )

    OP_8E(0x109, 0xFFFFD120, 0x0, 0x2328, 0x1770, 0x0)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x40)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 36)
    SetChrSubChip(0x109, 24)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3749():
        OP_96(0x109, 0xFFFFCE00, 0xDAC, 0x1770, 0xFA0, 0x1770)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3749)
    OP_56(0x0)
    OP_99(0x109, 0x19, 0x1C, 0x5DC)
    OP_22(0xEE, 0x0, 0x64)
    LoadEffect(0x3, "Scraft\\\\sc008_02.eff")
    OP_20(0x0)
    OP_23(0x10F)
    OP_23(0x90)
    PlayEffect(0x3, 0xFF, 0xFF, -12000, 4600, 5930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_82(0x0, 0x2)
    FadeToDark(2000, 16777215, -1)

    ChrTalk(    #70 op#A op#5
        0xB,
        "#1189F#6P#10AWAAAAAAH!\x05\x02",
    )


    def lambda_37FC():
        OP_96(0x109, 0xFFFFCE00, 0x0, 0x1E50, 0xC8, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_37FC)
    OP_99(0x109, 0x1D, 0x20, 0x2EE)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x3)
    SetChrPos(0x10F, -3000, 0, 1690, 270)
    ClearChrFlags(0x109, 0x4)
    SetChrPos(0x109, -11320, 0, 9220, 180)
    ClearChrFlags(0x109, 0x2)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 65535)
    OP_6D(-11790, 0, 4700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(224000, 0)
    OP_6E(402, 0)
    OP_8C(0x109, 180, 0)
    OP_8C(0x10F, 270, 0)
    CloseMessageWindow()
    OP_7A(0xFF, 0x2)
    OP_7B()
    ClearChrFlags(0x109, 0x2000)
    OP_6F(0x3, 10)
    OP_6F(0x4, 10)
    SetMapFlags(0x10)
    Sleep(2000)
    FadeToBright(3000, 16777215)
    OP_D7(0x0, 0, 0)
    LoadEffect(0x3, "Scraft\\\\sc000_31.eff")
    PlayEffect(0x3, 0x7, 0xFF, -11960, 4500, 5930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x10F, 0x0, 0x0, 0x14)
    Sleep(3000)
    OP_82(0x7, 0x0)
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #71
        0x10F,
        (
            "#173F#5PThe lights are back on...\x02\x03",

            "The suppression effect has ended! How...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #72
        0xB,
        (
            "#1185F#6PHow is this...?\x02\x03",

            "What did you do, priest?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #73
        0x109,
        (
            "#1066FHeheh! Nothin' too special.\x02\x03",

            "When you break an artifact, there tends\x01",
            "to be a massive release of orbal energy.\x02\x03",

            "Looks like even the Gospel can't quite\x01",
            "handle eating all that power at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xB,
        "#1187F#6PYou madman!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -12110, 0, 16900, 180)
    SetChrPos(0xF7, -9990, 0, 16900, 180)

    def lambda_3B07():
        OP_8E(0xFE, 0xFFFFD0B2, 0x0, 0x2940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B07)
    Sleep(100)

    def lambda_3B27():
        OP_8E(0xFE, 0xFFFFD8FA, 0x0, 0x2940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3B27)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #75
        0x101,
        "#1018F#2PWay to go, Kevin!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B95")

    ChrTalk(    #76
        0x106,
        "#051F#2PNot bad, priest!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BB5")

    label("loc_3B95")


    ChrTalk(    #77
        0x103,
        "#021F#2PWell done, Father!\x02",
    )

    CloseMessageWindow()

    label("loc_3BB5")


    ChrTalk(    #78
        0x109,
        (
            "#1071F#2PHeeey, don't give me TOO much credit\x01",
            "or you'll make me blush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xB,
        (
            "#1187F#6PTch! SILENCE! So what?!\x02\x03",

            "I don't need the full power of the Gospel\x01",
            "to crush you!\x02\x03",

            "#1186FWitness the Orgueille's fury!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x29)
    Sleep(500)
    OP_8F(0xB, 0xFFFFCFFE, 0x7D0, 0x73A, 0x7D0, 0x0)

    def lambda_3CA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3CA7)
    OP_22(0xE6, 0x0, 0x64)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 331)
    OP_70(0x5, 0x15E)
    OP_73(0x5)
    SetChrFlags(0xB, 0x80)

    def lambda_3CD8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3CD8)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D22")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_3D2C")

    label("loc_3D22")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_3D2C")

    OP_0D()
    OP_22(0x10F, 0x0, 0x64)
    OP_43(0x2F, 0x0, 0x0, 0x15)
    OP_8C(0x109, 90, 400)
    OP_6D(-9950, 0, 4770, 1500)

    ChrTalk(    #80
        0x109,
        (
            "#1069F#2PYo, Captain Schwarz!\x02\x03",

            "Making the Gospel freak out should've\x01",
            "made that tank weaker, too!\x02\x03",

            "If you want to bring that monster down,\x01",
            "now's your chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        "#178F#5PI see... Right!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)

    ChrTalk(    #82
        0x101,
        "#1006F#2PJulia, c'mon!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E8E")

    ChrTalk(    #83
        0x106,
        (
            "#051F#2PLet's see some of that swordsmanship the\x01",
            "old man taught you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EDA")

    label("loc_3E8E")


    ChrTalk(    #84
        0x103,
        (
            "#526F#2PGive us a little bit of that swordsmanship\x01",
            "Cassius taught you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EDA")


    ChrTalk(    #85
        0x10F,
        "#171F#5PIndeed! ATTACK!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2F, 0x0)
    Fade(250)
    PlayEffect(0x1, 0x3, 0x2F, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x2F, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x2F, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x2F, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(250)

    def lambda_3FE1():
        OP_6D(-11160, 0, 3600, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FE1)

    def lambda_3FF9():
        OP_6B(2000, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FF9)
    SetChrFlags(0x10F, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0xF7, 0x1000)
    SetChrChipByIndex(0x10F, 43)

    def lambda_4022():
        OP_8F(0xFE, 0xFFFFDBA2, 0x0, 0x55A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_4022)
    Sleep(50)
    SetChrChipByIndex(0x109, 42)

    def lambda_4047():
        OP_8F(0xFE, 0xFFFFCEA0, 0x0, 0x1284, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4047)
    Sleep(50)
    SetChrChipByIndex(0x101, 39)

    def lambda_406C():
        OP_8F(0xFE, 0xFFFFCBDA, 0x0, 0x15FE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_406C)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_409C")
    SetChrChipByIndex(0x106, 40)
    Jump("loc_40A1")

    label("loc_409C")

    SetChrChipByIndex(0x103, 41)

    label("loc_40A1")


    def lambda_40A7():
        OP_8F(0xFE, 0xFFFFD396, 0x0, 0x164E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_40A7)
    Sleep(400)
    OP_31(0xE, 0x0, 0x3B)
    OP_31(0xE, 0x3, 0xFA)
    OP_31(0xE, 0x5, 0x6E)
    OP_31(0xE, 0xFE, 0x0)
    OP_41(0xE, 0x82, 0xFF)
    OP_41(0xE, 0x101, 0xFF)
    OP_41(0xE, 0x122, 0xFF)
    OP_35(0xE, 0x0)
    OP_37(0xE, 0x0)
    OP_37(0xE, 0x1)
    OP_37(0xE, 0x2)
    OP_37(0xE, 0x3)
    OP_37(0xE, 0x4)
    OP_37(0xE, 0x5)
    OP_34(0xE, 0x6F)
    OP_34(0xE, 0x73)
    OP_34(0xE, 0x39)
    OP_34(0xE, 0x46)
    OP_34(0xE, 0x47)
    OP_34(0xE, 0x11)
    OP_BB(0xE, 0x6, 0x11A)
    OP_44(0x101, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0x10F, 0xFF)
    OP_44(0xF7, 0xFF)
    Battle(0x44E, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_17_1396 end

    def Function_18_4137(): pass

    label("Function_18_4137")

    PlayEffect(0x3, 0x1, 0xFF, -9700, 1500, 1670, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0x2, 0xFF, -9700, 1500, 1000, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0xFF, 0xFF, -800, 250, -1940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x0)
    OP_6F(0x1, 2)
    OP_70(0x1, 0xA)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFF, -800, 250, -1940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x2, 0x0)
    Sleep(100)
    OP_6F(0x1, 11)
    OP_70(0x1, 0x3C)

    def lambda_4247():
        OP_96(0x1B, 0x5B4, 0x0, 0xFFFFE7DC, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4247)
    SetChrChipByIndex(0x1B, 21)
    SetChrSubChip(0x1B, 3)
    Sleep(100)
    WaitChrThread(0x1B, 0x1)
    SetChrFlags(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 29)
    SetChrSubChip(0x1B, 1)
    Return()

    # Function_18_4137 end

    def Function_19_4283(): pass

    label("Function_19_4283")


    def lambda_4289():

        label("loc_4289")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_4289")

    QueueWorkItem2(0xFE, 3, lambda_4289)
    Sleep(500)
    OP_99(0xFE, 0x3, 0x0, 0x3E8)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Sleep(500)
    Return()

    # Function_19_4283 end

    def Function_20_42C2(): pass

    label("Function_20_42C2")

    SetChrChipByIndex(0xFE, 43)
    OP_8E(0xFE, 0xFFFFEC78, 0x0, 0x69A, 0x3E8, 0x0)
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    OP_8C(0x10F, 0, 400)
    Sleep(500)
    OP_8C(0x10F, 270, 400)
    Sleep(500)
    Return()

    # Function_20_42C2 end

    def Function_21_4302(): pass

    label("Function_21_4302")


    def lambda_4308():

        label("loc_4308")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_4308")

    QueueWorkItem2(0x2F, 3, lambda_4308)
    OP_22(0x110, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x2F, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2F, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x2F, 45, 20)
    Sleep(500)
    OP_8F(0x2F, 0xFFFFCDA6, 0x0, 0xA28, 0x3E8, 0x0)
    Sleep(500)
    OP_8F(0x2F, 0xFFFFC5FE, 0x0, 0x4B0, 0x3E8, 0x0)
    OP_23(0x110)
    OP_44(0x2F, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Return()

    # Function_21_4302 end

    def Function_22_43D3(): pass

    label("Function_22_43D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x10F)
    AddParty(0xE, 0xF9, 0xFF)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    ClearChrFlags(0x2F, 0x80)
    OP_72(0x5, 0x4)
    SetChrPos(0x2F, -14380, 0, -8330, 0)
    OP_A1(0x2F, 0x5)
    OP_6F(0x5, 311)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -13200, 3500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 2000, 600, 3460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 1220, 600, -2270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, -14540, 0, -1200, 180)
    SetChrPos(0x10F, -12870, 0, -1230, 180)
    SetChrPos(0xF7, -14350, 0, 570, 180)
    SetChrPos(0x109, -12660, 0, 750, 180)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4547")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_4551")

    label("loc_4547")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_4551")

    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0x30, 0x0)
    OP_A1(0x31, 0x1)
    SetChrPos(0x30, 1540, 0, 3700, 90)
    SetChrPos(0x31, 1190, 0, -2000, 90)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x3, 10)
    OP_6F(0x4, 10)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1A, 2130, 0, 6400, 270)
    SetChrPos(0x1B, 1460, 0, -6180, 270)
    SetChrPos(0x1C, 5510, 0, -1750, 270)
    SetChrPos(0x1D, 5700, 0, 520, 270)
    SetChrPos(0x1E, 5710, 0, -3450, 270)
    SetChrPos(0x1F, 5630, 0, 1960, 270)
    SetChrPos(0x20, 7090, 0, -1780, 270)
    SetChrPos(0x21, 7090, 0, -120, 270)
    SetChrChipByIndex(0x1A, 21)
    SetChrChipByIndex(0x1B, 21)
    SetChrChipByIndex(0x1C, 21)
    SetChrChipByIndex(0x1D, 21)
    SetChrChipByIndex(0x1E, 21)
    SetChrChipByIndex(0x1F, 21)
    SetChrChipByIndex(0x20, 21)
    SetChrChipByIndex(0x21, 21)
    SetChrSubChip(0x1A, 3)
    SetChrSubChip(0x1B, 3)
    SetChrSubChip(0x1C, 3)
    SetChrSubChip(0x1D, 3)
    SetChrSubChip(0x1E, 3)
    SetChrSubChip(0x1F, 3)
    SetChrSubChip(0x20, 3)
    SetChrSubChip(0x21, 3)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    OP_6D(-15120, 0, -4350, 0)
    OP_67(0, 6960, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(224000, 0)
    OP_6E(422, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #86
        0x101,
        "#1018F#2PWe did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10F,
        "#171F#2PYes, we did. It's wholly inoperable.\x02",
    )

    CloseMessageWindow()

    def lambda_476D():
        OP_6D(-15080, 0, -6490, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_476D)

    def lambda_4785():
        OP_67(0, 8370, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4785)

    def lambda_479D():
        OP_6B(2250, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_479D)
    OP_22(0x6A, 0x0, 0x64)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 311)
    OP_70(0x5, 0x14A)
    OP_73(0x5)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, -13000, 2000, -8200, 0)
    SetChrFlags(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)

    def lambda_47F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_47F7)
    OP_8F(0xB, 0xFFFFCD38, 0x9C4, 0xFFFFDFF8, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #88
        0xB,
        "#1187F#6PYou... You would dare...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10F,
        (
            "#178F#2PKanone, you've lost.\x02\x03",

            "Come on.\x01",
            "It's time to accept it and surrender.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        (
            "#1185F#6PDON'T YOU DARE!\x02\x03",

            "A little setback like this WILL NOT stop\x01",
            "me from rescuing the colonel and fulfilling\x01",
            "his vision!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_491B():
        OP_67(0, 7100, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_491B)

    def lambda_4933():
        OP_6B(2590, 3000)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4933)
    SetChrChipByIndex(0xB, 44)
    SetChrSubChip(0xB, 4)
    OP_22(0x23B, 0x0, 0x64)
    OP_96(0xB, 0xFFFFCB30, 0xABE, 0xFFFFE278, 0x3E8, 0x1388)
    SetChrChipByIndex(0xB, 23)
    SetChrSubChip(0xB, 0)
    Sleep(300)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    OP_43(0x2C, 0x1, 0x0, 0x19)
    Sleep(300)
    OP_43(0x2D, 0x1, 0x0, 0x1A)
    Sleep(300)
    OP_43(0x2E, 0x1, 0x0, 0x1B)
    WaitChrThread(0x2E, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_1D(0x33)

    ChrTalk(    #91
        0xB,
        (
            "#1186F#6PJulia! Bracer scum!\x01",
            "This is the end!\x02\x03",

            "I'll beat you into the mud myself\x01",
            "if I have to! COME!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1007F#2PBig words from someone who\x01",
            "brought a tank to a sword fight...\x02\x03",

            "#1006FBut all right! Let's do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10F,
        (
            "#176F#2PThe time has come to bring an\x01",
            "end to this.\x02\x03",

            "#177FHere I come, Kanone!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 39)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AFD")
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x106, 40)
    Jump("loc_4B07")

    label("loc_4AFD")

    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 41)

    label("loc_4B07")

    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 42)
    SetChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 43)
    SetChrChipByIndex(0xB, 44)
    SetChrChipByIndex(0x2C, 25)
    SetChrChipByIndex(0x2D, 26)
    SetChrChipByIndex(0x2E, 25)

    def lambda_4B35():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B35)

    def lambda_4B50():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_4B50)

    def lambda_4B6B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4B6B)

    def lambda_4B86():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4B86)

    def lambda_4BA1():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4BA1)

    def lambda_4BBC():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4BBC)

    def lambda_4BD7():
        OP_90(0xFE, 0x1F4, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_4BD7)

    def lambda_4BF2():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BF2)
    Sleep(300)
    OP_44(0x101, 0xFF)
    OP_44(0x10F, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x2C, 0xFF)
    OP_44(0x2D, 0xFF)
    OP_44(0x2E, 0xFF)
    Battle(0x45E, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_20(0x0)
    Return()

    # Function_22_43D3 end

    def Function_23_4C56(): pass

    label("Function_23_4C56")

    OP_7E(0x3E8, 0xF830, 0xFE0C, 0x50, 0x0)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    Sleep(2000)
    OP_1D(0x54)
    AddParty(0xE, 0xF9, 0xFF)
    SetChrPos(0x101, -18580, 0, -1200, 270)
    SetChrPos(0xF7, -17350, 0, 170, 270)
    SetChrPos(0x109, -17070, 0, -1450, 270)
    SetChrPos(0x10F, -18780, 0, 320, 270)
    SetChrChipByIndex(0x101, 32)
    SetChrSubChip(0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CE7")
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    Jump("loc_4CF1")

    label("loc_4CE7")

    SetChrChipByIndex(0x103, 34)
    SetChrSubChip(0x103, 0)

    label("loc_4CF1")

    SetChrChipByIndex(0x109, 35)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 22)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0xB, -23470, 0, -40, 90)
    SetChrPos(0x2C, -23800, 0, 2380, 90)
    SetChrPos(0x2D, -25000, 0, 1040, 90)
    SetChrPos(0x2E, -24000, 0, -1130, 90)
    SetChrFlags(0x2C, 0x2)
    SetChrFlags(0x2D, 0x2)
    SetChrFlags(0x2E, 0x2)
    SetChrFlags(0x2C, 0x800)
    SetChrFlags(0x2D, 0x800)
    SetChrFlags(0x2E, 0x800)
    SetChrChipByIndex(0xB, 27)
    SetChrChipByIndex(0x2C, 28)
    SetChrChipByIndex(0x2D, 28)
    SetChrChipByIndex(0x2E, 28)
    SetChrSubChip(0xB, 3)
    SetChrSubChip(0x2C, 1)
    SetChrSubChip(0x2D, 4)
    SetChrSubChip(0x2E, 7)
    ClearChrFlags(0x2F, 0x80)
    OP_72(0x5, 0x4)
    SetChrPos(0x2F, -14380, 0, -8330, 0)
    OP_A1(0x2F, 0x5)
    OP_6F(0x5, 330)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    PlayEffect(0x0, 0x0, 0xFF, -14380, 2500, -6590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 2000, 600, 3460, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 1220, 600, -2270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x1, "map\\\\mp064_01.eff")
    LoadEffect(0x2, "map\\\\mp065_01.eff")
    LoadEffect(0x3, "map\\\\mp064_00.eff")
    LoadEffect(0x4, "map\\\\mp065_00.eff")
    LoadEffect(0x5, "map\\\\mp021_00.eff")
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0x30, 0x0)
    OP_A1(0x31, 0x1)
    SetChrPos(0x30, 1540, 0, 3700, 90)
    SetChrPos(0x31, 1190, 0, -2000, 90)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_6F(0x3, 10)
    OP_6F(0x4, 10)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    OP_6D(-21000, 0, -490, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(224000, 0)
    OP_6E(422, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1A, 0x20)
    SetChrBattleFlags(0x1B, 0x20)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1A, 2130, 0, 6400, 270)
    SetChrPos(0x1B, 1460, 0, -6180, 270)
    SetChrPos(0x1C, 5510, 0, -1750, 270)
    SetChrPos(0x1D, 5700, 0, 520, 270)
    SetChrPos(0x1E, 5710, 0, -3450, 270)
    SetChrPos(0x1F, 5630, 0, 1960, 270)
    SetChrPos(0x20, 7090, 0, -1780, 270)
    SetChrPos(0x21, 7090, 0, -120, 270)
    SetChrChipByIndex(0x1A, 21)
    SetChrChipByIndex(0x1B, 21)
    SetChrChipByIndex(0x1C, 21)
    SetChrChipByIndex(0x1D, 21)
    SetChrChipByIndex(0x1E, 21)
    SetChrChipByIndex(0x1F, 21)
    SetChrChipByIndex(0x20, 21)
    SetChrChipByIndex(0x21, 21)
    SetChrSubChip(0x1A, 3)
    SetChrSubChip(0x1B, 3)
    SetChrSubChip(0x1C, 3)
    SetChrSubChip(0x1D, 3)
    SetChrSubChip(0x1E, 3)
    SetChrSubChip(0x1F, 3)
    SetChrSubChip(0x20, 3)
    SetChrSubChip(0x21, 3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #94
        0xB,
        (
            "#1321F#4PAgh... Aaaargh...\x02\x03",

            "Colonel...forgive me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10F,
        (
            "#175F#5P*pant*...*pant*...\x02\x03",

            "That...is the end of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1007F#5PI think my legs're gonna fall off...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x109,
        (
            "#1068F#5PW-Well...*pant* we did fight her and\x01",
            "a TANK back to back, y'know...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51DC")

    ChrTalk(    #98
        0x106,
        "#556F#5PHeh... We did it, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5225")

    label("loc_51DC")


    ChrTalk(    #99
        0x103,
        (
            "#524F#5PHaah... Well, that's something...\x01",
            "like victory, at least...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5225")

    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -17890, 0, -11940, 0)

    NpcTalk(    #100
        0xC,
        "Man's Voice",
        "#4PI-Is it over...?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(100)
    ClearChrFlags(0xF7, 0x2)
    SetChrChipByIndex(0xF7, 65535)
    SetChrSubChip(0xF7, 0)
    Sleep(100)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    ClearChrFlags(0x10F, 0x2)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(100)

    def lambda_52BC():
        OP_6D(-19790, 0, -4520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_52BC)

    def lambda_52D4():
        OP_6B(2009, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52D4)
    ClearChrFlags(0xC, 0x80)

    def lambda_52E9():
        OP_8E(0xC, 0xFFFFB9B0, 0x0, 0xFFFFDCB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_52E9)

    def lambda_5304():

        label("loc_5304")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_5304")

    QueueWorkItem2(0x101, 2, lambda_5304)
    Sleep(100)

    def lambda_531A():

        label("loc_531A")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_531A")

    QueueWorkItem2(0xF7, 2, lambda_531A)
    Sleep(50)

    def lambda_5330():

        label("loc_5330")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_5330")

    QueueWorkItem2(0x109, 2, lambda_5330)
    Sleep(50)

    def lambda_5346():

        label("loc_5346")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_5346")

    QueueWorkItem2(0x10F, 2, lambda_5346)
    WaitChrThread(0xC, 0x1)
    OP_8C(0xC, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #101
        0x101,
        "#1004F#2PDuke Dunan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x109,
        "#1060F#2POh, hey! They threw you in the tank, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        "#220F#6PErm, well, yes!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    OP_44(0x10F, 0x2)

    def lambda_53E7():
        OP_6D(-18080, 0, -2070, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53E7)

    def lambda_53FF():
        OP_6B(1670, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53FF)
    OP_8E(0xC, 0xFFFFBA50, 0x0, 0xFFFFF38A, 0x7D0, 0x0)
    OP_8C(0xC, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #104
        0xC,
        (
            "#220F#6PFor once, brigand, it seems I actually need\x01",
            "to be thankful for your violent, lawless ways!\x02\x03",

            "#221FAs proof of my gratitude, I shall bestow\x01",
            "upon you a magnificent work of art from\x01",
            "my private collection!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x101,
        (
            "#1016FI, uh, think I'll pass, thanks.\x02\x03",

            "#1006FStill, never thought I'd hear gratitude fro--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_55E2():
        OP_6D(-17930, 0, -2800, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55E2)
    OP_8F(0x101, 0xFFFFB924, 0x0, 0xFFFFF600, 0x1388, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #106
        0x101,
        (
            "#1020F#4P#3SWait! RENNE!#2S\x02\x03",

            "#3SIs Renne safe?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #107
        0xC,
        (
            "#226F#6PWhat is this now...\x02\x03",

            "Who or what is a 'Renne'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1005F#4PA girl! Wearing a white dress!\x02\x03",

            "Isn't she in the tank?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        "#222F#6PI...was the only one inside...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)
    Sleep(500)

    def lambda_5719():
        OP_6D(-22590, 0, -220, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5719)

    def lambda_5731():
        OP_8F(0xFE, 0xFFFFAC04, 0x0, 0xFFFFFF56, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5731)

    def lambda_574C():

        label("loc_574C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_574C")

    QueueWorkItem2(0xC, 2, lambda_574C)

    def lambda_575D():

        label("loc_575D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_575D")

    QueueWorkItem2(0xF7, 2, lambda_575D)

    def lambda_576E():

        label("loc_576E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_576E")

    QueueWorkItem2(0x109, 2, lambda_576E)

    def lambda_577F():

        label("loc_577F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_577F")

    QueueWorkItem2(0x10F, 2, lambda_577F)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 270, 400)
    OP_44(0xC, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    OP_44(0x10F, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #110
        0x101,
        (
            "#1005F#6POKAY, YOU! WHERE'S RENNE?!\x02\x03",

            "Where are you keeping her?!\x01",
            "TELL ME!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        "#1182FWh-What...? What are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1009F#6PYou REALLY think you can play\x01",
            "dumb at this point?!\x02\x03",

            "THE GIRL! The one you kidnapped\x01",
            "from the guildhouse!\x01",
            "TELL. ME. WHERE. SHE. IS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "#1184FKidnapped? Girl...?\x02\x03",

            "#1183FI see... So that was the plan all along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1004F#6PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        "#1181FHeh... Hahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_20(0x7D0)

    ChrTalk(    #116
        0xB,
        "#1188F#3SHAHAHAHAHAHA!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1020F#6PWhat in the--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x10F,
        "#173F#5PKanone! What's wrong with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        (
            "#1181FWhat's wrong? EVERYTHING!\x01",
            "How can I not laugh at myself?!\x02\x03",

            "#1189FI! Kanone Amalthea!\x01",
            "Captain of the Intelligence Division!\x02\x03",

            "I, the author of this plan to restore the\x01",
            "colonel to glory!\x02\x03",

            "#1187FI...was played like a FIDDLE by\x01",
            "a little girl!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x1)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, -27100, 7300, -880, 90)
    Sleep(500)

    NpcTalk(    #120
        0x14,
        "Girl's Voice",
        (
            "#3PHeehee. How rude of you to call\x01",
            "me a 'little girl.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x5A)
    Sleep(500)

    def lambda_5BC3():
        OP_6D(-29980, 870, -950, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BC3)

    def lambda_5BDB():
        OP_67(0, 5490, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BDB)

    def lambda_5BF3():
        OP_6B(2810, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BF3)

    def lambda_5C03():
        OP_6E(599, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5C03)
    OP_6C(270000, 4000)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #121
        0x101,
        (
            "#1004F#5P...\x02\x03",

            "...Umm.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-34440, 890, 2870, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(297000, 0)
    OP_6E(272, 0)
    OP_0D()

    def lambda_5C89():
        OP_8E(0xFE, 0xFFFFAF10, 0x0, 0xFFFFFB96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_5C89)
    Sleep(200)

    def lambda_5CA9():
        OP_8E(0xFE, 0xFFFFAF10, 0x0, 0x37A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5CA9)
    Sleep(100)

    def lambda_5CC9():
        OP_8E(0xFE, 0xFFFFB41A, 0x0, 0xFFFFFFC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5CC9)

    NpcTalk(    #122
        0x14,
        "Renne",
        (
            "#261FHeehee! Good evening.\x01",
            "Isn't the moon lovely tonight?\x02\x03",

            "Did everyone enjoy the tea party?\x01",
            "I thought the explosions and screams\x01",
            "were best myself.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #123
        0x109,
        "#1064F#5P...Oh. Oh, crap.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DD0")

    ChrTalk(    #124
        0x106,
        "#055F#5PA kid?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DE6")

    label("loc_5DD0")


    ChrTalk(    #125
        0x103,
        "#023F#5PA child?\x02",
    )

    CloseMessageWindow()

    label("loc_5DE6")


    ChrTalk(    #126
        0x101,
        (
            "#1026F#2P...Renne?\x02\x03",

            "Wh... What are you doing, Renne?\x01",
            "Climbing all the way up there.\x02\x03",

            "#1020FIt's dangerous up there, you know!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #127
        0x14,
        "Renne",
        "#263F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1025F#2POh, Renne, you really are like a cat.\x02\x03",

            "Okay, I'll climb up to help you down,\x01",
            "so just wait a--\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #129
        0x14,
        "Renne",
        (
            "#1305FHeehee... There's no need.\x02\x03",

            "After all, this is the best seat.\x02\x03",

            "Only fitting for the master\x01",
            "of the tea party, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1026F#2PWh...at...?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 8)
    OP_0D()
    Sleep(500)

    def lambda_5FA8():
        OP_99(0x14, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5FA8)
    Sleep(200)
    Fade(500)

    def lambda_5FC2():
        OP_6B(3300, 0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5FC2)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    def lambda_5FE1():
        OP_99(0x14, 0x2, 0x1, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5FE1)
    WaitChrThread(0x14, 0x1)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    OP_0D()
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x4B, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS116._CH")
    OP_C6(0x0, 0x0, 100000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Renne")

    AnonymousTalk(    #131
        (
            "#1306FEnforcer No. XV, the Angel of Slaughter.\x02\x03",

            "That is me.\x02\x03",

            "And I...am Renne.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(1000)
    OP_C6(0x0, 0x6, 0, 0, 0)

    ChrTalk(    #132
        0x101,
        "#1020F#2PWhat? No... No.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x10F,
        (
            "#173F#5PThis is insane! A small child like that\x01",
            "is a member of Ouroboros?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x14,
        (
            "#263FHeheh! Silly lady. There are no 'children'\x01",
            "or 'adults' in the Grandmaster's sight.\x02\x03",

            "Just useful people...and useless people.\x02\x03",

            "#1305FAnd I, Lady Renne, am very useful.\x02\x03",

            "Just like the Black Fang used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1020F#2PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x109,
        (
            "#1069F#5PSo then... Hang on!\x02\x03",

            "You're the one who sent me that letter,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x14,
        (
            "#1306FMm-hmm! That was me.\x02\x03",

            "#263FNine threatening letters.\x02\x03",

            "One letter to the churchman.\x02\x03",

            "One to the traitor lady.\x02\x03",

            "And one to Estelle.\x02\x03",

            "#1305FTwelve letters in all!\x01",
            "Heehee, feels like all I did\x01",
            "was write, write, write!\x02\x03",

            "I bet even Loewe would compliment\x01",
            "my handwriting now!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E4")

    ChrTalk(    #138
        0x106,
        "#057F#5PSo you staged this whole thing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_641A")

    label("loc_63E4")


    ChrTalk(    #139
        0x103,
        (
            "#022F#5PSo you staged all of this?\x01",
            "Impossible...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_641A")


    ChrTalk(    #140
        0x14,
        (
            "#263FWell, I'm the one who organized\x01",
            "the tea party, you know.\x02\x03",

            "I couldn't let my guests be bored,\x01",
            "could I?\x02\x03",

            "I worked really hard to make this fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1003F#2PBut... But...then...\x02\x03",

            "#1005FWhat about your papa? Your mama?\x02\x03",

            "Renne, where are your parents?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x14,
        (
            "#264FHuuuuh?\x02\x03",

            "#269FOoooooh, wait. You never, ever realized.\x02\x03",

            "#263FHeehee. I must be really good at this!\x02\x03",

            "Either that, or you're just that dumb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1019F#2PWait a minute, who're you callin' dumb?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x14,
        (
            "#1306FHeehee! Don't be angry, Estelle.\x02\x03",

            "You meant these, right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xBD, 0x0, 0x64)
    SetChrPos(0x18, -27000, 8500, -2300, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x4)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_666A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_666A)

    def lambda_667C():
        OP_8F(0xFE, 0xFFFF9688, 0x1F40, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_667C)
    Sleep(300)
    OP_22(0xBD, 0x0, 0x64)
    SetChrPos(0x19, -27000, 8500, -3200, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x19, 0x4)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_66CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_66CC)

    def lambda_66DE():
        OP_8F(0xFE, 0xFFFF9688, 0x1F40, 0xFFFFF380, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_66DE)
    WaitChrThread(0x19, 0x3)
    Sleep(500)

    ChrTalk(    #145
        0x18,
        "#1364F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x19,
        "#1373F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #147
        0x101,
        "#1020F#2POh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x14,
        (
            "#263FThese aren't my papa and mama,\x01",
            "silly.\x02\x03",

            "#1306FI'm actually done with them anyway,\x01",
            "so...let's BREAK them!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x20)
    OP_8C(0x14, 180, 400)
    ClearChrFlags(0x14, 0x20)
    Fade(250)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 1)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x19, 0x20)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6801():
        OP_6D(-34440, 1890, 1870, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6801)

    def lambda_6819():
        OP_67(0, 7000, -10000, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6819)

    def lambda_6831():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6831)

    def lambda_6841():
        OP_96(0xFE, 0xFFFF9566, 0x2260, 0xFFFFFA24, 0x7D0, 0x2710)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6841)
    Sleep(200)
    OP_22(0x1F9, 0x0, 0x64)

    def lambda_6869():
        OP_99(0x14, 0x1, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6869)
    OP_43(0x14, 0x1, 0x0, 0x26)
    WaitChrThread(0x14, 0x0)
    OP_96(0x14, 0xFFFF9566, 0x1C84, 0xFFFFFA24, 0x0, 0xBB8)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(500)
    OP_6D(-22230, 0, -20, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2009, 0)
    OP_6C(315000, 0)
    OP_6E(336, 0)
    OP_0D()

    def lambda_68F3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68F3)

    def lambda_6901():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6901)
    Sleep(100)

    def lambda_6914():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6914)

    def lambda_6922():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6922)
    WaitChrThread(0x14, 0x1)

    ChrTalk(    #149
        0x10F,
        "#173F#4PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1020F#4PWh-Wh...\x02\x03",

            "#1022FY-Y... You...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 500)
    Sleep(500)

    ChrTalk(    #151
        0x101,
        "#1005F#6P#3SWHAT DID YOU DO?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0xF7, 270, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69FD")

    ChrTalk(    #152
        0x106,
        (
            "#054F#5PEstelle! Calm down!\x02\x03",

            "There's...no blood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A37")

    label("loc_69FD")


    ChrTalk(    #153
        0x103,
        (
            "#024F#5PCalm down, Estelle!\x02\x03",

            "They...aren't bleeding!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A37")


    ChrTalk(    #154
        0x101,
        "#1004F#6PWh...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #155
        0x101,
        "#1026F#4PYou... You're right. How...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x109,
        (
            "#1067F#2PSociety-manufactured orbal puppets...\x01",
            "and they look just like humans.\x02\x03",

            "#1065FHow are they even...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, -27290, 7300, -880, 90)
    Sleep(100)
    Fade(500)
    OP_6D(-34440, 890, 2870, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3420, 0)
    OP_6C(297000, 0)
    OP_6E(272, 0)
    OP_8C(0x101, 180, 0)
    OP_8C(0xF7, 180, 0)
    OP_8C(0x109, 180, 0)
    OP_8C(0x10F, 180, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #157
        0x14,
        (
            "#263FHeehee! They don't act like people\x01",
            "when I'm not around, though.\x02\x03",

            "I'm pretty sure I'm at least as good\x01",
            "as Pedro from The Doll Knight.\x02\x03",

            "#1306FOh, but this time I got kidnapped,\x01",
            "and had to be the master of a tea\x01",
            "party...\x02\x03",

            "So I'm more like Princess Tia, huh?\x01",
            "'Princess Renne' has a nice ring to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x109,
        "#1068F#5POf all the things to joke about...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x14,
        (
            "#1305FOh, but you asked about Mama\x01",
            "and Papa, right, Estelle? Let's call\x01",
            "Princess Renne's real mama and papa now.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x14, 47)
    SetChrSubChip(0x14, 0)
    OP_0D()
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x14, 0x0, 0x1, 0x3E8)
    Sleep(500)

    ChrTalk(    #160
        0x14,
        "#263FPater-Mater! Come!\x02",
    )

    CloseMessageWindow()
    OP_DB()
    Sleep(500)
    OP_22(0x113, 0x1, 0x46)
    OP_24(0x113, 0x46)
    Sleep(500)

    def lambda_6DA9():

        label("loc_6DA9")

        OP_7C(0x14, 0x14, 0x7D0, 0x64)
        OP_48()
        Jump("loc_6DA9")

    QueueWorkItem2(0x2F, 3, lambda_6DA9)
    Sleep(1000)
    OP_A3(0x0)
    OP_43(0x101, 0x1, 0x0, 0x1E)
    Sleep(50)
    OP_43(0xF7, 0x1, 0x0, 0x1F)
    Sleep(50)
    OP_43(0x109, 0x1, 0x0, 0x20)
    Sleep(50)
    OP_43(0x10F, 0x1, 0x0, 0x21)
    Sleep(50)
    OP_43(0xC, 0x1, 0x0, 0x1E)

    def lambda_6E03():
        OP_6D(-24790, 0, -7120, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E03)

    def lambda_6E1B():
        OP_6C(225000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6E1B)

    def lambda_6E2B():
        OP_6B(4300, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6E2B)
    OP_24(0x113, 0x50)
    Sleep(1000)
    OP_24(0x113, 0x55)
    Sleep(1000)
    OP_24(0x113, 0x5A)
    Sleep(1000)
    OP_24(0x113, 0x5F)
    Sleep(1000)
    OP_24(0x113, 0x64)

    def lambda_6E63():

        label("loc_6E63")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_6E63")

    QueueWorkItem2(0x2F, 3, lambda_6E63)
    WaitChrThread(0x101, 0x3)
    OP_A2(0x0)
    OP_DC()

    ChrTalk(    #161
        0x101,
        "#1026F#5PWhat's that sound?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0x10F,
        "#177F#2PFrom above! Look out!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x33, 0x6)
    SetChrFlags(0x33, 0x4)
    ClearChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x8)
    OP_72(0x6, 0x4)
    SetChrPos(0x33, -21490, 15000, -8050, 0)
    SetChrFlags(0x33, 0x1)
    OP_51(0x33, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x33, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_71(0x6, 0x20)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 241)
    OP_70(0x6, 0x104)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 260)
    OP_70(0x6, 0xF1)

    def lambda_6FF8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FF8)

    def lambda_7006():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7006)
    Sleep(100)

    def lambda_7019():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7019)

    def lambda_7027():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7027)

    def lambda_7035():
        OP_8F(0x33, 0xFFFFAC0E, 0x0, 0xFFFFE08E, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7035)
    Sleep(500)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 221)
    OP_70(0x6, 0xF0)
    WaitChrThread(0x33, 0x1)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    OP_6D(-22260, 0, -9450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(212000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x19, 0x800)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x2F, 0x3)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    OP_73(0x6)
    OP_71(0x6, 0x20)
    OP_D8(0x6, 0x1F4)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x28)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMapFlags(0x10)

    ChrTalk(    #163
        0x101,
        "#1020F#3SWHAT THE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xC,
        "#226F#3S#5PKIYAAAAAAAAAAAAAAAH!\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x0, 0x25)
    OP_43(0xC, 0x0, 0x0, 0x24)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7187")

    ChrTalk(    #165
        0x106,
        "#055FIt's HUGE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_71A7")

    label("loc_7187")


    ChrTalk(    #166
        0x103,
        "#523FIt's enormous! What--\x02",
    )

    CloseMessageWindow()

    label("loc_71A7")


    ChrTalk(    #167
        0x109,
        "#1069F#5PThe heck is THAT?!\x02",
    )

    CloseMessageWindow()

    def lambda_71CE():
        OP_6C(237000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71CE)
    OP_72(0x6, 0x20)

    def lambda_71E3():
        OP_8C(0xFE, 45, 60)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_71E3)
    OP_6F(0x6, 201)
    OP_70(0x6, 0xD2)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(300)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(300)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x33, 0x1)
    OP_73(0x6)
    Sleep(500)
    OP_22(0x115, 0x0, 0x64)
    OP_B0(0x6, 0xA)
    OP_6F(0x6, 301)
    OP_70(0x6, 0x13B)
    OP_73(0x6)
    OP_6F(0x5, 231)
    OP_70(0x5, 0xFA)
    OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
    OP_6F(0x6, 316)
    OP_70(0x6, 0x154)
    OP_22(0x3C6, 0x0, 0x64)
    OP_73(0x6)
    OP_71(0x6, 0x20)
    OP_6F(0x6, 341)
    OP_70(0x6, 0x17C)

    ChrTalk(    #168
        0x101,
        "#1026F#1POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x10F,
        "#173F#1PThe Gospel...!\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_72C0():
        OP_6D(-31920, 0, -6080, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72C0)
    OP_B0(0x6, 0x19)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 381)
    OP_70(0x6, 0x1A4)
    OP_22(0x115, 0x0, 0x64)
    Sleep(800)
    OP_7D(0x0, 0x14, 0x32, 0x1F4)

    def lambda_7301():
        OP_6D(-25540, 0, -10760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7301)

    def lambda_7319():
        OP_67(0, 5750, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7319)

    def lambda_7331():
        OP_6B(3750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7331)

    def lambda_7341():
        OP_6C(225000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7341)

    def lambda_7351():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_7351)
    SetChrChipByIndex(0x14, 46)
    SetChrSubChip(0x14, 4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_7370():
        OP_96(0x14, 0xFFFFAA10, 0xBB8, 0xFFFFEC78, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7370)
    Sleep(700)
    OP_CF(0x14, 0x6, "Frame85__ren")
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x1)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 0)
    SetChrSubChip(0x14, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x14, 0x0, 0x0)
    ClearChrFlags(0x14, 0x1)
    OP_8C(0x14, 180, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #170
        0x14,
        (
            "#1306F#5PThis is my Pater-Mater.\x02\x03",

            "As big as any papa, as kind as any mama!\x02\x03",

            "I don't need any other papa or mama.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(500)
    SetChrPos(0x22, -10900, 0, 230, 270)
    SetChrPos(0x23, -10370, 0, -1430, 270)

    NpcTalk(    #171
        0x22,
        "Man's Voice",
        "#2PThere! Ahead!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #172
        0x23,
        "Girl's Voice",
        "#5PWHOA! What the heck is THAT THING?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_74F9():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74F9)

    def lambda_7507():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_7507)

    def lambda_7515():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7515)

    def lambda_7523():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7523)

    def lambda_7531():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7531)
    Fade(1000)
    OP_6D(-21560, 0, -7400, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(8250, 0)
    OP_6C(223000, 0)
    OP_6E(165, 0)
    OP_D2(0x2702EA, 0x2702F4, 0x1D)
    OP_D2(0x2702EB, 0x2702F5, 0x1E)
    OP_D2(0x702EF, 0x702F6, 0x1F)
    OP_D2(0x70021, 0x70029, 0x20)
    OP_D2(0x70051, 0x70059, 0x21)
    OP_D2(0x70031, 0x70039, 0x22)
    OP_D2(0x70041, 0x70049, 0x23)
    OP_D2(0x70061, 0x70069, 0x24)
    OP_D2(0x70071, 0x70079, 0x25)
    OP_D2(0x270091, 0x270095, 0x27)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0x2B, 0x40)
    SetChrPos(0x13, 6000, 0, -1790, 270)
    SetChrPos(0x11, 6000, 0, -1370, 270)
    SetChrPos(0x12, 6000, 0, -3420, 270)
    SetChrPos(0x10, 6000, 0, -2160, 270)
    SetChrPos(0xF, 6000, 0, -2300, 270)
    SetChrPos(0x16, 6000, 0, -3260, 270)
    SetChrPos(0x15, 8000, 0, 510, 270)
    SetChrPos(0x22, 8000, 0, 2500, 270)
    SetChrPos(0x23, 8000, 0, 2400, 270)
    SetChrPos(0x24, 8000, 0, 800, 270)
    SetChrPos(0x25, 8000, 0, -90, 270)
    SetChrPos(0x26, 8000, 0, 2110, 270)
    SetChrPos(0x27, 8000, 0, 270, 270)
    SetChrPos(0x28, 8000, 0, 1610, 270)
    SetChrPos(0x29, 8000, 0, 2750, 270)
    SetChrPos(0x2A, 8000, 0, 2170, 270)
    SetChrPos(0x2B, 8000, 0, 1040, 270)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_77D6")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0xE, 6000, 0, -3010, 270)
    OP_43(0xE, 0x0, 0x0, 0x28)
    Jump("loc_77F8")

    label("loc_77D6")

    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, 6000, 0, -3010, 270)
    OP_43(0xD, 0x0, 0x0, 0x27)

    label("loc_77F8")

    OP_43(0x13, 0x0, 0x0, 0x29)
    OP_43(0x11, 0x0, 0x0, 0x2B)
    OP_43(0x10, 0x0, 0x0, 0x2C)
    OP_43(0x12, 0x0, 0x0, 0x2A)
    OP_43(0xF, 0x0, 0x0, 0x2D)
    OP_43(0x16, 0x0, 0x0, 0x2E)
    OP_43(0x15, 0x0, 0x0, 0x2F)
    OP_43(0x22, 0x0, 0x0, 0x30)
    OP_43(0x23, 0x0, 0x0, 0x31)
    OP_43(0x24, 0x0, 0x0, 0x32)
    OP_43(0x25, 0x0, 0x0, 0x33)
    OP_43(0x26, 0x0, 0x0, 0x34)
    OP_43(0x27, 0x0, 0x0, 0x35)
    OP_43(0x28, 0x0, 0x0, 0x36)
    OP_43(0x29, 0x0, 0x0, 0x37)
    OP_43(0x2A, 0x0, 0x0, 0x38)
    OP_43(0x2B, 0x0, 0x0, 0x39)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #173
        0x13,
        "#1317F#5PSome kinda giant...thingy?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x0)

    ChrTalk(    #174
        0x15,
        "#702F#2PThis is impossible!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_78F5")

    ChrTalk(    #175
        0xE,
        "#054F#1PWhat the heck is...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7919")

    label("loc_78F5")


    ChrTalk(    #176
        0xD,
        "#024F#1PWhat's going on here?!\x02",
    )

    CloseMessageWindow()

    label("loc_7919")


    ChrTalk(    #177
        0x11,
        "#065F#5PR-Renne?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #178
        0x101,
        "#1026F#2PEveryone...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(-30740, 0, -15630, 0)
    OP_67(0, 2870, -10000, 0)
    OP_6B(5020, 0)
    OP_6C(225000, 0)
    OP_6E(245, 0)
    OP_8C(0x14, 180, 0)
    OP_8C(0x13, 270, 0)
    OP_8C(0x12, 270, 0)
    OP_8C(0xF, 270, 0)
    OP_8C(0x17, 270, 0)
    OP_8C(0x16, 270, 0)
    OP_8C(0x11, 270, 0)
    OP_8C(0x10, 270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #179
        0x14,
        (
            "#263F#5PHeheh! Yay, the sleeping medicine wore\x01",
            "off juuuust when it was supposed to!\x02\x03",

            "Just like Joshua taught me a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#1002F#2PJoshua?! How do you--\x02",
    )

    CloseMessageWindow()

    def lambda_7A84():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7A84)

    def lambda_7A92():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_7A92)
    Sleep(100)

    def lambda_7AA5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7AA5)

    def lambda_7AB3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7AB3)
    Sleep(100)

    def lambda_7AC6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7AC6)

    ChrTalk(    #181
        0x14,
        (
            "#1305F#5PYou know, I was just gonna gut you like\x01",
            "a fish and rip out your heart at the end\x01",
            "of this, Estelle.\x02\x03",

            "After all, the professor says YOU'RE\x01",
            "the reason Joshua won't come back.\x01",
            "It's YOUR fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1020F#2PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x14,
        (
            "#261F#5PBut I really, really had a lot of fun,\x01",
            "so I think I can forgive you for now.\x02\x03",

            "But only this once, okay? Heehee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#1020F#2PW-Wait! Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x11,
        "#065F#5PReeeeenne! What's going on?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x14,
        (
            "#263F#5PHeheh! Bye-bye, Tita.\x02\x03",

            "I did have fun with you... Maybe we\x01",
            "can share ice cream again someday.\x02\x03",

            "#1306FWell, everyone...\x02\x03",

            "Thank you for attending the tea party.\x01",
            "Ciao!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_DB()

    def lambda_7D32():
        OP_6D(-21660, 3000, -6840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7D32)

    def lambda_7D4A():
        OP_6B(2400, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D4A)
    OP_22(0x113, 0x0, 0x64)
    Sleep(500)

    def lambda_7D64():

        label("loc_7D64")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_7D64")

    QueueWorkItem2(0x2F, 3, lambda_7D64)
    OP_22(0x85, 0x1, 0x50)

    def lambda_7D84():
        OP_67(0, 32810, -10000, 25000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D84)

    def lambda_7D9C():
        OP_6C(0, 25000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D9C)
    ClearChrFlags(0x2C, 0x800)
    ClearChrFlags(0x2D, 0x800)
    ClearChrFlags(0x2E, 0x800)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x2)
    SetChrSubChip(0x14, 6)
    PlayEffect(0x5, 0x5, 0x33, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x3, 0x3, 0x33, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x33, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)

    def lambda_7E73():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7E73)
    OP_B0(0x6, 0xA)
    OP_71(0x6, 0x20)
    OP_D8(0x6, 0x7D0)
    OP_6F(0x6, 461)
    OP_70(0x6, 0x1E0)
    PlayEffect(0x1, 0x3, 0x33, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x33, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7F13():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7F13)

    def lambda_7F21():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7F21)

    def lambda_7F2F():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7F2F)

    def lambda_7F3D():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7F3D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7F5D")

    def lambda_7F52():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_7F52)
    Jump("loc_7F6B")

    label("loc_7F5D")


    def lambda_7F63():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_7F63)

    label("loc_7F6B")


    def lambda_7F71():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7F71)

    def lambda_7F7F():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_7F7F)

    def lambda_7F8D():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7F8D)

    def lambda_7F9B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_7F9B)

    def lambda_7FA9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_7FA9)

    def lambda_7FB7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7FB7)

    def lambda_7FC5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_7FC5)

    def lambda_7FD3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_7FD3)

    def lambda_7FE1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_7FE1)

    def lambda_7FEF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_7FEF)
    Sleep(1000)

    def lambda_8002():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8002)
    Sleep(1000)

    def lambda_8022():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8022)
    OP_71(0x6, 0x20)
    OP_B0(0x6, 0xA)
    OP_82(0x5, 0x2)
    Sleep(800)

    def lambda_804E():
        OP_8F(0x33, 0xFFFFAC0E, 0x1388, 0xFFFFE08E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_804E)
    Sleep(800)
    WaitChrThread(0x33, 0x1)

    def lambda_8073():
        OP_8C(0x33, 180, 50)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8073)
    Sleep(500)
    SetChrSubChip(0x14, 7)
    Sleep(1000)
    SetChrSubChip(0x14, 0)
    WaitChrThread(0x33, 0x1)

    def lambda_809A():
        OP_6D(-21660, 3000, -15000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_809A)

    def lambda_80B2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_80B2)

    def lambda_80C0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_80C0)

    def lambda_80CE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_80CE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_80EE")

    def lambda_80E3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_80E3)
    Jump("loc_80FC")

    label("loc_80EE")


    def lambda_80F4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_80F4)

    label("loc_80FC")


    def lambda_8102():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8102)

    def lambda_8110():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8110)

    def lambda_811E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_811E)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 481)
    OP_70(0x6, 0x1F4)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x6)
    OP_71(0x6, 0x20)
    OP_6F(0x6, 501)
    OP_70(0x6, 0x208)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x33, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x33, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x33, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_829D():
        OP_90(0x33, 0x0, 0x2710, 0xFFFF2928, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_829D)
    Sleep(1500)
    ClearChrFlags(0x33, 0x1)

    def lambda_82C2():
        OP_90(0x33, 0x0, 0x7530, 0xFFFF2928, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_82C2)
    Sleep(1500)
    OP_43(0x14, 0x3, 0x0, 0x3A)

    def lambda_82E9():

        label("loc_82E9")

        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        OP_48()
        Jump("loc_82E9")

    QueueWorkItem2(0x2F, 3, lambda_82E9)

    def lambda_8304():
        OP_90(0x33, 0x0, 0x9C40, 0xFFFF2928, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8304)
    Sleep(1500)

    def lambda_8324():
        OP_90(0x33, 0x1388, 0xEA60, 0xFFFF2928, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8324)
    Sleep(1000)

    def lambda_8344():
        OP_90(0x33, 0x1388, 0x186A0, 0xFFFF2928, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8344)
    Sleep(1000)
    SetChrSubChip(0x14, 7)

    def lambda_8369():
        OP_90(0x33, 0x1388, 0x249F0, 0xFFFF2928, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8369)
    Sleep(1000)
    SetChrSubChip(0x14, 6)

    def lambda_838E():
        OP_90(0x33, 0x1388, 0x3D090, 0xFFFF2158, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_838E)
    OP_24(0x113, 0x64)
    Sleep(1000)

    ChrTalk(    #187 op#A op#5
        0x101,
        "#5S#30A#5PREEEEENNNNNE!\x05\x02",
    )

    FadeToDark(4000, 0, -1)
    OP_24(0x113, 0x50)
    OP_24(0x85, 0x50)
    Sleep(1000)
    OP_24(0x113, 0x3C)
    OP_24(0x85, 0x3C)
    Sleep(1000)
    OP_24(0x113, 0x28)
    OP_24(0x85, 0x28)
    Sleep(1000)
    OP_24(0x113, 0x14)
    OP_24(0x85, 0x14)
    Sleep(1000)
    OP_23(0x113)
    OP_20(0xBB8)
    OP_44(0x2F, 0x3)
    OP_23(0x85)
    OP_44(0x33, 0x1)
    SetChrFlags(0x14, 0x80)
    OP_71(0x6, 0x4)
    WaitChrThread(0x101, 0x1)
    OP_21()
    OP_0D()
    ClearChrFlags(0x101, 0x40)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    Sleep(1000)
    OP_DC()
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4C56 end

    def Function_24_8454(): pass

    label("Function_24_8454")

    OP_96(0xFE, 0xFFFFBD02, 0x0, 0xFFFFEE80, 0x5DC, 0x1388)
    OP_96(0xFE, 0xFFFFB3F2, 0x0, 0xFFFFFFD8, 0x3E8, 0x1388)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_24_8454 end

    def Function_25_848A(): pass

    label("Function_25_848A")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -14240, 0, -12370, 0)
    OP_8E(0xFE, 0xFFFFD60C, 0x0, 0xFFFFD0D0, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD620, 0x0, 0xFFFFE3EA, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 48)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_25_848A end

    def Function_26_84DF(): pass

    label("Function_26_84DF")

    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -14240, 0, -12370, 0)
    OP_8E(0xFE, 0xFFFFD60C, 0x0, 0xFFFFD0D0, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD88C, 0x0, 0xFFFFDEA4, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_26_84DF end

    def Function_27_853E(): pass

    label("Function_27_853E")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -14240, 0, -12370, 0)
    OP_8E(0xFE, 0xFFFFBADC, 0x0, 0xFFFFCE8C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFBAF0, 0x0, 0xFFFFE39A, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 48)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_27_853E end

    def Function_28_8593(): pass

    label("Function_28_8593")

    OP_8E(0xFE, 0xFFFFCBB2, 0x0, 0xA0, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x14, 400)
    Return()

    # Function_28_8593 end

    def Function_29_85AF(): pass

    label("Function_29_85AF")

    OP_8E(0xFE, 0xFFFFD1B6, 0x0, 0x33E, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x14, 400)
    Return()

    # Function_29_85AF end

    def Function_30_85CB(): pass

    label("Function_30_85CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8601")
    Sleep(200)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Jump("Function_30_85CB")

    label("loc_8601")

    Return()

    # Function_30_85CB end

    def Function_31_8602(): pass

    label("Function_31_8602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8638")
    Sleep(50)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Jump("Function_31_8602")

    label("loc_8638")

    Return()

    # Function_31_8602 end

    def Function_32_8639(): pass

    label("Function_32_8639")

    OP_8C(0xFE, 90, 400)
    Sleep(500)

    label("loc_8645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_867B")
    Sleep(150)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Jump("loc_8645")

    label("loc_867B")

    Return()

    # Function_32_8639 end

    def Function_33_867C(): pass

    label("Function_33_867C")

    OP_8C(0xFE, 90, 400)
    Sleep(500)

    label("loc_8688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86BE")
    Sleep(100)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Jump("loc_8688")

    label("loc_86BE")

    Return()

    # Function_33_867C end

    def Function_34_86BF(): pass

    label("Function_34_86BF")


    def lambda_86C5():
        OP_8F(0xFE, 0xFFFFC3CE, 0x1B58, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86C5)
    OP_8C(0xFE, 180, 100)
    Return()

    # Function_34_86BF end

    def Function_35_86E2(): pass

    label("Function_35_86E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86F7")
    OP_99(0x109, 0xC, 0xF, 0x5DC)
    Jump("Function_35_86E2")

    label("loc_86F7")

    Return()

    # Function_35_86E2 end

    def Function_36_86F8(): pass

    label("Function_36_86F8")

    OP_8E(0xFE, 0xFFFFB744, 0x0, 0x622, 0xFA0, 0x0)
    OP_44(0xC, 0x1)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_36_86F8 end

    def Function_37_8718(): pass

    label("Function_37_8718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_873B")
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_37_8718")

    label("loc_873B")

    Return()

    # Function_37_8718 end

    def Function_38_873C(): pass

    label("Function_38_873C")

    Sleep(200)
    OP_22(0x38F, 0x0, 0x64)

    def lambda_874C():
        OP_99(0xFE, 0x0, 0x4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_874C)

    def lambda_875C():
        OP_96(0x18, 0xFFFFA272, 0x0, 0xFFFFF36C, 0x32, 0x1B58)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_875C)
    Sleep(50)
    OP_22(0x38F, 0x0, 0x64)

    def lambda_8784():
        OP_99(0xFE, 0x0, 0x4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_8784)

    def lambda_8794():
        OP_96(0x19, 0xFFFFA7F4, 0x0, 0xFFFFEF34, 0x32, 0x1B58)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8794)
    WaitChrThread(0x18, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_87BC():
        OP_99(0xFE, 0x5, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_87BC)
    WaitChrThread(0x19, 0x1)

    def lambda_87D1():
        OP_99(0xFE, 0x5, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_87D1)
    Return()

    # Function_38_873C end

    def Function_39_87DC(): pass

    label("Function_39_87DC")

    SetChrChipByIndex(0xFE, 32)
    OP_8E(0xFE, 0xFFFFBFFA, 0x0, 0xFFFFF43E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 3)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_39_87DC end

    def Function_40_8802(): pass

    label("Function_40_8802")

    SetChrChipByIndex(0xFE, 33)
    OP_8E(0xFE, 0xFFFFBFFA, 0x0, 0xFFFFF43E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 4)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_40_8802 end

    def Function_41_8828(): pass

    label("Function_41_8828")

    Sleep(200)
    SetChrChipByIndex(0xFE, 39)
    OP_8E(0xFE, 0xFFFFBCC6, 0x0, 0xFFFFF902, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 9)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_41_8828 end

    def Function_42_8853(): pass

    label("Function_42_8853")

    Sleep(400)
    SetChrChipByIndex(0xFE, 37)
    OP_8E(0xFE, 0xFFFFC64E, 0x0, 0xFFFFF2A4, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_42_8853 end

    def Function_43_887E(): pass

    label("Function_43_887E")

    Sleep(600)
    SetChrChipByIndex(0xFE, 36)
    OP_8E(0xFE, 0xFFFFC20C, 0x0, 0xFFFFFAA6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 7)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_43_887E end

    def Function_44_88A9(): pass

    label("Function_44_88A9")

    Sleep(800)
    SetChrChipByIndex(0xFE, 35)
    OP_8E(0xFE, 0xFFFFC5CC, 0x0, 0xFFFFF790, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 6)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_44_88A9 end

    def Function_45_88D4(): pass

    label("Function_45_88D4")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0xFFFFCB76, 0x0, 0xFFFFF704, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_45_88D4 end

    def Function_46_88FF(): pass

    label("Function_46_88FF")

    Sleep(1200)
    OP_8E(0xFE, 0xFFFFCDBA, 0x0, 0xFFFFF344, 0x1388, 0x0)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_46_88FF end

    def Function_47_8920(): pass

    label("Function_47_8920")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 30)
    OP_8E(0xFE, 0xFFFFBE88, 0x0, 0x1FE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 29)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_47_8920 end

    def Function_48_894B(): pass

    label("Function_48_894B")

    Sleep(1700)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC400, 0x0, 0x1D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_48_894B end

    def Function_49_8976(): pass

    label("Function_49_8976")

    Sleep(1900)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC1A8, 0x0, 0x960, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_49_8976 end

    def Function_50_89A1(): pass

    label("Function_50_89A1")

    Sleep(2100)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC9FA, 0x0, 0x320, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_50_89A1 end

    def Function_51_89CC(): pass

    label("Function_51_89CC")

    Sleep(2300)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFCC3E, 0x0, 0xFFFFFFA6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_51_89CC end

    def Function_52_89F7(): pass

    label("Function_52_89F7")

    Sleep(2500)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFC7F2, 0x0, 0x83E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_52_89F7 end

    def Function_53_8A22(): pass

    label("Function_53_8A22")

    Sleep(2600)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFD256, 0x0, 0x10E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_53_8A22 end

    def Function_54_8A4D(): pass

    label("Function_54_8A4D")

    Sleep(2700)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFD102, 0x0, 0x64A, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_54_8A4D end

    def Function_55_8A78(): pass

    label("Function_55_8A78")

    Sleep(2900)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFCE6E, 0x0, 0xABE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_55_8A78 end

    def Function_56_8AA3(): pass

    label("Function_56_8AA3")

    Sleep(3100)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFD6DE, 0x0, 0x87A, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_56_8AA3 end

    def Function_57_8ACE(): pass

    label("Function_57_8ACE")

    Sleep(3300)
    SetChrChipByIndex(0xFE, 31)
    OP_8E(0xFE, 0xFFFFDA12, 0x0, 0x410, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 17)
    OP_8C(0xFE, 215, 400)
    Return()

    # Function_57_8ACE end

    def Function_58_8AF9(): pass

    label("Function_58_8AF9")

    SetChrFlags(0x101, 0x40)

    def lambda_8B04():
        OP_8E(0x101, 0xFFFFAD6C, 0x0, 0xFFFFC4E6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B04)
    Sleep(800)

    def lambda_8B24():
        OP_8E(0xFE, 0xFFFFA600, 0x0, 0xFFFFC52C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_8B24)
    Sleep(200)

    def lambda_8B44():
        OP_8E(0xFE, 0xFFFFB28A, 0x0, 0xFFFFC658, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8B44)
    Sleep(200)

    def lambda_8B64():
        OP_8E(0xFE, 0xFFFFAD1C, 0x0, 0xFFFFCA40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_8B64)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8BA3")

    def lambda_8B8B():
        OP_8E(0xFE, 0xFFFFB1A4, 0x0, 0xFFFFCA72, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8B8B)
    Jump("loc_8BBE")

    label("loc_8BA3")


    def lambda_8BA9():
        OP_8E(0xFE, 0xFFFFB1A4, 0x0, 0xFFFFCA72, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_8BA9)

    label("loc_8BBE")

    Sleep(200)

    def lambda_8BC9():
        OP_8E(0xFE, 0xFFFFB474, 0x0, 0xFFFFCEC8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_8BC9)
    Sleep(300)

    def lambda_8BE9():
        OP_8E(0xFE, 0xFFFFA8D0, 0x0, 0xFFFFCA04, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8BE9)
    Sleep(300)

    def lambda_8C09():
        OP_8E(0xFE, 0xFFFFAB96, 0x0, 0xFFFFD0A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8C09)
    Sleep(200)

    def lambda_8C29():
        OP_8E(0xFE, 0xFFFFAF4C, 0x0, 0xFFFFD4AE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_8C29)
    Sleep(200)

    def lambda_8C49():
        OP_8E(0xFE, 0xFFFFB3DE, 0x0, 0xFFFFD864, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8C49)
    Sleep(300)

    def lambda_8C69():
        OP_8E(0xFE, 0xFFFFAAEC, 0x0, 0xFFFFE2FA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8C69)
    Sleep(200)

    def lambda_8C89():
        OP_8E(0xFE, 0xFFFFAE7A, 0x0, 0xFFFFE4A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_8C89)
    Sleep(300)
    SetChrChipByIndex(0x15, 11)

    def lambda_8CAE():
        OP_8E(0xFE, 0xFFFFAE7A, 0x0, 0xFFFFDC1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_8CAE)
    Sleep(300)

    def lambda_8CCE():
        OP_8E(0xFE, 0xFFFFAC36, 0x0, 0xFFFFEB10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_8CCE)
    Sleep(200)

    def lambda_8CEE():
        OP_8E(0xFE, 0xFFFFB23A, 0x0, 0xFFFFEB42, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_8CEE)
    Sleep(300)

    def lambda_8D0E():
        OP_8E(0xFE, 0xFFFFB884, 0x0, 0xFFFFE994, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_8D0E)

    def lambda_8D29():
        OP_8E(0xFE, 0xFFFFAF88, 0x0, 0xFFFFF06A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_8D29)
    Sleep(300)

    def lambda_8D49():
        OP_8E(0xFE, 0xFFFFB546, 0x0, 0xFFFFEFB6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_8D49)
    Sleep(200)

    def lambda_8D69():
        OP_8E(0xFE, 0xFFFFBBE0, 0x0, 0xFFFFEE62, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_8D69)
    Sleep(200)

    def lambda_8D89():
        OP_8E(0xFE, 0xFFFFB5D2, 0x0, 0xFFFFF588, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_8D89)
    Sleep(200)

    def lambda_8DA9():
        OP_8E(0xFE, 0xFFFFBCA8, 0x0, 0xFFFFF3EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_8DA9)
    Sleep(200)

    def lambda_8DC9():
        OP_8E(0xFE, 0xFFFFBD16, 0x0, 0xFFFFFA42, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_8DC9)
    Sleep(200)

    def lambda_8DE9():
        OP_8E(0xFE, 0xFFFFC2C0, 0x0, 0xFFFFF470, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_8DE9)
    Return()

    # Function_58_8AF9 end

    def Function_59_8DFF(): pass

    label("Function_59_8DFF")

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
        (0, "loc_8E78"),
        (1, "loc_8E7E"),
        (SWITCH_DEFAULT, "loc_8E84"),
    )


    label("loc_8E78")

    OP_A2(0x1200)
    Jump("loc_8E84")

    label("loc_8E7E")

    OP_A2(0x1201)
    Jump("loc_8E84")

    label("loc_8E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8E92")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_8E96")

    label("loc_8E92")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_8E96")

    Return()

    # Function_59_8DFF end

    def Function_60_8E97(): pass

    label("Function_60_8E97")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_60_8E97 end

    SaveToFile()

Try(main)
