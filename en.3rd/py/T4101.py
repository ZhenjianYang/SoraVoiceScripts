from ED63RDScenarioHelper import *

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
            '',
            '',
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
        'Sorbet',                               # 9
        'Man in Black',                         # 10
        'Man in Black',                         # 11
        'Man in Black',                         # 12
        'Man in Black',                         # 13
        'Man in Black',                         # 14
        'Man in Black',                         # 15
        'Nial',                                 # 16
        'Dorothy',                              # 17
        'Private Tact',                         # 18
        'Private Bergan',                       # 19
        'Robyn',                                # 20
        'Miele',                                # 21
        'Godfrey',                              # 22
        'Phoebe',                               # 23
        'Nana',                                 # 24
        'Anton',                                # 25
        'Ricky',                                # 26
        'Clare',                                # 27
        'Nemo',                                 # 28
        'Jimmy',                                # 29
        'Laone',                                # 30
        'Marsha',                               # 31
        'Builna',                               # 32
        'Royal Army Soldier',                   # 33
        'Royal Army Soldier',                   # 34
        'Royal Army Soldier',                   # 35
        'Tourist',                              # 36
        'Tourist',                              # 37
        'Ian',                                  # 38
        'Private Brans',                        # 39
        'Panna',                                # 40
        'Aldan',                                # 41
        'Pigeon',                               # 42
        'Pigeon',                               # 43
        'Pigeon',                               # 44
        'Grancel - North Block',                # 45
        'Grancel - South Block',                # 46
        'Grancel - Landing Port',               # 47
        'Major Vander',                         # 48
        'Smoke Target Character',               # 49
        'Target Camera',                        # 50
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
        'ED6_DT07/CH01050 ._CH',             # 00
        'ED6_DT27/CH03460 ._CH',             # 01
        'ED6_DT07/CH02060 ._CH',             # 02
        'ED6_DT07/CH02720 ._CH',             # 03
        'ED6_DT27/CH04230 ._CH',             # 04
        'ED6_DT27/CH04232 ._CH',             # 05
        'ED6_DT27/CH04234 ._CH',             # 06
        'ED6_DT27/CH04464 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
        'ED6_DT07/CH01540 ._CH',             # 09
        'ED6_DT07/CH01470 ._CH',             # 0A
        'ED6_DT07/CH01150 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH02480 ._CH',             # 0E
        'ED6_DT07/CH02490 ._CH',             # 0F
        'ED6_DT07/CH01143 ._CH',             # 10
        'ED6_DT07/CH01100 ._CH',             # 11
        'ED6_DT07/CH01210 ._CH',             # 12
        'ED6_DT07/CH01110 ._CH',             # 13
        'ED6_DT07/CH01680 ._CH',             # 14
        'ED6_DT07/CH01030 ._CH',             # 15
        'ED6_DT06/CH20086 ._CH',             # 16
        'ED6_DT07/CH01140 ._CH',             # 17
        'ED6_DT07/CH01350 ._CH',             # 18
        'ED6_DT07/CH01070 ._CH',             # 19
        'ED6_DT07/CH02900 ._CH',             # 1A
        'ED6_DT26/CH20783 ._CH',             # 1B
        'ED6_DT07/CH01730 ._CH',             # 1C
        'ED6_DT07/CH01731 ._CH',             # 1D
        'ED6_DT07/CH01410 ._CH',             # 1E
        'ED6_DT06/CH20112 ._CH',             # 1F
        'ED6_DT26/CH20770 ._CH',             # 20
        'ED6_DT27/CH03570 ._CH',             # 21
        'ED6_DT27/CH03573 ._CH',             # 22
        'ED6_DT07/CH01480 ._CH',             # 23
        'ED6_DT26/CH20680 ._CH',             # 24
        'ED6_DT26/CH20681 ._CH',             # 25
        'ED6_DT26/CH20688 ._CH',             # 26
        'ED6_DT27/CH03233 ._CH',             # 27
        'ED6_DT26/CH20692 ._CH',             # 28
        'ED6_DT26/CH20686 ._CH',             # 29
        'ED6_DT26/CH20689 ._CH',             # 2A
        'ED6_DT26/CH20690 ._CH',             # 2B
        'ED6_DT26/CH20618 ._CH',             # 2C
        'ED6_DT27/CH04460 ._CH',             # 2D
        'ED6_DT27/CH04463 ._CH',             # 2E
        'ED6_DT27/CH03231 ._CH',             # 2F
        'ED6_DT26/CH20684 ._CH',             # 30
        'ED6_DT27/CH03234 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT07/CH01050P._CP',             # 00
        'ED6_DT27/CH03460P._CP',             # 01
        'ED6_DT07/CH02060P._CP',             # 02
        'ED6_DT07/CH02720P._CP',             # 03
        'ED6_DT27/CH04230P._CP',             # 04
        'ED6_DT27/CH04232P._CP',             # 05
        'ED6_DT27/CH04234P._CP',             # 06
        'ED6_DT27/CH04464P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
        'ED6_DT07/CH01540P._CP',             # 09
        'ED6_DT07/CH01470P._CP',             # 0A
        'ED6_DT07/CH01150P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH02480P._CP',             # 0E
        'ED6_DT07/CH02490P._CP',             # 0F
        'ED6_DT07/CH01143P._CP',             # 10
        'ED6_DT07/CH01100P._CP',             # 11
        'ED6_DT07/CH01210P._CP',             # 12
        'ED6_DT07/CH01110P._CP',             # 13
        'ED6_DT07/CH01680P._CP',             # 14
        'ED6_DT07/CH01030P._CP',             # 15
        'ED6_DT06/CH20086P._CP',             # 16
        'ED6_DT07/CH01140P._CP',             # 17
        'ED6_DT07/CH01350P._CP',             # 18
        'ED6_DT07/CH01070P._CP',             # 19
        'ED6_DT07/CH02900P._CP',             # 1A
        'ED6_DT26/CH20783P._CP',             # 1B
        'ED6_DT07/CH01730P._CP',             # 1C
        'ED6_DT07/CH01731P._CP',             # 1D
        'ED6_DT07/CH01410P._CP',             # 1E
        'ED6_DT06/CH20112P._CP',             # 1F
        'ED6_DT26/CH20770P._CP',             # 20
        'ED6_DT27/CH03570P._CP',             # 21
        'ED6_DT27/CH03573P._CP',             # 22
        'ED6_DT07/CH01480P._CP',             # 23
        'ED6_DT26/CH20680P._CP',             # 24
        'ED6_DT26/CH20681P._CP',             # 25
        'ED6_DT26/CH20688P._CP',             # 26
        'ED6_DT27/CH03233P._CP',             # 27
        'ED6_DT26/CH20692P._CP',             # 28
        'ED6_DT26/CH20686P._CP',             # 29
        'ED6_DT26/CH20689P._CP',             # 2A
        'ED6_DT26/CH20690P._CP',             # 2B
        'ED6_DT26/CH20618P._CP',             # 2C
        'ED6_DT27/CH04460P._CP',             # 2D
        'ED6_DT27/CH04463P._CP',             # 2E
        'ED6_DT27/CH03231P._CP',             # 2F
        'ED6_DT26/CH20684P._CP',             # 30
        'ED6_DT27/CH03234P._CP',             # 31
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 1250,
        Y                   = 49800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        X                   = 40490,
        Z                   = 1250,
        Y                   = 50080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 74970,
        Z                   = 0,
        Y                   = 71250,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 100180,
        Z                   = 250,
        Y                   = 33080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 46290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 44530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 46260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 47860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70490,
        Z                   = 250,
        Y                   = 6990,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 71500,
        Z                   = 750,
        Y                   = 7870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = 250,
        Y                   = 49340,
        Direction           = 227,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49630,
        Z                   = 0,
        Y                   = 61870,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 50410,
        Z                   = 0,
        Y                   = 81110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81160,
        Z                   = 0,
        Y                   = -2940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 69020,
        Z                   = 250,
        Y                   = 4960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63010,
        Z                   = 0,
        Y                   = 62930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 93700,
        Z                   = 0,
        Y                   = 32900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53830,
        Z                   = 250,
        Y                   = 24100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54040,
        Z                   = 250,
        Y                   = 8750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 76500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 77950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44290,
        Z                   = 250,
        Y                   = 75360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 100960,
        Z                   = 250,
        Y                   = 34810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 59400,
        Z                   = 1250,
        Y                   = 24170,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 70180,
        Z                   = 250,
        Y                   = 4580,
        Direction           = 47,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70180,
        Z                   = 250,
        Y                   = 4580,
        Direction           = 47,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70180,
        Z                   = 250,
        Y                   = 4580,
        Direction           = 47,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1EE,
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


    DeclEvent(
        X                   = 109720,
        Y                   = 1000,
        Z                   = 32980,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 68,
    )

    DeclEvent(
        X                   = 76740,
        Y                   = 1000,
        Z                   = 23010,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 69950,
        Y                   = 1000,
        Z                   = 14290,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 63260,
        Y                   = 1000,
        Z                   = 22960,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 69910,
        Y                   = 1000,
        Z                   = 31710,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 42920,
        Y                   = 0,
        Z                   = 81110,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 70,
    )

    DeclEvent(
        X                   = 70940,
        Y                   = 0,
        Z                   = -9490,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 75010,
        Y                   = 0,
        Z                   = 71300,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 72,
    )

    DeclEvent(
        X                   = 41440,
        Y                   = 0,
        Z                   = -5500,
        Range               = 39540,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xDAC,
        Unknown_18          = 0x0,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 37140,
        Y                   = 0,
        Z                   = 56520,
        Range               = 35140,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x1188C,
        Unknown_18          = 0x0,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 72300,
        Y                   = 3500,
        Z                   = 50780,
        Range               = 67700,
        Unknown_10          = 0x0,
        Unknown_14          = 0xBF18,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )

    DeclEvent(
        X                   = 72300,
        Y                   = 3500,
        Z                   = 39180,
        Range               = 67700,
        Unknown_10          = 0x0,
        Unknown_14          = 0x9F4C,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
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
        TalkFunctionIndex   = 64,
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
        TalkFunctionIndex   = 67,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_942",          # 00, 0
        "Function_1_BBE",          # 01, 1
        "Function_2_CED",          # 02, 2
        "Function_3_E6A",          # 03, 3
        "Function_4_E8E",          # 04, 4
        "Function_5_F7B",          # 05, 5
        "Function_6_1028",         # 06, 6
        "Function_7_1161",         # 07, 7
        "Function_8_1206",         # 08, 8
        "Function_9_130B",         # 09, 9
        "Function_10_1410",        # 0A, 10
        "Function_11_1434",        # 0B, 11
        "Function_12_1637",        # 0C, 12
        "Function_13_1672",        # 0D, 13
        "Function_14_18AF",        # 0E, 14
        "Function_15_1C27",        # 0F, 15
        "Function_16_1FE3",        # 10, 16
        "Function_17_21EA",        # 11, 17
        "Function_18_23E7",        # 12, 18
        "Function_19_2661",        # 13, 19
        "Function_20_2A15",        # 14, 20
        "Function_21_2C85",        # 15, 21
        "Function_22_2DA7",        # 16, 22
        "Function_23_30DB",        # 17, 23
        "Function_24_33AE",        # 18, 24
        "Function_25_35D2",        # 19, 25
        "Function_26_387C",        # 1A, 26
        "Function_27_3931",        # 1B, 27
        "Function_28_3995",        # 1C, 28
        "Function_29_3ABC",        # 1D, 29
        "Function_30_3C1B",        # 1E, 30
        "Function_31_4687",        # 1F, 31
        "Function_32_471C",        # 20, 32
        "Function_33_4A93",        # 21, 33
        "Function_34_4BD3",        # 22, 34
        "Function_35_4CA3",        # 23, 35
        "Function_36_4D2E",        # 24, 36
        "Function_37_4DB4",        # 25, 37
        "Function_38_4DFF",        # 26, 38
        "Function_39_4E40",        # 27, 39
        "Function_40_631B",        # 28, 40
        "Function_41_63BF",        # 29, 41
        "Function_42_6450",        # 2A, 42
        "Function_43_647D",        # 2B, 43
        "Function_44_7943",        # 2C, 44
        "Function_45_7981",        # 2D, 45
        "Function_46_79C2",        # 2E, 46
        "Function_47_7A03",        # 2F, 47
        "Function_48_7A50",        # 30, 48
        "Function_49_7A9D",        # 31, 49
        "Function_50_7B05",        # 32, 50
        "Function_51_7B6D",        # 33, 51
        "Function_52_7D2A",        # 34, 52
        "Function_53_7EE7",        # 35, 53
        "Function_54_89EF",        # 36, 54
        "Function_55_8B20",        # 37, 55
        "Function_56_8DD1",        # 38, 56
        "Function_57_9157",        # 39, 57
        "Function_58_9295",        # 3A, 58
        "Function_59_92E9",        # 3B, 59
        "Function_60_933D",        # 3C, 60
        "Function_61_9391",        # 3D, 61
        "Function_62_93E5",        # 3E, 62
        "Function_63_9529",        # 3F, 63
        "Function_64_ADFA",        # 40, 64
        "Function_65_AE8C",        # 41, 65
        "Function_66_AED6",        # 42, 66
        "Function_67_AF2C",        # 43, 67
        "Function_68_AF84",        # 44, 68
        "Function_69_AF88",        # 45, 69
        "Function_70_AF8C",        # 46, 70
        "Function_71_AF90",        # 47, 71
        "Function_72_AF94",        # 48, 72
        "Function_73_AF98",        # 49, 73
    )


    def Function_0_942(): pass

    label("Function_0_942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B44")
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrChipByIndex(0x20, 26)
    SetChrSubChip(0x20, 0)
    SetChrChipByIndex(0x21, 27)
    SetChrSubChip(0x21, 0)
    SetChrFlags(0x20, 0x10)
    SetChrPos(0x20, 70490, 250, 6990, 180)
    SetChrPos(0x1D, 48230, 250, 52350, 270)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    OP_43(0x31, 0x0, 0x0, 0xB)
    OP_43(0x32, 0x0, 0x0, 0xB)
    OP_43(0x33, 0x0, 0x0, 0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9EE")
    Jump("loc_B44")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A39")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32100, 0, 64760, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32100, 0, 62820, 0)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x3, 0x0, 0xC)
    Jump("loc_B44")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_AFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_END)), "loc_AA2")
    SetChrPos(0x17, 73240, 250, 43820, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x18, 72140, 250, 43820, 270)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)

    def lambda_A83():

        label("loc_A83")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_A83")

    QueueWorkItem2(0x17, 2, lambda_A83)
    OP_43(0x17, 0x3, 0x0, 0x36)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    Jump("loc_ACC")

    label("loc_AA2")

    SetChrPos(0x17, 73960, 260, 45140, 0)
    SetChrChipByIndex(0x17, 38)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x40)

    label("loc_ACC")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32320, 0, 63960, 270)
    OP_43(0x11, 0x0, 0x0, 0x2)
    SetChrPos(0x30, 59400, 1250, 24170, 270)
    Jump("loc_B44")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_B44")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32320, 0, 63960, 270)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_62(0x20, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    label("loc_B44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_B6F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 32)
    Jump("loc_B8B")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_B8B")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 39)

    label("loc_B8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_BAA")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 63)

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_BBD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_BBD")

    Return()

    # Function_0_942 end

    def Function_1_BBE(): pass

    label("Function_1_BBE")

    OP_16(0x2, 0xFA0, 0xFFFF4C50, 0xFFFEA070, 0x23005C)
    OP_B1("t4101_n")
    OP_82(0x80, 0x0)
    OP_71(0x411, 0x0)
    ExitThread()
    OP_10(0xB, 0x0)
    OP_10(0xC, 0x1)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_72(0x1005, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_64(0x1, 0x1)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_B2(0x0, 0x8, 0x80)
    OP_B2(0x0, 0x9, 0x80)
    OP_B2(0x0, 0xA, 0x80)
    OP_B2(0x0, 0xB, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    OP_65(0x1, 0x1)
    OP_1B(0xC, 0x0, 0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C49")
    Jump("loc_CEC")

    label("loc_C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_C84")
    OP_B2(0x1, 0x9, 0x80)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_1C(0x0, 0x0, 0x3C)
    OP_1C(0x1, 0x0, 0x3D)
    OP_1C(0x2, 0x0, 0x3A)
    OP_1C(0x3, 0x0, 0x3B)
    Jump("loc_CEC")

    label("loc_C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_CCE")
    OP_B2(0x1, 0x8, 0x80)
    OP_B2(0x1, 0x9, 0x80)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_1C(0x0, 0x0, 0x3C)
    OP_1C(0x1, 0x0, 0x3D)
    OP_1C(0x2, 0x0, 0x3A)
    OP_1C(0x3, 0x0, 0x3B)
    OP_B2(0x1, 0xA, 0x80)
    OP_B2(0x1, 0xB, 0x80)
    Jump("loc_CEC")

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_CEC")
    OP_B2(0x1, 0x9, 0x80)
    OP_62(0x20, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    label("loc_CEC")

    Return()

    # Function_1_BBE end

    def Function_2_CED(): pass

    label("Function_2_CED")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D12")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E54")

    label("loc_D12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E54")

    label("loc_D2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E54")

    label("loc_D44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E54")

    label("loc_D5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D76")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E54")

    label("loc_D76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E54")

    label("loc_D8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E54")

    label("loc_DA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E54")

    label("loc_DC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E54")

    label("loc_DDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E54")

    label("loc_DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E54")

    label("loc_E0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E25")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E54")

    label("loc_E25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E54")

    label("loc_E3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E54")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E69")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E54")

    label("loc_E69")

    Return()

    # Function_2_CED end

    def Function_3_E6A(): pass

    label("Function_3_E6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E8D")
    OP_8D(0xFE, 102900, 37500, 97550, 28500, 2000)
    Jump("Function_3_E6A")

    label("loc_E8D")

    Return()

    # Function_3_E6A end

    def Function_4_E8E(): pass

    label("Function_4_E8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F7A")
    OP_8E(0xFE, 0xCCF6, 0x0, 0xFFFFF484, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0x8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0xF32A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCFE4, 0x0, 0x100A4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15AC2, 0x0, 0xFCBC, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16314, 0x0, 0xFB86, 0x9C4, 0x0)
    OP_8E(0xFE, 0x164E0, 0x0, 0x826E, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(4000)
    OP_8E(0xFE, 0x164E0, 0x0, 0x7E86, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x16152, 0x0, 0x4CE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15B12, 0x0, 0xFFFFF8BC, 0x9C4, 0x0)
    Jump("Function_4_E8E")

    label("loc_F7A")

    Return()

    # Function_4_E8E end

    def Function_5_F7B(): pass

    label("Function_5_F7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1027")
    OP_8E(0xFE, 0xCE9A, 0x0, 0xF5D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0xF258, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0x816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCEEA, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15590, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0x6B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0xEF56, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15572, 0x28, 0xF5D2, 0x7D0, 0x0)
    Jump("Function_5_F7B")

    label("loc_1027")

    Return()

    # Function_5_F7B end

    def Function_6_1028(): pass

    label("Function_6_1028")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1160")
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
    Jump("Function_6_1028")

    label("loc_1160")

    Return()

    # Function_6_1028 end

    def Function_7_1161(): pass

    label("Function_7_1161")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1205")
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
    Jump("Function_7_1161")

    label("loc_1205")

    Return()

    # Function_7_1161 end

    def Function_8_1206(): pass

    label("Function_8_1206")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130A")
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
    Jump("Function_8_1206")

    label("loc_130A")

    Return()

    # Function_8_1206 end

    def Function_9_130B(): pass

    label("Function_9_130B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_140F")
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
    Jump("Function_9_130B")

    label("loc_140F")

    Return()

    # Function_9_130B end

    def Function_10_1410(): pass

    label("Function_10_1410")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1433")
    OP_8D(0xFE, 102900, 37500, 97550, 28500, 2000)
    Jump("Function_10_1410")

    label("loc_1433")

    Return()

    # Function_10_1410 end

    def Function_11_1434(): pass

    label("Function_11_1434")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 67800, 6820, 72340, 2850, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1636")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FF")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14EF")

    def lambda_14D3():

        label("loc_14D3")

        OP_97(0xFE, 0x11224, 0x11E4, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_14D3")

    QueueWorkItem2(0xFE, 1, lambda_14D3)
    Jump("loc_150E")

    label("loc_14EF")


    def lambda_14F5():

        label("loc_14F5")

        OP_97(0xFE, 0x11224, 0x11E4, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_14F5")

    QueueWorkItem2(0xFE, 1, lambda_14F5)

    label("loc_150E")

    SetChrChipByIndex(0xFE, 28)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_151D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1555")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154D")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_1555")

    label("loc_154D")

    Sleep(15)
    Jump("loc_151D")

    label("loc_1555")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 70140, 250, 4470, 143)

    label("loc_1574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15F4")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 29)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 67800, 6820, 72340, 2850, 0)
    Jump("loc_15FC")

    label("loc_15F4")

    Sleep(500)
    Jump("loc_1574")

    label("loc_15FC")

    Jump("loc_1633")

    label("loc_15FF")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1633")

    def lambda_161B():
        OP_8D(0xFE, 67800, 6820, 72340, 2850, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_161B)

    label("loc_1633")

    Jump("loc_1468")

    label("loc_1636")

    Return()

    # Function_11_1434 end

    def Function_12_1637(): pass

    label("Function_12_1637")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1671")
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jump("Function_12_1637")

    label("loc_1671")

    Return()

    # Function_12_1637 end

    def Function_13_1672(): pass

    label("Function_13_1672")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_167F")
    Jump("loc_18AB")

    label("loc_167F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16E9")

    ChrTalk(    #0
        0xFE,
        "They're sure taking their time getting here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "I hope something didn't happen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_173F")

    label("loc_16E9")


    ChrTalk(    #2
        0xFE,
        "They're sure taking their time getting here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "What are they even doing?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_173F")

    Jump("loc_18AB")

    label("loc_1742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_18AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_17F2")

    ChrTalk(    #4
        0xFE,
        "I often meet up with people here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "This spot's so easy to find that there's not\x01",
            "much chance the other person'll get lost\x01",
            "and not be able to find you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AB")

    label("loc_17F2")


    ChrTalk(    #6
        0xFE,
        "I'm waiting for someone here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "It's a pretty convenient spot when you need to\x01",
            "get together with someone. Just say 'in front\x01",
            "of the history museum,' and anyone can find you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_18AB")

    TalkEnd(0xFE)
    Return()

    # Function_13_1672 end

    def Function_14_18AF(): pass

    label("Function_14_18AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_18BC")
    Jump("loc_1C23")

    label("loc_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_195D")

    ChrTalk(    #8
        0xFE,
        (
            "This is the Erebonian embassy. Only authorized\x01",
            "personnel may pass beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "If that does not describe you, please step away.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A32")

    label("loc_195D")


    ChrTalk(    #10
        0xFE,
        (
            "...What's up with all the men in black suits\x01",
            "I keep seeing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "*cough* Excuse me. Please forget I said anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "This is the Erebonian embassy. Only authorized\x01",
            "personnel may pass beyond this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1A32")

    Jump("loc_1C23")

    label("loc_1A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1AF6")

    ChrTalk(    #13
        0xFE,
        (
            "This is the Erebonian embassy. Only authorized\x01",
            "personnel may pass beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "If you were to cause any trouble inside, it may\x01",
            "cause an international incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B89")

    label("loc_1AF6")


    ChrTalk(    #15
        0xFE,
        (
            "This is the Erebonian embassy. Only authorized\x01",
            "personnel may pass beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "If that does not describe you, please step away.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1B89")

    Jump("loc_1C23")

    label("loc_1B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1C23")

    ChrTalk(    #17
        0xFE,
        (
            "This is the Erebonian embassy. Only authorized\x01",
            "personnel may pass beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "If that does not describe you, please step away.\x02",
    )

    CloseMessageWindow()

    label("loc_1C23")

    TalkEnd(0xFE)
    Return()

    # Function_14_18AF end

    def Function_15_1C27(): pass

    label("Function_15_1C27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1C34")
    Jump("loc_1FDF")

    label("loc_1C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 7)), scpexpr(EXPR_END)), "loc_1D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(    #19
        0xFE,
        "He always was one with a strong sense of justice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I don't think he regretted the way he died.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D29")

    label("loc_1CB4")


    ChrTalk(    #21
        0xFE,
        "My older brother was a bracer, you see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He lost his life in the war while trying to\x01",
            "evacuate civilians.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1D29")

    Jump("loc_1DC0")

    label("loc_1D2C")

    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0xFE,
        "...You there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Are you a bracer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        "#1643FWhat? I am, but why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "O-Oh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Nah, no particular reason.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F57)

    label("loc_1DC0")

    Jump("loc_1FDF")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E65")

    ChrTalk(    #28
        0xFE,
        (
            "Sorry, but unless you've got proof you're allowed\x01",
            "inside, you're not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "There's been a lot of strange people around lately, \x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE0")

    label("loc_1E65")


    ChrTalk(    #30
        0xFE,
        "This is the Calvardian embassy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Sorry, but I'm gonna have to ask you to step away.\x01",
            "Authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1EE0")

    Jump("loc_1FDF")

    label("loc_1EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F64")

    ChrTalk(    #32
        0xFE,
        "This is the Calvardian embassy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Sorry, but unless you've got proof you're allowed\x01",
            "inside, you're not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDF")

    label("loc_1F64")


    ChrTalk(    #34
        0xFE,
        "This is the Calvardian embassy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Sorry, but I'm gonna have to ask you to step away.\x01",
            "Authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1FDF")

    TalkEnd(0xFE)
    Return()

    # Function_15_1C27 end

    def Function_16_1FE3(): pass

    label("Function_16_1FE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1FF0")
    Jump("loc_21E6")

    label("loc_1FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2067")

    ChrTalk(    #36
        0xFE,
        "Mommy's super spacey sometimes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I hope she didn't forget about me\x01",
            "and go home on her own...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20FE")

    label("loc_2067")


    ChrTalk(    #38
        0xFE,
        "Mommy sure is taking her time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I hope she didn't seriously forget about me\x01",
            "and go home on her own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "She better not have.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_20FE")

    Jump("loc_21E6")

    label("loc_2101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_21E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_218C")

    ChrTalk(    #42
        0xFE,
        (
            "I wonder if Mommy's shopping in the department\x01",
            "store again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "*sigh* I guess I'll just have to wait for her here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E6")

    label("loc_218C")


    ChrTalk(    #44
        0xFE,
        "Me and Mommy got separated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "But it's okay! I can find my way\x01",
            "home on my own.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_21E6")

    TalkEnd(0xFE)
    Return()

    # Function_16_1FE3 end

    def Function_17_21EA(): pass

    label("Function_17_21EA")

    TalkBegin(0xFE)
    SetMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_21FC")
    Jump("loc_23DE")

    label("loc_21FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_22D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2245")

    ChrTalk(    #46
        0xFE,
        "#3SLook at me! I'm right here!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_22D5")

    label("loc_2245")


    ChrTalk(    #47
        0xFE,
        (
            "Huh? What's wrong with me? My chest feels\x01",
            "kinda painful all of a sudden...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #48
        0xFE,
        "#3SLook at me! I'm right here!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_22D5")

    Jump("loc_23DE")

    label("loc_22D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_23DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_230F")

    ChrTalk(    #49
        0xFE,
        "Behold, the beauty of the world!\x02",
    )

    CloseMessageWindow()
    Jump("loc_23DE")

    label("loc_230F")


    ChrTalk(    #50
        0xFE,
        (
            "The sun's rays are warm, the clouds are white\x01",
            "and fluffy, the breeze is gentle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Look, Ricky! It's like the whole world is blessing\x01",
            "us!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #52
        0xFE,
        "#4SHurray for school life!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_23DE")

    ClearMapFlags(0x20)
    TalkEnd(0xFE)
    Return()

    # Function_17_21EA end

    def Function_18_23E7(): pass

    label("Function_18_23E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_23F4")
    Jump("loc_265D")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2488")

    ChrTalk(    #53
        0xFE,
        (
            "Oh, well. I know Anton too well to think he'll stay\x01",
            "like this for long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "He'll get back to being a gloomy worrywart soon\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265D")

    label("loc_2488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_265D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_254D")

    ChrTalk(    #55
        0xFE,
        (
            "What's up with you today, Anton? I don't think\x01",
            "I've ever seen your face that lit up before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "No one around you's gonna need a light bulb\x01",
            "ever again if you stay like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265D")

    label("loc_254D")


    ChrTalk(    #57
        0xFE,
        (
            "By some miracle of the universe, Anton actually\x01",
            "ended up getting accepted into Jenis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "...By the same miracle, I did, too. I only took\x01",
            "the exam because I had nothing better to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I can only assume Aidios is playing a prank on\x01",
            "the two of us or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_265D")

    TalkEnd(0xFE)
    Return()

    # Function_18_23E7 end

    def Function_19_2661(): pass

    label("Function_19_2661")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_266E")
    Jump("loc_2A11")

    label("loc_266E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2790")

    ChrTalk(    #60
        0xFE,
        (
            "I only found out when I bought the latest issue\x01",
            "of the Liberl News earlier. It's right on the\x01",
            "front page.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "The timing of this seriously couldn't have\x01",
            "been worse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I've got the champagne and cake for my\x01",
            "celebration, but now I don't even feel like\x01",
            "having one!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_2790")


    ChrTalk(    #63
        0xFE,
        "Y-You there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Did you know that the famous Saul Holden, who\x01",
            "contributed massively to the establishment of\x01",
            "the Liberl Orbalship Corporation, passed away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "I can't believe it... I was a huge fan of his, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x151,
        "#1654F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_287F")

    Jump("loc_2A11")

    label("loc_2882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2911")

    ChrTalk(    #67
        0xFE,
        (
            "First, I need to buy what I need here at the\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I'm going to need champagne and a cake\x01",
            "for starters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A11")

    label("loc_2911")


    ChrTalk(    #69
        0xFE,
        (
            "This year is the twentieth year the Cecilia \x01",
            "airliner has been in operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "There's not going to be a major celebration\x01",
            "taking place, but I'm planning to hold one of\x01",
            "my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "First, I need to buy what I need here at the\x01",
            "department store!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2A11")

    TalkEnd(0xFE)
    Return()

    # Function_19_2661 end

    def Function_20_2A15(): pass

    label("Function_20_2A15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2A22")
    Jump("loc_2C81")

    label("loc_2A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2AC3")

    ChrTalk(    #72
        0xFE,
        (
            "The girl running that ice cream stall is still a\x01",
            "student from what I hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I guess it's just a part-time job she's doing on\x01",
            "the side?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B3B")

    label("loc_2AC3")


    ChrTalk(    #74
        0xFE,
        (
            "I think that ice cream stall was indeed\x01",
            "only set up recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "The girl running it is still a student, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2B3B")

    Jump("loc_2C81")

    label("loc_2B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2C02")

    ChrTalk(    #76
        0xFE,
        (
            "I don't remember there being an ice cream\x01",
            "stall up there before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "It's possible I just never noticed, but I feel\x01",
            "like I would have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "Maybe it's new or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C81")

    label("loc_2C02")

    OP_8C(0xFE, 270, 0)

    ChrTalk(    #79
        0xFE,
        (
            "Huh? I don't remember there being an ice cream\x01",
            "stall up there before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "Maybe I just never noticed? Hmm...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2C81")

    TalkEnd(0xFE)
    Return()

    # Function_20_2A15 end

    def Function_21_2C85(): pass

    label("Function_21_2C85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2CEF")

    NpcTalk(    #81
        0xFE,
        "Freckled Girl",
        (
            "#1660F*sigh* I'm so booored...\x02\x03",

            "Maybe I should get some ice cream!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA3")

    label("loc_2CEF")


    NpcTalk(    #82
        0xFE,
        "Freckled Girl",
        (
            "#1660F*sigh* I'm so booored...\x02\x03",

            "Going through all the lesser-known spots in \x01",
            "Grancel mentioned in these books was fun for\x01",
            "a while, but I've had enough now...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_2DA3")

    TalkEnd(0xFE)
    Return()

    # Function_21_2C85 end

    def Function_22_2DA7(): pass

    label("Function_22_2DA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2DB4")
    Jump("loc_30D7")

    label("loc_2DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2F4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2E4D")

    ChrTalk(    #83
        0xFE,
        (
            "The tourism industry is apparently booming\x01",
            "over in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I'd like to head on over there and see what the\x01",
            "big deal is, myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F47")

    label("loc_2E4D")


    ChrTalk(    #85
        0xFE,
        (
            "Rumor has it that Ruan's become the place\x01",
            "to visit these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Supposedly, Mayor Dalmore's really putting\x01",
            "his back into trying to encourage tourism in\x01",
            "the region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I'd like to head on over there and see what\x01",
            "the big deal is, myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_2F47")

    Jump("loc_30D7")

    label("loc_2F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_30D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3002")

    ChrTalk(    #88
        0xFE,
        (
            "I hear the mayor's daughter attends Jenis Royal\x01",
            "Academy and is one of the most intelligent \x01",
            "students there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Haha. Bose has a bright future ahead of it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_30D7")

    label("loc_3002")


    ChrTalk(    #90
        0xFE,
        "Are you familiar with Mayor Windolman of Bose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "With the leadership he showed leading the post-war\x01",
            "relief efforts and the managerial skills he gained\x01",
            "from living in Bose, he sounds remarkably capable.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_30D7")

    TalkEnd(0xFE)
    Return()

    # Function_22_2DA7 end

    def Function_23_30DB(): pass

    label("Function_23_30DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_30E8")
    Jump("loc_33AA")

    label("loc_30E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_3243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_31AF")

    ChrTalk(    #92
        0xFE,
        (
            "Crown Prince Judis and his wife have a daughter.\x01",
            "Err... Princess Klaudia, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "She was still really small when I last saw her,\x01",
            "but she was the sweetest little thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_31AF")


    ChrTalk(    #94
        0xFE,
        (
            "Come to think of it, the crown prince and his\x01",
            "wife have a daughter, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "What was her name again? Princess Klaudia,\x01",
            "I think?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3240")

    Jump("loc_33AA")

    label("loc_3243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_33AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_32F7")

    ChrTalk(    #96
        0xFE,
        (
            "It was a terrible shock when Crown Prince Judis\x01",
            "and his wife died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Their smiles are permanently burned into my \x01",
            "memory... I doubt I'll ever forget them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AA")

    label("loc_32F7")


    ChrTalk(    #98
        0xFE,
        (
            "It was a terrible shock when Crown Prince Judis\x01",
            "and his wife lost their lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "They were both such lovely people... It's a terrible\x01",
            "tragedy that we had to lose them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_33AA")

    TalkEnd(0xFE)
    Return()

    # Function_23_30DB end

    def Function_24_33AE(): pass

    label("Function_24_33AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_33BB")
    Jump("loc_35CE")

    label("loc_33BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_3482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_3421")

    ChrTalk(    #100
        0xFE,
        "Hello! Can I interest you in some ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "They really are delicious! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_347F")

    label("loc_3421")


    ChrTalk(    #102
        0xFE,
        "Oh, hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Thank you again for your purchase.\x01",
            "Stop by here again sometime!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_347F")

    Jump("loc_35CE")

    label("loc_3482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_3490")
    Call(0, 30)
    Jump("loc_35CE")

    label("loc_3490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_35CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_357B")

    ChrTalk(    #104
        0xFE,
        (
            "I'm actually a student first and foremost.\x01",
            "This is just a part-time job I do on the side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "Still, I feel like I'm really cut out for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Heehee! What do you think? Think I should\x01",
            "make a career out of it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35CE")

    label("loc_357B")


    ChrTalk(    #107
        0xFE,
        "Welcome! Would you like some ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "It's delicious, I assure you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_35CE")

    TalkEnd(0xFE)
    Return()

    # Function_24_33AE end

    def Function_25_35D2(): pass

    label("Function_25_35D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 68770, 250, -9000, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 77220, 250, 71250, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 38350, 1250, 48810, 315)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 72940, 250, 45680, 180)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 72920, 250, 44130, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 48280, 250, 49330, 180)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 48150, 250, 48100, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 39220, 1250, 48760, 270)
    SetChrChipByIndex(0x24, 35)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 24)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2B, 41350, 1250, 47920, 315)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 40300, 1250, 48720, 270)
    OP_43(0x1C, 0x0, 0x0, 0x1A)
    OP_43(0x1D, 0x0, 0x0, 0x1B)
    OP_43(0x1F, 0x0, 0x0, 0x1C)
    OP_43(0x1E, 0x0, 0x0, 0x1C)
    OP_43(0x23, 0x0, 0x0, 0x1D)
    OP_43(0x10, 0x0, 0x0, 0x1C)
    OP_62(0x21, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(70530, 0, 180, 0)
    OP_67(0, 9250, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(33000, 0)
    OP_6E(406, 0)

    def lambda_377A():
        OP_6D(71110, 0, 47280, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_377A)

    def lambda_3792():
        OP_67(0, 9250, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3792)

    def lambda_37AA():
        OP_6B(3900, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_37AA)

    def lambda_37BA():
        OP_6C(33000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_37BA)

    def lambda_37CA():
        OP_6E(406, 3000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37CA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)

    def lambda_37E9():
        OP_6D(41760, 1250, 46430, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37E9)

    def lambda_3801():
        OP_67(0, 9250, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3801)

    def lambda_3819():
        OP_6B(3900, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3819)

    def lambda_3829():
        OP_6C(333000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3829)

    def lambda_3839():
        OP_6E(406, 6000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3839)
    Sleep(4000)
    OP_62(0x1B, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_23(0xF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_25_35D2 end

    def Function_26_387C(): pass

    label("Function_26_387C")

    Sleep(4000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 64550, 1810, 22920, 270)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    OP_8E(0xFE, 0xEC9A, 0x4E2, 0x5AA0, 0x1388, 0x0)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xEB0A, 0x4E2, 0xB900, 0x1388, 0x0)
    OP_8E(0xFE, 0xD6E2, 0xFA, 0xB946, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xA5FA, 0x4E2, 0xB914, 0x1388, 0x0)
    Return()

    # Function_26_387C end

    def Function_27_3931(): pass

    label("Function_27_3931")

    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 68820, 250, 6150, 0)
    OP_8E(0xFE, 0x1112A, 0x5D2, 0x3412, 0x7D0, 0x0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_8E(0xFE, 0x10FC2, 0x6D6, 0x401A, 0x7D0, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    Return()

    # Function_27_3931 end

    def Function_28_3995(): pass

    label("Function_28_3995")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3ABB")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D1")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3AB8")

    label("loc_39D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F8")
    Sleep(1300)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3AB8")

    label("loc_39F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1F")
    Sleep(1600)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3AB8")

    label("loc_3A1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A46")
    Sleep(1900)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3AB8")

    label("loc_3A46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6D")
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3AB8")

    label("loc_3A6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A94")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3AB8")

    label("loc_3A94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB8")
    Sleep(2800)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_3AB8")

    Jump("Function_28_3995")

    label("loc_3ABB")

    Return()

    # Function_28_3995 end

    def Function_29_3ABC(): pass

    label("Function_29_3ABC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C1A")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B00")
    Sleep(1000)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_3C17")

    label("loc_3B00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2F")
    Sleep(1300)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_3C17")

    label("loc_3B2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5E")
    Sleep(160)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_3C17")

    label("loc_3B5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B8D")
    Sleep(1900)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_3C17")

    label("loc_3B8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BBC")
    Sleep(2200)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_3C17")

    label("loc_3BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BEB")
    Sleep(2500)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_3C17")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C17")
    Sleep(2800)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)

    label("loc_3C17")

    Jump("Function_29_3ABC")

    label("loc_3C1A")

    Return()

    # Function_29_3ABC end

    def Function_30_3C1B(): pass

    label("Function_30_3C1B")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(37620, 1250, 49780, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x151, 38880, 1250, 48440, 315)
    SetChrPos(0x103, 38660, 1250, 46800, 0)
    TurnDirection(0x10, 0x151, 0)
    Sleep(1500)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_62(0x151, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #109
        "\x07\x05Aina bought two ice cream cones from the stall.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    TurnDirection(0x151, 0x103, 400)
    Sleep(500)

    def lambda_3D35():
        OP_8F(0xFE, 0x9704, 0x4E2, 0xBB30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3D35)
    WaitChrThread(0x151, 0x1)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_3D76():
        OP_6D(34940, 1450, 43480, 5000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_3D76)

    def lambda_3D8E():
        OP_67(0, 5940, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_3D8E)

    def lambda_3DA6():
        OP_6C(300000, 5000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_3DA6)

    def lambda_3DB6():

        label("loc_3DB6")

        TurnDirection(0xFE, 0x151, 400)
        OP_48()
        Jump("loc_3DB6")

    QueueWorkItem2(0x103, 3, lambda_3DB6)

    def lambda_3DC7():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xB644, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3DC7)
    WaitChrThread(0x151, 0x1)

    def lambda_3DE7():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xA53C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3DE7)
    Sleep(1000)
    OP_44(0x103, 0x3)
    OP_43(0x103, 0x3, 0x0, 0x1F)
    WaitChrThread(0x151, 0x1)

    def lambda_3E17():
        OP_8E(0xFE, 0x8D90, 0x4E2, 0xA53C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3E17)
    WaitChrThread(0x151, 0x1)
    SetChrFlags(0x151, 0x40)
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x151, 40)
    SetChrSubChip(0x151, 0)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x151, 35580, 1450, 42300, 90)
    Sleep(250)
    WaitChrThread(0x103, 0x3)
    Sleep(500)
    WaitChrThread(0x39, 0x0)
    Sleep(500)
    OP_62(0x103, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #110
        0x103,
        (
            "#1645F#2PDid your brain decide to selectively switch off\x01",
            "when I said I don't like sweet things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x151,
        "#1651FYou'll like this. Promise! It's really nice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#1647F#2P(That's not how it works!)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3F66():
        OP_6D(37860, 4500, 36920, 3000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_3F66)

    def lambda_3F7E():
        OP_67(0, 6040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_3F7E)

    def lambda_3F96():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_3F96)
    WaitChrThread(0x39, 0x0)
    Sleep(200)
    SetChrSubChip(0x151, 2)
    Sleep(500)

    ChrTalk(    #113
        0x151,
        (
            "#1654F#3P(It's almost noon...)\x02\x03",

            "(That means I've only got 24 hours left...\x01",
            "I'm running out of time.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrPos(0x11, 68800, 1250, 38200, 0)
    SetChrPos(0x12, 68800, 250, 46000, 180)

    def lambda_4058():
        OP_6D(65286, 250, 44280, 3500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_4058)

    def lambda_4070():
        OP_67(0, 8300, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_4070)

    def lambda_4088():
        OP_6B(2920, 3500)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_4088)

    def lambda_4098():
        OP_6C(225000, 3500)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_4098)

    def lambda_40A8():
        OP_8E(0xFE, 0x10CC0, 0xFA, 0xACA8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_40A8)
    SetChrSubChip(0x151, 0)
    WaitChrThread(0x39, 0x0)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    OP_8C(0x11, 180, 400)

    def lambda_411C():
        OP_8E(0xFE, 0x10CC0, 0x4E2, 0x8408, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_411C)
    Sleep(500)
    OP_8C(0x12, 0, 400)

    def lambda_4143():
        OP_8E(0xFE, 0x10CC0, 0x4E2, 0xD098, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4143)
    Sleep(1000)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Aina")

    AnonymousTalk(    #114
        "\x07\x00#1656F(It might be a bit risky, but...)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(400, 50, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #115
        "\x07\x00#1644F#3SHey!#2S\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrSubChip(0x103, 2)
    Fade(500)
    OP_6D(34940, 1450, 43480, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)

    ChrTalk(    #116
        0x151,
        "#1653FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#1642F#2PWhat are you spacing out and ignoring me for?\x02\x03",

            "I was trying to ask you something!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x151, 1)
    Sleep(300)

    ChrTalk(    #118
        0x151,
        (
            "#1653F...Sorry...\x02\x03",

            "#1651FWhat was it? You look angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#1646F#2PYou're hiding something from me, aren't you?\x02\x03",

            "It's REALLY obvious.\x02\x03",

            "#1648FSo come on. Out with it.\x02\x03",

            "Or are you involved in something you can't\x01",
            "even talk to me about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x151,
        (
            "#1652F...\x02\x03",

            "Well, it's just that...\x02\x03",

            "#1651F...I realized I left something back at the hotel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        "#1647F#2PGrrr...\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #122
        0x103,
        (
            "#1646F#2P(As if anyone would buy that!)\x02\x03",

            "#1648F(Not going to talk, huh? Well, fine! Be that way!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x151,
        (
            "#1650FCan we make our way back there so I can go\x01",
            "and get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#1646F#2P...Fine. Whatever. I'll come with you.\x02\x03",

            "#1642F(At least until I get an idea of what you're\x01",
            "really up to.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x151,
        (
            "#1651FThank you! Well, shall we be going?\x02\x03",

            "Let's go through the south block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x103,
        "#1642F#2PFine.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrPos(0x151, 36240, 1250, 42300, 90)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Fade(250)
    SetChrPos(0x103, 36240, 1250, 43680, 90)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    ClearChrFlags(0x103, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x151, 0x40)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32100, 0, 64760, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32100, 0, 62820, 0)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x3, 0x0, 0xC)
    OP_B2(0x0, 0xA, 0x80)
    OP_B2(0x0, 0xB, 0x80)
    OP_B2(0x0, 0x8, 0x80)
    OP_A2(0x2F4C)
    EventEnd(0x0)
    Return()

    # Function_30_3C1B end

    def Function_31_4687(): pass

    label("Function_31_4687")


    def lambda_468D():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xB02C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_468D)
    WaitChrThread(0x103, 0x1)

    def lambda_46AD():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xAAA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_46AD)
    WaitChrThread(0x103, 0x1)

    def lambda_46CD():
        OP_8E(0xFE, 0x8D90, 0x4E2, 0xAAA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_46CD)
    WaitChrThread(0x103, 0x1)
    SetChrFlags(0x103, 0x40)
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x103, 39)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 35580, 1450, 43680, 90)
    Sleep(250)
    Return()

    # Function_31_4687 end

    def Function_32_471C(): pass

    label("Function_32_471C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(50600, 0, 45600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(354, 0)
    SetChrPos(0x103, 51540, 0, 65160, 180)
    SetChrPos(0x151, 50540, 0, 63540, 180)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    SetChrPos(0x11, 51740, 0, 70120, 180)
    SetChrPos(0x12, 50320, 0, 68900, 180)
    SetChrChipByIndex(0x11, 41)
    SetChrChipByIndex(0x12, 41)
    SetChrChipByIndex(0x13, 41)
    SetChrChipByIndex(0x14, 41)
    SetChrChipByIndex(0x15, 41)
    SetChrChipByIndex(0x16, 41)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    FadeToBright(1000, 0)

    def lambda_480E():
        OP_6D(50600, 0, 25600, 8000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_480E)

    def lambda_4826():
        OP_6B(2700, 8000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_4826)

    def lambda_4836():
        OP_6E(302, 8000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_4836)

    def lambda_4846():
        OP_67(0, 7000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_4846)

    def lambda_485E():
        OP_8E(0xFE, 0xC56C, 0x0, 0xB7C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_485E)
    Sleep(10)

    def lambda_487E():
        OP_8E(0xFE, 0xC954, 0x0, 0x14F0, 0x1F72, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_487E)
    Sleep(900)

    def lambda_489E():
        OP_8E(0xFE, 0xC490, 0x0, 0x22C4, 0x1E78, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_489E)
    Sleep(100)

    def lambda_48BE():
        OP_8E(0xFE, 0xCA1C, 0x0, 0x2788, 0x1EDC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_48BE)
    Sleep(7000)
    Fade(250)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x151, 0xFF)
    OP_44(0x103, 0xFF)
    OP_6D(50720, 0, 2400, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(304000, 0)
    OP_6E(322, 0)
    SetChrPos(0x151, 51060, 0, 13620, 180)
    SetChrPos(0x103, 51060, 0, 16620, 180)
    SetChrPos(0x11, 51060, 0, 32900, 180)
    SetChrPos(0x12, 51060, 0, 35200, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, 18600, 0, -1640, 90)
    SetChrPos(0x14, 17300, 0, -2880, 90)

    def lambda_49A0():
        OP_6D(50720, 0, -400, 2500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_49A0)

    def lambda_49B8():
        OP_6B(2800, 2500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_49B8)
    Sleep(250)
    OP_43(0x151, 0x3, 0x0, 0x21)
    Sleep(100)
    OP_43(0x103, 0x3, 0x0, 0x22)
    Sleep(2000)
    OP_43(0x13, 0x3, 0x0, 0x25)
    Sleep(100)
    OP_43(0x14, 0x3, 0x0, 0x26)
    OP_43(0x11, 0x3, 0x0, 0x23)
    OP_43(0x12, 0x3, 0x0, 0x24)
    Sleep(500)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 17300, 0, -2080, 90)

    def lambda_4A26():
        OP_8E(0xFE, 0x15A7C, 0x0, 0xFFFFF7E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4A26)
    Sleep(500)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x16, 18600, 0, 640, 90)

    def lambda_4A61():
        OP_8E(0xFE, 0x1633C, 0x0, 0x280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4A61)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_471C end

    def Function_33_4A93(): pass

    label("Function_33_4A93")


    def lambda_4A99():
        OP_8E(0xFE, 0xC774, 0x0, 0x190, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4A99)
    WaitChrThread(0x151, 0x1)

    def lambda_4AB9():
        OP_8E(0xFE, 0xC2EC, 0x0, 0xFFFFFD58, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4AB9)
    WaitChrThread(0x151, 0x1)

    def lambda_4AD9():
        OP_8E(0xFE, 0xBF04, 0x0, 0xFFFFF970, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4AD9)
    WaitChrThread(0x151, 0x1)

    def lambda_4AF9():
        OP_8E(0xFE, 0xBB80, 0x0, 0xFFFFF970, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4AF9)
    WaitChrThread(0x151, 0x1)

    def lambda_4B19():
        OP_8E(0xFE, 0xBB1C, 0x0, 0xFFFFF970, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4B19)
    WaitChrThread(0x151, 0x1)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x151, 0x0, 0x0, 0x0, 0x320, 0x1388)
    Sleep(500)
    OP_8C(0x151, 90, 500)
    Sleep(200)

    def lambda_4B78():
        OP_8E(0xFE, 0x15E50, 0x0, 0xFFFFF970, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4B78)
    WaitChrThread(0x151, 0x1)

    def lambda_4B98():
        OP_8E(0xFE, 0x16300, 0x0, 0xFFFFFE20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4B98)
    WaitChrThread(0x151, 0x1)

    def lambda_4BB8():
        OP_8E(0xFE, 0x16300, 0x0, 0xC0A8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4BB8)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_33_4A93 end

    def Function_34_4BD3(): pass

    label("Function_34_4BD3")


    def lambda_4BD9():
        OP_8E(0xFE, 0xC774, 0x0, 0x50, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BD9)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 500)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_4C1C():
        OP_8F(0xFE, 0xCB5C, 0x0, 0x50, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C1C)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(200)

    def lambda_4C48():
        OP_8E(0xFE, 0x15680, 0x0, 0x50, 0x1EDC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C48)
    WaitChrThread(0x103, 0x1)

    def lambda_4C68():
        OP_8E(0xFE, 0x15A68, 0x0, 0x438, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C68)
    WaitChrThread(0x103, 0x1)

    def lambda_4C88():
        OP_8E(0xFE, 0x15A68, 0x0, 0xC3A0, 0x1E14, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C88)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_34_4BD3 end

    def Function_35_4CA3(): pass

    label("Function_35_4CA3")


    def lambda_4CA9():
        OP_8E(0xFE, 0xC774, 0x0, 0x44C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4CA9)
    WaitChrThread(0x11, 0x1)

    def lambda_4CC9():
        OP_8E(0xFE, 0xC968, 0x0, 0x258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4CC9)
    WaitChrThread(0x11, 0x1)

    def lambda_4CE9():
        OP_8E(0xFE, 0x15860, 0x0, 0x258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4CE9)
    WaitChrThread(0x11, 0x1)
    Sleep(750)

    def lambda_4D0E():
        OP_8E(0xFE, 0x15860, 0x0, 0xC5A8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4D0E)
    Sleep(50)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_35_4CA3 end

    def Function_36_4D2E(): pass

    label("Function_36_4D2E")


    def lambda_4D34():
        OP_8E(0xFE, 0xC774, 0x0, 0xFFFFFF9C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4D34)
    WaitChrThread(0x12, 0x1)

    def lambda_4D54():
        OP_8E(0xFE, 0xC968, 0x0, 0xFFFFFDA8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4D54)
    WaitChrThread(0x12, 0x1)

    def lambda_4D74():
        OP_8E(0xFE, 0x15F40, 0x0, 0xFFFFFDA8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4D74)
    WaitChrThread(0x12, 0x1)
    Sleep(50)

    def lambda_4D99():
        OP_8E(0xFE, 0x15F40, 0x0, 0xC094, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4D99)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_36_4D2E end

    def Function_37_4DB4(): pass

    label("Function_37_4DB4")


    def lambda_4DBA():
        OP_8E(0xFE, 0x1633C, 0x0, 0xFFFFF998, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4DBA)
    WaitChrThread(0x13, 0x1)
    Sleep(250)

    def lambda_4DDF():
        OP_8E(0xFE, 0x1633C, 0x0, 0xC1E8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4DDF)
    Sleep(300)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_37_4DB4 end

    def Function_38_4DFF(): pass

    label("Function_38_4DFF")


    def lambda_4E05():
        OP_8E(0xFE, 0x15A7C, 0x0, 0xFFFFF4C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4E05)
    WaitChrThread(0x14, 0x1)

    def lambda_4E25():
        OP_8E(0xFE, 0x15A7C, 0x0, 0xBC98, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4E25)
    WaitChrThread(0x14, 0x1)
    Return()

    # Function_38_4DFF end

    def Function_39_4E40(): pass

    label("Function_39_4E40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(102420, 1250, 14240, 0)
    OP_67(0, 9840, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(328, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, 103800, 1250, 16600, 270)
    SetChrPos(0x151, 102560, 1250, 15500, 270)
    SetChrChipByIndex(0x103, 49)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x2F, 0x80)

    def lambda_4ED9():
        OP_6D(103660, 1250, 15100, 6000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_4ED9)

    def lambda_4EF1():
        OP_67(0, 4280, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_4EF1)

    def lambda_4F09():
        OP_6C(145000, 6000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_4F09)

    def lambda_4F19():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_4F19)
    OP_20(0x1770)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x39, 0x0)

    def lambda_4F3D():
        OP_8F(0xFE, 0x18FC4, 0x4E2, 0x4178, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4F3D)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #127
        0x151,
        "#1652FI think we lost them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        (
            "#1645F#5P*pant*...*pant*...\x01",
            "J-Just about...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #129
        0x103,
        (
            "#1642F#5PO-Okay, I've had enough of this.\x01",
            "It's time for you to open that mouth\x01",
            "of yours.\x02\x03",

            "#1644FJust who are these guys?\x02\x03",

            "Why do they want to catch you?\x02\x03",

            "What do you even want?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #130
        0x151,
        "#1656F#4PWell...\x02",
    )

    CloseMessageWindow()
    OP_59()

    ChrTalk(    #131
        0x103,
        (
            "#1646F#5PDon't even try and worm your way out of answering.\x01",
            "I will hurt you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    Sleep(500)

    ChrTalk(    #132
        0x103,
        "#1648F#5P...With THIS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x151,
        (
            "#1655F#4PTh-That sounds painful...\x02\x03",

            "#1654F...\x02\x03",

            "#1656FNo use hiding it any longer, is there?\x02\x03",

            "They're trying to capture me.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(400)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    Sleep(800)

    ChrTalk(    #134
        0x103,
        (
            "#1645F#5PThank you, Captain Obvious.\x02\x03",

            "#1642FI'm asking WHY they want to capture you.\x02\x03",

            "Go on. Get talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x151,
        "#1654F#4PL-Let me start from the beginning.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x103, 104040, 1250, 17520, 250)
    SetChrPos(0x151, 102460, 1250, 16600, 60)
    OP_6D(102880, 750, 14840, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(186000, 0)
    OP_6E(262, 0)

    def lambda_52CF():
        OP_6D(102880, 1250, 14840, 18000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_52CF)

    def lambda_52E7():
        OP_67(0, 4200, -10000, 18000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_52E7)
    Sleep(1000)
    OP_1D(0x73)
    Sleep(500)

    ChrTalk(    #136
        0x151,
        (
            "#1656F#2PI suppose it started about a month ago...\x02\x03",

            "My grandfather, who I was living with,\x01",
            "passed away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x103,
        "#1642FYour grandfather?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x151,
        (
            "#1654F#2PThat's right.\x02\x03",

            "He did mention that he intended to leave some\x01",
            "of his fortune to me...\x02\x03",

            "...but the will didn't just say 'some'--he wrote\x01",
            "that he intended to leave me everything he had.\x02\x03",

            "#1656FSo...well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#1646FA super rich guy leaving his fortune to a young\x01",
            "girl...\x02\x03",

            "Okay. Everything's starting to fall into place.\x02\x03",

            "#1648FSo now every relative you have under the sun\x01",
            "is on you like ants trying to get their share?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x151,
        (
            "#1654F#2PAt the very least, I still think my uncle is a very\x01",
            "nice man.\x02\x03",

            "#1656FHe said he wants to look after me until I turn\x01",
            "twenty, so as part of that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#1648F...you should let him 'look after' all the money\x01",
            "you've inherited?\x02\x03",

            "#1648FUgh. Unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x151,
        (
            "#1656F#2PMaybe.\x02\x03",

            "#1651FHis eyes when he said that kind of scared me,\x01",
            "so I ended up turning his offer down.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #143
        0x103,
        "#1647F...Wait. Hide!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x39, 0xFF)
    Fade(500)
    OP_6D(97630, 250, 16560, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 97100, 250, 5380, 0)

    def lambda_574F():
        OP_8E(0xFE, 0x17B4C, 0xFA, 0x6FB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_574F)
    SetChrPos(0x103, 103230, 1250, 16079, 270)
    SetChrPos(0x151, 102560, 1250, 15500, 270)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    Sleep(500)

    ChrTalk(    #144
        0x151,
        (
            "#1656F#4PAnd now someone's hired those men\x01",
            "to come after me.\x02\x03",

            "If I don't formally inherit his money, \x01",
            "Grandfather's will becomes invalid,\x01",
            "you see...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_5836():
        OP_6D(103660, 1250, 15100, 2500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_5836)

    def lambda_584E():
        OP_67(0, 4100, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_584E)

    def lambda_5866():
        OP_6C(145000, 2500)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_5866)

    def lambda_5876():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_5876)

    def lambda_5886():
        OP_6E(262, 2500)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_5886)
    Sleep(500)

    def lambda_589B():
        OP_8F(0xFE, 0x18FC4, 0x4E2, 0x4178, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_589B)
    Sleep(500)

    def lambda_58BB():
        OP_8F(0xFE, 0x19578, 0x4E2, 0x40D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58BB)
    WaitChrThread(0x39, 0x0)

    ChrTalk(    #145
        0x151,
        (
            "#1656F#4PMost likely, that's the reason they want to\x01",
            "capture me. So I'm not able to do that.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #146
        0x103,
        (
            "#1646F#5PThey're no ordinary street thugs, either.\x01",
            "They clearly have some experience under\x01",
            "their belts.\x02\x03",

            "I can't believe they're just able to wander\x01",
            "the streets of the capital in broad daylight\x01",
            "like this...\x02\x03",

            "#1642FJust what is the army even doing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #147
        0x151,
        (
            "#1652F#4POne of my relatives has connections in\x01",
            "the Royal Army, so that's probably why.\x02\x03",

            "#1651FMy family's pretty influential, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x103,
        (
            "#1645F#5PArgh... I'm getting a headache just listening\x01",
            "to all of this...\x02\x03",

            "Hiring a bunch of suspicious, highly-trained\x01",
            "underlings to fight over an inheritance?\x02\x03",

            "You don't get more stereotypically 'spiteful rich\x01",
            "person' than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x151,
        (
            "#1656F#4PI...\x02\x03",

            "#1655FI'm sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x103,
        "#1646F#5PI'm not looking for an apology from you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)

    ChrTalk(    #151
        0x103,
        (
            "#1642F(Still, this really isn't looking good...)\x02\x03",

            "(I might have been able to win the last battle,\x01",
            "but I'm not confident I could win another.)\x02\x03",

            "(I think the best thing we can do is try and get\x01",
            "back to the guildhouse without getting caught,\x01",
            "but I can't see that being easy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_5D71():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5D71)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_5D9B():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_5D9B)
    Sleep(450)

    def lambda_5DAE():
        OP_8F(0xFE, 0x190A0, 0x4E2, 0x3C8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5DAE)

    def lambda_5DC9():
        OP_6D(97630, 250, 16560, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_5DC9)

    def lambda_5DE1():
        OP_67(0, 5860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_5DE1)

    def lambda_5DF9():
        OP_6C(140000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_5DF9)

    def lambda_5E09():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_5E09)

    def lambda_5E19():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_5E19)
    Sleep(200)

    def lambda_5E2E():
        OP_8F(0xFE, 0x1933E, 0x4E2, 0x3ECF, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E2E)
    WaitChrThread(0x39, 0x0)
    OP_44(0x103, 0x1)
    ClearChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    SetChrPos(0x12, 97100, 250, 28600, 0)

    def lambda_5E6C():
        OP_8E(0xFE, 0x17B4C, 0xFA, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E6C)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #152
        0x151,
        "#4P(...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x103,
        "#4P(*gulp*)\x02",
    )

    CloseMessageWindow()

    def lambda_5ECF():
        OP_8E(0xFE, 0x17B4C, 0xFA, 0x2C10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5ECF)
    Sleep(600)

    ChrTalk(    #154
        0x103,
        "#1645F#4PWhew...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_20(0x3E8)

    ChrTalk(    #155
        0x12,
        (
            "#3P...\x02\x03",

            "#3PCome to think of it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x12,
        "#3PI forgot to feed the birds.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #157
        0x151,
        "#1653F#4P(Feed the birds?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#1642F#4P(I doubt it's meant to be taken literally.\x01",
            "It's probably some kind of code they use...)\x02\x03",

            "(...which means...)\x02\x03",

            "#1647F...Crap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x151,
        "#1653F#4P...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    SetChrPos(0x13, 100900, 250, 40500, 180)
    SetChrPos(0x14, 97960, 250, 40900, 180)

    def lambda_605C():
        OP_8E(0xFE, 0x18A24, 0xFA, 0x8980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_605C)
    OP_43(0x14, 0x3, 0x0, 0x2A)
    Fade(500)
    SetChrPos(0x103, 101700, 1250, 14500, 0)
    SetChrPos(0x151, 100740, 1250, 14300, 0)
    OP_6D(101400, 0, 26460, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_43(0x103, 0x3, 0x0, 0x28)
    OP_43(0x151, 0x3, 0x0, 0x29)
    WaitChrThread(0x103, 0x3)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #160
        0x13,
        "#6PSorry. This way's a dead end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        (
            "#6PYou've been giving us a hell of a lot of trouble,\x01",
            "but your luck just ran out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6176():
        OP_8F(0xFE, 0x18C18, 0xFA, 0x7738, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6176)

    ChrTalk(    #162
        0x103,
        "#1647F#5PUgh!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 600)
    Sleep(250)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, 98100, 250, 21760, 0)

    def lambda_61E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_61E5)

    def lambda_61F7():
        OP_8E(0xFE, 0x17F34, 0xFA, 0x6824, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_61F7)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #163
        0x12,
        (
            "#1PHmph. You're fast, though.\x01",
            "I'll give you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x12,
        "#1P...#3SNow grab her!#2S\x02",
    )

    Sleep(30)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6296():
        OP_6B(2100, 1000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_6296)
    SetChrChipByIndex(0x13, 41)
    SetChrSubChip(0x13, 0)

    def lambda_62B0():
        OP_8F(0xFE, 0x18A24, 0xFA, 0x7ABC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_62B0)
    SetChrChipByIndex(0x14, 41)
    SetChrSubChip(0x14, 0)

    def lambda_62D5():
        OP_8F(0xFE, 0x1863C, 0xFA, 0x7ABC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_62D5)
    Sleep(400)
    OP_44(0x39, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    Battle(0x3AD, 0x0, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 43)
    Return()

    # Function_39_4E40 end

    def Function_40_631B(): pass

    label("Function_40_631B")


    def lambda_6321():
        OP_8E(0xFE, 0x18C18, 0x4E2, 0x4CF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6321)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 47)
    SetChrSubChip(0x103, 2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6350():
        OP_96(0xFE, 0x18C18, 0xFA, 0x66BC, 0x546, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6350)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    ClearChrFlags(0x103, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_6387():
        OP_8E(0xFE, 0x18C18, 0xFA, 0x78C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6387)

    def lambda_63A2():
        OP_6D(101400, 250, 29720, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_63A2)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x39, 0x0)
    Return()

    # Function_40_631B end

    def Function_41_63BF(): pass

    label("Function_41_63BF")

    Sleep(100)

    def lambda_63CA():
        OP_8E(0xFE, 0x18984, 0x4E2, 0x4B00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_63CA)
    WaitChrThread(0x151, 0x1)
    SetChrChipByIndex(0x151, 48)
    SetChrSubChip(0x151, 5)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_63F9():
        OP_96(0xFE, 0x18984, 0xFA, 0x6270, 0x514, 0xA8C)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_63F9)
    WaitChrThread(0x151, 0x1)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_6435():
        OP_8E(0xFE, 0x18984, 0xFA, 0x74A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6435)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_41_63BF end

    def Function_42_6450(): pass

    label("Function_42_6450")

    Sleep(150)

    def lambda_645B():
        OP_8E(0xFE, 0x17EA8, 0xFA, 0x8750, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_645B)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 135, 500)
    Return()

    # Function_42_6450 end

    def Function_43_647D(): pass

    label("Function_43_647D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x50, 0xFC, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    OP_1D(0x29)
    OP_6D(101400, 0, 29720, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 101400, 250, 30520, 0)
    SetChrPos(0x151, 100740, 250, 29860, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x13, 100900, 250, 35200, 180)
    SetChrPos(0x14, 97960, 250, 34640, 135)
    SetChrPos(0x12, 98100, 250, 26660, 0)
    SetChrPos(0x15, 91000, 0, 35280, 90)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 45)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x13, 45)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x2F, 0x80)
    LoadEffect(0x1, "map\\\\mp286_00.eff")
    SoundLoad(393)
    SoundLoad(127)
    SoundLoad(132)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_65D5"),
        (0, "loc_65E2"),
        (SWITCH_DEFAULT, "loc_65EF"),
    )


    label("loc_65D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65EF")

    label("loc_65E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_65EF")

    label("loc_65EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6627")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆Won\x01",       # 0
            "◆Lost\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_6627")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_6638"),
        (0, "loc_6645"),
        (SWITCH_DEFAULT, "loc_6659"),
    )


    label("loc_6638")

    SetChrChipByIndex(0x103, 6)
    SetChrSubChip(0x103, 3)
    Jump("loc_6659")

    label("loc_6645")

    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 0)
    Jump("loc_6659")

    label("loc_6659")

    FadeToBright(1000, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_6674"),
        (0, "loc_679E"),
        (SWITCH_DEFAULT, "loc_6857"),
    )


    label("loc_6674")


    ChrTalk(    #165
        0x103,
        "#1647F*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x103,
        "#1645FUgh... *cough*\x02",
    )

    OP_9E(0x103, 0xA, 0x0, 0x1F4, 0xBB8)
    CloseMessageWindow()

    ChrTalk(    #167
        0x151,
        (
            "#1652FMiss Scherazard?!\x02\x03",

            "A-Are you all right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66F8():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_66F8)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 0)
    Sleep(500)

    ChrTalk(    #168
        0x103,
        (
            "#1647FI-I'm fine...\x02\x03",

            "Just get back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x12,
        (
            "#1PWell, I'll give you a little more credit\x01",
            "for not giving up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6857")

    label("loc_679E")

    OP_8C(0x103, 315, 0)

    ChrTalk(    #170
        0x12,
        "#1PWell, well... Not half bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        (
            "#1642F#1P*pant*...*pant*...\x02\x03",

            "#1647F(I don't think I can fight my way\x01",
            "out of this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x151,
        "#1653FA-Are you all right, Miss Scherazard?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6857")

    label("loc_6857")


    ChrTalk(    #173
        0x15,
        "#1PHave you guys still not caught her?\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_688A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_688A)
    SetChrPos(0x15, 90800, 0, 31660, 90)

    def lambda_68AD():
        OP_8E(0xFE, 0x17C78, 0xFA, 0x7BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_68AD)
    Sleep(400)

    def lambda_68CD():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_68CD)
    Sleep(200)

    def lambda_68E0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_68E0)
    Sleep(200)

    def lambda_68F3():
        OP_8F(0xFE, 0x18D80, 0xFA, 0x72B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_68F3)
    Sleep(1000)

    def lambda_6913():
        OP_6D(99000, 0, 29760, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6913)

    def lambda_692B():
        OP_6B(2860, 1000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_692B)
    OP_43(0x103, 0x3, 0x0, 0x2C)
    WaitChrThread(0x15, 0x1)

    ChrTalk(    #174 op#A
        0x15,
        "#10AWell, well.\x02",
    )

    Sleep(50)

    def lambda_695F():
        OP_96(0xFE, 0x17340, 0x0, 0x7C74, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_695F)
    WaitChrThread(0x15, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Sleep(300)
    OP_22(0xD8, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x15, 45)
    SetChrSubChip(0x15, 0)
    Sleep(250)
    OP_22(0xD8, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x12, 45)
    SetChrSubChip(0x12, 0)
    Sleep(250)

    ChrTalk(    #175
        0x15,
        (
            "You almost stood a chance against us.\x01",
            "Almost.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #176
        0x103,
        (
            "#1647F#3P*pant*...*pant*...\x02\x03",

            "(I don't want to be beaten by a bunch\x01",
            "of low-life scum like these guys...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x151,
        (
            "#1652F#4P(Do you have any ideas for getting us\x01",
            "out of this?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x103,
        "#1643F#3PMe?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x151,
        "#1652F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#1643F#3P...Oh.\x02\x03",

            "#1642F(There's an entrance to the sewers nearby.)\x02\x03",

            "(If we can get to that, we might be able to \x01",
            "escape to the west block. That's a huge IF,\x01",
            "though.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x151,
        (
            "#1654F#4P...All right. Let's go with that.\x02\x03",

            "#1656FClose your eyes for a second.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)

    def lambda_6BD4():
        OP_6D(100660, 0, 30060, 1400)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6BD4)

    def lambda_6BEC():
        OP_6C(135000, 1400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_6BEC)

    def lambda_6BFC():
        OP_6B(3260, 1400)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_6BFC)

    def lambda_6C0C():
        OP_8E(0xFE, 0x18BF0, 0xFA, 0x72B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6C0C)
    WaitChrThread(0x151, 0x1)

    def lambda_6C2C():
        OP_8E(0xFE, 0x18740, 0xFA, 0x7760, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6C2C)
    WaitChrThread(0x151, 0x1)
    WaitChrThread(0x39, 0x0)
    Fade(250)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 0)
    OP_0D()

    ChrTalk(    #182 op#A
        0x103,
        "#1642F#3P#17AWh-What are you...?!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x151, 42)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 45, 0)
    Sleep(800)

    ChrTalk(    #183
        0x151,
        "#1652FOne, two...\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x15,
        "Wh-Whoa! What are you...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6B(3060, 0)
    OP_0D()

    def lambda_6D1A():
        OP_6D(100660, 1000, 30060, 500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6D1A)
    PlayEffect(0x1, 0x1, 0x151, -1500, 1500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #185 op#A
        0x151,
        "#4S#10A#6PThree!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    SetChrSubChip(0x151, 1)
    Sleep(500)

    def lambda_6D9A():
        OP_6D(100660, 0, 30060, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6D9A)

    def lambda_6DB2():
        OP_6B(3260, 1000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_6DB2)
    Sleep(900)
    OP_22(0x189, 0x0, 0x64)
    Sleep(2600)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 400)
    Sleep(300)

    ChrTalk(    #186
        0x103,
        "#1643F#3SWh-What's THAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x12,
        "#3SA-A smoke grenade?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 0)

    def lambda_6EDD():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_6EDD)
    OP_22(0x20C, 0x0, 0x64)

    ChrTalk(    #188
        0x13,
        "*cough* *cough*\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 0)

    def lambda_6F11():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_6F11)
    OP_22(0x20C, 0x0, 0x64)

    ChrTalk(    #189
        0x14,
        "M-My eyes!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x12, 7)
    SetChrSubChip(0x12, 0)

    def lambda_6F40():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_6F40)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x15, 7)
    SetChrSubChip(0x15, 0)

    def lambda_6F64():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_6F64)
    OP_22(0x20C, 0x0, 0x64)
    WaitChrThread(0x15, 0x3)
    OP_82(0x1, 0x2)
    OP_11(0xFF, 0xFF, 0x0, 0x9C40, 0x249F0, 0x0)
    StopSound(0x64, 0x249F0, 0x3E8)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 315, 0)
    Sleep(500)

    def lambda_6FBE():
        OP_6D(101760, 250, 32900, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6FBE)

    def lambda_6FD6():
        OP_6B(3100, 1000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_6FD6)

    def lambda_6FE6():
        OP_8E(0xFE, 0x188F8, 0xFA, 0x8318, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6FE6)
    Sleep(800)

    def lambda_7006():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7006)
    WaitChrThread(0x151, 0x1)
    Fade(250)
    SetChrChipByIndex(0x151, 43)
    SetChrSubChip(0x151, 0)
    Sleep(250)

    def lambda_702D():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_702D)
    WaitChrThread(0x151, 0x3)
    Sleep(100)

    def lambda_7047():
        OP_6B(3000, 500)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_7047)
    SetChrFlags(0x151, 0x20)
    SetChrFlags(0x151, 0x1000)

    def lambda_7061():
        OP_99(0xFE, 0x2, 0x6, 0x5DC)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_7061)

    def lambda_7071():
        OP_96(0xFE, 0x188F8, 0xFA, 0x850C, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7071)

    ChrTalk(    #190 op#A
        0x151,
        "#3S#5A#2PHah!#2S\x02",
    )

    Sleep(150)

    def lambda_70A9():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_70A9)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_70BE():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_70BE)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 46)
    SetChrSubChip(0x13, 0)

    def lambda_70E7():
        OP_95(0xFE, 0x0, 0xFFFFFF9C, 0x5DC, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_70E7)

    ChrTalk(    #191 op#A
        0x13,
        "#3S#8AGraaah!#2S\x02",
    )

    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
    WaitChrThread(0x13, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrPos(0x13, 100550, 250, 37400, 180)
    ClearChrFlags(0x13, 0x1)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 44)
    SetChrSubChip(0x13, 0)
    Sleep(500)

    def lambda_7165():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7165)
    Sleep(1000)
    SetChrSubChip(0x151, 7)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x20)
    ClearChrFlags(0x151, 0x1000)
    OP_0D()
    Sleep(100)
    TurnDirection(0x151, 0x103, 500)
    WaitChrThread(0x39, 0x2)
    Sleep(100)

    ChrTalk(    #192
        0x151,
        "#1651FReady to go?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x151, 0x3, 0x0, 0x2D)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #193
        0x103,
        "#1643F#2PWh... #3SWhaaat?!#2S\x02",
    )

    CloseMessageWindow()
    StopSound(0x64, 0x13880, 0x3E8)

    ChrTalk(    #194
        0x103,
        (
            "#1642F#2P(Ugh... What is this smell?)\x02\x03",

            "(Is this mustard gas?)\x02\x03",

            "#1644F#3SW-Wait up!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x2E)
    Sleep(1000)

    def lambda_728C():
        OP_6D(100660, 0, 30060, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_728C)
    WaitChrThread(0x39, 0x0)

    def lambda_72A9():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_72A9)

    ChrTalk(    #195
        0x14,
        "*cough*...*cough*...\x02",
    )

    CloseMessageWindow()
    OP_99(0x15, 0x3, 0x1, 0x3E8)
    Fade(100)
    SetChrChipByIndex(0x15, 1)
    SetChrSubChip(0x15, 0)
    Sleep(100)
    OP_8C(0x15, 0, 500)
    Sleep(300)

    ChrTalk(    #196
        0x15,
        "#3SD-Don't let them get away!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrChipByIndex(0x15, 41)
    SetChrSubChip(0x15, 0)

    def lambda_7347():
        OP_8E(0xFE, 0x17480, 0x0, 0xAFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7347)
    Sleep(100)
    OP_99(0x12, 0x3, 0x1, 0x3E8)
    Fade(100)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    Sleep(100)
    SetChrChipByIndex(0x12, 41)
    SetChrSubChip(0x12, 0)

    def lambda_738E():
        OP_8E(0xFE, 0x184AC, 0xFA, 0x7EF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_738E)
    WaitChrThread(0x12, 0x1)

    def lambda_73AE():
        OP_8E(0xFE, 0x184AC, 0xFA, 0xADD4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_73AE)
    Sleep(1500)
    Fade(1000)
    OP_44(0x15, 0x1)
    OP_44(0x12, 0x1)
    SetChrPos(0x15, 97400, 250, 39800, 0)
    SetChrPos(0x12, 95300, 0, 38340, 0)
    OP_44(0x103, 0x3)
    OP_44(0x151, 0x3)
    SetChrPos(0x151, 124140, -3500, 70900, 110)
    SetChrPos(0x103, 97140, 250, 39000, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(97000, 250, 49280, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_7490():
        OP_8E(0xFE, 0x17B74, 0xFA, 0x10DD8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7490)
    StopSound(0x9C40, 0x249F0, 0x5DC)
    PlayEffect(0x1, 0x1, 0xFF, 96160, 250, 39220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 4000)
    Sleep(1000)
    OP_11(0xA4, 0xB7, 0xFF, 0x9C40, 0x249F0, 0x0)
    Sleep(700)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    ChrTalk(    #197 op#A
        0x103,
        (
            "#1644F#3S#22AWhy do you even HAVE that thing?!#2S\x02\x03",

            "#1644F#40A#3S...And what was the point of knocking\x01",
            "that guy out, too?!#2S\x02",
        )
    )

    Sleep(100)

    def lambda_75B9():
        OP_6D(97140, 250, 54600, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_75B9)
    Sleep(2000)

    def lambda_75D6():
        OP_8E(0xFE, 0x17C78, 0xFA, 0x110A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_75D6)

    def lambda_75F1():
        OP_8E(0xFE, 0x17444, 0x0, 0x10AF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_75F1)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x103, 0x1)
    OP_6D(125460, -3500, 72120, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(70000, 0)
    OP_6E(262, 0)
    OP_82(0x1, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #198
        0x151,
        "#1655F#6PIt's locked...\x02",
    )

    CloseMessageWindow()
    OP_44(0x103, 0xFF)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x103, 105160, 250, 69000, 90)

    ChrTalk(    #199
        0x103,
        "#1644F#3SGet out of the way!#2S\x02",
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x2F)
    Sleep(1000)
    Sleep(500)
    TurnDirection(0x151, 0x103, 500)
    Sleep(500)

    def lambda_7717():
        OP_8F(0xFE, 0x1E26C, 0xFFFFF254, 0x11954, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7717)
    WaitChrThread(0x151, 0x1)

    def lambda_7737():

        label("loc_7737")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_7737")

    QueueWorkItem2(0x151, 3, lambda_7737)
    WaitChrThread(0x103, 0x3)
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #200
        "\x07\x05Scherazard took out a wire and jammed it into the keyhole.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x64)
    Sleep(200)
    OP_22(0x73, 0x0, 0x64)
    Sleep(350)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_70(0xB, 0x78)
    OP_73(0xB)

    def lambda_77DA():
        OP_8F(0xFE, 0x1ECA8, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_77DA)
    WaitChrThread(0x103, 0x1)
    OP_44(0x151, 0x3)
    OP_8C(0x103, 290, 500)
    Sleep(100)

    ChrTalk(    #201
        0x103,
        "#1644FCome on! Hurry!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 110, 500)
    Sleep(100)
    OP_43(0x14, 0x3, 0x0, 0x30)

    def lambda_7838():
        OP_8F(0xFE, 0x1FA40, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7838)

    def lambda_7853():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7853)
    Sleep(100)

    def lambda_786A():
        OP_8E(0xFE, 0x1E424, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_786A)
    WaitChrThread(0x151, 0x1)

    def lambda_788A():
        OP_8E(0xFE, 0x1ECA8, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_788A)
    WaitChrThread(0x151, 0x1)

    def lambda_78AA():
        OP_8E(0xFE, 0x1FA40, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_78AA)

    def lambda_78C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_78C5)
    Sleep(500)
    OP_6F(0xB, 120)
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_72(0xB, 0x8)
    ExitThread()
    OP_70(0xB, 0x0)
    Sleep(100)
    OP_22(0xA8, 0x0, 0x64)
    OP_73(0xB)
    OP_43(0x12, 0x3, 0x0, 0x31)
    Sleep(800)
    OP_43(0x15, 0x3, 0x0, 0x32)
    OP_22(0x73, 0x0, 0x64)
    WaitChrThread(0x12, 0x3)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(1300)
    FadeToDark(2000, 0, -1)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(1300)
    OP_0D()
    NewScene("ED6_DT21/C4202   ._SN", 121, 0, 0)
    IdleLoop()
    Return()

    # Function_43_647D end

    def Function_44_7943(): pass

    label("Function_44_7943")


    ChrTalk(    #202 op#A
        0x103,
        "#3S#6A#1PHaaah!\x02",
    )

    Sleep(200)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 5)

    def lambda_796C():
        OP_99(0x103, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_796C)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_44_7943 end

    def Function_45_7981(): pass

    label("Function_45_7981")


    def lambda_7987():
        OP_8E(0xFE, 0x1854C, 0xFA, 0x8890, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_7987)
    WaitChrThread(0x151, 0x1)

    def lambda_79A7():
        OP_8E(0xFE, 0x1854C, 0xFA, 0xB388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_79A7)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_45_7981 end

    def Function_46_79C2(): pass

    label("Function_46_79C2")


    def lambda_79C8():
        OP_8E(0xFE, 0x1854C, 0xFA, 0x80C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79C8)
    WaitChrThread(0x103, 0x1)

    def lambda_79E8():
        OP_8E(0xFE, 0x1854C, 0xFA, 0xB388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79E8)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_46_79C2 end

    def Function_47_7A03(): pass

    label("Function_47_7A03")


    def lambda_7A09():
        OP_8F(0xFE, 0x1D164, 0xFFFFF254, 0x10D88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A09)
    WaitChrThread(0x103, 0x1)

    def lambda_7A29():
        OP_8F(0xFE, 0x1E4EC, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A29)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 110, 500)
    Sleep(100)
    Return()

    # Function_47_7A03 end

    def Function_48_7A50(): pass

    label("Function_48_7A50")

    SetChrPos(0x14, 105760, 250, 68820, 90)

    ChrTalk(    #203 op#A
        0x14,
        "#10A#3SWait! Get back here, damn it!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    CloseMessageWindow()
    Return()

    # Function_48_7A50 end

    def Function_49_7A9D(): pass

    label("Function_49_7A9D")

    SetChrPos(0x12, 105160, 250, 69000, 90)

    def lambda_7AB4():
        OP_8E(0xFE, 0x1D164, 0xFFFFF254, 0x10D88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7AB4)
    WaitChrThread(0x12, 0x1)

    def lambda_7AD4():
        OP_8E(0xFE, 0x1E4EC, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7AD4)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 110, 500)
    Sleep(100)
    Return()

    # Function_49_7A9D end

    def Function_50_7B05(): pass

    label("Function_50_7B05")

    SetChrPos(0x15, 105160, 250, 69600, 90)

    def lambda_7B1C():
        OP_8E(0xFE, 0x1D164, 0xFFFFF254, 0x10FE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7B1C)
    WaitChrThread(0x15, 0x1)

    def lambda_7B3C():
        OP_8E(0xFE, 0x1DF24, 0xFFFFF254, 0x11940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7B3C)
    WaitChrThread(0x15, 0x1)
    SetChrChipByIndex(0x15, 1)
    SetChrSubChip(0x15, 0)
    OP_8C(0x15, 110, 500)
    Sleep(100)
    Return()

    # Function_50_7B05 end

    def Function_51_7B6D(): pass

    label("Function_51_7B6D")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C3D")
    Fade(1000)
    OP_6D(72000, 1250, 52940, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 71700, 1250, 52340, 180)
    SetChrPos(0x151, 70340, 1250, 52400, 180)
    OP_0D()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(150)
    OP_62(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_7C1A():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7C1A)
    Sleep(150)

    def lambda_7C2D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_7C2D)
    Sleep(300)
    Jump("loc_7C59")

    label("loc_7C3D")


    def lambda_7C43():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7C43)

    def lambda_7C51():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_7C51)

    label("loc_7C59")

    Call(0, 53)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CC2")

    def lambda_7C6B():
        OP_6D(72000, 1250, 52940, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_7C6B)
    WaitChrThread(0x39, 0x0)
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x151, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_A2(0x2F53)
    EventEnd(0x0)
    Jump("loc_7D29")

    label("loc_7CC2")

    Fade(1000)
    SetChrPos(0x103, 70000, 1250, 51780, 180)
    SetChrPos(0x151, 70000, 1250, 51780, 180)
    OP_6D(70000, 1250, 51780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    EventEnd(0x0)

    label("loc_7D29")

    Return()

    # Function_51_7B6D end

    def Function_52_7D2A(): pass

    label("Function_52_7D2A")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DFA")
    Fade(1000)
    OP_6D(71440, 1250, 39340, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 70700, 1250, 38560, 315)
    SetChrPos(0x151, 69340, 1250, 38040, 315)
    OP_0D()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(150)
    OP_62(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_7DD7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7DD7)
    Sleep(150)

    def lambda_7DEA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_7DEA)
    Sleep(300)
    Jump("loc_7E16")

    label("loc_7DFA")


    def lambda_7E00():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7E00)

    def lambda_7E0E():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_7E0E)

    label("loc_7E16")

    Call(0, 53)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E7F")

    def lambda_7E28():
        OP_6D(71440, 1250, 39340, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_7E28)
    WaitChrThread(0x39, 0x0)
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x151, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_A2(0x2F53)
    EventEnd(0x0)
    Jump("loc_7EE6")

    label("loc_7E7F")

    Fade(1000)
    SetChrPos(0x103, 70000, 1250, 38200, 0)
    SetChrPos(0x151, 70000, 1250, 38200, 0)
    OP_6D(70000, 1250, 38200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    EventEnd(0x0)

    label("loc_7EE6")

    Return()

    # Function_52_7D2A end

    def Function_53_7EE7(): pass

    label("Function_53_7EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_END)), "loc_812C")

    def lambda_7EF4():
        OP_6D(74200, 500, 45620, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_7EF4)

    def lambda_7F0C():
        OP_67(0, 7500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_7F0C)

    def lambda_7F24():
        OP_6C(55000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_7F24)
    WaitChrThread(0x39, 0x0)
    Sleep(500)

    NpcTalk(    #204
        0x17,
        "Unkempt Man",
        (
            "#143FG-Give that back!\x02\x03",

            "If that gets broken, there's no way I can replace\x01",
            "it with my joke of a wage!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 37)
    SetChrSubChip(0x18, 0)
    Sleep(250)

    NpcTalk(    #205
        0x18,
        "Freckled Girl",
        (
            "#1661FI won't break it! Honestly!\x02\x03",

            "#1662FWow... You can see things that are really\x01",
            "far away so well!\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x17, 3)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    NpcTalk(    #206
        0x17,
        "Unkempt Man",
        "#144F#3SS-Stooooooooop!\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x3E8)
    CloseMessageWindow()
    Sleep(1000)
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    Sleep(250)
    OP_4B(0x17, 3)
    Jump("loc_89EE")

    label("loc_812C")


    def lambda_8132():
        OP_6D(74200, 500, 45620, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_8132)

    def lambda_814A():
        OP_67(0, 7500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_814A)

    def lambda_8162():
        OP_6C(55000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_8162)
    WaitChrThread(0x39, 0x0)
    Sleep(500)

    NpcTalk(    #207
        0x17,
        "Unkempt Man",
        (
            "#142F#2PUgh... Of all the times to run out of \x01",
            "photo-quartz...\x02\x03",

            "I guess I'll have to get these developed first.\x02\x03",

            "#145FThis manuscript needs to be finished by two\x01",
            "or I'm never gonna be done in time.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_8268"),
        (0, "loc_8297"),
        (SWITCH_DEFAULT, "loc_82C6"),
    )


    label("loc_8268")

    SetChrPos(0x18, 70400, 1250, 51500, 180)

    def lambda_827F():
        OP_8E(0xFE, 0x1142C, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_827F)
    Jump("loc_82C6")

    label("loc_8297")

    SetChrPos(0x18, 70400, 1250, 37500, 0)

    def lambda_82AE():
        OP_8E(0xFE, 0x1142C, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_82AE)
    Jump("loc_82C6")

    label("loc_82C6")

    WaitChrThread(0x18, 0x1)
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #208
        0x18,
        "Freckled Girl",
        "#1662FHmm? What's up with him?\x02",
    )

    CloseMessageWindow()

    def lambda_832B():
        OP_8E(0xFE, 0x11D14, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_832B)
    WaitChrThread(0x18, 0x1)

    def lambda_834B():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_834B)

    NpcTalk(    #209
        0x17,
        "Unkempt Man",
        (
            "#143F#2P#3SH-Hey there!#2S\x02\x03",

            "What are you doing?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_22(0x124, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    SetChrChipByIndex(0x17, 22)
    SetChrSubChip(0x17, 0)
    SetChrPos(0x17, 73960, 500, 45140, 270)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #210
        (
            "\x07\x05The girl forcibly took the camera from the man,\x01",
            "exposing the photo-quartz inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_8463():
        OP_8F(0xFE, 0x119CC, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8463)
    WaitChrThread(0x18, 0x1)

    def lambda_8483():
        OP_96(0xFE, 0x11E7C, 0xFA, 0xB054, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8483)
    WaitChrThread(0x17, 0x1)
    SetChrChipByIndex(0x17, 2)
    SetChrSubChip(0x17, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x17, 270, 0)
    ClearChrFlags(0x17, 0x4)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #211
        0x17,
        "Unkempt Man",
        (
            "#143F#3S#2PAaaaaah!#2S\x02\x03",

            "#144FWhat the hell do you think you're doing?!\x02\x03",

            "Those are useless if light shines directly\x01",
            "on them!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x1F4)
    CloseMessageWindow()
    CloseMessageWindow()

    NpcTalk(    #212
        0x18,
        "Freckled Girl",
        "#1662FHuh? Reeeally?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #213
        0x17,
        "Unkempt Man",
        "#144F#2PYes, really! Shut the cover! NOW!\x02",
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #214
        0x17,
        "Unkempt Man",
        (
            "#145F#2PD-Damn... That gave me a scare...\x02\x03",

            "Do you have any idea how much a set\x01",
            "of photo-quartz costs?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #215
        0x18,
        "Freckled Girl",
        "#1660FOh, I know!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 270, 500)
    Sleep(300)

    NpcTalk(    #216
        0x18,
        "Freckled Girl",
        "#1661FHe looks just like the dog that lives near me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #217
        0x17,
        "Unkempt Man",
        "#143F#2PWhat are you doing with that thing?!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_871F():

        label("loc_871F")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_871F")

    QueueWorkItem2(0x17, 2, lambda_871F)

    def lambda_8730():
        OP_8F(0xFE, 0x11A58, 0xFA, 0xAD5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8730)
    WaitChrThread(0x17, 0x1)

    def lambda_8750():
        OP_8F(0xFE, 0x115E4, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8750)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 90, 500)
    Sleep(300)

    NpcTalk(    #218
        0x17,
        "Unkempt Man",
        "#144F#3PDon't you dare damage it! It's not mine!\x02",
    )

    CloseMessageWindow()

    def lambda_87BE():
        OP_8F(0xFE, 0x11AD0, 0xFA, 0xB48C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_87BE)
    WaitChrThread(0x17, 0x1)

    def lambda_87DE():
        OP_8F(0xFE, 0x11E7C, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_87DE)
    WaitChrThread(0x17, 0x1)

    def lambda_87FE():
        OP_8E(0xFE, 0x119CC, 0xFA, 0xAB2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_87FE)
    WaitChrThread(0x18, 0x1)

    def lambda_881E():
        OP_8F(0xFE, 0x11E18, 0xFA, 0xAB2C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_881E)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 270, 500)
    Sleep(300)

    NpcTalk(    #219
        0x17,
        "Unkempt Man",
        (
            "#144F#2PThat's the editor-in-chief's REALLY EXPENSIVE\x01",
            "prized orbal camera!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #220
        0x18,
        "Freckled Girl",
        (
            "#1661FHow do you use it?\x02\x03",

            "#1662F*click* Oooh, it moved!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 37)
    SetChrSubChip(0x18, 0)
    Sleep(250)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    NpcTalk(    #221
        0x17,
        "Unkempt Man",
        "#144F#2P#3SStooooooooop!\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    Sleep(250)
    OP_43(0x17, 0x3, 0x0, 0x36)
    Sleep(2000)

    label("loc_89EE")

    Return()

    # Function_53_7EE7 end

    def Function_54_89EF(): pass

    label("Function_54_89EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B1F")

    def lambda_89FE():
        OP_8E(0xFE, 0x119CC, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_89FE)
    WaitChrThread(0x18, 0x1)

    def lambda_8A1E():
        OP_8F(0xFE, 0x11E7C, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8A1E)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 270, 500)
    Sleep(1000)

    def lambda_8A4A():
        OP_8F(0xFE, 0x11AD0, 0xFA, 0xB48C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8A4A)
    WaitChrThread(0x17, 0x1)

    def lambda_8A6A():
        OP_8F(0xFE, 0x115E4, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8A6A)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 90, 500)
    Sleep(1000)

    def lambda_8A96():
        OP_8F(0xFE, 0x11A58, 0xFA, 0xAD5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8A96)
    WaitChrThread(0x17, 0x1)

    def lambda_8AB6():
        OP_8F(0xFE, 0x11E7C, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8AB6)
    WaitChrThread(0x17, 0x1)

    def lambda_8AD6():
        OP_8E(0xFE, 0x119CC, 0xFA, 0xAB2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8AD6)
    WaitChrThread(0x18, 0x1)

    def lambda_8AF6():
        OP_8F(0xFE, 0x11E18, 0xFA, 0xAB2C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8AF6)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 270, 500)
    Sleep(1000)
    Jump("Function_54_89EF")

    label("loc_8B1F")

    Return()

    # Function_54_89EF end

    def Function_55_8B20(): pass

    label("Function_55_8B20")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8B2C")
    Jump("loc_8DB5")

    label("loc_8B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8BDF")
    TurnDirection(0x151, 0x103, 400)
    Sleep(200)

    ChrTalk(    #222
        0x151,
        (
            "#1653FUmm... Miss Scherazard...\x02\x03",

            "Have you never flown on an airship before?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(200)

    ChrTalk(    #223
        0x103,
        "#1644FO-Of course I have! What do you take me for?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C82")

    label("loc_8BDF")

    TurnDirection(0x151, 0x103, 400)
    Sleep(200)

    ChrTalk(    #224
        0x151,
        (
            "#1653FUmm... Miss Scherazard...\x02\x03",

            "This way leads to the landing port, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(200)

    ChrTalk(    #225
        0x103,
        "#1647FI know that! Do I look that dumb to you?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8C82")

    Jump("loc_8DB5")

    label("loc_8C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_8DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8D12")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #226
        0x151,
        (
            "#1653FUmm... Miss Scherazard...\x02\x03",

            "Do you want to board an airliner or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x103,
        "#1648F...Why would I?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DB5")

    label("loc_8D12")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #228
        0x151,
        (
            "#1653FUmm... Miss Scherazard...\x02\x03",

            "This way leads to the landing port, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #229
        0x103,
        "#1642FI know that! Do I look that dumb to you?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8DB5")

    OP_90(0xEE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_55_8B20 end

    def Function_56_8DD1(): pass

    label("Function_56_8DD1")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8DDD")
    Jump("loc_913B")

    label("loc_8DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8EDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8E27")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #230
        0x151,
        "#1650FLet's go through the south block.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EDB")

    label("loc_8E27")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #231
        0x151,
        (
            "#1650FWe should turn around and go through\x01",
            "the south block.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #232
        0x103,
        "#1642FWe're going round the long way, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x151,
        "#1651FWe sure are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x103,
        "#1646F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8EDB")

    Jump("loc_913B")

    label("loc_8EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8F5A")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #235
        0x151,
        (
            "#1653FThe ice cream stall isn't this way.\x02\x03",

            "Let's turn around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x103,
        "#1642F(I know that...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FE2")

    label("loc_8F5A")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #237
        0x151,
        (
            "#1653FHmm? Where are you going, \x01",
            "Miss Scherazard?\x02\x03",

            "This isn't the right way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #238
        0x103,
        "#1646FI know, I know.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8FE2")

    Jump("loc_913B")

    label("loc_8FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_913B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_906D")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #239
        0x151,
        (
            "#1653FWhere are you going, Miss Scherazard?\x01",
            "We're in the right block now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x103,
        "#1642FI-I know that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_913B")

    label("loc_906D")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #241
        0x151,
        (
            "#1653FHmm? Where are you going, Miss Scherazard?\x02\x03",

            "We're in the right block now. We don't need to\x01",
            "go to any others.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #242
        0x103,
        "#1646F...I-I know that! I just got mixed up a little.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_913B")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_8DD1 end

    def Function_57_9157(): pass

    label("Function_57_9157")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9163")
    Jump("loc_9279")

    label("loc_9163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_916D")
    Jump("loc_9279")

    label("loc_916D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_9272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_91FA")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #243
        0x151,
        (
            "#1653FThe ice cream stall isn't this way.\x02\x03",

            "Let's turn around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x103,
        "#1647F(Who died and made you the boss?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_926F")

    label("loc_91FA")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #245
        0x151,
        (
            "#1653FThe ice cream stall isn't this way.\x02\x03",

            "Let's turn around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #246
        0x103,
        "#1646FFine, fine.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_926F")

    Jump("loc_9279")

    label("loc_9272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9279")

    label("loc_9279")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_57_9157 end

    def Function_58_9295(): pass

    label("Function_58_9295")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_92A1")
    Jump("loc_92E1")

    label("loc_92A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_92B8")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_92E1")

    label("loc_92B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_92DA")
    Call(0, 62)
    OP_90(0xEE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    Jump("loc_92E1")

    label("loc_92DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_92E1")

    label("loc_92E1")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_58_9295 end

    def Function_59_92E9(): pass

    label("Function_59_92E9")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_92F5")
    Jump("loc_9335")

    label("loc_92F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_930C")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_9335")

    label("loc_930C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_932E")
    Call(0, 62)
    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Jump("loc_9335")

    label("loc_932E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9335")

    label("loc_9335")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_59_92E9 end

    def Function_60_933D(): pass

    label("Function_60_933D")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9349")
    Jump("loc_9389")

    label("loc_9349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_9360")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_9389")

    label("loc_9360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_9382")
    Call(0, 62)
    OP_90(0xEE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    Jump("loc_9389")

    label("loc_9382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9389")

    label("loc_9389")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_60_933D end

    def Function_61_9391(): pass

    label("Function_61_9391")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_939D")
    Jump("loc_93DD")

    label("loc_939D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_93B4")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_93DD")

    label("loc_93B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_93D6")
    Call(0, 62)
    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    Jump("loc_93DD")

    label("loc_93D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_93DD")

    label("loc_93DD")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_61_9391 end

    def Function_62_93E5(): pass

    label("Function_62_93E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_93EF")
    Jump("loc_9528")

    label("loc_93EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_9410")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9528")

    label("loc_9410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_9521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9499")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #247
        0x151,
        (
            "#1653FOh, I'm sorry! Did you have something that\x01",
            "you needed to buy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #248
        0x103,
        "#1646FNot really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_951E")

    label("loc_9499")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #249
        0x151,
        (
            "#1650FI've bought everything I need in the\x01",
            "department store now.\x02\x03",

            "Next is the ice cream stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x103,
        "#1645FUgh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_951E")

    Jump("loc_9528")

    label("loc_9521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9528")

    label("loc_9528")

    Return()

    # Function_62_93E5 end

    def Function_63_9529(): pass

    label("Function_63_9529")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(70000, 250, 45560, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x10E, 30)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, 70000, 750, 49840, 180)
    ClearChrFlags(0x37, 0x80)
    SetChrPos(0x37, 70000, 250, 48340, 180)
    OP_43(0x37, 0x3, 0x0, 0x41)
    Sleep(100)
    OP_43(0x10E, 0x3, 0x0, 0x42)
    FadeToBright(2000, 0)
    OP_6B(2960, 2000)
    OP_0D()
    WaitChrThread(0x37, 0x3)
    Sleep(500)

    ChrTalk(    #251
        0x37,
        (
            "#276FWell, this area seems to be empty...\x02\x03",

            "#277FWill this be far enough, do you think?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x3)

    NpcTalk(    #252
        0x10E,
        "Sister Julia",
        "It should be...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10E, 270, 400)
    Sleep(300)
    OP_20(0xBB8)

    def lambda_966D():
        OP_6D(68460, 250, 46040, 3000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_966D)

    def lambda_9685():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9685)

    def lambda_9695():

        label("loc_9695")

        TurnDirection(0xFE, 0x10E, 500)
        OP_48()
        Jump("loc_9695")

    QueueWorkItem2(0x37, 2, lambda_9695)

    def lambda_96A6():
        OP_8E(0xFE, 0x104BE, 0xFA, 0xB1BC, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_96A6)
    WaitChrThread(0x10E, 0x1)
    Sleep(500)
    Fade(500)
    OP_22(0xCB, 0x0, 0x50)
    SetChrChipByIndex(0x10E, 31)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #253
        0x10E,
        "Captain Schwarz",
        "#465F#5PWhew...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10E, 90, 500)
    Sleep(200)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 32)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, 66200, 250, 45500, 90)
    SetChrFlags(0x10E, 0x4)
    OP_0D()
    Sleep(300)
    OP_44(0x37, 0x2)
    Sleep(300)

    NpcTalk(    #254
        0x10E,
        "Captain Schwarz",
        "#464F#5PI can't apologize enough for this, Major.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x37,
        "#270F#12POh, think nothing of it.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x1)

    def lambda_97C0():
        OP_6D(65620, 500, 46040, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_97C0)

    def lambda_97D8():
        OP_67(0, 6460, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_97D8)

    def lambda_97F0():
        OP_8E(0xFE, 0x104BE, 0xFA, 0xAD70, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_97F0)
    WaitChrThread(0x37, 0x1)
    Sleep(300)
    OP_8C(0x37, 90, 500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x37, 34)
    SetChrSubChip(0x37, 0)
    SetChrPos(0x37, 66200, 500, 44400, 90)
    SetChrFlags(0x37, 0x4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #256
        0x37,
        (
            "#277F#6PI'm used to having to run around without\x01",
            "being discovered.\x02\x03",

            "#272FUsually because Olivier's caused some\x01",
            "kind of predicament...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #257
        0x10E,
        "Captain Schwarz",
        (
            "#460F#5PHaha. I can see that.\x02\x03",

            "#465FI'm still ashamed of what happened, though.\x02\x03",

            "#464FI let a simple commotion like that ruin my\x01",
            "plans to go outside the city for my day off...\x02\x03",

            "I wasn't able to calm the situation at all.\x01",
            "I wouldn't even have been able to leave\x01",
            "the castle without resorting to a disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x37,
        (
            "#270F#6P...\x02\x03",

            "#272FI'm not sure you've any reason to be blaming\x01",
            "yourself here, Captain.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #259
        0x10E,
        "Captain Schwarz",
        (
            "#464F#5PI'm afraid I must disagree.\x02\x03",

            "As a member of the Royal Guard, I am utterly\x01",
            "useless...and this isn't the first time that I've\x01",
            "felt that way.\x02\x03",

            "#465FDuring the coup d'etat, I was powerless.\x02\x03",

            "I should have been able to protect Her Highness,\x01",
            "and yet she ended up being captured and placed\x01",
            "in danger.\x02\x03",

            "The same was true when Grancel was attacked\x01",
            "by Ouroboros, too.\x02\x03",

            "Not only could I not protect Her Majesty from \x01",
            "being endangered by them, I wasn't even able\x01",
            "to be anywhere near her.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #260
        0x10E,
        "Captain Schwarz",
        (
            "#464F#5PI, of all people, should have been right by her\x01",
            "side in her hour of need. How dare I learn of\x01",
            "what happened only after the fact?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D2F():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_9D2F)
    Sleep(1000)

    NpcTalk(    #261
        0x10E,
        "Captain Schwarz",
        "#464F#5PI'm not fit to even serve them! I... I...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x37, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x37)
    Sleep(500)
    SetChrSubChip(0x37, 1)
    Sleep(500)

    ChrTalk(    #262
        0x37,
        (
            "#277F#6PWhile I can certainly understand your frustrations,\x01",
            "they were both safe, were they not?\x02\x03",

            "Surely that is what counts above all.\x02\x03",

            "#278FMuch as we may wish to be, no human is omnipotent.\x01",
            "Neither of us are any exception to that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #263
        0x10E,
        "Captain Schwarz",
        (
            "#465F#5PI understand that...or at least I want to believe\x01",
            "that I do.\x02\x03",

            "#464FBut to make matters worse, I now find out there\x01",
            "are magazine articles about me, making me out\x01",
            "to be some kind of great hero.\x02\x03",

            "There's even talk of me being promoted.\x02\x03",

            "I don't even feel like I've done my job in a way\x01",
            "that's worthy of praise, never mind anything to\x01",
            "deserve being given a higher position...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x10E, 66200, 250, 45600, 90)
    SetChrPos(0x37, 66200, 500, 44500, 90)
    OP_6D(64819, 250, 45310, 0)
    OP_67(0, 6430, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(269000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #264
        0x10E,
        "Captain Schwarz",
        (
            "#465F#12P...No, none of that is what bothers me most.\x02\x03",

            "If people want to give me greater praise than\x01",
            "I deserve, let them.\x02\x03",

            "And receiving a promotion isn't in itself a cause\x01",
            "to be unhappy--more the opposite. On paper,\x01",
            "at least.\x02\x03",

            "#464FBut in reality, it will result in me becoming\x01",
            "busier because of my new duties.\x02\x03",

            "Which will result in me ending up even further\x01",
            "away from Her Highness than I am now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x37,
        "#272F#5P...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #266
        0x10E,
        "Captain Schwarz",
        (
            "#464F#12P...I'm a little envious of you, to tell the truth,\x01",
            "Major.\x02\x03",

            "#465FYou've always been able to go and escort\x01",
            "Prince Olivert like it's the most natural\x01",
            "thing in the world.\x02\x03",

            "Maybe you weren't always by his side, but\x01",
            "you were when he needed you the most.\x02\x03",

            "You did more than escort him, too; you were\x01",
            "able to help and aid him in ways beyond the\x01",
            "call of duty.\x02\x03",

            "#464F...By comparison, I can't seem to be able to\x01",
            "help Her Highness at all. I can't even lend\x01",
            "her an ear when she is plagued with worry.\x02\x03",

            "When she was agonizing over whether\x01",
            "to assume her position as crown princess,\x01",
            "I couldn't do a single thing for her...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x10E, 66200, 250, 45500, 90)
    SetChrPos(0x37, 66200, 500, 44400, 90)
    OP_6D(65620, 500, 46040, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x37, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x37)
    Sleep(500)

    ChrTalk(    #267
        0x37,
        (
            "#272F#6PI feel somewhat reluctant to give my opinion\x01",
            "here, as I can hardly pretend to be well versed\x01",
            "in your situation...\x02\x03",

            "#270F...but from where I stand, your position seems\x01",
            "the more fortunate one.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    SetChrSubChip(0x10E, 2)

    NpcTalk(    #268
        0x10E,
        "Captain Schwarz",
        (
            "#463F#11PHow so?\x02\x03",

            "What exactly do you mean, Major?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x37,
        (
            "#272F#6PI didn't mean to offend you, so I apologize\x01",
            "if I did...\x02\x03",

            "#277F...but protecting that fool is a task that was\x01",
            "thrust upon me the moment I was born.\x02\x03",

            "Between us, I find myself envious of your\x01",
            "natural loyalty to the ones you serve.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #270
        0x10E,
        "Captain Schwarz",
        (
            "#462F#11PThe moment you were born?\x02\x03",

            "Oh, right. You're a Vander...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x37,
        (
            "#277F#6PAnd we're a military family who traditionally\x01",
            "serves the Imperial family, yes.\x02\x03",

            "#278FMy luck for anything less than a hectic life\x01",
            "ran out the second I was given it, I fear.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #272
        0x10E,
        "Captain Schwarz",
        (
            "#461F#11PHaha... That's certainly a great responsibility\x01",
            "to be destined to fulfill.\x02\x03",

            "#460FEspecially when you're chosen to protect Prince\x01",
            "Olivert of all people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x37,
        (
            "#274F#6PQuite so.\x02\x03",

            "#272F#6P...\x02\x03",
        )
    )

    CloseMessageWindow()
    OP_62(0x37, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x37)
    Sleep(500)
    SetChrSubChip(0x37, 0)
    Sleep(500)

    ChrTalk(    #274
        0x37,
        (
            "#277F#6PStill, my point stands. I do believe that it's a \x01",
            "happy, fortunate thing to be able to serve and\x01",
            "devote yourself to those you genuinely care for.\x02\x03",

            "I may hardly be an expert on the subject seeing\x01",
            "as Her Highness is much less of a handful, but\x01",
            "am I wrong?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10E, 0)
    Sleep(800)

    NpcTalk(    #275
        0x10E,
        "Captain Schwarz",
        (
            "#465F#5P...No. I see your point.\x02\x03",

            "Perhaps I should see being able to sit and worry\x01",
            "about something like this as a luxury.\x02\x03",

            "#464FAlthough whether someone who isn't able to defend\x01",
            "Her Highness can really be called a member of the\x01",
            "Royal Guard is another issue entirely...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)

    ChrTalk(    #276
        0x37,
        (
            "#278F#6P...Captain.\x02\x03",

            "If you'd like, I would be happy to teach you\x01",
            "a good way to clear your head.\x02",
        )
    )

    OP_63(0x10E)
    Sleep(500)
    CloseMessageWindow()
    OP_59()
    SetChrPos(0x10E, 66200, 250, 45500, 68)

    def lambda_AC78():
        OP_6D(65730, 250, 45870, 1200)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_AC78)

    def lambda_AC90():
        OP_6C(293000, 1200)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_AC90)
    Fade(500)
    SetChrChipByIndex(0x37, 33)
    SetChrSubChip(0x37, 0)
    SetChrPos(0x37, 66750, 250, 44400, 80)
    ClearChrFlags(0x37, 0x4)
    OP_0D()

    def lambda_ACC6():
        OP_8F(0xFE, 0x10B94, 0xFA, 0xB02C, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_ACC6)
    Sleep(800)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    WaitChrThread(0x37, 0x1)
    Fade(500)
    SetChrChipByIndex(0x10E, 31)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, 66750, 250, 45500, 80)
    ClearChrFlags(0x10E, 0x4)
    OP_0D()
    TurnDirection(0x10E, 0x37, 400)
    Sleep(500)

    NpcTalk(    #277
        0x10E,
        "Captain Schwarz",
        "#463F#5PTo clear my head, you say?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x37, 0x10E, 400)
    Sleep(500)

    ChrTalk(    #278
        0x37,
        (
            "#278F#6PIndeed. Still...\x02\x03",

            "#277F...I would like you to keep this off the record.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ADCD():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_ADCD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_63_9529 end

    def Function_64_ADFA(): pass

    label("Function_64_ADFA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #279
        (
            "\x07\x05'The Second Orbally-Powered Clock'\x01",
            "Made in year 1163 of the Septian Calendar\x01",
            "by Zeissian manufacturers.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_64_ADFA end

    def Function_65_AE8C(): pass

    label("Function_65_AE8C")


    def lambda_AE92():
        OP_8E(0xFE, 0x11170, 0xFA, 0xAD34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_AE92)
    WaitChrThread(0x37, 0x1)
    Sleep(300)
    OP_8C(0x37, 225, 500)
    Sleep(700)
    OP_8C(0x37, 135, 500)
    Sleep(700)
    OP_8C(0x37, 180, 500)
    Sleep(300)
    Return()

    # Function_65_AE8C end

    def Function_66_AED6(): pass

    label("Function_66_AED6")


    def lambda_AEDC():
        OP_8E(0xFE, 0x11170, 0xFA, 0xB310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_AEDC)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)
    OP_8C(0x10E, 0, 600)
    Sleep(700)
    OP_8C(0x10E, 315, 500)
    Sleep(700)
    OP_8C(0x10E, 45, 500)
    Sleep(700)
    OP_8C(0x10E, 0, 500)
    Sleep(300)
    Return()

    # Function_66_AED6 end

    def Function_67_AF2C(): pass

    label("Function_67_AF2C")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #280
        "\x07\x05The gate is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_67_AF2C end

    def Function_68_AF84(): pass

    label("Function_68_AF84")

    SetPlaceName(0xBA)
    Return()

    # Function_68_AF84 end

    def Function_69_AF88(): pass

    label("Function_69_AF88")

    SetPlaceName(0xB1)
    Return()

    # Function_69_AF88 end

    def Function_70_AF8C(): pass

    label("Function_70_AF8C")

    SetPlaceName(0xBB)
    Return()

    # Function_70_AF8C end

    def Function_71_AF90(): pass

    label("Function_71_AF90")

    SetPlaceName(0xBC)
    Return()

    # Function_71_AF90 end

    def Function_72_AF94(): pass

    label("Function_72_AF94")

    SetPlaceName(0xBD)
    Return()

    # Function_72_AF94 end

    def Function_73_AF98(): pass

    label("Function_73_AF98")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_73_AF98 end

    SaveToFile()

Try(main)
