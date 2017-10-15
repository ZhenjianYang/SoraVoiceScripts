from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131   ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1131   ._SN',
            'ED6_DT21/T1131_1 ._SN',
            'ED6_DT21/T1131_2 ._SN',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Manager Lechter',                      # 9
        'Head Chef Ross',                       # 10
        'Gwen',                                 # 11
        'Citron',                               # 12
        'Lenore',                               # 13
        'Horrace',                              # 14
        'Alta',                                 # 15
        'Caron',                                # 16
        'Shaque',                               # 17
        'Orvid',                                # 18
        'Felicity',                             # 19
        'Reina',                                # 20
        'Butler',                               # 21
        'Imperial Noble',                       # 22
        'Young Butler',                         # 23
        'Lucas',                                # 24
        'Elegia',                               # 25
        'Letta',                                # 26
        'Fannie',                               # 27
        'Warner',                               # 28
        'Platina',                              # 29
        'Lyndon',                               # 30
        'Katrina',                              # 31
        'Finel',                                # 32
        'Corna',                                # 33
        'Hardt',                                # 34
        'Zosimov',                              # 35
        '料理',                                 # 36
        'スプーン',                             # 37
        'Gantz',                                # 38
        'Mayor Maybelle',                       # 39
        'Lila',                                 # 40
        'スープ皿',                             # 41
        'スプーン',                             # 42
        'フォーク',                             # 43
        'フォーク',                             # 44
        'ナイフ',                               # 45
        'ナイフ',                               # 46
        'スープ皿',                             # 47
        'ワイン',                               # 48
        'スプーン',                             # 49
        'ティーポット',                         # 50
        'ティーポット',                         # 51
        'ティーポット',                         # 52
        'ティーポット',                         # 53
        'ボトル',                               # 54
        'ワイングラス',                         # 55
        'ティーポット',                         # 56
        'カップ',                               # 57
        'カップ',                               # 58
        'スープ皿',                             # 59
        'スプーン',                             # 60
        'ボトル',                               # 61
        'ワイングラス',                         # 62
        'デザート',                             # 63
        'デザート',                             # 64
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01280 ._CH',             # 01
        'ED6_DT07/CH02480 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH02540 ._CH',             # 04
        'ED6_DT07/CH01003 ._CH',             # 05
        'ED6_DT07/CH01183 ._CH',             # 06
        'ED6_DT07/CH01023 ._CH',             # 07
        'ED6_DT07/CH01123 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01220 ._CH',             # 0B
        'ED6_DT07/CH01223 ._CH',             # 0C
        'ED6_DT07/CH01570 ._CH',             # 0D
        'ED6_DT07/CH01093 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01053 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01180 ._CH',             # 14
        'ED6_DT07/CH01153 ._CH',             # 15
        'ED6_DT07/CH01143 ._CH',             # 16
        'ED6_DT07/CH01020 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
        'ED6_DT07/CH01270 ._CH',             # 1A
        'ED6_DT07/CH01050 ._CH',             # 1B
        'ED6_DT07/CH01660 ._CH',             # 1C
        'ED6_DT07/CH02490 ._CH',             # 1D
        'ED6_DT07/CH01040 ._CH',             # 1E
        'ED6_DT07/CH02360 ._CH',             # 1F
        'ED6_DT07/CH02370 ._CH',             # 20
        'ED6_DT07/CH01090 ._CH',             # 21
        'ED6_DT07/CH01453 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01280P._CP',             # 01
        'ED6_DT07/CH02480P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH02540P._CP',             # 04
        'ED6_DT07/CH01003P._CP',             # 05
        'ED6_DT07/CH01183P._CP',             # 06
        'ED6_DT07/CH01023P._CP',             # 07
        'ED6_DT07/CH01123P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01220P._CP',             # 0B
        'ED6_DT07/CH01223P._CP',             # 0C
        'ED6_DT07/CH01570P._CP',             # 0D
        'ED6_DT07/CH01093P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01053P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01180P._CP',             # 14
        'ED6_DT07/CH01153P._CP',             # 15
        'ED6_DT07/CH01143P._CP',             # 16
        'ED6_DT07/CH01020P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
        'ED6_DT07/CH01270P._CP',             # 1A
        'ED6_DT07/CH01050P._CP',             # 1B
        'ED6_DT07/CH01660P._CP',             # 1C
        'ED6_DT07/CH02490P._CP',             # 1D
        'ED6_DT07/CH01040P._CP',             # 1E
        'ED6_DT07/CH02360P._CP',             # 1F
        'ED6_DT07/CH02370P._CP',             # 20
        'ED6_DT07/CH01090P._CP',             # 21
        'ED6_DT07/CH01453P._CP',             # 22
    )

    DeclNpc(
        X                   = -42600,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 0,
        Y                   = 46700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -47450,
        Z                   = 0,
        Y                   = 44160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -42610,
        Z                   = 0,
        Y                   = 41570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -53300,
        Z                   = 1500,
        Y                   = 200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -48300,
        Z                   = 1650,
        Y                   = 10950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -36300,
        Z                   = 1650,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -54970,
        Z                   = 1600,
        Y                   = 5570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -55100,
        Z                   = 1600,
        Y                   = 2970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -33640,
        Z                   = 0,
        Y                   = 42550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -32930,
        Z                   = 1600,
        Y                   = 2650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -33800,
        Z                   = 1500,
        Y                   = 1300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -31760,
        Z                   = 1500,
        Y                   = 1300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -33060,
        Z                   = 1750,
        Y                   = 5350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -32560,
        Z                   = 1500,
        Y                   = 6200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -51940,
        Z                   = 1500,
        Y                   = 6490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -46030,
        Z                   = 0,
        Y                   = -1790,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -40300,
        Z                   = 1650,
        Y                   = 5950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -39100,
        Z                   = 1650,
        Y                   = 7340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 2970,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = 0,
        Y                   = 1480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -2790,
        Z                   = 0,
        Y                   = -5200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -2790,
        Z                   = 0,
        Y                   = -3690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = 1480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 4480,
        Z                   = 0,
        Y                   = 1520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = -7160,
        Z                   = 1580,
        Y                   = -4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = -6140,
        Z                   = 2250,
        Y                   = -4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262169,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6480,
        Z                   = 2250,
        Y                   = -4300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = -3980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -980,
        Z                   = 0,
        Y                   = -2730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -230,
        Z                   = 0,
        Y                   = -1730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 2150,
        Y                   = -1060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196633,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35750,
        Z                   = 2150,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1350,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47350,
        Z                   = 2150,
        Y                   = 11000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196633,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47200,
        Z                   = 2150,
        Y                   = 11400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327704,
        ChipIndex           = 0x18,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47650,
        Z                   = 2150,
        Y                   = 11050,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -46400,
        Z                   = 2200,
        Y                   = 11000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -55000,
        Z                   = 2200,
        Y                   = 4250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703961,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -55000,
        Z                   = 2200,
        Y                   = 4750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -55000,
        Z                   = 2200,
        Y                   = 3550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6490,
        Z                   = 2100,
        Y                   = -3560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6360,
        Z                   = 2100,
        Y                   = -4420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -33100,
        Z                   = 2200,
        Y                   = 4100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703961,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -33000,
        Z                   = 2200,
        Y                   = 4600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -33000,
        Z                   = 2200,
        Y                   = 3400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53250,
        Z                   = 2250,
        Y                   = -950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 524313,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53750,
        Z                   = 2150,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52920,
        Z                   = 2250,
        Y                   = -630,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53500,
        Z                   = 2150,
        Y                   = -630,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327704,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39550,
        Z                   = 2250,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -38990,
        Z                   = 2250,
        Y                   = 6430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3050,
        TriggerZ            = 0,
        TriggerY            = 1520,
        TriggerRange        = 400,
        ActorX              = 2970,
        ActorZ              = 1500,
        ActorY              = 3650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_8E6",          # 00, 0
        "Function_1_E56",          # 01, 1
        "Function_2_E8F",          # 02, 2
        "Function_3_EB3",          # 03, 3
        "Function_4_114C",         # 04, 4
        "Function_5_12CB",         # 05, 5
        "Function_6_12EF",         # 06, 6
        "Function_7_21DF",         # 07, 7
        "Function_8_2B69",         # 08, 8
        "Function_9_2BAE",         # 09, 9
        "Function_10_3B75",        # 0A, 10
        "Function_11_465E",        # 0B, 11
        "Function_12_5039",        # 0C, 12
        "Function_13_5ADC",        # 0D, 13
        "Function_14_65F4",        # 0E, 14
        "Function_15_6C51",        # 0F, 15
        "Function_16_7329",        # 10, 16
        "Function_17_9F1E",        # 11, 17
        "Function_18_A077",        # 12, 18
        "Function_19_A8B6",        # 13, 19
        "Function_20_AE69",        # 14, 20
        "Function_21_B423",        # 15, 21
        "Function_22_B7A9",        # 16, 22
        "Function_23_BE5E",        # 17, 23
        "Function_24_C645",        # 18, 24
        "Function_25_CA68",        # 19, 25
        "Function_26_CD9F",        # 1A, 26
        "Function_27_D31D",        # 1B, 27
        "Function_28_D495",        # 1C, 28
        "Function_29_D5FF",        # 1D, 29
        "Function_30_D604",        # 1E, 30
        "Function_31_E0D3",        # 1F, 31
        "Function_32_EAF2",        # 20, 32
        "Function_33_EC0B",        # 21, 33
        "Function_34_EF12",        # 22, 34
        "Function_35_F4F8",        # 23, 35
        "Function_36_F621",        # 24, 36
        "Function_37_F622",        # 25, 37
        "Function_38_F8A9",        # 26, 38
    )


    def Function_0_8E6(): pass

    label("Function_0_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_905")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 6)
    Jump("loc_92E")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_91B")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 10)
    Jump("loc_92E")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_92E")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(2, 4)

    label("loc_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_99D")
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_99A")

    label("loc_98B")

    ClearChrFlags(0x23, 0x80)
    SetChrSubChip(0x23, 8)
    ClearChrFlags(0x24, 0x80)

    label("loc_99A")

    Jump("loc_E1F")

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A5A")
    SetChrPos(0x2E, -47250, 2250, 11000, 90)
    SetChrSubChip(0x2E, 8)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    SetChrPos(0xB, -38500, 1500, 14200, 180)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x1C, -1230, 0, 4400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A57")
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 2400, 0, 1370, 0)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x38, 2250, 700, 2330, 0)

    label("loc_A57")

    Jump("loc_E1F")

    label("loc_A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B07")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -45760, 1550, 11100, 270)
    SetChrChipByIndex(0x17, 22)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -54180, 1600, -1120, 90)
    SetChrChipByIndex(0x18, 21)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -2790, 0, -4580, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -2790, 0, -3690, 90)
    Jump("loc_E1F")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_B9D")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -42360, 0, -1790, 0)
    OP_43(0x17, 0x0, 0x6, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -54180, 1650, -1120, 90)
    SetChrChipByIndex(0x18, 21)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -2790, 0, -4580, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -2790, 0, -3690, 90)
    Jump("loc_E1F")

    label("loc_B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D4B")
    ClearChrFlags(0x17, 0x80)
    OP_43(0x17, 0x0, 0x6, 0x2)
    ClearChrFlags(0x18, 0x80)
    OP_43(0x18, 0x0, 0x0, 0x5)
    SetChrPos(0xD, -52150, 1500, 8020, 180)
    SetChrChipByIndex(0xD, 19)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x1)
    OP_43(0xD, 0x0, 0x6, 0x2)
    SetChrPos(0xE, -36410, 1500, 90, 225)
    SetChrChipByIndex(0xE, 20)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x1)
    OP_43(0xE, 0x0, 0x6, 0x2)
    SetChrPos(0xF, -53390, 1500, 3430, 132)
    SetChrChipByIndex(0xF, 23)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x1)
    OP_43(0xF, 0x0, 0x6, 0x2)
    SetChrPos(0x10, -53720, 1500, 2050, 135)
    SetChrChipByIndex(0x10, 9)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x1)
    OP_43(0x10, 0x0, 0x6, 0x2)
    SetChrPos(0xC, -46440, 1500, 12150, 180)
    OP_43(0xC, 0x0, 0x6, 0x2)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1C, 140, 0, 1780, 180)
    OP_43(0x1C, 0x0, 0x6, 0x2)
    SetChrPos(0x12, -33720, 1500, 2810, 261)
    SetChrChipByIndex(0x12, 33)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x1)
    OP_43(0x12, 0x0, 0x6, 0x2)
    SetChrPos(0x15, -35370, 1500, 2950, 103)
    SetChrChipByIndex(0x15, 11)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x1)
    OP_43(0x15, 0x0, 0x6, 0x2)
    SetChrPos(0x14, -31820, 1500, 2029, 270)
    SetChrPos(0x13, -40690, 0, -510, 180)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_E1F")

    label("loc_D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_E1F")
    ClearChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9E")
    SetChrPos(0x13, -33800, 1500, 1300, 0)
    SetChrPos(0x14, -31760, 1500, 1300, 0)
    SetChrPos(0x12, -32930, 1600, 2650, 0)
    Jump("loc_E1F")

    label("loc_D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE4")
    SetChrPos(0x13, -47400, 0, -1660, 90)
    SetChrPos(0x14, -33780, 1500, 2840, 0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x14, 0x10)
    Jump("loc_E1F")

    label("loc_DE4")

    SetChrPos(0x13, -47400, 0, -1660, 180)
    SetChrPos(0x14, -47400, 0, -2880, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x39, 0x80)

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E2E")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_E55")

    label("loc_E2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E45")
    SetChrFlags(0xA, 0x10)

    label("loc_E45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_E55")
    ClearChrFlags(0x11, 0x80)

    label("loc_E55")

    Return()

    # Function_0_8E6 end

    def Function_1_E56(): pass

    label("Function_1_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6E")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x5, 0x1)

    label("loc_E6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8E")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)

    label("loc_E8E")

    Return()

    # Function_1_E56 end

    def Function_2_E8F(): pass

    label("Function_2_E8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EB2")
    OP_8D(0xFE, -48200, 42570, -46450, 46500, 1000)
    Jump("Function_2_E8F")

    label("loc_EB2")

    Return()

    # Function_2_E8F end

    def Function_3_EB3(): pass

    label("Function_3_EB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_114B")
    OP_8E(0xFE, 0xFFFF2CFC, 0x5DC, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF3350, 0x5DC, 0xCE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x21FC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2580, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D18, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF4D7C, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5FD8, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x1F40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6DE8, 0x5DC, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF72FC, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF748C, 0x5DC, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF7428, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7748, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x960, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF3990, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x1CE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x9C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF2FCC, 0x5DC, 0xC8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    Jump("Function_3_EB3")

    label("loc_114B")

    Return()

    # Function_3_EB3 end

    def Function_4_114C(): pass

    label("Function_4_114C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12CA")
    Sleep(2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1175")
    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x3C, 0x7D0, 0x0)

    label("loc_1175")

    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_12A7")
    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x3C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB32, 0x0, 0x1130, 0x7D0, 0x0)
    Jump("loc_12BB")

    label("loc_12A7")

    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)

    label("loc_12BB")

    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("Function_4_114C")

    label("loc_12CA")

    Return()

    # Function_4_114C end

    def Function_5_12CB(): pass

    label("Function_5_12CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12EE")
    OP_8D(0xFE, -47100, -2490, -44490, -1060, 2000)
    Jump("Function_5_12CB")

    label("loc_12EE")

    Return()

    # Function_5_12CB end

    def Function_6_12EF(): pass

    label("Function_6_12EF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1445")

    ChrTalk(    #0
        0xFE,
        (
            "The liners being suspended has\x01",
            "proved to be quite the predicament\x01",
            "for our establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "We pride ourselves in serving only the finest\x01",
            "of wines from across the land, so losing access\x01",
            "to the skies reduces our stock significantly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I pray from the depths of my heart\x01",
            "that service will be restored quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1534")

    label("loc_1445")


    ChrTalk(    #3
        0xFE,
        (
            "The liners being suspended has\x01",
            "proved to be quite the predicament\x01",
            "for our establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "We pride ourselves in serving only the finest\x01",
            "of wines from across the land, so losing access\x01",
            "to the skies reduces our stock significantly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1534")

    Jump("loc_21DB")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170D")

    ChrTalk(    #5
        0xFE,
        (
            "Mayor Maybelle has been running herself\x01",
            "ragged trying to address every little thing\x01",
            "with the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Yet she still somehow manages to keep\x01",
            "popping her head back here between meetings\x01",
            "to make sure things are running smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I tell her time and time again not to worry\x01",
            "about the restaurant, but she won't hear a\x01",
            "word of it, of course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "She so much like her father in that respect--\x01",
            "always pushing herself too hard for her own\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_17F6")

    label("loc_170D")


    ChrTalk(    #9
        0xFE,
        (
            "Mayor Maybelle has been running herself\x01",
            "ragged trying to address every little thing\x01",
            "with the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Yet she still somehow manages to keep\x01",
            "popping her head back here between meetings\x01",
            "to make sure things are running smoothly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F6")

    Jump("loc_21DB")

    label("loc_17F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_19DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18A0")

    ChrTalk(    #11
        0xFE,
        (
            "The city's finally returned to normal,\x01",
            "and my palate returns along with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Truly, there's no finer complement for\x01",
            "wine than peaceful days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D8")

    label("loc_18A0")


    ChrTalk(    #13
        0xFE,
        "Welcome to the Anterose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Things are finally back to normal. It's hard\x01",
            "to really appreciate wine when there are\x01",
            "so many distractions and unrest in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "There's a saying that 'hunger is the greatest\x01",
            "spice,' but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "In my experience, I would say that\x01",
            "peace is the greatest hidden flavor.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_19D8")

    Jump("loc_21DB")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(    #17
        0xFE,
        (
            "Perhaps you've heard that the owner of\x01",
            "this fine establishment is none other than\x01",
            "Mayor Maybelle herself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "With her managing both the restoration of\x01",
            "the market and Ravennue, however, she's hardly\x01",
            "in any position to worry about the restaurant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C54")

    label("loc_1AE8")


    ChrTalk(    #19
        0xFE,
        (
            "Perhaps you've heard that the owner\x01",
            "of this establishment is none other than\x01",
            "Mayor Maybelle herself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "With her managing both the restoration of\x01",
            "the market and Ravennue, however, she's hardly\x01",
            "in any position to worry about the restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "We'd hate to see her burdened with more\x01",
            "than she can handle, so we'll be doing all\x01",
            "we can here in her place.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1C54")

    Jump("loc_21DB")

    label("loc_1C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D04")

    ChrTalk(    #22
        0xFE,
        (
            "Things may be a tad chaotic at the\x01",
            "moment, but we'll continue to stay open\x01",
            "for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Come by any time--it would be our\x01",
            "pleasure to serve you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E71")

    label("loc_1D04")


    ChrTalk(    #24
        0xFE,
        (
            "Welcome. Yesterday was most frightful,\x01",
            "wasn't it? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Still, the merchants here are known for\x01",
            "banding together to help in times of crisis,\x01",
            "and yesterday was no exception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Even our restaurant once helped\x01",
            "distribute emergency rations during\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Should it be required, it would be our\x01",
            "honor to provide to those in need once\x01",
            "more.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1E71")

    Jump("loc_21DB")

    label("loc_1E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EE6")

    ChrTalk(    #28
        0xFE,
        (
            "We've received word from the owner\x01",
            "that the situation is more severe than\x01",
            "we'd anticipated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEB")

    label("loc_1EE6")


    ChrTalk(    #29
        0xFE,
        (
            "We've received word from the owner\x01",
            "that the situation is more severe than\x01",
            "we'd anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Thankfully, we'd already started\x01",
            "preparing plenty of soup for those\x01",
            "who evacuated here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Nothing helps to calm the mind\x01",
            "quite like a warm bowl of soup.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1FEB")

    Jump("loc_21DB")

    label("loc_1FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_21DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20A8")

    ChrTalk(    #32
        0xFE,
        (
            "By all means, I more than welcome\x01",
            "you to come and taste the best that\x01",
            "Liberlian cuisine has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Come by any time--it would be our\x01",
            "pleasure to serve you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DB")

    label("loc_20A8")


    ChrTalk(    #34
        0xFE,
        "Welcome to the Anterose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Our restaurant has long been lauded for\x01",
            "selecting only the most superlative ingredients\x01",
            "to complement a marvelous dining experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Ah, but seeing is believing. By all means,\x01",
            "I more than welcome you to come and taste\x01",
            "the best that Liberlian cuisine has to offer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_21DB")

    TalkEnd(0x8)
    Return()

    # Function_6_12EF end

    def Function_7_21DF(): pass

    label("Function_7_21DF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DF")

    ChrTalk(    #37
        0xFE,
        "That new merchant's something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "We haven't had any problems getting\x01",
            "specialized ingredients in stock thanks\x01",
            "to him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D9")

    ChrTalk(    #39
        0xFE,
        (
            "I owe you guys big. You introduced us\x01",
            "to someone who really knows their stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D9")

    OP_A2(0x1)
    Jump("loc_2335")

    label("loc_22DF")


    ChrTalk(    #40
        0xFE,
        "That new merchant's something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Even if his stock's a little...extreme.\x02",
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_2B65")

    label("loc_2338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_23D6")

    ChrTalk(    #42
        0xFE,
        (
            "Eh, working without orbal cooking\x01",
            "tools is no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "You aren't a real chef if you need\x01",
            "some fancy equipment to whip up\x01",
            "a decent meal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B65")

    label("loc_23D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_24B5")

    ChrTalk(    #44
        0xFE,
        (
            "We were having trouble for a while,\x01",
            "but now I've got all the ingredients a\x01",
            "guy could ask for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "It wasn't easy to be so conservative\x01",
            "with our stock. I'm ready to cook up\x01",
            "exotic meals like the best of 'em!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B65")

    label("loc_24B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2703")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25CF")

    ChrTalk(    #46
        0xFE,
        (
            "With the liners out of commission,\x01",
            "restocking the larder's starting to be\x01",
            "a real pain... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I'm hoping that new merchant will\x01",
            "be able to make things easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "It's not like we've got a whole lot of\x01",
            "variety, but the larder IS pretty full.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2700")

    label("loc_25CF")


    ChrTalk(    #49
        0xFE,
        (
            "With the liners out of commission,\x01",
            "though, restocking is starting to be\x01",
            "a real pain... \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "If this drags out much longer, I might\x01",
            "have to cut back on our menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I'd like to avoid that if I can. I mean, we have\x01",
            "guests coming from all over to try our dishes.\x01",
            "I want to make it worth their while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2700")

    Jump("loc_2B65")

    label("loc_2703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_28B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_280C")

    ChrTalk(    #52
        0xFE,
        (
            "The scheduled liners aren't running\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I hope they do something about it soon.\x01",
            "It's only going to get harder to restock\x01",
            "ingredients if this keeps up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Maybe we can expect something from\x01",
            "that newbie merchant...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B4")

    label("loc_280C")


    ChrTalk(    #55
        0xFE,
        (
            "The scheduled liners aren't running\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I hope they do something about it soon.\x01",
            "It's only going to get harder to restock\x01",
            "ingredients if this keeps up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B4")

    Jump("loc_2B65")

    label("loc_28B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2923")

    ChrTalk(    #57
        0xFE,
        (
            "The manager just ordered some soup,\x01",
            "and he was pale as a ghost...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B65")

    label("loc_2923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_29EF")

    ChrTalk(    #59
        0xFE,
        (
            "I've finally put a dish that Gwen thought\x01",
            "up on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "It's so different compared to our usual\x01",
            "stuff. She really brings out her own\x01",
            "personal style with every dish she cooks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B65")

    label("loc_29EF")


    ChrTalk(    #61
        0xFE,
        (
            "I've finally put a dish that Gwen thought\x01",
            "up on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "It's so different compared to our usual\x01",
            "stuff. She really brings out her own\x01",
            "personal style with every dish she cooks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "To constantly surprise and delight your\x01",
            "guests, a fluid menu is best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "To be a top-class chef, you must also have\x01",
            "the power to innovate outside of your culinary\x01",
            "comfort zone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2B65")

    TalkEnd(0x9)
    Return()

    # Function_7_21DF end

    def Function_8_2B69(): pass

    label("Function_8_2B69")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B84")
    Call(0, 9)
    Jump("loc_2BAA")

    label("loc_2B84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2B95")
    Call(2, 1)
    Jump("loc_2BAA")

    label("loc_2B95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2BA6")
    Call(2, 0)
    Jump("loc_2BAA")

    label("loc_2BA6")

    Call(0, 9)

    label("loc_2BAA")

    TalkEnd(0xA)
    Return()

    # Function_8_2B69 end

    def Function_9_2BAE(): pass

    label("Function_9_2BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2C29")

    ChrTalk(    #65
        0xA,
        "Thanks for today! It was a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "If you've ever got some time,\x01",
            "come by and have a meal, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B74")

    label("loc_2C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2E21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D94")

    ChrTalk(    #67
        0xA,
        "Head Chef Ross is just amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "None of the orbal equipment is\x01",
            "working, but the meals he's putting\x01",
            "out haven't dropped in quality a whit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "I'm still an amateur by comparison...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "All right, I'm on fire now! I've just\x01",
            "gotta work until I'm as awesome\x01",
            "as he is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "I'll surpass the head chef someday.\x01",
            "You just wait and see!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2E1E")

    label("loc_2D94")


    ChrTalk(    #72
        0xA,
        (
            "Compared to the head chef,\x01",
            "I'm just an amateur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "All right, I'm on fire now! I've just\x01",
            "gotta work until I'm as awesome\x01",
            "as he is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1E")

    Jump("loc_3B74")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F00")

    ChrTalk(    #74
        0xA,
        "The orbal stove's not working...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "The head chef's waving it off\x01",
            "like it's no big deal, but to me,\x01",
            "it's a huge, HUGE deal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "I've got to learn how to work an\x01",
            "old-fashioned stove, and fast...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2F79")

    label("loc_2F00")


    ChrTalk(    #77
        0xA,
        "The orbal stove's not working...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "Mmmm... I don't even know if I could\x01",
            "even boil an egg well on a fire stove...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F79")

    Jump("loc_3B74")

    label("loc_2F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_32A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_305A")

    ChrTalk(    #79
        0xA,
        (
            "The scheduled liners are running now.\x01",
            "We can get stuff in stock normally again!\x01",
            "Woohoo!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "We can finally put together a brand\x01",
            "new menu. And believe me, I'm up for\x01",
            "the challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3197")

    label("loc_305A")


    ChrTalk(    #81
        0xA,
        (
            "The scheduled liners are running now.\x01",
            "We can get stuff in stock normally again!\x01",
            "Woohoo!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "Seems like that new merchant's gonna\x01",
            "get us any rare ingredients we need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "We could finally put together a brand\x01",
            "new menu this way. And believe me,\x01",
            "I'm up for the challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        "All right, time to get serious!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3197")

    Jump("loc_32A6")

    label("loc_319A")


    ChrTalk(    #85
        0xA,
        (
            "The scheduled liners are running\x01",
            "now, and we can get stuff in stock\x01",
            "normally again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "It's still hard to get certain rare ingredients,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "It'd sure be nice if we could get some\x01",
            "nice, rare ingredients in stock. We could\x01",
            "put together a whole new menu!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32A6")

    Jump("loc_3B74")

    label("loc_32A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3607")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_346C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3345")

    ChrTalk(    #88
        0xA,
        (
            "The head chef's worrying about our\x01",
            "stock, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "I hope working together with Orvid\x01",
            "will fix things around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3469")

    label("loc_3345")


    ChrTalk(    #90
        0xA,
        (
            "The head chef's worrying about our\x01",
            "stock, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "I hope working together with Orvid\x01",
            "will fix things around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "I don't know why, but he hasn't been\x01",
            "bothered one bit by the scheduled flights\x01",
            "stopping at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "Does he have some different sources\x01",
            "than the other merchants?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3469")

    Jump("loc_3604")

    label("loc_346C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_351E")

    ChrTalk(    #94
        0xA,
        (
            "The head chef's worrying about our\x01",
            "stock, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "The merchants have been so focused\x01",
            "on the market that they just don't have\x01",
            "the time to work with us, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3604")

    label("loc_351E")


    ChrTalk(    #96
        0xA,
        (
            "The head chef's worrying about our\x01",
            "stock, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "The merchants have been so focused\x01",
            "on the market that they just don't have\x01",
            "the time to work with us, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "*sigh* Anxiety really dulls the taste buds,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3604")

    Jump("loc_3B74")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_37E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_36E9")

    ChrTalk(    #99
        0xA,
        (
            "I heard from Lenore that there's\x01",
            "a customer out there who's having\x01",
            "a meeting for an arranged marriage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "Wedding talk's some heavy-duty stuff,\x01",
            "but I hope our dishes can help lighten\x01",
            "the mood for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DD")

    label("loc_36E9")


    ChrTalk(    #101
        0xA,
        (
            "I heard from Lenore that there's\x01",
            "a customer out there who's having\x01",
            "a meeting for an arranged marriage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        "Talk about pressure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "What if things go wrong because we\x01",
            "serve a bad meal? Atmosphere means\x01",
            "everything at times like this\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_37DD")

    Jump("loc_3B74")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_38AD")

    ChrTalk(    #104
        0xA,
        (
            "There's some kind of fuss happening\x01",
            "out front...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "That's the least of my worries, now,\x01",
            "though. I've gotta finish prepping for\x01",
            "the main course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        "All right, gotta focus! Focus!\x02",
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_38AD")


    ChrTalk(    #107
        0xA,
        (
            "There's some kind of fuss happening\x01",
            "out front...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "That's the least of my worries, now,\x01",
            "though. I've gotta finish prepping for\x01",
            "the main course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "Slacking off here can seriously jam\x01",
            "you up later when you need to start\x01",
            "cooking.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_399E")

    Jump("loc_3B74")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A29")

    ChrTalk(    #110
        0xA,
        "A dish I made is finally on the menu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "But I can't let myself be satisfied by\x01",
            "this. I gotta work even harder!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B74")

    label("loc_3A29")


    ChrTalk(    #112
        0xA,
        "A dish I made is finally on the menu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "I'm super happy, but it's really all\x01",
            "thanks to the head chef staying late\x01",
            "to help me test out my ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "I won't be satisfied until I can create\x01",
            "a dish all on my own, though! No siree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "That's exactly why I'm going to start\x01",
            "experimenting with my next new dish\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3B74")

    Return()

    # Function_9_2BAE end

    def Function_10_3B75(): pass

    label("Function_10_3B75")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0E")

    ChrTalk(    #116
        0xFE,
        "The airship flights STILL haven't resumed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Right as I was gonna order some wine,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "*sigh* What awful timing...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3C6E")

    label("loc_3C0E")


    ChrTalk(    #119
        0xFE,
        "The airship flights STILL haven't resumed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Right as I was gonna order some wine,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6E")

    Jump("loc_465A")

    label("loc_3C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6B")

    ChrTalk(    #121
        0xFE,
        (
            "I was in the wine cellar when the\x01",
            "orbments all stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Thanks to that, I ended up having\x01",
            "to find my way out by hand in total\x01",
            "darkness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I was covered head to toe in dust by\x01",
            "the time I got out. What awful timing...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3DF6")

    label("loc_3D6B")


    ChrTalk(    #124
        0xFE,
        (
            "I was in the wine cellar when the\x01",
            "orbments all stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I ended up having to find my way out\x01",
            "by hand in total darkness, damn it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF6")

    Jump("loc_465A")

    label("loc_3DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3E82")

    ChrTalk(    #126
        0xFE,
        (
            "Thank Aidios. We finally got some\x01",
            "wine delivered this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "We were dangerously close to\x01",
            "running out, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F86")

    label("loc_3E82")


    ChrTalk(    #128
        0xFE,
        (
            "Thank Aidios. We finally got some\x01",
            "wine delivered this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I freak out every time an airship\x01",
            "stops by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Still, airships are the whole reason\x01",
            "we can drink liquor from around the\x01",
            "world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Hard to complain too much with\x01",
            "perks like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3F86")

    Jump("loc_465A")

    label("loc_3F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_41A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4023")

    ChrTalk(    #132
        0xFE,
        (
            "The flight restrictions on Bose\x01",
            "airspace still haven't been lifted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "We're almost totally out of\x01",
            "certain brands of wine, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_419D")

    label("loc_4023")


    ChrTalk(    #134
        0xFE,
        "What awful timing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "The flight restrictions on Bose\x01",
            "airspace still haven't been lifted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "We're almost totally out of\x01",
            "certain brands of wine, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "The wines we're running out of,\x01",
            "from a price perspective, are the\x01",
            "middle-of-the-road brands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "We get a lot of connoisseurs here,\x01",
            "and they've all got an eye for the best\x01",
            "wines for the least amount of mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_419D")

    Jump("loc_465A")

    label("loc_41A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_432C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4236")

    ChrTalk(    #139
        0xFE,
        (
            "Thanks to the army's plan,\x01",
            "all airships have been stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "If this goes on for too long,\x01",
            "we'll be short on wines to serve.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4329")

    label("loc_4236")


    ChrTalk(    #141
        0xFE,
        "What awful timing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Thanks to the army's plan,\x01",
            "all airships have been stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "We were supposed to get some\x01",
            "North Ambrian wines in, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I wish they'd just hurry up and\x01",
            "catch this dragon and lift flight\x01",
            "restrictions.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4329")

    Jump("loc_465A")

    label("loc_432C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4392")

    ChrTalk(    #145
        0xFE,
        (
            "I don't know the details,\x01",
            "but something big went down\x01",
            "outside, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4435")

    label("loc_4392")


    ChrTalk(    #146
        0xFE,
        (
            "I don't know the details,\x01",
            "but something big went down\x01",
            "outside, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "We can at least put out some\x01",
            "cases of mineral water for now,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_4435")

    Jump("loc_465A")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_465A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_44DF")

    ChrTalk(    #148
        0xFE,
        (
            "The manager and I have been\x01",
            "talking, and we're thinking of getting\x01",
            "some sake from the Eastern lands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "It's got a flavor as rich as any wine!\x02",
    )

    CloseMessageWindow()
    Jump("loc_465A")

    label("loc_44DF")


    ChrTalk(    #150
        0xFE,
        "I'm the sommelier at this restaurant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "I know most people think of wine\x01",
            "when you say 'sommelier,' but I handle\x01",
            "all kinds of liquors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "The manager and I have been talking,\x01",
            "and we're even thinking of getting\x01",
            "some sake from the Eastern lands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "It's got a flavor as rich as any wine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I have a hunch that it'll work better\x01",
            "with lighter dishes than wine, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_465A")

    TalkEnd(0xB)
    Return()

    # Function_10_3B75 end

    def Function_11_465E(): pass

    label("Function_11_465E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_477E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_470B")

    ChrTalk(    #155
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "The town's finally calmed down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Please, take all the time you need\x01",
            "too enjoy your dining experience to\x01",
            "your heart's content.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_477B")

    label("loc_470B")


    ChrTalk(    #158
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "Please, take all the time you need\x01",
            "too enjoy your dining experience to\x01",
            "your heart's content.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477B")

    Jump("loc_5035")

    label("loc_477E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C5")

    ChrTalk(    #160
        0xFE,
        (
            "We were in the restaurant when the\x01",
            "riots erupted in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "A lot of people were gathered in front\x01",
            "of the guild, and they spent all night\x01",
            "yelling at each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "The restaurant was pitch black, too,\x01",
            "so I couldn't tell what was going on\x01",
            "at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "You wouldn't believe how scared I\x01",
            "was.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_4972")

    label("loc_48C5")


    ChrTalk(    #164
        0xFE,
        (
            "We were in the restaurant when the\x01",
            "riots erupted in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "A lot of people were gathered in front\x01",
            "of the guild, and they spent all night\x01",
            "yelling at each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4972")

    Jump("loc_5035")

    label("loc_4975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4A28")

    ChrTalk(    #166
        0xFE,
        (
            "That Imperial gentleman who came\x01",
            "for the arranged marriage meeting has\x01",
            "already gone home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "The young lady he was meeting with\x01",
            "has returned home as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B67")

    label("loc_4A28")


    ChrTalk(    #168
        0xFE,
        (
            "That Imperial gentleman who came\x01",
            "for the arranged marriage meeting\x01",
            "has already left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "The young lady he was meeting with\x01",
            "has returned home as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "*sigh* The two of them must have\x01",
            "been born into well-to-do families,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Here they were, in our restaurant,\x01",
            "talking marriage proposals!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4B67")

    Jump("loc_5035")

    label("loc_4B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4BE7")

    ChrTalk(    #172
        0xFE,
        (
            "Everyone's working hard to restore\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "I can hear the pounding of the\x01",
            "hammers at work from here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5035")

    label("loc_4BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4D9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4CA3")

    ChrTalk(    #174
        0xFE,
        (
            "No matter how you slice it, that girl's\x01",
            "only a student, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "Kind of early for her to be thinking\x01",
            "about marriage, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "Or am I being too naive here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9C")

    label("loc_4CA3")


    ChrTalk(    #177
        0xFE,
        (
            "Apparently, there's a meeting for an\x01",
            "arranged marriage happening at that\x01",
            "table over there as we speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "No matter how you slice it, that girl's\x01",
            "only a student, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "K-Kind of early for her to be thinking\x01",
            "about marriage, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4D9C")

    Jump("loc_5035")

    label("loc_4D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4E27")

    ChrTalk(    #180
        0xFE,
        (
            "Is it true the market was attacked\x01",
            "by an enormous monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I hope I have enough seats for all\x01",
            "the evacuees. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8A")

    label("loc_4E27")


    ChrTalk(    #182
        0xFE,
        (
            "Is it true the market was attacked\x01",
            "by an enormous monster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "I... I can't believe it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4E8A")

    Jump("loc_5035")

    label("loc_4E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5035")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F2B")

    ChrTalk(    #184
        0xFE,
        (
            "The young lady that gentleman\x01",
            "was waiting for appears to have\x01",
            "arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "What a relief! Now we can finally\x01",
            "serve them their food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5035")

    label("loc_4F2B")


    ChrTalk(    #186
        0xFE,
        (
            "We had a reservation put in by a guest\x01",
            "from the Empire a while back, and he'll\x01",
            "be coming in later today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "You would not believe what he's here for!\x01",
            "Get this--it's a meeting for an ARRANGED\x01",
            "MARRIAGE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "Makes me wonder if he's meeting\x01",
            "someone from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5035")

    TalkEnd(0xC)
    Return()

    # Function_11_465E end

    def Function_12_5039(): pass

    label("Function_12_5039")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_51F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5140")

    ChrTalk(    #189
        0xFE,
        (
            "Hmm, hmm... Well! Why, it tastes\x01",
            "the same as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "The Anterose doesn't have access\x01",
            "to its orbal stoves now, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "I suppose this comes as no surprise.\x01",
            "Only they would know how to maintain\x01",
            "such standards during a blackout.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_51F5")

    label("loc_5140")


    ChrTalk(    #192
        0xFE,
        (
            "The Anterose doesn't have access\x01",
            "to its orbal stoves now, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I suppose this comes as no surprise.\x01",
            "Only they would know how to maintain\x01",
            "such standards during a blackout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F5")

    Jump("loc_5AD8")

    label("loc_51F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_532E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C9")

    ChrTalk(    #194
        0xFE,
        (
            "I thought it was just my orbments\x01",
            "that were broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "One look around the city, however,\x01",
            "and it was plain to see the problem\x01",
            "extended far beyond myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "Whatever shall we do?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_532B")

    label("loc_52C9")


    ChrTalk(    #197
        0xFE,
        (
            "This problem is more than a few\x01",
            "broken orbments here and there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "Most curious, indeed...\x02",
    )

    CloseMessageWindow()

    label("loc_532B")

    Jump("loc_5AD8")

    label("loc_532E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_54F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_53D7")

    ChrTalk(    #199
        0xFE,
        (
            "It's always a joy to talk with\x01",
            "the young--they're always so\x01",
            "rich with inspiration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "Truly, I wish that young man\x01",
            "all the success in the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F4")

    label("loc_53D7")


    ChrTalk(    #201
        0xFE,
        (
            "I've been talking business with\x01",
            "this fascinating new merchant\x01",
            "over the last few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Ah, to converse with the young! I thought\x01",
            "to give him a few pointers and instead found\x01",
            "myself inspired by his youthful vigor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Ho ho ho! I hope we get the chance to\x01",
            "chat again soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_54F4")

    Jump("loc_5AD8")

    label("loc_54F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_55ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_55E6")

    ChrTalk(    #204
        0xFE,
        (
            "The best businessman know that the\x01",
            "only way to connect with your clients is\x01",
            "the the old-fashioned way: face to face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "If you spend all your time chase after\x01",
            "numbers, it'll always come back to bite\x01",
            "you in the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55EA")

    label("loc_55E6")

    Call(0, 25)

    label("loc_55EA")

    Jump("loc_5AD8")

    label("loc_55ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_57A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5683")

    ChrTalk(    #206
        0xFE,
        (
            "Just yesterday, I met a young man\x01",
            "who told me he's about to set up shop\x01",
            "in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "We agreed to meet here later today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_57A2")

    label("loc_5683")


    ChrTalk(    #208
        0xFE,
        (
            "Just yesterday, I met a young man\x01",
            "who told me he's about to set up shop\x01",
            "in the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "I thought I'd offer him some business\x01",
            "advice, so we agreed to meet here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "Ho ho ho! Passing along advice to the\x01",
            "young is but one of the many wonderful\x01",
            "pleasures of the elderly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_57A2")

    Jump("loc_5AD8")

    label("loc_57A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_58AB")

    ChrTalk(    #211
        0xFE,
        (
            "This man here had the misfortune of\x01",
            "getting caught up in that whole monster\x01",
            "mess, all while trying to open his store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "I wish there was some way I could help.\x01",
            "I remember getting my start in the very\x01",
            "same market back in my younger days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A07")

    label("loc_58AB")


    ChrTalk(    #213
        0xFE,
        (
            "Some enormous monster attacked\x01",
            "the market!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "And this young man here had the nasty\x01",
            "misfortune of getting caught up in it,\x01",
            "all while preparing to open his new store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "I wish there was some way I could help...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "I know how very well hard it is to get your\x01",
            "start in the market--I myself went through\x01",
            "as much back in my younger days.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5A07")

    Jump("loc_5AD8")

    label("loc_5A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_5AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5A30")

    ChrTalk(    #217
        0xFE,
        "*slurp* *slurp*\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AD8")

    label("loc_5A30")


    ChrTalk(    #218
        0xFE,
        "*slurp* *slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "This new potage is positively divine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "The food here never ceases to keep\x01",
            "me on my toes. I'm always eager to\x01",
            "try their latest dishes. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5AD8")

    TalkEnd(0xD)
    Return()

    # Function_12_5039 end

    def Function_13_5ADC(): pass

    label("Function_13_5ADC")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_5CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C04")

    ChrTalk(    #221
        0xFE,
        (
            "The smiles are finally returning to\x01",
            "the townspeople at last. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "I do worry, though--how long will it\x01",
            "be until orbments are up and running\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "As much as I'd love to put a smile on\x01",
            "like everyone else, the thought that\x01",
            "they may never work again haunts me...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_5CC0")

    label("loc_5C04")


    ChrTalk(    #224
        0xFE,
        (
            "I wonder how much longer it'll be until\x01",
            "the orbments are fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "As much as I'd love to put a smile on\x01",
            "like everyone else, the thought that\x01",
            "they may never work again haunts me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC0")

    Jump("loc_65F0")

    label("loc_5CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DEA")

    ChrTalk(    #226
        0xFE,
        "All the commotion was terrifying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "If not for Mayor Maybelle, we would've\x01",
            "had riots on our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "It's times like these when people\x01",
            "need to be at their best and work\x01",
            "together, not behave like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "I hope to never see such shameful\x01",
            "behavior ever again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_5E55")

    label("loc_5DEA")


    ChrTalk(    #230
        0xFE,
        "All the commotion was terrifying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "If not for Mayor Maybelle, we would've\x01",
            "had riots on our hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E55")

    Jump("loc_65F0")

    label("loc_5E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_5FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5EC1")

    ChrTalk(    #232
        0xFE,
        (
            "So this potage is a new dish,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "Mmmmm! It's delicious!\x01",
            "Simply delicious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDC")

    label("loc_5EC1")


    ChrTalk(    #234
        0xFE,
        (
            "Oh, my. I hadn't even realized\x01",
            "until just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "This delectable potage is a new\x01",
            "dish on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "How silly of me! I've had it so many\x01",
            "times that it just feels like a classic\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "*sigh* All the turmoil that's come\x01",
            "about in recent days has worried\x01",
            "me so.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_5FDC")

    Jump("loc_65F0")

    label("loc_5FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_61E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_607E")

    ChrTalk(    #238
        0xFE,
        (
            "Mayor Maybelle is managing things\x01",
            "quite well, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "I'm sure her father and Aidios are\x01",
            "beside her, smiling wholeheartedly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E0")

    label("loc_607E")


    ChrTalk(    #240
        0xFE,
        (
            "Our former mayor's political\x01",
            "savviness was something to\x01",
            "behold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Fortunately for us, our current mayor,\x01",
            "Mayor Maybelle, happens to be his\x01",
            "daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "Oh, she gets compared to her father\x01",
            "plenty, naturally, but she's done a fine\x01",
            "job carving out a name for herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "I'm sure her father and Aidios are\x01",
            "beside her, smiling wholeheartedly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_61E0")

    Jump("loc_65F0")

    label("loc_61E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_62D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6246")

    ChrTalk(    #244
        0xFE,
        (
            "Looking at the state of the city\x01",
            "right now reminds me of the war...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62CD")

    label("loc_6246")


    ChrTalk(    #246
        0xFE,
        (
            "Repair work on the market,\x01",
            "army men strutting down the\x01",
            "streets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "It's the same as after the\x01",
            "Hundred Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_62CD")

    Jump("loc_65F0")

    label("loc_62D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_6459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_637B")

    ChrTalk(    #249
        0xFE,
        (
            "All those awful sounds made\x01",
            "me feel like we were reliving the\x01",
            "Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "Whenever stone buildings collapse,\x01",
            "there's always that sound...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6456")

    label("loc_637B")


    ChrTalk(    #251
        0xFE,
        "I heard an awful noise just now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "It reminded me of the\x01",
            "Hundred Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "I'd heard it then, too. The city was\x01",
            "filled with that terrible, terrible sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "The sound...of buildings collapsing...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_6456")

    Jump("loc_65F0")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_65F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_64E0")

    ChrTalk(    #255
        0xFE,
        (
            "It's not uncommon to see Imperials\x01",
            "around here now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I can't help but feel uncomfortable\x01",
            "around them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65F0")

    label("loc_64E0")


    ChrTalk(    #257
        0xFE,
        (
            "By all appearances, the man at that\x01",
            "table is from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "I know a non-aggression pact was signed,\x01",
            "and there's not as much tension hovering\x01",
            "in the background as there used to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "...Still, I can't help but feel\x01",
            "uncomfortable about the whole\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_65F0")

    TalkEnd(0xE)
    Return()

    # Function_13_5ADC end

    def Function_14_65F4(): pass

    label("Function_14_65F4")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6665")

    ChrTalk(    #260
        0xFE,
        (
            "I hurried over here as soon\x01",
            "as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "All right, let's get down to business.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_6691")

    label("loc_6665")


    ChrTalk(    #262
        0xFE,
        "All right, let's get down to business.\x02",
    )

    CloseMessageWindow()

    label("loc_6691")

    Jump("loc_6C4D")

    label("loc_6694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_67A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_66CF")

    ChrTalk(    #263
        0xFE,
        "Thank you so much for all your help!\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A2")

    label("loc_66CF")


    ChrTalk(    #264
        0xFE,
        "Thank you so much for all your help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "I was wondering how things would\x01",
            "turn out with the market closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "Thanks to you, not only did we\x01",
            "manage to minimize the damage,\x01",
            "we've even turned a profit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_67A2")

    Jump("loc_6C4D")

    label("loc_67A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_6994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_687B")

    ChrTalk(    #267
        0xFE,
        (
            "If you're ever in need of fruit stock,\x01",
            "our company would be more than\x01",
            "happy to provide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "No, it's precisely because this is\x01",
            "an emergency situation that we'll\x01",
            "be keeping prices reasonable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6991")

    label("loc_687B")


    ChrTalk(    #269
        0xFE,
        (
            "If you're looking for Ravennue\x01",
            "produce, our company will be\x01",
            "happy to provide from our stores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "You seem to be in a bit of a fix,\x01",
            "so we'd be glad to help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "No, it's precisely because this is\x01",
            "an emergency situation that we'll\x01",
            "be keeping prices reasonable.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_6991")

    Jump("loc_6C4D")

    label("loc_6994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_6A3D")

    ChrTalk(    #272
        0xFE,
        (
            "First the market closed, now the\x01",
            "scheduled liners have stopped, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "Boy, what a mess! We won't be\x01",
            "able to ship our stock around if\x01",
            "this keeps up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C4D")

    label("loc_6A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_6BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_6AE2")

    ChrTalk(    #274
        0xFE,
        (
            "With the market closed, prices are\x01",
            "bound to fluctuate drastically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "Ugh... We're gonna have rework our\x01",
            "pricing model from the ground up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BB6")

    label("loc_6AE2")


    ChrTalk(    #276
        0xFE,
        (
            "You're kidding me! THAT'S what\x01",
            "happened at the market?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Ugh... We're gonna have rework our\x01",
            "pricing model from the ground up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "With the market closed, prices are\x01",
            "bound to fluctuate drastically.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_6BB6")

    Jump("loc_6C4D")

    label("loc_6BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_6C4D")

    ChrTalk(    #279
        0xFE,
        (
            "What do you think of this price?\x01",
            "Sound like a fair deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "I think you'll find our prices are\x01",
            "a steal compared to the other\x01",
            "venders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C4D")

    TalkEnd(0xF)
    Return()

    # Function_14_65F4 end

    def Function_15_6C51(): pass

    label("Function_15_6C51")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CD8")

    ChrTalk(    #281
        0xFE,
        (
            "My apologies for calling you out\x01",
            "so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "There's something I'd like you to\x01",
            "examine immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_6D4B")

    label("loc_6CD8")


    ChrTalk(    #283
        0xFE,
        (
            "My apologies for calling you out\x01",
            "so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "I'd love it if we could work together\x01",
            "again in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D4B")

    Jump("loc_7325")

    label("loc_6D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6F31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6E27")

    ChrTalk(    #285
        0xFE,
        (
            "I haven't been taking profit into account\x01",
            "at all, but I'm sure we could come to a\x01",
            "deal in some way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "Good fortune always comes to\x01",
            "people who help out one another\x01",
            "in times of need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F2E")

    label("loc_6E27")


    ChrTalk(    #287
        0xFE,
        "No, no, I've been quite helped already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "I haven't been taking profit into\x01",
            "account at all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "...I'm sure we could come to a deal\x01",
            "in some way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "Perhaps the scheduled airships\x01",
            "being resumed sooner than expected\x01",
            "had some effect?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_6F2E")

    Jump("loc_7325")

    label("loc_6F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_70E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_6FE7")

    ChrTalk(    #291
        0xFE,
        (
            "Leave it to us to provide anything\x01",
            "from the sea you might need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "This is an emergency situation,\x01",
            "after all--it's only right that we help\x01",
            "as much as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70E3")

    label("loc_6FE7")


    ChrTalk(    #293
        0xFE,
        "You can leave stocking seafood to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "We'll be able to pull through this crisis\x01",
            "just fine with all we have in stored in the\x01",
            "warehouse in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "This is an emergency situation,\x01",
            "after all--it's only right that we help\x01",
            "as much as we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_70E3")

    Jump("loc_7325")

    label("loc_70E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7188")

    ChrTalk(    #296
        0xFE,
        (
            "They say orchards at Ravennue have\x01",
            "been almost entirely destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "We get almost all of our fruit from there,\x01",
            "too. This could be a problem...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7325")

    label("loc_7188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7215")

    ChrTalk(    #298
        0xFE,
        (
            "Hard to believe something this\x01",
            "terrible would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "*sigh* I thought things would finally\x01",
            "go smoothly, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7286")

    label("loc_7215")


    ChrTalk(    #300
        0xFE,
        "Hmm... That's not good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "Guess I'll need to review all the\x01",
            "business deals I have going on\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_7286")

    Jump("loc_7325")

    label("loc_7289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7325")

    ChrTalk(    #302
        0xFE,
        (
            "Sorry, but I can't accept the price\x01",
            "you're asking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "Distribution's just dandy right now,\x01",
            "so you should have plenty in stock,\x01",
            "shouldn't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7325")

    TalkEnd(0x10)
    Return()

    # Function_15_6C51 end

    def Function_16_7329(): pass

    label("Function_16_7329")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74C3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as old man 123 complete + all related quests finished\x01",      # 0
            "Set as old man 123 complete\x01",                                    # 1
            "Set as 101 Clear\x01",                                               # 2
            "Set as never touched latter half\x01",                               # 3
            "Set as seeing for the first time in chapter 5\x01",                  # 4
            "No change\x01",                                                      # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7438"),
        (1, "loc_7455"),
        (2, "loc_7472"),
        (3, "loc_748F"),
        (4, "loc_74AC"),
        (5, "loc_74C0"),
        (SWITCH_DEFAULT, "loc_74C3"),
    )


    label("loc_7438")

    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_74C3")

    label("loc_7455")

    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_74C3")

    label("loc_7472")

    OP_28(0x7B, 0x3, 0x10)
    OP_28(0x7B, 0x2, 0x8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_74C3")

    label("loc_748F")

    OP_28(0x7B, 0x3, 0x10)
    OP_28(0x7B, 0x2, 0x8)
    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_74C3")

    label("loc_74AC")

    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x7B, 0x1, 0x8000)
    Jump("loc_74C3")

    label("loc_74C0")

    Jump("loc_74C3")

    label("loc_74C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8602")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -35260, 0, 42950, 90)
    SetChrPos(0xF7, -35690, 0, 41950, 90)
    SetChrPos(0xF8, -36550, 0, 43150, 90)
    SetChrPos(0xF9, -36640, 0, 41730, 90)
    OP_8C(0x11, 270, 0)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7558")
    SetChrPos(0x4, -35970, 0, 44280, 135)

    label("loc_7558")

    OP_6D(-35000, 0, 42570, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #304
        0x11,
        "Ooh, hey! Hey!! You guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x11,
        "Listen to this: I did it! I got the deal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x11,
        (
            "At long last, I've managed to form a\x01",
            "partnership with a first-class restaurant!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #307
        0x101,
        (
            "#1004FR-Really?!\x02\x03",

            "#1001FThat's great!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        "#1040FCongratulations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x11,
        (
            "Ladies and gentlemen of the bracers,\x01",
            "I couldn't be more grateful than I am\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x11,
        (
            "Striking a deal with the Anterose\x01",
            "has been my dream for as long as\x01",
            "I can remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x11,
        (
            "And I have you to thank for it.\x01",
            "You've made my lifelong dream\x01",
            "finally come true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1017FHaha, you bet'cha.\x02\x03",

            "But, really, it worked out because\x01",
            "you worked so hard.\x02\x03",

            "We just helped out a little.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8106")

    ChrTalk(    #313
        0x11,
        (
            "Yes, well, you've been 'helping a little'\x01",
            "for quite a while, in my opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x11,
        (
            "I know that I've caused you a lot of grief,\x01",
            "but thank you again for putting up with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x11,
        (
            "Allow me the pleasure of offering\x01",
            "you a gift in exchange for everything\x01",
            "you've done.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #316
        0x101,
        (
            "#1020FUh oh...\x02\x03",

            "You're not gonna give us a ton\x01",
            "of those weird mushrooms again,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x11,
        "Hmm? Would you like mushrooms?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x11,
        "I DO have plenty of those in stock...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #319
        0x101,
        (
            "#1007FEr, no. Seriously. No. I REALLY\x01",
            "don't want any.\x02\x03",

            "#1015F...Uh, what we're we talking about\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x11,
        "We were talking about my gift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x11,
        (
            "And my gift is nothing less than\x01",
            "a platinum membership to my\x01",
            "company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x11,
        (
            "The 'platinum' isn't just for show, either!\x01",
            "We're talking an exclusive, all-access\x01",
            "pass type of membership here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        (
            "#1019FE-Er, okay. And what does that\x01",
            "get me, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x11,
        (
            "Well, as you know, I am a merchant\x01",
            "specializing in foodstuffs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x11,
        (
            "Normally, I would only deal with\x01",
            "professionals. I don't sell to the\x01",
            "general public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x11,
        (
            "However, I owe you guys a lot, so I'm\x01",
            "thinking that it's only right that I offer you\x01",
            "special dispensation to deal with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#1044FSo, essentially...\x02\x03",

            "We can buy things from you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x11,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x11,
        (
            "If there are any ingredients you need,\x01",
            "just talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x11,
        (
            "As long as you can pay, I'd be glad to\x01",
            "provide you with any and all ingredients\x01",
            "you might need in turn.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E1D")

    ChrTalk(    #331
        0x104,
        (
            "#033FMy, that is impressive.\x02\x03",

            "So you can really procure any\x01",
            "ingredient we ask for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E72")

    ChrTalk(    #332
        0x108,
        (
            "#070FOh, very impressive.\x02\x03",

            "So you can get us anything\x01",
            "we want?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7E72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EBD")

    ChrTalk(    #333
        0x106,
        (
            "#052FHuh. Cool.\x02\x03",

            "So you can get us anythin'\x01",
            "we want?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7EBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F1D")

    ChrTalk(    #334
        0x103,
        (
            "#023FMy, that is impressive.\x02\x03",

            "Can you really find any ingredient\x01",
            "we ask for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F1D")


    ChrTalk(    #335
        0x11,
        (
            "Yes, as long as it's something\x01",
            "it's something eaten within the\x01",
            "boundaries of the Liberl Kingdom. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x11,
        (
            "I know that those in your line\x01",
            "of work often end up preparing\x01",
            "their own meals out in the field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x11,
        (
            "Don't you hesitate to call on me\x01",
            "for whatever you need!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1006FSure! Sounds handy. If something\x01",
            "comes up, we'll let you know.\x02\x03",

            "See you later, Mr. Orvid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x11,
        "Oh, pardon me! Sorry to have kept you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x11,
        "Till we meet again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        "#1040FPardon us.\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x4000)
    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0x11, 0, 0)
    OP_4B(0x11, 255)
    Return()

    label("loc_8106")


    ChrTalk(    #342
        0x11,
        "Perhaps so, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x11,
        (
            "Still, I didn't have it in me to take\x01",
            "the last step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x11,
        (
            "Allow me the pleasure of offering\x01",
            "you a gift in exchange for everything\x01",
            "you've done.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #345
        0x101,
        (
            "#1020FUh oh...\x02\x03",

            "You're not gonna give us a ton\x01",
            "of those weird mushrooms again,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x11,
        "Hmm? Would you like mushrooms?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x11,
        "I DO have plenty of those in stock...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #348
        0x101,
        (
            "#1007FEr, no. Seriously. No. I REALLY\x01",
            "don't want any.\x02\x03",

            "#1015F...Uh, what we're we talking about\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x11,
        "We were talking about my gift.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x11,
        (
            "And my gift is nothing less than a\x01",
            "gold membership to my company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x101,
        (
            "#1011FE-Er, okay. And what does that\x01",
            "get me, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x11,
        (
            "Well, as you know, I am a merchant\x01",
            "specializing in foodstuffs, but I don't\x01",
            "sell to the general public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x11,
        (
            "However, I owe you guys a lot, so I'm\x01",
            "thinking that it's only right that I offer you\x01",
            "special permission to deal with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x11,
        (
            "Of course, I'll have to limit that to only\x01",
            "fairly standard products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        (
            "#1017FNeat! Sounds handy.\x02\x03",

            "Given the situation these days, even\x01",
            "normal ingredients might start being\x01",
            "hard to come by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        "#1040FWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x11,
        (
            "If there are any ingredients you need,\x01",
            "just talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x11,
        (
            "I've got all the ingredients you might\x01",
            "find in stores.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0x11, 0, 0)
    OP_4B(0x11, 255)
    Return()

    label("loc_8602")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8648")

    ChrTalk(    #359
        0x11,
        "Oh, hey, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x11,
        "Thanks again for all your help!\x02",
    )

    CloseMessageWindow()
    Jump("loc_866D")

    label("loc_8648")


    ChrTalk(    #361
        0x11,
        "Oh, you're bracers, aren't you?\x02",
    )

    CloseMessageWindow()

    label("loc_866D")


    ChrTalk(    #362
        0x11,
        (
            "With all distribution systems frozen,\x01",
            "I'm sure it's difficult to get food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x11,
        (
            "It's times like these when the\x01",
            "Orvid Company sparkles more\x01",
            "mightily than the shiniest pom!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x11,
        (
            "I will be glad to provide you with rare tastes\x01",
            "obtained through proprietary routes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x11,
        "Now, come look at what I've got to offer!\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x8000)
    OP_A2(0xC)
    Jump("loc_9614")

    label("loc_87B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9614")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -35260, 0, 42950, 90)
    SetChrPos(0xF7, -35690, 0, 41950, 90)
    SetChrPos(0xF8, -36550, 0, 43150, 90)
    SetChrPos(0xF9, -36640, 0, 41730, 90)
    OP_8C(0x11, 270, 0)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8837")
    SetChrPos(0x4, -35970, 0, 44280, 135)

    label("loc_8837")

    OP_6D(-35000, 0, 42570, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #366
        0x11,
        (
            "To think I'd be able to so easily\x01",
            "bring an offer to them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x11,
        "Bracers... Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x11,
        (
            "It's been my dream of many years to\x01",
            "deal with a first-class restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x11,
        (
            "To know that'll come true soon...\x01",
            "This is thanks to all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1017FHaha, thanks.\x02\x03",

            "But, really, it worked out because you\x01",
            "worked so hard.\x02\x03",

            "We just helped out a little.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A5A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Completed all Orvid-related quests\x01",      # 0
            "No change\x01",                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8A45"),
        (1, "loc_8A57"),
        (SWITCH_DEFAULT, "loc_8A5A"),
    )


    label("loc_8A45")

    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_8A5A")

    label("loc_8A57")

    Jump("loc_8A5A")

    label("loc_8A5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9288")

    ChrTalk(    #371
        0x11,
        (
            "Well, one way or another we have been\x01",
            "working at this for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x11,
        (
            "I know that I've caused you a lot of trouble,\x01",
            "but thank you for putting up with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x11,
        (
            "Allow me to offer my thanks in physical form,\x01",
            "for everything you've done.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #374
        0x101,
        (
            "#1020FUh oh...\x02\x03",

            "You're not gonna give us a ton of those\x01",
            "weird mushrooms again, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x11,
        "Hmm? Would you like mushrooms?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x11,
        "In that case I do have quite a lot in stock...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #377
        0x101,
        (
            "#1007FEr, no. Seriously. No.\x01",
            "I REALLY don't want any.\x02\x03",

            "#1015F...Uh,what we're we talking about again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x11,
        "We were talking about my thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x11,
        (
            "My thanks to you is nothing less than the right\x01",
            "to patronize the Orvid Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x101,
        "#1011FHuh? Use rights?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x11,
        (
            "Yes, as you know, I am a merchant specializing\x01",
            "solely in ingredients, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x11,
        (
            "Ultimately I only do business with professionals.\x01",
            "I don't sell to the general populace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x11,
        (
            "However, I owe you quite a bit. I'll offer\x01",
            "special permission to deal with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        (
            "#1000FSo basically...\x02\x03",

            "We can buy things from your store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x11,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x11,
        (
            "If there are any ingredients you need,\x01",
            "just talk to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x11,
        (
            "As long as you can provide the correct payment,\x01",
            "I'll be glad to provide you in turn with any\x01",
            "ingredients you need.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FB4")

    ChrTalk(    #388
        0x104,
        (
            "#033FMy, that is impressive.\x02\x03",

            "Can you really procure any ingredients at all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90BC")

    label("loc_8FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9010")

    ChrTalk(    #389
        0x108,
        (
            "#070FOh, very impressive.\x02\x03",

            "Can you really get any ingredients at all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90BC")

    label("loc_9010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9060")

    ChrTalk(    #390
        0x106,
        (
            "#052FHn. Impressive.\x02\x03",

            "Can you really get anythin' at all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90BC")

    label("loc_9060")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90BC")

    ChrTalk(    #391
        0x103,
        (
            "#020FMy, that is impressive.\x02\x03",

            "Can you really get any ingredients at all?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90BC")


    ChrTalk(    #392
        0x11,
        (
            "Yes, as long as it's something it's something\x01",
            "eaten within the boundaries of the Liberl\x01",
            "Kingdom. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x11,
        (
            "I know that ladies and gentlemen in your line\x01",
            "of work often end up preparing their own\x01",
            "meals in the field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x11,
        "Please, do not hesitate to use my services.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        (
            "#1006FYeah, okay. If the chance comes up,\x01",
            "we will.\x02\x03",

            "All right, if you'll excuse us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x11,
        (
            "Ohh, yes, my apologies.\x01",
            "Sorry to have kept you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x11,
        "I'll be waiting for your business.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x4000)
    Jump("loc_9604")

    label("loc_9288")


    ChrTalk(    #398
        0x11,
        "Perhaps so, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x11,
        "Allow me to offer my thanks in physical form.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x11,
        (
            "Allow me to provide you with the right\x01",
            "to patronize the Orvid Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x101,
        "#1011FHuh? Use rights?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x11,
        (
            "Yes, as you know, I am a merchant specializing\x01",
            "solely in ingredients, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x11,
        (
            "Ultimately I only do business with professionals.\x01",
            "I don't sell to the general populace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x11,
        (
            "However, I owe you quite a bit. I'll offer\x01",
            "special permission to deal with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        (
            "#1000FSo basically...\x02\x03",

            "We can buy things from your store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x11,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x11,
        (
            "If there are any ingredients\x01",
            "you need, just let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x11,
        (
            "I've got much better stock\x01",
            "than your average store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x101,
        (
            "#1018FThat sure sounds handy.\x02\x03",

            "#1006FYeah, okay. If the chance comes up,\x01",
            "we will.\x02\x03",

            "All right, if you'll excuse us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x11,
        (
            "Ohh, yes, my apologies.\x01",
            "Sorry to have kept you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x11,
        (
            "Well, then, best of luck to you\x01",
            "with your business as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x101,
        "#1001FLater!\x02",
    )

    CloseMessageWindow()

    label("loc_9604")

    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x8000)
    EventEnd(0x0)
    OP_4B(0x11, 255)
    Return()

    label("loc_9614")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96E7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D6")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96A7")

    ChrTalk(    #413
        0x11,
        "Would you like to buy something?\x02",
    )

    CloseMessageWindow()

    label("loc_96A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_96B7")
    OP_A9(0x38)
    Jump("loc_96B9")

    label("loc_96B7")

    OP_A9(0x37)

    label("loc_96B9")

    OP_A3(0xC)

    ChrTalk(    #414
        0x11,
        "Come again!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_96D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96E7")
    TalkEnd(0x11)
    Return()

    label("loc_96E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_9856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97D0")

    ChrTalk(    #415
        0x11,
        (
            "My ingredients were rated quite\x01",
            "highly by the head chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x11,
        (
            "Well, as a professional food supplier\x01",
            "that's only natural! Heh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x11,
        (
            "I am honestly quite happy. After all,\x01",
            "I've worked hard to get here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_9853")

    label("loc_97D0")


    ChrTalk(    #418
        0x11,
        (
            "My ingredients were rated quite\x01",
            "highly by the head chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x11,
        (
            "Well, as a professional food supplier\x01",
            "that's only natural! Heh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9853")

    Jump("loc_9EBC")

    label("loc_9856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9954")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9887")

    ChrTalk(    #420
        0x11,
        "Oh, hello!\x02",
    )

    CloseMessageWindow()

    label("loc_9887")


    ChrTalk(    #421
        0x11,
        (
            "Seems like the world's in a rough spot,\x01",
            "but my business is going quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x11,
        (
            "While the major suppliers are having trouble\x01",
            "distributing, I'll be taking the opportunity to\x01",
            "expand my markets.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_9A1B")

    label("loc_9954")


    ChrTalk(    #423
        0x11,
        (
            "Seems like the world's in a rough spot,\x01",
            "but my business is going quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x11,
        (
            "While the major suppliers are having trouble\x01",
            "distributing, I'll be taking the opportunity to\x01",
            "expand my markets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A1B")

    Jump("loc_9EBC")

    label("loc_9A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_9B15")

    ChrTalk(    #425
        0x11,
        (
            "It seems the scheduled liners have resumed,\x01",
            "but it has no effect on my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x11,
        (
            "After all, my business is more about rare,\x01",
            "idiosyncratic gems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x11,
        (
            "Heh heh, I've got a lineup no one else\x01",
            "in the business could hope to imitate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EBC")

    label("loc_9B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9CB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_9BD8")

    ChrTalk(    #428
        0x11,
        (
            "It's because my company takes personal\x01",
            "responsibility for collecting our product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x11,
        (
            "Should the scheduled liners stop or whatever\x01",
            "else might come, it has no effect on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CB3")

    label("loc_9BD8")


    ChrTalk(    #430
        0x11,
        (
            "It's because my company takes personal\x01",
            "responsibility for collecting our product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x11,
        (
            "It doesn't make a difference whether the\x01",
            "liners are functioning or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x11,
        "Heh heh, this is the ultimate in independence.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_9CB3")

    Jump("loc_9EBC")

    label("loc_9CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_9D51")

    ChrTalk(    #433
        0x11,
        (
            "It seems that getting in stock is harder for\x01",
            "people now that the scheduled liners have\x01",
            "stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x11,
        "Heh heh, looks like this is my chance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EBC")

    label("loc_9D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_9E1F")

    ChrTalk(    #435
        0x11,
        (
            "Thanks to the incident the restaurant\x01",
            "is...a bit out of sorts, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x11,
        (
            "*sigh* Well, it means my deal will be delayed,\x01",
            "most likely, but given that it's an emergency\x01",
            "I can't blame them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EBC")

    label("loc_9E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9EBC")

    ChrTalk(    #437
        0x11,
        (
            "As soon as the head chef has time,\x01",
            "I intend to bring my offer to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x11,
        (
            "He's quite the busy one, it seems.\x01",
            "As expected of a first class chef.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EBC")

    Jump("loc_9F1A")

    label("loc_9EBF")


    ChrTalk(    #439
        0x11,
        "Please, use my store whenever you'd like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x11,
        (
            "Why don't you buy something?\x01",
            "Go ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F1A")

    TalkEnd(0x11)
    Return()

    # Function_16_7329 end

    def Function_17_9F1E(): pass

    label("Function_17_9F1E")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_9F7C")

    ChrTalk(    #441
        0xFE,
        "N-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xFE,
        (
            "P-Please, stop. I am nothing but an\x01",
            "inexperienced girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F80")

    label("loc_9F7C")

    Call(0, 23)

    label("loc_9F80")

    Jump("loc_A073")

    label("loc_9F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_A013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_A00C")

    ChrTalk(    #443
        0xFE,
        (
            "As you say, life in the cities can be\x01",
            "quite constraining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0xFE,
        (
            "It might be nice to live in a more\x01",
            "natural setting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A010")

    label("loc_A00C")

    Call(0, 23)

    label("loc_A010")

    Jump("loc_A073")

    label("loc_A013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_A061")

    ChrTalk(    #445
        0x12,
        "What a fearsome sound...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x12,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A065")

    label("loc_A061")

    Call(0, 23)

    label("loc_A065")

    Jump("loc_A073")

    label("loc_A068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_A073")
    Call(0, 23)

    label("loc_A073")

    TalkEnd(0x12)
    Return()

    # Function_17_9F1E end

    def Function_18_A077(): pass

    label("Function_18_A077")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A1F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 5)), scpexpr(EXPR_END)), "loc_A1F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A112")

    ChrTalk(    #447
        0xFE,
        (
            "After this proposal, next a return to her\x01",
            "family in the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "Really, Miss Felicity hasn't even the\x01",
            "time to rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1EE")

    label("loc_A112")


    ChrTalk(    #449
        0xFE,
        (
            "It seems that this arranged marriage\x01",
            "meeting will end on a positive note.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "Still, next is a return to her family in\x01",
            "the Empire as soon as this ends...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        (
            "Really, Miss Felicity hasn't even the\x01",
            "time to rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_A1EE")

    Jump("loc_A1F5")

    label("loc_A1F1")

    Call(0, 19)

    label("loc_A1F5")

    Jump("loc_A8B2")

    label("loc_A1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_A375")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 5)), scpexpr(EXPR_END)), "loc_A36E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A28F")

    ChrTalk(    #452
        0xFE,
        (
            "Now that some time has passed, Felicity\x01",
            "seems to have calmed down a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        (
            "Truly this was a fortunate problem\x01",
            "to have.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A36B")

    label("loc_A28F")


    ChrTalk(    #454
        0xFE,
        (
            "Due to yesterday's incident, the arranged marriage\x01",
            "meeting was temporarily canceled, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xFE,
        (
            "If anything, things seem to be\x01",
            "flowing more smoothly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xFE,
        (
            "We might be able to expect\x01",
            "good things from this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_A36B")

    Jump("loc_A372")

    label("loc_A36E")

    Call(0, 19)

    label("loc_A372")

    Jump("loc_A8B2")

    label("loc_A375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A3F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 5)), scpexpr(EXPR_END)), "loc_A3EB")

    ChrTalk(    #457
        0xFE,
        (
            "It sounds like something terrible has\x01",
            "happened outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xFE,
        "For now, we should remain indoors.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3EF")

    label("loc_A3EB")

    Call(0, 19)

    label("loc_A3EF")

    Jump("loc_A8B2")

    label("loc_A3F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_A8B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A460")

    ChrTalk(    #459
        0xFE,
        (
            "The arranged marriage meeting has\x01",
            "already begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        "Everyone, please remain quiet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8B2")

    label("loc_A460")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_A633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A503")

    ChrTalk(    #461
        0xFE,
        "Please find the young mistress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xFE,
        (
            "If you find yourself in difficulty,\x01",
            "then please recall that advice about\x01",
            "the young mistress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A59F")

    label("loc_A503")


    ChrTalk(    #463
        0xFE,
        "Oh, hello...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        "Please find the young mistress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "If you find yourself in difficulty,\x01",
            "then please recall that advice about\x01",
            "the young mistress.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_A59F")

    Jump("loc_A630")

    label("loc_A5A2")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #466
        0xFE,
        "Do your best, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "If you find yourself in difficulty,\x01",
            "then please recall that advice about\x01",
            "the young mistress.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    label("loc_A630")

    Jump("loc_A8B2")

    label("loc_A633")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A656")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_A64F")
    Call(1, 8)
    Jump("loc_A653")

    label("loc_A64F")

    Call(1, 7)

    label("loc_A653")

    Jump("loc_A8B2")

    label("loc_A656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 4)), scpexpr(EXPR_END)), "loc_A70E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A6B1")

    ChrTalk(    #468
        0xFE,
        "I've already acted on that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xFE,
        "Now it's just a fight against time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A70B")

    label("loc_A6B1")


    ChrTalk(    #470
        0xFE,
        "Please, buy time somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        "I've already set actions in motion on that matter.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_A70B")

    Jump("loc_A8B2")

    label("loc_A70E")


    ChrTalk(    #472
        0xFE,
        "Please, buy time somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        "I've already set actions in motion on that matter.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #474
        0x101,
        "#1004F(Hey, I've seen her before...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #475
        0x106,
        "#050F(You know her?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A843")

    ChrTalk(    #476
        0x101,
        "#1002F(Y-Yeah...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x105,
        (
            "#040F(Reina from the royal academy.)\x02\x03",

            "(I wonder what she's doing here...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8AF")

    label("loc_A843")


    ChrTalk(    #478
        0x101,
        (
            "#1015F(Y-Yeah... She's one of the students\x01",
            "from the royal academy.)\x02\x03",

            "(I wonder what she's doing here.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8AF")

    OP_A2(0x1A54)

    label("loc_A8B2")

    TalkEnd(0x13)
    Return()

    # Function_18_A077 end

    def Function_19_A8B6(): pass

    label("Function_19_A8B6")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #479
        0xFE,
        "Oh, you are...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9D7")

    ChrTalk(    #480
        0x101,
        (
            "#1004FHuh?!\x02\x03",

            "#1011FYou're Reina...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x105,
        (
            "#040FYes, we met during our investigation\x01",
            "at the academy.\x02\x03",

            "Reina, it's been a while.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #482
        0xFE,
        "Oh, even Kloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x101,
        (
            "#1015FUm, what are you doing in a place\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA94")

    label("loc_A9D7")


    ChrTalk(    #484
        0x101,
        (
            "#1004FHuh?!\x02\x03",

            "#1011FYou're Reina...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x107,
        "#064FYou know her, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x101,
        (
            "#1015FYeah, we spoke a little bit during\x01",
            "the investigation at the academy...\x02\x03",

            "#1002FSo why are you here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA94")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #487
        0xFE,
        "I'm here accompanying Felicity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0xFE,
        (
            "After all, today is a very important\x01",
            "arranged marriage meeting for her.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #489
        0x101,
        (
            "#1004FEh?!\x02\x03",

            "A-Arranged marriage meeting for...Felicity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        (
            "Yes, there have been numerous obstacles,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0xFE,
        (
            "With the support of various people we\x01",
            "managed to put it together successfully.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_AD5E")

    ChrTalk(    #492
        0x101,
        (
            "#1016FStill, uh, isn't she a bit young for\x01",
            "an arranged marriage?\x02\x03",

            "After all, she's still a student, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "Though she may be a student, she is\x01",
            "already sixteen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        (
            "As a member of upper class Imperial society,\x01",
            "it would be shameful to not have even one\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        (
            "#1008FI-Is that so...\x02\x03",

            "#1015FMmmm, can't say I understand\x01",
            "that kind of world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE65")

    label("loc_AD5E")


    ChrTalk(    #496
        0xFE,
        (
            "...More importantly, things seem...\x01",
            "loud outside. Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x101,
        (
            "#1002FYeah...\x02\x03",

            "There's no danger now, but you should\x01",
            "probably stay inside for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        "I see. Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0xFE,
        "Take care, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x101,
        "#1002FY-Yeah... You too, Reina.\x02",
    )

    CloseMessageWindow()

    label("loc_AE65")

    OP_A2(0x1A55)
    Return()

    # Function_19_A8B6 end

    def Function_20_AE69(): pass

    label("Function_20_AE69")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_AFC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_AF1B")

    ChrTalk(    #501
        0xFE,
        (
            "It seems the young mistress has taken\x01",
            "to her companion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xFE,
        (
            "After this, we will need for them to communicate\x01",
            "via letter to deepen their relationship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC6")

    label("loc_AF1B")


    ChrTalk(    #503
        0xFE,
        (
            "It seems this marriage meeting will\x01",
            "end with some measure of success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0xFE,
        (
            "This has been a valuable chance to deepen the\x01",
            "friendship between both families, indeed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_AFC6")

    Jump("loc_B41F")

    label("loc_AFC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_B0B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_B044")

    ChrTalk(    #505
        0xFE,
        (
            "It seems the young mistress has taken\x01",
            "an interest in her companion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        "Keep it up, young mistress!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0B5")

    label("loc_B044")


    ChrTalk(    #507
        0xFE,
        (
            "It seems the young mistress has taken\x01",
            "an interest in her companion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        "Something to celebrate, indeed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_B0B5")

    Jump("loc_B41F")

    label("loc_B0B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_B131")

    ChrTalk(    #509
        0xFE,
        (
            "That sound...\x01",
            "It was almost as if thunder had struck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0xFE,
        (
            "I wonder what could have happened\x01",
            "out front...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B41F")

    label("loc_B131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B41F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B2D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_B1E6")

    ChrTalk(    #511
        0xFE,
        (
            "Despite such a strong resistance to\x01",
            "this meeting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0xFE,
        (
            "Now that it's begun, for such an exchange\x01",
            "of words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xFE,
        "Very impressive, young mistress.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2D1")

    label("loc_B1E6")


    ChrTalk(    #514
        0xFE,
        (
            "Despite such a strong resistance to\x01",
            "this meeting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xFE,
        (
            "Now that it's begun, for such an exchange\x01",
            "of words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0xFE,
        (
            "This flexible attitude is the ability needed\x01",
            "to survive in high society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        "Very impressive, young mistress.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_B2D1")

    Jump("loc_B41F")

    label("loc_B2D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_B374")

    ChrTalk(    #518
        0xFE,
        (
            "The young lady is currently applying\x01",
            "her cosmetics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0xFE,
        (
            "She will arrive shortly, so we ask for your\x01",
            "patience for just a short time longer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B41F")

    label("loc_B374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_B397")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_B390")
    Call(1, 8)
    Jump("loc_B394")

    label("loc_B390")

    Call(1, 7)

    label("loc_B394")

    Jump("loc_B41F")

    label("loc_B397")


    ChrTalk(    #520
        0xFE,
        (
            "I'm buying as much time as I can by claiming\x01",
            "the mistress is attending to her face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0xFE,
        "Well, I'll leave the search party to you.\x02",
    )

    CloseMessageWindow()

    label("loc_B41F")

    TalkEnd(0x14)
    Return()

    # Function_20_AE69 end

    def Function_21_B423(): pass

    label("Function_21_B423")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B4C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B4BB")

    ChrTalk(    #522
        0xFE,
        (
            "No, it is definitely not an excessive estimation,\x01",
            "I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xFE,
        (
            "Compared to you, I am far more the\x01",
            "inexperienced party here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4BF")

    label("loc_B4BB")

    Call(0, 23)

    label("loc_B4BF")

    Jump("loc_B7A5")

    label("loc_B4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_B588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B581")

    ChrTalk(    #524
        0xFE,
        (
            "I find that the hectic pace and confines of\x01",
            "the capital suit my personality poorly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0xFE,
        (
            "I find it far easier to live with nature as\x01",
            "my companion than crowds of people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B585")

    label("loc_B581")

    Call(0, 23)

    label("loc_B585")

    Jump("loc_B7A5")

    label("loc_B588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_B641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B63A")

    ChrTalk(    #526
        0xFE,
        (
            "It seems the danger has passed, but at the\x01",
            "same time whatever made that sound must\x01",
            "have been terrible, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x15,
        "Perhaps we should end for the day here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B63E")

    label("loc_B63A")

    Call(0, 23)

    label("loc_B63E")

    Jump("loc_B7A5")

    label("loc_B641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_B7A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B659")
    Call(0, 23)
    Jump("loc_B7A5")

    label("loc_B659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B6E2")

    ChrTalk(    #528
        0xFE,
        (
            "Perhaps she saw I was dressed in\x01",
            "casual clothes and was angered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0xFE,
        (
            "Hmm, perhaps I really should\x01",
            "have worn a suit here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7A5")

    label("loc_B6E2")


    ChrTalk(    #530
        0xFE,
        "My companion has yet to appear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0xFE,
        (
            "Perhaps she saw I was dressed in\x01",
            "casual clothes and was angered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0xFE,
        (
            "Though it was a proposal from her,\x01",
            "it's true it's ill-suited to the occasion.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_B7A5")

    TalkEnd(0x15)
    Return()

    # Function_21_B423 end

    def Function_22_B7A9(): pass

    label("Function_22_B7A9")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B978")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_B854")

    ChrTalk(    #533
        0xFE,
        "It seems this meeting has ended in success.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0xFE,
        (
            "To deepen the relationship between both families\x01",
            "I hope they will continue their correspondence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B975")

    label("loc_B854")


    ChrTalk(    #535
        0xFE,
        (
            "At first I was worried how things would\x01",
            "go, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0xFE,
        "It seems this meeting has ended in success.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0xFE,
        (
            "To deepen the relationship between both families\x01",
            "I hope they will continue their correspondence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0xFE,
        (
            "Whether it will proceed to marriage\x01",
            "will depend on their opinions, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_B975")

    Jump("loc_BE5A")

    label("loc_B978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_BA19")

    ChrTalk(    #539
        0xFE,
        (
            "The young master is just a bit too\x01",
            "lacking in ambition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0xFE,
        (
            "His lineage is more than enough to ensure\x01",
            "his success in the political arena, yet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE5A")

    label("loc_BA19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_BB6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_BAA6")

    ChrTalk(    #541
        0xFE,
        (
            "It seems nothing serious happened to\x01",
            "this establishment, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0xFE,
        (
            "Young master, please remain\x01",
            "seated as you are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB69")

    label("loc_BAA6")


    ChrTalk(    #543
        0xFE,
        (
            "Young master, it seems nothing serious\x01",
            "happened to this establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0xFE,
        "Please remain seated as you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0xFE,
        (
            "As soon as I understand the situation outside,\x01",
            "I shall convey it to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_BB69")

    Jump("loc_BE5A")

    label("loc_BB6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_BE5A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BD39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_BC3C")

    ChrTalk(    #546
        0xFE,
        (
            "It seems her reputation as\x01",
            "a woman of talent was not false.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xFE,
        (
            "Her understated grace and confidence are\x01",
            "no less than I would expect from someone\x01",
            "born of such a noted family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD36")

    label("loc_BC3C")


    ChrTalk(    #548
        0xFE,
        (
            "The young lady was painted as a woman\x01",
            "of talent studying abroad in the kingdom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #549
        0xFE,
        "It appears that picture was not false.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0xFE,
        (
            "Her understated grace and confidence are\x01",
            "no less than I would expect from someone\x01",
            "born of such a noted family.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_BD36")

    Jump("loc_BE5A")

    label("loc_BD39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_BDC5")

    ChrTalk(    #551
        0xFE,
        "The young master is simply too kind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0xFE,
        (
            "I have a slight fear that he is likely to find\x01",
            "himself at the mercies of the girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE5A")

    label("loc_BDC5")


    ChrTalk(    #553
        0xFE,
        (
            "Young master, there is no failing\x01",
            "on our part in this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0xFE,
        (
            "It was the proposal of your companion\x01",
            "to dress in casual wear, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_BE5A")

    TalkEnd(0x16)
    Return()

    # Function_22_B7A9 end

    def Function_23_BE5E(): pass

    label("Function_23_BE5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_C065")

    ChrTalk(    #555
        0x15,
        (
            "I see, so you will be returning to your\x01",
            "family in the Empire after this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0x12,
        "Yes, that is my current schedule.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x12,
        (
            "I still have a short break from the academy,\x01",
            "so I shall visit with my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x15,
        (
            "You truly are the woman\x01",
            "I expected you to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0x15,
        (
            "Possessed of progressive thoughts on one hand,\x01",
            "while also equipped with our moral principles\x01",
            "from yore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0x15,
        (
            "I feel I should again offer thanks\x01",
            "to Aidios for allowing us to meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x12,
        "N-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #562
        0x12,
        (
            "P-Please, stop. I am nothing\x01",
            "but an inexperienced girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C63E")

    label("loc_C065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_C2B6")

    ChrTalk(    #563
        0x12,
        (
            "Pardon me, but what work\x01",
            "do you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #564
        0x15,
        (
            "Normally, I manage the agricultural land and\x01",
            "mountain forests I inherited from my grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #565
        0x15,
        (
            "It is a free, open rural life, with little to do\x01",
            "during the off seasons save read and hunt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #566
        0x15,
        (
            "I find that the hectic pace and confines of\x01",
            "the capital suit my personality poorly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #567
        0x12,
        "A rural life, you say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x15,
        (
            "Yes, while it may sound dull, I think you\x01",
            "will find it quite pleasant once you become\x01",
            "accustomed to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0x15,
        (
            "I find it far easier to live with nature as\x01",
            "my companion than crowds of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0x12,
        "Hmm... I see. Perhaps so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C63E")

    label("loc_C2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C3CE")
    OP_4A(0x12, 255)
    OP_4A(0x15, 255)

    ChrTalk(    #571
        0x12,
        "What a fearsome sound...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0x12,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #573
        0x15,
        (
            "It seems there's no immediate danger.\x01",
            "Let us remain here for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #574
        0x15,
        (
            "Still, whatever made that sound must\x01",
            "have been terrible, indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #575
        0x15,
        "Perhaps we should end for the day here.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)
    OP_4B(0x15, 255)
    Jump("loc_C63E")

    label("loc_C3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_C63E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_C497")

    ChrTalk(    #576
        0x15,
        "First, a toast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0x15,
        (
            "To our meeting, and to the future\x01",
            "of our glorious families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0x12,
        "Yes, gladly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #579
        0x12,
        (
            "However, I shall have to give my salute to\x01",
            "the occasion with a soft drink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C63E")

    label("loc_C497")


    ChrTalk(    #580
        0x12,
        "A pleasure to meet you. I am Felicity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0x12,
        (
            "Allow me to offer my sincerest apologies\x01",
            "for keeping you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #582
        0x12,
        (
            "I was busy with live studies of modern society,\x01",
            "a task from the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #583
        0x15,
        (
            "I have eagerly awaited the day\x01",
            "I would meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #584
        0x15,
        (
            "I was a bit concerned when you\x01",
            "hadn't showed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0x15,
        "Regardless, we have at last met.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x15,
        (
            "As a man of the Empire, I have no intention\x01",
            "of picking over the little things.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_C63E")

    OP_A2(0x12)
    OP_A2(0x10)
    Return()

    # Function_23_BE5E end

    def Function_24_C645(): pass

    label("Function_24_C645")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_C704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_C6FD")

    ChrTalk(    #587
        0xFE,
        (
            "Yes, what really matters is a relationship\x01",
            "of trust with the customer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #588
        0xFE,
        (
            "When you really think it through, business\x01",
            "is also a form of human relationship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C701")

    label("loc_C6FD")

    Call(0, 25)

    label("loc_C701")

    Jump("loc_CA64")

    label("loc_C704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_C921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_C7DA")

    ChrTalk(    #589
        0xFE,
        (
            "I came to listen to the old merchant\x01",
            "guy again today, too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #590
        0xFE,
        (
            "The, uh, place is kinda out of my spending\x01",
            "league, if you know what I mean. I couldn't\x01",
            "quite convince myself to step in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C91E")

    label("loc_C7DA")


    ChrTalk(    #591
        0xFE,
        (
            "The other day when I evacuated into\x01",
            "here I met a kind older man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0xFE,
        (
            "He was a former merchant himself\x01",
            "and gave me a lot of advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0xFE,
        (
            "He told me to come again tomorrow,\x01",
            "so I came, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0xFE,
        (
            "The, uh, place is kinda out of my spending\x01",
            "league, if you know what I mean. I couldn't\x01",
            "quite convince myself to step in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_C91E")

    Jump("loc_CA64")

    label("loc_C921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_CA64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_C9A7")

    ChrTalk(    #595
        0xFE,
        (
            "Just as I finally got permission to have\x01",
            "a store and was preparing to open...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #596
        0xFE,
        "*sigh* Talk about a shock...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA64")

    label("loc_C9A7")


    ChrTalk(    #597
        0xFE,
        (
            "Just as I finally got permission to have\x01",
            "a store and was preparing to open...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #598
        0xFE,
        (
            "I never thought something like\x01",
            "that could happen to the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #599
        0xFE,
        "*sigh* Talk about a shock...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_CA64")

    TalkEnd(0x17)
    Return()

    # Function_24_C645 end

    def Function_25_CA68(): pass

    label("Function_25_CA68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_CBF4")

    ChrTalk(    #600
        0x17,
        (
            "Umm, I think it's most important to catch\x01",
            "the customer's eye, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #601
        0x17,
        (
            "I know it's just a matter of advertising\x01",
            "and publicity, but...that costs money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #602
        0xD,
        (
            "The customer's eye goes to where\x01",
            "other customers are going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0xD,
        (
            "Satisfy each customer at a time,\x01",
            "and make sure they'll come back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #604
        0xD,
        (
            "That, more than anything, is the basis\x01",
            "of business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0x17,
        "I-I see...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)
    OP_A2(0x6)
    Jump("loc_CD9E")

    label("loc_CBF4")


    ChrTalk(    #606
        0xD,
        (
            "So, then, where in the market will\x01",
            "you be opening your store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #607
        0x17,
        "Umm, right next to the southern entrance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #608
        0x17,
        (
            "It just happened to be open, but\x01",
            "I think it's a pretty good spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #609
        0xD,
        "True. It's not bad at all, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #610
        0xD,
        (
            "If you're near the entrance, you'll need\x01",
            "a trick to stop the customer's legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #611
        0xD,
        (
            "Customers just entering tend to walk fast.\x01",
            "If you don't do anything they'll zoom right\x01",
            "by you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #612
        0x17,
        "I-I see...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_CD9E")

    Return()

    # Function_25_CA68 end

    def Function_26_CD9F(): pass

    label("Function_26_CD9F")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_CFC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_CE5D")

    ChrTalk(    #613
        0xFE,
        (
            "Atmosphere's critical in shopping. A temporary\x01",
            "store's not nearly enough to satisfy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #614
        0xFE,
        (
            "Buying something isn't the goal, it's\x01",
            "everything UNTIL you buy that's fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFC4")

    label("loc_CE5D")


    ChrTalk(    #615
        0xFE,
        (
            "The shopkeepers from the market are\x01",
            "operating out of the hotel, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #616
        0xFE,
        (
            "Atmosphere's critical in shopping. A temporary\x01",
            "store's not nearly enough to satisfy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #617
        0xFE,
        (
            "A tall ceiling, a nice display with good design\x01",
            "sense, and a modest, kind clerk...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #618
        0xFE,
        (
            "The sweet experience that is shopping is\x01",
            "born when all those elements blend together\x01",
            "in harmony.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_CFC4")

    Jump("loc_D319")

    label("loc_CFC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_D174")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_D079")

    ChrTalk(    #619
        0xFE,
        (
            "I'll just enjoy meals here until\x01",
            "the market's restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #620
        0xFE,
        (
            "After all, with everything that's happened,\x01",
            "I need to clear my mind with some\x01",
            "delicious meals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D171")

    label("loc_D079")


    ChrTalk(    #621
        0xFE,
        (
            "It seems the market's restoration\x01",
            "will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #622
        0xFE,
        (
            "I suppose I have no choice but to enjoy\x01",
            "meals here until the market's restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #623
        0xFE,
        (
            "After all, with everything that's happened,\x01",
            "I need to clear my mind with some\x01",
            "delicious meals.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_D171")

    Jump("loc_D319")

    label("loc_D174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_D24D")

    ChrTalk(    #624
        0xFE,
        "I ran here when I saw that enormous monster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #625
        0xFE,
        (
            "But, now that I look carefully,\x01",
            "this is the Anterose, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #626
        0xFE,
        (
            "Ahaha, well done, me. My body naturally\x01",
            "seeks out top-class establishments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D319")

    label("loc_D24D")


    ChrTalk(    #627
        0xFE,
        (
            "I thought a strong wind was blowing when\x01",
            "suddenly everything became very dark...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #628
        0xFE,
        (
            "The next moment, there was that huge\x01",
            "monster landing on the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #629
        0xFE,
        "I ran in here without even thinking.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_D319")

    TalkEnd(0x18)
    Return()

    # Function_26_CD9F end

    def Function_27_D31D(): pass

    label("Function_27_D31D")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_D48A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_D397")

    ChrTalk(    #630
        0xFE,
        (
            "Feels way different than the last time\x01",
            "I was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #631
        0xFE,
        "Today I feel strangely calm and natural.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D487")

    label("loc_D397")


    ChrTalk(    #632
        0xFE,
        (
            "I was invited by the mayor as thanks for\x01",
            "my efforts during the market's repair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #633
        0xFE,
        (
            "Perhaps because of that it feels very\x01",
            "different than when I was here last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #634
        0xFE,
        (
            "Today I feel strangely calm and natural,\x01",
            "even from my perspective.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)

    label("loc_D487")

    Jump("loc_D491")

    label("loc_D48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D491")

    label("loc_D491")

    TalkEnd(0x19)
    Return()

    # Function_27_D31D end

    def Function_28_D495(): pass

    label("Function_28_D495")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_D5F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_D522")

    ChrTalk(    #635
        0xFE,
        (
            "Yeah, the meals here really\x01",
            "are the best I've ever had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #636
        0xFE,
        (
            "It tastes even better knowing\x01",
            "it's on the mayor's tab.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5F1")

    label("loc_D522")


    ChrTalk(    #637
        0xFE,
        (
            "Yeah, the meals here really\x01",
            "are the best I've ever had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #638
        0xFE,
        (
            "It tastes even better knowing\x01",
            "it's on the mayor's tab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #639
        0xFE,
        (
            "Teehee, it was worth helping out with\x01",
            "the construction for a treat like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_D5F1")

    Jump("loc_D5FB")

    label("loc_D5F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D5FB")

    label("loc_D5FB")

    TalkEnd(0x1A)
    Return()

    # Function_28_D495 end

    def Function_29_D5FF(): pass

    label("Function_29_D5FF")

    Call(0, 30)
    Return()

    # Function_29_D5FF end

    def Function_30_D604(): pass

    label("Function_30_D604")

    TalkBegin(0x1B)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Golden Risotto] - 1400 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D681")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x0)
    TalkEnd(0x1B)
    Return()

    label("loc_D681")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7C0")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D786")
    SubMira(1400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #640
        "\x06Ate #2CGolden Risotto#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFC, 0x0)
    OP_31(0x1, 0xFC, 0x0)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x3, 0xFC, 0x0)
    OP_31(0x4, 0xFC, 0x0)
    OP_31(0x5, 0xFC, 0x0)
    OP_31(0x6, 0xFC, 0x0)
    OP_31(0x7, 0xFC, 0x0)
    OP_31(0x8, 0xFC, 0x0)
    OP_31(0x0, 0xFD, 0xDAC)
    OP_31(0x1, 0xFD, 0xDAC)
    OP_31(0x2, 0xFD, 0xDAC)
    OP_31(0x3, 0xFD, 0xDAC)
    OP_31(0x4, 0xFD, 0xDAC)
    OP_31(0x5, 0xFD, 0xDAC)
    OP_31(0x6, 0xFD, 0xDAC)
    OP_31(0x7, 0xFD, 0xDAC)
    OP_31(0x8, 0xFD, 0xDAC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D778")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x5)"), scpexpr(EXPR_END)), "loc_D748")
    Jump("loc_D778")

    label("loc_D748")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #641
        "\x06Learned [#2CGolden Risotto#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_D778")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_D7AE")

    label("loc_D786")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #642
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_D7AE")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x1B)
    Return()

    label("loc_D7C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7DA")
    FadeToBright(300, 0)
    TalkEnd(0x1B)
    Return()

    label("loc_D7DA")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8BE")

    ChrTalk(    #643
        0x1B,
        (
            "The people at the factory said\x01",
            "repairs were impossible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #644
        0x1B,
        "I'd like the stoves to at least be working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #645
        0x1B,
        (
            "It's hard to get our best flavor without\x01",
            "the strong heat of an orbal stove.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)
    Jump("loc_D940")

    label("loc_D8BE")


    ChrTalk(    #646
        0x1B,
        "I'd like the stoves to at least be working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #647
        0x1B,
        (
            "It's hard to get our best flavor without\x01",
            "the strong heat of an orbal stove.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D940")

    Jump("loc_E0CF")

    label("loc_D943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DA65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9ED")

    ChrTalk(    #648
        0x1B,
        (
            "Certainly it's hard on us not being able to use\x01",
            "orbments, but that doesn't make it okay to riot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #649
        0x1B,
        "I'm embarrassed as a fellow Bose citizen.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A)
    Jump("loc_DA62")

    label("loc_D9ED")


    ChrTalk(    #650
        0x1B,
        (
            "While I can understand wanting to riot,\x01",
            "that doesn't make it okay to actually do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #651
        0x1B,
        "Really! How shameful.\x02",
    )

    CloseMessageWindow()

    label("loc_DA62")

    Jump("loc_E0CF")

    label("loc_DA65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_DAC0")

    ChrTalk(    #652
        0x1B,
        "Ahh, I'm glad the market's been repaired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #653
        0x1B,
        "Yep, it's a very good thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0CF")

    label("loc_DAC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_DC6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_DB96")

    ChrTalk(    #654
        0x1B,
        (
            "Ever since that castella shop came, my sales\x01",
            "have just been on a downward slide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #655
        0x1B,
        "Still, though, I can't ask them to leave now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #656
        0x1B,
        (
            "...Stuck between my humanity and my finances.\x01",
            "*sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC6C")

    label("loc_DB96")


    ChrTalk(    #657
        0x1B,
        "This is bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #658
        0x1B,
        (
            "Ever since that castella shop came, my sales\x01",
            "have just been on a downward slide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #659
        0x1B,
        "Still, though, I can't ask them to leave now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #660
        0x1B,
        "R-Really, talk about uncomfortable situations.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_DC6C")

    Jump("loc_E0CF")

    label("loc_DC6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_DD87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_DCE0")

    ChrTalk(    #661
        0x1B,
        "That castella shop's really popular.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #662
        0x1B,
        (
            "Thanks to that, no one's been ordering\x01",
            "our food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD84")

    label("loc_DCE0")


    ChrTalk(    #663
        0x1B,
        "Man, that castella shop's really popular.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #664
        0x1B,
        (
            "Thanks to that, no one's been ordering\x01",
            "our food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #665
        0x1B,
        (
            "Haha...ha... Well, I suppose\x01",
            "this is just helping out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_DD84")

    Jump("loc_E0CF")

    label("loc_DD87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_DFDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_DEAE")

    ChrTalk(    #666
        0x1B,
        (
            "The ice cream and castella shop\x01",
            "owners evacuated over to our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #667
        0x1B,
        (
            "Seems like they're continuing their business,\x01",
            "so if you'd like, buy something from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #668
        0x1B,
        (
            "Really, they're business rivals of ours,\x01",
            "but, heck, gotta help each other out at\x01",
            "times like these, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFDC")

    label("loc_DEAE")


    ChrTalk(    #669
        0x1B,
        (
            "To have the market collapse...\x01",
            "That's just crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #670
        0x1B,
        (
            "We wanted to help, so we listed our\x01",
            "place as an evacuation destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #671
        0x1B,
        (
            "So, the people who run the ice cream\x01",
            "and castella stands came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #672
        0x1B,
        (
            "Seems like they're continuing their business,\x01",
            "so if you'd like, buy something from them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_DFDC")

    Jump("loc_E0CF")

    label("loc_DFDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_E0CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_E037")

    ChrTalk(    #673
        0x1B,
        (
            "We're a cheap, delicious, everyman's restaurant.\x01",
            "Take a load off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0CF")

    label("loc_E037")


    ChrTalk(    #674
        0x1B,
        (
            "Hey, welcome. We're a cheap, delicious,\x01",
            "everyman's restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #675
        0x1B,
        (
            "Our selling point's a more at-home atmosphere,\x01",
            "in contrast to the Anterose.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_E0CF")

    TalkEnd(0x1B)
    Return()

    # Function_30_D604 end

    def Function_31_E0D3(): pass

    label("Function_31_E0D3")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_E1CF")

    ChrTalk(    #676
        0xFE,
        "Our owner can't use anything but orbal stoves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #677
        0xFE,
        (
            "But lately we've had to resort to using fire\x01",
            "for cooking, so everything's been a bit\x01",
            "smoky and burnt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #678
        0xFE,
        (
            "Forget about flavor. The real issue is burning\x01",
            "the heck out of everything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAEE")

    label("loc_E1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2D2")

    ChrTalk(    #679
        0xFE,
        (
            "Our owner's acting like the riot's\x01",
            "something other people did, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #680
        0xFE,
        (
            "He's one of the people who barged into\x01",
            "the mayoral residence too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #681
        0xFE,
        (
            "He's sort of excluding himself from that little\x01",
            "mess and trying to put on airs, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)
    Jump("loc_E352")

    label("loc_E2D2")


    ChrTalk(    #682
        0xFE,
        (
            "He's one of the people who barged into\x01",
            "the mayoral residence too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #683
        0xFE,
        (
            "What he says and actually does are\x01",
            "total opposites.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E352")

    Jump("loc_EAEE")

    label("loc_E355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_E547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_E441")

    ChrTalk(    #684
        0xFE,
        (
            "We were in a real pinch there for a bit.\x01",
            "All our customers were being taken by\x01",
            "the castella shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #685
        0xFE,
        (
            "If the restoration had taken a bit longer,\x01",
            "they probably would have ended up\x01",
            "running us right out of business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E544")

    label("loc_E441")


    ChrTalk(    #686
        0xFE,
        "Phew! The market's been put back to right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #687
        0xFE,
        (
            "If the restoration had taken a bit longer,\x01",
            "we probably would have ended up being\x01",
            "swallowed up by the castella shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #688
        0xFE,
        (
            "Well, that probably would have made our\x01",
            "business better the way things are going.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_E544")

    Jump("loc_EAEE")

    label("loc_E547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_E6C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_E5DA")

    ChrTalk(    #689
        0xFE,
        (
            "Lately, we've pretty much just been\x01",
            "a castella bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #690
        0xFE,
        (
            "Eeeeeveryone eats the castella,\x01",
            "and noooooo one orders our cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6BD")

    label("loc_E5DA")


    ChrTalk(    #691
        0xFE,
        (
            "Lately, we've pretty much just been\x01",
            "a castella bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #692
        0xFE,
        (
            "Eeeeeveryone eats the castella,\x01",
            "and noooooo one orders our cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #693
        0xFE,
        (
            "Well, natural result,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #694
        0xFE,
        (
            "Our cooking's only real selling\x01",
            "point is it's cheap.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_E6BD")

    Jump("loc_EAEE")

    label("loc_E6C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_E8F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_E756")

    ChrTalk(    #695
        0xFE,
        (
            "The castella shop that relocated here after the\x01",
            "market mess is as popular as I'd thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #696
        0xFE,
        "They've taken all our customers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E8ED")

    label("loc_E756")


    ChrTalk(    #697
        0xFE,
        (
            "The castella shop that relocated here after the\x01",
            "market mess is as popular as I'd thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #698
        0xFE,
        (
            "The people working on the construction\x01",
            "come to buy some on their breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #699
        0xFE,
        (
            "The manager was impressed at first,\x01",
            "but now he doesn't have the confidence\x01",
            "to be impressed lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #700
        0xFE,
        (
            "This is what he gets for putting on airs.\x01",
            "It's not like we're some popular store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #701
        0xFE,
        "...Well, he gets what he deserves.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_E8ED")

    Jump("loc_EAEE")

    label("loc_E8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_EAA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_E9AF")

    ChrTalk(    #702
        0xFE,
        (
            "Letting them operate in our store...\x01",
            "Isn't that a bit too generous?\x01",
            "We're rivals, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #703
        0xFE,
        (
            "I'm pretty sure the bartender's cooking\x01",
            "would lose to them hands down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAA5")

    label("loc_E9AF")


    ChrTalk(    #704
        0xFE,
        (
            "It makes sense to welcome people who\x01",
            "evacuated from the market, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #705
        0xFE,
        (
            "Letting them operate in our store...\x01",
            "Isn't that a bit too generous?\x01",
            "We're rivals, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #706
        0xFE,
        (
            "I wonder if he intends to wipe out\x01",
            "what little business we get.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_EAA5")

    Jump("loc_EAEE")

    label("loc_EAA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_EAEE")

    ChrTalk(    #707
        0xFE,
        (
            "Welcome! Sit anywhere you like.\x01",
            "There's plenty of room...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAEE")

    TalkEnd(0x1C)
    Return()

    # Function_31_E0D3 end

    def Function_32_EAF2(): pass

    label("Function_32_EAF2")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_EC07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_EB76")

    ChrTalk(    #708
        0xFE,
        (
            "I'm sure what I've sought\x01",
            "after is in these lands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #709
        0xFE,
        "I WILL complete my research and claim the honor!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC07")

    label("loc_EB76")


    ChrTalk(    #710
        0xFE,
        "Hehehe... I'm a researcher of ancient life.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #711
        0xFE,
        (
            "I'm sure what I've sought\x01",
            "after is in these lands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #712
        0xFE,
        "Ha, well, look forward to it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C)

    label("loc_EC07")

    TalkEnd(0x1D)
    Return()

    # Function_32_EAF2 end

    def Function_33_EC0B(): pass

    label("Function_33_EC0B")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_ED95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_EC9A")

    ChrTalk(    #713
        0xFE,
        (
            "It really is fun to work with someone\x01",
            "you love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #714
        0xFE,
        (
            "Right now I just want to enjoy that\x01",
            "feeling a little bit longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED92")

    label("loc_EC9A")


    ChrTalk(    #715
        0xFE,
        (
            "Until now he and I have run\x01",
            "our stores separately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #716
        0xFE,
        (
            "It really is fun to work with someone\x01",
            "you love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #717
        0xFE,
        (
            "I just want to enjoy that feeling...\x01",
            "a little bit longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #718
        0xFE,
        (
            "After all, we'll be back to rivals\x01",
            "once the market re-opens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_ED92")

    Jump("loc_EF0E")

    label("loc_ED95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_EE9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_EE14")

    ChrTalk(    #719
        0xFE,
        "After a night, I'm finally calm again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #720
        0xFE,
        (
            "Right now he and I are working\x01",
            "together to get through this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE99")

    label("loc_EE14")


    ChrTalk(    #721
        0xFE,
        "Welcome, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #722
        0xFE,
        "After a night, I'm finally calm again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #723
        0xFE,
        (
            "Right now he and I are working\x01",
            "together to get through this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_EE99")

    Jump("loc_EF0E")

    label("loc_EE9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_EF0E")

    ChrTalk(    #724
        0xFE,
        (
            "Some rubble came crashing down\x01",
            "right behind my wagon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #725
        0xFE,
        "I wonder if the people there are okay...\x02",
    )

    CloseMessageWindow()

    label("loc_EF0E")

    TalkEnd(0x1E)
    Return()

    # Function_33_EC0B end

    def Function_34_EF12(): pass

    label("Function_34_EF12")

    TalkBegin(0x1F)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF72")
    OP_0D()
    OP_A9(0x51)
    OP_56(0x0)
    TalkEnd(0x1F)
    Return()

    label("loc_EF72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF83")
    TalkEnd(0x1F)
    Return()

    label("loc_EF83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_F125")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_F027")

    ChrTalk(    #726
        0xFE,
        (
            "If we work together, I feel like we\x01",
            "could make some really good stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #727
        0xFE,
        (
            "Maybe we should develop some new\x01",
            "product once the market reopens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F122")

    label("loc_F027")


    ChrTalk(    #728
        0xFE,
        (
            "It's really been a while since I worked with\x01",
            "Katrina, but it's been fun. I've discovered\x01",
            "a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #729
        0xFE,
        (
            "If we work together, I feel like we\x01",
            "could make some really good stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #730
        0xFE,
        (
            "Maybe we should develop some new\x01",
            "product once the market reopens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_F122")

    Jump("loc_F4F4")

    label("loc_F125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_F348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_F1E4")

    ChrTalk(    #731
        0xFE,
        (
            "The reconstruction work's begun,\x01",
            "but it'll be a while before it's\x01",
            "back open for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #732
        0xFE,
        (
            "Anyway, right now we need to keep up\x01",
            "business and not lose our customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F345")

    label("loc_F1E4")


    ChrTalk(    #733
        0xFE,
        (
            "The reconstruction work's begun,\x01",
            "but it'll be a while before it's\x01",
            "back open for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #734
        0xFE,
        (
            "Anyway, right now we need to keep up\x01",
            "business and not lose our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #735
        0xFE,
        (
            "Still, maybe because we changed locations,\x01",
            "we're not getting as many customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #736
        0xFE,
        (
            "Katrina was worried this one repeat guy\x01",
            "customer who came every day might\x01",
            "not return.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_F345")

    Jump("loc_F4F4")

    label("loc_F348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_F4F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_F3EB")

    ChrTalk(    #737
        0xFE,
        (
            "It seems like the shock's been\x01",
            "pretty big for Katrina, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #738
        0xFE,
        (
            "At times like this I've got to hold in\x01",
            "there and support her as her fiance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4F4")

    label("loc_F3EB")


    ChrTalk(    #739
        0xFE,
        (
            "It's a terrible situation, but for the sake\x01",
            "of my fiancee, we've got to overcome it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #740
        0xFE,
        "A while back I left the stand empty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #741
        0xFE,
        (
            "During that time, she held down the\x01",
            "fort all on her own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #742
        0xFE,
        (
            "That's why this time...\x01",
            "This time it's my turn to support her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_F4F4")

    TalkEnd(0x1F)
    Return()

    # Function_34_EF12 end

    def Function_35_F4F8(): pass

    label("Function_35_F4F8")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_F58F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_F576")

    ChrTalk(    #743
        0x20,
        "Remember: I'm counting on you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #744
        0x20,
        (
            "If anything turns up, you come\x01",
            "right back here, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F58C")

    label("loc_F576")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_F588")
    Call(1, 4)
    Jump("loc_F58C")

    label("loc_F588")

    Call(1, 3)

    label("loc_F58C")

    Jump("loc_F61D")

    label("loc_F58F")


    ChrTalk(    #745
        0x20,
        "*siiigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #746
        0x20,
        (
            "Foreign lands are always\x01",
            "so frightening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #747
        0x20,
        (
            "I'm sure that girl has had\x01",
            "her fair share of hardships\x01",
            "as well, but still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F61D")

    TalkEnd(0x20)
    Return()

    # Function_35_F4F8 end

    def Function_36_F621(): pass

    label("Function_36_F621")

    Return()

    # Function_36_F621 end

    def Function_37_F622(): pass

    label("Function_37_F622")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_F70E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6ED")

    ChrTalk(    #748
        0xFE,
        "*munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #749
        0xFE,
        "*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #750
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #751
        0xFE,
        (
            "It could just be my imagination,\x01",
            "but...this seems kinda burnt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #752
        0xFE,
        (
            "Eh, whatever. It's all the same\x01",
            "once it's down in your stomach.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)
    Jump("loc_F70B")

    label("loc_F6ED")


    ChrTalk(    #753
        0xFE,
        "*munch* *munch*...*gulp*\x02",
    )

    CloseMessageWindow()

    label("loc_F70B")

    Jump("loc_F8A5")

    label("loc_F70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F8A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7FB")

    ChrTalk(    #754
        0xFE,
        (
            "Oh, hey there. You're bracers,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #755
        0xFE,
        (
            "I've seen you on the Cecilia\x01",
            "a few times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #756
        0xFE,
        (
            "Sorry for our ship being outta\x01",
            "commission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #757
        0xFE,
        (
            "Doesn't look like we can leave\x01",
            "port, so I'm just gettin' some grub.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)
    Jump("loc_F8A5")

    label("loc_F7FB")


    ChrTalk(    #758
        0xFE,
        "Nooow, what should I eat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #759
        0xFE,
        (
            "The dish of the day here's\x01",
            "expensive, so I screw that\x01",
            "one. Nope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #760
        0xFE,
        (
            "I mean, that's not even somethin'\x01",
            "you could eat on your own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8A5")

    TalkEnd(0x22)
    Return()

    # Function_37_F622 end

    def Function_38_F8A9(): pass

    label("Function_38_F8A9")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_F8B6")
    Jump("loc_FA3C")

    label("loc_F8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_F8C0")
    Jump("loc_FA3C")

    label("loc_F8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_FA3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 1)), scpexpr(EXPR_END)), "loc_F95D")

    ChrTalk(    #761
        0xFE,
        (
            "The castella lady's running\x01",
            "a shop with her fiance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #762
        0xFE,
        (
            "I figured it'd eventually turn\x01",
            "out like this, but it's still kind\x01",
            "of a shock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA3C")

    label("loc_F95D")


    ChrTalk(    #763
        0xFE,
        (
            "I heard the castella lady'd\x01",
            "evacuated to this bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #764
        0xFE,
        (
            "But when I came inside,\x01",
            "I saw her and her fiance\x01",
            "running the shop together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #765
        0xFE,
        (
            "I figured it'd eventually turn\x01",
            "out like this, but it's still kind\x01",
            "of a shock.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x21)

    label("loc_FA3C")

    TalkEnd(0x25)
    Return()

    # Function_38_F8A9 end

    SaveToFile()

Try(main)
