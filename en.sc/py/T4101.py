from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T4101   ._SN',
            'ED6_DT21/T4101_1 ._SN',
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
        'Private Tact',                         # 9
        'Private Bergan',                       # 10
        'Robyn',                                # 11
        'Miele',                                # 12
        'Godfrey',                              # 13
        'Phoebe',                               # 14
        'Nana',                                 # 15
        'Anton',                                # 16
        'Ricky',                                # 17
        'Sorbet',                               # 18
        'Clare',                                # 19
        'Nemo',                                 # 20
        'Jimmy',                                # 21
        'Laone',                                # 22
        'Marsha',                               # 23
        'Builna',                               # 24
        'Royal Army Soldier',                   # 25
        'Royal Army Soldier',                   # 26
        'Royal Army Soldier',                   # 27
        'Renne',                                # 28
        'Tita',                                 # 29
        'Tourist',                              # 30
        'Tourist',                              # 31
        'Berry',                                # 32
        'Tourist',                              # 33
        'Tourist',                              # 34
        'Tourist',                              # 35
        'Royal Army Soldier',                   # 36
        'Licia',                                # 37
        'Maintenance Chief Gustav',             # 38
        'Faye',                                 # 39
        'Haulage Vehicle',                      # 40
        'Kanone',                               # 41
        'Special Ops Soldier',                  # 42
        'Special Ops Soldier',                  # 43
        'Special Ops Soldier',                  # 44
        'Special Ops Soldier',                  # 45
        'Special Ops Soldier',                  # 46
        'Special Ops Soldier',                  # 47
        'Special Ops Soldier',                  # 48
        'Special Ops Soldier',                  # 49
        'Special Ops Soldier',                  # 50
        'Special Ops Soldier',                  # 51
        'Special Ops Soldier',                  # 52
        'Special Ops Soldier',                  # 53
        'Special Ops Soldier',                  # 54
        'Special Ops Soldier',                  # 55
        'Special Ops Soldier',                  # 56
        'Special Ops Soldier',                  # 57
        'Enhanced Jaeger',                      # 58
        'Enhanced Jaeger',                      # 59
        'Enhanced Jaeger',                      # 60
        'Enhanced Jaeger',                      # 61
        'Enhanced Jaeger',                      # 62
        'Enhanced Jaeger',                      # 63
        'Enhanced Jaeger',                      # 64
        'Enhanced Jaeger',                      # 65
        'Enhanced Jaeger',                      # 66
        'Enhanced Jaeger',                      # 67
        'Vanguard',                             # 68
        'Vanguard',                             # 69
        'Steel Cougar',                         # 70
        'Steel Cougar',                         # 71
        'Nial',                                 # 72
        'Dorothy',                              # 73
        'Soldier',                              # 74
        'Soldier',                              # 75
        'Soldier',                              # 76
        'Soldier',                              # 77
        'Grancel - North Block',                # 78
        'Grancel - South Block',                # 79
        'Grancel Landing Port',                 # 80
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
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02440 ._CH',             # 03
        'ED6_DT26/CH20304 ._CH',             # 04
        'ED6_DT07/CH01470 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH02480 ._CH',             # 09
        'ED6_DT07/CH02490 ._CH',             # 0A
        'ED6_DT07/CH01143 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT07/CH01110 ._CH',             # 0E
        'ED6_DT07/CH01680 ._CH',             # 0F
        'ED6_DT07/CH01690 ._CH',             # 10
        'ED6_DT07/CH01050 ._CH',             # 11
        'ED6_DT07/CH01490 ._CH',             # 12
        'ED6_DT07/CH01153 ._CH',             # 13
        'ED6_DT07/CH01030 ._CH',             # 14
        'ED6_DT27/CH03510 ._CH',             # 15
        'ED6_DT27/CH03060 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02440P._CP',             # 03
        'ED6_DT26/CH20304P._CP',             # 04
        'ED6_DT07/CH01470P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH02480P._CP',             # 09
        'ED6_DT07/CH02490P._CP',             # 0A
        'ED6_DT07/CH01143P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT07/CH01110P._CP',             # 0E
        'ED6_DT07/CH01680P._CP',             # 0F
        'ED6_DT07/CH01690P._CP',             # 10
        'ED6_DT07/CH01050P._CP',             # 11
        'ED6_DT07/CH01490P._CP',             # 12
        'ED6_DT07/CH01153P._CP',             # 13
        'ED6_DT07/CH01030P._CP',             # 14
        'ED6_DT27/CH03510P._CP',             # 15
        'ED6_DT27/CH03060P._CP',             # 16
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 74970,
        Z                   = 0,
        Y                   = 71250,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 100180,
        Z                   = 250,
        Y                   = 33080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 46290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 44530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 46260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 47860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 70490,
        Z                   = 250,
        Y                   = 6990,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 71500,
        Z                   = 750,
        Y                   = 7870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 1250,
        Y                   = 49800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = 250,
        Y                   = 49340,
        Direction           = 227,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 49630,
        Z                   = 0,
        Y                   = 61870,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 50410,
        Z                   = 0,
        Y                   = 81110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 81160,
        Z                   = 0,
        Y                   = -2940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 69020,
        Z                   = 250,
        Y                   = 4960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 63010,
        Z                   = 0,
        Y                   = 62930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 93700,
        Z                   = 0,
        Y                   = 32900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 53830,
        Z                   = 250,
        Y                   = 24100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 54040,
        Z                   = 250,
        Y                   = 8750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 42240,
        Z                   = 1250,
        Y                   = 51400,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 41280,
        Z                   = 1250,
        Y                   = 52380,
        Direction           = 146,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 76500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 77950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 69930,
        Z                   = 250,
        Y                   = 67560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 49030,
        Z                   = 0,
        Y                   = -3820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 73950,
        Z                   = 250,
        Y                   = 44280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 47630,
        Z                   = 250,
        Y                   = 29460,
        Direction           = 257,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 124170,
        Z                   = -3500,
        Y                   = 72870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17760,
        Z                   = 0,
        Y                   = 63880,
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
        X                   = 29270,
        Z                   = 0,
        Y                   = -950,
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
        X                   = 51010,
        Z                   = 0,
        Y                   = 102170,
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
        X                   = 42000,
        Y                   = -2000,
        Z                   = 71500,
        Range               = 59000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x122A0,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 109720,
        Y                   = 1000,
        Z                   = 32980,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 36,
    )

    DeclEvent(
        X                   = 76740,
        Y                   = 1000,
        Z                   = 23010,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 69950,
        Y                   = 1000,
        Z                   = 14290,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 63260,
        Y                   = 1000,
        Z                   = 22960,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 69910,
        Y                   = 1000,
        Z                   = 31710,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 42920,
        Y                   = 0,
        Z                   = 81110,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 70940,
        Y                   = 0,
        Z                   = -9490,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )

    DeclEvent(
        X                   = 75010,
        Y                   = 0,
        Z                   = 71300,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 40,
    )


    DeclActor(
        TriggerX            = 38820,
        TriggerZ            = 1250,
        TriggerY            = 36920,
        TriggerRange        = 800,
        ActorX              = 38820,
        ActorZ              = 2250,
        ActorY              = 36920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 124880,
        TriggerZ            = -3500,
        TriggerY            = 70940,
        TriggerRange        = 800,
        ActorX              = 124880,
        ActorZ              = -2500,
        ActorY              = 70940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_BCA",          # 00, 0
        "Function_1_F47",          # 01, 1
        "Function_2_1269",         # 02, 2
        "Function_3_128D",         # 03, 3
        "Function_4_137A",         # 04, 4
        "Function_5_1427",         # 05, 5
        "Function_6_1560",         # 06, 6
        "Function_7_1605",         # 07, 7
        "Function_8_170A",         # 08, 8
        "Function_9_181F",         # 09, 9
        "Function_10_1880",        # 0A, 10
        "Function_11_18DB",        # 0B, 11
        "Function_12_1E2D",        # 0C, 12
        "Function_13_2612",        # 0D, 13
        "Function_14_2DDF",        # 0E, 14
        "Function_15_3BE9",        # 0F, 15
        "Function_16_411F",        # 10, 16
        "Function_17_41D4",        # 11, 17
        "Function_18_4289",        # 12, 18
        "Function_19_433E",        # 13, 19
        "Function_20_43F3",        # 14, 20
        "Function_21_4BBE",        # 15, 21
        "Function_22_4BE3",        # 16, 22
        "Function_23_4C08",        # 17, 23
        "Function_24_4C49",        # 18, 24
        "Function_25_5286",        # 19, 25
        "Function_26_6716",        # 1A, 26
        "Function_27_6732",        # 1B, 27
        "Function_28_674E",        # 1C, 28
        "Function_29_676A",        # 1D, 29
        "Function_30_6786",        # 1E, 30
        "Function_31_67CA",        # 1F, 31
        "Function_32_6812",        # 20, 32
        "Function_33_68AD",        # 21, 33
        "Function_34_6937",        # 22, 34
        "Function_35_69C6",        # 23, 35
        "Function_36_6A15",        # 24, 36
        "Function_37_6A19",        # 25, 37
        "Function_38_6A1D",        # 26, 38
        "Function_39_6A21",        # 27, 39
        "Function_40_6A25",        # 28, 40
        "Function_41_6A29",        # 29, 41
    )


    def Function_0_BCA(): pass

    label("Function_0_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C08")
    SetChrPos(0x9, 77220, 250, 71250, 180)
    SetChrPos(0x13, 47790, 250, 48080, 37)
    SetChrFlags(0x13, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C08")
    ClearChrFlags(0x13, 0x10)

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C24")
    SetChrPos(0x8, 68770, 250, -9000, 0)

    label("loc_C24")

    OP_43(0x19, 0x2, 0x0, 0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C53")
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    Jump("loc_E74")

    label("loc_C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_CB5")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x13, 47790, 250, 48080, 37)
    SetChrPos(0x1D, 47840, 250, 78050, 2)
    SetChrPos(0x1E, 47840, 250, 79500, 180)
    SetChrPos(0x22, 42990, 1250, 52970, 29)
    SetChrFlags(0x1D, 0x10)
    Jump("loc_E74")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D19")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x13, 49630, 0, 61870, 45)
    SetChrPos(0x1D, 53310, 250, 72710, 324)
    SetChrPos(0x1E, 53180, 250, 74370, 320)
    SetChrPos(0x1F, 60880, 250, 67010, 180)
    SetChrPos(0x22, 53110, 250, 8150, 273)
    Jump("loc_E74")

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB3")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrPos(0x13, 49630, 0, 61870, 45)
    SetChrPos(0x1D, 53140, 250, 23270, 180)
    SetChrPos(0x1E, 53500, 250, 22190, 315)
    SetChrPos(0x1F, 71900, 250, 60850, 9)
    SetChrPos(0x22, 56200, 250, 26240, 252)
    SetChrPos(0x23, 124210, -3500, 70990, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB0")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_DB0")

    Jump("loc_E74")

    label("loc_DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E21")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrPos(0x13, 47790, 250, 48080, 37)
    SetChrPos(0x1D, 93990, 0, 34340, 180)
    SetChrPos(0x1E, 93990, 0, 32670, 0)
    SetChrPos(0x22, 39640, 1250, 51520, 221)
    SetChrPos(0x23, 124210, -3500, 70990, 270)
    Jump("loc_E74")

    label("loc_E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E74")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x1D, 107750, 1250, 32920, 93)
    SetChrPos(0x1E, 109710, 1650, 31920, 75)
    SetChrPos(0x23, 124210, -3500, 70990, 270)

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_E8A")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_F46")

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_EA0")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 20)
    Jump("loc_F46")

    label("loc_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_F22")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Event(1, 29)
    Jump("loc_F46")

    label("loc_F22")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_F2E"),
        (SWITCH_DEFAULT, "loc_F46"),
    )


    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F43")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_F43")

    Jump("loc_F46")

    label("loc_F46")

    Return()

    # Function_0_BCA end

    def Function_1_F47(): pass

    label("Function_1_F47")

    OP_16(0x2, 0xFA0, 0xFFFF4C50, 0xFFFEA070, 0x23005C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F79")
    OP_B1("t4101_y")
    Jump("loc_F82")

    label("loc_F79")

    OP_B1("t4101_n")

    label("loc_F82")

    OP_71(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9C")
    OP_10(0xC, 0x1)
    OP_10(0xB, 0x0)
    Jump("loc_FB2")

    label("loc_F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_FAC")
    OP_10(0xC, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_FB2")

    label("loc_FAC")

    OP_10(0xB, 0x0)
    OP_10(0xC, 0x1)

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FC6")
    OP_71(0x9, 0x10)
    OP_1C(0x9, 0x0, 0x29)
    Jump("loc_102C")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_FE1")
    OP_71(0x9, 0x10)
    OP_1C(0x9, 0x0, 0x29)
    Jump("loc_FE6")

    label("loc_FE1")

    OP_72(0x9, 0x10)

    label("loc_FE6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_FF2"),
        (SWITCH_DEFAULT, "loc_1010"),
    )


    label("loc_FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1010")
    OP_71(0x9, 0x10)
    OP_1C(0x9, 0x0, 0x29)
    OP_A2(0x5)
    Jump("loc_1010")

    label("loc_1010")

    Jump("loc_102C")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 7)), scpexpr(EXPR_END)), "loc_1027")
    OP_71(0x9, 0x10)
    OP_1C(0x9, 0x0, 0x29)
    Jump("loc_102C")

    label("loc_1027")

    OP_72(0x9, 0x10)

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1040")
    OP_71(0xA, 0x10)
    OP_1C(0xA, 0x0, 0x29)
    Jump("loc_10A6")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_108D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_105B")
    OP_71(0xA, 0x10)
    OP_1C(0xA, 0x0, 0x29)
    Jump("loc_1060")

    label("loc_105B")

    OP_72(0xA, 0x10)

    label("loc_1060")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_106C"),
        (SWITCH_DEFAULT, "loc_108A"),
    )


    label("loc_106C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108A")
    OP_71(0xA, 0x10)
    OP_1C(0xA, 0x0, 0x29)
    OP_A2(0x3)
    Jump("loc_108A")

    label("loc_108A")

    Jump("loc_10A6")

    label("loc_108D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 3)), scpexpr(EXPR_END)), "loc_10A1")
    OP_71(0xA, 0x10)
    OP_1C(0xA, 0x0, 0x29)
    Jump("loc_10A6")

    label("loc_10A1")

    OP_72(0xA, 0x10)

    label("loc_10A6")

    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0x8, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FE")
    OP_71(0x5, 0x10)
    OP_71(0x6, 0x10)
    OP_71(0x7, 0x10)
    OP_71(0x8, 0x10)
    OP_1C(0x5, 0x1, 0x4A)
    OP_1C(0x6, 0x1, 0x49)
    OP_1C(0x7, 0x1, 0x49)
    OP_1C(0x8, 0x1, 0x4B)

    label("loc_10FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112D")
    OP_71(0x5, 0x10)
    OP_71(0x6, 0x10)
    OP_71(0x7, 0x10)
    OP_71(0x8, 0x10)

    label("loc_112D")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_113E")
    OP_72(0xB, 0x10)

    label("loc_113E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117A")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 59)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 59)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 59)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 59)

    label("loc_117A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1268")
    OP_D2(0x70120, 0x70124, 0x0)
    OP_D2(0x7010A, 0x7010E, 0x1)
    OP_D2(0x700E3, 0x700E7, 0x2)
    OP_D2(0x70354, 0x70359, 0x3)
    OP_D2(0x2600CC, 0x2600D1, 0x4)
    OP_D2(0x700FB, 0x700FF, 0x5)
    OP_D2(0x700BB, 0x700BF, 0x6)
    OP_D2(0x700A8, 0x700AC, 0x7)
    OP_D2(0x700B8, 0x700BC, 0x8)
    OP_D2(0x7035D, 0x70362, 0x9)
    OP_D2(0x7035E, 0x70363, 0xA)
    OP_D2(0x703E4, 0x703E8, 0xB)
    OP_D2(0x700B2, 0x700B6, 0xC)
    OP_D2(0x700C9, 0x700CD, 0xD)
    OP_D2(0x700B3, 0x700B7, 0xE)
    OP_D2(0x70128, 0x7012C, 0xF)
    OP_D2(0x70129, 0x7012D, 0x10)
    OP_D2(0x700A9, 0x700AD, 0x11)
    OP_D2(0x70101, 0x70105, 0x12)
    OP_D2(0x703E5, 0x703E9, 0x13)
    OP_D2(0x700A3, 0x700A7, 0x14)
    OP_D2(0x2701C7, 0x2701CC, 0x15)
    OP_D2(0x270060, 0x270064, 0x16)

    label("loc_1268")

    Return()

    # Function_1_F47 end

    def Function_2_1269(): pass

    label("Function_2_1269")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_128C")
    OP_8D(0xFE, 102900, 37500, 97550, 28500, 2000)
    Jump("Function_2_1269")

    label("loc_128C")

    Return()

    # Function_2_1269 end

    def Function_3_128D(): pass

    label("Function_3_128D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1379")
    OP_8E(0xFE, 0xCCF6, 0x0, 0xFFFFF484, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0x8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0xF32A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCFE4, 0x0, 0x100A4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15AC2, 0x0, 0xFCBC, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16314, 0x0, 0xFB86, 0x9C4, 0x0)
    OP_8E(0xFE, 0x164E0, 0x0, 0x826E, 0x9C4, 0x0)
    OP_8C(0x15, 90, 400)
    Sleep(4000)
    OP_8E(0xFE, 0x164E0, 0x0, 0x7E86, 0x9C4, 0x0)
    OP_8C(0x15, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x16152, 0x0, 0x4CE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15B12, 0x0, 0xFFFFF8BC, 0x9C4, 0x0)
    Jump("Function_3_128D")

    label("loc_1379")

    Return()

    # Function_3_128D end

    def Function_4_137A(): pass

    label("Function_4_137A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1426")
    OP_8E(0xFE, 0xCE9A, 0x0, 0xF5D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0xF258, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0x816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCEEA, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15590, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0x6B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0xEF56, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15572, 0x28, 0xF5D2, 0x7D0, 0x0)
    Jump("Function_4_137A")

    label("loc_1426")

    Return()

    # Function_4_137A end

    def Function_5_1427(): pass

    label("Function_5_1427")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_155F")
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x1360, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x59EC, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEA2E, 0x4E2, 0x59EC, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEA2E, 0x4E2, 0x84B2, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFA5A, 0x4E2, 0x8CC8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10928, 0x4E2, 0x8CC8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11148, 0x4E2, 0x9470, 0x9C4, 0x0)
    OP_8E(0xFE, 0x111CA, 0x4E2, 0xCAB2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x130BA, 0x4E2, 0xCAB2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x130BA, 0x4E2, 0xBA36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0xABF4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11968, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10CE8, 0x4E2, 0x272E, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10CE8, 0xFA, 0x16C6, 0x9C4, 0x0)
    Jump("Function_5_1427")

    label("loc_155F")

    Return()

    # Function_5_1427 end

    def Function_6_1560(): pass

    label("Function_6_1560")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1604")
    OP_8E(0xFE, 0x16E04, 0x0, 0x9DBC, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x8084, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x61EE, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x8084, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_6_1560")

    label("loc_1604")

    Return()

    # Function_6_1560 end

    def Function_7_1605(): pass

    label("Function_7_1605")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1709")
    OP_8E(0xFE, 0xD2F0, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14F64, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14C44, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x10F86, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10F86, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0x6586, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD246, 0xFA, 0x5E24, 0x9C4, 0x0)
    Jump("Function_7_1605")

    label("loc_1709")

    Return()

    # Function_7_1605 end

    def Function_8_170A(): pass

    label("Function_8_170A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_181E")
    OP_8E(0xFE, 0xD2F0, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    Call(0, 10)
    OP_8E(0xFE, 0x14F64, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    Call(0, 10)
    OP_8E(0xFE, 0x14C44, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    Call(0, 10)
    OP_8E(0xFE, 0x10F86, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10F86, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(1500)
    Call(0, 10)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0x6586, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD246, 0xFA, 0x5E24, 0x9C4, 0x0)
    Jump("Function_8_170A")

    label("loc_181E")

    Return()

    # Function_8_170A end

    def Function_9_181F(): pass

    label("Function_9_181F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_187F")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1873")
    OP_4B(0xFE, 0)
    Jump("loc_1877")

    label("loc_1873")

    OP_4A(0xFE, 0)

    label("loc_1877")

    Sleep(100)
    Jump("Function_9_181F")

    label("loc_187F")

    Return()

    # Function_9_181F end

    def Function_10_1880(): pass

    label("Function_10_1880")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18DA")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D2")
    Sleep(100)
    Return()

    label("loc_18D2")

    Sleep(100)
    Jump("Function_10_1880")

    label("loc_18DA")

    Return()

    # Function_10_1880 end

    def Function_11_18DB(): pass

    label("Function_11_18DB")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x108, 70950, 0, -6900, 180)
    SetChrPos(0x101, 71720, 0, -5910, 180)
    SetChrPos(0x105, 70350, 0, -5760, 180)
    SetChrPos(0x104, 70950, 0, -4800, 180)
    OP_6D(71730, 0, -7500, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 0, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 4)), scpexpr(EXPR_END)), "loc_1A14")

    ChrTalk(    #0
        0x8,
        (
            "Hey, Zin! Still keepin' busy?\x02\x03",

            "Lemme guess, business at the embassy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        (
            "#070F#6PYeah, I'd like to speak to\x01",
            "Elsa about something.\x02\x03",

            "She's in, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF9")

    label("loc_1A14")


    ChrTalk(    #2
        0x108,
        "#071F#6PHey! How goes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "Huh? Zin! Holy crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "Wastin' time in Liberl-ville again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x108,
        (
            "#070F#6PHaha. Something like that.\x02\x03",

            "Thought I'd say hello to Elsa, and I have\x01",
            "something I need to talk to her about.\x02\x03",

            "Is she in?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF9")


    ChrTalk(    #6
        0x8,
        (
            "Well, I haven't seen her leave,\x01",
            "so I guess she's around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Oh, who's with you?\x01",
            "Gotta ask, you know. Policy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x108,
        (
            "#070F#6POh, they're helping me with some\x01",
            "guild work.\x02\x03",

            "I'm going to introduce them to Elsa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Huh, well, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "If they're with you, Zin,\x01",
            "I guess I can let 'em in.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1000)
    OP_8E(0x8, 0x10CA2, 0xFA, 0xFFFFDCD8, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #11
        0x8,
        "So! Welcome to the Calvardian embassy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Oh, do keep in mind that the embassy hall\x01",
            "is Calvard soil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "Calvard and Liberl are friends, but still,\x01",
            "keep your nose clean, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #14
        0x101,
        "#1006F#6PYou hear that, Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x104,
        (
            "#034FAnd again my heart is assaulted with arrows!\x01",
            "How little trust you have in me!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71150, 0, -6670, 180)
    SetChrPos(0x1, 71150, 0, -6670, 180)
    SetChrPos(0x2, 71150, 0, -6670, 180)
    SetChrPos(0x3, 71150, 0, -6670, 180)
    OP_0D()
    OP_A2(0x161B)
    EventEnd(0x0)
    Return()

    # Function_11_18DB end

    def Function_12_1E2D(): pass

    label("Function_12_1E2D")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 75060, 0, 69850, 0)
    SetChrPos(0x101, 74090, 0, 68370, 0)
    SetChrPos(0x105, 75800, 0, 68680, 0)
    SetChrPos(0x108, 74770, 0, 67260, 0)
    OP_6D(75780, 0, 70890, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 5)), scpexpr(EXPR_END)), "loc_1F4A")

    ChrTalk(    #16
        0x9,
        "#6POh, Olivier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#035F#7PHeh, you continue to play your\x01",
            "role well, Bergan.\x02\x03",

            "#030FI would like to enter. May we pass?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1F4A")


    ChrTalk(    #18
        0x104,
        "#031F#7PHello, Bergan. You've been well, I hope?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x9,
        "#6POLIVIER?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        "#6PWhere in the hell have you BEEN?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        "#033F#7PWhy, I've been places. What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        "#6PHmph. 'What's wrong,' he says...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#6PYou've been totally incommunicado\x01",
            "ever since you went to Elmo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#6PMajor Vander's about ready to\x01",
            "throw you out a window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x104,
        (
            "#035F#7PAh, he wishes to launch me like a love rocket!\x01",
            "Adorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1007F#2PUh... Olivier?\x02\x03",

            "#1019FDid you seriously forget to tell Mueller\x01",
            "and the embassy you were with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x104,
        (
            "#031F#6PHa-ha-ha!\x02\x03",

            "When wandering the roads, hunting for love,\x01",
            "one must be discreet and secretive!\x02\x03",

            "#030FWell, Bergan. May we enter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F7")


    ChrTalk(    #28
        0x9,
        (
            "#6PI can't say no to you, but,\x01",
            "uh...who's with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1006F#2POh! We're from the Bracer Guild.\x02\x03",

            "We'd like to ask the ambassador a few things,\x01",
            "if that's okay.\x02\x03",

            "We thought we'd try having Olivier\x01",
            "introduce us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "#6POh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        "#6PWell, I can certainly let you in, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#6PLord Ambassador Crainagh and Major Vander\x01",
            "are out at the moment, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x104,
        "#033F#7POh? A pity.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 180, 400)

    ChrTalk(    #34
        0x104,
        (
            "#030F#6PWhat shall we do, Estelle?\x01",
            "We can wait inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1015F#2PWe could, but...\x02\x03",

            "#1006FWe're kind of burning daylight here,\x01",
            "so I'd like to visit some of the other\x01",
            "places while we wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x105,
        (
            "#040F#4PWe could visit the Calvardian embassy\x01",
            "first, then.\x02\x03",

            "It's just across the plaza from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x108,
        (
            "#070FYes, getting back here won't take long\x01",
            "after meeting with Elsa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1006F#2PThat's decided, then.\x02\x03",

            "We'll be back later, sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#6PI'll let the major know you were here.\x01",
            "See you later!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_8C(0x9, 180, 0)
    OP_6D(74860, 0, 68920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74860, 0, 68920, 0)
    SetChrPos(0x1, 74860, 0, 68920, 0)
    SetChrPos(0x2, 74860, 0, 68920, 0)
    SetChrPos(0x3, 74860, 0, 68920, 0)
    OP_0D()
    OP_A2(0x161E)
    EventEnd(0x0)
    Return()

    # Function_12_1E2D end

    def Function_13_2612(): pass

    label("Function_13_2612")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 75060, 0, 69850, 0)
    SetChrPos(0x101, 74090, 0, 68370, 0)
    SetChrPos(0x105, 75800, 0, 68680, 0)
    SetChrPos(0x108, 74770, 0, 67260, 0)
    OP_6D(75780, 0, 70890, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2752")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "- Set as first convo w/ Bergan\x01",            # 0
            "- Set as already talking with Bergan\x01",      # 1
            "- No change\x01",                               # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2746"),
        (1, "loc_274C"),
        (SWITCH_DEFAULT, "loc_2752"),
    )


    label("loc_2746")

    OP_A3(0x161E)
    Jump("loc_2752")

    label("loc_274C")

    OP_A2(0x161E)
    Jump("loc_2752")

    label("loc_2752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 5)), scpexpr(EXPR_END)), "loc_27E2")

    ChrTalk(    #40
        0x9,
        "#6POh, Olivier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x104,
        (
            "#035F#7PHeh, you continue to play your\x01",
            "role well, Bergan.\x02\x03",

            "#030FI would like to enter. May we pass?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A90")

    label("loc_27E2")


    ChrTalk(    #42
        0x104,
        "#031F#7PHello, Bergan. You've been well, I hope?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x9,
        "#6POLIVIER?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "#6PWhere in the hell have you BEEN?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x104,
        "#033F#7PWhy, I've been places. What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#6PHmph. 'What's wrong?', he says...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "#6PYou've been totally incommunicado\x01",
            "ever since you went to Elmo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#6PMajor Vander's about ready to\x01",
            "throw you out a window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x104,
        (
            "#035F#7PAh, he wishes to launch me like a love rocket!\x01",
            "Adorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1007F#2PUh... Olivier?\x02\x03",

            "#1019FDid you seriously forget to tell Mueller\x01",
            "and the embassy you were with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x104,
        (
            "#031F#6PHa-ha-ha!\x02\x03",

            "When wandering the roads, hunting for love,\x01",
            "one must be discreet and secretive!\x02\x03",

            "#030FWell, Bergan. May we enter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A90")


    ChrTalk(    #52
        0x9,
        (
            "#6PI can't say no to you, but,\x01",
            "uh...who's with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1006F#2POh! We're from the Bracer Guild.\x02\x03",

            "We'd like to ask the ambassador a few things,\x01",
            "if that's okay.\x02\x03",

            "We thought we'd try having Olivier introduce\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "#6POh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#6PWell, there shouldn't be a problem with\x01",
            "letting you in, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C71")

    label("loc_2BC6")


    ChrTalk(    #56
        0x9,
        "#6POh, hello again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "#6PLord Ambassador Crainagh and Major Vander\x01",
            "just returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x104,
        "#031F#7PAh, perfect timing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1011F#2PCan we go in, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "#6PSure!\x02",
    )

    CloseMessageWindow()

    label("loc_2C71")

    OP_8C(0x9, 0, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3C)
    Sleep(1000)
    OP_8E(0x9, 0x12DA4, 0xFA, 0x11652, 0xBB8, 0x0)
    OP_8C(0x9, 225, 400)
    Sleep(500)

    ChrTalk(    #61
        0x9,
        "#6PWelcome to the Erebonian embassy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#6PDo remember that the embassy is\x01",
            "Erebonian soil, so be careful,\x01",
            "yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1006F#2PWe will be!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_8C(0x9, 180, 0)
    OP_6D(74870, 0, 68640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74870, 0, 68640, 0)
    SetChrPos(0x1, 74870, 0, 68640, 0)
    SetChrPos(0x2, 74870, 0, 68640, 0)
    SetChrPos(0x3, 74870, 0, 68640, 0)
    OP_0D()
    OP_A2(0x161F)
    EventEnd(0x0)
    Return()

    # Function_13_2612 end

    def Function_14_2DDF(): pass

    label("Function_14_2DDF")

    EventBegin(0x0)
    OP_4A(0x15, 255)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F85")
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as not visited the castle (heard Nial is not present)\x01",              # 0
            "Set as not visited the castle (haven't heard Nial is not present)\x01",      # 1
            "Set as visited the castle (heard Nial is not present)\x01",                  # 2
            "Set as visited the castle (haven't heard Nial is not present)\x01",          # 3
            "No change\x01",                                                              # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F31"),
        (1, "loc_2F46"),
        (2, "loc_2F5B"),
        (3, "loc_2F70"),
        (SWITCH_DEFAULT, "loc_2F85"),
    )


    label("loc_2F31")

    OP_A3(0x1623)
    OP_A3(0x1624)
    OP_A3(0x1625)
    OP_A3(0x1626)
    OP_A3(0x1627)
    OP_A2(0x1680)
    Jump("loc_2F85")

    label("loc_2F46")

    OP_A3(0x1623)
    OP_A3(0x1624)
    OP_A3(0x1625)
    OP_A3(0x1626)
    OP_A3(0x1627)
    OP_A3(0x1680)
    Jump("loc_2F85")

    label("loc_2F5B")

    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1680)
    Jump("loc_2F85")

    label("loc_2F70")

    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A3(0x1680)
    Jump("loc_2F85")

    label("loc_2F85")

    SetChrPos(0x104, 75810, 0, 65960, 0)
    SetChrPos(0x101, 74720, 0, 65970, 0)
    SetChrPos(0x105, 76080, 0, 64650, 0)
    SetChrPos(0x108, 74790, 0, 64580, 9)
    SetChrPos(0x130, 75150, 0, 67480, 180)
    OP_6D(74330, 0, 66970, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(308000, 0)
    OP_6E(262, 0)
    OP_6F(0x9, 60)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #64
        0x101,
        (
            "#1006F#3PThanks, Mueller.\x02\x03",

            "Talking with the ambassador\x01",
            "was a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x130,
        (
            "#277F#4PNo, you don't need to thank me.\x01",
            "I didn't do anything important, really.\x02\x03",

            "Besides, this is a problem affecting all\x01",
            "our nations. We should be working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x108,
        "#070F#3PHah! Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#542F#5PI do hope we can solve this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x104,
        "#032F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #69
        0x101,
        "#1004F#6PHuh? Olivier, you're awfully quiet.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 270, 400)

    ChrTalk(    #70
        0x104,
        (
            "#030F#7PHm? Ah, it's nothing... I was simply lost\x01",
            "in reverie for a moment.\x02\x03",

            "It...doesn't concern our current business.\x01",
            "Pay me no mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1015F#6POooookay...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x130,
        (
            "#270F#4P...\x02\x03",

            "#272FOlivier. You'll be staying here at the\x01",
            "embassy in the evenings while you're\x01",
            "here in Grancel, yes?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 0, 400)

    ChrTalk(    #73
        0x104,
        (
            "#031FHeh, where else?\x02\x03",

            "I would not miss the chance to have more\x01",
            "sweet dreams in your bed, as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1004F#6PWh-Whaaaaaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        "#044F#5POh...my...\x02",
    )

    CloseMessageWindow()
    OP_62(0x130, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x130,
        (
            "#274F#4P...Stop with the jokes before you give\x01",
            "the ladies too many ideas. And images.\x02\x03",

            "Push those jokes too far and I may have\x01",
            "to spear you upon the embassy flagpole.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0x104,
        (
            "#037FAh, so that's the direction I should approach\x01",
            "from! You teach me more every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x130,
        (
            "#276F#4PAlternately.\x02\x03",

            "I could just cut you in half right here.\x01",
            "I'm fairly sure I could explain it to\x01",
            "Lord Crainagh.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x104,
        (
            "#034FThat...would be rather less lovely.\x01",
            "Forgive the joke, my friend.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #80
        0x101,
        (
            "#1016F#3PAhaha... So that's how you keep\x01",
            "Olivier under control.\x01",
            "Maybe I should write this down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x108,
        (
            "#071F#3PHaha! I'd say they match each other\x01",
            "perfectly myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x130,
        (
            "#272F#4P...That's a terrifying thought.\x02\x03",

            "#277FWell, regardless. I shall pardon myself\x01",
            "here.\x02\x03",

            "Good luck with the rest of your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1006F#3PThanks again, Mueller!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 0, 400)

    def lambda_370D():
        OP_6D(74890, 0, 70490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_370D)

    def lambda_3725():
        OP_8E(0x130, 0x1228C, 0x0, 0x12D9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x130, 1, lambda_3725)
    Sleep(4000)
    OP_4A(0x9, 255)
    OP_8C(0x9, 270, 400)
    OP_8E(0x9, 0x124DA, 0x0, 0x11652, 0x7D0, 0x0)
    OP_8C(0x9, 0, 400)
    OP_22(0x6E, 0x0, 0x64)
    OP_71(0x9, 0x10)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)
    Sleep(1500)
    OP_8E(0x9, 0x12DA4, 0xFA, 0x11652, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    OP_4B(0x9, 255)

    def lambda_37A7():
        OP_6D(74740, 0, 65560, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37A7)

    def lambda_37BF():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37BF)
    OP_8C(0x9, 180, 400)
    OP_8C(0x104, 180, 400)
    WaitChrThread(0x101, 0x2)
    SetChrFlags(0x130, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3958")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_38A6")

    ChrTalk(    #84
        0x101,
        (
            "#1006F#7POkay! Looks like we got some daylight\x01",
            "to burn, still.\x02\x03",

            "How about we put the Liberl News aside for\x01",
            "the moment and go to Grancel Castle instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x105,
        "#040F#5PAfter you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3955")

    label("loc_38A6")


    ChrTalk(    #86
        0x101,
        (
            "#1006F#7PWith the embassies out of the way,\x01",
            "all that's left is the Liberl News.\x02\x03",

            "Hopefully Nial or someone will be\x01",
            "able to help us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x105,
        "#040FHopefully! Shall we be off?\x02",
    )

    CloseMessageWindow()

    label("loc_3955")

    Jump("loc_3B39")

    label("loc_3958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_3A35")

    ChrTalk(    #88
        0x104,
        (
            "#030F#4PEvening already... Time does fly when\x01",
            "you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x105,
        "#040F#5PNial should be back by now, hopefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1011F#7PYeah, hopefully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x108,
        "#070F#3PAll right! Let's get over to that newspaper.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B39")

    label("loc_3A35")


    ChrTalk(    #92
        0x104,
        (
            "#030F#4PEvening already... Time does fly when\x01",
            "you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x105,
        (
            "#040F#5PThe only letter victim we've yet to\x01",
            "visit is the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1006F#7PYep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x108,
        (
            "#070F#3PWell, let's not waste any more time, eh?\x01",
            "Let's get over there and see what's what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B39")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x2F, 0xFF)
    OP_6D(74890, 0, 65620, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74890, 0, 65620, 180)
    SetChrPos(0x1, 74890, 0, 65620, 180)
    SetChrPos(0x2, 74890, 0, 65620, 180)
    SetChrPos(0x3, 74890, 0, 65620, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1622)
    OP_71(0x9, 0x10)
    EventEnd(0x0)
    OP_4B(0x15, 255)
    OP_4B(0x17, 255)
    Return()

    # Function_14_2DDF end

    def Function_15_3BE9(): pass

    label("Function_15_3BE9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C0A")
    Call(0, 32)
    Call(0, 33)

    label("loc_3C0A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_3C22"),
        (106, "loc_3CA6"),
        (107, "loc_3D2A"),
        (108, "loc_3DAE"),
        (SWITCH_DEFAULT, "loc_3E32"),
    )


    label("loc_3C22")

    SetChrPos(0x101, 69080, 1250, 35450, 315)
    SetChrPos(0x107, 71080, 1250, 35550, 45)
    SetChrPos(0xF7, 69580, 1250, 33780, 225)
    SetChrPos(0xF9, 70630, 1250, 33820, 135)
    OP_6D(70020, 1250, 34440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    Jump("loc_3E32")

    label("loc_3CA6")

    SetChrPos(0x101, 81200, 1250, 24440, 45)
    SetChrPos(0x107, 81200, 1250, 22600, 135)
    SetChrPos(0xF7, 79390, 1250, 24250, 225)
    SetChrPos(0xF9, 79200, 1250, 22670, 315)
    OP_6D(79940, 1250, 23610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(303000, 0)
    OP_6E(262, 0)
    Jump("loc_3E32")

    label("loc_3D2A")

    SetChrPos(0x101, 71120, 1250, 10530, 135)
    SetChrPos(0x107, 69070, 1250, 10520, 225)
    SetChrPos(0xF7, 71070, 1250, 12090, 315)
    SetChrPos(0xF9, 69540, 1250, 12070, 45)
    OP_6D(70260, 1250, 11450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_3E32")

    label("loc_3DAE")

    SetChrPos(0x101, 59140, 1250, 22220, 225)
    SetChrPos(0x107, 59260, 1250, 24340, 315)
    SetChrPos(0xF7, 61220, 1250, 22110, 135)
    SetChrPos(0xF9, 61090, 1250, 23790, 45)
    OP_6D(59990, 1250, 23630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    Jump("loc_3E32")

    label("loc_3E32")

    SetChrFlags(0x16, 0x80)
    OP_4A(0x16, 255)
    SetChrPos(0x16, 62410, 250, 5400, 270)
    OP_43(0x101, 0x1, 0x0, 0x10)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    Sleep(300)
    OP_43(0xF7, 0x1, 0x0, 0x12)
    Sleep(100)
    OP_43(0x107, 0x1, 0x0, 0x11)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    OP_44(0x101, 0x1)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(1000)

    ChrTalk(    #96
        0x101,
        "#1007FErrrgh. I think we lost her again.\x02",
    )

    CloseMessageWindow()
    OP_44(0xF7, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(500)

    def lambda_3EDB():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3EDB)
    Sleep(100)

    def lambda_3EEE():
        TurnDirection(0xFE, 0xF9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3EEE)
    Sleep(100)

    def lambda_3F01():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3F01)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F63")

    ChrTalk(    #97
        0x106,
        (
            "#555FHow in the hell is she able to scuttle\x01",
            "around like this? Kids...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAD")

    label("loc_3F63")


    ChrTalk(    #98
        0x103,
        (
            "#524FMy goodness, this is like trying to catch\x01",
            "a hyperactive kitten.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_400D")

    ChrTalk(    #99
        0x108,
        (
            "#070FTita, you came with Renne to this department\x01",
            "store yesterday, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4060")

    label("loc_400D")


    ChrTalk(    #100
        0x105,
        (
            "#542FTita, you and Renne visited this department\x01",
            "store yesterday, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4060")


    ChrTalk(    #101
        0x107,
        (
            "#063FAh, yeah!\x02\x03",

            "#561FShe might've gone somewhere\x01",
            "else, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1006FI don't think she could've gotten too far.\x02\x03",

            "Let's look around the eastern block for her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x162E)
    OP_28(0x8C, 0x1, 0x4)
    EventEnd(0x0)
    ClearChrFlags(0x16, 0x80)
    OP_4B(0x16, 255)
    Return()

    # Function_15_3BE9 end

    def Function_16_411F(): pass

    label("Function_16_411F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_4137"),
        (106, "loc_415E"),
        (107, "loc_4185"),
        (108, "loc_41AC"),
        (SWITCH_DEFAULT, "loc_41D3"),
    )


    label("loc_4137")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_415B")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_4137")

    label("loc_415B")

    Jump("loc_41D3")

    label("loc_415E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4182")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_415E")

    label("loc_4182")

    Jump("loc_41D3")

    label("loc_4185")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A9")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_4185")

    label("loc_41A9")

    Jump("loc_41D3")

    label("loc_41AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41D0")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_41AC")

    label("loc_41D0")

    Jump("loc_41D3")

    label("loc_41D3")

    Return()

    # Function_16_411F end

    def Function_17_41D4(): pass

    label("Function_17_41D4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_41EC"),
        (106, "loc_4213"),
        (107, "loc_423A"),
        (108, "loc_4261"),
        (SWITCH_DEFAULT, "loc_4288"),
    )


    label("loc_41EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4210")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_41EC")

    label("loc_4210")

    Jump("loc_4288")

    label("loc_4213")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4237")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_4213")

    label("loc_4237")

    Jump("loc_4288")

    label("loc_423A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_425E")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_423A")

    label("loc_425E")

    Jump("loc_4288")

    label("loc_4261")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4285")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_4261")

    label("loc_4285")

    Jump("loc_4288")

    label("loc_4288")

    Return()

    # Function_17_41D4 end

    def Function_18_4289(): pass

    label("Function_18_4289")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_42A1"),
        (106, "loc_42C8"),
        (107, "loc_42EF"),
        (108, "loc_4316"),
        (SWITCH_DEFAULT, "loc_433D"),
    )


    label("loc_42A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42C5")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_42A1")

    label("loc_42C5")

    Jump("loc_433D")

    label("loc_42C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42EC")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_42C8")

    label("loc_42EC")

    Jump("loc_433D")

    label("loc_42EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4313")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_42EF")

    label("loc_4313")

    Jump("loc_433D")

    label("loc_4316")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_433A")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_4316")

    label("loc_433A")

    Jump("loc_433D")

    label("loc_433D")

    Return()

    # Function_18_4289 end

    def Function_19_433E(): pass

    label("Function_19_433E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_4356"),
        (106, "loc_437D"),
        (107, "loc_43A4"),
        (108, "loc_43CB"),
        (SWITCH_DEFAULT, "loc_43F2"),
    )


    label("loc_4356")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_437A")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_4356")

    label("loc_437A")

    Jump("loc_43F2")

    label("loc_437D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43A1")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_437D")

    label("loc_43A1")

    Jump("loc_43F2")

    label("loc_43A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C8")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_43A4")

    label("loc_43C8")

    Jump("loc_43F2")

    label("loc_43CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43EF")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_43CB")

    label("loc_43EF")

    Jump("loc_43F2")

    label("loc_43F2")

    Return()

    # Function_19_433E end

    def Function_20_43F3(): pass

    label("Function_20_43F3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440A")
    Call(0, 32)
    Call(0, 33)

    label("loc_440A")

    SetChrPos(0x101, 45720, 250, 79960, 180)
    SetChrPos(0x107, 45460, 250, 81610, 360)
    SetChrPos(0xF7, 44130, 250, 80220, 180)
    SetChrPos(0xF9, 44120, 250, 81630, 360)
    OP_6D(43920, 500, 81110, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x16)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x15)
    Sleep(300)
    OP_43(0x107, 0x1, 0x0, 0x16)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #103
        0x101,
        "#1007F#5PStill not here...\x02",
    )

    CloseMessageWindow()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3B)
    Sleep(1000)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 41000, 750, 81110, 90)
    OP_8E(0x24, 0xA7A8, 0x1F4, 0x13CD6, 0x7D0, 0x0)

    ChrTalk(    #104
        0x24,
        "#6PI'm so sorry!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_4549():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4549)
    Sleep(50)

    def lambda_455C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_455C)
    Sleep(50)

    def lambda_456F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_456F)
    Sleep(50)

    def lambda_4582():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4582)
    Sleep(300)

    ChrTalk(    #105
        0x24,
        "#6PI did try to stop her, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1016F#2PNo, it's okay.\x02\x03",

            "#1015FDid she say anything before she left, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x24,
        (
            "#6PAh, yes... She asked me a very\x01",
            "strange question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x24,
        (
            "#6PShe said, 'Do you know where the colorless\x01",
            "fish are?'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#2P#1004FBwuh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4824")

    ChrTalk(    #110
        0x108,
        (
            "#074FHmmm. Somewhat deep for a simple child's\x01",
            "question...\x02\x03",

            "It's a riddle of some kind, I think.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_470B():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_470B)

    def lambda_4719():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4719)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #111
        0x101,
        "#1020F#5PA RIDDLE?! What?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x108, 135, 400)

    ChrTalk(    #112
        0x108,
        (
            "#070F#6PShe's trying to get us to find her using\x01",
            "the riddles, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1005F#5PYou're KIDDING ME!\x02\x03",

            "Now she's running away from us ON PURPOSE?!\x01",
            "Ohhhhh, Renne, you little...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x108,
        "#071F#6PSeems like it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_49E0")

    label("loc_4824")


    ChrTalk(    #115
        0x105,
        (
            "#047FHmm. That doesn't seem like a...\x01",
            "typical question for a little girl.\x02\x03",

            "I think that's a riddle, actually.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_489D():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_489D)

    def lambda_48AB():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_48AB)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #116
        0x101,
        "#1020F#5PA RIDDLE?! What?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(    #117
        0x105,
        (
            "#542F#6PI think she's trying to make us chase her\x01",
            "by solving riddles she leaves behind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1005F#5PYou're KIDDING ME!\x02\x03",

            "Now she's running away from us ON PURPOSE?!\x01",
            "Ohhhhh, Renne, you little...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x105,
        "#045F#6PAh, well, it's just a guess, really...\x02",
    )

    CloseMessageWindow()

    label("loc_49E0")


    ChrTalk(    #120
        0x101,
        (
            "#1019F#5POkay, little catgirl, you want to play like\x01",
            "that, then let's do it.\x02\x03",

            "I am not about to lose to an eleven-year-old!\x01",
            "Come on!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4AB3")

    ChrTalk(    #121
        0x106,
        "#551F#6PThat's not really the point here, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_4AB3")


    ChrTalk(    #122
        0x103,
        "#025F#6PEr, Estelle, winning isn't the point.\x02",
    )

    CloseMessageWindow()

    label("loc_4AE6")

    OP_8C(0x107, 180, 400)

    ChrTalk(    #123
        0x107,
        (
            "#067F#2PUm, so...\x02\x03",

            "The riddle is: 'Do you know where the\x01",
            "colorless fish are?'\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #124
        0x101,
        (
            "#1006F#5PYeah, so we need to find us some\x01",
            "colorless fish first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x24,
        "#6PWell, good luck!\x02",
    )

    CloseMessageWindow()
    OP_43(0x24, 0x1, 0x0, 0x17)
    OP_A2(0x1631)
    OP_28(0x8C, 0x1, 0x10)
    OP_28(0x8C, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_20_43F3 end

    def Function_21_4BBE(): pass

    label("Function_21_4BBE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BE2")
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_21_4BBE")

    label("loc_4BE2")

    Return()

    # Function_21_4BBE end

    def Function_22_4BE3(): pass

    label("Function_22_4BE3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C07")
    OP_8C(0xFE, 360, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_22_4BE3")

    label("loc_4C07")

    Return()

    # Function_22_4BE3 end

    def Function_23_4C08(): pass

    label("Function_23_4C08")

    OP_8C(0x24, 270, 400)
    OP_8E(0x24, 0xA028, 0x2EE, 0x13CD6, 0x7D0, 0x0)
    SetChrFlags(0x24, 0x80)
    OP_72(0x4, 0x800)
    OP_6F(0x4, 59)
    OP_70(0x4, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_71(0x4, 0x800)
    Return()

    # Function_23_4C08 end

    def Function_24_4C49(): pass

    label("Function_24_4C49")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C69")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_4C69")

    Fade(1000)
    SetChrPos(0x107, 38700, 1250, 50460, 270)
    SetChrPos(0x101, 38820, 1250, 49280, 270)
    SetChrPos(0xF7, 38450, 1250, 48150, 315)
    SetChrPos(0xF9, 40210, 1250, 49430, 270)
    OP_6D(37890, 1250, 50340, 0)
    OP_67(0, 10000, -10000, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x11, 90, 0)
    SetChrSubChip(0x11, 0)
    OP_0D()

    ChrTalk(    #126
        0x101,
        (
            "#1006F#6PHmmm... 'Sweets that disappear if\x01",
            "you leave them alone.'\x02\x03",

            "I get it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DAE")

    ChrTalk(    #127
        0x108,
        (
            "#070FThose'll sure melt if you\x01",
            "leave 'em out in the sun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DFF")

    label("loc_4DAE")


    ChrTalk(    #128
        0x105,
        (
            "#542FYes, if you leave frozen treats alone,\x01",
            "they do 'disappear' by melting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DFF")


    ChrTalk(    #129
        0x11,
        "#6POh, hey, you're the girl from yesterday!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        (
            "#6PYour cute little friend just stopped by\x01",
            "for an ice pop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x11,
        "#6PYou two aren't together today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        (
            "#067FI thought so...\x02\x03",

            "#560FUm, miss? Did she tell you a\x01",
            "riddle by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x11,
        "#6PA riddle? I don't think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        (
            "#6PShe was very cheerful and told me, 'I'm\x01",
            "gonna go see my friends at the landing port!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1015F#6PThe 'friends' being us, I bet.\x02\x03",

            "#1007FPhew! Finally done with riddles,\x01",
            "I hope.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5017")

    ChrTalk(    #136
        0x106,
        "#051FHeh. For bein' a kid, she got us pretty good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_504E")

    label("loc_5017")


    ChrTalk(    #137
        0x103,
        (
            "#021FHeh. We've certainly been toyed\x01",
            "with enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504E")


    ChrTalk(    #138
        0x101,
        (
            "#1019F#6PSeriously. Making us worry and run around\x01",
            "like this?\x02\x03",

            "I am giving her the BIGGEST LECTURE when\x01",
            "we finally catch her.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #139
        0x107,
        (
            "#065F#4PUm, E-Estelle? Please don't get too mad\x01",
            "at her.\x02\x03",

            "#063FI think Renne is just kind of lonely...\x02\x03",

            "You've all been busy with work, and her\x01",
            "parents are missing, and...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51C8")

    ChrTalk(    #140
        0x108,
        "#070FTita does have something of a point.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5201")

    label("loc_51C8")


    ChrTalk(    #141
        0x105,
        (
            "#045FThat's true...\x01",
            "We have neglected her a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5201")


    ChrTalk(    #142
        0x101,
        (
            "#1007F#6PAww... Way to kill my righteous lecture\x01",
            "fury, Tita.\x02\x03",

            "#1006FEither way, we need to get to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1634)
    OP_28(0x8C, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_24_4C49 end

    def Function_25_5286(): pass

    label("Function_25_5286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5293")
    Return()

    label("loc_5293")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52B3")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_52B3")

    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x1)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x40)
    SetChrPos(0x25, 50460, 0, 85300, 180)
    SetChrPos(0x27, 50900, 100, 87500, 180)
    OP_A1(0x27, 0x11)
    OP_72(0x11, 0x4)
    OP_71(0x11, 0x40)
    OP_71(0x11, 0x20)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_48()
    SetChrBattleFlags(0x26, 0x20)
    OP_89(0x26, 50900, 350, 87200, 270)
    Fade(1000)
    SetChrPos(0x101, 47230, 250, 72940, 0)
    SetChrPos(0x107, 46120, 250, 72830, 0)
    SetChrPos(0xF7, 47390, 250, 71550, 0)
    SetChrPos(0xF9, 46230, 250, 71360, 0)
    OP_6D(47050, 250, 72580, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #143
        0x101,
        "#1004F#6POh!\x02",
    )

    CloseMessageWindow()

    def lambda_53CB():
        OP_6D(49820, 0, 82670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53CB)

    def lambda_53E3():
        OP_67(0, 8200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_53E3)

    def lambda_53FB():
        OP_6B(1960, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_53FB)

    def lambda_540B():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_540B)

    def lambda_541B():
        OP_6E(419, 3000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_541B)
    Sleep(1000)

    def lambda_5430():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_5430)
    Sleep(300)

    def lambda_5450():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_5450)
    OP_22(0xCF, 0x1, 0x64)
    OP_43(0x27, 0x2, 0x0, 0x1E)
    WaitChrThread(0x27, 0x1)
    OP_72(0x11, 0x20)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_24(0xCF, 0x50)
    WaitChrThread(0x107, 0x2)

    ChrTalk(    #144
        0x25,
        "#692F#6PHey!\x02",
    )

    CloseMessageWindow()

    def lambda_54AA():

        label("loc_54AA")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_54AA")

    QueueWorkItem2(0x25, 2, lambda_54AA)
    OP_43(0x101, 0x0, 0x0, 0x1A)
    Sleep(300)
    OP_43(0x107, 0x0, 0x0, 0x1B)
    OP_43(0xF7, 0x0, 0x0, 0x1C)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x1D)
    WaitChrThread(0xF9, 0x0)
    OP_44(0x25, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55AF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Maintenance Chief Gustav in Chapter 2\x01",          # 0
            "Set as not met Maintenance Chief Gustav in Chapter 2\x01",      # 1
            "No change\x01",                                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_55A3"),
        (1, "loc_55A9"),
        (SWITCH_DEFAULT, "loc_55AF"),
    )


    label("loc_55A3")

    OP_A2(0x1483)
    Jump("loc_55AF")

    label("loc_55A9")

    OP_A3(0x1483)
    Jump("loc_55AF")

    label("loc_55AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_56EC")

    ChrTalk(    #145
        0x107,
        "#064FGustav, Faye!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x26,
        "#6PWhat? Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x25,
        (
            "#693F#4PWell, well!\x01",
            "Little Tita! And Estelle, too!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_567D")

    ChrTalk(    #148
        0x101,
        "#1001F#1PHello, Gustav!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x106,
        (
            "#051FWhat's up? Kind of an odd place\x01",
            "to meet you guys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56E9")

    label("loc_567D")


    ChrTalk(    #150
        0x101,
        (
            "#1001F#1PHello, Gustav!\x02\x03",

            "#1006FWhat're you guys doing here?\x01",
            "This is kind of off the path for you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56E9")

    Jump("loc_5806")

    label("loc_56EC")


    ChrTalk(    #151
        0x107,
        "#064FGustav, Faye!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x26,
        "#6PWhat? Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x25,
        (
            "#693F#4PWhoa, Tita!\x02\x03",

            "#691FAnd...is that Estelle Bright?\x01",
            "Well, hot damn! Long time no see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1001F#1PYeah! It's good to see you're doing okay,\x01",
            "Gustav!\x02\x03",

            "#1006FWhat're you guys doing here?\x01",
            "This is kind of off the path for you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5806")


    ChrTalk(    #155
        0x25,
        "#691F#4PHeh. We're bringin' these things over.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x25, 315, 400)

    def lambda_5847():
        OP_6D(49350, 250, 84910, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5847)
    Sleep(300)

    def lambda_5864():
        OP_8E(0xFE, 0xBEF0, 0xFA, 0x151E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5864)
    Sleep(800)

    def lambda_5884():
        OP_8E(0xFE, 0xBEAA, 0xFA, 0x14C44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5884)
    Sleep(200)

    def lambda_58A4():
        OP_8E(0xFE, 0xBE78, 0xFA, 0x14604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_58A4)
    Sleep(200)

    def lambda_58C4():
        OP_8E(0xFE, 0xBBF8, 0xFA, 0x13F2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_58C4)
    Sleep(500)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 45, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 400)
    SetChrSubChip(0x26, 2)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 45, 400)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #156
        0x101,
        "#1004F#6PWhoa, what the heck are those?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x107,
        "#064F#3PWait, wait! That's gotta be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x25,
        (
            "#691F#2PYep. These are the samples of the XG-02.\x01",
            "It's the new engine we developed for the\x01",
            "Arseille.\x02\x03",

            "These're the real deal, too--just about\x01",
            "as much performance as what we've got\x01",
            "in her now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1008F#6PSo this is what it looks like? Neat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x107,
        (
            "#560F#3PReally?! Really-really?! Oh, wow!\x02\x03",

            "It's tiny for an engine, but it really\x01",
            "produces as much output as the sheet\x01",
            "Grandpa showed me?!\x02\x03",

            "The design is functional AND adorable, too!\x02\x03",

            "#067FIt's amazing!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #161
        0x101,
        "#1016F#6PUh, down, Tita, down.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5BC6")

    ChrTalk(    #162
        0x106,
        (
            "#551F#6POh, brother. It's like showing\x01",
            "a kitten some catnip or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C14")

    label("loc_5BC6")


    ChrTalk(    #163
        0x103,
        (
            "#021F#6PI think Tita's so high above the clouds\x01",
            "she can't even hear you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C14")

    OP_8C(0xF9, 45, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CC0")

    ChrTalk(    #164
        0x108,
        (
            "#070F#1PAnyway, if you're bringing them to the capital...\x02\x03",

            "...that means these are the treaty samples\x01",
            "for the Republic and Empire, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D4F")

    label("loc_5CC0")


    ChrTalk(    #165
        0x105,
        (
            "#040F#5PA pair of engines brought to the capital...\x02\x03",

            "These must be the engine samples that will\x01",
            "be presented at the treaty signing, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D4F")

    OP_8C(0x25, 225, 400)

    ChrTalk(    #166
        0x25,
        (
            "#691F#2PYeah! Guess word got around, huh?\x02\x03",

            "We just finished putting the Arseille\x01",
            "back together, so we had to cart these\x01",
            "over here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_8C(0xF7, 135, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60C8")

    ChrTalk(    #167
        0x105,
        (
            "#048F#5PI see... Thank you greatly for\x01",
            "your hard work, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x25,
        (
            "#692F#2PUh, okay...?\x02\x03",

            "Sorry, but you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x105,
        (
            "#047F#5POh, my apologies... I guess there's no\x01",
            "point in hiding it from you, sir.\x02\x03",

            "#040FI am Klaudia von Auslese.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x25,
        "#692F#2PKlaudia... W-Wait, as in PRINCESS Klaudia?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#1006F#6PYep! She's Queen Alicia's granddaughter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x105,
        (
            "#048F#5PThe Arseille is the property of the royal\x01",
            "family, so...\x02\x03",

            "Allow me to offer my gratitude for your\x01",
            "hard work in Grandmother's place.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #173
        0x25,
        (
            "#692F#2PW-Well, no, thank YOU, ma'am--\x01",
            "er, Your Highness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1016F#6PHaha! It's always kind of a shock to hear\x01",
            "about Kloe, isn't it?\x02\x03",

            "#1006FSo where're you guys lugging these\x01",
            "things off to, anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_611B")

    label("loc_60C8")


    ChrTalk(    #175
        0x101,
        (
            "#1006F#6POh, okay!\x02\x03",

            "So where're you guys lugging these\x01",
            "things off to, anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611B")

    TurnDirection(0x25, 0x101, 400)

    ChrTalk(    #176
        0x25,
        (
            "#691F#2PThere's a warehouse out near the water port\x01",
            "we'll be using.\x02\x03",

            "They'll be stored there until the ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#1011F#6PFair enough!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 135, 400)

    ChrTalk(    #178
        0x107,
        (
            "#560F#3PUm, Gustav, are you going back to\x01",
            "Zeiss after this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x25,
        (
            "#691F#2PYep! We make trails as soon as these are\x01",
            "locked up!\x02\x03",

            "Now, Tita, you behave yourself and stay safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x107,
        "#061F#3PI will! Stay safe too, Gustav!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6316")

    ChrTalk(    #181
        0x25,
        (
            "#691F#2PEstelle, Agate.\x01",
            "Take care of our little Tita, you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1006F#6PYou bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x106,
        "#051F#6PNo worries.\x02",
    )

    CloseMessageWindow()
    Jump("loc_636B")

    label("loc_6316")


    ChrTalk(    #184
        0x25,
        (
            "#691F#2PEstelle. Take care of our little\x01",
            "Tita, you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1006F#6PYou bet.\x02",
    )

    CloseMessageWindow()

    label("loc_636B")


    ChrTalk(    #186
        0x26,
        "#4PSee ya, bracers!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(50680, 250, 83000, 0)
    OP_67(0, 9530, -10000, 0)
    OP_6B(1780, 0)
    OP_6C(315000, 0)
    OP_6E(419, 0)
    OP_0D()
    OP_24(0xCF, 0x64)

    def lambda_63D1():

        label("loc_63D1")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_63D1")

    QueueWorkItem2(0x101, 1, lambda_63D1)

    def lambda_63E2():

        label("loc_63E2")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_63E2")

    QueueWorkItem2(0x107, 1, lambda_63E2)

    def lambda_63F3():

        label("loc_63F3")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_63F3")

    QueueWorkItem2(0xF7, 1, lambda_63F3)

    def lambda_6404():

        label("loc_6404")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_6404")

    QueueWorkItem2(0xF9, 1, lambda_6404)
    SetChrSubChip(0x26, 0)

    def lambda_641A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_641A)
    Sleep(300)

    def lambda_643A():
        OP_6D(50680, 250, 79000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_643A)

    def lambda_6452():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_6452)
    OP_43(0x27, 0x2, 0x0, 0x1F)
    WaitChrThread(0x27, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    OP_71(0x11, 0x4)
    OP_6D(48760, 250, 84990, 2000)
    Sleep(500)

    ChrTalk(    #187
        0x101,
        (
            "#1008F#6PWow... So that's the Arseille's engine?\x02\x03",

            "I still don't really get how it works,\x01",
            "but it looks cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        (
            "#560FYeah! Seeing that was amazing!\x02\x03",

            "#061FI hope I can make a machine that incredible\x01",
            "and cute someday!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_663C")
    OP_8C(0x106, 0, 400)

    ChrTalk(    #189
        0x106,
        (
            "#551F#1PShe's goin' for the orbal catnip again...\x02\x03",

            "#051FWell, ain't nothin' wrong with having a\x01",
            "goal, shortstuff. Keep at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x107,
        "#067FHaha! I will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_666F")

    label("loc_663C")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #191
        0x101,
        "#1017F#6PI bet you will someday, Tita!\x02",
    )

    CloseMessageWindow()

    label("loc_666F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(48450, 250, 85560, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 48450, 250, 85560, 180)
    SetChrPos(0x1, 48450, 250, 85560, 180)
    SetChrPos(0x2, 48450, 250, 85560, 180)
    SetChrPos(0x3, 48450, 250, 85560, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1635)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_25_5286 end

    def Function_26_6716(): pass

    label("Function_26_6716")

    OP_8E(0xFE, 0xBCE8, 0xFA, 0x13EB6, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_26_6716 end

    def Function_27_6732(): pass

    label("Function_27_6732")

    OP_8E(0xFE, 0xB914, 0xFA, 0x13C04, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_27_6732 end

    def Function_28_674E(): pass

    label("Function_28_674E")

    OP_8E(0xFE, 0xBDF6, 0xFA, 0x139A2, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_28_674E end

    def Function_29_676A(): pass

    label("Function_29_676A")

    OP_8E(0xFE, 0xBA22, 0xFA, 0x13678, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_29_676A end

    def Function_30_6786(): pass

    label("Function_30_6786")

    OP_24(0xCF, 0x41)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x4B)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x55)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_24(0xCF, 0x5F)
    Sleep(100)
    OP_24(0xCF, 0x64)
    Return()

    # Function_30_6786 end

    def Function_31_67CA(): pass

    label("Function_31_67CA")

    Sleep(6500)
    OP_24(0xCF, 0x5F)
    Sleep(500)
    OP_24(0xCF, 0x5A)
    Sleep(500)
    OP_24(0xCF, 0x55)
    Sleep(500)
    OP_24(0xCF, 0x50)
    Sleep(500)
    OP_24(0xCF, 0x4B)
    Sleep(500)
    OP_24(0xCF, 0x46)
    Sleep(500)
    OP_24(0xCF, 0x41)
    Sleep(500)
    OP_23(0xCF)
    Return()

    # Function_31_67CA end

    def Function_32_6812(): pass

    label("Function_32_6812")

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
        (0, "loc_688E"),
        (1, "loc_6894"),
        (SWITCH_DEFAULT, "loc_689A"),
    )


    label("loc_688E")

    OP_A2(0x1200)
    Jump("loc_689A")

    label("loc_6894")

    OP_A2(0x1201)
    Jump("loc_689A")

    label("loc_689A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_68A8")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_68AC")

    label("loc_68A8")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_68AC")

    Return()

    # Function_32_6812 end

    def Function_33_68AD(): pass

    label("Function_33_68AD")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    OP_6D(22110, 0, 124540, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_68FD")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_6917")

    label("loc_68FD")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_6917")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_33_68AD end

    def Function_34_6937(): pass

    label("Function_34_6937")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #192
        (
            "\x07\x05[Second Orbally-Powered Clock]\x01",
            "Made in year 1163 of the Septian Calendar,\x01",
            "by Zeissian manufacturers.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_6937 end

    def Function_35_69C6(): pass

    label("Function_35_69C6")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #193
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_69C6 end

    def Function_36_6A15(): pass

    label("Function_36_6A15")

    SetPlaceName(0xBA)
    Return()

    # Function_36_6A15 end

    def Function_37_6A19(): pass

    label("Function_37_6A19")

    SetPlaceName(0xB1)
    Return()

    # Function_37_6A19 end

    def Function_38_6A1D(): pass

    label("Function_38_6A1D")

    SetPlaceName(0xBB)
    Return()

    # Function_38_6A1D end

    def Function_39_6A21(): pass

    label("Function_39_6A21")

    SetPlaceName(0xBC)
    Return()

    # Function_39_6A21 end

    def Function_40_6A25(): pass

    label("Function_40_6A25")

    SetPlaceName(0xBD)
    Return()

    # Function_40_6A25 end

    def Function_41_6A29(): pass

    label("Function_41_6A29")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_41_6A29 end

    SaveToFile()

Try(main)
