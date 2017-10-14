from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4105   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4105.x',
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
        'Finella',                              # 9
        'Carnero',                              # 10
        'Tiffany',                              # 11
        'Mechanic Payton',                      # 12
        'Rutherford',                           # 13
        'Anton',                                # 14
        'Ricky',                                # 15
        'Kitty',                                # 16
        'Nemo',                                 # 17
        'Clare',                                # 18
        'Elderly Man',                          # 19
        'Elderly Woman',                        # 20
        'Middle-Aged Man',                      # 21
        'Middle-Aged Woman',                    # 22
        'Young Man',                            # 23
        'Young Woman',                          # 24
        'Airship Passenger',                    # 25
        'Airship Passenger',                    # 26
        'Airship Passenger',                    # 27
        'Airship Passenger',                    # 28
        'Airship Passenger',                    # 29
        'Airship Passenger',                    # 30
        'Airship Passenger',                    # 31
        'Airship Passenger',                    # 32
        'Olivier',                              # 33
        'Kloe',                                 # 34
        'Tita',                                 # 35
        'Zin',                                  # 36
        'Major Vander',                         # 37
        'Renne',                                # 38
        'Nial',                                 # 39
        'Dorothy',                              # 40
        'グレトナ号影',                         # 41
        'Airliner, Gretna',                     # 42
        'Scherazard',                           # 43
        'Agate',                                # 44
        'Father Kevin',                         # 45
        'Dummy',                                # 46
        'Grancel - East Block',                 # 47
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01010 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH00030 ._CH',             # 07
        'ED6_DT07/CH00040 ._CH',             # 08
        'ED6_DT07/CH00060 ._CH',             # 09
        'ED6_DT07/CH00070 ._CH',             # 0A
        'ED6_DT27/CH03570 ._CH',             # 0B
        'ED6_DT27/CH03510 ._CH',             # 0C
        'ED6_DT07/CH02060 ._CH',             # 0D
        'ED6_DT07/CH02070 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT07/CH00050 ._CH',             # 10
        'ED6_DT27/CH03080 ._CH',             # 11
        'ED6_DT06/CH20063 ._CH',             # 12
        'ED6_DT06/CH20064 ._CH',             # 13
        'ED6_DT06/CH20038 ._CH',             # 14
        'ED6_DT26/CH20311 ._CH',             # 15
        'ED6_DT07/CH01450 ._CH',             # 16
        'ED6_DT07/CH01550 ._CH',             # 17
        'ED6_DT07/CH01140 ._CH',             # 18
        'ED6_DT07/CH01770 ._CH',             # 19
        'ED6_DT07/CH01470 ._CH',             # 1A
        'ED6_DT07/CH01590 ._CH',             # 1B
        'ED6_DT07/CH01480 ._CH',             # 1C
        'ED6_DT07/CH01490 ._CH',             # 1D
        'ED6_DT07/CH01200 ._CH',             # 1E
        'ED6_DT07/CH01230 ._CH',             # 1F
        'ED6_DT07/CH01150 ._CH',             # 20
        'ED6_DT07/CH01460 ._CH',             # 21
        'ED6_DT07/CH01470 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01010P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH00030P._CP',             # 07
        'ED6_DT07/CH00040P._CP',             # 08
        'ED6_DT07/CH00060P._CP',             # 09
        'ED6_DT07/CH00070P._CP',             # 0A
        'ED6_DT27/CH03570P._CP',             # 0B
        'ED6_DT27/CH03510P._CP',             # 0C
        'ED6_DT07/CH02060P._CP',             # 0D
        'ED6_DT07/CH02070P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT07/CH00050P._CP',             # 10
        'ED6_DT27/CH03080P._CP',             # 11
        'ED6_DT06/CH20063P._CP',             # 12
        'ED6_DT06/CH20064P._CP',             # 13
        'ED6_DT06/CH20038P._CP',             # 14
        'ED6_DT26/CH20311P._CP',             # 15
        'ED6_DT07/CH01450P._CP',             # 16
        'ED6_DT07/CH01550P._CP',             # 17
        'ED6_DT07/CH01140P._CP',             # 18
        'ED6_DT07/CH01770P._CP',             # 19
        'ED6_DT07/CH01470P._CP',             # 1A
        'ED6_DT07/CH01590P._CP',             # 1B
        'ED6_DT07/CH01480P._CP',             # 1C
        'ED6_DT07/CH01490P._CP',             # 1D
        'ED6_DT07/CH01200P._CP',             # 1E
        'ED6_DT07/CH01230P._CP',             # 1F
        'ED6_DT07/CH01150P._CP',             # 20
        'ED6_DT07/CH01460P._CP',             # 21
        'ED6_DT07/CH01470P._CP',             # 22
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 83950,
        Z                   = 1500,
        Y                   = 142840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 82520,
        Z                   = 1500,
        Y                   = 142760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = -10000,
        Y                   = 163540,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 68650,
        Z                   = 250,
        Y                   = 147890,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 55860,
        Z                   = 250,
        Y                   = 134560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 54740,
        Z                   = 250,
        Y                   = 134560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 56060,
        Z                   = 250,
        Y                   = 145340,
        Direction           = 169,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 64980,
        Z                   = 250,
        Y                   = 147870,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 66300,
        Z                   = 250,
        Y                   = 147820,
        Direction           = 253,
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
        X                   = 53780,
        Z                   = 250,
        Y                   = 136340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 62390,
        Z                   = 0,
        Y                   = 144850,
        Direction           = 246,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 60950,
        Z                   = 0,
        Y                   = 143420,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 53110,
        Z                   = 250,
        Y                   = 145310,
        Direction           = 322,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 62500,
        Z                   = -3000,
        Y                   = 170810,
        Direction           = 101,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 57230,
        Z                   = 250,
        Y                   = 138300,
        Direction           = 134,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 66300,
        Z                   = 250,
        Y                   = 147820,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 64980,
        Z                   = 250,
        Y                   = 147870,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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
        X                   = 48500,
        Y                   = -200,
        Z                   = 94500,
        Range               = 53500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x17318,
        Unknown_18          = 0x0,
        Unknown_1C          = 39,
    )


    DeclActor(
        TriggerX            = 56800,
        TriggerZ            = 250,
        TriggerY            = 136940,
        TriggerRange        = 800,
        ActorX              = 58770,
        ActorZ              = 1750,
        ActorY              = 137000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53710,
        TriggerZ            = 250,
        TriggerY            = 137720,
        TriggerRange        = 800,
        ActorX              = 53710,
        ActorZ              = 2450,
        ActorY              = 137720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 44,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71160,
        TriggerZ            = -10000,
        TriggerY            = 151550,
        TriggerRange        = 800,
        ActorX              = 71160,
        ActorZ              = -8500,
        ActorY              = 151550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 45,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_72E",          # 00, 0
        "Function_1_811",          # 01, 1
        "Function_2_8DA",          # 02, 2
        "Function_3_8F0",          # 03, 3
        "Function_4_8F5",          # 04, 4
        "Function_5_1155",         # 05, 5
        "Function_6_1218",         # 06, 6
        "Function_7_1335",         # 07, 7
        "Function_8_14C4",         # 08, 8
        "Function_9_14CB",         # 09, 9
        "Function_10_1545",        # 0A, 10
        "Function_11_157C",        # 0B, 11
        "Function_12_15E7",        # 0C, 12
        "Function_13_1611",        # 0D, 13
        "Function_14_1632",        # 0E, 14
        "Function_15_16A1",        # 0F, 15
        "Function_16_16DE",        # 10, 16
        "Function_17_1742",        # 11, 17
        "Function_18_1809",        # 12, 18
        "Function_19_1849",        # 13, 19
        "Function_20_189A",        # 14, 20
        "Function_21_18D2",        # 15, 21
        "Function_22_18EF",        # 16, 22
        "Function_23_32CC",        # 17, 23
        "Function_24_3313",        # 18, 24
        "Function_25_335A",        # 19, 25
        "Function_26_33A1",        # 1A, 26
        "Function_27_33E8",        # 1B, 27
        "Function_28_342F",        # 1C, 28
        "Function_29_3476",        # 1D, 29
        "Function_30_3492",        # 1E, 30
        "Function_31_34DA",        # 1F, 31
        "Function_32_366D",        # 20, 32
        "Function_33_36CE",        # 21, 33
        "Function_34_40EC",        # 22, 34
        "Function_35_4141",        # 23, 35
        "Function_36_41AA",        # 24, 36
        "Function_37_420E",        # 25, 37
        "Function_38_425E",        # 26, 38
        "Function_39_6A9F",        # 27, 39
        "Function_40_6D1B",        # 28, 40
        "Function_41_6DA1",        # 29, 41
        "Function_42_6E1A",        # 2A, 42
        "Function_43_6E9F",        # 2B, 43
        "Function_44_6EC3",        # 2C, 44
        "Function_45_6F8C",        # 2D, 45
    )


    def Function_0_72E(): pass

    label("Function_0_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_75B")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_806")

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_END)), "loc_7DC")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x9, 61450, -3000, 162010, 6)
    SetChrPos(0xA, 61450, -3000, 163810, 180)
    Jump("loc_806")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F8")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_806")

    label("loc_7F8")

    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_806")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_72E end

    def Function_1_811(): pass

    label("Function_1_811")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_836")
    OP_B1("T4105_1")
    Jump("loc_869")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_849")
    OP_B1("T4105_2")
    Jump("loc_869")

    label("loc_849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_860")
    OP_B1("T4105_1")
    Jump("loc_869")

    label("loc_860")

    OP_B1("T4105_3")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 3)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_882")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_89B")
    OP_71(0x5, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    Jump("loc_8B1")

    label("loc_89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_END)), "loc_8B1")
    OP_71(0x5, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)

    label("loc_8B1")

    OP_E5(0xB, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D9")

    label("loc_8CF")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D9")

    Return()

    # Function_1_811 end

    def Function_2_8DA(): pass

    label("Function_2_8DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_8DA")

    label("loc_8EF")

    Return()

    # Function_2_8DA end

    def Function_3_8F0(): pass

    label("Function_3_8F0")

    Call(0, 4)
    Return()

    # Function_3_8F0 end

    def Function_4_8F5(): pass

    label("Function_4_8F5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_906")
    Call(0, 22)
    Jump("loc_1151")

    label("loc_906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_924")

    ChrTalk(    #0
        0x8,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1151")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_110C")
    EventBegin(0x0)
    Fade(1000)
    ClearMapFlags(0x1)
    OP_6D(57940, 250, 137110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 56920, 250, 136300, 85)
    SetChrPos(0xF7, 56810, 250, 137100, 79)
    TurnDirection(0x8, 0xF7, 0)
    OP_0D()

    ChrTalk(    #1
        0x8,
        (
            "Hello and welcome.\x01",
            "Will you be flying with us today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "If you are, you will need to check\x01",
            "in and present your tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AA5")
    TurnDirection(0x106, 0x101, 500)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(    #3
        0x106,
        (
            "#050F#3POnce we check in, we should stick\x01",
            "around and wait for the ship.\x02\x03",

            "Sure you got everything you need?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_AA5")

    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(    #4
        0x103,
        (
            "#020F#3POnce we've checked in, we should\x01",
            "wait here for the ship to arrive.\x02\x03",

            "Are you ready to go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B19")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Still Have Stuff To Do\x01",      # 0
            "Check In\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B81"),
        (1, "loc_BDB"),
        (SWITCH_DEFAULT, "loc_1109"),
    )


    label("loc_B81")

    TurnDirection(0xF7, 0x8, 500)
    OP_8C(0x101, 85, 500)

    ChrTalk(    #5
        0x8,
        "Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Please come by when you\x01",
            "are ready to fly with us.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1109")

    label("loc_BDB")

    TurnDirection(0xF7, 0x8, 500)
    OP_8C(0x101, 85, 500)

    ChrTalk(    #7
        0x8,
        "Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "Please sign these papers, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1011F#5PAh, sure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C62")

    ChrTalk(    #10
        0x106,
        "#3P#053F...*scritch scratch*\x02",
    )

    CloseMessageWindow()
    Jump("loc_C84")

    label("loc_C62")


    ChrTalk(    #11
        0x103,
        "#3P#027F...*scritch scratch*\x02",
    )

    CloseMessageWindow()

    label("loc_C84")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x07\x05Estelle and her companion finished checking in.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x3F2, 2)

    ChrTalk(    #13
        0x8,
        "Thank you, everything is in order.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Please wait in the harbor area\x01",
            "for the next airship arrival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1000F#5POkay!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_DC9")

    ChrTalk(    #16
        0x106,
        (
            "#051F#3PRight, then. Let's find a good bench\x01",
            "and wait for the next ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1E")

    label("loc_DC9")


    ChrTalk(    #17
        0x103,
        (
            "#021F#3PWell, shall we find a particularly comfy\x01",
            "bench to hurry up and wait on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1E")

    OP_DB()
    FadeToDark(2000, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_71(0x9, 0x4)
    ClearMapFlags(0x10)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    ClearMapFlags(0x10)
    OP_48()
    OP_89(0x101, 83040, 1500, 143200, 4)
    OP_89(0xF7, 83180, 1700, 141880, 192)
    OP_6D(83210, 1700, 140260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_ED5():
        OP_8E(0xF7, 0x142BC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_ED5)

    def lambda_EF0():
        OP_8E(0x101, 0x142BC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EF0)

    def lambda_F0B():
        OP_6D(82850, 1700, 135080, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F0B)
    Sleep(4000)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xF7, 0x8)
    OP_6D(87540, 1500, 134660, 0)
    OP_67(0, 12280, -10000, 0)
    OP_6B(6180, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x29, 0x40)
    OP_A1(0x28, 0xB)
    OP_A1(0x29, 0xA)
    OP_72(0xB, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0x9, 0x4)
    SetChrPos(0x28, 87000, -5300, 131150, 90)
    SetChrPos(0x29, 87000, -5300, 131150, 90)
    OP_48()
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(3000)
    OP_6F(0xA, 2)
    OP_70(0xA, 0x64)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xA)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_6F(0xB, 100)
    OP_70(0xA, 0xC8)
    OP_70(0xB, 0xC8)
    OP_73(0xB)
    OP_6F(0xA, 200)
    OP_6F(0xB, 200)
    OP_70(0xA, 0x12C)
    OP_70(0xB, 0x12C)

    def lambda_103B():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_103B)

    def lambda_1056():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1056)
    WaitChrThread(0x29, 0x1)
    Fade(1000)
    OP_6D(108820, 1500, 134250, 0)
    OP_67(0, 9790, -10000, 0)
    OP_6B(7800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_10B8():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 3, lambda_10B8)

    def lambda_10D3():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_10D3)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    WaitChrThread(0x29, 0x3)
    OP_DC()
    NewScene("ED6_DT21/E0000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1109")

    label("loc_1109")

    Jump("loc_1151")

    label("loc_110C")


    ChrTalk(    #18
        0x8,
        (
            "Ticket purchases are handled in\x01",
            "the building nearby, thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1151")

    TalkEnd(0x8)
    Return()

    # Function_4_8F5 end

    def Function_5_1155(): pass

    label("Function_5_1155")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_11E6")

    ChrTalk(    #19
        0xFE,
        (
            "Er... No problems at all in the engine\x01",
            "section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I've finished tuning the orbal pressure...\x01",
            "Is... Is that everything then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1214")

    label("loc_11E6")


    ChrTalk(    #21
        0xFE,
        "Ummmm... The next arriving airship is...\x02",
    )

    CloseMessageWindow()

    label("loc_1214")

    TalkEnd(0xFE)
    Return()

    # Function_5_1155 end

    def Function_6_1218(): pass

    label("Function_6_1218")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12E2")

    ChrTalk(    #22
        0xFE,
        (
            "The final overall check is the job\x01",
            "of the chief engineer, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "More to the point, why are you talking\x01",
            "to me like I'm in charge here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Really, why is it always like this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1331")

    label("loc_12E2")


    ChrTalk(    #25
        0xFE,
        "Ticks me off... The Cecilia just left!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Next is the Linde! THE LINDE!\x02",
    )

    CloseMessageWindow()

    label("loc_1331")

    TalkEnd(0xFE)
    Return()

    # Function_6_1218 end

    def Function_7_1335(): pass

    label("Function_7_1335")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1466")

    ChrTalk(    #27
        0xFE,
        (
            "The new engine's capabilities\x01",
            "are really something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "But it looks like we'll still need to do\x01",
            "multiple flight tests to gather data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "We've also got to think of tuning the\x01",
            "machine to make the most out of its\x01",
            "output.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I'd like to get Professor Russell's\x01",
            "opinion at some point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C0")

    label("loc_1466")


    ChrTalk(    #31
        0xFE,
        "Just a bit longer, just a bit longer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Once the new model engine's finished...\x02",
    )

    CloseMessageWindow()

    label("loc_14C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1335 end

    def Function_8_14C4(): pass

    label("Function_8_14C4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_14C4 end

    def Function_9_14CB(): pass

    label("Function_9_14CB")

    OP_EA(0x1, 0xD, 0x0, 0x0)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1541")

    ChrTalk(    #33
        0xFE,
        (
            "Yeah!! If you're a real man, you have\x01",
            "to open your own road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "The time to set forth has come!\x02",
    )

    CloseMessageWindow()

    label("loc_1541")

    TalkEnd(0xFE)
    Return()

    # Function_9_14CB end

    def Function_10_1545(): pass

    label("Function_10_1545")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1578")

    ChrTalk(    #35
        0xFE,
        "Haha! It's never boring with Anton.\x02",
    )

    CloseMessageWindow()

    label("loc_1578")

    TalkEnd(0xFE)
    Return()

    # Function_10_1545 end

    def Function_11_157C(): pass

    label("Function_11_157C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_15E3")

    ChrTalk(    #36
        0xFE,
        "I've finally found what I want to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "That's why I plan on going to Bose\x01",
            "to study.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E3")

    TalkEnd(0xFE)
    Return()

    # Function_11_157C end

    def Function_12_15E7(): pass

    label("Function_12_15E7")

    TalkBegin(0xFE)

    ChrTalk(    #38
        0xFE,
        "You take care while I'm away.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_15E7 end

    def Function_13_1611(): pass

    label("Function_13_1611")

    TalkBegin(0xFE)

    ChrTalk(    #39
        0xFE,
        "Mama, see you later!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1611 end

    def Function_14_1632(): pass

    label("Function_14_1632")

    TalkBegin(0xFE)

    ChrTalk(    #40
        0xFE,
        (
            "This is my first time riding an\x01",
            "airship alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Wh-What? I'm not n-nervous!!\x01",
            "N-Nope, not me!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1632 end

    def Function_15_16A1(): pass

    label("Function_15_16A1")

    TalkBegin(0xFE)

    ChrTalk(    #42
        0xFE,
        (
            "Grandpa, I wanna ride that airship\x01",
            "over theeere!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_16A1 end

    def Function_16_16DE(): pass

    label("Function_16_16DE")

    TalkBegin(0xFE)

    ChrTalk(    #43
        0xFE,
        "Th-That's the queen's airship, sweetie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "I-I mean, I kind of want to ride it too...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_16DE end

    def Function_17_1742(): pass

    label("Function_17_1742")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 3)), scpexpr(EXPR_END)), "loc_17AA")

    ChrTalk(    #45
        0xFE,
        "Wh-What on earth...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Those two who just came out glared\x01",
            "at me something fierce!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1805")

    label("loc_17AA")


    ChrTalk(    #47
        0xFE,
        (
            "This is the airship company's\x01",
            "headquarters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "It's a nice looking building.\x02",
    )

    CloseMessageWindow()

    label("loc_1805")

    TalkEnd(0xFE)
    Return()

    # Function_17_1742 end

    def Function_18_1809(): pass

    label("Function_18_1809")

    TalkBegin(0xFE)

    ChrTalk(    #49
        0xFE,
        "So this is the Arseille!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "What a lovely ship...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1809 end

    def Function_19_1849(): pass

    label("Function_19_1849")

    TalkBegin(0xFE)

    ChrTalk(    #51
        0xFE,
        (
            "If we ride the next airship, when\x01",
            "will we arrive at Zeiss, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1849 end

    def Function_20_189A(): pass

    label("Function_20_189A")

    TalkBegin(0xFE)

    ChrTalk(    #52
        0xFE,
        (
            "Listen, you have to be good and\x01",
            "keep quiet.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_189A end

    def Function_21_18D2(): pass

    label("Function_21_18D2")

    TalkBegin(0xFE)

    ChrTalk(    #53
        0xFE,
        "Yeah, I promise!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_18D2 end

    def Function_22_18EF(): pass

    label("Function_22_18EF")

    EventBegin(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1919")
    Call(0, 40)
    Call(0, 42)
    FadeToBright(0, 0)

    label("loc_1919")

    Fade(1000)
    OP_6D(57660, 250, 137100, 0)
    OP_67(0, 8420, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 56940, 250, 136330, 90)
    SetChrPos(0xF7, 56900, 250, 137490, 90)
    SetChrPos(0xF8, 55560, 250, 135910, 90)
    SetChrPos(0xF9, 55480, 250, 137370, 90)
    OP_8C(0x8, 276, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C17")
    OP_A2(0x163E)

    ChrTalk(    #54
        0x8,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "You're the party of bracers heading\x01",
            "for Bose, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1011FYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Very good. We've received your fare\x01",
            "from Elnan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        "Are you ready to check in?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1AE3")

    ChrTalk(    #59
        0x106,
        (
            "#050F#6PAs usual, we should wait here once\x01",
            "we check in.\x02\x03",

            "Got anything left to do around town?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6C")

    label("loc_1AE3")


    ChrTalk(    #60
        0x103,
        (
            "#020F#6PJust like last time, we should wait here\x01",
            "for the ship if we check in.\x02\x03",

            "Do you have any unfinished business here\x01",
            "in Grancel?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Still Have Things To Do\x01",      # 0
            "All Done\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C14")

    ChrTalk(    #61
        0x8,
        (
            "Well, once your business is concluded,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_1C14")

    Jump("loc_1CE8")

    label("loc_1C17")


    ChrTalk(    #62
        0x8,
        (
            "Ah, hello.\x01",
            "Will you be checking in?\x02",
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
            "Still Have Things To Do\x01",      # 0
            "All Done\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE8")

    ChrTalk(    #63
        0x8,
        (
            "Well, once your business is concluded,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_1CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D98")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(56610, 250, 137000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 56610, 250, 137000, 90)
    SetChrPos(0x1, 56610, 250, 137000, 90)
    SetChrPos(0x2, 56610, 250, 137000, 90)
    SetChrPos(0x3, 56610, 250, 137000, 90)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_1D98")

    OP_E9(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xCA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E48")
    OP_4F(0xCA, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(56610, 250, 137000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 56610, 250, 137000, 90)
    SetChrPos(0x1, 56610, 250, 137000, 90)
    SetChrPos(0x2, 56610, 250, 137000, 90)
    SetChrPos(0x3, 56610, 250, 137000, 90)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_1E48")


    ChrTalk(    #64
        0x8,
        "Very well.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)

    ChrTalk(    #65
        0x8,
        (
            "I will contact the guild branch and call\x01",
            "the rest of your party.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #66
        "\x07\x05Estelle's group began to wait for the next passenger ship.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Call(0, 31)
    OP_6D(87590, 1500, 142760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 91000, 1500, 143280, 270)
    SetChrPos(0x103, 91860, 1500, 142720, 270)
    SetChrPos(0x106, 91910, 1500, 143800, 270)
    SetChrPos(0x105, 93140, 1500, 142720, 270)
    SetChrPos(0x107, 92990, 1500, 143800, 270)
    SetChrPos(0x108, 94220, 1500, 142720, 270)
    SetChrPos(0x104, 94240, 1500, 143800, 270)
    SetChrPos(0x12, 82860, 1500, 143460, 180)
    SetChrPos(0x13, 84050, 1500, 143590, 270)
    SetChrPos(0x14, 86810, 1500, 143690, 270)
    SetChrPos(0x15, 88180, 1500, 143410, 270)
    SetChrPos(0x16, 85280, 1500, 143380, 270)
    SetChrPos(0x17, 89440, 1500, 143050, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_6F(0xA, 60)
    OP_6F(0x5, 100)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x1, 0x5A)
    Sleep(3000)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_71(0x9, 0x4)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 100)
    OP_70(0x5, 0xC8)
    OP_73(0x5)
    OP_43(0x12, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0x13, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0x16, 0x1, 0x0, 0x17)
    Sleep(600)
    OP_43(0x14, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0x17, 0x1, 0x0, 0x17)
    Sleep(500)

    def lambda_2137():
        OP_8E(0xFE, 0x14564, 0x5DC, 0x22FB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2137)
    Sleep(500)

    def lambda_2157():
        OP_6D(83300, 1500, 143110, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2157)

    def lambda_216F():
        OP_8E(0xFE, 0x14C94, 0x5DC, 0x22D80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_216F)
    Sleep(200)

    def lambda_218F():
        OP_8E(0xFE, 0x14CEE, 0x5DC, 0x231B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_218F)
    Sleep(100)

    def lambda_21AF():
        OP_8E(0xFE, 0x150E0, 0x5DC, 0x231B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_21AF)
    Sleep(100)

    def lambda_21CF():
        OP_8E(0xFE, 0x15112, 0x5DC, 0x22D80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_21CF)
    Sleep(100)

    def lambda_21EF():
        OP_8E(0xFE, 0x15572, 0x5DC, 0x231B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21EF)
    Sleep(100)

    def lambda_220F():
        OP_8E(0xFE, 0x1559A, 0x5DC, 0x22D80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_220F)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    SetChrPos(0x26, 73360, 1500, 142950, 90)
    SetChrPos(0x27, 73360, 1500, 143830, 90)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    NpcTalk(    #67
        0x26,
        "Man's Voice",
        "#1PThank Aidios, we made it in time!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 400)

    def lambda_2363():
        OP_6D(81000, 1500, 142960, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2363)

    def lambda_237B():
        OP_67(0, 7210, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_237B)

    def lambda_2393():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2393)

    def lambda_23A3():
        OP_6B(2270, 3000)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_23A3)

    def lambda_23B3():
        OP_6E(362, 3000)
        ExitThread()

    QueueWorkItem(0x26, 3, lambda_23B3)

    def lambda_23C3():
        OP_8E(0xFE, 0x135F6, 0x5DC, 0x22E66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_23C3)
    Sleep(500)

    def lambda_23E3():
        OP_8E(0xFE, 0x133E4, 0x5DC, 0x231D6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_23E3)
    WaitChrThread(0x26, 0x1)
    WaitChrThread(0x26, 0x2)

    ChrTalk(    #68
        0x101,
        "#1004F#5PHuh? Nial! And Dorothy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x27,
        "#154F#4PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x26,
        (
            "#145F#4PPhew! Thought we'd missed you.\x01",
            "We stopped by the guild, but they said\x01",
            "you'd left already.\x02\x03",

            "#140FGlad we managed to catch you before your\x01",
            "flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#5PUm... What's wrong?\x02\x03",

            "I thought we told you everything\x01",
            "about the case last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x26,
        "#142F#4PIt...ain't that.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x26, 135, 400)
    Sleep(500)
    TurnDirection(0x26, 0x101, 400)
    Sleep(500)

    ChrTalk(    #73
        0x26,
        (
            "#140F#4PWe've got somethin' to tell you personally.\x02\x03",

            "You mind speaking with us, ah, alone-like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1004F#5PMe?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #75
        0x101,
        "#1015F#2PUm, Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#027FGo ahead, Estelle. Hear them out.\x02\x03",

            "I'll be sure to save you a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1006F#2PThanks, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#040F#5PGood day, then, Nial, Dorothy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        "#061F#5PBye-bye!\x02",
    )

    CloseMessageWindow()

    def lambda_26C9():
        OP_8E(0xFE, 0x13D4E, 0x5DC, 0x22FB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26C9)

    def lambda_26E4():
        OP_6D(79800, 1500, 143330, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26E4)

    def lambda_26FC():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_26FC)
    OP_43(0x103, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0x106, 0x1, 0x0, 0x19)
    Sleep(300)
    OP_43(0x107, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x1B)
    Sleep(300)
    OP_43(0x108, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x1D)
    Sleep(4000)

    ChrTalk(    #80
        0x101,
        (
            "#1011F#6POkay, so what's all this about?\x01",
            "What's so--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #81
        0x101,
        "#1019F#4PEr. Olivier. Why are you still here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x104,
        (
            "#035FAh! Think of me as...a stone in the\x01",
            "pavement. A butterfly gracing the wind.\x02\x03",

            "#030FPlease, speak freely.\x01",
            "Pay me no mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1007F#4PI swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x26,
        "#142F#4PThat's one helluva talkative stone.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x103, 0x80)
    SetChrPos(0x103, 83210, 1500, 134330, 0)
    OP_8E(0x103, 0x143AC, 0x6A4, 0x22880, 0xFA0, 0x0)

    ChrTalk(    #85
        0x103,
        (
            "#027F#6PI thought this might be the case when\x01",
            "I didn't see him board.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x103, 0x104, 0x1F4, 0xBB8, 0x0)

    ChrTalk(    #86
        0x104,
        "#036F#5PEr, Schera, just a--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#021F#1PLet's get you to your seat,\x01",
            "my DEAR Lenheim.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    def lambda_2996():

        label("loc_2996")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_2996")

    QueueWorkItem2(0x101, 1, lambda_2996)

    def lambda_29A7():

        label("loc_29A7")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_29A7")

    QueueWorkItem2(0x26, 1, lambda_29A7)

    def lambda_29B8():

        label("loc_29B8")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_29B8")

    QueueWorkItem2(0x27, 1, lambda_29B8)
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_29DB():
        OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29DB)
    Sleep(100)

    def lambda_29FB():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_29FB)

    def lambda_2A09():
        OP_8F(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A09)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 20)
    SetChrSubChip(0x104, 5)
    OP_6D(80980, 1500, 139850, 2000)
    WaitChrThread(0x103, 0x1)
    SetChrFlags(0x103, 0x80)
    WaitChrThread(0x104, 0x1)
    SetChrFlags(0x104, 0x80)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x26, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x27, 0x1)
    OP_6D(79960, 1500, 143070, 1500)
    TurnDirection(0x26, 0x101, 400)

    ChrTalk(    #88
        0x26,
        "#142F#4PHe's the same as always, then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x26, 400)

    ChrTalk(    #89
        0x101,
        "#1016F#6PHaha. Pretty much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x27,
        "#154F#4PUm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x27, 400)

    ChrTalk(    #91
        0x101,
        (
            "#1015F#6PDorothy? You look kinda out of it.\x01",
            "Even more so than usual, I mean.\x02\x03",

            "What's wrong? I thought you were\x01",
            "off taking photos in Bose.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x101, 400)
    Sleep(500)

    ChrTalk(    #92
        0x27,
        (
            "#154FYeah... I, um, just got back this morning...\x02\x03",

            "Ummmm, Estellllle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F#6PWait, I remember!\x02\x03",

            "You were off at that old fort in\x01",
            "the misty valley!\x02\x03",

            "The one they're using as a military...\x01",
            "train...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#1004F#6PWait, isn't that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x26,
        (
            "#140F#4PFinally twigged to it, huh?\x02\x03",

            "That's the base the bandits raided last\x01",
            "night.\x02\x03",

            "Dorothy here was literally on the scene\x01",
            "when those thugs took their ship back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1002F#6POh, man, okay.\x02\x03",

            "#1011FSo you came out here to tell us\x01",
            "what happened?\x02\x03",

            "#1001FAwww! Thanks, I appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x26,
        (
            "#145F#4PUh, to 'tell' you what happened.\x01",
            "You might say that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x26,
        (
            "#142F#4PHell with it, it's a thousand words\x01",
            "or a picture. Dorothy, hand it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x27,
        "#154FY-Yes, sir...\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_8E(0x27, 0x13A6A, 0x5DC, 0x22FBA, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #101
        0x27,
        (
            "#155F#4PUmmm...Estelle?\x02\x03",

            "Don't go crazy about this, okay?\x02\x03",

            "Pictures don't always tell the whole truth,\x01",
            "forever! Or something. Or, did I just insult\x01",
            "myse--umm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1008F#6PWhat's all this about?\x01",
            "Why do you look so serious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x27,
        "#154F#4PI...um...took this picture.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #104
        "\x07\x05Dorothy handed Estelle a single photograph.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x41A, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AD(0x240091, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetMessageWindowPos(100, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #105
        (
            "\x07\x00#1015F#6PUh, lesse... I recognize Miss Tomboy\x01",
            "the bandit over there.\x02\x03",

            "And that would...be...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("Estelle")

    AnonymousTalk(    #106
        "\x07\x00#1004F#3SWhat...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0x27, 79680, 1500, 144000, 90)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #107
        0x26,
        (
            "#142F#4PI'm...holding off on giving this photo\x01",
            "to the army for the moment.\x02\x03",

            "I won't run it in the paper, either.\x02\x03",

            "I'll let you...deal with it how you want.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x26, 0x3, 0x0, 0x1E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 32)
    Sleep(1000)
    OP_AD(0x2400B0, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_28(0xA9, 0x4, 0x40)
    OP_28(0xAA, 0x4, 0x40)
    OP_28(0xAB, 0x4, 0x40)
    OP_28(0xAC, 0x4, 0x40)
    OP_A2(0x1683)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0x10, 0x0, 0x0, 0x0)

    Menu(
        0,
        240,
        180,
        0,
        (
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3293")
    ShowSaveMenu()

    label("loc_3293")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A3(0x1683)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1683)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_18EF end

    def Function_23_32CC(): pass

    label("Function_23_32CC")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_32CC end

    def Function_24_3313(): pass

    label("Function_24_3313")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_3313 end

    def Function_25_335A(): pass

    label("Function_25_335A")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_335A end

    def Function_26_33A1(): pass

    label("Function_26_33A1")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_33A1 end

    def Function_27_33E8(): pass

    label("Function_27_33E8")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_33E8 end

    def Function_28_342F(): pass

    label("Function_28_342F")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_342F end

    def Function_29_3476(): pass

    label("Function_29_3476")

    OP_8E(0xFE, 0x143F2, 0x5DC, 0x2335C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_3476 end

    def Function_30_3492(): pass

    label("Function_30_3492")

    Sleep(600)
    OP_24(0x75, 0x50)
    Sleep(300)
    OP_24(0x75, 0x46)
    Sleep(300)
    OP_24(0x75, 0x3C)
    Sleep(300)
    OP_24(0x75, 0x32)
    Sleep(300)
    OP_24(0x75, 0x28)
    Sleep(300)
    OP_24(0x75, 0x1E)
    Sleep(300)
    OP_24(0x75, 0x14)
    Sleep(300)
    OP_23(0x75)
    Return()

    # Function_30_3492 end

    def Function_31_34DA(): pass

    label("Function_31_34DA")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3513")
    AddParty(0x5, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3513")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3538")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3585")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_356D")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3585")

    label("loc_356D")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35FA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35BA")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_35FA")

    label("loc_35BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E2")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_35FA")

    label("loc_35E2")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_35FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3647")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362F")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3647")

    label("loc_362F")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3647")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_366C")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_366C")

    Return()

    # Function_31_34DA end

    def Function_32_366D(): pass

    label("Function_32_366D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_367D")
    RemoveParty(0x5, 0xFF)

    label("loc_367D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_368D")
    RemoveParty(0x2, 0xFF)

    label("loc_368D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_369D")
    RemoveParty(0x6, 0xFF)

    label("loc_369D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_36AD")
    RemoveParty(0x3, 0xFF)

    label("loc_36AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_36BD")
    RemoveParty(0x4, 0xFF)

    label("loc_36BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_36CD")
    RemoveParty(0x7, 0xFF)

    label("loc_36CD")

    Return()

    # Function_32_366D end

    def Function_33_36CE(): pass

    label("Function_33_36CE")

    ClearMapFlags(0x1)
    ClearMapFlags(0x80)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_DB()
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x9, 0x4)
    ClearMapFlags(0x10)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(83480, 1500, 131810, 0)
    OP_67(0, 15200, -10000, 0)
    OP_6B(7000, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    OP_6F(0x5, 100)
    OP_6F(0xA, 410)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x29, 0x40)
    OP_A1(0x28, 0xB)
    OP_A1(0x29, 0xA)
    OP_72(0xB, 0x4)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 390)
    OP_70(0xA, 0x12C)
    FadeToBright(3000, 0)
    SetChrPos(0x28, 87000, -5100, 130500, 90)
    SetChrPos(0x29, 87000, 5500, 130500, 90)

    def lambda_37D3():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37D3)

    def lambda_37E3():
        OP_67(0, 11200, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37E3)

    def lambda_37FB():
        OP_6B(3500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37FB)
    OP_43(0x2D, 0x0, 0x0, 0x2B)

    def lambda_3812():
        OP_8F(0xFE, 0x153D8, 0xFFFFE9EE, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_3812)
    WaitChrThread(0x29, 0x2)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(100)
    OP_72(0xA, 0x20)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xA, 80)
    OP_70(0xA, 0x1)
    Sleep(2700)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x0)
    Sleep(3000)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    OP_73(0xA)
    Sleep(300)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x10A, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    SetChrBattleFlags(0x13, 0x20)
    SetChrBattleFlags(0x14, 0x20)
    SetChrBattleFlags(0x15, 0x20)
    SetChrBattleFlags(0x16, 0x20)
    OP_48()
    OP_89(0x12, 86970, 1700, 130570, 189)
    OP_89(0x13, 89160, 1500, 133510, 189)
    OP_89(0x14, 86970, 1700, 130570, 189)
    OP_89(0x15, 86970, 1700, 130570, 189)
    OP_89(0x16, 89160, 1500, 133510, 189)
    OP_89(0x101, 86970, 1700, 130570, 189)
    OP_89(0x10A, 86970, 1700, 130570, 189)
    OP_43(0x12, 0x1, 0x0, 0x23)
    Sleep(1000)
    OP_43(0x13, 0x1, 0x0, 0x22)
    Sleep(2000)
    OP_43(0x14, 0x1, 0x0, 0x23)
    Sleep(1000)
    OP_43(0x15, 0x1, 0x0, 0x23)
    Sleep(1000)
    OP_43(0x16, 0x1, 0x0, 0x22)
    Sleep(2000)
    OP_43(0x10A, 0x1, 0x0, 0x24)
    Sleep(800)
    OP_43(0x101, 0x1, 0x0, 0x25)
    Sleep(4000)
    Fade(1000)
    OP_6D(82440, 1500, 142990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x10A, 0x1)
    OP_DC()
    Sleep(500)

    ChrTalk(    #108
        0x10A,
        (
            "#819F*phewwwww*\x02\x03",

            "Being on an airship for over half\x01",
            "a day is kinda tiring, huh?\x02\x03",

            "#810FI know how to stretch our legs, though.\x01",
            "Let's go report the completion of our\x01",
            "training and duty-readiness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1015F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10A,
        "#814FUh, Estelle? Hello?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1025F#6POh, yeah...\x02\x03",

            "You're right, we should go\x01",
            "say hi to Elnan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10A,
        (
            "#810FHeeey... Are you...\x02\x03",

            "Estelle, you've got a case of\x01",
            "the nerves, don'cha?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1007F#6PI... Yeah, I do.\x01",
            "I dunno why, either...\x02\x03",

            "#1026FI didn't feel this way AT ALL before\x01",
            "I went to training, but now...\x02\x03",

            "Somehow, thinking that I'm really\x01",
            "going to be a full bracer now is\x01",
            "making me really, really antsy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10A,
        (
            "#810FHeheh! I get it.\x02\x03",

            "#1314FYou're trembling with\x01",
            "excitement, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1004F#6PExcitement? Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10A,
        (
            "#816FYou've grown way, way stronger\x01",
            "over this past month, Estelle.\x02\x03",

            "And not just in, like, the whacking-stuff-with-\x01",
            "a-stick department. You're more knowledgeable,\x01",
            "careful, and you make better judgments.\x02\x03",

            "#817FAnd now you're about to start hunting down the\x01",
            "mystery creepos who want to doom us all or\x01",
            "whatever, and you're gonna bring Joshua back...\x02\x03",

            "#816FI bet all that's only just now sinking in for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1004F#6PHmm...\x02\x03",

            "#1000FYeah. When you put it that way,\x01",
            "that is how I'm feeling...\x02\x03",

            "#1007F*sigh* I'm such a dimwit.\x02\x03",

            "I'm like a mountain climber who didn't\x01",
            "even bother looking up at how big the\x01",
            "mountain before her is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x10A,
        (
            "#1314FHaving second thoughts\x01",
            "about climbing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1006F#6PNo way! If anything, I'm even more\x01",
            "fired up now than I used to be.\x02\x03",

            "No matter how big a mountain is, you can\x01",
            "only climb it one step at a time, anyway.\x02\x03",

            "#1018FEven if I have to crawl, I'll reach\x01",
            "the top no matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10A,
        (
            "#811FHeehee! That's more like it!\x02\x03",

            "#1310FOkay, are we gonna head over\x01",
            "to the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1006F#6PLet's go!\x02",
    )

    CloseMessageWindow()
    FadeToBright(1500, 0)
    OP_0D()
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_36CE end

    def Function_34_40EC(): pass

    label("Function_34_40EC")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x14438, 0x6A4, 0x20832, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 278, 1000)
    OP_8E(0xFE, 0x110DA, 0x640, 0x22ED4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_40EC end

    def Function_35_4141(): pass

    label("Function_35_4141")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x14938, 0x6A4, 0x1FD6A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142B2, 0x6A4, 0x2071A, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 278, 1000)
    OP_8E(0xFE, 0x110DA, 0x640, 0x22ED4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_4141 end

    def Function_36_41AA(): pass

    label("Function_36_41AA")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1491A, 0x640, 0x1FFCC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14406, 0x5DC, 0x2097C, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13E8E, 0x5DC, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 500)
    Return()

    # Function_36_41AA end

    def Function_37_420E(): pass

    label("Function_37_420E")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x14820, 0x640, 0x1FFCC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14406, 0x5DC, 0x2097C, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 500)
    Return()

    # Function_37_420E end

    def Function_38_425E(): pass

    label("Function_38_425E")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_22(0x75, 0x0, 0x64)
    OP_71(0x9, 0x4)
    ClearMapFlags(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_428A")
    Call(0, 40)

    label("loc_428A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_429C")
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x5, 0xF8, 0xFF)
    Jump("loc_42A4")

    label("loc_429C")

    AddParty(0x5, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)

    label("loc_42A4")

    OP_6D(83200, 1500, 143040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 83490, 1700, 143700, 180)
    SetChrPos(0xF7, 82560, 1700, 143700, 180)
    SetChrPos(0xF8, 83490, 1700, 142100, 360)
    SetChrPos(0x10A, 82560, 1700, 142100, 360)
    SetChrPos(0x17, 81620, 1500, 115180, 360)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6C(135000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_496B")

    ChrTalk(    #122
        0x106,
        (
            "#053FRight, then.\x01",
            "We'll head out ahead of you two.\x02\x03",

            "#050F...Yo. Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1011F#6PHm? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x106,
        (
            "#050FThere'll be times when you gotta\x01",
            "put your foot down, be stubborn,\x01",
            "and push yourself, but...\x02\x03",

            "Remember, you're a woman, too.\x02\x03",

            "You can rely on others and\x01",
            "admit your weaknesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1026F#6PWhat...?\x02\x03",

            "#1002FWhat the hell? Are you making\x01",
            "fun of me because I'm a girl?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x106,
        (
            "#053FNo, that ain't... Damn it,\x01",
            "I'm bad at this. Look...\x02\x03",

            "#552FMen are big, dumb oafs who are too friggin'\x01",
            "stubborn to ask for help for their own good,\x01",
            "ninety-five percent of the time.\x02\x03",

            "Me, your old man...Joshua. We're all like\x01",
            "that. Society kinda expects it, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1026F#6PUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x106,
        (
            "#051FWe're all stubborn idiots, for better or worse.\x01",
            "You can't change that no matter what you do.\x02\x03",

            "My point is, there's no reason for you,\x01",
            "a woman, to get stuck thinkin' like that.\x02\x03",

            "Don't forget to ask others for help when\x01",
            "you need it. You've got a lot of friends\x01",
            "out there. Make use of 'em!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1017F#6PAgate...\x02\x03",

            "I'll remember that. Thanks.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x106, 400)

    ChrTalk(    #130
        0x103,
        (
            "#027F#6POho? Showing your soft side\x01",
            "for once, Agate? I'll give an A for effort,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x106, 400)

    ChrTalk(    #131
        0x10A,
        (
            "#1310FYeah, uh, hold the presses,\x01",
            "I need to get my jaw off the floor!\x02\x03",

            "#811FEven AGATE can be nice to girls...sorta!\x01",
            "Aidios does grant miracles!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x103, 400)

    ChrTalk(    #132
        0x106,
        "#054FThe heck's THAT supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x10A,
        "#1315FAh..haha! It's a joke, really!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 400)

    def lambda_4915():
        TurnDirection(0x106, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4915)
    Sleep(100)

    def lambda_4928():
        TurnDirection(0x103, 0x10A, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4928)
    Sleep(300)

    ChrTalk(    #134
        0x10A,
        (
            "#1314FGuess this is goodbye for now,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CF7")

    label("loc_496B")


    ChrTalk(    #135
        0x103,
        (
            "#021FOkay, we'll get a bit of an early start,\x01",
            "then.\x02\x03",

            "#020FEstelle...you'd just gotten back, too.\x01",
            "I'm sorry we couldn't spend more time\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1016F#6PMe too...\x02\x03",

            "#1011FIt sounds like Aina and Rolent really\x01",
            "need some help too, though.\x02\x03",

            "Be sure to say hi to everyone for me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x103,
        (
            "#020FYou got it.\x02\x03",

            "...Estelle. I'm sure you're fine, but...\x02\x03",

            "Don't fret yourself to loose ends, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1026F#6PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#026FMy tarot tells me that the bond between\x01",
            "you and Joshua has not been severed...\x01",
            "yet.\x02\x03",

            "#020FSo...don't worry.\x01",
            "Believe in your connection to him.\x02\x03",

            "Follow it and your trail will be clear.\x01",
            "I know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1017F#6PYeah...\x02\x03",

            "Thanks, Schera.\x01",
            "I feel a lot braver now.\x02\x03",

            "#1003FI...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#021FCome on now, don't make that face.\x02\x03",

            "#027FYou're a full bracer, remember?\x01",
            "Be proud of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1017F#6P...Right, I am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10A,
        (
            "#1314FHeehee!\x02\x03",

            "So...Estelle.\x01",
            "Guess this is goodbye for now, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF7")


    ChrTalk(    #144
        0x101,
        (
            "#1017F#6PAnelace...\x02\x03",

            "Thanks for going with me on my training.\x02\x03",

            "Schera asked you to come\x01",
            "along with me, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4D85")

    ChrTalk(    #145
        0x103,
        "#023FErm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D99")

    label("loc_4D85")


    ChrTalk(    #146
        0x103,
        "#023F#6PErm...\x02",
    )

    CloseMessageWindow()

    label("loc_4D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4DAE")
    TurnDirection(0x103, 0x101, 400)
    TurnDirection(0x106, 0x103, 400)

    label("loc_4DAE")


    ChrTalk(    #147
        0x10A,
        (
            "#1315FAck! I've been found out like\x01",
            "a pie-thief in the night!\x02\x03",

            "#810FSchera said having someone who didn't\x01",
            "know Joshua too well around would\x01",
            "help you sort out your feelings.\x02\x03",

            "So yeah, she asked me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1001F#6PHaha... I thought so.\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x103, 0x10A, 800)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4EF3")

    ChrTalk(    #149
        0x103,
        (
            "#024FWhat th--\x01",
            "Don't tell her EVERYTHING!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F25")

    label("loc_4EF3")


    ChrTalk(    #150
        0x103,
        (
            "#024F#6PWhat th--\x01",
            "Don't tell her EVERYTHING!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F25")

    TurnDirection(0x10A, 0x103, 400)

    ChrTalk(    #151
        0x10A,
        (
            "#819FHey, what's wrong with being\x01",
            "up-front at this point, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4F87")
    TurnDirection(0x103, 0x101, 400)
    TurnDirection(0x10A, 0x106, 400)

    label("loc_4F87")

    Sleep(400)

    ChrTalk(    #152
        0x10A,
        (
            "#816FBut...the real truth is, it wasn't just\x01",
            "that. I did want to train myself, too.\x02\x03",

            "And I really do think I learned a\x01",
            "lot by training with you, Estelle.\x02\x03",

            "#811FSo I've gotta say it, too: thank YOU.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1017F#6PAnelace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10A,
        (
            "#1316FAnd, and, um...\x02\x03",

            "(Okay, deep breaths...)\x01",
            "I know you might think I'm\x01",
            "weird for saying this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#1011F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10A,
        (
            "#1314FI, um, like to think we're already\x01",
            "friends, but...well...\x02\x03",

            "I'd like it if you and me, Estelle,\x01",
            "if we became something...more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#1011F#6P.                .                    .\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #158
        0x101,
        "#1004F#6P#4SWHAAAAAAAAAAAAAAAAA?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5211")
    TurnDirection(0x103, 0x10A, 400)

    label("loc_5211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5259")

    ChrTalk(    #159
        0x103,
        (
            "#023FWha...? Are you saying what I\x01",
            "think you're saying?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529A")

    label("loc_5259")


    ChrTalk(    #160
        0x103,
        (
            "#023F#6PWha...? Are you saying what I\x01",
            "think you're saying?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529A")

    TurnDirection(0x10A, 0x103, 400)

    ChrTalk(    #161
        0x10A,
        (
            "#812FNo! Don't try to stop me, Schera!\x02\x03",

            "I'm serious! I'm absolutely sure about this!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5385")

    ChrTalk(    #162
        0x103,
        (
            "#025F'Serious'...?\x01",
            "Oh... Oh, my...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x106,
        (
            "#552F#6P(Really? Right here? In public? You\x01",
            "have GOT to be freaking kiddin' me...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5405")

    label("loc_5385")


    ChrTalk(    #164
        0x103,
        (
            "#025F#6P'Serious'...?\x01",
            "Oh... Oh, my...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x106,
        (
            "#552F(Really? Right here? In public? You\x01",
            "have GOT to be freaking kiddin' me...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5416")
    TurnDirection(0x10A, 0x103, 400)
    Jump("loc_5424")

    label("loc_5416")

    TurnDirection(0x10A, 0x106, 400)
    TurnDirection(0x103, 0x106, 400)

    label("loc_5424")


    ChrTalk(    #166
        0x10A,
        (
            "#1311FI, well, I know I'm a couple\x01",
            "years older than you, Estelle...\x02\x03",

            "But we've totally spent about the\x01",
            "same amount of time in the guild.\x02\x03",

            "#1314FAnd you know what? Age doesn't matter\x01",
            "when it comes to something like this!\x02\x03",

            "So...what do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1008F#6PU-Umm! Well! Umm...!\x02\x03",

            "#1013FI mean, um, I'm really happy, and I think\x01",
            "my heart is racing out of my chest, but\x01",
            "this is kind of a surprise, to say the least!\x02\x03",

            "Besides, there's, um, Joshua, and there's\x01",
            "kind of some issues on a couple fronts, or\x01",
            "more than a couple...or, rather, I don't, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10A,
        (
            "#814FJoshua? What does he have to do with this?\x02\x03",

            "And what problems would there be on\x01",
            "'a couple fronts' if we become rivals?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x103)
    OP_63(0x106)

    ChrTalk(    #169
        0x101,
        (
            "#1004F#6P... \x01",
            "... \x01",
            "...Rivals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10A,
        (
            "#816FYeah, yeah! We're about the same\x01",
            "age, about equal in skill level...\x02\x03",

            "I thought it'd help us both try\x01",
            "to reach even higher, but...\x02\x03",

            "#1316FYou...don't actually like\x01",
            "the idea, do you...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #171
        0x101,
        (
            "#1016F#6PA-hahahaha...haaaaaa...\x01",
            "That's what you meant...\x01",
            "Ooookay...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_58CE")

    ChrTalk(    #172
        0x103,
        (
            "#025F*siiiigh*...\x01",
            "As unpredictable as always, I see.\x02\x03",

            "Not quite the punch line I was expecting...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5938")

    label("loc_58CE")


    ChrTalk(    #173
        0x103,
        (
            "#025F#6P*siiiigh*...\x01",
            "As unpredictable as always, I see.\x02\x03",

            "Not quite the punch line I was expecting...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5938")


    ChrTalk(    #174
        0x10A,
        "#814FPunch line?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1012F#6PHaha... Well, if that's what you meant...\x02\x03",

            "#1006FAll right, then!\x02\x03",

            "#1018FI, Estelle Bright, hereby recognize you as\x01",
            "my rival, Anelace Elfead! Consider the\x01",
            "gauntlet THROWN! In your face, even!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10A,
        (
            "#811FSweet!\x02\x03",

            "#1310FAll right, step one: a race to see which of us\x01",
            "can reach Agate and Schera's level first! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1006F#6PBring it, sword-brain!\x02\x03",

            "I'll leave you eating my bracer-point dust!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5B9E")

    ChrTalk(    #178
        0x103,
        (
            "#027FOh, boy...\x02\x03",

            "I do believe we are in some amount\x01",
            "of peril, my good Mr. Crosner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x106,
        (
            "#051F#6PHeh, seriously.\x02\x03",

            "Nothin' scarier than a couple kids\x01",
            "charging straight ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C50")

    label("loc_5B9E")


    ChrTalk(    #180
        0x103,
        (
            "#027F#6POh, boy...\x02\x03",

            "I do believe we are in some amount\x01",
            "of peril, my good Mr. Crosner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x106,
        (
            "#051FHeh, seriously.\x02\x03",

            "Nothin' scarier than a couple kids\x01",
            "charging straight ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C50")

    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #182
        (
            "\x07\x05This is the final boarding call for\x01",
            "the Cecilia, bound for Rolent.\x02\x03",

            "All passengers, please embark immediately.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrFlags(0x10A, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5F5F")

    ChrTalk(    #183
        0x106,
        "#052FHey, that's our cue.\x02",
    )

    CloseMessageWindow()

    def lambda_5D20():
        OP_6D(82810, 1580, 137840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D20)

    def lambda_5D38():
        OP_67(0, 6980, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D38)

    def lambda_5D50():
        OP_6B(3130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D50)
    OP_8C(0x106, 180, 400)

    def lambda_5D67():
        OP_8E(0x106, 0x14334, 0x6A4, 0x21F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5D67)
    Sleep(500)
    OP_8C(0x10A, 180, 400)

    def lambda_5D8E():
        OP_8E(0x10A, 0x1438E, 0x5DC, 0x20F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5D8E)

    def lambda_5DA9():
        OP_8E(0x101, 0x14622, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5DA9)
    Sleep(200)

    def lambda_5DC9():
        OP_8E(0x103, 0x14280, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5DC9)
    WaitChrThread(0x106, 0x1)

    def lambda_5DE9():
        OP_8E(0x106, 0x146C2, 0x60E, 0x20904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5DE9)
    Sleep(1000)

    def lambda_5E09():
        OP_8E(0x106, 0x145C8, 0x60E, 0x20B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5E09)

    def lambda_5E24():
        OP_8E(0x10A, 0x1428A, 0x60E, 0x20B34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5E24)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x101, 500)
    WaitChrThread(0x10A, 0x1)

    def lambda_5E50():
        OP_8E(0x10A, 0x14244, 0x60E, 0x2097C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5E50)
    WaitChrThread(0x10A, 0x1)
    TurnDirection(0x10A, 0x101, 500)
    Sleep(500)

    ChrTalk(    #184
        0x106,
        (
            "#051F#4PAll right, then. See ya!\x02\x03",

            "Remember, you find anything, contact us\x01",
            "through the guild--we'll do the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x103,
        "#020F#5POf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1018F#1PSee you, Anelace, Agate!\x01",
            "Stay safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10A,
        "#811F#4PYeah! Good luck, Estelle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_61D6")

    label("loc_5F5F")


    ChrTalk(    #188
        0x103,
        "#023FThat's us, I'm afraid.\x02",
    )

    CloseMessageWindow()

    def lambda_5F86():
        OP_6D(82810, 1580, 137840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F86)

    def lambda_5F9E():
        OP_67(0, 6980, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F9E)

    def lambda_5FB6():
        OP_6B(3130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5FB6)
    OP_8C(0x103, 180, 400)

    def lambda_5FCD():
        OP_8E(0x103, 0x14334, 0x6A4, 0x21F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FCD)
    Sleep(500)
    OP_8C(0x10A, 180, 400)

    def lambda_5FF4():
        OP_8E(0x10A, 0x1438E, 0x5DC, 0x20F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5FF4)

    def lambda_600F():
        OP_8E(0x101, 0x14622, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_600F)
    Sleep(200)

    def lambda_602F():
        OP_8E(0x106, 0x14280, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_602F)
    WaitChrThread(0x106, 0x1)

    def lambda_604F():
        OP_8E(0x103, 0x146C2, 0x60E, 0x20904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_604F)
    Sleep(1000)

    def lambda_606F():
        OP_8E(0x103, 0x145C8, 0x60E, 0x20B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_606F)

    def lambda_608A():
        OP_8E(0x10A, 0x1428A, 0x60E, 0x20B34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_608A)
    WaitChrThread(0x103, 0x1)
    TurnDirection(0x103, 0x101, 500)
    WaitChrThread(0x10A, 0x1)

    def lambda_60B6():
        OP_8E(0x10A, 0x14244, 0x60E, 0x2097C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_60B6)
    WaitChrThread(0x10A, 0x1)
    TurnDirection(0x10A, 0x101, 500)
    Sleep(500)

    ChrTalk(    #189
        0x103,
        (
            "#020F#4PWell, then, you two.\x01",
            "Stay safe.\x02\x03",

            "We'll contact you through the guild\x01",
            "should we find anything. Keep in\x01",
            "touch with us as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x106,
        "#051F#5PWill do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1018F#1PSee you, Anelace, Schera!\x01",
            "Stay safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x10A,
        "#811F#4PYeah! Good luck, Estelle!\x02",
    )

    CloseMessageWindow()

    label("loc_61D6")

    Sleep(100)
    Fade(1000)
    SetChrFlags(0x10A, 0x8)
    SetChrFlags(0xF8, 0x8)
    OP_6D(82160, 1700, 131180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x29, 0x40)
    OP_A1(0x28, 0xB)
    OP_A1(0x29, 0xA)
    OP_72(0xB, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x28, 87000, -5200, 130500, 90)
    SetChrPos(0x29, 87000, -5200, 130500, 90)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(3000)
    OP_6F(0xA, 2)
    OP_70(0xA, 0x64)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xA)
    OP_8C(0x101, 145, 0)
    OP_8C(0xF7, 145, 0)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_6F(0xB, 100)
    OP_70(0xA, 0xC8)
    OP_70(0xB, 0xC8)
    OP_73(0xB)
    OP_6F(0xA, 200)
    OP_6F(0xB, 200)
    OP_70(0xA, 0x12C)
    OP_70(0xB, 0x12C)

    def lambda_62F7():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_62F7)

    def lambda_6312():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6312)
    Sleep(1000)
    Fade(1000)
    OP_6D(91460, 1500, 134290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(6440, 0)
    OP_6C(146000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x29, 0x1)
    Fade(1000)
    OP_6D(108820, 1500, 134250, 0)
    OP_6B(7800, 0)
    OP_67(0, 9790, -10000, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_63BB():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 3, lambda_63BB)

    def lambda_63D6():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_63D6)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    WaitChrThread(0x29, 0x3)
    OP_0D()
    OP_23(0x77)
    OP_72(0x9, 0x4)
    Sleep(1000)
    SetChrPos(0x101, 83630, 1500, 142960, 270)
    SetChrPos(0xF7, 82000, 1500, 142960, 90)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_668B")

    ChrTalk(    #193
        0x101,
        (
            "#1011F#3POkay, then...\x02\x03",

            "Should we finish our check-in and\x01",
            "wait for the next Ruan-bound flight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x103,
        (
            "#026FYes, the ship bound for Ruan\x01",
            "should be arriving soon.\x02\x03",

            "#020FWe could also do some shopping here\x01",
            "in the capital, though. It's your first\x01",
            "time back in a month, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1016F#3PNo, that's fine, I can get\x01",
            "what I need in Ruan.\x02\x03",

            "#1006FLet's finish checking in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x103,
        (
            "#021FHAll right.\x02\x03",

            "#020FThe tickets should be available in the\x01",
            "lobby of the landing port company building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#1006F#3PLet's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_69AE")

    label("loc_668B")


    ChrTalk(    #198
        0x101,
        (
            "#1000F#3POkay, then...\x02\x03",

            "Should we finish our check-in and\x01",
            "wait for the next Ruan-bound flight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x106,
        (
            "#051FYeah, the ship bound for Ruan\x01",
            "oughtta get here soon enough.\x02\x03",

            "Sure you don't want to do some shopping\x01",
            "or something, though? Been a month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#1011F#3PHmmm. I wouldn't mind hitting\x01",
            "the department store, but...\x02\x03",

            "Are you sure you wouldn't mind, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x106,
        (
            "#051FAh, I'm easy, really.\x02\x03",

            "Guys just charge into things without any\x01",
            "planning, you see. Girls're the ones who\x01",
            "actually bother preparing and whatnot.\x02\x03",

            "I say choose what you think is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1016F#3PHaha... Okay.\x02\x03",

            "#1015FHmm... Well, to be honest,\x01",
            "I can get what I need in Ruan.\x02\x03",

            "#1006FLet's just get our tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#051FWorks for me.\x02\x03",

            "Tickets should be sold in the lobby\x01",
            "of the airship company building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1006F#3PLet's go!\x02",
    )

    CloseMessageWindow()

    label("loc_69AE")

    Sleep(100)
    OP_A2(0x1202)
    OP_28(0x81, 0x4, 0x2)
    OP_28(0x81, 0x4, 0x8)
    OP_28(0x81, 0x1, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_69E2")
    OP_28(0x81, 0x1, 0x8)
    OP_28(0x81, 0x1, 0x10)
    OP_28(0x81, 0x1, 0x20)
    Jump("loc_69FB")

    label("loc_69E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_69FB")
    OP_28(0x81, 0x1, 0x1)
    OP_28(0x81, 0x1, 0x2)
    OP_28(0x81, 0x1, 0x4)

    label("loc_69FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6A0B")
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x5, 0xFF)
    Jump("loc_6A11")

    label("loc_6A0B")

    RemoveParty(0x9, 0xFF)
    RemoveParty(0x2, 0xFF)

    label("loc_6A11")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x9, 61450, -3000, 162010, 6)
    SetChrPos(0xA, 61450, -3000, 163810, 180)
    EventEnd(0x0)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    Return()

    # Function_38_425E end

    def Function_39_6A9F(): pass

    label("Function_39_6A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D1A")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_6BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6B33")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #205
        0x106,
        (
            "#050FWhat is it? Gonna go back into town?\x02\x03",

            "We can check in for our flight at the\x01",
            "reception desk outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9D")

    label("loc_6B33")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #206
        0x103,
        (
            "#020FOh, going back into town?\x02\x03",

            "We can check in for our flight at the\x01",
            "reception desk outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9D")

    Jump("loc_6CFF")

    label("loc_6BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6C4F")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #207
        0x106,
        (
            "#052FWhat, wanna do some shoppin' in\x01",
            "town after all?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #208
        0x101,
        (
            "#1016FNo, I'm good.\x02\x03",

            "#1006FLet's go to the waiting area over\x01",
            "there and get our tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CFF")

    label("loc_6C4F")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #209
        0x103,
        (
            "#023FOh, decide you want to do some\x01",
            "shopping in town after all?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #210
        0x101,
        (
            "#1016FNo, I'm good.\x02\x03",

            "#1006FLet's go to the waiting area over\x01",
            "there and get our tickets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CFF")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6D1A")

    Return()

    # Function_39_6A9F end

    def Function_40_6D1B(): pass

    label("Function_40_6D1B")

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
        (0, "loc_6D94"),
        (1, "loc_6D9A"),
        (SWITCH_DEFAULT, "loc_6DA0"),
    )


    label("loc_6D94")

    OP_A2(0x1200)
    Jump("loc_6DA0")

    label("loc_6D9A")

    OP_A2(0x1201)
    Jump("loc_6DA0")

    label("loc_6DA0")

    Return()

    # Function_40_6D1B end

    def Function_41_6DA1(): pass

    label("Function_41_6DA1")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6DE0")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_6DFA")

    label("loc_6DE0")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_6DFA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_41_6DA1 end

    def Function_42_6E1A(): pass

    label("Function_42_6E1A")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6E5F")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_6E7F")

    label("loc_6E5F")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_6E7F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_42_6E1A end

    def Function_43_6E9F(): pass

    label("Function_43_6E9F")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    OP_DE("Grancel")
    Return()

    # Function_43_6E9F end

    def Function_44_6EC3(): pass

    label("Function_44_6EC3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #211
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Rolent\x01",
            "⇒ To Zeiss\x01",
            "⇒ To Calvard\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #212
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_44_6EC3 end

    def Function_45_6F8C(): pass

    label("Function_45_6F8C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #213
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_45_6F8C end

    SaveToFile()

Try(main)
