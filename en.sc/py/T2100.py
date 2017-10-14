from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2100   ._SN',
            'ED6_DT21/T2100_1 ._SN',
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
        'Dorothy',                              # 10
        'Norman',                               # 11
        'Dels',                                 # 12
        'Herio',                                # 13
        'Portos',                               # 14
        'Kuper',                                # 15
        'Benoit',                               # 16
        'Tourist',                              # 17
        'Tourist',                              # 18
        'Tourist',                              # 19
        'Tourist',                              # 20
        'Tourist',                              # 21
        'Tourist',                              # 22
        'Tourist',                              # 23
        'Tourist',                              # 24
        'Tourist',                              # 25
        'Tourist',                              # 26
        'Tourist',                              # 27
        'Tourist',                              # 28
        'Tourist',                              # 29
        'Tourist',                              # 30
        'Tourist',                              # 31
        'Tourist',                              # 32
        'Tourist',                              # 33
        'Tourist',                              # 34
        'Tourist',                              # 35
        'Middle-Aged Man',                      # 36
        'Hardt',                                # 37
        'Lloyd',                                # 38
        'Lloyd',                                # 39
        'Thelma',                               # 40
        'Matilda',                              # 41
        'Phelio',                               # 42
        'Lakeisha',                             # 43
        'Kuper',                                # 44
        'Lytton',                               # 45
        'Murray',                               # 46
        'Ruvie',                                # 47
        'Atget',                                # 48
        'Herio',                                # 49
        'Sister Frieda',                        # 50
        'Santos',                               # 51
        'Boat',                                 # 52
        'Targeting Camera',                     # 53
        'Renzo',                                # 54
        'Alund',                                # 55
        'Eletta',                               # 56
        'Deen',                                 # 57
        'Rais',                                 # 58
        'Rocco',                                # 59
        'Burt',                                 # 60
        'Gull Seaside Way',                     # 61
        'Ruan - South Block',                   # 62
        'Ruan Landing Port',                    # 63
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH02070 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01500 ._CH',             # 07
        'ED6_DT07/CH01020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01070 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH01140 ._CH',             # 0E
        'ED6_DT07/CH01150 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01130 ._CH',             # 11
        'ED6_DT07/CH01250 ._CH',             # 12
        'ED6_DT06/CH20092 ._CH',             # 13
        'ED6_DT07/CH01090 ._CH',             # 14
        'ED6_DT07/CH01153 ._CH',             # 15
        'ED6_DT07/CH01170 ._CH',             # 16
        'ED6_DT07/CH01000 ._CH',             # 17
        'ED6_DT07/CH01410 ._CH',             # 18
        'ED6_DT06/CH20063 ._CH',             # 19
        'ED6_DT06/CH20064 ._CH',             # 1A
        'ED6_DT06/CH20045 ._CH',             # 1B
        'ED6_DT06/CH20039 ._CH',             # 1C
        'ED6_DT07/CH01663 ._CH',             # 1D
        'ED6_DT07/CH01290 ._CH',             # 1E
        'ED6_DT07/CH02510 ._CH',             # 1F
        'ED6_DT07/CH02520 ._CH',             # 20
        'ED6_DT07/CH02530 ._CH',             # 21
        'ED6_DT07/CH01390 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH02070P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01500P._CP',             # 07
        'ED6_DT07/CH01020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01070P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH01140P._CP',             # 0E
        'ED6_DT07/CH01150P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01130P._CP',             # 11
        'ED6_DT07/CH01250P._CP',             # 12
        'ED6_DT06/CH20092P._CP',             # 13
        'ED6_DT07/CH01090P._CP',             # 14
        'ED6_DT07/CH01153P._CP',             # 15
        'ED6_DT07/CH01170P._CP',             # 16
        'ED6_DT07/CH01000P._CP',             # 17
        'ED6_DT07/CH01410P._CP',             # 18
        'ED6_DT06/CH20063P._CP',             # 19
        'ED6_DT06/CH20064P._CP',             # 1A
        'ED6_DT06/CH20045P._CP',             # 1B
        'ED6_DT06/CH20039P._CP',             # 1C
        'ED6_DT07/CH01663P._CP',             # 1D
        'ED6_DT07/CH01290P._CP',             # 1E
        'ED6_DT07/CH02510P._CP',             # 1F
        'ED6_DT07/CH02520P._CP',             # 20
        'ED6_DT07/CH02530P._CP',             # 21
        'ED6_DT07/CH01390P._CP',             # 22
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70990,
        Z                   = 1050,
        Y                   = 79010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 22310,
        Z                   = 0,
        Y                   = 76950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 29307,
        Z                   = -1800,
        Y                   = 68254,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 21840,
        Z                   = 0,
        Y                   = 70280,
        Direction           = 60,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 23580,
        Z                   = 2160,
        Y                   = 102820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 46320,
        Z                   = 0,
        Y                   = 79740,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 47990,
        Z                   = 0,
        Y                   = 80530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 46730,
        Z                   = 0,
        Y                   = 78510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 28500,
        Z                   = 0,
        Y                   = 82470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 990,
        Z                   = -2250,
        Y                   = 94250,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 26280,
        Z                   = 0,
        Y                   = 88370,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24400,
        Z                   = 0,
        Y                   = 93520,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 54940,
        Z                   = 0,
        Y                   = 78510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 67840,
        Z                   = 500,
        Y                   = 93830,
        Direction           = 270,
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
        X                   = 39560,
        Z                   = -1770,
        Y                   = 69520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xA4,
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
        X                   = 52980,
        Z                   = 0,
        Y                   = 95770,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 43460,
        Z                   = 3500,
        Y                   = 72520,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 29170,
        Z                   = 0,
        Y                   = 89110,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51800,
        Z                   = 0,
        Y                   = 71000,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 50200,
        Z                   = 0,
        Y                   = 71000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 51000,
        Z                   = 0,
        Y                   = 72300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 93780,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 25260,
        Z                   = 0,
        Y                   = 128199,
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
        X                   = 51060,
        Z                   = 400,
        Y                   = 27190,
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
        X                   = 81750,
        Z                   = 0,
        Y                   = 80640,
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
        X                   = 20100,
        Y                   = -2000,
        Z                   = 118500,
        Range               = 28900,
        Unknown_10          = 0x708,
        Unknown_14          = 0x1D524,
        Unknown_18          = 0x0,
        Unknown_1C          = 41,
    )

    DeclEvent(
        X                   = 48500,
        Y                   = -2000,
        Z                   = 68000,
        Range               = 53500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x11170,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 67740,
        Y                   = 0,
        Z                   = 84010,
        Range               = 66350,
        Unknown_10          = 0x708,
        Unknown_14          = 0x130B0,
        Unknown_18          = 0x0,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 46730,
        Y                   = -1000,
        Z                   = 78510,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 28500,
        Y                   = -1000,
        Z                   = 82470,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 54940,
        Y                   = -1000,
        Z                   = 78510,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 50950,
        Y                   = -1000,
        Z                   = 75000,
        Range               = 3000,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 44990,
        Y                   = 0,
        Z                   = 89330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 38080,
        Y                   = 0,
        Z                   = 78540,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 58,
    )

    DeclEvent(
        X                   = 37930,
        Y                   = 0,
        Z                   = 89380,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = 30610,
        Y                   = 0,
        Z                   = 96060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 108200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 60,
    )

    DeclEvent(
        X                   = 20930,
        Y                   = -1500,
        Z                   = 93960,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 61,
    )

    DeclEvent(
        X                   = 61000,
        Y                   = 0,
        Z                   = 78900,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )

    DeclEvent(
        X                   = 66890,
        Y                   = -500,
        Z                   = 93800,
        Range               = 2200,
        Unknown_10          = 0x898,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 63,
    )

    DeclEvent(
        X                   = 73630,
        Y                   = 0,
        Z                   = 80790,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 64,
    )


    DeclActor(
        TriggerX            = 23750,
        TriggerZ            = 1000,
        TriggerY            = 102860,
        TriggerRange        = 1000,
        ActorX              = 23580,
        ActorZ              = 4000,
        ActorY              = 102820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26630,
        TriggerZ            = 0,
        TriggerY            = 86030,
        TriggerRange        = 800,
        ActorX              = 26330,
        ActorZ              = 1000,
        ActorY              = 86030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 55,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16250,
        TriggerZ            = -1800,
        TriggerY            = 112100,
        TriggerRange        = 1000,
        ActorX              = 13840,
        ActorZ              = -2500,
        ActorY              = 112130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 56,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_B0E",          # 00, 0
        "Function_1_E1D",          # 01, 1
        "Function_2_E90",          # 02, 2
        "Function_3_100D",         # 03, 3
        "Function_4_1031",         # 04, 4
        "Function_5_1055",         # 05, 5
        "Function_6_10A9",         # 06, 6
        "Function_7_14A6",         # 07, 7
        "Function_8_16DA",         # 08, 8
        "Function_9_1A57",         # 09, 9
        "Function_10_1DF1",        # 0A, 10
        "Function_11_2441",        # 0B, 11
        "Function_12_2D4E",        # 0C, 12
        "Function_13_2DCD",        # 0D, 13
        "Function_14_2E5F",        # 0E, 14
        "Function_15_2F38",        # 0F, 15
        "Function_16_3323",        # 10, 16
        "Function_17_3472",        # 11, 17
        "Function_18_3570",        # 12, 18
        "Function_19_3575",        # 13, 19
        "Function_20_3D0F",        # 14, 20
        "Function_21_3E19",        # 15, 21
        "Function_22_3EE6",        # 16, 22
        "Function_23_4353",        # 17, 23
        "Function_24_44D9",        # 18, 24
        "Function_25_468F",        # 19, 25
        "Function_26_4794",        # 1A, 26
        "Function_27_4A9E",        # 1B, 27
        "Function_28_4B37",        # 1C, 28
        "Function_29_4D93",        # 1D, 29
        "Function_30_5DA7",        # 1E, 30
        "Function_31_6C33",        # 1F, 31
        "Function_32_6F7F",        # 20, 32
        "Function_33_931A",        # 21, 33
        "Function_34_9430",        # 22, 34
        "Function_35_9451",        # 23, 35
        "Function_36_9472",        # 24, 36
        "Function_37_9DB1",        # 25, 37
        "Function_38_9DCD",        # 26, 38
        "Function_39_9E02",        # 27, 39
        "Function_40_9E37",        # 28, 40
        "Function_41_9E56",        # 29, 41
        "Function_42_A280",        # 2A, 42
        "Function_43_A359",        # 2B, 43
        "Function_44_AB5C",        # 2C, 44
        "Function_45_AD2B",        # 2D, 45
        "Function_46_AD40",        # 2E, 46
        "Function_47_AD69",        # 2F, 47
        "Function_48_AD92",        # 30, 48
        "Function_49_ADBB",        # 31, 49
        "Function_50_AEE5",        # 32, 50
        "Function_51_C116",        # 33, 51
        "Function_52_CB18",        # 34, 52
        "Function_53_D182",        # 35, 53
        "Function_54_D21A",        # 36, 54
        "Function_55_D273",        # 37, 55
        "Function_56_D312",        # 38, 56
        "Function_57_D41C",        # 39, 57
        "Function_58_D420",        # 3A, 58
        "Function_59_D424",        # 3B, 59
        "Function_60_D428",        # 3C, 60
        "Function_61_D42C",        # 3D, 61
        "Function_62_D430",        # 3E, 62
        "Function_63_D434",        # 3F, 63
        "Function_64_D438",        # 40, 64
    )


    def Function_0_B0E(): pass

    label("Function_0_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B96")
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x30, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x39, 0x80)
    SetChrPos(0x2C, 28500, 0, 82470, 45)
    SetChrPos(0x2E, 27820, 0, 98030, 225)
    SetChrPos(0x2F, 29470, 0, 97990, 45)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7D")
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x2F, 0x10)
    Jump("loc_B93")

    label("loc_B7D")

    ClearChrFlags(0x36, 0x80)
    SetChrPos(0x39, 50750, 0, 78770, 0)

    label("loc_B93")

    Jump("loc_CEA")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_BF3")
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 22804, 0, 71275, 220)
    TurnDirection(0x25, 0x27, 0)
    TurnDirection(0x27, 0x25, 0)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x27, 0x10)
    SetChrFlags(0x30, 0x80)
    SetChrPos(0x2C, 46730, 0, 78510, 0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x37, 0x80)
    Jump("loc_CEA")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_C11")
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x2F, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jump("loc_CEA")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_C8D")
    Call(0, 31)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrPos(0x2E, 47440, 0, 78530, 180)
    SetChrPos(0x2F, 46010, 0, 79440, 130)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x35, 66540, 0, 72560, 211)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 29920, -1800, 68470, 138)
    SetChrFlags(0x2D, 0x10)
    OP_71(0x12, 0x4)
    SetChrFlags(0x2F, 0x10)
    Jump("loc_CEA")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CB4")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CB1")
    ClearChrFlags(0x32, 0x80)

    label("loc_CB1")

    Jump("loc_CEA")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_CEA")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CDE")
    ClearChrFlags(0x32, 0x80)

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_END)), "loc_CEA")
    ClearChrFlags(0x25, 0x80)

    label("loc_CEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFB")
    SetChrFlags(0x2D, 0x80)

    label("loc_CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0A")
    OP_A2(0x1231)

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_D20")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_E1C")

    label("loc_D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_D3F")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 44)
    Jump("loc_E1C")

    label("loc_D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_D55")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_E1C")

    label("loc_D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_D6B")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(1, 5)
    Jump("loc_E1C")

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_D81")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(1, 4)
    Jump("loc_E1C")

    label("loc_D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_D97")
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 52)
    Jump("loc_E1C")

    label("loc_D97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB1")
    OP_A3(0x10F6)
    Event(0, 43)
    Jump("loc_E1C")

    label("loc_DB1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_DC5"),
        (105, "loc_DDD"),
        (118, "loc_E09"),
        (SWITCH_DEFAULT, "loc_E1C"),
    )


    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDA")
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_DDA")

    Jump("loc_E1C")

    label("loc_DDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD")
    SetMapFlags(0x10000000)
    Event(0, 50)
    Jump("loc_E06")

    label("loc_DFD")

    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_E06")

    Jump("loc_E1C")

    label("loc_E09")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E19")
    Call(0, 49)

    label("loc_E19")

    Jump("loc_E1C")

    label("loc_E1C")

    Return()

    # Function_0_B0E end

    def Function_1_E1D(): pass

    label("Function_1_E1D")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFF5420, 0x230047)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E40")
    OP_64(0x2, 0x1)

    label("loc_E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E55")
    OP_71(0x12, 0x4)

    label("loc_E55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F")
    OP_6F(0x11, 1500)
    OP_72(0x1A, 0x2)
    OP_71(0x12, 0x4)
    OP_71(0x1B, 0x4)
    OP_64(0x1, 0x1)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)

    label("loc_E8F")

    Return()

    # Function_1_E1D end

    def Function_2_E90(): pass

    label("Function_2_E90")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_FF7")

    label("loc_EB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_FF7")

    label("loc_ECE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_FF7")

    label("loc_EE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F00")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_FF7")

    label("loc_F00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F19")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_FF7")

    label("loc_F19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F32")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_FF7")

    label("loc_F32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_FF7")

    label("loc_F4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F64")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_FF7")

    label("loc_F64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_FF7")

    label("loc_F7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F96")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_FF7")

    label("loc_F96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_FF7")

    label("loc_FAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_FF7")

    label("loc_FC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_FF7")

    label("loc_FE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_FF7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_100C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_FF7")

    label("loc_100C")

    Return()

    # Function_2_E90 end

    def Function_3_100D(): pass

    label("Function_3_100D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1030")
    OP_8D(0xFE, 24600, 90150, 28170, 94510, 4000)
    Jump("Function_3_100D")

    label("loc_1030")

    Return()

    # Function_3_100D end

    def Function_4_1031(): pass

    label("Function_4_1031")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1054")
    OP_8D(0xFE, 28420, 86550, 31010, 89470, 4000)
    Jump("Function_4_1031")

    label("loc_1054")

    Return()

    # Function_4_1031 end

    def Function_5_1055(): pass

    label("Function_5_1055")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "I'm playing outside with Atget today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Heehee, it's so much fun! ♪\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1055 end

    def Function_6_10A9(): pass

    label("Function_6_10A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1143")

    ChrTalk(    #2
        0xFE,
        (
            "Apparently it takes a fair chunk of mira\x01",
            "to go to the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I better make some serious cash\x01",
            "on this next trip out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122E")

    label("loc_1143")

    OP_A2(0xE)

    ChrTalk(    #4
        0xFE,
        (
            "My son's got it into his head to take the\x01",
            "entrance exam for the royal academy,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "That school ain't cheap. It takes a fair\x01",
            "chunk of mira to go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Guess I'd better make some serious\x01",
            "bank on this next trip out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122E")

    Jump("loc_14A2")

    label("loc_1231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_133A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(    #7
        0xFE,
        (
            "There ain't no way to get to know someone\x01",
            "by avoidin' conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "That's what I think.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1337")

    label("loc_12A1")

    OP_A2(0xE)

    ChrTalk(    #9
        0xFE,
        (
            "If there's a bit of a brawl, well, fights\x01",
            "are part of life, as they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "There ain't no way to get to know someone\x01",
            "by avoidin' conflict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1337")

    Jump("loc_14A2")

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_139A")

    ChrTalk(    #11
        0xFE,
        "Whoa, whoa, what's goin' on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Seems like somethin's happenin' on\x01",
            "the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_13EE")

    ChrTalk(    #13
        0xFE,
        (
            "Norman's a great guy, but I just can't\x01",
            "accept his campaign platform.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_13EE")

    OP_A2(0xE)

    ChrTalk(    #14
        0xFE,
        (
            "Norman's a great guy, but I just can't\x01",
            "accept his campaign platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Ruan ain't a tourism town, it's\x01",
            "a town of sailors and fishers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I wish people would get that.\x02",
    )

    CloseMessageWindow()

    label("loc_14A2")

    TalkEnd(0xFE)
    Return()

    # Function_6_10A9 end

    def Function_7_14A6(): pass

    label("Function_7_14A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14BE")
    SetChrSubChip(0xFE, 2)
    Jump("loc_14C3")

    label("loc_14BE")

    SetChrSubChip(0xFE, 1)

    label("loc_14C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_154D")

    ChrTalk(    #17
        0xFE,
        "Ahhhh, I'd like to just stay in Ruan forever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Ahhh, I wonder if the capital-bound ships\x01",
            "will stop running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1605")

    label("loc_154D")

    OP_A2(0xD)

    ChrTalk(    #19
        0xFE,
        (
            "That first drink after a hard day at\x01",
            "work sure is special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Ahhhh, I'd like to just stay in Ruan forever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Ahhh, I wonder if the capital-bound ships\x01",
            "will stop running.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1605")

    Jump("loc_16D1")

    label("loc_1608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_16D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1663")

    ChrTalk(    #22
        0xFE,
        "Man, the sea breeze feels great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Ahhh, Ruan really is the best.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D1")

    label("loc_1663")

    OP_A2(0xD)

    ChrTalk(    #24
        0xFE,
        "Hey, everyone. Still on the job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I'm just enjoying a little vacation\x01",
            "before I ship back on home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_7_14A6 end

    def Function_8_16DA(): pass

    label("Function_8_16DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_185B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1762")

    ChrTalk(    #26
        0xFE,
        (
            "Those guys tried to make the ghost\x01",
            "thing out to be our fault!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Ahh, just thinkin' back on it ticks me off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1858")

    label("loc_1762")

    OP_A2(0xC)

    ChrTalk(    #28
        0xFE,
        (
            "Boss Portos told me to go\x01",
            "apologize to Norman, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I don't see why I've gotta go apologize even\x01",
            "though they're the ones accusin' us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Well, I guess insulting his son\x01",
            "WAS kind of a low blow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Hmm, I just can't accept it.\x02",
    )

    CloseMessageWindow()

    label("loc_1858")

    Jump("loc_1A53")

    label("loc_185B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_193B")

    ChrTalk(    #32
        0xFE,
        (
            "Mayoral Candidate Portos! Vote\x01",
            "in the election for Portoooos!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Man of the sea, Portos! Vote\x01",
            "in the election for Portoooos!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Portos will live up to your expectations!\x01",
            "Believe in his passion!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A53")

    label("loc_193B")

    OP_A2(0xC)

    ChrTalk(    #35
        0xFE,
        (
            "Like I thought, Norman's camp mobilized\x01",
            "a lot of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "It's just me out here by myself, but a man\x01",
            "of the sea fights with his guts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "All right... Time to show 'em what a\x01",
            "man of the sea is worth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Mayoral Candidate Portos! Vote\x01",
            "in the election for Portoooos!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A53")

    TalkEnd(0xFE)
    Return()

    # Function_8_16DA end

    def Function_9_1A57(): pass

    label("Function_9_1A57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B00")

    ChrTalk(    #39
        0xFE,
        (
            "That huge thing you can see faaaar\x01",
            "away in the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "No one will tell me what it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Hmm, maybe I should ask next Sunday School.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_1B72")

    label("loc_1B00")


    ChrTalk(    #42
        0xFE,
        (
            "No one will tell me what that\x01",
            "thing floating in the sky is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Hmm, maybe I should ask next Sunday School.\x02",
    )

    CloseMessageWindow()

    label("loc_1B72")

    Jump("loc_1DED")

    label("loc_1B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE4")

    ChrTalk(    #44
        0xFE,
        "Hey, Mama.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "What's that big thing floating in the sky?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Is it a new airship?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_1C24")

    label("loc_1BE4")


    ChrTalk(    #47
        0xFE,
        "Hey, Mama.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "What's that big thing floating in the sky?\x02",
    )

    CloseMessageWindow()

    label("loc_1C24")

    Jump("loc_1DED")

    label("loc_1C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1C9B")

    ChrTalk(    #49
        0xFE,
        "Mama's been staring at that poster for a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "But the guy on the poster isn't even that cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DED")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1CBC")

    ChrTalk(    #51
        0xFE,
        "Mama? What is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DED")

    label("loc_1CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D1F")

    ChrTalk(    #52
        0xFE,
        "I've got Sunday School today. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I can't wait! All my friends'll be there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DED")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1D79")

    ChrTalk(    #54
        0xFE,
        (
            "I wonder if it's the loudest person\x01",
            "who gets to be the new mayor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DED")

    label("loc_1D79")

    OP_A2(0xB)

    ChrTalk(    #55
        0xFE,
        (
            "It seems like those old guys\x01",
            "are yelling really loud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "When I asked Mama she said it was\x01",
            "an 'elecshun.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DED")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A57 end

    def Function_10_1DF1(): pass

    label("Function_10_1DF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA0")

    ChrTalk(    #57
        0xFE,
        (
            "A bunch of people ran into\x01",
            "the Bracer Guild a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Maybe something happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "At times like this it's the\x01",
            "bracers you can rely on.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1F37")

    label("loc_1EA0")


    ChrTalk(    #60
        0xFE,
        (
            "At times like this it's the\x01",
            "bracers you can rely on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Unlike the Royal Army, the Bracer Guild has\x01",
            "branches in every region. That helps a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F37")

    Jump("loc_243D")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2017")

    ChrTalk(    #62
        0xFE,
        (
            "Since the bridge isn't working, it's\x01",
            "hard to get to the South Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Really, why hasn't Mayor Norman done\x01",
            "something about this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "He can't think just arranging a ferry is enough,\x01",
            "can he?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_20A1")

    label("loc_2017")


    ChrTalk(    #65
        0xFE,
        (
            "Since the bridge isn't working, it's\x01",
            "hard to get to the South Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Really, why hasn't Mayor Norman done\x01",
            "something about this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A1")

    Jump("loc_243D")

    label("loc_20A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_219B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(    #67
        0xFE,
        "What really matters is character.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Well, not that you can really tell that\x01",
            "from a poster.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2198")

    label("loc_2118")

    OP_A2(0xA)

    ChrTalk(    #69
        0xFE,
        "What really matters is character.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I've decided to vote based on which\x01",
            "candidate proves to have the best\x01",
            "character.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2198")

    Jump("loc_243D")

    label("loc_219B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_225C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_21E7")

    ChrTalk(    #71
        0xFE,
        (
            "Unbelievable. That almost turned into\x01",
            "a real brawl...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2259")

    label("loc_21E7")

    OP_A2(0xA)

    ChrTalk(    #72
        0xFE,
        (
            "Unbelievable. That almost turned into\x01",
            "a real brawl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "How shameful.\x01",
            "They all need to just cool down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2259")

    Jump("loc_243D")

    label("loc_225C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_22CE")

    ChrTalk(    #74
        0xFE,
        (
            "Ah, looks like there's an argument\x01",
            "on the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "At this rate, a fight's going to break out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_243D")

    label("loc_22CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_239F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2347")

    ChrTalk(    #76
        0xFE,
        (
            "Candidate Portos is young and handsome,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "That's not really a good basis for voting.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239C")

    label("loc_2347")

    OP_A2(0xA)

    ChrTalk(    #78
        0xFE,
        "Hmm, who should I vote for...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Both of them lack a decisive 'something.'\x02",
    )

    CloseMessageWindow()

    label("loc_239C")

    Jump("loc_243D")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_243D")

    ChrTalk(    #80
        0xFE,
        (
            "Ah, I'm REALLY not a fan of all this promotional\x01",
            "campaigning during an election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Well, I guess I'll just have\x01",
            "to put up with it for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243D")

    TalkEnd(0xFE)
    Return()

    # Function_10_1DF1 end

    def Function_11_2441(): pass

    label("Function_11_2441")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_25B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2524")

    ChrTalk(    #82
        0xFE,
        (
            "That thing floating in the sky...\x01",
            "I wonder what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Could it be...a new Imperial weapon\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "N-No... That's ridiculous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Even the Empire couldn't make something\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_25B5")

    label("loc_2524")


    ChrTalk(    #86
        0xFE,
        (
            "That thing floating in the sky...\x01",
            "I wonder what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "That thing being an Imperial weapon of\x01",
            "some sort is kinda plausible, I guess...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B5")

    Jump("loc_2D4A")

    label("loc_25B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_273D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269D")

    ChrTalk(    #88
        0xFE,
        "H-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "That thing floating in the sky...\x01",
            "I wonder what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "If there was just some kind of statement\x01",
            "from the mayor, I'd be able to relax a bit,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "So far it's been total silence.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_273A")

    label("loc_269D")


    ChrTalk(    #92
        0xFE,
        (
            "That thing floating in the sky...\x01",
            "I wonder what it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "If there was just some kind of statement\x01",
            "from the mayor, I'd be able to relax a bit,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273A")

    Jump("loc_2D4A")

    label("loc_273D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_28AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(    #94
        0xFE,
        "Vote for Mayoral Candidate Norman, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Norman will use the tourism industry to\x01",
            "reignite the City of Ruan's furnace!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A9")

    label("loc_27D7")

    OP_A2(0x7)

    ChrTalk(    #96
        0xFE,
        (
            "Norman doesn't consider the problems\x01",
            "of the harbor minor issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I want the people of the city to know\x01",
            "that he cares about that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "All right, one more push! Time to\x01",
            "drive home this message!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A9")

    Jump("loc_295E")

    label("loc_28AC")

    OP_A2(0x6)

    ChrTalk(    #99
        0xFE,
        (
            "Norman doesn't consider the problems\x01",
            "of the harbor minor issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "If he did, I sure as heck wouldn't be\x01",
            "backing him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "After all, I used to be a fisherman myself.\x02",
    )

    CloseMessageWindow()

    label("loc_295E")

    Jump("loc_2D4A")

    label("loc_2961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_29F5")

    ChrTalk(    #102
        0xFE,
        (
            "If this division infects the whole city,\x01",
            "that'll be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Both camps really need to work\x01",
            "harder to understand each other.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADB")

    label("loc_29F5")

    OP_A2(0x6)

    ChrTalk(    #104
        0xFE,
        (
            "Oh, man, that little brouhaha\x01",
            "back there was a near thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Everyone was really angry. A few seconds\x01",
            "more and we'd have had an outright brawl\x01",
            "on our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "If this division infects the whole city,\x01",
            "that'll be bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ADB")

    Jump("loc_2D4A")

    label("loc_2ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2B77")

    ChrTalk(    #107
        0xFE,
        (
            "Once I have a bit of a breather I'm gonna\x01",
            "get back out there and campaign my heart\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "I really want Norman to be mayor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C87")

    label("loc_2B77")

    OP_A2(0x6)

    ChrTalk(    #109
        0xFE,
        (
            "I make my living as a tour guide here,\x01",
            "but I'm taking time off to support Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "The election period seems to attract less\x01",
            "tourists anyway, so I can spare the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Once I have a bit of a breather I'm gonna\x01",
            "get back out there and campaign my heart\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C87")

    Jump("loc_2D4A")

    label("loc_2C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2D4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2CDC")

    ChrTalk(    #112
        0xFE,
        (
            "Ruan's tourism is its future!\x01",
            "Your vote for Norman, please!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4A")

    label("loc_2CDC")

    OP_A2(0x6)

    ChrTalk(    #113
        0xFE,
        (
            "A vote for Mayoral Candidate Norman is\x01",
            "a vote for the tourism industry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Vote for Norman, please!\x02",
    )

    CloseMessageWindow()

    label("loc_2D4A")

    TalkEnd(0xFE)
    Return()

    # Function_11_2441 end

    def Function_12_2D4E(): pass

    label("Function_12_2D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D59")
    Return()

    label("loc_2D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2D64")
    Return()

    label("loc_2D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2D6F")
    Return()

    label("loc_2D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_2D7A")
    Return()

    label("loc_2D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D88")
    Jump("loc_2D8F")

    label("loc_2D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2D8F")

    label("loc_2D8F")

    OP_4A(0x30, 0)

    ChrTalk(    #115 op#A
        0x30,
        (
            "#4AVote for Norman!\x01",
            "Please vote for Norman!\x02",
        )
    )

    Sleep(2000)
    OP_4B(0x30, 0)
    Return()

    # Function_12_2D4E end

    def Function_13_2DCD(): pass

    label("Function_13_2DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DD8")
    Return()

    label("loc_2DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2DE3")
    Return()

    label("loc_2DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2DEE")
    Return()

    label("loc_2DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_2DF9")
    Return()

    label("loc_2DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E07")
    Jump("loc_2E0E")

    label("loc_2E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2E0E")

    label("loc_2E0E")

    OP_4A(0x2C, 0)

    ChrTalk(    #116 op#A
        0x2C,
        (
            "#4ARuan's tourism is its future!\x01",
            "Your vote for Norman, please!\x02",
        )
    )

    Sleep(2000)
    OP_4B(0x2C, 0)
    Return()

    # Function_13_2DCD end

    def Function_14_2E5F(): pass

    label("Function_14_2E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2E6A")
    Return()

    label("loc_2E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2E74")
    Jump("loc_2EA0")

    label("loc_2E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2E7F")
    Return()

    label("loc_2E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_2E8A")
    Return()

    label("loc_2E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E98")
    Jump("loc_2EA0")

    label("loc_2E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2EA0")
    Return()

    label("loc_2EA0")

    OP_4A(0x2B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2EF1")

    ChrTalk(    #117 op#A
        0x2C,
        (
            "#4ARuan's tourism is its future!\x01",
            "Your vote for Norman, please!\x02",
        )
    )

    Jump("loc_2F2E")

    label("loc_2EF1")


    ChrTalk(    #118 op#A
        0x2B,
        (
            "#4AMayoral Candidate Portos!\x01",
            "Please vote for Pooooortos!\x02",
        )
    )


    label("loc_2F2E")

    Sleep(2000)
    OP_4B(0x2B, 0)
    Return()

    # Function_14_2E5F end

    def Function_15_2F38(): pass

    label("Function_15_2F38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_30CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2FD6")

    ChrTalk(    #119
        0xFE,
        (
            "Perhaps it was rash to blame the\x01",
            "ghost on Portos' camp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "But that's no reason to speak ill of\x01",
            "Norman's son, at the very least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_2FD6")

    OP_A2(0x5)

    ChrTalk(    #121
        0xFE,
        (
            "It's true that a 'ghost' of sorts appeared\x01",
            "in the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Perhaps it was rash to blame the ghost\x01",
            "on Portos' camp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "But that's no reason to speak ill of\x01",
            "Norman's son, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Ahh, just remembering makes me angry.\x02",
    )

    CloseMessageWindow()

    label("loc_30CC")

    Jump("loc_331F")

    label("loc_30CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3178")

    ChrTalk(    #125
        0xFE,
        "Mayoral Candidate Norman, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Norman will restore us to a lively tourism city!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Please, vote in the upcoming election\x01",
            "for Norman!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3234")

    label("loc_3178")

    OP_A2(0x5)

    ChrTalk(    #128
        0xFE,
        (
            "Seems like Portos' camp managed to\x01",
            "mobilize some people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "All right, time to really get into it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "Mayoral Candidate Norman, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Vote for Norman! Norman for mayor!\x02",
    )

    CloseMessageWindow()

    label("loc_3234")

    Jump("loc_331F")

    label("loc_3237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_331F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_32CD")

    ChrTalk(    #132
        0xFE,
        "Mayoral Candidate Norman, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "Norman will restore us to a lively tourism city!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Vote for Norman! Norman for mayor!\x02",
    )

    CloseMessageWindow()
    Jump("loc_331F")

    label("loc_32CD")

    OP_A2(0x5)

    ChrTalk(    #135
        0xFE,
        "Mayoral Candidate Norman, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Vote for Norman! Norman for mayor!\x02",
    )

    CloseMessageWindow()

    label("loc_331F")

    TalkEnd(0xFE)
    Return()

    # Function_15_2F38 end

    def Function_16_3323(): pass

    label("Function_16_3323")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_33A7")

    ChrTalk(    #137
        0xFE,
        (
            "Those people yelling everywhere about\x01",
            "the election are annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "No wonder the tours are so cheap right now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_346E")

    label("loc_33A7")

    OP_A2(0x4)

    ChrTalk(    #139
        0xFE,
        (
            "The view of white buildings framed by the\x01",
            "blue sea is beautiful, but those election\x01",
            "voices are spoiling it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "It's totally ruining the atmosphere. *sigh*\x01",
            "Oh, well, nothing for it I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346E")

    TalkEnd(0xFE)
    Return()

    # Function_16_3323 end

    def Function_17_3472(): pass

    label("Function_17_3472")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_351A")

    ChrTalk(    #141
        0xFE,
        (
            "To be honest, I chose this place for our\x01",
            "vacation because I wanted to try out the\x01",
            "casino...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "But, can't skip touring the city, either,\x01",
            "now can I?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356C")

    label("loc_351A")

    OP_A2(0x3)

    ChrTalk(    #143
        0xFE,
        "Oooh, what an amazing bridge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "I'd love to see it in motion sometime.\x02",
    )

    CloseMessageWindow()

    label("loc_356C")

    TalkEnd(0xFE)
    Return()

    # Function_17_3472 end

    def Function_18_3570(): pass

    label("Function_18_3570")

    Call(0, 19)
    Return()

    # Function_18_3570 end

    def Function_19_3575(): pass

    label("Function_19_3575")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_367D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362F")

    ChrTalk(    #145
        0x28,
        (
            "That island in the sky is shining\x01",
            "with the same golden light today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x28,
        "Is that glow the door to the future?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x28,
        "Or is it a sign of the end, I wonder...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_367A")

    label("loc_362F")


    ChrTalk(    #148
        0x28,
        (
            "That island in the sky is shining\x01",
            "with the same golden light today...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367A")

    Jump("loc_3D0B")

    label("loc_367D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_37F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378A")

    ChrTalk(    #149
        0x28,
        (
            "Even if you build castles out of it,\x01",
            "sand is sand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x28,
        "Should rain fall, all will be wiped away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x28,
        (
            "That which is hardest to claim is hardest\x01",
            "to lose, and so too, that which is gained\x01",
            "easily shall pass swiftly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x28,
        "...A well-worn idiom.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_37F2")

    label("loc_378A")


    ChrTalk(    #153
        0x28,
        (
            "Even if you build castles out of it,\x01",
            "sand is sand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x28,
        "Should rain fall, it will be wiped away.\x02",
    )

    CloseMessageWindow()

    label("loc_37F2")

    Jump("loc_3D0B")

    label("loc_37F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_3966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3893")

    ChrTalk(    #155
        0x28,
        (
            "Expecting that which has happened\x01",
            "once to happen again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x28,
        (
            "The hearts of man truly are well made.\x01",
            "Most people are like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3963")

    label("loc_3893")

    OP_A2(0x2)

    ChrTalk(    #157
        0x28,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x28,
        (
            "Expecting that which has happened\x01",
            "once to happen again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x28,
        (
            "That kind of thinking is probably an inherent\x01",
            "fault in people's hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x28,
        (
            "Corruption of the soul doesn't make\x01",
            "it so, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3963")

    Jump("loc_3A13")

    label("loc_3966")


    ChrTalk(    #161
        0x28,
        (
            "To gather, to connect, to be severed,\x01",
            "and to be blown apart...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x28,
        (
            "Just like the clouds in the sky...\x01",
            "In exchange for one's freedom one must\x01",
            "bear countless farewells.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A13")

    Jump("loc_3D0B")

    label("loc_3A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3AB2")

    ChrTalk(    #163
        0x28,
        (
            "The heart of man is a mirror that\x01",
            "reflects others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x28,
        (
            "Love and hate both gain strength in their\x01",
            "shine when they are reflected back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_3AB2")

    OP_A2(0x2)

    ChrTalk(    #165
        0x28,
        (
            "The heart of man is a mirror that\x01",
            "reflects others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x28,
        (
            "If I hate you, then someday you too\x01",
            "will hate me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x28,
        (
            "And that will make my hate for\x01",
            "you grow ever stronger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B62")

    Jump("loc_3D0B")

    label("loc_3B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BEC")

    ChrTalk(    #168
        0x28,
        (
            "Ah, the blue sky is so sublimely\x01",
            "clear today again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x28,
        "See, look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x28,
        "From its heights, it looks down upon us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D0B")

    label("loc_3BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C7B")

    ChrTalk(    #171
        0x28,
        "Ah, how free one would be without a name...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x28,
        (
            "Even though like a butterfly I might have\x01",
            "been able to remain myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D0B")

    label("loc_3C7B")

    OP_A2(0x2)

    ChrTalk(    #173
        0x28,
        "I wonder what meaning names have to people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x28,
        "I am myself, and yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x28,
        (
            "Why must we use words to create\x01",
            "another self, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0B")

    TalkEnd(0x28)
    Return()

    # Function_19_3575 end

    def Function_20_3D0F(): pass

    label("Function_20_3D0F")


    ChrTalk(    #176
        0x27,
        "Uncle, you were very late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x27,
        "I've been waiting almost an hour now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x25,
        "Ahh, sorry, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x25,
        "I got a real big bite on my line outta nowhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x27,
        "You've gotta be kidding me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x27,
        "You were fishing? Inside city boundaries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x25,
        "Haha, don't get so angry.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_20_3D0F end

    def Function_21_3E19(): pass

    label("Function_21_3E19")

    TalkBegin(0xFE)
    OP_4A(0x25, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3ED7")

    ChrTalk(    #183
        0xFE,
        (
            "If you're looking for some good local food,\x01",
            "the fisherman's bar in the South Block\x01",
            "comes to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "I would think it's a much nicer place to\x01",
            "hang out than a casino.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EDE")

    label("loc_3ED7")

    OP_A2(0x1)
    Call(0, 20)

    label("loc_3EDE")

    OP_4B(0x25, 255)
    TalkEnd(0xFE)
    Return()

    # Function_21_3E19 end

    def Function_22_3EE6(): pass

    label("Function_22_3EE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3F5D")
    OP_4A(0x27, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F4F")

    ChrTalk(    #185
        0xFE,
        "Anyway, let's get a bite to eat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "Do you know a good place around here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F56")

    label("loc_3F4F")

    OP_A2(0x1)
    Call(0, 20)

    label("loc_3F56")

    OP_4B(0x27, 255)
    Jump("loc_434F")

    label("loc_3F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_400C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3FD4")

    ChrTalk(    #187
        0xFE,
        "Hmm, so it's a test of patience.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Well that's just fine. Come on,\x01",
            "let's see what you've got.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4009")

    label("loc_3FD4")

    OP_A2(0x1)

    ChrTalk(    #189
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "...Now, see. You've taken the bait.\x02",
    )

    CloseMessageWindow()

    label("loc_4009")

    Jump("loc_434F")

    label("loc_400C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_4038")

    ChrTalk(    #191
        0xFE,
        "What, what? What's the fuss?\x02",
    )

    CloseMessageWindow()
    Jump("loc_434F")

    label("loc_4038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41B3")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4070")
    SetChrSubChip(0xFE, 1)
    Jump("loc_4075")

    label("loc_4070")

    SetChrSubChip(0xFE, 2)

    label("loc_4075")

    OP_8C(0xFE, 225, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_40FE")

    ChrTalk(    #192
        0xFE,
        (
            "My friend wasn't kidding.\x01",
            "This is quite the spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "Heh heh heh...\x01",
            "Now I'm really looking forward to this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41AB")

    label("loc_40FE")

    OP_A2(0x1)

    ChrTalk(    #194
        0xFE,
        (
            "This is a pretty good spot\x01",
            "for being inside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "It's not what I'd call a traditional fishing\x01",
            "hole, but you get a lot of bites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "Just like Percy said.\x02",
    )

    CloseMessageWindow()

    label("loc_41AB")

    SetChrSubChip(0xFE, 0)
    Jump("loc_434F")

    label("loc_41B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_434F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_428F")

    ChrTalk(    #197
        0xFE,
        (
            "Ruan seems totally worked up over their\x01",
            "election, just like the rumors said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "I'm worried that the noise\x01",
            "might scare the fish away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Anyway, I'm gonna get a drink\x01",
            "then get started for real.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434F")

    label("loc_428F")

    OP_A2(0x1)

    ChrTalk(    #200
        0xFE,
        "Hey, you all. Already hard at work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Still, Ruan seems totally worked up over\x01",
            "their election, just like the rumors said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "I'm worried that the noise\x01",
            "might scare the fish away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434F")

    TalkEnd(0xFE)
    Return()

    # Function_22_3EE6 end

    def Function_23_4353(): pass

    label("Function_23_4353")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_44D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_43EE")

    ChrTalk(    #203
        0x24,
        (
            "I'm gonna wait a bit then go check out\x01",
            "the South Block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x24,
        (
            "It's got some real iffy areas, though,\x01",
            "so this could be a bit risky.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44D5")

    label("loc_43EE")

    OP_A2(0x0)

    ChrTalk(    #205
        0x24,
        "Hmm, what a lovely view.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x24,
        (
            "I'm a merchant from Bose scouting out\x01",
            "new tourist attractions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x24,
        (
            "The real draw of this city is the harbor,\x01",
            "after all. I think development of the South\x01",
            "Block will be crucial to their future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D5")

    TalkEnd(0xFE)
    Return()

    # Function_23_4353 end

    def Function_24_44D9(): pass

    label("Function_24_44D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B6")

    ChrTalk(    #208
        0xFE,
        (
            "I-I'd planned on making enough at a part\x01",
            "time job to see me through to the next\x01",
            "town, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "I blew it all already...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "Haha... What should I do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "Ha...haha...haha... Ahhhhh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4625")

    label("loc_45B6")


    ChrTalk(    #212
        0xFE,
        (
            "I-I already blew the money I earned\x01",
            "at my part-time job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Now I'm back to nothing.\x01",
            "Ha...hahahaha...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4625")

    Jump("loc_468B")

    label("loc_4628")


    ChrTalk(    #214
        0xFE,
        (
            "I gambled away everything, even\x01",
            "the mira for my ticket home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "Ahh... What should I do...?\x02",
    )

    CloseMessageWindow()

    label("loc_468B")

    TalkEnd(0xFE)
    Return()

    # Function_24_44D9 end

    def Function_25_468F(): pass

    label("Function_25_468F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4718")

    ChrTalk(    #216
        0xFE,
        (
            "#1740FI have patrol and tour duty\x01",
            "from morning till night.\x02\x03",

            "#1749FMan, I kinda get what it's like for\x01",
            "bracers now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_4790")

    label("loc_4718")


    ChrTalk(    #217
        0xFE,
        (
            "#1740FI have patrol and tour duty\x01",
            "from morning till night.\x02\x03",

            "#1749FMan, I kinda get what it's like for\x01",
            "bracers now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4790")

    TalkEnd(0xFE)
    Return()

    # Function_25_468F end

    def Function_26_4794(): pass

    label("Function_26_4794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CD")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #218
        0xFE,
        (
            "#1751FHeyyyy there, Estelle. ㈱\x02\x03",

            "#1750FI'm sure you know already, but you gotta\x01",
            "take a boat to get to the South Block.\x02\x03",

            "#1754F*siiigh* Maaan, it's tough bein' a guide.\x02\x03",

            "#1756FI mean, you know.\x01",
            "I'm a real nice guy, right?\x02\x03",

            "Everyone relies on me, and I just\x01",
            "can't turn 'em down.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_496F")

    label("loc_48CD")


    ChrTalk(    #219
        0xFE,
        (
            "#1756FI'd planned on takin' it easy, but\x01",
            "this gig's harder than I thought.\x02\x03",

            "#1751FI'm such a nice guy. I just can't say no\x01",
            "when people need my help, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496F")

    Jump("loc_4A9A")

    label("loc_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1A")

    ChrTalk(    #220
        0xFE,
        (
            "#1756FYou can't cross via the bridge, so you gotta\x01",
            "use a boat to get to the South Block, okay?\x02\x03",

            "You can get to the dock from\x01",
            "under the hotel.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_4A9A")

    label("loc_4A1A")


    ChrTalk(    #221
        0xFE,
        (
            "#1756FYou can get to the dock from\x01",
            "under the hotel.\x02\x03",

            "#1750FOne of our members is workin' that area\x01",
            "as a guide, so ask him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9A")

    TalkEnd(0xFE)
    Return()

    # Function_26_4794 end

    def Function_27_4A9E(): pass

    label("Function_27_4A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4B33")

    ChrTalk(    #222
        0xFE,
        (
            "#1763FThe city's mostly cooled down, but we\x01",
            "still don't know what might happen.\x02\x03",

            "#1760FWe're gonna keep up our guard\x01",
            "and our patrols.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B33")

    TalkEnd(0xFE)
    Return()

    # Function_27_4A9E end

    def Function_28_4B37(): pass

    label("Function_28_4B37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")

    ChrTalk(    #223
        0xFE,
        (
            "Persons going to the South Block,\x01",
            "please enter the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "You can reach the ferry port from\x01",
            "the first floor of the basement.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_4C2B")

    label("loc_4BD6")


    ChrTalk(    #225
        0xFE,
        "It's good to have something to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "At the very least, I won't be bored.\x02",
    )

    CloseMessageWindow()
    OP_A3(0x12)

    label("loc_4C2B")

    Jump("loc_4D8F")

    label("loc_4C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D08")

    ChrTalk(    #227
        0xFE,
        (
            "Ahh, currently the bridge is\x01",
            "not available for crossing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "Persons going to the South Block,\x01",
            "please enter the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "You can reach the ferry port from\x01",
            "the first floor of the basement.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_4D8F")

    label("loc_4D08")


    ChrTalk(    #230
        0xFE,
        (
            "Persons going to the South Block,\x01",
            "please enter the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "You can reach the ferry port from\x01",
            "the first floor of the basement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8F")

    TalkEnd(0xFE)
    Return()

    # Function_28_4B37 end

    def Function_29_4D93(): pass

    label("Function_29_4D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DA4")
    Return()

    label("loc_4DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB9")
    Call(0, 53)
    Call(0, 54)

    label("loc_4DB9")

    EventBegin(0x0)
    OP_4A(0x3A, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    TurnDirection(0x0, 0x3A, 0)
    TurnDirection(0x1, 0x3A, 0)
    TurnDirection(0x2, 0x3A, 0)
    TurnDirection(0x3, 0x3A, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #232
        0x101,
        "#1004FAh...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    def lambda_4E48():
        OP_6D(51000, 0, 70500, 3000)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_4E48)
    OP_0D()
    WaitChrThread(0x38, 0x1)
    Sleep(1000)
    SetChrPos(0x101, 51550, 0, 79700, 180)
    SetChrPos(0x102, 50300, 0, 80000, 180)
    SetChrPos(0xF8, 51550, 0, 80960, 180)
    SetChrPos(0xF9, 50300, 0, 81370, 180)

    ChrTalk(    #233
        0x3A,
        "#1761FHey, how's it goin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x38,
        (
            "#1741FWe're helpin' direct the citizens just like\x01",
            "we were told.\x02\x03",

            "The bridge is out of order, so if you're headin'\x01",
            "to the South Block, you gotta take a boat from\x01",
            "the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x39,
        (
            "#1750F#4PThe other members are all holdin'\x01",
            "up their positions too.\x02\x03",

            "#1751F#4PThere's a surprisin' lot of dedicated\x01",
            "guys in our group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x3A,
        (
            "#1763FYeah, they're doin' good.\x02\x03",

            "#1760FIf you see anyone slackin' off,\x01",
            "come tell me immediately.\x02\x03",

            "I'll give 'em a good punch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x38,
        "#1740FY-Yeah...\x02",
    )

    CloseMessageWindow()

    def lambda_50A3():
        OP_6D(50910, 0, 72470, 2500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_50A3)

    def lambda_50BB():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50BB)
    Sleep(100)

    def lambda_50D6():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_50D6)
    Sleep(100)

    def lambda_50F1():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_50F1)
    Sleep(100)

    def lambda_510C():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_510C)
    WaitChrThread(0xF9, 0x2)
    WaitChrThread(0x38, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51E0")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as heard about the Ravens' change\x01",              # 0
            "Set as haven't heard about the Ravens' change\x01",      # 1
            "No changes\x01",                                         # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_51D4"),
        (1, "loc_51DA"),
        (SWITCH_DEFAULT, "loc_51E0"),
    )


    label("loc_51D4")

    OP_A2(0x2080)
    Jump("loc_51E0")

    label("loc_51DA")

    OP_A3(0x2080)
    Jump("loc_51E0")

    label("loc_51E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_END)), "loc_521D")

    ChrTalk(    #238
        0x101,
        (
            "#1011F#3PHuh?\x02\x03",

            "What's THIS all about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52B3")

    label("loc_521D")


    ChrTalk(    #239
        0x101,
        (
            "#1009F#3PPunch, my butt.\x02\x03",

            "What are you guys up to sneaking\x01",
            "around like this?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52B3")

    ChrTalk(    #240
        0x106,
        (
            "#551FHmph.\x01",
            "You guys just can't move on, can you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B3")

    Jump("loc_5304")

    label("loc_52B6")


    ChrTalk(    #241
        0x101,
        (
            "#1011F#3PHuuuh... Well, that's a surprise.\x02\x03",

            "You really are working hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5304")

    OP_62(0x3A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x38, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x39, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_535E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_535E)

    def lambda_536C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_536C)

    def lambda_537A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_537A)
    Sleep(500)

    ChrTalk(    #242
        0x3A,
        "#1762F#4PY-You guys...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53CD")

    ChrTalk(    #243
        0x38,
        "#1743F#4PA-Agate...\x02",
    )

    CloseMessageWindow()
    Jump("loc_53EE")

    label("loc_53CD")


    ChrTalk(    #244
        0x38,
        "#1741F#4PHey, been a while.\x02",
    )

    CloseMessageWindow()

    label("loc_53EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_END)), "loc_545C")

    ChrTalk(    #245
        0x101,
        (
            "#1015F#3PI saw you guys here and there in\x01",
            "the South Block, but...\x02\x03",

            "What are you up to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_554B")

    label("loc_545C")


    ChrTalk(    #246
        0x101,
        (
            "#1019F#3PSo, what kind of nasty business\x01",
            "are you planning now?\x02\x03",

            "Theft? Muggings?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x39, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #247
        0x39,
        (
            "#1755FE-Estelle... You've got it all wrong,\x01",
            "I swear!\x02\x03",

            "#1756FUs Ravens have been reborn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#1004F#3PHuh? What's that mean?\x02",
    )

    CloseMessageWindow()

    label("loc_554B")


    ChrTalk(    #249
        0x38,
        (
            "#1740F#4PR-Right... So this was Rocco's plan.\x02\x03",

            "#1741FWe've been doing guide work and patrols\x01",
            "in the city for a while now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5624")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5662")

    label("loc_5624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_564B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5662")

    label("loc_564B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5662")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5689")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56C7")

    label("loc_5689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56C7")

    label("loc_56B0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_56C7")

    Sleep(1000)

    ChrTalk(    #250
        0x101,
        "#1004F#3PN-No way...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_571A")

    ChrTalk(    #251
        0x106,
        "#052FYou're not kiddin', are ya?\x02",
    )

    CloseMessageWindow()

    label("loc_571A")


    ChrTalk(    #252
        0x102,
        "#1044F#1PSo...you're essentially a neighborhood watch?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x3A,
        (
            "#1761F#4PNah. Nothin' that formal.\x02\x03",

            "We were just havin' a meetin'\x01",
            "about the future of our gang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1015F#3PWow...\x02\x03",

            "I dunno, it's just such an about-face that\x01",
            "it's hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x102,
        "#1040F#1PStill, it seems it's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x3A,
        (
            "#1763F#4PWell, we don't need you to believe\x01",
            "us anyway.\x02\x03",

            "#1764FThis ain't for anyone's sake... We're doin'\x01",
            "this on our own to settle things our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x3A, 180, 400)
    Sleep(500)

    ChrTalk(    #257
        0x3A,
        "#1760F...Anyway, let's get back to business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x38,
        "#1743F#4PY-Yeah.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x38, 315, 400)

    ChrTalk(    #259
        0x39,
        (
            "#1750FIf you wanna go to the South Block,\x01",
            "use the ferry.\x02\x03",

            "You can reach the port from\x01",
            "the basement of the hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D84")

    label("loc_59A8")


    ChrTalk(    #260
        0x39,
        (
            "#1751FHeh heh, how 'bout it, Estelle?\x02\x03",

            "You already heard about our great deeds\x01",
            "and shit, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x101,
        (
            "#1000F#3PYup. Jean told me.\x02\x03",

            "Apparently you guys helped stop the panic\x01",
            "in the city before it got out of control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x38,
        (
            "#1740FYeah, it was Rocco's idea.\x02\x03",

            "We've taken up patrollin' the city\x01",
            "and guidin' citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x102,
        (
            "#1044F#1PSo...you guys are like a neighborhood\x01",
            "watch or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x3A,
        (
            "#1761FNah. Nothin' that formal.\x02\x03",

            "We were just havin' a meetin'\x01",
            "about the future of our gang.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BF0")

    ChrTalk(    #265
        0x106,
        (
            "#053FWell, it's your way of settlin' things.\x02\x03",

            "#051FWe'll see how far you can go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF0")


    ChrTalk(    #266
        0x3A,
        (
            "#1763FWe started it on our own, and we're\x01",
            "not causin' trouble for anyone.\x02\x03",

            "#1761FOf course, by doin' this we'll be helpin'\x01",
            "the guild a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1006F#3PAh, yeah. Go for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x102,
        "#1040F#1PWe appreciate the help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x3A,
        "#1760FAnyway, we've still got a meetin'.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x3A, 180, 400)

    ChrTalk(    #270
        0x39,
        (
            "#1750FIf you wanna go to the South Block,\x01",
            "use the ferry.\x02\x03",

            "There's a dock in the basement of the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x38,
        "#1741FWell, see ya.\x02",
    )

    CloseMessageWindow()

    label("loc_5D84")

    OP_8C(0x38, 315, 400)
    OP_8C(0x39, 45, 400)
    OP_4B(0x3A, 255)
    OP_4B(0x38, 255)
    OP_4B(0x39, 255)
    OP_A2(0x20BA)
    OP_A2(0x2080)
    EventEnd(0x0)
    Return()

    # Function_29_4D93 end

    def Function_30_5DA7(): pass

    label("Function_30_5DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DB8")
    Call(0, 53)

    label("loc_5DB8")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(25350, 0, 114410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 25710, 0, 114720, 179)
    SetChrPos(0xF7, 24700, 0, 115030, 168)
    SetChrPos(0x109, 25250, 0, 113150, 181)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #272
        0x109,
        (
            "#1068F#6PAhh, finally back!\x01",
            "Feels good to be in Ruan again.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    ChrTalk(    #273
        0x109,
        (
            "#1062FThanks, guys. Was nice of you to\x01",
            "make sure I got back here safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x101,
        (
            "#1016F#6PHaha, aww, c'mon.\x01",
            "You don't need to thank us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5FA9")

    ChrTalk(    #275
        0x106,
        (
            "#051FYeah, besides, like you really\x01",
            "needed the help, anyway.\x02\x03",

            "That bowgun of yours is an antique...\x01",
            "but you're pretty good with it, don't lie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_604B")

    label("loc_5FA9")


    ChrTalk(    #276
        0x103,
        (
            "#027FYes, I hardly think you needed\x01",
            "our help, either way.\x02\x03",

            "After all, crossbows are rare these days...\x01",
            "and people who are skilled with them are\x01",
            "rarer still.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_604B")


    ChrTalk(    #277
        0x109,
        (
            "#1066FWha...? Aw, nawww. A wandering priest\x01",
            "spends a lot of time out in the wilderness,\x01",
            "y'know.\x02\x03",

            "I gotta be able to defend myself somehow,\x01",
            "but there's no way I could match a pro!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#1015F#6PYou really think so?\x02\x03",

            "I think you'd make a really good bracer,\x01",
            "actually. You're really skilled.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #279
        0x109,
        (
            "#1061FAwww, Estelle, you're makin' me blush.\x02\x03",

            "You keep the flattery up and we\x01",
            "might have to get...serious!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #280
        0x101,
        (
            "#1019F#6PI thought we agreed to knock\x01",
            "it off with the come-ons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x109,
        (
            "#1061FHaha! Anyway...\x02\x03",

            "#1060FAbout this spook you're hunting.\x01",
            "People have been coming to the\x01",
            "local church about it, too.\x02\x03",

            "But, ah, Father Theodore thinks we ain't\x01",
            "dealin' with a normal spirit, here.\x01",
            "Assuming it IS a 'spirit' at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #282
        0x101,
        "#1004F#6PReally? Why isn't it normal?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6417")

    ChrTalk(    #283
        0x106,
        (
            "#050FWell, the church likes to say that when\x01",
            "people die, all the good little boys 'n girls\x01",
            "join Aidios in the sky, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6490")

    label("loc_6417")


    ChrTalk(    #284
        0x103,
        (
            "#020FHmm... The Testaments state that when\x01",
            "a person dies, a righteous soul will\x01",
            "ascend to the sky to join Aidios...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6490")


    ChrTalk(    #285
        0x109,
        (
            "#1065FRight, and sinners are condemned to\x01",
            "fall into the darkness of Gehenna.\x02\x03",

            "Sometimes, though, you get souls who...\x01",
            "don't really fall into either camp.\x02\x03",

            "#1060FThat's what the church typically\x01",
            "refers to as a 'ghost.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #286
        0x101,
        (
            "#1007F#6PNnngaaaaaah... W-Wandering souls, ooooookay...\x02\x03",

            "#1015FBut, then, I still don't get what makes OUR\x01",
            "ghost not normal. If it's a wandering soul...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x109,
        (
            "#1063FWelllll, they don't really 'wander.'\x01",
            "According to doctrine, ghosts are\x01",
            "usually bound to something.\x02\x03",

            "Could be a place, could be a person--\x01",
            "point is, it's SOMETHING.\x02\x03",

            "The 'ghost' everyone's been reporting, though,\x01",
            "doesn't seem to behave that way.\x02\x03",

            "It's got Father Theodore worried,\x01",
            "I can tell you that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        "#1002F#6PNow I get it. Yeah, that's...worrying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x109,
        (
            "#1062FAnyway, just something to keep\x01",
            "in mind as you investigate.\x02\x03",

            "#1061FNow, I gotta get to the church!\x02\x03",

            "See ya, gang! Stay cool and spookless!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)

    def lambda_683D():
        OP_8E(0x109, 0x6356, 0x41A, 0x19262, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_683D)

    def lambda_6858():
        OP_6D(25620, 0, 112450, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6858)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)

    def lambda_687A():
        OP_6D(25470, 0, 115430, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_687A)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #290
        0x101,
        (
            "#1025F#4PHuh. That was really good advice.\x01",
            "I guess he does really know the Testaments...\x02\x03",

            "He still doesn't seem like much\x01",
            "of a priest, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_69DE")

    ChrTalk(    #291
        0x106,
        (
            "#051F#3PAh, don't sweat it too much.\x01",
            "The wanderers really are a bunch'a weirdos.\x02\x03",

            "The guy who used to come to Ravennue way\x01",
            "back when was a real bowl of nuts, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AAF")

    label("loc_69DE")


    ChrTalk(    #292
        0x103,
        (
            "#021F#3PWell, I've always heard that the\x01",
            "wandering priests are a strange bunch.\x02\x03",

            "#020FBack when I was with the troupe, we\x01",
            "had the oddest wandering sister traveling\x01",
            "with us. I never found out why, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AAF")

    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_6B65")
    OP_28(0x82, 0x1, 0x400)

    ChrTalk(    #293
        0x101,
        (
            "#1016F#4PHmm... Okay.\x02\x03",

            "#1006FSo anyway. We've heard from all the\x01",
            "witnesses Jean wanted us to talk to.\x02\x03",

            "I guess we should head back\x01",
            "to the guild now, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE6")

    label("loc_6B65")


    ChrTalk(    #294
        0x101,
        (
            "#1016F#4PHmm... Okay.\x02\x03",

            "#1006FSo anyway. We do still have some\x01",
            "people we need to talk to.\x02\x03",

            "Let's continue our investigation!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6C08")

    ChrTalk(    #295
        0x106,
        "#051F#3PAfter you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C27")

    label("loc_6C08")


    ChrTalk(    #296
        0x103,
        "#020F#3PRight behind you.\x02",
    )

    CloseMessageWindow()

    label("loc_6C27")

    OP_59()
    OP_B7(0x8)
    RemoveParty(0x8, 0xFF)
    OP_A2(0x121B)
    EventEnd(0x0)
    Return()

    # Function_30_5DA7 end

    def Function_31_6C33(): pass

    label("Function_31_6C33")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
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
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x10, 0x200)
    SetChrFlags(0x11, 0x200)
    SetChrFlags(0x12, 0x200)
    SetChrFlags(0x13, 0x200)
    SetChrFlags(0x14, 0x200)
    SetChrFlags(0x15, 0x200)
    SetChrFlags(0x16, 0x200)
    SetChrFlags(0x17, 0x200)
    SetChrFlags(0x18, 0x200)
    SetChrFlags(0x19, 0x200)
    SetChrFlags(0x1A, 0x200)
    SetChrFlags(0x1B, 0x200)
    SetChrFlags(0x1C, 0x200)
    SetChrFlags(0x1D, 0x200)
    SetChrFlags(0x1E, 0x200)
    SetChrFlags(0x1F, 0x200)
    SetChrFlags(0x20, 0x200)
    SetChrFlags(0x21, 0x200)
    SetChrFlags(0x22, 0x200)
    SetChrPos(0x8, 50530, 500, 56000, 180)
    SetChrPos(0x9, 49520, 500, 56510, 180)
    SetChrChipByIndex(0x9, 25)
    SetChrPos(0xA, 51000, 500, 53200, 180)
    SetChrPos(0xB, 52000, 500, 53900, 180)
    SetChrPos(0xC, 50000, 500, 53900, 180)
    SetChrPos(0xD, 51000, 500, 50900, 0)
    SetChrPos(0xE, 52000, 500, 50200, 0)
    SetChrPos(0xF, 50000, 500, 50200, 0)
    SetChrPos(0x10, 52430, 500, 57380, 180)
    SetChrPos(0x12, 51660, 500, 58000, 180)
    SetChrPos(0x13, 50430, 500, 58170, 180)
    SetChrPos(0x11, 51470, 500, 56000, 180)
    SetChrPos(0x15, 49980, 500, 58910, 180)
    SetChrPos(0x18, 51100, 500, 58910, 180)
    SetChrPos(0x16, 52320, 500, 58610, 180)
    SetChrPos(0x14, 49520, 500, 59500, 180)
    SetChrPos(0x19, 49520, 500, 57540, 180)
    SetChrPos(0x17, 52480, 500, 56280, 180)
    SetChrPos(0x1A, 52460, 500, 48150, 0)
    SetChrPos(0x1C, 51560, 500, 48150, 0)
    SetChrPos(0x1D, 50340, 500, 48330, 0)
    SetChrPos(0x21, 49530, 500, 48350, 0)
    SetChrPos(0x1B, 51920, 500, 47190, 0)
    SetChrPos(0x20, 50310, 500, 47010, 0)
    SetChrPos(0x1F, 49520, 500, 47190, 0)
    SetChrPos(0x22, 50900, 500, 46310, 0)
    SetChrPos(0x1E, 52460, 500, 46310, 0)
    OP_43(0x8, 0x1, 0x0, 0x2)
    OP_43(0x9, 0x1, 0x0, 0x2)
    Return()

    # Function_31_6C33 end

    def Function_32_6F7F(): pass

    label("Function_32_6F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F8C")
    Return()

    label("loc_6F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9D")
    Call(0, 53)

    label("loc_6F9D")

    EventBegin(0x0)
    Fade(500)
    OP_6D(51260, 0, 69660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 51710, 0, 69900, 180)
    SetChrPos(0xF7, 50470, 0, 70110, 180)
    OP_0D()
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0xF, 49710, 500, 50290, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    AddParty(0x3, 0xF8, 0xFF)
    ClearMapFlags(0x1)
    ClearMapFlags(0x10)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0xF7, 0x40)
    SetChrPos(0x101, 51880, 0, 66000, 180)
    SetChrPos(0xF7, 50550, 0, 66000, 180)
    OP_6D(51370, 500, 44910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4620, 0)
    OP_6C(51000, 0)
    OP_6E(262, 0)

    def lambda_70BB():
        OP_6D(51130, 500, 57140, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70BB)
    Sleep(300)

    def lambda_70D8():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_70D8)

    def lambda_70F0():
        OP_8E(0xFE, 0xC9C2, 0x1F4, 0xEF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_70F0)
    Sleep(300)

    def lambda_7110():
        OP_8E(0xFE, 0xC454, 0x1F4, 0xEFBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_7110)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    Fade(1000)
    OP_6D(51380, 500, 52340, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #297
        0xC,
        "#6PYou aren't fooling anyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        (
            "#6PWe KNOW that you're behind the\x01",
            "ghost that appeared at the hotel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xB,
        "#4PNorman's son is bedridden from the shock!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xB,
        (
            "#4PHave you no shame?! What disgusting\x01",
            "tricks WON'T you stoop to?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xF,
        (
            "#6POh, PLEASE! That 'son' is a\x01",
            "member of the Ravens!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xF,
        (
            "#6PHow do you expect us to trust something\x01",
            "a worthless THUG says?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xA,
        "#6P...Wait a moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xA,
        (
            "#6PCriticize me as you wish, but only\x01",
            "a coward would attack my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xA,
        (
            "#6PYou will retract your statement\x01",
            "calling my son a 'thug.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xD,
        "#5PUh, that...was probably a little much, there...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #307
        0xE,
        "#2PBut, but, sir! Why are you agreeing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xE,
        (
            "#2PIt's because you bend on issues\x01",
            "like this that the Tourism Party\x01",
            "dares to try such tactics!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xB, 400)

    ChrTalk(    #309
        0xC,
        "#6PWHO'S 'daring to try things'?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xB,
        "#4PThe Harbor Party is the one crossing the line!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xB,
        (
            "#4PDo you really think your harassment with\x01",
            "this ghost trick will really stop us?!\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x7D0)

    ChrTalk(    #312
        0x101,
        (
            "#1007F#4PYikes, this is really getting out of hand...\x02\x03",

            "#1002FD'you think we should step in?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_762B")

    ChrTalk(    #313
        0x106,
        (
            "#050F#6PThey ain't throwin' punches...yet.\x01",
            "So stay cool.\x02\x03",

            "Get into a good position, though.\x01",
            "If this DOES get 'real,' we need\x01",
            "to be ready to jump right in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F6")

    label("loc_762B")


    ChrTalk(    #314
        0x103,
        (
            "#022F#6PThey haven't actually gotten violent,\x01",
            "so we can't do anything...yet.\x02\x03",

            "Let's try to get into a good position,\x01",
            "though. If this does turn into fight, we\x01",
            "need to jump in immediately to stop it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F6")


    ChrTalk(    #315
        0x101,
        (
            "#1007F#4PYeah, but...rrrgh, there are so many\x01",
            "spectators we can't GET any closer.\x02\x03",

            "#1019FHow the heck did Nial manage\x01",
            "to get up front already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7790():
        OP_6D(51380, 500, 52340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7790)
    OP_62(0xE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    Sleep(100)
    OP_62(0xF, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    OP_62(0xC, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    OP_62(0xB, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #316
        0xF,
        "#6PI can't take this anymore!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xE,
        (
            "#2PDo you limp-wristed tourist-suckers think\x01",
            "you can beat us in a straight fight?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #318
        0xC,
        "#6POoooh, that's IT! Let's do this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xB,
        (
            "#4PThe employees of the Norman Firm\x01",
            "WILL uphold Mr. Norman's honor!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 300, 500)
    Sleep(300)
    OP_8C(0xA, 49, 500)
    Sleep(300)

    ChrTalk(    #320
        0xA,
        (
            "#6PSTOP, all of you!\x01",
            "Do not sink to the level of thuggery!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 124, 500)
    Sleep(300)
    OP_8C(0xD, 213, 500)
    Sleep(300)

    ChrTalk(    #321
        0xD,
        (
            "#5PEveryone, calm down!\x01",
            "We should discuss this...rationally...\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)

    ChrTalk(    #322
        0x101,
        "#1005F#4P(Oh, crap!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7A5A")

    ChrTalk(    #323
        0x106,
        (
            "#552F#6P(Son of a... Don't think we\x01",
            "can stop them now...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A99")

    label("loc_7A5A")


    ChrTalk(    #324
        0x103,
        (
            "#025F#6P(Oh, no... I don't think we\x01",
            "can stop this now...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A99")

    OP_1F(0x0, 0x190)
    Sleep(400)
    OP_20(0x0)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x19, 0x2)
    OP_71(0x19, 0x20)
    OP_71(0x19, 0x40)
    OP_6F(0x19, 301)
    OP_70(0x19, 0x168)
    OP_A1(0x33, 0x19)
    SetChrFlags(0x33, 0x40)
    SetChrPos(0x33, 30000, -2800, 52100, 90)
    OP_8C(0x33, 270, 0)
    OP_89(0x104, 30500, -2500, 52100, 90)
    SetChrChipByIndex(0x104, 27)
    SetChrSubChip(0x104, 0)

    NpcTalk(    #325
        0x104,
        "Man's Voice",
        "My goodness. What a tragedy in the making.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(40290, 500, 51970, 0)
    OP_67(0, 7050, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_43(0x33, 0x0, 0x0, 0x21)

    def lambda_7E49():
        OP_6D(47120, 500, 52000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E49)

    def lambda_7E61():
        OP_6C(270000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7E61)
    OP_0D()

    def lambda_7E72():

        label("loc_7E72")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7E72")

    QueueWorkItem2(0x101, 1, lambda_7E72)

    def lambda_7E83():

        label("loc_7E83")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7E83")

    QueueWorkItem2(0xF7, 1, lambda_7E83)

    def lambda_7E94():

        label("loc_7E94")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7E94")

    QueueWorkItem2(0x8, 1, lambda_7E94)
    Sleep(50)

    def lambda_7EAA():

        label("loc_7EAA")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7EAA")

    QueueWorkItem2(0x9, 1, lambda_7EAA)

    def lambda_7EBB():

        label("loc_7EBB")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7EBB")

    QueueWorkItem2(0xA, 1, lambda_7EBB)

    def lambda_7ECC():

        label("loc_7ECC")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7ECC")

    QueueWorkItem2(0xB, 1, lambda_7ECC)
    Sleep(50)

    def lambda_7EE2():

        label("loc_7EE2")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7EE2")

    QueueWorkItem2(0xC, 1, lambda_7EE2)

    def lambda_7EF3():

        label("loc_7EF3")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7EF3")

    QueueWorkItem2(0xD, 1, lambda_7EF3)

    def lambda_7F04():

        label("loc_7F04")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F04")

    QueueWorkItem2(0xE, 1, lambda_7F04)

    def lambda_7F15():

        label("loc_7F15")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F15")

    QueueWorkItem2(0xF, 1, lambda_7F15)
    Sleep(50)

    def lambda_7F2B():

        label("loc_7F2B")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F2B")

    QueueWorkItem2(0x10, 1, lambda_7F2B)

    def lambda_7F3C():

        label("loc_7F3C")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F3C")

    QueueWorkItem2(0x11, 1, lambda_7F3C)

    def lambda_7F4D():

        label("loc_7F4D")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F4D")

    QueueWorkItem2(0x12, 1, lambda_7F4D)
    Sleep(50)

    def lambda_7F63():

        label("loc_7F63")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F63")

    QueueWorkItem2(0x13, 1, lambda_7F63)

    def lambda_7F74():

        label("loc_7F74")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F74")

    QueueWorkItem2(0x14, 1, lambda_7F74)

    def lambda_7F85():

        label("loc_7F85")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F85")

    QueueWorkItem2(0x15, 1, lambda_7F85)
    Sleep(50)

    def lambda_7F9B():

        label("loc_7F9B")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7F9B")

    QueueWorkItem2(0x16, 1, lambda_7F9B)

    def lambda_7FAC():

        label("loc_7FAC")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7FAC")

    QueueWorkItem2(0x17, 1, lambda_7FAC)

    def lambda_7FBD():

        label("loc_7FBD")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7FBD")

    QueueWorkItem2(0x18, 1, lambda_7FBD)

    def lambda_7FCE():

        label("loc_7FCE")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7FCE")

    QueueWorkItem2(0x19, 1, lambda_7FCE)
    Sleep(50)

    def lambda_7FE4():

        label("loc_7FE4")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7FE4")

    QueueWorkItem2(0x1A, 1, lambda_7FE4)

    def lambda_7FF5():

        label("loc_7FF5")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_7FF5")

    QueueWorkItem2(0x1B, 1, lambda_7FF5)

    def lambda_8006():

        label("loc_8006")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_8006")

    QueueWorkItem2(0x1C, 1, lambda_8006)
    Sleep(50)

    def lambda_801C():

        label("loc_801C")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_801C")

    QueueWorkItem2(0x1D, 1, lambda_801C)

    def lambda_802D():

        label("loc_802D")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_802D")

    QueueWorkItem2(0x1E, 1, lambda_802D)

    def lambda_803E():

        label("loc_803E")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_803E")

    QueueWorkItem2(0x1F, 1, lambda_803E)
    Sleep(50)

    def lambda_8054():

        label("loc_8054")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_8054")

    QueueWorkItem2(0x20, 1, lambda_8054)

    def lambda_8065():

        label("loc_8065")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_8065")

    QueueWorkItem2(0x21, 1, lambda_8065)

    def lambda_8076():

        label("loc_8076")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_8076")

    QueueWorkItem2(0x22, 1, lambda_8076)
    WaitChrThread(0x33, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)
    OP_44(0x21, 0xFF)
    OP_44(0x22, 0xFF)
    Sleep(500)

    NpcTalk(    #326
        0x104,
        "Golden-Haired Man",
        (
            "#035FViolence creates nothing. It only opens\x01",
            "empty chasms between men.\x02\x03",

            "#030FTo you, I offer this song.\x02\x03",

            "A gentle, sad song, to encourage\x01",
            "you to overcome that which divides\x01",
            "your hearts and joins hands as one...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(1000)
    OP_1D(0x47)
    OP_43(0x104, 0x0, 0x0, 0x2)
    Sleep(1000)
    Sleep(500)
    OP_DB()

    NpcTalk(    #327 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#035F#50WThe sun shines,#2000W #50Wa rainbow bridge...\x05\x02",
    )

    Sleep(6500)

    NpcTalk(    #328 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#035F#50WI cross it to#1000W #50Wreach you...\x05\x02",
    )

    Sleep(6500)

    NpcTalk(    #329 op#A op#5
        0x104,
        "Golden-Haired Man",
        (
            "#70A#035F#50WAnd yet as I search...#1000W \x01",
            "#50Wit fades...into the sky...\x05\x02",
        )
    )

    Sleep(7000)

    NpcTalk(    #330 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#035F#50WDancing with loneliness#1000W #50Won the wind...\x05\x02",
    )

    Sleep(7500)

    NpcTalk(    #331 op#A op#5
        0x104,
        "Golden-Haired Man",
        (
            "#70A#032F#50WIf this wish is doomed to fade...#2000W \x01",
            "#50Wwithout ever coming true...\x05\x02",
        )
    )

    Sleep(7500)

    NpcTalk(    #332 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#032F#50WThen may it leave#2500W #50Wat least a scar...\x05\x02",
    )

    Sleep(8000)

    NpcTalk(    #333 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#032F#50WMy first promise,#2500W #50Wa promise I cannot keep...\x05\x02",
    )

    Sleep(6500)

    NpcTalk(    #334 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#035F#50WI keep your breath#3000W #50Wencased in amber...\x05\x02",
    )

    Sleep(8000)

    NpcTalk(    #335 op#A op#5
        0x104,
        "Golden-Haired Man",
        "#70A#035F#50WSealing within this#3000W #50Weternal dream...\x05\x02",
    )

    OP_21()
    Sleep(300)
    OP_4A(0x104, 255)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 28)
    SetChrSubChip(0x104, 0)
    OP_0D()
    OP_99(0x104, 0x0, 0x3, 0x5DC)
    Sleep(300)
    OP_99(0x104, 0x3, 0xA, 0x3E8)
    Sleep(500)
    OP_DC()

    ChrTalk(    #336
        0x104,
        (
            "#035FAhhh. It seems you were all\x01",
            "touched by my song.\x02\x03",

            "Remember! There is but one truth:\x02\x03",

            "#030FLove is eternal.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x104, 0x12C, 1900, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x104)
    OP_1D(0xC)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x34, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x34, 0x5DC)

    ChrTalk(    #337
        0xA,
        "#5P*cough* Ahem...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #338
        0xA,
        "#2PWell, Portos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xA,
        (
            "#2PI think it would be a good idea for\x01",
            "both of us to cool our heads a bit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #340
        0xD,
        (
            "#1PYes, I agree. Besides, we're, uh...\x01",
            "obstructing traffic. Yes...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    ChrTalk(    #341
        0xD,
        "#2PBack to the harbor, everyone!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xD, 400)

    ChrTalk(    #342
        0xF,
        "#6PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xC,
        "#4PRight, I've got flyers to distribute.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_43(0x13, 0x1, 0x0, 0x22)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x12, 0x1, 0x0, 0x22)
    Sleep(150)
    OP_43(0x1D, 0x1, 0x0, 0x23)
    OP_43(0x1E, 0x1, 0x0, 0x23)
    OP_43(0x1F, 0x1, 0x0, 0x23)
    Sleep(130)
    OP_43(0x10, 0x1, 0x0, 0x22)
    OP_43(0x11, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x22)
    OP_43(0x16, 0x1, 0x0, 0x22)
    Sleep(150)
    OP_43(0x1A, 0x1, 0x0, 0x23)
    OP_43(0x1B, 0x1, 0x0, 0x23)
    OP_43(0x1C, 0x1, 0x0, 0x23)
    Sleep(130)
    OP_43(0x17, 0x1, 0x0, 0x22)
    OP_43(0x18, 0x1, 0x0, 0x22)
    OP_43(0x19, 0x1, 0x0, 0x22)
    Sleep(150)
    OP_43(0xD, 0x1, 0x0, 0x23)
    OP_43(0xE, 0x1, 0x0, 0x23)
    OP_43(0xF, 0x1, 0x0, 0x23)
    Sleep(150)
    OP_43(0x20, 0x1, 0x0, 0x23)
    OP_43(0x21, 0x1, 0x0, 0x23)
    OP_43(0x22, 0x1, 0x0, 0x23)
    Sleep(250)
    OP_43(0xA, 0x1, 0x0, 0x22)
    OP_43(0xB, 0x1, 0x0, 0x22)
    OP_43(0xC, 0x1, 0x0, 0x22)
    Sleep(2500)

    def lambda_8B38():
        OP_8E(0xFE, 0xCA94, 0x1F4, 0xE254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B38)

    def lambda_8B53():
        OP_8E(0xFE, 0xC468, 0x1F4, 0xE0F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8B53)

    def lambda_8B6E():
        OP_8E(0xFE, 0xC15C, 0x1F4, 0xD39A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8B6E)

    def lambda_8B89():
        OP_6D(49500, 500, 55540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8B89)

    def lambda_8BA1():
        OP_67(0, 7640, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8BA1)

    def lambda_8BB9():
        OP_6B(3330, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_8BB9)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x104, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF7, 0x2)

    ChrTalk(    #344
        0x101,
        "#1019F(And the fleeing begins...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8C32")

    ChrTalk(    #345
        0x106,
        "#551F#6P(...Can't blame 'em.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C5E")

    label("loc_8C32")


    ChrTalk(    #346
        0x103,
        "#025F#6P(Somehow...I'm not surprised.)\x02",
    )

    CloseMessageWindow()

    label("loc_8C5E")


    ChrTalk(    #347
        0x104,
        (
            "#035FAh, but the citizens here are as easily stirred\x01",
            "to both action and rest as anywhere else.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0xF7, 0x104, 400)
    Sleep(200)

    ChrTalk(    #348
        0x104,
        (
            "#033FNo, what truly moves them is the\x01",
            "miraculous power of my melody!\x02\x03",

            "#031FYou there, reporters! Take photos\x01",
            "and write articles to your heart's\x01",
            "content over this day's miracle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x9,
        (
            "#150F#6POh, okay! Here we go!\x02\x03",

            "#151FSay cheeeeese! ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 26)
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sleep(500)

    ChrTalk(    #350
        0x104,
        "#035FMmm... Marvelous.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x104, 3)
    OP_0D()
    Sleep(250)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x104, 4)
    OP_0D()
    OP_8F(0x9, 0xC15C, 0x1F4, 0xC9EA, 0xBB8, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x104, 7)
    OP_0D()
    OP_8F(0x9, 0xC15C, 0x1F4, 0xCF80, 0xBB8, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x104, 10)
    OP_0D()
    OP_8F(0x9, 0xC15C, 0x1F4, 0xCB2A, 0xBB8, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0xF7, 0x8, 400)

    ChrTalk(    #351
        0x8,
        (
            "#145F#6PEr, right...\x02\x03",

            "#141FYou guys still in the mood to talk about\x01",
            "that stuff you mentioned before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        (
            "#1016FY-Yeah, sure.\x02\x03",

            "I feel like I'll forget it if we don't\x01",
            "report it soon, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_90E9")

    ChrTalk(    #353
        0x106,
        (
            "#051F#6PLet's get back to the guildhouse\x01",
            "and report to Jean a.s.a.p.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9127")

    label("loc_90E9")


    ChrTalk(    #354
        0x103,
        (
            "#021F#6PWell, then, let's hurry back\x01",
            "and report to Jean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9127")

    OP_43(0x101, 0x1, 0x0, 0x22)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x22)
    Sleep(500)
    OP_43(0x8, 0x1, 0x0, 0x22)
    Sleep(500)
    OP_69(0x104, 0x7D0)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)
    TurnDirection(0x104, 0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #355
        0x104,
        (
            "#033FHmm...?\x02\x03",

            "Oh! Estelle! To where are you going? \x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x104, 0xA2E4, 0xFFFFF4B6, 0xCB5C, 0x7D0, 0x0)
    TurnDirection(0x104, 0x101, 400)
    Sleep(500)

    ChrTalk(    #356
        0x104,
        "#036F#6PW-Wait! No, please wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x9,
        (
            "#151F#5POoooh, what a great expression!\x02\x03",

            "How heartbroken! It's so cuuuute! ㈱\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_31(0x3, 0x0, 0x29)
    OP_31(0x3, 0xFE, 0x0)
    OP_41(0x3, 0x61, 0xFF)
    OP_41(0x3, 0xFF, 0xFF)
    OP_41(0x3, 0x120, 0xFF)
    OP_41(0x3, 0x25C, 0x0)
    OP_41(0x3, 0x276, 0x1)
    OP_41(0x3, 0x26A, 0x2)
    OP_41(0x3, 0x261, 0x3)
    OP_35(0x3, 0x0)
    OP_35(0x3, 0x8C)
    OP_BB(0x3, 0x6, 0xF5)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_32_6F7F end

    def Function_33_931A(): pass

    label("Function_33_931A")

    LoadEffect(0x1, "map\\\\mp013_00.eff")
    LoadEffect(0x2, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0x33, 0, -100, 2000, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_937D():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_937D)
    Sleep(2000)

    def lambda_939D():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_939D)
    Sleep(1200)

    def lambda_93BD():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_93BD)
    Sleep(500)

    def lambda_93DD():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_93DD)
    WaitChrThread(0x33, 0x1)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0xFF, 0x33, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_33_931A end

    def Function_34_9430(): pass

    label("Function_34_9430")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xC738, 0x0, 0x102AC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_9430 end

    def Function_35_9451(): pass

    label("Function_35_9451")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xC738, 0x0, 0x9858, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_9451 end

    def Function_36_9472(): pass

    label("Function_36_9472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9483")
    Call(0, 53)

    label("loc_9483")

    EventBegin(0x0)
    AddParty(0x26, 0xFF, 0xFF)
    ClearChrFlags(0x127, 0x80)
    SetChrFlags(0x127, 0x40)
    SetChrFlags(0x104, 0x8)
    SetChrPos(0x101, 45070, 500, 91500, 180)
    SetChrPos(0xF7, 45070, 500, 91500, 180)
    SetChrPos(0x127, 45070, 500, 91500, 180)
    SetChrPos(0x104, 45070, 500, 91500, 180)
    OP_6D(45200, 0, 86800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1D)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x25)
    OP_43(0xF7, 0x1, 0x0, 0x26)
    OP_43(0x127, 0x1, 0x0, 0x27)
    OP_43(0x104, 0x1, 0x0, 0x28)
    Sleep(3800)
    OP_72(0x5, 0x800)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x104, 0x1)
    OP_71(0x5, 0x800)

    ChrTalk(    #358
        0x101,
        (
            "#1007F#5PI don't even know why I'm bothering\x01",
            "to ask at this point, but...\x02\x03",

            "#1011FI suppose you want to come too, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x104,
        (
            "#031F#4PHa-ha-ha! Oh, my dear Estelle!\x02\x03",

            "You may as well ask if fish swim or birds fly!\x02\x03",

            "#030FWhy, after all, do you think I abandoned the\x01",
            "warm, moist embrace of Elmo to come here?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_99FB")

    ChrTalk(    #360
        0x101,
        (
            "#1015F#5PFigures. Hmm.\x02\x03",

            "Agate, what do you think?\x01",
            "Should he come with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x106,
        (
            "#551F#3PWhatever. I don't care THAT much.\x02\x03",

            "#552FLet's get one thing straight, though.\x01",
            "I don't really trust you, 'pal.'\x02\x03",

            "You do anything strange,\x01",
            "and I'll wreck you. Clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x104,
        (
            "#034F#4P*sigh* Such hostility. Such negativity!\x01",
            "What a pity.\x02\x03",

            "Sometimes a wild type like you\x01",
            "isn't bad, either, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x106,
        "#055F#3P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x104,
        (
            "#037F#4PAh, but fear not!\x02\x03",

            "I shall refrain from pouring my\x01",
            "affection into your untamed vessel\x01",
            "until after I have earned your trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x106,
        "#055F#3P... \x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #366
        0x106,
        (
            "#054F#3P#3SSCREW IT. HOW ABOUT I WRECK\x01",
            "YOU RIGHT NOW, THEN?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x127, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #367
        0x127,
        (
            "#153F#5PWhoaaaa, something feels really...\x01",
            "adult here! It's...exciting...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        (
            "#1007F#5P(Oh, boy... Time to start lockin'\x01",
            "your door at night, Agate.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D92")

    label("loc_99FB")


    ChrTalk(    #369
        0x101,
        (
            "#1015F#5PFigures. Hmm.\x02\x03",

            "Schera, what do you think?\x01",
            "Should he come with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x103,
        (
            "#026F#3PWell, to be honest, I think we\x01",
            "could use the help, but...\x02\x03",

            "#027FLet me ask you one question,\x01",
            "Olivier.\x02\x03",

            "Does Cassius know you're still\x01",
            "in Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        "#1004F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x104,
        (
            "#033F#4P...\x02\x03",

            "#035FMy... Oh, Schera!\x01",
            "You wound me with such insinuations!\x02\x03",

            "#030FThe answer, however, is yes.\x01",
            "Cassius, or, shall I say, Brigadier General Bright,\x01",
            "is well aware.\x02\x03",

            "Does that answer satisfy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x101,
        "#1015F#5P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x103,
        (
            "#021F#3PFair enough.\x02\x03",

            "#027FBut since you'll be helping us,\x01",
            "don't expect me to go easy on you.\x02\x03",

            "If you don't give it your all,\x01",
            "I'll keep you up all night. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x104,
        (
            "#034F#4PEr, yes, of course. I shall commit\x01",
            "my body and soul to your cause.\x01",
            "Have no, er, fear.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x127, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #376
        0x127,
        (
            "#151F#5PWhoaaa, something feels really...\x01",
            "adult here! It's exciting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#1016F#5P(Haha, nice, Schera! Looks like\x01",
            "you know how to manage Olivier.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D92")

    OP_28(0x82, 0x1, 0x1000)
    OP_28(0x82, 0x1, 0x2000)
    OP_28(0x83, 0x4, 0x2)
    OP_28(0x83, 0x4, 0x8)
    OP_28(0x83, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_36_9472 end

    def Function_37_9DB1(): pass

    label("Function_37_9DB1")

    OP_8E(0xFE, 0xB180, 0x0, 0x14AF0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_37_9DB1 end

    def Function_38_9DCD(): pass

    label("Function_38_9DCD")

    Sleep(1000)
    OP_8E(0xFE, 0xB036, 0x0, 0x1561C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xADC0, 0x0, 0x14F50, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_38_9DCD end

    def Function_39_9E02(): pass

    label("Function_39_9E02")

    Sleep(1800)
    OP_8E(0xFE, 0xB036, 0x0, 0x1561C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB3F6, 0x0, 0x14E4C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_39_9E02 end

    def Function_40_9E37(): pass

    label("Function_40_9E37")

    Sleep(3000)
    ClearChrFlags(0x104, 0x8)
    OP_8E(0xFE, 0xB054, 0x0, 0x1564E, 0x7D0, 0x0)
    Return()

    # Function_40_9E37 end

    def Function_41_9E56(): pass

    label("Function_41_9E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F2F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9EC5")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #378
        0x106,
        (
            "#050FWe don't have time to wander off.\x01",
            "Let's hurry to the Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F14")

    label("loc_9EC5")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #379
        0x103,
        (
            "#020FWe don't have to waste.\x01",
            "We must hurry to the Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F14")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_9F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A27F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_A0E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A014")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #380
        0x106,
        (
            "#050FWe still haven't heard from Belden\x01",
            "about the ghost thing.\x02\x03",

            "We can head out of the town later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #381
        0x101,
        (
            "#1007FAh, right.\x02\x03",

            "#1006FHe's at the house to the right of\x01",
            "the mayor's mansion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0DD")

    label("loc_A014")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #382
        0x103,
        (
            "#020FWe still haven't asked that kid\x01",
            "Belden about the white shadow.\x02\x03",

            "We can leave the city later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #383
        0x101,
        (
            "#1007FAh, right.\x02\x03",

            "#1006FHe's at the house to the right of\x01",
            "the mayor's mansion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0DD")

    Jump("loc_A264")

    label("loc_A0E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A19E")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #384
        0x106,
        (
            "#050FWe still haven't asked the Ravens\x01",
            "about the ghost yet.\x02\x03",

            "We can leave town later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #385
        0x101,
        (
            "#1007FAh, right.\x02\x03",

            "#1006FWe need to go to the warehouse\x01",
            "by the harbor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A264")

    label("loc_A19E")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #386
        0x103,
        (
            "#020FWe still haven't asked those Raven\x01",
            "boys about that white shadow yet.\x02\x03",

            "We can leave the city later.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #387
        0x101,
        (
            "#1007FAh, right.\x02\x03",

            "#1006FWe need to go to the warehouse\x01",
            "by the harbor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A264")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A27F")

    Return()

    # Function_41_9E56 end

    def Function_42_A280(): pass

    label("Function_42_A280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A358")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A2EA")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #388
        0x106,
        (
            "#050FWe ain't got time to make side trips.\x01",
            "Let's hurry to the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A33D")

    label("loc_A2EA")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #389
        0x103,
        (
            "#020FWe don't have time to make side trips.\x01",
            "Let's hurry to the bridge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A33D")

    OP_90(0x0, 0xFFFFF830, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A358")

    Return()

    # Function_42_A280 end

    def Function_43_A359(): pass

    label("Function_43_A359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A36A")
    Call(0, 53)

    label("loc_A36A")

    EventBegin(0x0)
    OP_6D(44890, 0, 88850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 44960, 0, 92120, 180)
    SetChrPos(0xF7, 44960, 0, 93120, 180)
    SetChrPos(0x105, 44960, 0, 94120, 180)
    SetChrPos(0x104, 44960, 0, 95120, 180)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1D)
    OP_73(0x5)
    Sleep(500)

    def lambda_A44E():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A44E)
    Sleep(100)

    def lambda_A46E():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A46E)
    Sleep(100)

    def lambda_A48E():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A48E)

    def lambda_A4A9():
        OP_6D(44470, 0, 84530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4A9)
    Sleep(200)

    def lambda_A4C6():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4C6)
    Sleep(2700)
    OP_72(0x5, 0x800)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    OP_71(0x5, 0x800)

    def lambda_A50B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A50B)

    def lambda_A526():
        OP_90(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A526)

    def lambda_A541():
        OP_90(0xFE, 0x3E8, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A541)

    def lambda_A55C():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A55C)
    WaitChrThread(0x101, 0x1)

    def lambda_A57C():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A57C)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 90, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 270, 400)

    ChrTalk(    #390
        0x101,
        (
            "#1006F#5POkay, we're off to Zeiss!\x02\x03",

            "Anyone have anything else they\x01",
            "want to do before we go?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A658")

    ChrTalk(    #391
        0x106,
        (
            "#051F#6PNah, don't think so.\x02\x03",

            "Unless you can think of anything,\x01",
            "let's book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6A5")

    label("loc_A658")


    ChrTalk(    #392
        0x103,
        (
            "#020F#6PNo, not I.\x02\x03",

            "If you can't think of anything,\x01",
            "we should be going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6A5")


    ChrTalk(    #393
        0x104,
        (
            "#033FI can think of one piece of business...\x01",
            "where did Miss Dorothy go?\x02\x03",

            "She disappeared quite suddenly, and I'm\x01",
            "curious as to where she could have gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x101,
        (
            "#1011F#5PI think she went to go\x01",
            "see Nial in the hotel.\x02\x03",

            "That's a good point. I think we\x01",
            "should go say hi, and thanks,\x01",
            "before we leave Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x105,
        (
            "#041FHaha. Yes, I think so, too.\x01",
            "We owe Dorothy our lives, really.\x02\x03",

            "#542FI wanted to say goodbye to Matron\x01",
            "Theresa and the children before\x01",
            "we left, as well, but...\x02\x03",

            "I tried calling them from the guild a\x01",
            "minute ago and I think they're out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        (
            "#1015F#5PThey are? Aww...\x02\x03",

            "#1007FI wanted to say goodbye, too...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A9B5")

    ChrTalk(    #397
        0x106,
        (
            "#051F#6PHey, we can write 'em a letter\x01",
            "when we get to Zeiss.\x01",
            "They'll get a kick out of it.\x02\x03",

            "Worst comes to worst, ain't\x01",
            "too hard to get back here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA65")

    label("loc_A9B5")


    ChrTalk(    #398
        0x103,
        (
            "#021F#6PWell, we can always write them\x01",
            "a letter from Zeiss, you know.\x01",
            "I bet they'd love it, in fact.\x02\x03",

            "And we can always come back here\x01",
            "easily enough if we really need to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA65")


    ChrTalk(    #399
        0x105,
        (
            "#041FYes, that's true.\x01",
            "I'll write them, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x101,
        (
            "#1001F#5PHey, hey! WE'LL write them!\x01",
            "I want in, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x104,
        (
            "#035FHeh... Well, come, my friends.\x01",
            "Let us away.\x02\x03",

            "#030FTo the pulsing heart of the Orbal Revolution,\x01",
            "and the seat of geniuses!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1400)
    EventEnd(0x0)
    Return()

    # Function_43_A359 end

    def Function_44_AB5C(): pass

    label("Function_44_AB5C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearMapFlags(0x10)
    OP_6F(0x11, 1500)
    SetChrPos(0x10, 51560, 0, 69340, 180)
    SetChrPos(0x14, 50310, 0, 70350, 180)
    SetChrPos(0x15, 51050, 0, 71430, 180)
    SetChrPos(0x2C, 51850, 0, 73410, 180)
    SetChrPos(0x12, 51850, 1050, 80560, 180)
    SetChrPos(0x16, 59910, 0, 81770, 270)
    SetChrPos(0x13, 39190, 0, 82810, 90)
    SetChrPos(0x18, 37700, 0, 82310, 90)
    OP_4A(0x2C, 255)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(52150, 0, 68780, 0)
    OP_67(0, 8740, -10000, 0)
    OP_6B(4730, 0)
    OP_6C(139000, 0)
    OP_6E(343, 0)
    OP_43(0x12, 0x1, 0x0, 0x2D)
    OP_43(0x16, 0x1, 0x0, 0x2E)
    OP_43(0x13, 0x1, 0x0, 0x2F)
    OP_43(0x18, 0x1, 0x0, 0x30)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_ACBA():
        OP_6D(51840, 0, 52250, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_ACBA)

    def lambda_ACD2():
        OP_67(0, 7140, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_ACD2)

    def lambda_ACEA():
        OP_6B(4970, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_ACEA)

    def lambda_ACFA():
        OP_6C(113000, 7000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_ACFA)
    OP_6E(431, 7000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_44_AB5C end

    def Function_45_AD2B(): pass

    label("Function_45_AD2B")

    OP_8E(0xFE, 0xCA94, 0x0, 0x127E6, 0xFA0, 0x0)
    Return()

    # Function_45_AD2B end

    def Function_46_AD40(): pass

    label("Function_46_AD40")

    OP_8E(0xFE, 0xCD78, 0x0, 0x13F60, 0xFA0, 0x0)
    OP_8E(0xFE, 0xCD78, 0x0, 0x11A30, 0xFA0, 0x0)
    Return()

    # Function_46_AD40 end

    def Function_47_AD69(): pass

    label("Function_47_AD69")

    OP_8E(0xFE, 0xC1C0, 0x0, 0x13A24, 0xFA0, 0x0)
    OP_8E(0xFE, 0xC1C0, 0x0, 0x11CA6, 0xFA0, 0x0)
    Return()

    # Function_47_AD69 end

    def Function_48_AD92(): pass

    label("Function_48_AD92")

    OP_8E(0xFE, 0xC1C0, 0x0, 0x13A24, 0xFA0, 0x0)
    OP_8E(0xFE, 0xC382, 0x0, 0x122BE, 0xFA0, 0x0)
    Return()

    # Function_48_AD92 end

    def Function_49_ADBB(): pass

    label("Function_49_ADBB")

    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    OP_43(0x23, 0x0, 0x0, 0x2)
    Return()

    # Function_49_ADBB end

    def Function_50_AEE5(): pass

    label("Function_50_AEE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF06")
    Call(0, 53)
    Call(0, 54)

    label("loc_AF06")

    OP_A2(0x2035)
    SetChrPos(0x101, 6140, -2250, 93480, 270)
    SetChrPos(0x102, 6120, -2250, 92390, 270)
    SetChrPos(0xF8, 7260, -2250, 93700, 270)
    SetChrPos(0xF9, 7310, -2250, 92540, 270)
    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(2810, -2250, 93730, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A5")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as stopped by Jean's place (Ruan Branch phone fixed)\x01",                  # 0
            "Set as not yet stopped by Jean's place (Ruan Branch phone not fixed)\x01",      # 1
            "No change\x01",                                                                 # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B146"),
        (1, "loc_B14C"),
        (SWITCH_DEFAULT, "loc_B152"),
    )


    label("loc_B146")

    OP_A2(0x2001)
    Jump("loc_B152")

    label("loc_B14C")

    OP_A3(0x2001)
    Jump("loc_B152")

    label("loc_B152")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_END)), "loc_B16D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_B17E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_END)), "loc_B18F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B18F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B1A2")
    OP_A2(0x2091)
    Jump("loc_B1A5")

    label("loc_B1A2")

    OP_A3(0x2091)

    label("loc_B1A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B502")
    OP_6D(7470, -2250, 94090, 2000)

    ChrTalk(    #402
        0x101,
        "#1004F#2PWhat's all this about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x102,
        (
            "#1042F#2PSomething seems to be causing\x01",
            "a lot of confusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B240():
        OP_6D(7160, -2250, 96060, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B240)
    TurnDirection(0x23, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #404
        0x23,
        (
            "#5PYou kids looking to cross\x01",
            "over to the other side?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B29E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B29E)
    Sleep(100)

    def lambda_B2B1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B2B1)
    Sleep(100)

    def lambda_B2C4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2C4)
    Sleep(100)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #405
        0x101,
        "#1004F#2PHuh? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x23,
        (
            "#5PWhat do I...?\x02\x03",

            "Don't you know the Langland Bridge isn't\x01",
            "working and stuck raised right now?\x02\x03",

            "Thanks to that, we've got to use\x01",
            "boats to get across the river now.\x02\x03",

            "And this is the dock we're using!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        (
            "#1007F#2PThe bridge is stuck?\x01",
            "Oh, man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x102,
        (
            "#1043F#2PWell, that's...inconvenient,\x01",
            "to say the least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x23,
        (
            "#5PNo kidding it's inconvenient.\x01",
            "Frankly, I don't think the city\x01",
            "can take much more of this.\x02\x03",

            "At the direction of the mayor,\x01",
            "rides are free.\x02\x03",

            "But...thanks to that, we end\x01",
            "up backed up half an hour.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71B")

    label("loc_B502")

    OP_6D(7470, -2250, 94090, 2000)

    ChrTalk(    #410
        0x101,
        "#1004F#2POh, this must be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x102,
        "#1042F#2PThis must be the ferry Jean mentioned.\x02",
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B587():
        OP_6D(7160, -2250, 96060, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B587)
    TurnDirection(0x23, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #412
        0x23,
        (
            "#5PYou kids looking to cross\x01",
            "over to the other side?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5E5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5E5)
    Sleep(100)

    def lambda_B5F8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B5F8)
    Sleep(100)

    def lambda_B60B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B60B)
    Sleep(100)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #413
        0x101,
        (
            "#1025F#2PEr, yes! We'd like to, but, um...\x02\x03",

            "How much does it cost, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x23,
        (
            "#5PNo fare, miss, by order of the mayor.\x02\x03",

            "The wait's going to be about\x01",
            "half an hour or so, though.\x02\x03",

            "This whole thing's been murder\x01",
            "on the residents, let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B71B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B754")

    ChrTalk(    #415
        0x107,
        "#065FAwwww! That's almost forever!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B7D5")

    label("loc_B754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B790")

    ChrTalk(    #416
        0x103,
        "#025FThat...would be a bit of a wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B7D5")

    label("loc_B790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7D5")

    ChrTalk(    #417
        0x106,
        (
            "#052FThat's a bit more of a wait\x01",
            "than I expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B82D")

    ChrTalk(    #418
        0x108,
        (
            "#074FIt has to go there and back.\x01",
            "There's not much anyone can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8FC")

    label("loc_B82D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B893")

    ChrTalk(    #419
        0x106,
        (
            "#053FIt's gotta get passengers on both sides\x01",
            "of the river. Not much you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8FC")

    label("loc_B893")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8FC")

    ChrTalk(    #420
        0x103,
        (
            "#025FWell, considering it has to ferry\x01",
            "both ways, there's not much for it,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8FC")

    OP_6D(7470, -2250, 94090, 1500)

    ChrTalk(    #421
        0x102,
        (
            "#1042F#2PWell, how about it, Estelle?\x01",
            "Shall we cross over?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B953():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B953)
    Sleep(100)

    def lambda_B966():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B966)
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #422
        0x101,
        "#1015F#1PUm...\x02",
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
            "Cross to the South Side\x01",      # 0
            "Waiting is Evil!\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAA5")

    ChrTalk(    #423
        0x101,
        (
            "#1025F#1PNo, not yet, I think.\x02\x03",

            "There's still some stuff we've\x01",
            "got to do over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x102,
        (
            "#1040F#2PAll right, then.\x01",
            "Let's get out of the way.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T2132   ._SN", 108, 0, 0)
    IdleLoop()

    label("loc_BAA5")

    OP_A2(0x2036)

    ChrTalk(    #425
        0x101,
        (
            "#1007F#1PDoesn't look like there's any\x01",
            "other way across, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x102,
        "#1040F#2PLet's get in line, then.\x02",
    )

    CloseMessageWindow()
    OP_DB()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(5640, -2250, 96310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(116000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 1310, -2250, 94760, 270)
    SetChrPos(0x16, 1960, -2250, 94550, 270)
    SetChrPos(0x17, 2700, -2250, 94650, 270)
    SetChrPos(0x18, 3410, -2250, 94720, 270)
    SetChrPos(0x19, 4130, -2250, 94610, 270)
    SetChrPos(0x23, 4450, -2250, 95100, 180)
    SetChrPos(0x101, 4460, -2250, 95780, 180)
    SetChrPos(0x102, 4470, -2250, 96560, 180)
    SetChrPos(0xF8, 5090, -2250, 96860, 225)
    SetChrPos(0xF9, 5880, -2250, 96840, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(4070, -2250, 95380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    SetChrPos(0x17, 1310, -2250, 94760, 270)
    SetChrPos(0x18, 1960, -2250, 94550, 270)
    SetChrPos(0x19, 2700, -2250, 94650, 270)
    SetChrPos(0x23, 3410, -2250, 94720, 270)
    SetChrPos(0x101, 4130, -2250, 94610, 270)
    SetChrPos(0x102, 4450, -2250, 95100, 180)
    SetChrPos(0xF8, 4460, -2250, 95780, 180)
    SetChrPos(0xF9, 4470, -2250, 96560, 180)
    SetChrPos(0x13, 5090, -2250, 96860, 225)
    SetChrPos(0x12, 5880, -2250, 96840, 225)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(2540, -2250, 94610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1310, -2250, 94760, 270)
    SetChrPos(0x102, 1960, -2250, 94550, 270)
    SetChrPos(0xF8, 2700, -2250, 94650, 270)
    SetChrPos(0xF9, 3410, -2250, 94720, 270)
    SetChrPos(0x13, 4130, -2250, 94610, 270)
    SetChrPos(0x12, 4450, -2250, 95100, 180)
    SetChrPos(0x16, 4460, -2250, 95780, 180)
    SetChrPos(0x10, 4470, -2250, 96560, 180)
    SetChrPos(0x15, 5090, -2250, 96860, 225)
    SetChrPos(0x19, 5880, -2250, 96840, 225)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-600, -2250, 94270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0xFF, -1050, -3100, 92700, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x2)
    OP_71(0x20, 0x400)
    OP_71(0x20, 0x40)
    OP_71(0x20, 0x20)
    OP_B0(0x20, 0x1E)
    OP_6F(0x20, 1)
    OP_70(0x20, 0xF0)
    OP_72(0x20, 0x4)
    OP_A1(0x33, 0x20)
    SetChrPos(0x33, -810, -2850, 92590, 0)
    OP_8C(0x33, 90, 0)
    OP_4A(0x2D, 255)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x40)
    SetChrBattleFlags(0x2D, 0x20)
    OP_89(0x2D, 400, -3000, 93100, 0)
    OP_48()
    SetChrPos(0x101, -650, -2250, 94360, 180)
    SetChrPos(0x102, 280, -2250, 94270, 180)
    SetChrPos(0xF8, -50, -2250, 95350, 180)
    SetChrPos(0xF9, 1040, -2250, 95340, 180)
    SetChrPos(0x13, 2700, -2250, 94650, 270)
    SetChrPos(0x12, 3410, -2250, 94720, 270)
    SetChrPos(0x16, 4130, -2250, 94610, 270)
    SetChrPos(0x10, 4450, -2250, 95100, 180)
    SetChrPos(0x15, 4460, -2250, 95780, 180)
    SetChrPos(0x19, 4470, -2250, 96560, 180)
    OP_6D(40, -2250, 94620, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(9000, 0)
    OP_6E(390, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_DC()

    ChrTalk(    #427
        0x2D,
        (
            "#6PSorry for the wait.\x01",
            "It's your turn next.\x02\x03",

            "Onto the boat, now, come on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x102,
        "#1040F#6PThank you.\x02",
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2101   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_50_AEE5 end

    def Function_51_C116(): pass

    label("Function_51_C116")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C137")
    Call(0, 53)
    Call(0, 54)

    label("loc_C137")

    SetChrPos(0x101, 6140, -2250, 93480, 270)
    SetChrPos(0x102, 6120, -2250, 92390, 270)
    SetChrPos(0xF8, 7260, -2250, 93700, 270)
    SetChrPos(0xF9, 7310, -2250, 92540, 270)
    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(7470, -2250, 94090, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C301")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #430
        0x102,
        (
            "#1042F#2PWell, how about it, Estelle?\x01",
            "Shall we cross over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x101,
        "#1015F#2PUm...\x02",
    )

    CloseMessageWindow()

    label("loc_C301")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cross to the South Side\x01",      # 0
            "Waiting is Evil!\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C40E")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #432
        0x101,
        (
            "#1025F#1PNo, not yet, I think.\x02\x03",

            "There's still some stuff we've\x01",
            "got to do over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x102,
        (
            "#1040F#2PAll right, then.\x01",
            "Let's get out of the way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C40E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T2132   ._SN", 108, 0, 0)
    IdleLoop()

    label("loc_C427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4A1")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #434
        0x101,
        (
            "#1007F#1PDoesn't look like there's any\x01",
            "other way across, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x102,
        "#1040F#2PLet's get in line, then.\x02",
    )

    CloseMessageWindow()

    label("loc_C4A1")

    OP_DB()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(5640, -2250, 96310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(116000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 1310, -2250, 94760, 270)
    SetChrPos(0x16, 1960, -2250, 94550, 270)
    SetChrPos(0x17, 2700, -2250, 94650, 270)
    SetChrPos(0x18, 3410, -2250, 94720, 270)
    SetChrPos(0x19, 4130, -2250, 94610, 270)
    SetChrPos(0x23, 4450, -2250, 95100, 180)
    SetChrPos(0x101, 4460, -2250, 95780, 180)
    SetChrPos(0x102, 4470, -2250, 96560, 180)
    SetChrPos(0xF8, 5090, -2250, 96860, 225)
    SetChrPos(0xF9, 5880, -2250, 96840, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(4070, -2250, 95380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    SetChrPos(0x17, 1310, -2250, 94760, 270)
    SetChrPos(0x18, 1960, -2250, 94550, 270)
    SetChrPos(0x19, 2700, -2250, 94650, 270)
    SetChrPos(0x23, 3410, -2250, 94720, 270)
    SetChrPos(0x101, 4130, -2250, 94610, 270)
    SetChrPos(0x102, 4450, -2250, 95100, 180)
    SetChrPos(0xF8, 4460, -2250, 95780, 180)
    SetChrPos(0xF9, 4470, -2250, 96560, 180)
    SetChrPos(0x13, 5090, -2250, 96860, 225)
    SetChrPos(0x12, 5880, -2250, 96840, 225)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(2540, -2250, 94610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1310, -2250, 94760, 270)
    SetChrPos(0x102, 1960, -2250, 94550, 270)
    SetChrPos(0xF8, 2700, -2250, 94650, 270)
    SetChrPos(0xF9, 3410, -2250, 94720, 270)
    SetChrPos(0x13, 4130, -2250, 94610, 270)
    SetChrPos(0x12, 4450, -2250, 95100, 180)
    SetChrPos(0x16, 4460, -2250, 95780, 180)
    SetChrPos(0x10, 4470, -2250, 96560, 180)
    SetChrPos(0x15, 5090, -2250, 96860, 225)
    SetChrPos(0x19, 5880, -2250, 96840, 225)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-600, -2250, 94270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0xFF, -1050, -3100, 92700, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x2)
    OP_71(0x20, 0x400)
    OP_71(0x20, 0x40)
    OP_71(0x20, 0x20)
    OP_B0(0x20, 0x1E)
    OP_6F(0x20, 1)
    OP_70(0x20, 0xF0)
    OP_72(0x20, 0x4)
    OP_A1(0x33, 0x20)
    SetChrPos(0x33, -810, -2850, 92590, 0)
    OP_8C(0x33, 90, 0)
    OP_4A(0x2D, 255)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x40)
    SetChrBattleFlags(0x2D, 0x20)
    OP_89(0x2D, 400, -3000, 93100, 0)
    OP_48()
    SetChrPos(0x101, -650, -2250, 94360, 180)
    SetChrPos(0x102, 280, -2250, 94270, 180)
    SetChrPos(0xF8, -50, -2250, 95350, 180)
    SetChrPos(0xF9, 1040, -2250, 95340, 180)
    SetChrPos(0x13, 2700, -2250, 94650, 270)
    SetChrPos(0x12, 3410, -2250, 94720, 270)
    SetChrPos(0x16, 4130, -2250, 94610, 270)
    SetChrPos(0x10, 4450, -2250, 95100, 180)
    SetChrPos(0x15, 4460, -2250, 95780, 180)
    SetChrPos(0x19, 4470, -2250, 96560, 180)
    OP_6D(40, -2250, 94620, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(9000, 0)
    OP_6E(390, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_DC()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA8D")
    OP_A2(0x2036)

    ChrTalk(    #436
        0x2D,
        (
            "#6PSorry for the wait.\x01",
            "It's your turn next.\x02\x03",

            "Onto the boat, now, come on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x102,
        "#1040F#6PThank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAF3")

    label("loc_CA8D")


    ChrTalk(    #439
        0x2D,
        (
            "#6PAll right, your turn.\x02\x03",

            "There's a line forming behind ya,\x01",
            "so please hurry and get on the boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAF3")

    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2101   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_51_C116 end

    def Function_52_CB18(): pass

    label("Function_52_CB18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB3A")
    Call(0, 53)
    Call(0, 54)

    label("loc_CB3A")

    OP_D2(0x270003, 0x270007, 0x23)
    OP_D2(0x270013, 0x270017, 0x24)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_CB67"),
        (5, "loc_CB74"),
        (6, "loc_CB81"),
        (7, "loc_CB8E"),
        (SWITCH_DEFAULT, "loc_CB9B"),
    )


    label("loc_CB67")

    OP_D2(0x70023, 0x7002B, 0x25)
    Jump("loc_CB9B")

    label("loc_CB74")

    OP_D2(0x70053, 0x7005B, 0x25)
    Jump("loc_CB9B")

    label("loc_CB81")

    OP_D2(0x70063, 0x7006B, 0x25)
    Jump("loc_CB9B")

    label("loc_CB8E")

    OP_D2(0x70073, 0x7007B, 0x25)
    Jump("loc_CB9B")

    label("loc_CB9B")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_CBB4"),
        (5, "loc_CBC1"),
        (6, "loc_CBCE"),
        (7, "loc_CBDB"),
        (SWITCH_DEFAULT, "loc_CBE8"),
    )


    label("loc_CBB4")

    OP_D2(0x70023, 0x7002B, 0x26)
    Jump("loc_CBE8")

    label("loc_CBC1")

    OP_D2(0x70053, 0x7005B, 0x26)
    Jump("loc_CBE8")

    label("loc_CBCE")

    OP_D2(0x70063, 0x7006B, 0x26)
    Jump("loc_CBE8")

    label("loc_CBDB")

    OP_D2(0x70073, 0x7007B, 0x26)
    Jump("loc_CBE8")

    label("loc_CBE8")

    SetChrChipByIndex(0x101, 35)
    SetChrChipByIndex(0x102, 36)
    SetChrChipByIndex(0xF8, 37)
    SetChrChipByIndex(0xF9, 38)
    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_4A(0x2D, 255)
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    PlayEffect(0x0, 0x0, 0x33, 0, -150, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    OP_72(0x20, 0x4)
    OP_71(0x20, 0x2)
    OP_71(0x20, 0x40)
    OP_71(0x20, 0x20)
    OP_B0(0x20, 0x1E)
    OP_6F(0x20, 1)
    OP_70(0x20, 0xF0)
    OP_72(0x20, 0x4)
    OP_A1(0x33, 0x20)
    SetChrPos(0x33, -15000, -2850, 92590, 90)
    SetChrBattleFlags(0x2D, 0x20)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_48()
    OP_8C(0x33, 90, 0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2D, 0x1)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    ClearChrFlags(0x2D, 0x1)
    SetChrFlags(0x2D, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    OP_48()
    OP_8C(0x33, 270, 0)
    OP_89(0x101, -14050, -2800, 92360, 90)
    OP_89(0x102, -14050, -2800, 93000, 90)
    OP_89(0xF8, -15400, -2800, 93000, 90)
    OP_89(0xF9, -15400, -2800, 92360, 90)
    OP_89(0x2D, -16100, -3000, 92200, 180)
    OP_6D(-2540, -2820, 92800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_CE86():

        label("loc_CE86")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CE86")

    QueueWorkItem2(0x23, 1, lambda_CE86)

    def lambda_CE97():

        label("loc_CE97")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CE97")

    QueueWorkItem2(0x10, 1, lambda_CE97)

    def lambda_CEA8():

        label("loc_CEA8")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CEA8")

    QueueWorkItem2(0x11, 1, lambda_CEA8)

    def lambda_CEB9():

        label("loc_CEB9")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CEB9")

    QueueWorkItem2(0x12, 1, lambda_CEB9)

    def lambda_CECA():

        label("loc_CECA")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CECA")

    QueueWorkItem2(0x13, 1, lambda_CECA)

    def lambda_CEDB():

        label("loc_CEDB")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CEDB")

    QueueWorkItem2(0x14, 1, lambda_CEDB)

    def lambda_CEEC():

        label("loc_CEEC")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CEEC")

    QueueWorkItem2(0x16, 1, lambda_CEEC)

    def lambda_CEFD():

        label("loc_CEFD")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CEFD")

    QueueWorkItem2(0x17, 1, lambda_CEFD)

    def lambda_CF0E():

        label("loc_CF0E")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CF0E")

    QueueWorkItem2(0x18, 1, lambda_CF0E)

    def lambda_CF1F():

        label("loc_CF1F")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_CF1F")

    QueueWorkItem2(0x19, 1, lambda_CF1F)

    def lambda_CF30():
        OP_8F(0xFE, 0xFFFFFCE0, 0xFFFFF4DE, 0x169AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_CF30)

    def lambda_CF4B():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_CF4B)

    def lambda_CF66():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF66)

    def lambda_CF81():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF81)

    def lambda_CF9C():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_CF9C)

    def lambda_CFB7():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_CFB7)
    Sleep(2000)

    def lambda_CFD7():
        OP_6D(200, -2250, 92990, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CFD7)
    Sleep(4000)

    def lambda_CFF4():
        OP_8F(0xFE, 0xFFFFFCD6, 0xFFFFF4DE, 0x169AE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_CFF4)

    def lambda_D00F():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_D00F)

    def lambda_D02A():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D02A)

    def lambda_D045():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D045)

    def lambda_D060():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_D060)

    def lambda_D07B():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D07B)
    Sleep(2000)

    def lambda_D09B():
        OP_8F(0xFE, 0xFFFFFCD6, 0xFFFFF4DE, 0x169AE, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_D09B)

    def lambda_D0B6():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_D0B6)

    def lambda_D0D1():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0D1)

    def lambda_D0EC():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D0EC)

    def lambda_D107():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_D107)

    def lambda_D122():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D122)
    WaitChrThread(0x33, 0x1)
    OP_44(0x2D, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_82(0x0, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0xF8, 0x1)
    SetChrFlags(0xF9, 0x1)
    OP_DC()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T2132   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_52_CB18 end

    def Function_53_D182(): pass

    label("Function_53_D182")

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
        (0, "loc_D1FB"),
        (1, "loc_D201"),
        (SWITCH_DEFAULT, "loc_D207"),
    )


    label("loc_D1FB")

    OP_A2(0x1200)
    Jump("loc_D207")

    label("loc_D201")

    OP_A2(0x1201)
    Jump("loc_D207")

    label("loc_D207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D215")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_D219")

    label("loc_D215")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_D219")

    Return()

    # Function_53_D182 end

    def Function_54_D21A(): pass

    label("Function_54_D21A")

    ClearMapFlags(0x1)
    OP_6D(-11050, -2250, 166960, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_54_D21A end

    def Function_55_D273(): pass

    label("Function_55_D273")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #440
        (
            "\x07\x05《Ruan Mayoral Election》※ Make sure to go to the voting site\x01",
            "on voting day! -Election Management Committee\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_55_D273 end

    def Function_56_D312(): pass

    label("Function_56_D312")

    EventBegin(0x1)

    ChrTalk(    #441
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_D33E():
        OP_6D(15010, -1800, 111900, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D33E)

    def lambda_D356():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D356)

    def lambda_D366():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_D366)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #442
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D40C")
    OP_C0(0xE, 0x19, 0x3F7A, 0xFFFFF8F8, 0x1B5E4, 0x10E, 0x3610, 0xFFFFF510, 0x1B602)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_D41B")

    label("loc_D40C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D41B")
    EventEnd(0x1)

    label("loc_D41B")

    Return()

    # Function_56_D312 end

    def Function_57_D41C(): pass

    label("Function_57_D41C")

    SetPlaceName(0x48)
    Return()

    # Function_57_D41C end

    def Function_58_D420(): pass

    label("Function_58_D420")

    SetPlaceName(0x4D)
    Return()

    # Function_58_D420 end

    def Function_59_D424(): pass

    label("Function_59_D424")

    SetPlaceName(0x4C)
    Return()

    # Function_59_D424 end

    def Function_60_D428(): pass

    label("Function_60_D428")

    SetPlaceName(0x4A)
    Return()

    # Function_60_D428 end

    def Function_61_D42C(): pass

    label("Function_61_D42C")

    SetPlaceName(0x4E)
    Return()

    # Function_61_D42C end

    def Function_62_D430(): pass

    label("Function_62_D430")

    SetPlaceName(0x4B)
    Return()

    # Function_62_D430 end

    def Function_63_D434(): pass

    label("Function_63_D434")

    SetPlaceName(0x49)
    Return()

    # Function_63_D434 end

    def Function_64_D438(): pass

    label("Function_64_D438")

    SetPlaceName(0x4F)
    Return()

    # Function_64_D438 end

    SaveToFile()

Try(main)
