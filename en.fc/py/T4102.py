from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4102.x',
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
        'Nial',                                 # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Seagull',                              # 16
        'Seagull',                              # 17
        'Seagull',                              # 18
        'Seagull',                              # 19
        'Seagull',                              # 20
        'Seagull',                              # 21
        'Seagull',                              # 22
        'Seagull',                              # 23
        'Seagull',                              # 24
        'Seagull',                              # 25
        'Armand',                               # 26
        'Ellie',                                # 27
        'Dalia',                                # 28
        'Phelio',                               # 29
        'Lakeisha',                             # 30
        'Private Datten',                       # 31
        'Peter',                                # 32
        'Sharnelle',                            # 33
        'Soldier',                              # 34
        'Soldier',                              # 35
        'Soldier',                              # 36
        'Special Ops Soldier',                  # 37
        'Special Ops Soldier',                  # 38
        'Rianne',                               # 39
        'Tourist',                              # 40
        'Tourist',                              # 41
        'Tourist',                              # 42
        'Tourist',                              # 43
        'Tourist',                              # 44
        'Tourist',                              # 45
        'Tourist',                              # 46
        'Tourist',                              # 47
        'Tourist',                              # 48
        'Seagull',                              # 49
        'Seagull',                              # 50
        'Seagull',                              # 51
        'Seagull',                              # 52
        'Seagull',                              # 53
        'Seagull',                              # 54
        'Seagull',                              # 55
        'Grancel - North Block',                # 56
        'Grancel - South Block',                # 57
    )

    DeclEntryPoint(
        Unknown_00              = -80000,
        Unknown_04              = 0,
        Unknown_08              = 0,
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH01730 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
        'ED6_DT07/CH01680 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH01610 ._CH',             # 0B
        'ED6_DT07/CH01480 ._CH',             # 0C
        'ED6_DT07/CH01143 ._CH',             # 0D
        'ED6_DT07/CH01023 ._CH',             # 0E
        'ED6_DT07/CH01003 ._CH',             # 0F
        'ED6_DT07/CH01220 ._CH',             # 10
        'ED6_DT07/CH01120 ._CH',             # 11
        'ED6_DT07/CH01200 ._CH',             # 12
        'ED6_DT07/CH01180 ._CH',             # 13
        'ED6_DT07/CH01050 ._CH',             # 14
        'ED6_DT07/CH01070 ._CH',             # 15
        'ED6_DT07/CH01730 ._CH',             # 16
        'ED6_DT07/CH01731 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH01730P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
        'ED6_DT07/CH01680P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH01610P._CP',             # 0B
        'ED6_DT07/CH01480P._CP',             # 0C
        'ED6_DT07/CH01143P._CP',             # 0D
        'ED6_DT07/CH01023P._CP',             # 0E
        'ED6_DT07/CH01003P._CP',             # 0F
        'ED6_DT07/CH01220P._CP',             # 10
        'ED6_DT07/CH01120P._CP',             # 11
        'ED6_DT07/CH01200P._CP',             # 12
        'ED6_DT07/CH01180P._CP',             # 13
        'ED6_DT07/CH01050P._CP',             # 14
        'ED6_DT07/CH01070P._CP',             # 15
        'ED6_DT07/CH01730P._CP',             # 16
        'ED6_DT07/CH01731P._CP',             # 17
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 36,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 37,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 38,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 39,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 40,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 41,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        Direction           = 90,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -55940,
        Z                   = 250,
        Y                   = 30,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -58170,
        Z                   = -3500,
        Y                   = -16100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -59550,
        Z                   = -3500,
        Y                   = -16100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -88950,
        Z                   = 0,
        Y                   = -3950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -78290,
        Z                   = 0,
        Y                   = -2530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -40940,
        Z                   = 0,
        Y                   = -5120,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -55400,
        Z                   = 0,
        Y                   = -3050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -62950,
        Z                   = -3750,
        Y                   = -31290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -55890,
        Z                   = 0,
        Y                   = -1830,
        Direction           = 185,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -78990,
        Z                   = 1250,
        Y                   = 8029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -55990,
        Z                   = 250,
        Y                   = -1280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -58060,
        Z                   = -3250,
        Y                   = -23920,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -60050,
        Z                   = -3250,
        Y                   = -24510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -58590,
        Z                   = -3250,
        Y                   = -22150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -55610,
        Z                   = -3750,
        Y                   = -27100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -60830,
        Z                   = -3500,
        Y                   = -28840,
        Direction           = 204,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -61010,
        Z                   = 250,
        Y                   = -870,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = -82230,
        Z                   = 250,
        Y                   = 4330,
        Direction           = 41,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -79740,
        Z                   = 250,
        Y                   = 4870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = -78570,
        Z                   = 250,
        Y                   = 4270,
        Direction           = 4,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39960,
        Z                   = 0,
        Y                   = 43920,
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
        X                   = -7520,
        Z                   = 300,
        Y                   = -20000,
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
        X                   = -82190,
        Y                   = 0,
        Z                   = 123740,
        Range               = -75710,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x292C,
        Unknown_18          = 0x0,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = -63040,
        Y                   = -3750,
        Z                   = -33480,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = -63390,
        Y                   = -3750,
        Z                   = -24940,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 49,
    )

    DeclEvent(
        X                   = -78840,
        Y                   = 1250,
        Z                   = 12430,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 50,
    )


    DeclActor(
        TriggerX            = -76990,
        TriggerZ            = -3500,
        TriggerY            = -30450,
        TriggerRange        = 800,
        ActorX              = -76990,
        ActorZ              = -2500,
        ActorY              = -30450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92000,
        TriggerZ            = 800,
        TriggerY            = -4000,
        TriggerRange        = 800,
        ActorX              = -92000,
        ActorZ              = 1800,
        ActorY              = -4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 46,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -72220,
        TriggerZ            = -3180,
        TriggerY            = -15630,
        TriggerRange        = 800,
        ActorX              = -72220,
        ActorZ              = -2000,
        ActorY              = -15630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_876",          # 00, 0
        "Function_1_A1B",          # 01, 1
        "Function_2_B97",          # 02, 2
        "Function_3_D14",          # 03, 3
        "Function_4_D99",          # 04, 4
        "Function_5_E26",          # 05, 5
        "Function_6_EB7",          # 06, 6
        "Function_7_EDB",          # 07, 7
        "Function_8_F38",          # 08, 8
        "Function_9_F5C",          # 09, 9
        "Function_10_115F",        # 0A, 10
        "Function_11_141E",        # 0B, 11
        "Function_12_18D0",        # 0C, 12
        "Function_13_1BB0",        # 0D, 13
        "Function_14_1CAA",        # 0E, 14
        "Function_15_1DD0",        # 0F, 15
        "Function_16_2419",        # 10, 16
        "Function_17_2DCD",        # 11, 17
        "Function_18_3750",        # 12, 18
        "Function_19_37CF",        # 13, 19
        "Function_20_3829",        # 14, 20
        "Function_21_3852",        # 15, 21
        "Function_22_3A37",        # 16, 22
        "Function_23_3C6D",        # 17, 23
        "Function_24_3CFF",        # 18, 24
        "Function_25_3D30",        # 19, 25
        "Function_26_3D64",        # 1A, 26
        "Function_27_3DAA",        # 1B, 27
        "Function_28_3E25",        # 1C, 28
        "Function_29_3E87",        # 1D, 29
        "Function_30_3ECD",        # 1E, 30
        "Function_31_3F3F",        # 1F, 31
        "Function_32_3F6B",        # 20, 32
        "Function_33_3F97",        # 21, 33
        "Function_34_4554",        # 22, 34
        "Function_35_479C",        # 23, 35
        "Function_36_49EC",        # 24, 36
        "Function_37_4A32",        # 25, 37
        "Function_38_4A78",        # 26, 38
        "Function_39_4AE6",        # 27, 39
        "Function_40_4B54",        # 28, 40
        "Function_41_4BC2",        # 29, 41
        "Function_42_4C30",        # 2A, 42
        "Function_43_4DB4",        # 2B, 43
        "Function_44_5049",        # 2C, 44
        "Function_45_506D",        # 2D, 45
        "Function_46_51BB",        # 2E, 46
        "Function_47_5239",        # 2F, 47
        "Function_48_529B",        # 30, 48
        "Function_49_529F",        # 31, 49
        "Function_50_52A3",        # 32, 50
    )


    def Function_0_876(): pass

    label("Function_0_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_884")
    OP_A3(0x3FA)
    Event(0, 33)

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_8A0")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 43)

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_8FF")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x10)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x10)
    Jump("loc_A08")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_913")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_A08")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_92C")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_A08")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_94A")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_A08")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_963")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x26, 0x80)
    Jump("loc_A08")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_9A8")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -85310, 0, -4390, 270)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -84980, 0, -3470, 270)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_A08")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_9E3")
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -79040, 500, 6080, 0)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -79040, 1250, 7750, 180)
    Jump("loc_A08")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9ED")
    Jump("loc_A08")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_9F7")
    Jump("loc_A08")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_A01")
    Jump("loc_A08")

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_A08")

    label("loc_A08")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_A14"),
        (SWITCH_DEFAULT, "loc_A1A"),
    )


    label("loc_A14")

    OP_A2(0x622)
    Jump("loc_A1A")

    label("loc_A1A")

    Return()

    # Function_0_876 end

    def Function_1_A1B(): pass

    label("Function_1_A1B")

    OP_16(0x2, 0xFA0, 0xFFFD2D58, 0xFFFE0048, 0x3005D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A60")
    OP_B1("t4102_y")
    Jump("loc_A69")

    label("loc_A60")

    OP_B1("t4102_n")

    label("loc_A69")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A82")
    OP_72(0xA, 0x10)
    OP_65(0x0, 0x1)

    label("loc_A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A95")
    OP_1B(0x3, 0x0, 0x2D)

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADA")
    OP_72(0xE, 0x8)
    OP_72(0xE, 0x20)
    OP_72(0xE, 0x2)
    OP_6F(0xE, 0)
    OP_72(0xB, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0xD, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x9, 0x10)
    OP_72(0xA, 0x10)

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B38")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x23)
    OP_43(0xA, 0x1, 0x0, 0x23)
    OP_43(0xB, 0x1, 0x0, 0x23)
    OP_43(0xC, 0x1, 0x0, 0x23)
    OP_43(0xD, 0x1, 0x0, 0x23)
    OP_43(0xE, 0x1, 0x0, 0x23)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_B96")
    OP_72(0x10, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -63240, -3240, -25080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_B96")

    Return()

    # Function_1_A1B end

    def Function_2_B97(): pass

    label("Function_2_B97")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CFE")

    label("loc_BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CFE")

    label("loc_BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CFE")

    label("loc_BEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C07")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CFE")

    label("loc_C07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C20")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CFE")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C39")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CFE")

    label("loc_C39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C52")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CFE")

    label("loc_C52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CFE")

    label("loc_C6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C84")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CFE")

    label("loc_C84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CFE")

    label("loc_C9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CFE")

    label("loc_CB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CFE")

    label("loc_CCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CFE")

    label("loc_CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D13")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CFE")

    label("loc_D13")

    Return()

    # Function_2_B97 end

    def Function_3_D14(): pass

    label("Function_3_D14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D98")
    OP_8E(0xFE, 0xFFFF63CA, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF291E, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF259A, 0x0, 0xFFFFF416, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_3_D14")

    label("loc_D98")

    Return()

    # Function_3_D14 end

    def Function_4_D99(): pass

    label("Function_4_D99")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E25")
    OP_8E(0xFE, 0xFFFED716, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEC014, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFECB72, 0x4E2, 0x1F5D, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_4_D99")

    label("loc_E25")

    Return()

    # Function_4_D99 end

    def Function_5_E26(): pass

    label("Function_5_E26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EB6")
    OP_8E(0xFE, 0xFFFF1FB4, 0xFFFFF15A, 0xFFFF85C6, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFEF5F2, 0xFFFFF15A, 0xFFFF85C6, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFF09F2, 0xFFFFF15A, 0xFFFF85C6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("Function_5_E26")

    label("loc_EB6")

    Return()

    # Function_5_E26 end

    def Function_6_EB7(): pass

    label("Function_6_EB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDA")
    OP_8D(0xFE, -83110, 1920, -74690, -5430, 3000)
    Jump("Function_6_EB7")

    label("loc_EDA")

    Return()

    # Function_6_EB7 end

    def Function_7_EDB(): pass

    label("Function_7_EDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F37")
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFF711C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C52, 0xFFFFF15A, 0xFFFF727A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF2C0C, 0x0, 0xFFFFEC82, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFF6014, 0x0, 0xFFFFEC00, 0x9C4, 0x0)
    Jump("Function_7_EDB")

    label("loc_F37")

    Return()

    # Function_7_EDB end

    def Function_8_F38(): pass

    label("Function_8_F38")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5B")
    OP_8D(0xFE, -59380, 250, -52780, -3730, 3000)
    Jump("Function_8_F38")

    label("loc_F5B")

    Return()

    # Function_8_F38 end

    def Function_9_F5C(): pass

    label("Function_9_F5C")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_115E")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1127")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1017")

    def lambda_FFB():

        label("loc_FFB")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_FFB")

    QueueWorkItem2(0xFE, 1, lambda_FFB)
    Jump("loc_1036")

    label("loc_1017")


    def lambda_101D():

        label("loc_101D")

        OP_97(0xFE, 0xFFFECB7C, 0x3926, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_101D")

    QueueWorkItem2(0xFE, 1, lambda_101D)

    label("loc_1036")

    SetChrChipByIndex(0xFE, 22)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_1045")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107D")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1075")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_107D")

    label("loc_1075")

    Sleep(15)
    Jump("loc_1045")

    label("loc_107D")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -78690, 0, -40, 74)

    label("loc_109C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1124")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111C")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 23)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -74920, -1510, -82870, 5610, 0)
    Jump("loc_1124")

    label("loc_111C")

    Sleep(500)
    Jump("loc_109C")

    label("loc_1124")

    Jump("loc_115B")

    label("loc_1127")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115B")

    def lambda_1143():
        OP_8D(0xFE, -74920, -1510, -82870, 5610, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1143)

    label("loc_115B")

    Jump("loc_F90")

    label("loc_115E")

    Return()

    # Function_9_F5C end

    def Function_10_115F(): pass

    label("Function_10_115F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(    #0
        0xFE,
        (
            "I heard General Morgan's grand-\x01",
            "child was one of the hostages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I can't imagine Colonel Richard\x01",
            "doing such a thing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_11EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_11F5")
    Jump("loc_141A")

    label("loc_11F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1276")

    ChrTalk(    #2
        0xFE,
        (
            "The girl who lives here hasn't\x01",
            "come home yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I just heard about it from base.\x01",
            "I sure hope she's found soon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1376")

    ChrTalk(    #4
        0xFE,
        (
            "I actually had...a lunch break\x01",
            "today! Aidios must surely be\x01",
            "smiling upon me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "I really needed it, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "But...why was I the only one to\x01",
            "be given a break?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I feel kind of guilty relaxing\x01",
            "while everyone else busts their\x01",
            "butts...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1380")
    Jump("loc_141A")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_13EB")

    ChrTalk(    #8
        0xFE,
        (
            "I heard that all these anti-terrorist\x01",
            "countermeasures are keeping General\x01",
            "Morgan real busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_13F5")
    Jump("loc_141A")

    label("loc_13F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13FF")
    Jump("loc_141A")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1409")
    Jump("loc_141A")

    label("loc_1409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1413")
    Jump("loc_141A")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_141A")

    label("loc_141A")

    TalkEnd(0xFE)
    Return()

    # Function_10_115F end

    def Function_11_141E(): pass

    label("Function_11_141E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(    #9
        0xFE,
        "...Why am I still here?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1453")
    Jump("loc_18CC")

    label("loc_1453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_14F6")

    ChrTalk(    #10
        0xFE,
        (
            "They're not giving anyone any\x01",
            "details on Her Majesty's illness.\x01",
            "Including us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "All we can do is keep patrolling.\x01",
            "We have our orders, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_14F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_173A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_15F8")

    ChrTalk(    #12
        0xFE,
        (
            "Even if we should find any Royal\x01",
            "Guardsmen, I'd really prefer we\x01",
            "not have to fight them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Aside from the obvious conflict of interests of\x01",
            "a soldier for the crown fighting another soldier\x01",
            "for the crown...they're much better trained!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1737")

    label("loc_15F8")

    OP_A2(0x8)

    ChrTalk(    #14
        0xFE,
        (
            "Even if we should find any Royal\x01",
            "Guardsmen, I'd really prefer we\x01",
            "not have to fight them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Aside from the obvious conflict of interests of\x01",
            "a soldier for the crown fighting another soldier\x01",
            "for the crown...they're much better trained!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "*sigh* Why won't they just do\x01",
            "us all a favor, and surrender\x01",
            "already?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1737")

    Jump("loc_18CC")

    label("loc_173A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_184E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_17AA")

    ChrTalk(    #17
        0xFE,
        "Heh, heh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "One of them purdy nuns just said\x01",
            "'Hello' to me. I feel all funny\x01",
            "inside!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184B")

    label("loc_17AA")

    OP_A2(0x8)

    ChrTalk(    #19
        0xFE,
        "Heh, heh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "One of them purdy nuns just said\x01",
            "'Hello' to me. I feel all funny\x01",
            "inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "All right, time to help keep the\x01",
            "peace in the royal city!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184B")

    Jump("loc_18CC")

    label("loc_184E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_189D")

    ChrTalk(    #22
        0xFE,
        (
            "We've been tasked with patrolling\x01",
            "all the major establishments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_18A7")
    Jump("loc_18CC")

    label("loc_18A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18B1")
    Jump("loc_18CC")

    label("loc_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_18BB")
    Jump("loc_18CC")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_18C5")
    Jump("loc_18CC")

    label("loc_18C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_18CC")

    label("loc_18CC")

    TalkEnd(0xFE)
    Return()

    # Function_11_141E end

    def Function_12_18D0(): pass

    label("Function_12_18D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_19B2")

    ChrTalk(    #23
        0xFE,
        (
            "There are still some Intelligence Division\x01",
            "members at large, and it's entirely possible\x01",
            "they could try to target Grancel City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Looks like we're going to be well\x01",
            "and truly busy for quite some time\x01",
            "yet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAC")

    label("loc_19B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_19BC")
    Jump("loc_1BAC")

    label("loc_19BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1A2E")

    ChrTalk(    #25
        0xFE,
        (
            "There seemed to be some kind of\x01",
            "commotion with the workers here.\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BAC")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1AAD")

    ChrTalk(    #27
        0xFE,
        "Wow, evening already...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Normally it'd be time to change\x01",
            "shifts...but I'm working a double\x01",
            "tonight. *sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAC")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1B0D")

    ChrTalk(    #29
        0xFE,
        (
            "Some girl took my picture as she\x01",
            "was leaving just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "She said I was cute!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BAC")

    label("loc_1B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1B7D")

    ChrTalk(    #31
        0xFE,
        "What's your business here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "We've been ordered to keep a\x01",
            "strict eye on the employees\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAC")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1B87")
    Jump("loc_1BAC")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1B91")
    Jump("loc_1BAC")

    label("loc_1B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1B9B")
    Jump("loc_1BAC")

    label("loc_1B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1BA5")
    Jump("loc_1BAC")

    label("loc_1BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1BAC")

    label("loc_1BAC")

    TalkEnd(0xFE)
    Return()

    # Function_12_18D0 end

    def Function_13_1BB0(): pass

    label("Function_13_1BB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1BBD")
    Jump("loc_1CA6")

    label("loc_1BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1C4F")

    ChrTalk(    #33
        0xFE,
        (
            "Hey, you're the guys who won\x01",
            "the tournament, aren't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "...I've got my eyes on you.\x01",
            "Don't you try anything funny,\x01",
            "you hear?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA6")

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1C59")
    Jump("loc_1CA6")

    label("loc_1C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1C63")
    Jump("loc_1CA6")

    label("loc_1C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C6D")
    Jump("loc_1CA6")

    label("loc_1C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1C77")
    Jump("loc_1CA6")

    label("loc_1C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1C81")
    Jump("loc_1CA6")

    label("loc_1C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_1CA6")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1C95")
    Jump("loc_1CA6")

    label("loc_1C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1C9F")
    Jump("loc_1CA6")

    label("loc_1C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1CA6")

    label("loc_1CA6")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BB0 end

    def Function_14_1CAA(): pass

    label("Function_14_1CAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1CB7")
    Jump("loc_1DCC")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1D75")

    ChrTalk(    #35
        0xFE,
        (
            "Commander Lorence is inside the\x01",
            "castle, so I don't think there'll\x01",
            "be any problems there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Our responsibility is to the\x01",
            "city streets right now. And we\x01",
            "will keep them safe!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DCC")

    label("loc_1D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1D7F")
    Jump("loc_1DCC")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D89")
    Jump("loc_1DCC")

    label("loc_1D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1D93")
    Jump("loc_1DCC")

    label("loc_1D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1D9D")
    Jump("loc_1DCC")

    label("loc_1D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1DA7")
    Jump("loc_1DCC")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1DB1")
    Jump("loc_1DCC")

    label("loc_1DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1DBB")
    Jump("loc_1DCC")

    label("loc_1DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1DC5")
    Jump("loc_1DCC")

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1DCC")

    label("loc_1DCC")

    TalkEnd(0xFE)
    Return()

    # Function_14_1CAA end

    def Function_15_1DD0(): pass

    label("Function_15_1DD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1E6F")

    ChrTalk(    #37
        0xFE,
        (
            "Both Her Majesties the Queen and\x01",
            "princess looked well, did they not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I caught no sight of Duke Dunan,\x01",
            "however. I wonder where he was...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(    #39
        0xFE,
        "Wh-What's going on...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1F4E")

    ChrTalk(    #40
        0xFE,
        (
            "I hope I get to see Princess\x01",
            "Klaudia at least once during\x01",
            "the Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "She's so cute, in that 'girl\x01",
            "next door' way. I wish I had\x01",
            "a daughter like her...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_1F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1FFB")

    ChrTalk(    #42
        0xFE,
        (
            "With soldiers everywhere this\x01",
            "year, no one seems willing to\x01",
            "really 'cut loose,' so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Makes the festivities a lot less...\x01",
            "festive, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2087")

    ChrTalk(    #44
        0xFE,
        (
            "Usually on the last day of the\x01",
            "tournament, the city's just\x01",
            "buzzing with excitement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I wonder how it'll be this\x01",
            "year...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_2087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_20E9")

    ChrTalk(    #46
        0xFE,
        "Is it evening already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "The days fly by so quickly as\x01",
            "you get older, it seems.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_20E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2162")

    ChrTalk(    #48
        0xFE,
        (
            "Maybe I'll go by the store while\x01",
            "everyone else is at the tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Fewer crowds and all, you know?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_2162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_21A4")

    ChrTalk(    #50
        0xFE,
        (
            "I need to get home and start\x01",
            "getting dinner ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_21A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_226D")

    ChrTalk(    #51
        0xFE,
        (
            "I was quite shocked to hear\x01",
            "there would be no discount on\x01",
            "tournament tickets this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "They're so expensive without the\x01",
            "discount that...well, I decided\x01",
            "not to go at all this year!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2392")

    ChrTalk(    #53
        0xFE,
        (
            "Half of my excitement for the tournament\x01",
            "is gone, anyway, with Her Majesty having\x01",
            "fallen ill. Makes me worried!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I do NOT like that skeevy Duke\x01",
            "Dunan has been named the royal\x01",
            "successor. Not one bit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Poor Colonel Richard, too, forced\x01",
            "to protect a jackanapes like him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2415")

    ChrTalk(    #56
        0xFE,
        (
            "So are all those rumors about\x01",
            "the terrorist attack true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I hope it doesn't adversely affect\x01",
            "our cost of living...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2415")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DD0 end

    def Function_16_2419(): pass

    label("Function_16_2419")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_246A")

    ChrTalk(    #58
        0xFE,
        (
            "I'm so glad the Birthday Celebration\x01",
            "went off without a hitch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_246A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_252A")

    ChrTalk(    #59
        0xFE,
        (
            "Seems the Royal Guardsmen have gone\x01",
            "into hiding in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "So all those rumors about the terrorist\x01",
            "attacks are actually true? Maybe I should\x01",
            "get out of here...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260D")

    label("loc_252A")

    OP_A2(0x5)

    ChrTalk(    #61
        0xFE,
        (
            "I overheard some of the soldiers\x01",
            "talking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Seems the Royal Guardsmen have gone\x01",
            "into hiding in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "So all those rumors about the terrorist\x01",
            "attacks are actually true? Maybe I should\x01",
            "get out of here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260D")

    Jump("loc_2DC9")

    label("loc_2610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_26A8")

    ChrTalk(    #64
        0xFE,
        (
            "Early this morning I crossed\x01",
            "paths with one of the nuns from\x01",
            "the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Where could she have been going\x01",
            "at that time of day...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_26A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_2743")

    ChrTalk(    #66
        0xFE,
        (
            "Usually there are people up\x01",
            "partying all night this time\x01",
            "of year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "But I guess that's pretty well\x01",
            "out of the question THIS year,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_2743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_27FF")

    ChrTalk(    #68
        0xFE,
        (
            "Last night it seemed like they'd\x01",
            "increased the number of soldiers\x01",
            "on patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "It sucks to have all the stores\x01",
            "closing down so early during the\x01",
            "Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_27FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_2876")

    ChrTalk(    #70
        0xFE,
        (
            "There are a LOT more soldiers\x01",
            "on patrol than usual...and more\x01",
            "than any other year, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "How come?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2932")

    ChrTalk(    #72
        0xFE,
        (
            "Everything is closed down! The\x01",
            "castle, the landing port, the\x01",
            "seaport...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Guess all there really is to do\x01",
            "around here right now is go see\x01",
            "the Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_2932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_29FD")

    ChrTalk(    #74
        0xFE,
        (
            "The cathedral is a pretty famous\x01",
            "sightseeing spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "It's kind of quiet now, but that's because\x01",
            "everyone's here for the tournament--not\x01",
            "for sightseeing or religious fulfillment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AFE")

    label("loc_29FD")

    OP_A2(0x5)

    ChrTalk(    #76
        0xFE,
        (
            "The cathedral is a pretty famous\x01",
            "sightseeing spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I heard it's the oldest church\x01",
            "building in the entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "It's kind of quiet now, but that's because\x01",
            "everyone's here for the tournament--not\x01",
            "for sightseeing or religious fulfillment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFE")

    Jump("loc_2DC9")

    label("loc_2B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2BA7")

    ChrTalk(    #79
        0xFE,
        (
            "The main headquarters for the\x01",
            "Liberl News is in this block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "You can usually find their\x01",
            "reporters holding a meeting \x01",
            "at the coffee shop next door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC9")

    label("loc_2BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2C6D")

    ChrTalk(    #81
        0xFE,
        (
            "I heard General Morgan's so busy, he\x01",
            "doesn't even have time to go back to\x01",
            "his own house...pretty much ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "The only exception is during the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D50")

    label("loc_2C6D")

    OP_A2(0x5)

    ChrTalk(    #83
        0xFE,
        (
            "General Morgan lives in one of\x01",
            "the houses here in West Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "He's usually so busy he doesn't\x01",
            "actually get a chance to go home.\x01",
            "Pretty much ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "The only exception is during the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D50")

    Jump("loc_2DC9")

    label("loc_2D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2DC9")

    ChrTalk(    #86
        0xFE,
        (
            "I just saw some guys in handcuffs\x01",
            "being led around by a group of\x01",
            "soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "They came from the docks.\x02",
    )

    CloseMessageWindow()

    label("loc_2DC9")

    TalkEnd(0xFE)
    Return()

    # Function_16_2419 end

    def Function_17_2DCD(): pass

    label("Function_17_2DCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2E56")

    ChrTalk(    #88
        0xFE,
        (
            "Colonel Richard being behind\x01",
            "the coup d'etat blows my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "I had no idea, and I was working\x01",
            "right alongside him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_2E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_2F15")

    ChrTalk(    #90
        0xFE,
        (
            "I can't say exactly when, but the Royal\x01",
            "Garrison seem to have been completely\x01",
            "replaced by Special Ops soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "What in the name of Aidios is\x01",
            "going on inside the castle?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_2F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2FC5")

    ChrTalk(    #92
        0xFE,
        (
            "There are rumors that the terrorists\x01",
            "who claimed to be bracers just...up\x01",
            "and ran!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "They got through the Zeiss inspection,\x01",
            "then disappeared, who knows where.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_2FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_306E")

    ChrTalk(    #94
        0xFE,
        (
            "Looks like the tournament went\x01",
            "off without incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Thank goodness there wasn't a terrorist\x01",
            "attack or anything during the Martial\x01",
            "Arts Competition!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_312B")

    ChrTalk(    #96
        0xFE,
        (
            "I saw that the border garrison\x01",
            "had come to participate in the\x01",
            "tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "...but they seemed troubled that \x01",
            "they couldn't get into contact\x01",
            "with General Morgan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_320F")

    label("loc_312B")

    OP_A2(0x4)

    ChrTalk(    #98
        0xFE,
        (
            "I saw that the border garrison\x01",
            "had come to participate in the\x01",
            "tournament...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "...but they seemed troubled that \x01",
            "they couldn't get in contact with\x01",
            "General Morgan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I hope nothing is amiss at the\x01",
            "imperial border...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_320F")

    Jump("loc_374C")

    label("loc_3212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_33C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_32C3")

    ChrTalk(    #101
        0xFE,
        (
            "I haven't seen Colonel Richard\x01",
            "since he went into Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "If he's here for anti-terror\x01",
            "planning, shouldn't he be out\x01",
            "at the Erbe Royal Villa?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C6")

    label("loc_32C3")

    OP_A2(0x4)

    ChrTalk(    #103
        0xFE,
        (
            "I haven't seen Colonel Richard\x01",
            "since he went into Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "If he's here for anti-terror\x01",
            "planning, shouldn't he be out\x01",
            "at the Erbe Royal Villa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Or maybe Her Majesty asked him\x01",
            "to stay because she can't count\x01",
            "on Duke Dunan worth a damn!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C6")

    Jump("loc_374C")

    label("loc_33C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3470")

    ChrTalk(    #106
        0xFE,
        (
            "I heard the Intelligence Division\x01",
            "set up the Special Ops themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "They scouted out and inducted\x01",
            "some really talented soldiers\x01",
            "for the job, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_3470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_351B")

    ChrTalk(    #108
        0xFE,
        (
            "Isn't Professor Russell a student\x01",
            "of the guy who invented orbment,\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "What are the Royal Guardsmen\x01",
            "planning to do with someone\x01",
            "like him...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_351B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_35D4")

    ChrTalk(    #110
        0xFE,
        (
            "Everyone on this list is a\x01",
            "member of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "But there's no way anybody's going to\x01",
            "be caught dead in that uniform with\x01",
            "all these wanted posters everywhere!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374C")

    label("loc_35D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3641")

    ChrTalk(    #112
        0xFE,
        "Colonel Richard is so amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "He's smart, he's a good soldier,\x01",
            "AND he's popular.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3702")

    label("loc_3641")

    OP_A2(0x4)

    ChrTalk(    #114
        0xFE,
        (
            "Colonel Richard has been at the\x01",
            "castle these past few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "He came into port here from\x01",
            "Leiston Fortress. Isn't he\x01",
            "awesome?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "He's smart, he's a good soldier,\x01",
            "AND he's popular.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3702")

    Jump("loc_374C")

    label("loc_3705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_374C")

    ChrTalk(    #117
        0xFE,
        (
            "The port is closed right now\x01",
            "as an anti-terrorist measure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374C")

    TalkEnd(0xFE)
    Return()

    # Function_17_2DCD end

    def Function_18_3750(): pass

    label("Function_18_3750")

    TalkBegin(0xFE)

    ChrTalk(    #118
        0xFE,
        (
            "Why would that famous army guy\x01",
            "stage a coup like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I wish he hadn't gotten the\x01",
            "whole city involved in it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3750 end

    def Function_19_37CF(): pass

    label("Function_19_37CF")

    TalkBegin(0xFE)

    ChrTalk(    #120
        0xFE,
        (
            "Once things calm down, I'm\x01",
            "sending my husband out to\x01",
            "go look for a job again!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_37CF end

    def Function_20_3829(): pass

    label("Function_20_3829")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0xFE,
        "Rianne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Where are you?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3829 end

    def Function_21_3852(): pass

    label("Function_21_3852")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_385F")
    Jump("loc_3A33")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3869")
    Jump("loc_3A33")

    label("loc_3869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3873")
    Jump("loc_3A33")

    label("loc_3873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_387D")
    Jump("loc_3A33")

    label("loc_387D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3887")
    Jump("loc_3A33")

    label("loc_3887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_38CE")

    ChrTalk(    #123
        0xFE,
        "Seems we can't go to the harbor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "That's too bad...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A33")

    label("loc_38CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3A0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3943")

    ChrTalk(    #125
        0xFE,
        (
            "Seeing you on the corner, with\x01",
            "the cathedral to your back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "It's a picture for the ages!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A0B")

    label("loc_3943")

    OP_A2(0x0)

    ChrTalk(    #127
        0xFE,
        (
            "Seeing you on the corner, with\x01",
            "the Cathedral to your back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "It's a picture for the ages! Oh,\x01",
            "if only I had an orbal camera...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "All I can do is burn this image\x01",
            "into my heart forever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0B")

    Jump("loc_3A33")

    label("loc_3A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A18")
    Jump("loc_3A33")

    label("loc_3A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3A22")
    Jump("loc_3A33")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3A2C")
    Jump("loc_3A33")

    label("loc_3A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3A33")

    label("loc_3A33")

    TalkEnd(0xFE)
    Return()

    # Function_21_3852 end

    def Function_22_3A37(): pass

    label("Function_22_3A37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3A44")
    Jump("loc_3C69")

    label("loc_3A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_3A4E")
    Jump("loc_3C69")

    label("loc_3A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3A58")
    Jump("loc_3C69")

    label("loc_3A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A62")
    Jump("loc_3C69")

    label("loc_3A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3A6C")
    Jump("loc_3C69")

    label("loc_3A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3AD8")

    ChrTalk(    #130
        0xFE,
        (
            "The harbor is supposed to be\x01",
            "absolutely stunning at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "It says so in the guidebook.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C69")

    label("loc_3AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3B85")

    ChrTalk(    #132
        0xFE,
        (
            "There are so many things here\x01",
            "that I've never seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "All the date spots in Rolent\x01",
            "have gotten so stale... It's\x01",
            "so nice to be somewhere new!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C41")

    label("loc_3B85")

    OP_A2(0x1)

    ChrTalk(    #134
        0xFE,
        (
            "There are so many things here\x01",
            "that I've never seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "All the date spots in Rolent\x01",
            "have gotten so stale... It's\x01",
            "so nice to be somewhere new!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Vacations are the best!\x02",
    )

    CloseMessageWindow()

    label("loc_3C41")

    Jump("loc_3C69")

    label("loc_3C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C4E")
    Jump("loc_3C69")

    label("loc_3C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_3C58")
    Jump("loc_3C69")

    label("loc_3C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_3C62")
    Jump("loc_3C69")

    label("loc_3C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C69")

    label("loc_3C69")

    TalkEnd(0xFE)
    Return()

    # Function_22_3A37 end

    def Function_23_3C6D(): pass

    label("Function_23_3C6D")

    TalkBegin(0xFE)

    ChrTalk(    #137
        0xFE,
        (
            "Grandpa didn't come home this\x01",
            "year, and he isn't even in the\x01",
            "tournament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Why's he gotta be so boring?\x01",
            "I'm gonna go play outside!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3C6D end

    def Function_24_3CFF(): pass

    label("Function_24_3CFF")

    TalkBegin(0xFE)

    ChrTalk(    #139
        0xFE,
        (
            "Ew, there's bits of paper in\x01",
            "my cup!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3CFF end

    def Function_25_3D30(): pass

    label("Function_25_3D30")

    TalkBegin(0xFE)

    ChrTalk(    #140
        0xFE,
        (
            "We're lucky we found these\x01",
            "empty seats.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_3D30 end

    def Function_26_3D64(): pass

    label("Function_26_3D64")

    TalkBegin(0xFE)

    ChrTalk(    #141
        0xFE,
        (
            "The coffee here just has that\x01",
            "aroma of quality, you know?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3D64 end

    def Function_27_3DAA(): pass

    label("Function_27_3DAA")

    TalkBegin(0xFE)

    ChrTalk(    #142
        0xFE,
        "I like the feel in the air here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I'm not really all that tired,\x01",
            "but it can't hurt to take a\x01",
            "short rest...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_3DAA end

    def Function_28_3E25(): pass

    label("Function_28_3E25")

    TalkBegin(0xFE)

    ChrTalk(    #144
        0xFE,
        (
            "So this is the famous Liberl News\x01",
            "building, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "I wonder if we can go inside?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_3E25 end

    def Function_29_3E87(): pass

    label("Function_29_3E87")

    TalkBegin(0xFE)

    ChrTalk(    #146
        0xFE,
        (
            "Incredible. Even the regular\x01",
            "neighborhoods here are posh.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_3E87 end

    def Function_30_3ECD(): pass

    label("Function_30_3ECD")

    TalkBegin(0xFE)

    ChrTalk(    #147
        0xFE,
        (
            "Maybe I'll go say some prayers\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I think I'm going to have fun\x01",
            "here. Long live the queen!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_3ECD end

    def Function_31_3F3F(): pass

    label("Function_31_3F3F")

    TalkBegin(0xFE)

    ChrTalk(    #149
        0xFE,
        "So this is Grancel Cathedral...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_3F3F end

    def Function_32_3F6B(): pass

    label("Function_32_3F6B")

    TalkBegin(0xFE)

    ChrTalk(    #150
        0xFE,
        "So this is Grancel Cathedral...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_3F6B end

    def Function_33_3F97(): pass

    label("Function_33_3F97")

    EventBegin(0x0)
    OP_6D(-63290, -3220, -25240, 0)
    OP_67(0, 12660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(269000, 0)
    OP_6E(442, 0)

    def lambda_3FDC():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FDC)

    def lambda_3FF4():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FF4)

    def lambda_4004():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4004)

    def lambda_4014():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4014)
    SetChrPos(0x101, -61850, -3500, -25070, 270)
    SetChrPos(0x102, -62010, -3500, -26170, 270)
    SetChrPos(0x8, -63080, -3500, -25100, 270)
    ClearChrFlags(0x8, 0x80)
    Sleep(6000)

    ChrTalk(    #151
        0x101,
        (
            "#000FHeeey, this is a nice little place.\x02\x03",

            "Feels less like a bar and\x01",
            "more like a coffee shop.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #152
        0x102,
        (
            "#010FThat might explain the\x01",
            "smell of coffee.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(    #153
        0x8,
        (
            "#140FI hear the owner started up\x01",
            "this place as a hobby.\x02\x03",

            "The brew here is amazing.\x02\x03",

            "Plus, he took some advice from someone\x01",
            "later on and added curry rice to the\x01",
            "menu. Curry with AUTHENTIC spices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#000FHmmm... Isn't that the\x01",
            "super-hot stuff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        (
            "#010FIt's pretty spicy, but it's really\x01",
            "good. Savory, you might say.\x02\x03",

            "I haven't had it in ages,\x01",
            "but I loved it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#000FEep...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#140FHeh heh... Try it once, and\x01",
            "you'll be addicted for life.\x02\x03",

            "I just like the atmosphere out here,\x01",
            "though, personally. Have a seat! Let's\x01",
            "get this interview started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#000FNot so fast!\x02\x03",

            "We were just in that big match, so we're\x01",
            "pretty damned hungry. And I'm not about\x01",
            "to smell food without EATING food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x102,
        (
            "#010FDinner does sound lovely right\x01",
            "about now, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#140FGrrr... Damn kids.\x02\x03",

            "Fine! I'll buy you dinner.\x02\x03",

            "And while you're stuffing your faces,\x01",
            "you can give me the exclusive on any\x01",
            "news you've found!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#000FAaaand, there's the pitch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x102,
        (
            "#010FBy the way, isn't Dorothy\x01",
            "with you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "#140FNah, I gave her something else\x01",
            "to work on...\x02\x03",

            "Now, come on.\x01",
            "Inside with the both of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_3F97 end

    def Function_34_4554(): pass

    label("Function_34_4554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x36D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45AB")
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #164
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Jump("loc_479B")

    label("loc_45AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4733")
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #165
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_END)), "loc_4682")

    ChrTalk(    #166
        0x102,
        (
            "#010FIt's late. Why don't we save\x01",
            "the sewers for later?\x02\x03",

            "We can check it out when\x01",
            "Zin and Olivier are with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472D")

    label("loc_4682")


    ChrTalk(    #167
        0x102,
        (
            "#010FThis must be the entrance to\x01",
            "the Grancel Sewers that the\x01",
            "Ravens mentioned.\x02\x03",

            "It's late, so why don't we check\x01",
            "this out tomorrow when Zin and\x01",
            "Olivier are with us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_472D")

    TalkEnd(0xFF)
    Jump("loc_479B")

    label("loc_4733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x73, 0x0, 0x64)

    AnonymousTalk(    #168
        "\x07\x00Used \x07\x02Grancel Sewer Key A\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x622)
    OP_71(0xA, 0x10)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)

    label("loc_479B")

    Return()

    # Function_34_4554 end

    def Function_35_479C(): pass

    label("Function_35_479C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49EB")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47CF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_47CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47F5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_47F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_481B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_481B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4842")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_4842")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4868")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_4868")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_488E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_488E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48B3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_48B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48EC")

    label("loc_48D8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    OP_69(0xFE, 0x3E8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D9")

    ChrTalk(    #169
        0xFE,
        "Hey! You two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#000F(Crap...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        "#010F(Caught already...)\x02",
    )

    CloseMessageWindow()

    label("loc_49D9")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_49E8")

    Jump("Function_35_479C")

    label("loc_49EB")

    Return()

    # Function_35_479C end

    def Function_36_49EC(): pass

    label("Function_36_49EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A31")
    SetChrPos(0xFE, -43700, 250, -8520, 0)
    OP_8E(0xFE, 0xFFFF554C, 0xFA, 0xFFFF7D1A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF554C, 0xFA, 0xFFFFDEB8, 0xBB8, 0x0)
    Jump("Function_36_49EC")

    label("loc_4A31")

    Return()

    # Function_36_49EC end

    def Function_37_4A32(): pass

    label("Function_37_4A32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A77")
    SetChrPos(0xFE, -39120, 0, -7690, 180)
    OP_8E(0xFE, 0xFFFF6730, 0x0, 0xFFFF7E5A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF6730, 0x0, 0xFFFFE1F6, 0xBB8, 0x0)
    Jump("Function_37_4A32")

    label("loc_4A77")

    Return()

    # Function_37_4A32 end

    def Function_38_4A78(): pass

    label("Function_38_4A78")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AE5")
    SetChrPos(0xFE, -54990, -3750, -18870, 180)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    Jump("Function_38_4A78")

    label("loc_4AE5")

    Return()

    # Function_38_4A78 end

    def Function_39_4AE6(): pass

    label("Function_39_4AE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B53")
    SetChrPos(0xFE, -74820, -3500, -19000, 180)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    Jump("Function_39_4AE6")

    label("loc_4B53")

    Return()

    # Function_39_4AE6 end

    def Function_40_4B54(): pass

    label("Function_40_4B54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BC1")
    SetChrPos(0xFE, -74820, -3500, -30850, 180)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    Jump("Function_40_4B54")

    label("loc_4BC1")

    Return()

    # Function_40_4B54 end

    def Function_41_4BC2(): pass

    label("Function_41_4BC2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C2F")
    SetChrPos(0xFE, -54990, -3750, -30850, 180)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFF877E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFEDBBC, 0xFFFFF254, 0xFFFFB5C8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFFB64A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF2932, 0xFFFFF15A, 0xFFFF877E, 0xBB8, 0x0)
    Jump("Function_41_4BC2")

    label("loc_4C2F")

    Return()

    # Function_41_4BC2 end

    def Function_42_4C30(): pass

    label("Function_42_4C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB3")
    OP_A2(0x62E)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -78280, 1760, 11580, 0)
    SetChrPos(0x102, -79290, 1760, 11770, 45)

    def lambda_4C6E():
        OP_6C(350000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C6E)
    OP_6D(-79030, 1760, 13490, 2000)
    Sleep(1000)

    ChrTalk(    #172
        0x101,
        "#000F(All right, we made it!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        (
            "#010F(Stay focused, Estelle...)\x02\x03",

            "(I'll go in first. Stay close.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#000F(Okay...!)\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFECB04, 0x6E0, 0x30C0, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_70(0xC, 0x3C)
    OP_73(0xC)

    def lambda_4D37():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D37)

    def lambda_4D49():
        OP_8E(0xFE, 0xFFFECBB8, 0x6E0, 0x369C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D49)
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_8E(0x101, 0xFFFECCDA, 0x6E0, 0x30A2, 0x3E8, 0x0)

    def lambda_4D87():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D87)
    OP_8E(0x101, 0xFFFECBB8, 0x6E0, 0x369C, 0x3E8, 0x0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4134   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4DB3")

    Return()

    # Function_42_4C30 end

    def Function_43_4DB4(): pass

    label("Function_43_4DB4")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_6D(-79450, 4770, 11320, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(39000, 0)
    OP_6E(478, 0)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrPos(0xF, -80280, 1520, 11070, 218)
    SetChrPos(0x10, -77730, 1490, 10600, 146)
    SetChrPos(0x11, -81930, 1250, 9130, 327)
    SetChrPos(0x12, -79450, 1250, 9450, 44)
    SetChrPos(0x13, -76040, 1250, 8290, 156)
    SetChrPos(0x14, -81880, 750, 6280, 145)
    SetChrPos(0x15, -79420, 250, 5000, 190)
    SetChrPos(0x16, -77590, 750, 6270, 7)

    def lambda_4F08():
        OP_67(0, 11700, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F08)

    def lambda_4F20():
        OP_6C(351000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F20)

    def lambda_4F30():
        OP_6E(544, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F30)
    OP_43(0x101, 0x0, 0x0, 0x2C)

    def lambda_4F47():
        OP_90(0xFE, 0xFFFFEC78, 0x27B0, 0xFFFFB1E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4F47)
    Sleep(500)
    OP_22(0x8D, 0x0, 0x64)

    def lambda_4F6C():
        OP_90(0xFE, 0xFFFFF63C, 0x6630, 0xFFFFADF8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F6C)

    def lambda_4F87():
        OP_90(0xFE, 0x2710, 0x4EC0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4F87)
    Sleep(200)

    def lambda_4FA7():
        OP_90(0xFE, 0x3A98, 0x3B38, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4FA7)
    Sleep(200)

    def lambda_4FC7():
        OP_90(0xFE, 0x3A98, 0x4EC0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4FC7)

    def lambda_4FE2():
        OP_90(0xFE, 0xFFFFEC78, 0x3B38, 0xFFFFD8F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4FE2)
    Sleep(500)

    def lambda_5002():
        OP_90(0xFE, 0x3A98, 0x3B38, 0xFFFFEC78, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5002)
    Sleep(300)

    def lambda_5022():
        OP_90(0xFE, 0xFFFFD8F0, 0x3B38, 0xFFFFC568, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5022)
    Sleep(6000)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_4DB4 end

    def Function_44_5049(): pass

    label("Function_44_5049")

    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Return()

    # Function_44_5049 end

    def Function_45_506D(): pass

    label("Function_45_506D")

    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_END)), "loc_50F4")

    ChrTalk(    #175
        0x102,
        (
            "#010FIt's late. Why don't we save\x01",
            "the sewers for later?\x02\x03",

            "We can check it out when\x01",
            "Zin and Olivier are with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519F")

    label("loc_50F4")


    ChrTalk(    #176
        0x102,
        (
            "#010FThis must be the entrance to\x01",
            "the Grancel Sewers that the\x01",
            "Ravens mentioned.\x02\x03",

            "It's late, so why don't we check\x01",
            "this out tomorrow when Zin and\x01",
            "Olivier are with us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519F")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_45_506D end

    def Function_46_51BB(): pass

    label("Function_46_51BB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #177
        (
            "\x07\x05Harbor District\x01",
            "※Unauthorized entry prohibited\x01",
            "due to heightened security.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_51BB end

    def Function_47_5239(): pass

    label("Function_47_5239")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #178
        (
            "\x07\x05House for Sale\x01",
            "※Easy conversion to restaurant!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_5239 end

    def Function_48_529B(): pass

    label("Function_48_529B")

    SetPlaceName(0xB8)
    Return()

    # Function_48_529B end

    def Function_49_529F(): pass

    label("Function_49_529F")

    SetPlaceName(0xB7)
    Return()

    # Function_49_529F end

    def Function_50_52A3(): pass

    label("Function_50_52A3")

    SetPlaceName(0xAF)
    Return()

    # Function_50_52A3 end

    SaveToFile()

Try(main)
