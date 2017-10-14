from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0131   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0131   ._SN',
            'ED6_DT21/T0131_1 ._SN',
            'ED6_DT21/T0131_2 ._SN',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Tabitha',                              # 9
        'Tabitha',                              # 10
        'Elissa',                               # 11
        'Densel',                               # 12
        'Faulkner',                             # 13
        'Miner Trent',                          # 14
        'Miner Bones',                          # 15
        'Captain Petrov',                       # 16
        'Crew Mem. Roger',                      # 17
        'Radford',                              # 18
        'Bloom',                                # 19
        'ロレント風ごった煮',                   # 20
        'Armand',                               # 21
        'Ellie',                                # 22
        "Groom's Family",                       # 23
        "Groom's Family",                       # 24
        "Groom's Family",                       # 25
        "Bride's Family",                       # 26
        "Bride's Family",                       # 27
        "Bride's Family",                       # 28
        "Bride's Friend",                       # 29
        "Bride's Friend",                       # 30
        'Serra',                                # 31
        '料理',                                 # 32
        '料理',                                 # 33
        '料理',                                 # 34
        '料理',                                 # 35
        '料理',                                 # 36
        'Father Divine',                        # 37
        'Anton',                                # 38
        'Aina',                                 # 39
        'Olivier',                              # 40
        '酒瓶',                                 # 41
        '酒瓶',                                 # 42
        '酒瓶',                                 # 43
        '酒瓶',                                 # 44
        '酒瓶',                                 # 45
        '酒瓶',                                 # 46
        '酒瓶',                                 # 47
        '酒瓶',                                 # 48
        '酒瓶',                                 # 49
        '酒瓶',                                 # 50
        '酒瓶',                                 # 51
        'グラス',                               # 52
        'グラス',                               # 53
        'グラス',                               # 54
        'グラス',                               # 55
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
        'ED6_DT07/CH01130 ._CH',             # 00
        'ED6_DT07/CH02490 ._CH',             # 01
        'ED6_DT07/CH01280 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01503 ._CH',             # 04
        'ED6_DT26/CH20330 ._CH',             # 05
        'ED6_DT07/CH01500 ._CH',             # 06
        'ED6_DT07/CH01443 ._CH',             # 07
        'ED6_DT07/CH01290 ._CH',             # 08
        'ED6_DT07/CH01000 ._CH',             # 09
        'ED6_DT07/CH01010 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT07/CH01400 ._CH',             # 0C
        'ED6_DT07/CH01040 ._CH',             # 0D
        'ED6_DT07/CH01043 ._CH',             # 0E
        'ED6_DT07/CH02560 ._CH',             # 0F
        'ED6_DT07/CH00030 ._CH',             # 10
        'ED6_DT07/CH00033 ._CH',             # 11
        'ED6_DT26/CH20213 ._CH',             # 12
        'ED6_DT06/CH20020 ._CH',             # 13
        'ED6_DT06/CH20021 ._CH',             # 14
        'ED6_DT07/CH00023 ._CH',             # 15
        'ED6_DT07/CH00043 ._CH',             # 16
        'ED6_DT07/CH00053 ._CH',             # 17
        'ED6_DT07/CH00063 ._CH',             # 18
        'ED6_DT07/CH00073 ._CH',             # 19
        'ED6_DT26/CH20452 ._CH',             # 1A
        'ED6_DT26/CH20453 ._CH',             # 1B
        'ED6_DT07/CH01200 ._CH',             # 1C
        'ED6_DT07/CH01470 ._CH',             # 1D
        'ED6_DT07/CH01213 ._CH',             # 1E
        'ED6_DT07/CH01490 ._CH',             # 1F
        'ED6_DT07/CH01180 ._CH',             # 20
        'ED6_DT07/CH01480 ._CH',             # 21
        'ED6_DT07/CH01133 ._CH',             # 22
        'ED6_DT27/CH03003 ._CH',             # 23
        'ED6_DT07/CH00031 ._CH',             # 24
    )

    AddCharChipPat(
        'ED6_DT07/CH01130P._CP',             # 00
        'ED6_DT07/CH02490P._CP',             # 01
        'ED6_DT07/CH01280P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01503P._CP',             # 04
        'ED6_DT26/CH20330P._CP',             # 05
        'ED6_DT07/CH01500P._CP',             # 06
        'ED6_DT07/CH01443P._CP',             # 07
        'ED6_DT07/CH01290P._CP',             # 08
        'ED6_DT07/CH01000P._CP',             # 09
        'ED6_DT07/CH01010P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT07/CH01400P._CP',             # 0C
        'ED6_DT07/CH01040P._CP',             # 0D
        'ED6_DT07/CH01043P._CP',             # 0E
        'ED6_DT07/CH02560P._CP',             # 0F
        'ED6_DT07/CH00030P._CP',             # 10
        'ED6_DT07/CH00033P._CP',             # 11
        'ED6_DT26/CH20213P._CP',             # 12
        'ED6_DT06/CH20020P._CP',             # 13
        'ED6_DT06/CH20021P._CP',             # 14
        'ED6_DT07/CH00023P._CP',             # 15
        'ED6_DT07/CH00043P._CP',             # 16
        'ED6_DT07/CH00053P._CP',             # 17
        'ED6_DT07/CH00063P._CP',             # 18
        'ED6_DT07/CH00073P._CP',             # 19
        'ED6_DT26/CH20452P._CP',             # 1A
        'ED6_DT26/CH20453P._CP',             # 1B
        'ED6_DT07/CH01200P._CP',             # 1C
        'ED6_DT07/CH01470P._CP',             # 1D
        'ED6_DT07/CH01213P._CP',             # 1E
        'ED6_DT07/CH01490P._CP',             # 1F
        'ED6_DT07/CH01180P._CP',             # 20
        'ED6_DT07/CH01480P._CP',             # 21
        'ED6_DT07/CH01133P._CP',             # 22
        'ED6_DT27/CH03003P._CP',             # 23
        'ED6_DT07/CH00031P._CP',             # 24
    )

    DeclNpc(
        X                   = 87400,
        Z                   = 0,
        Y                   = 81630,
        Direction           = 344,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 88620,
        Z                   = 0,
        Y                   = 78900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 131077,
        ChipIndex           = 0x5,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 36450,
        Z                   = 0,
        Y                   = 126300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 40200,
        Z                   = 1500,
        Y                   = 78700,
        Direction           = 180,
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
        X                   = 39320,
        Z                   = 220,
        Y                   = 70940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 36640,
        Z                   = 0,
        Y                   = 72850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 39470,
        Z                   = 1620,
        Y                   = 77070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 41450,
        Z                   = 0,
        Y                   = 67700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 36700,
        Z                   = 0,
        Y                   = 75440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 35520,
        Z                   = 800,
        Y                   = 74850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40660,
        Z                   = 0,
        Y                   = 75350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 39580,
        Z                   = 0,
        Y                   = 75440,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 43710,
        Z                   = 0,
        Y                   = 73240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 40620,
        Z                   = 0,
        Y                   = 66290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 39720,
        Z                   = 220,
        Y                   = 66420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 43810,
        Z                   = 0,
        Y                   = 71980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 38130,
        Z                   = 0,
        Y                   = 75250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 36600,
        Z                   = 0,
        Y                   = 72650,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 42470,
        Z                   = 0,
        Y                   = 65640,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 43540,
        Z                   = 0,
        Y                   = 66710,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 38730,
        Z                   = 220,
        Y                   = 73090,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 39370,
        Z                   = 700,
        Y                   = 72160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131091,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 700,
        Y                   = 67800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327699,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39660,
        Z                   = 700,
        Y                   = 67220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589843,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44970,
        Z                   = 700,
        Y                   = 65470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1769491,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44150,
        Z                   = 700,
        Y                   = 65349,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131091,
        ChipIndex           = 0x13,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39680,
        Z                   = 600,
        Y                   = 67660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40400,
        Z                   = 2100,
        Y                   = 76950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39480,
        Z                   = 600,
        Y                   = 67190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39440,
        Z                   = 600,
        Y                   = 67960,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39510,
        Z                   = 600,
        Y                   = 67480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40620,
        Z                   = 600,
        Y                   = 67910,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40420,
        Z                   = 600,
        Y                   = 67930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40780,
        Z                   = 600,
        Y                   = 67090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40390,
        Z                   = 600,
        Y                   = 67140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 38760,
        Z                   = 600,
        Y                   = 67050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39040,
        Z                   = 600,
        Y                   = 67220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39910,
        Z                   = 500,
        Y                   = 67970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 38760,
        Z                   = 500,
        Y                   = 67940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40080,
        Z                   = 500,
        Y                   = 66980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40770,
        Z                   = 500,
        Y                   = 67760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 35580,
        TriggerZ            = 0,
        TriggerY            = 74990,
        TriggerRange        = 1000,
        ActorX              = 34500,
        ActorZ              = 1500,
        ActorY              = 75200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_7D6",          # 00, 0
        "Function_1_9A8",          # 01, 1
        "Function_2_A30",          # 02, 2
        "Function_3_BE0",          # 03, 3
        "Function_4_C92",          # 04, 4
        "Function_5_CA5",          # 05, 5
        "Function_6_2EBA",         # 06, 6
        "Function_7_459E",         # 07, 7
        "Function_8_5C4A",         # 08, 8
        "Function_9_7434",         # 09, 9
        "Function_10_7871",        # 0A, 10
        "Function_11_7AA3",        # 0B, 11
        "Function_12_7C50",        # 0C, 12
        "Function_13_7D3C",        # 0D, 13
        "Function_14_82FB",        # 0E, 14
        "Function_15_84B8",        # 0F, 15
        "Function_16_85B2",        # 10, 16
        "Function_17_8649",        # 11, 17
        "Function_18_86C0",        # 12, 18
        "Function_19_874A",        # 13, 19
        "Function_20_87B5",        # 14, 20
        "Function_21_881A",        # 15, 21
        "Function_22_886A",        # 16, 22
        "Function_23_88E2",        # 17, 23
        "Function_24_895F",        # 18, 24
        "Function_25_8AFA",        # 19, 25
        "Function_26_8C43",        # 1A, 26
    )


    def Function_0_7D6(): pass

    label("Function_0_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E8")
    Jump("loc_86A")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F3")
    Jump("loc_86A")

    label("loc_7F3")

    SetChrChipByIndex(0x1C, 35)
    SetChrChipByIndex(0x1D, 36)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
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
    SetChrPos(0xC, 41270, 0, 71880, 270)
    OP_43(0xC, 0x0, 0x6, 0x2)
    SetChrFlags(0xC, 0x10)

    label("loc_86A")

    OP_A2(0xF)
    Jump("loc_983")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_89A")
    SetChrPos(0xB, 37110, 0, 127270, 360)
    OP_43(0xB, 0x0, 0x6, 0x2)
    ClearChrFlags(0x11, 0x80)
    OP_A2(0xF)
    Jump("loc_983")

    label("loc_89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_901")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 86530, 0, 81370, 133)
    SetChrPos(0xB, 87000, 0, 79140, 90)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrPos(0xC, 34500, 0, 75200, 90)
    OP_43(0xC, 0x0, 0x6, 0x2)
    OP_A3(0xF)
    Jump("loc_983")

    label("loc_901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_946")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 87000, 0, 79140, 90)
    SetChrPos(0xC, 34500, 0, 75200, 90)
    OP_43(0xC, 0x0, 0x6, 0x2)
    OP_A3(0xF)
    Jump("loc_983")

    label("loc_946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_97B")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 36550, 0, 72670, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_975")
    SetChrFlags(0x8, 0x10)

    label("loc_975")

    OP_A2(0xF)
    Jump("loc_983")

    label("loc_97B")

    ClearChrFlags(0xD, 0x80)
    OP_A2(0xF)

    label("loc_983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_994")
    OP_A3(0x10F0)
    Event(0, 25)
    Jump("loc_9A7")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_9A7")
    SetMapFlags(0x10000000)
    OP_A3(0x10F1)
    Event(2, 0)

    label("loc_9A7")

    Return()

    # Function_0_7D6 end

    def Function_1_9A8(): pass

    label("Function_1_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_9B2")
    Jump("loc_9DE")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_9C3")
    OP_6F(0x0, 10)
    Jump("loc_9DE")

    label("loc_9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_9D4")
    OP_6F(0x0, 10)
    Jump("loc_9DE")

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_9DE")
    Jump("loc_9DE")

    label("loc_9DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F0")
    Jump("loc_A0F")

    label("loc_9F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FB")
    Jump("loc_A0F")

    label("loc_9FB")

    OP_D2(0x700A9, 0x700AD, 0x23)
    OP_D2(0x700CB, 0x700CF, 0x24)

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_A2F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2F")
    Call(0, 26)

    label("loc_A2F")

    Return()

    # Function_1_9A8 end

    def Function_2_A30(): pass

    label("Function_2_A30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDF")
    Sleep(3000)
    OP_8E(0xFE, 0xA85C, 0x5DC, 0x13434, 0x9C4, 0x0)
    OP_8B(0xFE, 0x186A0, 0x13434, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0xA7B7, 0x5DC, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA79B, 0x5DC, 0x129A8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA795, 0x0, 0x12296, 0x3E8, 0x0)
    OP_8E(0xFE, 0xA0F0, 0x0, 0x11940, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0x11940, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0xA730, 0x0, 0xFFDC, 0x7D0, 0x0)
    OP_8B(0xFE, 0x186A0, 0xFFDC, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8854, 0x0, 0xF974, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0xF938, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x186A0, 0xF938, 0x1F4)
    OP_8E(0xFE, 0x90EC, 0x0, 0xFBF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9344, 0x0, 0x10680, 0x9C4, 0x0)
    OP_8B(0xFE, 0x186A0, 0x10680, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x81B0, 0x0, 0x10D88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81B0, 0x0, 0x121D8, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0x121D8, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8930, 0x0, 0x1320E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8E30, 0x0, 0x133DA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9D08, 0x5DC, 0x1336C, 0x9C4, 0x0)
    OP_8B(0xFE, 0x9D08, 0x0, 0x1F4)
    Jump("Function_2_A30")

    label("loc_BDF")

    Return()

    # Function_2_A30 end

    def Function_3_BE0(): pass

    label("Function_3_BE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C91")
    Sleep(3000)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1E26C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1E26C, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1ED5C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1ED5C, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x9AB0, 0x0, 0x1F2D4, 0x9C4, 0x0)
    OP_8B(0xFE, 0x9AB0, 0x30D40, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x0, 0x1F2D4, 0x1F4)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1ED5C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1ED5C, 0x1F4)
    Jump("Function_3_BE0")

    label("loc_C91")

    Return()

    # Function_3_BE0 end

    def Function_4_C92(): pass

    label("Function_4_C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_CA0")
    Call(0, 5)
    Jump("loc_CA4")

    label("loc_CA0")

    Call(0, 8)

    label("loc_CA4")

    Return()

    # Function_4_C92 end

    def Function_5_CA5(): pass

    label("Function_5_CA5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Three-Eyed Soup] - 1600 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D54")
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D49")
    OP_A9(0x9)
    Jump("loc_D4B")

    label("loc_D49")

    OP_A9(0x4)

    label("loc_D4B")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_D54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E68")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2E")
    SubMira(1600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06Ate #2CThree-Eyed Soup#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x7D0)
    OP_31(0x1, 0xFD, 0x7D0)
    OP_31(0x2, 0xFD, 0x7D0)
    OP_31(0x3, 0xFD, 0x7D0)
    OP_31(0x4, 0xFD, 0x7D0)
    OP_31(0x5, 0xFD, 0x7D0)
    OP_31(0x6, 0xFD, 0x7D0)
    OP_31(0x7, 0xFD, 0x7D0)
    OP_31(0x8, 0xFD, 0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E20")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_DEF")
    Jump("loc_E20")

    label("loc_DEF")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06Learned [#2CThree-Eyed Soup#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_E20")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_E56")

    label("loc_E2E")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_E56")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xA)
    Return()

    label("loc_E68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E82")
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_E82")

    FadeToBright(300, 0)

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_195C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(    #3
        0xA,
        "Welcooome! ☆\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x102, 400)
    Sleep(1000)

    ChrTalk(    #4
        0xA,
        "Oh, is that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1041FIt's been a while, Elissa.\x02\x03",

            "It seems you're doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "You're FINALLY home! I was really worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "After all, Estelle ALWAYS seems to \x01",
            "dragging around other men these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "Made me wonder if you guys hit\x01",
            "some sort of snag in your relationship\x01",
            "or something, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1054FAh...haha...\x02\x03",

            "Well, I'm sorry.\x01",
            "Didn't mean to make you worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1007FOh, Elissa. Your worries are always so...\x01",
            "unique.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #11
        0xA,
        "So how about it, you two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        (
            "You can take it easy this time around,\x01",
            "can't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1015FMmmm...\x02\x03",

            "I'm not sure that we'll get the chance\x01",
            "the way things are right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #14
        0x103,
        (
            "#021FWell, I suppose a little wouldn't hurt.\x02\x03",

            "Even we still need our days off.\x01",
            "We're only human, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AD")

    label("loc_11C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1253")

    ChrTalk(    #15
        0x108,
        (
            "#070FWell, I suppose a short breather wouldn't hurt.\x02\x03",

            "Even if we do have a mission, we bracers are\x01",
            "still only human.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AD")

    label("loc_1253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(    #16
        0x106,
        (
            "#051FEh, a little bit probably wouldn't hurt.\x02\x03",

            "But don't go overboard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AD")


    ChrTalk(    #17
        0xA,
        "Well, come by when your work is done, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        "I want Joshua to test some of my best recipes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1040FYou've got some new recipes, huh?\x01",
            "I'd absolutely love to try them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1001FYeah, we'll come by for a meal!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20A3)
    Jump("loc_1959")

    label("loc_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_150A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1433")

    ChrTalk(    #21
        0xA,
        "My recipes are on the menu, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "One of them is a really popular dish. I'm pretty\x01",
            "proud of it, so make sure you give it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1507")

    label("loc_1433")


    ChrTalk(    #23
        0xA,
        (
            "Speaking of which, we've got a lot\x01",
            "of customers today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        "It's actually a wedding party.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "Not only are we crazy busy,\x01",
            "but we can't use orbments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        "Phew! Today's prep was like a battlefield.\x02",
    )

    CloseMessageWindow()
    OP_A3(0x6)
    OP_A2(0x5)

    label("loc_1507")

    Jump("loc_1959")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_169A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")

    ChrTalk(    #27
        0xA,
        "Estelle, Joshua! Welcome! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        (
            "Sorry it's so crowded. We have a \x01",
            "wedding party in today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "Thanks to that, our kitchen's an absolute\x01",
            "battlefield right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "Not only are we crazy busy,\x01",
            "but we can't use orbments...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1697")

    label("loc_1604")


    ChrTalk(    #31
        0xA,
        (
            "Our kitchen's been transformed into\x01",
            "an absolute battlefield right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "We're already knee deep in party prep,\x01",
            "yet we can't use orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1697")

    Jump("loc_1959")

    label("loc_169A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_180A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1784")

    ChrTalk(    #33
        0xA,
        "Welcome! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "We FINALLY finished preparing\x01",
            "the meals for the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "Now we just have to wait for the ceremony\x01",
            "to start and the guests to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "Phew! Gotta take a breather when\x01",
            "I get the chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1807")

    label("loc_1784")


    ChrTalk(    #37
        0xA,
        (
            "We FINALLY finished preparing\x01",
            "the meals for the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "We can't use orbments, so it took\x01",
            "way longer than it should have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1807")

    Jump("loc_1959")

    label("loc_180A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F8")

    ChrTalk(    #39
        0xA,
        "Heya, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        "We've got a reservation for a party today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "My dad's been busy with prep\x01",
            "since early this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        "It's a huge event, and we can't even use orbments.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "Seriously, Aidios, give us a break.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1959")

    label("loc_18F8")


    ChrTalk(    #44
        0xA,
        "Of all things to bust on such a big day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        "Thanks to that, my dad's been busy nonstop.\x02",
    )

    CloseMessageWindow()

    label("loc_1959")

    Jump("loc_2EB6")

    label("loc_195C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1E6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 0)), scpexpr(EXPR_END)), "loc_1C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_19EB")

    ChrTalk(    #46
        0xA,
        (
            "That crazy fog just disappeared\x01",
            "like it was never there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "Just one of those great mysteries,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B41")

    label("loc_19EB")


    ChrTalk(    #48
        0xA,
        (
            "When my mom awoke, the fog cleared\x01",
            "like it had never been there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "It was so clear. You never coulda guessed it'd\x01",
            "been impossible to see in front of your nose\x01",
            "just a bit before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "We still don't know why my mom\x01",
            "fell asleep like that, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "Really, everything is just strange as heck.\x01",
            "I can't make heads or tails of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1B41")

    Jump("loc_1C1E")

    label("loc_1B44")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #52
        0xA,
        (
            "Thank you so much for what you did\x01",
            "for my mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "The fog's cleared, too. So come on and\x01",
            "hang around the store for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "The least I can do is try to make\x01",
            "a great meal for you guys, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1E")

    Jump("loc_1E68")

    label("loc_1C21")

    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #55
        0xA,
        "Ahhh, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "Mom's opened her eyes!\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "*sniffle* I'm so... I'm so glad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1017FElissa...\x02\x03",

            "Yeah, I'm relieved too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #59
        0xA,
        (
            "...You too, Schera.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x103,
        (
            "#524FYou're welcome.\x01",
            "I'm happy to have been of help.\x02\x03",

            "I hope you'll continue to take care of Tabitha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "Yes, I'll do my best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "You and Aina should stop by again for\x01",
            "a drink one of these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#027FI'm looking forward to it.\x02\x03",

            "#525FGive my best to Faulkner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1007FWhoa...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E62")

    ChrTalk(    #65
        0x104,
        "#034FA-A death sentence...\x02",
    )

    CloseMessageWindow()

    label("loc_1E62")

    OP_A2(0x1A60)
    OP_A2(0x6)

    label("loc_1E68")

    Jump("loc_2EB6")

    label("loc_1E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_206C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1EFF")
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #66
        0xA,
        (
            "Please, I'm begging you, don't\x01",
            "push yourself too hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "I don't know what I'd do if you\x01",
            "collapsed, too, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2069")

    label("loc_1EFF")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #68
        0xA,
        "Hi there. It's nice to see you gu...\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #69
        0xA,
        "...Hey, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        "Your expressions seem awfully dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1025FN-No...\x02\x03",

            "#1016FIt's okay. It's nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        "Really? You're not tired or anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "I do want you to do your best on the\x01",
            "investigation, but don't push yourself\x01",
            "too hard, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2069")

    Jump("loc_2EB6")

    label("loc_206C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_20D9")
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #74
        0xA,
        "You all be careful, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "The fog's even thicker than\x01",
            "it was yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218E")

    label("loc_20D9")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #76
        0xA,
        "Oh, hey, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "Mom hasn't changed since yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        "If you find anything out, let me know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        "I'm going to be with Mom today, so...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_218E")

    Jump("loc_2EB6")

    label("loc_2191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 2)), scpexpr(EXPR_END)), "loc_22DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(    #80
        0xA,
        "Still, though, the fog outside is insane.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        (
            "We put up some weather sealant on the store,\x01",
            "but I still need to pick up the chairs on the\x01",
            "terrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        "With it being this humid, they might get damaged.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22DC")

    label("loc_2279")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #83
        0xA,
        "Anyway, take it easy today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "If you'd like, try the new recipes\x01",
            "I've come up with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22DC")

    Jump("loc_283E")

    label("loc_22DF")

    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #85
        0xA,
        "Ah... Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #86
        0xA,
        "And Schera's with you too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#021FWell, hellooooo, Elissa.\x01",
            "You doing all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1017FHaha! It's been a while, Elissa.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #89
        0xA,
        "Yay! You came back from training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "I was worried.\x01",
            "You hadn't been to visit at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1011FWork's been kinda hectic, and I've\x01",
            "had to travel about the regions.\x02\x03",

            "That's why I'm a bit late on my return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        "Oh, so you are busy. I thought so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "That's right. I heard your training was\x01",
            "done in a different country, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "Ohhhh, that's so cool\x01",
            "You bracers sure do get around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1008FAhaha, come on. It's not a big deal.\x02\x03",

            "It may have been in a different nation,\x01",
            "but it was just a guild facility.\x02\x03",

            "#1015F...Well, thanks to that, I HAVE definitely had\x01",
            "a chance to get a fresh start and really put\x01",
            "myself into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        "Hmm, a fresh start... Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "Maybe that skirt is a reflection\x01",
            "of your dedication?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1008FAh... You noticed, huh?\x02\x03",

            "#1013FUmm... D-Does it look weird?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        "What are you saying? It looks great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "It's a very cute design, but it\x01",
            "also looks easy to move in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        "Yeah, it's perfect on you, Estelle. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1016FTh-Thanks, Elissa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "I'm sure you have a lot on your mind with\x01",
            "what's going on with Joshua, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "Keep on staying positive. That's the\x01",
            "most like you, I think, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1017FY-Yeah... I'll do my best.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1882)
    OP_A2(0x5)

    label("loc_283E")

    Jump("loc_2EB6")

    label("loc_2841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 3)), scpexpr(EXPR_END)), "loc_28E2")

    ChrTalk(    #106
        0xA,
        "Oh, yeah, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#506FUh, was there something else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        "Tio really wants to see you, y'know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        "The whole family does, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EB6")

    label("loc_28E2")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #110
        0xA,
        "Welcom... MUH?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #111
        0xA,
        "ESTELLE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#001FHi, Elissa. It's been a while, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        "It's been a while? COME ON!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "You haven't been back since you\x01",
            "went to Bose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#505FWell, uh, a lot kinda happened...\x02\x03",

            "#008FAnyway, sorry if I worried you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        (
            "Oh, I heard all about it! You became\x01",
            "a full bracer AND stopped\x01",
            "Alan Richard, huh? You're so cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "Oh, yeah! Meanwhile, I'm finally allowed\x01",
            "full run of the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#004FWhoa, really?! That's great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        (
            "Heehee! Come by and eat sometime!\x01",
            "I'll treat you to my very super best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#001FYou bet your butt I will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "Now, with all THAT outta the way,\x01",
            "let's talk about the REAL topic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#505F...The who wha?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        "Oh, don't play coy with me, Miss Bracer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        (
            "(Y'know... I'm talking about the total stud\x01",
            "behind you. What happened to Joshua?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#501F(Uh...)\x02\x03",

            "#008F(I-It's not like that!!)\x02\x03",

            "#503F(Father Graham was just worried about me\x01",
            "being alone, so he came... I mean, he,\x01",
            "or, uh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xA,
        (
            "(Ooooooh, so he was worried\x01",
            "about you being alone, you saaaaaay?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#504FGnaaaaaaaaah, it's not LIKE THAT!\x02\x03",

            "#506FI'm here to go catch up to Joshua at home.\x01",
            "JOSH-U-A. He went a little ahead of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xA,
        (
            "Did he...? Oh, well, fiiiiiine.\x01",
            "That's enough for one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        (
            "Unfortunately I'm still on the clock, so come\x01",
            "by again. Make sure you bring Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        (
            "I bet I'll hear a lot more interesting\x01",
            "stuff if you do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#007FI'm telling you, you have it all wrong...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x142,
        "#1060F(Umm, huh?)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x102B)

    label("loc_2EB6")

    TalkEnd(0xA)
    Return()

    # Function_5_CA5 end

    def Function_6_2EBA(): pass

    label("Function_6_2EBA")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_37FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340E")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #133
        0xFE,
        "Oh, Estelle!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #134
        0xFE,
        "And hey, Joshua's with you today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        "#1040FHello, it's been quite some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Yeah, glad to see you're well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "Here in Rolent for work again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1002FYeah... Things are getting pretty crazy,\x01",
            "after all.\x02\x03",

            "Everything okay with you, Densel?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #139
        0xFE,
        "Well, not being able to use my orbal oven hurts.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_312D")

    ChrTalk(    #140
        0xFE,
        (
            "But I managed to make something for\x01",
            "the party through effort and guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1004FNow that's a professional for you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        "#1040FThe willpower of a cook, huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #143
        0xFE,
        (
            "Hmph. Can't call yourself a real cook\x01",
            "if you rely too heavily on your tools.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3359")

    label("loc_312D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_3230")

    ChrTalk(    #144
        0xFE,
        (
            "After all, of all things to be going on during\x01",
            "this mess, we have a party reservation today.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #145
        0x101,
        "#1004FP-Party...? Were you able to manage it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Yeah, we've even got some pretty good stuff\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3359")

    label("loc_3230")


    ChrTalk(    #147
        0xFE,
        (
            "After all, of all things to be going on during this\x01",
            "mess, we have a party reservation today.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #148
        0x101,
        "#1004FP-Party?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        "#1044FIs the food prep going okay?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #150
        0xFE,
        (
            "Heh. I may be down an orbal oven, but no\x01",
            "professional was ever stopped by losing\x01",
            "one of his tools.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3359")


    ChrTalk(    #151
        0xFE,
        (
            "Of course, I wouldn't mind getting that\x01",
            "tool back eventually...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "I'm counting on your bracers to make it happen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1006FAh... Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x102,
        "#1040FWe'll do our best.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20A1)
    Jump("loc_37FA")

    label("loc_340E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_35AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F6")

    ChrTalk(    #155
        0xFE,
        "It seems the party's proceeding very nicely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Pleasant conversation and well wishing...\x01",
            "And delicious food to commemorate the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Mmm, this is perfect. This is a happy\x01",
            "moment for me as a cook.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_35AB")

    label("loc_34F6")


    ChrTalk(    #158
        0xFE,
        "The party's proceeding very nicely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Now, then, I guess I'd better\x01",
            "get to preparing desert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "The plan is to end the affair with a glamorous,\x01",
            "champagne-flavored sorbet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AB")

    Jump("loc_37FA")

    label("loc_35AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_373B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369C")

    ChrTalk(    #161
        0xFE,
        (
            "Now, then, that's the food to serve at\x01",
            "the party ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Today's main course is a meat dish\x01",
            "using a selection of fresh herbs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Mmm, a scent that lures the appetite\x01",
            "permeates throughout the whole kitchen.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3738")

    label("loc_369C")


    ChrTalk(    #164
        0xFE,
        (
            "Today's main course is a meat dish\x01",
            "using a selection of fresh herbs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Mmm, a scent that lures the appetite\x01",
            "permeates throughout the whole kitchen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3738")

    Jump("loc_37FA")

    label("loc_373B")


    ChrTalk(    #166
        0xFE,
        (
            "It's certainly a pain that I can't\x01",
            "use my orbal stove, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "Real cooks are the ones who don't\x01",
            "choose their tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I'll overcome it somehow with the\x01",
            "equipment I have on hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FA")

    Jump("loc_459A")

    label("loc_37FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_38DA")

    ChrTalk(    #169
        0xFE,
        (
            "Thanks to Bloom, I think I've figured\x01",
            "out the trick to that recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "It's a pretty difficult dish, but I'd like\x01",
            "to master it and put it on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "I owe you a lot today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "Well, take care.\x02",
    )

    CloseMessageWindow()
    Jump("loc_459A")

    label("loc_38DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_38EC")
    Call(1, 6)
    Jump("loc_459A")

    label("loc_38EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_38FE")
    Call(1, 5)
    Jump("loc_459A")

    label("loc_38FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_3994")

    ChrTalk(    #173
        0xFE,
        "Good luck on the investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "If you find the recipe, come report it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "And when you do, don't forget the ingredients.\x02",
    )

    CloseMessageWindow()
    Jump("loc_459A")

    label("loc_3994")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3A4B")

    ChrTalk(    #176
        0xFE,
        (
            "Hey, Estelle. How's the investigation\x01",
            "coming along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "If you find the recipe, come report it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Oh, yeah, and when you do, don't\x01",
            "forget the ingredients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459A")

    label("loc_3A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3A6E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3A67")
    Call(1, 1)
    Jump("loc_3A6B")

    label("loc_3A67")

    Call(1, 0)

    label("loc_3A6B")

    Jump("loc_459A")

    label("loc_3A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3B37")

    ChrTalk(    #179
        0xFE,
        (
            "The fog's cleared and Tabitha's awoken.\x01",
            "That settles things for now, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "You guys can relax a bit today, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "Order anything you want.\x01",
            "I'll put my soul into it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C32")

    label("loc_3B37")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #182
        0xFE,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "Tabitha has finally opened her eyes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "I know full well how much trouble we've\x01",
            "caused you this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Since you came by, take a load\x01",
            "off and relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "I'll do my best work and whip you up\x01",
            "something amazing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3C32")

    Jump("loc_459A")

    label("loc_3C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3CA7")

    ChrTalk(    #187
        0xFE,
        "Tabitha sure looks happy in her sleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "She doesn't even know how we feel,\x01",
            "does she...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E15")

    label("loc_3CA7")


    ChrTalk(    #189
        0xFE,
        (
            "The morning rush finished, so I came\x01",
            "up to see how she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "Seriously, she looks like she doesn't\x01",
            "have a care in the world while we...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Haha. Still, with that kind of peaceful face\x01",
            "on her, I suppose I don't need to worry too\x01",
            "much right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "In that case, I'd better get back to the kitchen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I'm sure Falkner's starting to lose\x01",
            "it in there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3E15")

    Jump("loc_459A")

    label("loc_3E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3EDE")

    ChrTalk(    #194
        0xFE,
        (
            "Tabitha's the same as before. She's just\x01",
            "snoozing peacefully without a care in the\x01",
            "world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "If you haven't had breakfast yet, eat here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "We're pretty popular, you know.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FCF")

    label("loc_3EDE")


    ChrTalk(    #197
        0xFE,
        "Hey, the fog's pretty bad today, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "We may have made you worry last night,\x01",
            "but Tabitha's the same as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "According to Father Divine, her situation's\x01",
            "stabilized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "Right now, all we can do is watch\x01",
            "over her and wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3FCF")

    Jump("loc_459A")

    label("loc_3FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_438D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 3)), scpexpr(EXPR_END)), "loc_4238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4095")

    ChrTalk(    #201
        0xFE,
        (
            "There's a pretty nasty fog out, so we just\x01",
            "did a spot of weather sealing on the first\x01",
            "floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Hopefully it clears without staying around\x01",
            "too long, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_419A")

    label("loc_4095")


    ChrTalk(    #203
        0xFE,
        "Still, though, the fog today is awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "We just rushed to put up weather\x01",
            "sealant on our first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "If this fog drags on for too long, I might\x01",
            "have trouble getting stock in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "After all, fresh ingredients are\x01",
            "what make my place what it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_419A")

    Jump("loc_4235")

    label("loc_419D")


    ChrTalk(    #207
        0xFE,
        "Still, though, the fog today's awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "We just rushed to put up weather\x01",
            "sealant on our first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "Well, it's not stopping our business.\x02",
    )

    CloseMessageWindow()

    label("loc_4235")

    Jump("loc_438A")

    label("loc_4238")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #210
        0xFE,
        "Hey, Estelle, Scherazard. Been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1001FYeah, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x103,
        "#020FHow's business?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #213
        0xFE,
        "Great. As always, mornings have been killer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "I'm really glad the new dishes Elissa came\x01",
            "up with are popular. It's a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "Anyway, come on by and have\x01",
            "a drink once you're off work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1893)
    OP_A2(0x4)

    label("loc_438A")

    Jump("loc_459A")

    label("loc_438D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_459A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_4411")

    ChrTalk(    #216
        0xFE,
        "Oh, yeah, we've got a new dish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "It's the 'Three-Eyed Soup.'\x01",
            "Give it a try and 'see' what you think! Heh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459A")

    label("loc_4411")


    ChrTalk(    #218
        0xFE,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    TurnDirection(0xB, 0x101, 300)

    ChrTalk(    #219
        0xFE,
        (
            "Oh, welcome indeed!\x01",
            "If it isn't Estelle Bright!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#001FHi, Densel.\x01",
            "You sure seem full of energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "Darn right, I am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "No one'd want to eat food cooked by\x01",
            "some lazy slob, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        "#506FHaha. I guess not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "Oh, yeah, we've got a new dish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "It's the 'Three-Eyed Soup.'\x01",
            "Give it a try and 'see' what you think! Heh.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x104B)

    label("loc_459A")

    TalkEnd(0xB)
    Return()

    # Function_6_2EBA end

    def Function_7_459E(): pass

    label("Function_7_459E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4DF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF4")
    TurnDirection(0x8, 0x102, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0xFE,
        "Oh, my... It's Joshua and Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "I've been waiting for you two.\x01",
            "You've finally come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#1008FAhaha... Sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x102,
        "#1040FIt's been a while, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "Oh, come on! There's no need to be\x01",
            "so polite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "But you two've come back at a hard time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1026FAh, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x102,
        "#1040FIs the business faring well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "Yes, my husband and Elissa are\x01",
            "managing to hang in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "But, getting stock will become a problem soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "After all, scheduled liners and freight\x01",
            "transport are both stalled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x102,
        "#1043FAs I thought, distribution will be a problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "As the coordinator for the store,\x01",
            "it's quite the headache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "*sigh* Why do terrible things like this\x01",
            "keep happening...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#1003FI know what you mean...\x02\x03",

            "#1006FBut we bracers are doing our best as well,\x01",
            "to make things better even by a little.\x02\x03",

            "It may take some time, but we'll put things\x01",
            "back in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#1040FOf course, it's not just us on the case.\x01",
            "The Royal Army is also putting together\x01",
            "a plan of action.\x02\x03",

            "Do your best, Tabitha, until our actions\x01",
            "begin to bear fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "So just hang in there, in other words?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Well, we'll just have to make do with\x01",
            "the store somehow for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "Of course, I'll be expecting a lot from\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AEB")

    ChrTalk(    #245
        0x103,
        "#020FWe'll try to deliver just that.\x02",
    )

    CloseMessageWindow()

    label("loc_4AEB")

    OP_A2(0xE)
    OP_A2(0x20A2)
    Jump("loc_4DED")

    label("loc_4AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_4B82")

    ChrTalk(    #246
        0xFE,
        (
            "Things'll be hard at the store, but\x01",
            "we'll just have to make do somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "Of course, I'll be expecting a lot from\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DED")

    label("loc_4B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_4CE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C64")

    ChrTalk(    #248
        0xFE,
        (
            "YES!! We managed to get through\x01",
            "the party in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "I'm still worried about stock, but we\x01",
            "can manage with a few of my tricks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "If we can keep this up, then we can\x01",
            "stay open for business.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_4CE2")

    label("loc_4C64")


    ChrTalk(    #251
        0xFE,
        (
            "YES!! We managed to get through\x01",
            "the party in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "If we can keep this up, then we can\x01",
            "stay open for business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE2")

    Jump("loc_4DED")

    label("loc_4CE5")


    ChrTalk(    #253
        0xFE,
        (
            "We're still managing okay over here\x01",
            "because we've got farms nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "I'm sure the capital and Bose must\x01",
            "be in trouble, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "In this kind of situation I should probably be\x01",
            "focusing on our own problems, but it's hard\x01",
            "not to worry about the country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DED")

    Jump("loc_5C46")

    label("loc_4DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_5597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 7)), scpexpr(EXPR_END)), "loc_4F53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_4EC6")

    ChrTalk(    #256
        0x8,
        (
            "Sorry, sweetie. I don't know about\x01",
            "that recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x8,
        (
            "By the time I learned to cook, no one\x01",
            "made it anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x8,
        (
            "It might be best to ask some of the\x01",
            "older folk. They might remember it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F50")

    label("loc_4EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF1")
    Call(1, 4)
    Jump("loc_4F50")

    label("loc_4EF1")


    ChrTalk(    #259
        0xFE,
        (
            "If you can find some time,\x01",
            "come visit the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "Elissa and I would love to see you.\x02",
    )

    CloseMessageWindow()

    label("loc_4F50")

    Jump("loc_5594")

    label("loc_4F53")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #261
        0xFE,
        "Oh... Estelle and Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1001FHello, Tabitha.\x02\x03",

            "#1025FThank Aidios.\x01",
            "I'm glad to see you're awake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x103,
        "#020FHow are you feeling?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #264
        0xFE,
        "I'm still a little lightheaded, to be honest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "I'm sure it's because of the odd dream\x01",
            "I had...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#1026FAh, so you had one too.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #267
        0xFE,
        "Yes, it was such a nostalgic dream...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "I was about your age, out on a picnic\x01",
            "with everyone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "My old Sunday School friends...\x01",
            "Hannah and Lena.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#1004FHuh? Lena...\x02\x03",

            "My mother was there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "Well, not just Lena, mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "You and Joshua were there too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "Right next to your, ah, same-age mother,\x01",
            "to boot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x101,
        "#1020FSay whaaaat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x103,
        "#023FWell, that IS quite the dream.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #276
        0xFE,
        "Yes, odd, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "The picnic was very fun, and I think\x01",
            "it was quite a happy dream, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "It was so terribly happy, it actually\x01",
            "filled me with a sense of unease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "It was a dream with an unpleasant aftertaste,\x01",
            "like the whole thing was just made up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        "#1003FI-I see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #281
        0xFE,
        (
            "It was nice to see Lena as she was,\x01",
            "though. Especially after so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Perhaps she borrowed the world\x01",
            "of dreams to see you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "I'm sure she could hardly stand\x01",
            "to just watch beside the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        (
            "#1025FAhaha... Maybe...\x02\x03",

            "Can't really say I know for sure, but...\x01",
            "I guess I can think that now.\x02\x03",

            "#1015FTo be honest, I'm not sure I ended\x01",
            "up how she would have wanted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "Don't worry. You're fine. Trust me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "So, hold your head high as you tend to your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "You're a good, professional bracer\x01",
            "no matter how you look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        "#1006FYeah... Thank you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5F)

    label("loc_5594")

    Jump("loc_5C46")

    label("loc_5597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_59E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 5)), scpexpr(EXPR_END)), "loc_562D")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #289
        0xFE,
        (
            "It seems like you're going to be busy, but\x01",
            "come by and visit if you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "You're always welcome, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_59DD")

    label("loc_562D")

    ClearChrFlags(0xFE, 0x10)

    ChrTalk(    #291
        0xFE,
        "...Now, then, I should get to checking the books.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #292
        0xFE,
        "Oh, hello, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "It really has been some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        "#1000FHello, Tabitha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x103,
        "#020FYou look like you're doing well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #296
        0xFE,
        "Yes, decently enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "If you'd like, have something\x01",
            "to eat while you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "The new dish Elissa came up with has\x01",
            "quite the reputation for being delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#1018FAh, I'd love to have that!\x02\x03",

            "#1001FI've really been looking forward\x01",
            "to trying out her cooking. ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #300
        0xFE,
        "Can't wait for you to try it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "That girl's been wanting to\x01",
            "see you for some time now, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "While you're enjoying your meal,\x01",
            "go and say hi.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 2)), scpexpr(EXPR_END)), "loc_596E")

    ChrTalk(    #303
        0x101,
        "#1017FAhaha, actually, I already did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "Oh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "Do stop in from time to time, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        "You're always welcome, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_59DA")

    label("loc_596E")


    ChrTalk(    #307
        0x101,
        "#1017FYeah, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "Do stop in from time to time, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "You're always welcome, Estelle.\x02",
    )

    CloseMessageWindow()

    label("loc_59DA")

    OP_A2(0x1895)

    label("loc_59DD")

    Jump("loc_5C46")

    label("loc_59E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_5C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_5A4C")

    ChrTalk(    #310
        0xFE,
        "My family's doing well as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "If you have the time,\x01",
            "do say hello to them all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C46")

    label("loc_5A4C")


    ChrTalk(    #312
        0xFE,
        (
            "Grrrr, thanks to Alan Richard,\x01",
            "ingredient prices have...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 300)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #313
        0xFE,
        "...Estelle?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        "My goodness! It's been so long!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#008FHaha! Yeah, it really has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "You surprised me, sweetie.\x01",
            "When did you return to Rolent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        "#000FI practically just got off the airship.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "Is that so? Well, well... I'm sure\x01",
            "Elissa will be over the moon to\x01",
            "see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        "Do come by with your friends again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x101,
        "#001FYou don't need to tell me twice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        "I'll see you soon, then!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x104A)

    label("loc_5C46")

    TalkEnd(0x8)
    Return()

    # Function_7_459E end

    def Function_8_5C4A(): pass

    label("Function_8_5C4A")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E18")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Three-Eyed Soup] - 1600 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CE1")
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD6")
    OP_A9(0x9)
    Jump("loc_5CD8")

    label("loc_5CD6")

    OP_A9(0x4)

    label("loc_5CD8")

    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_5CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DF5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5DBB")
    SubMira(1600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #322
        "\x06Ate #2CThree-Eyed Soup#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x7D0)
    OP_31(0x1, 0xFD, 0x7D0)
    OP_31(0x2, 0xFD, 0x7D0)
    OP_31(0x3, 0xFD, 0x7D0)
    OP_31(0x4, 0xFD, 0x7D0)
    OP_31(0x5, 0xFD, 0x7D0)
    OP_31(0x6, 0xFD, 0x7D0)
    OP_31(0x7, 0xFD, 0x7D0)
    OP_31(0x8, 0xFD, 0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DAD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_5D7C")
    Jump("loc_5DAD")

    label("loc_5D7C")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #323
        "\x06Learned [#2CThree-Eyed Soup#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_5DAD")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_5DE3")

    label("loc_5DBB")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #324
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_5DE3")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xC)
    Return()

    label("loc_5DF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E0F")
    FadeToBright(300, 0)
    TalkEnd(0xC)
    Return()

    label("loc_5E0F")

    FadeToBright(300, 0)

    label("loc_5E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_5ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA7")

    ChrTalk(    #325
        0xC,
        (
            "Phew! Looks like the party's in full\x01",
            "swing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xC,
        (
            "All right, just a bit more.\x01",
            "This is where I gotta hold on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)
    OP_A2(0x0)
    Jump("loc_5EC9")

    label("loc_5EA7")


    ChrTalk(    #327
        0xC,
        "Excuse me. I I'll take that.\x02",
    )

    CloseMessageWindow()

    label("loc_5EC9")

    Jump("loc_7430")

    label("loc_5ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_60B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC2")

    ChrTalk(    #328
        0xC,
        "Ah... Sch-Scherazard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xC,
        "D-Done with work already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x103,
        (
            "#020FYes, I just finished up, but...\x02\x03",

            "Unfortunately, I can't have a drink right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xC,
        "Oh... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xC,
        "Umm... Well, then, we'll be waiting.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_601B")

    label("loc_5FC2")


    ChrTalk(    #333
        0xC,
        "Umm... Well, then, we'll be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xC,
        "Come by and relax when you have the time.\x02",
    )

    CloseMessageWindow()

    label("loc_601B")

    Jump("loc_60B4")

    label("loc_601E")


    ChrTalk(    #335
        0xC,
        (
            "The preparation for the party's finally done,\x01",
            "so the kitchen gets to rest a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xC,
        (
            "As the bartender, though, things are\x01",
            "starting to get busy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B4")

    Jump("loc_7430")

    label("loc_60B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_632E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6214")
    TurnDirection(0xC, 0x103, 0)

    ChrTalk(    #337
        0xC,
        "Sch-Scherazard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xC,
        (
            "Th-The sun's still high in the sky,\x01",
            "so you're still working, r-right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x103,
        "#025FYes, sadly. I'm still on the job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xC,
        (
            "Phew!\x01",
            "(Thank you, Aidios.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x103,
        "#027FWhat's with that relieved sigh?\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #342
        0xC,
        "N-No, it's nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xC,
        "Umm... Well, then, we'll be waiting.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_625D")

    label("loc_6214")


    ChrTalk(    #344
        0xC,
        "Umm... Well, then, we'll be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xC,
        "Good luck with your work.\x02",
    )

    CloseMessageWindow()

    label("loc_625D")

    Jump("loc_632B")

    label("loc_6260")


    ChrTalk(    #346
        0xC,
        (
            "There's a group with a reservation in for\x01",
            "the evening today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xC,
        "The chef's insanely busy with prep right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xC,
        (
            "I'm sure it's way harder than normal without\x01",
            "use of the orbal equipment and all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632B")

    Jump("loc_7430")

    label("loc_632E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_67C2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_63AB")

    ChrTalk(    #349
        0xC,
        (
            "To think that Bloom was once like\x01",
            "an angel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xC,
        "Hmm. It's kinda hard to imagine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_64D8")

    label("loc_63AB")


    ChrTalk(    #351
        0xC,
        (
            "That traditional recipe we had a bit ago...\x01",
            "It was something special all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xC,
        (
            "But... I feel like the impact of Radford's\x01",
            "story was stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xC,
        (
            "I don't really remember the\x01",
            "taste of the meal itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xC,
        (
            "To think that Bloom was once like\x01",
            "an angel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xC,
        "Hmm. It's kinda hard to imagine.\x02",
    )

    CloseMessageWindow()

    label("loc_64D8")

    Jump("loc_67BF")

    label("loc_64DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6562")

    ChrTalk(    #356
        0xC,
        "Th-Thankfully, there wasn't any damage today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xC,
        (
            "We should be able to live each day\x01",
            "safely for a while now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6660")

    label("loc_6562")


    ChrTalk(    #358
        0xC,
        "Phew! Thanks goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xC,
        "Th-Thankfully, there wasn't any damage today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        (
            "Still, though, to deliberately invite Aina\x01",
            "out to drink?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_662B")

    ChrTalk(    #361
        0xC,
        "Does he have some sorta death wish?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6660")

    label("loc_662B")


    ChrTalk(    #362
        0xC,
        "That Olivier guy must be suicidal or something.\x02",
    )

    CloseMessageWindow()

    label("loc_6660")

    Jump("loc_67BF")

    label("loc_6663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_66FB")

    ChrTalk(    #363
        0xC,
        (
            "Apparently, since the fog lifted, the scheduled\x01",
            "liners are back in action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xC,
        (
            "All the stranded passengers headed for\x01",
            "the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67BF")

    label("loc_66FB")


    ChrTalk(    #365
        0xC,
        "The owner's wife finally opened her eyes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xC,
        (
            "Plus, that bloody fog cleared up,\x01",
            "so everything's back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xC,
        (
            "Feels like I'll be able to get to work\x01",
            "with a very clean feeling now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_67BF")

    Jump("loc_7430")

    label("loc_67C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_69AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6871")

    ChrTalk(    #368
        0xC,
        (
            "With the miners back from the mine,\x01",
            "things just got a WHOLE lot busier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xC,
        (
            "Ahh, Densel! Please hurry and get back\x01",
            "to the kitchen! We're dyin' in here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69AB")

    label("loc_6871")


    ChrTalk(    #370
        0xC,
        (
            "With the miners back from the mine,\x01",
            "things just got a WHOLE lot busier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xC,
        (
            "They all eat a lot, probably since\x01",
            "their work is hard, physical labor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xC,
        (
            "Just as I was thinking the morning\x01",
            "rush was over and I'd get a break...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xC,
        (
            "Ahh, Densel! Please hurry and get back\x01",
            "to the kitchen! We're dyin' in here!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_69AB")

    Jump("loc_7430")

    label("loc_69AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_6BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A7A")

    ChrTalk(    #374
        0xC,
        (
            "There are hardly any customers\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xC,
        (
            "I'm sure those folks from the airship\x01",
            "will be back at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xC,
        (
            "They're all stuck and don't really\x01",
            "have anywhere else to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD9")

    label("loc_6A7A")


    ChrTalk(    #377
        0xC,
        (
            "There haven't been many customers\x01",
            "this morning for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xC,
        (
            "I'm sure those folks from the airship\x01",
            "will be back at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xC,
        (
            "They're all stuck and don't really\x01",
            "have anywhere else to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xC,
        "This is a bar's time to shine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xC,
        (
            "Good food and the power of alcohol is\x01",
            "at least something of a distraction from\x01",
            "the troubles outside.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6BD9")

    Jump("loc_7430")

    label("loc_6BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_71FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 6)), scpexpr(EXPR_END)), "loc_7067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6D18")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C86")

    ChrTalk(    #382
        0xC,
        "Sch-Scherazard. Good luck with your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xC,
        (
            "Umm, with the fog out, you might want\x01",
            "to wait for a nicer day to drink...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D15")

    label("loc_6C86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D15")

    ChrTalk(    #384
        0xC,
        "Scherazard and Aina? Drinking at the same time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xC,
        (
            "The horror of such can only be known\x01",
            "by those who have experienced it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D15")

    Jump("loc_6FEA")

    label("loc_6D18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E11")

    ChrTalk(    #386
        0xC,
        "Sch-Scherazard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xC,
        (
            "Y-You haven't...uh...already come to drink...?\x01",
            "...Have you? *gulp*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x103,
        "#020FI wish...but, unfortunately, I'm on the job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xC,
        "Ah...haha, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xC,
        (
            "(Phew! Dear Goddess, I thank thee\x01",
            "for thy mercy...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6FEA")

    label("loc_6E11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F54")

    ChrTalk(    #391
        0xC,
        "H-Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xC,
        (
            "That white coat...\x01",
            "You're not...THAT guy, are you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x104,
        "#031FHeh, I owe you from that time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xC,
        (
            "As someone who's experienced that pain,\x01",
            "I've got a lotta sympathy for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xC,
        (
            "We both have been scarred for life,\x01",
            "but we must be strong and carry on\x01",
            "in spite of such terrible memories.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6FEA")

    label("loc_6F54")


    ChrTalk(    #396
        0xC,
        "Scherazard alone'd be okay-ish, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xC,
        "Getting Aina involved makes it too dangerous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xC,
        "Ahh... Maybe I should take two to three days off.\x02",
    )

    CloseMessageWindow()

    label("loc_6FEA")

    Jump("loc_7064")

    label("loc_6FED")


    ChrTalk(    #399
        0xC,
        "Sch-Scherazard brought Aina in to drink...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xC,
        (
            "...I might need to take two, maybe three\x01",
            "days off from the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7064")

    Jump("loc_71F8")

    label("loc_7067")


    ChrTalk(    #401
        0x103,
        "#526FHey, Faulkner.\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xC, 0x103, 400)
    Sleep(400)

    ChrTalk(    #402
        0xC,
        "Sch-Scherazard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0xC,
        "Wh-When did you get back?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x103,
        (
            "#027FAwww. Did you miss me?\x02\x03",

            "#525FWell, I figure I'll be dragging Aina in to\x01",
            "drink at some point, so see you then!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #405
        0xC,
        "Ah...haha... We'll be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x101,
        "#1016F(A-As always, she's feared.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71F2")

    ChrTalk(    #407
        0x104,
        "#034FFaulkner... I understand your plight.\x02",
    )

    CloseMessageWindow()

    label("loc_71F2")

    OP_A2(0x1896)
    OP_A2(0x1)

    label("loc_71F8")

    Jump("loc_7430")

    label("loc_71FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_7430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_72A7")

    ChrTalk(    #408
        0xC,
        (
            "I had no regrets about leaving early that\x01",
            "day, so I'm not sure what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0xC,
        (
            "Ahhh, even just imagining what must have\x01",
            "happened is horrifying...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7430")

    label("loc_72A7")


    ChrTalk(    #410
        0xC,
        (
            "A while back, Scherazard brought in some\x01",
            "guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xC,
        "He was wearing this white coat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xC,
        (
            "He was a weird one, to be sure. Guy talked like\x01",
            "he was drunk before he even touched a glass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xC,
        (
            "Then Aina came in as well, straight from\x01",
            "the guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xC,
        (
            "The guy didn't seem to know any better\x01",
            "and he greeted her warmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xC,
        (
            "To me, he looked like a downed velgr\x01",
            "among a pack of dinediles.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7430")

    TalkEnd(0xC)
    Return()

    # Function_8_5C4A end

    def Function_9_7434(): pass

    label("Function_9_7434")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_751D")

    ChrTalk(    #416
        0xFE,
        (
            "*sigh* Hard to have an appetite today,\x01",
            "even for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xFE,
        (
            "But...if I don't eat somehow,\x01",
            "it'll be bad for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        "Oh, well. Guess I'll eat just a little...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "*crunch* *crunch* *crunch*\x01",
            "*munch* *munch*\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    Jump("loc_7631")

    label("loc_751D")


    ChrTalk(    #420
        0xFE,
        (
            "*crunch* *crunch* *munch*\x01",
            "*crunch* *crunch*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        "*chew* *chew*...*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "W-We got attacked by mist monsters\x01",
            "on the way back into town!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "The bracers managed to push them back\x01",
            "somehow, but...that was horrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        "Hard to have an appetite today, even for me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_7631")

    Jump("loc_786D")

    label("loc_7634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_7774")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_766E")

    ChrTalk(    #425
        0xFE,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0xFE,
        "*gulp*\x02",
    )

    CloseMessageWindow()
    Jump("loc_7771")

    label("loc_766E")


    ChrTalk(    #427
        0xFE,
        "*crunch* *crunch* *crunch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0xFE,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xFE,
        "*chew* *chew* *chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0xFE,
        "*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        "Man, the fog out there's crazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        (
            "I'm kinda worried now if I'll be\x01",
            "able to get to the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0xFE,
        (
            "A-Anyway, I'd better finish eating\x01",
            "and get going...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_7771")

    Jump("loc_786D")

    label("loc_7774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_786D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_77C2")

    ChrTalk(    #434
        0xFE,
        "*crunch* *crunch* *crunch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()
    Jump("loc_786D")

    label("loc_77C2")


    ChrTalk(    #436
        0xFE,
        "*chew* *chew* *chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        "*munch* *munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xFE,
        "*crunch* *crunch* *crunch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        "*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0xFE,
        (
            "Ahhhh, the boss is off today,\x01",
            "so I can skip work without worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_786D")

    TalkEnd(0xD)
    Return()

    # Function_9_7434 end

    def Function_10_7871(): pass

    label("Function_10_7871")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7931")

    ChrTalk(    #441
        0xFE,
        (
            "Those monsters that appeared from the fog...\x01",
            "Even just remembering them makes me\x01",
            "break out in a cold sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xFE,
        (
            "I can tell I'm hungry, but\x01",
            "I've just got no appetite.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A9F")

    label("loc_7931")


    ChrTalk(    #443
        0xFE,
        (
            "We came back from the mines today\x01",
            "with a bracer escort, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0xFE,
        (
            "Along the way, we were attacked\x01",
            "by monsters we've never seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0xFE,
        (
            "With the way they looked, scary can hardly\x01",
            "describe it. Even just remembering them\x01",
            "makes me break out in a cold sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "I can tell I'm hungry, but\x01",
            "I've just got no appetite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xFE,
        "I envy Trent at times like this.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_7A9F")

    TalkEnd(0xE)
    Return()

    # Function_10_7871 end

    def Function_11_7AA3(): pass

    label("Function_11_7AA3")

    TalkBegin(0xF)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7AC8")
    SetChrSubChip(0xFE, 2)
    Jump("loc_7AE3")

    label("loc_7AC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7ADE")
    SetChrSubChip(0xFE, 2)
    Jump("loc_7AE3")

    label("loc_7ADE")

    SetChrSubChip(0xFE, 1)

    label("loc_7AE3")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_7C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7B74")

    ChrTalk(    #448
        0xFE,
        (
            "All the crew's been on standby\x01",
            "in the ship since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xFE,
        "Right now, we're eating and sleeping in shifts.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C47")

    label("loc_7B74")


    ChrTalk(    #450
        0xFE,
        "Hey, good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        (
            "All the crew's been on standby\x01",
            "in the ship since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xFE,
        "Right now, we're eating and sleeping in shifts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        (
            "I didn't just come to the bar on my own\x01",
            "because I'm captain...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_7C47")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xF)
    Return()

    # Function_11_7AA3 end

    def Function_12_7C50(): pass

    label("Function_12_7C50")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7CCD")

    ChrTalk(    #454
        0xFE,
        (
            "*sigh* It really doesn't seem\x01",
            "like this fog's gonna clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xFE,
        "I wish I'd gone praying with Quint.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D38")

    label("loc_7CCD")


    ChrTalk(    #456
        0xFE,
        (
            "There's not much as useless\x01",
            "as a grounded airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0xFE,
        "*sigh* I want to get back to the air soon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_7D38")

    TalkEnd(0x10)
    Return()

    # Function_12_7C50 end

    def Function_13_7D3C(): pass

    label("Function_13_7D3C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7EF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_7DD9")

    ChrTalk(    #458
        0xFE,
        (
            "Thank you for everything today.\x01",
            "I'm sorry to take up your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "Thanks to you, I had a chance to\x01",
            "recall a nostalgic flavor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF1")

    label("loc_7DD9")


    ChrTalk(    #460
        0xFE,
        (
            "Thank you for everything today.\x01",
            "I'm sorry to take up your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xFE,
        (
            "Thanks to you, I had a chance to\x01",
            "recall a nostalgic flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xFE,
        (
            "Bloom's still got the stuff.\x01",
            "Yes siree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xFE,
        (
            "Her cooking skills have only gotten\x01",
            "better with age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        "It seems the years weren't wasted.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_7EF1")

    Jump("loc_82F7")

    label("loc_7EF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_7FF0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_7FE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_7F76")

    ChrTalk(    #465
        0xFE,
        "Good luck with your investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xFE,
        (
            "I'm looking forward to trying that recipe,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FE6")

    label("loc_7F76")


    ChrTalk(    #467
        0xFE,
        (
            "Ohh, it's you guys.\x01",
            "How goes the investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xFE,
        (
            "I'm looking forward to trying that recipe,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE6")

    Jump("loc_7FED")

    label("loc_7FE9")

    Call(1, 3)

    label("loc_7FED")

    Jump("loc_82F7")

    label("loc_7FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_827F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_80DD")

    ChrTalk(    #469
        0xFE,
        (
            "It's been quite some time since\x01",
            "I had a dream of my youth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        (
            "Still, thanks to that, I recalled\x01",
            "a very nostalgic recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        (
            "It'll be trouble for the chef, but I'm looking\x01",
            "forward to tasting it somethin' mighty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827C")

    label("loc_80DD")


    ChrTalk(    #472
        0xFE,
        (
            "Ahh, I had a dream of my youth for\x01",
            "the first time in a while yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        (
            "I was together with some old acquaintances,\x01",
            "for some reason, and we were cookin' up a\x01",
            "storm... It was a very odd dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0xFE,
        (
            "When I woke up, though, all I could think\x01",
            "about was that dish we made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "So I came here to the bar to\x01",
            "get them to make it for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0xFE,
        (
            "After all, it's an old recipe.\x01",
            "I'm sure it'll be hard on the chef.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_827C")

    Jump("loc_82F7")

    label("loc_827F")


    ChrTalk(    #477
        0xFE,
        "It was so clear, yet why this sudden fog?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0xFE,
        (
            "It feels like the trick of some naughty spirit\x01",
            "out of a fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82F7")

    TalkEnd(0x11)
    Return()

    # Function_13_7D3C end

    def Function_14_82FB(): pass

    label("Function_14_82FB")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_83F8")

    ChrTalk(    #479
        0xFE,
        "Hey, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        (
            "Thank you so much for coming! I'm\x01",
            "glad you could attend the ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0xFE,
        (
            "There's been a lot of bad happenings lately,\x01",
            "but enjoy yourselves while you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xFE,
        "It's a rare chance to celebrate, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8457")

    label("loc_83F8")


    ChrTalk(    #483
        0xFE,
        "Thanks for coming out today for my sake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xFE,
        "Since you're here, please enjoy yourselves.\x02",
    )

    CloseMessageWindow()

    label("loc_8457")

    OP_A2(0xA)
    Jump("loc_84B4")

    label("loc_845D")


    ChrTalk(    #485
        0xFE,
        "You came all the way, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0xFE,
        "It's a rare chance to celebrate, you know..\x02",
    )

    CloseMessageWindow()

    label("loc_84B4")

    TalkEnd(0x14)
    Return()

    # Function_14_82FB end

    def Function_15_84B8(): pass

    label("Function_15_84B8")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8571")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8526")

    ChrTalk(    #487
        0xFE,
        "Why, hello there! Thank you for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0xFE,
        "I promise. I promise we'll be happy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_856B")

    label("loc_8526")


    ChrTalk(    #489
        0xFE,
        "Thank you for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        "I promise. I promise we'll be happy.\x02",
    )

    CloseMessageWindow()

    label("loc_856B")

    OP_A2(0xB)
    Jump("loc_85AE")

    label("loc_8571")


    ChrTalk(    #491
        0xFE,
        (
            "Thank you so much for coming.\x01",
            "Please, enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85AE")

    TalkEnd(0x15)
    Return()

    # Function_15_84B8 end

    def Function_16_85B2(): pass

    label("Function_16_85B2")

    TalkBegin(0x16)

    ChrTalk(    #492
        0xFE,
        (
            "No, no. Now that it's over, it was\x01",
            "a wonderful wedding ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "Let us celebrate the future of our\x01",
            "newly wedded couple with a drink!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_16_85B2 end

    def Function_17_8649(): pass

    label("Function_17_8649")

    TalkBegin(0x17)

    ChrTalk(    #494
        0xFE,
        "Armand was sooo cool at the wedding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0xFE,
        (
            "It's the first time my brother's really\x01",
            "seemed like a grown man.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_17_8649 end

    def Function_18_86C0(): pass

    label("Function_18_86C0")

    TalkBegin(0x18)

    ChrTalk(    #496
        0xFE,
        (
            "Yeah, this place is as good as people say.\x01",
            "The food is great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0xFE,
        (
            "Thanks to that, my dress is feeling\x01",
            "a bit tight already...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_18_86C0 end

    def Function_19_874A(): pass

    label("Function_19_874A")

    TalkBegin(0x19)

    ChrTalk(    #498
        0xFE,
        "The bride's dress was beautifully tailored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0xFE,
        "Ahhh, I wish her father could have seen it...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_19_874A end

    def Function_20_87B5(): pass

    label("Function_20_87B5")

    TalkBegin(0x1A)

    ChrTalk(    #500
        0xFE,
        "I'm relieved the ceremony went okay. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0xFE,
        "I'm sure her father was watching from heaven.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_20_87B5 end

    def Function_21_881A(): pass

    label("Function_21_881A")

    TalkBegin(0x1B)

    ChrTalk(    #502
        0xFE,
        "My sister's dress was so pretty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        "I wanna be a bride soon, too.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_21_881A end

    def Function_22_886A(): pass

    label("Function_22_886A")

    TalkBegin(0x1C)

    ChrTalk(    #504
        0xFE,
        "Ellie was positively glowing today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xFE,
        (
            "I wonder if you can really change so much\x01",
            "just by donning a dress.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_22_886A end

    def Function_23_88E2(): pass

    label("Function_23_88E2")

    TalkBegin(0x1D)

    ChrTalk(    #506
        0xFE,
        "Ellie and Armand. They look really happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0xFE,
        (
            "I envy 'em... Maybe I should start\x01",
            "seriously looking for someone.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1D)
    Return()

    # Function_23_88E2 end

    def Function_24_895F(): pass

    label("Function_24_895F")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 7)), scpexpr(EXPR_END)), "loc_89DE")

    ChrTalk(    #508
        0xFE,
        "Ahhhhh... The liquor's great today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xFE,
        (
            "I helped dress her, so I have the\x01",
            "right to attend the party, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF6")

    label("loc_89DE")


    ChrTalk(    #510
        0xFE,
        "Ahhhhh... The liquor's great today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xFE,
        (
            "I'm feeling really good, so here, I'll give\x01",
            "you this book my husband bought.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #512
        "\x07\x00Received #580i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x244, 1)
    OP_A2(0x10BF)
    OP_0D()

    ChrTalk(    #513
        0xFE,
        (
            "Ahhhhh... The liquor's great today.\x01",
            "It tastes even better since it's free!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AF6")

    TalkEnd(0x1E)
    Return()

    # Function_24_895F end

    def Function_25_8AFA(): pass

    label("Function_25_8AFA")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xA, 84020, 0, 81160, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 2)
    OP_6F(0x0, 10)
    SetChrPos(0x8, 88750, 0, 78900, 270)
    ClearChrFlags(0x8, 0x80)
    OP_6D(83860, 0, 81320, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_8BA9():
        OP_6D(87450, 0, 79790, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8BA9)
    FadeToBright(1000, 0)
    Sleep(3000)
    SetChrSubChip(0x8, 3)
    Sleep(300)
    TurnDirection(0xA, 0x8, 400)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0xA, 0x153D8, 0x0, 0x138E4, 0x1388, 0x0)
    OP_8E(0xA, 0x153D8, 0x0, 0x1354C, 0x1388, 0x0)
    TurnDirection(0xA, 0x8, 400)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0111   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_25_8AFA end

    def Function_26_8C43(): pass

    label("Function_26_8C43")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x19)
    Return()

    # Function_26_8C43 end

    SaveToFile()

Try(main)
