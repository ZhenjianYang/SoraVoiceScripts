from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E1110   ._SN',
        MapName             = 'event',
        Location            = 'E1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60170",
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
        'Mysterious Person',                    # 9
        'Conrad',                               # 10
        'Man in Black',                         # 11
        'Man in Black',                         # 12
        'Man in Black',                         # 13
        'Man in Black',                         # 14
        'Man in Black',                         # 15
        'Man in Black',                         # 16
        'Man in Black',                         # 17
        'Man in Black',                         # 18
        'Masked Woman',                         # 19
        'Masked Man',                           # 20
        'Masked Old Man',                       # 21
        'Masked Woman',                         # 22
        'Masked Man',                           # 23
        'Masked Young Man',                     # 24
        'Masked Young Man',                     # 25
        'Masked Gentleman',                     # 26
        'Masked Young Man',                     # 27
        'Masked Man',                           # 28
        'Masked Woman',                         # 29
        'Masked Old Man',                       # 30
        'Masked Man',                           # 31
        'Masked Woman',                         # 32
        'Masked Man',                           # 33
        'Masked Woman',                         # 34
        'Masked Woman',                         # 35
        'Masked Gentleman',                     # 36
        'Masked Old Man',                       # 37
        'Maid',                                 # 38
        'Maid',                                 # 39
        'Waiter',                               # 40
        'Waiter',                               # 41
        'Guest',                                # 42
        'Guest',                                # 43
        'Guest',                                # 44
        'Guest',                                # 45
        'Staff Member',                         # 46
        'Man in Black',                         # 47
        'Man in Black',                         # 48
        'Noble Gentleman',                      # 49
        'Passenger',                            # 50
        'Passenger',                            # 51
        'Masked Young Man',                     # 52
        'Masked Man',                           # 53
        'Dealer',                               # 54
        'Dealer',                               # 55
        'Dealer',                               # 56
        'Dealer',                               # 57
        'Receptionist',                         # 58
        'Man in Black',                         # 59
        'Man in Black',                         # 60
        'Elderly Gentleman',                    # 61
        'Elderly Lady',                         # 62
        'Tea',                                  # 63
        'Tea',                                  # 64
        'Maid',                                 # 65
        'Guest',                                # 66
        'Guest',                                # 67
        'Man in Black',                         # 68
        'Man in Black',                         # 69
        'Man in Black',                         # 70
        'Man in Black',                         # 71
        'Guest',                                # 72
        'Guest',                                # 73
        'Maid',                                 # 74
        'Nielsen',                              # 75
        'Man in Black',                         # 76
        'Man in Black',                         # 77
        'Dummy Character',                      # 78
        'Dummy Character',                      # 79
        'Dummy Character',                      # 80
        'Dummy Character',                      # 81
        'Dummy Character',                      # 82
        'Dummy Character',                      # 83
        'Dummy Character',                      # 84
        'Dummy Character',                      # 85
        'Dummy Character',                      # 86
        'Dummy Character',                      # 87
        'Dummy Character',                      # 88
        'Dummy Character',                      # 89
        'Dummy Character',                      # 90
        'Dummy Character',                      # 91
        'Steel Cougar',                         # 92
        'Steel Cougar',                         # 93
        'Jaeger',                               # 94
        'Jaeger',                               # 95
        'Jaeger',                               # 96
        'Jaeger',                               # 97
        'Jaeger',                               # 98
        'Jaeger',                               # 99
        'Jaeger',                               # 100
        'Jaeger',                               # 101
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02650 ._CH',             # 00
        'ED6_DT07/CH02770 ._CH',             # 01
        'ED6_DT07/CH02880 ._CH',             # 02
        'ED6_DT27/CH03420 ._CH',             # 03
        'ED6_DT27/CH03460 ._CH',             # 04
        'ED6_DT27/CH04420 ._CH',             # 05
        'ED6_DT27/CH04421 ._CH',             # 06
        'ED6_DT27/CH04422 ._CH',             # 07
        'ED6_DT27/CH04423 ._CH',             # 08
        'ED6_DT26/CH20613 ._CH',             # 09
        'ED6_DT27/CH04460 ._CH',             # 0A
        'ED6_DT27/CH04461 ._CH',             # 0B
        'ED6_DT27/CH04462 ._CH',             # 0C
        'ED6_DT27/CH04463 ._CH',             # 0D
        'ED6_DT26/CH20618 ._CH',             # 0E
        'ED6_DT26/CH20603 ._CH',             # 0F
        'ED6_DT26/CH20373 ._CH',             # 10
        'ED6_DT27/CH04080 ._CH',             # 11
        'ED6_DT27/CH04081 ._CH',             # 12
        'ED6_DT27/CH04082 ._CH',             # 13
        'ED6_DT26/CH20604 ._CH',             # 14
        'ED6_DT26/CH20605 ._CH',             # 15
        'ED6_DT27/CH04440 ._CH',             # 16
        'ED6_DT27/CH04441 ._CH',             # 17
        'ED6_DT27/CH04442 ._CH',             # 18
        'ED6_DT07/CH02660 ._CH',             # 19
        'ED6_DT07/CH02840 ._CH',             # 1A
        'ED6_DT07/CH02850 ._CH',             # 1B
        'ED6_DT07/CH02860 ._CH',             # 1C
        'ED6_DT07/CH02870 ._CH',             # 1D
        'ED6_DT07/CH01350 ._CH',             # 1E
        'ED6_DT07/CH01570 ._CH',             # 1F
        'ED6_DT27/CH03930 ._CH',             # 20
        'ED6_DT07/CH01560 ._CH',             # 21
        'ED6_DT29/CH12330 ._CH',             # 22
        'ED6_DT29/CH12331 ._CH',             # 23
        'ED6_DT07/CH01210 ._CH',             # 24
        'ED6_DT07/CH01143 ._CH',             # 25
        'ED6_DT07/CH01493 ._CH',             # 26
        'ED6_DT07/CH01223 ._CH',             # 27
        'ED6_DT07/CH01120 ._CH',             # 28
        'ED6_DT07/CH01140 ._CH',             # 29
        'ED6_DT07/CH01023 ._CH',             # 2A
        'ED6_DT07/CH01040 ._CH',             # 2B
        'ED6_DT07/CH02540 ._CH',             # 2C
        'ED6_DT07/CH01183 ._CH',             # 2D
        'ED6_DT07/CH01060 ._CH',             # 2E
        'ED6_DT07/CH01150 ._CH',             # 2F
        'ED6_DT07/CH01660 ._CH',             # 30
        'ED6_DT07/CH01220 ._CH',             # 31
        'ED6_DT06/CH20020 ._CH',             # 32
    )

    AddCharChipPat(
        'ED6_DT07/CH02650P._CP',             # 00
        'ED6_DT07/CH02770P._CP',             # 01
        'ED6_DT07/CH02880P._CP',             # 02
        'ED6_DT27/CH03420P._CP',             # 03
        'ED6_DT27/CH03460P._CP',             # 04
        'ED6_DT27/CH04420P._CP',             # 05
        'ED6_DT27/CH04421P._CP',             # 06
        'ED6_DT27/CH04422P._CP',             # 07
        'ED6_DT27/CH04423P._CP',             # 08
        'ED6_DT26/CH20613P._CP',             # 09
        'ED6_DT27/CH04460P._CP',             # 0A
        'ED6_DT27/CH04461P._CP',             # 0B
        'ED6_DT27/CH04462P._CP',             # 0C
        'ED6_DT27/CH04463P._CP',             # 0D
        'ED6_DT26/CH20618P._CP',             # 0E
        'ED6_DT26/CH20603P._CP',             # 0F
        'ED6_DT26/CH20373P._CP',             # 10
        'ED6_DT27/CH04080P._CP',             # 11
        'ED6_DT27/CH04081P._CP',             # 12
        'ED6_DT27/CH04082P._CP',             # 13
        'ED6_DT26/CH20604P._CP',             # 14
        'ED6_DT26/CH20605P._CP',             # 15
        'ED6_DT27/CH04440P._CP',             # 16
        'ED6_DT27/CH04441P._CP',             # 17
        'ED6_DT27/CH04442P._CP',             # 18
        'ED6_DT07/CH02660P._CP',             # 19
        'ED6_DT07/CH02840P._CP',             # 1A
        'ED6_DT07/CH02850P._CP',             # 1B
        'ED6_DT07/CH02860P._CP',             # 1C
        'ED6_DT07/CH02870P._CP',             # 1D
        'ED6_DT07/CH01350P._CP',             # 1E
        'ED6_DT07/CH01570P._CP',             # 1F
        'ED6_DT27/CH03930P._CP',             # 20
        'ED6_DT07/CH01560P._CP',             # 21
        'ED6_DT29/CH12330P._CP',             # 22
        'ED6_DT29/CH12331P._CP',             # 23
        'ED6_DT07/CH01210P._CP',             # 24
        'ED6_DT07/CH01143P._CP',             # 25
        'ED6_DT07/CH01493P._CP',             # 26
        'ED6_DT07/CH01223P._CP',             # 27
        'ED6_DT07/CH01120P._CP',             # 28
        'ED6_DT07/CH01140P._CP',             # 29
        'ED6_DT07/CH01023P._CP',             # 2A
        'ED6_DT07/CH01040P._CP',             # 2B
        'ED6_DT07/CH02540P._CP',             # 2C
        'ED6_DT07/CH01183P._CP',             # 2D
        'ED6_DT07/CH01060P._CP',             # 2E
        'ED6_DT07/CH01150P._CP',             # 2F
        'ED6_DT07/CH01660P._CP',             # 30
        'ED6_DT07/CH01220P._CP',             # 31
        'ED6_DT06/CH20020P._CP',             # 32
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
        X                   = -370,
        Z                   = 0,
        Y                   = 21560,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = -2810,
        Z                   = 0,
        Y                   = -390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = -2810,
        Z                   = 0,
        Y                   = -390,
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
        X                   = 2750,
        Z                   = 0,
        Y                   = -420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 2750,
        Z                   = 0,
        Y                   = -420,
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
        X                   = 7000,
        Z                   = 1000,
        Y                   = 21890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 7000,
        Z                   = 1000,
        Y                   = 21890,
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
        X                   = -7950,
        Z                   = 1000,
        Y                   = 22550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = -7950,
        Z                   = 1000,
        Y                   = 22550,
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
        X                   = 6300,
        Z                   = 0,
        Y                   = 13440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = -2620,
        Z                   = 0,
        Y                   = 15940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = -110,
        Z                   = 0,
        Y                   = 18900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 5160,
        Z                   = 0,
        Y                   = 7060,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = -3730,
        Z                   = 0,
        Y                   = 5490,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 59,
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 3830,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 60,
    )

    DeclNpc(
        X                   = 3420,
        Z                   = 0,
        Y                   = 12930,
        Direction           = 80,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 61,
    )

    DeclNpc(
        X                   = 9240,
        Z                   = 0,
        Y                   = 8690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 62,
    )

    DeclNpc(
        X                   = 10750,
        Z                   = 0,
        Y                   = 8690,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 63,
    )

    DeclNpc(
        X                   = 5340,
        Z                   = 0,
        Y                   = 7140,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 64,
    )

    DeclNpc(
        X                   = 3640,
        Z                   = 0,
        Y                   = 6190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 65,
    )

    DeclNpc(
        X                   = -10530,
        Z                   = 0,
        Y                   = 8540,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 66,
    )

    DeclNpc(
        X                   = -11800,
        Z                   = 0,
        Y                   = 9200,
        Direction           = 125,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 67,
    )

    DeclNpc(
        X                   = -6590,
        Z                   = 0,
        Y                   = 14350,
        Direction           = 115,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 68,
    )

    DeclNpc(
        X                   = -5090,
        Z                   = 0,
        Y                   = 13560,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 69,
    )

    DeclNpc(
        X                   = -8260,
        Z                   = 0,
        Y                   = 6010,
        Direction           = 167,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 70,
    )

    DeclNpc(
        X                   = -8390,
        Z                   = 0,
        Y                   = 4210,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 71,
    )

    DeclNpc(
        X                   = -14250,
        Z                   = 0,
        Y                   = 2670,
        Direction           = 181,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 73,
    )

    DeclNpc(
        X                   = 8310,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 74,
    )

    DeclNpc(
        X                   = -5030,
        Z                   = 0,
        Y                   = 8760,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 75,
    )

    DeclNpc(
        X                   = -9430,
        Z                   = 0,
        Y                   = 13630,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 76,
    )

    DeclNpc(
        X                   = 14280,
        Z                   = 0,
        Y                   = 2410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 77,
    )

    DeclNpc(
        X                   = -14030,
        Z                   = 0,
        Y                   = -70,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 78,
    )

    DeclNpc(
        X                   = -58040,
        Z                   = 0,
        Y                   = -26840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 79,
    )

    DeclNpc(
        X                   = -60670,
        Z                   = 350,
        Y                   = -36890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 80,
    )

    DeclNpc(
        X                   = -60620,
        Z                   = 250,
        Y                   = -39170,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 81,
    )

    DeclNpc(
        X                   = -53910,
        Z                   = 300,
        Y                   = -45800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 82,
    )

    DeclNpc(
        X                   = -51030,
        Z                   = 20,
        Y                   = -40450,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 83,
    )

    DeclNpc(
        X                   = -50920,
        Z                   = 0,
        Y                   = -27420,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 84,
    )

    DeclNpc(
        X                   = -50920,
        Z                   = 0,
        Y                   = -27420,
        Direction           = 225,
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
        X                   = -59640,
        Z                   = 0,
        Y                   = -118280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 85,
    )

    DeclNpc(
        X                   = -54670,
        Z                   = 0,
        Y                   = -110110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 86,
    )

    DeclNpc(
        X                   = -51170,
        Z                   = 300,
        Y                   = -126580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 87,
    )

    DeclNpc(
        X                   = -58300,
        Z                   = 0,
        Y                   = -123940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 88,
    )

    DeclNpc(
        X                   = -56940,
        Z                   = 0,
        Y                   = -112010,
        Direction           = 284,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 89,
    )

    DeclNpc(
        X                   = -60310,
        Z                   = 0,
        Y                   = -111770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 90,
    )

    DeclNpc(
        X                   = -58240,
        Z                   = 0,
        Y                   = -121360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 91,
    )

    DeclNpc(
        X                   = -58520,
        Z                   = 0,
        Y                   = -128880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 92,
    )

    DeclNpc(
        X                   = -51630,
        Z                   = 0,
        Y                   = -110280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 93,
    )

    DeclNpc(
        X                   = -51660,
        Z                   = 0,
        Y                   = -120900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 94,
    )

    DeclNpc(
        X                   = -61170,
        Z                   = 0,
        Y                   = -115150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 95,
    )

    DeclNpc(
        X                   = -61170,
        Z                   = 0,
        Y                   = -115150,
        Direction           = 90,
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
        X                   = 80880,
        Z                   = 300,
        Y                   = -35450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 96,
    )

    DeclNpc(
        X                   = 82600,
        Z                   = 300,
        Y                   = -37010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 97,
    )

    DeclNpc(
        X                   = 81900,
        Z                   = 650,
        Y                   = -37000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638450,
        ChipIndex           = 0x32,
        NpcIndex            = 0x167,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81000,
        Z                   = 650,
        Y                   = -36100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638450,
        ChipIndex           = 0x32,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 85160,
        Z                   = 20,
        Y                   = -72010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 98,
    )

    DeclNpc(
        X                   = 79610,
        Z                   = 0,
        Y                   = -110650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 99,
    )

    DeclNpc(
        X                   = 79590,
        Z                   = 0,
        Y                   = -112460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 100,
    )

    DeclNpc(
        X                   = 1940,
        Z                   = 0,
        Y                   = -85780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 104,
    )

    DeclNpc(
        X                   = 1940,
        Z                   = 0,
        Y                   = -85780,
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
        X                   = 84380,
        Z                   = 0,
        Y                   = -168870,
        Direction           = 222,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 105,
    )

    DeclNpc(
        X                   = 84380,
        Z                   = 0,
        Y                   = -168870,
        Direction           = 222,
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
        X                   = 3460,
        Z                   = 0,
        Y                   = -198800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 102,
    )

    DeclNpc(
        X                   = 5030,
        Z                   = 0,
        Y                   = -198760,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 103,
    )

    DeclNpc(
        X                   = 3060,
        Z                   = 0,
        Y                   = -132830,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 101,
    )

    DeclNpc(
        X                   = 92200,
        Z                   = 0,
        Y                   = -175500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 106,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 1800,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 1800,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = -139810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2580,
        Z                   = 0,
        Y                   = -138900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = -140260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2520,
        Z                   = 0,
        Y                   = -139340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2530,
        Z                   = 0,
        Y                   = -137270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3450,
        Z                   = 0,
        Y                   = -137000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2020,
        Z                   = 0,
        Y                   = -137880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2920,
        Z                   = 0,
        Y                   = -137420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
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
        Unknown3            = 34,
        ChipIndex           = 0x22,
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
        Unknown3            = 34,
        ChipIndex           = 0x22,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5500,
        Y                   = -1000,
        Z                   = -143000,
        Range               = 6000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFDDD20,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -5500,
        Y                   = -1000,
        Z                   = -103000,
        Range               = 6000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFE7960,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = -380,
        Y                   = 0,
        Z                   = 20340,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = -380,
        Y                   = 0,
        Z                   = 20340,
        Range               = 2000,
        Unknown_10          = 0x640,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 53,
    )

    DeclEvent(
        X                   = -2500,
        Y                   = -1000,
        Z                   = -209500,
        Range               = 2500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFCC7C8,
        Unknown_18          = 0x0,
        Unknown_1C          = 110,
    )

    DeclEvent(
        X                   = 77000,
        Y                   = -1000,
        Z                   = -161500,
        Range               = 83000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFD92E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 111,
    )


    DeclActor(
        TriggerX            = 5020,
        TriggerZ            = 0,
        TriggerY            = -96990,
        TriggerRange        = 500,
        ActorX              = 5020,
        ActorZ              = 1000,
        ActorY              = -96990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5060,
        TriggerZ            = 0,
        TriggerY            = -120950,
        TriggerRange        = 500,
        ActorX              = 5060,
        ActorZ              = 1000,
        ActorY              = -120950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5050,
        TriggerZ            = 0,
        TriggerY            = -144940,
        TriggerRange        = 500,
        ActorX              = 5050,
        ActorZ              = 1000,
        ActorY              = -144940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85860,
        TriggerZ            = 0,
        TriggerY            = -27250,
        TriggerRange        = 1000,
        ActorX              = 85860,
        ActorZ              = 1000,
        ActorY              = -27250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86100,
        TriggerZ            = 0,
        TriggerY            = -78920,
        TriggerRange        = 1000,
        ActorX              = 86100,
        ActorZ              = 1000,
        ActorY              = -78920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 83290,
        TriggerZ            = 0,
        TriggerY            = -106000,
        TriggerRange        = 1000,
        ActorX              = 83290,
        ActorZ              = 1000,
        ActorY              = -106000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84750,
        TriggerZ            = 0,
        TriggerY            = -106000,
        TriggerRange        = 1000,
        ActorX              = 84750,
        ActorZ              = 1000,
        ActorY              = -106000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -52700,
        TriggerZ            = 0,
        TriggerY            = -121000,
        TriggerRange        = 800,
        ActorX              = -51660,
        ActorZ              = 1500,
        ActorY              = -120900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 94,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12500,
        TriggerZ            = 0,
        TriggerY            = 2410,
        TriggerRange        = 500,
        ActorX              = 14280,
        ActorZ              = 1500,
        ActorY              = 2410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 77,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 92500,
        TriggerZ            = 0,
        TriggerY            = -175750,
        TriggerRange        = 500,
        ActorX              = 92500,
        ActorZ              = 1000,
        ActorY              = -175750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53840,
        TriggerZ            = 0,
        TriggerY            = -25950,
        TriggerRange        = 500,
        ActorX              = -53840,
        ActorZ              = 1000,
        ActorY              = -25950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 112,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_102E",         # 00, 0
        "Function_1_120C",         # 01, 1
        "Function_2_12BD",         # 02, 2
        "Function_3_1444",         # 03, 3
        "Function_4_158E",         # 04, 4
        "Function_5_16A9",         # 05, 5
        "Function_6_17C4",         # 06, 6
        "Function_7_1941",         # 07, 7
        "Function_8_1965",         # 08, 8
        "Function_9_318C",         # 09, 9
        "Function_10_3265",        # 0A, 10
        "Function_11_3292",        # 0B, 11
        "Function_12_32B9",        # 0C, 12
        "Function_13_3437",        # 0D, 13
        "Function_14_36D5",        # 0E, 14
        "Function_15_3710",        # 0F, 15
        "Function_16_371C",        # 10, 16
        "Function_17_3C00",        # 11, 17
        "Function_18_40E4",        # 12, 18
        "Function_19_4510",        # 13, 19
        "Function_20_4573",        # 14, 20
        "Function_21_45DB",        # 15, 21
        "Function_22_461A",        # 16, 22
        "Function_23_4659",        # 17, 23
        "Function_24_4C22",        # 18, 24
        "Function_25_4C43",        # 19, 25
        "Function_26_50D1",        # 1A, 26
        "Function_27_6B2B",        # 1B, 27
        "Function_28_6B7B",        # 1C, 28
        "Function_29_6B9F",        # 1D, 29
        "Function_30_6BC3",        # 1E, 30
        "Function_31_6BE7",        # 1F, 31
        "Function_32_6C0B",        # 20, 32
        "Function_33_6C2F",        # 21, 33
        "Function_34_6C53",        # 22, 34
        "Function_35_6C77",        # 23, 35
        "Function_36_6C9B",        # 24, 36
        "Function_37_6CC0",        # 25, 37
        "Function_38_6CE5",        # 26, 38
        "Function_39_6D0A",        # 27, 39
        "Function_40_6D2F",        # 28, 40
        "Function_41_6D54",        # 29, 41
        "Function_42_6D69",        # 2A, 42
        "Function_43_6D7E",        # 2B, 43
        "Function_44_6D93",        # 2C, 44
        "Function_45_6E4E",        # 2D, 45
        "Function_46_6F42",        # 2E, 46
        "Function_47_7036",        # 2F, 47
        "Function_48_7497",        # 30, 48
        "Function_49_74D2",        # 31, 49
        "Function_50_7558",        # 32, 50
        "Function_51_75C7",        # 33, 51
        "Function_52_775D",        # 34, 52
        "Function_53_776A",        # 35, 53
        "Function_54_7B23",        # 36, 54
        "Function_55_7C08",        # 37, 55
        "Function_56_7DF6",        # 38, 56
        "Function_57_7EEB",        # 39, 57
        "Function_58_801E",        # 3A, 58
        "Function_59_80BD",        # 3B, 59
        "Function_60_828E",        # 3C, 60
        "Function_61_8444",        # 3D, 61
        "Function_62_851C",        # 3E, 62
        "Function_63_865E",        # 3F, 63
        "Function_64_8775",        # 40, 64
        "Function_65_8924",        # 41, 65
        "Function_66_8AA5",        # 42, 66
        "Function_67_8C92",        # 43, 67
        "Function_68_8EBF",        # 44, 68
        "Function_69_90D1",        # 45, 69
        "Function_70_9336",        # 46, 70
        "Function_71_95A1",        # 47, 71
        "Function_72_96AE",        # 48, 72
        "Function_73_96B5",        # 49, 73
        "Function_74_985C",        # 4A, 74
        "Function_75_9A1D",        # 4B, 75
        "Function_76_9B67",        # 4C, 76
        "Function_77_9CD7",        # 4D, 77
        "Function_78_9DD3",        # 4E, 78
        "Function_79_9F17",        # 4F, 79
        "Function_80_A08D",        # 50, 80
        "Function_81_A294",        # 51, 81
        "Function_82_A502",        # 52, 82
        "Function_83_A678",        # 53, 83
        "Function_84_A7B7",        # 54, 84
        "Function_85_A7FD",        # 55, 85
        "Function_86_AA09",        # 56, 86
        "Function_87_AAE5",        # 57, 87
        "Function_88_ACAC",        # 58, 88
        "Function_89_AD88",        # 59, 89
        "Function_90_AF36",        # 5A, 90
        "Function_91_AFFB",        # 5B, 91
        "Function_92_B107",        # 5C, 92
        "Function_93_B1E0",        # 5D, 93
        "Function_94_B2A2",        # 5E, 94
        "Function_95_B435",        # 5F, 95
        "Function_96_B490",        # 60, 96
        "Function_97_B5E0",        # 61, 97
        "Function_98_B71A",        # 62, 98
        "Function_99_B8F2",        # 63, 99
        "Function_100_BB0B",       # 64, 100
        "Function_101_BBB8",       # 65, 101
        "Function_102_BDAC",       # 66, 102
        "Function_103_BF52",       # 67, 103
        "Function_104_C049",       # 68, 104
        "Function_105_C259",       # 69, 105
        "Function_106_C36F",       # 6A, 106
        "Function_107_C4ED",       # 6B, 107
        "Function_108_C545",       # 6C, 108
        "Function_109_C5BF",       # 6D, 109
        "Function_110_C639",       # 6E, 110
        "Function_111_C6EC",       # 6F, 111
        "Function_112_C86A",       # 70, 112
    )


    def Function_0_102E(): pass

    label("Function_0_102E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104F")
    Event(0, 16)

    label("loc_104F")

    Jump("loc_1073")

    label("loc_1052")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1073")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1073")
    Event(0, 17)

    label("loc_1073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1084")
    OP_A3(0x2506)
    Event(0, 47)
    Jump("loc_10AB")

    label("loc_1084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1095")
    OP_A3(0x2505)
    Event(0, 26)
    Jump("loc_10AB")

    label("loc_1095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_10AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AB")
    OP_A3(0x2504)
    Event(0, 8)

    label("loc_10AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 0)), scpexpr(EXPR_END)), "loc_1196")
    OP_8C(0x1B, 0, 0)
    OP_8C(0x1C, 270, 0)
    OP_8C(0x1D, 225, 0)
    OP_8C(0x1E, 270, 0)
    OP_8C(0x1F, 360, 0)
    OP_8C(0x20, 0, 0)
    OP_8C(0x21, 90, 0)
    OP_8C(0x22, 270, 0)
    OP_8C(0x23, 180, 0)
    OP_8C(0x24, 0, 0)
    OP_8C(0x25, 270, 0)
    OP_8C(0x26, 135, 0)
    OP_8C(0x27, 115, 0)
    OP_8C(0x28, 270, 0)
    OP_8C(0x29, 180, 0)
    OP_8C(0x2A, 360, 0)
    OP_8C(0x2B, 180, 0)
    OP_8C(0x2C, 270, 0)
    SetChrPos(0x11, -370, 0, 21560, 180)
    SetChrPos(0x1B, -110, 0, 18900, 0)
    SetChrPos(0x1C, -1300, 0, 19540, 0)
    SetChrPos(0x1D, 870, 0, 20420, 270)
    SetChrPos(0x20, 3700, 0, 13120, 91)
    SetChrPos(0x23, 3670, 0, 7920, 180)

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_11CF")
    SetChrFlags(0x4D, 0x80)
    SetChrFlags(0x4B, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x44, 0x80)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x52, 0x80)

    label("loc_11CF")

    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_43(0x16, 0x0, 0x0, 0x6)
    OP_43(0x18, 0x0, 0x0, 0x6)
    OP_43(0x42, 0x0, 0x0, 0x6)
    OP_43(0x4D, 0x0, 0x0, 0x6)
    OP_43(0x36, 0x0, 0x0, 0x6)
    OP_43(0x4B, 0x0, 0x0, 0x6)
    Call(0, 25)
    Return()

    # Function_0_102E end

    def Function_1_120C(): pass

    label("Function_1_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_1221")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_1221")

    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x4, 0x0, 0x6C)
    OP_1B(0x5, 0x0, 0x6D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_124C")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_1258")

    label("loc_124C")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126A")
    OP_6F(0xB, 0)
    Jump("loc_1271")

    label("loc_126A")

    OP_6F(0xB, 60)

    label("loc_1271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1283")
    OP_6F(0xC, 0)
    Jump("loc_128A")

    label("loc_1283")

    OP_6F(0xC, 60)

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129C")
    OP_6F(0xD, 0)
    Jump("loc_12A3")

    label("loc_129C")

    OP_6F(0xD, 60)

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B5")
    OP_6F(0xE, 0)
    Jump("loc_12BC")

    label("loc_12B5")

    OP_6F(0xE, 60)

    label("loc_12BC")

    Return()

    # Function_1_120C end

    def Function_2_12BD(): pass

    label("Function_2_12BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_132B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25F8)
    Jump("loc_1393")

    label("loc_132B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_1393")

    Jump("loc_1436")

    label("loc_1396")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05The treasure chest reveals itself to be a crafty mimic, and licks your\x01",
            "unsuspecting hand. Better break out the disinfectant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x14, 0x0)

    label("loc_1436")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_12BD end

    def Function_3_1444(): pass

    label("Function_3_1444")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_14B2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xFE\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25F9)
    Jump("loc_151A")

    label("loc_14B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xFE\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFE\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_151A")

    Jump("loc_1580")

    label("loc_151D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05The message: Remember, there is but one truth: Love is ETERNAL.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x15, 0x0)

    label("loc_1580")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1444 end

    def Function_4_158E(): pass

    label("Function_4_158E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1667")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_15FC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25FA)
    Jump("loc_1664")

    label("loc_15FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1664")

    Jump("loc_169B")

    label("loc_1667")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Mmm. Pine fresh!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x16, 0x0)

    label("loc_169B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_158E end

    def Function_5_16A9(): pass

    label("Function_5_16A9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1782")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1717")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\xFE\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25FB)
    Jump("loc_177F")

    label("loc_1717")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\xFE\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFE\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_177F")

    Jump("loc_17B6")

    label("loc_1782")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05We need to talk.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x17, 0x0)

    label("loc_17B6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16A9 end

    def Function_6_17C4(): pass

    label("Function_6_17C4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E9")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_192B")

    label("loc_17E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1802")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_192B")

    label("loc_1802")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_192B")

    label("loc_181B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1834")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_192B")

    label("loc_1834")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_192B")

    label("loc_184D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1866")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_192B")

    label("loc_1866")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_192B")

    label("loc_187F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1898")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_192B")

    label("loc_1898")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B1")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_192B")

    label("loc_18B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18CA")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_192B")

    label("loc_18CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E3")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_192B")

    label("loc_18E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_192B")

    label("loc_18FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1915")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_192B")

    label("loc_1915")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_192B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1940")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_192B")

    label("loc_1940")

    Return()

    # Function_6_17C4 end

    def Function_7_1941(): pass

    label("Function_7_1941")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1964")
    OP_8D(0xFE, 1950, -130840, 3370, -135280, 2000)
    Jump("Function_7_1941")

    label("loc_1964")

    Return()

    # Function_7_1941 end

    def Function_8_1965(): pass

    label("Function_8_1965")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    SetChrPos(0x109, 14170, 0, 16810, 270)
    SetChrPos(0x1A, 13860, 0, 12730, 270)
    SetChrPos(0x1B, 11840, 0, 2410, 90)
    SetChrPos(0x1C, 3340, 0, 12270, 90)
    SetChrPos(0x20, -3460, 0, 14470, 315)
    SetChrPos(0x23, 3450, 0, 14610, 45)
    OP_8C(0x24, 45, 0)
    OP_4A(0x12, 0)
    OP_4A(0x14, 0)
    OP_4A(0x16, 0)
    OP_4A(0x18, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    OP_4A(0x28, 0)
    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    OP_4A(0x2D, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x30, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -250, 0, -2840, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-3910, 3570, 1000, 0)
    OP_6C(45000, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(1400, 0)
    OP_6E(628, 0)

    def lambda_1AB3():
        OP_6D(-2710, 3570, 23290, 20000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1AB3)

    def lambda_1ACB():
        OP_6C(33000, 20000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1ACB)
    OP_43(0x11, 0x0, 0x0, 0xB)
    OP_22(0xEA, 0x1, 0x64)
    OP_43(0x11, 0x3, 0x0, 0xC)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_1B42():

        label("loc_1B42")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B42")

    QueueWorkItem2(0x1E, 1, lambda_1B42)
    Sleep(200)

    def lambda_1B58():

        label("loc_1B58")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B58")

    QueueWorkItem2(0x1F, 1, lambda_1B58)
    Sleep(600)

    def lambda_1B6E():

        label("loc_1B6E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B6E")

    QueueWorkItem2(0x1D, 1, lambda_1B6E)
    Sleep(100)

    def lambda_1B84():

        label("loc_1B84")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B84")

    QueueWorkItem2(0x24, 1, lambda_1B84)
    Sleep(600)

    def lambda_1B9A():

        label("loc_1B9A")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B9A")

    QueueWorkItem2(0x23, 1, lambda_1B9A)
    Sleep(100)

    def lambda_1BB0():

        label("loc_1BB0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BB0")

    QueueWorkItem2(0x29, 1, lambda_1BB0)
    Sleep(100)

    def lambda_1BC6():

        label("loc_1BC6")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BC6")

    QueueWorkItem2(0x2A, 1, lambda_1BC6)
    Sleep(100)

    def lambda_1BDC():

        label("loc_1BDC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BDC")

    QueueWorkItem2(0x20, 1, lambda_1BDC)
    Sleep(100)

    def lambda_1BF2():

        label("loc_1BF2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BF2")

    QueueWorkItem2(0x1C, 1, lambda_1BF2)
    Sleep(100)

    def lambda_1C08():

        label("loc_1C08")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C08")

    QueueWorkItem2(0x21, 1, lambda_1C08)
    Sleep(100)

    def lambda_1C1E():

        label("loc_1C1E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C1E")

    QueueWorkItem2(0x22, 1, lambda_1C1E)
    Sleep(100)

    def lambda_1C34():

        label("loc_1C34")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C34")

    QueueWorkItem2(0x1B, 1, lambda_1C34)
    Sleep(200)

    def lambda_1C4A():

        label("loc_1C4A")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C4A")

    QueueWorkItem2(0x25, 1, lambda_1C4A)
    Sleep(100)

    def lambda_1C60():

        label("loc_1C60")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C60")

    QueueWorkItem2(0x26, 1, lambda_1C60)
    Sleep(100)

    def lambda_1C76():

        label("loc_1C76")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C76")

    QueueWorkItem2(0x27, 1, lambda_1C76)
    Sleep(100)

    def lambda_1C8C():

        label("loc_1C8C")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C8C")

    QueueWorkItem2(0x28, 1, lambda_1C8C)
    Sleep(100)

    def lambda_1CA2():

        label("loc_1CA2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1CA2")

    QueueWorkItem2(0x2B, 1, lambda_1CA2)
    Sleep(100)

    def lambda_1CB8():

        label("loc_1CB8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1CB8")

    QueueWorkItem2(0x2C, 1, lambda_1CB8)
    Sleep(1000)

    def lambda_1CCE():
        OP_8E(0xFE, 0x7B2, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1CCE)
    Sleep(200)

    def lambda_1CEE():
        OP_8E(0xFE, 0x8AC, 0x0, 0x2FA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1CEE)
    WaitChrThread(0x1C, 0x1)
    WaitChrThread(0x23, 0x1)
    WaitChrThread(0x11, 0x0)
    OP_8C(0x11, 90, 400)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(300)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_43(0x11, 0x0, 0x0, 0xA)

    def lambda_1D6B():

        label("loc_1D6B")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1D6B")

    QueueWorkItem2(0x23, 2, lambda_1D6B)

    def lambda_1D7C():

        label("loc_1D7C")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1D7C")

    QueueWorkItem2(0x1C, 2, lambda_1D7C)
    Sleep(3500)
    Fade(1000)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_6D(1000, 1070, 29960, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(326, 0)
    OP_23(0xEA)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x11, 0x0)

    NpcTalk(    #12
        0x11,
        "Host",
        "#5P*cough* If I may have your attention, please...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x11,
        "Host",
        (
            "#5POn behalf of the Conrad Company,\x01",
            "I would like to take the time to thank\x01",
            "you all for attending this party today.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x11,
        "Host",
        (
            "#5PAs I'm sure you're all aware, this is a most \x01",
            "auspicious day...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EF9():
        OP_6D(14860, 0, 17520, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EF9)

    def lambda_1F11():
        OP_67(0, 5000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F11)

    def lambda_1F29():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1F29)
    Sleep(4000)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("Host")

    AnonymousTalk(    #15
        (
            "\x07\x00Yes, indeed!\x02\x03",

            "#4POn this historic day ten years ago, this fine \x01",
            "company...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x1A, 0, 400)
    Sleep(500)

    def lambda_1FE5():
        OP_6D(14860, 0, 18520, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FE5)
    OP_8F(0x1A, 0x36BA, 0x0, 0x3D2C, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(14920, 0, 15780, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(135000, 0)
    OP_6E(480, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x1A,
        (
            "#11PTeehee. You don't seem to be enjoying this\x01",
            "quite as much as he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1A,
        (
            "#11PYou ought to at least try and feign interest\x01",
            "in what he's saying, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x1A,
        (
            "#11PSurely you must understand what kind of man\x01",
            "he is if you're here?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(1000, 1070, 29960, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(326, 0)
    OP_0D()
    Sleep(500)
    OP_43(0x11, 0x0, 0x0, 0x9)
    Sleep(500)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("Masked Man")

    AnonymousTalk(    #19
        (
            "\x07\x00#1600FOh, that I do.\x02\x03",

            "He's a merchant of death who made a fortune during\x01",
            "the Hundred Days War--and one of the Empire's most\x01",
            "wealthy men, despite being a relative newcomer.\x02\x03",

            "Why, it was only a few years ago that he partnered up\x01",
            "with the famous Reinford Group, and now he's serving\x01",
            "on their board of directors!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    Fade(500)
    OP_6D(14920, 0, 15780, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(135000, 0)
    OP_6E(480, 0)
    OP_0D()
    Sleep(500)
    OP_44(0x11, 0x0)

    NpcTalk(    #20
        0x109,
        "Masked Man",
        (
            "#1600F#6PHis record makes for a most impressive read, that\x01",
            "much is for certain.\x02\x03",

            "...Although, I dare say he's less impressive in person\x01",
            "compared to on paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x1A,
        (
            "#11PMy, my! You'd best refrain from making such\x01",
            "remarks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1A,
        (
            "#11PThat mask of yours may disguise your identity,\x01",
            "but it won't keep those naughty men in black\x01",
            "away should you make an enemy of them.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0x109,
        "Masked Man",
        (
            "#1600F#6PNow, that's a terrifying prospect.\x02\x03",

            "I can't imagine I'd last very long if I did.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    NpcTalk(    #24
        0x109,
        "Masked Man",
        (
            "#1603F#6PI'd surely be cast through this window as\x01",
            "easily as a pebble plunges through water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1A,
        "#11PHmm... I must say, I find you rather intriguing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1A,
        (
            "#11PAre you a member of the press, perhaps?\x01",
            "Or maybe even a government official?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 190, 400)

    NpcTalk(    #27
        0x109,
        "Masked Man",
        (
            "#1600F#6PI would answer, but where's the fun in spilling\x01",
            "secrets? I'll leave the pondering to your fertile\x01",
            "imagination, mademoiselle.\x02\x03",

            "Leaving my identity aside, however...this ship\x01",
            "is an impressive work of art.\x02\x03",

            "It's hard to believe we're inside one at all, and\x01",
            "yet here we are, thousands of arge in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x1A,
        (
            "#11PWell, it is Reinford's latest model. One would\x01",
            "expect nothing less than art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1A,
        (
            "#11PLast I heard, they were advertising it as the\x01",
            "largest airship in the world.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #30
        0x109,
        "Masked Man",
        (
            "#1600F#6PIt IS 120 arge across, so they're probably right.\x02\x03",

            "#1601F...As far as most of the world knows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1A,
        (
            "#11PHeehee. You certainly know how to make a lady\x01",
            "curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1A,
        (
            "#11PBut even with the mask, it's no secret that you're\x01",
            "so young. Practically still a boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1A,
        (
            "#11PI wonder, how often do you go around charming\x01",
            "your way through these drab parties with that\x01",
            "aura of mystique?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #34
        0x109,
        "Masked Man",
        (
            "#1603F#6PWell, well! Seems the mask can't hide ALL my\x01",
            "secrets.\x02\x03",

            "#1600FPerhaps I ought to make my daring escape before\x01",
            "I give away anything more about myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1A,
        (
            "#11PIf you must, although it would be my pleasure to\x01",
            "continue keeping you company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x1A,
        (
            "#11PIt's not every day that one gets to enjoy chatting\x01",
            "the night away with a mysterious stranger like this,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B3B():
        OP_6B(1400, 2200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2B3B)
    SetChrFlags(0x1A, 0x40)
    OP_8F(0x1A, 0x36BA, 0x0, 0x401A, 0x1F4, 0x0)
    WaitChrThread(0x109, 0x2)
    Sleep(500)

    ChrTalk(    #37
        0x1A,
        (
            "#11PWe could even take our chat somewhere more...\x01",
            "comfortable. Like your room?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x109,
        "Masked Man",
        (
            "#1600F#6PHaha... I would be honored to, fair lady.\x02\x03",

            "But only if you can promise the Goddess has\x01",
            "Her eyes turned away; She may blush if She's\x01",
            "watching.\x02\x03",

            "#1601FMeanwhile, I'll refrain from asking why your\x01",
            "room would not be an acceptable location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1A,
        (
            "#11PAnd I'll thank you for not forcing me to bring\x01",
            "up that oaf of a man.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8F(0x109, 0x33CC, 0x0, 0x4164, 0x3E8, 0x0)
    Fade(500)
    OP_6D(13500, 0, 16790, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)
    OP_0D()
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x24, 0x1)
    OP_44(0x1B, 0x2)
    OP_44(0x23, 0x2)
    OP_44(0x25, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x27, 0x1)
    OP_44(0x28, 0x1)
    OP_44(0x29, 0x1)
    OP_44(0x2A, 0x1)
    OP_44(0x2B, 0x1)
    OP_44(0x2C, 0x1)
    OP_8C(0x1B, 0, 0)
    OP_8C(0x1C, 270, 0)
    OP_8C(0x1D, 225, 0)
    OP_8C(0x1E, 270, 0)
    OP_8C(0x1F, 360, 0)
    OP_8C(0x20, 0, 0)
    OP_8C(0x21, 90, 0)
    OP_8C(0x22, 270, 0)
    OP_8C(0x23, 180, 0)
    OP_8C(0x24, 0, 0)
    OP_8C(0x25, 270, 0)
    OP_8C(0x26, 135, 0)
    OP_8C(0x27, 115, 0)
    OP_8C(0x28, 270, 0)
    OP_8C(0x29, 180, 0)
    OP_8C(0x2A, 360, 0)
    OP_8C(0x2B, 180, 0)
    OP_8C(0x2C, 270, 0)
    SetChrPos(0x11, -370, 0, 21560, 180)
    SetChrPos(0x1B, -110, 0, 18900, 0)
    SetChrPos(0x1C, -1300, 0, 19540, 0)
    SetChrPos(0x1D, 870, 0, 20420, 270)
    SetChrPos(0x20, 3700, 0, 13120, 91)
    SetChrPos(0x23, 3670, 0, 7920, 180)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x1B, 0x0, 0x0, 0x9)
    OP_43(0x1C, 0x0, 0x0, 0x9)
    OP_43(0x1D, 0x0, 0x0, 0x9)

    def lambda_2EC1():

        label("loc_2EC1")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_2EC1")

    QueueWorkItem2(0x1A, 0, lambda_2EC1)

    def lambda_2ED2():
        OP_8F(0xFE, 0x3430, 0x0, 0x38E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2ED2)
    Sleep(500)

    def lambda_2EF2():
        OP_6D(11220, 0, 4480, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EF2)
    WaitChrThread(0x109, 0x1)
    OP_8E(0x109, 0x283C, 0x0, 0xDFC, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0x109, 0, 400)
    Fade(500)
    OP_6D(760, 0, 21620, 0)
    OP_67(0, 5970, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    OP_0D()
    SetChrPos(0x109, 900, 0, 9460, 0)
    Sleep(1000)

    NpcTalk(    #40
        0x109,
        "Masked Man",
        (
            "#1602F#5P(Well, the party's in full swing now...\x01",
            "This chance is as good as any.)\x02\x03",

            "(His private room's on the highest floor of\x01",
            "the ship and on the other side of the deck.)\x02\x03",

            "#1601F(Okay... Let's get to work.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(10300, 0, 3580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 10300, 0, 3580, 0)
    OP_0D()
    OP_44(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 6300, 0, 13440, 270)
    OP_44(0x11, 0x0)
    OP_44(0x1B, 0x0)
    OP_44(0x1C, 0x0)
    OP_44(0x1D, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x6)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    OP_43(0x1B, 0x0, 0x0, 0x6)
    OP_43(0x1C, 0x0, 0x0, 0x6)
    OP_43(0x1D, 0x0, 0x0, 0x6)
    OP_4B(0x11, 0)
    OP_4B(0x12, 0)
    OP_4B(0x14, 0)
    OP_4B(0x16, 0)
    OP_4B(0x18, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x20, 0)
    OP_4B(0x21, 0)
    OP_4B(0x22, 0)
    OP_4B(0x23, 0)
    OP_4B(0x24, 0)
    OP_4B(0x25, 0)
    OP_4B(0x26, 0)
    OP_4B(0x27, 0)
    OP_4B(0x28, 0)
    OP_4B(0x29, 0)
    OP_4B(0x2A, 0)
    OP_4B(0x2B, 0)
    OP_4B(0x2C, 0)
    OP_4B(0x2D, 0)
    OP_4B(0x2E, 0)
    OP_4B(0x2F, 0)
    OP_4B(0x30, 0)
    OP_A2(0x25E0)
    OP_3F(0x590, 1)
    OP_3F(0x591, 1)
    OP_3F(0x12F, 1)
    EventEnd(0x0)
    Return()

    # Function_8_1965 end

    def Function_9_318C(): pass

    label("Function_9_318C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3264")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C8")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3261")

    label("loc_31C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31EF")
    Sleep(1500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3261")

    label("loc_31EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3216")
    Sleep(2000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3261")

    label("loc_3216")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323D")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3261")

    label("loc_323D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3261")
    Sleep(3000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_3261")

    Jump("Function_9_318C")

    label("loc_3264")

    Return()

    # Function_9_318C end

    def Function_10_3265(): pass

    label("Function_10_3265")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x0, 0x42E, 0x7148, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    Return()

    # Function_10_3265 end

    def Function_11_3292(): pass

    label("Function_11_3292")


    def lambda_3298():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3298)
    OP_8E(0xFE, 0x28, 0x0, 0x3084, 0x7D0, 0x0)
    Return()

    # Function_11_3292 end

    def Function_12_32B9(): pass

    label("Function_12_32B9")

    Sleep(3000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS533._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS533._CH")
    OP_C6(0x0, 0x3, -1996488705, 1500, 0)
    OP_C6(0x1, 0x3, -1996488705, 1500, 0)
    Sleep(3000)
    OP_C6(0x0, 0x0, 100000, 0, 2500)
    OP_C6(0x1, 0x0, -100000, 0, 2500)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(4000)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS534._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS534._CH")
    OP_C6(0x2, 0x3, -1996488705, 1500, 0)
    OP_C6(0x3, 0x3, -1996488705, 1500, 0)
    Sleep(3000)
    OP_C6(0x2, 0x0, 100000, 0, 2500)
    OP_C6(0x3, 0x0, -100000, 0, 2500)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    Return()

    # Function_12_32B9 end

    def Function_13_3437(): pass

    label("Function_13_3437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 1)), scpexpr(EXPR_END)), "loc_3448")
    NewScene("ED6_DT21/E1110   ._SN", 101, 1, 0)
    IdleLoop()
    Return()

    label("loc_3448")

    EventBegin(0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 12000, 180)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 0, 400)
    Fade(500)
    OP_6D(-80, 0, 5270, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(1260, 0)
    OP_6C(0, 0)
    OP_6E(590, 0)
    SetChrPos(0x109, 0, 0, 1270, 0)

    def lambda_34DC():
        OP_6D(0, 0, 13110, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34DC)

    def lambda_34F4():
        OP_67(0, 4480, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_34F4)
    OP_43(0x10, 0x0, 0x0, 0xF)
    Sleep(4000)

    NpcTalk(    #41
        0x109,
        "Masked Man",
        (
            "#1602F#5P(...)\x02\x03",

            "(Strange... Felt like someone was watching\x01",
            "me for a minute.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #42
        0x109,
        "Masked Man",
        "#1600F#5P(...Ahhh, forget it. I've got work to do.)\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(630, 0, 2000, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(44000, 0)
    OP_6E(285, 0)
    OP_0D()
    OP_8C(0x109, 180, 400)
    Sleep(500)

    NpcTalk(    #43
        0x109,
        "Masked Man",
        (
            "#1601F#5P(His private room's on the highest floor\x01",
            "of the ship, on the other side of the deck.\x01",
            "Time to move.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0xE)

    def lambda_369B():
        OP_6D(630, 0, 0, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_369B)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    OP_A2(0x25E1)
    Sleep(1000)
    NewScene("ED6_DT21/E1110   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_13_3437 end

    def Function_14_36D5(): pass

    label("Function_14_36D5")

    OP_8E(0xFE, 0xFFFFFF56, 0x0, 0xFFFFFC90, 0x7D0, 0x0)

    def lambda_36EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36EF)
    OP_8E(0xFE, 0xFFFFFEE8, 0x0, 0xFFFFF150, 0x7D0, 0x0)
    Return()

    # Function_14_36D5 end

    def Function_15_3710(): pass

    label("Function_15_3710")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Return()

    # Function_15_3710 end

    def Function_16_371C(): pass

    label("Function_16_371C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 6350, 0, -203180, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_44(0x12, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x16, 0xFF)
    SetChrPos(0x12, 680, 0, -202850, 270)
    SetChrPos(0x14, -650, 0, -202040, 180)
    SetChrPos(0x16, -1100, 0, -204230, 0)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x14, 4)
    SetChrChipByIndex(0x16, 4)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x16, 0)
    OP_6D(7830, 500, -202430, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)

    def lambda_37E8():
        OP_6D(3050, 0, -202330, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37E8)

    def lambda_3800():
        OP_67(0, 7020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3800)

    def lambda_3818():
        OP_6B(2670, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3818)

    def lambda_3828():
        OP_6E(284, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3828)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_38B2():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_38B2)
    Sleep(100)

    def lambda_38C5():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_38C5)
    Sleep(100)
    OP_8C(0x16, 90, 600)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x16, 10)
    SetChrSubChip(0x16, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_3936():
        OP_6D(5520, 0, -202080, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3936)

    def lambda_394E():
        OP_67(0, 7020, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_394E)

    def lambda_3966():
        OP_6B(2150, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3966)

    def lambda_3976():
        OP_6E(275, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3976)
    SetChrChipByIndex(0x12, 6)

    def lambda_398B():
        OP_8F(0xFE, 0x1482, 0x0, 0xFFFCE5DC, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_398B)
    Sleep(30)
    SetChrChipByIndex(0x14, 11)

    def lambda_39B0():
        OP_8F(0xFE, 0xFDB, 0x0, 0xFFFCE7B2, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_39B0)
    Sleep(30)
    SetChrChipByIndex(0x16, 11)

    def lambda_39D5():
        OP_8F(0xFE, 0x107C, 0x0, 0xFFFCE276, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_39D5)
    WaitChrThread(0x109, 0x0)
    Battle(0x78, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x12, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, 1810, 0, -201990, 45)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, 2430, 0, -201300, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, 2290, 0, -202020, 0)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 930, 0, -204040, 90)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 1330, 0, -204100, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 400, 0, -204320, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, -270, 0, -201860, 135)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 130, 0, -202300, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, -700, 0, -201900, 0)
    SetChrPos(0x109, 4490, 0, -203260, 270)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(4490, 0, -203260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25EA)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_371C end

    def Function_17_3C00(): pass

    label("Function_17_3C00")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -6370, 0, -202880, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_44(0x12, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x16, 0xFF)
    SetChrPos(0x12, -1460, 0, -203170, 90)
    SetChrPos(0x14, 410, 0, -202170, 225)
    SetChrPos(0x16, -160, 0, -204510, 0)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x14, 4)
    SetChrChipByIndex(0x16, 4)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x16, 0)
    OP_6D(-5970, 0, -202340, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(283, 0)

    def lambda_3CCC():
        OP_6D(-2000, 0, -202240, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3CCC)

    def lambda_3CE4():
        OP_67(0, 7020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CE4)

    def lambda_3CFC():
        OP_6B(2670, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3CFC)

    def lambda_3D0C():
        OP_6E(284, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3D0C)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3D96():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3D96)
    Sleep(100)

    def lambda_3DA9():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3DA9)
    Sleep(100)
    OP_8C(0x16, 270, 600)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x16, 10)
    SetChrSubChip(0x16, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_3E1A():
        OP_6D(-4170, 0, -202320, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E1A)

    def lambda_3E32():
        OP_67(0, 7020, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3E32)

    def lambda_3E4A():
        OP_6B(2150, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E4A)

    def lambda_3E5A():
        OP_6E(275, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3E5A)
    SetChrChipByIndex(0x12, 6)

    def lambda_3E6F():
        OP_8F(0xFE, 0xFFFFEBC4, 0x0, 0xFFFCE79E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3E6F)
    Sleep(30)
    SetChrChipByIndex(0x14, 11)

    def lambda_3E94():
        OP_8F(0xFE, 0xFFFFF09C, 0x0, 0xFFFCE9BA, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3E94)
    Sleep(30)
    SetChrChipByIndex(0x16, 11)

    def lambda_3EB9():
        OP_8F(0xFE, 0xFFFFEFC0, 0x0, 0xFFFCE5BE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_3EB9)
    WaitChrThread(0x109, 0x0)
    Battle(0x78, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x12, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, -1540, 0, -203070, 270)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, -1850, 0, -202700, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, -880, 0, -203000, 0)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 690, 0, -201320, 315)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 170, 0, -201120, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 750, 0, -201740, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, 690, 0, -203800, 225)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 370, 0, -204200, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, 880, 0, -203500, 0)
    SetChrPos(0x109, -4900, 0, -202900, 90)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(-4900, 0, -202900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25EB)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_17_3C00 end

    def Function_18_40E4(): pass

    label("Function_18_40E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 4)), scpexpr(EXPR_END)), "loc_40EF")
    Return()

    label("loc_40EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F8")
    Return()

    label("loc_40F8")

    EventBegin(0x0)
    Fade(500)
    OP_6D(930, 0, -141490, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    SetChrPos(0x109, -70, 0, -142470, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_417A():
        OP_6D(790, 0, -138040, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_417A)

    def lambda_4192():
        OP_67(0, 5920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4192)

    def lambda_41AA():
        OP_6B(2850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_41AA)

    def lambda_41BA():
        OP_6E(270, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_41BA)
    OP_44(0x18, 0xFF)
    OP_44(0x42, 0xFF)
    OP_44(0x4D, 0xFF)
    OP_44(0x36, 0xFF)
    OP_43(0x18, 0x0, 0x0, 0x13)
    OP_43(0x42, 0x0, 0x0, 0x14)
    OP_43(0x4D, 0x0, 0x0, 0x15)
    OP_43(0x36, 0x0, 0x0, 0x16)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x42, 0x0)
    WaitChrThread(0x4D, 0x0)
    WaitChrThread(0x36, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_4229():
        OP_6D(720, 0, -139720, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4229)

    def lambda_4241():
        OP_67(0, 6200, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4241)

    def lambda_4259():
        OP_6B(2450, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4259)

    def lambda_4269():
        OP_6E(255, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4269)
    SetChrChipByIndex(0x18, 6)

    def lambda_427E():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_427E)
    Sleep(30)
    SetChrChipByIndex(0x42, 6)

    def lambda_42A3():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 0, lambda_42A3)
    Sleep(30)
    SetChrChipByIndex(0x4D, 11)

    def lambda_42C8():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x4D, 0, lambda_42C8)
    Sleep(30)
    SetChrChipByIndex(0x36, 11)

    def lambda_42ED():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_42ED)
    WaitChrThread(0x109, 0x0)
    Battle(0x79, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x18, 0x0)
    OP_44(0x42, 0x0)
    OP_44(0x4D, 0x0)
    OP_44(0x36, 0x0)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x19, 0x1)
    SetChrFlags(0x19, 0x800)
    SetChrPos(0x19, 2500, 0, -139480, 180)
    ClearChrFlags(0x5B, 0x80)
    OP_9F(0x5B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5C, 0x80)
    OP_9F(0x5C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    OP_51(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x43, 9)
    SetChrSubChip(0x43, 0)
    ClearChrFlags(0x43, 0x1)
    SetChrFlags(0x43, 0x800)
    SetChrPos(0x43, -2500, 0, -140020, 135)
    ClearChrFlags(0x5D, 0x80)
    OP_9F(0x5D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5E, 0x80)
    OP_9F(0x5E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    OP_51(0x4E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x4E, 14)
    SetChrSubChip(0x4E, 0)
    ClearChrFlags(0x4E, 0x1)
    SetChrFlags(0x4E, 0x800)
    SetChrPos(0x4E, 3200, 0, -136900, 270)
    ClearChrFlags(0x5F, 0x80)
    OP_9F(0x5F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x60, 0x80)
    OP_9F(0x60, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    OP_51(0x37, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x37, 14)
    SetChrSubChip(0x37, 0)
    ClearChrFlags(0x37, 0x1)
    SetChrFlags(0x37, 0x800)
    SetChrPos(0x37, -2440, 0, -137500, 135)
    ClearChrFlags(0x61, 0x80)
    OP_9F(0x61, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x62, 0x80)
    OP_9F(0x62, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x109, -340, 0, -140900, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(-340, 0, -140900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25EC)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_18_40E4 end

    def Function_19_4510(): pass

    label("Function_19_4510")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -6420, 0, -137240, 90)
    SetChrChipByIndex(0xFE, 3)

    def lambda_453C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_453C)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x172, 0x0, 0xFFFDE69E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD5, 0x0, 0x64)
    Return()

    # Function_19_4510 end

    def Function_20_4573(): pass

    label("Function_20_4573")

    Sleep(600)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -6420, 0, -137240, 90)
    SetChrChipByIndex(0xFE, 3)

    def lambda_45A4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45A4)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFFFFAF6, 0x0, 0xFFFDE680, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD5, 0x0, 0x64)
    Return()

    # Function_20_4573 end

    def Function_21_45DB(): pass

    label("Function_21_45DB")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 390, 0, -125960, 180)
    SetChrChipByIndex(0xFE, 4)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x294, 0x0, 0xFFFDEE82, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 10)
    OP_22(0xD8, 0x0, 0x64)
    Return()

    # Function_21_45DB end

    def Function_22_461A(): pass

    label("Function_22_461A")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2170, 0, -126000, 180)
    SetChrChipByIndex(0xFE, 4)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0xFFFFF970, 0x0, 0xFFFDEBA8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 10)
    OP_22(0xD8, 0x0, 0x64)
    Return()

    # Function_22_461A end

    def Function_23_4659(): pass

    label("Function_23_4659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 5)), scpexpr(EXPR_END)), "loc_4664")
    Return()

    label("loc_4664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466D")
    Return()

    label("loc_466D")

    EventBegin(0x0)
    Fade(500)
    OP_6D(660, 0, -101930, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(45000, 0)
    OP_6E(252, 0)
    SetChrPos(0x109, -300, 0, -103010, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x54, 0x80)
    SetChrChipByIndex(0x54, 5)
    SetChrSubChip(0x54, 0)
    SetChrPos(0x54, 1100, 0, -85000, 180)
    ClearChrFlags(0x53, 0x80)
    SetChrChipByIndex(0x53, 10)
    SetChrSubChip(0x53, 0)
    SetChrPos(0x53, -1000, 0, -85150, 180)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    SetChrPos(0x63, 1290, 0, -88670, 180)
    SetChrPos(0x64, -1420, 0, -88700, 180)
    SetChrFlags(0x63, 0x800)
    SetChrFlags(0x64, 0x800)
    OP_51(0x63, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x64, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_477B():

        label("loc_477B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_477B")

    QueueWorkItem2(0x63, 3, lambda_477B)

    def lambda_478E():

        label("loc_478E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_478E")

    QueueWorkItem2(0x64, 3, lambda_478E)

    def lambda_47A1():
        OP_6D(1060, 350, -89440, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_47A1)

    def lambda_47B9():
        OP_67(0, 4710, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_47B9)

    def lambda_47D1():
        OP_6B(3240, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_47D1)

    def lambda_47E1():
        OP_6E(267, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_47E1)
    OP_8F(0x109, 0xBE, 0x0, 0xFFFE8D92, 0x1388, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #44
        0x53,
        "#5PThere you are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x54,
        (
            "#2POn the name of the Northern Jaegers,\x01",
            "we won't let you to go any farther!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #46
        0x109,
        "Kevin Graham",
        (
            "#1068F#4P*sigh* So you really are an active jaeger corps.\x01",
            "And a pretty famous one, to boot.\x02\x03",

            "#1066FStill, I get stuff's rough going for your country\x01",
            "and all, but I couldn't ask you to just...I don't\x01",
            "know. Step aside?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x53,
        (
            "#5PHow dare you? What do you know about the\x01",
            "hardships endured by our people?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #48
        0x54,
        (
            "#2PWe won't allow ourselves to be shamed with\x01",
            "defeat here. Not as long as we suffer!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #49
        0x109,
        "Kevin Graham",
        "#1065F...Bah. Should've known.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #50
        0x109,
        "Kevin Graham",
        "#1069F#4POkay, then! Then I'll come at you with all I've got!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    def lambda_4AD1():
        OP_6D(450, 0, -92000, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4AD1)

    def lambda_4AE9():
        OP_67(0, 6230, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4AE9)

    def lambda_4B01():
        OP_6B(2720, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4B01)

    def lambda_4B11():
        OP_6E(235, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4B11)
    SetChrChipByIndex(0x63, 35)

    def lambda_4B26():

        label("loc_4B26")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_4B26")

    QueueWorkItem2(0x63, 3, lambda_4B26)

    def lambda_4B39():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x63, 0, lambda_4B39)
    Sleep(30)
    SetChrChipByIndex(0x64, 35)

    def lambda_4B5E():

        label("loc_4B5E")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_4B5E")

    QueueWorkItem2(0x64, 3, lambda_4B5E)

    def lambda_4B71():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x64, 0, lambda_4B71)
    OP_43(0x64, 0x3, 0x0, 0x18)
    Sleep(10)
    SetChrChipByIndex(0x54, 6)

    def lambda_4B9D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x54, 0, lambda_4B9D)
    Sleep(10)
    SetChrChipByIndex(0x53, 11)

    def lambda_4BC2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x53, 0, lambda_4BC2)
    WaitChrThread(0x109, 0x0)
    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x54, 0x0)
    OP_44(0x53, 0x0)
    OP_44(0x63, 0x0)
    OP_44(0x64, 0x0)
    OP_44(0x63, 0x3)
    OP_44(0x64, 0x3)
    OP_A2(0x25ED)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4659 end

    def Function_24_4C22(): pass

    label("Function_24_4C22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C42")
    OP_22(0x13F, 0x0, 0x50)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(300)
    Jump("Function_24_4C22")

    label("loc_4C42")

    Return()

    # Function_24_4C22 end

    def Function_25_4C43(): pass

    label("Function_25_4C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 2)), scpexpr(EXPR_END)), "loc_4DCA")
    SetChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, 1810, 0, -201990, 45)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, 2430, 0, -201300, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, 2290, 0, -202020, 0)
    SetChrFlags(0x14, 0x80)
    OP_44(0x14, 0xFF)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 930, 0, -204040, 90)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 1330, 0, -204100, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 400, 0, -204320, 0)
    SetChrFlags(0x16, 0x80)
    OP_44(0x16, 0xFF)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, -270, 0, -201860, 135)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 130, 0, -202300, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, -700, 0, -201900, 0)

    label("loc_4DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 3)), scpexpr(EXPR_END)), "loc_4F51")
    SetChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, -1540, 0, -203070, 270)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, -1850, 0, -202700, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, -880, 0, -203000, 0)
    SetChrFlags(0x14, 0x80)
    OP_44(0x14, 0xFF)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 690, 0, -201320, 315)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 170, 0, -201120, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 750, 0, -201740, 0)
    SetChrFlags(0x16, 0x80)
    OP_44(0x16, 0xFF)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, 690, 0, -203800, 225)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 370, 0, -204200, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, 880, 0, -203500, 0)

    label("loc_4F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 4)), scpexpr(EXPR_END)), "loc_50D0")
    SetChrFlags(0x18, 0x80)
    OP_44(0x18, 0xFF)
    ClearChrFlags(0x19, 0x80)
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x19, 0x1)
    SetChrFlags(0x19, 0x800)
    SetChrPos(0x19, 2500, 0, -139480, 180)
    ClearChrFlags(0x5B, 0x80)
    OP_9F(0x5B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5C, 0x80)
    OP_9F(0x5C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x42, 0x80)
    OP_44(0x42, 0xFF)
    ClearChrFlags(0x43, 0x80)
    OP_51(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x43, 9)
    SetChrSubChip(0x43, 0)
    ClearChrFlags(0x43, 0x1)
    SetChrFlags(0x43, 0x800)
    SetChrPos(0x43, -2500, 0, -140020, 135)
    ClearChrFlags(0x5D, 0x80)
    OP_9F(0x5D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5E, 0x80)
    OP_9F(0x5E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x4D, 0x80)
    OP_44(0x4D, 0xFF)
    ClearChrFlags(0x4E, 0x80)
    OP_51(0x4E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x4E, 14)
    SetChrSubChip(0x4E, 0)
    ClearChrFlags(0x4E, 0x1)
    SetChrFlags(0x4E, 0x800)
    SetChrPos(0x4E, 3200, 0, -136900, 270)
    ClearChrFlags(0x5F, 0x80)
    OP_9F(0x5F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x60, 0x80)
    OP_9F(0x60, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x36, 0x80)
    OP_44(0x36, 0xFF)
    ClearChrFlags(0x37, 0x80)
    OP_51(0x37, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x37, 14)
    SetChrSubChip(0x37, 0)
    ClearChrFlags(0x37, 0x1)
    SetChrFlags(0x37, 0x800)
    SetChrPos(0x37, -2440, 0, -137500, 135)
    ClearChrFlags(0x61, 0x80)
    OP_9F(0x61, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x62, 0x80)
    OP_9F(0x62, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_50D0")

    Return()

    # Function_25_4C43 end

    def Function_26_50D1(): pass

    label("Function_26_50D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -170, 1070, 28810, 180)
    SetChrFlags(0x1B, 0x40)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x53, 0x80)
    SetChrPos(0x54, 160, 1070, 27030, 0)
    SetChrPos(0x53, -1290, 1020, 26650, 45)
    SetChrFlags(0x54, 0x40)
    SetChrFlags(0x53, 0x40)
    SetChrPos(0x109, 10, 0, 11000, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1B, 660, 0, 20500, 225)
    SetChrPos(0x20, 650, 0, 18760, 0)
    SetChrPos(0x23, -1060, 0, 19200, 45)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrPos(0x1C, -2290, 0, 16710, 0)
    SetChrPos(0x1D, 2490, 0, 17300, 45)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    OP_4A(0x11, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x20, 255)
    OP_4A(0x23, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    SetChrChipByIndex(0x23, 2)
    SetChrSubChip(0x23, 0)
    OP_6D(930, 1070, 28880, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #51
        0x11,
        "#5PWh-What is all this commotion?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x54,
        "#4PWe believe there to be an intruder, s-sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x53,
        "#6PAnd a competent one, at that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#5PAn intruder?! And just what do you think\x01",
            "I paid good mira to hire you for?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        (
            "#5PI don't care if he's alive or full of holes!\x01",
            "Get rid of him!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x109,
        "Kevin's Voice",
        (
            "#1POh, getting me dead OR alive is too much to ask\x01",
            "of those guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x54, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x53, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_540C():
        OP_6D(1470, 0, 21330, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_540C)

    def lambda_5424():
        OP_67(0, 5580, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5424)

    def lambda_543C():
        OP_6B(3080, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_543C)

    def lambda_544C():
        OP_6E(278, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_544C)

    def lambda_545C():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x54, 0, lambda_545C)
    Sleep(100)
    OP_8C(0x53, 180, 600)

    def lambda_5476():

        label("loc_5476")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5476")

    QueueWorkItem2(0x1B, 3, lambda_5476)

    def lambda_5487():

        label("loc_5487")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5487")

    QueueWorkItem2(0x20, 3, lambda_5487)

    def lambda_5498():

        label("loc_5498")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_5498")

    QueueWorkItem2(0x23, 3, lambda_5498)

    def lambda_54A9():

        label("loc_54A9")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_54A9")

    QueueWorkItem2(0x1C, 3, lambda_54A9)

    def lambda_54BA():

        label("loc_54BA")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_54BA")

    QueueWorkItem2(0x1D, 3, lambda_54BA)
    OP_22(0xB0, 0x0, 0x64)
    WaitChrThread(0x11, 0x0)

    def lambda_54D5():
        OP_8E(0xFE, 0xFFFFFE34, 0x0, 0x54B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_54D5)
    Sleep(500)

    def lambda_54F5():
        OP_6B(3200, 1850)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_54F5)
    Sleep(1500)
    OP_43(0x20, 0x0, 0x0, 0x2A)
    Sleep(200)
    OP_43(0x23, 0x0, 0x0, 0x2B)
    Sleep(150)
    OP_43(0x1B, 0x0, 0x0, 0x29)

    def lambda_5529():
        OP_6D(1770, 0, 26480, 2500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5529)

    def lambda_5541():
        OP_67(0, 5170, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5541)

    def lambda_5559():
        OP_6B(3080, 2500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5559)

    def lambda_5569():
        OP_6E(289, 2500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5569)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #57
        0x11,
        "#5PWh-Who the hell are you?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x11,
        "#5PWait... A priest?! No!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #59
        0x109,
        "Kevin Graham",
        (
            "#1071F#4PHaha. Yeah, I figured with something like this in\x01",
            "your possession, you'd at least have heard of us.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x2)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    OP_0D()
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x11,
        "#5PH-How dare you?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #61
        0x11,
        "#3S#5PGive that BACK! That's MINE!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    CloseMessageWindow()

    NpcTalk(    #62
        0x109,
        "Kevin Graham",
        (
            "#1075F#4PUh-uh! Wrong answer. This belongs to the Goddess,\x01",
            "and it needs to be rightfully returned to Her.\x02\x03",

            "It's not something mere mortals like you should be\x01",
            "keeping for themselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #63
        0x11,
        "#5P#80WK-Kill him...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #64
        0x11,
        "#3S#5PKill him and get me back my locket! NOW!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    CloseMessageWindow()

    def lambda_5842():
        OP_6D(1190, 270, 24840, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5842)

    def lambda_585A():
        OP_67(0, 4290, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_585A)

    def lambda_5872():
        OP_6B(3050, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5872)

    def lambda_5882():
        OP_6E(289, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5882)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x54, 12)
    SetChrSubChip(0x54, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x53, 12)
    SetChrSubChip(0x53, 0)
    Sleep(100)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x2)
    OP_0D()
    Sleep(300)
    OP_22(0x15E, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x20, 0x0, 0x0, 0x24)
    Sleep(30)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x23, 0x0, 0x0, 0x25)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1C, 0x0, 0x0, 0x27)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1B, 0x0, 0x0, 0x26)
    Sleep(100)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1D, 0x0, 0x0, 0x28)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x0, "monster\\msc0311.eff")
    LoadEffect(0x1, "monster\\ms10997.eff")
    LoadEffect(0x2, "scraft\\sc008_02.eff")
    LoadEffect(0x3, "monster\\ms31004a.eff")
    LoadEffect(0x4, "map\\mp009_00.eff")
    LoadEffect(0x5, "scraft\\sc000_11.eff")
    LoadEffect(0x6, "battle\\btgun10.eff")
    Fade(250)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    PlayEffect(0x2, 0xFF, 0xFF, -430, 1100, 22410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD7, 0x0, 0x64)
    Sleep(300)
    PlayEffect(0x3, 0x0, 0x109, 0, 500, 0, 0, 0, 0, 3000, 3500, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_5A9D():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5A9D)
    PlayEffect(0x0, 0x1, 0x53, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5AE2():

        label("loc_5AE2")

        OP_99(0xFE, 0x0, 0x1, 0x9C4)
        OP_48()
        Jump("loc_5AE2")

    QueueWorkItem2(0x53, 3, lambda_5AE2)
    PlayEffect(0x0, 0x2, 0x54, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5B2A():

        label("loc_5B2A")

        OP_99(0xFE, 0x0, 0x1, 0x9C4)
        OP_48()
        Jump("loc_5B2A")

    QueueWorkItem2(0x54, 3, lambda_5B2A)
    PlayEffect(0x1, 0xFF, 0xFF, -460, 500, 22500, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x109, 0x0, 0x0, 0x2C)
    Sleep(2000)
    OP_82(0x1, 0x0)
    OP_44(0x53, 0x3)
    SetChrSubChip(0x53, 0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x53, 10)
    SetChrSubChip(0x53, 0)
    Sleep(100)
    OP_44(0x54, 0x3)
    OP_82(0x2, 0x0)
    SetChrSubChip(0x54, 0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x54, 10)
    SetChrSubChip(0x54, 0)
    OP_44(0x109, 0x0)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x53, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x54, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x109, 19)
    OP_99(0x109, 0x0, 0x7, 0xBB8)
    OP_22(0xD8, 0x0, 0x64)

    def lambda_5C4F():
        OP_6D(440, 1070, 26800, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5C4F)

    def lambda_5C67():
        OP_67(0, 4290, -10000, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5C67)

    def lambda_5C7F():
        OP_6B(2920, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5C7F)

    def lambda_5C8F():
        OP_6E(289, 500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5C8F)

    def lambda_5C9F():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C9F)
    Sleep(300)
    OP_43(0x54, 0x0, 0x0, 0x2D)

    def lambda_5CBB():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5CBB)
    Sleep(200)
    OP_43(0x53, 0x0, 0x0, 0x2E)
    WaitChrThread(0x109, 0x1)
    SetChrSubChip(0x109, 7)
    Sleep(1500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #65
        0x11,
        "#5P#80WG...ah...\x02",
    )

    CloseMessageWindow()

    def lambda_5D05():
        OP_6D(1500, 1070, 29500, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5D05)

    def lambda_5D1D():
        OP_67(0, 4290, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5D1D)

    def lambda_5D35():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5D35)
    SetChrChipByIndex(0x109, 20)

    def lambda_5D4A():
        OP_8E(0xFE, 0xFFFFFEE8, 0x42E, 0x6842, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5D4A)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5D7C():
        OP_8F(0xFE, 0xFFFFFF56, 0x42E, 0x733C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5D7C)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x3)
    WaitChrThread(0x11, 0x0)
    Sleep(500)

    NpcTalk(    #66
        0x109,
        "Kevin Graham",
        (
            "#1065F#4PHermann Conrad.\x02\x03",

            "#1063FIn accordance with the laws of the church, and in\x01",
            "the name of Aidios, I am placing you under arrest.\x02\x03",

            "You stand charged with the unauthorized possession\x01",
            "of, and illegal use of, an artifact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#5PD-Don't you think you can get away with this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "#5PYou might be with the church, but I'm a Reinford\x01",
            "director! If you lay a hand on me...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0x109,
        "Kevin Graham",
        (
            "#1068F#4POh, don't you worry. We cleared this with the big\x01",
            "guys already.\x02\x03",

            "#1066FI'm sure you've got a preeetty good idea of just\x01",
            "how recklessly you've been acting with this thing,\x01",
            "right?\x02\x03",

            "You've been causing a whole lotta trouble for a\x01",
            "whole lotta people, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        "#5P#3S...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #71
        0x109,
        "Kevin Graham",
        (
            "#1075F#4PGuys like you have a habit of making themselves\x01",
            "no shortage of enemies, and you've done a stellar\x01",
            "job of that.\x02\x03",

            "#1060FSo just accept that your luck's run out and come \x01",
            "quietly, 'kay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        "#5P#80WNo...\x02",
    )

    CloseMessageWindow()

    def lambda_613F():
        OP_6D(1500, 1070, 30000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_613F)
    SetChrFlags(0x11, 0x40)
    OP_8F(0x11, 0xFFFFFF56, 0x42E, 0x7530, 0x1F4, 0x0)
    Fade(250)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 1)
    SetChrFlags(0x11, 0x2)
    OP_0D()

    def lambda_6185():
        OP_6B(2750, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6185)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x11, 2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #73 op#A op#5
        0x11,
        "#5P#4S#8ANooooo!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_61D5():
        OP_6D(1000, 1070, 31000, 200)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_61D5)

    def lambda_61ED():
        OP_67(0, 4290, -10000, 200)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_61ED)

    def lambda_6205():
        OP_6B(2750, 200)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6205)

    def lambda_6215():
        OP_6E(260, 200)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_6215)
    OP_7D(0x0, 0x109, 0x32, 0x1F4)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)

    def lambda_623C():
        OP_8F(0xFE, 0xFFFFFD62, 0x42E, 0x6F54, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_623C)
    WaitChrThread(0x109, 0x0)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 3)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x109, 0x8)
    SetChrPos(0x109, -670, 1070, 29000, 0)
    Sleep(50)
    SetChrSubChip(0x11, 4)
    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)

    def lambda_629A():
        OP_7C(0x28, 0x28, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_629A)
    OP_7D(0x1, 0x109, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #74 op#A op#5
        0x11,
        "#5P#15AGrah!\x05\x02",
    )

    CloseMessageWindow()
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x11, 0x5, 0x8, 0x3E8)
    Sleep(1000)

    NpcTalk(    #75
        0x109,
        "Kevin Graham",
        (
            "#1067F#4P...You just couldn't make this easy for me,\x01",
            "could you?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x11, 0x9, 0xC, 0x3E8)
    Sleep(500)

    NpcTalk(    #76
        0x109,
        "Kevin Graham",
        (
            "#1068F#5PSo much for this being a piece of cake.\x02\x03",

            "Catching guys like this alive is more like\x01",
            "trying to sneak off with the whole damn\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x65, 0x80)
    SetChrPos(0x65, -430, 0, 13590, 0)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    SetChrPos(0x66, 800, 0, 12480, 0)
    SetChrPos(0x67, -1980, 0, 11780, 0)
    SetChrPos(0x68, -630, 0, 10730, 0)
    SetChrPos(0x69, 580, 0, 10220, 0)
    SetChrPos(0x6A, -2310, 0, 9980, 0)
    SetChrPos(0x6B, -1290, 0, 8820, 0)
    SetChrPos(0x6C, -330, 0, 7600, 0)
    Sleep(500)

    NpcTalk(    #77
        0x65,
        "Man's Voice",
        "#3SStop right there!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x65, 0x1, 0x0, 0x1C)
    OP_43(0x66, 0x1, 0x0, 0x1D)
    OP_43(0x67, 0x1, 0x0, 0x1E)
    OP_43(0x68, 0x1, 0x0, 0x1F)
    OP_43(0x69, 0x1, 0x0, 0x20)
    OP_43(0x6A, 0x1, 0x0, 0x21)
    OP_43(0x6B, 0x1, 0x0, 0x22)
    OP_43(0x6C, 0x1, 0x0, 0x23)
    Fade(500)
    OP_6D(580, 1000, 25220, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    OP_99(0x11, 0xD, 0x13, 0x5DC)
    WaitChrThread(0x65, 0x1)
    WaitChrThread(0x66, 0x1)
    WaitChrThread(0x67, 0x1)
    WaitChrThread(0x68, 0x1)
    WaitChrThread(0x69, 0x1)
    WaitChrThread(0x6A, 0x1)
    WaitChrThread(0x6B, 0x1)
    WaitChrThread(0x6C, 0x1)
    Sleep(300)

    NpcTalk(    #78
        0x109,
        "Kevin Graham",
        (
            "#1060F#5PAww. You pulled out all the stops just for lil' old me?\x02\x03",

            "Now I get why you guys are so popular. That's some\x01",
            "quick work getting all dolled up and ready to take me\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x65,
        (
            "#6PSilence!\x02\x03",

            "You might've had your way before, but that's not how\x01",
            "it's gonna go this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x66,
        (
            "#4PAnd just so you know, there's an entire company of\x01",
            "us on this ship!\x02\x03",

            "Even if you have a hostage you can use against us,\x01",
            "you've got nowhere to run!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0x109,
        "Kevin Graham",
        (
            "#1075F#5PHeh...\x02\x03",

            "We're all lucky boys and girls today, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x66,
        "#4PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x65,
        "#6PWh-What are you talking about?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x109,
        "Kevin Graham",
        (
            "#1075F#5PIf this idiot here had been branded a heretic...\x02\x03",

            "#1073F...I would've had to hunt each and every one\x01",
            "of you down to the last member.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x67, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x66, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x6C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x6B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x69, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x68, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x6A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x65, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x65,
        "#6PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x66,
        "#4PWh-What's up with this guy?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #87
        0x109,
        "Kevin Graham",
        (
            "#1072F#5PWell, don't let it get to you. Keep up the good\x01",
            "work for your homeland or whatever.\x02\x03",

            "Just don't go giving us any reason to slaughter\x01",
            "you in the process.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 1000, 32000, 0)
    OP_67(0, 4160, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(0, 0)
    OP_6E(376, 0)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 22)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x1B)

    def lambda_6A9D():
        OP_6D(3420, 1550, 35070, 600)
        ExitThread()

    QueueWorkItem(0x65, 0, lambda_6A9D)

    def lambda_6AB5():
        OP_67(0, 5290, -10000, 600)
        ExitThread()

    QueueWorkItem(0x65, 1, lambda_6AB5)

    def lambda_6ACD():
        OP_6B(1690, 2000)
        ExitThread()

    QueueWorkItem(0x65, 2, lambda_6ACD)

    def lambda_6ADD():
        OP_6C(12000, 600)
        ExitThread()

    QueueWorkItem(0x65, 3, lambda_6ADD)

    def lambda_6AED():
        OP_6E(427, 2000)
        ExitThread()

    QueueWorkItem(0x66, 1, lambda_6AED)
    Sleep(300)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_50D1 end

    def Function_27_6B2B(): pass

    label("Function_27_6B2B")

    SetChrFlags(0x11, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_6B3B():
        OP_99(0xFE, 0x14, 0x15, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6B3B)
    WaitChrThread(0x11, 0x2)
    SetChrFlags(0x11, 0x800)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x11, 0x32, 0x1F4)

    def lambda_6B62():
        OP_96(0xFE, 0x12AC, 0xFFFFEC78, 0x8F16, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B62)
    Return()

    # Function_27_6B2B end

    def Function_28_6B7B(): pass

    label("Function_28_6B7B")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFFE2A, 0x0, 0x5546, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_28_6B7B end

    def Function_29_6B9F(): pass

    label("Function_29_6B9F")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0x53C, 0x0, 0x5294, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_29_6B9F end

    def Function_30_6BC3(): pass

    label("Function_30_6BC3")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFF7C2, 0x0, 0x53B6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_30_6BC3 end

    def Function_31_6BE7(): pass

    label("Function_31_6BE7")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFFBE6, 0x0, 0x4F06, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_31_6BE7 end

    def Function_32_6C0B(): pass

    label("Function_32_6C0B")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0x352, 0x0, 0x4CFE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_32_6C0B end

    def Function_33_6C2F(): pass

    label("Function_33_6C2F")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFF254, 0x0, 0x4C40, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_33_6C2F end

    def Function_34_6C53(): pass

    label("Function_34_6C53")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFF66E, 0x0, 0x4948, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_34_6C53 end

    def Function_35_6C77(): pass

    label("Function_35_6C77")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFFCC2, 0x0, 0x46E6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_35_6C77 end

    def Function_36_6C9B(): pass

    label("Function_36_6C9B")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0x29E, 0x0, 0x276A, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_6C9B end

    def Function_37_6CC0(): pass

    label("Function_37_6CC0")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 270, 600)
    OP_8E(0xFE, 0xFFFFD5E4, 0x0, 0x4704, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_6CC0 end

    def Function_38_6CE5(): pass

    label("Function_38_6CE5")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0x238C, 0x0, 0x3F20, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_6CE5 end

    def Function_39_6D0A(): pass

    label("Function_39_6D0A")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0xFFFFF3F8, 0x0, 0x2576, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_39_6D0A end

    def Function_40_6D2F(): pass

    label("Function_40_6D2F")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0x6F4, 0x0, 0x25A8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_40_6D2F end

    def Function_41_6D54(): pass

    label("Function_41_6D54")

    OP_8F(0xFE, 0xAA0, 0x0, 0x50E6, 0x7D0, 0x0)
    Return()

    # Function_41_6D54 end

    def Function_42_6D69(): pass

    label("Function_42_6D69")

    OP_8F(0xFE, 0x74E, 0x0, 0x49B6, 0x7D0, 0x0)
    Return()

    # Function_42_6D69 end

    def Function_43_6D7E(): pass

    label("Function_43_6D7E")

    OP_8F(0xFE, 0xFFFFF56A, 0x0, 0x4B6E, 0x7D0, 0x0)
    Return()

    # Function_43_6D7E end

    def Function_44_6D93(): pass

    label("Function_44_6D93")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4D")
    PlayEffect(0x4, 0xFF, 0xFF, -260, 600, 23000, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x4, 0xFF, 0xFF, 460, 500, 22500, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 700, 22000, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    Jump("Function_44_6D93")

    label("loc_6E4D")

    Return()

    # Function_44_6D93 end

    def Function_45_6E4E(): pass

    label("Function_45_6E4E")

    PlayEffect(0x6, 0x3, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x54, 0, 500, 0, 0)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(200)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6ED9():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6ED9)

    def lambda_6EF3():
        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6EF3)

    def lambda_6F0B():
        OP_96(0xFE, 0xA8C, 0x3E8, 0x7724, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F0B)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_45_6E4E end

    def Function_46_6F42(): pass

    label("Function_46_6F42")

    PlayEffect(0x6, 0x3, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x53, 0, 500, 0, 0)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(200)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6FCD():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6FCD)

    def lambda_6FE7():
        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6FE7)

    def lambda_6FFF():
        OP_96(0xFE, 0xFFFFF556, 0x3E8, 0x7724, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6FFF)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_46_6F42 end

    def Function_47_7036(): pass

    label("Function_47_7036")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    SetChrPos(0x65, 2180, 1000, 31360, 45)
    SetChrPos(0x66, 4150, 1000, 29590, 0)
    SetChrPos(0x67, 890, 1000, 30840, 45)
    SetChrPos(0x68, -1480, 1000, 30440, 45)
    SetChrPos(0x69, 3100, 1000, 27910, 0)
    SetChrPos(0x6A, 380, 1000, 28930, 45)
    SetChrPos(0x6B, -680, 1000, 27990, 45)
    SetChrPos(0x6C, 1100, 1000, 27030, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -140, 0, 9680, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x1A, 1530, 0, 16510, 0)
    SetChrPos(0x1B, 20, 0, 17600, 0)
    SetChrPos(0x1C, -1080, 0, 16600, 0)
    SetChrPos(0x1D, 710, 0, 15170, 0)
    SetChrPos(0x1E, -290, 0, 15120, 0)
    SetChrPos(0x1F, 2400, 0, 14670, 0)
    SetChrPos(0x20, -3340, 0, 13820, 45)
    SetChrPos(0x21, -2480, 0, 17130, 0)
    SetChrPos(0x22, 4970, 0, 18670, 0)
    SetChrPos(0x23, -4860, 0, 18200, 45)
    SetChrPos(0x24, -2520, 0, 13550, 0)
    OP_8C(0x27, 45, 0)
    OP_8C(0x28, 0, 0)
    SetChrPos(0x2D, 2800, 0, 12100, 0)
    SetChrPos(0x2E, 3630, 0, 12040, 315)
    SetChrPos(0x2F, -1940, 0, 12660, 0)
    SetChrPos(0x30, 6290, 0, 13380, 315)
    ClearChrFlags(0x54, 0x80)
    SetChrPos(0x54, 3000, 1000, 30000, 225)
    SetChrChipByIndex(0x54, 14)
    SetChrSubChip(0x54, 0)
    ClearChrFlags(0x54, 0x1)
    SetChrFlags(0x54, 0x800)
    ClearChrFlags(0x53, 0x80)
    SetChrPos(0x53, -2730, 1000, 30500, 135)
    SetChrChipByIndex(0x53, 14)
    SetChrSubChip(0x53, 0)
    ClearChrFlags(0x53, 0x1)
    SetChrFlags(0x53, 0x800)
    OP_4A(0x12, 0)
    OP_4A(0x14, 0)
    OP_4A(0x16, 0)
    OP_4A(0x18, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    OP_4A(0x28, 0)
    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    OP_4A(0x2D, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x30, 0)
    OP_6D(2570, 1000, 33180, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(0, 0)
    OP_6E(282, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #88
        0x65,
        "#5PI-Impossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x66,
        "Those Gralsritter are monsters...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0x2710)
    Fade(1000)
    OP_6D(1280, 0, 18500, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(44000, 0)
    OP_6E(289, 0)

    def lambda_73D7():
        OP_6D(1230, 0, 11100, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73D7)
    OP_22(0xB0, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_7404():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7404)

    ChrTalk(    #90
        0x10,
        (
            "\x07\x02#5PHaha... That was quite a splendid show.\x02\x03",

            "But our tale is only just beginning,\x01",
            "Kevin Graham...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 225, 300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_47_7036 end

    def Function_48_7497(): pass

    label("Function_48_7497")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_74B0")
    OP_A2(0x0)

    ChrTalk(    #91
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_74CE")

    label("loc_74B0")


    ChrTalk(    #92
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "Can I help you?\x02",
    )

    CloseMessageWindow()

    label("loc_74CE")

    TalkEnd(0xFE)
    Return()

    # Function_48_7497 end

    def Function_49_74D2(): pass

    label("Function_49_74D2")

    TalkBegin(0xFE)

    ChrTalk(    #94
        0xFE,
        (
            "The safety of this party is guaranteed so long\x01",
            "as we are here to ensure it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "So please, rest easy and enjoy yourself.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_74D2 end

    def Function_50_7558(): pass

    label("Function_50_7558")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0xFE,
        "Please, pay us no mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "We are merely here so that you might enjoy\x01",
            "this party to its fullest.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_7558 end

    def Function_51_75C7(): pass

    label("Function_51_75C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7681")
    OP_A2(0x1)

    ChrTalk(    #98
        0xFE,
        (
            "I apologize for our presence here at this most\x01",
            "elegant occasion, but be assured that we are\x01",
            "only here for your safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "I hope I can ask for your understanding.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7759")

    label("loc_7681")


    ChrTalk(    #100
        0xFE,
        (
            "I apologize for our boorish presence here at this\x01",
            "most elegant occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I'm afraid it is a necessary evil in order to ensure\x01",
            "the safety of our guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "All that I can do is ask for your understanding.\x02",
    )

    CloseMessageWindow()

    label("loc_7759")

    TalkEnd(0xFE)
    Return()

    # Function_51_75C7 end

    def Function_52_775D(): pass

    label("Function_52_775D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7769")
    Call(0, 53)

    label("loc_7769")

    Return()

    # Function_52_775D end

    def Function_53_776A(): pass

    label("Function_53_776A")

    EventBegin(0x1)
    TurnDirection(0x0, 0x11, 400)
    OP_6D(80, 0, 20820, 1500)
    Fade(500)
    OP_4A(0x11, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7873")

    ChrTalk(    #103
        0x11,
        "Yes... Yes, but of course...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        (
            "If I do say so myself, my company's prospects\x01",
            "are very bright...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #105
        0x109,
        "Masked Man",
        (
            "#1600F(He won't be paying attention to anything\x01",
            "else any time soon.)\x02\x03",

            "#1601F(Suits me.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AEA")

    label("loc_7873")


    ChrTalk(    #106
        0x1C,
        (
            "Hahaha! You certainly know how to hold a party, \x01",
            "Conrad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x1C,
        (
            "There aren't many who are wealthy enough to be \x01",
            "able to organize a gathering like this in the sky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x1D,
        "Oh, absolutely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x11,
        (
            "Haha. If my guests are satisfied, then I have done\x01",
            "my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        (
            "Still, today's party is but a minor diversion \x01",
            "compared to what the future holds for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x5DC)

    NpcTalk(    #111
        0x109,
        "Masked Man",
        (
            "#1602F(Quite the gathering we've got here...)\x02\x03",

            "#1602F(That looks like Marquis Ballad, known for his\x01",
            "extravagant spending...and this guy's the\x01",
            "president of that one big jeweler, Corries & Co.)\x02\x03",

            "#1601F(Heh. Hopefully, they'll keep our friend occupied\x01",
            "for a while.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AEA")

    Sleep(500)
    Fade(500)
    OP_4B(0x11, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    SetChrPos(0x109, 100, 0, 16140, 174)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2)
    EventEnd(0x1)
    Return()

    # Function_53_776A end

    def Function_54_7B23(): pass

    label("Function_54_7B23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7C00")

    ChrTalk(    #112
        0x11,
        "Yes... Yes, but of course...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        (
            "If I do say so myself, my company's prospects\x01",
            "are very bright...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #114
        0x109,
        "Masked Man",
        (
            "#1600F(He won't be paying attention to anything\x01",
            "else any time soon.)\x02\x03",

            "#1601F(Suits me.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C04")

    label("loc_7C00")

    Call(0, 52)

    label("loc_7C04")

    TalkEnd(0xFE)
    Return()

    # Function_54_7B23 end

    def Function_55_7C08(): pass

    label("Function_55_7C08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7D03")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x0, 450)

    ChrTalk(    #115
        0x1A,
        "Oh, my. Come to say hello again so soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x1A,
        (
            "My offer still stands if you find yourself with\x01",
            "an appetite for excitement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I'll be able to get rid of this gentleman in no\x01",
            "time at all, really.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    Jump("loc_7DF2")

    label("loc_7D03")

    OP_4A(0x1A, 0)
    OP_4A(0x20, 0)

    ChrTalk(    #118
        0x1A,
        "I'm sorry, what was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x20,
        (
            "I... Uhh... I said that no mask can hope to \x01",
            "disguise the beauty of your ivory-white skin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x20,
        "...or the luster of those fine red lips.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1A,
        "Teehee! Well, aren't you the flatterer?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x1A, 0)
    OP_4B(0x20, 0)
    OP_A2(0x3)

    label("loc_7DF2")

    TalkEnd(0xFE)
    Return()

    # Function_55_7C08 end

    def Function_56_7DF6(): pass

    label("Function_56_7DF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7EE3")

    ChrTalk(    #122
        0xFE,
        (
            "#2PHonestly, I'm still amazed at just how rapidly\x01",
            "your company has been growing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "#2P...By the way, I truly do appreciate your help\x01",
            "the other day.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x11, 255)

    ChrTalk(    #124
        0x11,
        "All is well, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#2P#1KHahaha!\x02",
    )


    ChrTalk(    #126
        0x11,
        "#1KHahaha!\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_4B(0x11, 255)
    Jump("loc_7EE7")

    label("loc_7EE3")

    Call(0, 52)

    label("loc_7EE7")

    TalkEnd(0xFE)
    Return()

    # Function_56_7DF6 end

    def Function_57_7EEB(): pass

    label("Function_57_7EEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8016")

    ChrTalk(    #127
        0xFE,
        (
            "I'm truly proud to be able to support your\x01",
            "wonderful company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Still, it's clear that you still have your best\x01",
            "days ahead of you, Conrad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "You can't stay a mere director in the Reinford\x01",
            "Group forever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "You've got to keep moving further and further\x01",
            "up the ladder. Haha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_801A")

    label("loc_8016")

    Call(0, 52)

    label("loc_801A")

    TalkEnd(0xFE)
    Return()

    # Function_57_7EEB end

    def Function_58_801E(): pass

    label("Function_58_801E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_80B5")

    ChrTalk(    #131
        0xFE,
        (
            "You still have more surprises ready for us as\x01",
            "the evening goes on, I hope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "I can hardly wait to find out what's still in store.\x02",
    )

    CloseMessageWindow()
    Jump("loc_80B9")

    label("loc_80B5")

    Call(0, 52)

    label("loc_80B9")

    TalkEnd(0xFE)
    Return()

    # Function_58_801E end

    def Function_59_80BD(): pass

    label("Function_59_80BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_8167")

    ChrTalk(    #133
        0xFE,
        (
            "This food definitely isn't set out as nicely as\x01",
            "it is back at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "This is unacceptable! I will need to speak with\x01",
            "the head chef about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_828A")

    label("loc_8167")


    ChrTalk(    #135
        0xFE,
        (
            "The chefs here ordinarily work at my hotel, \x01",
            "I'll have you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "They may be working in a different environment\x01",
            "with different equipment than usual, but that is\x01",
            "no excuse for slacking off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Perhaps I'm going to need to keep a watchful\x01",
            "eye on them to ensure they don't slip.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_828A")

    TalkEnd(0xFE)
    Return()

    # Function_59_80BD end

    def Function_60_828E(): pass

    label("Function_60_828E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8351")

    ChrTalk(    #138
        0xFE,
        (
            "We're here as guests today. We're supposed to be\x01",
            "enjoying ourselves, not concerning ourselves with\x01",
            "the party's organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Now, hurry up and go greet that Conrad fellow!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8440")

    label("loc_8351")


    ChrTalk(    #140
        0xFE,
        "Stop it, Dad! You're just embarrassing yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "We're here as guests today. We're supposed to be\x01",
            "enjoying ourselves, not concerning ourselves with\x01",
            "the party's organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "Now, hurry up and go greet that Conrad fellow!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_8440")

    TalkEnd(0xFE)
    Return()

    # Function_60_828E end

    def Function_61_8444(): pass

    label("Function_61_8444")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8514")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #143
        0xFE,
        (
            "*sigh* She was the one who initiated the \x01",
            "conversation with me, if you're wondering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Still, I can't very well ignore her. I'll just try\x01",
            "and keep the conversation going.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_8518")

    label("loc_8514")

    Call(0, 55)

    label("loc_8518")

    TalkEnd(0xFE)
    Return()

    # Function_61_8444 end

    def Function_62_851C(): pass

    label("Function_62_851C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_85B1")

    ChrTalk(    #145
        0xFE,
        (
            "A party like this would have been the perfect\x01",
            "chance for her to find a good husband, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "Must she oppose me at every turn?\x02",
    )

    CloseMessageWindow()
    Jump("loc_865A")

    label("loc_85B1")


    ChrTalk(    #147
        0xFE,
        (
            "*sigh* Why does she have to choose a party\x01",
            "like this to feel unwell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "I hope she isn't faking it to stay in her room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Must she oppose me at every turn?\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_865A")

    TalkEnd(0xFE)
    Return()

    # Function_62_851C end

    def Function_63_865E(): pass

    label("Function_63_865E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_86EC")

    ChrTalk(    #150
        0xFE,
        "I think it would be wise to let her rest for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "It isn't as though tonight's party is the only one\x01",
            "on the horizon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8771")

    label("loc_86EC")


    ChrTalk(    #152
        0xFE,
        "Yes, Lady Lindel is currently resting in her room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "She said that she is feeling a little unwell at\x01",
            "the moment, you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_8771")

    TalkEnd(0xFE)
    Return()

    # Function_63_865E end

    def Function_64_8775(): pass

    label("Function_64_8775")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_8856")

    ChrTalk(    #154
        0xFE,
        (
            "Changing the subject for a moment--I still\x01",
            "can't believe how Prince Olivert chose to\x01",
            "make his return to Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I can't recall anything more surprising that's\x01",
            "happened in the capital in recent times!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8920")

    label("loc_8856")


    ChrTalk(    #156
        0xFE,
        "And I couldn't agree more there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "The air of the capital is positively suffocating.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I try to get away from it as often as I can,\x01",
            "so I spend all of my time off in my villa to\x01",
            "the south.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_8920")

    TalkEnd(0xFE)
    Return()

    # Function_64_8775 end

    def Function_65_8924(): pass

    label("Function_65_8924")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_89C5")

    ChrTalk(    #159
        0xFE,
        "I truly am sick of the gloomy skies of the capital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Can't someone get rid of them and replace\x01",
            "them with something a little more cheerful?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AA1")

    label("loc_89C5")


    ChrTalk(    #161
        0xFE,
        "This truly is a spectacular ship.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "I was getting sick and tired of looking at\x01",
            "the gloomy skies of the capital, so this is\x01",
            "a wonderful change of scenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "I'll have to be sure to make the most of tonight.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_8AA1")

    TalkEnd(0xFE)
    Return()

    # Function_65_8924 end

    def Function_66_8AA5(): pass

    label("Function_66_8AA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_8B77")

    ChrTalk(    #164
        0xFE,
        (
            "The national government is more or less a collection\x01",
            "of civil servants, with all their flaws and weaknesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "You can get anything out of it as long as you know\x01",
            "the right buttons to push.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C8E")

    label("loc_8B77")


    ChrTalk(    #166
        0xFE,
        (
            "Hah. You still have much to learn about the ways\x01",
            "of the world, young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "The national government is more or less a collection\x01",
            "of civil servants, with all their flaws and weaknesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "You can get anything out of it as long as you know\x01",
            "the right buttons to push.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_8C8E")

    TalkEnd(0xFE)
    Return()

    # Function_66_8AA5 end

    def Function_67_8C92(): pass

    label("Function_67_8C92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_8DB0")

    ChrTalk(    #169
        0xFE,
        (
            "And that's saying nothing about THAT damn law\x01",
            "that froze my personal bank account!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "I may have been able to get it back by appealing,\x01",
            "but that's not the point!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "It was still a massive inconvenience that HE was \x01",
            "responsible for! I really cannot stand that man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EBB")

    label("loc_8DB0")


    ChrTalk(    #172
        0xFE,
        (
            "Hmph. Who does that upstart chancellor think\x01",
            "he is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "All he's done since marching into politics from\x01",
            "out of the army is pass one unpleasant law after\x01",
            "another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "I can't understand how he thinks. Where's the\x01",
            "benefit in appeasing commoners all the time?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_8EBB")

    TalkEnd(0xFE)
    Return()

    # Function_67_8C92 end

    def Function_68_8EBF(): pass

    label("Function_68_8EBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_8F6B")

    ChrTalk(    #175
        0xFE,
        (
            "The Reinford Group still has plenty of room\x01",
            "for growth in my personal opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Perhaps I should consider increasing my\x01",
            "investment in the group, hmm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90CD")

    label("loc_8F6B")


    ChrTalk(    #177
        0xFE,
        (
            "Being a part of the vast Reinford Group, the\x01",
            "Conrad Company certainly has strong backing to\x01",
            "support it in working towards greater growth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "After all, the Reinford Group is immensely\x01",
            "successful, and it manufactures everything\x01",
            "from military weapons to household goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "Perhaps I should consider increasing my\x01",
            "investment in the group, hmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_90CD")

    TalkEnd(0xFE)
    Return()

    # Function_68_8EBF end

    def Function_69_90D1(): pass

    label("Function_69_90D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_91FA")

    ChrTalk(    #180
        0xFE,
        (
            "Conrad really does know how to get the finest of\x01",
            "everything. Even this party's security seem to be\x01",
            "some of the best in the business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I have no idea where he found them, but I should\x01",
            "ask him to tell me. I could do with recruiting new\x01",
            "personnel into my private army as it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9332")

    label("loc_91FA")


    ChrTalk(    #182
        0xFE,
        (
            "I must say, I'm impressed at just how reliable the\x01",
            "security guards at today's party appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I'd been thinking it was about time to recruit\x01",
            "some new personnel to my own private army,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Perhaps I ought to ask Conrad where he found\x01",
            "these people. I might be able to recruit some of\x01",
            "them, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_9332")

    TalkEnd(0xFE)
    Return()

    # Function_69_90D1 end

    def Function_70_9336(): pass

    label("Function_70_9336")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_9413")

    ChrTalk(    #185
        0x29,
        (
            "When it comes to quality, Bareahard cannot be\x01",
            "beaten!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "In particular, the fur of the black minks raised in\x01",
            "the north is so soft! It's simply divine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x2A,
        "(Someone certainly cheered up in a hurry...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_959D")

    label("loc_9413")

    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)

    ChrTalk(    #188
        0x29,
        "Umm... Madam, I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x2A,
        (
            "What a surprising coincidence to find you here!\x01",
            "I wasn't aware that you had been invited to this\x01",
            "party as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x2A,
        (
            "Did it happen while you were in Bareahard buying\x01",
            "furs, perchance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x29,
        "Y-Yes, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x29,
        (
            "St-Still...I would very much appreciate it if you\x01",
            "could keep this a secret from my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x2A,
        "Oh, I wouldn't dream of telling him.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x29, 0)
    OP_4B(0x2A, 0)
    OP_A2(0x12)

    label("loc_959D")

    TalkEnd(0xFE)
    Return()

    # Function_70_9336 end

    def Function_71_95A1(): pass

    label("Function_71_95A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_96A6")

    ChrTalk(    #194
        0xFE,
        (
            "Still, if you really want to ensure that I won't,\x01",
            "I could do with a little favor from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "You see, I can't seem to find any furs that meet\x01",
            "my standards in the capital. Might you be willing\x01",
            "to introduce me to somewhere I could find some?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96AA")

    label("loc_96A6")

    Call(0, 70)

    label("loc_96AA")

    TalkEnd(0xFE)
    Return()

    # Function_71_95A1 end

    def Function_72_96AE(): pass

    label("Function_72_96AE")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_72_96AE end

    def Function_73_96B5(): pass

    label("Function_73_96B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_974D")
    OP_8C(0xFE, 180, 0)

    ChrTalk(    #196
        0xFE,
        (
            "Why, yes! I should probably have it now before\x01",
            "it starts getting cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "I'll take that tart there, too, if you don't mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9858")

    label("loc_974D")


    ChrTalk(    #198
        0xFE,
        (
            "Pardon me, but you haven't seen my wife around,\x01",
            "have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "*sigh* I keep telling her not to go wandering off\x01",
            "without telling me, but she never listens...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #200
        0x109,
        "Masked Man",
        (
            "#1602F#6P(Hold on...)\x02\x03",

            "#1601F#6P(Heh. Could this be Madame Frisky's\x01",
            "'oaf of a man'?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_9858")

    TalkEnd(0xFE)
    Return()

    # Function_73_96B5 end

    def Function_74_985C(): pass

    label("Function_74_985C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_9906")

    ChrTalk(    #201
        0xFE,
        (
            "That Conrad needs to stop getting so full of\x01",
            "himself and learn his place, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "And stop making moves into MY territory while\x01",
            "he's at it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A19")

    label("loc_9906")


    ChrTalk(    #203
        0xFE,
        (
            "Hmph. The Conrad Company might have made\x01",
            "a lot of progress in the past 10 years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "...but that was all thanks to the Reinford Group.\x01",
            "They couldn't have done a thing by themselves,\x01",
            "so they've got no right trying to act big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "They need to realize their place.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_9A19")

    TalkEnd(0xFE)
    Return()

    # Function_74_985C end

    def Function_75_9A1D(): pass

    label("Function_75_9A1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_9AD1")

    ChrTalk(    #206
        0xFE,
        (
            "This is a luxury airship, and we promise to provide\x01",
            "the most luxurious of service to match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "So please do let us know if there is anything we\x01",
            "can do for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B63")

    label("loc_9AD1")


    ChrTalk(    #208
        0xFE,
        (
            "Here on the Lusitania, we will be striving to meet\x01",
            "your every need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "So please do let us know if there is anything we\x01",
            "can do for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_9B63")

    TalkEnd(0xFE)
    Return()

    # Function_75_9A1D end

    def Function_76_9B67(): pass

    label("Function_76_9B67")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_9C07")

    ChrTalk(    #210
        0xFE,
        (
            "The evening is only just beginning--there's plenty\x01",
            "of entertainment still to look forward to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "I hope you will thoroughly enjoy yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CD3")

    label("loc_9C07")


    ChrTalk(    #212
        0xFE,
        (
            "There is plenty of entertainment to look forward \x01",
            "to this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "Furlan du Ciel's concert will be beginning\x01",
            "soon, and at eleven, we will be holding an\x01",
            "opera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "Be sure not to miss them.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_9CD3")

    TalkEnd(0xFE)
    Return()

    # Function_76_9B67 end

    def Function_77_9CD7(): pass

    label("Function_77_9CD7")

    TalkBegin(0x2F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_9D53")

    ChrTalk(    #215
        0x2F,
        "We are humbly at your service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x2F,
        (
            "Should there be anything we can do to assist you,\x01",
            "please let us know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DCF")

    label("loc_9D53")


    ChrTalk(    #217
        0x2F,
        "Might I interest you in something to drink, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x2F,
        (
            "We have some well-aged Steinrose, if you would\x01",
            "care for some.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_9DCF")

    TalkEnd(0x2F)
    Return()

    # Function_77_9CD7 end

    def Function_78_9DD3(): pass

    label("Function_78_9DD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_9E66")

    ChrTalk(    #219
        0xFE,
        (
            "All of our dishes are made using the finest and\x01",
            "most carefully selected ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "Why not try some of them for yourself?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F13")

    label("loc_9E66")


    ChrTalk(    #221
        0xFE,
        (
            "Today's dish of choice is steamed abalone with\x01",
            "cream, made to the highest of standards by our\x01",
            "chefs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "I must insist you try it! I'm certain you'll become\x01",
            "a fan.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_9F13")

    TalkEnd(0xFE)
    Return()

    # Function_78_9DD3 end

    def Function_79_9F17(): pass

    label("Function_79_9F17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_A01F")

    ChrTalk(    #223
        0xFE,
        "Goodness! They even have Carnelia here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "If you've never heard of it, it's a book that\x01",
            "has quite the rabid following.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "Ever since it was first published, there have \x01",
            "been rumors that it's actually a non-fiction.\x01",
            "I wonder if they're true?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A089")

    label("loc_A01F")


    ChrTalk(    #226
        0xFE,
        (
            "Heehee. This ship does have a fine collection\x01",
            "of books. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "I wonder which I should read first?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C)

    label("loc_A089")

    TalkEnd(0xFE)
    Return()

    # Function_79_9F17 end

    def Function_80_A08D(): pass

    label("Function_80_A08D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_A143")

    ChrTalk(    #228
        0xFE,
        (
            "Still, whatever happened, it has nothing to do\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "I'm sure if it was anything that serious, the army\x01",
            "would step in and sort it all out. We needn't fret.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A290")

    label("loc_A143")


    ChrTalk(    #230
        0xFE,
        (
            "You're talking about when they couldn't use\x01",
            "orbments all of a sudden along the southern\x01",
            "edge of Erebonia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "I heard that even the trains and international\x01",
            "flights in that region had to be stopped on\x01",
            "account of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "I haven't a clue what caused it all, though...\x01",
            "I can't imagine it was anything THAT serious,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_A290")

    TalkEnd(0xFE)
    Return()

    # Function_80_A08D end

    def Function_81_A294(): pass

    label("Function_81_A294")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_A3B3")

    ChrTalk(    #233
        0xFE,
        (
            "A friend of mine says he saw that massive flying\x01",
            "object I've heard mentioned a few times collapse\x01",
            "with his own eyes, but I have my doubts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "He's the only person I know who claims to\x01",
            "have seen it, so I can't help but wonder if\x01",
            "his eyes were playing tricks on him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4FE")

    label("loc_A3B3")


    ChrTalk(    #235
        0xFE,
        (
            "There are rumors the cause was a new weapon\x01",
            "developed by Liberl's army, though. That sounds\x01",
            "most serious to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Although, it's hard to be sure since the government\x01",
            "issued a ban on talking about the whole thing after\x01",
            "the fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "And without any official announcements on the \x01",
            "matter, all we're left with is hearsay.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_A4FE")

    TalkEnd(0xFE)
    Return()

    # Function_81_A294 end

    def Function_82_A502(): pass

    label("Function_82_A502")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 7)), scpexpr(EXPR_END)), "loc_A5D5")

    ChrTalk(    #238
        0xFE,
        (
            "I feel a little bad not being able to enjoy this party\x01",
            "after my son and his wife were kind enough to give\x01",
            "me a ticket to come here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "Parties like these don't seem to be my kind of thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A674")

    label("loc_A5D5")


    ChrTalk(    #240
        0xFE,
        (
            "*sigh* I just can't seem to relax on board this\x01",
            "ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "Everything is just so fancy and luxurious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "It's all too much for an old man like me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1F)

    label("loc_A674")

    TalkEnd(0xFE)
    Return()

    # Function_82_A502 end

    def Function_83_A678(): pass

    label("Function_83_A678")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 4)), scpexpr(EXPR_END)), "loc_A756")

    ChrTalk(    #243
        0xFE,
        (
            "You're welcome to take any of the books\x01",
            "here out of the library so long as you don't\x01",
            "take them outside of the ship itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "So if you would prefer to read in your room\x01",
            "rather than here, by all means.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7B3")

    label("loc_A756")


    ChrTalk(    #245
        0xFE,
        "This is the Lusitania's library.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "I hope you will enjoy your time relaxing here.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C)

    label("loc_A7B3")

    TalkEnd(0xFE)
    Return()

    # Function_83_A678 end

    def Function_84_A7B7(): pass

    label("Function_84_A7B7")

    TalkBegin(0xFE)

    ChrTalk(    #247
        0xFE,
        (
            "Please refrain from talking loudly when within\x01",
            "this room.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_84_A7B7 end

    def Function_85_A7FD(): pass

    label("Function_85_A7FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_END)), "loc_A8DC")

    ChrTalk(    #248
        0xFE,
        (
            "Haha! The dealers seem quite familiar with\x01",
            "how to ensure players have a good time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "That's something that's often sorely lacking in\x01",
            "the employees at less refined establishments,\x01",
            "but not here. No, sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA05")

    label("loc_A8DC")


    ChrTalk(    #250
        0xFE,
        (
            "This club is part of the Alicia chain of high-class\x01",
            "clubs which has its main branch in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "You would expect its employees to be trained to\x01",
            "the highest caliber...and you would be right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "And speaking of the highest caliber, perhaps\x01",
            "I ought to sample some of the wine now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)

    label("loc_AA05")

    TalkEnd(0xFE)
    Return()

    # Function_85_A7FD end

    def Function_86_AA09(): pass

    label("Function_86_AA09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 1)), scpexpr(EXPR_END)), "loc_AA59")

    ChrTalk(    #253
        0xFE,
        "C-Come on! I need to win this time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "Come on, black 11!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAE1")

    label("loc_AA59")


    ChrTalk(    #255
        0xFE,
        "C-Come on, black!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "It's gotta be black this time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "It's been red five times now! This next one\x01",
            "HAS to be black! Surely!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x21)

    label("loc_AAE1")

    TalkEnd(0xFE)
    Return()

    # Function_86_AA09 end

    def Function_87_AAE5(): pass

    label("Function_87_AAE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 2)), scpexpr(EXPR_END)), "loc_ABDA")

    ChrTalk(    #258
        0xFE,
        (
            "Still, if it weren't for the chancellor, a commoner\x01",
            "like me couldn't even dare to dream about going\x01",
            "to a party like that. We owe everything to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "Ah, is there a more wonderful word out there than\x01",
            "meritocracy? I say nay!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACA8")

    label("loc_ABDA")


    ChrTalk(    #260
        0xFE,
        (
            "I guess the party over in the room at the end of\x01",
            "the hall must be in full swing right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "Just you watch... One day, I'll be rich and famous\x01",
            "enough to go to fancy-schmancy parties, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22)

    label("loc_ACA8")

    TalkEnd(0xFE)
    Return()

    # Function_87_AAE5 end

    def Function_88_ACAC(): pass

    label("Function_88_ACAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 3)), scpexpr(EXPR_END)), "loc_AD1B")

    ChrTalk(    #262
        0xFE,
        "Heh! Bring it on, my good man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "There's no fun in winning every single game, \x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD84")

    label("loc_AD1B")


    ChrTalk(    #264
        0xFE,
        "You played rather well yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "Well, what do you say to another game?\x01",
            "I'm up for another.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x23)

    label("loc_AD84")

    TalkEnd(0xFE)
    Return()

    # Function_88_ACAC end

    def Function_89_AD88(): pass

    label("Function_89_AD88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 4)), scpexpr(EXPR_END)), "loc_AE2C")

    ChrTalk(    #266
        0xFE,
        "Spending money is all about having fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "People who don't understand that have\x01",
            "no right to be here partaking in the same\x01",
            "entertainment as me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF32")

    label("loc_AE2C")


    ChrTalk(    #268
        0xFE,
        (
            "Spending money is all about having fun,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "Whether you win or lose is a trivial detail.\x01",
            "You need only to focus on enjoying the\x01",
            "act of spending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "People who obsess over winning above all \x01",
            "else are base fools who have no right to be\x01",
            "here. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x24)

    label("loc_AF32")

    TalkEnd(0xFE)
    Return()

    # Function_89_AD88 end

    def Function_90_AF36(): pass

    label("Function_90_AF36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 6)), scpexpr(EXPR_END)), "loc_AF76")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #271
        0xFE,
        "Would you care for a game, sir?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_AFF7")

    label("loc_AF76")

    OP_4A(0xFE, 0)
    OP_4A(0x3C, 0)

    ChrTalk(    #272
        0x3C,
        "All right! It's time for me to make my wager.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x3C,
        "I'll put 300,000 mira on red 21.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "A sharp choice.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 0)
    OP_4B(0x3C, 0)
    OP_A2(0x2E)

    label("loc_AFF7")

    TalkEnd(0xFE)
    Return()

    # Function_90_AF36 end

    def Function_91_AFFB(): pass

    label("Function_91_AFFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 7)), scpexpr(EXPR_END)), "loc_B050")

    ChrTalk(    #275
        0xFE,
        "Certainly, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "However, I intend to be the victor this time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B103")

    label("loc_B050")


    ChrTalk(    #277
        0xFE,
        (
            "Well! That was a well-earned victory on your\x01",
            "part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "It's easy to tell that you're a real veteran\x01",
            "when it comes to card games.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "What would you like to do now, sir?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F)

    label("loc_B103")

    TalkEnd(0xFE)
    Return()

    # Function_91_AFFB end

    def Function_92_B107(): pass

    label("Function_92_B107")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 0)), scpexpr(EXPR_END)), "loc_B16D")

    ChrTalk(    #280
        0xFE,
        "Would you be interested in a quick game of cards?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "I'm sure you would enjoy it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1DC")

    label("loc_B16D")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #282
        0xFE,
        "*shuffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "*shuffle*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(    #284
        0xFE,
        (
            "Oh, hello there. Would you be interested in a \x01",
            "quick game?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x30)

    label("loc_B1DC")

    TalkEnd(0xFE)
    Return()

    # Function_92_B107 end

    def Function_93_B1E0(): pass

    label("Function_93_B1E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 1)), scpexpr(EXPR_END)), "loc_B213")

    ChrTalk(    #285
        0xFE,
        "Please, do enjoy your time here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B29E")

    label("loc_B213")


    ChrTalk(    #286
        0xFE,
        "Please, do enjoy your time here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "Still, do try not to get absorbed into your games.\x01",
            "Everything is best enjoyed in moderation.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x31)

    label("loc_B29E")

    TalkEnd(0xFE)
    Return()

    # Function_93_B1E0 end

    def Function_94_B2A2(): pass

    label("Function_94_B2A2")

    TalkBegin(0x41)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 5)), scpexpr(EXPR_END)), "loc_B366")

    ChrTalk(    #288
        0x41,
        (
            "All invited guests will be recognized here as \x01",
            "official members of this club and welcomed\x01",
            "accordingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x41,
        (
            "So please, do enjoy yourself and make use of the\x01",
            "facilities on offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B431")

    label("loc_B366")


    ChrTalk(    #290
        0x41,
        "Are you an invited guest, perchance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x41,
        (
            "If you are, we would be happy to treat you as an\x01",
            "official member of this club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x41,
        (
            "So please do enjoy yourself and make use of the\x01",
            "facilities on offer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2D)

    label("loc_B431")

    TalkEnd(0x41)
    Return()

    # Function_94_B2A2 end

    def Function_95_B435(): pass

    label("Function_95_B435")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 2)), scpexpr(EXPR_END)), "loc_B462")

    ChrTalk(    #293
        0xFE,
        "Please, do enjoy yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B48C")

    label("loc_B462")


    ChrTalk(    #294
        0xFE,
        "I hope you are enjoying yourself.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A)

    label("loc_B48C")

    TalkEnd(0xFE)
    Return()

    # Function_95_B435 end

    def Function_96_B490(): pass

    label("Function_96_B490")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 5)), scpexpr(EXPR_END)), "loc_B524")

    ChrTalk(    #295
        0xFE,
        (
            "These airship things truly are comfortable forms\x01",
            "of transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "I'll have to try and travel on them more often in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5DC")

    label("loc_B524")


    ChrTalk(    #297
        0xFE,
        (
            "Well, this is supposed to be the latest airship\x01",
            "from Reinford.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "Hoho! It's certainly comfortable enough to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "I'll have to try and travel on it again whenever\x01",
            "I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25)

    label("loc_B5DC")

    TalkEnd(0xFE)
    Return()

    # Function_96_B490 end

    def Function_97_B5E0(): pass

    label("Function_97_B5E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 5)), scpexpr(EXPR_END)), "loc_B65E")

    ChrTalk(    #300
        0xFE,
        (
            "Even the furnishings in these rooms all seem\x01",
            "to be of the highest class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "I have to say, I'm impressed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B716")

    label("loc_B65E")


    ChrTalk(    #302
        0xFE,
        "I have to say, I'm impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        "This tea's fragrance is rather pleasant, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "I'm glad to see that the level of service here\x01",
            "befits the price we paid to come on board.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25)

    label("loc_B716")

    TalkEnd(0xFE)
    Return()

    # Function_97_B5E0 end

    def Function_98_B71A(): pass

    label("Function_98_B71A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_B807")

    ChrTalk(    #305
        0xFE,
        (
            "This is one of the ship's second-class guest rooms,\x01",
            "though it's not being used for anything in particular\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "If you would like to use it and you're an invited guest,\x01",
            "you would be more than welcome to, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8EE")

    label("loc_B807")


    ChrTalk(    #307
        0xFE,
        "...Oh, please excuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "I assume you must be an invited guest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "The party is being held in the room at\x01",
            "the end of the corridor if you're having\x01",
            "difficulties finding the way.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #310
        0x109,
        "Masked Man",
        "#1600FThank you, miss.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_B8EE")

    TalkEnd(0xFE)
    Return()

    # Function_98_B71A end

    def Function_99_B8F2(): pass

    label("Function_99_B8F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 7)), scpexpr(EXPR_END)), "loc_B9D3")

    ChrTalk(    #311
        0xFE,
        (
            "This is the life rich people in our country\x01",
            "lead. Burn this sight into your memory and\x01",
            "never forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "I'm counting on you to make your way into\x01",
            "this world when you're older and make life\x01",
            "easy for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB07")

    label("loc_B9D3")


    ChrTalk(    #313
        0xFE,
        "Listen, son.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "I spent what little money we have just to get\x01",
            "you on this ship today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "This is the life rich people in our country lead.\x01",
            "Burn this sight into your memory and never\x01",
            "forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "I'm counting on you to make your way into\x01",
            "this world when you're older and make life\x01",
            "easy for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x27)

    label("loc_BB07")

    TalkEnd(0xFE)
    Return()

    # Function_99_B8F2 end

    def Function_100_BB0B(): pass

    label("Function_100_BB0B")

    TalkBegin(0xFE)

    ChrTalk(    #317
        0xFE,
        (
            "So you want me to grow up to become a\x01",
            "soldier and get famous and rich, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "If that lets me spend time on neat ships\x01",
            "like this, sure! This is so cool! ♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_100_BB0B end

    def Function_101_BBB8(): pass

    label("Function_101_BBB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC6")
    OP_A2(0x18)

    ChrTalk(    #319
        0xFE,
        "Are you taking a walk around the ship, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "If so, might I suggest following the stairs ahead\x01",
            "and stepping out onto the main deck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "I find gazing up at the stars while enjoying the\x01",
            "night breeze an especially relaxing way to pass\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDA8")

    label("loc_BCC6")


    ChrTalk(    #322
        0xFE,
        (
            "If you follow this corridor and travel up the stairs,\x01",
            "you'll find yourself on the main deck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "I find gazing up at the stars while enjoying the\x01",
            "night breeze an especially relaxing way to pass\x01",
            "the time. Why not try it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA8")

    TalkEnd(0xFE)
    Return()

    # Function_101_BBB8 end

    def Function_102_BDAC(): pass

    label("Function_102_BDAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 0)), scpexpr(EXPR_END)), "loc_BE19")

    ChrTalk(    #324
        0xFE,
        "...Hmm?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x0, 500)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #325
        0xFE,
        "U-Umm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "H-Hello...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_BF4E")

    label("loc_BE19")

    OP_4A(0x4F, 0)
    OP_4A(0x50, 0)

    ChrTalk(    #327
        0x4F,
        "H-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x4F,
        (
            "I, uh, kinda found an invitation to that \x01",
            "costume party that's going on right now... \x01",
            "What should I do with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x50,
        "Y-You idiot! What'd you pick it up for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x50,
        (
            "Those are only for the super-rich people in\x01",
            "the first-class rooms, not the likes of us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x4F,
        "B-But still...\x02",
    )

    CloseMessageWindow()
    OP_4B(0x4F, 0)
    OP_4B(0x50, 0)
    OP_A2(0x28)

    label("loc_BF4E")

    TalkEnd(0xFE)
    Return()

    # Function_102_BDAC end

    def Function_103_BF52(): pass

    label("Function_103_BF52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 0)), scpexpr(EXPR_END)), "loc_C041")

    NpcTalk(    #332
        0x109,
        "Masked Man",
        (
            "#1600FExcuse me, but is this the staircase that\x01",
            "leads to the observation deck?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(    #333
        0xFE,
        "Oh... Y-Yes! Yes, it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        "P-Please, go on ahead!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #335
        0x109,
        "Masked Man",
        "#1603FHaha. Thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    Jump("loc_C045")

    label("loc_C041")

    Call(0, 102)

    label("loc_C045")

    TalkEnd(0xFE)
    Return()

    # Function_103_BF52 end

    def Function_104_C049(): pass

    label("Function_104_C049")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 3)), scpexpr(EXPR_END)), "loc_C100")

    ChrTalk(    #336
        0xFE,
        (
            "We've been asked to personally validate every\x01",
            "guest's invitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "This is merely a precaution in order to secure\x01",
            "the safety of our lovely guests at this party.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C255")

    label("loc_C100")


    ChrTalk(    #338
        0xFE,
        "May I see your invite, sir?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0x109,
        "Masked Man",
        "#1600FThis, you mean?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #340
        "\x07\x05The masked man swiftly presented his invitation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #341
        0xFE,
        "My apologies, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "This is merely a precaution in order to secure\x01",
            "the safety of our lovely guests here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #343
        0x109,
        "Masked Man",
        "#1601FDon't worry about it. I understand.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B)

    label("loc_C255")

    TalkEnd(0xFE)
    Return()

    # Function_104_C049 end

    def Function_105_C259(): pass

    label("Function_105_C259")

    TalkBegin(0xFE)

    ChrTalk(    #344
        0xFE,
        (
            "Oh? Might I ask what business you have in this\x01",
            "area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        (
            "If you're looking for the observation deck,\x01",
            "you can reach it through those doors over\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "If you're looking for the area where the party\x01",
            "is being held, however, you will need to head\x01",
            "down the stairs.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_105_C259 end

    def Function_106_C36F(): pass

    label("Function_106_C36F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 2)), scpexpr(EXPR_END)), "loc_C3F1")

    ChrTalk(    #347
        0xFE,
        (
            "Can't say I'm familiar with the sound of this\x01",
            "airship's engines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        "I assume they must be a new model, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4E9")

    label("loc_C3F1")


    ChrTalk(    #349
        0xFE,
        (
            "So this is that new passenger airship model\x01",
            "I've heard so much about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "Can't say I'm familiar with the sound of its\x01",
            "engines, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "I assume they must be a new model, too...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #352
        0x109,
        "Masked Man",
        "#1602F(Hmm? Could this man be blind?)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x32)

    label("loc_C4E9")

    TalkEnd(0xFE)
    Return()

    # Function_106_C36F end

    def Function_107_C4ED(): pass

    label("Function_107_C4ED")

    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #353
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(50)
    EventEnd(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_C544")
    SetMapFlags(0x2000000)

    label("loc_C544")

    Return()

    # Function_107_C4ED end

    def Function_108_C545(): pass

    label("Function_108_C545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_C5B5")
    EventBegin(0x1)
    OP_8C(0x0, 270, 0)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #354
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_C5BE")

    label("loc_C5B5")

    NewScene("ED6_DT21/E1110   ._SN", 113, 1, 0)
    IdleLoop()

    label("loc_C5BE")

    Return()

    # Function_108_C545 end

    def Function_109_C5BF(): pass

    label("Function_109_C5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_C62F")
    EventBegin(0x1)
    OP_8C(0x0, 270, 0)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #355
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_C638")

    label("loc_C62F")

    NewScene("ED6_DT21/E1110   ._SN", 114, 1, 0)
    IdleLoop()

    label("loc_C638")

    Return()

    # Function_109_C5BF end

    def Function_110_C639(): pass

    label("Function_110_C639")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_C67B")

    NpcTalk(    #356
        0x109,
        "Kevin Graham",
        "#1060FOops. Get it together, Kevin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C6D0")

    label("loc_C67B")


    NpcTalk(    #357
        0x109,
        "Masked Man",
        (
            "#1602F(Whoops. Wrong way.)\x02\x03",

            "#1602F(I need to head up the staircase.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6D0")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_110_C639 end

    def Function_111_C6EC(): pass

    label("Function_111_C6EC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_C758")

    NpcTalk(    #358
        0x109,
        "Kevin Graham",
        "#1060FOops. Didn't mean to get turned around.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_C869")

    label("loc_C758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 3)), scpexpr(EXPR_END)), "loc_C7BA")

    NpcTalk(    #359
        0x109,
        "Masked Man",
        "#1602F(...I probably shouldn't go this way.)\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_C869")

    label("loc_C7BA")

    OP_4A(0x4D, 255)
    SetChrPos(0x4D, 82560, 0, -169000, 0)
    OP_8E(0x4D, 0x13BC8, 0x0, 0xFFFD759C, 0xBB8, 0x0)

    ChrTalk(    #360
        0x4D,
        "May I help you, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x4D, 400)

    NpcTalk(    #361
        0x109,
        "Masked Man",
        "#1602F...Oh, no. Sorry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x33)
    Sleep(300)
    Fade(300)
    SetChrPos(0x109, 80000, 0, -162800, 180)
    OP_4B(0x4D, 255)
    SetChrPos(0x4D, 84380, 0, -168870, 222)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x1)

    label("loc_C869")

    Return()

    # Function_111_C6EC end

    def Function_112_C86A(): pass

    label("Function_112_C86A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #362
        "\x07\x05The bookshelf contains chapters of Carnelia.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Chapters 1-6]\x01",           # 0
            "[Chapters 7-Finale]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C8FD"),
        (1, "loc_CA27"),
        (SWITCH_DEFAULT, "loc_CB34"),
    )


    label("loc_C8FD")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read Chapter 1]\x01",      # 0
            "[Read Chapter 2]\x01",      # 1
            "[Read Chapter 3]\x01",      # 2
            "[Read Chapter 4]\x01",      # 3
            "[Read Chapter 5]\x01",      # 4
            "[Read Chapter 6]\x01",      # 5
            "[Cancel]\x01",              # 6
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9CA")
    OP_B8(0xE6, 0x0)

    label("loc_C9CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9DC")
    OP_B8(0xE7, 0x0)

    label("loc_C9DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9EE")
    OP_B8(0xE8, 0x0)

    label("loc_C9EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA00")
    OP_B8(0xE9, 0x0)

    label("loc_CA00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA12")
    OP_B8(0xEA, 0x0)

    label("loc_CA12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA24")
    OP_B8(0xEB, 0x0)

    label("loc_CA24")

    Jump("loc_CB34")

    label("loc_CA27")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        10,
        1,
        (
            "[Read Chapter 7]\x01",           # 0
            "[Read Chapter 8]\x01",           # 1
            "[Read Chapter 9]\x01",           # 2
            "[Read Chapter 10]\x01",          # 3
            "[Read Chapter Finale]\x01",      # 4
            "[Cancel]\x01",                   # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAE9")
    OP_B8(0xEC, 0x0)

    label("loc_CAE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAFB")
    OP_B8(0xED, 0x0)

    label("loc_CAFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB0D")
    OP_B8(0xEE, 0x0)

    label("loc_CB0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB1F")
    OP_B8(0xEF, 0x0)

    label("loc_CB1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB31")
    OP_B8(0xF0, 0x0)

    label("loc_CB31")

    Jump("loc_CB34")

    label("loc_CB34")

    OP_5F(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_112_C86A end

    SaveToFile()

Try(main)
