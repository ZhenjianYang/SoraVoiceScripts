from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '士兵',                                 # 9
        '士兵',                                 # 10
        '爱娜',                                 # 11
        '佛莱迪',                               # 12
        '梅尔达斯',                             # 13
        '里农',                                 # 14
        '鲁克',                                 # 15
        '帕特',                                 # 16
        '克露莎',                               # 17
        '胡里奥',                               # 18
        '艾娅莉',                               # 19
        '阿鲁姆',                               # 20
        '提克',                                 # 21
        '莫莉',                                 # 22
        '利吉',                                 # 23
        '商人',                                 # 24
        '旅行者',                               # 25
        '旅行者',                               # 26
        '鸽子',                                 # 27
        '鸽子',                                 # 28
        '鸽子',                                 # 29
        '鸽子',                                 # 30
        '鸽子',                                 # 31
        '士兵斯科特',                           # 32
        '士兵哈罗德',                           # 33
        '士兵拉科斯',                           # 34
        '士兵霍帕',                             # 35
        '士兵安托斯',                           # 36
        '士兵多明戈',                           # 37
        '士兵迈尔斯',                           # 38
        '士兵马克斯',                           # 39
        '戴恩副队长',                           # 40
        '阿斯顿队长',                           # 41
        '基蒂',                                 # 42
        '安敦',                                 # 43
        '利库斯',                               # 44
        '迪拜恩教区长',                         # 45
        '修女梅',                               # 46
        '伴娘',                                 # 47
        '布露姆老奶奶',                         # 48
        '亚尔丽 ',                              # 49
        '赛拉',                                 # 50
        '托露塔',                               # 51
        '伊娜',                                 # 52
        '安莉尔',                               # 53
        '年轻的女性',                           # 54
        '临时演员',                             # 55
        '年轻的女性',                           # 56
        '临时演员',                             # 57
        '临时演员',                             # 58
        '新郎的亲属',                           # 59
        '新郎的亲属',                           # 60
        '新郎的亲属',                           # 61
        '新娘的亲属',                           # 62
        '新娘的亲属',                           # 63
        '新娘的亲属',                           # 64
        '新娘的朋友',                           # 65
        '新娘的朋友',                           # 66
        '捧花',                                 # 67
        '小猫',                                 # 68
        '小猫',                                 # 69
        '小猫',                                 # 70
        '菲特 ',                                # 71
        '林德号的乘客',                         # 72
        '林德号的乘客',                         # 73
        '洛连特·市长官邸',                     # 74
        '洛连特飞船坪',                         # 75
        '艾利兹街道方向',                       # 76
        '米尔西街道方向',                       # 77
        '玛鲁加山道方向',                       # 78
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 19,
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
        TalkScenaIndex      = 18,
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
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 20,
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
        TalkScenaIndex      = 21,
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
        TalkScenaIndex      = 22,
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
        TalkScenaIndex      = 23,
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
        TalkScenaIndex      = 24,
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
        TalkScenaIndex      = 25,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkScenaIndex      = 29,
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
        TalkScenaIndex      = 30,
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
        TalkScenaIndex      = 31,
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
        TalkScenaIndex      = 32,
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
        TalkScenaIndex      = 33,
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
        TalkScenaIndex      = 34,
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
        TalkScenaIndex      = 35,
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
        TalkScenaIndex      = 36,
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
        TalkScenaIndex      = 27,
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
        TalkScenaIndex      = 26,
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
        TalkScenaIndex      = 37,
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
        TalkScenaIndex      = 40,
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
        TalkScenaIndex      = 41,
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
        TalkScenaIndex      = 38,
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
        TalkScenaIndex      = 39,
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
        TalkScenaIndex      = 73,
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
        TalkScenaIndex      = 74,
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
        TalkScenaIndex      = 75,
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
        Unknown_1C          = 81,
    )

    DeclEvent(
        X                   = 18000,
        Y                   = 0,
        Z                   = 44000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x9088,
        Unknown_18          = 0x0,
        Unknown_1C          = 80,
    )

    DeclEvent(
        X                   = 26300,
        Y                   = 0,
        Z                   = 72000,
        Range               = 29700,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x1142C,
        Unknown_18          = 0x0,
        Unknown_1C          = 79,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 18950,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )

    DeclEvent(
        X                   = 52800,
        Y                   = 0,
        Z                   = 29050,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 88,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 33020,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 89,
    )

    DeclEvent(
        X                   = 44700,
        Y                   = 0,
        Z                   = 21990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 90,
    )

    DeclEvent(
        X                   = 30900,
        Y                   = 0,
        Z                   = 47270,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 91,
    )

    DeclEvent(
        X                   = 34300,
        Y                   = 0,
        Z                   = 52980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 91,
    )

    DeclEvent(
        X                   = 66000,
        Y                   = 0,
        Z                   = 52470,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 92,
    )

    DeclEvent(
        X                   = 73000,
        Y                   = 0,
        Z                   = 34550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 93,
    )

    DeclEvent(
        X                   = 54800,
        Y                   = 0,
        Z                   = 49170,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 94,
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
        TalkFunctionIndex   = 82,
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
        TalkFunctionIndex   = 83,
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
        TalkFunctionIndex   = 84,
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
        "Function_7_176F",         # 07, 7
        "Function_8_18B0",         # 08, 8
        "Function_9_19B5",         # 09, 9
        "Function_10_1A10",        # 0A, 10
        "Function_11_1BC4",        # 0B, 11
        "Function_12_1C30",        # 0C, 12
        "Function_13_1C49",        # 0D, 13
        "Function_14_25DC",        # 0E, 14
        "Function_15_295D",        # 0F, 15
        "Function_16_2F54",        # 10, 16
        "Function_17_304A",        # 11, 17
        "Function_18_30A6",        # 12, 18
        "Function_19_3743",        # 13, 19
        "Function_20_4709",        # 14, 20
        "Function_21_4832",        # 15, 21
        "Function_22_4951",        # 16, 22
        "Function_23_4C75",        # 17, 23
        "Function_24_4CE7",        # 18, 24
        "Function_25_4D51",        # 19, 25
        "Function_26_4DA1",        # 1A, 26
        "Function_27_4F1C",        # 1B, 27
        "Function_28_4F7F",        # 1C, 28
        "Function_29_5103",        # 1D, 29
        "Function_30_5221",        # 1E, 30
        "Function_31_5402",        # 1F, 31
        "Function_32_55F7",        # 20, 32
        "Function_33_56EC",        # 21, 33
        "Function_34_58AB",        # 22, 34
        "Function_35_5A22",        # 23, 35
        "Function_36_5B55",        # 24, 36
        "Function_37_5C38",        # 25, 37
        "Function_38_5CCC",        # 26, 38
        "Function_39_62D7",        # 27, 39
        "Function_40_632D",        # 28, 40
        "Function_41_6463",        # 29, 41
        "Function_42_6640",        # 2A, 42
        "Function_43_70EA",        # 2B, 43
        "Function_44_7124",        # 2C, 44
        "Function_45_7154",        # 2D, 45
        "Function_46_7184",        # 2E, 46
        "Function_47_71DE",        # 2F, 47
        "Function_48_7356",        # 30, 48
        "Function_49_74B3",        # 31, 49
        "Function_50_7624",        # 32, 50
        "Function_51_7A0D",        # 33, 51
        "Function_52_7D2E",        # 34, 52
        "Function_53_7D7C",        # 35, 53
        "Function_54_7ECC",        # 36, 54
        "Function_55_7F3E",        # 37, 55
        "Function_56_7FB5",        # 38, 56
        "Function_57_8044",        # 39, 57
        "Function_58_80D8",        # 3A, 58
        "Function_59_8158",        # 3B, 59
        "Function_60_81DB",        # 3C, 60
        "Function_61_A14E",        # 3D, 61
        "Function_62_A190",        # 3E, 62
        "Function_63_A1D2",        # 3F, 63
        "Function_64_A207",        # 40, 64
        "Function_65_A23C",        # 41, 65
        "Function_66_A281",        # 42, 66
        "Function_67_A2C6",        # 43, 67
        "Function_68_A30B",        # 44, 68
        "Function_69_A32C",        # 45, 69
        "Function_70_A365",        # 46, 70
        "Function_71_A37B",        # 47, 71
        "Function_72_A3BD",        # 48, 72
        "Function_73_A86E",        # 49, 73
        "Function_74_AB29",        # 4A, 74
        "Function_75_AC0E",        # 4B, 75
        "Function_76_ACC1",        # 4C, 76
        "Function_77_AD5D",        # 4D, 77
        "Function_78_ADAF",        # 4E, 78
        "Function_79_AE08",        # 4F, 79
        "Function_80_B06A",        # 50, 80
        "Function_81_B225",        # 51, 81
        "Function_82_B2C8",        # 52, 82
        "Function_83_B3CC",        # 53, 83
        "Function_84_B415",        # 54, 84
        "Function_85_B458",        # 55, 85
        "Function_86_B47C",        # 56, 86
        "Function_87_B504",        # 57, 87
        "Function_88_B508",        # 58, 88
        "Function_89_B50C",        # 59, 89
        "Function_90_B510",        # 5A, 90
        "Function_91_B514",        # 5B, 91
        "Function_92_B518",        # 5C, 92
        "Function_93_B51C",        # 5D, 93
        "Function_94_B520",        # 5E, 94
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
    Event(0, 42)
    Jump("loc_10C3")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_102C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 51)
    Jump("loc_10C3")

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1042")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 53)
    Jump("loc_10C3")

    label("loc_1042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_1061")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 60)
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
    Event(0, 47)
    Jump("loc_10B1")

    label("loc_1099")

    SetMapFlags(0x10000000)
    Event(0, 48)
    Jump("loc_10B1")

    label("loc_10A5")

    SetMapFlags(0x10000000)
    Event(0, 49)
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_176E")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1737")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15E7")

    def lambda_15CB():

        label("loc_15CB")

        OP_97(0xFE, 0xD6D8, 0xB824, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_15CB")

    QueueWorkItem2(0xFE, 1, lambda_15CB)
    Jump("loc_1606")

    label("loc_15E7")


    def lambda_15ED():

        label("loc_15ED")

        OP_97(0xFE, 0xD6D8, 0xB824, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_15ED")

    QueueWorkItem2(0xFE, 1, lambda_15ED)

    label("loc_1606")

    SetChrChipByIndex(0xFE, 11)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_1615")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_164D")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1645")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_164D")

    label("loc_1645")

    Sleep(15)
    Jump("loc_1615")

    label("loc_164D")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 55000, 0, 47140, 74)

    label("loc_166C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1734")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x25, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_172C")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 12)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 51380, 38050, 58760, 43900, 0)
    Jump("loc_1734")

    label("loc_172C")

    Sleep(500)
    Jump("loc_166C")

    label("loc_1734")

    Jump("loc_176B")

    label("loc_1737")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176B")

    def lambda_1753():
        OP_8D(0xFE, 51380, 38050, 58760, 43900, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1753)

    label("loc_176B")

    Jump("loc_14DF")

    label("loc_176E")

    Return()

    # Function_6_14AB end

    def Function_7_176F(): pass

    label("Function_7_176F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18AF")
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
    Jump("Function_7_176F")

    label("loc_18AF")

    Return()

    # Function_7_176F end

    def Function_8_18B0(): pass

    label("Function_8_18B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B4")
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
    Jump("Function_8_18B0")

    label("loc_19B4")

    Return()

    # Function_8_18B0 end

    def Function_9_19B5(): pass

    label("Function_9_19B5")

    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A0F")
    OP_8D(0xFE, 43070, 48140, 44730, 52710, 3000)
    Jump("loc_19EC")

    label("loc_1A0F")

    Return()

    # Function_9_19B5 end

    def Function_10_1A10(): pass

    label("Function_10_1A10")

    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_1BAE")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A85")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_1BAE")

    label("loc_1A85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A9E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_1BAE")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB7")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_1BAE")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD0")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_1BAE")

    label("loc_1AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_1BAE")

    label("loc_1AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B02")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_1BAE")

    label("loc_1B02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_1BAE")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B34")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_1BAE")

    label("loc_1B34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_1BAE")

    label("loc_1B4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B66")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_1BAE")

    label("loc_1B66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B7F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_1BAE")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B98")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_1BAE")

    label("loc_1B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_1BAE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BC3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_1BAE")

    label("loc_1BC3")

    Return()

    # Function_10_1A10 end

    def Function_11_1BC4(): pass

    label("Function_11_1BC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C2F")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1C")
    Sleep(100)
    OP_4B(0xFE, 0)
    Jump("loc_1C27")

    label("loc_1C1C")

    OP_4A(0xFE, 0)
    TurnDirection(0xFE, 0xF, 400)

    label("loc_1C27")

    Sleep(100)
    Jump("Function_11_1BC4")

    label("loc_1C2F")

    Return()

    # Function_11_1BC4 end

    def Function_12_1C30(): pass

    label("Function_12_1C30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C48")
    TurnDirection(0xFE, 0xE, 0)
    Sleep(100)
    Jump("Function_12_1C30")

    label("loc_1C48")

    Return()

    # Function_12_1C30 end

    def Function_13_1C49(): pass

    label("Function_13_1C49")

    TalkBegin(0xE)
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C69")
    OP_A2(0x14)
    Call(0, 72)
    Jump("loc_1E6C")

    label("loc_1C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_1E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_1D0C")

    ChrTalk(    #0
        0xE,
        (
            "话说回来帕特的\x01",
            "妈妈还真是过分。\x02\x03",

            "刚才还硬把人家\x01",
            "带去教会。\x02\x03",

            "虽然是第一次出席婚礼，\x01",
            "感觉真是特别无聊。\x02\x03",

            "就算我长大了\x01",
            "也绝对不做那种事。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x16)
    OP_A2(0x15)
    Jump("loc_1E1B")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCD")

    ChrTalk(    #1
        0xE,
        (
            "真是的……\x01",
            "帕特的妈妈好过分哦！\x02\x03",

            "人家在这里玩，\x01",
            "却硬给她拉去教会……\x02\x03",

            "结果一直坐着，\x01",
            "还让人家老实点。\x02\x03",

            "唉，大人还真是的，\x01",
            "老是做那么无聊的事。\x02\x03",

            "我长大以后\x01",
            "绝对不要什么婚礼。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_1E1B")

    label("loc_1DCD")


    ChrTalk(    #2
        0xE,
        (
            "为什么连毫无关联的我们\x01",
            "也得去参加婚礼啊。\x02\x03",

            "真是的……\x01",
            "帕特的妈妈好过分。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1B")

    Jump("loc_1E6C")

    label("loc_1E1E")


    ChrTalk(    #3
        0xE,
        (
            "外面的街道很危险，\x01",
            "我们也明白啦。\x02\x03",

            "唉，虽然很可惜，\x01",
            "今天还是在城里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6C")

    Jump("loc_25D4")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_22F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 0)), scpexpr(EXPR_END)), "loc_1F16")
    TurnDirection(0xE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_1EC5")

    ChrTalk(    #4
        0xE,
        (
            "艾丝蒂尔！\x01",
            "这次是真正的决斗了！\x02\x03",

            "绝对不能忘了哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F13")

    label("loc_1EC5")


    ChrTalk(    #5
        0xE,
        (
            "我也要苦练剑术\x01",
            "当上游击士给你看！\x02\x03",

            "艾丝蒂尔这种程度\x01",
            "我马上就可以超越了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F13")

    Jump("loc_22F3")

    label("loc_1F16")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #6
        0xE,
        "啊，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1000F哟嗬～～鲁克！\x02\x03",

            "#1025F太好了……\x01",
            "看上去很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xE,
        (
            "嘿嘿，已经全好啦。\x02\x03",

            "不过，醒过来\x01",
            "还觉得有点遗憾呢。\x02\x03",

            "因为睡着的时候，\x01",
            "我一直做着超级棒的好梦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1015F嗯……好梦啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xE,
        (
            "嘿嘿，我成为游击士后\x01",
            "神勇威猛大活跃的梦喔！\x02\x03",

            "哼哼，简直是艾丝蒂尔\x01",
            "想都想不到的活跃啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1016F啊哈哈，你可真单纯啊～\x02\x03",

            "嗯，想要梦想成真\x01",
            "就要从现在开始努力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xE,
        (
            "哼，艾丝蒂尔这水平\x01",
            "我马上就可以超越了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_2298")

    ChrTalk(    #13
        0xE,
        (
            "对了对了，艾丝蒂尔。\x01",
            "关于决斗的约定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1007F啊～你还记着啊。\x02\x03",

            "约是约好了没错，\x01",
            "……真的要来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xE,
        (
            "不……\x01",
            "今天还是算了。\x02\x03",

            "这次的事也给\x01",
            "艾丝蒂尔添了不少麻烦……\x02\x03",

            "嗯，就特别放你一马吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1019F真是，嘴不饶人啊。\x02\x03",

            "#1006F……不过，我知道了。\x01",
            "以后有机会再决胜负吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xE,
        (
            "哦，你做好心理准备吧！\x02\x03",

            "鲁克大人华丽的剑术\x01",
            "会把你彻底打垮！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1006F哼哼，好好\x01",
            "努力修行吧。\x02\x03",

            "要不然，可是会被我揍得惨兮兮哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xE,
        "嘿嘿，你才是呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_22F0")

    label("loc_2298")


    ChrTalk(    #20
        0x101,
        (
            "#1006F哼哼，好好\x01",
            "努力修行吧。\x02\x03",

            "游击士的道路\x01",
            "可没那么简单哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xE,
        "嘿嘿，等着瞧吧！\x02",
    )

    CloseMessageWindow()

    label("loc_22F0")

    OP_A2(0x1A68)

    label("loc_22F3")

    Jump("loc_25D4")

    label("loc_22F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_234C")
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(    #22
        0xE,
        (
            "趁天亮\x01",
            "赶快回家吧？\x02\x03",

            "绝对别忘了决斗哦！\x01",
            "那是我们的约定！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2350")

    label("loc_234C")

    Call(0, 15)

    label("loc_2350")

    Jump("loc_25D4")

    label("loc_2353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_25D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 0)), scpexpr(EXPR_END)), "loc_23AE")

    ChrTalk(    #23
        0xE,
        "好不容易……做的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#501F咦，什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #25
        0xE,
        "……没什么啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25D4")

    label("loc_23AE")

    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x101, 400)
    Sleep(600)
    OP_63(0xE)

    ChrTalk(    #26
        0xE,
        "啊───！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xE,
        "这不是艾、艾丝蒂尔吗！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#000F鲁克，好久不见呢。\x01",
            "还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xE,
        "呼呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        "……哼哼哼哼哼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        (
            "１００年没见了吧………\x01",
            "现在就让你见识见识我的修行成果吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "艾丝蒂尔·布莱特，\x01",
            "与本大人一决胜负！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#505F胜负……什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xE,
        "还用问吗，决斗啦决斗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "话说在前头，\x01",
            "我可不是以前的我了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#000F是吗……\x01",
            "决斗还是下次吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        "………………啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        "什、什么嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        (
            "才当了正游击士，\x01",
            "胆子就没了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xE,
        "……你是不是怎么啦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#001F你胡说什么。\x01",
            "我和平时一样啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1028)

    label("loc_25D4")

    OP_4B(0xFE, 255)
    TalkEnd(0xE)
    Return()

    # Function_13_1C49 end

    def Function_14_25DC(): pass

    label("Function_14_25DC")

    TalkBegin(0xF)
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FC")
    OP_A3(0x14)
    Call(0, 72)
    Jump("loc_2716")

    label("loc_25FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_26B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266E")

    ChrTalk(    #42
        0xF,
        (
            "刚才和妈妈一起\x01",
            "出席了婚礼……\x02\x03",

            "妈妈也真是的，\x01",
            "硬把鲁克也拉了去。\x02\x03",

            "鲁克真是\x01",
            "有点可怜啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_26B0")

    label("loc_266E")


    ChrTalk(    #43
        0xF,
        (
            "妈妈真是的，\x01",
            "把鲁克也带去参加婚礼了。\x02\x03",

            "鲁克真是\x01",
            "有点可怜啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B0")

    Jump("loc_2716")

    label("loc_26B3")


    ChrTalk(    #44
        0xF,
        (
            "其实我都想\x01",
            "和鲁克一起玩的……\x02\x03",

            "可是今天有要事\x01",
            "不得不早点回去。\x02\x03",

            "唉～婚礼什么的\x01",
            "我也不想去啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2716")

    Jump("loc_2955")

    label("loc_2719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_27E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2771")

    ChrTalk(    #45
        0xF,
        (
            "鲁克也真是的，\x01",
            "从刚才起就一直在说做梦的事。\x02\x03",

            "看来相当开心的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DD")

    label("loc_2771")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #46
        0xF,
        (
            "啊，姐姐！\x01",
            "鲁克完全没事了哦！\x02\x03",

            "不过，他从刚刚开始\x01",
            "就一直在说做梦的事。\x02\x03",

            "看来相当开心的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_27DD")

    Jump("loc_2955")

    label("loc_27E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_284D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_END)), "loc_2846")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #47
        0xF,
        (
            "我会听姐姐的话，\x01",
            "今天趁天还亮先回家去。\x02\x03",

            "会顺便将鲁克也\x01",
            "带走的，请放心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284A")

    label("loc_2846")

    Call(0, 15)

    label("loc_284A")

    Jump("loc_2955")

    label("loc_284D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 1)), scpexpr(EXPR_END)), "loc_28AE")

    ChrTalk(    #48
        0xF,
        (
            "鲁克听说了姐姐你们的事迹，\x01",
            "也开始学剑术了。\x02\x03",

            "他说一定要变得\x01",
            "和姐姐一样强。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2955")

    label("loc_28AE")


    ChrTalk(    #49
        0xF,
        "……艾丝蒂尔姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "你回来了，\x01",
            "回来了呢！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#000F嗯，我回来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xF,
        (
            "鲁克听说了姐姐你们的事迹，\x01",
            "也开始学剑术了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        (
            "他说一定要变得\x01",
            "和姐姐一样强。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1029)

    label("loc_2955")

    OP_4B(0xFE, 255)
    TalkEnd(0xF)
    Return()

    # Function_14_25DC end

    def Function_15_295D(): pass

    label("Function_15_295D")

    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xE)"), scpexpr(EXPR_END)), "loc_29C2")
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xE)

    ChrTalk(    #54
        0xE,
        "啊～！？艾丝蒂尔！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #55
        0xF,
        "艾丝蒂尔姐姐！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A14")

    label("loc_29C2")

    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xF)

    ChrTalk(    #56
        0xF,
        "啊，艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #57
        0xE,
        "啊～回来啦！\x02",
    )

    CloseMessageWindow()

    label("loc_2A14")


    ChrTalk(    #58
        0x101,
        (
            "#1001F啊哈哈，\x01",
            "不用那么大声啦。\x02\x03",

            "#1028F嗯……看来是\x01",
            "非常想我了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "才、才没在等你呢。\x02\x03",

            "你突、突然出现\x01",
            "稍微有点吃惊而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 400)

    ChrTalk(    #60
        0xF,
        (
            "咦……可是……？\x02\x03",

            "鲁克不是\x01",
            "一直在等姐姐回来吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)
    OP_62(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_63(0xE)

    ChrTalk(    #61
        0xE,
        (
            "笨、笨蛋！\x01",
            "我可没那么说过！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1012F哼哼，鲁克啊…\x01",
            "偶尔还挺可爱的嘛⊙\x02\x03",

            "#1018F来，别害臊…\x01",
            "对姐姐撒娇吧～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B6B():
        TurnDirection(0xE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B6B)
    Sleep(150)
    TurnDirection(0xF, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 0)), scpexpr(EXPR_END)), "loc_2BE8")

    ChrTalk(    #63
        0xE,
        (
            "别、别说得\x01",
            "那么恶心啦！\x02\x03",

            "话、话说回来\x01",
            "可别说你忘了！\x02\x03",

            "决斗吧！艾丝蒂尔。\x01",
            "先和我决斗再说！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C53")

    label("loc_2BE8")


    ChrTalk(    #64
        0xE,
        (
            "别、别说得\x01",
            "那么恶心啦！\x02\x03",

            "话、话说回来决胜负吧！\x01",
            "和我一对一单挑！\x02\x03",

            "决斗吧！艾丝蒂尔。\x01",
            "可别吓得逃跑哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C53")


    ChrTalk(    #65
        0x101,
        (
            "#1007F啊，决斗……\x01",
            "真是的，说什么呢。\x02\x03",

            "没看见这么大雾吗？\x01",
            "赶快回家啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "笨蛋，有雾正好。\x02\x03",

            "在雾中决斗\x01",
            "简直酷毙了不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1009F说这种话\x01",
            "就证明你还是个小鬼。\x02\x03",

            "让别人担心\x01",
            "可是一点都不酷哦。\x02\x03",

            "那个翡翠之塔的事……\x01",
            "难不成你就忘了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #68
        0xE,
        "呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xF,
        "姐、姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1010F要想成为独当一面的男子汉，\x01",
            "首先要做到不用别人担心哦。\x02\x03",

            "自己一个人都照顾不好，\x01",
            "就别想照顾别人了。\x02\x03",

            "#1002F这种事……\x01",
            "你们现在也该明白了吧？\x02\x03",

            "让我看看你们\x01",
            "稍微成熟的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xE,
        (
            "……切…………\x02\x03",

            "知、知道啦。\x01",
            "决斗就下次吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xF,
        (
            "抱歉哦，姐姐。\x02\x03",

            "趁着天还没黑\x01",
            "我们得先回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1006F嗯，赶快去吧。\x01",
            "答应姐姐哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xF,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "随便怎样都好啦，\x01",
            "决斗的事可别忘了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1007F唉～好好好。\x02\x03",

            "等到这阵雾散了\x01",
            "随时奉陪啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xE,
        "好，就这么说定啰！\x02",
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_A2(0x1883)
    Return()

    # Function_15_295D end

    def Function_16_2F54(): pass

    label("Function_16_2F54")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_3046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2FBC")

    ChrTalk(    #78
        0xFE,
        (
            "和女朋友一起去王都\x01",
            "参观女王诞辰庆典。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "不过被卷进那个\x01",
            "政变，运气真够差的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3046")

    label("loc_2FBC")


    ChrTalk(    #80
        0xFE,
        (
            "和女朋友一起去王都\x01",
            "参观女王诞辰庆典。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "不过居然遇到那个\x01",
            "政变事件，运气真够差的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "难得的求婚也被\x01",
            "冲进城里的亲卫队打乱了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3046")

    TalkEnd(0x13)
    Return()

    # Function_16_2F54 end

    def Function_17_304A(): pass

    label("Function_17_304A")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_30A2")

    ChrTalk(    #83
        0xFE,
        (
            "跟他的王都之旅\x01",
            "确实非常棒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "不过像现在这样的\x01",
            "平凡日子也很不错哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A2")

    TalkEnd(0x12)
    Return()

    # Function_17_304A end

    def Function_18_30A6(): pass

    label("Function_18_30A6")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3139")

    ChrTalk(    #85
        0xFE,
        (
            "虽然定期船停了，\x01",
            "还是要做好出货的准备……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "得尽快做完工作，\x01",
            "准备去礼拜堂才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "因为今天\x01",
            "我被邀请参加婚礼了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_3181")

    label("loc_3139")


    ChrTalk(    #88
        0xFE,
        (
            "早点弄完工作\x01",
            "准备去礼拜堂才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "因为今天\x01",
            "我被邀请参加婚礼了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3181")

    Jump("loc_373F")

    label("loc_3184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_355B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 2)), scpexpr(EXPR_END)), "loc_327B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3208")

    ChrTalk(    #90
        0xFE,
        (
            "雾也散了，\x01",
            "总算能放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "那么，接下来\x01",
            "就要忙木材的出货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "我也得鼓起干劲\x01",
            "努力工作才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3278")

    label("loc_3208")


    ChrTalk(    #93
        0xFE,
        (
            "我也要学习岳父\x01",
            "从现在开始努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "定期船的航行也恢复了，\x01",
            "要开始忙木材的出货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "那么，你们也当心。\x02",
    )

    CloseMessageWindow()

    label("loc_3278")

    Jump("loc_3558")

    label("loc_327B")


    ChrTalk(    #96
        0xFE,
        "呀，游击士们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "托你们的福，岳父\x01",
            "总算清醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1015F岳父是……\x02\x03",

            "#1011F啊，是说拉欧爷爷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x103,
        (
            "#020F爱娜说的对，\x01",
            "看来大家都醒了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #100
        0xFE,
        (
            "嗯嗯，岳父\x01",
            "虽然还有点迷糊，\x01",
            "但身体应该是没有问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "有精神得想赶快工作，\x01",
            "还把我赶出门呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1001F啊哈哈，那看来没问题了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C8")

    ChrTalk(    #103
        0x105,
        "#048F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3451")

    label("loc_33C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F2")

    ChrTalk(    #104
        0x107,
        "#061F嘿嘿……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3451")

    label("loc_33F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3424")

    ChrTalk(    #105
        0x106,
        "#051F啊啊，看来可以放心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3451")

    label("loc_3424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3451")

    ChrTalk(    #106
        0x108,
        "#070F啊啊，不用担心了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3451")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #107
        0xFE,
        (
            "真是的……\x01",
            "我还那么担心，真傻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "不过，我也得向岳父学习，\x01",
            "增强体力才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "定期船的航行也恢复了，\x01",
            "要开始忙木材的出货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1006F嗯，请加油吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x103,
        "#525F别输给你岳父哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #112
        0xFE,
        "啊啊，我会尽最大努力的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "那么，\x01",
            "你们也当心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A62)
    OP_A2(0x1)

    label("loc_3558")

    Jump("loc_373F")

    label("loc_355B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35C4")

    ChrTalk(    #114
        0xFE,
        (
            "突然就起这么大的雾，\x01",
            "感觉很不寻常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "去森林巡视的时候，\x01",
            "也要小心不要迷路啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3650")

    label("loc_35C4")


    ChrTalk(    #116
        0xFE,
        (
            "突然就起这么大的雾，\x01",
            "感觉很不寻常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "不过，大自然这东西\x01",
            "就是这么反复无常，没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "要应付好它就是\x01",
            "我们经营林业之人的宿命。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3650")

    Jump("loc_373F")

    label("loc_3653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_373F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_36B1")

    ChrTalk(    #119
        0xFE,
        (
            "砍伐结束之后，\x01",
            "在日落前都要进行植树的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "今天看来也会很忙呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_373F")

    label("loc_36B1")


    ChrTalk(    #121
        0xFE,
        (
            "接下来就要去神秘森林\x01",
            "砍伐树木了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "树可是这片大地唯一\x01",
            "能够再生的天然资源哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "培育森林，与森林一起生活──\x01",
            "这就是真正的林业。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_373F")

    TalkEnd(0x11)
    Return()

    # Function_18_30A6 end

    def Function_19_3743(): pass

    label("Function_19_3743")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_3AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BE")
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #124
        0xFE,
        "啊，艾丝蒂尔和约修亚！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37FB")
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #125
        0xFE,
        "呀，还有雪拉小姐☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x103,
        "#021F呵呵，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        "#1040F还好吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3838")

    label("loc_37FB")


    ChrTalk(    #128
        0x101,
        "#1001F哟嗬～克露莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#1040F好久不见了呢。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3838")

    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #130
        0xFE,
        (
            "克露莎一直都很好哦。\x01",
            "因为身体就是记者的资本啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "不过，艾丝蒂尔你们似乎\x01",
            "也相当活跃嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C3")

    label("loc_38A2")


    ChrTalk(    #132
        0xFE,
        (
            "我都听说了哦。\x01",
            "相当活跃嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C3")


    ChrTalk(    #133
        0xFE,
        (
            "你们在玛鲁加矿山\x01",
            "救了矿工们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1008F啊，你的消息还是那么灵通。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#1044F感觉上……\x01",
            "比以前更加厉害了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "你们才刚刚回来\x01",
            "就马上活跃起来，真有一套。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "照这个情况看来，连那个浮游岛的谜\x01",
            "也能很快解开吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "克露莎，好期待哦☆\x02",
    )

    CloseMessageWindow()
    OP_A2(0x13)
    OP_A2(0x20A6)
    Jump("loc_3AB3")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A57")

    ChrTalk(    #139
        0xFE,
        (
            "阿鲁姆他们的婚礼\x01",
            "也没发生什么特别的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "但是，即使是无聊的新闻\x01",
            "也得拿去撑版面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "嗯，这个意义上来说\x01",
            "阿鲁姆还算是不错的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3AB3")

    label("loc_3A57")


    ChrTalk(    #142
        0xFE,
        (
            "阿鲁姆他们的婚礼\x01",
            "也没发生什么特别的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "但是，即使是无聊的新闻\x01",
            "也得拿去撑版面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB3")

    Jump("loc_4705")

    label("loc_3AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7D")
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #144
        0xFE,
        "啊，艾丝蒂尔和约修亚！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B63")
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #145
        0xFE,
        "呀，还有雪拉小姐☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        "#021F呵呵，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        "#1040F还好吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA0")

    label("loc_3B63")


    ChrTalk(    #148
        0x101,
        "#1001F哟嗬～克露莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        (
            "#1040F好久不见了呢。\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA0")

    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #150
        0xFE,
        (
            "克露莎一直都很好哦。\x01",
            "因为身体就是记者的资本啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C4F")

    ChrTalk(    #151
        0xFE,
        (
            "但是，这么有前途的年轻游击士\x01",
            "同时出现３个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "这一定是为了那个吧。\x01",
            "导力停止现象的调查？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB1")

    label("loc_3C4F")


    ChrTalk(    #153
        0xFE,
        (
            "但是，这么有前途的年轻游击士\x01",
            "两人一起回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "这一定是为了那个吧。\x01",
            "导力停止现象的调查？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB1")


    ChrTalk(    #155
        0x101,
        "#1007F嗯……你还是那么敏锐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        (
            "#1044F这么难的词\x01",
            "你竟然也知道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "我采访过佛莱迪先生啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "虽然浮游岛的事也很受瞩目，\x01",
            "不过最热门话题还是这次异变嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "克露莎也打算\x01",
            "跟踪报导哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    OP_A2(0x20A5)
    Jump("loc_3EAB")

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E47")

    ChrTalk(    #160
        0xFE,
        (
            "谁说最热门话题\x01",
            "是导力停止现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "今天预定去报道\x01",
            "阿鲁姆和艾娅莉的婚礼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "从相关人员那里拿到了请帖，\x01",
            "克露莎正打算去采访呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "不加入点地方性的话题，\x01",
            "读者就不会有兴趣嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3EAB")

    label("loc_3E47")


    ChrTalk(    #164
        0xFE,
        (
            "今天预定去报道\x01",
            "阿鲁姆和艾娅莉的婚礼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "从相关人员那里拿到了请帖，\x01",
            "克露莎正打算去采访呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EAB")

    Jump("loc_4705")

    label("loc_3EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_40DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 1)), scpexpr(EXPR_END)), "loc_3F1E")

    ChrTalk(    #166
        0xFE,
        "竟然在这时候发生事件啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "帝国主战派和情报部……\x01",
            "还有空贼团呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "唔～想不出来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40D7")

    label("loc_3F1E")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #169
        0xFE,
        "啊，艾丝蒂尔和雪拉小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "你们真的要离开洛连特？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        "#020F嗯嗯，很快就要走了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1007F抱歉哦，克露莎。\x01",
            "别的地方还有工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "两人一起去……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "啊，一定发生了大事吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "帝国主战派以互不侵犯条约掩人耳目，\x01",
            "准备偷偷侵略的阴谋？\x01",
            "还是情报部的余党？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "嗯嗯，也有可能\x01",
            "是空贼团的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "呼，想不出来啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #178
        0x101,
        (
            "#1019F（这、这个小鬼\x01",
            "的直觉还真是敏锐。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x103,
        "#021F（真是，不能小看啊。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A61)

    label("loc_40D7")

    Jump("loc_4705")

    label("loc_40DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_44B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 1)), scpexpr(EXPR_END)), "loc_4298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_414C")

    ChrTalk(    #180
        0xFE,
        (
            "卡西乌斯先生不在城里，\x01",
            "最近的话题好少哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "只有利吉先生一个人，\x01",
            "实在是好无趣啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4295")

    label("loc_414C")

    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_41AB")

    ChrTalk(    #182
        0xFE,
        "话说回来，你们俩也是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "乘坐定期船\x01",
            "中途停在这里被赶下来的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F6")

    label("loc_41AB")


    ChrTalk(    #184
        0xFE,
        "啊，艾丝蒂尔和雪拉小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "你们俩也是从定期船上\x01",
            "中途被赶下来的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F6")


    ChrTalk(    #186
        0x101,
        (
            "#1015F唔，嗯，是这样……\x02\x03",

            "#1007F观察真的很敏锐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "卡西乌斯先生不在\x01",
            "话题也好少哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "嗯，你们俩要加油\x01",
            "想办法热闹一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "克露莎很期待哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_4295")

    Jump("loc_44AD")

    label("loc_4298")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #190
        0xFE,
        (
            "啊～艾丝蒂尔！\x01",
            "还有雪拉小姐！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        "#1018F嗨～克露莎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x103,
        "#021F呵呵，乖乖的吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #193
        0xFE,
        (
            "嘿嘿，克露莎\x01",
            "一直都是乖孩子呀。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #194
        0xFE,
        "对了对了，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "听说现在约修亚\x01",
            "在单独行动哟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "不过根据克露莎的直觉\x01",
            "这是假情报吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "其实是接受了协会的秘密指令\x01",
            "与邪恶组织作战去了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #198
        0x101,
        (
            "#1019F（呼……\x01",
            "　好、好厉害！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "嗯，这才是最佳剧情吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "因为约修亚\x01",
            "根本不适合平凡的剧情嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "独自潜入\x01",
            "邪恶组织基地的约修亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "啊啊，克露莎都着迷了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x1899)

    label("loc_44AD")

    Jump("loc_4705")

    label("loc_44B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_4705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 2)), scpexpr(EXPR_END)), "loc_4555")

    ChrTalk(    #203
        0xFE,
        "艾丝蒂尔，约修亚在哪里？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "还是说旁边这人是你新男朋友，\x01",
            "你就把约修亚给甩了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#000F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x142,
        "#1064F（……小妹妹，嘘……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4705")

    label("loc_4555")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #207
        0xFE,
        "啊～是艾丝蒂尔！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#000F克露莎，好久不见。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x142, 400)
    Sleep(600)

    ChrTalk(    #209
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "你是谁啦～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x142,
        "#1064F咦，说我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "啊，难道是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "……破坏约修亚和艾丝蒂尔\x01",
            "关系的神秘男人登场了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "在克露莎不知道的情况下\x01",
            "关系发展得如火如荼。\x01",
            "这是绝对不允许的～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#506F我说……克露莎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "对了，他一定会和约修亚\x01",
            "作战，产生了友情\x01",
            "最后却命丧黄泉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x142,
        "#1061F好、好厉害的孩子啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x102A)

    label("loc_4705")

    TalkEnd(0x10)
    Return()

    # Function_19_3743 end

    def Function_20_4709(): pass

    label("Function_20_4709")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_482E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4768")

    ChrTalk(    #218
        0xFE,
        "这就是洛连特的钟楼吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "这里是背负了沉重历史的\x01",
            "百日战役的遗迹吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_482E")

    label("loc_4768")


    ChrTalk(    #220
        0xFE,
        "这就是洛连特的钟楼吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "虽说容易被错过，这里也是\x01",
            "那个百日战役的遗迹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "洛连特攻防战中，这里\x01",
            "被帝国军的炮弹直接击中了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "据说因此牺牲了很多不幸的市民，\x01",
            "背负着沉重的历史啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_482E")

    TalkEnd(0x14)
    Return()

    # Function_20_4709 end

    def Function_21_4832(): pass

    label("Function_21_4832")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_494D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4898")

    ChrTalk(    #224
        0xFE,
        (
            "终于雾散天晴了，\x01",
            "可以尽情拍摄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "首先从洛连特的标志…\x01",
            "这个钟楼开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494D")

    label("loc_4898")


    ChrTalk(    #226
        0xFE,
        (
            "终于雾散天晴了，\x01",
            "可以尽情拍摄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "首先从洛连特的标志…\x01",
            "本打算从钟楼开始拍……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "但听了这里的历史，\x01",
            "都不敢随便按下快门了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "从镜头里看过去\x01",
            "感觉气氛也好严肃哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_494D")

    TalkEnd(0x15)
    Return()

    # Function_21_4832 end

    def Function_22_4951(): pass

    label("Function_22_4951")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 0)), scpexpr(EXPR_END)), "loc_49E0")

    ChrTalk(    #230
        0xFE,
        (
            "客人们请集中，\x01",
            "我们打算出发去王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "就像雪拉前辈说的一样，\x01",
            "现在能见度太差了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "我们也会十分小心地\x01",
            "前去王都。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C71")

    label("loc_49E0")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x103, 0)
    Sleep(400)

    ChrTalk(    #233
        0xFE,
        "啊，艾丝蒂尔和雪拉前辈！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x103,
        "#020F哎呀，这不是利吉吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        "#1001F利吉先生，好久不见。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #236
        0xFE,
        (
            "哟，艾丝蒂尔。\x01",
            "出发去了训练场以后就没见到你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "我听爱娜小姐说了哦。\x01",
            "你在做很重要的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#1015F嗯……算是吧。\x02\x03",

            "利吉先生也\x01",
            "在工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "啊啊，这边的客人们\x01",
            "好像有急事要去王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "这样下去今天\x01",
            "定期船恐怕也没法航行了，\x01",
            "所以要我送他们去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        "#1011F啊～要去王都啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x103,
        (
            "#026F由于起雾，道路上的视野很不好呢。\x02\x03",

            "#027F要比平常\x01",
            "更加注意周围哟。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #243
        0xFE,
        "是，我会小心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "那么，前辈你们也\x01",
            "请努力完成任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        (
            "#1006F利吉先生也是。\x01",
            "护卫的工作请加油。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #246
        0xFE,
        "啊啊，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "客人们我\x01",
            "必定平安送到。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1880)

    label("loc_4C71")

    TalkEnd(0x16)
    Return()

    # Function_22_4951 end

    def Function_23_4C75(): pass

    label("Function_23_4C75")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4CE3")

    ChrTalk(    #248
        0xFE,
        (
            "据说在王都有重要的贸易谈判呢。\x01",
            "无论如何也必须要去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "是做大生意的机会，\x01",
            "绝对不能错过的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE3")

    TalkEnd(0x17)
    Return()

    # Function_23_4C75 end

    def Function_24_4CE7(): pass

    label("Function_24_4CE7")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4D4D")

    ChrTalk(    #250
        0xFE,
        (
            "哎呀，这种时候有游击士在\x01",
            "真是令人安心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "一个人在大雾里奔走\x01",
            "实在连想都不敢想啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D4D")

    TalkEnd(0x18)
    Return()

    # Function_24_4CE7 end

    def Function_25_4D51(): pass

    label("Function_25_4D51")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4D9D")

    ChrTalk(    #252
        0xFE,
        (
            "没想到定期船\x01",
            "会停航啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "嗯，不过有游击士\x01",
            "护送就放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9D")

    TalkEnd(0x19)
    Return()

    # Function_25_4D51 end

    def Function_26_4DA1(): pass

    label("Function_26_4DA1")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4EB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4E34")

    ChrTalk(    #254
        0xFE,
        (
            "刚才稍微看了一下\x01",
            "偷溜出去的鲁克哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "意识还没恢复，\x01",
            "但睡得很安稳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "现在为了那孩子\x01",
            "我也必须完成自己的责任和义务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EB6")

    label("loc_4E34")


    ChrTalk(    #257
        0xFE,
        (
            "现在还没什么问题，\x01",
            "总之警备还算顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "但是，只要这个状态持续，\x01",
            "说不定还会发生事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "大家看来都\x01",
            "不能放松警惕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4EB6")

    Jump("loc_4F18")

    label("loc_4EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_4F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 0)), scpexpr(EXPR_END)), "loc_4F14")

    ChrTalk(    #260
        0xFE,
        (
            "我们\x01",
            "已经开始警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "这边就交给我们吧。\x01",
            "协会的工作就靠你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F18")

    label("loc_4F14")

    Call(0, 28)

    label("loc_4F18")

    TalkEnd(0x28)
    Return()

    # Function_26_4DA1 end

    def Function_27_4F1C(): pass

    label("Function_27_4F1C")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_4F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x314, 0)), scpexpr(EXPR_END)), "loc_4F77")

    ChrTalk(    #262
        0xFE,
        "总之先开始警备吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "嗯，应该会有些问题\x01",
            "不过一定能慢慢解决的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F7B")

    label("loc_4F77")

    Call(0, 28)

    label("loc_4F7B")

    TalkEnd(0x27)
    Return()

    # Function_27_4F1C end

    def Function_28_4F7F(): pass

    label("Function_28_4F7F")

    OP_4A(0x28, 255)
    OP_4A(0x27, 255)
    ClearChrFlags(0x28, 0x10)
    ClearChrFlags(0x27, 0x10)

    ChrTalk(    #264
        0x28,
        (
            "……对了戴恩副队长。\x01",
            "西门的配置完成了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x27,
        (
            "……啊，那个地方\x01",
            "安排了两个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x27,
        (
            "不过视情况\x01",
            "应该得考虑增员吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x28,
        (
            "原来如此……\x01",
            "好，那么接下来是定期报告……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x28)

    def lambda_5057():
        TurnDirection(0x28, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_5057)
    Sleep(150)
    TurnDirection(0x27, 0x101, 400)

    ChrTalk(    #268
        0x28,
        "噢，艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x28,
        (
            "我们\x01",
            "已经开始警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x28,
        (
            "这边就交给我们吧。\x01",
            "协会的工作就靠你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#1002F嗯！警备就拜托了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x28, 0x27, 0)
    TurnDirection(0x27, 0x28, 0)
    OP_4B(0x28, 255)
    OP_4B(0x27, 255)
    OP_A2(0x18A0)
    Return()

    # Function_28_4F7F end

    def Function_29_5103(): pass

    label("Function_29_5103")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_51C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5175")

    ChrTalk(    #272
        0xFE,
        (
            "感觉市民们都在看着\x01",
            "一刻也不敢松懈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "嗯，虽说想想也不会有人\x01",
            "有兴趣在雾中盯着士兵看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51C1")

    label("loc_5175")


    ChrTalk(    #274
        0xFE,
        (
            "但是感觉市民们都在看着，\x01",
            "一刻也不敢松懈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "却连个哈欠也不敢打。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_51C1")

    Jump("loc_521D")

    label("loc_51C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_521D")

    ChrTalk(    #276
        0xFE,
        (
            "离开威尔特桥，\x01",
            "这可是第一次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "呼，呼……\x01",
            "这种紧张感果然还是不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_521D")

    TalkEnd(0x1F)
    Return()

    # Function_29_5103 end

    def Function_30_5221(): pass

    label("Function_30_5221")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_531D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5293")

    ChrTalk(    #278
        0xFE,
        (
            "就算有魔兽和可疑人士，\x01",
            "不走到近距离也很难辨认。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "警，警备的我们\x01",
            "老实说都有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531A")

    label("loc_5293")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #280
        0xFE,
        (
            "怎、怎么……\x01",
            "你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "呼，呼……\x01",
            "别吓唬我啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "一想到会出现魔兽和可疑人士\x01",
            "就好紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_531A")

    Jump("loc_53FE")

    label("loc_531D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_53FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5384")

    ChrTalk(    #283
        0xFE,
        (
            "我才刚到这城市，\x01",
            "突然就派任务下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "今天的阿斯顿队长\x01",
            "也比平时更加严厉哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53FE")

    label("loc_5384")


    ChrTalk(    #285
        0xFE,
        (
            "我才刚到这城市，\x01",
            "突然就开始派任务下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "今天的阿斯顿队长\x01",
            "也比平时更加严厉哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "队长这次果然\x01",
            "很严格啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_53FE")

    TalkEnd(0x20)
    Return()

    # Function_30_5221 end

    def Function_31_5402(): pass

    label("Function_31_5402")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_551B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5480")

    ChrTalk(    #288
        0xFE,
        (
            "执行这种任务的时候，\x01",
            "身旁有个沉默寡言的伙伴可真叫人受不了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "就算鼓起勇气搭话，\x01",
            "那边也没反应。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5518")

    label("loc_5480")


    ChrTalk(    #290
        0xFE,
        (
            "如果是平常的话\x01",
            "我不讨厌沉默的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "执、执行这种任务的时候\x01",
            "身旁有个沉默寡言的伙伴可叫人受不了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "意外的让人分心\x01",
            "反而自己更觉得累。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_5518")

    Jump("loc_55F3")

    label("loc_551B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_55F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_557E")

    ChrTalk(    #293
        0xFE,
        (
            "现在的洛连特\x01",
            "简直像另一个世界似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "盯着看一下下\x01",
            "就感觉到丝丝的寒意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55F3")

    label("loc_557E")


    ChrTalk(    #295
        0xFE,
        (
            "平常休息我偶尔也会\x01",
            "来洛连特玩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "不过现在像是另一个世界似的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "盯着看一下下\x01",
            "就感觉到丝丝的寒意呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_55F3")

    TalkEnd(0x21)
    Return()

    # Function_31_5402 end

    def Function_32_55F7(): pass

    label("Function_32_55F7")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_568E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5634")

    ChrTalk(    #298
        0xFE,
        (
            "…………………………\x01",
            "……没有异常。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_568B")

    label("loc_5634")


    ChrTalk(    #299
        0xFE,
        (
            "…………………………\x01",
            "……没有异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "…………………………\x01",
            "……有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_568B")

    Jump("loc_56E8")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_56E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_56B7")

    ChrTalk(    #301
        0xFE,
        "………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_56E8")

    label("loc_56B7")


    ChrTalk(    #302
        0xFE,
        "………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        "……有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_56E8")

    TalkEnd(0x22)
    Return()

    # Function_32_55F7 end

    def Function_33_56EC(): pass

    label("Function_33_56EC")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_57AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5758")

    ChrTalk(    #304
        0xFE,
        (
            "多明戈先生这种自信\x01",
            "是从哪儿来的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "不过，万一有事\x01",
            "希望他还能维持这种自信啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A9")

    label("loc_5758")


    ChrTalk(    #306
        0xFE,
        (
            "多明戈先生这种自信\x01",
            "是从哪儿来的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "从哈肯大门来的人\x01",
            "果然不一样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_57A9")

    Jump("loc_58A7")

    label("loc_57AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_58A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_581F")

    ChrTalk(    #308
        0xFE,
        (
            "威尔特桥那边\x01",
            "是由补充部队负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "既然是国境师团所属的士兵，\x01",
            "实力上应该也不会有什么问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A7")

    label("loc_581F")


    ChrTalk(    #310
        0xFE,
        (
            "现在威尔特桥那边\x01",
            "是由补充部队负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "虽说是补充部队\x01",
            "但实力上应该没有任何问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "因为他们平时可是\x01",
            "国境师团所属的士兵呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_58A7")

    TalkEnd(0x23)
    Return()

    # Function_33_56EC end

    def Function_34_58AB(): pass

    label("Function_34_58AB")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_596C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_5900")

    ChrTalk(    #313
        0xFE,
        "城市方面也完全没有问题啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "哈哈哈。\x01",
            "别这么担心嘛老兄！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5969")

    label("loc_5900")


    ChrTalk(    #315
        0xFE,
        "城市方面也完全没有问题啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "哈哈哈。\x01",
            "别这么担心嘛老兄！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "既然我都这么说了\x01",
            "就一定没错啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_5969")

    Jump("loc_5A1E")

    label("loc_596C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_5A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_59BF")

    ChrTalk(    #318
        0xFE,
        (
            "既然我来了\x01",
            "城市的安全就有保障啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "哈哈哈。\x01",
            "总之放心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A1E")

    label("loc_59BF")


    ChrTalk(    #320
        0xFE,
        (
            "哦，你们是刚才在街道\x01",
            "碰见的那些游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "啊啊，放心吧。\x01",
            "我可以保证城市的安全啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_5A1E")

    TalkEnd(0x24)
    Return()

    # Function_34_58AB end

    def Function_35_5A22(): pass

    label("Function_35_5A22")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_5ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5A84")

    ChrTalk(    #322
        0xFE,
        (
            "总之天黑以前\x01",
            "就这样继续在外面巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "我们这样做\x01",
            "市民也会感到安心吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD9")

    label("loc_5A84")


    ChrTalk(    #324
        0xFE,
        (
            "现在这时，\x01",
            "不会有可疑人物的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "不过，在这大雾之中\x01",
            "能见度的确十分的低啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_5AD9")

    Jump("loc_5B51")

    label("loc_5ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_5B51")

    ChrTalk(    #326
        0xFE,
        (
            "虽说听过传闻，\x01",
            "实际看来是相当诡异的雾啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        (
            "虽然我们是记下地图才来的\x01",
            "但在这浓雾中还是会迷路的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B51")

    TalkEnd(0x25)
    Return()

    # Function_35_5A22 end

    def Function_36_5B55(): pass

    label("Function_36_5B55")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_5BDF")

    ChrTalk(    #328
        0xFE,
        (
            "哟，游击士。\x01",
            "这边没什么异常啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "硬要说有什么异常的话，\x01",
            "那就是这些鸽子旺盛的食欲了，\x01",
            "都起这么大雾了还是那么能吃啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C34")

    label("loc_5BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_5C34")

    ChrTalk(    #330
        0xFE,
        (
            "真是好久没离开哈肯大门\x01",
            "执行任务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "这种工作用来\x01",
            "换换心情倒是不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C34")

    TalkEnd(0x26)
    Return()

    # Function_36_5B55 end

    def Function_37_5C38(): pass

    label("Function_37_5C38")

    TalkBegin(0x29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_5CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_5C65")

    ChrTalk(    #332
        0xFE,
        (
            "欢迎！\x01",
            "请随便看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CC8")

    label("loc_5C65")


    ChrTalk(    #333
        0xFE,
        (
            "请进！\x01",
            "欢迎光临里农杂货铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "虽然今天也很大雾，\x01",
            "不过还是照常营业哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        "请随便看看。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_5CC8")

    TalkEnd(0x29)
    Return()

    # Function_37_5C38 end

    def Function_38_5CCC(): pass

    label("Function_38_5CCC")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_5DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D89")
    OP_4A(0x34, 255)

    ChrTalk(    #336
        0xFE,
        (
            "阿鲁姆和艾娅莉。\x01",
            "非常棒呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "唉～我家的安莉尔\x01",
            "也能举行那样的婚礼就好了～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x34, 400)

    ChrTalk(    #338
        0xFE,
        (
            "是吧～～安莉尔～～\x01",
            "和你老公商量看看～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #339
        0x34,
        "喵～～呜。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x34, 255)
    OP_A2(0x10)
    Jump("loc_5DDD")

    label("loc_5D89")


    ChrTalk(    #340
        0xFE,
        (
            "阿鲁姆和艾娅莉。\x01",
            "非常棒呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "唉～我家的安莉尔\x01",
            "也能举行那样的婚礼就好了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDD")

    Jump("loc_62D3")

    label("loc_5DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5E38")

    ChrTalk(    #342
        0xFE,
        (
            "喂喂小猫咪们～\x01",
            "别玩了，快准备好～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        (
            "等下要去出席\x01",
            "很重要的婚礼哦～～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D3")

    label("loc_5E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_622C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5FE2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_5ECA")

    ChrTalk(    #344
        0xFE,
        (
            "嗯～怎样的名字\x01",
            "才适合小猫咪呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        (
            "科洛～蒂娅……\x01",
            "简称小科洛\x01",
            "应该很可爱～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        "不过对公主殿下太失礼了吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FDF")

    label("loc_5ECA")


    ChrTalk(    #347
        0xFE,
        (
            "哎呀～～\x01",
            "游击士们～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "你们看～～\x01",
            "小猫咪们很精神吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        (
            "#1001F啊哈哈，没错没错。\x02\x03",

            "#1011F对了对了，名字决定了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #350
        0xFE,
        (
            "嗯，这个\x01",
            "还没呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "虽然想了很久…\x01",
            "还是很伤脑筋啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "唉～长大之前\x01",
            "能决定就好了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1019F不、不……\x01",
            "别等到长大还没名字吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x2000)

    label("loc_5FDF")

    Jump("loc_6229")

    label("loc_5FE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_6140")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_606D")

    ChrTalk(    #354
        0xFE,
        (
            "嗯～怎样的名字\x01",
            "才适合小猫咪呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "科洛～蒂娅……\x01",
            "简称小科洛\x01",
            "应该很可爱～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        "不过对公主殿下太失礼了吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_613D")

    label("loc_606D")


    ChrTalk(    #357
        0xFE,
        (
            "哎呀～～\x01",
            "游击士们～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        (
            "你们看～～安莉尔\x01",
            "当了妈妈回来了哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #359
        0x101,
        (
            "#1004F咦咦！？\x02\x03",

            "这……带着自己的宝宝们回来的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #360
        0xFE,
        "嗯～是啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xFE,
        (
            "所以，现在\x01",
            "正在想名字哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x2000)

    label("loc_613D")

    Jump("loc_6229")

    label("loc_6140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_6192")

    ChrTalk(    #362
        0xFE,
        (
            "安莉尔的宝宝们\x01",
            "可得早点起名字才行～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "嗯～怎样的\x01",
            "名字才好呢～～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6229")

    label("loc_6192")


    ChrTalk(    #364
        0xFE,
        (
            "安莉尔的宝宝们\x01",
            "可得早点起名字才行～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "嗯～怎样的\x01",
            "名字才好呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "科洛～蒂娅……\x01",
            "简称小科洛\x01",
            "应该很可爱～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        "不过对公主殿下太失礼了吧～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_6229")

    Jump("loc_62D3")

    label("loc_622C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_62D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_6267")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #368
        0xFE,
        "……呼呼。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_62D3")

    label("loc_6267")

    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #369
        0xFE,
        "嗯～…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "……呼呼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x101,
        (
            "#1019F（这、这种情况下\x01",
            "居然睡得着啊～）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    OP_A2(0x10)

    label("loc_62D3")

    TalkEnd(0x33)
    Return()

    # Function_38_5CCC end

    def Function_39_62D7(): pass

    label("Function_39_62D7")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_62F9")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #372
        0xFE,
        "喵～～呜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6329")

    label("loc_62F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6318")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #373
        0xFE,
        "喵～～呜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6329")

    label("loc_6318")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #374
        0xFE,
        "喵啊～\x02",
    )

    CloseMessageWindow()

    label("loc_6329")

    TalkEnd(0x34)
    Return()

    # Function_39_62D7 end

    def Function_40_632D(): pass

    label("Function_40_632D")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_6377")

    ChrTalk(    #375
        0xFE,
        "哎呀，姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        (
            "我虽然酒量很差，\x01",
            "但我是真心的哦……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645F")

    label("loc_6377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_645F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_63E4")

    ChrTalk(    #377
        0xFE,
        (
            "没想到那么漂亮的人\x01",
            "居然那么能喝啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "唔唔～……真糟糕。\x01",
            "这下可就不能随便约她了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_645F")

    label("loc_63E4")


    ChrTalk(    #379
        0xFE,
        "啊啊，真伤脑筋……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "没想到那么漂亮的人\x01",
            "居然那么能喝啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "唔唔～真糟糕啊。\x01",
            "这不就没法草率地提出邀请了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_645F")

    TalkEnd(0x2A)
    Return()

    # Function_40_632D end

    def Function_41_6463(): pass

    label("Function_41_6463")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_6551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_64B9")

    ChrTalk(    #382
        0xFE,
        (
            "请别介意\x01",
            "我旁边的同伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "只是平常的相思病\x01",
            "又发作了而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_654E")

    label("loc_64B9")


    ChrTalk(    #384
        0xFE,
        (
            "士兵们\x01",
            "似乎开始城市警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "好像很紧张似的，\x01",
            "要发生事件了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "此外……\x01",
            "请别介意我旁边的同伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "只是平常的相思病\x01",
            "又发作了罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_654E")

    Jump("loc_663C")

    label("loc_6551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_663C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_65B4")

    ChrTalk(    #388
        0xFE,
        (
            "安敦喜欢的女性\x01",
            "感觉和他不合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        (
            "不可能的事就早点死心，\x01",
            "看看鸽子就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_663C")

    label("loc_65B4")


    ChrTalk(    #390
        0xFE,
        (
            "安敦中意的女性，\x01",
            "感觉实在跟他不合啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "不可能的事就早点死心，\x01",
            "还不如去看看鸽子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "鸽子真有趣啊……\x01",
            "怎么看也看不腻呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_663C")

    TalkEnd(0x2B)
    Return()

    # Function_41_6463 end

    def Function_42_6640(): pass

    label("Function_42_6640")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6660")
    Call(0, 76)
    FadeToBright(0, 0)
    Call(0, 77)

    label("loc_6660")

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
    OP_43(0x101, 0x1, 0x0, 0x2B)
    OP_43(0x103, 0x1, 0x0, 0x2C)
    OP_43(0xF8, 0x1, 0x0, 0x2D)
    OP_43(0xF9, 0x1, 0x0, 0x2E)
    Sleep(2000)

    def lambda_6728():
        OP_6D(50680, 250, 28860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6728)

    def lambda_6740():
        OP_6C(39000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6740)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #393
        0x101,
        (
            "#1007F呼……\x01",
            "话说回来还真厉害呢。\x02\x03",

            "明明是熟到不能再熟的城市，\x01",
            "但却感觉会迷路似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x103,
        (
            "#020F为了不迷路\x01",
            "才带了地图和罗盘嘛。\x02\x03",

            "如果迷失了方向\x01",
            "就一边找方向一边前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68D1")

    ChrTalk(    #395
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "阿加特，提妲。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x106,
        "#051F啊啊，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x107,
        (
            "#061F姐姐的家啊。\x01",
            "嘿嘿，有点期待啊⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_68D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69B4")

    ChrTalk(    #398
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "阿加特，奥利维尔。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x106,
        "#051F啊啊，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x104,
        (
            "#031F艾丝蒂尔的家啊……\x01",
            "呵呵呵，真令人期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_69B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A91")

    ChrTalk(    #401
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "阿加特，科洛丝。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x106,
        "#051F啊啊，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x105,
        (
            "#048F艾丝蒂尔的家吗？\x01",
            "呵呵，有点期待呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B6A")

    ChrTalk(    #404
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "阿加特，金先生。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x106,
        "#051F啊啊，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x108,
        (
            "#071F哈哈，看来马上\x01",
            "就要承蒙款待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C4D")

    ChrTalk(    #407
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "提妲，奥利维尔。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x107,
        "#061F嗯，当然可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x104,
        (
            "#031F艾丝蒂尔的家啊……\x01",
            "呵呵呵，真令人期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D2A")

    ChrTalk(    #410
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "提妲，科洛丝。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x107,
        "#061F嗯，当然可以⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x105,
        (
            "#048F艾丝蒂尔的家吗～？\x01",
            "呵呵，有点期待呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E01")

    ChrTalk(    #413
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "#1015F提妲，金先生。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x107,
        "#061F嗯，当然可以⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x108,
        (
            "#071F哈哈，看来马上\x01",
            "就要承蒙款待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6E01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EE4")

    ChrTalk(    #416
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "科洛丝，奥利维尔。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x105,
        "#048F好的，我们陪你去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x104,
        (
            "#031F艾丝蒂尔的家啊……\x01",
            "呵呵，真是期待。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FC1")

    ChrTalk(    #419
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "奥利维尔，金先生。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x104,
        "#031F呵，当然可以啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x108,
        (
            "#071F哈哈，看来马上\x01",
            "就要承蒙款待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709B")

    label("loc_6FC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_709B")

    ChrTalk(    #422
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "#1015F总之先去各条路\x01",
            "调查一下雾的范围……\x02\x03",

            "科洛丝，金先生。\x02\x03",

            "我先回家里看看，\x01",
            "确认一下情况可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x105,
        "#048F好的，我们陪你去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x108,
        (
            "#071F哈哈，看来马上\x01",
            "就要承蒙款待了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709B")


    ChrTalk(    #425
        0x103,
        (
            "#027F接下来……\x01",
            "那么就出发喽。\x02",
        )
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

    # Function_42_6640 end

    def Function_43_70EA(): pass

    label("Function_43_70EA")

    SetChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_43_70EA end

    def Function_44_7124(): pass

    label("Function_44_7124")

    OP_90(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_44_7124 end

    def Function_45_7154(): pass

    label("Function_45_7154")

    OP_90(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_45_7154 end

    def Function_46_7184(): pass

    label("Function_46_7184")

    OP_8E(0xFE, 0xCEAE, 0xFA, 0x70BC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_6F(0xA, 59)
    OP_70(0xA, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    OP_90(0xFE, 0xFFFFFB32, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_46_7184 end

    def Function_47_71DE(): pass

    label("Function_47_71DE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71FE")
    Call(0, 76)
    FadeToBright(0, 0)
    Call(0, 77)

    label("loc_71FE")

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

    def lambda_728E():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_728E)
    Sleep(100)

    def lambda_72AE():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_72AE)
    Sleep(200)

    def lambda_72CE():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_72CE)
    Sleep(100)

    def lambda_72EE():
        OP_90(0xFE, 0x0, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_72EE)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x32)
    Sleep(500)

    ChrTalk(    #426
        0x101,
        "#1004F咦……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(1000)
    Call(0, 50)
    Return()

    # Function_47_71DE end

    def Function_48_7356(): pass

    label("Function_48_7356")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7376")
    Call(0, 76)
    FadeToBright(0, 0)
    Call(0, 77)

    label("loc_7376")

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

    def lambda_7406():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7406)
    Sleep(100)

    def lambda_7426():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7426)
    Sleep(200)

    def lambda_7446():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_7446)
    Sleep(100)

    def lambda_7466():
        OP_90(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7466)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x32)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(1000)
    Call(0, 50)
    Return()

    # Function_48_7356 end

    def Function_49_74B3(): pass

    label("Function_49_74B3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D3")
    Call(0, 76)
    FadeToBright(0, 0)
    Call(0, 77)

    label("loc_74D3")

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

    def lambda_7563():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7563)
    Sleep(100)

    def lambda_7583():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7583)
    Sleep(200)

    def lambda_75A3():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_75A3)
    Sleep(100)

    def lambda_75C3():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_75C3)
    WaitChrThread(0xF9, 0x1)
    OP_22(0x118, 0x0, 0x32)
    Sleep(500)

    ChrTalk(    #427
        0x101,
        "#1004F啊……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(1000)
    Call(0, 50)
    Return()

    # Function_49_74B3 end

    def Function_50_7624(): pass

    label("Function_50_7624")


    ChrTalk(    #428
        0x101,
        (
            "#1011F刚才……\x01",
            "听到铃声了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7677")

    ChrTalk(    #429
        0x107,
        (
            "#061F嗯。\x01",
            "从远方传来的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7742")

    label("loc_7677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76A7")

    ChrTalk(    #430
        0x106,
        (
            "#051F啊啊。\x01",
            "从远方传来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7742")

    label("loc_76A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76DF")

    ChrTalk(    #431
        0x104,
        (
            "#035F呼……\x01",
            "似乎是从远方传来的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7742")

    label("loc_76DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770F")

    ChrTalk(    #432
        0x105,
        (
            "#048F嗯。\x01",
            "从远方传来的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7742")

    label("loc_770F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7742")

    ChrTalk(    #433
        0x108,
        (
            "#070F啊啊。\x01",
            "似乎是从远方传来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7778")

    ChrTalk(    #434
        0x107,
        (
            "#061F呼呼……\x01",
            "相当悦耳的音色呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7847")

    label("loc_7778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77AC")

    ChrTalk(    #435
        0x106,
        (
            "#051F哦……\x01",
            "相当不错的音色啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7847")

    label("loc_77AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77E0")

    ChrTalk(    #436
        0x104,
        (
            "#035F呼……\x01",
            "多么优雅的铃声啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7847")

    label("loc_77E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7816")

    ChrTalk(    #437
        0x105,
        (
            "#048F呼呼……\x01",
            "非常悦耳的音色呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7847")

    label("loc_7816")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7847")

    ChrTalk(    #438
        0x108,
        (
            "#070F嗯……\x01",
            "相当优雅的铃声啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7847")


    ChrTalk(    #439
        0x101,
        (
            "#1001F嗯嗯。\x01",
            "都听得入迷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x103,
        "#023F……………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #441
        0x101,
        (
            "#1015F咦……\x01",
            "怎么了，雪拉姐？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #442
        0x103,
        (
            "#524F啊，不，没什么。\x02\x03",

            "只是音色太悦耳\x01",
            "听得入迷了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x101,
        (
            "#1006F怎么，雪拉姐也会这样啊。\x02\x03",

            "铃声虽然少见\x01",
            "会不会是里农先生的杂货铺\x01",
            "新进的货品呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x103,
        (
            "#026F有可能呢。\x02\x03",

            "#020F先不说这个……\x01",
            "这下雾的产生范围\x01",
            "大概就清楚了。\x02\x03",

            "差不多该回协会了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1006F啊，嗯。\x01",
            "得向爱娜姐报告才行。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_50_7624 end

    def Function_51_7A0D(): pass

    label("Function_51_7A0D")

    EventBegin(0x0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A49")
    Call(0, 76)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)

    label("loc_7A49")

    FadeToDark(0, 0, -1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    SetChrName("")

    AnonymousTalk(    #446
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
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
    OP_43(0x101, 0x1, 0x0, 0x34)
    OP_43(0x103, 0x1, 0x0, 0x2C)
    OP_43(0xF8, 0x1, 0x0, 0x2D)
    OP_43(0xF9, 0x1, 0x0, 0x2E)
    Sleep(2000)

    def lambda_7BC4():
        OP_6D(50680, 250, 28860, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7BC4)

    def lambda_7BDC():
        OP_6C(39000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7BDC)
    WaitChrThread(0xF9, 0x1)
    Sleep(200)

    ChrTalk(    #447
        0x101,
        (
            "#1011F#6P接下来，按照最初的计划\x01",
            "该去柏斯地区了呢。\x02\x03",

            "那是唯一一个\x01",
            "还没有做过实验的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x103,
        (
            "#020F#5P嗯，是啊。\x02\x03",

            "以现状来看，柏斯地区\x01",
            "似乎还没发生什么奇怪的事件。\x02\x03",

            "某种程度上来说，协助\x01",
            "完成洛连特的工作后再去也来得及。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x101,
        (
            "#1006F#6P嗯，明白了。\x02\x03",

            "那把事情都完成以后\x01",
            "就去飞船坪吧。\x02",
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

    # Function_51_7A0D end

    def Function_52_7D2E(): pass

    label("Function_52_7D2E")

    SetChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_52_7D2E end

    def Function_53_7D7C(): pass

    label("Function_53_7D7C")

    EventBegin(0x0)
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
    OP_43(0x8, 0x1, 0x0, 0x36)
    OP_43(0x9, 0x1, 0x0, 0x37)
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_6D(49420, 0, 47770, 0)
    OP_67(0, 12280, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(19000, 0)
    OP_6E(386, 0)
    FadeToBright(1000, 0)
    StopSound(0x0, 0x0, 0x1F40)
    Sleep(8000)

    def lambda_7E49():
        OP_6D(49240, 0, 28690, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7E49)

    def lambda_7E61():
        OP_67(0, 6000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_7E61)

    def lambda_7E79():
        OP_6C(13000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7E79)

    def lambda_7E89():
        OP_6E(401, 10000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_7E89)
    OP_43(0xA, 0x1, 0x0, 0x38)
    OP_43(0xB, 0x1, 0x0, 0x39)
    OP_43(0xC, 0x1, 0x0, 0x3A)
    OP_43(0xD, 0x1, 0x0, 0x3B)
    WaitChrThread(0x1, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0210   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_53_7D7C end

    def Function_54_7ECC(): pass

    label("Function_54_7ECC")

    OP_8E(0xFE, 0xC0F8, 0x0, 0xB3C4, 0x3E8, 0x0)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_7F01")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F3D")
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(400)
    Jump("loc_7F01")

    label("loc_7F3D")

    Return()

    # Function_54_7ECC end

    def Function_55_7F3E(): pass

    label("Function_55_7F3E")

    Sleep(500)
    OP_8E(0xFE, 0xB9C8, 0x0, 0xA104, 0x3E8, 0x0)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_7F78")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FB4")
    OP_8C(0xFE, 180, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(400)
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    Jump("loc_7F78")

    label("loc_7FB4")

    Return()

    # Function_55_7F3E end

    def Function_56_7FB5(): pass

    label("Function_56_7FB5")

    SetChrPos(0xFE, 54290, 250, 28900, 270)
    OP_72(0xA, 0x10)
    OP_70(0xA, 0x3B)
    OP_73(0xA)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC378, 0x0, 0x7800, 0x7D0, 0x0)

    label("loc_8007")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8043")
    OP_8C(0xFE, 315, 400)
    Sleep(400)
    OP_8C(0xFE, 45, 400)
    Sleep(400)
    OP_8C(0xFE, 315, 400)
    Sleep(400)
    OP_8C(0xFE, 225, 400)
    Sleep(400)
    Jump("loc_8007")

    label("loc_8043")

    Return()

    # Function_56_7FB5 end

    def Function_57_8044(): pass

    label("Function_57_8044")

    Sleep(500)
    SetChrPos(0xFE, 43270, 250, 33060, 90)
    OP_72(0x3, 0x10)
    OP_70(0x3, 0x3B)
    OP_73(0x3)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBCFC, 0x0, 0x8340, 0x7D0, 0x0)

    label("loc_809B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_80D7")
    OP_8C(0xFE, 180, 300)
    Sleep(600)
    OP_8C(0xFE, 270, 300)
    Sleep(600)
    OP_8C(0xFE, 0, 300)
    Sleep(600)
    OP_8C(0xFE, 90, 300)
    Sleep(600)
    Jump("loc_809B")

    label("loc_80D7")

    Return()

    # Function_57_8044 end

    def Function_58_80D8(): pass

    label("Function_58_80D8")

    Sleep(4000)
    SetChrPos(0xFE, 43270, 250, 33060, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBA18, 0x0, 0x89EE, 0x7D0, 0x0)

    label("loc_811B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8157")
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 360, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    Jump("loc_811B")

    label("loc_8157")

    Return()

    # Function_58_80D8 end

    def Function_59_8158(): pass

    label("Function_59_8158")

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

    label("loc_81B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_81DA")
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 135, 400)
    Sleep(1000)
    Jump("loc_81B6")

    label("loc_81DA")

    Return()

    # Function_59_8158 end

    def Function_60_81DB(): pass

    label("Function_60_81DB")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SoundLoad(191)
    SoundLoad(180)
    SoundLoad(141)
    OP_D2(0x260221, 0x260226, 0x9)
    OP_D2(0x260220, 0x260225, 0xA)
    SetChrChipByIndex(0x33, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_821E")
    Call(0, 76)
    Call(0, 78)

    label("loc_821E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8352")
    SetChrPos(0x106, 69130, 0, 40270, 135)

    label("loc_8352")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8371")
    SetChrPos(0x108, 69000, 0, 38290, 135)

    label("loc_8371")

    SetChrPos(0x101, 73140, 0, 40470, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83A1")
    SetChrPos(0x103, 74000, 0, 40300, 180)

    label("loc_83A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83C0")
    SetChrPos(0x107, 72170, 0, 40280, 180)

    label("loc_83C0")

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

    def lambda_84CA():
        OP_6C(135000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84CA)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x55)

    def lambda_84F0():
        OP_6D(73060, 500, 34550, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84F0)

    def lambda_8508():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8508)
    OP_43(0x1A, 0x1, 0x0, 0x41)
    OP_43(0x1A, 0x3, 0x0, 0x44)
    Sleep(200)
    OP_43(0x1B, 0x1, 0x0, 0x42)
    OP_43(0x1B, 0x3, 0x0, 0x44)
    Sleep(200)
    OP_43(0x1C, 0x1, 0x0, 0x43)
    OP_43(0x1C, 0x3, 0x0, 0x44)
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
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_22(0xBF, 0x0, 0x64)
    OP_43(0x12, 0x1, 0x0, 0x3D)
    Sleep(1000)
    OP_43(0x13, 0x1, 0x0, 0x3E)
    Sleep(1000)
    OP_43(0x2D, 0x1, 0x0, 0x3F)
    Sleep(1000)
    OP_43(0x2C, 0x1, 0x0, 0x40)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x2C, 0x1)
    OP_82(0x0, 0x2)
    WaitChrThread(0x2D, 0x1)
    OP_8E(0x2D, 0x12264, 0x0, 0x8E4E, 0x7D0, 0x0)

    ChrTalk(    #450
        0x2D,
        (
            "#1P──那么，接下来\x01",
            "请新娘抛捧花。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x2D,
        (
            "#1P未婚的女性\x01",
            "请上前。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87AD():
        OP_6D(72780, 0, 39500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87AD)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_87D7():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_87D7)
    Sleep(100)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_8804():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_8804)
    Sleep(100)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_8831():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_8831)
    Sleep(100)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_885E():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_885E)
    Sleep(100)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_888B():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_888B)
    Sleep(100)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_88B8():
        OP_94(0x0, 0xFE, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_88B8)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #452
        0x35,
        "#4P呀～要开始了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #453
        0x30,
        "年轻的女性",
        "#1P艾娅莉～朝这边扔～～！\x02",
    )

    CloseMessageWindow()
    OP_43(0xE, 0x1, 0x0, 0x56)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89B8")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #454
        0x108,
        (
            "#070F原来如此，还有这样的风俗啊。\x02\x03",

            "#071F哈哈，女孩子们\x01",
            "连眼睛都亮了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #455
        0x102,
        (
            "#1040F某种意义上来说这是\x01",
            "婚礼上最热闹的场面了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A56")

    label("loc_89B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A56")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #456
        0x106,
        (
            "#053F嗯，抛捧花啊……\x02\x03",

            "#555F虽不知道有什么有趣的，\x01",
            "但感觉杀气很重啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #457
        0x102,
        (
            "#1040F某种意义上来说这是\x01",
            "婚礼上最热闹的场面了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A56")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #458
        0x101,
        (
            "#1016F#2P嗯～大家\x01",
            "都鼓足了劲儿呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B8E")
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #459
        0x103,
        (
            "#020F快，艾丝蒂尔。\x01",
            "别磨磨蹭蹭的！\x02\x03",

            "看看风向，\x01",
            "占个好位置哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    SetChrFlags(0x30, 0x40)

    def lambda_8B06():
        OP_94(0x0, 0x30, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_8B06)
    Sleep(200)
    OP_94(0x1, 0x103, 0x10E, 0xC8, 0x7D0, 0x0)
    OP_62(0x103, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x103, 0x30, 400)

    ChrTalk(    #460
        0x103,
        "#024F呼，别挤啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x101,
        "#1019F#2P……哟，很认真啊。\x02",
    )

    CloseMessageWindow()

    def lambda_8B86():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8B86)

    label("loc_8B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C80")

    ChrTalk(    #462
        0x107,
        "#062F#2P（心跳心跳……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #463
        0x101,
        (
            "#1007F#2P我说……\x01",
            "提妲也满是干劲嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x0, 0x107, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #464
        0x107,
        (
            "#062F#2P嗯嗯，湿度５５％……\x01",
            "东南偏东风３．５亚矩。\x02\x03",

            "嗯……\x01",
            "就机率上来说这里最好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x101,
        "#1016F#2P要、要做到这种程度吗……\x02",
    )

    CloseMessageWindow()

    label("loc_8C80")

    OP_8C(0x101, 180, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CE3")

    ChrTalk(    #466
        0x101,
        (
            "#1015F#2P嗯，那么\x01",
            "也算我一份吧。\x02\x03",

            "怎么说\x01",
            "我也是个年轻女孩嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CE3")


    def lambda_8CE9():
        OP_6D(73720, 500, 33120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CE9)
    OP_44(0xE, 0x1)
    Sleep(500)
    OP_8C(0x12, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #467
        0x12,
        (
            "#2P要抛向正后方\x01",
            "可是相当难的哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x12,
        (
            "#2P那么，各位!\x01",
            "要是没接到可别生气哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x12,
        "#2P一～二～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x12,
        "#2P……嘿咻────！！\x02",
    )

    CloseMessageWindow()
    OP_43(0x42, 0x1, 0x0, 0x47)

    def lambda_8DA0():

        label("loc_8DA0")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8DA0")

    QueueWorkItem2(0x101, 1, lambda_8DA0)

    def lambda_8DB1():

        label("loc_8DB1")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8DB1")

    QueueWorkItem2(0x102, 1, lambda_8DB1)

    def lambda_8DC2():

        label("loc_8DC2")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8DC2")

    QueueWorkItem2(0xF8, 1, lambda_8DC2)

    def lambda_8DD3():

        label("loc_8DD3")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8DD3")

    QueueWorkItem2(0xF9, 1, lambda_8DD3)

    def lambda_8DE4():

        label("loc_8DE4")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8DE4")

    QueueWorkItem2(0x35, 1, lambda_8DE4)

    def lambda_8DF5():

        label("loc_8DF5")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8DF5")

    QueueWorkItem2(0x36, 1, lambda_8DF5)

    def lambda_8E06():

        label("loc_8E06")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E06")

    QueueWorkItem2(0x37, 1, lambda_8E06)

    def lambda_8E17():

        label("loc_8E17")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E17")

    QueueWorkItem2(0x38, 1, lambda_8E17)

    def lambda_8E28():

        label("loc_8E28")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E28")

    QueueWorkItem2(0x39, 1, lambda_8E28)

    def lambda_8E39():

        label("loc_8E39")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E39")

    QueueWorkItem2(0x3A, 1, lambda_8E39)

    def lambda_8E4A():

        label("loc_8E4A")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E4A")

    QueueWorkItem2(0x3B, 1, lambda_8E4A)

    def lambda_8E5B():

        label("loc_8E5B")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E5B")

    QueueWorkItem2(0x3C, 1, lambda_8E5B)

    def lambda_8E6C():

        label("loc_8E6C")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E6C")

    QueueWorkItem2(0x3D, 1, lambda_8E6C)

    def lambda_8E7D():

        label("loc_8E7D")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E7D")

    QueueWorkItem2(0x3E, 1, lambda_8E7D)

    def lambda_8E8E():

        label("loc_8E8E")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E8E")

    QueueWorkItem2(0x3F, 1, lambda_8E8E)

    def lambda_8E9F():

        label("loc_8E9F")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8E9F")

    QueueWorkItem2(0x40, 1, lambda_8E9F)

    def lambda_8EB0():

        label("loc_8EB0")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8EB0")

    QueueWorkItem2(0x41, 1, lambda_8EB0)

    def lambda_8EC1():

        label("loc_8EC1")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8EC1")

    QueueWorkItem2(0x13, 1, lambda_8EC1)

    def lambda_8ED2():

        label("loc_8ED2")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8ED2")

    QueueWorkItem2(0x2E, 1, lambda_8ED2)

    def lambda_8EE3():

        label("loc_8EE3")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8EE3")

    QueueWorkItem2(0x2F, 1, lambda_8EE3)

    def lambda_8EF4():

        label("loc_8EF4")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8EF4")

    QueueWorkItem2(0x30, 1, lambda_8EF4)

    def lambda_8F05():

        label("loc_8F05")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F05")

    QueueWorkItem2(0x31, 1, lambda_8F05)

    def lambda_8F16():

        label("loc_8F16")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F16")

    QueueWorkItem2(0x32, 1, lambda_8F16)

    def lambda_8F27():

        label("loc_8F27")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F27")

    QueueWorkItem2(0x11, 1, lambda_8F27)

    def lambda_8F38():

        label("loc_8F38")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F38")

    QueueWorkItem2(0x33, 1, lambda_8F38)

    def lambda_8F49():

        label("loc_8F49")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F49")

    QueueWorkItem2(0x10, 1, lambda_8F49)

    def lambda_8F5A():

        label("loc_8F5A")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F5A")

    QueueWorkItem2(0x2D, 1, lambda_8F5A)

    def lambda_8F6B():

        label("loc_8F6B")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F6B")

    QueueWorkItem2(0x2C, 1, lambda_8F6B)

    def lambda_8F7C():

        label("loc_8F7C")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F7C")

    QueueWorkItem2(0x34, 1, lambda_8F7C)

    def lambda_8F8D():

        label("loc_8F8D")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F8D")

    QueueWorkItem2(0xF, 1, lambda_8F8D)

    def lambda_8F9E():

        label("loc_8F9E")

        TurnDirection(0xFE, 0x42, 400)
        OP_48()
        Jump("loc_8F9E")

    QueueWorkItem2(0xE, 1, lambda_8F9E)
    OP_6D(79220, 3000, 36290, 2000)

    ChrTalk(    #471
        0x35,
        "#2P呀～那边不行～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x37,
        "#2P往哪里抛啊～！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9060")

    ChrTalk(    #473
        0x107,
        "#562F呜呜～好可惜……\x02",
    )

    CloseMessageWindow()

    label("loc_9060")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_908A")

    ChrTalk(    #474
        0x103,
        (
            "#025F唉……\x01",
            "又没接住。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908A")


    ChrTalk(    #475
        0x101,
        (
            "#1007F简、简直就是\x01",
            "往相反的方向飞了去。\x02\x03",

            "有人接得到吗？\x02",
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

    NpcTalk(    #476
        0x29,
        "年轻的女性",
        "#3P请，请问～……\x02",
    )

    CloseMessageWindow()

    def lambda_919F():
        OP_6D(78070, 0, 40000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_919F)

    def lambda_91B7():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_91B7)

    def lambda_91C7():

        label("loc_91C7")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_91C7")

    QueueWorkItem2(0x101, 1, lambda_91C7)

    def lambda_91D8():

        label("loc_91D8")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_91D8")

    QueueWorkItem2(0x102, 1, lambda_91D8)

    def lambda_91E9():

        label("loc_91E9")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_91E9")

    QueueWorkItem2(0xF8, 1, lambda_91E9)

    def lambda_91FA():

        label("loc_91FA")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_91FA")

    QueueWorkItem2(0xF9, 1, lambda_91FA)

    def lambda_920B():

        label("loc_920B")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_920B")

    QueueWorkItem2(0x35, 1, lambda_920B)

    def lambda_921C():

        label("loc_921C")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_921C")

    QueueWorkItem2(0x36, 1, lambda_921C)

    def lambda_922D():

        label("loc_922D")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_922D")

    QueueWorkItem2(0x37, 1, lambda_922D)

    def lambda_923E():

        label("loc_923E")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_923E")

    QueueWorkItem2(0x38, 1, lambda_923E)

    def lambda_924F():

        label("loc_924F")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_924F")

    QueueWorkItem2(0x39, 1, lambda_924F)

    def lambda_9260():

        label("loc_9260")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9260")

    QueueWorkItem2(0x3A, 1, lambda_9260)

    def lambda_9271():

        label("loc_9271")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9271")

    QueueWorkItem2(0x3B, 1, lambda_9271)

    def lambda_9282():

        label("loc_9282")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9282")

    QueueWorkItem2(0x3C, 1, lambda_9282)

    def lambda_9293():

        label("loc_9293")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9293")

    QueueWorkItem2(0x3D, 1, lambda_9293)

    def lambda_92A4():

        label("loc_92A4")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_92A4")

    QueueWorkItem2(0x3E, 1, lambda_92A4)

    def lambda_92B5():

        label("loc_92B5")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_92B5")

    QueueWorkItem2(0x3F, 1, lambda_92B5)

    def lambda_92C6():

        label("loc_92C6")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_92C6")

    QueueWorkItem2(0x40, 1, lambda_92C6)

    def lambda_92D7():

        label("loc_92D7")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_92D7")

    QueueWorkItem2(0x41, 1, lambda_92D7)

    def lambda_92E8():

        label("loc_92E8")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_92E8")

    QueueWorkItem2(0x13, 1, lambda_92E8)

    def lambda_92F9():

        label("loc_92F9")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_92F9")

    QueueWorkItem2(0x2E, 1, lambda_92F9)

    def lambda_930A():

        label("loc_930A")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_930A")

    QueueWorkItem2(0x2F, 1, lambda_930A)

    def lambda_931B():

        label("loc_931B")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_931B")

    QueueWorkItem2(0x30, 1, lambda_931B)

    def lambda_932C():

        label("loc_932C")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_932C")

    QueueWorkItem2(0x31, 1, lambda_932C)

    def lambda_933D():

        label("loc_933D")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_933D")

    QueueWorkItem2(0x32, 1, lambda_933D)

    def lambda_934E():

        label("loc_934E")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_934E")

    QueueWorkItem2(0x11, 1, lambda_934E)

    def lambda_935F():

        label("loc_935F")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_935F")

    QueueWorkItem2(0x33, 1, lambda_935F)

    def lambda_9370():

        label("loc_9370")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9370")

    QueueWorkItem2(0x10, 1, lambda_9370)

    def lambda_9381():

        label("loc_9381")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9381")

    QueueWorkItem2(0x2D, 1, lambda_9381)

    def lambda_9392():

        label("loc_9392")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_9392")

    QueueWorkItem2(0x2C, 1, lambda_9392)

    def lambda_93A3():

        label("loc_93A3")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_93A3")

    QueueWorkItem2(0x34, 1, lambda_93A3)

    def lambda_93B4():

        label("loc_93B4")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_93B4")

    QueueWorkItem2(0xF, 1, lambda_93B4)

    def lambda_93C5():

        label("loc_93C5")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_93C5")

    QueueWorkItem2(0xE, 1, lambda_93C5)

    def lambda_93D6():

        label("loc_93D6")

        TurnDirection(0xFE, 0x29, 400)
        OP_48()
        Jump("loc_93D6")

    QueueWorkItem2(0x12, 1, lambda_93D6)
    ClearChrFlags(0x29, 0x80)
    WaitChrThread(0x101, 0x3)

    def lambda_93F1():
        OP_8E(0xFE, 0x130B0, 0x258, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_93F1)
    OP_8E(0x29, 0x130F6, 0x0, 0x9C40, 0x7D0, 0x0)

    ChrTalk(    #477
        0x29,
        "这、这是什么？这个。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0x29,
        (
            "从天空\x01",
            "掉下来的……\x02",
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
    OP_6D(75450, 0, 37780, 2000)

    ChrTalk(    #479
        0x12,
        "哎呀，你捡到的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x12,
        (
            "那是我抛出的\x01",
            "新娘捧花哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #481
        0x29,
        "啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x13,
        (
            "#2P恭喜你了，小姐。\x01",
            "你一定会结下良缘的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #483
        0x29,
        "怎，怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0x29,
        (
            "怎么办……我……\x01",
            "还，还没有心理准备……\x02",
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

    ChrTalk(    #485
        0x101,
        (
            "#1016F#3P呼，嗯……\x02\x03",

            "感觉是\x01",
            "物归其所了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9669")

    ChrTalk(    #486
        0x103,
        "#025F#1P呼，一点不错……\x02",
    )

    CloseMessageWindow()

    label("loc_9669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96A2")

    ChrTalk(    #487
        0x107,
        (
            "#067F#4P嘿嘿，捧花\x01",
            "说不定正适合她……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96A2")

    OP_6D(73230, 260, 34450, 2000)
    TurnDirection(0x2C, 0x13, 400)
    Sleep(500)

    ChrTalk(    #488
        0x2C,
        "#2P好了──\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0x2C,
        (
            "#2P婚礼进行到这里\x01",
            "也总算结束了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_96FC():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_96FC)

    def lambda_970A():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_970A)

    def lambda_9718():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9718)

    def lambda_9726():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9726)

    def lambda_9734():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9734)

    def lambda_9742():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_9742)

    def lambda_9750():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_9750)

    def lambda_975E():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_975E)

    def lambda_976C():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_976C)

    def lambda_977A():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_977A)

    def lambda_9788():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9788)

    def lambda_9796():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_9796)

    def lambda_97A4():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_97A4)

    def lambda_97B2():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_97B2)

    def lambda_97C0():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_97C0)

    def lambda_97CE():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_97CE)

    def lambda_97DC():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_97DC)

    def lambda_97EA():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_97EA)

    def lambda_97F8():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_97F8)

    def lambda_9806():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_9806)

    def lambda_9814():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_9814)

    def lambda_9822():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_9822)

    def lambda_9830():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_9830)

    def lambda_983E():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_983E)

    def lambda_984C():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_984C)

    def lambda_985A():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_985A)

    def lambda_9868():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_9868)

    def lambda_9876():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_9876)

    def lambda_9884():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_9884)

    def lambda_9892():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9892)

    def lambda_98A0():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_98A0)

    def lambda_98AE():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_98AE)

    def lambda_98BC():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_98BC)
    Sleep(400)

    ChrTalk(    #490
        0x2D,
        (
            "#1P祝愿你们俩\x01",
            "幸福到永远……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x2D, 400)

    ChrTalk(    #491
        0x12,
        "#2P谢谢你，修女。\x02",
    )

    CloseMessageWindow()

    def lambda_990F():
        TurnDirection(0xFE, 0x2C, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_990F)
    TurnDirection(0x13, 0x2C, 400)

    ChrTalk(    #492
        0x13,
        (
            "#1P还有教区长……\x01",
            "今天真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x2C,
        "#2P现在王国的情况很严峻……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x2C,
        (
            "#2P但请不要畏惧任何困难，\x01",
            "努力构筑幸福的家庭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x2C,
        (
            "#2P这就是对出席的人们\x01",
            "最好的回报哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x13,
        "#1P……是，是！\x02",
    )

    CloseMessageWindow()

    def lambda_99E4():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99E4)

    def lambda_99F2():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_99F2)

    def lambda_9A00():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9A00)

    def lambda_9A0E():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_9A0E)

    def lambda_9A1C():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_9A1C)

    def lambda_9A2A():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_9A2A)

    def lambda_9A38():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_9A38)

    def lambda_9A46():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_9A46)

    def lambda_9A54():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9A54)

    def lambda_9A62():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9A62)

    def lambda_9A70():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_9A70)

    def lambda_9A7E():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_9A7E)

    def lambda_9A8C():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_9A8C)

    def lambda_9A9A():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_9A9A)

    def lambda_9AA8():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_9AA8)

    def lambda_9AB6():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_9AB6)

    def lambda_9AC4():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_9AC4)

    def lambda_9AD2():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_9AD2)

    def lambda_9AE0():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_9AE0)

    def lambda_9AEE():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_9AEE)

    def lambda_9AFC():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_9AFC)

    def lambda_9B0A():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_9B0A)

    def lambda_9B18():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9B18)

    def lambda_9B26():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_9B26)

    def lambda_9B34():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9B34)

    def lambda_9B42():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_9B42)

    def lambda_9B50():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_9B50)

    def lambda_9B5E():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9B5E)

    def lambda_9B6C():
        TurnDirection(0x13, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9B6C)
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
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_8C(0x13, 0, 400)
    OP_8C(0x12, 0, 400)
    OP_22(0xBF, 0x0, 0x64)

    def lambda_9D35():
        OP_94(0x1, 0xFE, 0x10E, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9D35)

    def lambda_9D4B():
        OP_94(0x1, 0xFE, 0x5A, 0xC8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9D4B)
    Sleep(500)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x12, 0x40)
    OP_8C(0x13, 270, 400)
    OP_8C(0x12, 90, 400)

    def lambda_9D7E():
        OP_94(0x0, 0xFE, 0x0, 0x96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9D7E)
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
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
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
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
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

    # Function_60_81DB end

    def Function_61_A14E(): pass

    label("Function_61_A14E")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11B0C, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11B0C, 0x1F4, 0x896C, 0x3E8, 0x0)
    Return()

    # Function_61_A14E end

    def Function_62_A190(): pass

    label("Function_62_A190")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11F44, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x11F44, 0x1E0, 0x896C, 0x3E8, 0x0)
    Return()

    # Function_62_A190 end

    def Function_63_A1D2(): pass

    label("Function_63_A1D2")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x1220A, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_63_A1D2 end

    def Function_64_A207(): pass

    label("Function_64_A207")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11CC4, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8E(0xFE, 0x1186E, 0x1F4, 0x870A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_64_A207 end

    def Function_65_A23C(): pass

    label("Function_65_A23C")

    SetChrChipByIndex(0x1A, 11)
    ClearChrFlags(0x1A, 0x400)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x40)
    OP_98(0x0, 0x1A)
    OP_98(0x1, 0x11BA2, 0x1B58, 0x9132)
    OP_98(0x1, 0x16C10, 0x1F40, 0x97F4)
    OP_43(0xFE, 0x2, 0x0, 0x46)
    OP_98(0x2, 0x1A, 0x157C, 0x2)
    Return()

    # Function_65_A23C end

    def Function_66_A281(): pass

    label("Function_66_A281")

    SetChrChipByIndex(0x1B, 11)
    ClearChrFlags(0x1B, 0x400)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x40)
    OP_98(0x0, 0x1B)
    OP_98(0x1, 0x10D88, 0x1B58, 0x91DC)
    OP_98(0x1, 0x16C10, 0x1388, 0x9BDC)
    OP_43(0xFE, 0x2, 0x0, 0x46)
    OP_98(0x2, 0x1B, 0x157C, 0x2)
    Return()

    # Function_66_A281 end

    def Function_67_A2C6(): pass

    label("Function_67_A2C6")

    SetChrChipByIndex(0x1C, 11)
    ClearChrFlags(0x1C, 0x400)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x40)
    OP_98(0x0, 0x1C)
    OP_98(0x1, 0x109A0, 0x2328, 0x9D94)
    OP_98(0x1, 0x16C10, 0x1F40, 0x940C)
    OP_43(0xFE, 0x2, 0x0, 0x46)
    OP_98(0x2, 0x1C, 0x157C, 0x2)
    Return()

    # Function_67_A2C6 end

    def Function_68_A30B(): pass

    label("Function_68_A30B")

    Sleep(800)
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(4000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Return()

    # Function_68_A30B end

    def Function_69_A32C(): pass

    label("Function_69_A32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A364")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A35C")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_A364")

    label("loc_A35C")

    Sleep(15)
    Jump("Function_69_A32C")

    label("loc_A364")

    Return()

    # Function_69_A32C end

    def Function_70_A365(): pass

    label("Function_70_A365")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A37A")
    OP_99(0xFE, 0x0, 0x7, 0x1770)
    Jump("Function_70_A365")

    label("loc_A37A")

    Return()

    # Function_70_A365 end

    def Function_71_A37B(): pass

    label("Function_71_A37B")

    ClearChrFlags(0x42, 0x80)
    OP_22(0xCB, 0x0, 0x64)
    OP_98(0x0, 0x42)
    OP_98(0x1, 0x12AF2, 0x2710, 0x8D54)
    OP_98(0x1, 0x13A42, 0x1F40, 0x8DCC)
    OP_98(0x1, 0x150A4, 0x0, 0x9CFE)
    OP_98(0x2, 0x42, 0x157C, 0x2)
    Return()

    # Function_71_A37B end

    def Function_72_A3BD(): pass

    label("Function_72_A3BD")

    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_A453")
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #497
        0xE,
        (
            "啊～！？\x01",
            "艾丝蒂尔和约修亚！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(    #498
        0xF,
        (
            "啊，姐姐和哥哥。\x02\x03",

            "你们回来了。\x01",
            "今天两人在一起呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4D7")

    label("loc_A453")

    TurnDirection(0xF, 0x101, 0)

    ChrTalk(    #499
        0xF,
        (
            "啊……！？\x02\x03",

            "艾丝蒂尔姐姐\x01",
            "和约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x102, 400)
    Sleep(1000)

    ChrTalk(    #500
        0xE,
        (
            "啊～！？约修亚！！\x02\x03",

            "终于回来啦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    label("loc_A4D7")


    ChrTalk(    #501
        0x101,
        "#1001F嗯，不容易呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 400)

    ChrTalk(    #502
        0x102,
        (
            "#1040F好久没见你们俩了。\x02\x03",

            "哈哈，还是\x01",
            "那么活泼的样子嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 400)

    ChrTalk(    #503
        0xE,
        (
            "嘿嘿，当然喽。\x02\x03",

            "艾丝蒂尔你们\x01",
            "今天也要工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0xF,
        (
            "是不是导力器\x01",
            "停止事件的调查？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xF, 400)

    ChrTalk(    #505
        0x102,
        (
            "#1040F嗯，是在干这个呢。\x02\x03",

            "虽说这问题\x01",
            "一时半刻是解决不了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xE,
        (
            "唉～好无聊。\x02\x03",

            "那还不如去调查\x01",
            "那个浮在空中的岛呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A72F")

    ChrTalk(    #507
        0x101,
        (
            "#1007F要能那么做\x01",
            "早就去做了啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 400)

    ChrTalk(    #508
        0x102,
        (
            "#1042F现在街道的灯都熄灭了，\x01",
            "城外边非常危险。\x02\x03",

            "鲁克你们\x01",
            "也不能到街道上去哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 400)

    ChrTalk(    #509
        0xE,
        (
            "嘿嘿，这个\x01",
            "我还是知道的啦。\x02\x03",

            "唉，虽然有点可惜，\x01",
            "今天就在城中一日游吧！\x02\x03",

            "好！走吧帕特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0xF,
        (
            "嗯、嗯……\x02\x03",

            "哥哥姐姐。\x01",
            "那么，回头见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84E")

    label("loc_A72F")


    ChrTalk(    #511
        0x101,
        (
            "#1007F要能那么做\x01",
            "早就去做了啦。\x02\x03",

            "导力器不能用了，\x01",
            "你们也知道吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x102,
        (
            "#1042F现在街道的灯都熄灭了，\x01",
            "城外是很危险的状态。\x02\x03",

            "鲁克你们\x01",
            "也不能到街道上去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xE,
        (
            "嘿嘿，这个\x01",
            "我还是知道的啦。\x02\x03",

            "唉，虽然有点可惜，\x01",
            "今天就忍忍待在城里面吧！\x02\x03",

            "好！走吧帕特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0xF,
        (
            "嗯！\x02\x03",

            "那么，哥哥姐姐。\x01",
            "回头见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A84E")

    OP_8C(0xE, 90, 400)
    OP_8C(0xF, 270, 400)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_A2(0x17)
    OP_A2(0x16)
    OP_A2(0x20A0)
    Return()

    # Function_72_A3BD end

    def Function_73_A86E(): pass

    label("Function_73_A86E")

    TalkBegin(0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AB25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8E")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(1000)

    ChrTalk(    #515
        0xFE,
        (
            "哟，艾丝蒂尔啊……\x01",
            "这，这不是约修亚吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0x102,
        "#1035F好久不见了，菲特先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        (
            "哟，才多久没见啊，\x01",
            "就完全长成个男子汉了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0xFE,
        (
            "呀，这我就放心了。\x01",
            "和艾丝蒂尔在游击士的道路上都\x01",
            "做得很漂亮嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x102,
        "#1040F这都是托您的福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0xFE,
        (
            "看来王国中\x01",
            "好像发生了严重的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0xFE,
        (
            "回归军队的卡西乌斯\x01",
            "也忙得不可开交吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #522
        0xFE,
        (
            "作为游击士的你们两个\x01",
            "可要努力，不能输给他哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0x101,
        (
            "#1006F嗯！\x01",
            "我们会尽全力完成工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x102,
        (
            "#1040F有什么困难\x01",
            "就联系协会吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #525
        0xFE,
        (
            "我会的。\x01",
            "那么，两人都要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    OP_A2(0x209B)
    Jump("loc_AB25")

    label("loc_AA8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_AAD1")

    ChrTalk(    #526
        0xFE,
        (
            "有什么事我\x01",
            "会联络协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0xFE,
        "那么，两人都要小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB25")

    label("loc_AAD1")


    ChrTalk(    #528
        0xFE,
        (
            "今天早上起来的时候\x01",
            "发现导力灯打不开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0xFE,
        (
            "总之先想办法\x01",
            "把照明问题解决了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB25")

    TalkEnd(0x46)
    Return()

    # Function_73_A86E end

    def Function_74_AB29(): pass

    label("Function_74_AB29")

    TalkBegin(0x47)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_ABAE")

    ChrTalk(    #530
        0xFE,
        (
            "虽然导力器停止了，\x01",
            "洛连特的人们还是挺悠然的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0xFE,
        (
            "不过，单是慌张也于事无补。 \x01",
            "或许这种态度倒是应该大家仿效的。 \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC0A")

    label("loc_ABAE")


    ChrTalk(    #532
        0xFE,
        (
            "本打算看看传闻中的浮游岛\x01",
            "就从旅馆走出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0xFE,
        (
            "嗯～从这里看过去\x01",
            "视野很差看不太清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC0A")

    TalkEnd(0x47)
    Return()

    # Function_74_AB29 end

    def Function_75_AC0E(): pass

    label("Function_75_AC0E")

    TalkBegin(0x48)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_AC6D")

    ChrTalk(    #534
        0xFE,
        (
            "定期船要修复\x01",
            "看来还有得等呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #535
        0xFE,
        (
            "只要有浮游岛在\x01",
            "可能就恢复不了也说不定……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACBD")

    label("loc_AC6D")


    ChrTalk(    #536
        0xFE,
        (
            "从钟楼上\x01",
            "好像能清楚看到浮游岛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0xFE,
        (
            "连洛连特都看得到，\x01",
            "到底有多大呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACBD")

    TalkEnd(0x48)
    Return()

    # Function_75_AC0E end

    def Function_76_ACC1(): pass

    label("Function_76_ACC1")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AD3E"),
        (1, "loc_AD44"),
        (SWITCH_DEFAULT, "loc_AD4A"),
    )


    label("loc_AD3E")

    OP_A2(0x1200)
    Jump("loc_AD4A")

    label("loc_AD44")

    OP_A2(0x1201)
    Jump("loc_AD4A")

    label("loc_AD4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AD58")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_AD5C")

    label("loc_AD58")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_AD5C")

    Return()

    # Function_76_ACC1 end

    def Function_77_AD5D(): pass

    label("Function_77_AD5D")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_77_AD5D end

    def Function_78_ADAF(): pass

    label("Function_78_ADAF")

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

    # Function_78_ADAF end

    def Function_79_AE08(): pass

    label("Function_79_AE08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE8A")
    EventBegin(0x1)

    ChrTalk(    #538
        0x101,
        (
            "#505F……这边是反方向吧。\x01",
            "得早点回家才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x142, 0x0, 400)

    ChrTalk(    #539
        0x142,
        (
            "#1060F这么说\x01",
            "是从南门出去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_B069")

    label("loc_AE8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFC7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEAE")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_AEB5")

    label("loc_AEAE")

    TurnDirection(0x103, 0x0, 400)

    label("loc_AEB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_AEF3")

    ChrTalk(    #540
        0x103,
        (
            "#020F虽然也担心外面的情况，\x01",
            "但还是先去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFA9")

    label("loc_AEF3")


    ChrTalk(    #541
        0x103,
        (
            "#020F虽然也担心外面的情况，\x01",
            "但还是先去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF53")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #542
        0x101,
        "#1000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_AF53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF7E")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #543
        0x105,
        "#040F嗯，是呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_AF7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFA9")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #544
        0x107,
        "#060F啊，是哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_AFA9")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_B069")

    label("loc_AFC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B069")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B021")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #545
        0x103,
        (
            "#020F现在不是到处跑的时候。\x01",
            "先得去协会报告才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B04E")

    label("loc_B021")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #546
        0x103,
        (
            "#020F去哪里？\x01",
            "先得去协会报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B04E")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_B069")

    Return()

    # Function_79_AE08 end

    def Function_80_B06A(): pass

    label("Function_80_B06A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0EA")
    EventBegin(0x1)

    ChrTalk(    #547
        0x101,
        (
            "#000F约修亚一定\x01",
            "已经回家了哦。\x02\x03",

            "早点去家里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0x142,
        "#1063F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_B224")

    label("loc_B0EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B224")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B10E")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_B115")

    label("loc_B10E")

    TurnDirection(0x103, 0x0, 400)

    label("loc_B115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_B153")

    ChrTalk(    #549
        0x103,
        (
            "#020F虽然也担心外面的情况，\x01",
            "但还是先去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B209")

    label("loc_B153")


    ChrTalk(    #550
        0x103,
        (
            "#020F虽然也担心外面的情况，\x01",
            "但还是先去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1B3")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #551
        0x101,
        "#1000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_B1B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1DE")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #552
        0x105,
        "#040F嗯，是呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_B1DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B209")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #553
        0x107,
        "#060F啊，是哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_B209")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_B224")

    Return()

    # Function_80_B06A end

    def Function_81_B225(): pass

    label("Function_81_B225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2C7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B27F")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #554
        0x103,
        (
            "#020F现在不是到处跑的时候。\x01",
            "先得去协会报告才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2AC")

    label("loc_B27F")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #555
        0x103,
        (
            "#020F去哪儿？\x01",
            "先得去协会报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2AC")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_B2C7")

    Return()

    # Function_81_B225 end

    def Function_82_B2C8(): pass

    label("Function_82_B2C8")

    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #556
        (
            "\x07\x05『七耀历１０７５年』\x01",
            "　由利贝尔王室、七耀教会\x01",
            "　以及洛连特市共同建造。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #557
        (
            "\x07\x05『七耀历１１９２年』\x01",
            "　百日战役中，被围攻洛连特的\x01",
            "　埃雷波尼亚帝国军队炮击而倒塌。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #558
        (
            "\x07\x05『七耀历１１９７年』\x01",
            "　在市民的协力下得以重建。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_82_B2C8 end

    def Function_83_B3CC(): pass

    label("Function_83_B3CC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #559
        "\x07\x05西　玛鲁加山道一侧出口\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_83_B3CC end

    def Function_84_B415(): pass

    label("Function_84_B415")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #560
        "\x07\x05北　洛连特飞船坪\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_84_B415 end

    def Function_85_B458(): pass

    label("Function_85_B458")

    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Sleep(2500)
    OP_22(0xB4, 0x0, 0x64)
    Return()

    # Function_85_B458 end

    def Function_86_B47C(): pass

    label("Function_86_B47C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B503")
    OP_62(0x30, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x37, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x40, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x41, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)
    Jump("Function_86_B47C")

    label("loc_B503")

    Return()

    # Function_86_B47C end

    def Function_87_B504(): pass

    label("Function_87_B504")

    SetPlaceName(0x4)
    Return()

    # Function_87_B504 end

    def Function_88_B508(): pass

    label("Function_88_B508")

    SetPlaceName(0x2)
    Return()

    # Function_88_B508 end

    def Function_89_B50C(): pass

    label("Function_89_B50C")

    SetPlaceName(0x6)
    Return()

    # Function_89_B50C end

    def Function_90_B510(): pass

    label("Function_90_B510")

    SetPlaceName(0x5)
    Return()

    # Function_90_B510 end

    def Function_91_B514(): pass

    label("Function_91_B514")

    SetPlaceName(0x7)
    Return()

    # Function_91_B514 end

    def Function_92_B518(): pass

    label("Function_92_B518")

    SetPlaceName(0x8)
    Return()

    # Function_92_B518 end

    def Function_93_B51C(): pass

    label("Function_93_B51C")

    SetPlaceName(0x3)
    Return()

    # Function_93_B51C end

    def Function_94_B520(): pass

    label("Function_94_B520")

    SetPlaceName(0xA)
    Return()

    # Function_94_B520 end

    SaveToFile()

Try(main)
