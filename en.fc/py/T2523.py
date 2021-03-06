from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2523   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2523.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60075",
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
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Polly',                                # 11
        'Matron Theresa',                       # 12
        'Daniel',                               # 13
        'Mary',                                 # 14
        'Clem',                                 # 15
        'Princess Cecilia',                     # 16
        'Ruby Knight Julius',                   # 17
        'Azure Knight Oscar',                   # 18
        'Maid Laurel',                          # 19
        'Maid Rainey',                          # 20
        'Duke Radmont',                         # 21
        'Chairman Claude',                      # 22
        'Drunkard',                             # 23
        'Commoner',                             # 24
        'Royal Pontiff',                        # 25
        'Aristocrat',                           # 26
        'Aidios',                               # 27
        'Dean Collins',                         # 28
        'Duke Dunan',                           # 29
        'Phillip the Butler',                   # 30
        'Mayor Dalmore',                        # 31
        'Nial',                                 # 32
        'Captain Amalthea',                     # 33
        'Mayor Maybelle',                       # 34
        'Lila',                                 # 35
        'Loewe',                                # 36
        'Mickey',                               # 37
        'Janitor Parkes',                       # 38
        ' ',                                    # 39
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
        'Spectator',                            # 65
        'Spectator',                            # 66
        'Spectator',                            # 67
        'Spectator',                            # 68
        'Spectator',                            # 69
        'Spectator',                            # 70
        'Spectator',                            # 71
        'Spectator',                            # 72
        'Spectator',                            # 73
        'Spectator',                            # 74
        'Spectator',                            # 75
        'Spectator',                            # 76
        'Spectator',                            # 77
        'Spectator',                            # 78
        'Spectator',                            # 79
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02590 ._CH',             # 02
        'ED6_DT07/CH02640 ._CH',             # 03
        'ED6_DT07/CH02630 ._CH',             # 04
        'ED6_DT07/CH02570 ._CH',             # 05
        'ED6_DT07/CH02280 ._CH',             # 06
        'ED6_DT07/CH02260 ._CH',             # 07
        'ED6_DT07/CH02270 ._CH',             # 08
        'ED6_DT07/CH02540 ._CH',             # 09
        'ED6_DT07/CH01350 ._CH',             # 0A
        'ED6_DT07/CH02603 ._CH',             # 0B
        'ED6_DT07/CH01220 ._CH',             # 0C
        'ED6_DT07/CH01570 ._CH',             # 0D
        'ED6_DT06/CH20088 ._CH',             # 0E
        'ED6_DT07/CH02470 ._CH',             # 0F
        'ED6_DT07/CH02413 ._CH',             # 10
        'ED6_DT07/CH02063 ._CH',             # 11
        'ED6_DT07/CH02103 ._CH',             # 12
        'ED6_DT07/CH02363 ._CH',             # 13
        'ED6_DT07/CH02370 ._CH',             # 14
        'ED6_DT07/CH01040 ._CH',             # 15
        'ED6_DT07/CH01140 ._CH',             # 16
        'ED6_DT07/CH01670 ._CH',             # 17
        'ED6_DT07/CH01230 ._CH',             # 18
        'ED6_DT07/CH02040 ._CH',             # 19
        'ED6_DT07/CH01080 ._CH',             # 1A
        'ED6_DT07/CH01020 ._CH',             # 1B
        'ED6_DT07/CH02500 ._CH',             # 1C
        'ED6_DT06/CH20069 ._CH',             # 1D
        'ED6_DT06/CH20068 ._CH',             # 1E
        'ED6_DT06/CH20071 ._CH',             # 1F
        'ED6_DT06/CH20070 ._CH',             # 20
        'ED6_DT06/CH20072 ._CH',             # 21
        'ED6_DT06/CH20073 ._CH',             # 22
        'ED6_DT06/CH20075 ._CH',             # 23
        'ED6_DT06/CH20076 ._CH',             # 24
        'ED6_DT07/CH01223 ._CH',             # 25
        'ED6_DT07/CH01573 ._CH',             # 26
        'ED6_DT06/CH20131 ._CH',             # 27
        'ED6_DT06/CH20135 ._CH',             # 28
        'ED6_DT06/CH20136 ._CH',             # 29
        'ED6_DT07/CH02573 ._CH',             # 2A
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02590P._CP',             # 02
        'ED6_DT07/CH02640P._CP',             # 03
        'ED6_DT07/CH02630P._CP',             # 04
        'ED6_DT07/CH02570P._CP',             # 05
        'ED6_DT07/CH02280P._CP',             # 06
        'ED6_DT07/CH02260P._CP',             # 07
        'ED6_DT07/CH02270P._CP',             # 08
        'ED6_DT07/CH02540P._CP',             # 09
        'ED6_DT07/CH01350P._CP',             # 0A
        'ED6_DT07/CH02603P._CP',             # 0B
        'ED6_DT07/CH01220P._CP',             # 0C
        'ED6_DT07/CH01570P._CP',             # 0D
        'ED6_DT06/CH20088P._CP',             # 0E
        'ED6_DT07/CH02470P._CP',             # 0F
        'ED6_DT07/CH02413P._CP',             # 10
        'ED6_DT07/CH02063P._CP',             # 11
        'ED6_DT07/CH02103P._CP',             # 12
        'ED6_DT07/CH02363P._CP',             # 13
        'ED6_DT07/CH02370P._CP',             # 14
        'ED6_DT07/CH01040P._CP',             # 15
        'ED6_DT07/CH01140P._CP',             # 16
        'ED6_DT07/CH01670P._CP',             # 17
        'ED6_DT07/CH01230P._CP',             # 18
        'ED6_DT07/CH02040P._CP',             # 19
        'ED6_DT07/CH01080P._CP',             # 1A
        'ED6_DT07/CH01020P._CP',             # 1B
        'ED6_DT07/CH02500P._CP',             # 1C
        'ED6_DT06/CH20069P._CP',             # 1D
        'ED6_DT06/CH20068P._CP',             # 1E
        'ED6_DT06/CH20071P._CP',             # 1F
        'ED6_DT06/CH20070P._CP',             # 20
        'ED6_DT06/CH20072P._CP',             # 21
        'ED6_DT06/CH20073P._CP',             # 22
        'ED6_DT06/CH20075P._CP',             # 23
        'ED6_DT06/CH20076P._CP',             # 24
        'ED6_DT07/CH01223P._CP',             # 25
        'ED6_DT07/CH01573P._CP',             # 26
        'ED6_DT06/CH20131P._CP',             # 27
        'ED6_DT06/CH20135P._CP',             # 28
        'ED6_DT06/CH20136P._CP',             # 29
        'ED6_DT07/CH02573P._CP',             # 2A
    )

    DeclNpc(
        X                   = 59640,
        Z                   = 1000,
        Y                   = 13450,
        Direction           = 90,
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
        X                   = 66040,
        Z                   = 1000,
        Y                   = 16210,
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
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4300,
        Z                   = 200,
        Y                   = 2900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -64500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -30,
        Z                   = 0,
        Y                   = -2630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        X                   = -3500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 7100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65575,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 852007,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131111,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196647,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262183,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 5100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589863,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655399,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 720935,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 3100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327719,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 852007,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917543,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 983079,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1048615,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1114151,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179687,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245223,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = 1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 393255,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1376295,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1441831,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458791,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65575,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131111,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196647,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262183,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 200,
        Y                   = -900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_AE2",          # 00, 0
        "Function_1_C1D",          # 01, 1
        "Function_2_C1E",          # 02, 2
        "Function_3_D9B",          # 03, 3
        "Function_4_DDA",          # 04, 4
        "Function_5_E9B",          # 05, 5
        "Function_6_1071",         # 06, 6
        "Function_7_10EE",         # 07, 7
        "Function_8_1123",         # 08, 8
        "Function_9_1171",         # 09, 9
        "Function_10_11CE",        # 0A, 10
        "Function_11_11FA",        # 0B, 11
        "Function_12_1A6C",        # 0C, 12
        "Function_13_21A3",        # 0D, 13
        "Function_14_2205",        # 0E, 14
        "Function_15_226C",        # 0F, 15
        "Function_16_22D8",        # 10, 16
        "Function_17_52E8",        # 11, 17
        "Function_18_964B",        # 12, 18
        "Function_19_9698",        # 13, 19
        "Function_20_96E5",        # 14, 20
        "Function_21_9732",        # 15, 21
        "Function_22_977F",        # 16, 22
        "Function_23_97BD",        # 17, 23
    )


    def Function_0_AE2(): pass

    label("Function_0_AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_AEC")
    Jump("loc_BE9")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_AF6")
    Jump("loc_BE9")

    label("loc_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_BA1")
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, -64400, 0, 3560, 270)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 140, 0, 7810, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, -37340, 1000, 5500, 0)
    SetChrPos(0xE, -33510, 1000, 7750, 90)
    SetChrPos(0xC, -34240, 1000, 8280, 45)
    SetChrPos(0xA, -37450, 1000, 9490, 0)
    SetChrPos(0xD, -36430, 1000, 8790, 0)
    OP_43(0xC, 0x0, 0x0, 0x3)
    Jump("loc_BE9")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_BB0")
    ClearChrFlags(0x25, 0x80)
    Jump("loc_BE9")

    label("loc_BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_BBA")
    Jump("loc_BE9")

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_BC4")
    Jump("loc_BE9")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_BCE")
    Jump("loc_BE9")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_BD8")
    Jump("loc_BE9")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_BE2")
    Jump("loc_BE9")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_BE9")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C00")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_C0E")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_C1C")
    OP_A3(0x3FC)
    Event(0, 16)

    label("loc_C1C")

    Return()

    # Function_0_AE2 end

    def Function_1_C1D(): pass

    label("Function_1_C1D")

    Return()

    # Function_1_C1D end

    def Function_2_C1E(): pass

    label("Function_2_C1E")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C43")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D85")

    label("loc_C43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D85")

    label("loc_C5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D85")

    label("loc_C75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D85")

    label("loc_C8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D85")

    label("loc_CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D85")

    label("loc_CC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D85")

    label("loc_CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF2")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D85")

    label("loc_CF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D85")

    label("loc_D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D24")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D85")

    label("loc_D24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D85")

    label("loc_D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D56")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D85")

    label("loc_D56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D85")

    label("loc_D6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D85")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D9A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D85")

    label("loc_D9A")

    Return()

    # Function_2_C1E end

    def Function_3_D9B(): pass

    label("Function_3_D9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD9")
    OP_8F(0xFE, 0xFFFF76EE, 0x3E8, 0x23BE, 0x7D0, 0x0)
    Sleep(5000)
    OP_8F(0xFE, 0xFFFF7856, 0x3E8, 0x21DE, 0x7D0, 0x0)
    Sleep(5000)
    Jump("Function_3_D9B")

    label("loc_DD9")

    Return()

    # Function_3_D9B end

    def Function_4_DDA(): pass

    label("Function_4_DDA")

    TalkBegin(0x24)

    ChrTalk(    #0
        0xFE,
        "Man, this is so dull.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I didn't want to have anything to\x01",
            "do with the play, and I didn't sign\x01",
            "up for this either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "This is all because of the damn\x01",
            "Student Council president.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x24)
    Return()

    # Function_4_DDA end

    def Function_5_E9B(): pass

    label("Function_5_E9B")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(    #3
        0xFE,
        (
            "It's almost time for the\x01",
            "play to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "They'll be calling for all of the\x01",
            "performers soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106D")

    label("loc_F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_106D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_FC6")

    ChrTalk(    #5
        0xFE,
        (
            "Until your big show, the auditorium's\x01",
            "not actually being used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Except by me, of course. Dean Collins\x01",
            "asked me to do a safety check before\x01",
            "the main event.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106D")

    label("loc_FC6")


    ChrTalk(    #7
        0xFE,
        (
            "Whew...I was busy all day putting\x01",
            "up those decorations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I made it, but just barely. And I\x01",
            "wouldn't have even managed that\x01",
            "without the help of some students.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106D")

    TalkEnd(0x25)
    Return()

    # Function_5_E9B end

    def Function_6_1071(): pass

    label("Function_6_1071")

    TalkBegin(0xE)

    ChrTalk(    #9
        0xFE,
        (
            "#772FPolly picks up on a lot of\x01",
            "different things...\x02\x03",

            "...but she always makes a beeline\x01",
            "for everything she spots.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_6_1071 end

    def Function_7_10EE(): pass

    label("Function_7_10EE")

    TalkBegin(0xC)

    ChrTalk(    #10
        0xFE,
        "I sure can't wait for the play to start.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_7_10EE end

    def Function_8_1123(): pass

    label("Function_8_1123")

    TalkBegin(0xA)

    ChrTalk(    #11
        0xFE,
        (
            "Misser Joshua wen'off to look for\x01",
            "the man with the pretty hair...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_8_1123 end

    def Function_9_1171(): pass

    label("Function_9_1171")

    TalkBegin(0xD)

    ChrTalk(    #12
        0xFE,
        "*sigh* What a beautiful dress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I'd love something like that\x01",
            "when I grow up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_9_1171 end

    def Function_10_11CE(): pass

    label("Function_10_11CE")

    TalkBegin(0xB)

    ChrTalk(    #14
        0xFE,
        "#752FHave you found Joshua yet?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_10_11CE end

    def Function_11_11FA(): pass

    label("Function_11_11FA")

    AddParty(0x1, 0xFF)
    EventBegin(0x0)
    OP_6D(60000, 1000, 15800, 0)
    OP_67(0, 6230, -10000, 0)
    OP_6B(1420, 0)
    OP_6C(0, 0)
    OP_6E(672, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x101, 60020, 1000, 13500, 0)
    SetChrPos(0x105, 61000, 1000, 14070, 315)
    SetChrPos(0x102, 59020, 1000, 14260, 45)
    SetChrPos(0x9, 59630, 1000, 15700, 180)
    SetChrPos(0x8, 60430, 1000, 15570, 180)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    Sleep(3000)
    OP_1E()
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #15
        0x8,
        (
            "#644F#4PThe stage is set perfectly...\x02\x03",

            "The lights are just right...\x02\x03",

            "#641FOkay! Looks like we're ready\x01",
            "to unleash our masterpiece!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#730F#3PWe'll be opening soon.\x02\x03",

            "We've got a bit before everything\x01",
            "starts, though. Go have some fun\x01",
            "in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#001FNow you're talking. ♪\x02\x03",

            "I'm gonna stuff my face with\x01",
            "something from every food\x01",
            "stand out there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#019FLooking around is fine...\x02\x03",

            "But if you eat too much,\x01",
            "you'll be too full to move\x01",
            "in the play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#000FY-Yeah... I probably shouldn't\x01",
            "overdo it.\x02\x03",

            "#000FHey, aren't you guys gonna\x01",
            "come with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#640F#4PCan't. We've still got student\x01",
            "council business to deal with.\x02\x03",

            "You'll be fine. Go have some fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#004FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        (
            "#044FWhat Student Council business?\x01",
            "And didn't you say the same\x01",
            "thing yesterday?\x02\x03",

            "Is there something I can do\x01",
            "to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#648F#4PWe're fine, I promise.\x02\x03",

            "All you need to do is show\x01",
            "Estelle and Joshua around.\x02\x03",

            "Aren't the pipsqueaks gonna\x01",
            "be showing up soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        "#043FOh...right. Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#730F#3PWe'll have time enough to go\x01",
            "out and enjoy the festival.\x02\x03",

            "#733FOh, yeah...and, Joshua?\x02\x03",

            "#731FIf you see any hot girls out there,\x01",
            "I expect you to beeline it right\x01",
            "back here and tell me, got it?\x02\x03",

            "I wouldn't want any of them\x01",
            "missing out on the pleasure\x01",
            "of my company. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#017FYeah, yeah, I got it.\x02\x03",

            "#010FTall, gorgeous, sensual, charming...\x01",
            "Did I miss anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "#731F#3PMy friend, I couldn't have said\x01",
            "it better, myself. ♪\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x89, 1)), scpexpr(EXPR_END)), "loc_18C6")

    ChrTalk(    #28
        0x8,
        "#645F#4PI swear, you're hopeless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#503F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x105,
        "#045F...Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "#643F#4PWhat's up, gals?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1926")

    label("loc_18C6")


    ChrTalk(    #32
        0x8,
        "#645F#4PHmph... Men.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#007FSeriously.\x01",
            "Talk about one track minds...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#045FHa ha...\x02",
    )

    CloseMessageWindow()

    label("loc_1926")

    OP_22(0xC4, 0x0, 0x64)
    OP_20(0x5DC)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #35
        (
            "\x07\x05The time you've all been waiting\x01",
            "for has finally arrived...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #36
        (
            "\x07\x05The 52nd Jenis Royal Academy\x01",
            "campus festival has begun!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_11FA end

    def Function_12_1A6C(): pass

    label("Function_12_1A6C")

    RemoveParty(0x1, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-34250, 1000, 11220, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, -36570, 250, 850, 0)
    SetChrPos(0x105, -36570, 250, 850, 0)
    SetChrPos(0xB, -36570, 250, 850, 0)
    SetChrPos(0xA, -35500, 1000, 9370, 0)
    SetChrPos(0xC, -36440, 1000, 8910, 0)
    SetChrPos(0xD, -37080, 1000, 9450, 0)
    SetChrPos(0xE, -36170, 1000, 9850, 0)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xB, 255)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #37
        0xE,
        (
            "#771F#2PWhoa... This is so cool!\x02\x03",

            "I wonder if I could wear it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        "Not with how short you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        "I wish I could try on a white dress.\x02",
    )

    CloseMessageWindow()

    def lambda_1C16():
        OP_6D(-34950, 1000, 8980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C16)
    OP_43(0x101, 0x1, 0x0, 0xD)
    OP_43(0x105, 0x1, 0x0, 0xE)
    OP_43(0xB, 0x1, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #40
        0x101,
        (
            "#001F#2PWell, well. You look like you're\x01",
            "having fun.\x02\x03",

            "#004FHuh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #41
        0x101,
        "#004F#2PWhere'd Joshua go?\x02",
    )

    CloseMessageWindow()

    def lambda_1CC8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CC8)
    Sleep(100)

    def lambda_1CDB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1CDB)

    def lambda_1CE9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CE9)
    Sleep(100)

    def lambda_1CFC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1CFC)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #42
        0xE,
        (
            "#774FMr. Joshua?\x02\x03",

            "He left after he brought us here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "He said, 'Wait here until the\x01",
            "girls arrive.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#002F#2PHmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        "#043FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        "#3PHee hee... I's knows.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#3PMisser Joshua went lookin' for\x01",
            "th' guy with silver hair.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xA, 400)
    TurnDirection(0x101, 0xA, 400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x101,
        "#501F#2PSilver hair?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#3PYah! He helped us get outta th'\x01",
            "fire before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        "#3PHis hair's all shiny and pretty...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        "#004F#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#044FS-So he's been seen on campus?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        "#3PUh-huh. Just for a second, doh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        "#3PMisser Joshua was sure surprised.\x02",
    )

    CloseMessageWindow()
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0xA, 400)

    ChrTalk(    #55
        0xE,
        (
            "#772FPolly, you dummy.\x02\x03",

            "Why didn't you come and tell\x01",
            "any of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        "#2PCause I was eatin' a crepe!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #57
        0x105,
        "#042FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#002F#2PI know...\x02\x03",

            "#002FI'll be right back, Matron.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #59
        0xB,
        (
            "#750FYes, that's fine.\x02\x03",

            "Kloe, would you please go\x01",
            "with her?\x02\x03",

            "Don't worry about us.\x01",
            "We'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(    #60
        0x105,
        "#043FBy your leave, Matron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xC,
        "Hey, you're going, too?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xE, 400)

    ChrTalk(    #62
        0x105,
        (
            "#045FYes... I'm sorry.\x02\x03",

            "#040FWe'll see you at the play.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #63
        0x101,
        (
            "#006F#2PYeah! It's gonna knock your\x01",
            "socks off. ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2500   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1A6C end

    def Function_13_21A3(): pass

    label("Function_13_21A3")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7478, 0x0, 0xC08, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7AD6, 0x0, 0x143C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7A40, 0x3E8, 0x1CDE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFF7068, 0x3E8, 0x1C20, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_21A3 end

    def Function_14_2205(): pass

    label("Function_14_2205")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7478, 0x0, 0xC08, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7AD6, 0x0, 0x143C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7A40, 0x3E8, 0x1CDE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFF74AA, 0x3E8, 0x1BEE, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_2205 end

    def Function_15_226C(): pass

    label("Function_15_226C")

    Sleep(500)
    Sleep(700)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF7478, 0x0, 0xC08, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7AD6, 0x0, 0x143C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFF7A40, 0x3E8, 0x1CDE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFF7842, 0x3E8, 0x2166, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_226C end

    def Function_16_22D8(): pass

    label("Function_16_22D8")

    AddParty(0x1, 0xFF)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(2220, 0, 290, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    SetChrPos(0x1D, 500, 0, 7200, 0)
    SetChrPos(0x1C, -500, 200, 7200, 0)
    SetChrPos(0x1E, -2500, 200, 7200, 0)
    SetChrPos(0x1B, -3500, 200, 7200, 0)
    SetChrPos(0x20, 2500, 200, 5200, 0)
    SetChrPos(0x21, 2500, 200, 7200, 0)
    SetChrPos(0x22, 3500, 0, 7200, 0)
    SetChrPos(0xD, -3500, 200, 3200, 0)
    SetChrPos(0xA, -2500, 200, 3200, 0)
    SetChrPos(0xB, -1500, 200, 3200, 0)
    SetChrPos(0xC, -500, 200, 3200, 0)
    SetChrPos(0xE, 500, 200, 3200, 0)
    SetChrChipByIndex(0xB, 42)
    SetChrSubChip(0xB, 0)
    OP_44(0xD, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrPos(0x1F, 3500, 200, -800, 0)
    SetChrPos(0x23, 0, -250, -5430, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4700, 1000, 14420, 180)
    FadeToBright(2000, 0)
    OP_6D(4700, 1000, 14420, 5000)
    OP_8C(0x10, 90, 400)
    OP_8E(0x10, 0x17AC, 0x3E8, 0x394E, 0xBB8, 0x0)
    Fade(1000)
    OP_6D(-34890, 1000, 8480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x14, -36680, 1000, 9450, 180)
    SetChrPos(0x15, -37710, 1000, 8930, 180)
    SetChrPos(0x16, -37550, 1000, 9790, 180)
    SetChrPos(0x18, 60020, 1000, 18870, 180)
    SetChrPos(0x12, -34800, 1000, 8460, 225)
    SetChrPos(0x13, -34310, 1000, 7560, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xF, -35990, 1000, 8670, 180)
    SetChrPos(0x11, -36100, 1000, 7440, 270)
    SetChrPos(0x10, -40540, 1000, 6830, 180)
    SetChrPos(0x8, -36960, 1000, 5930, 0)
    SetChrPos(0x9, -37860, 1000, 6000, 0)

    def lambda_2692():

        label("loc_2692")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2692")

    QueueWorkItem2(0xF, 1, lambda_2692)

    def lambda_26A3():

        label("loc_26A3")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_26A3")

    QueueWorkItem2(0x8, 1, lambda_26A3)

    def lambda_26B4():

        label("loc_26B4")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_26B4")

    QueueWorkItem2(0x9, 1, lambda_26B4)
    OP_8E(0x10, 0xFFFF6D5C, 0x3E8, 0x1D9C, 0xBB8, 0x0)

    NpcTalk(    #64
        0x10,
        "Estelle",
        (
            "#343FWow... Look at all the people!\x02\x03",

            "#347FOkay, now I'm getting kinda\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x11,
        "Kloe",
        (
            "#355F#2PYou'll be fine, Estelle.\x01",
            "This is what all the\x01",
            "rehearsals were for.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #66
        0xF,
        "Joshua",
        (
            "#360F#6PBesides, once we start up,\x01",
            "you'll forget they're even there.\x02\x03",

            "You're the type who can only\x01",
            "focus on one thing at a time,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #67
        0x10,
        "Estelle",
        (
            "#349FJust one thing at a time, huh?\x02\x03",

            "#341FWell, I guess I'll just focus\x01",
            "on the boy in the dress then.\x01",
            "That'll be easy. ㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #68
        0xF,
        "Joshua",
        "#368F#6PEr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#644F#2POkay, okay... You two can have\x01",
            "your little spat another time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x8, 400)
    TurnDirection(0x11, 0x8, 400)
    Sleep(500)

    ChrTalk(    #70
        0x8,
        (
            "#644F#2PAhem! This year's campus festival\x01",
            "is already a big success.\x02\x03",

            "Though we have many esteemed individuals\x01",
            "here, such as the duke and the mayor, we\x01",
            "can't afford to be intimidated.\x02\x03",

            "#648FSo just remember our number one rule and\x01",
            "you'll be fine. If you're gonna puke...\x01",
            "do it off stage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#730F#2PWe've done a good job of\x01",
            "keeping the festival lively,\x01",
            "so far...\x02\x03",

            "#731FNow, let's close it out with\x01",
            "a real bang!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_6D(63040, 4300, 7500, 0)
    OP_20(0x3E8)
    OP_72(0x9, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_44(0xF, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Sleep(1000)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_22(0x8B, 0x0, 0x64)
    Sleep(9000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #72
        "\x07\x05Without further ado...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        (
            "\x07\x05The Student Council proudly presents,\x01",
            "'Madrigal of the White Magnolia.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        "\x07\x05Enjoy the show...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMapFlags(0x4)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x2E, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x26, 0x4)
    SetChrPos(0x26, 63580, 2000, 13750, 180)
    SetChrPos(0x8, 63580, 1000, 13750, 180)

    label("loc_2C32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C57")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C53")
    Jump("loc_2C57")

    label("loc_2C53")

    OP_48()
    Jump("loc_2C32")

    label("loc_2C57")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(    #75
        0x8,
        (
            "#647F#5PIn year 1100 of the Septian Calendar...one hundred \x01",
            "years ago...\x02\x03",

            "...Liberl was still a land of nobles and aristocrats.\x02\x03",

            "#642FBut commoners, too, held some power, and they\x01",
            "were prodigious traders that grew more influential\x01",
            "with each passing year.\x02\x03",

            "During this period there was much friction between\x01",
            "the classes, and the nobles and commoners clashed\x01",
            "often. As time went on, these clashes intensified.\x02\x03",

            "#647FThe intercession of the royal family and the church\x01",
            "failed to end their squabbling...\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x5D)
    SetChrPos(0xF, 60000, 1000, 14400, 180)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2E82():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E82)

    label("loc_2E8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EB3")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EAF")
    Jump("loc_2EB3")

    label("loc_2EAF")

    OP_48()
    Jump("loc_2E8E")

    label("loc_2EB3")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #76
        0x8,
        (
            "#644F#5PThe stage was set for a final\x01",
            "conflict...\x02\x03",

            "A year had passed since illness\x01",
            "stole the king from his people.\x02\x03",

            "Our tale begins on an early\x01",
            "spring evening, in the rooftop\x01",
            "garden of Grancel Castle...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F92():
        OP_8F(0xFE, 0xEA60, 0x8FC, 0x3CC8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2F92)

    def lambda_2FAD():
        OP_6D(60010, 4300, 7500, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2FAD)
    OP_8C(0x8, 315, 400)
    OP_8E(0x8, 0xF30C, 0x3E8, 0x3D72, 0x7D0, 0x0)
    OP_8E(0x8, 0xF4BA, 0x3E8, 0x422C, 0x7D0, 0x0)
    OP_8E(0x8, 0x10040, 0x3E8, 0x4934, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x26, 0x1)
    SetChrPos(0x13, 55350, 1000, 17130, 90)
    SetChrPos(0x12, 55440, 1000, 18180, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_77(0x5A, 0x5A, 0x5A, 0x3E800, 0x0)
    WaitChrThread(0x26, 0x1)
    Sleep(1500)

    ChrTalk(    #77
        0xF,
        (
            "#363F#5PThe street lights shine\x01",
            "on everyone...\x02\x03",

            "Each bright with their own\x01",
            "happiness.\x02\x03",

            "#365FAnd in spite of that...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)

    def lambda_30D9():
        OP_8E(0xFE, 0xEFCE, 0x3E8, 0x41F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_30D9)
    Sleep(700)

    def lambda_30F9():
        OP_8E(0xFE, 0xE54C, 0x3E8, 0x413C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_30F9)
    WaitChrThread(0x13, 0x1)

    def lambda_3119():
        OP_8C(0xFE, 135, 300)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3119)
    WaitChrThread(0x12, 0x1)

    def lambda_312C():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_312C)
    Sleep(500)

    ChrTalk(    #78
        0x13,
        "#1PAh, here you are, Princess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x12,
        (
            "#2PPlease, don't you think you\x01",
            "should be going to bed soon,\x01",
            "Your Royal Highness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        (
            "#2PStaying up so late can\x01",
            "surely do you no good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xF,
        (
            "#363F#5PIt's all right.\x01",
            "If I should fall ill...\x02\x03",

            "If that happened, then perhaps I could\x01",
            "avoid becoming the last ember in this\x01",
            "dying flame we call Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x13,
        (
            "#1PPlease, do not speak of\x01",
            "such things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x12,
        (
            "#2PYour Highness, you are the\x01",
            "most exalted individual in\x01",
            "Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x12,
        (
            "#2PIf you were to take a husband,\x01",
            "you could take control of the\x01",
            "kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        (
            "#367F#5PI will not marry.\x02\x03",

            "Despite my father's wishes,\x01",
            "I shall not consent to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x13,
        "#1PBut why, Your Highness?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x13,
        (
            "#1PYou have two fine men as\x01",
            "suitors, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        (
            "#2POne is Sir Julius, of the Chivalric\x01",
            "Order of the Imperial Guards...\x01",
            "and the eldest son of a duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x13,
        (
            "#1PAnd Sir Oscar. Commoner though he\x01",
            "may be, he has been recognized often\x01",
            "in his battles against the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #90
        0x12,
        "#2P#1K*sigh* Both such fine men! ㈱\x02",
    )


    ChrTalk(    #91
        0x13,
        "#1P#1K*sigh* Both such fine men! ㈱\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    OP_56(0x1)
    OP_59()
    Sleep(400)

    ChrTalk(    #92
        0xF,
        (
            "#363F#5P...\x02\x03",

            "No one knows better than I the\x01",
            "quality of their characters...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 180, 300)
    Sleep(200)
    OP_8E(0xF, 0xEA74, 0x3E8, 0x3142, 0x5DC, 0x0)
    SetChrChipByIndex(0xF, 41)
    SetChrFlags(0xF, 0x2)
    OP_99(0xF, 0x0, 0x4, 0x3E8)
    Sleep(400)

    ChrTalk(    #93
        0xF,
        (
            "#365F#5POh, Oscar...Julius...\x02\x03",

            "How am I to choose between you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_66(0x1)
    OP_6D(3120, 0, 7140, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(    #94
        0x21,
        (
            "#611F#6P(Oh, my... Isn't that Joshua playing\x01",
            "the role of the princess?)\x02\x03",

            "(Ha ha... I suppose that Jill has\x01",
            "put a great deal of thought into\x01",
            "this reverse-casting business.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x22,
        (
            "#621F#6P(Indeed, ma'am.)\x02\x03",

            "#623F(He plays his role well, but the\x01",
            "two maids leave much to be desired.)\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    Call(0, 22)
    OP_71(0x9, 0x4)
    OP_72(0xA, 0x4)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 61060, 1000, 14810, 242)
    SetChrPos(0x11, 58970, 1000, 12820, 47)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x12)
    OP_1D(0x5E)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #96
        0x10,
        (
            "#420F#2PDo you remember, Oscar?\x02\x03",

            "How we spent our boyhood days in\x01",
            "this alley, running about and\x01",
            "pretending our sticks were swords?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x11,
        (
            "#352FI could never forget, Julius.\x02\x03",

            "In those days, it was all\x01",
            "so simple. With you and\x01",
            "with Cecilia alike.\x02\x03",

            "I treasure that time greatly.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    def lambda_3932():

        label("loc_3932")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_3932")

    QueueWorkItem2(0x11, 0, lambda_3932)
    OP_8E(0x10, 0xEE3E, 0x3E8, 0x323C, 0x7D0, 0x0)

    ChrTalk(    #98
        0x10,
        (
            "#420FHa ha... I recall how stunned\x01",
            "I was.\x02\x03",

            "I would always conspire to play with\x01",
            "her in secret, only to discover another\x01",
            "had been doing the same...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    OP_8C(0x11, 180, 300)

    ChrTalk(    #99
        0x11,
        (
            "#358FShe was as lovely as the\x01",
            "sight of the falling petals\x01",
            "in spring...\x02\x03",

            "Indeed, fair Cecilia was like\x01",
            "unto our very own sun.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 225, 300)

    ChrTalk(    #100
        0x10,
        (
            "#421FBut her light would dim with\x01",
            "each day that passed.\x02\x03",

            "The nobles and the commoners...\x02\x03",

            "The fury of that conflict could\x01",
            "never have been avoided.\x02\x03",

            "#424FThe princess' grief is\x01",
            "easily understandable...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 135, 300)

    ChrTalk(    #101
        0x11,
        (
            "#359FCruel fate mocks us so...\x02\x03",

            "For it is our very existence that\x01",
            "has brought her such sorrow.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_6D(-1340, 0, 3500, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(    #102
        0xD,
        "#6P(Oh, wow! They're so cool!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xE,
        (
            "#774F#6P(I hate to say it...but the\x01",
            "guy kinda looks cuter than\x01",
            "the girls...!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        (
            "#751F#6P(Ha ha... Hush now, and\x01",
            "watch the show.)\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_71(0xA, 0x4)
    OP_72(0xB, 0x4)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 37)
    SetChrPos(0x14, 57800, 1200, 17630, 135)
    SetChrPos(0x10, 60510, 1000, 13460, 315)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x13)
    FadeToBright(1000, 0)
    OP_1D(0x5F)
    OP_0D()

    ChrTalk(    #105
        0x14,
        "#5PKnow this, Julius.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x14,
        (
            "#5PThe commoners' impudence can\x01",
            "be tolerated no longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x14,
        (
            "#5PIf they should forget their\x01",
            "place and no longer view us\x01",
            "as their superiors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x14,
        (
            "#5PLiberl's power structure would\x01",
            "surely fall into ruin.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xE6F0, 0x3E8, 0x3B38, 0x7D0, 0x0)

    ChrTalk(    #109
        0x10,
        (
            "#424F#2PIf I may, Father...\x02\x03",

            "It has been roughly ten years since the Eastern\x01",
            "Republic was founded.\x02\x03",

            "#421FPerhaps the eventual seizing of power by the\x01",
            "common people is inevitable in any state.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F16():

        label("loc_3F16")

        TurnDirection(0xFE, 0x14, 0)
        OP_48()
        Jump("loc_3F16")

    QueueWorkItem2(0x10, 0, lambda_3F16)
    SetChrChipByIndex(0x14, 12)
    OP_96(0x14, 0xE0A6, 0x3E8, 0x4286, 0x12C, 0x1388)
    OP_8E(0x14, 0xE07E, 0x3E8, 0x3BB0, 0xBB8, 0x0)
    TurnDirection(0x14, 0x10, 800)

    ChrTalk(    #110
        0x14,
        "#5P#3SSpeak not of such repulsive events!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x14, 0x40)
    OP_92(0x14, 0x10, 0x190, 0xBB8, 0x0)

    def lambda_3FB1():
        OP_94(0x1, 0x14, 0x0, 0x12C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3FB1)
    OP_94(0x1, 0x10, 0xB4, 0x258, 0xBB8, 0x0)
    OP_94(0x1, 0x10, 0xB4, 0x12C, 0x5DC, 0x0)
    WaitChrThread(0x14, 0x3)

    ChrTalk(    #111
        0x14,
        "#5P#3SWhat is freedom?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x14, 0x40)
    OP_92(0x14, 0x10, 0x190, 0xBB8, 0x0)

    def lambda_402A():
        OP_94(0x1, 0x14, 0x0, 0x12C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_402A)
    OP_94(0x1, 0x10, 0xB4, 0x258, 0xBB8, 0x0)
    OP_94(0x1, 0x10, 0xB4, 0x12C, 0x5DC, 0x0)
    WaitChrThread(0x14, 0x3)

    ChrTalk(    #112
        0x14,
        "#5P#3SWhat is equality?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #113
        0x14,
        (
            "#5PWhat is ANYTHING, if commoners\x01",
            "and nobles alike should\x01",
            "cast all tradition aside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x14,
        (
            "#5PBetter we should fall to our knees\x01",
            "before the Empire's military, and\x01",
            "concede to their will!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #115
        0x10,
        "#422F#2P#3SFather!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_44(0x10, 0xFF)
    OP_77(0x5A, 0x5A, 0x5A, 0x0, 0x0)
    OP_6D(20, 0, 6850, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(    #116
        0x1C,
        (
            "#227F#6P*hic*... Now that's a damn\x01",
            "fine duke up there...\x02\x03",

            "You let the commoners get all\x01",
            "high and mighty, and your\x01",
            "whole society collapses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x1D,
        (
            "#722F#6P(Your Grace...perhaps\x01",
            "it would be best to keep\x01",
            "our voices down...?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_71(0xB, 0x4)
    OP_72(0xC, 0x4)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x15)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x15, 58930, 1000, 17140, 138)
    SetChrPos(0x11, 61080, 1000, 15250, 336)

    def lambda_4339():

        label("loc_4339")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_4339")

    QueueWorkItem2(0x11, 1, lambda_4339)
    OP_1F(0x64, 0xC8)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #118
        0x15,
        "#5POscar, I am expecting great things from you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x15,
        (
            "#5PIf you can get the royal family on our side,\x01",
            "we will have a great advantage over the nobles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x15,
        (
            "#5PAnd that advantage would allow us to seize\x01",
            "power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        (
            "#352F#2PBut, Chairman...\x01",
            "I cannot consent to this.\x02\x03",

            "I could never use Cecilia\x01",
            "for political gain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x15,
        (
            "#5PHa ha... Always putting others before yourself,\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x15,
        (
            "#5PEven though you now have the chance to become\x01",
            "king, albeit only on paper.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x15, 0xE678, 0x3E8, 0x348A, 0x7D0, 0x0)
    OP_8C(0x15, 223, 300)
    Sleep(300)

    ChrTalk(    #124
        0x15,
        (
            "#5PIf you would refuse, it will\x01",
            "lead only to a bloody uprising\x01",
            "and subsequent revolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x15,
        (
            "#5PThe royal family, and surely the\x01",
            "nobles as well, would disappear\x01",
            "into the shadows of history.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #126
        0x11,
        "#356F#2P#3SChairman!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_44(0x26, 0xFF)
    Sleep(100)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_44(0x11, 0xFF)
    OP_77(0x5A, 0x5A, 0x5A, 0x0, 0x0)
    OP_6D(-2940, 0, 7230, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(    #127
        0x1E,
        (
            "#661F(Impressive. They've\x01",
            "really done their research.)\x02\x03",

            "(I had severe doubts about this,\x01",
            "ever since I first heard about\x01",
            "the reverse-role gimmick.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x1B,
        (
            "#781F(Ha ha... The students have\x01",
            "all put a great deal of work\x01",
            "into this, it seems.)\x02\x03",

            "#780F(The young bracers have\x01",
            "had no small hand in this,\x01",
            "either... )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 22)
    OP_71(0xC, 0x4)
    OP_72(0xD, 0x4)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x26, 60000, 1000, 14500, 135)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x11, 59530, 1000, 13290, 135)
    SetChrPos(0x16, 64230, 1000, 18550, 60)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_1F(0x64, 0xC8)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #129
        0x11,
        (
            "#357F#5PI do not wish bloodshed on\x01",
            "anyone, revolution or not.\x02\x03",

            "I cannot simply allow Julius\x01",
            "and Cecilia to die...\x02\x03",

            "#359FAs for myself... I know\x01",
            "not what I should do.\x02",
        )
    )

    CloseMessageWindow()
    OP_77(0x5A, 0x5A, 0x5A, 0x7D000, 0x0)

    def lambda_48E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_48E0)
    OP_8E(0x16, 0xF122, 0x3E8, 0x418C, 0x7D0, 0x0)

    ChrTalk(    #130 op#A op#5
        0x16,
        "#10A#5POouuughhh...\x05\x02",
    )


    def lambda_491F():
        TurnDirection(0x11, 0x16, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_491F)
    OP_97(0x16, 0xF38E, 0x3D22, 0xFFFE2B40, 0x7D0, 0x0)
    OP_97(0x16, 0xF38E, 0x3D22, 0x2710, 0xFA0, 0x0)
    OP_97(0x16, 0xF38E, 0x3D22, 0xFFFFD8F0, 0xFA0, 0x0)

    def lambda_496C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_496C)
    OP_9E(0x16, 0x1E, 0x0, 0x1F4, 0xBB8)

    ChrTalk(    #131
        0x16,
        (
            "#5PUhh... S'no good...\x01",
            "I'm gonna be sick...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x16, 400)
    TurnDirection(0x11, 0x16, 400)

    ChrTalk(    #132
        0x11,
        "#354F#5PAre you all right?\x02",
    )

    CloseMessageWindow()
    OP_8E(0x11, 0xEDB2, 0x3E8, 0x3610, 0x7D0, 0x0)

    ChrTalk(    #133
        0x11,
        (
            "#352F#5PYou must have had quite a bit\x01",
            "more than you can handle.\x02\x03",

            "It may be spring, but you'll\x01",
            "surely catch your death if\x01",
            "you sleep out here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x11, 200)

    ChrTalk(    #134
        0x16,
        (
            "#2PUrrr... Thank you...\x01",
            "good sir knight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x11,
        (
            "#357F#5PIt has nothing to do with\x01",
            "being a knight...but rather\x01",
            "simple concern.\x02\x03",

            "#359FI would have to be quite\x01",
            "the young fool not to see\x01",
            "what I must do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x16,
        "#2PYou've got that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x11,
        "#354F#5PWhat?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x16, 0x4)
    OP_92(0x16, 0x11, 0x190, 0x1F40, 0x0)
    OP_22(0x1FD, 0x0, 0x64)

    def lambda_4BB6():
        OP_94(0x1, 0x16, 0x0, 0x12C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4BB6)
    TurnDirection(0x11, 0x16, 0)
    OP_94(0x1, 0x11, 0xB4, 0x3E8, 0x1F40, 0x0)
    OP_94(0x1, 0x11, 0xB4, 0x1F4, 0xFA0, 0x0)
    LoadEffect(0x0, "map\\\\mp020_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 60320, 1050, 12670, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x16, 0x3)
    OP_77(0xA0, 0x1E, 0x1E, 0x5DC00, 0x0)
    Fade(1000)
    SetChrChipByIndex(0x11, 34)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)
    OP_9E(0x11, 0x1E, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #138
        0x11,
        "#430FAgh! My arm...\x02",
    )

    CloseMessageWindow()
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x16, 0xF44C, 0x76C, 0x3BEC, 0x708, 0x1388)

    ChrTalk(    #139
        0x16,
        (
            "#2PHeh heh heh... Just a touch\x01",
            "of anesthetic on the blade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x16,
        (
            "#2PNow, if you'll be so kind\x01",
            "as to sit still...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x11, 0x0, 0x4, 0x320)

    ChrTalk(    #141
        0x11,
        (
            "#356FCurse you, assassin!\x01",
            "Who sent you?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #142
        0x16,
        "Assassin",
        (
            "#2PJust a noble who wants you\x01",
            "out of the picture.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #143
        0x16,
        "Assassin",
        (
            "#2PHe wanted it badly enough to pay me\x01",
            "up front--and pretty well, at that.\x01",
            "All you need to do is die!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    ClearMapFlags(0x4)
    OP_77(0x5A, 0x5A, 0x5A, 0x0, 0x0)
    SetMapFlags(0x4)
    OP_6D(5120, 0, 670, 0)
    Call(0, 23)
    OP_1F(0x5A, 0xC8)
    OP_0D()

    ChrTalk(    #144
        0x1F,
        (
            "#141F#5P(Ahhh, I get it...\x01",
            "Not bad, not bad at all.)\x02\x03",

            "(So, up next we should have...)\x02\x03",

            "#143F(Whoops... Almost got so wrapped\x01",
            "up that I forgot about my work.)\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    Call(0, 22)
    OP_71(0xD, 0x4)
    OP_72(0xE, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 40)
    SetChrPos(0x10, 66410, 1000, 16219, 90)
    SetChrPos(0xF, 58610, 1000, 14250, 315)
    FadeToBright(1000, 0)
    OP_1D(0x60)
    OP_0D()
    OP_8E(0x10, 0xF046, 0x3E8, 0x3732, 0x7D0, 0x0)
    OP_8C(0x10, 225, 400)

    ChrTalk(    #145
        0x10,
        (
            "#420FLong has it been since you have\x01",
            "entered my sight, fair princess.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 135, 400)

    ChrTalk(    #146
        0xF,
        (
            "#360F#5PYes, Julius...\x01",
            "It truly has.\x02\x03",

            "I cannot help but notice that\x01",
            "Oscar is not with you today...\x02\x03",

            "Back when my father yet breathed,\x01",
            "the both of you were oft spoken\x01",
            "of by the maids of the court.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        (
            "#424FAs you well know, Your Highness,\x01",
            "the kingdom is in the midst of a\x01",
            "crisis most dire...\x02\x03",

            "And as such, he and I may\x01",
            "never be as close as once\x01",
            "we were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xF,
        "#363F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x10,
        (
            "#421FI confess, I come to you\x01",
            "today to ask a favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xF,
        "#364F#5PWhat favor would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x10,
        (
            "#421FThat you would allow he and I...\x02\x03",

            "...head of the Chivalric Order of the\x01",
            "High Guard and a young general,\x01",
            "to engage in a duel of honor.\x02\x03",

            "And that the victor shall be\x01",
            "granted the great honor of\x01",
            "becoming your husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xF,
        "#362F#5P#3S!!!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(2830, 0, 5700, 0)
    Call(0, 23)
    OP_0D()

    ChrTalk(    #153
        0x20,
        "#182F(Ha ha... Quite dramatic, indeed.)\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 17)
    Return()

    # Function_16_22D8 end

    def Function_17_52E8(): pass

    label("Function_17_52E8")

    EventBegin(0x0)
    SetChrPos(0x101, 56670, 1000, 13640, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    Call(0, 22)
    OP_6D(60000, 4300, 7500, 0)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0xE, 0x4)
    OP_72(0xF, 0x4)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    SetChrPos(0x1D, 500, 0, 7200, 0)
    SetChrPos(0x1C, -500, 200, 7200, 0)
    SetChrPos(0x1E, -2500, 200, 7200, 0)
    SetChrPos(0x1B, -3500, 200, 7200, 0)
    SetChrPos(0x20, 2500, 200, 5200, 0)
    SetChrPos(0x21, 2500, 200, 7200, 0)
    SetChrPos(0x22, 3500, 0, 7200, 0)
    SetChrPos(0xD, -3500, 200, 3200, 0)
    SetChrPos(0xA, -2500, 200, 3200, 0)
    SetChrPos(0xB, -1500, 200, 3200, 0)
    SetChrPos(0xC, -500, 200, 3200, 0)
    SetChrPos(0xE, 500, 200, 3200, 0)
    SetChrChipByIndex(0xB, 42)
    SetChrSubChip(0xB, 0)
    OP_44(0xD, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrPos(0x1F, 3500, 200, -800, 0)
    SetChrPos(0x23, 0, -250, -5430, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 57100, 1000, 14000, 129)
    SetChrPos(0x11, 62900, 1000, 14000, 219)
    SetChrPos(0x15, 62100, 1000, 16600, 225)
    SetChrPos(0x14, 57900, 1000, 16600, 135)
    SetChrPos(0x17, 58300, 1000, 18930, 180)
    SetChrPos(0x18, 60000, 1000, 17730, 180)
    SetChrPos(0x19, 61700, 1000, 18930, 180)
    SetChrPos(0x13, 59250, 1000, 18200, 180)
    SetChrPos(0x12, 60750, 1000, 18200, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 7)
    SetChrChipByIndex(0x11, 8)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetMapFlags(0x4)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x2E, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x26, 0x4)
    SetChrPos(0x26, 60000, 2000, 12500, 180)
    SetChrPos(0x8, 60000, 1000, 12500, 180)

    label("loc_571A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_573F")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_573B")
    Jump("loc_573F")

    label("loc_573B")

    OP_48()
    Jump("loc_571A")

    label("loc_573F")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x5DC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    ChrTalk(    #154
        0x8,
        (
            "#647F#5PCaught up in the conflict\x01",
            "between noble and commoner... \x02\x03",

            "...these two close friends\x01",
            "have finally decided on a duel.\x02\x03",

            "The princess now realizes\x01",
            "their determination and\x01",
            "keeps silent.\x02\x03",

            "#642FAnd on the day of the duel...\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x61)

    def lambda_583C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_583C)

    def lambda_584E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_584E)

    def lambda_5860():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5860)

    def lambda_5872():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5872)

    def lambda_5884():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5884)

    def lambda_5896():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5896)

    def lambda_58A8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_58A8)

    def lambda_58BA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_58BA)

    def lambda_58CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_58CC)

    def lambda_58DE():
        OP_8F(0xFE, 0xEA60, 0x8FC, 0x3CC8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_58DE)

    label("loc_58F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5918")
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5914")
    Jump("loc_5918")

    label("loc_5914")

    OP_48()
    Jump("loc_58F3")

    label("loc_5918")

    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x26, 0x1)
    Sleep(500)

    ChrTalk(    #155
        0x8,
        (
            "#647FTwo knights step into the\x01",
            "Grand Arena of the royal city.\x02\x03",

            "Many have come to witness it...\x01",
            "Commoner, noble and all social\x01",
            "castes in between.\x02\x03",

            "...But conspicuously absent from the\x01",
            "proceedings is the one over whom they\x01",
            "fight: Princess Cecilia herself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    def lambda_5A3B():

        label("loc_5A3B")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A3B")

    QueueWorkItem2(0x15, 1, lambda_5A3B)

    def lambda_5A4C():

        label("loc_5A4C")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A4C")

    QueueWorkItem2(0x14, 1, lambda_5A4C)

    def lambda_5A5D():

        label("loc_5A5D")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A5D")

    QueueWorkItem2(0x17, 1, lambda_5A5D)

    def lambda_5A6E():

        label("loc_5A6E")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A6E")

    QueueWorkItem2(0x18, 1, lambda_5A6E)

    def lambda_5A7F():

        label("loc_5A7F")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A7F")

    QueueWorkItem2(0x19, 1, lambda_5A7F)

    def lambda_5A90():

        label("loc_5A90")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5A90")

    QueueWorkItem2(0x13, 1, lambda_5A90)

    def lambda_5AA1():

        label("loc_5AA1")

        TurnDirection(0xFE, 0x26, 0)
        OP_48()
        Jump("loc_5AA1")

    QueueWorkItem2(0x12, 1, lambda_5AA1)
    OP_8E(0x8, 0xF9B0, 0x3E8, 0x2E40, 0x7D0, 0x0)

    def lambda_5AC6():
        OP_8E(0xFE, 0xFB22, 0x0, 0x1B12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AC6)
    OP_77(0x5A, 0x5A, 0x5A, 0x7D000, 0x0)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    Sleep(500)

    ChrTalk(    #156
        0x10,
        (
            "#424FMy friend...I fear that\x01",
            "this was inevitable.\x02\x03",

            "Perhaps fate always intended\x01",
            "for us to meet in so base a\x01",
            "fashion.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 29)
    OP_8C(0x10, 90, 0)
    SetChrSubChip(0x10, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(    #157
        0x10,
        (
            "#421FSpeak, that we may\x01",
            "both be unburdened!\x02\x03",

            "If nothing else, for\x01",
            "our beloved princess!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #158
        0x11,
        (
            "#359FWe would cleave a path through\x01",
            "fate with our own hands...\x02\x03",

            "But at this moment, my words\x01",
            "and her smile seem lost...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10,
        (
            "#422FHas fear clutched your heart,\x01",
            "Oscar?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x11,
        (
            "#357FPerhaps. But what is this passion\x01",
            "that pierces me to the quick...?\x02\x03",

            "As I see you with blade drawn,\x01",
            "I feel as though I've been\x01",
            "waiting for this moment...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x11, 31)
    OP_8C(0x11, 270, 0)
    SetChrSubChip(0x11, 5)
    OP_0D()
    Sleep(400)

    ChrTalk(    #161
        0x11,
        (
            "#352FBefore this storm by the\x01",
            "name of revolution should\x01",
            "claim us both...\x02\x03",

            "...we shall let fate decide\x01",
            "our outcome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        (
            "#420FYes! And may the Goddess\x01",
            "above see our spirits as they\x01",
            "truly are!\x02\x03",

            "Come, then!\x01",
            "Let it be done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x11,
        "#356FEn guarde!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x26, 0x0, 0x0, 0x15)
    OP_20(0x3E8)
    OP_21()
    Sleep(1000)
    OP_1D(0x62)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrChipByIndex(0x11, 32)
    SetChrChipByIndex(0x10, 30)

    def lambda_5ED2():
        OP_8E(0xFE, 0xEDE4, 0x3E8, 0x37DC, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5ED2)

    def lambda_5EED():
        OP_8E(0xFE, 0xE6DC, 0x3E8, 0x3584, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5EED)
    WaitChrThread(0x11, 0x1)

    def lambda_5F0D():
        OP_8E(0xFE, 0xED1C, 0x3E8, 0x37DC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F0D)

    def lambda_5F28():
        OP_8E(0xFE, 0xE7A4, 0x3E8, 0x3584, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5F28)
    SetChrChipByIndex(0x11, 31)
    SetChrChipByIndex(0x10, 29)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x10, 2)
    WaitChrThread(0x11, 0x1)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_5F70():
        OP_8F(0xFE, 0xED80, 0x3E8, 0x37DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5F70)

    def lambda_5F8B():
        OP_8F(0xFE, 0xE740, 0x3E8, 0x3584, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5F8B)
    WaitChrThread(0x11, 0x1)

    def lambda_5FAB():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5FAB)

    def lambda_5FC5():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5FC5)

    def lambda_5FDF():
        OP_8F(0xFE, 0xEBF0, 0x3E8, 0x36B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5FDF)

    def lambda_5FFA():
        OP_8F(0xFE, 0xE8D0, 0x3E8, 0x36B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5FFA)
    Sleep(200)
    OP_8C(0x10, 135, 0)
    OP_8C(0x11, 225, 0)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    SetChrSubChip(0x11, 13)
    SetChrSubChip(0x10, 13)
    OP_8C(0x10, 90, 0)
    OP_8C(0x11, 270, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_604F():
        OP_96(0xFE, 0xF0A0, 0x3E8, 0x36B0, 0x15E, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_604F)

    def lambda_606D():
        OP_96(0xFE, 0xE420, 0x3E8, 0x36B0, 0x15E, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_606D)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x11, 12)
    SetChrSubChip(0x10, 12)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(400)

    def lambda_60A4():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x578, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_60A4)

    def lambda_60C0():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x578, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_60C0)
    WaitChrThread(0x11, 0x1)

    def lambda_60E1():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7D00, 0x6A4, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_60E1)

    def lambda_60FD():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7D00, 0x6A4, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_60FD)
    WaitChrThread(0x11, 0x1)

    def lambda_611E():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x80E8, 0x7D0, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_611E)

    def lambda_613A():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x80E8, 0x7D0, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_613A)
    WaitChrThread(0x11, 0x1)

    def lambda_615B():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x5DC, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_615B)

    def lambda_6177():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x7530, 0x5DC, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6177)
    WaitChrThread(0x11, 0x1)

    def lambda_6198():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x3A98, 0x3E8, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6198)

    def lambda_61B4():
        OP_97(0xFE, 0xEA60, 0x36B0, 0x3A98, 0x3E8, 0x2)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61B4)
    WaitChrThread(0x11, 0x1)
    Sleep(400)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 13)

    def lambda_61E4():
        OP_96(0xFE, 0xE790, 0x3E8, 0x349E, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61E4)
    Sleep(400)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    SetChrSubChip(0x10, 2)
    SetChrSubChip(0x11, 0)

    def lambda_621B():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_621B)
    Sleep(20)
    SetChrSubChip(0x11, 8)

    def lambda_6240():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6240)
    Sleep(20)

    def lambda_6260():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6260)
    Sleep(20)

    def lambda_6280():
        OP_8F(0xFE, 0xE344, 0x3E8, 0x2FD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6280)
    WaitChrThread(0x11, 0x1)
    Sleep(50)
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x11, 8)

    def lambda_62AF():
        OP_97(0xFE, 0xE790, 0x349E, 0xFFFEA070, 0x1B58, 0x2)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_62AF)
    Sleep(200)

    def lambda_62D0():
        OP_8C(0xFE, 146, 800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62D0)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 9)
    OP_8F(0x11, 0xEA88, 0x3E8, 0x31BA, 0x1F40, 0x0)
    OP_22(0xD6, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    OP_8F(0x10, 0xE498, 0x3E8, 0x38AE, 0x1F40, 0x0)

    def lambda_6324():
        OP_9E(0xFE, 0x1E, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6324)
    OP_9E(0x10, 0x1E, 0x0, 0x190, 0xFA0)
    SetChrSubChip(0x10, 8)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    SetChrSubChip(0x10, 10)
    OP_8C(0x11, 270, 0)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x10, 11)
    SetChrSubChip(0x11, 12)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6385():
        OP_96(0xFE, 0xEABA, 0x3E8, 0x393A, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6385)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x10, 5)
    Sleep(300)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x10, 7)

    def lambda_63C1():
        OP_8E(0xFE, 0xEE84, 0x3E8, 0x39A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_63C1)
    Sleep(50)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x11, 13)

    def lambda_63EB():
        OP_96(0xFE, 0xE6FA, 0x3E8, 0x39A8, 0x640, 0x1B58)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_63EB)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x11, 12)
    OP_8C(0x11, 269, 0)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x10, 12)
    OP_8C(0x10, 91, 0)
    Sleep(300)
    SetChrSubChip(0x10, 6)
    SetChrSubChip(0x11, 6)

    def lambda_643F():
        OP_8C(0x10, 225, 700)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_643F)

    def lambda_644D():
        OP_8C(0x11, 135, 700)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_644D)

    def lambda_645B():
        OP_8F(0xFE, 0xED1C, 0x3E8, 0x39A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_645B)

    def lambda_6476():
        OP_8F(0xFE, 0xE7A4, 0x3E8, 0x39A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6476)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_64A0():
        OP_9E(0xFE, 0x14, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_64A0)

    def lambda_64BA():
        OP_9E(0xFE, 0x14, 0x0, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_64BA)
    Sleep(100)

    def lambda_64D9():
        OP_8F(0xFE, 0xEEAC, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_64D9)

    def lambda_64F4():
        OP_8F(0xFE, 0xE614, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_64F4)
    Sleep(300)
    OP_8C(0x10, 270, 0)
    OP_8C(0x11, 90, 0)

    def lambda_6522():
        OP_8F(0xFE, 0xED1C, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6522)

    def lambda_653D():
        OP_8F(0xFE, 0xE7A4, 0x3E8, 0x39A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_653D)
    Sleep(100)
    OP_8C(0x10, 315, 0)
    OP_8C(0x11, 45, 0)
    Sleep(1000)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0x10, 270, 0)
    OP_8C(0x11, 90, 0)

    def lambda_6583():
        OP_96(0xFE, 0xE290, 0x3E8, 0x39D0, 0x190, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6583)

    def lambda_65A1():
        OP_96(0xFE, 0xF230, 0x3E8, 0x39D0, 0x190, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_65A1)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x11, 3)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x10, 0x4)

    def lambda_65E2():
        OP_96(0xFE, 0xE86C, 0xBB8, 0x39D0, 0x802, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_65E2)

    def lambda_6600():
        OP_96(0xFE, 0xEC54, 0xBB8, 0x39D0, 0x802, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6600)
    WaitChrThread(0x11, 0x1)
    SetChrPos(0x11, 60000, 3000, 14800, 90)
    SetChrPos(0x10, 60000, 3000, 14800, 270)
    SetChrChipByIndex(0x11, 33)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x10, 0x80)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_6659():
        OP_8C(0xFE, 270, 700)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_6659)

    def lambda_6667():
        OP_8C(0xFE, 90, 700)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_6667)

    def lambda_6675():
        OP_96(0xFE, 0xEA06, 0x3E8, 0x39D0, 0x0, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6675)

    def lambda_6693():
        OP_96(0xFE, 0xEABA, 0x3E8, 0x39D0, 0x0, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6693)
    WaitChrThread(0x11, 0x1)

    def lambda_66B6():

        label("loc_66B6")

        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        OP_48()
        Jump("loc_66B6")

    QueueWorkItem2(0x11, 2, lambda_66B6)

    def lambda_66D3():

        label("loc_66D3")

        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        OP_48()
        Jump("loc_66D3")

    QueueWorkItem2(0x10, 2, lambda_66D3)
    Sleep(1000)

    ChrTalk(    #164
        0x11,
        "#352F#2PImpressive, Julius...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10,
        (
            "#420F#1PI should say the same of you.\x02\x03",

            "But still, you seem to hesitate!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrChipByIndex(0x11, 31)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x11, 60500, 1000, 14800, 270)
    SetChrPos(0x10, 59500, 1000, 14800, 90)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 5)
    OP_96(0x10, 0xE5B0, 0x3E8, 0x39D0, 0x190, 0x1770)
    SetChrSubChip(0x10, 6)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_67CE():
        OP_8F(0xFE, 0xEA60, 0x3E8, 0x396C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_67CE)

    def lambda_67E9():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_67E9)
    Sleep(30)

    def lambda_6809():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6809)
    Sleep(30)

    def lambda_6829():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6829)
    Sleep(30)

    def lambda_6849():
        OP_8F(0xFE, 0xF230, 0x3E8, 0x39D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6849)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x10, 5)
    Sleep(100)
    SetChrSubChip(0x10, 7)

    def lambda_6878():
        OP_8F(0xFE, 0xF0AA, 0x3E8, 0x39DA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6878)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0xD6, 0x0, 0x64)
    OP_8C(0x11, 315, 0)

    def lambda_68A4():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_68A4)
    Sleep(30)

    def lambda_68C4():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_68C4)
    Sleep(30)

    def lambda_68E4():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_68E4)
    Sleep(30)

    def lambda_6904():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x37DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6904)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x10, 6)

    def lambda_692E():
        OP_9E(0xFE, 0x14, 0x0, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_692E)

    def lambda_6948():
        OP_9E(0xFE, 0x14, 0x0, 0x258, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6948)
    Sleep(300)

    def lambda_6967():
        OP_8F(0xFE, 0xF348, 0x3E8, 0x3A20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6967)

    def lambda_6982():
        OP_8F(0xFE, 0xF618, 0x3E8, 0x36B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6982)
    WaitChrThread(0x10, 0x1)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_69A7():

        label("loc_69A7")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_69A7")

    QueueWorkItem2(0x10, 1, lambda_69A7)

    def lambda_69B8():

        label("loc_69B8")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_69B8")

    QueueWorkItem2(0x11, 3, lambda_69B8)

    def lambda_69C9():
        OP_97(0xFE, 0xF0AA, 0x39DA, 0x15F90, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_69C9)
    WaitChrThread(0x11, 0x2)
    SetChrSubChip(0x10, 5)
    SetChrSubChip(0x11, 12)

    def lambda_69F4():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_69F4)
    Sleep(30)

    def lambda_6A14():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A14)
    Sleep(30)

    def lambda_6A34():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A34)
    Sleep(30)

    def lambda_6A54():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A54)
    Sleep(30)

    def lambda_6A74():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A74)
    Sleep(30)

    def lambda_6A94():
        OP_8F(0xFE, 0xE862, 0x3E8, 0x39EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A94)
    WaitChrThread(0x11, 0x1)
    Sleep(200)
    SetChrSubChip(0x10, 4)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0xE100, 0x3E8, 0x39EE, 0x258, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x11, 32)
    ClearChrFlags(0x11, 0x20)
    SetChrSubChip(0x11, 0)

    def lambda_6AEE():
        OP_8F(0xFE, 0xED76, 0x3E8, 0x39A8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6AEE)
    Sleep(380)
    SetChrChipByIndex(0x11, 31)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x20)
    SetChrSubChip(0x10, 2)
    OP_22(0x84, 0x0, 0x64)

    def lambda_6B27():
        OP_8F(0xFE, 0xEFD8, 0x3E8, 0x3A20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B27)

    def lambda_6B42():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B42)
    Sleep(20)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_6B67():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B67)
    Sleep(20)

    def lambda_6B87():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B87)
    Sleep(20)

    def lambda_6BA7():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6BA7)
    Sleep(20)

    def lambda_6BC7():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6BC7)
    Sleep(20)

    def lambda_6BE7():
        OP_8F(0xFE, 0xE4F2, 0x3E8, 0x3A20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6BE7)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x11, 3)
    Sleep(300)

    ChrTalk(    #166
        0x10,
        (
            "#345F#2PWhat troubles you, Oscar?! Is\x01",
            "this the extent of your skill?\x02\x03",

            "Perhaps the tales of your acts\x01",
            "of valor against the Empire\x01",
            "were grossly overstated!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        "#359F#1P...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #168
        0x11,
        "#356F#1P#3SHAAAAAAAAAHH!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    TurnDirection(0x11, 0x10, 0)

    def lambda_6D00():

        label("loc_6D00")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_6D00")

    QueueWorkItem2(0x10, 1, lambda_6D00)
    SetChrSubChip(0x11, 13)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6D1B():
        OP_96(0x11, 0xEDE4, 0x3E8, 0x39EE, 0x9C4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D1B)
    Sleep(300)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x10, 3)

    def lambda_6D4D():
        OP_96(0xFE, 0xF1C2, 0x3E8, 0x3354, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D4D)
    Sleep(300)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 7)

    def lambda_6D7A():
        OP_8E(0x11, 0xF172, 0x3E8, 0x32F0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6D7A)
    Sleep(50)
    SetChrSubChip(0x10, 3)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6DA4():
        OP_96(0xFE, 0xF802, 0x3E8, 0x32A0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6DA4)
    WaitChrThread(0x11, 0x1)
    SetChrSubChip(0x11, 5)
    WaitChrThread(0x10, 0x1)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 6)

    def lambda_6DDB():
        OP_8E(0x11, 0xFA00, 0x3E8, 0x3336, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6DDB)
    Sleep(50)
    SetChrSubChip(0x11, 7)
    SetChrSubChip(0x10, 13)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x10, 0xFD8E, 0xA50, 0x3214, 0x6A4, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x10, 12)
    SetChrSubChip(0x11, 5)
    Sleep(50)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_6E3A():
        OP_96(0x10, 0xF028, 0x3E8, 0x3214, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6E3A)
    SetChrSubChip(0x10, 12)
    Sleep(50)
    SetChrSubChip(0x11, 5)
    OP_8C(0x11, 270, 400)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x11, 7)

    def lambda_6E7D():
        OP_8E(0x11, 0xF550, 0x3E8, 0x31A6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E7D)
    Sleep(100)

    def lambda_6E9D():
        OP_8F(0x11, 0xF550, 0x3E8, 0x31A6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E9D)
    OP_22(0xD6, 0x0, 0x64)
    OP_8C(0x11, 315, 0)
    SetChrSubChip(0x11, 6)
    SetChrSubChip(0x10, 3)
    Sleep(200)

    def lambda_6ED3():
        OP_8F(0x11, 0xF550, 0x3E8, 0x31A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6ED3)
    OP_8C(0x10, 225, 0)

    def lambda_6EF5():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6EF5)

    def lambda_6F0F():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6F0F)
    Sleep(400)
    SetChrSubChip(0x10, 8)

    def lambda_6F33():
        OP_8C(0xFE, 135, 340)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6F33)

    def lambda_6F41():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6F41)

    def lambda_6F5B():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6F5B)
    Sleep(400)
    SetChrSubChip(0x10, 9)
    OP_22(0x84, 0x0, 0x64)

    def lambda_6F84():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6F84)

    def lambda_6F92():
        OP_96(0xFE, 0xE484, 0x3E8, 0x325A, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6F92)
    SetChrSubChip(0x11, 2)
    OP_8C(0x11, 270, 0)

    def lambda_6FBC():
        OP_94(0x1, 0x11, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6FBC)
    WaitChrThread(0x10, 0x2)
    SetChrSubChip(0x10, 3)
    WaitChrThread(0x11, 0x2)
    Sleep(500)
    SetChrSubChip(0x11, 3)

    def lambda_6FEB():
        OP_8F(0xFE, 0xF014, 0x3E8, 0x325A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6FEB)
    OP_8C(0x11, 270, 0)
    OP_77(0x5A, 0x5A, 0x5A, 0x7D000, 0x0)
    Sleep(1000)

    ChrTalk(    #169
        0x11,
        (
            "#357FWell done, Julius...\x01",
            "Magnificent swordsmanship...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x11, 0x14, 0x0, 0x1F4, 0xFA0)

    ChrTalk(    #170
        0x11,
        "#430FGah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #171
        0x10,
        "#422FOscar...your arm...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x11,
        (
            "#352FI've had worse.\x01",
            "'Tis but a scratch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x10,
        (
            "#422FNeither of our blades connected\x01",
            "with flesh. Not even a glancing\x01",
            "blow...\x02\x03",

            "Your wound...was struck prior!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #174
        0x15,
        (
            "#2PThis is a tactic most low, Duke\x01",
            "Radmont! Was this your intention\x01",
            "from the start?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x14,
        (
            "#5PHa ha ha... I'll thank you to\x01",
            "cease slandering my good name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x14,
        (
            "#5PAre you implying that I\x01",
            "instigated this?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #177
        0x10,
        (
            "#422FFather...is it true...?\x01",
            "Did you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x11,
        (
            "#357FIt's all right, Julius.\x01",
            "My own inexperience has\x01",
            "brought this about.\x02\x03",

            "#358FBesides, I've received far\x01",
            "worse on the field of battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10,
        "#422F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x11,
        (
            "#357FI will put everything I have\x01",
            "behind my next strike.\x02\x03",

            "#352FI intend... I intend to kill you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10,
        (
            "#421FOscar...\x02\x03",

            "#424FVery well. I will wager it all\x01",
            "on my next strike as well.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_73BC():
        OP_96(0xFE, 0xDBEC, 0x3E8, 0x323C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_73BC)

    def lambda_73DA():
        OP_96(0xFE, 0xF8D4, 0x3E8, 0x323C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_73DA)
    WaitChrThread(0x10, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Fade(1000)
    OP_8C(0x10, 135, 0)
    OP_8C(0x11, 225, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    OP_0D()

    ChrTalk(    #182
        0x10,
        (
            "#420FFor the fair princess, and the\x01",
            "future of the very kingdom...\x02\x03",

            "He who lives, when all is said\x01",
            "and done, will inherit the\x01",
            "responsibility for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x11,
        (
            "#358FAnd he who dies will watch\x01",
            "over it all, from the realm\x01",
            "of the spirits.\x02\x03",

            "Such is also the pride of a knight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10,
        (
            "#420FHa ha... I suppose it is.\x02\x03",

            "#424F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x11,
        "#357F...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    SetChrSubChip(0x11, 5)
    SetChrSubChip(0x10, 5)
    OP_8C(0x10, 90, 0)
    OP_8C(0x11, 270, 0)
    OP_0D()

    def lambda_7594():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7594)

    def lambda_75AE():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xDAC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_75AE)

    ChrTalk(    #186 op#A op#5
        0x10,
        "#10A#1P#3SHAAAAAAAAAHH!\x05\x02",
    )


    ChrTalk(    #187 op#A op#5
        0x11,
        "#10A#2P#3SYAAAAAAHHH!!\x05\x02",
    )

    Sleep(1000)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x11, 32)
    SetChrChipByIndex(0x10, 30)

    def lambda_761A():
        OP_8E(0xFE, 0xE678, 0x3E8, 0x38C2, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_761A)

    def lambda_7635():
        OP_8E(0xFE, 0xEE48, 0x3E8, 0x38C2, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7635)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x40)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7665():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7665)
    SetChrPos(0xF, 62800, 1000, 18980, 0)

    def lambda_7688():
        OP_8E(0xFE, 0xEA60, 0x3E8, 0x3368, 0x2328, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7688)
    OP_20(0x3E8)
    FadeToDark(500, 0, -1)
    Sleep(100)
    OP_22(0x9B, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #188
        "\x07\x00NOOOOOOOO!!!\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_56(0x0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x11, 31)
    SetChrChipByIndex(0x10, 29)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x10, 2)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x10, 0x20)
    OP_44(0xF, 0xFF)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 35)
    SetChrSubChip(0xF, 0)
    SetChrPos(0xF, 60000, 1000, 13160, 0)
    FadeToBright(300, 0)
    OP_44(0x26, 0xFF)
    SetChrPos(0x26, 60010, 1000, 13880, 0)
    OP_4F(0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_776F():

        label("loc_776F")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_776F")

    QueueWorkItem2(0x15, 1, lambda_776F)

    def lambda_7780():

        label("loc_7780")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_7780")

    QueueWorkItem2(0x14, 1, lambda_7780)

    def lambda_7791():

        label("loc_7791")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_7791")

    QueueWorkItem2(0x17, 1, lambda_7791)

    def lambda_77A2():

        label("loc_77A2")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77A2")

    QueueWorkItem2(0x18, 1, lambda_77A2)

    def lambda_77B3():

        label("loc_77B3")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77B3")

    QueueWorkItem2(0x19, 1, lambda_77B3)

    def lambda_77C4():

        label("loc_77C4")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77C4")

    QueueWorkItem2(0x13, 1, lambda_77C4)

    def lambda_77D5():

        label("loc_77D5")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_77D5")

    QueueWorkItem2(0x12, 1, lambda_77D5)
    Sleep(1000)

    ChrTalk(    #189
        0xF,
        "#364FOh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x11, 3)

    def lambda_7805():
        OP_99(0xFE, 0x0, 0xD, 0x2BC)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7805)

    def lambda_7815():
        OP_8C(0x10, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7815)

    def lambda_7823():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7823)

    NpcTalk(    #190 op#A op#5
        0x10,
        "Julius",
        "#422F#13A#2PWha...\x05\x02",
    )


    NpcTalk(    #191 op#A op#5
        0x11,
        "Oscar",
        "#354F#13A#1PC-Cecilia...?\x05\x02",
    )

    Sleep(1300)
    SetChrChipByIndex(0x11, 8)

    def lambda_787F():
        OP_8E(0xFE, 0xE86C, 0x3E8, 0x38C2, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_787F)

    def lambda_789A():

        label("loc_789A")

        OP_8C(0xFE, 126, 0)
        OP_48()
        Jump("loc_789A")

    QueueWorkItem2(0x11, 1, lambda_789A)
    SetChrChipByIndex(0x10, 7)
    ClearChrFlags(0x10, 0x20)

    def lambda_78B5():
        OP_8E(0x10, 0xEE20, 0x3E8, 0x2F8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_78B5)

    def lambda_78D0():

        label("loc_78D0")

        TurnDirection(0x10, 0xF, 0)
        OP_48()
        Jump("loc_78D0")

    QueueWorkItem2(0x10, 1, lambda_78D0)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0x11, 0x80)
    OP_99(0xF, 0xE, 0x10, 0x3E8)
    Sleep(800)
    OP_1D(0x63)
    Sleep(1000)

    ChrTalk(    #192
        0x10,
        "#422F#3SPrincess...!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #193
        0x11,
        (
            "#356F#1PCecilia, why...\x02\x03",

            "...were you not in attendance?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xF, 0x10, 0x12, 0x384)
    Sleep(200)

    ChrTalk(    #194
        0xF,
        (
            "#361FOh, Oscar... Julius...\x02\x03",

            "I did not wish to observe a\x01",
            "duel between the two of you.\x02\x03",

            "I felt I had to find a way to\x01",
            "put a stop to this fight.\x02\x03",

            "#365FPraise Aidios that I arrived\x01",
            "in time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x11,
        "#359F#5PCecilia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x10,
        "#422FPrincess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xF,
        (
            "#361FHear me, all in attendance...\x02\x03",

            "Dismiss me...and set aside\x01",
            "your differences, please...\x02\x03",

            "Are we not all of Liberl? And\x01",
            "do we not love this land?\x02\x03",

            "There is so little that separates\x01",
            "us from one another...\x02\x03",

            "If you would but take your\x01",
            "foe's hand...surely we could\x01",
            "find a peaceful resolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x14,
        "#5PY-Your Royal Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x15,
        "#2PYou need say no more...\x02",
    )

    CloseMessageWindow()
    OP_99(0xF, 0x12, 0x11, 0x3E8)

    ChrTalk(    #200
        0xF,
        (
            "#363FMy vision fades...\x02\x03",

            "But what of you two...?\x01",
            "Will you not do as I ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10,
        "#343FYour will be done, my princess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x11,
        "#359F#5PAt your side...\x02",
    )

    CloseMessageWindow()
    OP_99(0xF, 0x13, 0x16, 0x2BC)
    Sleep(200)

    ChrTalk(    #203
        0xF,
        (
            "#361FStrange...\x01",
            "Everything is floating...\x02\x03",

            "When I was young...I would\x01",
            "sneak out of the castle...\x01",
            "down to the alley...\x02\x03",

            "Oscar...Julius...you both\x01",
            "always...had smiles for me...\x02\x03",

            "I love...your smiles...\x02\x03",

            "#365FSo...please...\x02\x03",

            "...don't ever...stop...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xF, 0x16, 0x18, 0x2BC)
    Sleep(160)
    Fade(500)
    OP_99(0xF, 0x19, 0x19, 0x2BC)
    Sleep(1000)

    ChrTalk(    #204
        0x10,
        (
            "#422F#2PPrincess...?\x02\x03",

            "No... This cannot be, Princess!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #205
        0x10,
        "#423F#2P#3SI'll do anything! Please, no!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_99(0xF, 0x19, 0x1B, 0x384)

    ChrTalk(    #206
        0x11,
        (
            "#359F#5PCecilia...you...\x02\x03",

            "#357F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x13,
        "#5POur poor princess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x12,
        (
            "#2PI just don't understand why\x01",
            "she'd do such a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x14,
        (
            "#5POur princess gave her\x01",
            "life, that we might stop\x01",
            "this unending dispute...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x14,
        (
            "#5PCompared to that sacrifice...\x01",
            "what a trifle is the pride of\x01",
            "a nobleman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x14,
        (
            "#5PHad we not been fighting, it\x01",
            "would never have come to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x15,
        (
            "#2POnly now, when it is too late,\x01",
            "do I see our folly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x15,
        (
            "#2PIs this the fate of all men\x01",
            "with their spirits still\x01",
            "shackled to their flesh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x15,
        (
            "#2PAidios, great Goddess of the\x01",
            "skies...we now know of your\x01",
            "great resentment...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #215
        (
            "\x07\x05There is much that you do not\x01",
            "yet understand, it seems...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    SetChrPos(0x1A, 59990, 7000, 13110, 0)
    OP_22(0xD7, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp005_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 59990, 8500, 13110, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_77(0x1E, 0x1E, 0xA0, 0xFA000, 0x0)
    Sleep(4000)
    OP_99(0xF, 0x1B, 0x19, 0x4B0)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #216
        (
            "\x07\x05...I granted you flesh,\x01",
            "to be your vessel.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #217
        (
            "\x07\x05But your spirits still know\x01",
            "more of freedom and nobility...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #218
        (
            "\x07\x05Such contempt for it lies\x01",
            "only within you, yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #219
        0x17,
        "#5PS-So beautiful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x19,
        (
            "#2PA more beautiful voice\x01",
            "I have never heard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x18,
        "#5PIt's amazing...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x18,
        (
            "#5PAidios Herself has graced us\x01",
            "with Her presence...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x10,
        "#422FThe Goddess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x11,
        "#359F#5PIncredible...\x02",
    )

    CloseMessageWindow()
    SetChrName("Aidios")

    AnonymousTalk(    #225
        "\x07\x05Hear me, young knights.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #226
        "\x07\x05I have observed your contest.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #227
        (
            "\x07\x05You are both courageous and\x01",
            "strong...yet something vital\x01",
            "within you is broken.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #228
        0x10,
        "#424FIt is as you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x11,
        (
            "#352F#5POur own immaturity is what\x01",
            "invited this fate upon us...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Aidios")

    AnonymousTalk(    #230
        "\x07\x05Chairman...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #231
        (
            "\x07\x05Has your hate for the nobles and\x01",
            "the monarchy blinded you to the\x01",
            "fact that we are all but men?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #232
        0x15,
        "#2P...I am ashamed.\x02",
    )

    CloseMessageWindow()
    SetChrName("Aidios")

    AnonymousTalk(    #233
        "\x07\x05Duke...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #234
        (
            "\x07\x05You know your sins better\x01",
            "than anyone else could...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #235
        0x14,
        "#5P...\x02",
    )

    CloseMessageWindow()
    SetChrName("Aidios")

    AnonymousTalk(    #236
        (
            "\x07\x05And you...all the rest of you...\x01",
            "who have simply watched these\x01",
            "events unfold...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #237
        (
            "\x07\x05There is something\x01",
            "fundamental within you\x01",
            "that is lost as well...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #238
        (
            "\x07\x05Strike your hand upon your\x01",
            "breast and think well upon\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(400)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)
    OP_63(0x17)
    OP_63(0x18)
    OP_63(0x19)
    Sleep(400)
    SetChrName("Aidios")

    AnonymousTalk(    #239
        (
            "\x07\x05Ha ha...and it now seems that\x01",
            "you have each remembered your\x01",
            "hearts.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #240
        (
            "\x07\x05As such, perhaps hope yet\x01",
            "remains for Liberl.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #241
        (
            "\x07\x05So long as you never forget\x01",
            "the lessons learned this day.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_82(0x0, 0x2)
    OP_77(0x0, 0x0, 0x0, 0xBB800, 0x0)
    Sleep(3000)
    OP_21()

    ChrTalk(    #242
        0x13,
        "#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x12,
        "#2PShe has vanished...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #244
        0xF,
        "#5P...Mmnnn...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_99(0xF, 0x19, 0x16, 0x2BC)
    Sleep(300)
    OP_99(0xF, 0x16, 0x14, 0x352)
    OP_99(0xF, 0x14, 0x16, 0x352)
    Sleep(100)
    OP_99(0xF, 0x16, 0x14, 0x44C)
    OP_99(0xF, 0x14, 0x16, 0x44C)

    ChrTalk(    #245
        0xF,
        "#364FOh... Where am I...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x10,
        "#422FP-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x11,
        "#354F#5PCecilia?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xF,
        (
            "#364FOh, my...\x01",
            "Julius... Oscar...\x02\x03",

            "Have you both been called\x01",
            "up to heaven, as well?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #249
        0x10,
        "Julius",
        "#422F#2P#1K...\x02",
    )


    NpcTalk(    #250
        0x11,
        "Oscar",
        "#354F#1P#1K...\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #251
        0x18,
        "#5PIt's... It's a genuine miracle!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 59990, 2000, 13110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 59370, 1000, 13750, 126)
    SetChrChipByIndex(0xF, 40)
    ClearChrFlags(0xF, 0x2)
    SetChrSubChip(0xF, 0)
    OP_8C(0xF, 180, 0)
    OP_1D(0x64)
    OP_0D()
    OP_77(0x78, 0x78, 0x78, 0x7D000, 0x0)
    Sleep(2000)

    ChrTalk(    #252 op#A op#5
        0x13,
        "#10A#5PPrinceeeess!\x05\x02",
    )

    CloseMessageWindow()

    def lambda_89CF():
        OP_8E(0xFE, 0xE4E8, 0x3E8, 0x37A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_89CF)

    def lambda_89EA():

        label("loc_89EA")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_89EA")

    QueueWorkItem2(0x11, 1, lambda_89EA)

    def lambda_89FB():
        OP_8E(0xFE, 0xEFD8, 0x3E8, 0x37A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_89FB)

    def lambda_8A16():

        label("loc_8A16")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8A16")

    QueueWorkItem2(0x10, 1, lambda_8A16)

    def lambda_8A27():
        OP_8C(0xFE, 0, 300)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8A27)

    def lambda_8A35():
        OP_8E(0xFE, 0xEBF0, 0x3E8, 0x3624, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8A35)

    def lambda_8A50():

        label("loc_8A50")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8A50")

    QueueWorkItem2(0x12, 1, lambda_8A50)

    def lambda_8A61():
        OP_8E(0xFE, 0xE8D0, 0x3E8, 0x3624, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8A61)

    def lambda_8A7C():

        label("loc_8A7C")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8A7C")

    QueueWorkItem2(0x13, 1, lambda_8A7C)

    def lambda_8A8D():
        OP_8E(0xFE, 0xE164, 0x3E8, 0x323C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8A8D)

    def lambda_8AA8():

        label("loc_8AA8")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8AA8")

    QueueWorkItem2(0x14, 1, lambda_8AA8)

    def lambda_8AB9():
        OP_8E(0xFE, 0xF35C, 0x3E8, 0x323C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8AB9)

    def lambda_8AD4():

        label("loc_8AD4")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8AD4")

    QueueWorkItem2(0x15, 1, lambda_8AD4)

    def lambda_8AE5():
        OP_8E(0xFE, 0xE4E8, 0x3E8, 0x41E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8AE5)

    def lambda_8B00():

        label("loc_8B00")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8B00")

    QueueWorkItem2(0x17, 1, lambda_8B00)

    def lambda_8B11():
        OP_8E(0xFE, 0xEFD8, 0x3E8, 0x41E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_8B11)

    def lambda_8B2C():

        label("loc_8B2C")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8B2C")

    QueueWorkItem2(0x19, 1, lambda_8B2C)

    def lambda_8B3D():
        OP_8E(0xFE, 0xEA60, 0x3E8, 0x4010, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_8B3D)

    def lambda_8B58():

        label("loc_8B58")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_8B58")

    QueueWorkItem2(0x18, 1, lambda_8B58)
    WaitChrThread(0x12, 0x2)

    ChrTalk(    #253
        0x12,
        "#2POh, praise Aidios!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xF,
        (
            "#364FWha...? Why are the\x01",
            "two of you here...?\x02\x03",

            "And the duke...and\x01",
            "the chairman...\x02\x03",

            "So then...I'm not dead...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x14,
        "#5PAlmighty Aidios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x14,
        (
            "#5PAidios has given Liberl\x01",
            "back its beloved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x15,
        "#2PPraise her for her benevolence!\x02",
    )

    CloseMessageWindow()

    def lambda_8C6F():
        OP_8F(0xFE, 0xED1C, 0x3E8, 0x3BC4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8C6F)

    def lambda_8C8A():
        OP_8F(0xFE, 0xE7A4, 0x3E8, 0x3BC4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8C8A)
    WaitChrThread(0x12, 0x2)

    def lambda_8CAA():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8CAA)

    def lambda_8CB8():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8CB8)
    TurnDirection(0xF, 0x10, 300)
    Sleep(500)
    TurnDirection(0xF, 0x11, 300)

    ChrTalk(    #258
        0xF,
        (
            "#362FOscar... Julius...\x02\x03",

            "Umm...what happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x11, 0xFF)
    OP_44(0x10, 0xFF)

    ChrTalk(    #259
        0x11,
        (
            "#357F#5PNothing that you need concern\x01",
            "yourself over, Cecilia...\x02\x03",

            "#358FThe conflict is at an end...\x01",
            "I believe that everything will\x01",
            "be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x10,
        (
            "#420F#2PYou're being naive, Oscar.\x02\x03",

            "We still have a duel\x01",
            "to finish, do we not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x11,
        "#353F#5PJulius...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 300)

    ChrTalk(    #262
        0xF,
        "#363FNo... You still intend to fight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x10,
        (
            "#424F#2POn the contrary...\x01",
            "This match is concluded.\x02\x03",

            "And besides, this fool managed\x01",
            "to get hit on his sword arm.\x02\x03",

            "#420FBut it would not do for a duel such as this to\x01",
            "not have a clear victor.\x02\x03",

            "Thus it stands to reason that the man who\x01",
            "fought with a significant handicap, yet emerged\x01",
            "undefeated, should be regarded as the victor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x11,
        "#352F#5PWait, Julius!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x11, 300)
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #265
        0x10,
        (
            "#420F#2PDon't misunderstand me,\x01",
            "Oscar. I have not given\x01",
            "up on the princess.\x02\x03",

            "Once you are healed, our\x01",
            "duel will continue, but\x01",
            "with blades of wood.\x02\x03",

            "Just as when we were boys.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #266
        0x11,
        (
            "#358F#5PI see...\x02\x03",

            "Ha ha... Very well, then.\x01",
            "I accept your challenge.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 300)

    ChrTalk(    #267
        0xF,
        (
            "#367FHave neither of you any\x01",
            "regard for my own wishes?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)
    TurnDirection(0x11, 0xF, 400)

    ChrTalk(    #268
        0x11,
        "#354F#5PY-You are mistaken...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x10,
        (
            "#420F#2PYou, My Lady, shall judge today's\x01",
            "match. And I think it only fair for\x01",
            "the victor to be granted a kiss.\x02\x03",

            "Surely, everyone waits\x01",
            "with bated breath for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xF,
        "#360F...Very well.\x02",
    )

    CloseMessageWindow()

    def lambda_91F3():
        OP_8E(0xFE, 0xE920, 0x3E8, 0x3520, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_91F3)
    OP_8F(0xF, 0xEB28, 0x3E8, 0x3232, 0x5DC, 0x0)
    TurnDirection(0xF, 0x11, 300)
    Sleep(1000)
    SetChrFlags(0x11, 0x80)
    SetChrPos(0xF, 60000, 1000, 13160, 0)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 36)
    SetChrSubChip(0xF, 0)
    Sleep(200)
    OP_99(0xF, 0x0, 0x3, 0x384)
    Sleep(500)
    OP_99(0xF, 0x3, 0x0, 0x384)
    Sleep(200)
    OP_44(0x10, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)

    ChrTalk(    #271
        0x13,
        "#5PEeeek! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x12,
        (
            "#2PDon't they look marvelous\x01",
            "together? ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(400)

    ChrTalk(    #273
        0x10,
        (
            "#420F#2P#3SAlmighty Aidios, look well\x01",
            "upon this!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #274
        0x10,
        (
            "#420F#2P#3SAnd may this fine day\x01",
            "extend unto eternity!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 40)
    SetChrSubChip(0xF, 0)
    OP_8F(0x11, 0xE678, 0x3E8, 0x358E, 0x3E8, 0x0)
    OP_8C(0x11, 180, 400)
    OP_8C(0xF, 180, 400)
    Sleep(500)
    OP_8C(0x14, 180, 400)
    Sleep(400)

    ChrTalk(    #275
        0x14,
        "#5P#3SEternal peace to Liberl!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x15, 180, 400)
    Sleep(400)

    ChrTalk(    #276
        0x15,
        "#5P#3SEternal glory to Liberl!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0xF, 0x800)
    OP_22(0xBF, 0x0, 0x64)
    OP_22(0xAF, 0x0, 0x64)
    OP_70(0x5, 0x78)
    OP_73(0x5)
    Sleep(2000)
    Fade(1000)
    OP_1F(0x5A, 0xC8)
    OP_6D(130, 0, -1840, 0)
    Call(0, 23)
    ClearChrFlags(0x23, 0x80)
    OP_0D()
    Sleep(500)

    NpcTalk(    #277
        0x23,
        "Silver-Haired Man",
        (
            "#122F#2PHa ha... Quite the grand finale...\x02\x03",

            "#125FBut no matter.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x23, 180, 400)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)

    def lambda_94E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_94E3)
    OP_8E(0x23, 0x0, 0x0, 0xFFFFE160, 0x5DC, 0x0)
    SetChrFlags(0x23, 0x80)
    OP_0D()
    OP_21()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #278
        (
            "\x07\x05And so, the curtain fell on the Madrigal of the White Magnolia,' to grand\x01",
            "fanfare and acclaim.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #279
        (
            "\x07\x05And with its conclusion, an announcement went out that the campus festival\x01",
            "had reached its end.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #280
        (
            "\x07\x05The crowd began to disperse and leave the campus, each person wearing a\x01",
            "look of contentment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T2513   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_52E8 end

    def Function_18_964B(): pass

    label("Function_18_964B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9697")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_18_964B")

    label("loc_9697")

    Return()

    # Function_18_964B end

    def Function_19_9698(): pass

    label("Function_19_9698")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96E4")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_19_9698")

    label("loc_96E4")

    Return()

    # Function_19_9698 end

    def Function_20_96E5(): pass

    label("Function_20_96E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9731")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_20_96E5")

    label("loc_9731")

    Return()

    # Function_20_96E5 end

    def Function_21_9732(): pass

    label("Function_21_9732")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_977E")
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_21_9732")

    label("loc_977E")

    Return()

    # Function_21_9732 end

    def Function_22_977F(): pass

    label("Function_22_977F")

    OP_6D(60010, 4300, 7500, 0)
    OP_67(0, 840, -10000, 0)
    OP_6B(910, 0)
    OP_6C(0, 0)
    OP_6E(581, 0)
    Return()

    # Function_22_977F end

    def Function_23_97BD(): pass

    label("Function_23_97BD")

    OP_67(0, 6470, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Return()

    # Function_23_97BD end

    SaveToFile()

Try(main)
