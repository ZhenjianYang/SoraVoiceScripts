from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0011   ._SN',
        MapName             = 'event',
        Location            = 'E0011.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0011_1 ._SN',
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
        'Agate',                                # 9
        'Scherazard',                           # 10
        'Olivier',                              # 11
        'Tita',                                 # 12
        'Zin',                                  # 13
        'Kloe',                                 # 14
        'ワイングラス',                         # 15
        'Captain',                              # 16
        'Pilot',                                # 17
        'Pilot',                                # 18
        'Operator',                             # 19
        'Passenger',                            # 20
        'Passenger',                            # 21
        'Passenger',                            # 22
        'Crew Mem. Nora',                       # 23
        'Rutherford',                           # 24
        'Aldan',                                # 25
        'Mirano',                               # 26
        'Simon',                                # 27
        'Hardt',                                # 28
        'Crew Mem. Alex',                       # 29
        'Zosimov',                              # 30
        'Captain Petrov',                       # 31
        'Crew Mem. Roger',                      # 32
        'Crew Mem. Quint',                      # 33
        'Passenger',                            # 34
        'Passenger',                            # 35
        'Passenger',                            # 36
        'Passenger',                            # 37
        'Passenger',                            # 38
        'Passenger',                            # 39
        'Passenger',                            # 40
        'Passenger',                            # 41
        'Father Kevin',                         # 42
        'Bloom',                                # 43
        'Kitty',                                # 44
        'Passenger',                            # 45
        'Passenger',                            # 46
        'Passenger',                            # 47
        'Passenger',                            # 48
        'Passenger',                            # 49
        'Passenger',                            # 50
        'Passenger',                            # 51
        'Passenger',                            # 52
        'Passenger',                            # 53
        'Passenger',                            # 54
        'Passenger',                            # 55
        'Jimmy',                                # 56
        'Aldan',                                # 57
        '小説',                                 # 58
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
        'ED6_DT07/CH00053 ._CH',             # 00
        'ED6_DT07/CH00023 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00073 ._CH',             # 06
        'ED6_DT07/CH00040 ._CH',             # 07
        'ED6_DT07/CH00043 ._CH',             # 08
        'ED6_DT07/CH00063 ._CH',             # 09
        'ED6_DT06/CH20134 ._CH',             # 0A
        'ED6_DT07/CH01443 ._CH',             # 0B
        'ED6_DT07/CH01453 ._CH',             # 0C
        'ED6_DT07/CH01453 ._CH',             # 0D
        'ED6_DT07/CH01453 ._CH',             # 0E
        'ED6_DT07/CH01160 ._CH',             # 0F
        'ED6_DT07/CH01163 ._CH',             # 10
        'ED6_DT07/CH01120 ._CH',             # 11
        'ED6_DT07/CH01123 ._CH',             # 12
        'ED6_DT07/CH01143 ._CH',             # 13
        'ED6_DT27/CH03003 ._CH',             # 14
        'ED6_DT07/CH01540 ._CH',             # 15
        'ED6_DT07/CH01020 ._CH',             # 16
        'ED6_DT07/CH01040 ._CH',             # 17
        'ED6_DT07/CH01233 ._CH',             # 18
        'ED6_DT07/CH01140 ._CH',             # 19
        'ED6_DT07/CH01120 ._CH',             # 1A
        'ED6_DT07/CH01290 ._CH',             # 1B
        'ED6_DT07/CH01450 ._CH',             # 1C
        'ED6_DT07/CH01443 ._CH',             # 1D
        'ED6_DT07/CH01293 ._CH',             # 1E
        'ED6_DT07/CH01293 ._CH',             # 1F
        'ED6_DT07/CH01113 ._CH',             # 20
        'ED6_DT07/CH01490 ._CH',             # 21
        'ED6_DT07/CH01170 ._CH',             # 22
        'ED6_DT07/CH01130 ._CH',             # 23
        'ED6_DT07/CH01200 ._CH',             # 24
        'ED6_DT07/CH01183 ._CH',             # 25
        'ED6_DT07/CH01463 ._CH',             # 26
        'ED6_DT07/CH01140 ._CH',             # 27
        'ED6_DT27/CH03080 ._CH',             # 28
        'ED6_DT06/CH20045 ._CH',             # 29
        'ED6_DT26/CH20241 ._CH',             # 2A
        'ED6_DT26/CH20291 ._CH',             # 2B
        'ED6_DT07/CH01010 ._CH',             # 2C
        'ED6_DT07/CH01770 ._CH',             # 2D
        'ED6_DT07/CH01460 ._CH',             # 2E
        'ED6_DT07/CH01143 ._CH',             # 2F
        'ED6_DT07/CH01153 ._CH',             # 30
        'ED6_DT07/CH01103 ._CH',             # 31
        'ED6_DT07/CH01183 ._CH',             # 32
        'ED6_DT07/CH01023 ._CH',             # 33
        'ED6_DT07/CH01470 ._CH',             # 34
        'ED6_DT07/CH00050 ._CH',             # 35
        'ED6_DT07/CH01040 ._CH',             # 36
        'ED6_DT07/CH01043 ._CH',             # 37
        'ED6_DT07/CH01213 ._CH',             # 38
        'ED6_DT07/CH01070 ._CH',             # 39
        'ED6_DT07/CH01003 ._CH',             # 3A
    )

    AddCharChipPat(
        'ED6_DT07/CH00053P._CP',             # 00
        'ED6_DT07/CH00023P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00073P._CP',             # 06
        'ED6_DT07/CH00040P._CP',             # 07
        'ED6_DT07/CH00043P._CP',             # 08
        'ED6_DT07/CH00063P._CP',             # 09
        'ED6_DT06/CH20134P._CP',             # 0A
        'ED6_DT07/CH01443P._CP',             # 0B
        'ED6_DT07/CH01453P._CP',             # 0C
        'ED6_DT07/CH01453P._CP',             # 0D
        'ED6_DT07/CH01453P._CP',             # 0E
        'ED6_DT07/CH01160P._CP',             # 0F
        'ED6_DT07/CH01163P._CP',             # 10
        'ED6_DT07/CH01120P._CP',             # 11
        'ED6_DT07/CH01123P._CP',             # 12
        'ED6_DT07/CH01143P._CP',             # 13
        'ED6_DT27/CH03003P._CP',             # 14
        'ED6_DT07/CH01540P._CP',             # 15
        'ED6_DT07/CH01020P._CP',             # 16
        'ED6_DT07/CH01040P._CP',             # 17
        'ED6_DT07/CH01233P._CP',             # 18
        'ED6_DT07/CH01140P._CP',             # 19
        'ED6_DT07/CH01120P._CP',             # 1A
        'ED6_DT07/CH01290P._CP',             # 1B
        'ED6_DT07/CH01450P._CP',             # 1C
        'ED6_DT07/CH01443P._CP',             # 1D
        'ED6_DT07/CH01293P._CP',             # 1E
        'ED6_DT07/CH01293P._CP',             # 1F
        'ED6_DT07/CH01113P._CP',             # 20
        'ED6_DT07/CH01490P._CP',             # 21
        'ED6_DT07/CH01170P._CP',             # 22
        'ED6_DT07/CH01130P._CP',             # 23
        'ED6_DT07/CH01200P._CP',             # 24
        'ED6_DT07/CH01183P._CP',             # 25
        'ED6_DT07/CH01463P._CP',             # 26
        'ED6_DT07/CH01140P._CP',             # 27
        'ED6_DT27/CH03080P._CP',             # 28
        'ED6_DT06/CH20045P._CP',             # 29
        'ED6_DT26/CH20241P._CP',             # 2A
        'ED6_DT26/CH20291P._CP',             # 2B
        'ED6_DT07/CH01010P._CP',             # 2C
        'ED6_DT07/CH01770P._CP',             # 2D
        'ED6_DT07/CH01460P._CP',             # 2E
        'ED6_DT07/CH01143P._CP',             # 2F
        'ED6_DT07/CH01153P._CP',             # 30
        'ED6_DT07/CH01103P._CP',             # 31
        'ED6_DT07/CH01183P._CP',             # 32
        'ED6_DT07/CH01023P._CP',             # 33
        'ED6_DT07/CH01470P._CP',             # 34
        'ED6_DT07/CH00050P._CP',             # 35
        'ED6_DT07/CH01040P._CP',             # 36
        'ED6_DT07/CH01043P._CP',             # 37
        'ED6_DT07/CH01213P._CP',             # 38
        'ED6_DT07/CH01070P._CP',             # 39
        'ED6_DT07/CH01003P._CP',             # 3A
    )

    DeclNpc(
        X                   = 117300,
        Z                   = 0,
        Y                   = 1350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 117300,
        Z                   = 0,
        Y                   = 1350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 88690,
        Z                   = -1000,
        Y                   = 51250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 88530,
        Z                   = -500,
        Y                   = 51980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x191,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 116000,
        Z                   = 0,
        Y                   = 10280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 117420,
        Z                   = 80,
        Y                   = 7320,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 57210,
        Z                   = 0,
        Y                   = 1140,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 88880,
        Z                   = 100,
        Y                   = -1240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 87830,
        Z                   = 0,
        Y                   = 170,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 89360,
        Z                   = 0,
        Y                   = 8810,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 86120,
        Z                   = 0,
        Y                   = 47320,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 27850,
        Z                   = 0,
        Y                   = -8070,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 59020,
        Z                   = -530,
        Y                   = 49310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 56990,
        Z                   = -1800,
        Y                   = 51970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 59190,
        Z                   = -1950,
        Y                   = 54200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 88770,
        Z                   = 100,
        Y                   = -4910,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 115840,
        Z                   = 0,
        Y                   = -1200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 114590,
        Z                   = 100,
        Y                   = -2470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 113550,
        Z                   = 80,
        Y                   = 1410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 87890,
        Z                   = 0,
        Y                   = -1220,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 87890,
        Z                   = 0,
        Y                   = -2410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 56,
        ChipIndex           = 0x38,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 57,
        ChipIndex           = 0x39,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 58,
        ChipIndex           = 0x3A,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 116990,
        Z                   = 0,
        Y                   = 10300,
        Direction           = 56,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 57210,
        Z                   = 0,
        Y                   = 1140,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 88140,
        Z                   = -500,
        Y                   = 52020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703939,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_8C2",          # 00, 0
        "Function_1_1148",         # 01, 1
        "Function_2_11B1",         # 02, 2
        "Function_3_132E",         # 03, 3
        "Function_4_1408",         # 04, 4
        "Function_5_1653",         # 05, 5
        "Function_6_1967",         # 06, 6
        "Function_7_1E77",         # 07, 7
        "Function_8_1FC0",         # 08, 8
        "Function_9_2193",         # 09, 9
        "Function_10_2369",        # 0A, 10
        "Function_11_296F",        # 0B, 11
        "Function_12_2B57",        # 0C, 12
        "Function_13_2D3A",        # 0D, 13
        "Function_14_2EC5",        # 0E, 14
        "Function_15_2FDC",        # 0F, 15
        "Function_16_31E4",        # 10, 16
        "Function_17_3B12",        # 11, 17
        "Function_18_40B7",        # 12, 18
        "Function_19_4688",        # 13, 19
        "Function_20_4B28",        # 14, 20
        "Function_21_4E98",        # 15, 21
        "Function_22_52DE",        # 16, 22
        "Function_23_536A",        # 17, 23
        "Function_24_544F",        # 18, 24
        "Function_25_576C",        # 19, 25
        "Function_26_5A22",        # 1A, 26
        "Function_27_5C45",        # 1B, 27
        "Function_28_621A",        # 1C, 28
        "Function_29_640D",        # 1D, 29
        "Function_30_6573",        # 1E, 30
        "Function_31_677B",        # 1F, 31
        "Function_32_691F",        # 20, 32
        "Function_33_6A7E",        # 21, 33
        "Function_34_6C74",        # 22, 34
        "Function_35_6D37",        # 23, 35
        "Function_36_6E88",        # 24, 36
        "Function_37_70B8",        # 25, 37
        "Function_38_7127",        # 26, 38
        "Function_39_71D0",        # 27, 39
        "Function_40_7242",        # 28, 40
        "Function_41_73D3",        # 29, 41
        "Function_42_758B",        # 2A, 42
        "Function_43_761B",        # 2B, 43
        "Function_44_85A3",        # 2C, 44
        "Function_45_85B5",        # 2D, 45
        "Function_46_8D9C",        # 2E, 46
        "Function_47_96BB",        # 2F, 47
        "Function_48_A4F5",        # 30, 48
        "Function_49_A620",        # 31, 49
        "Function_50_A680",        # 32, 50
        "Function_51_B2B7",        # 33, 51
        "Function_52_B992",        # 34, 52
        "Function_53_C114",        # 35, 53
        "Function_54_D7CA",        # 36, 54
        "Function_55_D8D9",        # 37, 55
        "Function_56_D8F0",        # 38, 56
        "Function_57_D907",        # 39, 57
    )


    def Function_0_8C2(): pass

    label("Function_0_8C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DF")
    OP_89(0x101, 84860, 130, 5970, 0)

    label("loc_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F7")
    Event(0, 57)

    label("loc_8F7")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 91260, 0, 44910, 90)
    SetChrPos(0xD, 117350, 100, 3200, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 8)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 89280, 80, -3200, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    SetChrPos(0xC, 117350, 100, -850, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 57200, 0, -2270, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 53)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 114820, 0, 5050, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 86270, 0, 46740, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 113340, 100, 1260, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 116650, 0, 10640, 45)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 84990, 0, 9250, 180)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 84990, 0, 8270, 0)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 86180, 0, 80, 225)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 85340, 100, -1250, 0)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 117260, 100, 5450, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 88620, -1000, 52980, 0)
    Jump("loc_F0F")

    label("loc_A7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7A")
    SetChrPos(0x8, 116650, 100, 3200, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 117350, 50, 1200, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xC, 117350, 100, -850, 0)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF2")
    SetChrPos(0xD, 88410, -1000, 53020, 0)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x0, 0x0, 0x2)
    Jump("loc_B0D")

    label("loc_AF2")

    SetChrPos(0xD, 116650, 100, 5200, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 8)

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2E")
    SetChrPos(0xB, 58800, 0, -2020, 90)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_B52")

    label("loc_B2E")

    OP_44(0xB, 0x0)
    SetChrPos(0xB, 117350, 100, 5200, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 9)

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_END)), "loc_B7D")
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 117350, 80, 3100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)

    label("loc_B7D")

    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrPos(0x16, 114750, 0, 11170, 180)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 28120, 0, -8480, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 86270, 0, 46740, 180)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 117330, 100, 7280, 0)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, 86280, 0, 1960, 212)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2E, 84800, 100, 600, 0)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, 85460, 100, -3100, 0)
    ClearChrFlags(0x30, 0x80)
    SetChrPos(0x30, 89340, 150, -4890, 0)
    ClearChrFlags(0x31, 0x80)
    SetChrPos(0x31, 113350, 100, -700, 0)
    ClearChrFlags(0x32, 0x80)
    SetChrPos(0x32, 113380, 0, 0, 180)
    Jump("loc_F0F")

    label("loc_C7A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_C8A"),
        (109, "loc_C98"),
        (SWITCH_DEFAULT, "loc_CA6"),
    )


    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C95")

    label("loc_C95")

    Jump("loc_CA6")

    label("loc_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA3")

    label("loc_CA3")

    Jump("loc_CA6")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_E84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBE")
    Event(0, 57)

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CFE")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 41)
    SetChrPos(0x9, 88690, -1000, 51250, 0)
    SetChrPos(0xA, 88700, -1000, 52960, 180)
    Jump("loc_D2A")

    label("loc_CFE")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 88690, -1000, 51250, 0)
    SetChrPos(0xB, 88700, -1000, 52960, 360)

    label("loc_D2A")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 117200, 100, 1100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 1)), scpexpr(EXPR_END)), "loc_D4F")
    SetChrSubChip(0xC, 0)
    Jump("loc_D54")

    label("loc_D4F")

    SetChrSubChip(0xC, 2)

    label("loc_D54")

    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 114820, 0, 11500, 180)
    ClearChrFlags(0x37, 0x80)
    SetChrPos(0x37, 116990, 0, 10300, 56)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x38, 89290, 100, -3120, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 84670, 100, -1300, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 86270, 0, 46740, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 28120, 0, -8480, 270)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 113220, 100, 1280, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 91080, 0, 48580, 90)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 116700, 100, 5250, 0)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 88750, 100, 520, 0)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 87730, 0, 1190, 135)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x35, 85440, 100, -4860, 0)
    ClearChrFlags(0x36, 0x80)
    SetChrPos(0x36, 114160, 100, -2480, 0)
    Jump("loc_F0F")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_END)), "loc_F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9C")
    Event(0, 57)

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_EAB")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_EB0")

    label("loc_EAB")

    ClearChrFlags(0x8, 0x80)

    label("loc_EB0")

    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0xE, 5)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x39, 0x80)
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
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1E")
    Event(0, 43)
    Jump("loc_1147")

    label("loc_F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_F5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F47")
    Event(1, 16)
    Jump("loc_F57")

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F57")
    Event(1, 6)

    label("loc_F57")

    Jump("loc_1147")

    label("loc_F5A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1000")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7E")
    Event(1, 4)

    label("loc_F7E")

    Jump("loc_FFD")

    label("loc_F81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 7)), scpexpr(EXPR_END)), "loc_FA8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 0)), scpexpr(EXPR_END)), "loc_FB9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_END)), "loc_FCA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 2)), scpexpr(EXPR_END)), "loc_FDB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_END)), "loc_FEC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FFD")
    Event(1, 5)

    label("loc_FFD")

    Jump("loc_1147")

    label("loc_1000")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_103C"),
        (102, "loc_103C"),
        (103, "loc_103C"),
        (104, "loc_103C"),
        (105, "loc_103C"),
        (106, "loc_103C"),
        (107, "loc_103C"),
        (109, "loc_103C"),
        (110, "loc_103C"),
        (112, "loc_103C"),
        (113, "loc_103C"),
        (114, "loc_103C"),
        (115, "loc_103C"),
        (SWITCH_DEFAULT, "loc_1147"),
    )


    label("loc_103C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1052")
    Event(0, 49)
    Jump("loc_1147")

    label("loc_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_10CF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 3)), scpexpr(EXPR_END)), "loc_1074")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 5)), scpexpr(EXPR_END)), "loc_1085")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 7)), scpexpr(EXPR_END)), "loc_1096")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 0)), scpexpr(EXPR_END)), "loc_10A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 2)), scpexpr(EXPR_END)), "loc_10B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C9")
    Event(0, 54)

    label("loc_10C9")

    Jump("loc_1147")

    label("loc_10CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E5")
    Event(0, 44)
    Jump("loc_1147")

    label("loc_10E5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 4)), scpexpr(EXPR_END)), "loc_1100")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 5)), scpexpr(EXPR_END)), "loc_1111")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 6)), scpexpr(EXPR_END)), "loc_1122")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 7)), scpexpr(EXPR_END)), "loc_1133")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1133")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1144")
    Event(0, 48)

    label("loc_1144")

    Jump("loc_1147")

    label("loc_1147")

    Return()

    # Function_0_8C2 end

    def Function_1_1148(): pass

    label("Function_1_1148")

    OP_10(0x0, 0x0)
    OP_22(0x7A, 0x1, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_END)), "loc_115C")
    SetChrFlags(0x39, 0x80)

    label("loc_115C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1171")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B0")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1194")
    Call(0, 55)
    Jump("loc_11B0")

    label("loc_1194")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B0")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B0")
    Call(0, 56)

    label("loc_11B0")

    Return()

    # Function_1_1148 end

    def Function_2_11B1(): pass

    label("Function_2_11B1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D6")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1318")

    label("loc_11D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EF")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1318")

    label("loc_11EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1208")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1318")

    label("loc_1208")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1221")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1318")

    label("loc_1221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1318")

    label("loc_123A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1253")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1318")

    label("loc_1253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1318")

    label("loc_126C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1285")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1318")

    label("loc_1285")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1318")

    label("loc_129E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B7")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1318")

    label("loc_12B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D0")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1318")

    label("loc_12D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E9")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1318")

    label("loc_12E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1302")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1318")

    label("loc_1302")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1318")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_132D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1318")

    label("loc_132D")

    Return()

    # Function_2_11B1 end

    def Function_3_132E(): pass

    label("Function_3_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_1407")

    label("loc_1335")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1407")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_136B")
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Jump("loc_1384")

    label("loc_136B")

    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 7)), scpexpr(EXPR_END)), "loc_1391")
    OP_A3(0x1F)
    Jump("loc_13CD")

    label("loc_1391")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13CD")
    Sleep(80)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    OP_A2(0x1F)

    label("loc_13CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13F0")
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_1404")

    label("loc_13F0")

    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)

    label("loc_1404")

    Jump("loc_1335")

    label("loc_1407")

    Return()

    # Function_3_132E end

    def Function_4_1408(): pass

    label("Function_4_1408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_14F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141E")
    Call(1, 7)
    Jump("loc_14F0")

    label("loc_141E")

    TalkBegin(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x8,
        (
            "#552FLemme just say this: I'm only heading back\x01",
            "to Ravennue once we're settled with the job.\x02\x03",

            "Don't think you're just gonna drag me\x01",
            "out there or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1007FOh, you jerkface.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    TalkEnd(0x8)

    label("loc_14F0")

    Jump("loc_1652")

    label("loc_14F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1506")
    Call(1, 0)
    Jump("loc_1652")

    label("loc_1506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_164E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 3)), scpexpr(EXPR_END)), "loc_1647")
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1539")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1554")

    label("loc_1539")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154F")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1554")

    label("loc_154F")

    SetChrSubChip(0xFE, 1)

    label("loc_1554")

    OP_8C(0x8, 360, 0)
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #2
        0x8,
        (
            "#555FSomethin' with the army, huh?\x02\x03",

            "If they're callin' us out to the capital,\x01",
            "then it's gotta be something they don't\x01",
            "want gettin' out.\x02\x03",

            "We gotta keep an eye out for the society,\x01",
            "too. We'd better keep our guard up.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Jump("loc_164B")

    label("loc_1647")

    Call(0, 50)

    label("loc_164B")

    Jump("loc_1652")

    label("loc_164E")

    Call(0, 45)

    label("loc_1652")

    Return()

    # Function_4_1408 end

    def Function_5_1653(): pass

    label("Function_5_1653")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1802")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16EF")
    Jump("loc_1731")

    label("loc_16EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_170B")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1731")

    label("loc_170B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1727")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1731")

    label("loc_1727")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1731")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #3
        0x9,
        (
            "#027FWe'll have to pass through Rolent\x01",
            "before we reach Bose, so this'll be\x01",
            "a bit of a trip.\x02\x03",

            "Go ahead and walk off some of that\x01",
            "nervous energy if you want.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Jump("loc_1966")

    label("loc_1802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_1962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 7)), scpexpr(EXPR_END)), "loc_195B")
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1835")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1850")

    label("loc_1835")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_184B")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1850")

    label("loc_184B")

    SetChrSubChip(0xFE, 1)

    label("loc_1850")

    OP_8C(0x9, 360, 0)
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #4
        0x9,
        (
            "#522FA direct request from the army, huh?\x02\x03",

            "If they're calling us to the capital,\x01",
            "it must be a matter they don't want\x01",
            "leaking out under any circumstance.\x02\x03",

            "#022FWe have the society to worry about,\x01",
            "too, so we should be on guard for\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Jump("loc_195F")

    label("loc_195B")

    Call(0, 52)

    label("loc_195F")

    Jump("loc_1966")

    label("loc_1962")

    Call(0, 46)

    label("loc_1966")

    Return()

    # Function_5_1653 end

    def Function_6_1967(): pass

    label("Function_6_1967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_1B2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197D")
    Call(1, 10)
    Jump("loc_1B28")

    label("loc_197D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1990")
    Call(1, 11)
    Jump("loc_1B28")

    label("loc_1990")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A20")
    Jump("loc_1A62")

    label("loc_1A20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A3C")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A62")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A58")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A62")

    label("loc_1A58")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A62")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #5
        0xA,
        (
            "#030FSpeaking of Bose, I remember that\x01",
            "lovely mayor and her handmaiden\x01",
            "with the cool gaze.\x02\x03",

            "#031FAh, I thrill at the thought of meeting\x01",
            "them again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)

    label("loc_1B28")

    Jump("loc_1E76")

    label("loc_1B2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 3)), scpexpr(EXPR_END)), "loc_1B42")
    Call(1, 4)

    label("loc_1B42")

    Jump("loc_1E76")

    label("loc_1B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_1E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 7)), scpexpr(EXPR_END)), "loc_1E6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D6B")
    TalkBegin(0xA)
    OP_43(0xA, 0x0, 0x0, 0x3)
    OP_A2(0x0)

    ChrTalk(    #6
        0xA,
        (
            "#032FIn truth, Schera I do not mind sharing a drink\x01",
            "with.\x02\x03",

            "She may drink endlessly, but at least her\x01",
            "face reddens and the liquor begins to tell on\x01",
            "her demeanor.\x02\x03",

            "#034FBut, Aina... No matter how much Aina drinks,\x01",
            "she remains as sober as a statue.\x02\x03",

            "And when such a seemingly-sober individual\x01",
            "pours the libations, one can hardly judge his\x01",
            "own intake with any degree of accuracy.\x02\x03",

            "#037FHahaha... Heheheh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1007F(Oooookay... I probably shouldn't encourage\x01",
            "Olivier any more on THIS train of thought...)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Jump("loc_1E68")

    label("loc_1D6B")

    TalkBegin(0xA)
    OP_43(0xA, 0x0, 0x0, 0x3)

    ChrTalk(    #8
        0xA,
        (
            "#034FAina... No matter how much she drinks,\x01",
            "she remains as sober as a statue.\x02\x03",

            "And when such a seemingly-sober individual\x01",
            "pours the libations, one can hardly judge his\x01",
            "own intake with any degree of accuracy.\x02\x03",

            "#037FHahaha... Heheheh...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_1E68")

    Jump("loc_1E6F")

    label("loc_1E6B")

    Call(0, 52)

    label("loc_1E6F")

    Jump("loc_1E76")

    label("loc_1E72")

    Call(0, 47)

    label("loc_1E76")

    Return()

    # Function_6_1967 end

    def Function_7_1E77(): pass

    label("Function_7_1E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_1F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8D")
    Call(1, 8)
    Jump("loc_1EFF")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9C")
    Call(1, 9)
    Jump("loc_1EFF")

    label("loc_1E9C")

    TalkBegin(0xB)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #9
        0xB,
        (
            "#060FMischa, huh...?\x02\x03",

            "#061FHeehee! I hope I can be her\x01",
            "friend if we meet!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    OP_8C(0xFE, 90, 400)

    label("loc_1EFF")

    Jump("loc_1FBF")

    label("loc_1F02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F15")
    Call(1, 3)
    Jump("loc_1FBF")

    label("loc_1F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 3)), scpexpr(EXPR_END)), "loc_1FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 4)), scpexpr(EXPR_END)), "loc_1FB4")
    TalkBegin(0xB)

    ChrTalk(    #10
        0xB,
        (
            "#061FThe last time I came to the capital,\x01",
            "I saw the Arseille! It's really, really\x01",
            "pretty!\x02\x03",

            "Heehee! I wonder if we'll see it again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Jump("loc_1FB8")

    label("loc_1FB4")

    Call(0, 51)

    label("loc_1FB8")

    Jump("loc_1FBF")

    label("loc_1FBB")

    Call(0, 50)

    label("loc_1FBF")

    Return()

    # Function_7_1E77 end

    def Function_8_1FC0(): pass

    label("Function_8_1FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_217B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD6")
    Call(1, 14)
    Jump("loc_2178")

    label("loc_1FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FE9")
    Call(1, 15)
    Jump("loc_2178")

    label("loc_1FE9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2079")
    Jump("loc_20BB")

    label("loc_2079")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2095")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20BB")

    label("loc_2095")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20B1")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20BB")

    label("loc_20B1")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20BB")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #11
        0xC,
        (
            "#070FUp next is Bose, the closest area to the\x01",
            "Empire in Liberl, eh?\x02\x03",

            "I'd like to get a look at the famous\x01",
            "Haken Gate some time, if we can.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)

    label("loc_2178")

    Jump("loc_2192")

    label("loc_217B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218E")
    Call(1, 1)
    Jump("loc_2192")

    label("loc_218E")

    Call(0, 53)

    label("loc_2192")

    Return()

    # Function_8_1FC0 end

    def Function_9_2193(): pass

    label("Function_9_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_2364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A9")
    Call(1, 12)
    Jump("loc_2361")

    label("loc_21A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21BC")
    Call(1, 13)
    Jump("loc_2361")

    label("loc_21BC")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_224C")
    Jump("loc_228E")

    label("loc_224C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2268")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_228E")

    label("loc_2268")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2284")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_228E")

    label("loc_2284")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_228E")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #12
        0xD,
        (
            "#048F...It's been ages since I've\x01",
            "been to Bose, come to think of it.\x02\x03",

            "I think the last time was when Jill took\x01",
            "me on a little shopping spree at the\x01",
            "Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)

    label("loc_2361")

    Jump("loc_2368")

    label("loc_2364")

    Call(1, 2)

    label("loc_2368")

    Return()

    # Function_9_2193 end

    def Function_10_2369(): pass

    label("Function_10_2369")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2422")

    ChrTalk(    #13
        0xFE,
        (
            "To your right, currently, you can view\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "At the end of that valley are the peaks\x01",
            "which mark part of our border with the\x01",
            "Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E3")

    label("loc_2422")


    ChrTalk(    #15
        0xFE,
        (
            "Ah, hello, miss.\x01",
            "Thank you for your patronage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "To your right, currently, you can view\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "The fog around Rolent has cleared, but\x01",
            "that area remains foggy year-round.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_24E3")

    Jump("loc_296B")

    label("loc_24E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2687")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2594")

    ChrTalk(    #18
        0xFE,
        (
            "Our ship is currently in the air above\x01",
            "Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Please enjoy your travels in the sky with us\x01",
            "until our next stop at the Rolent Landing Port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2684")

    label("loc_2594")


    ChrTalk(    #20
        0xFE,
        "Ladies and gentlemen, your attention please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Visible to our right is the kingdom's\x01",
            "largest continuous forest, Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It remains home to a large number of\x01",
            "woodsmen, and is the source of 70%\x01",
            "of the lumber used in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2684")

    Jump("loc_296B")

    label("loc_2687")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2846")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_271F")

    ChrTalk(    #23
        0xFE,
        (
            "Our vessel is currently in flight above\x01",
            "the Tratt Plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Please enjoy a relaxing journey until our\x01",
            "arrival in Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2843")

    label("loc_271F")


    ChrTalk(    #25
        0xFE,
        (
            "Currently, to your right is the front of\x01",
            "the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "It has a long and storied history, which\x01",
            "dates back to before the birth of the\x01",
            "Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "According to some theories, it's linked to\x01",
            "the ancient Zemurian civilization, but the\x01",
            "truth of the matter is unclear.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2843")

    Jump("loc_296B")

    label("loc_2846")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28BF")

    ChrTalk(    #28
        0xFE,
        (
            "Our ship is currently above the Kaldia\x01",
            "Tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "We will be arriving in Zeiss on schedule.\x02",
    )

    CloseMessageWindow()
    Jump("loc_296B")

    label("loc_28BF")


    ChrTalk(    #30
        0xFE,
        (
            "Currently to our right is the Titith Bay,\x01",
            "Liberl's gate to the great sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "While it is currently slightly cloudy,\x01",
            "you should be able to make out the\x01",
            "coastline.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_296B")

    TalkEnd(0x16)
    Return()

    # Function_10_2369 end

    def Function_11_296F(): pass

    label("Function_11_296F")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F8")

    ChrTalk(    #32
        0xFE,
        (
            "I've got a deal to make with Ambassador\x01",
            "Cochrane of Calvard, and this is the big one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "I hope it goes well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B53")

    label("loc_29F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A9F")

    ChrTalk(    #34
        0xFE,
        (
            "I haven't had a chance to rest in forever.\x01",
            "Been busy the whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Once I get back to Zeiss, I want to kick\x01",
            "back and relax a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B53")

    label("loc_2A9F")


    ChrTalk(    #36
        0xFE,
        "I'm heading home to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I haven't had a chance to rest in a while.\x01",
            "Been workin' all the time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Once I get home, I just want to kick back\x01",
            "and relax for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2B53")

    TalkEnd(0x17)
    Return()

    # Function_11_296F end

    def Function_12_2B57(): pass

    label("Function_12_2B57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BCF")

    ChrTalk(    #39
        0xFE,
        "Heheheheh. Just you wait, Arseille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Your lovely white frame will be MINE...\x01",
            "in this camera!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2BCF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2C9F")

    ChrTalk(    #41
        0xFE,
        (
            "Heheheh. Next is Zeiss, eh? I hope the\x01",
            "workshop ship is in the harbor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "If I'm lucky, the Arseille will be in port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Heheheh. I'm so excited that my camera\x01",
            "hand is shaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D36")

    label("loc_2C9F")


    ChrTalk(    #44
        0xFE,
        (
            "Okay, okay! Deep breaths.\x01",
            "I need to ready my camera before we land!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "My one and only chance to get the picture\x01",
            "will be when we're landing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2D36")

    TalkEnd(0xFE)
    Return()

    # Function_12_2B57 end

    def Function_13_2D3A(): pass

    label("Function_13_2D3A")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2E21")

    ChrTalk(    #46
        0xFE,
        (
            "I declare, this non-aggression pact is a perfect\x01",
            "match! Once the ink is dry, the markets will rise\x01",
            "like the clouds of Aidios Herself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "We'd be well served to have as many\x01",
            "orbments on hand before that happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC1")

    label("loc_2E21")


    ChrTalk(    #48
        0xFE,
        (
            "Simon, you made right sure to secure the\x01",
            "orbments, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "We MUST make sure those ducks are all in\x01",
            "a row before the Imperial traders start arriving.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2EC1")

    TalkEnd(0x19)
    Return()

    # Function_13_2D3A end

    def Function_14_2EC5(): pass

    label("Function_14_2EC5")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2F50")

    ChrTalk(    #50
        0xFE,
        (
            "W-We should at least have the amount\x01",
            "we would need on hand, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Anything further will be up to more negotiation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FD8")

    label("loc_2F50")


    ChrTalk(    #52
        0xFE,
        (
            "Y-Yes, ma'am! We've already spoken to\x01",
            "the head of the central factory!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "All we need now is a contract to move\x01",
            "the orbments.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2FD8")

    TalkEnd(0x1A)
    Return()

    # Function_14_2EC5 end

    def Function_15_2FDC(): pass

    label("Function_15_2FDC")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_308C")

    ChrTalk(    #54
        0xFE,
        (
            "So this non-aggression pact binds the\x01",
            "Empire, the Republic, and Liberl, huh?\x02\x03",

            "Hopefully it'll also serve to\x01",
            "better relations between the\x01",
            "three in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E0")

    label("loc_308C")


    ChrTalk(    #55
        0xFE,
        (
            "Ruan may be focused on their local election\x01",
            "problems, but the rest of the kingdom's\x01",
            "talking about the signing ceremony!\x02\x03",

            "After all, we're signing a non-aggression pact\x01",
            "with the same country that we fought for three\x01",
            "months of bloody slaughter just a decade ago.\x02\x03",

            "I hope it will finally melt the ice a little\x01",
            "between our two nations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_31E0")

    TalkEnd(0x1B)
    Return()

    # Function_15_2FDC end

    def Function_16_31E4(): pass

    label("Function_16_31E4")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3263")

    ChrTalk(    #56
        0xFE,
        "We're very sorry for the delays at Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "We've never experienced fog of that\x01",
            "sort before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3301")

    label("loc_3263")


    ChrTalk(    #58
        0xFE,
        "Oh! Hello, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "We're very sorry for the delays at Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I'm afraid merely launching into that fog\x01",
            "would've been incredibly dangerous...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3301")

    Jump("loc_3B0E")

    label("loc_3304")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 1)), scpexpr(EXPR_END)), "loc_346A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_339B")

    ChrTalk(    #61
        0xFE,
        (
            "When I was a kid, I really admired the\x01",
            "royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Even now, I think those uniforms have a\x01",
            "beautiful design.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3467")

    label("loc_339B")


    ChrTalk(    #63
        0xFE,
        (
            "When I was a kid, I really admired the\x01",
            "royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Well...okay, to be honest, what I really\x01",
            "wanted to do was wear the uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Uh... The male uniform, that is, of course.\x01",
            "Yes. Yes...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3467")

    Jump("loc_35CA")

    label("loc_346A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3512")

    ChrTalk(    #66
        0xFE,
        (
            "Not really surprising that students of a\x01",
            "famous school would be refined, I guess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I'm sure they get some really strict\x01",
            "lessons on proper etiquette.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35CA")

    label("loc_3512")


    ChrTalk(    #68
        0xFE,
        (
            "That passenger's a student from\x01",
            "the royal academy, isn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Yeah, I can definitely tell she is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "You really get a sense of refinement\x01",
            "from every movement she makes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_35CA")

    Jump("loc_3B0E")

    label("loc_35CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3665")

    ChrTalk(    #71
        0xFE,
        (
            "I was an only child, so looking at that\x01",
            "makes me a little sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I wish I had a little brother or sister\x01",
            "that age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3730")

    label("loc_3665")


    ChrTalk(    #73
        0xFE,
        "Are the passengers over there siblings?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "They've got...uh, 'different'\x01",
            "personalities for siblings, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I dunno, they seem really close.\x01",
            "Looking at them makes you smile,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3730")

    Jump("loc_38ED")

    label("loc_3733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_37DC")

    ChrTalk(    #76
        0xFE,
        (
            "That passenger with the lute, uh...\x01",
            "How do I put this? He sure seems\x01",
            "like he loves himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I guess he's the textbook definition\x01",
            "of narcissism, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38ED")

    label("loc_37DC")


    ChrTalk(    #78
        0xFE,
        (
            "You've seen that passenger playing\x01",
            "the lute, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It isn't just his music that's unique.\x01",
            "His singing and the way he talks is\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "How do I put it...?\x01",
            "I feel like he loves himself. A lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I guess he's the textbook definition\x01",
            "of narcissism, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_38ED")

    Jump("loc_3B0E")

    label("loc_38F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_39C0")

    ChrTalk(    #82
        0xFE,
        (
            "The observation lounge is usually\x01",
            "pretty popular, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "For some reason, our passengers feel\x01",
            "less inclined to sit here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "It's...because of that passenger,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0E")

    label("loc_39C0")


    ChrTalk(    #85
        0xFE,
        (
            "Thank goodness. That passenger has finally\x01",
            "quieted down. I thought I was going to have\x01",
            "to step in and brain him with his instrument...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Until a little while ago, he was playing\x01",
            "some very...um, bright tunes on his lute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "He even forced me into a duet with him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "It takes all kinds, I guess...including\x01",
            "pushy kinds.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_3B0E")

    TalkEnd(0x1C)
    Return()

    # Function_16_31E4 end

    def Function_17_3B12(): pass

    label("Function_17_3B12")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3BAF")

    ChrTalk(    #89
        0xFE,
        (
            "That fog in Rolent was totally a kick,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I took the chance to get out and enjoy\x01",
            "some nature when we were docked!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6A")

    label("loc_3BAF")


    ChrTalk(    #91
        0xFE,
        (
            "Hiiii, ma'am!\x01",
            "You've been riding a lot lately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "That fog in Rolent was totally a kick,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I took the chance to get out and enjoy\x01",
            "some nature when we were docked!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3C6A")

    Jump("loc_40B3")

    label("loc_3C6D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3D0D")

    ChrTalk(    #94
        0xFE,
        (
            "That passenger with the white coat\x01",
            "sure is something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "He was, like, totally muttering to himself.\x01",
            "I wonder what that was about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E2A")

    label("loc_3D0D")


    ChrTalk(    #96
        0xFE,
        (
            "That passenger with the white coat\x01",
            "sure is something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "He was, like, totally muttering to himself.\x01",
            "I wonder what that was about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "And then he started laughing in the middle of it!\x01",
            "Oooh, I wonder if he's a dangerous psycho!\x01",
            "That'd be so cool! But...also kinda freaky...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3E2A")

    Jump("loc_40B3")

    label("loc_3E2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3EBC")

    ChrTalk(    #99
        0xFE,
        (
            "I need to start getting stuff ready to\x01",
            "unload when we dock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "We've got sooooo much cargo to offload\x01",
            "in Grancel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F77")

    label("loc_3EBC")


    ChrTalk(    #101
        0xFE,
        (
            "Oooh, ooh, Grancel's up next, isn't it?\x01",
            "It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Yiiiiikes, I need to start getting stuff\x01",
            "ready to unload when we dock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "We've got sooooo much cargo to offload\x01",
            "in Grancel.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_3F77")

    Jump("loc_40B3")

    label("loc_3F7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4037")

    ChrTalk(    #104
        0xFE,
        (
            "Heya! Welcome to the cargo room!\x01",
            "It's dangerous down here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "The bridge is on the deck just above us.\x01",
            "If you haven't seen it yet, you TOTALLY\x01",
            "need to go look!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40B3")

    label("loc_4037")


    ChrTalk(    #106
        0xFE,
        (
            "Hello, ma'am!\x01",
            "Need a hand with something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "This is the cargo room! It's dangerous\x01",
            "down here, so watch yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_40B3")

    TalkEnd(0x1D)
    Return()

    # Function_17_3B12 end

    def Function_18_40B7(): pass

    label("Function_18_40B7")

    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40D9")
    SetChrSubChip(0xFE, 1)
    Jump("loc_40EC")

    label("loc_40D9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40EC")
    SetChrSubChip(0xFE, 2)

    label("loc_40EC")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4195")

    ChrTalk(    #108
        0xFE,
        (
            "I've been captaining for years and\x01",
            "I've NEVER seen fog that thick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Even the lights at full beam couldn't\x01",
            "burn through it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4292")

    label("loc_4195")


    ChrTalk(    #110
        0xFE,
        (
            "My apologies for the late departure\x01",
            "from port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Still, I've been a captain for years\x01",
            "and I've NEVER seen fog that thick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Even the lights at full beam couldn't\x01",
            "burn through it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Flying in that would've been\x01",
            "impossible...even for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_4292")

    Jump("loc_467F")

    label("loc_4295")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_440A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4332")

    ChrTalk(    #114
        0xFE,
        (
            "The green, rolling hills of Rolent when viewed\x01",
            "from up here are something else, eh?\x01",
            "That sight is calming and...healing, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4407")

    label("loc_4332")


    ChrTalk(    #115
        0xFE,
        (
            "Hello, come to see the view from\x01",
            "the bridge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "The green, rolling hills of Rolent when viewed\x01",
            "from up here are something else, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Staring at such a sea of green is\x01",
            "calming and...healing, somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_4407")

    Jump("loc_467F")

    label("loc_440A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_449C")

    ChrTalk(    #118
        0xFE,
        (
            "We're above the Tratt Plains at the\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "The weather's fantastic. Why not step\x01",
            "out on deck and catch the view?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455B")

    label("loc_449C")


    ChrTalk(    #120
        0xFE,
        (
            "Hello, miss. Having a look around the ship?\x01",
            "Or just bored?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "We're above the Tratt Plains at the\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "The weather's fantastic. Why not step\x01",
            "out on deck and catch the view?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_455B")

    Jump("loc_467F")

    label("loc_455E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_45FC")

    ChrTalk(    #123
        0xFE,
        (
            "The skies are calm and we should be\x01",
            "arriving on schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "If you're full of energy, feel free to\x01",
            "have a look around the ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_467F")

    label("loc_45FC")


    ChrTalk(    #125
        0xFE,
        "Hello, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "The skies are calm and we should be\x01",
            "arriving on schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "Please, relax and enjoy the voyage.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_467F")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0x1E)
    Return()

    # Function_18_40B7 end

    def Function_19_4688(): pass

    label("Function_19_4688")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_472D")

    ChrTalk(    #128
        0xFE,
        (
            "Please correct course slightly to the south,\x01",
            "avoiding the mountainside, Helm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Try to put our course above the eastern\x01",
            "Bose roads.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C0")

    label("loc_472D")


    ChrTalk(    #130
        0xFE,
        "Helm, you're going a bit too far northwest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "We don't want to get too close to the\x01",
            "mountainside. I want to avoid turbulence\x01",
            "if we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_47C0")

    Jump("loc_4B24")

    label("loc_47C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4842")

    ChrTalk(    #132
        0xFE,
        (
            "Helm, maintain current course for the\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Hmm... Rolent's winds are as calm\x01",
            "as ever today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48EB")

    label("loc_4842")


    ChrTalk(    #134
        0xFE,
        (
            "No need to alter course at the moment,\x01",
            "Helmsman. You may leave the rudder as\x01",
            "it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Keep our course steady... We'll be starting\x01",
            "our descent to Rolent soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_48EB")

    Jump("loc_4B24")

    label("loc_48EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_49A4")

    ChrTalk(    #136
        0xFE,
        (
            "Looks like there's a bit of wind coming\x01",
            "down from above...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "The winds around here change at\x01",
            "the drop of a hat, so I have to stay\x01",
            "on the ball about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A32")

    label("loc_49A4")


    ChrTalk(    #138
        0xFE,
        (
            "Helm, we're a bit high.\x01",
            "Can you drop us down slightly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Let's reduce altitude now before we get\x01",
            "caught in an air current, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_4A32")

    Jump("loc_4B24")

    label("loc_4A35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4AB3")

    ChrTalk(    #140
        0xFE,
        "Another sea breeze, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I can't let my attention waver when\x01",
            "we're in the air over this area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B24")

    label("loc_4AB3")


    ChrTalk(    #142
        0xFE,
        "Helm, adjust course slightly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I think the stern of the ship is being\x01",
            "dragged to the north slightly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_4B24")

    TalkEnd(0x1F)
    Return()

    # Function_19_4688 end

    def Function_20_4B28(): pass

    label("Function_20_4B28")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4BB8")

    ChrTalk(    #144
        0xFE,
        (
            "Ba-dum-ba-dum-baaaa-bummm. ♪\x01",
            "Men of the skyyyyy-yyy... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Fly like crooooows,\x01",
            "from town-to-tooooooown... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C2E")

    label("loc_4BB8")


    ChrTalk(    #146
        0xFE,
        (
            "Ba-dum-ba-da-dum. ♪\x01",
            "Yes, sirrrrr, understooood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Correcting course to souuuuth,\x01",
            "bum-da-dum-da-duuuum. ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4C2E")

    Jump("loc_4E94")

    label("loc_4C31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4C7F")

    ChrTalk(    #148
        0xFE,
        (
            "Waaah, wooooh... ♪\x01",
            "Doot-doo-da-dee-doot-doo... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CEE")

    label("loc_4C7F")


    ChrTalk(    #149
        0xFE,
        (
            "Waaah, doot-doo... ♪\x01",
            "Yes, understooood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Maintaaaaining current coooourse,\x01",
            "la-de-da-daaaaaa... ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4CEE")

    Jump("loc_4E94")

    label("loc_4CF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4D3E")

    ChrTalk(    #151
        0xFE,
        (
            "La-de-da-daaaaaaa... ♪\x01",
            "Da-da-da-duuuuuuuum... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DBC")

    label("loc_4D3E")


    ChrTalk(    #152
        0xFE,
        (
            "La-da-laaaaaa... ♪\x01",
            "Yes, affiiiirmative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Immeeeediately restorrring cooooooorrect\x01",
            "altitude, ba-da-da-bummmmm. ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4DBC")

    Jump("loc_4E94")

    label("loc_4DBF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_4E1A")

    ChrTalk(    #154
        0xFE,
        (
            "Bum-du-du-du, doo-doot-doo,\x01",
            "BAM-ba-ba-ba, bowwww-doot-dow... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E94")

    label("loc_4E1A")


    ChrTalk(    #155
        0xFE,
        (
            "Baaaa-doo-doo-doo-doooooot... ♪\x01",
            "Ah, affirmaatiiiiive... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "Changing course, doot-doo doo-doo-doooooot... ♪\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_4E94")

    TalkEnd(0x20)
    Return()

    # Function_20_4B28 end

    def Function_21_4E98(): pass

    label("Function_21_4E98")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4ED5")

    ChrTalk(    #157
        0xFE,
        "My, my, that fog was terrible.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F64")

    label("loc_4ED5")


    ChrTalk(    #158
        0xFE,
        "My, my, that fog was terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "And then it just...dissipated in\x01",
            "an instant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "I've never seen such strange fog\x01",
            "in all my days!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_4F64")

    Jump("loc_52DA")

    label("loc_4F67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4FFC")

    ChrTalk(    #161
        0xFE,
        (
            "I know they said it was safe, but I did\x01",
            "lose my composure for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "We're on an airship now, though,\x01",
            "so we're safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DA")

    label("loc_4FFC")


    ChrTalk(    #163
        0xFE,
        (
            "Those earthquakes in Zeiss were quite\x01",
            "a surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "To be so localized and happening in so\x01",
            "many different places like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I've been around the block a few times,\x01",
            "but I've never seen anything like that!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_50DA")

    Jump("loc_52DA")

    label("loc_50DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5193")

    ChrTalk(    #166
        0xFE,
        (
            "Honestly, only someone who is familiar\x01",
            "with technology could run Zeiss anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "Combining the jobs of mayor and factory\x01",
            "head was a fantastic decision!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52DA")

    label("loc_5193")


    ChrTalk(    #168
        0xFE,
        (
            "Ruan may be all excited about their\x01",
            "mayoral election, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Okay, so, Zeiss? You know,\x01",
            "the place we're headed to now?\x01",
            "Doesn't even HAVE a mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "Instead, the head of the central factory\x01",
            "fulfills the mayoral duties for the city and\x01",
            "region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Perfect system for an industrial city\x01",
            "like that, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_52DA")

    TalkEnd(0x21)
    Return()

    # Function_21_4E98 end

    def Function_22_52DE(): pass

    label("Function_22_52DE")

    TalkBegin(0x22)

    ChrTalk(    #172
        0xFE,
        (
            "Seems like the non-aggression pact\x01",
            "was signed with no delays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "I hope it leads to harmony between\x01",
            "Liberl and its neighbors.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_22_52DE end

    def Function_23_536A(): pass

    label("Function_23_536A")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_53D1")

    ChrTalk(    #174
        0xFE,
        "Bose hassa reeeeally famous restaurant in it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "Mommy, Mommy! Let's go eat there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_544B")

    label("loc_53D1")


    ChrTalk(    #176
        0xFE,
        "Bose hassa reeeeally famous restaurant in it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Oh, oh, I know! I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "Mommy, Mommy! Let's go eat there!\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_544B")

    TalkEnd(0x23)
    Return()

    # Function_23_536A end

    def Function_24_544F(): pass

    label("Function_24_544F")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_54E1")

    ChrTalk(    #179
        0xFE,
        (
            "My daughter really wants to\x01",
            "eat at the Anterose in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Children are so innocent...\x01",
            "And clueless about money.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_559F")

    label("loc_54E1")


    ChrTalk(    #181
        0xFE,
        "Really, child...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "My daughter keeps saying she wants to\x01",
            "eat at the Anterose Restaurant in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "*sigh* It must be nice to be a child...\x01",
            "so innocent, so unaware of...prices.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_559F")

    Jump("loc_5768")

    label("loc_55A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_564A")

    ChrTalk(    #184
        0xFE,
        (
            "Edel Department Store's merchandise is\x01",
            "really of fantastic quality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Apparently that store's been the source\x01",
            "of several recent fashions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5768")

    label("loc_564A")


    ChrTalk(    #186
        0xFE,
        (
            "If you need to shop in the capital, really\x01",
            "the only stop you need to make is Edel\x01",
            "Department Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "Sure, it isn't as big as Bose Market,\x01",
            "but their merchandise is the best in\x01",
            "the kingdom!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Aaaaah, if I had the time and mira, I'd\x01",
            "love to stop in and shop till I drop...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_5768")

    TalkEnd(0x24)
    Return()

    # Function_24_544F end

    def Function_25_576C(): pass

    label("Function_25_576C")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_5818")

    ChrTalk(    #189
        0xFE,
        (
            "Bose has been absolutely peaceful for a\x01",
            "while now, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "Hmm... Well, I'm sure their MARKET isn't\x01",
            "quite 'peaceful,' at least. Ho ho!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58CB")

    label("loc_5818")


    ChrTalk(    #191
        0xFE,
        (
            "Bose has been absolutely peaceful for a\x01",
            "while now, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "Even the Liberl News says nothing of\x01",
            "note's happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "That's something to be happy about,\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_58CB")

    Jump("loc_5A1E")

    label("loc_58CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_5956")

    ChrTalk(    #194
        0xFE,
        (
            "I suppose the non-aggression pact is a\x01",
            "good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "It's time we reconciled with Erebonia,\x01",
            "in any event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A1E")

    label("loc_5956")


    ChrTalk(    #196
        0xFE,
        (
            "I suppose the non-aggression pact is a\x01",
            "good thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "My own feelings toward Erebonia are...\x01",
            "complicated, to say the least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "After all this time, though, it's for\x01",
            "the best to reconcile.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_5A1E")

    TalkEnd(0x25)
    Return()

    # Function_25_576C end

    def Function_26_5A22(): pass

    label("Function_26_5A22")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5ADC")

    ChrTalk(    #199
        0xFE,
        (
            "I've heard even the manager of the Edel\x01",
            "Department Store's a fan of the Bose\x01",
            "Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "I think the pilgrimage journal my husband\x01",
            "wrote talks about that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_5ADC")


    ChrTalk(    #201
        0xFE,
        (
            "Bose Market is dreamland for anyone who\x01",
            "likes to shop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "I've heard even the manager of the Edel\x01",
            "Department Store's a fan of the Bose\x01",
            "Market.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_5B75")

    Jump("loc_5C41")

    label("loc_5B78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C41")

    ChrTalk(    #203
        0xFE,
        (
            "They say the three nations are going to\x01",
            "be signing a non-aggression pact soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "I'm impressed with Queen Alicia, bringing\x01",
            "both the Empire and Republic to the same\x01",
            "table like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C41")

    TalkEnd(0x26)
    Return()

    # Function_26_5A22 end

    def Function_27_5C45(): pass

    label("Function_27_5C45")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x27)
    ClearChrFlags(0x27, 0x10)
    TurnDirection(0x27, 0x0, 0)
    OP_51(0x27, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CD5")
    Jump("loc_5D17")

    label("loc_5CD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CF1")
    OP_51(0x27, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D17")

    label("loc_5CF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D0D")
    OP_51(0x27, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D17")

    label("loc_5D0D")

    OP_51(0x27, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D17")

    OP_51(0x27, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x27, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DCC")

    ChrTalk(    #205
        0xFE,
        (
            "Apparently, there's some very nice\x01",
            "lodging at the edge of Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "It's very popular with fishermen, I've heard.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6211")

    label("loc_5DCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5EA4")

    ChrTalk(    #207
        0xFE,
        (
            "I heard that on the day of the signing,\x01",
            "no civilians are being allowed into the\x01",
            "villa where the ceremony's being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "It would've been nice to see the moment\x01",
            "it was signed, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6003")

    label("loc_5EA4")


    ChrTalk(    #209
        0xFE,
        (
            "So, about that non-aggression pact\x01",
            "that's being signed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "I heard that on the day of the signing,\x01",
            "no civilians are being allowed into the\x01",
            "villa where the ceremony's being held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "Not surprising given that it hasn't been\x01",
            "that long since that detestable coup,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "It would've been nice to see the moment\x01",
            "it was signed, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_6003")

    Jump("loc_6211")

    label("loc_6006")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_6115")

    ChrTalk(    #213
        0xFE,
        (
            "I've heard they still haven't caught all\x01",
            "the remnants of the old Intelligence\x01",
            "Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "Most people don't seem to pay them much\x01",
            "mind anymore, but them skulking around\x01",
            "out there is a scary thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "Peace really is a fragile thing, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6211")

    label("loc_6115")


    ChrTalk(    #216
        0xFE,
        (
            "Apparently that non-aggression pact's\x01",
            "being signed at the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "Speaking of... That makes me think\x01",
            "of that whole mess with Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "Of course, last I heard he's still in\x01",
            "the stockade at Leiston Fortress,\x01",
            "under guard 24/7.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_6211")

    SetChrSubChip(0x27, 0)
    TalkEnd(0x27)
    Return()

    # Function_27_5C45 end

    def Function_28_621A(): pass

    label("Function_28_621A")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_62F2")

    ChrTalk(    #219
        0xFE,
        (
            "The existence of the Empire weighs more\x01",
            "heavily on the minds of our troops than\x01",
            "anyone else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "Ironically, I think our military men will\x01",
            "welcome the non-aggression pact more\x01",
            "than the rest of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6409")

    label("loc_62F2")


    ChrTalk(    #221
        0xFE,
        (
            "My friend's one of the guards at Haken\x01",
            "Gate, and let me tell you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "The existence of the Empire weighs more\x01",
            "heavily on the minds of our troops\x01",
            "than anyone else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "Ironically, I think our military men will\x01",
            "welcome the non-aggression pact more\x01",
            "than the rest of us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_6409")

    TalkEnd(0x28)
    Return()

    # Function_28_621A end

    def Function_29_640D(): pass

    label("Function_29_640D")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_6483")

    ChrTalk(    #224
        0xFE,
        (
            "Sadly, it seems like this girl's going\x01",
            "on to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "I'm sure Rinon would like this girl,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_656F")

    label("loc_6483")


    ChrTalk(    #226
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "I couldn't find any girls Rinon would like,\x01",
            "even in Grancel! What am I going to do\x01",
            "for that boy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "I'm just glad I met this girl to talk to\x01",
            "on the trip back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "I'm sure Rinon would like her a lot,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_656F")

    TalkEnd(0x2A)
    Return()

    # Function_29_640D end

    def Function_30_6573(): pass

    label("Function_30_6573")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_6646")

    ChrTalk(    #230
        0xFE,
        "I'd love to go see this lady's store...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "But I'm heading out to Bose to spend my\x01",
            "precious, precious vacation time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "It's kind of a pity, since we just got\x01",
            "to know each other and all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6777")

    label("loc_6646")


    ChrTalk(    #233
        0xFE,
        (
            "This lady said she runs a store in the\x01",
            "city of Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "I'm part of the staff for Edel's\x01",
            "in Grancel, so we got to talking\x01",
            "about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "I bet it'd be wonderful to run your own\x01",
            "store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Who cares if it's a tiny hole in the wall,\x01",
            "even? Oh, I wish I could have a store of\x01",
            "my own someday!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_6777")

    TalkEnd(0x2B)
    Return()

    # Function_30_6573 end

    def Function_31_677B(): pass

    label("Function_31_677B")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_6840")

    ChrTalk(    #237
        0xFE,
        (
            "Ahhhhh, Mistwald is lovely when viewed\x01",
            "from the air! However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "That fine lady attendant over there is\x01",
            "just as lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "Mmm, I feel like I don't want to get off\x01",
            "anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_691B")

    label("loc_6840")


    ChrTalk(    #240
        0xFE,
        (
            "Ahhhhh, Mistwald is lovely when viewed\x01",
            "from the air!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Looking down at that enormous forest\x01",
            "gives you a sense of just how wild the\x01",
            "Rolent region really is, still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "Mmm, I feel like I could watch forever.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_691B")

    TalkEnd(0x2C)
    Return()

    # Function_31_677B end

    def Function_32_691F(): pass

    label("Function_32_691F")

    TalkBegin(0x2D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_69B0")

    ChrTalk(    #243
        0xFE,
        (
            "I've heard Rolent has a lot of nice\x01",
            "fishing spots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Rolent itself isn't too famous, though,\x01",
            "so they're all kind of secret.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A7A")

    label("loc_69B0")


    ChrTalk(    #245
        0xFE,
        (
            "I've heard Rolent has a lot of nice\x01",
            "fishing spots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "Rolent itself isn't too famous, though,\x01",
            "so they're all kind of secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "I should try them before someone\x01",
            "writes a guide or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_6A7A")

    TalkEnd(0x2D)
    Return()

    # Function_32_691F end

    def Function_33_6A7E(): pass

    label("Function_33_6A7E")

    TalkBegin(0x2E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_6B45")

    ChrTalk(    #248
        0xFE,
        (
            "The Rolent region's one of those\x01",
            "places I'd just love to go to be touristy\x01",
            "as heck for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Delicious food, clean mountain air...\x01",
            "The perfect place to refine one's beauty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C70")

    label("loc_6B45")


    ChrTalk(    #250
        0xFE,
        "Rolent up next, hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "I'm not going there today, but I'd like\x01",
            "to spend some time on a farm there\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "Delicious food, clean mountain air...\x01",
            "The perfect place to refine one's beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "Heehee... Plus, my guy wants to go\x01",
            "fishing, so there'd be something for\x01",
            "him to do as well!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_6C70")

    TalkEnd(0x2E)
    Return()

    # Function_33_6A7E end

    def Function_34_6C74(): pass

    label("Function_34_6C74")

    TalkBegin(0x2F)

    ChrTalk(    #254
        0xFE,
        (
            "Tomorrow's the day they finally sign the\x01",
            "non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "It's been ten years now since the Hundred\x01",
            "Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "Perhaps it IS time we make proper peace\x01",
            "with the Empire.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x2F)
    Return()

    # Function_34_6C74 end

    def Function_35_6D37(): pass

    label("Function_35_6D37")

    TalkBegin(0x30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_6DB6")

    ChrTalk(    #257
        0xFE,
        "So...real peace with the Empire, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "Thinking about it, it sure seems like the\x01",
            "last ten years flew by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E84")

    label("loc_6DB6")


    ChrTalk(    #259
        0xFE,
        (
            "It wasn't so long ago that I thought real\x01",
            "peace with the Empire would've been\x01",
            "impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "Now it's almost upon us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "This is a real victory for Queen Alicia's\x01",
            "diplomatic efforts, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_6E84")

    TalkEnd(0x30)
    Return()

    # Function_35_6D37 end

    def Function_36_6E88(): pass

    label("Function_36_6E88")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F18")
    Jump("loc_6F5A")

    label("loc_6F18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F34")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F5A")

    label("loc_6F34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F50")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F5A")

    label("loc_6F50")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F5A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_7012")

    ChrTalk(    #262
        0xFE,
        (
            "Gotta finish this business fast and get\x01",
            "home soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "*sigh* My wife works me to the bone\x01",
            "AND complains all the time. It's rough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70AF")

    label("loc_7012")


    ChrTalk(    #264
        0xFE,
        (
            "Today I've got to head off to Bose Market\x01",
            "on an errand for my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "*sigh* My wife works me to the bone\x01",
            "AND complains all the time. It's rough.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_70AF")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_36_6E88 end

    def Function_37_70B8(): pass

    label("Function_37_70B8")

    TalkBegin(0x32)

    ChrTalk(    #266
        0xFE,
        (
            "Heehee! I'm going to Bose to help Daddy\x01",
            "with shopping!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "Shopping, shopping, so much fun...! ♪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x32)
    Return()

    # Function_37_70B8 end

    def Function_38_7127(): pass

    label("Function_38_7127")

    TalkBegin(0x33)

    ChrTalk(    #268
        0xFE,
        "I said, 'NO!'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "The last time you said that, you climbed\x01",
            "the railing on the deck, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "You're staying put right here,\x01",
            "no matter what!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x33, 0)
    TalkEnd(0x33)
    TalkEnd(0x33)
    Return()

    # Function_38_7127 end

    def Function_39_71D0(): pass

    label("Function_39_71D0")

    TalkBegin(0x34)

    ChrTalk(    #271
        0xFE,
        "Heeeey, Siiiiiiiis!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "I don't wanna sit heeeere.\x01",
            "Let's go outside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "I'll be good, I prooomise!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x34)
    Return()

    # Function_39_71D0 end

    def Function_40_7242(): pass

    label("Function_40_7242")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_72E9")

    ChrTalk(    #274
        0xFE,
        (
            "I've heard not all of the ringleaders\x01",
            "of the coup have been captured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "The few left may well have fled the\x01",
            "country by now. Good riddance, I say!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73CF")

    label("loc_72E9")


    ChrTalk(    #276
        0xFE,
        (
            "Ahhhhh! Next is the seat of Her Majesty\x01",
            "herself, Grancel, the city of beauty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "It makes my heart rejoice to see it\x01",
            "again...but it also brings to mind that\x01",
            "recent coup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "Something like that must never happen\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_73CF")

    TalkEnd(0x35)
    Return()

    # Function_40_7242 end

    def Function_41_73D3(): pass

    label("Function_41_73D3")

    TalkBegin(0x36)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_7465")

    ChrTalk(    #279
        0xFE,
        (
            "Speaking of, I remember hearing about\x01",
            "some weird ghost rumor in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "I wonder what became of that.\x01",
            "Nobody talks about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_7465")


    ChrTalk(    #281
        0xFE,
        (
            "Oh, right, the Ruan mayoral election is\x01",
            "coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "It's between Norman, who's promoting\x01",
            "tourism, and Portos, who's been promoting\x01",
            "the harbor business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "I wonder which candidate will get elected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "Even if you're not a citizen of Ruan,\x01",
            "it's still worth taking note of.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C)

    label("loc_7587")

    TalkEnd(0x36)
    Return()

    # Function_41_73D3 end

    def Function_42_758B(): pass

    label("Function_42_758B")

    TalkBegin(0x37)

    ChrTalk(    #285
        0xFE,
        "Whoooooa! So that's the fort?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "If it really is a ruin, then maybe there's\x01",
            "some hidden treasure inside that nobody\x01",
            "knows about!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x37)
    Return()

    # Function_42_758B end

    def Function_43_761B(): pass

    label("Function_43_761B")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x29, 0x40)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x101, 87690, -1000, 52960, 90)
    SetChrPos(0x29, 88760, -1000, 52950, 270)
    OP_6D(88640, -1000, 48310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(27000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 91200, 200, 47000, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 86380, 0, 45000, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 86380, 0, 46350, 180)
    FadeToBright(1500, 0)

    def lambda_76E1():
        OP_6D(88300, -1000, 52980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76E1)

    def lambda_76F9():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76F9)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #287
        0x101,
        (
            "#007F#6PUm... Kevin, right?\x02\x03",

            "I'm sorry. That was pathetic\x01",
            "of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x29,
        (
            "#1061FHeeey, no big, seriously. My shoulder's\x01",
            "always got room for a girl to cry on.\x02\x03",

            "#1060FSo how 'bout it? Feel a bit better now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#008F#6PYeah...a little.\x02\x03",

            "I'm Estelle. Estelle Bright.\x02\x03",

            "I'm a member of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x29,
        (
            "#1061FEsteeeelle, eh?\x01",
            "Dang, even your name is cute!\x02\x03",

            "...\x02\x03",

            "#1064F...Er, hang on, you said the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#006F#6PYeah, I'm a newly-minted senior bracer.\x02\x03",

            "#506FMight be hard to believe after seeing\x01",
            "me break down like that, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x29,
        (
            "#1060FNo, not at all. Now that you mention\x01",
            "it, you do kinda look loaded for bear.\x02\x03",

            "You a martial artist of some kind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        (
            "#501F#6PI guess you could call me that.\x01",
            "I focus on staff combat.\x02\x03",

            "#006FThough you said you're a priest, Kevin?\x02\x03",

            "I do appreciate the shoulder, but I gotta\x01",
            "admit, you don't look much like any priest\x01",
            "I know. Or would trust, usually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x29,
        (
            "#1068FAhaaa, ka-zing.\x01",
            "Through the chest, madam!\x02\x03",

            "#1066FWell, I'll admit that us wandering priests\x01",
            "are sheep of a different color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        "#505F#6PWandering what now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x29,
        (
            "#1060FWell, okay.\x01",
            "You know how there's villages 'n farms 'n\x01",
            "whatnot without churches, right?\x02\x03",

            "My order heads to such places at set\x01",
            "times each year and offers church\x01",
            "services and teaches Sunday School.\x02\x03",

            "Think of it as 'home delivery churchening'!\x01",
            "Or something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#000F#6PHuh. I never knew there were priests like\x01",
            "that, but it does make a lot of sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x29,
        (
            "#1061FAnd unlike church-bound priests,\x01",
            "there's a lot of us who are more\x01",
            "carefree about dress code.\x02\x03",

            "The church just kind of lets us do\x01",
            "our thing, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#506F#6PUh, well, fair enough I guess!\x02\x03",

            "#501FSo, Kevin, I guess you're off\x01",
            "to some village somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x29,
        (
            "#1060FNah, not immediately. I actually only\x01",
            "just arrived in Liberl, like, today.\x02\x03",

            "The High Seat dispatched me here since,\x01",
            "apparently, there's not enough wandering\x01",
            "priests around right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#501F#6POh, really? Okay, then.\x02\x03",

            "#505FThe High Seat... They mentioned that\x01",
            "in Sunday School, but I don't remember\x01",
            "where...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x29,
        (
            "#1060FIt's in the Holy City of Arteria, in the middle\x01",
            "of the continent.\x02\x03",

            "#1061FAnyway, I figured I'd do a bit of sightseein'\x01",
            "before I went and reported my assignment\x01",
            "to the bishop of Grancel Cathedral.\x02\x03",

            "And, well, here I am!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x101,
        (
            "#007F#6PUh... That seems just a bit irresponsible\x01",
            "to me...\x02\x03",

            "#509FYou really are kind of a half-baked priest,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x29,
        (
            "#1062FHeeey, it's cool. I'm checking out the\x01",
            "places I'll be wandering to in advance.\x02\x03",

            "Besides, I got to meet a troubled\x01",
            "--and lovely!--young woman.\x02\x03",

            "#1071FThis is surely a blessing from Aidios,\x01",
            "praise be to Her name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        (
            "#506F#6PYeah, smooth recovery, there.\x02\x03",

            "#006FBut...really, thank you, either\x01",
            "way. Letting it all out helped to\x01",
            "clear my head a bit, I think.\x02\x03",

            "Seriously, I'm being a ninny.\x01",
            "I should trust Joshua. He won't\x01",
            "do anything stupid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x29,
        "#1064FHuh? Who?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        (
            "#008F#6POh, uh, Joshua is my b--my, um,\x01",
            "brother. Sort of, in a sense.\x02\x03",

            "He disappeared suddenly,\x01",
            "which has been a bit of a shock...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x29,
        (
            "#1063F 'Disappeared,' huh...?\x02\x03",

            "You mean he ran away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x101,
        (
            "#506F#6PAhhh, no, no, no. He just went back\x01",
            "home ahead of the rest of us.\x02\x03",

            "I mean, he's family.\x01",
            "He wouldn't just run off on his own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x29,
        "#1063FI...see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        (
            "#503F#6PReally, though, what was I THINKING?\x01",
            "Worst mistake ever, telling him how I felt.\x01",
            "Especially at THAT moment.\x02\x03",

            "Next time I see him, I'll have to make\x01",
            "up some kinda excuse about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x29,
        (
            "#1063F...\x02\x03",

            "#1065FHey. Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x29,
        (
            "#1067FWell...\x02\x03",

            "...\x02\x03",

            "#1060FWell, like I was saying!\x01",
            "I'm basically just a tourist without\x01",
            "a plan or a clue right now, so!\x02\x03",

            "Howsabout I land with you in Rolent\x01",
            "and make sure you get home safely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#004F#6P#3SWhaaa...?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x29, 0)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_761B end

    def Function_44_85A3(): pass

    label("Function_44_85A3")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_A2(0x1240)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_44_85A3 end

    def Function_45_85B5(): pass

    label("Function_45_85B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CEF")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    SetChrSubChip(0x8, 1)
    OP_0D()

    ChrTalk(    #316
        0x8,
        (
            "#052F#4PEstelle? Somethin' up?\x01",
            "Wandering around the ship again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        (
            "#1016F#6PPretty much.\x02\x03",

            "I never rode airships much before now,\x01",
            "so it's all kind of new to me still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x8,
        (
            "#051F#4PAh, I got'cha. Yeah, full bracers do a lot\x01",
            "of traveling, so airships are real handy.\x02\x03",

            "Heck, we probably use 'em even\x01",
            "more than merchants and whatnot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#1015F#6PYeah, I remember how Dad\x01",
            "was always out on business.\x02\x03",

            "I wonder how he's doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x8,
        (
            "#051F#4PLast I heard, he was made top general\x01",
            "of the army, so I bet he's so busy it'd\x01",
            "make our eyes spin.\x02\x03",

            "Heh. Just desserts for the man who always\x01",
            "tried to take it as easy as he could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1016F#6PIt IS kinda hard to imagine Dad\x01",
            "being busy, somehow...\x02\x03",

            "#1011FI'm curious, though, Agate. You seem\x01",
            "to respect Dad, more or less.\x02\x03",

            "So why do you always trash-talk\x01",
            "him so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x8,
        (
            "#551F#4P...It's not...talkin' trash, really.\x02\x03",

            "#555F'Sides, your old man's the\x01",
            "one who's rude, y'know.\x02\x03",

            "Every time he sees me it's all 'Good work'\x01",
            "or 'What a good kid,' treatin' me like some\x01",
            "fresh-faced punk...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        (
            "#1007F#6PYyyyeah...\x01",
            "Dad does like to tease people...\x02\x03",

            "That's how he is to everyone, though,\x01",
            "so I never paid attention to it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x8,
        (
            "#051F#4PY'know, you're kinda lucky,\x01",
            "bein' a girl and all.\x02\x03",

            "If you were his son, you'd probably\x01",
            "be in the middle of a huge rebellious\x01",
            "phase right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x101,
        "#1008F#6PUh, r-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x8,
        (
            "#551F#4PA father is...sort of a wall for\x01",
            "a son to overcome, y'see.\x02\x03",

            "Going up against a wall the size of Cassius?\x01",
            "Yeah, that'd lead to one hell of a complex, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x101,
        (
            "#1016F#6PUh. Well, I guess it's more\x01",
            "of a guy thing, but...\x02\x03",

            "#1006FDoes that mean you've got a\x01",
            "complex about my dad, then, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x8,
        "#052F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x101,
        "#1004F#6POh, I'm sorry! Didn't mean to pry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x8,
        (
            "#552F#4PAh, just leave it.\x01",
            "You're just like your dad...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1404)
    EventEnd(0x0)
    SetChrSubChip(0x8, 0)
    Jump("loc_8D9B")

    label("loc_8CEF")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D14")
    SetChrSubChip(0xFE, 2)
    Jump("loc_8D2F")

    label("loc_8D14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D2A")
    SetChrSubChip(0xFE, 2)
    Jump("loc_8D2F")

    label("loc_8D2A")

    SetChrSubChip(0xFE, 1)

    label("loc_8D2F")

    OP_8C(0x8, 360, 0)
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #331
        0x8,
        (
            "#552FAnyway. Zeiss is comin' up.\x02\x03",

            "We're gettin' off soon,\x01",
            "so don't wander too far.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)

    label("loc_8D9B")

    Return()

    # Function_45_85B5 end

    def Function_46_8D9C(): pass

    label("Function_46_8D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95E2")
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    SetChrSubChip(0x9, 1)
    OP_0D()

    ChrTalk(    #332
        0x9,
        (
            "#526F#4PHello, Estelle.\x01",
            "Looking around the ship again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        (
            "#1016F#6PPretty much.\x02\x03",

            "I never rode airships much before now,\x01",
            "so it's all kind of new to me still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x9,
        (
            "#021F#4PI remember my first 'work-trips' on\x01",
            "them and getting all excited, too.\x02\x03",

            "I'd never ridden an airship\x01",
            "before in all my travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1011F#6PI guess the circus didn't\x01",
            "use airships much, huh?\x02\x03",

            "Did you guys ride around in orbal-powered\x01",
            "carriages, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x9,
        (
            "#027F#4PNo, no. Most of our carriages were of\x01",
            "the 'single-horsepower' variety.\x02\x03",

            "Mr. Harvey did have an old orbal-drive\x01",
            "carriage, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        (
            "#1015F#6PHuh, okay.\x02\x03",

            "Now that I think about it, whenever\x01",
            "your troupe visited you guys WERE\x01",
            "in a lot of covered wagons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x9,
        (
            "#021F#4PYou remember! You touch your teacher's\x01",
            "heart, my dear, sweet Estelle!\x02\x03",

            "#526FAnyway, airships are still fairly uncommon\x01",
            "outside of Liberl, as I understand it.\x01",
            "Especially as civilian vehicles.\x02\x03",

            "Most other countries prefer orbal-driven\x01",
            "ground-based transport.\x02\x03",

            "The Erebonians favor orbal-driven trains,\x01",
            "and have a pretty large rail system\x01",
            "connecting their major cities...\x02\x03",

            "And our Calvardian neighbors use orbal\x01",
            "buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x101,
        (
            "#1004F#6POrbal...buses?\x02\x03",

            "#1015FWhat kind of vehicle is a 'bus'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x9,
        (
            "#020F#4PA bus is basically a VERY\x01",
            "large orbal carriage.\x02\x03",

            "It's a little like an airship. You pay\x01",
            "in advance and it'll take you from\x01",
            "place to place.\x02\x03",

            "It isn't nearly as fast as an airship,\x01",
            "but the pace is gentler. They're easy\x01",
            "to maintain and they're quite pleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1001F#6PHuh, neato.\x01",
            "I kinda want to ride one now!\x02\x03",

            "#1006FSpeaking of which...\x01",
            "Schera, you've been to Calvard, right?\x02\x03",

            "I heard you met Zin then.\x01",
            "C'mon, I gotta hear that story!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x9,
        (
            "#027F#4PHaha! There's not that much to it,\x01",
            "I'm afraid. I was on an errand for\x01",
            "Cassius.\x02\x03",

            "He needed me to deliver a document\x01",
            "to Calvard's Eastern Quarter.\x02\x03",

            "That's where I first met Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        (
            "#1011F#6PI see.\x02\x03",

            "#1015FI gotta admit, I can't imagine what a\x01",
            "town full of Easterners would be like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x9,
        (
            "#021F#4PIt was exciting. Very different culturally,\x01",
            "and exotic.\x02\x03",

            "You should visit, if you get the chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1405)
    EventEnd(0x0)
    SetChrSubChip(0x9, 0)
    Jump("loc_96BA")

    label("loc_95E2")

    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9607")
    SetChrSubChip(0xFE, 2)
    Jump("loc_9622")

    label("loc_9607")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_961D")
    SetChrSubChip(0xFE, 2)
    Jump("loc_9622")

    label("loc_961D")

    SetChrSubChip(0xFE, 1)

    label("loc_9622")

    OP_8C(0x9, 360, 0)
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #345
        0x9,
        (
            "#020FWell, Zeiss is up next, so\x01",
            "we'll be getting off soon.\x02\x03",

            "Don't wander around too much or you\x01",
            "may miss us when we disembark.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)

    label("loc_96BA")

    Return()

    # Function_46_8D9C end

    def Function_47_96BB(): pass

    label("Function_47_96BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A037")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(89060, -1000, 51690, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 89560, -1000, 51470, 270)
    SetChrSubChip(0xA, 2)
    OP_0D()

    ChrTalk(    #346
        0xA,
        (
            "#030FEstelle!\x01",
            "Enjoying our flight through the heavens?\x02\x03",

            "#031FLook--gaze upon this magnificent\x01",
            "azure sky!\x02\x03",

            "Ah, but there is nothing\x01",
            "better to drink to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1016FWell, uh, the weather is great\x01",
            "and the sky is pretty, but...\x02\x03",

            "We're, um...almost to Zeiss, Olivier.\x01",
            "Should you really be drinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xA,
        (
            "#030FOh, come now. Don't say that.\x02\x03",

            "#034FSomewhere beneath this brilliant\x01",
            "sky is my beloved Joshua.\x02\x03",

            "The pain he must be feeling\x01",
            "on his solitary journey...\x02\x03",

            "#030FSuch thoughts DRIVE a man\x01",
            "to drink, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        (
            "#1019FExcuse me, but that is entirely\x01",
            "and exclusively my line.\x02\x03",

            "#1007F*sigh* At least things never get TOO\x01",
            "serious with you around. I guess that's\x01",
            "a good thing. Kinda. Maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xA,
        (
            "#031FI shall take that as the highest praise!\x02\x03",

            "#030FI am relieved, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xA,
        (
            "#035FThe 'Black Fang'...\x02\x03",

            "I had wondered if the words of the\x01",
            "Phantom Thief had shaken you.\x02\x03",

            "#030FI see I had no cause to be concerned,\x01",
            "however. You have a will of iron, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1025FO-Oh...\x02\x03",

            "#1016FAh-haha... You were worried about me,\x01",
            "Olivier? That's...kinda sweet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xA,
        (
            "#031FHaha! Remember, I am a wandering\x01",
            "bard and poet, ever in search of that\x01",
            "pinnacle of human affection!\x02\x03",

            "Maidens in love shall find\x01",
            "no greater ally than I!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        "#1013FErm, um, well...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xA,
        (
            "#030FAh, please.\x01",
            "I do not need a...'staffing' today.\x02\x03",

            "I promise, I was not teasing you. I actually\x01",
            "find your relationship heartwarming.\x02\x03",

            "Those new clothes of yours, for example.\x01",
            "You purchased them because you wish\x01",
            "for Joshua to see you in them, yes?\x02\x03",

            "#031FYou look excellent in them, I must say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x101,
        (
            "#1017FTh-Thanks...\x02\x03",

            "#1007FWhat's with the embarrassing\x01",
            "compliments all of a sudden?\x02\x03",

            "Besides, Schera got me these\x01",
            "clothes as a present.\x02\x03",

            "#1013FJoshua... Well, maybe he'd\x01",
            "like them. A little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xA,
        "#033F...Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        "#1019FWh-What's with that look?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xA,
        (
            "#035FHeh... Forgive me.\x01",
            "That was just...more than I expected.\x02\x03",

            "#030FLet us leave that topic behind\x01",
            "for a while, then.\x02\x03",

            "Come, Estelle.\x01",
            "I shall treat you to a 'legal' cocktail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1015FI guess it is a bit tempting,\x01",
            "but we're nearly to Zeiss.\x02\x03",

            "#1006FTry not to drink the whole bar\x01",
            "yourself, Olivier, or you'll pass\x01",
            "out and miss our stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xA,
        (
            "#031FHah! Don't you worry.\x02\x03",

            "I only lose myself in drink when\x01",
            "it is poured by a lovely lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        (
            "#1007FYou realize that's not something\x01",
            "to brag about, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1406)
    EventEnd(0x0)
    SetChrSubChip(0xA, 0)
    Jump("loc_A4F4")

    label("loc_A037")

    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A05C")
    SetChrSubChip(0xFE, 2)
    Jump("loc_A077")

    label("loc_A05C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A072")
    SetChrSubChip(0xFE, 2)
    Jump("loc_A077")

    label("loc_A072")

    SetChrSubChip(0xFE, 1)

    label("loc_A077")

    OP_8C(0xA, 360, 0)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_END)), "loc_A15A")

    ChrTalk(    #364
        0xA,
        (
            "#031FNow, then...Zeiss!\x01",
            "Ah, I cannot wait.\x02\x03",

            "I went straight to Elmo for the hot\x01",
            "springs the last time I was here,\x01",
            "so I did not see much of the region.\x02\x03",

            "I'm eager to see everything\x01",
            "Zeiss has to offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4EC")

    label("loc_A15A")


    ChrTalk(    #365
        0xA,
        (
            "#033FOh, on that note, Estelle, would you\x01",
            "like to read a certain book?\x02\x03",

            "#031FIt's very interesting, although\x01",
            "it is banned in Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        (
            "#1019FA banned... If you're trying to push smut\x01",
            "on me, Olivier, I swear to Aidios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xA,
        (
            "#030FNot at all. It's a pleasant novel\x01",
            "set in the Calvard Republic.\x02\x03",

            "But, alas, our noble Imperial overlords have\x01",
            "deemed it...'improper for our education.'\x01",
            "So you cannot find it in the Empire's borders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        (
            "#1013FOh, I... I see. The Empire's...\x01",
            "kind of a hard place to live, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xA,
        (
            "#030FI'd heard reports of its quality,\x01",
            "and now I've finally had a\x01",
            "chance to read it.\x02\x03",

            "#035FEverything I'd heard was true.\x01",
            "It is most excellent reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1011FHuh, neat.\x01",
            "What kind of story is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xA,
        (
            "#030FSee for yourself! I'm quite done\x01",
            "with it, so go ahead and take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x101,
        "#1001FReally? Cool! Thanks!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x39, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #373
        "\x07\x00Received #572i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23C, 1)
    OP_A2(0x10B7)

    label("loc_A4EC")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)

    label("loc_A4F4")

    Return()

    # Function_47_96BB end

    def Function_48_A4F5(): pass

    label("Function_48_A4F5")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #374
        "\x07\x05Thank you for flying with us today.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #375
        "\x07\x05We will be arriving in Zeiss momentarily.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #376
        (
            "\x07\x05Please be aware that there may be turbulence\x01",
            "while landing, so we ask that all passengers\x01",
            "take their seats.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A60A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_A60E")

    label("loc_A60A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_A60E")

    AddParty(0x4, 0xF8, 0xFF)
    AddParty(0x3, 0xF9, 0xFF)
    NewScene("ED6_DT21/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_48_A4F5 end

    def Function_49_A620(): pass

    label("Function_49_A620")

    EventBegin(0x0)
    OP_6D(88630, 0, 2860, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 88630, 0, 2860, 270)
    FadeToBright(1000, 0)
    OP_A2(0x1681)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_49_A620 end

    def Function_50_A680(): pass

    label("Function_50_A680")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xB, 255)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 87980, -1000, 53080, 153)
    SetChrPos(0x101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(    #377
        0xB,
        "#061FHi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x8,
        (
            "#051F#6PWhat's up, Estelle?\x02\x03",

            "You creepin' around the ship AGAIN?\x01",
            "Man, you just cannot stay still, can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x101,
        (
            "#1007FOh, c'mon, I'm not a cat in\x01",
            "a carrier or something.\x02\x03",

            "#1008FI just...yeah, I do get kind of antsy,\x01",
            "having to sit down and wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x8,
        (
            "#051F#6PI thought you flew to Le Locle, though.\x02\x03",

            "That's a good half-day on an airship,\x01",
            "at least. You must've worn a rut in\x01",
            "the deck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        (
            "#1016FUh, well, I was asleep for both trips,\x01",
            "actually...\x02\x03",

            "I was so nervous to be going that I couldn't\x01",
            "sleep the night before, and coming back\x01",
            "I was wiped out from that last test...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x8,
        "#551F#6PI shoulda seen that one coming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xB,
        (
            "#061F*giggle* That's definitely an 'Estelle'\x01",
            "thing to do.\x02\x03",

            "#066FHmmm... Leaving the country...\x01",
            "I'd really like to do that someday,\x01",
            "too!\x02\x03",

            "Maybe I could even go visit Mom\x01",
            "and Dad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        (
            "#1025FOh, yeah.\x02\x03",

            "Tita, your mom and dad are out\x01",
            "of the country working, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xB,
        (
            "#560FYeah...\x02\x03",

            "They're helping to establish orbal\x01",
            "technology in places that don't have\x01",
            "it yet.\x02\x03",

            "They've been gone for two years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        (
            "#1015FWow, that IS a long time...\x02\x03",

            "I hope they write you letters\x01",
            "or something at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xB,
        (
            "#061FYeah, once every month. ♪\x02\x03",

            "#060FI, um, wrote about you last time,\x01",
            "Estelle, and in the reply...\x02\x03",

            "They said to give you their regards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        (
            "#1016FAww, that's sweet of them.\x02\x03",

            "#1006FSo what kind of people are\x01",
            "your parents, Tita?\x02\x03",

            "Is your mom like you? I bet she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xB,
        (
            "#064FLike me? I don't think so...\x02\x03",

            "#060FMom's got a really...um,\x01",
            "powerful personality, I guess.\x02\x03",

            "#061FShe and Grandpa kinda end up fighting\x01",
            "and wrestling a lot over stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x101,
        "#1004F...Wrestling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xB,
        (
            "#067FOh, but they usually get\x01",
            "along really well!\x02\x03",

            "Dad says their fighting is just a\x01",
            "way they express their love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x101,
        (
            "#1016FWell, uh, okay...\x02\x03",

            "#1011FSo what's your dad like, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xB,
        (
            "#560FHe's not like Mom at all. He's sorta\x01",
            "quiet and...reliable, I guess?\x02\x03",

            "He was a bracer until about ten\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x101,
        "#1004FWait, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x8,
        (
            "#051F#6PReal serious. I actually talked to\x01",
            "Gramps about that, and Dan was\x01",
            "the real deal back in his day.\x02\x03",

            "The professor said he had to retire\x01",
            "and become an engineer due to an\x01",
            "injury of some sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        (
            "#1006FHuh, okay.\x02\x03",

            "#1001FThey sound great! I'd love to\x01",
            "meet them when they get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xB,
        (
            "#061FYeah! When they do, come over\x01",
            "to play and I'll introduce you. ♪\x02\x03",

            "#560FAgate, you'll have to meet them,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #398
        0x8,
        (
            "#055F#6PHuh?\x02\x03",

            "Why would I have to\x01",
            "meet your folks?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xB,
        (
            "#061FWell, you get along really well\x01",
            "with Grandpa...\x02\x03",

            "...and I wrote a lot about you, and,\x01",
            "and, Mom and Dad said in their reply\x01",
            "that they really want to meet you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x8,
        "#552F#6POf all the...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x101,
        "#1006FHaha! Time to pay the piper, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xB,
        (
            "#063FUm... If you don't want to,\x01",
            "Agate, you don't have to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x8,
        (
            "#555F#6PNah, it's...fine.\x02\x03",

            "#551FLook, I'll stop by and say hi to them\x01",
            "if I'm ever in Zeiss for work, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xB,
        "#061FHeehee, okay! ♪\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xB, 88700, -1000, 52960, 0)
    SetChrPos(0x101, 89770, -1000, 52480, 270)
    OP_4B(0xB, 255)
    OP_0D()
    OP_A2(0x1603)
    EventEnd(0x0)
    Return()

    # Function_50_A680 end

    def Function_51_B2B7(): pass

    label("Function_51_B2B7")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xB, 255)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 87980, -1000, 53080, 153)
    SetChrPos(0x101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(    #405
        0xB,
        (
            "#560FOh, yeah, Estelle!\x02\x03",

            "Do you know why the wind's nice\x01",
            "and gentle out on the deck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x101,
        "#1004FUh... Isn't it just like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0xB,
        (
            "#060FOh, no! At the speed we're going,\x01",
            "the wind should be really strong!\x02\x03",

            "We wouldn't be able to hear each other...\x01",
            "We'd get swept off the deck, in fact!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x101,
        "#1015FWait, seriously...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #409
        0x8,
        (
            "#052F#6PAin't there some bit of the airship\x01",
            "that prevents that? Think I heard\x01",
            "about that once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xB,
        (
            "#560FUh-huh! It's a side effect of the 'flight field'\x01",
            "that keeps the ship in the air.\x02\x03",

            "#061FAn orbal flight engine envelops\x01",
            "the ship in a field that counteracts\x01",
            "gravity, you see!\x02\x03",

            "It also has an anti-inertial effect on anything\x01",
            "striking the field, and that includes the\x01",
            "particles that make up the wind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        "#1019F(...Agate, are you following any of this?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x8,
        "#552F#6P(You're kiddin', right?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xB,
        (
            "#060FBut generating a flight field\x01",
            "takes a lot of power...\x02\x03",

            "You need a really high output orbal\x01",
            "engine to create the field at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x101,
        (
            "#1006FOkay...\x02\x03",

            "So that's why people always say\x01",
            "that it's the engine that determines\x01",
            "what an airship can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x8,
        (
            "#051F#6PAhhh, okay, so that's why everyone's\x01",
            "made such a fuss about that new\x01",
            "engine for the royal airship.\x02\x03",

            "Ain't that thing supposed to be absolutely\x01",
            "crazy in terms of how strong it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xB,
        (
            "#061FUh-huh! Grandpa showed me the spec sheet\x01",
            "for it, and its capabilities are waaaaaaaay\x01",
            "beyond existing engines!\x02\x03",

            "Grandpa and the rest of the team at the\x01",
            "central factory worked really hard on it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        "#1016FHaha! I hope I get to see it someday.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xB, 88700, -1000, 52960, 0)
    SetChrPos(0x101, 89770, -1000, 52480, 270)
    OP_4B(0xB, 255)
    OP_0D()
    OP_A2(0x1604)
    EventEnd(0x0)
    Return()

    # Function_51_B2B7 end

    def Function_52_B992(): pass

    label("Function_52_B992")

    EventBegin(0x0)
    OP_20(0x3E8)
    Fade(1000)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0xA, 42)
    SetChrSubChip(0xA, 0)
    OP_6D(88650, -1000, 52950, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 87980, -1000, 53080, 153)
    SetChrPos(0x101, 89300, -1000, 52860, 249)
    OP_0D()

    ChrTalk(    #418
        0xA,
        (
            "#031FAh, Estelle, my fair rose.\x02\x03",

            "Welcome to Olivier Lenheim's lovely\x01",
            "solo recital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x101,
        (
            "#1007FOh, Aidios, he escaped his chair.\x02\x03",

            "#1019FSeriously. Who let you out of your seat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xA,
        (
            "#035FHeh.\x02\x03",

            "Just as bracers protect the innocent,\x01",
            "and military men protect their homes...\x02\x03",

            "It is the duty of performers such as I to\x01",
            "protect the soul and pathos of the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x9,
        (
            "#020F#6PHe did, apparently, beg permission\x01",
            "from the steward, Estelle.\x02\x03",

            "There's no harm in letting him play.\x01",
            "No lasting harm, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xA,
        (
            "#036FSchera! Have you no appreciation for\x01",
            "song?\x02\x03",

            "#034FYou even turned down my invitation to\x01",
            "the Elmo springs a month ago, in the\x01",
            "most casual fashion imaginable...\x02\x03",

            "And I would drink myself under\x01",
            "the table for you! What tragedy!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(300)

    ChrTalk(    #423
        0x9,
        (
            "#021F#6PIf I actually had time to fool\x01",
            "around like that, I'd consider it.\x02\x03",

            "#027FBesides, I'd never actually drink you\x01",
            "under the table deliberately.\x02\x03",

            "I just want someone who can\x01",
            "match my...pace.\x02\x03",

            "#021FThat's all I need from a drinking\x01",
            "partner. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xA,
        "#033F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        (
            "#1007FEr, Olivier?\x01",
            "Schera...doesn't quite get it.\x02\x03",

            "She doesn't realize how crazy her\x01",
            "drinking speed is or how her liver is\x01",
            "basically the Gehenna of Alcohol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x9,
        (
            "#025F#6PI am sitting right here, you know,\x01",
            "Estelle.\x02\x03",

            "#027FBut if you want to 'serenade me,'\x01",
            "my dear Lenheim, you'd better be\x01",
            "ready to keep up with me.\x02\x03",

            "And remember, I won't work your liver\x01",
            "nearly as hard as Aina would.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x14, 0x0, 0x1F4, 0xFA0)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #427
        0xA,
        (
            "#036FOh, please, let us never speak\x01",
            "of that night again.\x02\x03",

            "#034FThe...memories alone make my heart\x01",
            "quail...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x9,
        "#021F#6PHeh! I bet they do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x101,
        (
            "#1016F(Just what the heck...? You know,\x01",
            "I don't actually want to know...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(89770, -1000, 52480, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 88700, -1000, 52960, 0)
    SetChrPos(0x101, 89770, -1000, 52480, 270)
    OP_8C(0xA, 180, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 41)
    SetChrSubChip(0xA, 0)
    OP_4B(0xA, 255)
    OP_1D(0x49)
    OP_0D()
    OP_A2(0x1607)
    EventEnd(0x0)
    Return()

    # Function_52_B992 end

    def Function_53_C114(): pass

    label("Function_53_C114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1D2")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    OP_0D()

    ChrTalk(    #430
        0xC,
        "#572F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x101,
        "#1015F#6PUm...Zin?\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0xFE, 0)
    Sleep(75)
    SetChrSubChip(0xFE, 1)
    Sleep(300)

    ChrTalk(    #432
        0xC,
        (
            "#070F#4PAh, Estelle!\x02\x03",

            "What is it? Need me for something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x101,
        (
            "#1016F#6POh, uh, no, not really. It's just...\x02\x03",

            "#1025FYou kinda looked like you\x01",
            "were lost in thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xC,
        (
            "#074F#4PMmm... Yes.\x02\x03",

            "#070FJust...remembering the past a bit,\x01",
            "is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x101,
        (
            "#1015F#6PWith that sunglasses wolf guy,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xC,
        (
            "#070F#4PYeah.\x02\x03",

            "We last met six years ago.\x01",
            "At first, it felt like longer, but...\x01",
            "it hasn't been that long, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        (
            "#1025F#6PI guess not...\x02\x03",

            "#1002FSo, that man was your senior\x01",
            "at your, um, dojo, right?\x02\x03",

            "What kind of martial artist is he,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xC,
        "#074F#4PWell...\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_AD(0x24007B, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_1D(0x53)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #439
        (
            "\x07\x00#070FSimply put, he's a natural.\x02\x03",

            "His reflexes are perfect, and\x01",
            "his sense for battle is keen.\x02\x03",

            "When I knew him, he kept himself\x01",
            "in perfect shape, and it looks like\x01",
            "that's still true today.\x02\x03",

            "And on top of all that, he knows\x01",
            "how to utilize his chi exactly.\x02\x03",

            "In every sense, he is a cut above\x01",
            "the normal man.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #440
        (
            "\x07\x00#1007FYeah, his moves... I've never seen\x01",
            "anything like that.\x02\x03",

            "I think he might even be faster and\x01",
            "stronger in some ways than that\x01",
            "Lorence guy, and that's scary.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #441
        (
            "\x07\x00#070FI think you might be right, yeah.\x02\x03",

            "#074FWhen we were students, I admired\x01",
            "that strength of his. Envied it, even.\x02\x03",

            "At least I did until six years ago, when\x01",
            "he killed our mentor and master of the\x01",
            "dojo, Ryuga.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #442
        (
            "\x07\x00#1020FWh-What?!\x02\x03",

            "He... He killed his own...?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #443
        (
            "\x07\x00#070FAh, sorry, I'm getting ahead of it.\x01",
            "They both agreed to the fight, mind.\x02\x03",

            "#074FMaster Ryuga had long been aware\x01",
            "of the darkness in Walter's heart.\x02\x03",

            "He'd grown drunk on his own power,\x01",
            "and hungered for still more...\x02\x03",

            "Master constantly rebuked him for his\x01",
            "actions and reminded him what the proper\x01",
            "heart of a martial artist is supposed to be...\x02\x03",

            "#070F...the 'Living Fist' of the Taito style,\x01",
            "that seeks to perfect one's self through\x01",
            "the medium of honorable combat.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #444
        (
            "\x07\x00#1006FThe 'Living Fist,' huh?\x01",
            "That has a neat ring to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #445
        (
            "\x07\x00#072FUltimately, though, Walter never listened.\x02\x03",

            "He relished the power which the most\x01",
            "aggressive side of Taito style gave him.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #446
        "\x07\x00#1004FThe aggressive side?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #447
        (
            "\x07\x00#074FMartial arts are used in combat, and so no\x01",
            "one can deny that they can be used to hurt\x01",
            "people as much as defend them.\x02\x03",

            "And while there are many who train for the\x01",
            "latter purpose, there are also those who\x01",
            "seek to do the former.\x02\x03",

            "#072FThose who do eventually become monsters,\x01",
            "whose fists exist only to kill... We call\x01",
            "this side of Taito the 'Murderer's Fist.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #448
        "\x07\x00#1020FThe...what...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24007C, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #449
        (
            "\x07\x00#072FIn the end, Master Ryuga challenged\x01",
            "Walter as he was preparing to leave\x01",
            "the dojo to pursue that path.\x02\x03",

            "They fought a duel to the death over it...\x01",
            "and Master lost.\x02\x03",

            "#074FI was the observer for that match.\x01",
            "I could do nothing but watch.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(275, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #450
        "\x07\x00#1026FZin...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x3E8)
    Sleep(1500)

    ChrTalk(    #451
        0xC,
        (
            "#070F#4PWell, that's what happened,\x01",
            "and I've been looking for Walter,\x01",
            "off and on, ever since.\x02\x03",

            "To think we'd meet here, now,\x01",
            "in Liberl, though...\x02\x03",

            "This is the hand of She Who Dwells\x01",
            "Above at work, mark my words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x101,
        "#1003F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xC,
        (
            "#073F#4POh, sorry, Estelle.\x02\x03",

            "I didn't mean to chew your head off.\x01",
            "Or, wait, was it ear...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x101,
        (
            "#1007F#6PNo, you didn't chew anything...\x01",
            "Thanks for telling me.\x02\x03",

            "#1002FBut, Zin...\x02\x03",

            "You're...searching for Walter to\x01",
            "get revenge, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xC,
        (
            "#070F#4PHaha! No, no. Like I said, their match\x01",
            "was fairly fought. Master knew what could\x01",
            "happen when he challenged Walter.\x02\x03",

            "There's no revenge to take.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x101,
        (
            "#1016F#6PO-Oh... Yeah, that's right.\x02\x03",

            "#1026FBut then, why are you looking for him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0xC,
        (
            "#074F#4PMmm...\x02\x03",

            "#572FThere's something...I want to confirm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x101,
        (
            "#1015F#6PSomething to... Huh?\x01",
            "Now I REALLY don't get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xC,
        (
            "#071F#4PHah! It's, ah, kind of embarrassing.\x02\x03",

            "#070FEither way, I'm still too\x01",
            "inexperienced to find out...\x02\x03",

            "I hope I can sharpen myself\x01",
            "by helping you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        (
            "#1012F#6PI see... Yeah.\x02\x03",

            "#1018FWell, then, I hope you can keep up, Zin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xC,
        (
            "#071F#4PWe'll see, Estelle.\x01",
            "You're the one with the shorter legs!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_A2(0x1609)
    EventEnd(0x0)
    SetChrSubChip(0xC, 0)
    OP_1D(0x1)
    Jump("loc_D7C9")

    label("loc_D1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3F1")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(117080, 0, 1830, 0)
    SetChrPos(0x101, 116400, 0, 1690, 90)
    SetChrSubChip(0xC, 1)
    OP_0D()

    ChrTalk(    #462
        0x101,
        (
            "#1004F#6POh, yeah, speaking of...\x01",
            "uh, the story, not my legs...\x02\x03",

            "#1025FI think I get what's going on\x01",
            "between you and Walter...\x02\x03",

            "But how does Kilika fit\x01",
            "into all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xC,
        (
            "#073F#4PErm...\x02\x03",

            "#074FIt's...not really my place to say.\x01",
            "I'll only say this much:\x02\x03",

            "Kilika is--was--Master Ryuga's\x01",
            "daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x101,
        "#1026F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xC,
        (
            "#070F#4PI think you can fill in the rest\x01",
            "yourself for now, yeah?\x02\x03",

            "She'll probably tell you the\x01",
            "full story someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        "#1006F#6PYeah... Fair enough.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x160A)
    EventEnd(0x0)
    SetChrSubChip(0xC, 0)
    Jump("loc_D7C9")

    label("loc_D3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6DF")
    OP_A2(0x1)
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D421")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D43C")

    label("loc_D421")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D437")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D43C")

    label("loc_D437")

    SetChrSubChip(0xFE, 1)

    label("loc_D43C")

    OP_8C(0xC, 0, 0)
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #467
        0xC,
        (
            "#070FAnyway! Once we get to the capital,\x01",
            "I should show my face at the Calvardian\x01",
            "embassy.\x02\x03",

            "Can't wait too long or Elsa is gonna\x01",
            "give me hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x101,
        (
            "#1015FElsa... That wouldn't be a strict, harsh-\x01",
            "looking woman with glasses, would it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xC,
        "#073FHuh, you know Elsa Cochrane?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x101,
        (
            "#1006FI've only seen her briefly, really.\x02\x03",

            "We were at the landing port, and she\x01",
            "was in the middle of an argument\x01",
            "with the Imperial ambassador.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xC,
        (
            "#075FAh. Yes, she is not what I would\x01",
            "call a fan of Erebonia.\x02\x03",

            "She's quite confident and intelligent,\x01",
            "usually, but Erebonia...and their\x01",
            "nobility...tend to make her see red.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        (
            "#1011FI can kinda understand that,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Jump("loc_D7C9")

    label("loc_D6DF")

    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D704")
    SetChrSubChip(0xFE, 2)
    Jump("loc_D71F")

    label("loc_D704")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D71A")
    SetChrSubChip(0xFE, 2)
    Jump("loc_D71F")

    label("loc_D71A")

    SetChrSubChip(0xFE, 1)

    label("loc_D71F")

    OP_8C(0xC, 0, 0)
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #473
        0xC,
        (
            "#070FAnyway! Once we get to the capital,\x01",
            "I should show my face at the Calvardian\x01",
            "embassy.\x02\x03",

            "Can't wait too long or Elsa\x01",
            "is going to give me hell.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)

    label("loc_D7C9")

    Return()

    # Function_53_C114 end

    def Function_54_D7CA(): pass

    label("Function_54_D7CA")

    EventBegin(0x0)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #474
        "\x07\x05Thank you for flying with us today.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #475
        "\x07\x05We will be arriving in Grancel shortly.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #476
        (
            "\x07\x05Please be aware that there may be turbulence\x01",
            "while landing, so we ask that all passengers\x01",
            "take their seats.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_54_D7CA end

    def Function_55_D8D9(): pass

    label("Function_55_D8D9")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x49)
    Return()

    # Function_55_D8D9 end

    def Function_56_D8F0(): pass

    label("Function_56_D8F0")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x1)
    Return()

    # Function_56_D8F0 end

    def Function_57_D907(): pass

    label("Function_57_D907")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
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
        (0, "loc_D982"),
        (1, "loc_D988"),
        (SWITCH_DEFAULT, "loc_D98E"),
    )


    label("loc_D982")

    OP_A2(0x1200)
    Jump("loc_D98E")

    label("loc_D988")

    OP_A2(0x1201)
    Jump("loc_D98E")

    label("loc_D98E")

    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_57_D907 end

    SaveToFile()

Try(main)
