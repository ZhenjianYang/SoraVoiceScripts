from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '托露塔',                               # 9
        '托露塔',                               # 10
        '伊莉莎',                               # 11
        '德瑟鲁',                               # 12
        '福克纳',                               # 13
        '矿工提恩特',                           # 14
        '矿工彭兹',                             # 15
        '佩特洛夫船长',                         # 16
        '乘务员罗杰',                           # 17
        '拉欧老人',                             # 18
        '布露姆老奶奶',                         # 19
        '洛连特风味炖煮',                       # 20
        '阿鲁姆',                               # 21
        '艾娅莉',                               # 22
        '新郎的亲属',                           # 23
        '新郎的亲属',                           # 24
        '新郎的亲属',                           # 25
        '新娘的亲属',                           # 26
        '新娘的亲属',                           # 27
        '新娘的亲属',                           # 28
        '新娘的朋友',                           # 29
        '新娘的朋友',                           # 30
        '赛拉',                                 # 31
        '料理',                                 # 32
        '料理',                                 # 33
        '料理',                                 # 34
        '料理',                                 # 35
        '料理',                                 # 36
        '迪拜恩教区长',                         # 37
        '安敦',                                 # 38
        '爱娜',                                 # 39
        '奥利维尔',                             # 40
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
        '酒杯',                                 # 52
        '酒杯',                                 # 53
        '酒杯',                                 # 54
        '酒杯',                                 # 55
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
        "Function_6_25E8",         # 06, 6
        "Function_7_35B9",         # 07, 7
        "Function_8_4658",         # 08, 8
        "Function_9_571E",         # 09, 9
        "Function_10_5A14",        # 0A, 10
        "Function_11_5B5E",        # 0B, 11
        "Function_12_5C7A",        # 0C, 12
        "Function_13_5D38",        # 0D, 13
        "Function_14_60F3",        # 0E, 14
        "Function_15_6214",        # 0F, 15
        "Function_16_62D2",        # 10, 16
        "Function_17_6325",        # 11, 17
        "Function_18_637C",        # 12, 18
        "Function_19_63C9",        # 13, 19
        "Function_20_6414",        # 14, 20
        "Function_21_646F",        # 15, 21
        "Function_22_64B0",        # 16, 22
        "Function_23_64FB",        # 17, 23
        "Function_24_6550",        # 18, 24
        "Function_25_665B",        # 19, 25
        "Function_26_67A2",        # 1A, 26
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                  # 0
            "买东西\x01",                                # 1
            "招牌菜『三蛋黄杂烩粥』　1600米拉\x01",      # 2
            "离开\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58")
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4D")
    OP_A9(0x9)
    Jump("loc_D4F")

    label("loc_D4D")

    OP_A9(0x4)

    label("loc_D4F")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_D58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E69")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E31")
    SubMira(1600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x02三蛋黄杂烩粥\x07\x00已经品尝过了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_DF7")
    Jump("loc_E23")

    label("loc_DF7")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x02三蛋黄杂烩粥\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_E23")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_E57")

    label("loc_E31")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_E57")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xA)
    Return()

    label("loc_E69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E83")
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_E83")

    FadeToBright(300, 0)

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A5")

    ChrTalk(    #3
        0xA,
        "欢迎光临～☆\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x102, 400)
    Sleep(1000)

    ChrTalk(    #4
        0xA,
        "啊，这不是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1041F好久不见啦，伊莉莎。\x02\x03",

            "太好了，总算放心了。\x01",
            "看起来似乎很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "你终于回来了啊！\x01",
            "我都快担心死了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "真是的～艾丝蒂尔每次\x01",
            "都带不同的男人回来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "难道和约修亚\x01",
            "闹别扭了吗？\x01",
            "真让人不放心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1054F哈、哈哈……\x02\x03",

            "抱歉，\x01",
            "让你担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1007F不、不愧是伊莉莎……\x01",
            "担心的东西都和别人不同。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #11
        0xA,
        (
            "那么……\x01",
            "你们二位，打算怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        (
            "这次是否准备\x01",
            "多休息一下再走？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1015F嗯，我也想那样……\x02\x03",

            "不过还是要看\x01",
            "情况而定了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(    #14
        0x103,
        (
            "#021F嗯，稍微放松一下也无所谓，\x02\x03",

            "不管是谁也都需要\x01",
            "偶尔休息一下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C6")

    label("loc_1106")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1170")

    ChrTalk(    #15
        0x108,
        (
            "#070F啊，稍微放松一下\x01",
            "也没关系。\x02\x03",

            "不管有什么重大任务，\x01",
            "我们游击士毕竟也只是普通人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C6")

    label("loc_1170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(    #16
        0x106,
        (
            "#051F哈～稍微休息一下也没关系。\x02\x03",

            "但是可不能放松过头\x01",
            "把正事忘了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C6")


    ChrTalk(    #17
        0xA,
        (
            "那么，等工作完成之后\x01",
            "要再来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "还想让约修亚见识一下\x01",
            "我充满自信的新料理呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1040F伊莉莎的新料理吗……\x01",
            "那可是一定要吃的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_127C")

    ChrTalk(    #20
        0x101,
        "#1001F嗯！一定会再来吃！\x02",
    )

    CloseMessageWindow()
    Jump("loc_129C")

    label("loc_127C")


    ChrTalk(    #21
        0x101,
        "#1001F嗯，一定会再来吃的！\x02",
    )

    CloseMessageWindow()

    label("loc_129C")

    OP_A2(0x6)
    OP_A2(0x20A3)
    Jump("loc_16E0")

    label("loc_12A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_13B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130F")

    ChrTalk(    #22
        0xA,
        (
            "我的料理已经\x01",
            "被写到菜单上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "这可是我充满自信的作品，\x01",
            "希望约修亚也能尝一尝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE")

    label("loc_130F")


    ChrTalk(    #24
        0xA,
        (
            "今天的客人\x01",
            "似乎不同寻常啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "好像在举办结婚仪式的庆祝会呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "不但忙得要死，\x01",
            "而且导力器也不能使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "呼～今天早上的工作\x01",
            "简直就是战场啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x6)
    OP_A2(0x5)

    label("loc_13AE")

    Jump("loc_16E0")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_14E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1480")

    ChrTalk(    #28
        0xA,
        (
            "啊～艾丝蒂尔和约修亚～\x01",
            "欢迎光临～☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "抱歉啊，这里乱的很，\x01",
            "其实正在举办结婚仪式的庆祝会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "所以今天早上的厨房\x01",
            "简直就是恐怖的战场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "不但忙得要死，\x01",
            "而且导力器也不能使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_14DE")

    label("loc_1480")


    ChrTalk(    #32
        0xA,
        (
            "所以今天早上的厨房\x01",
            "简直就是恐怖的战场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "准备庆祝会忙得要死，\x01",
            "而且导力器也不能使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DE")

    Jump("loc_16E0")

    label("loc_14E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_15D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157E")

    ChrTalk(    #34
        0xA,
        "啊！欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "庆祝会的料理终于\x01",
            "准备完成了哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "好期待结婚仪式结束之后\x01",
            "客人们赶快过来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        "呼～总算可以休息一下了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_15D0")

    label("loc_157E")


    ChrTalk(    #38
        0xA,
        (
            "庆祝会的料理终于\x01",
            "准备完成了哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "导力器无法使用，\x01",
            "干什么都比平时花时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D0")

    Jump("loc_16E0")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1696")

    ChrTalk(    #40
        0xA,
        "啊～艾丝蒂尔和约修亚～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "今天有人预约在店里\x01",
            "举办庆祝会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "所以我和爸爸从一大早\x01",
            "开始就忙个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "不仅如此，而且连导力器\x01",
            "也都不能使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        "真是的～简直要累死人。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_16E0")

    label("loc_1696")


    ChrTalk(    #45
        0xA,
        (
            "不但要准备庆祝会，\x01",
            "而且导力器也不能使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "我和爸爸都快\x01",
            "忙死了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E0")

    Jump("loc_25E4")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 0)), scpexpr(EXPR_END)), "loc_1854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(    #47
        0xA,
        (
            "那么浓的雾，\x01",
            "竟然这么快就散去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xA,
        (
            "真是让人觉得\x01",
            "不可思议啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17EA")

    label("loc_1749")


    ChrTalk(    #49
        0xA,
        (
            "妈妈醒来的时候，\x01",
            "天已经完全放晴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "那么浓的雾，\x01",
            "却这么快就散去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "妈妈昏睡过去的原因\x01",
            "到现在也让人想不通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "这次的事件还\x01",
            "真是让人奇怪呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_17EA")

    Jump("loc_1851")

    label("loc_17ED")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #53
        0xA,
        (
            "妈妈的事\x01",
            "多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "雾散了，\x01",
            "店里也恢复了正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "今后也要更加\x01",
            "努力制作料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1851")

    Jump("loc_1A3C")

    label("loc_1854")

    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #56
        0xA,
        "啊～艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "我妈妈醒来了呢。\x01",
            "真是太谢谢你们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "呜，真的太感谢了… \x01",
            "……实在太好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1017F伊莉莎……\x02\x03",

            "嗯，我也松了一口气呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #60
        0xA,
        (
            "……雪拉姐也是。\x01",
            "真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#524F没什么……\x01",
            "能帮上忙我也很高兴。\x02\x03",

            "今后也要多帮助\x01",
            "托露塔阿姨啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        "是！我一定会努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "下次再叫上爱娜\x01",
            "一起来喝酒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x103,
        (
            "#027F呵呵，我很期待呢。\x02\x03",

            "#525F也向福克纳\x01",
            "问声好吧㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1007F哇……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A36")

    ChrTalk(    #66
        0x104,
        "#034F这、这是死亡宣告啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1A36")

    OP_A2(0x1A60)
    OP_A2(0x6)

    label("loc_1A3C")

    Jump("loc_25E4")

    label("loc_1A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1AA2")
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #67
        0xA,
        "拜托了，不要乱来啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "连艾丝蒂尔也倒下的话…\x01",
            "我该怎么办才好啊…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCD")

    label("loc_1AA2")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #69
        0xA,
        (
            "啊～艾丝蒂尔，还有大家，\x01",
            "以后要再来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0xA,
        "……不过，发生什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "艾丝蒂尔的表情\x01",
            "好像很消沉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1025F啊，没什么……\x02\x03",

            "#1016F不要紧，我没事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "真的吗？\x01",
            "你是太累了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "虽然工作应该努力，\x01",
            "但也不要太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1BCD")

    Jump("loc_25E4")

    label("loc_1BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C22")
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #75
        0xA,
        (
            "艾丝蒂尔你们\x01",
            "要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "雾好像比昨天\x01",
            "更加浓了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC7")

    label("loc_1C22")

    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 0)
    Sleep(400)

    ChrTalk(    #77
        0xA,
        "啊～艾丝蒂尔和大家。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "妈妈的样子从昨天\x01",
            "开始就一直没变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "下次再来看看有\x01",
            "什么情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "我……今天要守在\x01",
            "妈妈身旁… \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1CC7")

    Jump("loc_25E4")

    label("loc_1CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 2)), scpexpr(EXPR_END)), "loc_1DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D60")

    ChrTalk(    #81
        0xA,
        (
            "外边的雾还\x01",
            "真厉害啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "店里虽然还没关系，\x01",
            "但阳台的椅子也要去收拾一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "总这样下去的话，\x01",
            "潮湿可真是让人受不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAF")

    label("loc_1D60")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #84
        0xA,
        (
            "无论如何，今天就\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "有兴趣的话尝尝\x01",
            "我的新料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAF")

    Jump("loc_217D")

    label("loc_1DB2")

    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #86
        0xA,
        "啊…这不是艾丝蒂尔吗！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #87
        0xA,
        "连雪拉扎德小姐也来拉！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        "#021F呵呵～最近还好吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1017F嘿嘿，真是好久不见了啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #90
        0xA,
        (
            "太好了～～\x01",
            "看来训练顺利结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "我真是好担心呢～\x01",
            "总算是回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1011F现在有些工作，\x01",
            "才在各地来回跑。\x02\x03",

            "所以一直到现在\x01",
            "才回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        "呵呵～果然很忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "对了，听说训练\x01",
            "是在国外进行的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "还真是厉害呀，\x01",
            "游击士果然是国际性的职业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1008F哈哈，哪里～\x01",
            "过奖过奖。\x02\x03",

            "虽说是国外，\x01",
            "但也只是协会的设施而已。\x02\x03",

            "#1015F……～不过也多亏这次训练\x01",
            "让我转换心情下定决心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        "呼～是下定决心啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "那么…那条裙子\x01",
            "也是你决心的表现吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1008F啊……\x01",
            "果然注意到了啊。\x02\x03",

            "#1013F那个……是不是很奇怪？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "哪里的话啊～\x01",
            "很适合你的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "虽然式样可爱，\x01",
            "但却活动方便，一点也不累赘。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        "嗯，和艾丝蒂尔真是绝配啊⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1016F谢、谢谢称赞。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "我明白约修亚的事情\x01",
            "给你带来了很大压力…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "不过一定要保持现在的精神继续努力啊！\x01",
            "那样才像艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1017F嗯、嗯……我会加油的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1882)
    OP_A2(0x5)

    label("loc_217D")

    Jump("loc_25E4")

    label("loc_2180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_25E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 3)), scpexpr(EXPR_END)), "loc_2202")

    ChrTalk(    #107
        0xA,
        "对啦对啦～艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#506F啊，还有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "缇欧可是\x01",
            "很想你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "农场的那些\x01",
            "孩子也是一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E4")

    label("loc_2202")

    TurnDirection(0xA, 0x101, 0)

    ChrTalk(    #111
        0xA,
        "欢迎光临……\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0xA,
        "艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#001F伊莉莎，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        "什么好久不见嘛～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "自从你去了柏斯以后\x01",
            "就一直没回来过！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#505F啊，因为发生了很多事情……\x02\x03",

            "#008F总之让你担心了，对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "事情我也听说了，\x01",
            "你终于升为正游击士了，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "对了，我也终于可以\x01",
            "下厨做料理了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#004F好棒啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xA,
        (
            "嘿嘿嘿，那就经常来尝尝\x01",
            "我亲手作的料理吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#001F嗯，那是一定的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xA,
        (
            "……好了，寒暄结束，\x01",
            "转入正题吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#505F……正题？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xA,
        "别再装傻啦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xA,
        (
            "（你和约修亚怎么了？\x01",
            "　那个男人又是谁～？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#501F（啊…………）\x02\x03",

            "#008F（你、你误会啦！！）\x02\x03",

            "#503F（凯文先生是担心我孤身一人，\x01",
            "　才会陪同一起的……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "（喔……担心你孤身一人，\x01",
            "　所以陪同一起…吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#504F啊啊啊啊啊……\x01",
            "总之不是你想象中的那样啦！！\x02\x03",

            "#506F这就要回家\x01",
            "去见约修亚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        (
            "好了，今天就\x01",
            "聊到这里吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xA,
        (
            "我也要开始工作了，\x01",
            "下次你一定要带上约修亚，三个人一起来啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xA,
        (
            "看起来似乎有很多\x01",
            "有趣的内情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#007F呵呵呵……\x01",
            "都说了不是你想的那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x142,
        "#1060F？？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x102B)

    label("loc_25E4")

    TalkEnd(0xA)
    Return()

    # Function_5_CA5 end

    def Function_6_25E8(): pass

    label("Function_6_25E8")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298F")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #134
        0xFE,
        "噢，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #135
        0xFE,
        (
            "怎么回事，今天连\x01",
            "约修亚也一起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        "#1040F好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "噢！平安无事就比什么都好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "今天在洛连特有工作吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1002F嗯……有些麻烦\x01",
            "的事情需要处理。\x02\x03",

            "德瑟鲁大叔似乎\x01",
            "很烦恼的样子啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #140
        0xFE,
        (
            "啊～导力炉没法用了，\x01",
            "真让人头疼。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_27C8")

    ChrTalk(    #141
        0xFE,
        (
            "这样一来，庆祝会的料理\x01",
            "可要费力气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1004F哈，果然是专业的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        "#1040F这就是厨师的自尊啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #144
        0xFE,
        (
            "必须借助道具才能做菜的厨师\x01",
            "便不能算是一流的厨师。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290F")

    label("loc_27C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_285F")

    ChrTalk(    #145
        0xFE,
        (
            "今天这里要\x01",
            "举办一个庆祝会呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #146
        0x101,
        (
            "#1004F庆、庆祝会吗……\x01",
            "那么料理准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "嗯，总算是都\x01",
            "准备好了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290F")

    label("loc_285F")


    ChrTalk(    #148
        0xFE,
        (
            "今天这里要\x01",
            "举办一个庆祝会呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #149
        0x101,
        "#1004F庆、庆祝会？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#1044F准备料理\x01",
            "的事没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #151
        0xFE,
        (
            "一流的厨师可不能没了道具\x01",
            "就什么都干不了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290F")


    ChrTalk(    #152
        0xFE,
        (
            "当然了，还是很希望\x01",
            "赶快恢复正常…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "所以一切就拜托\x01",
            "你们游击士了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1006F啊……嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        "#1040F我们会尽力的！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20A1)
    Jump("loc_2C07")

    label("loc_298F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_2A93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2B")

    ChrTalk(    #156
        0xFE,
        (
            "看来庆祝会\x01",
            "办得很顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "欢声笑语、祝福的言辞，\x01",
            "还有丰富美味的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "嗯，真是完美啊！\x01",
            "对厨师来说，这就是最幸福的一刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2A90")

    label("loc_2A2B")


    ChrTalk(    #159
        0xFE,
        (
            "看来庆祝会\x01",
            "办得很顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "那么，接下来\x01",
            "该准备甜品了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "预定品种是香槟酒口味\x01",
            "的冰淇淋。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A90")

    Jump("loc_2C07")

    label("loc_2A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1F")

    ChrTalk(    #162
        0xFE,
        (
            "呼，庆祝会的料理\x01",
            "终于全部做完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "今日的主打菜式是\x01",
            "香草为配料的肉料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "嗯，料理的香气\x01",
            "这里都能闻到呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2B73")

    label("loc_2B1F")


    ChrTalk(    #165
        0xFE,
        (
            "庆祝会的主打菜式是\x01",
            "香草为配料的肉料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "嗯～料理的香气让\x01",
            "身体彻底放松了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B73")

    Jump("loc_2C07")

    label("loc_2B76")


    ChrTalk(    #167
        0xFE,
        (
            "导力炉无法使用\x01",
            "确实让人头疼…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "但不借助工具就不会做菜的人，\x01",
            "根本就不能算是真正的厨师！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "呼！就算只用手边的工具，\x01",
            "我也一定能完成的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C07")

    Jump("loc_35B5")

    label("loc_2C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CC3")

    ChrTalk(    #170
        0xFE,
        (
            "多亏布露姆老奶奶，\x01",
            "总算学会了那道菜的做法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "虽然烹饪方法很复杂，\x01",
            "但我会努力掌握，\x01",
            "然后加到菜单中的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "今天真的是\x01",
            "多谢各位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "那么，接下来也要加油啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B5")

    label("loc_2CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2CD5")
    Call(1, 6)
    Jump("loc_35B5")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_2CE7")
    Call(1, 5)
    Jump("loc_35B5")

    label("loc_2CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_2D4E")

    ChrTalk(    #174
        0xFE,
        "调查的事就拜托各位了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "找到食谱以后\x01",
            "别忘了马上来报告啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "另外食材也不要忘记。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35B5")

    label("loc_2D4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2DDA")

    ChrTalk(    #177
        0xFE,
        (
            "哟，艾丝蒂尔。\x01",
            "调查进行得如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "找到食谱以后\x01",
            "别忘了马上来报告啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "对了对了，到那时\x01",
            "食材也不要忘记啊，拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B5")

    label("loc_2DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2DFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2DF6")
    Call(1, 1)
    Jump("loc_2DFA")

    label("loc_2DF6")

    Call(1, 0)

    label("loc_2DFA")

    Jump("loc_35B5")

    label("loc_2DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(    #180
        0xFE,
        (
            "雾散了，托露塔也醒来了。\x01",
            "总算是让人松了口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "艾丝蒂尔，你们今天也\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "想点什么请随意说！\x01",
            "我会认真做的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F3F")

    label("loc_2E93")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #183
        0xFE,
        "哟，艾丝蒂尔，还有大家！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "我家的\x01",
            "托露塔也醒来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "这次真是快\x01",
            "担心死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "难得来一次，\x01",
            "今天就多待一会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "我会给\x01",
            "大家制作最拿手的料理的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2F3F")

    Jump("loc_35B5")

    label("loc_2F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_305C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F90")

    ChrTalk(    #188
        0xFE,
        (
            "托露塔\x01",
            "好像睡得很舒服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "完全都不知道别人有多担心…\x02",
    )

    CloseMessageWindow()
    Jump("loc_3059")

    label("loc_2F90")


    ChrTalk(    #190
        0xFE,
        (
            "趁着早上有空，\x01",
            "来看看她的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "她似乎完全都没察觉到，\x01",
            "睡得那么熟… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "哈哈，不过看到她那熟睡的样子，\x01",
            "也算是放心多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "那么，要赶快\x01",
            "回厨房了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "不然福克纳一定\x01",
            "又会大喊大叫了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3059")

    Jump("loc_35B5")

    label("loc_305C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30D5")

    ChrTalk(    #195
        0xFE,
        (
            "托露塔的样子没什么变化。\x01",
            "睡得很熟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "要是没吃早饭的话，\x01",
            "就在这里吃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "还能增加些人气呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3175")

    label("loc_30D5")


    ChrTalk(    #198
        0xFE,
        "啊，今天早上雾还是这么大啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "昨天就很担心，\x01",
            "托露塔的样子没什么变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "但听了教区长的话之后\x01",
            "就平静不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "呼～现在也只有\x01",
            "安安静静地观望了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3175")

    Jump("loc_35B5")

    label("loc_3178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 3)), scpexpr(EXPR_END)), "loc_3306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_31E4")

    ChrTalk(    #202
        0xFE,
        (
            "雾实在太大，\x01",
            "在一楼什么都看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "希望别持续太久，\x01",
            "早点天晴吧…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3279")

    label("loc_31E4")


    ChrTalk(    #204
        0xFE,
        (
            "今天外边的雾\x01",
            "还是很大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "真担心我的店啊，\x01",
            "在一楼什么都看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "因为这些雾\x01",
            "而没法进货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "我家的店全都是\x01",
            "选用最新鲜的食材。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3279")

    Jump("loc_3303")

    label("loc_327C")


    ChrTalk(    #208
        0xFE,
        (
            "话虽如此……\x01",
            "今天怎么这么大雾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "真担心我的店啊，\x01",
            "在一楼什么都看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "算了，反正不影响正常营业，\x01",
            "还是努力工作去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3303")

    Jump("loc_3406")

    label("loc_3306")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #211
        0xFE,
        (
            "哟，艾丝蒂尔和雪拉扎德。\x01",
            "好久不见了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#1001F嗯，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x103,
        "#020F呵呵，最近还好吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #214
        0xFE,
        (
            "嗯，还是和以前一样，\x01",
            "生意很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "伊莉莎的新料理\x01",
            "也很受好评呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "工作之余就来\x01",
            "这里休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1893)
    OP_A2(0x4)

    label("loc_3406")

    Jump("loc_35B5")

    label("loc_3409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_35B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_3470")

    ChrTalk(    #217
        0xFE,
        (
            "对了对了，我们增加\x01",
            "了新菜式哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "就是『三蛋黄杂烩粥』。\x01",
            "有兴趣的话来尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B5")

    label("loc_3470")


    ChrTalk(    #219
        0xFE,
        "哟！欢迎光临。\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    TurnDirection(0xB, 0x101, 300)

    ChrTalk(    #220
        0xFE,
        "啊，这不是艾丝蒂尔吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#001F德瑟鲁大叔，您很有精神啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "哈哈，我一向都是如此啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "在心情好的时候制作的料理，\x01",
            "客人吃起来会更觉得美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#506F哈哈，确实是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "对了对了，我们增加\x01",
            "了新菜式哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "就是『三蛋黄杂烩粥』。\x01",
            "有兴趣的话来尝尝吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x104B)

    label("loc_35B5")

    TalkEnd(0xB)
    Return()

    # Function_6_25E8 end

    def Function_7_35B9(): pass

    label("Function_7_35B9")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397F")
    TurnDirection(0x8, 0x102, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #227
        0xFE,
        (
            "啊……！？\x01",
            "艾丝蒂尔和约修亚\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "啊啊！你们两个\x01",
            "终于一起回来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        (
            "#1008F嘿嘿……\x01",
            "让您久等了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x102,
        "#1040F好久不见了，托露塔阿姨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "呵呵呵，不用那么正经啦，\x01",
            "又不是外人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "你们两个……\x01",
            "正赶在这种非常时期回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        "#1026F啊，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x102,
        "#1040F店里没什么问题吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "嗯，还好，先生和\x01",
            "伊莉莎一直都很努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "只是…进货现在\x01",
            "成了大问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "定期船和搬运车\x01",
            "都动不了了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        "#1043F果然，物流问题很严重呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "这个对店里的影响很大，\x01",
            "实在让人头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "呼～为什么讨厌的事件\x01",
            "一直发生个没完呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1003F确实如此呢……\x02\x03",

            "#1006F不过我们游击士一定\x01",
            "会努力解决这一切的。\x02\x03",

            "虽然也许要花些时间，\x01",
            "但肯定会让一切都恢复正常！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x102,
        (
            "#1040F当然了，不仅是我们在努力，\x01",
            "王国军也一直在努力思考对策。\x02\x03",

            "在转机出现之前，\x01",
            "请阿姨也要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "是啊…\x01",
            "现在正是考验人的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "呼，总之只有努力\x01",
            "坚持下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "当然了，我也会期待\x01",
            "你们的好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3976")

    ChrTalk(    #246
        0x103,
        "#020F嗯！我们一定会尽力而为。\x02",
    )

    CloseMessageWindow()

    label("loc_3976")

    OP_A2(0xE)
    OP_A2(0x20A2)
    Jump("loc_3B72")

    label("loc_397F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_39E5")

    ChrTalk(    #247
        0xFE,
        (
            "店里的情况虽然很头疼，\x01",
            "但也只能努力坚持下去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "当然了，我也会期待\x01",
            "你们的好消息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B72")

    label("loc_39E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_3AE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A90")

    ChrTalk(    #249
        0xFE,
        (
            "似乎庆祝会\x01",
            "顺利结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "虽然进货问题还是让人头疼，\x01",
            "但只要努力，\x01",
            "总会有解决的办法…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "嗯，只要保持现在的斗志，\x01",
            "一定可以坚持营业下去的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_3AE6")

    label("loc_3A90")


    ChrTalk(    #252
        0xFE,
        (
            "似乎庆祝会\x01",
            "顺利结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "嗯，只要保持现在的斗志，\x01",
            "一定可以坚持营业下去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE6")

    Jump("loc_3B72")

    label("loc_3AE9")


    ChrTalk(    #254
        0xFE,
        (
            "要是店附近能\x01",
            "有个农场就好了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "王都和柏斯的店\x01",
            "一定也都遇到大麻烦了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "虽然现在我已经无暇顾及别人了，\x01",
            "但实在无法不去关心…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B72")

    Jump("loc_4654")

    label("loc_3B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 7)), scpexpr(EXPR_END)), "loc_3C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_3C0A")

    ChrTalk(    #257
        0x8,
        (
            "很遗憾，\x01",
            "我不知道那道料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x8,
        (
            "在我开始学烹饪的时候，\x01",
            "就已经没人做那道菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x8,
        (
            "还是找更年长的人问问\x01",
            "可能比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C79")

    label("loc_3C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C35")
    Call(1, 4)
    Jump("loc_3C79")

    label("loc_3C35")


    ChrTalk(    #260
        0xFE,
        (
            "有空的话\x01",
            "就再来店里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "我和伊莉莎一起，\x01",
            "期待你们回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C79")

    Jump("loc_4182")

    label("loc_3C7C")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #262
        0xFE,
        (
            "啊……艾丝蒂尔，\x01",
            "还有雪拉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        (
            "#1001F您好，托露塔阿姨。\x02\x03",

            "#1025F太好了。\x01",
            "您终于醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x103,
        "#020F身体现在怎样了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #265
        0xFE,
        (
            "啊啊～还有点\x01",
            "恍惚吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "好像是做了个\x01",
            "奇怪的梦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#1026F啊，果然，\x01",
            "阿姨也做了梦吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #268
        0xFE,
        "嗯，很让人怀念的梦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "在梦中，我回到了艾丝蒂尔这么大的年龄，\x01",
            "和大家一起玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "主日学校时代的朋友……\x01",
            "汉娜和莱娜也都在一起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#1004F啊？莱娜……\x02\x03",

            "妈妈也出现了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "不只是你妈妈哦，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "连你和约修亚\x01",
            "也都在一起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "而且就是现在这种年龄。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        "#1020F咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x103,
        "#023F果然是有趣的梦啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #277
        0xFE,
        "嗯，很奇妙的情景吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "虽然在梦境中的\x01",
            "经历很快乐…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "但因为太过幸福，反而有些不真实，\x01",
            "让我一直隐隐感到不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "似乎一切都像是人造的幻境，\x01",
            "清醒之后越想越是毛骨悚然…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        "#1003F是、是这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #282
        0xFE,
        (
            "不过，再次看到了莱娜，\x01",
            "真的很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "也许是你妈妈借着这次的机会，\x01",
            "来到我的梦中和我相见吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "平常一直都在女神的身旁默默注视着我们，\x01",
            "这次终于忍耐不住了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#1025F啊哈哈……那也说不定吧……\x02\x03",

            "虽然还是不明白……\x01",
            "不过我也那么想啊。\x02\x03",

            "#1015F嗯，不过我究竟能否达到妈妈的期望呢，\x01",
            "说实话，还是很没自信呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "不用担心，你没问题的，\x01",
            "这一点我就可以确定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "所以，拿出自信来，\x01",
            "继续努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "你现在已经是个很厉害的游击士了，\x01",
            "无论各方面都很优秀呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        "#1006F嗯……谢谢！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5F)

    label("loc_4182")

    Jump("loc_4654")

    label("loc_4185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_44A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 5)), scpexpr(EXPR_END)), "loc_41FB")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #290
        0xFE,
        (
            "现在你们看起来很忙，\x01",
            "但以后有空的话一定再来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "艾丝蒂尔的话，\x01",
            "我可是随时欢迎的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A0")

    label("loc_41FB")

    ClearChrFlags(0xFE, 0x10)

    ChrTalk(    #292
        0xFE,
        (
            "……那么，我去\x01",
            "检查帐本了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #293
        0xFE,
        (
            "啊，艾丝蒂尔，\x01",
            "还有雪拉也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "真是好久不见了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        "#1000F托露塔阿姨，您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x103,
        "#020F呵呵，看起来很热闹啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #297
        0xFE,
        "嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "可以的话你们也来\x01",
            "吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "伊莉莎的新料理\x01",
            "最近大受好评了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        (
            "#1018F啊，那当然要尝尝！\x02\x03",

            "#1001F伊莉莎的料理\x01",
            "肯定很期待啊⊙\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #301
        0xFE,
        "呵呵，敬请期待吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "那孩子也一直\x01",
            "都很想见艾丝蒂尔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "在品尝料理的时候\x01",
            "顺便见上一面吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 2)), scpexpr(EXPR_END)), "loc_4450")

    ChrTalk(    #304
        0x101,
        (
            "#1017F呵呵，其实\x01",
            "我们都已经见过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "啊，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "今后也要再\x01",
            "来啊!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "艾丝蒂尔的话，\x01",
            "随时欢迎啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_449D")

    label("loc_4450")


    ChrTalk(    #308
        0x101,
        "#1017F嗯，一定！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "今后也要再\x01",
            "来啊!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "艾丝蒂尔的话，\x01",
            "随时欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449D")

    OP_A2(0x1895)

    label("loc_44A0")

    Jump("loc_4654")

    label("loc_44A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_4654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_44F3")

    ChrTalk(    #311
        0xFE,
        "我们一家一直都很健康呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "有时间的话，\x01",
            "随时过来玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4654")

    label("loc_44F3")


    ChrTalk(    #313
        0xFE,
        (
            "嗯，受政变的影响，\x01",
            "食材价格飞涨。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 300)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #314
        0xFE,
        "……艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        "好久不见了啊！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        "#008F嘿嘿嘿，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "真是让我吃了一惊！\x01",
            "你什么时候回洛连特的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x101,
        (
            "#000F啊，刚刚下\x01",
            "飞船没多久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "哎呀……\x01",
            "伊莉莎看见你也会高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "以后一定多来\x01",
            "店里玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#001F嗯，您不说\x01",
            "我也会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        "嗯……呵呵呵。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x104A)

    label("loc_4654")

    TalkEnd(0x8)
    Return()

    # Function_7_35B9 end

    def Function_8_4658(): pass

    label("Function_8_4658")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4827")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                  # 0
            "买东西\x01",                                # 1
            "招牌菜『三蛋黄杂烩粥』　1600米拉\x01",      # 2
            "离开\x01",                                  # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F3")
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46E8")
    OP_A9(0x9)
    Jump("loc_46EA")

    label("loc_46E8")

    OP_A9(0x4)

    label("loc_46EA")

    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_46F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4804")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_47CC")
    SubMira(1600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #323
        "\x06\x07\x02三蛋黄杂烩粥\x07\x00已经品尝过了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_4792")
    Jump("loc_47BE")

    label("loc_4792")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #324
        "\x06\x07\x02三蛋黄杂烩粥\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_47BE")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_47F2")

    label("loc_47CC")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #325
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_47F2")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xC)
    Return()

    label("loc_4804")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_481E")
    FadeToBright(300, 0)
    TalkEnd(0xC)
    Return()

    label("loc_481E")

    FadeToBright(300, 0)

    label("loc_4827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_489E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4884")

    ChrTalk(    #326
        0xC,
        "呼，还有宴会要办。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xC,
        (
            "好了，一鼓作气干完吧。\x01",
            "我也要去忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xFE, 0x10)
    OP_A2(0x0)
    Jump("loc_489B")

    label("loc_4884")


    ChrTalk(    #328
        0xC,
        (
            "失陪～\x01",
            "请自便吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_489B")

    Jump("loc_571A")

    label("loc_489E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_4A26")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4988")

    ChrTalk(    #329
        0xC,
        (
            "啊……\x01",
            "雪、雪拉扎德！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xC,
        (
            "难、难道说……\x01",
            "工作已经结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x103,
        (
            "#020F嗯，虽然暂时解决了……\x02\x03",

            "……但遗憾的是接下来\x01",
            "还有不少事情要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xC,
        "啊……是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xC,
        (
            "那、那个……\x01",
            "我会继续等的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_49C6")

    label("loc_4988")


    ChrTalk(    #334
        0xC,
        (
            "那、那个……\x01",
            "我会继续等的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xC,
        (
            "有时间的时候\x01",
            "要再来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C6")

    Jump("loc_4A23")

    label("loc_49C9")


    ChrTalk(    #336
        0xC,
        (
            "终于准备完庆祝会了，\x01",
            "暂时可以休息一下啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xC,
        (
            "呼～其实我这个服务生\x01",
            "接下来才要忙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A23")

    Jump("loc_571A")

    label("loc_4A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4BDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B22")
    TurnDirection(0xC, 0x103, 0)

    ChrTalk(    #338
        0xC,
        (
            "啊……\x01",
            "雪、雪拉扎德！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xC,
        (
            "哦，\x01",
            "在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x103,
        "#025F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xC,
        "嗯……太、太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x103,
        "#027F什么啊，怎么那种反应。\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #343
        0xC,
        "啊……没、没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xC,
        (
            "那、那个……\x01",
            "我会继续等的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4B57")

    label("loc_4B22")


    ChrTalk(    #345
        0xC,
        (
            "那、那个……\x01",
            "我会继续等的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xC,
        "工作要加油啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4B57")

    Jump("loc_4BD7")

    label("loc_4B5A")


    ChrTalk(    #347
        0xC,
        (
            "今天下午\x01",
            "有团体预约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xC,
        (
            "好像是结婚仪式的庆祝会，\x01",
            "所以有的忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xC,
        (
            "导力式的烹饪器具都没法用，\x01",
            "所以比平时还要累的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD7")

    Jump("loc_571A")

    label("loc_4BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4ED0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4C46")

    ChrTalk(    #350
        0xC,
        (
            "那个布露姆老奶奶\x01",
            "就像天使一样和善呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xC,
        (
            "嗯……\x01",
            "有点难以想象啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CFF")

    label("loc_4C46")


    ChrTalk(    #352
        0xC,
        (
            "刚才的传统料理…\x01",
            "还真是美味啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xC,
        (
            "不过，拉欧爷爷\x01",
            "的印象还真是强烈啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xC,
        (
            "竟然会对料理的味道\x01",
            "那么执着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xC,
        (
            "那个布露姆老奶奶\x01",
            "就像天使一样和善呢…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xC,
        (
            "嗯……\x01",
            "有点难以想象啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CFF")

    Jump("loc_4ECD")

    label("loc_4D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4D5C")

    ChrTalk(    #357
        0xC,
        (
            "今、今天所幸\x01",
            "没有出现大事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xC,
        (
            "这样暂时就\x01",
            "可以松口气了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E10")

    label("loc_4D5C")


    ChrTalk(    #359
        0xC,
        "哈，太好了…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        (
            "今、今天所幸\x01",
            "没有出现大事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xC,
        (
            "不过，特地邀请爱娜小姐\x01",
            "来喝酒…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DED")

    ChrTalk(    #362
        0xC,
        "奥利维尔先生…难道不想活了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E10")

    label("loc_4DED")


    ChrTalk(    #363
        0xC,
        (
            "看来奥利维尔先生\x01",
            "是想自杀呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E10")

    Jump("loc_4ECD")

    label("loc_4E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4E63")

    ChrTalk(    #364
        0xC,
        (
            "雾散去了，\x01",
            "定期船也恢复航行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xC,
        (
            "滞留的客人们\x01",
            "都去飞船坪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ECD")

    label("loc_4E63")


    ChrTalk(    #366
        0xC,
        (
            "太太她也终于\x01",
            "清醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xC,
        (
            "阴影已经散去，\x01",
            "好像一切都恢复原状了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xC,
        (
            "我也要调整心情\x01",
            "好好工作了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4ECD")

    Jump("loc_571A")

    label("loc_4ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F27")

    ChrTalk(    #369
        0xC,
        (
            "矿工们回来以后\x01",
            "又要开始忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xC,
        (
            "啊啊，老板！\x01",
            "快点回厨房吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FD2")

    label("loc_4F27")


    ChrTalk(    #371
        0xC,
        (
            "矿工们回来以后\x01",
            "又要开始忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xC,
        (
            "全都是力气活，\x01",
            "但为了让大家吃上东西也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xC,
        (
            "早上终于过去了，\x01",
            "本以为可以休息一下了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xC,
        (
            "啊啊，老板！\x01",
            "快点回厨房吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4FD2")

    Jump("loc_571A")

    label("loc_4FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_511C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5056")

    ChrTalk(    #375
        0xC,
        "今天早上的客人还是很少…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xC,
        (
            "不过定期船上的\x01",
            "人好像要来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xC,
        (
            "大家都被禁止出行了，\x01",
            "也没有别的地方可去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5119")

    label("loc_5056")


    ChrTalk(    #378
        0xC,
        "今天早上的客人还是很少…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xC,
        (
            "不过定期船上的\x01",
            "人好像要来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xC,
        (
            "大家都被禁止出行了，\x01",
            "也没有别的地方可去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xC,
        (
            "这样的话，正是轮到\x01",
            "酒馆起作用的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xC,
        (
            "美味的酒菜也\x01",
            "可以让人解忧呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5119")

    Jump("loc_571A")

    label("loc_511C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_5599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 6)), scpexpr(EXPR_END)), "loc_543D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5201")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5198")

    ChrTalk(    #383
        0xC,
        (
            "雪、雪拉。\x01",
            "工作要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xC,
        (
            "那个，今天这么大雾，\x01",
            "要喝酒的话还是改日吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51FE")

    label("loc_5198")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51FE")

    ChrTalk(    #385
        0xC,
        (
            "雪拉小姐和爱娜小姐\x01",
            "两个人一起喝酒…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xC,
        (
            "那种情景实在太恐怖，\x01",
            "没经历过的人很难体会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51FE")

    Jump("loc_53F6")

    label("loc_5201")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A5")

    ChrTalk(    #387
        0xC,
        "雪、雪拉扎德！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xC,
        "难、难道已经喝了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x103,
        (
            "#020F我也想那样……\x01",
            "但很遗憾，现在在工作中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xC,
        "哈、哈哈……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xC,
        "（哈～……太好了～）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_53F6")

    label("loc_52A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537D")

    ChrTalk(    #392
        0xC,
        "啊，那个……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xC,
        (
            "那件白色外套……\x01",
            "你难道是那时的？！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x104,
        "#031F呵，肯定要多关照关照啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xC,
        (
            "身为同甘共苦过的人，\x01",
            "一定会更有默契吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0xC,
        (
            "那种恐怖的事情都经历过，\x01",
            "接下来一定更要顽强活下去。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_53F6")

    label("loc_537D")


    ChrTalk(    #397
        0xC,
        (
            "要是只有雪拉的话\x01",
            "还能勉强撑一下…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0xC,
        (
            "但要再加上爱娜的话\x01",
            "就和送死没区别了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0xC,
        (
            "啊啊…\x01",
            "至少要２、３天起不来床了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53F6")

    Jump("loc_543A")

    label("loc_53F9")


    ChrTalk(    #400
        0xC,
        (
            "雪、雪拉要带\x01",
            "爱娜来喝酒的话…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xC,
        "……要关门２、３天了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_543A")

    Jump("loc_5596")

    label("loc_543D")


    ChrTalk(    #402
        0x103,
        "#526F啊，福克纳。\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xC, 0x103, 400)
    Sleep(400)

    ChrTalk(    #403
        0xC,
        "雪、雪拉扎德！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xC,
        "什、什么时候回来的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x103,
        (
            "#027F呵呵，你看起来\x01",
            "很想见我啊。\x02\x03",

            "#525F那到时我带爱娜一起来喝酒，\x01",
            "就请多关照了㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #406
        0xC,
        "哈、哈哈……我等你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        (
            "#1016F（还、还是\x01",
            "   那么恐怖啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5590")

    ChrTalk(    #408
        0x104,
        (
            "#034F福克纳兄。\x01",
            "……我了解你的心情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5590")

    OP_A2(0x1896)
    OP_A2(0x1)

    label("loc_5596")

    Jump("loc_571A")

    label("loc_5599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_571A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_561A")

    ChrTalk(    #409
        0xC,
        (
            "那天毫不犹豫地就赶紧下班了，\x01",
            "所以后面的事情就不知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0xC,
        (
            "啊啊，究竟发生什么事呢，\x01",
            "光是想想就很可怕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_571A")

    label("loc_561A")


    ChrTalk(    #411
        0xC,
        (
            "之前雪拉扎德带\x01",
            "来过一个金发的男子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xC,
        "一个穿着白色外套的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xC,
        (
            "在喝酒前就一直说些醉话，\x01",
            "真是个奇怪的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xC,
        (
            "然后游击士协会的爱娜\x01",
            "也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0xC,
        (
            "那个男子好像什么都不知道，\x01",
            "很欢迎她的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xC,
        (
            "但在我看来，他简直就像是冲向野狼\x01",
            "的可怜小羊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_571A")

    TalkEnd(0xC)
    Return()

    # Function_8_4658 end

    def Function_9_571E(): pass

    label("Function_9_571E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_587B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_57BB")

    ChrTalk(    #417
        0xFE,
        (
            "哈，我今天实在\x01",
            "是没食欲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        (
            "可是，什么都不吃的话\x01",
            "对身体不好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "没办法……\x01",
            "稍微吃一点吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "咔咔咔咔\x01",
            "呱呱呱呱呱…\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    Jump("loc_5878")

    label("loc_57BB")


    ChrTalk(    #421
        0xFE,
        (
            "呼呼呼呼呼…\x01",
            "咯咯咯咯咯…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "喔喔喔喔喔…\x01",
            "…………嗝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        (
            "啊，回城的途中，\x01",
            "遭到雾妖的袭击了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        (
            "游击士们虽然\x01",
            "帮我打退了它们，\x01",
            "不过还是好可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "我今天实在\x01",
            "是没食欲啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5878")

    Jump("loc_5A10")

    label("loc_587B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_596B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_58B9")

    ChrTalk(    #426
        0xFE,
        (
            "咔咔咔咔\x01",
            "呱呱呱呱呱…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        "…………嗝。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5968")

    label("loc_58B9")


    ChrTalk(    #428
        0xFE,
        "呼呼呼呼呼…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0xFE,
        "咯咯咯咯咯…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0xFE,
        "喔喔喔喔喔…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        "…………嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        "呀，外边的雾还很浓啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0xFE,
        (
            "要去矿山吗？\x01",
            "总有些不安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xFE,
        (
            "不管怎么样，\x01",
            "还是快点吃完出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5968")

    Jump("loc_5A10")

    label("loc_596B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_5A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_59A0")

    ChrTalk(    #435
        0xFE,
        "呼呼呼呼呼…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xFE,
        "咯咯咯咯咯…\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A10")

    label("loc_59A0")


    ChrTalk(    #437
        0xFE,
        "呼呼呼呼呼…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xFE,
        "咯咯咯咯咯…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        "喔喔喔喔喔…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0xFE,
        "…………嗝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xFE,
        (
            "呼，今天老大休息，\x01",
            "总算安心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_5A10")

    TalkEnd(0xD)
    Return()

    # Function_9_571E end

    def Function_10_5A14(): pass

    label("Function_10_5A14")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_5B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5A7E")

    ChrTalk(    #442
        0xFE,
        (
            "雾中现身的魔兽…\x01",
            "想想就让人直流冷汗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xFE,
        (
            "虽然肚子很饿，\x01",
            "但是实在提不起食欲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B5A")

    label("loc_5A7E")


    ChrTalk(    #444
        0xFE,
        (
            "今天多亏有游击士护送，\x01",
            "才能从矿山回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0xFE,
        (
            "途中遭到了从来没见过\x01",
            "的魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "它们的样子就像一团烟雾…\x01",
            "想想就让人直流冷汗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xFE,
        (
            "虽然肚子很饿，\x01",
            "但是实在提不起食欲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "这种时候，好羡慕\x01",
            "提恩特那小子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_5B5A")

    TalkEnd(0xE)
    Return()

    # Function_10_5A14 end

    def Function_11_5B5E(): pass

    label("Function_11_5B5E")

    TalkBegin(0xF)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B83")
    SetChrSubChip(0xFE, 2)
    Jump("loc_5B9E")

    label("loc_5B83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B99")
    SetChrSubChip(0xFE, 2)
    Jump("loc_5B9E")

    label("loc_5B99")

    SetChrSubChip(0xFE, 1)

    label("loc_5B9E")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_5C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5BF9")

    ChrTalk(    #449
        0xFE,
        (
            "乘务员他们\x01",
            "一天基本都待在船上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "除了吃饭就是\x01",
            "休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C71")

    label("loc_5BF9")


    ChrTalk(    #451
        0xFE,
        "哟，早啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xFE,
        (
            "乘务员他们\x01",
            "一天基本都待在船上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        (
            "除了吃饭就是\x01",
            "休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0xFE,
        (
            "……可不是只有\x01",
            "船长我才来酒馆啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_5C71")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xF)
    Return()

    # Function_11_5B5E end

    def Function_12_5C7A(): pass

    label("Function_12_5C7A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_5D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5CE4")

    ChrTalk(    #455
        0xFE,
        (
            "呼，看来这雾\x01",
            "短时间内不会散去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xFE,
        (
            "我要是也和库因特那家伙\x01",
            "一起去祈祷就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D34")

    label("loc_5CE4")


    ChrTalk(    #457
        0xFE,
        (
            "飞不起来的飞船，\x01",
            "简直一点用处也没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xFE,
        "呼，真想早日重新飞到空中。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5D34")

    TalkEnd(0x10)
    Return()

    # Function_12_5C7A end

    def Function_13_5D38(): pass

    label("Function_13_5D38")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5D9D")

    ChrTalk(    #459
        0xFE,
        (
            "今天真是谢谢了，\x01",
            "让你们费心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        (
            "全靠你们，我才能再次\x01",
            "尝到怀念的味道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E69")

    label("loc_5D9D")


    ChrTalk(    #461
        0xFE,
        (
            "今天真是谢谢了，\x01",
            "让你们费心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xFE,
        (
            "全靠你们，我才能再次\x01",
            "尝到怀念的味道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0xFE,
        (
            "嗯，布露姆老奶奶\x01",
            "的烹饪水平真是一流啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "不愧是从小就学习\x01",
            "烹饪的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "只有经过岁月的累积\x01",
            "才能达到这种水平啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_5E69")

    Jump("loc_60EF")

    label("loc_5E6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_5F14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_5F0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_5EC2")

    ChrTalk(    #466
        0xFE,
        "调查的事情就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "期待你们发现\x01",
            "新的线索。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F0A")

    label("loc_5EC2")


    ChrTalk(    #468
        0xFE,
        (
            "喔喔，是你们吗？\x01",
            "调查怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xFE,
        (
            "期待你们发现\x01",
            "那怀念的食谱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F0A")

    Jump("loc_5F11")

    label("loc_5F0D")

    Call(1, 3)

    label("loc_5F11")

    Jump("loc_60EF")

    label("loc_5F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_6099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_5F9E")

    ChrTalk(    #470
        0xFE,
        (
            "已经很久没有\x01",
            "做过年轻时的梦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        (
            "所以才想起了\x01",
            "怀念的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0xFE,
        (
            "虽然给厨师添了不少麻烦，\x01",
            "不过总算是如愿以偿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6096")

    label("loc_5F9E")


    ChrTalk(    #473
        0xFE,
        (
            "呀，昨天梦见了很久没梦到过的\x01",
            "年轻时代。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0xFE,
        (
            "梦的内容很奇怪，\x01",
            "是和当时的恋人一起\x01",
            "拼命制作料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "醒来之后，就非常\x01",
            "想要吃那料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0xFE,
        (
            "所以就跑到酒馆\x01",
            "来找寻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        (
            "不过那是很久以前的菜式，\x01",
            "厨师实在是找不到了。\x01",
            "嗯，不过总算是如愿以偿了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_6096")

    Jump("loc_60EF")

    label("loc_6099")


    ChrTalk(    #478
        0xFE,
        (
            "终于天晴了，\x01",
            "但为何会突然出现浓雾呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xFE,
        (
            "这简直是故事中出现过的\x01",
            "妖精恶作剧啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EF")

    TalkEnd(0x11)
    Return()

    # Function_13_5D38 end

    def Function_14_60F3(): pass

    label("Function_14_60F3")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6190")

    ChrTalk(    #480
        0xFE,
        "呀，游击士们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0xFE,
        (
            "来了啊。\x01",
            "快来参加庆祝会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xFE,
        (
            "最近虽然有很多事情让人不安，\x01",
            "但也让人很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0xFE,
        (
            "毕竟是很难得\x01",
            "的经历啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61C4")

    label("loc_6190")


    ChrTalk(    #484
        0xFE,
        (
            "今天真是\x01",
            "谢谢了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0xFE,
        (
            "机会难得，\x01",
            "一定要去啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61C4")

    OP_A2(0xA)
    Jump("loc_6210")

    label("loc_61CA")


    ChrTalk(    #486
        0xFE,
        (
            "难得的机会，\x01",
            "今天一定要好好享受啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        (
            "毕竟是很难得\x01",
            "的经历啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6210")

    TalkEnd(0x14)
    Return()

    # Function_14_60F3 end

    def Function_15_6214(): pass

    label("Function_15_6214")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_626E")

    ChrTalk(    #488
        0xFE,
        (
            "啊，游击士。\x01",
            "今天谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0xFE,
        (
            "约定了哦。\x01",
            "我们一定会幸福的，\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62A7")

    label("loc_626E")


    ChrTalk(    #490
        0xFE,
        "谢谢你们来捧场。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0xFE,
        (
            "约定了哦。\x01",
            "我们一定会幸福的，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62A7")

    OP_A2(0xB)
    Jump("loc_62CE")

    label("loc_62AD")


    ChrTalk(    #492
        0xFE,
        (
            "谢谢你们来捧场。\x01",
            "请随意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62CE")

    TalkEnd(0x15)
    Return()

    # Function_15_6214 end

    def Function_16_62D2(): pass

    label("Function_16_62D2")

    TalkBegin(0x16)

    ChrTalk(    #493
        0xFE,
        (
            "真是完美的\x01",
            "结婚仪式啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        (
            "为了祝福年轻的夫妇，\x01",
            "今天一定要多喝几杯。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_16_62D2 end

    def Function_17_6325(): pass

    label("Function_17_6325")

    TalkBegin(0x17)

    ChrTalk(    #495
        0xFE,
        (
            "阿鲁姆哥哥在结婚仪式上\x01",
            "真是好帅啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xFE,
        (
            "第一次感觉到哥哥\x01",
            "是个优秀的男人。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_17_6325 end

    def Function_18_637C(): pass

    label("Function_18_637C")

    TalkBegin(0x18)

    ChrTalk(    #497
        0xFE,
        (
            "嗯，果然是家不错的店呢。\x01",
            "料理非常美味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        (
            "所以很早就\x01",
            "跑来了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x18)
    Return()

    # Function_18_637C end

    def Function_19_63C9(): pass

    label("Function_19_63C9")

    TalkBegin(0x19)

    ChrTalk(    #499
        0xFE,
        (
            "新娘的结婚礼服\x01",
            "很漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0xFE,
        (
            "呼，真想让那孩子的父亲\x01",
            "也看看…\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_19_63C9 end

    def Function_20_6414(): pass

    label("Function_20_6414")

    TalkBegin(0x1A)

    ChrTalk(    #501
        0xFE,
        (
            "仪式顺利结束了，\x01",
            "总算可以稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xFE,
        (
            "希望那孩子的父亲在\x01",
            "天国也能看见。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_20_6414 end

    def Function_21_646F(): pass

    label("Function_21_646F")

    TalkBegin(0x1B)

    ChrTalk(    #503
        0xFE,
        (
            "姐姐的礼服\x01",
            "真是太漂亮了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0xFE,
        (
            "我也想早点\x01",
            "当新娘啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_21_646F end

    def Function_22_64B0(): pass

    label("Function_22_64B0")

    TalkBegin(0x1C)

    ChrTalk(    #505
        0xFE,
        (
            "今天的艾娅莉\x01",
            "真的很漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        (
            "穿上礼服之后\x01",
            "简直像变了个人。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1C)
    Return()

    # Function_22_64B0 end

    def Function_23_64FB(): pass

    label("Function_23_64FB")

    TalkBegin(0x1D)

    ChrTalk(    #507
        0xFE,
        (
            "艾娅莉和阿鲁姆\x01",
            "好像很幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        (
            "真羡慕他们…\x01",
            "要开始认真寻找目标了吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1D)
    Return()

    # Function_23_64FB end

    def Function_24_6550(): pass

    label("Function_24_6550")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 7)), scpexpr(EXPR_END)), "loc_65A2")

    ChrTalk(    #509
        0xFE,
        "呼～今天的酒真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0xFE,
        (
            "帮了这么多忙，\x01",
            "总有权利出席庆祝会吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6657")

    label("loc_65A2")


    ChrTalk(    #511
        0xFE,
        "呼～今天的酒真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0xFE,
        (
            "因为心情很好，\x01",
            "就把这书送你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #513
        "\x07\x00得到了\x1F\x44\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x244, 1)
    OP_A2(0x10BF)
    OP_0D()

    ChrTalk(    #514
        0xFE,
        (
            "呼～真是好酒。\x01",
            "光是想想就很舒服了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6657")

    TalkEnd(0x1E)
    Return()

    # Function_24_6550 end

    def Function_25_665B(): pass

    label("Function_25_665B")

    EventBegin(0x0)
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

    def lambda_6709():
        OP_6D(87450, 0, 79790, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6709)
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
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0111   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_25_665B end

    def Function_26_67A2(): pass

    label("Function_26_67A2")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x19)
    Return()

    # Function_26_67A2 end

    SaveToFile()

Try(main)
