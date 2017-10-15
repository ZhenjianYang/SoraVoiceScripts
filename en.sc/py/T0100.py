from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100   ._SN',
        MapName             = 'rolent',
        Location            = 'T0100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0100_1 ._SN',
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
        'Soldier',                              # 9
        'Soldier',                              # 10
        'Aina',                                 # 11
        'Freddy',                               # 12
        'Melders',                              # 13
        'Rinon',                                # 14
        'Luke',                                 # 15
        'Pat',                                  # 16
        'Claire',                               # 17
        'Freemont',                             # 18
        'Ellie',                                # 19
        'Armand',                               # 20
        'Tico',                                 # 21
        'Morie',                                # 22
        'Ridge',                                # 23
        'Merchant',                             # 24
        'Traveler',                             # 25
        'Traveler',                             # 26
        'Grilled Cheese',                       # 27
        'Strawberry Crepe',                     # 28
        'Waffles',                              # 29
        'Maple Syrup',                          # 30
        'Bagel',                                # 31
        'Private Scott',                        # 32
        'Private Harold',                       # 33
        'Private Lacos',                        # 34
        'Private Hopper',                       # 35
        'Private Antose',                       # 36
        'Private Domingo',                      # 37
        'Private Malone',                       # 38
        'Private Max',                          # 39
        'Warrant Officer Dyne',                 # 40
        'CWO Ashton',                           # 41
        'Kitty',                                # 42
        'Anton',                                # 43
        'Ricky',                                # 44
        'Father Divine',                        # 45
        'Sister May',                           # 46
        'Attendant',                            # 47
        'Bloom',                                # 48
        'Euridice',                             # 49
        'Serra',                                # 50
        'Tabitha',                              # 51
        'Ida',                                  # 52
        'Aryll',                                # 53
        'Young Woman',                          # 54
        'エキストラ',                           # 55
        'Young Woman',                          # 56
        'エキストラ',                           # 57
        'エキストラ',                           # 58
        "Groom's Family",                       # 59
        "Groom's Family",                       # 60
        "Groom's Family",                       # 61
        "Bride's Family",                       # 62
        "Bride's Family",                       # 63
        "Bride's Family",                       # 64
        "Bride's Friend",                       # 65
        "Bride's Friend",                       # 66
        '花束',                                 # 67
        'Kitten',                               # 68
        'Kitten',                               # 69
        'Kitten',                               # 70
        'Fate',                                 # 71
        'Linde Passenger',                      # 72
        'Linde Passenger',                      # 73
        "Rolent - Mayor's Residence",           # 74
        'Rolent Landing Port',                  # 75
        'Elize Highway',                        # 76
        'Milch Main Road',                      # 77
        'Malga Trail',                          # 78
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
        'ED6_DT07/CH02560 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01000 ._CH',             # 03
        'ED6_DT27/CH03080 ._CH',             # 04
        'ED6_DT07/CH01160 ._CH',             # 05
        'ED6_DT07/CH01060 ._CH',             # 06
        'ED6_DT07/CH01070 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT07/CH01730 ._CH',             # 0B
        'ED6_DT07/CH01731 ._CH',             # 0C
        'ED6_DT07/CH01050 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH01200 ._CH',             # 0F
        'ED6_DT07/CH01220 ._CH',             # 10
        'ED6_DT07/CH01230 ._CH',             # 11
        'ED6_DT07/CH01300 ._CH',             # 12
        'ED6_DT07/CH01310 ._CH',             # 13
        'ED6_DT07/CH01770 ._CH',             # 14
        'ED6_DT07/CH01400 ._CH',             # 15
        'ED6_DT07/CH01410 ._CH',             # 16
        'ED6_DT07/CH01210 ._CH',             # 17
        'ED6_DT07/CH01010 ._CH',             # 18
        'ED6_DT07/CH01030 ._CH',             # 19
        'ED6_DT07/CH01130 ._CH',             # 1A
        'ED6_DT07/CH01700 ._CH',             # 1B
        'ED6_DT07/CH02480 ._CH',             # 1C
        'ED6_DT07/CH01180 ._CH',             # 1D
        'ED6_DT26/CH20247 ._CH',             # 1E
        'ED6_DT07/CH01033 ._CH',             # 1F
        'ED6_DT07/CH01470 ._CH',             # 20
        'ED6_DT07/CH01490 ._CH',             # 21
        'ED6_DT07/CH01480 ._CH',             # 22
        'ED6_DT27/CH03880 ._CH',             # 23
        'ED6_DT27/CH03881 ._CH',             # 24
        'ED6_DT27/CH03882 ._CH',             # 25
        'ED6_DT26/CH20311 ._CH',             # 26
        'ED6_DT07/CH01020 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH02560P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01000P._CP',             # 03
        'ED6_DT27/CH03080P._CP',             # 04
        'ED6_DT07/CH01160P._CP',             # 05
        'ED6_DT07/CH01060P._CP',             # 06
        'ED6_DT07/CH01070P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT07/CH01730P._CP',             # 0B
        'ED6_DT07/CH01731P._CP',             # 0C
        'ED6_DT07/CH01050P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH01200P._CP',             # 0F
        'ED6_DT07/CH01220P._CP',             # 10
        'ED6_DT07/CH01230P._CP',             # 11
        'ED6_DT07/CH01300P._CP',             # 12
        'ED6_DT07/CH01310P._CP',             # 13
        'ED6_DT07/CH01770P._CP',             # 14
        'ED6_DT07/CH01400P._CP',             # 15
        'ED6_DT07/CH01410P._CP',             # 16
        'ED6_DT07/CH01210P._CP',             # 17
        'ED6_DT07/CH01010P._CP',             # 18
        'ED6_DT07/CH01030P._CP',             # 19
        'ED6_DT07/CH01130P._CP',             # 1A
        'ED6_DT07/CH01700P._CP',             # 1B
        'ED6_DT07/CH02480P._CP',             # 1C
        'ED6_DT07/CH01180P._CP',             # 1D
        'ED6_DT26/CH20247P._CP',             # 1E
        'ED6_DT07/CH01033P._CP',             # 1F
        'ED6_DT07/CH01470P._CP',             # 20
        'ED6_DT07/CH01490P._CP',             # 21
        'ED6_DT07/CH01480P._CP',             # 22
        'ED6_DT27/CH03880P._CP',             # 23
        'ED6_DT27/CH03881P._CP',             # 24
        'ED6_DT27/CH03882P._CP',             # 25
        'ED6_DT26/CH20311P._CP',             # 26
        'ED6_DT07/CH01020P._CP',             # 27
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49120,
        Z                   = 0,
        Y                   = 48300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 49870,
        Z                   = 0,
        Y                   = 50090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 30420,
        Z                   = 0,
        Y                   = 40090,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 51830,
        Z                   = 0,
        Y                   = 35210,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 32700,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 31830,
        Z                   = 3250,
        Y                   = 33000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 61150,
        Z                   = 0,
        Y                   = 39190,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 60650,
        Z                   = 0,
        Y                   = 38310,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 59490,
        Z                   = 0,
        Y                   = 44360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 60290,
        Z                   = 0,
        Y                   = 42390,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 60630,
        Z                   = 0,
        Y                   = 41060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 59130,
        Z                   = 0,
        Y                   = 41140,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 430,
        Y                   = 39120,
        Direction           = 240,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 19740,
        Z                   = 0,
        Y                   = 42720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 19740,
        Z                   = 0,
        Y                   = 38120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 46620,
        Z                   = 0,
        Y                   = 12050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 51800,
        Z                   = 0,
        Y                   = 12050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 26440,
        Z                   = 0,
        Y                   = 70940,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 29720,
        Z                   = 0,
        Y                   = 70940,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 57650,
        Z                   = 0,
        Y                   = 70870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 40910,
        Z                   = 0,
        Y                   = 14450,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 51560,
        Z                   = 0,
        Y                   = 45820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 51560,
        Z                   = 0,
        Y                   = 47080,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 46300,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 57080,
        Z                   = 0,
        Y                   = 36580,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 55920,
        Z                   = 0,
        Y                   = 37500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 72900,
        Z                   = 500,
        Y                   = 33000,
        Direction           = 0,
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
        X                   = 72900,
        Z                   = 500,
        Y                   = 33000,
        Direction           = 0,
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
        X                   = 76000,
        Z                   = 0,
        Y                   = 34520,
        Direction           = 270,
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
        X                   = 75940,
        Z                   = 0,
        Y                   = 36060,
        Direction           = 225,
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
        X                   = 74350,
        Z                   = 0,
        Y                   = 41130,
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
        X                   = 75990,
        Z                   = 0,
        Y                   = 37150,
        Direction           = 225,
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
        X                   = 70250,
        Z                   = 0,
        Y                   = 36610,
        Direction           = 135,
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
        X                   = 72180,
        Z                   = 0,
        Y                   = 42370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 70420,
        Z                   = 0,
        Y                   = 41930,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 71520,
        Z                   = 0,
        Y                   = 41600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70380,
        Z                   = 0,
        Y                   = 39760,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73420,
        Z                   = 0,
        Y                   = 41930,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75970,
        Z                   = 0,
        Y                   = 40020,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70410,
        Z                   = 0,
        Y                   = 40770,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75100,
        Z                   = 0,
        Y                   = 36700,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75180,
        Z                   = 0,
        Y                   = 37580,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75230,
        Z                   = 0,
        Y                   = 38600,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70630,
        Z                   = 0,
        Y                   = 35600,
        Direction           = 135,
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
        X                   = 70920,
        Z                   = 0,
        Y                   = 37110,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70880,
        Z                   = 0,
        Y                   = 38120,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 74610,
        Z                   = 0,
        Y                   = 42650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 71320,
        Z                   = 0,
        Y                   = 42840,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72450,
        Z                   = 1000,
        Y                   = 34820,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39440,
        Z                   = 0,
        Y                   = 52410,
        Direction           = 43,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 43700,
        Z                   = 0,
        Y                   = 48980,
        Direction           = 44,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44050,
        Z                   = 0,
        Y                   = 52220,
        Direction           = 337,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 45320,
        Z                   = 0,
        Y                   = 19750,
        Direction           = 268,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 78,
    )

    DeclNpc(
        X                   = 39240,
        Z                   = 3250,
        Y                   = 34030,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 79,
    )

    DeclNpc(
        X                   = 37550,
        Z                   = 3250,
        Y                   = 34980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 80,
    )

    DeclNpc(
        X                   = 90860,
        Z                   = 0,
        Y                   = 40240,
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
        X                   = 49150,
        Z                   = 0,
        Y                   = 95090,
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
        X                   = 48960,
        Z                   = 0,
        Y                   = 1120,
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
        X                   = 5400,
        Z                   = 0,
        Y                   = 39830,
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
        X                   = 28060,
        Z                   = 0,
        Y                   = 80870,
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
        X                   = 44000,
        Y                   = 0,
        Z                   = 12250,
        Range               = 54000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x2710,
        Unknown_18          = 0x0,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 18000,
        Y                   = 0,
        Z                   = 44000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x9088,
        Unknown_18          = 0x0,
        Unknown_1C          = 85,
    )

    DeclEvent(
        X                   = 26300,
        Y                   = 0,
        Z                   = 72000,
        Range               = 29700,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x1142C,
        Unknown_18          = 0x0,
        Unknown_1C          = 84,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 92,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 93,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 94,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 95,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 96,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 96,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 97,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 98,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 99,
    )


    DeclActor(
        TriggerX            = 55000,
        TriggerZ            = 0,
        TriggerY            = 45300,
        TriggerRange        = 1700,
        ActorX              = 55000,
        ActorZ              = 2500,
        ActorY              = 45300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 87,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44710,
        TriggerZ            = 0,
        TriggerY            = 70740,
        TriggerRange        = 1500,
        ActorX              = 44710,
        ActorZ              = 1800,
        ActorY              = 70740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 88,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45280,
        TriggerZ            = 0,
        TriggerY            = 71310,
        TriggerRange        = 1500,
        ActorX              = 45280,
        ActorZ              = 1800,
        ActorY              = 71310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 89,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61370,
        TriggerZ            = 250,
        TriggerY            = 19380,
        TriggerRange        = 1000,
        ActorX              = 61370,
        ActorZ              = 1500,
        ActorY              = 19380,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 76980,
        TriggerZ            = 0,
        TriggerY            = 19020,
        TriggerRange        = 800,
        ActorX              = 76980,
        ActorZ              = 0,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CDE",          # 00, 0
        "Function_1_10C4",         # 01, 1
        "Function_2_11B2",         # 02, 2
        "Function_3_132F",         # 03, 3
        "Function_4_13A6",         # 04, 4
        "Function_5_1487",         # 05, 5
        "Function_6_14AB",         # 06, 6
        "Function_7_17F3",         # 07, 7
        "Function_8_1934",         # 08, 8
        "Function_9_1A39",         # 09, 9
        "Function_10_1A94",        # 0A, 10
        "Function_11_1C48",        # 0B, 11
        "Function_12_1CB4",        # 0C, 12
        "Function_13_1CCD",        # 0D, 13
        "Function_14_1D0F",        # 0E, 14
        "Function_15_1D58",        # 0F, 15
        "Function_16_1DA3",        # 10, 16
        "Function_17_1DF1",        # 11, 17
        "Function_18_1E31",        # 12, 18
        "Function_19_2BCD",        # 13, 19
        "Function_20_30CD",        # 14, 20
        "Function_21_3962",        # 15, 21
        "Function_22_3B43",        # 16, 22
        "Function_23_3BD6",        # 17, 23
        "Function_24_45A2",        # 18, 24
        "Function_25_5C7A",        # 19, 25
        "Function_26_5E5D",        # 1A, 26
        "Function_27_6076",        # 1B, 27
        "Function_28_64EF",        # 1C, 28
        "Function_29_658D",        # 1D, 29
        "Function_30_6618",        # 1E, 30
        "Function_31_66A6",        # 1F, 31
        "Function_32_68F7",        # 20, 32
        "Function_33_6987",        # 21, 33
        "Function_34_6B8C",        # 22, 34
        "Function_35_6D39",        # 23, 35
        "Function_36_6FD5",        # 24, 36
        "Function_37_72C0",        # 25, 37
        "Function_38_7386",        # 26, 38
        "Function_39_7656",        # 27, 39
        "Function_40_781D",        # 28, 40
        "Function_41_79DF",        # 29, 41
        "Function_42_7B37",        # 2A, 42
        "Function_43_7C2E",        # 2B, 43
        "Function_44_845C",        # 2C, 44
        "Function_45_84B1",        # 2D, 45
        "Function_46_8640",        # 2E, 46
        "Function_47_8987",        # 2F, 47
        "Function_48_98FB",        # 30, 48
        "Function_49_9935",        # 31, 49
        "Function_50_9965",        # 32, 50
        "Function_51_9995",        # 33, 51
        "Function_52_99F9",        # 34, 52
        "Function_53_9B6D",        # 35, 53
        "Function_54_9CCA",        # 36, 54
        "Function_55_9E37",        # 37, 55
        "Function_56_A348",        # 38, 56
        "Function_57_A752",        # 39, 57
        "Function_58_A7A0",        # 3A, 58
        "Function_59_A901",        # 3B, 59
        "Function_60_A973",        # 3C, 60
        "Function_61_A9EA",        # 3D, 61
        "Function_62_AA79",        # 3E, 62
        "Function_63_AB0D",        # 3F, 63
        "Function_64_AB8D",        # 40, 64
        "Function_65_AC10",        # 41, 65
        "Function_66_CF4C",        # 42, 66
        "Function_67_CF8E",        # 43, 67
        "Function_68_CFD0",        # 44, 68
        "Function_69_D005",        # 45, 69
        "Function_70_D03A",        # 46, 70
        "Function_71_D07F",        # 47, 71
        "Function_72_D0C4",        # 48, 72
        "Function_73_D109",        # 49, 73
        "Function_74_D12A",        # 4A, 74
        "Function_75_D163",        # 4B, 75
        "Function_76_D179",        # 4C, 76
        "Function_77_D1BB",        # 4D, 77
        "Function_78_D813",        # 4E, 78
        "Function_79_DBF3",        # 4F, 79
        "Function_80_DD69",        # 50, 80
        "Function_81_DEAA",        # 51, 81
        "Function_82_DF45",        # 52, 82
        "Function_83_DF97",        # 53, 83
        "Function_84_DFF0",        # 54, 84
        "Function_85_E303",        # 55, 85
        "Function_86_E51B",        # 56, 86
        "Function_87_E601",        # 57, 87
        "Function_88_E776",        # 58, 88
        "Function_89_E7BF",        # 59, 89
        "Function_90_E80C",        # 5A, 90
        "Function_91_E830",        # 5B, 91
        "Function_92_E8B8",        # 5C, 92
        "Function_93_E8BC",        # 5D, 93
        "Function_94_E8C0",        # 5E, 94
        "Function_95_E8C4",        # 5F, 95
        "Function_96_E8C8",        # 60, 96
        "Function_97_E8CC",        # 61, 97
        "Function_98_E8D0",        # 62, 98
        "Function_99_E8D4",        # 63, 99
    )


    def Function_0_CDE(): pass

    label("Function_0_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E2B")
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    SetChrPos(0xE, 49900, 0, 72100, 0)
    SetChrPos(0xF, 46900, 0, 74100, 0)
    OP_43(0xE, 0x2, 0x0, 0xB)
    OP_43(0xF, 0x2, 0x0, 0xC)
    OP_43(0xE, 0x1, 0x0, 0x2)
    OP_43(0xF, 0x1, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA3")
    SetChrPos(0x33, 39880, 0, 53180, 125)
    SetChrFlags(0x33, 0x10)
    ClearChrFlags(0x33, 0x80)
    OP_43(0x33, 0x0, 0x0, 0x2)
    SetChrPos(0x34, 39880, 0, 53850, 125)
    ClearChrFlags(0x34, 0x80)
    OP_43(0x34, 0x0, 0x0, 0x2)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    SetChrFlags(0x44, 0x40)
    SetChrFlags(0x45, 0x40)
    OP_43(0x44, 0x1, 0x0, 0x9)
    OP_43(0x45, 0x1, 0x0, 0x9)
    ClearChrFlags(0x46, 0x80)
    Jump("loc_E28")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_E28")

    label("loc_DC2")

    SetChrFlags(0x11, 0x80)
    SetChrPos(0x33, 39880, 0, 53180, 125)
    ClearChrFlags(0x33, 0x80)
    OP_43(0x33, 0x0, 0x0, 0x2)
    SetChrPos(0x34, 39880, 0, 53850, 125)
    ClearChrFlags(0x34, 0x80)
    OP_43(0x34, 0x0, 0x0, 0x2)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    SetChrFlags(0x44, 0x40)
    SetChrFlags(0x45, 0x40)
    OP_43(0x44, 0x1, 0x0, 0x9)
    OP_43(0x45, 0x1, 0x0, 0x9)

    label("loc_E28")

    Jump("loc_1001")

    label("loc_E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_EA0")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x33, 39890, 0, 53530, 180)
    ClearChrFlags(0x33, 0x80)
    OP_43(0x33, 0x0, 0x0, 0x2)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 40130, 0, 52240, 0)
    OP_43(0x34, 0x0, 0x0, 0x2)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    SetChrFlags(0x44, 0x40)
    SetChrFlags(0x45, 0x40)
    OP_43(0x44, 0x1, 0x0, 0x9)
    OP_43(0x45, 0x1, 0x0, 0x9)
    Jump("loc_1001")

    label("loc_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_F06")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 51560, 0, 47080, 270)
    Jump("loc_1001")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_F8F")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, 45200, 0, 19640, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_F8C")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8C")
    SetChrFlags(0x28, 0x10)
    SetChrFlags(0x27, 0x10)

    label("loc_F8C")

    Jump("loc_1001")

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_FF7")
    ClearChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x10)
    SetChrFlags(0x33, 0x4)
    SetChrChipByIndex(0x33, 31)
    SetChrPos(0x33, 39420, 250, 51560, 315)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 38700, 0, 50720, 315)
    OP_43(0x34, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF4")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)

    label("loc_FF4")

    Jump("loc_1001")

    label("loc_FF7")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_1001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1012")
    OP_A3(0x10F0)
    Event(0, 47)
    Jump("loc_10C3")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_102C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 56)
    Jump("loc_10C3")

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1042")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 58)
    Jump("loc_10C3")

    label("loc_1042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_1061")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 65)
    Jump("loc_10C3")

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B4")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (119, "loc_108D"),
        (120, "loc_1099"),
        (121, "loc_10A5"),
        (SWITCH_DEFAULT, "loc_10B1"),
    )


    label("loc_108D")

    SetMapFlags(0x10000000)
    Event(0, 52)
    Jump("loc_10B1")

    label("loc_1099")

    SetMapFlags(0x10000000)
    Event(0, 53)
    Jump("loc_10B1")

    label("loc_10A5")

    SetMapFlags(0x10000000)
    Event(0, 54)
    Jump("loc_10B1")

    label("loc_10B1")

    Jump("loc_10C3")

    label("loc_10B4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_10C0"),
        (SWITCH_DEFAULT, "loc_10C3"),
    )


    label("loc_10C0")

    Jump("loc_10C3")

    label("loc_10C3")

    Return()

    # Function_0_CDE end

    def Function_1_10C4(): pass

    label("Function_1_10C4")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEA840, 0x230001)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EE")
    OP_B1("t0100_n")
    Jump("loc_112B")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1122")
    OP_B1("t0100_y")
    OP_11(0xDB, 0xB7, 0xFF, 0x0, 0xFF78, 0x0)
    Jump("loc_112B")

    label("loc_1122")

    OP_B1("t0100_n")

    label("loc_112B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1156")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_116B")

    label("loc_1156")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_116B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1177")
    OP_64(0x4, 0x1)

    label("loc_1177")

    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119B")
    OP_65(0x3, 0x1)

    label("loc_119B")

    OP_71(0x2F, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B1")
    OP_72(0x2F, 0x4)

    label("loc_11B1")

    Return()

    # Function_1_10C4 end

    def Function_2_11B2(): pass

    label("Function_2_11B2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D7")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1319")

    label("loc_11D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F0")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1319")

    label("loc_11F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1209")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1319")

    label("loc_1209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1222")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1319")

    label("loc_1222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1319")

    label("loc_123B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1254")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1319")

    label("loc_1254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126D")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1319")

    label("loc_126D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1286")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1319")

    label("loc_1286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1319")

    label("loc_129F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1319")

    label("loc_12B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D1")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1319")

    label("loc_12D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EA")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1319")

    label("loc_12EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1303")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1319")

    label("loc_1303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1319")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1319")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_132E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1319")

    label("loc_132E")

    Return()

    # Function_2_11B2 end

    def Function_3_132F(): pass

    label("Function_3_132F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1353")

    label("loc_1336")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1350")
    OP_93(0xFE, 0xE, 0x4B0, 0x1838, 0x0)
    Jump("loc_1336")

    label("loc_1350")

    Jump("loc_13A5")

    label("loc_1353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A5")
    OP_8D(0xFE, 48000, 49500, 50500, 50500, 3000)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A2")
    TurnDirection(0xFE, 0xE, 400)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A2")

    Jump("loc_1353")

    label("loc_13A5")

    Return()

    # Function_3_132F end

    def Function_4_13A6(): pass

    label("Function_4_13A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1434")

    label("loc_13AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1431")
    OP_8E(0xFE, 0xBF04, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xA5A0, 0x1770, 0x0)
    OP_8E(0xFE, 0xE614, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0xEA60, 0x1770, 0x0)
    OP_8E(0xFE, 0xE09C, 0x0, 0x115BC, 0x1770, 0x0)
    OP_8E(0xFE, 0xBF04, 0x0, 0x115BC, 0x1770, 0x0)
    Jump("loc_13AD")

    label("loc_1431")

    Jump("loc_1486")

    label("loc_1434")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1486")
    OP_8D(0xFE, 48000, 49000, 50500, 48000, 3000)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1483")
    TurnDirection(0xFE, 0xF, 400)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1483")

    Jump("loc_1434")

    label("loc_1486")

    Return()

    # Function_4_13A6 end

    def Function_5_1487(): pass

    label("Function_5_1487")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14AA")
    OP_8D(0xFE, 25948, 43568, 37838, 41060, 3000)
    Jump("Function_5_1487")

    label("loc_14AA")

    Return()

    # Function_5_1487 end

    def Function_6_14AB(): pass

    label("Function_6_14AB")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17F2")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17BB")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1630")
    Sleep(250)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1630")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1630")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1630")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1630")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1630")
    Sleep(500)

    label("loc_1630")

    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_166B")

    def lambda_164F():

        label("loc_164F")

        OP_97(0xFE, 0xD6D8, 0xB824, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_164F")

    QueueWorkItem2(0xFE, 1, lambda_164F)
    Jump("loc_168A")

    label("loc_166B")


    def lambda_1671():

        label("loc_1671")

        OP_97(0xFE, 0xD6D8, 0xB824, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1671")

    QueueWorkItem2(0xFE, 1, lambda_1671)

    label("loc_168A")

    SetChrChipByIndex(0xFE, 11)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_1699")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16D1")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C9")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_16D1")

    label("loc_16C9")

    Sleep(15)
    Jump("loc_1699")

    label("loc_16D1")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 55000, 0, 47140, 74)

    label("loc_16F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17B8")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B0")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 12)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    Jump("loc_17B8")

    label("loc_17B0")

    Sleep(500)
    Jump("loc_16F0")

    label("loc_17B8")

    Jump("loc_17EF")

    label("loc_17BB")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EF")

    def lambda_17D7():
        OP_8D(0xFE, 51380, 38050, 58760, 43900, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17D7)

    label("loc_17EF")

    Jump("loc_14DF")

    label("loc_17F2")

    Return()

    # Function_6_14AB end

    def Function_7_17F3(): pass

    label("Function_7_17F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1933")
    OP_8E(0xFE, 0xE132, 0x0, 0x114D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBD7E, 0x0, 0x114D6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xBD7E, 0x0, 0xA10E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFA8C, 0x0, 0xA10E, 0x7D0, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFA8C, 0x0, 0x48EE, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFA8C, 0x0, 0x38EA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC60C, 0x0, 0x38EA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xC60C, 0x0, 0xA10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE6B4, 0x0, 0xA10E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE6B4, 0x0, 0xCAF8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE132, 0x0, 0xCAF8, 0x7D0, 0x0)
    Jump("Function_7_17F3")

    label("loc_1933")

    Return()

    # Function_7_17F3 end

    def Function_8_1934(): pass

    label("Function_8_1934")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A38")
    OP_8E(0xFE, 0x9FCE, 0x0, 0x3872, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7620, 0x0, 0x3872, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7620, 0x0, 0x9C5E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x9C5E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x1098C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6E6E, 0x0, 0x1098C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x1098C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xB964, 0x0, 0x3872, 0x7D0, 0x0)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Jump("Function_8_1934")

    label("loc_1A38")

    Return()

    # Function_8_1934 end

    def Function_9_1A39(): pass

    label("Function_9_1A39")

    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A70")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A93")
    OP_8D(0xFE, 43070, 48140, 44730, 52710, 3000)
    Jump("loc_1A70")

    label("loc_1A93")

    Return()

    # Function_9_1A39 end

    def Function_10_1A94(): pass

    label("Function_10_1A94")

    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1C32")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B09")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1C32")

    label("loc_1B09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B22")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1C32")

    label("loc_1B22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1C32")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B54")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1C32")

    label("loc_1B54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1C32")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B86")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1C32")

    label("loc_1B86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1C32")

    label("loc_1B9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1C32")

    label("loc_1BB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1C32")

    label("loc_1BD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEA")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1C32")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C03")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1C32")

    label("loc_1C03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1C32")

    label("loc_1C1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C32")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1C32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C47")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1C32")

    label("loc_1C47")

    Return()

    # Function_10_1A94 end

    def Function_11_1C48(): pass

    label("Function_11_1C48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CB3")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA0")
    Sleep(100)
    OP_4B(0xFE, 0)
    Jump("loc_1CAB")

    label("loc_1CA0")

    OP_4A(0xFE, 0)
    TurnDirection(0xFE, 0xF, 400)

    label("loc_1CAB")

    Sleep(100)
    Jump("Function_11_1C48")

    label("loc_1CB3")

    Return()

    # Function_11_1C48 end

    def Function_12_1CB4(): pass

    label("Function_12_1CB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CCC")
    TurnDirection(0xFE, 0xE, 0)
    Sleep(100)
    Jump("Function_12_1CB4")

    label("loc_1CCC")

    Return()

    # Function_12_1CB4 end

    def Function_13_1CCD(): pass

    label("Function_13_1CCD")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        "*chirp...*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_13_1CCD end

    def Function_14_1D0F(): pass

    label("Function_14_1D0F")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #1
        0xFE,
        "*chirp chiiiirp!*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_14_1D0F end

    def Function_15_1D58(): pass

    label("Function_15_1D58")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #2
        0xFE,
        "*chirp chirp chirp*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_15_1D58 end

    def Function_16_1DA3(): pass

    label("Function_16_1DA3")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #3
        0xFE,
        "*chirp chiiirp chirp!*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_16_1DA3 end

    def Function_17_1DF1(): pass

    label("Function_17_1DF1")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #4
        0xFE,
        "*chirp?*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_17_1DF1 end

    def Function_18_1E31(): pass

    label("Function_18_1E31")

    TalkBegin(0xE)
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_211D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E51")
    OP_A2(0x14)
    Call(0, 77)
    Jump("loc_211A")

    label("loc_1E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_20BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_1F36")

    ChrTalk(    #5
        0xE,
        (
            "Pat's mom is so mean!\x02\x03",

            "She totally dragged me by the ear to\x01",
            "the church!\x02\x03",

            "That was the first time I ever saw a\x01",
            "wedding, but it was so boring.\x02\x03",

            "I'm not ever gonna have one of those,\x01",
            "even when I grow up!\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x16)
    OP_A2(0x15)
    Jump("loc_20BA")

    label("loc_1F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2059")

    ChrTalk(    #6
        0xE,
        (
            "Man, Pat's mom is SO mean!\x02\x03",

            "I was just playing here, and she came and\x01",
            "dragged me to church.\x02\x03",

            "And then she said I had to sit still\x01",
            "and be quiet for, like, ever! And ever!\x02\x03",

            "What is it with adults and doing boring\x01",
            "stuff?\x02\x03",

            "I'm never gonna have a wedding, even\x01",
            "when I grow up!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_20BA")

    label("loc_2059")


    ChrTalk(    #7
        0xE,
        (
            "Why do I gotta go to a wedding?\x01",
            "It's got nothing to do with me!\x02\x03",

            "Man, Pat's mom is SO mean!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BA")

    Jump("loc_211A")

    label("loc_20BD")


    ChrTalk(    #8
        0xE,
        (
            "Yeah, we know, the roads are dangerous.\x02\x03",

            "It's lame, but we'll stay in the town\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211A")

    Jump("loc_2BC5")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_27DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 0)), scpexpr(EXPR_END)), "loc_2213")
    TurnDirection(0xE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(    #9
        0xE,
        (
            "Estelle! We're totally having our duel\x01",
            "next time!\x02\x03",

            "You better not forget!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_218B")


    ChrTalk(    #10
        0xE,
        (
            "Just you watch! I'm gonna train with my\x01",
            "sword and become a bracer!\x02\x03",

            "I'll be better than YOU as soon as I get\x01",
            "my badge, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2210")

    Jump("loc_27D8")

    label("loc_2213")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #11
        0xE,
        "Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1000FHeya, Luke!\x02\x03",

            "#1025FThank Aidios... You're all better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xE,
        (
            "Heheh! Nothin' wrong with me now!\x02\x03",

            "I was kinda sad when I woke up, though.\x02\x03",

            "I was having this TOTALLY sweet dream\x01",
            "the whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1015FWere you, now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xE,
        (
            "Yeah, a dream where I was the best bracer\x01",
            "ever and went all over doing awesome stuff!\x02\x03",

            "Heheh! I was so awesome, you didn't even\x01",
            "compare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1016FHahaha, ahh, the dreams of children.\x02\x03",

            "Well, do your best to make it happen, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xE,
        (
            "Just you wait! I'll be better than you the\x01",
            "instant I get my badge!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_2744")

    ChrTalk(    #18
        0xE,
        "Oh, yeah, Estelle! What about our duel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1007FOh, boy. You're still on about that, huh?\x02\x03",

            "Yeah, I did promise...but you're REALLY\x01",
            "sure you want to duel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xE,
        (
            "Err...actually, I was gonna say...not today.\x02\x03",

            "I mean, I totally caused you a ton of\x01",
            "trouble with everything, so...\x02\x03",

            "So! I'm totally gonna spare you the\x01",
            "humiliation of losing today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1019FYeah, sure, humiliation is my biggest\x01",
            "worry here.\x02\x03",

            "#1006FBut yeah... I understand. We'll have our\x01",
            "'reckoning' another time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xE,
        (
            "Yeah, you better be ready!\x02\x03",

            "Luke the Amazing's awesome swordsmanship\x01",
            "is gonna send you packing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1006FOhhhh? You better make sure you practice,\x01",
            "then.\x02\x03",

            "Otherwise Luke the Amazing's going home\x01",
            "on a stretcher again! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        "Heheh! Same to you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D5")

    label("loc_2744")


    ChrTalk(    #25
        0x101,
        (
            "#1006FOhhhh? You better make sure you practice,\x01",
            "then.\x02\x03",

            "The road to being a bracer isn't easy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xE,
        (
            "Haha! I'll do better than YOU,\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D5")

    OP_A2(0x1A68)

    label("loc_27D8")

    Jump("loc_2BC5")

    label("loc_27DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2858")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_2851")
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(    #27
        0xE,
        (
            "I gotta get home while it's still light out.\x02\x03",

            "Don't forget about our duel!\x01",
            "You promised!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2855")

    label("loc_2851")

    Call(0, 20)

    label("loc_2855")

    Jump("loc_2BC5")

    label("loc_2858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 0)), scpexpr(EXPR_END)), "loc_28BA")

    ChrTalk(    #28
        0xE,
        "Estelle...where's...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#501FSay what, Luke?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #30
        0xE,
        "Nah... Nothin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BC5")

    label("loc_28BA")

    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x101, 400)
    Sleep(600)
    OP_63(0xE)

    ChrTalk(    #31
        0xE,
        "WHOA!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        "ESTELLE!! Estelle's back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#000FHey, Luke! You sound like you're doing okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xE,
        "Heheh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        "Heheheheheheheheh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        (
            "Meeting me here shall be your end.\x01",
            "Now, I shall show you the results of my\x01",
            "DAYS of training!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "ESTELLE BRIGHT!\x01",
            "It is time for...THE RECKONING!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#505FTime for the... What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        "Our DUEL, duuuuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        (
            "Just gonna tell you now, I'm the bestest\x01",
            "fighter in all of Rolent now!\x01",
            "So c'mon! Let's DUEL!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#000FOh... Uh, yeah, we'll do that later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xE,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        "What the crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xE,
        (
            "What kinda bracer backs down from\x01",
            "a totally awesome challenge like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xE,
        (
            "H-Hey...are you okay, Estelle?\x01",
            "You seem kinda... I dunno...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#001FWhat, no, I'm the same as always!\x01",
            "I just need to go do something.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1028)

    label("loc_2BC5")

    OP_4B(0xFE, 255)
    TalkEnd(0xE)
    Return()

    # Function_18_1E31 end

    def Function_19_2BCD(): pass

    label("Function_19_2BCD")

    TalkBegin(0xF)
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BED")
    OP_A3(0x14)
    Call(0, 77)
    Jump("loc_2D6E")

    label("loc_2BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_2CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7C")

    ChrTalk(    #47
        0xF,
        (
            "I went to the wedding a little bit ago.\x02\x03",

            "And, um, Mom made Luke come along\x01",
            "with us, too.\x02\x03",

            "I kinda feel bad for Luke.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2CD3")

    label("loc_2C7C")


    ChrTalk(    #48
        0xF,
        (
            "Mom kinda-sorta forced Luke to come to\x01",
            "the wedding.\x02\x03",

            "I kinda feel bad for Luke...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD3")

    Jump("loc_2D6E")

    label("loc_2CD6")


    ChrTalk(    #49
        0xF,
        (
            "I wish I could play with Luke for longer.\x02\x03",

            "But I've got something I need to do, so I gotta\x01",
            "head home soon.\x02\x03",

            "I don't wanna go to a wedding, either!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6E")

    Jump("loc_30C5")

    label("loc_2D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2DD4")

    ChrTalk(    #50
        0xF,
        (
            "Luke just keeps talking about his dream.\x02\x03",

            "It really sounds like he liked it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2DD4")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #51
        0xF,
        (
            "Estelle! Estelle! Luke's all better!\x02\x03",

            "He keeps talking about the dream he had\x01",
            "while he was asleep, though.\x02\x03",

            "It really sounds like he liked it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2E72")

    Jump("loc_30C5")

    label("loc_2E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2F0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_2F07")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #52
        0xF,
        (
            "We'll go home while it's still light out,\x01",
            "like you said, Estelle.\x02\x03",

            "I'll make sure Luke goes with me,\x01",
            "so don't worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0B")

    label("loc_2F07")

    Call(0, 20)

    label("loc_2F0B")

    Jump("loc_30C5")

    label("loc_2F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_30C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 1)), scpexpr(EXPR_END)), "loc_2FBE")

    ChrTalk(    #53
        0xF,
        (
            "Luke heard about what you guys did\x01",
            "and has really started practicing with\x01",
            "his sword.\x02\x03",

            "He keeps saying he'll absolutely become\x01",
            "stronger than you, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C5")

    label("loc_2FBE")


    ChrTalk(    #54
        0xF,
        "Estelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "You're back, you're back!\x01",
            "Welcome back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#000FHi, Pat! Yeah... I'm back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        (
            "Luke heard about what you guys did\x01",
            "and has really started practicing with\x01",
            "his sword.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xF,
        (
            "He keeps saying he'll absolutely become\x01",
            "stronger than you, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1029)

    label("loc_30C5")

    OP_4B(0xFE, 255)
    TalkEnd(0xF)
    Return()

    # Function_19_2BCD end

    def Function_20_30CD(): pass

    label("Function_20_30CD")

    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xE)"), scpexpr(EXPR_END)), "loc_312C")
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xE)

    ChrTalk(    #59
        0xE,
        "Wha?! Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #60
        0xF,
        "Estelle! Hi!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3181")

    label("loc_312C")

    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xF)

    ChrTalk(    #61
        0xF,
        "Huh? Oh, Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #62
        0xE,
        "Whoa, you're back!\x02",
    )

    CloseMessageWindow()

    label("loc_3181")


    ChrTalk(    #63
        0x101,
        (
            "#1001FHaha! Volume, guys!\x01",
            "I can hear you just fine without the yelling.\x02\x03",

            "#1028FSoooo, looks like you BOTH really missed me,\x01",
            "hmmmmm, Luke?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xE,
        (
            "N-No, I wasn't waiting for you.\x02\x03",

            "You just surprised me by showing up\x01",
            "like this, is all!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #65
        0xF,
        (
            "Huh...?\x02\x03",

            "Luke, you just told me the other day you\x01",
            "couldn't wait for Estelle to--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_63(0xE)

    ChrTalk(    #66
        0xE,
        "SH-SHUT UP, you dummy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1012FHaha... Aww, Luke, you're adorable. ♪\x02\x03",

            "#1018FC'mon, now, give ol' big sis Estelle a hug!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3372():
        TurnDirection(0xE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3372)
    Sleep(150)
    TurnDirection(0xF, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 0)), scpexpr(EXPR_END)), "loc_3411")

    ChrTalk(    #68
        0xE,
        (
            "Guaaaah, don't say it like THAT!\x01",
            "That sounds weird!\x02\x03",

            "Besides! Don't tell me you forgot!\x02\x03",

            "Our duel! C'mon, Estelle! Duel me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D1")

    label("loc_3411")


    ChrTalk(    #69
        0xE,
        (
            "Guaaaah, don't say it like THAT!\x01",
            "That sounds weird!\x02\x03",

            "Besides! There's something way more\x01",
            "important!\x02\x03",

            "We need to have a duel! Right now!\x01",
            "C'mon, Estelle, don't you dare get scared\x01",
            "and run!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D1")


    ChrTalk(    #70
        0x101,
        (
            "#1007FWha... A duel? Are you for real, kiddo?\x02\x03",

            "Look at this fog. You guys need\x01",
            "to scoot on home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xE,
        (
            "You dummy, this fog's why I want\x01",
            "to duel now!\x02\x03",

            "It'd be a CLIMACTIC DUEL in THE FOG!\x01",
            "Isn't that just the coolest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1009FAnd that's how I know you're both\x01",
            "still kids.\x02\x03",

            "There is absolutely NOTHING 'cool' about\x01",
            "making the people you love worry.\x02\x03",

            "Have you forgotten what happened at the\x01",
            "Esmelas Tower? How worried everyone was?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #73
        0xE,
        "Guh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xF,
        "Umm, um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1010FIf you want to be a 'big man,' first you\x01",
            "make sure you aren't going to cause\x01",
            "anyone to worry by being out.\x02\x03",

            "If you can't look after yourself, you\x01",
            "definitely can't hope to help anyone else.\x02\x03",

            "#1002FI think you're old enough to get what\x01",
            "I mean, right?\x02\x03",

            "Show me you've grown up a little bit,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "Tch...\x02\x03",

            "F-Fine, I get it.\x01",
            "We'll duel later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xF,
        (
            "Sorry, Estelle.\x02\x03",

            "We'll go home before it gets too dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1006FPlease do, Pat.\x01",
            "It's a promise between friends, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xF,
        "Uh-huh! Okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        "Whatever, just don't forget our duel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1007FOf course, of course.\x02\x03",

            "We'll have our big, final showdown\x01",
            "once the fog's cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        "Yeah! It's a promise!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_A2(0x1883)
    Return()

    # Function_20_30CD end

    def Function_21_3962(): pass

    label("Function_21_3962")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_3B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A1D")

    ChrTalk(    #83
        0xFE,
        (
            "I took Ellie with me to Grancel for the\x01",
            "Queen's Birthday Celebration last month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "We ended up stuck in the middle of\x01",
            "Alan Richard's coup! Some date that was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3F")

    label("loc_3A1D")


    ChrTalk(    #85
        0xFE,
        (
            "I took Ellie with me to Grancel for the\x01",
            "Queen's Birthday Celebration last month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "We ended up stuck in the middle of\x01",
            "Alan Richard's coup! Some date that was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I was actually gonna try to propose,\x01",
            "but then the Royal Guard came out of\x01",
            "nowhere and started storming the castle!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3B3F")

    TalkEnd(0x13)
    Return()

    # Function_21_3962 end

    def Function_22_3B43(): pass

    label("Function_22_3B43")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_3BD2")

    ChrTalk(    #88
        0xFE,
        "The trip up to Grancel with Armand was nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "But it's even nicer just being here,\x01",
            "spending a quiet, peaceful day with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD2")

    TalkEnd(0x12)
    Return()

    # Function_22_3B43 end

    def Function_23_3BD6(): pass

    label("Function_23_3BD6")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB6")

    ChrTalk(    #90
        0xFE,
        (
            "The freight liners may be down, but I need\x01",
            "to get the outgoing cargo ready anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "It needs to be ready to ship, and besides,\x01",
            "I need to get to church!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "It's Armand's wedding, after all!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_3D1C")

    label("loc_3CB6")


    ChrTalk(    #93
        0xFE,
        (
            "Gotta get done with work so I can get over\x01",
            "to the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "It's Armand's wedding, after all!\x02",
    )

    CloseMessageWindow()

    label("loc_3D1C")

    Jump("loc_459E")

    label("loc_3D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_42F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 2)), scpexpr(EXPR_END)), "loc_3EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E0F")

    ChrTalk(    #95
        0xFE,
        (
            "Really glad that fog cleared.\x01",
            "That stuff was ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Anyhow! We're going to be working through\x01",
            "a ton of back-orders on our lumber!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I really am gonna need to put my nose to\x01",
            "the grindstone at work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFC")

    label("loc_3E0F")


    ChrTalk(    #98
        0xFE,
        (
            "I need to take a lesson from Radford and\x01",
            "really put my back into our work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "The freight liners are coming in again\x01",
            "now that the fog's gone, and so we're\x01",
            "going through back-orders on our lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "Anyway, you guys be careful!\x02",
    )

    CloseMessageWindow()

    label("loc_3EFC")

    Jump("loc_42F3")

    label("loc_3EFF")


    ChrTalk(    #101
        0xFE,
        "Hey, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "Thanks to you guys, my father-in-law's awake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1015FFather-in-law?\x02\x03",

            "#1011FOhh, you mean Radford, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        (
            "#020FJust as Aina said, it seems everyone's\x01",
            "awake.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #105
        0xFE,
        (
            "Yeah, Radford took a bit longer to wake up,\x01",
            "but he seems just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "He said we need to get to work, and he's\x01",
            "still got enough energy to outpace me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1001FHaha! Sounds like he's fine, all right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40B8")

    ChrTalk(    #108
        0x105,
        "#048FReally?\x02",
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_40B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E1")

    ChrTalk(    #109
        0x107,
        "#061FHeehee! Yeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_40E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_410D")

    ChrTalk(    #110
        0x106,
        "#051FThat's a relief.\x02",
    )

    CloseMessageWindow()
    Jump("loc_413A")

    label("loc_410D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413A")

    ChrTalk(    #111
        0x108,
        "#070FYes, quite a relief!\x02",
    )

    CloseMessageWindow()

    label("loc_413A")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #112
        0xFE,
        (
            "Seriously. I shouldn't worry about him,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Anyway, guess I'd better learn from his\x01",
            "example and put my back into it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "The freight liners are coming in again\x01",
            "now that the fog's gone, and so we're\x01",
            "going through back-orders on our lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1006FGood luck with that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        (
            "#525FTry not to let your own father-in-law\x01",
            "leave you in the dust, Freemont.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #117
        0xFE,
        "I'll do my best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "You guys be careful, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A62)
    OP_A2(0x1)

    label("loc_42F3")

    Jump("loc_459E")

    label("loc_42F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4389")

    ChrTalk(    #119
        0xFE,
        "This fog is ridiculous. It came out of nowhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "I need to be careful not to get lost when\x01",
            "I go gathering in the forest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4434")

    label("loc_4389")


    ChrTalk(    #121
        0xFE,
        "This fog is ridiculous. It came out of nowhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Well, I guess nature is prone to whimsy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Handling that is part of the job for us\x01",
            "in the timber industry.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4434")

    Jump("loc_459E")

    label("loc_4437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_459E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44B9")

    ChrTalk(    #124
        0xFE,
        (
            "Once we're done cutting, we'll be\x01",
            "replanting until the evening, won't we...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "Gonna be a busy day today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_44B9")


    ChrTalk(    #126
        0xFE,
        (
            "I'm about to head off to cut some lumber\x01",
            "in Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Wood's one of the only resources we can\x01",
            "grow back after we use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "To tend the forest like a garden and\x01",
            "grow with it--that's what it means to\x01",
            "be a woodsman!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_459E")

    TalkEnd(0x11)
    Return()

    # Function_23_3BD6 end

    def Function_24_45A2(): pass

    label("Function_24_45A2")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_4AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493E")
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #129
        0xFE,
        "Oooh, Estelle, Joshua!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4762")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4669")
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #130
        0xFE,
        "Aaah! Schera, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        "#021FHello there, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        "#1040FHave you been well?\x02",
    )

    CloseMessageWindow()
    Jump("loc_46C4")

    label("loc_4669")


    ChrTalk(    #133
        0x101,
        "#1001FHi, Claire!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        (
            "#1040FI haven't seen you in quite a while.\x01",
            "Have you been well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C4")

    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #135
        0xFE,
        (
            "I'm always well!\x01",
            "Reporters have to be healthy to chase\x01",
            "the big scoops, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "And it sounds like you're already hard\x01",
            "at work, Estelle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_478C")

    label("loc_4762")


    ChrTalk(    #137
        0xFE,
        "I heard you're already hard at work!\x02",
    )

    CloseMessageWindow()

    label("loc_478C")


    ChrTalk(    #138
        0xFE,
        "You saved everyone over at the mine, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1008FYou really don't miss a beat, do you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#1044FIf anything, you're hearing about things\x01",
            "even faster now. I'm impressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "You only just got back and you're already\x01",
            "doing great things! That's the Estelle\x01",
            "and Joshua I know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "If you keep this up, I bet you'll figure\x01",
            "out what the floating island is in no\x01",
            "time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "Remember to give me the scoop when you do!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x13)
    OP_A2(0x20A6)
    Jump("loc_4AD6")

    label("loc_493E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A53")

    ChrTalk(    #144
        0xFE,
        (
            "Bleeech...\x01",
            "There's nothing really neato happening\x01",
            "at Armand's wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "But! Even the boring news is needed to put a\x01",
            "paper together! The Liberl News taught me that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Yeah, when you think about it like that,\x01",
            "Armand's wedding is a perfect page-filler!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_4AD6")

    label("loc_4A53")


    ChrTalk(    #147
        0xFE,
        (
            "There's nothing really neato happening\x01",
            "at Armand's wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "But! Even the boring news is needed to\x01",
            "put a paper together!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD6")

    Jump("loc_5C76")

    label("loc_4AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_50AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC6")
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #149
        0xFE,
        "Oooh, Estelle, Joshua!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B95")
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #150
        0xFE,
        "Aaah, Schera, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x103,
        "#021FHello there, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x102,
        "#1040FHave you been well?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF0")

    label("loc_4B95")


    ChrTalk(    #153
        0x101,
        "#1001FHi, Claire!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        (
            "#1040FI haven't seen you in quite a while.\x01",
            "Have you been well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF0")

    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #155
        0xFE,
        (
            "I'm always well!\x01",
            "Reporters have to be healthy to chase\x01",
            "the big scoops, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CF7")

    ChrTalk(    #156
        0xFE,
        (
            "But why are three awesome, famous bracer\x01",
            "stars here in Rolent now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Ohhh, I know!\x01",
            "You're investigating the Orbal Shutdown\x01",
            "Phenomenon, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8E")

    label("loc_4CF7")


    ChrTalk(    #158
        0xFE,
        (
            "But why are two awesome, famous bracer\x01",
            "stars here in Rolent now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Ohhh, I know!\x01",
            "You're investigating the Orbal Shutdown\x01",
            "Phenomenon, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8E")


    ChrTalk(    #160
        0x101,
        "#1007FWelp, she's as sharp as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x102,
        "#1044FI'm impressed you know such a big phrase.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "Freddy's been talking about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "The floating island is really weird, but the\x01",
            "weirdest thing is what's happened to the\x01",
            "orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I'm gonna get the scoop of the\x01",
            "millennium on this! Just you wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    OP_A2(0x20A5)
    Jump("loc_50A7")

    label("loc_4EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5009")

    ChrTalk(    #165
        0xFE,
        (
            "The number one topic on everyone's mind\x01",
            "is the Orbal Shutdown Phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "But today, I've got an appointment to go\x01",
            "to Armand and Ellie's wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I managed to get an invite from a person\x01",
            "on the inside, so I'll be covering it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "Gotta lock down that local news, or the\x01",
            "readers lose interest!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_50A7")

    label("loc_5009")


    ChrTalk(    #169
        0xFE,
        (
            "Today, I've got an appointment to go\x01",
            "to Armand and Ellie's wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I managed to get an invite from a person\x01",
            "on the inside, so I'll be covering it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A7")

    Jump("loc_5C76")

    label("loc_50AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_5425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 1)), scpexpr(EXPR_END)), "loc_5160")

    ChrTalk(    #171
        0xFE,
        "So a new case now, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "The war hawks in the Empire, the Intelligence\x01",
            "Division... Maybe even the sky bandits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "Aww, I can't see where this is going...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5422")

    label("loc_5160")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #174
        0xFE,
        "Oh, Estelle, Schera, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "Are you leaving Rolent?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x103,
        (
            "#020FYes, we'll be packing the wagons\x01",
            "shortly, here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1007FI'm sorry, Claire. We've got work to do\x01",
            "elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "You two are going together...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "That means there's a case!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "Is it a plot of the, um, Empire's war hawks\x01",
            "using the treaty as cover? Or the remnants of\x01",
            "the Intelligence Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "No, maybe it's the Capua sky bandits!\x01",
            "That'd surprise everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "Aww, I can't see where this is going...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #183
        0x101,
        (
            "#1019F(Huh, I'm not entirely sure what to think about\x01",
            "her being that close to the actual mark.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x103,
        (
            "#021F(I think a certain Mr. Burns should\x01",
            "fear for his job when she gets older.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A61)

    label("loc_5422")

    Jump("loc_5C76")

    label("loc_5425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_596F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 1)), scpexpr(EXPR_END)), "loc_568D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_54C2")

    ChrTalk(    #185
        0xFE,
        (
            "With Mr. Cassius gone, things have been\x01",
            "so boring lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "Things aren't very exciting when it's just Ridge\x01",
            "hanging around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_568A")

    label("loc_54C2")

    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_552E")

    ChrTalk(    #187
        0xFE,
        "Anyway...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I bet you two were on a passenger ship\x01",
            "and got stuck here, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_558F")

    label("loc_552E")


    ChrTalk(    #189
        0xFE,
        "Ah, Estelle, Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "I bet you two were on a passenger ship\x01",
            "and got stuck here, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_558F")


    ChrTalk(    #191
        0x101,
        (
            "#1015FYeah, actually...\x02\x03",

            "#1007FYou've always been so good at figuring\x01",
            "out what's going on, Claire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "There hasn't been much to figure out\x01",
            "with Mr. Cassius gone for so long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "Well, good luck, you two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "I expect the biggest scoops!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_568A")

    Jump("loc_596C")

    label("loc_568D")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #195
        0xFE,
        "Ahh! Estelle! Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1018FHiya, Claire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x103,
        "#021FHave you been a good girl?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #198
        0xFE,
        "Ehe! I'm ALWAYS a good girl!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #199
        0xFE,
        "Oh, yeah, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "I heard Joshua's working on his own now,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "My killer reporting instincts are telling\x01",
            "me that's misinformation! Isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "He's really fighting some evil organization\x01",
            "all on his own and you're trying to find\x01",
            "him, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #203
        0x101,
        (
            "#1019F(Uh. Killer instinct, nothing.\x01",
            "How does she DO that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "Yeah, that's how this story should go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "After all, a normal story just wouldn't\x01",
            "fit Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "Joshua secretly infiltrating an evil\x01",
            "organization's base all on his own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Aaaah, he's so cool!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x1899)

    label("loc_596C")

    Jump("loc_5C76")

    label("loc_596F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_5C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 2)), scpexpr(EXPR_END)), "loc_5A21")

    ChrTalk(    #208
        0xFE,
        "Estelle, where's Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Or is that really your new man, and you\x01",
            "ALREADY threw Joshua to the lions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#000F. . .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x142,
        "#1064F(Er, missy! Ix-naaaay!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C76")

    label("loc_5A21")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #212
        0xFE,
        "Aaaah! It's Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#000FHi, Claire. Sorry I haven't seen\x01",
            "you in a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x142, 400)
    Sleep(600)

    ChrTalk(    #214
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "HEY! Who're YOU?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x142,
        "#1064FUh, who, me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "Wait! Could it be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "...Is he a mystery man, here to tear\x01",
            "Estelle and Joshua apart?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "You aren't allowed to have an exciting\x01",
            "love triangle where I can't cover it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#506FUhhhhhh. Claire?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "Oh, I know, I'm sure he'll fight Joshua\x01",
            "TO THE DEATH! But the flames of friendship\x01",
            "will ignite as Mr. Green-Hair breathes his last...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x142,
        (
            "#1061FO-kaaay, the, uh, kids around here\x01",
            "are somethin' else...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x102A)

    label("loc_5C76")

    TalkEnd(0x10)
    Return()

    # Function_24_45A2 end

    def Function_25_5C7A(): pass

    label("Function_25_5C7A")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_5E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5D0F")

    ChrTalk(    #223
        0xFE,
        (
            "So this is the famous Rolent Clock Tower,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "This is another landmark of the Hundred\x01",
            "Days War with a lot of history.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E59")

    label("loc_5D0F")


    ChrTalk(    #225
        0xFE,
        (
            "So this is the famous Rolent Clock Tower,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "It gets overlooked by a lot of people, but\x01",
            "this is another landmark of the Hundred\x01",
            "Days War with a lot of history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "When Rolent was surrounded, an Imperial\x01",
            "Army tank shell hit it dead on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "And now the tower serves as a memorial to\x01",
            "the people who died from that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_5E59")

    TalkEnd(0x14)
    Return()

    # Function_25_5C7A end

    def Function_26_5E5D(): pass

    label("Function_26_5E5D")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_6072")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5F13")

    ChrTalk(    #229
        0xFE,
        (
            "The mist finally cleared up, so now I can\x01",
            "go hog wild on photographing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "Think I'll start with the Clock Tower.\x01",
            "It's kind of Rolent's symbol, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6072")

    label("loc_5F13")


    ChrTalk(    #231
        0xFE,
        (
            "The mist finally cleared up, so now I can\x01",
            "go hog wild on photographing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "Think I'll start with the Clock Tower.\x01",
            "It's kind of Rolent's symbol, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "Gotta admit, though, knowing its history\x01",
            "makes it hard to just snap the shutter\x01",
            "like a fiend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "Feels like you've got to get the proper\x01",
            "respect for the history into every frame.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_6072")

    TalkEnd(0x15)
    Return()

    # Function_26_5E5D end

    def Function_27_6076(): pass

    label("Function_27_6076")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_64EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 0)), scpexpr(EXPR_END)), "loc_6140")

    ChrTalk(    #235
        0xFE,
        (
            "Soon as the rest of my clients are here, we're\x01",
            "off for the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Like Schera said, it's getting hard\x01",
            "to see, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "I'll keep my guard up as I go, don't worry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_64EB")

    label("loc_6140")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x103, 0)
    Sleep(400)

    ChrTalk(    #238
        0xFE,
        "Ah, Estelle and Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x103,
        "#020FAh, hello, Ridge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        "#1001FHeya, Ridge.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #241
        0xFE,
        (
            "Hey, Estelle. Think we last saw each other\x01",
            "when you went off to train, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "I heard from Aina. Already on the job, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x101,
        (
            "#1015FYeah, pretty much.\x02\x03",

            "You make it sound like you're already\x01",
            "tied up, Ridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Yeah, I've got some clients who really\x01",
            "need to get to Grancel on urgent business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "Since it doesn't look like the passenger\x01",
            "ships are going anywhere soon, I'll be\x01",
            "escorting them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        "#1011FGoing back the way we just came, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x103,
        (
            "#026FVisibility on the roads is just as bad.\x02\x03",

            "#027FYou'll need to pay plenty of attention\x01",
            "as you go.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #248
        0xFE,
        "Yeah, don't worry, I'll be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Anyhow, good luck with your mission,\x01",
            "you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        (
            "#1006FYou too, Ridge.\x01",
            "Good luck with that escort job!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #251
        0xFE,
        "Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "I'll make sure they get there to become\x01",
            "repeat customers, don't you worry!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1880)

    label("loc_64EB")

    TalkEnd(0x16)
    Return()

    # Function_27_6076 end

    def Function_28_64EF(): pass

    label("Function_28_64EF")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_6589")

    ChrTalk(    #253
        0xFE,
        (
            "I've urgent business in the capital.\x01",
            "I absolutely must get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "This is my chance to get a big contract.\x01",
            "I can't let it slip by me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6589")

    TalkEnd(0x17)
    Return()

    # Function_28_64EF end

    def Function_29_658D(): pass

    label("Function_29_658D")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_6614")

    ChrTalk(    #255
        0xFE,
        (
            "It's nice to have bracers at a time like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I don't even want to think about walking\x01",
            "out in that fog on my own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6614")

    TalkEnd(0x18)
    Return()

    # Function_29_658D end

    def Function_30_6618(): pass

    label("Function_30_6618")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_66A2")

    ChrTalk(    #257
        0xFE,
        (
            "Never thought passenger ships would just\x01",
            "stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "Well, with a bracer along, nothing to fear\x01",
            "from a little walking tour.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A2")

    TalkEnd(0x19)
    Return()

    # Function_30_6618 end

    def Function_31_66A6(): pass

    label("Function_31_66A6")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_685C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_677A")

    ChrTalk(    #259
        0xFE,
        "I slipped out for a bit to go see Luke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "He's still unconscious, but he had a\x01",
            "very calm expression on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "Right now, I have to focus on completing\x01",
            "my duties, for his sake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6859")

    label("loc_677A")


    ChrTalk(    #262
        0xFE,
        (
            "No problems at the moment.\x01",
            "Our patrols are going normally for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "However, without anything changing,\x01",
            "the enemy could strike at us again at a\x01",
            "moment's notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "None of us can afford to let our\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_6859")

    Jump("loc_68F3")

    label("loc_685C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_68F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 0)), scpexpr(EXPR_END)), "loc_68EF")

    ChrTalk(    #265
        0xFE,
        (
            "We started patrolling as soon as\x01",
            "we arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "Leave the safety of the city to us.\x01",
            "You take care of the guild's missions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68F3")

    label("loc_68EF")

    Call(0, 33)

    label("loc_68F3")

    TalkEnd(0x28)
    Return()

    # Function_31_66A6 end

    def Function_32_68F7(): pass

    label("Function_32_68F7")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_6983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 0)), scpexpr(EXPR_END)), "loc_697F")

    ChrTalk(    #267
        0xFE,
        "We're going to start guard duty now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "I'm sure there'll be problems, but\x01",
            "we'll solve them as they come up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6983")

    label("loc_697F")

    Call(0, 33)

    label("loc_6983")

    TalkEnd(0x27)
    Return()

    # Function_32_68F7 end

    def Function_33_6987(): pass

    label("Function_33_6987")

    OP_4A(0x28, 255)
    OP_4A(0x27, 255)
    ClearChrFlags(0x28, 0x10)
    ClearChrFlags(0x27, 0x10)

    ChrTalk(    #269
        0x28,
        (
            "Officer Dyne. Did we get men posted to\x01",
            "the west gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x27,
        "Uh... yessir! I assigned two men there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x27,
        (
            "Given the situation, we should probably\x01",
            "think about assigning a few more, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x28,
        "Agreed... All right, give me periodic--\x02",
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x28)

    def lambda_6AA2():
        TurnDirection(0x28, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_6AA2)
    Sleep(150)
    TurnDirection(0x27, 0x101, 400)

    ChrTalk(    #273
        0x28,
        "Ah, Ms. Bright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x28,
        "We've already started duty, as you can see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x28,
        (
            "Leave the safety of the city to us.\x01",
            "You take care of the guild's missions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        "#1002FWill do. Keep it up, guys!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x27, 0)
    TurnDirection(0x27, 0x28, 0)
    OP_4B(0x28, 255)
    OP_4B(0x27, 255)
    OP_A2(0x18A0)
    Return()

    # Function_33_6987 end

    def Function_34_6B8C(): pass

    label("Function_34_6B8C")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_6CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6C34")

    ChrTalk(    #277
        0xFE,
        (
            "I can't relax for a second. I feel like the\x01",
            "citizens are watching us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "Well, granted, I dunno who can actually SEE\x01",
            "us in this junk, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CAC")

    label("loc_6C34")


    ChrTalk(    #279
        0xFE,
        (
            "I can't relax for a second. I feel like the\x01",
            "citizens are watching us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "I can't so much as yawn by accident!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_6CAC")

    Jump("loc_6D35")

    label("loc_6CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_6D35")

    ChrTalk(    #281
        0xFE,
        (
            "This is my first time being assigned\x01",
            "somewhere that isn't the Verte Bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "Maaan...whole different level of nerves.\x02",
    )

    CloseMessageWindow()

    label("loc_6D35")

    TalkEnd(0x1F)
    Return()

    # Function_34_6B8C end

    def Function_35_6D39(): pass

    label("Function_35_6D39")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_6EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6DD5")

    ChrTalk(    #283
        0xFE,
        (
            "Even if there are monsters or suspicious\x01",
            "persons out there, we won't know until\x01",
            "they get close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "Even us guards are on edge...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EA7")

    label("loc_6DD5")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #285
        0xFE,
        (
            "AH...!\x01",
            "O-Oh. It's you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "Sweet Aidios, don't sneak up on a guy\x01",
            "like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "Everyone's on edge, wondering if there\x01",
            "are any monsters or whatever out in the\x01",
            "fog.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_6EA7")

    Jump("loc_6FD1")

    label("loc_6EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_6FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6F2C")

    ChrTalk(    #288
        0xFE,
        (
            "We're already on patrol, even though we\x01",
            "just arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "C.W.O. Aston is even stricter than\x01",
            "normal today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FD1")

    label("loc_6F2C")


    ChrTalk(    #290
        0xFE,
        (
            "We're already on patrol, even though we\x01",
            "just arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "C.W.O. Aston is even stricter than\x01",
            "normal today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "Guess he's really serious about this\x01",
            "one...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_6FD1")

    TalkEnd(0x20)
    Return()

    # Function_35_6D39 end

    def Function_36_6FD5(): pass

    label("Function_36_6FD5")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_716B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_708B")

    ChrTalk(    #293
        0xFE,
        (
            "It's hard having a quiet type as your\x01",
            "partner on missions like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "Even if I work up the courage to try\x01",
            "and have a conversation, he barely\x01",
            "responds!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7168")

    label("loc_708B")


    ChrTalk(    #295
        0xFE,
        (
            "I don't really mind the quiet time\x01",
            "normally, but in this mess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "It's hard having a quiet type as your\x01",
            "partner on missions like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "It really tires you out, having to be\x01",
            "so quiet around him yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_7168")

    Jump("loc_72BC")

    label("loc_716B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_72BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7203")

    ChrTalk(    #298
        0xFE,
        (
            "Rolent feels like a whole different\x01",
            "world right now, compared to how it\x01",
            "usually is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "Just staring out at it gives me\x01",
            "a chill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72BC")

    label("loc_7203")


    ChrTalk(    #300
        0xFE,
        (
            "I've been to Rolent on leave days\x01",
            "before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "This town, right now? Feels like a whole\x01",
            "different world from the one I saw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "Just staring out at it gives me\x01",
            "a chill.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_72BC")

    TalkEnd(0x21)
    Return()

    # Function_36_6FD5 end

    def Function_37_72C0(): pass

    label("Function_37_72C0")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_72F7")

    ChrTalk(    #303
        0xFE,
        (
            "...\x01",
            "...\x01",
            "...Nothing to report.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_733D")

    label("loc_72F7")


    ChrTalk(    #304
        0xFE,
        (
            "...\x01",
            "...\x01",
            "...Nothing to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "...\x01",
            "...\x01",
            "...Need something?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_733D")

    Jump("loc_7382")

    label("loc_7340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_7382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_735A")

    ChrTalk(    #306
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7382")

    label("loc_735A")


    ChrTalk(    #307
        0xFE,
        ".  .  .\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "...Need something?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_7382")

    TalkEnd(0x22)
    Return()

    # Function_37_72C0 end

    def Function_38_7386(): pass

    label("Function_38_7386")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_74B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_741F")

    ChrTalk(    #309
        0xFE,
        (
            "I just wish I knew where Domingo's\x01",
            "confidence was coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "I just hope he doesn't lose it when\x01",
            "the stuff hits the fan!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74B3")

    label("loc_741F")


    ChrTalk(    #311
        0xFE,
        (
            "I just wish I knew where Domingo's\x01",
            "confidence was coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "I guess the Haken Gate guys are a\x01",
            "little bit different in general, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_74B3")

    Jump("loc_7652")

    label("loc_74B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_7652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_7561")

    ChrTalk(    #313
        0xFE,
        (
            "We've got a reserve unit holding down\x01",
            "the fort over at the Verte crossing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "They're border garrison, so there's\x01",
            "no question about their ability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7652")

    label("loc_7561")


    ChrTalk(    #315
        0xFE,
        (
            "We've got a reserve unit holding down\x01",
            "the fort over at the Verte crossing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "They might be reserves, but we're pretty\x01",
            "sure they're competent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "They're usually with the border garrison,\x01",
            "so their training should be up to snuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_7652")

    TalkEnd(0x23)
    Return()

    # Function_38_7386 end

    def Function_39_7656(): pass

    label("Function_39_7656")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_76AD")

    ChrTalk(    #318
        0xFE,
        "No problems to report!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        "So just chill out, dudes! Hahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7726")

    label("loc_76AD")


    ChrTalk(    #320
        0xFE,
        "No problems to report!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        "So just chill out, dudes! Hahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        (
            "I mean, I'm saying it,\x01",
            "so it's gotta be true.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_7726")

    Jump("loc_7819")

    label("loc_7729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_7819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_77A0")

    ChrTalk(    #323
        0xFE,
        (
            "I'm here, so this city's safety is as\x01",
            "good as guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "So just relax, all right? Hahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7819")

    label("loc_77A0")


    ChrTalk(    #325
        0xFE,
        (
            "Hey, you're the bracers we met on the\x01",
            "road, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "Well, you just relax.\x01",
            "This city's in good hands with me!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_7819")

    TalkEnd(0x24)
    Return()

    # Function_39_7656 end

    def Function_40_781D(): pass

    label("Function_40_781D")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_791F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_78AA")

    ChrTalk(    #327
        0xFE,
        "Anyway, we'll be on patrol till nightfall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "As long as we're out here,\x01",
            "I'm sure it'll help the citizenry relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_791C")

    label("loc_78AA")


    ChrTalk(    #329
        0xFE,
        "We haven't seen anything suspicious, yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        (
            "Well, not that we can see all that far\x01",
            "in this fog anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_791C")

    Jump("loc_79DB")

    label("loc_791F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_79DB")

    ChrTalk(    #331
        0xFE,
        (
            "We heard about it in the briefing,\x01",
            "but this fog really is strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "I memorized a map of the city in advance,\x01",
            "but I still feel like I could get lost before\x01",
            "I even know it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79DB")

    TalkEnd(0x25)
    Return()

    # Function_40_781D end

    def Function_41_79DF(): pass

    label("Function_41_79DF")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7A9B")

    ChrTalk(    #333
        0xFE,
        (
            "Hey, bracers.\x01",
            "Nothin' up over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "If there's anything off, I'd say it's those\x01",
            "pigeons eating away in the middle of this\x01",
            "soup like the world's just fine and dandy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B33")

    label("loc_7A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_7B33")

    ChrTalk(    #335
        0xFE,
        (
            "It's been a while since I've been on a\x01",
            "mission away from the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        (
            "Even with the creepy fog, it's kind of\x01",
            "a nice change of pace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B33")

    TalkEnd(0x26)
    Return()

    # Function_41_79DF end

    def Function_42_7B37(): pass

    label("Function_42_7B37")

    TalkBegin(0x29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_7C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7B7B")

    ChrTalk(    #337
        0xFE,
        "Welcome! Please, feel free to look around!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C2A")

    label("loc_7B7B")


    ChrTalk(    #338
        0xFE,
        "Welcome to Rinon General Goods!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        (
            "The fog may still be terrible, but we're\x01",
            "sticking it out to serve our customers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        "Please, take a look over anything you like.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_7C2A")

    TalkEnd(0x29)
    Return()

    # Function_42_7B37 end

    def Function_43_7C2E(): pass

    label("Function_43_7C2E")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_7D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D18")
    OP_4A(0x34, 255)

    ChrTalk(    #341
        0xFE,
        "Armand and Ellie were sooooooo lovely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "*siiiiiiiiiigh* I wish I could set up a wedding\x01",
            "like that for Aryll.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x34, 400)

    ChrTalk(    #343
        0xFE,
        (
            "Heeey, Aryllll!\x01",
            "You should talk to your man about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #344
        0x34,
        "Nya～o.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x34, 255)
    OP_A2(0x10)
    Jump("loc_7D8E")

    label("loc_7D18")


    ChrTalk(    #345
        0xFE,
        "Armand and Ellie were sooooooo lovely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "*siiiiiiiiiigh* I wish I could set up a wedding\x01",
            "like that for Aryll.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D8E")

    Jump("loc_8458")

    label("loc_7D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7E0D")

    ChrTalk(    #347
        0xFE,
        (
            "Come now, kittennnns!\x01",
            "Playtime's over, we need to get ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "We've got an important ceremony to\x01",
            "attend!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8458")

    label("loc_7E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_8393")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8093")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_7EE2")

    ChrTalk(    #349
        0xFE,
        (
            "Hmm...\x01",
            "I wonder what name would fit a kitten...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "Claudia...\x01",
            "You could shorten it to Claws for a\x01",
            "nice joke, I suppose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "Though I guess it'd be rude to the princess,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8090")

    label("loc_7EE2")


    ChrTalk(    #352
        0xFE,
        "Ooooh, my, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "Look, looook!\x01",
            "The kittens are all so fluffy and\x01",
            "happy and full of energy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x101,
        (
            "#1001FHaha. I'll say.\x02\x03",

            "#1011FOoh, decided on any names yet?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #355
        0xFE,
        "Umm, not yet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "I've thought of a few,\x01",
            "but I juuuuust can't decide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        (
            "*siiiigh* I hope I can decide before they\x01",
            "grow up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        (
            "#1019FUh. Yeah. Naming pets before they GROW UP\x01",
            "is generally good practice.\x01",
            "Y'know, just, little advice there.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x2000)

    label("loc_8090")

    Jump("loc_8390")

    label("loc_8093")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_8242")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_815F")

    ChrTalk(    #359
        0xFE,
        (
            "Hmm... I wonder what name would fit a\x01",
            "kitten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        (
            "Claudia...\x01",
            "You could shorten it to Claws for a\x01",
            "nice joke, I suppose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xFE,
        (
            "Though I guess it'd be rude to the princess,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_823F")

    label("loc_815F")


    ChrTalk(    #362
        0xFE,
        "Ooooh, my, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "Look, looook!\x01",
            "Aryll came back a mother!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #364
        0x101,
        (
            "#1004FWHAAAA?!\x02\x03",

            "Sh-She brought kittens back??\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #365
        0xFE,
        "That's riiight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        "So now I'm trying to name them all!\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x2000)

    label("loc_823F")

    Jump("loc_8390")

    label("loc_8242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_82AC")

    ChrTalk(    #367
        0xFE,
        (
            "I've got to hurry and give Aryll's babies\x01",
            "names!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        "Hmm... I wonder what'd be prettiest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8390")

    label("loc_82AC")


    ChrTalk(    #369
        0xFE,
        (
            "I've got to hurry and give Aryll's babies\x01",
            "names!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "Hmm... I wonder what'd be prettiest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "Claudia...\x01",
            "You could shorten it to Claws for a\x01",
            "nice joke, I suppose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "Though I guess it'd be rude to the princess,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_8390")

    Jump("loc_8458")

    label("loc_8393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_8458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_83CA")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #373
        0xFE,
        "Zzzzz.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_8458")

    label("loc_83CA")

    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #374
        0xFE,
        "Nnnn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        "Zzzz... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x101,
        (
            "#1019F(How in the name of heck can she\x01",
            "sleep like that in this situation?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    OP_A2(0x10)

    label("loc_8458")

    TalkEnd(0x33)
    Return()

    # Function_43_7C2E end

    def Function_44_845C(): pass

    label("Function_44_845C")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_847B")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #377
        0xFE,
        "Nya～o!\x02",
    )

    CloseMessageWindow()
    Jump("loc_84AD")

    label("loc_847B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8497")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #378
        0xFE,
        "Nya～o!\x02",
    )

    CloseMessageWindow()
    Jump("loc_84AD")

    label("loc_8497")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #379
        0xFE,
        "Nyayayaa～.\x02",
    )

    CloseMessageWindow()

    label("loc_84AD")

    TalkEnd(0x34)
    Return()

    # Function_44_845C end

    def Function_45_84B1(): pass

    label("Function_45_84B1")

    OP_EA(0x1, 0x2, 0x0, 0x0)
    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_8533")

    ChrTalk(    #380
        0xFE,
        "Oh, my sweet lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "I pride myself on my sobriety of\x01",
            "thought, but this intoxication of love\x01",
            "is real!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_863C")

    label("loc_8533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_863C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_85B3")

    ChrTalk(    #382
        0xFE,
        (
            "To think someone so lovely had such\x01",
            "a secret...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "I can't carelessly invite her out\x01",
            "like this. Curses!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_863C")

    label("loc_85B3")


    ChrTalk(    #384
        0xFE,
        "Ah, how terrible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "To think someone so lovely had such\x01",
            "a secret...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "I can't carelessly invite her out\x01",
            "like this. Curses!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_863C")

    TalkEnd(0x2A)
    Return()

    # Function_45_84B1 end

    def Function_46_8640(): pass

    label("Function_46_8640")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_87F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_86CD")

    ChrTalk(    #387
        0xFE,
        (
            "Just...ignore my partner off to the side\x01",
            "over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "He's come down with another case of the\x01",
            "same old disease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87F1")

    label("loc_86CD")


    ChrTalk(    #389
        0xFE,
        (
            "Looks like that army squad's started\x01",
            "patrolling the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "That is one hell of a patrol schedule, too,\x01",
            "looks like. I wonder if something happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "Oh, and don't mind my partner off\x01",
            "to the side over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "He's come down with another case of the\x01",
            "same old disease. Again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_87F1")

    Jump("loc_8983")

    label("loc_87F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_8983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_8893")

    ChrTalk(    #393
        0xFE,
        (
            "I dunno if that lady really matches Anton's\x01",
            "fever-dream of an ideal girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xFE,
        (
            "He'd get more out of watching the pigeons,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8983")

    label("loc_8893")


    ChrTalk(    #395
        0xFE,
        (
            "I dunno if that lady really matches Anton's\x01",
            "fever-dream of an ideal girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xFE,
        (
            "He'd get more out of watching the pigeons,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "I'm serious, too. Pigeons are good people!\x01",
            "Hard to get tired of watching them bird it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_8983")

    TalkEnd(0x2B)
    Return()

    # Function_46_8640 end

    def Function_47_8987(): pass

    label("Function_47_8987")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89A7")
    Call(0, 81)
    FadeToBright(0, 0)
    Call(0, 82)

    label("loc_89A7")

    SetChrPos(0x101, 55680, 250, 28860, 270)
    SetChrPos(0x103, 56680, 250, 28860, 270)
    SetChrPos(0xF8, 57680, 250, 28860, 270)
    SetChrPos(0xF9, 58680, 250, 28860, 270)
    OP_6D(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x30)
    OP_43(0x103, 0x1, 0x0, 0x31)
    OP_43(0xF8, 0x1, 0x0, 0x32)
    OP_43(0xF9, 0x1, 0x0, 0x33)
    Sleep(2000)

    def lambda_8A6F():
        OP_6D(50680, 250, 28860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A6F)

    def lambda_8A87():
        OP_6C(39000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8A87)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #398
        0x101,
        (
            "#1007FThis is ridiculous!\x02\x03",

            "I know this city like the back of my\x01",
            "hand and I STILL feel like I could get\x01",
            "lost in this soup!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x103,
        (
            "#020FAnd that, Estelle, is why you have a\x01",
            "map and compass.\x02\x03",

            "If you feel like you're losing direction,\x01",
            "be sure and keep an eye on them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CD5")

    ChrTalk(    #400
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads.\x01",
            "But, um...\x02\x03",

            "Agate? Tita?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x106,
        "#051FSure, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x107,
        (
            "#061FYour house, Estelle?\x01",
            "Ooooh, I can't wait! ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_8CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E14")

    ChrTalk(    #403
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Agate? Olivier?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x106,
        "#051FSure, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x104,
        (
            "#031FEstelle's home?\x01",
            "Oh, this should be quite the detour.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_8E14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F55")

    ChrTalk(    #406
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Agate? Kloe?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x106,
        "#051FSure, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x105,
        (
            "#048FA visit to your home, Estelle?\x01",
            "I'd love to see it myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_8F55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90A1")

    ChrTalk(    #409
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Agate? Zin?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x106,
        "#051FSure, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x108,
        (
            "#071FHaha! Looks like I'll get a chance to visit\x01",
            "sooner than expected, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_90A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91F2")

    ChrTalk(    #412
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Tita? Olivier?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x107,
        "#061FYeah, I'd love to see your house! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x104,
        (
            "#031FEstelle's home?\x01",
            "Oh, this should be quite the detour.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_91F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9345")

    ChrTalk(    #415
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Tita? Kloe?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x107,
        "#061FYeah, I'd love to see your house! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x105,
        (
            "#048FA visit to your home, Estelle?\x01",
            "I'd love to see it myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_9345")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94A3")

    ChrTalk(    #418
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "Okay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "#1015FTita? Zin?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x107,
        "#061FYeah, I'd love to see your house! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x108,
        (
            "#071FHaha! Looks like I'll get a chance to visit\x01",
            "sooner than expected, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_94A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95F7")

    ChrTalk(    #421
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Kloe? Olivier?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x105,
        (
            "#048FYes, I'd be happy to stop by\x01",
            "your home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x104,
        (
            "#031FEstelle's home?\x01",
            "Oh, this should be quite the detour.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_95F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_974A")

    ChrTalk(    #424
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay! So we need to check just how far\x01",
            "the fog's spread on the roads. But, umm...\x02\x03",

            "Olivier? Zin?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x104,
        "#031FNot in the slightest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x108,
        (
            "#071FHaha! Looks like I'll get a chance to visit\x01",
            "sooner than expected, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98A8")

    label("loc_974A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98A8")

    ChrTalk(    #427
        0x101,
        (
            "#1006FYeah, good point.\x02\x03",

            "#1015FOkay, so we need to check just how far\x01",
            "the fog's spread on the roads. But, um...\x02\x03",

            "Kloe? Zin?\x02\x03",

            "Do you mind if we stop by my house and\x01",
            "see how things are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x105,
        (
            "#048FYes, I'd be happy to stop by\x01",
            "your home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x108,
        (
            "#071FHaha! Looks like I'll get a chance to visit\x01",
            "sooner than expected, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98A8")


    ChrTalk(    #430
        0x103,
        "#027FWell, let's be off then, hmm?\x02",
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x4, 0x2)
    OP_28(0x8F, 0x4, 0x8)
    OP_28(0x8F, 0x1, 0x1)
    OP_28(0x8F, 0x1, 0x2)
    OP_28(0x8F, 0x1, 0x4)
    OP_28(0x8F, 0x1, 0x10)
    OP_28(0x8F, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_47_8987 end

    def Function_48_98FB(): pass

    label("Function_48_98FB")

    SetChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_48_98FB end

    def Function_49_9935(): pass

    label("Function_49_9935")

    OP_90(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_49_9935 end

    def Function_50_9965(): pass

    label("Function_50_9965")

    OP_90(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_50_9965 end

    def Function_51_9995(): pass

    label("Function_51_9995")

    OP_8E(0xFE, 0xCEAE, 0xFA, 0x70BC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 59)
    OP_70(0xA, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_71(0xA, 0x800)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_90(0xFE, 0xFFFFFB32, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_51_9995 end

    def Function_52_99F9(): pass

    label("Function_52_99F9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A19")
    Call(0, 81)
    FadeToBright(0, 0)
    Call(0, 82)

    label("loc_9A19")

    OP_6D(49260, 0, 15200, 0)
    OP_67(0, 8770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(29000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 48750, 0, 5350, 0)
    SetChrPos(0x103, 49910, 0, 5310, 0)
    SetChrPos(0xF8, 48680, 0, 4040, 0)
    SetChrPos(0xF9, 49870, 0, 3980, 0)
    FadeToBright(1000, 0)

    def lambda_9AA9():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AA9)
    Sleep(100)

    def lambda_9AC9():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9AC9)
    Sleep(200)

    def lambda_9AE9():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9AE9)
    Sleep(100)

    def lambda_9B09():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9B09)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x32)
    Sleep(500)

    ChrTalk(    #431
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(1000)
    Call(0, 55)
    Return()

    # Function_52_99F9 end

    def Function_53_9B6D(): pass

    label("Function_53_9B6D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B8D")
    Call(0, 81)
    FadeToBright(0, 0)
    Call(0, 82)

    label("loc_9B8D")

    OP_6D(17320, 0, 39700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(227000, 0)
    OP_6E(261, 0)
    SetChrPos(0x101, 10520, 0, 40860, 90)
    SetChrPos(0x103, 10520, 0, 39800, 90)
    SetChrPos(0xF8, 9520, 0, 41000, 90)
    SetChrPos(0xF9, 9520, 0, 39850, 90)
    FadeToBright(1000, 0)

    def lambda_9C1D():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C1D)
    Sleep(100)

    def lambda_9C3D():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C3D)
    Sleep(200)

    def lambda_9C5D():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9C5D)
    Sleep(100)

    def lambda_9C7D():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9C7D)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x32)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(1000)
    Call(0, 55)
    Return()

    # Function_53_9B6D end

    def Function_54_9CCA(): pass

    label("Function_54_9CCA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CEA")
    Call(0, 81)
    FadeToBright(0, 0)
    Call(0, 82)

    label("loc_9CEA")

    OP_6D(27470, 0, 70500, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(299000, 0)
    OP_6E(303, 0)
    SetChrPos(0x101, 28700, 0, 77670, 180)
    SetChrPos(0x103, 27450, 0, 77670, 180)
    SetChrPos(0xF8, 28690, 0, 78670, 180)
    SetChrPos(0xF9, 27410, 0, 78670, 180)
    FadeToBright(1000, 0)

    def lambda_9D7A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D7A)
    Sleep(100)

    def lambda_9D9A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9D9A)
    Sleep(200)

    def lambda_9DBA():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9DBA)
    Sleep(100)

    def lambda_9DDA():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9DDA)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x32)
    Sleep(500)

    ChrTalk(    #432
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(1000)
    Call(0, 55)
    Return()

    # Function_54_9CCA end

    def Function_55_9E37(): pass

    label("Function_55_9E37")


    ChrTalk(    #433
        0x101,
        (
            "#1011FDid you guys...hear the sound\x01",
            "of a bell just now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB7")

    ChrTalk(    #434
        0x107,
        (
            "#061FYeah! It sounds really far away,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FCB")

    label("loc_9EB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EF6")

    ChrTalk(    #435
        0x106,
        (
            "#051FYeah. Sounds pretty far off,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FCB")

    label("loc_9EF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F3F")

    ChrTalk(    #436
        0x104,
        (
            "#035FHeh, indeed. It sounds quite\x01",
            "distant, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FCB")

    label("loc_9F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F82")

    ChrTalk(    #437
        0x105,
        (
            "#048FI did. It sounds quite distant,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FCB")

    label("loc_9F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FCB")

    ChrTalk(    #438
        0x108,
        (
            "#070FYeah. It didn't sound like it\x01",
            "was nearby, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A008")

    ChrTalk(    #439
        0x107,
        "#061FHeehee. It was really pretty, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A102")

    label("loc_A008")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A03C")

    ChrTalk(    #440
        0x106,
        "#051FSounded pretty nice, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A102")

    label("loc_A03C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A093")

    ChrTalk(    #441
        0x104,
        (
            "#035FAnd, ah...such a beautiful sound!\x01",
            "It resonates with my soul.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A102")

    label("loc_A093")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D3")

    ChrTalk(    #442
        0x105,
        "#048FHaha. It was really very lovely, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A102")

    label("loc_A0D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A102")

    ChrTalk(    #443
        0x108,
        "#070FReal pretty sound, too.\x02",
    )

    CloseMessageWindow()

    label("loc_A102")


    ChrTalk(    #444
        0x101,
        (
            "#1001FYeah, I know! It was, like, hypnotizing\x01",
            "for a second, there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x103,
        "#023F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #446
        0x101,
        (
            "#1015FUh, Schera? You okay?\x01",
            "You're spacing out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #447
        0x103,
        (
            "#524FAh, no, it's nothing.\x02\x03",

            "Like you said, it's a lovely sound.\x01",
            "It...enchanted me for a moment,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x101,
        (
            "#1006FYou too, huh?\x02\x03",

            "You don't hear a bell that nice often!\x01",
            "I wonder if Rinon got one in or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x103,
        (
            "#026FIt's...possible.\x02\x03",

            "#020FAnyway, we have a clear picture of\x01",
            "how far the fog extends now.\x02\x03",

            "We should let Aina know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x101,
        "#1006FYeah, let's get back.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_55_9E37 end

    def Function_56_A348(): pass

    label("Function_56_A348")

    EventBegin(0x0)
    OP_20(0x3E8)
    OP_21()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38A")
    Call(0, 81)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)

    label("loc_A38A")

    FadeToDark(0, 0, -1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    SetChrName("")

    AnonymousTalk(    #451
        (
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from the\x01",
            "mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 55680, 250, 28860, 270)
    SetChrPos(0x103, 56680, 250, 28860, 270)
    SetChrPos(0xF8, 57680, 250, 28860, 270)
    SetChrPos(0xF9, 58680, 250, 28860, 270)
    OP_1D(0xA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x39)
    OP_43(0x103, 0x1, 0x0, 0x31)
    OP_43(0xF8, 0x1, 0x0, 0x32)
    OP_43(0xF9, 0x1, 0x0, 0x33)
    Sleep(2000)

    def lambda_A526():
        OP_6D(50680, 250, 28860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A526)

    def lambda_A53E():
        OP_6C(39000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A53E)
    WaitChrThread(0xF9, 0x1)
    Sleep(200)

    ChrTalk(    #452
        0x101,
        (
            "#1011F#6POkay! It's time we finally got to Bose.\x01",
            "Y'know, like we've been planning for a\x01",
            "million years now.\x02\x03",

            "It's the only place that hasn't seen an\x01",
            "experiment, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0x103,
        (
            "#020F#6PThat's true, \x02",

            "but from the sounds of it,\x01",
            "there isn't anything odd happening in\x01",
            "Bose.\x02\x03",

            "I think we can take our time, for once,\x01",
            "and help out here in Rolent a bit before\x01",
            "heading out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x101,
        (
            "#1006F#6PSounds good.\x02\x03",

            "Let's see if there's anything else to do,\x01",
            "and head for the landing port when we're done.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x92, 0x1, 0x100)
    OP_28(0x92, 0x1, 0x200)
    OP_28(0x92, 0x1, 0x400)
    OP_28(0x92, 0x1, 0x800)
    OP_28(0x92, 0x1, 0x1000)
    EventEnd(0x0)
    Return()

    # Function_56_A348 end

    def Function_57_A752(): pass

    label("Function_57_A752")

    SetChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_57_A752 end

    def Function_58_A7A0(): pass

    label("Function_58_A7A0")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrPos(0x8, 49400, 0, 53090, 180)
    SetChrPos(0x9, 40640, 0, 41220, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_43(0x8, 0x1, 0x0, 0x3B)
    OP_43(0x9, 0x1, 0x0, 0x3C)
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_6D(49420, 0, 47770, 0)
    OP_67(0, 12280, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(19000, 0)
    OP_6E(386, 0)
    FadeToBright(1000, 0)
    StopSound(0x0, 0x0, 0x1F40)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)

    def lambda_A87D():
        OP_6D(49240, 0, 28690, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_A87D)

    def lambda_A895():
        OP_67(0, 6000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_A895)

    def lambda_A8AD():
        OP_6C(13000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A8AD)

    def lambda_A8BD():
        OP_6E(401, 10000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A8BD)
    OP_43(0xA, 0x1, 0x0, 0x3D)
    OP_43(0xB, 0x1, 0x0, 0x3E)
    OP_43(0xC, 0x1, 0x0, 0x3F)
    OP_43(0xD, 0x1, 0x0, 0x40)
    WaitChrThread(0x1, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0210   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_58_A7A0 end

    def Function_59_A901(): pass

    label("Function_59_A901")

    OP_8E(0xFE, 0xC0F8, 0x0, 0xB3C4, 0x3E8, 0x0)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_A936")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A972")
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(400)
    Jump("loc_A936")

    label("loc_A972")

    Return()

    # Function_59_A901 end

    def Function_60_A973(): pass

    label("Function_60_A973")

    Sleep(500)
    OP_8E(0xFE, 0xB9C8, 0x0, 0xA104, 0x3E8, 0x0)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_A9AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9E9")
    OP_8C(0xFE, 180, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(400)
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    Jump("loc_A9AD")

    label("loc_A9E9")

    Return()

    # Function_60_A973 end

    def Function_61_A9EA(): pass

    label("Function_61_A9EA")

    SetChrPos(0xFE, 54290, 250, 28900, 270)
    OP_72(0xA, 0x10)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC378, 0x0, 0x7800, 0x7D0, 0x0)

    label("loc_AA3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA78")
    OP_8C(0xFE, 315, 400)
    Sleep(400)
    OP_8C(0xFE, 45, 400)
    Sleep(400)
    OP_8C(0xFE, 315, 400)
    Sleep(400)
    OP_8C(0xFE, 225, 400)
    Sleep(400)
    Jump("loc_AA3C")

    label("loc_AA78")

    Return()

    # Function_61_A9EA end

    def Function_62_AA79(): pass

    label("Function_62_AA79")

    Sleep(500)
    SetChrPos(0xFE, 43270, 250, 33060, 90)
    OP_72(0x3, 0x10)
    OP_70(0x3, 0x3B)
    OP_73(0x3)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBCFC, 0x0, 0x8340, 0x7D0, 0x0)

    label("loc_AAD0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB0C")
    OP_8C(0xFE, 180, 300)
    Sleep(600)
    OP_8C(0xFE, 270, 300)
    Sleep(600)
    OP_8C(0xFE, 0, 300)
    Sleep(600)
    OP_8C(0xFE, 90, 300)
    Sleep(600)
    Jump("loc_AAD0")

    label("loc_AB0C")

    Return()

    # Function_62_AA79 end

    def Function_63_AB0D(): pass

    label("Function_63_AB0D")

    Sleep(4000)
    SetChrPos(0xFE, 43270, 250, 33060, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBA18, 0x0, 0x89EE, 0x7D0, 0x0)

    label("loc_AB50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB8C")
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 360, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Jump("loc_AB50")

    label("loc_AB8C")

    Return()

    # Function_63_AB0D end

    def Function_64_AB8D(): pass

    label("Function_64_AB8D")

    Sleep(1000)
    SetChrPos(0xFE, 43290, 250, 22060, 90)
    OP_72(0x1, 0x10)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC0C, 0x0, 0x6306, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)

    label("loc_ABEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC0F")
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 135, 400)
    Sleep(1000)
    Jump("loc_ABEB")

    label("loc_AC0F")

    Return()

    # Function_64_AB8D end

    def Function_65_AC10(): pass

    label("Function_65_AC10")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SoundLoad(191)
    SoundLoad(180)
    SoundLoad(141)
    OP_D2(0x260221, 0x260226, 0x9)
    OP_D2(0x260220, 0x260225, 0xA)
    SetChrChipByIndex(0x33, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC53")
    Call(0, 81)
    Call(0, 83)

    label("loc_AC53")

    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x1A, 0x0)
    OP_44(0x1B, 0x0)
    OP_44(0x1C, 0x0)
    OP_44(0x1D, 0x0)
    OP_44(0x1E, 0x0)
    OP_44(0x29, 0x0)
    SetChrPos(0x12, 72900, 500, 33000, 0)
    SetChrPos(0x13, 72900, 500, 33000, 0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xE, 68880, 0, 41940, 135)
    SetChrPos(0xF, 68520, 0, 40910, 135)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 70270, 0, 37620, 135)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x10, 70320, 0, 38640, 135)
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
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    SetChrPos(0x102, 69140, 0, 39210, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8C")
    SetChrPos(0x106, 69130, 0, 40270, 135)

    label("loc_AD8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADAB")
    SetChrPos(0x108, 69000, 0, 38290, 135)

    label("loc_ADAB")

    SetChrPos(0x101, 73140, 0, 40470, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADDB")
    SetChrPos(0x103, 74000, 0, 40300, 180)

    label("loc_ADDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADFA")
    SetChrPos(0x107, 72170, 0, 40280, 180)

    label("loc_ADFA")

    LoadEffect(0x0, "map\\\\mp016_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 74440, 0, 38950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(65680, 0, 38210, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(110000, 0)
    OP_6E(262, 0)
    OP_44(0x1A, 0x0)
    OP_44(0x1B, 0x0)
    OP_44(0x1C, 0x0)
    SetChrPos(0x1A, 55200, 12320, 47260, 135)
    SetChrPos(0x1B, 54200, 12320, 46260, 0)
    SetChrPos(0x1C, 53570, 12000, 47000, 225)
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x40)

    def lambda_AF04():
        OP_6C(135000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AF04)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x5A)

    def lambda_AF2A():
        OP_6D(73060, 500, 34550, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF2A)

    def lambda_AF42():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AF42)
    OP_43(0x1A, 0x1, 0x0, 0x46)
    OP_43(0x1A, 0x3, 0x0, 0x49)
    Sleep(200)
    OP_43(0x1B, 0x1, 0x0, 0x47)
    OP_43(0x1B, 0x3, 0x0, 0x49)
    Sleep(200)
    OP_43(0x1C, 0x1, 0x0, 0x48)
    OP_43(0x1C, 0x3, 0x0, 0x49)
    OP_6E(262, 5000)
    OP_6F(0xE, 0)
    OP_70(0xE, 0x3B)
    OP_73(0xE)
    Sleep(200)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x38, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x39, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_22(0xBF, 0x0, 0x64)
    OP_43(0x12, 0x1, 0x0, 0x42)
    Sleep(1000)
    OP_43(0x13, 0x1, 0x0, 0x43)
    Sleep(1000)
    OP_43(0x2D, 0x1, 0x0, 0x44)
    Sleep(1000)
    OP_43(0x2C, 0x1, 0x0, 0x45)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x2C, 0x1)
    OP_82(0x0, 0x2)
    WaitChrThread(0x2D, 0x1)
    OP_8E(0x2D, 0x12264, 0x0, 0x8E4E, 0x7D0, 0x0)

    ChrTalk(    #455
        0x2D,
        "#5PAnd now, we throw the bride's bouquet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x2D,
        "#5PAll unmarried women, please step forward.\x02",
    )

    CloseMessageWindow()

    def lambda_B1F2():
        OP_6D(72780, 0, 39500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1F2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_B21C():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_B21C)
    Sleep(100)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_B249():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_B249)
    Sleep(100)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_B276():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_B276)
    Sleep(100)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_B2A3():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_B2A3)
    Sleep(100)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_B2D0():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_B2D0)
    Sleep(100)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_B2FD():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_B2FD)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #457
        0x35,
        "#5PAaaah! The moment of truth!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #458
        0x30,
        "Young Woman",
        "#6PEllieee! Throw it over heeeeere!\x02",
    )

    CloseMessageWindow()
    OP_43(0xE, 0x1, 0x0, 0x5B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B49F")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #459
        0x108,
        (
            "#070FAh, as I understand it, the lady who catches\x01",
            "the bouquet is likely to be married next?\x01",
            "An interesting tradition!\x02\x03",

            "#071FHaha! Easy to see why some of the ladies\x01",
            "in attendance are so worked up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #460
        0x102,
        (
            "#1040FIt is the most exciting part of a wedding,\x01",
            "in some ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A5")

    label("loc_B49F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5A5")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #461
        0x106,
        (
            "#053FOh, the bouquet throw...\x02\x03",

            "#555FMan, guys don't understand this stuff.\x01",
            "I guess it's exciting, but some of those ladies\x01",
            "look more bloodthirsty than anything.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #462
        0x102,
        (
            "#1040FIt is the most exciting part of a wedding,\x01",
            "in some ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5A5")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #463
        0x101,
        "#1016F#4PSeriously, everyone's getting into it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B72E")
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #464
        0x103,
        (
            "#020FYou're damned right.\x01",
            "C'mon, now, Estelle, stop wasting time!\x02\x03",

            "Check the wind and let's get a good spot!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    SetChrFlags(0x30, 0x40)

    def lambda_B691():
        OP_94(0x0, 0x30, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_B691)
    Sleep(200)
    OP_94(0x1, 0x103, 0x10E, 0xC8, 0x7D0, 0x0)
    OP_62(0x103, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x103, 0x30, 400)

    ChrTalk(    #465
        0x103,
        "#024F#4PHey, you! Stop pushing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        "#1019F#6PShe's...actually serious.\x02",
    )

    CloseMessageWindow()

    def lambda_B726():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B726)

    label("loc_B72E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B85C")

    ChrTalk(    #467
        0x107,
        "#062F#6POoo-ooooh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #468
        0x101,
        "#1007F#6PEr. Tita. You're going for it too?\x02",
    )

    CloseMessageWindow()
    OP_94(0x0, 0x107, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #469
        0x107,
        (
            "#062F#6PO-O-Okay, humidity 55%...\x01",
            "Wind is east-southeast at 3.5 arge a second...\x02\x03",

            "Yeah... This should be the most likely spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x101,
        "#1016F#6PI didn't think she'd be that serious...\x02",
    )

    CloseMessageWindow()

    label("loc_B85C")

    OP_8C(0x101, 180, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B907")

    ChrTalk(    #471
        0x101,
        (
            "#1015F#6POh, what the hey.\x01",
            "I might as well participate too.\x02\x03",

            "I am a comely maiden in the flower\x01",
            "of womanhood...or something, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B907")


    def lambda_B90D():
        OP_6D(73720, 500, 33120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B90D)
    OP_44(0xE, 0x1)
    Sleep(500)
    OP_8C(0x12, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #472
        0x12,
        (
            "#5PMm, it's pretty hard to throw something\x01",
            "behind you like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x12,
        (
            "#5PWell, everyone, don't be upset if it\x01",
            "misses you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x12,
        "#5POne, two...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x12,
        "#5PTHREE!\x02",
    )

    CloseMessageWindow()
    OP_43(0x42, 0x1, 0x0, 0x4C)

    def lambda_B9E5():

        label("loc_B9E5")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_B9E5")

    QueueWorkItem2(0x101, 1, lambda_B9E5)

    def lambda_B9F6():

        label("loc_B9F6")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_B9F6")

    QueueWorkItem2(0x102, 1, lambda_B9F6)

    def lambda_BA07():

        label("loc_BA07")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA07")

    QueueWorkItem2(0xF8, 1, lambda_BA07)

    def lambda_BA18():

        label("loc_BA18")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA18")

    QueueWorkItem2(0xF9, 1, lambda_BA18)

    def lambda_BA29():

        label("loc_BA29")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA29")

    QueueWorkItem2(0x35, 1, lambda_BA29)

    def lambda_BA3A():

        label("loc_BA3A")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA3A")

    QueueWorkItem2(0x36, 1, lambda_BA3A)

    def lambda_BA4B():

        label("loc_BA4B")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA4B")

    QueueWorkItem2(0x37, 1, lambda_BA4B)

    def lambda_BA5C():

        label("loc_BA5C")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA5C")

    QueueWorkItem2(0x38, 1, lambda_BA5C)

    def lambda_BA6D():

        label("loc_BA6D")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA6D")

    QueueWorkItem2(0x39, 1, lambda_BA6D)

    def lambda_BA7E():

        label("loc_BA7E")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA7E")

    QueueWorkItem2(0x3A, 1, lambda_BA7E)

    def lambda_BA8F():

        label("loc_BA8F")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BA8F")

    QueueWorkItem2(0x3B, 1, lambda_BA8F)

    def lambda_BAA0():

        label("loc_BAA0")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BAA0")

    QueueWorkItem2(0x3C, 1, lambda_BAA0)

    def lambda_BAB1():

        label("loc_BAB1")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BAB1")

    QueueWorkItem2(0x3D, 1, lambda_BAB1)

    def lambda_BAC2():

        label("loc_BAC2")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BAC2")

    QueueWorkItem2(0x3E, 1, lambda_BAC2)

    def lambda_BAD3():

        label("loc_BAD3")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BAD3")

    QueueWorkItem2(0x3F, 1, lambda_BAD3)

    def lambda_BAE4():

        label("loc_BAE4")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BAE4")

    QueueWorkItem2(0x40, 1, lambda_BAE4)

    def lambda_BAF5():

        label("loc_BAF5")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BAF5")

    QueueWorkItem2(0x41, 1, lambda_BAF5)

    def lambda_BB06():

        label("loc_BB06")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB06")

    QueueWorkItem2(0x13, 1, lambda_BB06)

    def lambda_BB17():

        label("loc_BB17")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB17")

    QueueWorkItem2(0x2E, 1, lambda_BB17)

    def lambda_BB28():

        label("loc_BB28")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB28")

    QueueWorkItem2(0x2F, 1, lambda_BB28)

    def lambda_BB39():

        label("loc_BB39")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB39")

    QueueWorkItem2(0x30, 1, lambda_BB39)

    def lambda_BB4A():

        label("loc_BB4A")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB4A")

    QueueWorkItem2(0x31, 1, lambda_BB4A)

    def lambda_BB5B():

        label("loc_BB5B")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB5B")

    QueueWorkItem2(0x32, 1, lambda_BB5B)

    def lambda_BB6C():

        label("loc_BB6C")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB6C")

    QueueWorkItem2(0x11, 1, lambda_BB6C)

    def lambda_BB7D():

        label("loc_BB7D")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB7D")

    QueueWorkItem2(0x33, 1, lambda_BB7D)

    def lambda_BB8E():

        label("loc_BB8E")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB8E")

    QueueWorkItem2(0x10, 1, lambda_BB8E)

    def lambda_BB9F():

        label("loc_BB9F")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BB9F")

    QueueWorkItem2(0x2D, 1, lambda_BB9F)

    def lambda_BBB0():

        label("loc_BBB0")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BBB0")

    QueueWorkItem2(0x2C, 1, lambda_BBB0)

    def lambda_BBC1():

        label("loc_BBC1")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BBC1")

    QueueWorkItem2(0x34, 1, lambda_BBC1)

    def lambda_BBD2():

        label("loc_BBD2")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BBD2")

    QueueWorkItem2(0xF, 1, lambda_BBD2)

    def lambda_BBE3():

        label("loc_BBE3")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_BBE3")

    QueueWorkItem2(0xE, 1, lambda_BBE3)
    OP_6D(79220, 3000, 36290, 2000)

    ChrTalk(    #476
        0x35,
        "#2PAaaaah, not that way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x37,
        "#2PWhere're you throwing iiiiiit?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x42, 0x1)
    Sleep(200)
    Fade(1000)
    OP_6D(73800, 0, 38790, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCC2")

    ChrTalk(    #478
        0x107,
        "#562F#5PAwww, I wanted it...\x02",
    )

    CloseMessageWindow()

    label("loc_BCC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD0C")

    ChrTalk(    #479
        0x103,
        (
            "#025F#6P*siiigh* I am doomed to spinsterdom,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD0C")


    ChrTalk(    #480
        0x101,
        (
            "#1007F#5PWelllll...that flew off in a totally\x01",
            "different direction.\x02\x03",

            "I wonder who even caught that?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x35, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x37, 0x1)
    OP_44(0x38, 0x1)
    OP_44(0x39, 0x1)
    OP_44(0x3A, 0x1)
    OP_44(0x3B, 0x1)
    OP_44(0x3C, 0x1)
    OP_44(0x3D, 0x1)
    OP_44(0x3E, 0x1)
    OP_44(0x3F, 0x1)
    OP_44(0x40, 0x1)
    OP_44(0x41, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x2E, 0x1)
    OP_44(0x2F, 0x1)
    OP_44(0x30, 0x1)
    OP_44(0x31, 0x1)
    OP_44(0x32, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x33, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x2D, 0x1)
    OP_44(0x2C, 0x1)
    OP_44(0x34, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x42, 0x1)
    SetChrPos(0x29, 82720, 0, 39930, 270)
    SetChrPos(0x42, 82650, 600, 39930, 90)
    SetChrFlags(0x42, 0x2)
    SetChrSubChip(0x42, 1)

    NpcTalk(    #481
        0x29,
        "Young Woman",
        "#3PUmmm...\x02",
    )

    CloseMessageWindow()

    def lambda_BE46():
        OP_6D(78070, 0, 40000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE46)

    def lambda_BE5E():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BE5E)

    def lambda_BE6E():

        label("loc_BE6E")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BE6E")

    QueueWorkItem2(0x101, 1, lambda_BE6E)

    def lambda_BE7F():

        label("loc_BE7F")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BE7F")

    QueueWorkItem2(0x102, 1, lambda_BE7F)

    def lambda_BE90():

        label("loc_BE90")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BE90")

    QueueWorkItem2(0xF8, 1, lambda_BE90)

    def lambda_BEA1():

        label("loc_BEA1")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BEA1")

    QueueWorkItem2(0xF9, 1, lambda_BEA1)

    def lambda_BEB2():

        label("loc_BEB2")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BEB2")

    QueueWorkItem2(0x35, 1, lambda_BEB2)

    def lambda_BEC3():

        label("loc_BEC3")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BEC3")

    QueueWorkItem2(0x36, 1, lambda_BEC3)

    def lambda_BED4():

        label("loc_BED4")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BED4")

    QueueWorkItem2(0x37, 1, lambda_BED4)

    def lambda_BEE5():

        label("loc_BEE5")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BEE5")

    QueueWorkItem2(0x38, 1, lambda_BEE5)

    def lambda_BEF6():

        label("loc_BEF6")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BEF6")

    QueueWorkItem2(0x39, 1, lambda_BEF6)

    def lambda_BF07():

        label("loc_BF07")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF07")

    QueueWorkItem2(0x3A, 1, lambda_BF07)

    def lambda_BF18():

        label("loc_BF18")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF18")

    QueueWorkItem2(0x3B, 1, lambda_BF18)

    def lambda_BF29():

        label("loc_BF29")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF29")

    QueueWorkItem2(0x3C, 1, lambda_BF29)

    def lambda_BF3A():

        label("loc_BF3A")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF3A")

    QueueWorkItem2(0x3D, 1, lambda_BF3A)

    def lambda_BF4B():

        label("loc_BF4B")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF4B")

    QueueWorkItem2(0x3E, 1, lambda_BF4B)

    def lambda_BF5C():

        label("loc_BF5C")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF5C")

    QueueWorkItem2(0x3F, 1, lambda_BF5C)

    def lambda_BF6D():

        label("loc_BF6D")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF6D")

    QueueWorkItem2(0x40, 1, lambda_BF6D)

    def lambda_BF7E():

        label("loc_BF7E")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF7E")

    QueueWorkItem2(0x41, 1, lambda_BF7E)

    def lambda_BF8F():

        label("loc_BF8F")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BF8F")

    QueueWorkItem2(0x13, 1, lambda_BF8F)

    def lambda_BFA0():

        label("loc_BFA0")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BFA0")

    QueueWorkItem2(0x2E, 1, lambda_BFA0)

    def lambda_BFB1():

        label("loc_BFB1")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BFB1")

    QueueWorkItem2(0x2F, 1, lambda_BFB1)

    def lambda_BFC2():

        label("loc_BFC2")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BFC2")

    QueueWorkItem2(0x30, 1, lambda_BFC2)

    def lambda_BFD3():

        label("loc_BFD3")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BFD3")

    QueueWorkItem2(0x31, 1, lambda_BFD3)

    def lambda_BFE4():

        label("loc_BFE4")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BFE4")

    QueueWorkItem2(0x32, 1, lambda_BFE4)

    def lambda_BFF5():

        label("loc_BFF5")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_BFF5")

    QueueWorkItem2(0x11, 1, lambda_BFF5)

    def lambda_C006():

        label("loc_C006")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C006")

    QueueWorkItem2(0x33, 1, lambda_C006)

    def lambda_C017():

        label("loc_C017")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C017")

    QueueWorkItem2(0x10, 1, lambda_C017)

    def lambda_C028():

        label("loc_C028")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C028")

    QueueWorkItem2(0x2D, 1, lambda_C028)

    def lambda_C039():

        label("loc_C039")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C039")

    QueueWorkItem2(0x2C, 1, lambda_C039)

    def lambda_C04A():

        label("loc_C04A")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C04A")

    QueueWorkItem2(0x34, 1, lambda_C04A)

    def lambda_C05B():

        label("loc_C05B")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C05B")

    QueueWorkItem2(0xF, 1, lambda_C05B)

    def lambda_C06C():

        label("loc_C06C")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C06C")

    QueueWorkItem2(0xE, 1, lambda_C06C)

    def lambda_C07D():

        label("loc_C07D")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_C07D")

    QueueWorkItem2(0x12, 1, lambda_C07D)
    ClearChrFlags(0x29, 0x80)
    WaitChrThread(0x101, 0x3)

    def lambda_C098():
        OP_8E(0xFE, 0x130B0, 0x258, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_C098)
    OP_8E(0x29, 0x130F6, 0x0, 0x9C40, 0x7D0, 0x0)

    ChrTalk(    #482
        0x29,
        "#6PHey, what's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x29,
        "#6PIt just fell from the sky...\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x35, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x37, 0x1)
    OP_44(0x38, 0x1)
    OP_44(0x39, 0x1)
    OP_44(0x3A, 0x1)
    OP_44(0x3B, 0x1)
    OP_44(0x3C, 0x1)
    OP_44(0x3D, 0x1)
    OP_44(0x3E, 0x1)
    OP_44(0x3F, 0x1)
    OP_44(0x40, 0x1)
    OP_44(0x41, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x2E, 0x1)
    OP_44(0x2F, 0x1)
    OP_44(0x30, 0x1)
    OP_44(0x31, 0x1)
    OP_44(0x32, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x33, 0x1)
    OP_44(0x10, 0x1)
    OP_44(0x2D, 0x1)
    OP_44(0x2C, 0x1)
    OP_44(0x34, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0xE, 0x1)
    OP_6D(75450, 0, 37780, 2000)

    ChrTalk(    #484
        0x12,
        "#2POh! So you picked it up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x12,
        "#2PThat's the wedding bouquet I threw.\x02",
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #486
        0x29,
        "#6PWHAAAAA?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x13,
        (
            "#2PCongratulations, miss. I'm sure you have\x01",
            "a wonderful future ahead of you!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #488
        0x29,
        "#6POh, no, no, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0x29,
        (
            "#6PI-I-I...\x01",
            "I'm not ready! What do I do?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(73160, 0, 40680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #490
        0x101,
        (
            "#1016F#6PAhh, haha...\x02\x03",

            "Y'know, I kinda think that ended up right\x01",
            "where it belonged.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C387")

    ChrTalk(    #491
        0x103,
        "#025F#6PI suppose...\x02",
    )

    CloseMessageWindow()

    label("loc_C387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3D8")

    ChrTalk(    #492
        0x107,
        (
            "#067F#6PHeehee! The bouquet does look really pretty\x01",
            "with her!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3D8")

    OP_6D(73230, 260, 34450, 2000)
    TurnDirection(0x2C, 0x13, 400)
    Sleep(500)

    ChrTalk(    #493
        0x2C,
        "#2PWell, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x2C,
        (
            "#2PWith...that, the wedding ceremony is\x01",
            "now formally concluded!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C454():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_C454)

    def lambda_C462():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C462)

    def lambda_C470():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C470)

    def lambda_C47E():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_C47E)

    def lambda_C48C():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C48C)

    def lambda_C49A():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_C49A)

    def lambda_C4A8():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_C4A8)

    def lambda_C4B6():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_C4B6)

    def lambda_C4C4():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_C4C4)

    def lambda_C4D2():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_C4D2)

    def lambda_C4E0():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_C4E0)

    def lambda_C4EE():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_C4EE)

    def lambda_C4FC():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_C4FC)

    def lambda_C50A():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_C50A)

    def lambda_C518():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_C518)

    def lambda_C526():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_C526)

    def lambda_C534():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_C534)

    def lambda_C542():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_C542)

    def lambda_C550():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_C550)

    def lambda_C55E():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_C55E)

    def lambda_C56C():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_C56C)

    def lambda_C57A():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_C57A)

    def lambda_C588():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_C588)

    def lambda_C596():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C596)

    def lambda_C5A4():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_C5A4)

    def lambda_C5B2():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C5B2)

    def lambda_C5C0():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_C5C0)

    def lambda_C5CE():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_C5CE)

    def lambda_C5DC():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_C5DC)

    def lambda_C5EA():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C5EA)

    def lambda_C5F8():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C5F8)

    def lambda_C606():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C606)

    def lambda_C614():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C614)
    Sleep(400)

    ChrTalk(    #495
        0x2D,
        "#1PMay Aidios' grace shine on you forevermore.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x2D, 400)

    ChrTalk(    #496
        0x12,
        "#2PThank you, Sister May.\x02",
    )

    CloseMessageWindow()

    def lambda_C681():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C681)
    TurnDirection(0x13, 0x2C, 400)

    ChrTalk(    #497
        0x13,
        (
            "#1PYou too, Father Divine...\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x2C,
        (
            "#2PThough our kingdom is beset on all sides\x01",
            "by storms and turmoil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x2C,
        (
            "#2PI pray to She Who Dwells Above that the\x01",
            "new tree of your family weathers it all\x01",
            "and grows strong and happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x2C,
        (
            "#2PIf you wish to thank me, and all assembled,\x01",
            "for this day, tend that tree and one\x01",
            "another as I know you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x13,
        "#1P...We will! I swear!\x02",
    )

    CloseMessageWindow()

    def lambda_C818():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C818)

    def lambda_C826():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C826)

    def lambda_C834():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_C834)

    def lambda_C842():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C842)

    def lambda_C850():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_C850)

    def lambda_C85E():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_C85E)

    def lambda_C86C():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_C86C)

    def lambda_C87A():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_C87A)

    def lambda_C888():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_C888)

    def lambda_C896():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_C896)

    def lambda_C8A4():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_C8A4)

    def lambda_C8B2():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_C8B2)

    def lambda_C8C0():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_C8C0)

    def lambda_C8CE():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_C8CE)

    def lambda_C8DC():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_C8DC)

    def lambda_C8EA():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_C8EA)

    def lambda_C8F8():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_C8F8)

    def lambda_C906():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_C906)

    def lambda_C914():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_C914)

    def lambda_C922():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_C922)

    def lambda_C930():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_C930)

    def lambda_C93E():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_C93E)

    def lambda_C94C():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C94C)

    def lambda_C95A():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_C95A)

    def lambda_C968():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C968)

    def lambda_C976():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_C976)

    def lambda_C984():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_C984)

    def lambda_C992():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C992)

    def lambda_C9A0():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C9A0)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x38, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x39, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_8C(0x13, 0, 400)
    OP_8C(0x12, 0, 400)
    OP_22(0xBF, 0x0, 0x64)

    def lambda_CB57():
        OP_94(0x1, 0xFE, 0x10E, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CB57)

    def lambda_CB6D():
        OP_94(0x1, 0xFE, 0x5A, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_CB6D)
    Sleep(500)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x12, 0x40)
    OP_8C(0x13, 270, 400)
    OP_8C(0x12, 90, 400)

    def lambda_CBA0():
        OP_94(0x0, 0xFE, 0x0, 0x96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CBA0)
    OP_94(0x0, 0x12, 0x0, 0x96, 0x1F4, 0x0)
    OP_62(0x13, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x38, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x39, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x38, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x39, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x3F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0xE, 0)
    ClearMapFlags(0x10000000)
    OP_20(0xBB8)
    Sleep(2000)
    OP_A2(0x2086)
    NewScene("ED6_DT21/T0130   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_65_AC10 end

    def Function_66_CF4C(): pass

    label("Function_66_CF4C")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11B0C, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11B0C, 0x1F4, 0x896C, 0x3E8, 0x0)
    Return()

    # Function_66_CF4C end

    def Function_67_CF8E(): pass

    label("Function_67_CF8E")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11F44, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11F44, 0x1E0, 0x896C, 0x3E8, 0x0)
    Return()

    # Function_67_CF8E end

    def Function_68_CFD0(): pass

    label("Function_68_CFD0")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x1220A, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_68_CFD0 end

    def Function_69_D005(): pass

    label("Function_69_D005")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x1186E, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_69_D005 end

    def Function_70_D03A(): pass

    label("Function_70_D03A")

    SetChrChipByIndex(0x1A, 11)
    ClearChrFlags(0x1A, 0x400)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x40)
    OP_98(0x0, 0x1A)
    OP_98(0x1, 0x11BA2, 0x1B58, 0x9132)
    OP_98(0x1, 0x16C10, 0x1F40, 0x97F4)
    OP_43(0xFE, 0x2, 0x0, 0x4B)
    OP_98(0x2, 0x1A, 0x157C, 0x2)
    Return()

    # Function_70_D03A end

    def Function_71_D07F(): pass

    label("Function_71_D07F")

    SetChrChipByIndex(0x1B, 11)
    ClearChrFlags(0x1B, 0x400)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x40)
    OP_98(0x0, 0x1B)
    OP_98(0x1, 0x10D88, 0x1B58, 0x91DC)
    OP_98(0x1, 0x16C10, 0x1388, 0x9BDC)
    OP_43(0xFE, 0x2, 0x0, 0x4B)
    OP_98(0x2, 0x1B, 0x157C, 0x2)
    Return()

    # Function_71_D07F end

    def Function_72_D0C4(): pass

    label("Function_72_D0C4")

    SetChrChipByIndex(0x1C, 11)
    ClearChrFlags(0x1C, 0x400)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x40)
    OP_98(0x0, 0x1C)
    OP_98(0x1, 0x109A0, 0x2328, 0x9D94)
    OP_98(0x1, 0x16C10, 0x1F40, 0x940C)
    OP_43(0xFE, 0x2, 0x0, 0x4B)
    OP_98(0x2, 0x1C, 0x157C, 0x2)
    Return()

    # Function_72_D0C4 end

    def Function_73_D109(): pass

    label("Function_73_D109")

    Sleep(800)
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(4000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Return()

    # Function_73_D109 end

    def Function_74_D12A(): pass

    label("Function_74_D12A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D162")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D15A")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_D162")

    label("loc_D15A")

    Sleep(15)
    Jump("Function_74_D12A")

    label("loc_D162")

    Return()

    # Function_74_D12A end

    def Function_75_D163(): pass

    label("Function_75_D163")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D178")
    OP_99(0xFE, 0x0, 0x7, 0x1770)
    Jump("Function_75_D163")

    label("loc_D178")

    Return()

    # Function_75_D163 end

    def Function_76_D179(): pass

    label("Function_76_D179")

    ClearChrFlags(0x42, 0x80)
    OP_22(0xCB, 0x0, 0x64)
    OP_98(0x0, 0x42)
    OP_98(0x1, 0x12AF2, 0x2710, 0x8D54)
    OP_98(0x1, 0x13A42, 0x1F40, 0x8DCC)
    OP_98(0x1, 0x150A4, 0x0, 0x9CFE)
    OP_98(0x2, 0x42, 0x157C, 0x2)
    Return()

    # Function_76_D179 end

    def Function_77_D1BB(): pass

    label("Function_77_D1BB")

    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_D264")
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #502
        0xE,
        "Whoa! It's Estelle AND Joshua!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #503
        0xF,
        (
            "Estelle, Joshua! Welcome back!\x02\x03",

            "You two are finally together again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2ED")

    label("loc_D264")

    TurnDirection(0xF, 0x101, 0)

    ChrTalk(    #504
        0xF,
        (
            "Huh?!\x02\x03",

            "Estelle! And JOSHUA'S with you!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x102, 400)
    Sleep(1000)

    ChrTalk(    #505
        0xE,
        (
            "WHOA! Joshua!\x02\x03",

            "Holy crap! You're back!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    label("loc_D2ED")


    ChrTalk(    #506
        0x101,
        "#1001FYeah, finally, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 400)

    ChrTalk(    #507
        0x102,
        (
            "#1040FHello, you two. Sorry I've been gone.\x02\x03",

            "Haha, you're both as energetic as ever.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 400)

    ChrTalk(    #508
        0xE,
        (
            "Heheh! Darn right!\x02\x03",

            "Are you guys working today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xF,
        (
            "You're investigating why the orbments\x01",
            "aren't working, I bet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xF, 400)

    ChrTalk(    #510
        0x102,
        (
            "#1040FEssentially, yes.\x02\x03",

            "Not that we can solve something like this\x01",
            "just by waving our hands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xE,
        (
            "Aww, that's obvious.\x02\x03",

            "You want to investigate something cool,\x01",
            "investigate that weird flying island\x01",
            "in the sky!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D65F")

    ChrTalk(    #512
        0x101,
        (
            "#1007FTrust me, if we could, we'd be over\x01",
            "there in a second.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 400)

    ChrTalk(    #513
        0x102,
        (
            "#1042FThe road lamps have been shut down,\x01",
            "so it's dangerous to head outside the\x01",
            "city.\x02\x03",

            "Luke, Pat, don't go out onto the roads.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 400)

    ChrTalk(    #514
        0xE,
        (
            "Haha! Yeah, another crisis, we know.\x02\x03",

            "It's kind of a bummer, but we'll stay\x01",
            "inside the city, don't worry.\x02\x03",

            "Okay! Let's go, Pat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xF,
        (
            "Uh, yeah!\x02\x03",

            "See you later, Estelle!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7F3")

    label("loc_D65F")


    ChrTalk(    #516
        0x101,
        (
            "#1007FIf we could, we'd be over there\x01",
            "in a second.\x02\x03",

            "You do know that orbments aren't working,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0x102,
        (
            "#1042FThe road lamps will all be dead,\x01",
            "so it's dangerous to head outside\x01",
            "the city.\x02\x03",

            "Luke, Pat, don't go out onto the roads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0xE,
        (
            "Haha! Yeah, another crisis, we know.\x02\x03",

            "It's kind of a bummer, but we'll stay\x01",
            "inside the city, don't worry.\x02\x03",

            "Okay! Let's go, Pat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0xF,
        (
            "Yeah!\x02\x03",

            "See you later, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7F3")

    OP_8C(0xE, 90, 400)
    OP_8C(0xF, 270, 400)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_A2(0x17)
    OP_A2(0x16)
    OP_A2(0x20A0)
    Return()

    # Function_77_D1BB end

    def Function_78_D813(): pass

    label("Function_78_D813")

    TalkBegin(0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DBEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB08")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(1000)

    ChrTalk(    #520
        0xFE,
        "Ah, Estelle...and Joshua's with you again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x102,
        "#1035FSorry I've been away, Fate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0xFE,
        (
            "My goodness, you've matured into quite\x01",
            "the man in the little while you've been\x01",
            "gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xFE,
        (
            "It's a relief to see you two together, though.\x01",
            "You seem to have become quite a bracer,\x01",
            "along with Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x102,
        "#1040FWe're managing, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0xFE,
        (
            "And things have gotten crazy all across\x01",
            "Liberl, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0xFE,
        (
            "I'm sure Cassius is even busier now than\x01",
            "he's ever been.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #527
        0xFE,
        (
            "I hope you two will work just as hard and\x01",
            "bring some honor to that badge you wear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0x101,
        "#1006FYeah! We'll do what we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0x102,
        "#1040FIf anything happens, please, contact the guild.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #530
        0xFE,
        "I will. You two be careful, yourselves.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x18)
    OP_A2(0x209B)
    Jump("loc_DBEF")

    label("loc_DB08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_DB5C")

    ChrTalk(    #531
        0xFE,
        "I'll contact the guild if anything happens.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0xFE,
        "You two be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DBEF")

    label("loc_DB5C")


    ChrTalk(    #533
        0xFE,
        (
            "When I woke up this morning, my orbal\x01",
            "devices wouldn't turn on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0xFE,
        (
            "I thought I should head out for the moment\x01",
            "and at least get some lights.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBEF")

    TalkEnd(0x46)
    Return()

    # Function_78_D813 end

    def Function_79_DBF3(): pass

    label("Function_79_DBF3")

    TalkBegin(0x47)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_DCC5")

    ChrTalk(    #535
        0xFE,
        (
            "The people of Rolent aren't panicking\x01",
            "even though their orbments aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0xFE,
        (
            "Still, there's nothing to be gained from fretting,\x01",
            "I suppose. Maybe I should take a page from\x01",
            "their book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD65")

    label("loc_DCC5")


    ChrTalk(    #537
        0xFE,
        (
            "I thought I'd step out of the hotel to take\x01",
            "a look at the floating island everyone's\x01",
            "talking about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0xFE,
        (
            "Sort of hard to see anything from here,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD65")

    TalkEnd(0x47)
    Return()

    # Function_79_DBF3 end

    def Function_80_DD69(): pass

    label("Function_80_DD69")

    TalkBegin(0x48)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_DE0F")

    ChrTalk(    #539
        0xFE,
        (
            "Looks like we can't expect the airships\x01",
            "to resume service any time soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0xFE,
        (
            "I guess as long as that floating island\x01",
            "is around, they won't work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEA6")

    label("loc_DE0F")


    ChrTalk(    #541
        0xFE,
        (
            "I heard you can see the floating island\x01",
            "very clearly from atop the clock tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0xFE,
        (
            "How big must it be if you can see it\x01",
            "from Rolent, though...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEA6")

    TalkEnd(0x48)
    Return()

    # Function_80_DD69 end

    def Function_81_DEAA(): pass

    label("Function_81_DEAA")

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
        (0, "loc_DF26"),
        (1, "loc_DF2C"),
        (SWITCH_DEFAULT, "loc_DF32"),
    )


    label("loc_DF26")

    OP_A2(0x1200)
    Jump("loc_DF32")

    label("loc_DF2C")

    OP_A2(0x1201)
    Jump("loc_DF32")

    label("loc_DF32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DF40")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_DF44")

    label("loc_DF40")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_DF44")

    Return()

    # Function_81_DEAA end

    def Function_82_DF45(): pass

    label("Function_82_DF45")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_82_DF45 end

    def Function_83_DF97(): pass

    label("Function_83_DF97")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_83_DF97 end

    def Function_84_DFF0(): pass

    label("Function_84_DFF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07F")
    EventBegin(0x1)

    ChrTalk(    #543
        0x101,
        (
            "#505FThis is...totally the wrong way.\x01",
            "I need to get home.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x142, 0x0, 400)

    ChrTalk(    #544
        0x142,
        "#1060FSo south exit, right?\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_E302")

    label("loc_E07F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E21D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0A3")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_E0AA")

    label("loc_E0A3")

    TurnDirection(0x103, 0x0, 400)

    label("loc_E0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_E11B")

    ChrTalk(    #545
        0x103,
        (
            "#020FI'm also curious as to what's going on\x01",
            "out there, but first we need to go to\x01",
            "the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1FF")

    label("loc_E11B")


    ChrTalk(    #546
        0x103,
        (
            "#020FI'm also curious as to what's going on\x01",
            "out there, but first we need to go to\x01",
            "the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1AA")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #547
        0x101,
        "#1000FRight.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E1AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1D5")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #548
        0x105,
        "#040FAll right.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E1D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1FF")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #549
        0x107,
        "#060FAh, okay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E1FF")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_E302")

    label("loc_E21D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E302")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E296")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #550
        0x103,
        (
            "#020FThis is no time for side-trips.\x01",
            "We need to report to the guildhouse first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2E7")

    label("loc_E296")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #551
        0x103,
        (
            "#020FWhere are you going?\x01",
            "We need to report to the guildhouse first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2E7")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_E302")

    Return()

    # Function_84_DFF0 end

    def Function_85_E303(): pass

    label("Function_85_E303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E37F")
    EventBegin(0x1)

    ChrTalk(    #552
        0x101,
        (
            "#000FI'm sure Joshua's back home.\x02\x03",

            "I should hurry. Back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #553
        0x142,
        "#1063F(...)\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_E51A")

    label("loc_E37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E51A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3A3")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_E3AA")

    label("loc_E3A3")

    TurnDirection(0x103, 0x0, 400)

    label("loc_E3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_E41B")

    ChrTalk(    #554
        0x103,
        (
            "#020FI'm also curious as to what's going on\x01",
            "out there, but first we need to go to\x01",
            "the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4FF")

    label("loc_E41B")


    ChrTalk(    #555
        0x103,
        (
            "#020FI'm also curious as to what's going on\x01",
            "out there, but first we need to go to\x01",
            "the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4AA")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #556
        0x101,
        "#1000FRight.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E4AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4D5")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #557
        0x105,
        "#040FAll right.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E4D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4FF")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #558
        0x107,
        "#060FAh, okay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_E4FF")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_E51A")

    Return()

    # Function_85_E303 end

    def Function_86_E51B(): pass

    label("Function_86_E51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E600")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E594")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #559
        0x103,
        (
            "#020FThis is no time for side trips.\x01",
            "We need to report to the guildhouse first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5E5")

    label("loc_E594")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #560
        0x103,
        (
            "#020FWhere are you going?\x01",
            "We need to report to the guildhouse first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5E5")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_E600")

    Return()

    # Function_86_E51B end

    def Function_87_E601(): pass

    label("Function_87_E601")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #561
        (
            "\x07\x05《Septian Calendar 1075》\x01",
            "Erected in partnership with the Liberl Royal\x01",
            "Family, Septian Church and Rolent City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #562
        (
            "\x07\x05《Septian Calendar 1192》\x01",
            "Destroyed during the Hundred Days War when Rolent\x01",
            "was bombarded by the Erebonian Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #563
        (
            "\x07\x05《Septian Calendar 1197》\x01",
            "Rebuilt with the cooperation\x01",
            "of the citizens of Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_87_E601 end

    def Function_88_E776(): pass

    label("Function_88_E776")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #564
        "\x07\x05West: Malga Trail Exit\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_88_E776 end

    def Function_89_E7BF(): pass

    label("Function_89_E7BF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #565
        "\x07\x05North: Rolent Landing Port\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_89_E7BF end

    def Function_90_E80C(): pass

    label("Function_90_E80C")

    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Return()

    # Function_90_E80C end

    def Function_91_E830(): pass

    label("Function_91_E830")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E8B7")
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)
    Jump("Function_91_E830")

    label("loc_E8B7")

    Return()

    # Function_91_E830 end

    def Function_92_E8B8(): pass

    label("Function_92_E8B8")

    SetPlaceName(0x4)
    Return()

    # Function_92_E8B8 end

    def Function_93_E8BC(): pass

    label("Function_93_E8BC")

    SetPlaceName(0x2)
    Return()

    # Function_93_E8BC end

    def Function_94_E8C0(): pass

    label("Function_94_E8C0")

    SetPlaceName(0x6)
    Return()

    # Function_94_E8C0 end

    def Function_95_E8C4(): pass

    label("Function_95_E8C4")

    SetPlaceName(0x5)
    Return()

    # Function_95_E8C4 end

    def Function_96_E8C8(): pass

    label("Function_96_E8C8")

    SetPlaceName(0x7)
    Return()

    # Function_96_E8C8 end

    def Function_97_E8CC(): pass

    label("Function_97_E8CC")

    SetPlaceName(0x8)
    Return()

    # Function_97_E8CC end

    def Function_98_E8D0(): pass

    label("Function_98_E8D0")

    SetPlaceName(0x3)
    Return()

    # Function_98_E8D0 end

    def Function_99_E8D4(): pass

    label("Function_99_E8D4")

    SetPlaceName(0xA)
    Return()

    # Function_99_E8D4 end

    SaveToFile()

Try(main)
