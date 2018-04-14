from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
            'ED6_DT21/T4101_1 ._SN',
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
        '士兵达克特',                           # 9
        '士兵贝尔坎',                           # 10
        '娜碧',                                 # 11
        '米亚尔',                               # 12
        '戈万',                                 # 13
        '帕菲',                                 # 14
        '娜娜',                                 # 15
        '安敦',                                 # 16
        '利库斯',                               # 17
        '索露贝',                               # 18
        '卡拉莉丝',                             # 19
        '尼莫',                                 # 20
        '吉米',                                 # 21
        '拉奥尼',                               # 22
        '梅夏',                                 # 23
        '维尔娜婆婆',                           # 24
        '王国军士兵',                           # 25
        '王国军士兵',                           # 26
        '王国军士兵',                           # 27
        '玲',                                   # 28
        '提妲',                                 # 29
        '游客',                                 # 30
        '游客',                                 # 31
        '贝利',                                 # 32
        '旅行者',                               # 33
        '游客',                                 # 34
        '游客',                                 # 35
        '王国军士兵',                           # 36
        '莉西娅',                               # 37
        '格斯塔夫维修长',                       # 38
        '菲',                                   # 39
        '运输车',                               # 40
        '凯诺娜',                               # 41
        '特务兵',                               # 42
        '特务兵',                               # 43
        '特务兵',                               # 44
        '特务兵',                               # 45
        '特务兵',                               # 46
        '特务兵',                               # 47
        '特务兵',                               # 48
        '特务兵',                               # 49
        '特务兵',                               # 50
        '特务兵',                               # 51
        '特务兵',                               # 52
        '特务兵',                               # 53
        '特务兵',                               # 54
        '特务兵',                               # 55
        '特务兵',                               # 56
        '特务兵',                               # 57
        '强化猎兵',                             # 58
        '强化猎兵',                             # 59
        '强化猎兵',                             # 60
        '强化猎兵',                             # 61
        '强化猎兵',                             # 62
        '强化猎兵',                             # 63
        '强化猎兵',                             # 64
        '强化猎兵',                             # 65
        '强化猎兵',                             # 66
        '强化猎兵',                             # 67
        '亡命守护者',                           # 68
        '亡命守护者',                           # 69
        '装甲猎豹',                             # 70
        '装甲猎豹',                             # 71
        '奈尔',                                 # 72
        '朵洛希',                               # 73
        '士兵',                                 # 74
        '士兵',                                 # 75
        '士兵',                                 # 76
        '士兵',                                 # 77
        '王都格兰赛尔·北街区',                 # 78
        '王都格兰赛尔·南街区',                 # 79
        '王都格兰赛尔·空港',                   # 80
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
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02440 ._CH',             # 03
        'ED6_DT26/CH20304 ._CH',             # 04
        'ED6_DT07/CH01470 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH02480 ._CH',             # 09
        'ED6_DT07/CH02490 ._CH',             # 0A
        'ED6_DT07/CH01143 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT07/CH01110 ._CH',             # 0E
        'ED6_DT07/CH01680 ._CH',             # 0F
        'ED6_DT07/CH01690 ._CH',             # 10
        'ED6_DT07/CH01050 ._CH',             # 11
        'ED6_DT07/CH01490 ._CH',             # 12
        'ED6_DT07/CH01153 ._CH',             # 13
        'ED6_DT07/CH01030 ._CH',             # 14
        'ED6_DT27/CH03510 ._CH',             # 15
        'ED6_DT27/CH03060 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02440P._CP',             # 03
        'ED6_DT26/CH20304P._CP',             # 04
        'ED6_DT07/CH01470P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH02480P._CP',             # 09
        'ED6_DT07/CH02490P._CP',             # 0A
        'ED6_DT07/CH01143P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT07/CH01110P._CP',             # 0E
        'ED6_DT07/CH01680P._CP',             # 0F
        'ED6_DT07/CH01690P._CP',             # 10
        'ED6_DT07/CH01050P._CP',             # 11
        'ED6_DT07/CH01490P._CP',             # 12
        'ED6_DT07/CH01153P._CP',             # 13
        'ED6_DT07/CH01030P._CP',             # 14
        'ED6_DT27/CH03510P._CP',             # 15
        'ED6_DT27/CH03060P._CP',             # 16
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 74970,
        Z                   = 0,
        Y                   = 71250,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 100180,
        Z                   = 250,
        Y                   = 33080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 46290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 44530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 46260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 47860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 70490,
        Z                   = 250,
        Y                   = 6990,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 71500,
        Z                   = 750,
        Y                   = 7870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 1250,
        Y                   = 49800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = 250,
        Y                   = 49340,
        Direction           = 227,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 49630,
        Z                   = 0,
        Y                   = 61870,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 50410,
        Z                   = 0,
        Y                   = 81110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 81160,
        Z                   = 0,
        Y                   = -2940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 69020,
        Z                   = 250,
        Y                   = 4960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 63010,
        Z                   = 0,
        Y                   = 62930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 93700,
        Z                   = 0,
        Y                   = 32900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 53830,
        Z                   = 250,
        Y                   = 24100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 54040,
        Z                   = 250,
        Y                   = 8750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 42240,
        Z                   = 1250,
        Y                   = 51400,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 41280,
        Z                   = 1250,
        Y                   = 52380,
        Direction           = 146,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 76500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 77950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 69930,
        Z                   = 250,
        Y                   = 67560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 49030,
        Z                   = 0,
        Y                   = -3820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 73950,
        Z                   = 250,
        Y                   = 44280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 47630,
        Z                   = 250,
        Y                   = 29460,
        Direction           = 257,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 124170,
        Z                   = -3500,
        Y                   = 72870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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
        NpcIndex            = 0x1A0,
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


    DeclEvent(
        X                   = 42000,
        Y                   = -2000,
        Z                   = 71500,
        Range               = 59000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x122A0,
        Unknown_18          = 0x0,
        Unknown_1C          = 48,
    )

    DeclEvent(
        X                   = 109720,
        Y                   = 1000,
        Z                   = 32980,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 103,
    )

    DeclEvent(
        X                   = 76740,
        Y                   = 1000,
        Z                   = 23010,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 104,
    )

    DeclEvent(
        X                   = 69950,
        Y                   = 1000,
        Z                   = 14290,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 104,
    )

    DeclEvent(
        X                   = 63260,
        Y                   = 1000,
        Z                   = 22960,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 104,
    )

    DeclEvent(
        X                   = 69910,
        Y                   = 1000,
        Z                   = 31710,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 104,
    )

    DeclEvent(
        X                   = 42920,
        Y                   = 0,
        Z                   = 81110,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 105,
    )

    DeclEvent(
        X                   = 70940,
        Y                   = 0,
        Z                   = -9490,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 106,
    )

    DeclEvent(
        X                   = 75010,
        Y                   = 0,
        Z                   = 71300,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 107,
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
        TalkFunctionIndex   = 101,
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
        TalkFunctionIndex   = 102,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_BCA",          # 00, 0
        "Function_1_F34",          # 01, 1
        "Function_2_114A",         # 02, 2
        "Function_3_116E",         # 03, 3
        "Function_4_125B",         # 04, 4
        "Function_5_1308",         # 05, 5
        "Function_6_1441",         # 06, 6
        "Function_7_14E6",         # 07, 7
        "Function_8_15EB",         # 08, 8
        "Function_9_16F0",         # 09, 9
        "Function_10_20A8",        # 0A, 10
        "Function_11_2A08",        # 0B, 11
        "Function_12_2C0B",        # 0C, 12
        "Function_13_2EB9",        # 0D, 13
        "Function_14_3158",        # 0E, 14
        "Function_15_32B8",        # 0F, 15
        "Function_16_3444",        # 10, 16
        "Function_17_36E0",        # 11, 17
        "Function_18_3876",        # 12, 18
        "Function_19_3CEF",        # 13, 19
        "Function_20_3DE0",        # 14, 20
        "Function_21_3FB1",        # 15, 21
        "Function_22_4292",        # 16, 22
        "Function_23_4537",        # 17, 23
        "Function_24_47C0",        # 18, 24
        "Function_25_4A92",        # 19, 25
        "Function_26_4B6A",        # 1A, 26
        "Function_27_4C49",        # 1B, 27
        "Function_28_4D52",        # 1C, 28
        "Function_29_4E77",        # 1D, 29
        "Function_30_4FA8",        # 1E, 30
        "Function_31_512D",        # 1F, 31
        "Function_32_5276",        # 20, 32
        "Function_33_53B0",        # 21, 33
        "Function_34_5548",        # 22, 34
        "Function_35_5928",        # 23, 35
        "Function_36_5F0B",        # 24, 36
        "Function_37_6561",        # 25, 37
        "Function_38_6FE5",        # 26, 38
        "Function_39_7444",        # 27, 39
        "Function_40_74F9",        # 28, 40
        "Function_41_75AE",        # 29, 41
        "Function_42_7663",        # 2A, 42
        "Function_43_7718",        # 2B, 43
        "Function_44_7D18",        # 2C, 44
        "Function_45_7D3D",        # 2D, 45
        "Function_46_7D62",        # 2E, 46
        "Function_47_7D99",        # 2F, 47
        "Function_48_821E",        # 30, 48
        "Function_49_927B",        # 31, 49
        "Function_50_9297",        # 32, 50
        "Function_51_92B3",        # 33, 51
        "Function_52_92CF",        # 34, 52
        "Function_53_92EB",        # 35, 53
        "Function_54_932F",        # 36, 54
        "Function_55_9377",        # 37, 55
        "Function_56_BAD1",        # 38, 56
        "Function_57_BB0A",        # 39, 57
        "Function_58_BB43",        # 3A, 58
        "Function_59_BC00",        # 3B, 59
        "Function_60_BCBE",        # 3C, 60
        "Function_61_BD4D",        # 3D, 61
        "Function_62_BE04",        # 3E, 62
        "Function_63_BEC9",        # 3F, 63
        "Function_64_BF87",        # 40, 64
        "Function_65_C005",        # 41, 65
        "Function_66_C0AB",        # 42, 66
        "Function_67_C1C9",        # 43, 67
        "Function_68_C2E7",        # 44, 68
        "Function_69_C405",        # 45, 69
        "Function_70_C433",        # 46, 70
        "Function_71_C461",        # 47, 71
        "Function_72_C4A3",        # 48, 72
        "Function_73_C4E5",        # 49, 73
        "Function_74_C527",        # 4A, 74
        "Function_75_C569",        # 4B, 75
        "Function_76_C5AB",        # 4C, 76
        "Function_77_C5F7",        # 4D, 77
        "Function_78_C634",        # 4E, 78
        "Function_79_C7B9",        # 4F, 79
        "Function_80_C891",        # 50, 80
        "Function_81_C962",        # 51, 81
        "Function_82_C9EF",        # 52, 82
        "Function_83_CA7C",        # 53, 83
        "Function_84_CBAB",        # 54, 84
        "Function_85_CDC6",        # 55, 85
        "Function_86_CE4F",        # 56, 86
        "Function_87_CF37",        # 57, 87
        "Function_88_D2B1",        # 58, 88
        "Function_89_D4FE",        # 59, 89
        "Function_90_D71E",        # 5A, 90
        "Function_91_D945",        # 5B, 91
        "Function_92_DB6C",        # 5C, 92
        "Function_93_DC3A",        # 5D, 93
        "Function_94_DCB1",        # 5E, 94
        "Function_95_DD28",        # 5F, 95
        "Function_96_DDB6",        # 60, 96
        "Function_97_DE44",        # 61, 97
        "Function_98_DE68",        # 62, 98
        "Function_99_DE8E",        # 63, 99
        "Function_100_DF2A",       # 64, 100
        "Function_101_DFB4",       # 65, 101
        "Function_102_E016",       # 66, 102
        "Function_103_E05C",       # 67, 103
        "Function_104_E060",       # 68, 104
        "Function_105_E064",       # 69, 105
        "Function_106_E068",       # 6A, 106
        "Function_107_E06C",       # 6B, 107
        "Function_108_E070",       # 6C, 108
    )


    def Function_0_BCA(): pass

    label("Function_0_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BFC")
    SetChrPos(0x9, 77220, 250, 71250, 180)
    SetChrPos(0x13, 47790, 250, 48080, 37)
    SetChrFlags(0x13, 0x10)

    label("loc_BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C18")
    SetChrPos(0x8, 68770, 250, -9000, 0)

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C40")
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    Jump("loc_E61")

    label("loc_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_CA2")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x13, 47790, 250, 48080, 37)
    SetChrPos(0x1D, 47840, 250, 78050, 2)
    SetChrPos(0x1E, 47840, 250, 79500, 180)
    SetChrPos(0x22, 42990, 1250, 52970, 29)
    SetChrFlags(0x1D, 0x10)
    Jump("loc_E61")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D06")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x13, 49630, 0, 61870, 45)
    SetChrPos(0x1D, 53310, 250, 72710, 324)
    SetChrPos(0x1E, 53180, 250, 74370, 320)
    SetChrPos(0x1F, 60880, 250, 67010, 180)
    SetChrPos(0x22, 53110, 250, 8150, 273)
    Jump("loc_E61")

    label("loc_D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA0")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrPos(0x13, 49630, 0, 61870, 45)
    SetChrPos(0x1D, 53140, 250, 23270, 180)
    SetChrPos(0x1E, 53500, 250, 22190, 315)
    SetChrPos(0x1F, 71900, 250, 60850, 9)
    SetChrPos(0x22, 56200, 250, 26240, 252)
    SetChrPos(0x23, 124210, -3500, 70990, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9D")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_D9D")

    Jump("loc_E61")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E0E")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrPos(0x13, 47790, 250, 48080, 37)
    SetChrPos(0x1D, 93990, 0, 34340, 180)
    SetChrPos(0x1E, 93990, 0, 32670, 0)
    SetChrPos(0x22, 39640, 1250, 51520, 221)
    SetChrPos(0x23, 124210, -3500, 70990, 270)
    Jump("loc_E61")

    label("loc_E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E61")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x1D, 107750, 1250, 32920, 93)
    SetChrPos(0x1E, 109710, 1650, 31920, 75)
    SetChrPos(0x23, 124210, -3500, 70990, 270)

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_E77")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_F33")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_E8D")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 43)
    Jump("loc_F33")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_F0F")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Event(0, 55)
    Jump("loc_F33")

    label("loc_F0F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_F1B"),
        (SWITCH_DEFAULT, "loc_F33"),
    )


    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F30")
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_F30")

    Jump("loc_F33")

    label("loc_F33")

    Return()

    # Function_0_BCA end

    def Function_1_F34(): pass

    label("Function_1_F34")

    OP_16(0x2, 0xFA0, 0xFFFF4C50, 0xFFFEA070, 0x23005C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F66")
    OP_B1("t4101_y")
    Jump("loc_F6F")

    label("loc_F66")

    OP_B1("t4101_n")

    label("loc_F6F")

    OP_71(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F89")
    OP_10(0xC, 0x1)
    OP_10(0xB, 0x0)
    Jump("loc_F9F")

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_F99")
    OP_10(0xC, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_F9F")

    label("loc_F99")

    OP_10(0xB, 0x0)
    OP_10(0xC, 0x1)

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FAE")
    OP_71(0x9, 0x10)
    Jump("loc_1005")

    label("loc_FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_FC4")
    OP_71(0x9, 0x10)
    Jump("loc_FC9")

    label("loc_FC4")

    OP_72(0x9, 0x10)

    label("loc_FC9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_FD5"),
        (SWITCH_DEFAULT, "loc_FEE"),
    )


    label("loc_FD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEE")
    OP_71(0x9, 0x10)
    OP_A2(0x5)
    Jump("loc_FEE")

    label("loc_FEE")

    Jump("loc_1005")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 7)), scpexpr(EXPR_END)), "loc_1000")
    OP_71(0x9, 0x10)
    Jump("loc_1005")

    label("loc_1000")

    OP_72(0x9, 0x10)

    label("loc_1005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1014")
    OP_71(0xA, 0x10)
    Jump("loc_106B")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1057")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_102A")
    OP_71(0xA, 0x10)
    Jump("loc_102F")

    label("loc_102A")

    OP_72(0xA, 0x10)

    label("loc_102F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_103B"),
        (SWITCH_DEFAULT, "loc_1054"),
    )


    label("loc_103B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1054")
    OP_71(0xA, 0x10)
    OP_A2(0x3)
    Jump("loc_1054")

    label("loc_1054")

    Jump("loc_106B")

    label("loc_1057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 3)), scpexpr(EXPR_END)), "loc_1066")
    OP_71(0xA, 0x10)
    Jump("loc_106B")

    label("loc_1066")

    OP_72(0xA, 0x10)

    label("loc_106B")

    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x7, 0x10)
    OP_72(0x8, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C3")
    OP_71(0x5, 0x10)
    OP_71(0x6, 0x10)
    OP_71(0x7, 0x10)
    OP_71(0x8, 0x10)
    OP_1C(0x5, 0x1, 0x4)
    OP_1C(0x6, 0x1, 0x3)
    OP_1C(0x7, 0x1, 0x3)
    OP_1C(0x8, 0x1, 0x5)

    label("loc_10C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F2")
    OP_71(0x5, 0x10)
    OP_71(0x6, 0x10)
    OP_71(0x7, 0x10)
    OP_71(0x8, 0x10)

    label("loc_10F2")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1103")
    OP_72(0xB, 0x10)

    label("loc_1103")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113F")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 59)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 59)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 59)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 59)

    label("loc_113F")

    OP_1C(0xA, 0x0, 0x6C)
    OP_1C(0x9, 0x0, 0x6C)
    Return()

    # Function_1_F34 end

    def Function_2_114A(): pass

    label("Function_2_114A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_116D")
    OP_8D(0xFE, 102900, 37500, 97550, 28500, 2000)
    Jump("Function_2_114A")

    label("loc_116D")

    Return()

    # Function_2_114A end

    def Function_3_116E(): pass

    label("Function_3_116E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_125A")
    OP_8E(0xFE, 0xCCF6, 0x0, 0xFFFFF484, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0x8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0xF32A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCFE4, 0x0, 0x100A4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15AC2, 0x0, 0xFCBC, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16314, 0x0, 0xFB86, 0x9C4, 0x0)
    OP_8E(0xFE, 0x164E0, 0x0, 0x826E, 0x9C4, 0x0)
    OP_8C(0x15, 90, 400)
    Sleep(4000)
    OP_8E(0xFE, 0x164E0, 0x0, 0x7E86, 0x9C4, 0x0)
    OP_8C(0x15, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x16152, 0x0, 0x4CE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15B12, 0x0, 0xFFFFF8BC, 0x9C4, 0x0)
    Jump("Function_3_116E")

    label("loc_125A")

    Return()

    # Function_3_116E end

    def Function_4_125B(): pass

    label("Function_4_125B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1307")
    OP_8E(0xFE, 0xCE9A, 0x0, 0xF5D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0xF258, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0x816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCEEA, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15590, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0x6B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0xEF56, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15572, 0x28, 0xF5D2, 0x7D0, 0x0)
    Jump("Function_4_125B")

    label("loc_1307")

    Return()

    # Function_4_125B end

    def Function_5_1308(): pass

    label("Function_5_1308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1440")
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
    Jump("Function_5_1308")

    label("loc_1440")

    Return()

    # Function_5_1308 end

    def Function_6_1441(): pass

    label("Function_6_1441")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14E5")
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
    Jump("Function_6_1441")

    label("loc_14E5")

    Return()

    # Function_6_1441 end

    def Function_7_14E6(): pass

    label("Function_7_14E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15EA")
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
    Jump("Function_7_14E6")

    label("loc_15EA")

    Return()

    # Function_7_14E6 end

    def Function_8_15EB(): pass

    label("Function_8_15EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16EF")
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
    Jump("Function_8_15EB")

    label("loc_16EF")

    Return()

    # Function_8_15EB end

    def Function_9_16F0(): pass

    label("Function_9_16F0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1808")

    ChrTalk(    #0
        0xFE,
        (
            "这不是金先生吗？\x01",
            "请进请进！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        (
            "#070F嗯，谢谢。\x02\x03",

            "在这种情况下大使馆的\x01",
            "那帮家伙也很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "是啊，特别是\x01",
            "爱尔莎大使，为了了解情况\x01",
            "好像在到处跑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "她想问你们一些事，\x01",
            "所以告诉我如果各位游击士\x01",
            "来了就领进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1000F哟，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_18CF")

    label("loc_1808")


    ChrTalk(    #5
        0xFE,
        "请进吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1004F咦？方便吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "爱尔莎大使说你们来了\x01",
            "就请进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1015F唔，到底是怎么了呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "看来为了了解情况\x01",
            "而想和各种人聊聊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1000F哦，原来如此……\x01",
            "那么我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CF")

    OP_A2(0x20D9)
    Jump("loc_18E1")

    label("loc_18D5")


    ChrTalk(    #11
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()

    label("loc_18E1")

    Jump("loc_20A4")

    label("loc_18E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_190F")

    ChrTalk(    #12
        0x8,
        "请进。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B09")

    label("loc_190F")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x108, 70570, 0, -7070, 180)
    SetChrPos(0x101, 70550, 0, -5430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1959")
    SetChrPos(0x106, 69580, 0, -4260, 180)
    Jump("loc_196A")

    label("loc_1959")

    SetChrPos(0x103, 69580, 0, -4260, 180)

    label("loc_196A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198B")
    SetChrPos(0xF9, 70970, 0, -4310, 180)
    Jump("loc_199C")

    label("loc_198B")

    SetChrPos(0xF8, 70970, 0, -4310, 180)

    label("loc_199C")

    OP_6D(71710, 0, -7860, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 0, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #13
        0x8,
        "#2P金先生，你要进大使馆吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x108,
        "#070F啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1000)
    OP_8E(0x8, 0x10CA2, 0xFA, 0xFFFFDCD8, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #15
        0x8,
        "#2P请进。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71150, 0, -6670, 180)
    SetChrPos(0x1, 71150, 0, -6670, 180)
    SetChrPos(0x2, 71150, 0, -6670, 180)
    SetChrPos(0x3, 71150, 0, -6670, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x3)
    EventEnd(0x0)

    label("loc_1B09")

    Jump("loc_1B6E")

    label("loc_1B0C")


    ChrTalk(    #16
        0xFE,
        (
            "潜伏在港口的\x01",
            "情报部余党好像被抓住了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "在签字仪式前减少了一个不\x01",
            "安因素，让人松了口气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6E")

    Jump("loc_20A4")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1DDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1B9C")

    ChrTalk(    #18
        0x8,
        "请进。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D96")

    label("loc_1B9C")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x108, 70570, 0, -7070, 180)
    SetChrPos(0x101, 70550, 0, -5430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE6")
    SetChrPos(0x106, 69580, 0, -4260, 180)
    Jump("loc_1BF7")

    label("loc_1BE6")

    SetChrPos(0x103, 69580, 0, -4260, 180)

    label("loc_1BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C18")
    SetChrPos(0xF9, 70970, 0, -4310, 180)
    Jump("loc_1C29")

    label("loc_1C18")

    SetChrPos(0xF8, 70970, 0, -4310, 180)

    label("loc_1C29")

    OP_6D(71710, 0, -7860, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 0, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #19
        0x8,
        "#2P金先生，你要进大使馆吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x108,
        "#070F啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1000)
    OP_8E(0x8, 0x10CA2, 0xFA, 0xFFFFDCD8, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #21
        0x8,
        "#2P请进。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71150, 0, -6670, 180)
    SetChrPos(0x1, 71150, 0, -6670, 180)
    SetChrPos(0x2, 71150, 0, -6670, 180)
    SetChrPos(0x3, 71150, 0, -6670, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x3)
    EventEnd(0x0)

    label("loc_1D96")

    Jump("loc_1DDC")

    label("loc_1D99")


    ChrTalk(    #22
        0xFE,
        "……穿着白色礼服的女孩子啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "没印象，\x01",
            "不过肯定不在里面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDC")

    Jump("loc_20A4")

    label("loc_1DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4E")

    ChrTalk(    #24
        0xFE,
        (
            "前不久爱尔莎大使和\x01",
            "帝国的达维尔大使\x01",
            "在这里撞见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "我清清楚楚地闻见两人\x01",
            "之间的火药味。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A4")

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1ECE")

    ChrTalk(    #26
        0xFE,
        (
            "各位见到\x01",
            "爱尔莎大使了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "爱尔莎大使从以前起\x01",
            "就是个有点可怕的人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "有时候也会让\x01",
            "客人吃闭门羹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F30")

    label("loc_1ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 3)), scpexpr(EXPR_END)), "loc_1F2C")

    ChrTalk(    #29
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "啊，因为大使馆的领域内\x01",
            "拥有治外法权，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "言行举止请\x01",
            "谨慎一些哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F30")

    label("loc_1F2C")

    Call(0, 34)

    label("loc_1F30")

    Jump("loc_20A4")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_20A4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 4)), scpexpr(EXPR_END)), "loc_1F83")

    ChrTalk(    #32
        0x8,
        (
            "金先生要是来了\x01",
            "爱尔莎大使一定会感到高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2051")

    label("loc_1F83")


    ChrTalk(    #33
        0x108,
        "#071F哟，兄弟，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "咦？\x01",
            "这不是金先生吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "你又来利贝尔\x01",
            "玩了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x108,
        (
            "#070F哈哈，也差不多吧。\x02\x03",

            "接下来会有一阵子\x01",
            "要面对些麻烦，\x01",
            "要请你帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "明白！\x01",
            "爱尔莎大使一定会感到高兴的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x166C)

    label("loc_2051")

    Jump("loc_20A4")

    label("loc_2054")


    ChrTalk(    #38
        0xFE,
        (
            "等等哦，这里是\x01",
            "卡尔瓦德共和国大使馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "抱歉，没有事的人\x01",
            "是不能出入的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A4")

    TalkEnd(0x8)
    Return()

    # Function_9_16F0 end

    def Function_10_20A8(): pass

    label("Function_10_20A8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(    #40
        0xFE,
        "你们是……请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1015F咦？奥利维尔不在\x01",
            "也能进去？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "在这种情况下大使\x01",
            "很需要各种信息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "他说如果各位游击士到来，\x01",
            "就让你们进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1000F原来如此，那我们就不客气了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D8)
    Jump("loc_21DF")

    label("loc_218B")


    ChrTalk(    #46
        0xFE,
        (
            "在这种情况下大使\x01",
            "很需要各种信息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "他说如果各位游击士到来，\x01",
            "就让你们进来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DF")

    Jump("loc_2A04")

    label("loc_21E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2582")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_220D")

    ChrTalk(    #48
        0x9,
        "请进。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23FB")

    label("loc_220D")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 75550, 0, 69160, 0)
    SetChrPos(0x101, 75460, 0, 67600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2257")
    SetChrPos(0x106, 76600, 0, 66230, 0)
    Jump("loc_2268")

    label("loc_2257")

    SetChrPos(0x103, 76600, 0, 66230, 0)

    label("loc_2268")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2289")
    SetChrPos(0xF9, 75320, 0, 66060, 0)
    Jump("loc_229A")

    label("loc_2289")

    SetChrPos(0xF8, 75320, 0, 66060, 0)

    label("loc_229A")

    OP_6D(74500, 0, 71450, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #49
        0x9,
        "#2P奥利维尔先生，你要进大使馆吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        "#030F嗯，我要进去。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3C)
    Sleep(1000)
    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #51
        0x9,
        "#2P请进。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(75200, 0, 68360, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 75200, 0, 68360, 0)
    SetChrPos(0x1, 75200, 0, 68360, 0)
    SetChrPos(0x2, 75200, 0, 68360, 0)
    SetChrPos(0x3, 75200, 0, 68360, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x5)
    EventEnd(0x0)

    label("loc_23FB")

    Jump("loc_257F")

    label("loc_23FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2468")

    ChrTalk(    #52
        0xFE,
        (
            "穆拉先生好像去柏斯\x01",
            "出差了，要过一阵子才能回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "这样的话奥利维尔先生\x01",
            "又能被放养了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257F")

    label("loc_2468")


    ChrTalk(    #54
        0xFE,
        (
            "穆拉先生好像去柏斯\x01",
            "出差了，要过一阵子才能回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "好像他说是去王国军\x01",
            "相关的设施了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "这样的话奥利维尔先生\x01",
            "又能被放养了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_257C")

    ChrTalk(    #57
        0x104,
        (
            "#033F士兵朋友，别说这种失礼的话\x01",
            "污人清白啊。\x02\x03",

            "#034F你知道他出门，我内心深处\x01",
            "有多么寂寞吗……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #58
        0xFE,
        "……请别撒谎。\x02",
    )

    CloseMessageWindow()

    label("loc_257C")

    OP_A2(0x4)

    label("loc_257F")

    Jump("loc_2A04")

    label("loc_2582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2611")

    ChrTalk(    #59
        0xFE,
        (
            "哎呀，诸位……\x01",
            "莫非是来找奥利维尔先生的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "奥利维尔先生刚才\x01",
            "跟穆拉先生出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "那两个人虽然常斗嘴，\x01",
            "不过感情非常好哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_2611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2669")

    ChrTalk(    #62
        0xFE,
        (
            "辛苦了。\x01",
            "和大使的会面怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "如果各位的目的\x01",
            "能够达成就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_2669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 7)), scpexpr(EXPR_END)), "loc_26B8")

    ChrTalk(    #64
        0xFE,
        "请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "大使馆的领域内\x01",
            "有治外法权，\x01",
            "所以请小心一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_271E")

    label("loc_26B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_26C6")
    Call(0, 36)
    Jump("loc_271E")

    label("loc_26C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 6)), scpexpr(EXPR_END)), "loc_271A")

    ChrTalk(    #66
        0xFE,
        (
            "达维尔大使和穆拉先生\x01",
            "还没从外面回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "虽然我想不会\x01",
            "拖到很晚……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_271E")

    label("loc_271A")

    Call(0, 35)

    label("loc_271E")

    Jump("loc_2A04")

    label("loc_2721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2A04")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_297E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 5)), scpexpr(EXPR_END)), "loc_2795")
    TurnDirection(0x9, 0x104, 0)

    ChrTalk(    #68
        0x9,
        (
            "奥利维尔先生，\x01",
            "请你不要藏头露尾的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "这次的事达维尔大使\x01",
            "也很生气哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_297B")

    label("loc_2795")

    TurnDirection(0x9, 0x104, 0)

    ChrTalk(    #70
        0x104,
        (
            "#031F#6P哟，士兵朋友。\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x9,
        "#5P奥、奥利维尔先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        "#5P你之前都在干什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x104,
        "#033F#6P咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "#5P不是怎么不怎么的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "#5P你去亚尔摩村后\x01",
            "就行踪不明了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#5P穆拉先生可生气了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x104,
        (
            "#035F#6P呼……\x01",
            "这个男人还是那么可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1007F#6P对了，奥利维尔……\x02\x03",

            "#1019F难道你没告诉\x01",
            "大使馆你和我们\x01",
            "在一起行动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x104,
        (
            "#031F#6P哈哈哈。\x02\x03",

            "寻求爱的彷徨旅途\x01",
            "是注定要隐忍的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1007F#6P你在嘟囔些什么\x01",
            "莫明其妙的东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x166D)

    label("loc_297B")

    Jump("loc_2A04")

    label("loc_297E")


    ChrTalk(    #81
        0xFE,
        (
            "前面是埃雷波尼亚帝国大使馆。\x01",
            "不相干人员禁止入内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "特别是临近签字仪式的现在，\x01",
            "我们接到了强化警戒的指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "抱歉，请谅解。\x02",
    )

    CloseMessageWindow()

    label("loc_2A04")

    TalkEnd(0x9)
    Return()

    # Function_10_20A8 end

    def Function_11_2A08(): pass

    label("Function_11_2A08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A7E")

    ChrTalk(    #84
        0xFE,
        (
            "导力器不能使用的话\x01",
            "华光之王都的夜真是一片漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "女王她们虽然\x01",
            "做了很多调查，\x01",
            "真的能恢复使用吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C07")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2AF9")

    ChrTalk(    #86
        0xFE,
        "港口的事件真厉害啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "那个罪犯凯诺娜就是一直紧贴着\x01",
            "理查德上校的那个人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "你的表情看上去很严肃呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C07")

    label("loc_2AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2B52")

    ChrTalk(    #89
        0xFE,
        "怎么了怎么了？难道是在找人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "穿白色礼服的女孩子……\x01",
            "唔～我没看见啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C07")

    label("loc_2B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7A")

    ChrTalk(    #91
        0xFE,
        "乌鸦在叫着让我回家⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C07")

    label("loc_2B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2BB1")

    ChrTalk(    #92
        0xFE,
        (
            "真无聊，要不要去艾德尔\x01",
            "百货店买东西呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C07")

    label("loc_2BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2C07")

    ChrTalk(    #93
        0xFE,
        "Ｙｅａｈ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "格兰竞技场没什么活动，\x01",
            "好像暂时休馆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "有点寂寞呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2C07")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A08 end

    def Function_12_2C0B(): pass

    label("Function_12_2C0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C93")

    ChrTalk(    #96
        0xFE,
        (
            "我还以为只有王都导力停止了呢，\x01",
            "看来其他地方也一样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "真想这样一直\x01",
            "如果导力器没法使用，\x01",
            "这个国家会变成什么样！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB5")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2D10")

    ChrTalk(    #98
        0xFE,
        (
            "确实，最近话题少，\x01",
            "感觉没劲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "不过还是不希望\x01",
            "发生昨天那种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "我想要能够大家\x01",
            "能在一起欢呼的话题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB5")

    label("loc_2D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2D61")

    ChrTalk(    #101
        0xFE,
        "最近没什么话题，感觉无聊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "能不能……\x01",
            "发生点什么刺激的事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB5")

    label("loc_2D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DBB")

    ChrTalk(    #103
        0xFE,
        (
            "傍晚很美，可你不觉得\x01",
            "它会让人感觉寂寞吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "看着晚霞，\x01",
            "我都流泪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB5")

    label("loc_2DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2E23")

    ChrTalk(    #105
        0xFE,
        (
            "哎呀，莫非你就是在武术大赛\x01",
            "中取得冠军的游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "啊，能在这种地方\x01",
            "遇见你真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB5")

    label("loc_2E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2EB5")

    ChrTalk(    #107
        0xFE,
        (
            "我是在看武术大赛时\x01",
            "喜欢上王都的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "现在我就在这座城市生活。\x01",
            "还是城市里有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "我也能顺利地参加明年的\x01",
            "诞辰庆典和武术大赛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB5")

    TalkEnd(0xFE)
    Return()

    # Function_12_2C0B end

    def Function_13_2EB9(): pass

    label("Function_13_2EB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F36")

    ChrTalk(    #110
        0xFE,
        (
            "利贝尔是因导力器\x01",
            "发展起来的国家吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "如果一直像这样不能使用导力器的话……\x01",
            "就不仅是不方便这么简单了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3154")

    label("loc_2F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2F8E")

    ChrTalk(    #112
        0xFE,
        (
            "情报部那些家伙们\x01",
            "又引发了不得了的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "没有市民伤亡\x01",
            "真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3154")

    label("loc_2F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3004")

    ChrTalk(    #114
        0xFE,
        (
            "天气真好，要不要去\x01",
            "离宫午睡呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "现在王国军的家伙们\x01",
            "把那儿当作警备本部了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "算了，也没办法。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3154")

    label("loc_3004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3063")

    ChrTalk(    #117
        0xFE,
        (
            "可能因为签字仪式近了，\x01",
            "在城里执勤的人看来也很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "公务员也真不容易啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3154")

    label("loc_3063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3108")

    ChrTalk(    #119
        0xFE,
        (
            "在那么多事件和活动之后，\x01",
            "王都总算平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "……不过，想一想\x01",
            "接下来就是等待签字仪式了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "反正，要是这么以来就能\x01",
            "得到和平的话我是很欢迎的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3154")

    label("loc_3108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3154")

    ChrTalk(    #122
        0xFE,
        "啊，好困……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "要不要去西街区的咖啡屋\x01",
            "要杯咖啡来提提神呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    TalkEnd(0xFE)
    Return()

    # Function_13_2EB9 end

    def Function_14_3158(): pass

    label("Function_14_3158")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_31A0")

    ChrTalk(    #124
        0xFE,
        (
            "……说起来，真\x01",
            "感觉受不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "这样的生活岂不悲惨？\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B4")

    label("loc_31A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_31D1")

    ChrTalk(    #126
        0xFE,
        (
            "那个超级差劲的\x01",
            "公爵好像回王都了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B4")

    label("loc_31D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_322D")

    ChrTalk(    #127
        0xFE,
        "说起来，幽灵到底是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "……咦，真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "不会吧，怎么可能有那东西！\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B4")

    label("loc_322D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3255")

    ChrTalk(    #130
        0xFE,
        "说起来，今天吃什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B4")

    label("loc_3255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3277")

    ChrTalk(    #131
        0xFE,
        "说起来，要玩什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B4")

    label("loc_3277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_32B4")

    ChrTalk(    #132
        0xFE,
        "说起来，签字仪式是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "和我们有～关系吗？\x02",
    )

    CloseMessageWindow()

    label("loc_32B4")

    TalkEnd(0xFE)
    Return()

    # Function_14_3158 end

    def Function_15_32B8(): pass

    label("Function_15_32B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3307")

    ChrTalk(    #134
        0xFE,
        (
            "出现在那座湖里\x01",
            "绝对可疑～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "因为一看不就\x01",
            "让人感觉很可疑？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3440")

    label("loc_3307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_334A")

    ChrTalk(    #136
        0xFE,
        (
            "咦，真的？\x01",
            "不过，那个公爵啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "是不是有点可爱？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3440")

    label("loc_334A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3397")

    ChrTalk(    #138
        0xFE,
        (
            "我都说了，真的\x01",
            "在卢安出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "你为什么不相信？　真气人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3440")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33E8")

    ChrTalk(    #140
        0xFE,
        "去不去西街区的咖啡店？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "那里的咖喱，\x01",
            "好吃得让人实在受不了\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3440")

    label("loc_33E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_340E")

    ChrTalk(    #142
        0xFE,
        "对了，想不想吃冰淇淋？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3440")

    label("loc_340E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3440")

    ChrTalk(    #143
        0xFE,
        (
            "总之就是那个。\x01",
            "大家搞好关系，之类的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3440")

    TalkEnd(0xFE)
    Return()

    # Function_15_32B8 end

    def Function_16_3444(): pass

    label("Function_16_3444")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3478")

    ChrTalk(    #144
        0xFE,
        (
            "恋破山河在……\x01",
            "千军万马梦留痕……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DC")

    label("loc_3478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_34FA")

    ChrTalk(    #145
        0xFE,
        (
            "昨天我面向夕阳全力狂奔，\x01",
            "想不到感觉很舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "好吧，光在这里发愁\x01",
            "也没任何的意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "对了，去什么地方旅行吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DC")

    label("loc_34FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3581")

    ChrTalk(    #148
        0xFE,
        (
            "夕阳染得云绯红……\x01",
            "世界多么美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "并且，我是个多么\x01",
            "渺小的存在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "喂，利库斯……\x01",
            "渺小的我应该做些什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DC")

    label("loc_3581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_35CE")

    ChrTalk(    #151
        0xFE,
        (
            "我这么苦恼，\x01",
            "亏你还能打哈欠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "是哥们的话就和我一起烦恼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DC")

    label("loc_35CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_36DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3682")

    ChrTalk(    #153
        0xFE,
        "呼，到头来什么也没改变……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "今天也是像这样\x01",
            "稀里糊涂地度过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "今天也是像这样\x01",
            "稀里糊涂地度过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "没有工作，没有女友……\x01",
            "我的人生像这样下去好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_36DC")

    label("loc_3682")


    ChrTalk(    #157
        0xFE,
        (
            "呼，今天到头来\x01",
            "稀里糊涂地度过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "没有工作，没有女友……\x01",
            "我的人生像这样下去好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DC")

    TalkEnd(0xFE)
    Return()

    # Function_16_3444 end

    def Function_17_36E0(): pass

    label("Function_17_36E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3734")

    ChrTalk(    #159
        0xFE,
        (
            "安敦那家伙，\x01",
            "在洛连特也失恋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "他的下一个目标好像是珀艾玛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3872")

    label("loc_3734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_37A0")

    ChrTalk(    #161
        0xFE,
        (
            "安敦那家伙，\x01",
            "真是语出惊人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "他说简单的最美。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "虽然意思有点不对，\x01",
            "不过也挺合适的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3872")

    label("loc_37A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_380C")

    ChrTalk(    #164
        0xFE,
        (
            "……面向夕阳\x01",
            "奔跑一下怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "虽然没什么大的意义，\x01",
            "不过有可能因为那节奏使心情变好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3872")

    label("loc_380C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3830")

    ChrTalk(    #166
        0xFE,
        "哇～今天天气也不错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3872")

    label("loc_3830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3872")

    ChrTalk(    #167
        0xFE,
        "哈哈，安敦，你看。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "那朵云像不像\x01",
            "杜南公爵的发型。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3872")

    TalkEnd(0xFE)
    Return()

    # Function_17_36E0 end

    def Function_18_3876(): pass

    label("Function_18_3876")

    TalkBegin(0x11)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3893")
    OP_A9(0xCE)
    TalkEnd(0x11)
    Return()

    label("loc_3893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38A4")
    TalkEnd(0x11)
    Return()

    label("loc_38A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3931")

    ChrTalk(    #169
        0xFE,
        (
            "冰淇淋是在格兰赛尔\x01",
            "城堡的厨房做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "女王说要把这里的\x01",
            "冰淇淋让大家一起吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "听说女王好像吃过我的冰淇淋，\x01",
            "我真吃惊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEB")

    label("loc_3931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_39A3")

    ChrTalk(    #172
        0xFE,
        "听说昨晚发生了可怕的事件。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "客人都在讨论\x01",
            "港口的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "因此我也了解了\x01",
            "不是关于事件的内容。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEB")

    label("loc_39A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 4)), scpexpr(EXPR_END)), "loc_3A17")

    ChrTalk(    #175
        0xFE,
        (
            "穿白色礼服的女孩子，\x01",
            "应该在空港吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "她倒是乐呵呵地说\x01",
            "『我和姐姐她们\x01",
            "约好在空港见面的』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A93")

    label("loc_3A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 3)), scpexpr(EXPR_END)), "loc_3A25")
    Call(0, 47)
    Jump("loc_3A93")

    label("loc_3A25")


    ChrTalk(    #177
        0xFE,
        (
            "象利贝尔通讯那样的杂志\x01",
            "能对我们介绍当然好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "不过最让我感到高兴的还是\x01",
            "孩子们能津津有味地吃冰淇淋。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A93")

    Jump("loc_3CEB")

    label("loc_3A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3ADB")

    ChrTalk(    #179
        0xFE,
        "欢迎～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "要不要来个冰淇淋\x01",
            "作为晚饭后的甜食？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEB")

    label("loc_3ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3B16")

    ChrTalk(    #181
        0xFE,
        "欢迎～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "要不要尝尝冰凉\x01",
            "美味的冰淇淋？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEB")

    label("loc_3B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C87")

    ChrTalk(    #183
        0xFE,
        (
            "有人说我们是王室御用的，\x01",
            "不过那只是传言而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "虽然能让科洛蒂娅殿下品尝\x01",
            "我自然很高兴……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C81")
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #185
        0x101,
        (
            "#1000F（……科洛丝，你\x01",
            "　吃过这里的冰淇淋吗？)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x105,
        (
            "#040F（…………唔。）\x02\x03",

            "(其实祖母大人也向我\x01",
            " 推荐过。)\x02\x03",

            "(她老人家吃得\x01",
            " 非常开心。)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(    #187
        0x101,
        (
            "#1001F大姐姐，没问题的。\x01",
            "我觉得你可以为王室御用这个称号感到自豪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "？？？\x02",
    )

    CloseMessageWindow()

    label("loc_3C81")

    OP_A2(0x1)
    Jump("loc_3CEB")

    label("loc_3C87")


    ChrTalk(    #189
        0xFE,
        (
            "有人说我们是王室御用的，\x01",
            "不过那到底只是传言而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "如果科洛蒂娅殿下真的吃过\x01",
            "我自然很高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CEB")

    TalkEnd(0x11)
    Return()

    # Function_18_3876 end

    def Function_19_3CEF(): pass

    label("Function_19_3CEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3D4C")

    ChrTalk(    #191
        0xFE,
        (
            "我搭乘的林德号\x01",
            "停泊在洛连特……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "不过因为担心孩子，\x01",
            "就急着返回王都了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDC")

    label("loc_3D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3D89")

    ChrTalk(    #193
        0xFE,
        "呵呵，抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "要不要一起\x01",
            "吃那边的冰淇淋？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDC")

    label("loc_3D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3DDC")

    ChrTalk(    #195
        0xFE,
        (
            "趁飞行的间歇\x01",
            "我来稍微陪会儿孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "平时总让这孩子\x01",
            "忍耐很多事情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DDC")

    TalkEnd(0xFE)
    Return()

    # Function_19_3CEF end

    def Function_20_3DE0(): pass

    label("Function_20_3DE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E65")

    ChrTalk(    #197
        0xFE,
        "房间又冷又暗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "我虽然很害怕，\x01",
            "可还是拼命忍耐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "我因为看到妈妈的脸而安心得\x01",
            "哭出来了，不过这可是秘密哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAD")

    label("loc_3E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3EA4")

    ChrTalk(    #200
        0xFE,
        (
            "嘿嘿，我很乖地\x01",
            "在家看家哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "一点也不寂寞！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FAD")

    label("loc_3EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3EF1")

    ChrTalk(    #202
        0xFE,
        (
            "嘿嘿，就算妈妈去工作\x01",
            "我也能忍耐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "因为我是妈妈的好孩子。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FAD")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F35")

    ChrTalk(    #204
        0xFE,
        "妈妈……呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "好想能早点和妈妈一起玩……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FAD")

    label("loc_3F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3F72")

    ChrTalk(    #206
        0xFE,
        (
            "太好了～妈妈从单位\x01",
            "回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "你们羡慕吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FAD")

    label("loc_3F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3FAD")

    ChrTalk(    #208
        0xFE,
        "妈妈能不能早点回来呢～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "我会努力等着的……\x02",
    )

    CloseMessageWindow()

    label("loc_3FAD")

    TalkEnd(0xFE)
    Return()

    # Function_20_3DE0 end

    def Function_21_3FB1(): pass

    label("Function_21_3FB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4045")

    ChrTalk(    #210
        0xFE,
        (
            "在国际社会中\x01",
            "利贝尔的优势\x01",
            "是基于导力技术保持的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "互不侵犯条约也算是这点的象征吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "如果这状况持续下去的话\x01",
            "就算是女王……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_4045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_40C5")

    ChrTalk(    #213
        0xFE,
        "情报部竟然闹出那种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "是因为念着理查德上校\x01",
            "所以才这么做的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "无论如何，武力解决\x01",
            "都无法让人钦佩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_40C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4135")

    ChrTalk(    #216
        0xFE,
        (
            "在签字仪式那天治理各地的\x01",
            "市长们好像也会出席。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "卢安应该会派\x01",
            "新市长来吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "不知道啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_4135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41BF")

    ChrTalk(    #219
        0xFE,
        (
            "王国军从政变的重创中\x01",
            "恢复过来需要时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "可是我们有尤莉亚上尉、\x01",
            "希德中校和卡西乌斯准将。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "利贝尔一定没问题的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_41BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4227")

    ChrTalk(    #222
        0xFE,
        (
            "帝国竟然也会同意在\x01",
            "互不侵犯条约上签字呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "呵呵，女王陛下究竟使用了\x01",
            "什么样的魔法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_4227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_428E")

    ChrTalk(    #224
        0xFE,
        (
            "王室亲卫队的尤莉亚队长\x01",
            "最近听说晋升为上尉了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "呵呵，想想她的能力和\x01",
            "实绩就能理解了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_428E")

    TalkEnd(0xFE)
    Return()

    # Function_21_3FB1 end

    def Function_22_4292(): pass

    label("Function_22_4292")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42F8")

    ChrTalk(    #226
        0xFE,
        (
            "呼，因为导力器不能使用\x01",
            "夜晚变长了，让人不安得睡不着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "日暮真是让人感觉忧郁……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4533")

    label("loc_42F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4372")

    ChrTalk(    #228
        0xFE,
        "我想了很多……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "要想遇上优秀的男性，\x01",
            "我也要对自己的内涵进行磨炼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "如果能和对方互相激励\x01",
            "岂不更好？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4533")

    label("loc_4372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_43F3")

    ChrTalk(    #231
        0xFE,
        (
            "人生会因为终生伴侣\x01",
            "而产生很大的改变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "我觉得还是要\x01",
            "磨炼好辨别男性的眼力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "首先要观察对方的表\x01",
            "和鞋子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4533")

    label("loc_43F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4466")

    ChrTalk(    #234
        0xFE,
        (
            "有个不认识的老奶奶\x01",
            "突然对我说\x01",
            "『能不能嫁给我儿子』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "我怎么可能嫁给一个\x01",
            "从来没见过的人呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4533")

    label("loc_4466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_44D3")

    ChrTalk(    #236
        0xFE,
        (
            "刚才有个不认识的老奶奶\x01",
            "直直地盯着我看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "到底是什么意思呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "难道我脸上有什么东西？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4533")

    label("loc_44D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4533")

    ChrTalk(    #239
        0xFE,
        (
            "我以前曾被一个呆在百货商店\x01",
            "台阶上的男人纠缠过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "那真令人感到恶心和毛骨悚然……\x02",
    )

    CloseMessageWindow()

    label("loc_4533")

    TalkEnd(0xFE)
    Return()

    # Function_22_4292 end

    def Function_23_4537(): pass

    label("Function_23_4537")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_45D4")

    ChrTalk(    #241
        0xFE,
        (
            "对现在年轻的人来说，\x01",
            "好像导力停止之后\x01",
            "都感到非常不安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "当然，烧热水是一件\x01",
            "很麻烦的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "即便是我也已经\x01",
            "习惯于有导力的生活了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_45D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4641")

    ChrTalk(    #244
        0xFE,
        (
            "昨天的事件亲卫队和游击士\x01",
            "好像联手解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "王国军和协会\x01",
            "如果合作的话\x01",
            "就没什么可怕的事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_4641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4680")

    ChrTalk(    #246
        0xFE,
        (
            "虽说是工作，不过每到节日\x01",
            "士兵们都要忙于警戒呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_4680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46B9")

    ChrTalk(    #247
        0xFE,
        (
            "哎呀，太阳落山的时间\x01",
            "有点提早了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_46B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4746")

    ChrTalk(    #248
        0xFE,
        (
            "最近看不到游击士协会的\x01",
            "克鲁茨先生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "他是不是出门\x01",
            "去了别的什么地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "克鲁茨先生那种彬彬有礼的\x01",
            "品格很受我们欢迎。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_4746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_47BC")
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #251
        0xFE,
        "呀，你胸口的那枚徽章……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "大姐和……\x01",
            "你莫非是正游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "你们工作辛苦了。\x01",
            "真是年轻有为啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BC")

    TalkEnd(0xFE)
    Return()

    # Function_23_4537 end

    def Function_24_47C0(): pass

    label("Function_24_47C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A45")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49A1")

    ChrTalk(    #254
        0xFE,
        (
            "历史资料馆……\x01",
            "嗯，应该就是这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        "#1011F咦，这不是吉米先生吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "啊？　对了，你是\x01",
            "在蔡斯救过我的游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#1000F你在这里干什么啊？\x02\x03",

            "#1004F哦，对了……是来上交\x01",
            "那个古代遗物的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "是啊，就算失去了力量，不过\x01",
            "还是不知道这东西会引起什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "我打算放在这里委托他们调查。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1001F是吗？了不起了不起。\x02\x03",

            "如果你能放弃寻宝\x01",
            "而认真工作的话，就更了不起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "哇，你嘴好厉害……\x01",
            "不过那是没的商量的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "除非我能找到比\x01",
            "寻宝更浪漫的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3F")

    label("loc_49A1")


    ChrTalk(    #263
        0xFE,
        (
            "历史资料馆……\x01",
            "哇，看来没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "这里一定能保管\x01",
            "古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "其实我在蔡斯找到了\x01",
            "已失去力量的古代遗物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "我想请这座历史资料馆\x01",
            "调查，就过来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3F")

    OP_A2(0x1649)
    Jump("loc_4A8E")

    label("loc_4A45")


    ChrTalk(    #267
        0xFE,
        (
            "准备让他们帮我\x01",
            "调查失去了力量的古代遗物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "首先得去见负责人……\x02",
    )

    CloseMessageWindow()

    label("loc_4A8E")

    TalkEnd(0xFE)
    Return()

    # Function_24_47C0 end

    def Function_25_4A92(): pass

    label("Function_25_4A92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4ADD")

    ChrTalk(    #269
        0xFE,
        (
            "要是蔡斯的拉赛尔博士\x01",
            "关于此次的事件\x01",
            "应该会知道点什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B66")

    label("loc_4ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4B41")

    ChrTalk(    #270
        0xFE,
        (
            "那样的巨大人形兵器……\x01",
            "靠我们实在无法对付。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "如果下次再被袭击的话\x01",
            "肯定承受不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B66")

    label("loc_4B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4B66")

    ChrTalk(    #272
        0xFE,
        "咦？你们在找迷路的孩子？\x02",
    )

    CloseMessageWindow()

    label("loc_4B66")

    TalkEnd(0xFE)
    Return()

    # Function_25_4A92 end

    def Function_26_4B6A(): pass

    label("Function_26_4B6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4BC0")

    ChrTalk(    #273
        0xFE,
        "王国军现在仍处于警戒态势。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "为了应付紧急情况，\x01",
            "我也必须努力了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C45")

    label("loc_4BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4C0B")

    ChrTalk(    #275
        0xFE,
        (
            "有传闻说事件的主谋\x01",
            "是个不多大的小孩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "可这怎么可能？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C45")

    label("loc_4C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4C45")

    ChrTalk(    #277
        0xFE,
        (
            "东街区有很多重要设施，\x01",
            "所以得一丝不苟地警戒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C45")

    TalkEnd(0xFE)
    Return()

    # Function_26_4B6A end

    def Function_27_4C49(): pass

    label("Function_27_4C49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4CAC")

    ChrTalk(    #278
        0xFE,
        (
            "王国军里有那卡西乌斯准将\x01",
            "希德中校在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "光是想到这点，\x01",
            "我们就能冷静地行动了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D4E")

    label("loc_4CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4D22")

    ChrTalk(    #280
        0xFE,
        (
            "昨天的事件虽然令人惊讶，\x01",
            "不过尤莉亚队长回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "是希德中校把她叫回来的，\x01",
            "不过时机真是恰到好处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D4E")

    label("loc_4D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4D4E")

    ChrTalk(    #282
        0xFE,
        (
            "现在没发生任何\x01",
            "疑似问题的问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D4E")

    TalkEnd(0xFE)
    Return()

    # Function_27_4C49 end

    def Function_28_4D52(): pass

    label("Function_28_4D52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4D5F")
    Jump("loc_4E73")

    label("loc_4D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4D90")

    ChrTalk(    #283
        0xFE,
        (
            "拜托了，光昨天一天，\x01",
            "还没看够呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E73")

    label("loc_4D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4DE7")

    ChrTalk(    #284
        0xFE,
        (
            "好不容易来一趟，\x01",
            "得参观一下学术方面的设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "对人来说教育也很重要。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E73")

    label("loc_4DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E1B")

    ChrTalk(    #286
        0xFE,
        "……对意料之外的费用感到头痛啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E73")

    label("loc_4E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4E4C")

    ChrTalk(    #287
        0xFE,
        (
            "想不到格兰竞技场竟然\x01",
            "处于淡季……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E73")

    label("loc_4E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4E73")

    ChrTalk(    #288
        0xFE,
        "哟，这里就是格兰竞技场啊？\x02",
    )

    CloseMessageWindow()

    label("loc_4E73")

    TalkEnd(0xFE)
    Return()

    # Function_28_4D52 end

    def Function_29_4E77(): pass

    label("Function_29_4E77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4E84")
    Jump("loc_4FA4")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4EE0")

    ChrTalk(    #289
        0xFE,
        (
            "这人看来是\x01",
            "迷上了历史资料馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "好不容易旅行一次，\x01",
            "我今天想去别的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA4")

    label("loc_4EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4F31")

    ChrTalk(    #291
        0xFE,
        "这历史资料馆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "也没什么有意思的东西，\x01",
            "说实话我不太感兴趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA4")

    label("loc_4F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F57")

    ChrTalk(    #293
        0xFE,
        "呵呵，购物很愉快。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FA4")

    label("loc_4F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4F80")

    ChrTalk(    #294
        0xFE,
        (
            "唉……这个人\x01",
            "真没计划性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FA4")

    label("loc_4F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4FA4")

    ChrTalk(    #295
        0xFE,
        (
            "那个……\x01",
            "莫非大门关着？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA4")

    TalkEnd(0xFE)
    Return()

    # Function_29_4E77 end

    def Function_30_4FA8(): pass

    label("Function_30_4FA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4FB5")
    Jump("loc_5129")

    label("loc_4FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_500A")

    ChrTalk(    #296
        0xFE,
        (
            "帝国虽然有种危险的感觉，\x01",
            "不过那也正是它的魅力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "真想去玩玩啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5129")

    label("loc_500A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_503F")

    ChrTalk(    #298
        0xFE,
        (
            "……穿白衣服的女孩子？\x01",
            "嗯，没看见啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5129")

    label("loc_503F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5095")

    ChrTalk(    #299
        0xFE,
        (
            "你们和黑发的\x01",
            "帝国军人说过话了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "真好啊……\x01",
            "我是他的粉丝啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5129")

    label("loc_5095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_50EB")

    ChrTalk(    #301
        0xFE,
        (
            "刚才从大使馆出来了\x01",
            "一个黑发的军人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "虽然不太亲切，\x01",
            "不过很帅啊㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5129")

    label("loc_50EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5129")

    ChrTalk(    #303
        0xFE,
        (
            "『黄金军马』的徽章啊……\x01",
            "凑近看的话真有震撼力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5129")

    TalkEnd(0xFE)
    Return()

    # Function_30_4FA8 end

    def Function_31_512D(): pass

    label("Function_31_512D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_513A")
    Jump("loc_5272")

    label("loc_513A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5163")

    ChrTalk(    #304
        0xFE,
        (
            "嗯……空港\x01",
            "在那个方向呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5272")

    label("loc_5163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5185")

    ChrTalk(    #305
        0xFE,
        "今天去哪儿参观呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5272")

    label("loc_5185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51CC")

    ChrTalk(    #306
        0xFE,
        "呼，在王都的参观很令我满意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "也该回\x01",
            "宾馆了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5272")

    label("loc_51CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_523E")

    ChrTalk(    #308
        0xFE,
        (
            "嗯～这里是东街区的\x01",
            "共和国大使馆前，那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "太广阔了，很容易迷路，\x01",
            "所以我在百货商店买了地图。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5272")

    label("loc_523E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5272")

    ChrTalk(    #310
        0xFE,
        (
            "我是第一次来王都，\x01",
            "这真是个广阔的城市。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5272")

    TalkEnd(0xFE)
    Return()

    # Function_31_512D end

    def Function_32_5276(): pass

    label("Function_32_5276")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5283")
    Jump("loc_53AC")

    label("loc_5283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_52BA")

    ChrTalk(    #311
        0xFE,
        (
            "好像发生了什么事件呢。\x01",
            "到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AC")

    label("loc_52BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_52FF")

    ChrTalk(    #312
        0xFE,
        "有没有看见一个女孩子？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "我看见了，\x01",
            "她走过这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AC")

    label("loc_52FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532B")

    ChrTalk(    #314
        0xFE,
        "哎呀，好漂亮的晚霞啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_53AC")

    label("loc_532B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5385")

    ChrTalk(    #315
        0xFE,
        (
            "光是参观景点\x01",
            "不能算是旅游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "像这样悠闲的时刻\x01",
            "也能成为旅行的美好回忆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AC")

    label("loc_5385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_53AC")

    ChrTalk(    #317
        0xFE,
        "呵呵，这里真是个好地方……\x02",
    )

    CloseMessageWindow()

    label("loc_53AC")

    TalkEnd(0xFE)
    Return()

    # Function_32_5276 end

    def Function_33_53B0(): pass

    label("Function_33_53B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_53BD")
    Jump("loc_5544")

    label("loc_53BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5419")

    ChrTalk(    #318
        0xFE,
        (
            "快乐的旅行也\x01",
            "只到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "从明天开始又要恢复\x01",
            "一如既往的主妇生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_5419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_546E")

    ChrTalk(    #320
        0xFE,
        (
            "穿白衣服的女孩子？\x01",
            "刚才我好像看见了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        "我记得好像就在这附近……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54D1")

    ChrTalk(    #322
        0xFE,
        (
            "在旅行目的地买东西的话，不知不觉\x01",
            "让钱包见底了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        "买纪念品的钱很快就不见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_54D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5515")

    ChrTalk(    #324
        0xFE,
        (
            "冰淇淋\x01",
            "非常好吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "好了，该去百货商店\x01",
            "买东西了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5544")

    label("loc_5515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5544")

    ChrTalk(    #326
        0xFE,
        (
            "附近有\x01",
            "好吃的冰淇淋\x01",
            "我是听说的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5544")

    TalkEnd(0xFE)
    Return()

    # Function_33_53B0 end

    def Function_34_5548(): pass

    label("Function_34_5548")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x108, 70950, 0, -6900, 180)
    SetChrPos(0x101, 71720, 0, -5910, 180)
    SetChrPos(0x105, 70350, 0, -5760, 180)
    SetChrPos(0x104, 70950, 0, -4800, 180)
    OP_6D(71730, 0, -7500, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 0, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 4)), scpexpr(EXPR_END)), "loc_5651")

    ChrTalk(    #327
        0x8,
        (
            "啊，金先生。\x01",
            "辛苦了。\x02\x03",

            "请问有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x108,
        (
            "#070F#6P嗯，我有事要找\x01",
            "爱尔莎大使商量……\x02\x03",

            "她现在在吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56FE")

    label("loc_5651")


    ChrTalk(    #329
        0x108,
        "#071F#6P哟，兄弟，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x8,
        (
            "咦？\x01",
            "这不是金先生吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x8,
        (
            "你又来利贝尔\x01",
            "玩了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x108,
        (
            "#070F#6P哈哈，是啊。\x02\x03",

            "来打个招呼，顺便有事要找\x01",
            "爱尔莎大使商量……\x02\x03",

            "她现在在吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FE")


    ChrTalk(    #333
        0x8,
        (
            "她没有外出，\x01",
            "应该在的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x8,
        "对了，那边的各位呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x108,
        (
            "#070F#6P是我在协会的工作伙伴。\x02\x03",

            "正准备介绍给\x01",
            "我们的大使呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x8,
        "嘿嘿，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x8,
        (
            "反正只要是金先生的\x01",
            "朋友，放行也没关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1000)
    OP_8E(0x8, 0x10CA2, 0xFA, 0xFFFFDCD8, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #338
        0x8,
        "请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x8,
        (
            "啊，因为大使馆的领域内\x01",
            "拥有治外法权，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x8,
        (
            "言行举止请\x01",
            "谨慎一些哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #341
        0x101,
        "#1006F#5P听见没，奥利维尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x104,
        "#034F唉，你们真不信任我。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71150, 0, -6670, 180)
    SetChrPos(0x1, 71150, 0, -6670, 180)
    SetChrPos(0x2, 71150, 0, -6670, 180)
    SetChrPos(0x3, 71150, 0, -6670, 180)
    OP_0D()
    OP_A2(0x161B)
    EventEnd(0x0)
    Return()

    # Function_34_5548 end

    def Function_35_5928(): pass

    label("Function_35_5928")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 75060, 0, 69850, 0)
    SetChrPos(0x101, 74090, 0, 68370, 0)
    SetChrPos(0x105, 75800, 0, 68680, 0)
    SetChrPos(0x108, 74770, 0, 67260, 0)
    OP_6D(75780, 0, 70890, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 5)), scpexpr(EXPR_END)), "loc_5A28")

    ChrTalk(    #343
        0x9,
        "#5P哎呀，奥利维尔先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x104,
        (
            "#035F#6P呵呵，你工作辛苦了。\x02\x03",

            "#030F我想进去，\x01",
            "请问能不能放行？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BFC")

    label("loc_5A28")


    ChrTalk(    #345
        0x104,
        (
            "#031F#6P哟，士兵朋友。\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #346
        0x9,
        "#5P奥、奥利维尔先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x9,
        "#5P你之前都在干什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x104,
        "#033F#6P咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x9,
        "#5P不是怎么不怎么的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x9,
        (
            "#5P你去亚尔摩村后就\x01",
            "就行踪不明了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x9,
        "#5P穆拉先生可生气了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x104,
        (
            "#035F#6P呼……\x01",
            "这个男人还是那么可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1007F#6P对了，奥利维尔……\x02\x03",

            "#1019F难道你没告诉\x01",
            "大使馆你和我们\x01",
            "在一起行动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x104,
        (
            "#031F#6P哈哈哈。\x02\x03",

            "寻求爱的彷徨旅途\x01",
            "是注定要隐忍的。\x02\x03",

            "#030F先不说这些……\x01",
            "能不能让我进去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BFC")


    ChrTalk(    #355
        0x9,
        (
            "#5P这倒没问题……\x01",
            "请问那边的几位是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        (
            "#1006F#6P我们是游击士协会的人。\x02\x03",

            "有点事想问问\x01",
            "这里的大使先生。\x02\x03",

            "所以就让这个得意忘形的大赖皮蛋\x01",
            "来介绍我们认识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x9,
        "#5P原来是这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x9,
        (
            "#5P身份也确认了，\x01",
            "应该能放行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x9,
        (
            "#5P不过不巧的是达维尔大使\x01",
            "和穆拉先生一同外出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x104,
        "#033F#6P哎呀，这样啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 180, 400)

    ChrTalk(    #361
        0x104,
        (
            "#030F#5P怎么办？艾丝蒂尔。\x01",
            "要在里面等吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x101,
        (
            "#1015F#6P嗯…虽然那样也可以……\x02\x03",

            "#1006F但我们并没有太多的时间，\x01",
            "还是先去别的地方转转吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x105,
        (
            "#040F#2P那么，我们先去拜访\x01",
            "共和国大使馆吧？\x02\x03",

            "同样也在东街区。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x108,
        (
            "#070F是啊。\x01",
            "回来也方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x101,
        (
            "#1006F#6P那就这么定了。\x02\x03",

            "士兵先生。\x01",
            "我们一会儿再回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x9,
        "#5P嗯，恭候。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_8C(0x9, 180, 0)
    OP_6D(74860, 0, 68920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74860, 0, 68920, 0)
    SetChrPos(0x1, 74860, 0, 68920, 0)
    SetChrPos(0x2, 74860, 0, 68920, 0)
    SetChrPos(0x3, 74860, 0, 68920, 0)
    OP_0D()
    OP_A2(0x161E)
    EventEnd(0x0)
    Return()

    # Function_35_5928 end

    def Function_36_5F0B(): pass

    label("Function_36_5F0B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 75060, 0, 69850, 0)
    SetChrPos(0x101, 74090, 0, 68370, 0)
    SetChrPos(0x105, 75800, 0, 68680, 0)
    SetChrPos(0x108, 74770, 0, 67260, 0)
    OP_6D(75780, 0, 70890, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6052")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第一次和贝尔坎说话的情况下】\x01",      # 0
            "【◇已经和贝尔坎说过话的情况下】\x01",      # 1
            "【◇什么也没有变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6046"),
        (1, "loc_604C"),
        (SWITCH_DEFAULT, "loc_6052"),
    )


    label("loc_6046")

    OP_A3(0x161E)
    Jump("loc_6052")

    label("loc_604C")

    OP_A2(0x161E)
    Jump("loc_6052")

    label("loc_6052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 5)), scpexpr(EXPR_END)), "loc_60C5")

    ChrTalk(    #367
        0x9,
        "#5P哎呀，奥利维尔先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x104,
        (
            "#035F#6P呵呵，你工作辛苦了。\x02\x03",

            "#030F我想进去，\x01",
            "请问能不能放行？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6299")

    label("loc_60C5")


    ChrTalk(    #369
        0x104,
        (
            "#031F#6P哟，士兵朋友。\x01",
            "你还好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #370
        0x9,
        "#5P奥、奥利维尔先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x9,
        "#5P你之前都在干什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x104,
        "#033F#6P咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x9,
        "#5P不是怎么不怎么的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x9,
        (
            "#5P你去亚尔摩村后就\x01",
            "就行踪不明了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x9,
        "#5P穆拉先生可生气了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x104,
        (
            "#035F#6P呼……\x01",
            "这个男人还是那么可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#1007F#6P对了，奥利维尔……\x02\x03",

            "#1019F难道你没告诉\x01",
            "大使馆你和我们\x01",
            "在一起行动？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x104,
        (
            "#031F#6P哈哈哈。\x02\x03",

            "寻求爱的彷徨旅途\x01",
            "是注定要隐忍的。\x02\x03",

            "#030F先不说这些……\x01",
            "能不能让我进去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6299")


    ChrTalk(    #379
        0x9,
        (
            "#5P这倒没问题……\x01",
            "请问那边的几位是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x101,
        (
            "#1006F#6P我们是游击士协会的人。\x02\x03",

            "有点事想问问\x01",
            "这里的大使先生。\x02\x03",

            "所以就让这个得意忘形的大赖皮蛋\x01",
            "来介绍我们认识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x9,
        "#5P原来是这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x9,
        (
            "#5P身份也确认了，\x01",
            "看来可以让你们进去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6421")

    label("loc_6382")


    ChrTalk(    #383
        0x9,
        "#5P啊，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x9,
        (
            "#5P就在刚才达维尔大使和\x01",
            "穆拉先生已经回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x104,
        "#031F#6P呵呵，看来我们来得是时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        "#1011F#6P那么，能不能放行？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x9,
        "#5P明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_6421")

    OP_8C(0x9, 0, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3C)
    Sleep(1000)
    OP_8E(0x9, 0x12DA4, 0xFA, 0x11652, 0xBB8, 0x0)
    OP_8C(0x9, 225, 400)
    Sleep(500)

    ChrTalk(    #388
        0x9,
        "#5P请进。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x9,
        (
            "#5P因为大使馆的领域内\x01",
            "有治外法权，\x01",
            "所以请小心一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x101,
        "#1006F#6P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_8C(0x9, 180, 0)
    OP_6D(74870, 0, 68640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74870, 0, 68640, 0)
    SetChrPos(0x1, 74870, 0, 68640, 0)
    SetChrPos(0x2, 74870, 0, 68640, 0)
    SetChrPos(0x3, 74870, 0, 68640, 0)
    OP_0D()
    OP_A2(0x161F)
    EventEnd(0x0)
    Return()

    # Function_36_5F0B end

    def Function_37_6561(): pass

    label("Function_37_6561")

    EventBegin(0x0)
    OP_4A(0x15, 255)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D6")
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇还没去过城里的各处目标（听说了奈尔不在）】\x01",      # 0
            "【◇还没去过城里的各处目标（没听说奈尔不在）】\x01",      # 1
            "【◇去过城里的各处目标（听说了奈尔不在）】\x01",          # 2
            "【◇去过城里的各处目标（没听说奈尔不在）】\x01",          # 3
            "【◇什么也没有变更】\x01",                                # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6682"),
        (1, "loc_6697"),
        (2, "loc_66AC"),
        (3, "loc_66C1"),
        (SWITCH_DEFAULT, "loc_66D6"),
    )


    label("loc_6682")

    OP_A3(0x1623)
    OP_A3(0x1624)
    OP_A3(0x1625)
    OP_A3(0x1626)
    OP_A3(0x1627)
    OP_A2(0x1680)
    Jump("loc_66D6")

    label("loc_6697")

    OP_A3(0x1623)
    OP_A3(0x1624)
    OP_A3(0x1625)
    OP_A3(0x1626)
    OP_A3(0x1627)
    OP_A3(0x1680)
    Jump("loc_66D6")

    label("loc_66AC")

    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A2(0x1680)
    Jump("loc_66D6")

    label("loc_66C1")

    OP_A2(0x1623)
    OP_A2(0x1624)
    OP_A2(0x1625)
    OP_A2(0x1626)
    OP_A2(0x1627)
    OP_A3(0x1680)
    Jump("loc_66D6")

    label("loc_66D6")

    SetChrPos(0x104, 75810, 0, 65960, 0)
    SetChrPos(0x101, 74720, 0, 65970, 0)
    SetChrPos(0x105, 76080, 0, 64650, 0)
    SetChrPos(0x108, 74790, 0, 64580, 9)
    SetChrPos(0x130, 75150, 0, 67480, 180)
    OP_6D(74330, 0, 66970, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(308000, 0)
    OP_6E(262, 0)
    OP_6F(0x9, 60)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #391
        0x101,
        (
            "#1006F#1P穆拉先生，谢谢你。\x02\x03",

            "多亏你的帮忙，我们从大使先生\x01",
            "那里听到了很多事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x130,
        (
            "#277F#2P哪里……\x01",
            "没什么大不了的。\x02\x03",

            "而且这本来也是三个国家的问题，\x01",
            "我当然要配合你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x108,
        "#070F#1P哈哈，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x105,
        (
            "#542F#6P要是能有办法\x01",
            "解决就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x104,
        "#032F………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #396
        0x101,
        (
            "#1004F#5P啊……\x01",
            "怎么了，奥利维尔？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 270, 400)

    ChrTalk(    #397
        0x104,
        (
            "#030F不……想了点事情而已。\x02\x03",

            "和恐吓事件无关，\x01",
            "不用介意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x101,
        "#1015F#5P嗯、嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x130,
        (
            "#270F#2P………………………………\x02\x03",

            "#272F奥利维尔，留在王都的期间，\x01",
            "你会住在大使馆吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 0, 400)

    ChrTalk(    #400
        0x104,
        (
            "#031F呵呵，当然了。\x02\x03",

            "就像平时一样，躺在你的\x01",
            "床上做着甜美的梦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x101,
        "#1004F#5P哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x105,
        "#044F#6P呼……\x02",
    )

    CloseMessageWindow()
    OP_62(0x130, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #403
        0x130,
        (
            "#274F#2P……小姐们会信以为真的，\x01",
            "别开这种无聊的玩笑。\x02\x03",

            "再开过分的玩笑我就用席子\x01",
            "把你卷起来扔到地板上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #404
        0x104,
        (
            "#037F讨厌，难道\x01",
            "这就是所谓的捆绑游戏……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x130,
        (
            "#276F#2P如果你希望的话。\x02\x03",

            "我还可以把你像\x01",
            "结草虫一样吊在窗口。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #406
        0x104,
        (
            "#034F对不起。\x01",
            "我太得意忘形了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #407
        0x101,
        "#1016F#1P嗯，不愧从小到大的朋友。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x108,
        (
            "#071F#1P哈哈，不管嘴上说什么，\x01",
            "脾气还是很合拍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x130,
        (
            "#272F#2P请不要说得\x01",
            "这么别扭。\x02\x03",

            "#277F算了……\x01",
            "我就先告辞了。\x02\x03",

            "请你们努力调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x101,
        "#1006F#1P嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 0, 400)

    def lambda_6C1F():
        OP_6D(74890, 0, 70490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C1F)

    def lambda_6C37():
        OP_8E(0x130, 0x1228C, 0x0, 0x12D9A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x130, 1, lambda_6C37)
    Sleep(4000)
    OP_4A(0x9, 255)
    OP_8C(0x9, 270, 400)
    OP_8E(0x9, 0x124DA, 0x0, 0x11652, 0x7D0, 0x0)
    OP_8C(0x9, 0, 400)
    OP_22(0x6E, 0x0, 0x64)
    OP_71(0x9, 0x10)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)
    Sleep(1500)
    OP_8E(0x9, 0x12DA4, 0xFA, 0x11652, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    OP_4B(0x9, 255)

    def lambda_6CB9():
        OP_6D(74740, 0, 65560, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6CB9)

    def lambda_6CD1():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CD1)
    OP_8C(0x9, 180, 400)
    OP_8C(0x104, 180, 400)
    WaitChrThread(0x101, 0x2)
    SetChrFlags(0x130, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_6D6E")

    ChrTalk(    #411
        0x101,
        (
            "#1006F#5P好了……\x01",
            "还没到傍晚。\x02\x03",

            "先去格兰赛尔城，\x01",
            "然后再去利贝尔通讯社吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x105,
        "#040F#6P嗯，就这么办。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DEA")

    label("loc_6D6E")


    ChrTalk(    #413
        0x101,
        (
            "#1006F#5P两个大使馆都解决了，\x01",
            "剩下的就是城堡和利贝尔通讯社了。\x02\x03",

            "要是能有线索就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x105,
        (
            "#040F是啊……\x01",
            "总之去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DEA")

    Jump("loc_6F35")

    label("loc_6DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_6E93")

    ChrTalk(    #415
        0x104,
        (
            "#030F#2P不过已经傍晚了呢……\x01",
            "时间过得真快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x105,
        (
            "#040F#6P可能奈尔先生\x01",
            "也回通讯社了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        "#1011F#5P嗯，也对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x108,
        (
            "#070F#3P好。\x01",
            "我们去通讯社看看吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F35")

    label("loc_6E93")


    ChrTalk(    #419
        0x104,
        (
            "#030F#2P不过已经傍晚了呢……\x01",
            "时间过得真快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x105,
        (
            "#040F#6P就只剩下\x01",
            "利贝尔通讯社没去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x101,
        "#1006F#5P嗯，对。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x108,
        (
            "#070F#3P时间也差不多了。\x01",
            "快去拜访一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F35")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x2F, 0xFF)
    OP_6D(74890, 0, 65620, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 74890, 0, 65620, 180)
    SetChrPos(0x1, 74890, 0, 65620, 180)
    SetChrPos(0x2, 74890, 0, 65620, 180)
    SetChrPos(0x3, 74890, 0, 65620, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1622)
    OP_71(0x9, 0x10)
    EventEnd(0x0)
    OP_4B(0x15, 255)
    OP_4B(0x17, 255)
    Return()

    # Function_37_6561 end

    def Function_38_6FE5(): pass

    label("Function_38_6FE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7006")
    Call(0, 99)
    Call(0, 100)

    label("loc_7006")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_701E"),
        (106, "loc_70A2"),
        (107, "loc_7126"),
        (108, "loc_71AA"),
        (SWITCH_DEFAULT, "loc_722E"),
    )


    label("loc_701E")

    SetChrPos(0x101, 69080, 1250, 35450, 315)
    SetChrPos(0x107, 71080, 1250, 35550, 45)
    SetChrPos(0xF7, 69580, 1250, 33780, 225)
    SetChrPos(0xF9, 70630, 1250, 33820, 135)
    OP_6D(70020, 1250, 34440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    Jump("loc_722E")

    label("loc_70A2")

    SetChrPos(0x101, 81200, 1250, 24440, 45)
    SetChrPos(0x107, 81200, 1250, 22600, 135)
    SetChrPos(0xF7, 79390, 1250, 24250, 225)
    SetChrPos(0xF9, 79200, 1250, 22670, 315)
    OP_6D(79940, 1250, 23610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(303000, 0)
    OP_6E(262, 0)
    Jump("loc_722E")

    label("loc_7126")

    SetChrPos(0x101, 71120, 1250, 10530, 135)
    SetChrPos(0x107, 69070, 1250, 10520, 225)
    SetChrPos(0xF7, 71070, 1250, 12090, 315)
    SetChrPos(0xF9, 69540, 1250, 12070, 45)
    OP_6D(70260, 1250, 11450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_722E")

    label("loc_71AA")

    SetChrPos(0x101, 59140, 1250, 22220, 225)
    SetChrPos(0x107, 59260, 1250, 24340, 315)
    SetChrPos(0xF7, 61220, 1250, 22110, 135)
    SetChrPos(0xF9, 61090, 1250, 23790, 45)
    OP_6D(59990, 1250, 23630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(262, 0)
    Jump("loc_722E")

    label("loc_722E")

    SetChrFlags(0x16, 0x80)
    OP_4A(0x16, 255)
    SetChrPos(0x16, 62410, 250, 5400, 270)
    OP_43(0x101, 0x1, 0x0, 0x27)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_43(0xF7, 0x1, 0x0, 0x29)
    Sleep(100)
    OP_43(0x107, 0x1, 0x0, 0x28)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    OP_44(0x101, 0x1)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(1000)

    ChrTalk(    #423
        0x101,
        (
            "#1007F嗯……\x01",
            "跟丢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xF7, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(500)

    def lambda_72C4():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_72C4)
    Sleep(100)

    def lambda_72D7():
        TurnDirection(0xFE, 0xF9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_72D7)
    Sleep(100)

    def lambda_72EA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_72EA)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7323")

    ChrTalk(    #424
        0x106,
        (
            "#555F真是的，\x01",
            "这么鬼灵精……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7344")

    label("loc_7323")


    ChrTalk(    #425
        0x103,
        "#524F嗯，这孩子真像只小猫。\x02",
    )

    CloseMessageWindow()

    label("loc_7344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7386")

    ChrTalk(    #426
        0x108,
        (
            "#070F你们昨天是一起\x01",
            "逛过这间\x01",
            "百货商店的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73BB")

    label("loc_7386")


    ChrTalk(    #427
        0x105,
        (
            "#542F我记得她和\x01",
            "提妲一起逛过\x01",
            "这间百货商店的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BB")


    ChrTalk(    #428
        0x107,
        (
            "#063F嗯，是的。\x02\x03",

            "#561F说不定是去了\x01",
            "别的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x101,
        (
            "#1006F没关系，应该还\x01",
            "没跑得太远吧。\x02\x03",

            "以东街区为中心搜索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x162E)
    OP_28(0x8C, 0x1, 0x4)
    EventEnd(0x0)
    ClearChrFlags(0x16, 0x80)
    OP_4B(0x16, 255)
    Return()

    # Function_38_6FE5 end

    def Function_39_7444(): pass

    label("Function_39_7444")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_745C"),
        (106, "loc_7483"),
        (107, "loc_74AA"),
        (108, "loc_74D1"),
        (SWITCH_DEFAULT, "loc_74F8"),
    )


    label("loc_745C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7480")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_745C")

    label("loc_7480")

    Jump("loc_74F8")

    label("loc_7483")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74A7")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_7483")

    label("loc_74A7")

    Jump("loc_74F8")

    label("loc_74AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74CE")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_74AA")

    label("loc_74CE")

    Jump("loc_74F8")

    label("loc_74D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74F5")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_74D1")

    label("loc_74F5")

    Jump("loc_74F8")

    label("loc_74F8")

    Return()

    # Function_39_7444 end

    def Function_40_74F9(): pass

    label("Function_40_74F9")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_7511"),
        (106, "loc_7538"),
        (107, "loc_755F"),
        (108, "loc_7586"),
        (SWITCH_DEFAULT, "loc_75AD"),
    )


    label("loc_7511")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7535")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_7511")

    label("loc_7535")

    Jump("loc_75AD")

    label("loc_7538")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_755C")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_7538")

    label("loc_755C")

    Jump("loc_75AD")

    label("loc_755F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7583")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_755F")

    label("loc_7583")

    Jump("loc_75AD")

    label("loc_7586")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75AA")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_7586")

    label("loc_75AA")

    Jump("loc_75AD")

    label("loc_75AD")

    Return()

    # Function_40_74F9 end

    def Function_41_75AE(): pass

    label("Function_41_75AE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_75C6"),
        (106, "loc_75ED"),
        (107, "loc_7614"),
        (108, "loc_763B"),
        (SWITCH_DEFAULT, "loc_7662"),
    )


    label("loc_75C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75EA")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_75C6")

    label("loc_75EA")

    Jump("loc_7662")

    label("loc_75ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7611")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_75ED")

    label("loc_7611")

    Jump("loc_7662")

    label("loc_7614")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7638")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_7614")

    label("loc_7638")

    Jump("loc_7662")

    label("loc_763B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_765F")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_763B")

    label("loc_765F")

    Jump("loc_7662")

    label("loc_7662")

    Return()

    # Function_41_75AE end

    def Function_42_7663(): pass

    label("Function_42_7663")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_767B"),
        (106, "loc_76A2"),
        (107, "loc_76C9"),
        (108, "loc_76F0"),
        (SWITCH_DEFAULT, "loc_7717"),
    )


    label("loc_767B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_769F")
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("loc_767B")

    label("loc_769F")

    Jump("loc_7717")

    label("loc_76A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76C6")
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("loc_76A2")

    label("loc_76C6")

    Jump("loc_7717")

    label("loc_76C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76ED")
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    OP_8C(0xFE, 45, 400)
    Sleep(2000)
    Jump("loc_76C9")

    label("loc_76ED")

    Jump("loc_7717")

    label("loc_76F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7714")
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8C(0xFE, 135, 400)
    Sleep(2000)
    Jump("loc_76F0")

    label("loc_7714")

    Jump("loc_7717")

    label("loc_7717")

    Return()

    # Function_42_7663 end

    def Function_43_7718(): pass

    label("Function_43_7718")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_772F")
    Call(0, 99)
    Call(0, 100)

    label("loc_772F")

    SetChrPos(0x101, 45720, 250, 79960, 180)
    SetChrPos(0x107, 45460, 250, 81610, 360)
    SetChrPos(0xF7, 44130, 250, 80220, 180)
    SetChrPos(0xF9, 44120, 250, 81630, 360)
    OP_6D(43920, 500, 81110, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x1, 0x0, 0x2C)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x2D)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x2C)
    Sleep(300)
    OP_43(0x107, 0x1, 0x0, 0x2D)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #430
        0x101,
        "#1007F#6P又、又不在……\x02",
    )

    CloseMessageWindow()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3B)
    Sleep(1000)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 41000, 750, 81110, 90)
    OP_8E(0x24, 0xA7A8, 0x1F4, 0x13CD6, 0x7D0, 0x0)

    ChrTalk(    #431
        0x24,
        "#5P对、对不起。\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_786A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_786A)
    Sleep(50)

    def lambda_787D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_787D)
    Sleep(50)

    def lambda_7890():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7890)
    Sleep(50)

    def lambda_78A3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_78A3)
    Sleep(300)

    ChrTalk(    #432
        0x24,
        (
            "#5P我虽然想留住\x01",
            "她的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x101,
        (
            "#1016F#6P不，没事的。\x02\x03",

            "#1015F倒是你有没有\x01",
            "跟她交谈过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x24,
        (
            "#5P嗯、嗯……\x01",
            "她跟我说的话很不可思议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x24,
        (
            "#5P她说『你知道哪儿有\x01",
            "没有颜色的鱼吗？』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x101,
        "#6P#1004F咦……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A94")

    ChrTalk(    #437
        0x108,
        (
            "#074F呼，这话真有深意。\x02\x03",

            "说不定是\x01",
            "解谜的线索。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_79C5():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_79C5)

    def lambda_79D3():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_79D3)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #438
        0x101,
        "#1020F#6P解、解谜！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x108, 135, 400)

    ChrTalk(    #439
        0x108,
        (
            "#070F#5P就是说她让我们\x01",
            "通过解谜来找到她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x101,
        (
            "#1005F#6P你、你说什么～！？\x02\x03",

            "那么她刚才也是\x01",
            "故意逃避我们的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x108,
        "#071F#5P嗯，应该是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7BAC")

    label("loc_7A94")


    ChrTalk(    #442
        0x105,
        (
            "#047F这话真有深意……\x02\x03",

            "也许这是\x01",
            "解谜的线索？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7ACC():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7ACC)

    def lambda_7ADA():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7ADA)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #443
        0x101,
        "#1020F#6P解、解谜！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    ChrTalk(    #444
        0x105,
        (
            "#542F#5P就是说她有可能\x01",
            "是希望我们通过\x01",
            "解谜来找到她……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1005F#6P你、你说什么～！？\x02\x03",

            "那么她刚才也是\x01",
            "故意逃避我们的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x105,
        (
            "#045F#5P唔……\x01",
            "应该是这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BAC")


    ChrTalk(    #447
        0x101,
        (
            "#1019F#6P好、好一个玲……\x02\x03",

            "既然她要玩这手，\x01",
            "我们也不会输！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7C28")

    ChrTalk(    #448
        0x106,
        (
            "#551F#5P我说啊……\x01",
            "现在问题不在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C53")

    label("loc_7C28")


    ChrTalk(    #449
        0x103,
        (
            "#025F#5P我说啊……\x01",
            "现在问题不在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C53")

    OP_8C(0x107, 180, 400)

    ChrTalk(    #450
        0x107,
        (
            "#067F#2P总、总之……\x02\x03",

            "线索就是『你知道哪儿有\x01",
            "没有颜色的鱼吗？』。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #451
        0x101,
        (
            "#1006F#6P嗯，在这个提示的基础上\x01",
            "我们要追查到那孩子去了哪儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x24,
        "#5P加、加油啊。\x02",
    )

    CloseMessageWindow()
    OP_43(0x24, 0x1, 0x0, 0x2E)
    OP_A2(0x1631)
    OP_28(0x8C, 0x1, 0x10)
    OP_28(0x8C, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_43_7718 end

    def Function_44_7D18(): pass

    label("Function_44_7D18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D3C")
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_44_7D18")

    label("loc_7D3C")

    Return()

    # Function_44_7D18 end

    def Function_45_7D3D(): pass

    label("Function_45_7D3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D61")
    OP_8C(0xFE, 360, 400)
    Sleep(2000)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_45_7D3D")

    label("loc_7D61")

    Return()

    # Function_45_7D3D end

    def Function_46_7D62(): pass

    label("Function_46_7D62")

    OP_8C(0x24, 270, 400)
    OP_8E(0x24, 0xA028, 0x2EE, 0x13CD6, 0x7D0, 0x0)
    SetChrFlags(0x24, 0x80)
    OP_6F(0x4, 59)
    OP_70(0x4, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_46_7D62 end

    def Function_47_7D99(): pass

    label("Function_47_7D99")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB9")
    Call(0, 99)
    Call(0, 100)
    FadeToBright(0, 0)

    label("loc_7DB9")

    Fade(1000)
    SetChrPos(0x107, 38700, 1250, 50460, 270)
    SetChrPos(0x101, 38820, 1250, 49280, 270)
    SetChrPos(0xF7, 38450, 1250, 48150, 315)
    SetChrPos(0xF9, 40210, 1250, 49430, 270)
    OP_6D(37890, 1250, 50340, 0)
    OP_67(0, 10000, -10000, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x11, 90, 0)
    SetChrSubChip(0x11, 0)
    OP_0D()

    ChrTalk(    #453
        0x101,
        (
            "#1006F『没人管就会消失的点心』……\x02\x03",

            "原来是这个啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ED8")

    ChrTalk(    #454
        0x108,
        (
            "#070F嗯，确实，没人管的话\x01",
            "就会化掉并消失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F06")

    label("loc_7ED8")


    ChrTalk(    #455
        0x105,
        (
            "#542F确实，没人管的话\x01",
            "就会化掉并消失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F06")


    ChrTalk(    #456
        0x11,
        "#5P哎呀，这不是昨天的小妹妹么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x11,
        (
            "#5P刚才你的朋友\x01",
            "还来买了冰淇淋哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x11,
        "#5P今天你们没在一起啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x107,
        (
            "#067F果然……\x02\x03",

            "#560F请问，那孩子\x01",
            "有说什么神秘兮兮的话吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x11,
        (
            "#5P神秘兮兮？\x01",
            "让我想想……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x11,
        (
            "#5P她倒是乐呵呵地说\x01",
            "『我和姐姐她们\x01",
            "约好在空港见面的』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x101,
        (
            "#1015F姐姐她们就是\x01",
            "在说我们吧。\x02\x03",

            "#1007F呼～谜题终于结束了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8091")

    ChrTalk(    #463
        0x106,
        (
            "#051F不过还真是被她\x01",
            "牵着鼻子走了一圈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80BF")

    label("loc_8091")


    ChrTalk(    #464
        0x103,
        (
            "#021F呵呵，还真是被她\x01",
            "牵着鼻子走了一圈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BF")


    ChrTalk(    #465
        0x101,
        (
            "#1019F真是的……\x01",
            "害我这么担心。\x02\x03",

            "找到她以后\x01",
            "要好好地说教一番。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #466
        0x107,
        (
            "#065F#2P姐、姐姐。\x01",
            "请不要对她发太大的脾气。\x02\x03",

            "#063F小玲一定是因为很寂寞\x01",
            "才这样做的吧。\x02\x03",

            "我们老是在说\x01",
            "工作的事……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81AD")

    ChrTalk(    #467
        0x108,
        (
            "#070F嗯……\x01",
            "也有可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81CD")

    label("loc_81AD")


    ChrTalk(    #468
        0x105,
        (
            "#045F嗯……\x01",
            "有可能是这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81CD")


    ChrTalk(    #469
        0x101,
        (
            "#1007F唔……我无可辩驳。\x02\x03",

            "#1006F好了，总之我们\x01",
            "先去空港接她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1634)
    OP_28(0x8C, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_47_7D99 end

    def Function_48_821E(): pass

    label("Function_48_821E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_822B")
    Return()

    label("loc_822B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_824B")
    Call(0, 99)
    Call(0, 100)
    FadeToBright(0, 0)

    label("loc_824B")

    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x1)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x40)
    SetChrPos(0x25, 50460, 0, 85300, 180)
    SetChrPos(0x27, 50900, 100, 87500, 180)
    OP_A1(0x27, 0x11)
    OP_72(0x11, 0x4)
    OP_71(0x11, 0x40)
    OP_71(0x11, 0x20)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_48()
    SetChrBattleFlags(0x26, 0x20)
    OP_89(0x26, 50900, 350, 87200, 270)
    Fade(1000)
    SetChrPos(0x101, 47230, 250, 72940, 0)
    SetChrPos(0x107, 46120, 250, 72830, 0)
    SetChrPos(0xF7, 47390, 250, 71550, 0)
    SetChrPos(0xF9, 46230, 250, 71360, 0)
    OP_6D(47050, 250, 72580, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #470
        0x101,
        "#1004F#5P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_8368():
        OP_6D(49820, 0, 82670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8368)

    def lambda_8380():
        OP_67(0, 8200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8380)

    def lambda_8398():
        OP_6B(1960, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8398)

    def lambda_83A8():
        OP_6C(21000, 3000)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_83A8)

    def lambda_83B8():
        OP_6E(419, 3000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_83B8)
    Sleep(1000)

    def lambda_83CD():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_83CD)
    Sleep(300)

    def lambda_83ED():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_83ED)
    OP_22(0xCF, 0x1, 0x64)
    OP_43(0x27, 0x2, 0x0, 0x35)
    WaitChrThread(0x27, 0x1)
    OP_72(0x11, 0x20)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_24(0xCF, 0x50)
    WaitChrThread(0x107, 0x2)

    ChrTalk(    #471
        0x25,
        "#692F#5P哟！\x02",
    )

    CloseMessageWindow()

    def lambda_8447():

        label("loc_8447")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8447")

    QueueWorkItem2(0x25, 2, lambda_8447)
    OP_43(0x101, 0x0, 0x0, 0x31)
    Sleep(300)
    OP_43(0x107, 0x0, 0x0, 0x32)
    OP_43(0xF7, 0x0, 0x0, 0x33)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x34)
    WaitChrThread(0xF9, 0x0)
    OP_44(0x25, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8537")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第２章见到了格斯塔夫维修长】\x01",      # 0
            "【◇没在第２章见到格斯塔夫维修长】\x01",      # 1
            "【◇什么也没有变更】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_852B"),
        (1, "loc_8531"),
        (SWITCH_DEFAULT, "loc_8537"),
    )


    label("loc_852B")

    OP_A2(0x1483)
    Jump("loc_8537")

    label("loc_8531")

    OP_A3(0x1483)
    Jump("loc_8537")

    label("loc_8537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_8653")

    ChrTalk(    #472
        0x107,
        "#064F维修长先生，还有菲小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x26,
        "#5P咦，这不是提妲么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x25,
        (
            "#693F#2P你好啊，小提妲！\x01",
            "艾丝蒂尔你们都在啊？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8603")

    ChrTalk(    #475
        0x101,
        "#1001F你好～维修长先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x106,
        (
            "#051F怎么了？\x01",
            "难得能在这里见到你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8650")

    label("loc_8603")


    ChrTalk(    #477
        0x101,
        (
            "#1001F你好～维修长先生。\x02\x03",

            "#1006F不过这是怎么了？\x01",
            "难得能在这里见到你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8650")

    Jump("loc_8739")

    label("loc_8653")


    ChrTalk(    #478
        0x107,
        "#064F维修长先生，还有菲小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x26,
        "#5P咦，这不是提妲么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x25,
        (
            "#693F#2P你好啊，小提妲！\x02\x03",

            "#691F还有……\x01",
            "好久不见了啊，艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        (
            "#1001F啊，嗯！\x01",
            "维修长你们看起来也挺精神的！\x02\x03",

            "#1006F不过这是怎么了？\x01",
            "难得能在这里见到你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8739")


    ChrTalk(    #482
        0x25,
        (
            "#691F#2P嘿嘿，我们是运送\x01",
            "这个来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x25, 315, 400)

    def lambda_876F():
        OP_6D(49350, 250, 84910, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_876F)
    Sleep(300)

    def lambda_878C():
        OP_8E(0xFE, 0xBEF0, 0xFA, 0x151E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_878C)
    Sleep(800)

    def lambda_87AC():
        OP_8E(0xFE, 0xBEAA, 0xFA, 0x14C44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87AC)
    Sleep(200)

    def lambda_87CC():
        OP_8E(0xFE, 0xBE78, 0xFA, 0x14604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_87CC)
    Sleep(200)

    def lambda_87EC():
        OP_8E(0xFE, 0xBBF8, 0xFA, 0x13F2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_87EC)
    Sleep(500)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 45, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 400)
    SetChrSubChip(0x26, 2)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 45, 400)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #483
        0x101,
        "#1004F#6P哇～这是什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0x107,
        "#064F#3P那个那个，莫非……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x25,
        (
            "#691F#4P这就是埃尔赛尤的新引擎，\x01",
            "『ＸＧ－０２』的样品？\x02\x03",

            "虽说是样品，不过\x01",
            "性能几乎和实机一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x101,
        "#1008F#6P哟～就是这个啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x107,
        (
            "#560F#3P哇～真不敢相信……\x02\x03",

            "设计得这么紧凑，竟然\x01",
            "还能提供那么强劲的马力……\x02\x03",

            "设计也兼备了功能性和可爱度……\x02\x03",

            "#067F啊～好厉害……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #488
        0x101,
        "#1016F#6P等等等等，提妲。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_89EC")

    ChrTalk(    #489
        0x106,
        (
            "#551F#6P啊……\x01",
            "又～进入忘我状态了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A18")

    label("loc_89EC")


    ChrTalk(    #490
        0x103,
        "#021F#6P呵呵……看来她已经沉醉其中了。\x02",
    )

    CloseMessageWindow()

    label("loc_8A18")

    OP_8C(0xF9, 45, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A89")

    ChrTalk(    #491
        0x108,
        (
            "#070F#6P不过，这既然是运来\x01",
            "王都的……\x02\x03",

            "就代表它是要提供给\x01",
            "共和国和帝国的样本？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AD7")

    label("loc_8A89")


    ChrTalk(    #492
        0x105,
        (
            "#040F#6P这既然是运来\x01",
            "王都的……\x02\x03",

            "就代表它是要赠送给\x01",
            "共和国和帝国的样本？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AD7")

    OP_8C(0x25, 225, 400)

    ChrTalk(    #493
        0x25,
        (
            "#691F#2P哟，你知道的还真不少。\x02\x03",

            "在埃尔赛尤上装配的\x01",
            "作业终于完成了，\x01",
            "所以就送来这边了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_8C(0xF7, 135, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D26")

    ChrTalk(    #494
        0x105,
        (
            "#048F#6P是吗……\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x25,
        (
            "#692F#2P啊、啊……？\x02\x03",

            "请问，小姐你是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x105,
        (
            "#047F#6P抱歉，这么晚才做自我介绍。\x02\x03",

            "#040F我是\x01",
            "科洛蒂娅·冯·奥赛雷丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x25,
        (
            "#692F#2P奥赛雷丝……\x01",
            "难道是王室的……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x101,
        "#1006F#5P嗯，她是女王陛下的孙女。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x105,
        (
            "#048F#6P埃尔赛尤应该算是\x01",
            "王室所有的船。\x02\x03",

            "所以我要代替陛下\x01",
            "向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x25, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #500
        0x25,
        "#692F#2P不、不胜荣幸。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x101,
        (
            "#1016F#5P哈哈，突然听到这些\x01",
            "你们会相当吃惊吧。\x02\x03",

            "#1006F话说回来，这引擎\x01",
            "要送去哪里？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D62")

    label("loc_8D26")


    ChrTalk(    #502
        0x101,
        (
            "#1006F#5P是吗，辛苦了。\x02\x03",

            "话说回来，这引擎\x01",
            "要送去哪里？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D62")

    TurnDirection(0x25, 0x101, 400)

    ChrTalk(    #503
        0x25,
        (
            "#691F#4P哦，要送往港口的仓库街。\x02\x03",

            "听说要由那边保管到\x01",
            "条约的签字仪式进行的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x101,
        "#1011F#5P哦？这样啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 135, 400)

    ChrTalk(    #505
        0x107,
        (
            "#560F#1P请问，维修长你们\x01",
            "什么时候回蔡斯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0x25,
        (
            "#691F#4P嗯，运送完这东西\x01",
            "就立刻出发。\x02\x03",

            "小提妲。\x01",
            "要乖乖的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0x107,
        (
            "#061F#1P啊，嗯。\x01",
            "维修长你们也要保重！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8F02")

    ChrTalk(    #508
        0x25,
        (
            "#691F#4P艾丝蒂尔……\x01",
            "还有那个叫阿加特的，\x02\x03",

            "小提妲就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0x101,
        "#1006F#5P嗯，请放心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x106,
        "#051F#5P好了，别担心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F4A")

    label("loc_8F02")


    ChrTalk(    #511
        0x25,
        (
            "#691F#4P艾丝蒂尔。\x01",
            "小提妲就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x101,
        "#1006F#5P嗯，请放心。\x02",
    )

    CloseMessageWindow()

    label("loc_8F4A")


    ChrTalk(    #513
        0x26,
        "#2P再见，各位游击士。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(50680, 250, 83000, 0)
    OP_67(0, 9530, -10000, 0)
    OP_6B(1780, 0)
    OP_6C(315000, 0)
    OP_6E(419, 0)
    OP_0D()
    OP_24(0xCF, 0x64)

    def lambda_8FB2():

        label("loc_8FB2")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_8FB2")

    QueueWorkItem2(0x101, 1, lambda_8FB2)

    def lambda_8FC3():

        label("loc_8FC3")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_8FC3")

    QueueWorkItem2(0x107, 1, lambda_8FC3)

    def lambda_8FD4():

        label("loc_8FD4")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_8FD4")

    QueueWorkItem2(0xF7, 1, lambda_8FD4)

    def lambda_8FE5():

        label("loc_8FE5")

        TurnDirection(0xFE, 0x25, 0)
        OP_48()
        Jump("loc_8FE5")

    QueueWorkItem2(0xF9, 1, lambda_8FE5)
    SetChrSubChip(0x26, 0)

    def lambda_8FFB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_8FFB)
    Sleep(300)

    def lambda_901B():
        OP_6D(50680, 250, 79000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_901B)

    def lambda_9033():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_9033)
    OP_43(0x27, 0x2, 0x0, 0x36)
    WaitChrThread(0x27, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    OP_71(0x11, 0x4)
    OP_6D(48760, 250, 84990, 2000)
    Sleep(500)

    ChrTalk(    #514
        0x101,
        (
            "#1008F#5P啊～那就是\x01",
            "埃尔赛尤用的引擎吗？\x02\x03",

            "虽然不太明白，\x01",
            "不过看上去是很厉害的机器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0x107,
        (
            "#560F嗯……\x01",
            "真让人吃惊。\x02\x03",

            "#061F我好想将来也能造出\x01",
            "那么了不起的机器来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_91B2")
    OP_8C(0x106, 0, 400)

    ChrTalk(    #516
        0x106,
        (
            "#551F#6P真拿你没办法……\x01",
            "你在机械方面真是一根筋。\x02\x03",

            "#051F不过有目标也是好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0x107,
        "#067F嘿嘿嘿……\x02",
    )

    CloseMessageWindow()
    Jump("loc_91D4")

    label("loc_91B2")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #518
        0x101,
        "#1017F#6P呵呵，也是。\x02",
    )

    CloseMessageWindow()

    label("loc_91D4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(48450, 250, 85560, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 48450, 250, 85560, 180)
    SetChrPos(0x1, 48450, 250, 85560, 180)
    SetChrPos(0x2, 48450, 250, 85560, 180)
    SetChrPos(0x3, 48450, 250, 85560, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1635)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_48_821E end

    def Function_49_927B(): pass

    label("Function_49_927B")

    OP_8E(0xFE, 0xBCE8, 0xFA, 0x13EB6, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_49_927B end

    def Function_50_9297(): pass

    label("Function_50_9297")

    OP_8E(0xFE, 0xB914, 0xFA, 0x13C04, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_50_9297 end

    def Function_51_92B3(): pass

    label("Function_51_92B3")

    OP_8E(0xFE, 0xBDF6, 0xFA, 0x139A2, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_51_92B3 end

    def Function_52_92CF(): pass

    label("Function_52_92CF")

    OP_8E(0xFE, 0xBA22, 0xFA, 0x13678, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_52_92CF end

    def Function_53_92EB(): pass

    label("Function_53_92EB")

    OP_24(0xCF, 0x41)
    Sleep(100)
    OP_24(0xCF, 0x46)
    Sleep(100)
    OP_24(0xCF, 0x4B)
    Sleep(100)
    OP_24(0xCF, 0x50)
    Sleep(100)
    OP_24(0xCF, 0x55)
    Sleep(100)
    OP_24(0xCF, 0x5A)
    Sleep(100)
    OP_24(0xCF, 0x5F)
    Sleep(100)
    OP_24(0xCF, 0x64)
    Return()

    # Function_53_92EB end

    def Function_54_932F(): pass

    label("Function_54_932F")

    Sleep(6500)
    OP_24(0xCF, 0x5F)
    Sleep(500)
    OP_24(0xCF, 0x5A)
    Sleep(500)
    OP_24(0xCF, 0x55)
    Sleep(500)
    OP_24(0xCF, 0x50)
    Sleep(500)
    OP_24(0xCF, 0x4B)
    Sleep(500)
    OP_24(0xCF, 0x46)
    Sleep(500)
    OP_24(0xCF, 0x41)
    Sleep(500)
    OP_23(0xCF)
    Return()

    # Function_54_932F end

    def Function_55_9377(): pass

    label("Function_55_9377")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_D2(0x700E1, 0x700E5, 0x0)
    OP_D2(0x7030A, 0x70311, 0x1)
    OP_D2(0x7030B, 0x70312, 0x2)
    OP_D2(0x7030C, 0x70313, 0x3)
    OP_D2(0x7013B, 0x7013F, 0x4)
    OP_D2(0x70530, 0x70538, 0x5)
    OP_D2(0x70531, 0x70539, 0x6)
    OP_D2(0x70532, 0x7053A, 0x7)
    OP_D2(0x2700C0, 0x2700C4, 0x8)
    OP_D2(0x7014A, 0x7014E, 0x9)
    OP_D2(0x6007B, 0x60080, 0xA)
    OP_D2(0x6007C, 0x60081, 0xB)
    OP_D2(0x290142, 0x290146, 0xC)
    OP_D2(0x29014C, 0x290150, 0xD)
    OP_D2(0x26000E, 0x260013, 0xE)
    OP_D2(0x270312, 0x27031C, 0xF)
    OP_D2(0x270315, 0x27031F, 0x10)
    OP_D2(0x270316, 0x270320, 0x11)
    OP_D2(0x70310, 0x70317, 0x12)
    OP_D3(0x13)
    OP_D2(0x60053, 0x60058, 0x13)
    OP_D3(0x14)
    OP_D2(0x290143, 0x290147, 0x14)
    OP_D2(0x290144, 0x290148, 0x15)
    OP_D2(0x29014A, 0x29014B, 0x16)
    OP_D2(0x70540, 0x70541, 0x17)
    OP_D2(0x29014D, 0x290151, 0x18)
    OP_D2(0x29014F, 0x290153, 0x19)
    OP_D2(0x29014E, 0x290152, 0x1A)
    OP_D2(0x7030F, 0x70316, 0x1B)
    OP_D2(0x70310, 0x70317, 0x1C)
    OP_D2(0x270313, 0x27031D, 0x1D)
    OP_D2(0x270314, 0x27031E, 0x1E)
    OP_D2(0x270318, 0x270322, 0x1F)
    OP_D2(0x26000D, 0x260012, 0x20)
    OP_D2(0x270326, 0x270330, 0x21)
    OP_D2(0x27032A, 0x270334, 0x22)
    OP_D2(0x270327, 0x270331, 0x23)
    OP_D2(0x270328, 0x270332, 0x24)
    OP_D2(0x27032C, 0x270336, 0x25)
    SetChrChipByIndex(0x28, 8)
    SetChrChipByIndex(0x29, 2)
    SetChrChipByIndex(0x2A, 2)
    SetChrChipByIndex(0x2B, 2)
    SetChrChipByIndex(0x2C, 2)
    SetChrChipByIndex(0x2D, 2)
    SetChrChipByIndex(0x2E, 2)
    SetChrChipByIndex(0x2F, 2)
    SetChrChipByIndex(0x30, 2)
    SetChrChipByIndex(0x31, 6)
    SetChrChipByIndex(0x32, 6)
    SetChrChipByIndex(0x33, 6)
    SetChrChipByIndex(0x34, 6)
    SetChrChipByIndex(0x35, 6)
    SetChrChipByIndex(0x36, 6)
    SetChrChipByIndex(0x37, 6)
    SetChrChipByIndex(0x38, 6)
    SetChrChipByIndex(0x49, 19)
    SetChrChipByIndex(0x4A, 19)
    SetChrChipByIndex(0x4B, 19)
    SetChrChipByIndex(0x4C, 19)
    SetChrSubChip(0x28, 0)
    SetChrSubChip(0x29, 0)
    SetChrSubChip(0x2A, 0)
    SetChrSubChip(0x2B, 0)
    SetChrSubChip(0x2C, 0)
    SetChrSubChip(0x2D, 0)
    SetChrSubChip(0x2E, 0)
    SetChrSubChip(0x2F, 0)
    SetChrSubChip(0x30, 0)
    SetChrSubChip(0x31, 0)
    SetChrSubChip(0x32, 0)
    SetChrSubChip(0x33, 0)
    SetChrSubChip(0x34, 0)
    SetChrSubChip(0x35, 0)
    SetChrSubChip(0x36, 0)
    SetChrSubChip(0x37, 0)
    SetChrSubChip(0x38, 0)
    SetChrSubChip(0x49, 0)
    SetChrSubChip(0x4A, 0)
    SetChrSubChip(0x4B, 0)
    SetChrSubChip(0x4C, 0)
    SetChrPos(0x28, 35820, 0, -960, 90)
    SetChrPos(0x29, 34250, 0, 720, 90)
    SetChrPos(0x2A, 34250, 0, -320, 90)
    SetChrPos(0x2B, 34250, 0, -1560, 90)
    SetChrPos(0x2C, 34250, 0, -2570, 90)
    SetChrPos(0x2D, 33000, 0, 720, 90)
    SetChrPos(0x2E, 33000, 0, -320, 90)
    SetChrPos(0x2F, 33000, 0, -1560, 90)
    SetChrPos(0x30, 33000, 0, -2570, 90)
    SetChrPos(0x31, 31750, 0, 720, 90)
    SetChrPos(0x32, 31750, 0, -320, 90)
    SetChrPos(0x33, 31750, 0, -1560, 90)
    SetChrPos(0x34, 31750, 0, -2570, 90)
    SetChrPos(0x35, 30500, 0, 720, 90)
    SetChrPos(0x36, 30500, 0, -320, 90)
    SetChrPos(0x37, 30500, 0, -1560, 90)
    SetChrPos(0x38, 30500, 0, -2570, 90)
    SetChrPos(0x49, 42120, 250, -7020, 90)
    SetChrPos(0x4A, 99670, 250, 40980, 180)
    SetChrPos(0x4B, 94910, 250, 44180, 90)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    OP_6D(41080, 0, -1410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(235000, 0)
    OP_6E(262, 0)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    LoadEffect(0x1, "monster\\\\msc0100.eff")
    LoadEffect(0x2, "Craft\\\\cr161_00.eff")
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    LoadEffect(0x4, "map\\\\mpsmk0.eff")
    LoadEffect(0x5, "map\\\\mpfire2.eff")
    LoadEffect(0x6, "map\\\\mpkaji0.eff")
    LoadEffect(0x7, "monster\\ms00300.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x6, 0xFF, 0xFF, 50440, 0, 64220, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 100140, 2900, 56810, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 43440, 4400, 53900, 0, 0, 0, 1200, 1400, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 73810, 4700, 56660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 63710, 4000, 48640, 0, 0, 0, 1400, 1700, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 75700, 4250, 42840, 0, 0, 0, 1600, 1900, 1600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 100140, 2400, 56810, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 43440, 3950, 53900, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 73810, 4250, 56660, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 63710, 3650, 48640, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 75700, 3750, 42840, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_C8(0x200, 0x46, "C_PLAC24._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(300)

    def lambda_9AF1():
        OP_6D(43810, 0, -2060, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9AF1)

    def lambda_9B09():
        OP_67(0, 6770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B09)

    def lambda_9B21():
        OP_6B(2200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B21)

    def lambda_9B31():
        OP_6E(368, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9B31)

    def lambda_9B41():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_9B41)
    Sleep(80)

    def lambda_9B5C():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9B5C)

    def lambda_9B72():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_9B72)

    def lambda_9B88():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_9B88)

    def lambda_9B9E():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_9B9E)
    Sleep(80)

    def lambda_9BB9():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9BB9)

    def lambda_9BCF():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_9BCF)

    def lambda_9BE5():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_9BE5)

    def lambda_9BFB():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_9BFB)
    Sleep(80)

    def lambda_9C16():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9C16)

    def lambda_9C2C():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_9C2C)

    def lambda_9C42():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_9C42)

    def lambda_9C58():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_9C58)
    Sleep(80)

    def lambda_9C73():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_9C73)

    def lambda_9C89():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_9C89)

    def lambda_9C9F():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_9C9F)

    def lambda_9CB5():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_9CB5)
    WaitChrThread(0x28, 0x1)
    OP_8C(0x28, 270, 400)
    WaitChrThread(0x35, 0x1)
    SetChrChipByIndex(0x29, 1)
    SetChrChipByIndex(0x2D, 1)
    SetChrChipByIndex(0x31, 4)
    SetChrChipByIndex(0x35, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x36, 0x1)
    SetChrChipByIndex(0x2A, 1)
    SetChrChipByIndex(0x2E, 1)
    SetChrChipByIndex(0x32, 4)
    SetChrChipByIndex(0x36, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x37, 0x1)
    SetChrChipByIndex(0x2B, 1)
    SetChrChipByIndex(0x2F, 1)
    SetChrChipByIndex(0x33, 4)
    SetChrChipByIndex(0x37, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x38, 0x1)
    SetChrChipByIndex(0x2C, 1)
    SetChrChipByIndex(0x30, 1)
    SetChrChipByIndex(0x34, 4)
    SetChrChipByIndex(0x38, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #519
        0x28,
        (
            "#1186F#6P现在开始对人形兵器和\x01",
            "猎兵团进行扫荡！\x02\x03",

            "保护市民和支援\x01",
            "正规军是我们的首要任务！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName("特务兵们")

    AnonymousTalk(    #520
        "\x07\x00#5S是，长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrChipByIndex(0x29, 2)
    SetChrChipByIndex(0x2A, 2)
    SetChrChipByIndex(0x2B, 2)
    SetChrChipByIndex(0x2C, 2)
    OP_43(0x29, 0x0, 0x0, 0x49)
    OP_43(0x2A, 0x0, 0x0, 0x4A)
    OP_43(0x2B, 0x0, 0x0, 0x4B)
    OP_43(0x2C, 0x0, 0x0, 0x4C)
    Sleep(100)
    SetChrChipByIndex(0x2D, 2)
    SetChrChipByIndex(0x2E, 2)
    SetChrChipByIndex(0x2F, 2)
    SetChrChipByIndex(0x30, 2)
    OP_43(0x2D, 0x0, 0x0, 0x49)
    OP_43(0x2E, 0x0, 0x0, 0x4A)
    OP_43(0x2F, 0x0, 0x0, 0x4B)
    OP_43(0x30, 0x0, 0x0, 0x4C)
    Sleep(100)
    SetChrChipByIndex(0x31, 6)
    SetChrChipByIndex(0x32, 6)
    SetChrChipByIndex(0x33, 6)
    SetChrChipByIndex(0x34, 6)
    OP_43(0x31, 0x0, 0x0, 0x49)
    OP_43(0x32, 0x0, 0x0, 0x4A)
    OP_43(0x33, 0x0, 0x0, 0x4B)
    OP_43(0x34, 0x0, 0x0, 0x4C)
    Sleep(100)
    SetChrChipByIndex(0x35, 6)
    SetChrChipByIndex(0x36, 6)
    SetChrChipByIndex(0x37, 6)
    SetChrChipByIndex(0x38, 6)
    OP_43(0x35, 0x0, 0x0, 0x49)
    OP_43(0x36, 0x0, 0x0, 0x4A)
    OP_43(0x37, 0x0, 0x0, 0x4B)
    OP_43(0x38, 0x0, 0x0, 0x4C)
    Sleep(100)

    def lambda_9ED1():
        OP_6D(47810, 0, -2060, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9ED1)
    OP_8C(0x28, 90, 400)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x0)
    OP_44(0x29, 0x0)
    OP_44(0x2A, 0x0)
    OP_44(0x2B, 0x0)
    OP_44(0x2C, 0x0)
    OP_44(0x2D, 0x0)
    OP_44(0x2E, 0x0)
    OP_44(0x2F, 0x0)
    OP_44(0x30, 0x0)
    OP_44(0x31, 0x0)
    OP_44(0x32, 0x0)
    OP_44(0x33, 0x0)
    OP_44(0x34, 0x0)
    OP_44(0x35, 0x0)
    OP_44(0x36, 0x0)
    OP_44(0x37, 0x0)
    OP_44(0x38, 0x0)
    OP_6D(97060, 250, 34890, 0)
    OP_67(0, 8290, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    SetChrFlags(0x43, 0x4)
    SetChrFlags(0x44, 0x4)
    SetChrFlags(0x45, 0x4)
    SetChrFlags(0x46, 0x4)
    SetChrChipByIndex(0x43, 20)
    SetChrChipByIndex(0x44, 20)
    SetChrChipByIndex(0x45, 13)
    SetChrChipByIndex(0x46, 13)
    SetChrSubChip(0x43, 0)
    SetChrSubChip(0x44, 0)
    SetChrSubChip(0x45, 0)
    SetChrSubChip(0x46, 0)
    SetChrPos(0x43, 100320, 1000, 33430, 270)
    SetChrPos(0x44, 103220, 1000, 36090, 270)
    SetChrPos(0x45, 96780, 550, 70110, 180)
    SetChrPos(0x46, 94780, 550, 70110, 180)
    SetChrPos(0x29, 95630, 250, 61420, 180)
    SetChrPos(0x31, 95850, 0, 24930, 0)
    SetChrPos(0x32, 88010, 0, 35790, 90)
    SetChrPos(0x33, 89710, 0, 40080, 90)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    SetChrFlags(0x29, 0x20)
    SetChrFlags(0x2A, 0x20)
    SetChrFlags(0x2B, 0x20)
    SetChrFlags(0x2C, 0x20)
    SetChrFlags(0x31, 0x20)
    SetChrFlags(0x32, 0x20)
    SetChrFlags(0x33, 0x20)
    SetChrFlags(0x34, 0x20)
    SetChrFlags(0x43, 0x20)

    def lambda_A095():

        label("loc_A095")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A095")

    QueueWorkItem2(0x43, 2, lambda_A095)
    OP_43(0x28, 0x3, 0x0, 0x61)

    def lambda_A0AF():
        OP_8F(0xFE, 0x16314, 0x3E8, 0x8296, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_A0AF)
    OP_43(0x43, 0x0, 0x0, 0x4D)
    Sleep(400)
    SetChrFlags(0x44, 0x20)

    def lambda_A0DB():

        label("loc_A0DB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A0DB")

    QueueWorkItem2(0x44, 2, lambda_A0DB)

    def lambda_A0EE():
        OP_8F(0xFE, 0x16CD8, 0x3E8, 0x8CFA, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_A0EE)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_A118():
        OP_6D(96790, 250, 33400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A118)

    def lambda_A130():
        OP_67(0, 5810, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A130)

    def lambda_A148():
        OP_6B(2860, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A148)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)
    OP_7D(0x0, 0x31, 0x32, 0xC8)
    ClearChrFlags(0x31, 0x20)

    def lambda_A16F():
        OP_8E(0xFE, 0x1766A, 0x0, 0x706C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_A16F)
    WaitChrThread(0x31, 0x1)
    OP_7D(0x1, 0x31, 0x0, 0x0)
    SetChrFlags(0x31, 0x20)
    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 1)

    def lambda_A1A6():
        OP_96(0xFE, 0x1766A, 0x0, 0x7E68, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_A1A6)
    Sleep(300)

    def lambda_A1C9():
        OP_99(0xFE, 0x1, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_A1C9)
    Sleep(100)

    def lambda_A1DE():
        OP_6D(96820, 250, 35080, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A1DE)
    OP_44(0x28, 0x3)
    OP_23(0x13A)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x43, 0, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x43, 0x1)
    OP_44(0x44, 0x1)
    OP_44(0x43, 0x2)
    SetChrChipByIndex(0x44, 12)
    SetChrSubChip(0x44, 0)
    SetChrChipByIndex(0x43, 12)
    SetChrSubChip(0x43, 0)

    def lambda_A268():
        OP_8C(0xFE, 220, 200)
        ExitThread()

    QueueWorkItem(0x44, 3, lambda_A268)

    def lambda_A276():
        OP_8F(0xFE, 0x17368, 0x2EE, 0x8E94, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_A276)

    def lambda_A291():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_A291)

    def lambda_A2AB():
        OP_8C(0xFE, 175, 400)
        ExitThread()

    QueueWorkItem(0x43, 3, lambda_A2AB)
    WaitChrThread(0x43, 0x1)

    def lambda_A2BE():

        label("loc_A2BE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A2BE")

    QueueWorkItem2(0x43, 2, lambda_A2BE)
    OP_44(0x44, 0x2)
    SetChrChipByIndex(0x44, 21)
    SetChrSubChip(0x44, 0)

    def lambda_A2DF():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_A2DF)
    Sleep(400)

    def lambda_A2F4():
        OP_99(0xFE, 0x2, 0x5, 0x9C4)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_A2F4)

    def lambda_A304():
        OP_8F(0xFE, 0x17A52, 0x3E8, 0x837C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_A304)
    Sleep(100)
    OP_7D(0x0, 0x31, 0x14, 0x64)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)

    def lambda_A336():
        OP_8C(0xFE, 310, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_A336)

    def lambda_A344():
        OP_96(0xFE, 0x1836C, 0xFA, 0x78A0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_A344)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x31, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x31, 0x0, 0x0)

    def lambda_A37E():
        OP_6C(55000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A37E)

    def lambda_A38E():
        OP_6B(3000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A38E)
    SetChrChipByIndex(0x32, 7)
    SetChrSubChip(0x32, 1)

    def lambda_A3A8():
        OP_96(0xFE, 0x16D78, 0x0, 0x8E94, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_A3A8)
    Sleep(300)

    def lambda_A3CB():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_A3CB)
    Sleep(200)

    def lambda_A3E0():
        OP_6D(98560, 250, 36300, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A3E0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x43, -1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)

    def lambda_A443():
        OP_8F(0xFE, 0x181B4, 0x3E8, 0x90F6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_A443)

    def lambda_A45E():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_A45E)

    def lambda_A478():
        OP_8C(0xFE, 280, 400)
        ExitThread()

    QueueWorkItem(0x43, 3, lambda_A478)
    SetChrFlags(0x33, 0x4)
    SetChrChipByIndex(0x33, 6)
    SetChrSubChip(0x33, 2)
    OP_7D(0x0, 0x33, 0x32, 0xC8)

    def lambda_A49D():
        OP_96(0xFE, 0x17AAC, 0xFA, 0x9C90, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A49D)
    WaitChrThread(0x33, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x33, 0x0, 0x0)
    OP_8C(0x33, 160, 0)

    def lambda_A4D4():
        OP_6D(99800, 250, 37640, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A4D4)

    def lambda_A4EC():
        OP_67(0, 4650, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4EC)

    def lambda_A504():
        OP_6B(3190, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A504)

    def lambda_A514():
        OP_96(0xFE, 0x18312, 0x7D0, 0x91E6, 0x9C4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A514)
    WaitChrThread(0x33, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_43(0x31, 0x0, 0x0, 0x4E)
    OP_8C(0x33, 225, 0)
    SetChrFlags(0x33, 0x800)
    SetChrChipByIndex(0x33, 23)
    SetChrSubChip(0x33, 1)

    def lambda_A559():
        OP_96(0xFE, 0x17D0E, 0xFA, 0x89B2, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A559)
    Sleep(200)

    def lambda_A57C():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_A57C)
    Sleep(200)

    def lambda_A591():
        OP_6D(98770, 250, 35640, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A591)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x44, 900, 500, 1200, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x44, 22)
    SetChrSubChip(0x44, 0)

    def lambda_A5FE():
        OP_8F(0xFE, 0x1739A, 0x2EE, 0x7D31, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_A5FE)

    def lambda_A619():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_A619)
    WaitChrThread(0x44, 0x1)
    SetChrFlags(0x32, 0x800)
    SetChrChipByIndex(0x32, 7)
    SetChrSubChip(0x32, 0)

    def lambda_A647():
        OP_96(0xFE, 0x1712E, 0x0, 0x843A, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_A647)
    OP_8C(0x32, 190, 1000)
    OP_8C(0x32, 270, 1000)
    OP_8C(0x32, 0, 1000)
    OP_8C(0x32, 90, 1000)
    Sleep(50)
    OP_8C(0x32, 190, 0)

    def lambda_A68D():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_A68D)
    Sleep(100)

    def lambda_A6A2():
        OP_6D(97710, 250, 35190, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A6A2)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x44, -500, 500, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)

    def lambda_A705():
        OP_8F(0xFE, 0x1717E, 0x2EE, 0x75BC, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_A705)

    def lambda_A720():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_A720)

    def lambda_A73A():
        OP_8C(0xFE, 190, 400)
        ExitThread()

    QueueWorkItem(0x44, 3, lambda_A73A)
    WaitChrThread(0x44, 0x1)

    def lambda_A74D():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_A74D)
    Sleep(1000)
    PlayEffect(0x1, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x1, 0x2)
    OP_44(0x44, 0x2)
    SetChrFlags(0x44, 0x80)
    OP_83(0x1, 0x0)
    WaitChrThread(0x31, 0x0)
    Sleep(600)
    OP_22(0x193, 0x0, 0x64)
    Sleep(600)
    SetChrChipByIndex(0x32, 5)
    SetChrSubChip(0x32, 0)

    def lambda_A7CE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x32, 3, lambda_A7CE)
    Sleep(50)
    SetChrChipByIndex(0x33, 5)
    SetChrSubChip(0x33, 0)

    def lambda_A7EB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x33, 3, lambda_A7EB)
    Sleep(50)
    SetChrChipByIndex(0x31, 5)
    SetChrSubChip(0x31, 0)

    def lambda_A808():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_A808)

    def lambda_A816():
        OP_6D(96430, 250, 59720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A816)

    def lambda_A82E():
        OP_67(0, 7420, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A82E)

    def lambda_A846():
        OP_6C(42000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A846)

    def lambda_A856():
        OP_6B(2630, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A856)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 2)
    SetChrChipByIndex(0x32, 23)
    SetChrSubChip(0x32, 2)
    SetChrFlags(0x32, 0x4)
    SetChrPos(0x31, 88410, 250, 51790, 75)
    SetChrPos(0x32, 102920, 1250, 51790, 255)
    SetChrChipByIndex(0x46, 24)
    SetChrSubChip(0x46, 0)
    OP_43(0x28, 0x3, 0x0, 0x62)

    def lambda_A8B7():
        OP_8E(0xFE, 0x1723C, 0x226, 0xB086, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_A8B7)
    Sleep(200)
    SetChrChipByIndex(0x45, 24)
    SetChrSubChip(0x45, 0)

    def lambda_A8E1():
        OP_8E(0xFE, 0x17A0C, 0x226, 0xB086, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_A8E1)
    Sleep(600)

    def lambda_A901():
        OP_6D(96430, 250, 52470, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A901)
    Sleep(450)
    OP_43(0x46, 0x0, 0x0, 0x4F)
    Sleep(50)
    OP_43(0x45, 0x0, 0x0, 0x50)
    WaitChrThread(0x46, 0x0)
    WaitChrThread(0x45, 0x0)
    Sleep(400)

    def lambda_A940():
        OP_6D(96010, 250, 52510, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A940)

    def lambda_A958():
        OP_6C(23000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A958)

    def lambda_A968():
        OP_6B(2530, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A968)
    SetChrChipByIndex(0x31, 5)
    SetChrSubChip(0x31, 0)

    def lambda_A982():
        OP_8C(0xFE, 355, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_A982)

    def lambda_A990():
        OP_96(0xFE, 0x1723C, 0xFA, 0xBD4C, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_A990)
    Sleep(200)
    SetChrChipByIndex(0x32, 5)
    SetChrSubChip(0x32, 0)

    def lambda_A9BD():
        OP_8C(0xFE, 355, 400)
        ExitThread()

    QueueWorkItem(0x32, 3, lambda_A9BD)

    def lambda_A9CB():
        OP_96(0xFE, 0x17A0C, 0xFA, 0xBF40, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_A9CB)
    WaitChrThread(0x31, 0x1)
    ClearChrFlags(0x31, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x32, 0x1)
    ClearChrFlags(0x32, 0x800)
    ClearChrFlags(0x32, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x46, 26)
    SetChrSubChip(0x46, 0)

    def lambda_AA16():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_AA16)
    Sleep(200)
    SetChrChipByIndex(0x45, 26)
    SetChrSubChip(0x45, 0)

    def lambda_AA35():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_AA35)
    WaitChrThread(0x45, 0x2)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x29, 0x80)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 0)

    def lambda_AA63():
        OP_6D(96010, 250, 58040, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA63)
    WaitChrThread(0x101, 0x0)
    Sleep(400)

    def lambda_AA85():
        OP_6D(96010, 250, 57370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA85)

    def lambda_AA9D():
        OP_67(0, 5360, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA9D)

    def lambda_AAB5():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AAB5)

    def lambda_AAC5():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_AAC5)
    Sleep(100)
    OP_82(0x1, 0x0)
    PlayEffect(0x7, 0x1, 0x29, -200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x45, 0, 0, -200, 0)
    Sleep(40)
    PlayEffect(0x7, 0x2, 0x29, 200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x46, 0, 0, -200, 0)
    Sleep(40)
    PlayEffect(0x7, 0x3, 0x29, -200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x45, 200, 0, 0, 0)
    Sleep(40)
    PlayEffect(0x7, 0x4, 0x29, 200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x46, -200, 0, 0, 0)
    Sleep(1300)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_43(0x46, 0x0, 0x0, 0x51)
    Sleep(50)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_43(0x45, 0x0, 0x0, 0x52)
    WaitChrThread(0x46, 0x0)
    WaitChrThread(0x45, 0x0)
    SetChrChipByIndex(0x29, 1)
    SetChrSubChip(0x29, 0)
    OP_8C(0x29, 0, 800)

    def lambda_AC15():
        OP_6B(3530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC15)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 0)
    ClearChrFlags(0x29, 0x20)

    def lambda_AC34():
        OP_8E(0xFE, 0x1758E, 0xFA, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_AC34)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)
    ClearChrFlags(0x31, 0x20)
    SetChrChipByIndex(0x32, 6)
    SetChrSubChip(0x32, 0)
    ClearChrFlags(0x32, 0x20)

    def lambda_AC6D():
        OP_8E(0xFE, 0x17A0C, 0xFA, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_AC6D)
    Sleep(100)

    def lambda_AC8D():
        OP_8E(0xFE, 0x1723C, 0xFA, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_AC8D)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadEffect(0x1, "monster\\\\msc0568.eff")
    LoadEffect(0x2, "monster\\\\msc0555.eff")
    LoadEffect(0x7, "map\\\\mp003_00.eff")
    OP_44(0x101, 0x0)
    OP_44(0x29, 0x1)
    OP_44(0x31, 0x1)
    OP_44(0x32, 0x1)
    SetChrPos(0x49, 40700, 1250, 46910, 270)
    SetChrPos(0x4A, 99670, 250, 40980, 180)
    SetChrPos(0x4B, 94910, 250, 44180, 90)
    OP_6D(70190, 1250, 52590, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(156000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x39, 29)
    SetChrChipByIndex(0x3A, 29)
    SetChrChipByIndex(0x3B, 35)
    SetChrChipByIndex(0x3C, 35)
    SetChrChipByIndex(0x3D, 35)
    SetChrChipByIndex(0x29, 0)
    SetChrChipByIndex(0x2A, 0)
    SetChrChipByIndex(0x2B, 2)
    SetChrChipByIndex(0x2C, 2)
    SetChrChipByIndex(0x2D, 2)
    SetChrChipByIndex(0x31, 4)
    SetChrSubChip(0x39, 0)
    SetChrSubChip(0x3A, 0)
    SetChrSubChip(0x3B, 0)
    SetChrSubChip(0x3C, 0)
    SetChrSubChip(0x3D, 0)
    SetChrSubChip(0x29, 0)
    SetChrSubChip(0x2A, 0)
    SetChrSubChip(0x2B, 0)
    SetChrSubChip(0x2C, 0)
    SetChrSubChip(0x2D, 0)
    SetChrSubChip(0x31, 0)
    SetChrPos(0x39, 81020, 1250, 53150, 0)
    SetChrPos(0x3A, 59440, 1250, 53150, 0)
    SetChrPos(0x3B, 70350, 1250, 33350, 0)
    SetChrPos(0x3C, 68900, 1250, 31550, 0)
    SetChrPos(0x3D, 71360, 1250, 31750, 0)
    SetChrPos(0x29, 59440, 1250, 53150, 90)
    SetChrPos(0x2A, 81020, 1250, 53150, 270)
    SetChrPos(0x2B, 70130, 1250, 35150, 0)
    SetChrPos(0x2C, 71250, 1250, 33950, 0)
    SetChrPos(0x2D, 69040, 1250, 33380, 0)
    SetChrPos(0x31, 69960, 250, 66900, 180)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x39, 0x40)
    SetChrFlags(0x3A, 0x40)
    SetChrFlags(0x3B, 0x40)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3D, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0x2B, 0x40)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x31, 0x40)

    def lambda_AF02():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF02)
    FadeToBright(1000, 0)

    def lambda_AF1B():
        OP_8E(0xFE, 0x1156C, 0x4E2, 0xCF9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_AF1B)
    Sleep(400)

    def lambda_AF3B():
        OP_8E(0xFE, 0x10F40, 0x4E2, 0xCF9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_AF3B)
    OP_0D()
    WaitChrThread(0x39, 0x1)
    SetChrChipByIndex(0x39, 14)
    SetChrSubChip(0x39, 0)
    WaitChrThread(0x3A, 0x1)
    SetChrChipByIndex(0x3A, 14)
    SetChrSubChip(0x3A, 0)
    WaitChrThread(0x101, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_43(0x29, 0x0, 0x0, 0x53)
    Sleep(400)

    def lambda_AF95():
        OP_6D(70280, 1250, 52460, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF95)

    def lambda_AFAD():
        OP_6B(2150, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFAD)
    Sleep(200)
    OP_43(0x2A, 0x0, 0x0, 0x56)
    WaitChrThread(0x29, 0x0)

    def lambda_AFCE():
        OP_6D(70160, 1250, 52920, 3400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFCE)

    def lambda_AFE6():
        OP_67(0, 11000, -10000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFE6)

    def lambda_AFFE():
        OP_6B(2340, 3400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AFFE)

    def lambda_B00E():
        OP_6C(90000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B00E)
    OP_43(0x3A, 0x0, 0x0, 0x55)
    WaitChrThread(0x2A, 0x0)
    OP_43(0x2A, 0x0, 0x0, 0x57)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x3A, 15)
    SetChrSubChip(0x3A, 0)
    SetChrPos(0x3A, 69170, 1250, 53160, 250)
    SetChrChipByIndex(0x2A, 1)
    SetChrSubChip(0x2A, 0)

    def lambda_B05B():
        OP_6D(69190, 2150, 55290, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B05B)

    def lambda_B073():
        OP_67(0, 7040, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B073)

    def lambda_B08B():
        OP_6C(46000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B08B)
    SetChrFlags(0x31, 0x800)
    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 2)

    def lambda_B0AA():
        OP_96(0xFE, 0x11148, 0x4E2, 0xD58E, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_B0AA)
    Sleep(650)

    def lambda_B0CD():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_B0CD)
    Sleep(150)
    PlayEffect(0x1, 0x1, 0xFF, 69960, 1250, 53070, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0xC8)

    def lambda_B128():
        OP_6D(69320, 2150, 48410, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B128)

    def lambda_B140():
        OP_6B(2560, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B140)

    def lambda_B150():
        OP_6C(32000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B150)
    SetChrChipByIndex(0x39, 16)
    SetChrSubChip(0x39, 0)
    OP_8C(0x39, 0, 0)

    def lambda_B171():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_B171)

    def lambda_B18B():
        OP_96(0xFE, 0x116CA, 0xFA, 0xB284, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_B18B)
    SetChrChipByIndex(0x3A, 16)
    SetChrSubChip(0x3A, 0)
    OP_8C(0x3A, 0, 0)

    def lambda_B1BA():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_B1BA)

    def lambda_B1D4():
        OP_96(0xFE, 0x10E96, 0xFA, 0xB158, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_B1D4)
    WaitChrThread(0x3A, 0x1)
    SetChrChipByIndex(0x3A, 17)
    SetChrSubChip(0x3A, 2)
    OP_43(0x3A, 0x0, 0x0, 0x38)
    WaitChrThread(0x39, 0x1)
    SetChrChipByIndex(0x39, 17)
    SetChrSubChip(0x39, 3)
    OP_43(0x39, 0x0, 0x0, 0x39)
    WaitChrThread(0x101, 0x0)

    def lambda_B223():
        OP_6D(71130, 250, 45090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B223)

    def lambda_B23B():
        OP_67(0, 9520, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B23B)

    def lambda_B253():
        OP_6B(1750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B253)

    def lambda_B263():
        OP_6C(44000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B263)

    def lambda_B273():
        OP_6E(354, 2000)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_B273)

    def lambda_B283():
        OP_8F(0xFE, 0x112CE, 0xFA, 0xAC4E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_B283)

    def lambda_B29E():
        OP_8F(0xFE, 0x10D24, 0xFA, 0xA97E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_B29E)

    def lambda_B2B9():
        OP_8F(0xFE, 0x116C0, 0xFA, 0xA7DA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_B2B9)
    WaitChrThread(0x3B, 0x1)
    SetChrChipByIndex(0x3B, 33)
    SetChrSubChip(0x3B, 0)
    WaitChrThread(0x3C, 0x1)
    SetChrChipByIndex(0x3C, 33)
    SetChrSubChip(0x3C, 0)
    WaitChrThread(0x3D, 0x1)
    SetChrChipByIndex(0x3D, 33)
    SetChrSubChip(0x3D, 0)
    WaitChrThread(0x101, 0x0)

    def lambda_B306():
        OP_6D(70780, 250, 47510, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B306)

    def lambda_B31E():
        OP_67(0, 8460, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B31E)

    def lambda_B336():
        OP_6B(2270, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B336)

    def lambda_B346():
        OP_6C(32000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B346)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 0)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)
    SetChrChipByIndex(0x2A, 2)
    SetChrSubChip(0x2A, 0)
    SetChrPos(0x29, 68800, 1250, 55030, 180)
    SetChrPos(0x31, 70040, 1250, 53370, 180)
    SetChrPos(0x2A, 71540, 1250, 55010, 180)
    ClearChrFlags(0x29, 0x20)
    ClearChrFlags(0x31, 0x20)
    ClearChrFlags(0x2A, 0x20)

    def lambda_B3B6():
        OP_8F(0xFE, 0x10CC0, 0x4E2, 0xC756, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_B3B6)

    def lambda_B3D1():
        OP_8F(0xFE, 0x11198, 0x4E2, 0xC4C2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_B3D1)

    def lambda_B3EC():
        OP_8F(0xFE, 0x11774, 0x4E2, 0xC742, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_B3EC)
    WaitChrThread(0x29, 0x1)
    SetChrChipByIndex(0x29, 1)
    SetChrSubChip(0x29, 0)
    WaitChrThread(0x31, 0x1)
    SetChrChipByIndex(0x31, 5)
    SetChrSubChip(0x31, 0)
    WaitChrThread(0x2A, 0x1)
    SetChrChipByIndex(0x2A, 1)
    SetChrSubChip(0x2A, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    OP_62(0x3D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(400)

    def lambda_B45F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3D, 3, lambda_B45F)
    Sleep(400)

    def lambda_B472():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3C, 3, lambda_B472)
    Sleep(200)

    def lambda_B485():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3B, 3, lambda_B485)
    Sleep(400)
    Fade(500)
    OP_6D(70570, 250, 40500, 0)
    OP_67(0, 8460, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(144000, 0)
    OP_6E(354, 0)
    SetChrPos(0x39, 71170, 250, 45200, 0)
    SetChrPos(0x3B, 70190, 250, 44050, 180)
    SetChrPos(0x3D, 71660, 250, 42970, 180)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2B, 0x20)
    ClearChrFlags(0x2C, 0x20)
    ClearChrFlags(0x2D, 0x20)

    def lambda_B52B():
        OP_8F(0xFE, 0x111F2, 0x4E2, 0x98EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_B52B)

    def lambda_B546():
        OP_8F(0xFE, 0x11652, 0x4E2, 0x9632, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_B546)

    def lambda_B561():
        OP_8F(0xFE, 0x10DB0, 0x4E2, 0x95EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_B561)
    WaitChrThread(0x2B, 0x1)
    SetChrChipByIndex(0x2B, 1)
    SetChrSubChip(0x2B, 0)
    WaitChrThread(0x2C, 0x1)
    SetChrChipByIndex(0x2C, 1)
    SetChrSubChip(0x2C, 0)
    WaitChrThread(0x2D, 0x1)
    SetChrChipByIndex(0x2D, 1)
    SetChrSubChip(0x2D, 0)

    def lambda_B5A9():
        OP_6D(70870, 250, 43890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B5A9)

    def lambda_B5C1():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5C1)

    def lambda_B5D1():
        OP_6C(135000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B5D1)
    SetChrChipByIndex(0x3C, 35)
    SetChrSubChip(0x3C, 0)

    def lambda_B5EB():
        OP_8F(0xFE, 0x10D24, 0xFA, 0xAAAA, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_B5EB)
    WaitChrThread(0x3C, 0x1)
    OP_44(0x3C, 0x2)
    SetChrChipByIndex(0x3C, 33)
    SetChrSubChip(0x3C, 0)
    SetChrChipByIndex(0x3D, 35)
    SetChrSubChip(0x3D, 0)

    def lambda_B623():
        OP_8F(0xFE, 0x117EC, 0xFA, 0xAA96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_B623)
    WaitChrThread(0x3D, 0x1)
    OP_44(0x3D, 0x2)
    SetChrChipByIndex(0x3D, 33)
    SetChrSubChip(0x3D, 0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_43(0x29, 0x0, 0x0, 0x3C)
    OP_43(0x2A, 0x0, 0x0, 0x3B)
    OP_43(0x31, 0x0, 0x0, 0x3A)
    OP_43(0x2B, 0x0, 0x0, 0x3D)
    OP_43(0x2C, 0x0, 0x0, 0x3E)
    OP_43(0x2D, 0x0, 0x0, 0x3F)
    OP_43(0x39, 0x0, 0x0, 0x40)
    OP_43(0x3A, 0x0, 0x0, 0x41)
    OP_43(0x3B, 0x0, 0x0, 0x42)
    OP_43(0x3C, 0x0, 0x0, 0x43)
    OP_43(0x3D, 0x0, 0x0, 0x44)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x5A)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x5A)
    Sleep(100)
    OP_22(0x84, 0x0, 0x5A)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x5A)
    Sleep(200)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x5A)
    Sleep(200)
    OP_22(0x84, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x50)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x46)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x46)
    Sleep(2000)
    OP_6D(42310, 1250, 51050, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(304000, 0)
    OP_6E(332, 0)
    SetChrChipByIndex(0x47, 9)
    SetChrChipByIndex(0x48, 10)
    SetChrPos(0x47, 43000, 1250, 50000, 90)
    SetChrPos(0x48, 43000, 1250, 51100, 90)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #521
        0x47,
        (
            "#143F#5P喂喂，是真的吗？！\x02\x03",

            "怎么特务兵\x01",
            "会突然出现！？\x02\x03",

            "而且他们似乎在\x01",
            "向『结社』发动攻击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x48,
        (
            "#151F#5P呵呵，他们一定是\x01",
            "反省之后来帮忙了吧～⊙\x02\x03",

            "这就叫作\x01",
            "洗心回面吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x47, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #523
        0x47,
        (
            "#145F#5P都回面了岂不是没意义了……\x01",
            "应该是洗心革面吧。\x02\x03",

            "#144F哎呀，无所谓了！\x02\x03",

            "终于轮到照相机\x01",
            "大显身手的时候了！\x02\x03",

            "在预定时间到来之前\x01",
            "尽情拍个够吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x48,
        "#150F#5P是，前辈！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x48, 11)
    OP_0D()
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x48, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x48, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x48, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_55_9377 end

    def Function_56_BAD1(): pass

    label("Function_56_BAD1")


    def lambda_BAD7():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_BAD7)
    Sleep(1200)
    OP_44(0x3A, 0x2)

    def lambda_BAFA():
        OP_99(0xFE, 0x2, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_BAFA)
    WaitChrThread(0x3A, 0x2)
    Return()

    # Function_56_BAD1 end

    def Function_57_BB0A(): pass

    label("Function_57_BB0A")


    def lambda_BB10():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_BB10)
    Sleep(2000)
    OP_44(0x39, 0x2)

    def lambda_BB33():
        OP_99(0xFE, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_BB33)
    WaitChrThread(0x39, 0x2)
    Return()

    # Function_57_BB0A end

    def Function_58_BB43(): pass

    label("Function_58_BB43")

    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 2)

    def lambda_BB53():
        OP_96(0xFE, 0x11198, 0xFA, 0xB4D2, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_BB53)
    Sleep(400)

    def lambda_BB76():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_BB76)
    WaitChrThread(0x31, 0x1)
    OP_22(0x84, 0x0, 0x64)
    Sleep(400)

    def lambda_BB95():
        OP_99(0xFE, 0x5, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_BB95)

    def lambda_BBA5():
        OP_96(0xFE, 0x11198, 0xFA, 0xBEB4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_BBA5)
    WaitChrThread(0x31, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BBCD():
        OP_96(0xFE, 0x11198, 0xFA, 0xAD02, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_BBCD)
    Sleep(300)

    def lambda_BBF0():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_BBF0)
    WaitChrThread(0x31, 0x1)
    Return()

    # Function_58_BB43 end

    def Function_59_BC00(): pass

    label("Function_59_BC00")

    Sleep(200)
    SetChrFlags(0x2A, 0x20)
    SetChrChipByIndex(0x2A, 2)
    SetChrSubChip(0x2A, 2)

    def lambda_BC1A():
        OP_96(0xFE, 0x117B0, 0xFA, 0xB98C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_BC1A)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BC42():
        OP_96(0xFE, 0x11E04, 0xFA, 0xB216, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_BC42)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BC6A():
        OP_96(0xFE, 0x11E86, 0xFA, 0xBA40, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_BC6A)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)
    OP_8C(0x2A, 220, 0)

    def lambda_BCA3():
        OP_8F(0xFE, 0x11864, 0xFA, 0xB31A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_BCA3)
    WaitChrThread(0x2A, 0x1)
    Return()

    # Function_59_BC00 end

    def Function_60_BCBE(): pass

    label("Function_60_BCBE")

    Sleep(600)
    SetChrFlags(0x29, 0x20)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 2)

    def lambda_BCD8():
        OP_96(0xFE, 0x10DEC, 0xFA, 0xBA2C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_BCD8)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BD00():
        OP_96(0xFE, 0x10E64, 0xFA, 0xBF68, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_BD00)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 5)

    def lambda_BD32():
        OP_8F(0xFE, 0x10E28, 0xFA, 0xB40A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_BD32)
    WaitChrThread(0x29, 0x1)
    Return()

    # Function_60_BCBE end

    def Function_61_BD4D(): pass

    label("Function_61_BD4D")

    Sleep(400)
    SetChrFlags(0x2B, 0x20)
    SetChrChipByIndex(0x2B, 2)
    SetChrSubChip(0x2B, 2)

    def lambda_BD67():
        OP_96(0xFE, 0x10CD4, 0xFA, 0xA0E6, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_BD67)
    WaitChrThread(0x2B, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BD8F():
        OP_96(0xFE, 0x11774, 0xFA, 0xA3DE, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_BD8F)
    WaitChrThread(0x2B, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BDB7():
        OP_96(0xFE, 0x111D4, 0x2EE, 0x9D58, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_BDB7)
    WaitChrThread(0x2B, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2B, 3)
    SetChrSubChip(0x2B, 5)

    def lambda_BDE9():
        OP_8F(0xFE, 0x111DE, 0xFA, 0xA8A2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_BDE9)
    WaitChrThread(0x2B, 0x1)
    Return()

    # Function_61_BD4D end

    def Function_62_BE04(): pass

    label("Function_62_BE04")

    Sleep(100)
    SetChrFlags(0x2C, 0x20)
    SetChrChipByIndex(0x2C, 2)
    SetChrSubChip(0x2C, 2)

    def lambda_BE1E():
        OP_96(0xFE, 0x11774, 0xFA, 0xA258, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_BE1E)
    WaitChrThread(0x2C, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x2C, 315, 0)

    def lambda_BE4D():
        OP_96(0xFE, 0x11D00, 0xFA, 0xA60E, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_BE4D)
    WaitChrThread(0x2C, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x2C, 225, 0)

    def lambda_BE7C():
        OP_96(0xFE, 0x11D8C, 0xFA, 0xAED8, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_BE7C)
    WaitChrThread(0x2C, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2C, 3)
    SetChrSubChip(0x2C, 5)

    def lambda_BEAE():
        OP_8F(0xFE, 0x11A44, 0xFA, 0xABAE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_BEAE)
    WaitChrThread(0x2C, 0x1)
    Return()

    # Function_62_BE04 end

    def Function_63_BEC9(): pass

    label("Function_63_BEC9")

    Sleep(600)
    SetChrFlags(0x2D, 0x20)
    SetChrChipByIndex(0x2D, 2)
    SetChrSubChip(0x2D, 2)

    def lambda_BEE3():
        OP_96(0xFE, 0x11594, 0x4E2, 0x9B78, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_BEE3)
    WaitChrThread(0x2D, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_BF0B():
        OP_96(0xFE, 0x10D6A, 0x1F4, 0x9E2A, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_BF0B)
    WaitChrThread(0x2D, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x2D, 45, 0)

    def lambda_BF3A():
        OP_96(0xFE, 0x10734, 0xFA, 0xA58C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_BF3A)
    WaitChrThread(0x2D, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2D, 3)
    SetChrSubChip(0x2D, 5)

    def lambda_BF6C():
        OP_8F(0xFE, 0x10AC2, 0xFA, 0xA910, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_BF6C)
    WaitChrThread(0x2D, 0x1)
    Return()

    # Function_63_BEC9 end

    def Function_64_BF87(): pass

    label("Function_64_BF87")

    Sleep(300)
    SetChrFlags(0x39, 0x20)
    SetChrChipByIndex(0x39, 29)
    SetChrSubChip(0x39, 2)
    OP_8C(0x39, 270, 0)

    def lambda_BFA8():
        OP_96(0xFE, 0x11CF6, 0xFA, 0xAF8C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_BFA8)
    WaitChrThread(0x39, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x39, 30)
    SetChrSubChip(0x39, 0)

    def lambda_BFDA():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_BFDA)

    def lambda_BFEA():
        OP_8F(0xFE, 0x115E4, 0xFA, 0xB130, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_BFEA)
    WaitChrThread(0x39, 0x1)
    Return()

    # Function_64_BF87 end

    def Function_65_C005(): pass

    label("Function_65_C005")

    Sleep(300)
    SetChrFlags(0x3A, 0x20)
    SetChrChipByIndex(0x3A, 29)
    SetChrSubChip(0x3A, 2)
    OP_8C(0x3A, 90, 0)

    def lambda_C026():
        OP_96(0xFE, 0x1091E, 0xFA, 0xB18A, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_C026)
    WaitChrThread(0x3A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_C04E():
        OP_96(0xFE, 0x107C0, 0xFA, 0xAADC, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_C04E)
    WaitChrThread(0x3A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x3A, 30)
    SetChrSubChip(0x3A, 0)

    def lambda_C080():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_C080)

    def lambda_C090():
        OP_8F(0xFE, 0x10E1E, 0xFA, 0xB22A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_C090)
    WaitChrThread(0x3A, 0x1)
    Return()

    # Function_65_C005 end

    def Function_66_C0AB(): pass

    label("Function_66_C0AB")

    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)
    SetChrSubChip(0xFE, 0)

    def lambda_C0C5():

        label("loc_C0C5")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_C0C5")

    QueueWorkItem2(0xFE, 2, lambda_C0C5)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(1000)
    OP_44(0xFE, 0x2)
    Return()

    # Function_66_C0AB end

    def Function_67_C1C9(): pass

    label("Function_67_C1C9")

    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)
    SetChrSubChip(0xFE, 0)

    def lambda_C1E3():

        label("loc_C1E3")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_C1E3")

    QueueWorkItem2(0xFE, 2, lambda_C1E3)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(1000)
    OP_44(0xFE, 0x2)
    Return()

    # Function_67_C1C9 end

    def Function_68_C2E7(): pass

    label("Function_68_C2E7")

    Sleep(600)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)
    SetChrSubChip(0xFE, 0)

    def lambda_C301():

        label("loc_C301")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_C301")

    QueueWorkItem2(0xFE, 2, lambda_C301)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(1000)
    OP_44(0xFE, 0x2)
    Return()

    # Function_68_C2E7 end

    def Function_69_C405(): pass

    label("Function_69_C405")

    OP_8E(0xFE, 0xB75C, 0x0, 0x532, 0x1388, 0x0)
    OP_8E(0xFE, 0xCA94, 0x0, 0x532, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_69_C405 end

    def Function_70_C433(): pass

    label("Function_70_C433")

    OP_8E(0xFE, 0xB75C, 0x0, 0x82, 0x1388, 0x0)
    OP_8E(0xFE, 0xCA62, 0x0, 0x82, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_70_C433 end

    def Function_71_C461(): pass

    label("Function_71_C461")

    OP_8E(0xFE, 0xB70C, 0x0, 0xFFFFF786, 0x1388, 0x0)
    OP_8E(0xFE, 0xBC0C, 0x0, 0xFFFFF966, 0x1388, 0x0)
    OP_8E(0xFE, 0xD4E4, 0x0, 0xFFFFF966, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_71_C461 end

    def Function_72_C4A3(): pass

    label("Function_72_C4A3")

    OP_8E(0xFE, 0xB70C, 0x0, 0xFFFFF312, 0x1388, 0x0)
    OP_8E(0xFE, 0xBC0C, 0x0, 0xFFFFF4DE, 0x1388, 0x0)
    OP_8E(0xFE, 0xD4E4, 0x0, 0xFFFFF4DE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_72_C4A3 end

    def Function_73_C4E5(): pass

    label("Function_73_C4E5")

    OP_8E(0xFE, 0xBF2C, 0x0, 0x65E, 0x1388, 0x0)
    OP_8E(0xFE, 0xC7BA, 0x0, 0xC8A, 0x1388, 0x0)
    OP_8E(0xFE, 0xCC74, 0x0, 0x15C2, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_73_C4E5 end

    def Function_74_C527(): pass

    label("Function_74_C527")

    OP_8E(0xFE, 0xBBC6, 0x0, 0xC8, 0x1388, 0x0)
    OP_8E(0xFE, 0xCB16, 0x0, 0x35C, 0x1388, 0x0)
    OP_8E(0xFE, 0xE448, 0x0, 0x35C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_74_C527 end

    def Function_75_C569(): pass

    label("Function_75_C569")

    OP_8E(0xFE, 0xBB62, 0x0, 0xFFFFF79A, 0x1388, 0x0)
    OP_8E(0xFE, 0xCA94, 0x0, 0xFFFFF4FC, 0x1388, 0x0)
    OP_8E(0xFE, 0xE3F8, 0x0, 0xFFFFF4FC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_75_C569 end

    def Function_76_C5AB(): pass

    label("Function_76_C5AB")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xB676, 0x0, 0xFFFFF164, 0x1388, 0x0)
    OP_8E(0xFE, 0xCF08, 0xFA, 0xFFFFE8FE, 0x1388, 0x0)
    OP_8E(0xFE, 0xDEF8, 0xFA, 0xFFFFE5D4, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_76_C5AB end

    def Function_77_C5F7(): pass

    label("Function_77_C5F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x178F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C60D")
    Sleep(15)
    Jump("Function_77_C5F7")

    label("loc_C60D")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x2EE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C61E():
        OP_8F(0xFE, 0x16314, 0x2EE, 0x8296, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C61E)
    Return()

    # Function_77_C5F7 end

    def Function_78_C634(): pass

    label("Function_78_C634")

    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 6)
    OP_7D(0x0, 0x31, 0x32, 0x64)

    def lambda_C64C():
        OP_8C(0xFE, 280, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_C64C)

    def lambda_C65A():
        OP_96(0xFE, 0x18D76, 0xFA, 0x8160, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_C65A)
    WaitChrThread(0x31, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x31, 0x0, 0x0)
    SetChrChipByIndex(0x31, 7)
    SetChrSubChip(0x31, 1)

    def lambda_C694():
        OP_96(0xFE, 0x184A2, 0xFA, 0x8B92, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_C694)
    Sleep(200)

    def lambda_C6B7():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_C6B7)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x43, 500, 500, -1200, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x43, 22)
    SetChrSubChip(0x43, 0)

    def lambda_C721():
        OP_8F(0xFE, 0x1780E, 0x2EE, 0x9448, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_C721)

    def lambda_C73C():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_C73C)
    WaitChrThread(0x43, 0x1)

    def lambda_C75B():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_C75B)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x1, 0x2)
    OP_44(0x43, 0x2)
    SetChrFlags(0x43, 0x80)
    OP_83(0x1, 0x0)
    Return()

    # Function_78_C634 end

    def Function_79_C7B9(): pass

    label("Function_79_C7B9")


    def lambda_C7BF():
        OP_96(0xFE, 0x16D8C, 0x0, 0xCA4E, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_C7BF)
    Sleep(400)

    def lambda_C7E2():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_C7E2)
    Sleep(200)
    OP_44(0x46, 0x1)
    OP_44(0x28, 0x3)
    OP_23(0x13F)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x31, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrFlags(0x46, 0x20)
    SetChrChipByIndex(0x46, 25)
    SetChrSubChip(0x46, 0)

    def lambda_C85C():
        OP_8F(0xFE, 0x1723C, 0x226, 0xD3D6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_C85C)

    def lambda_C877():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_C877)
    WaitChrThread(0x46, 0x1)
    Return()

    # Function_79_C7B9 end

    def Function_80_C891(): pass

    label("Function_80_C891")


    def lambda_C897():
        OP_96(0xFE, 0x17EBC, 0x0, 0xCA4E, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_C897)
    Sleep(550)

    def lambda_C8BA():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_C8BA)
    Sleep(200)
    OP_44(0x45, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x32, -1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrFlags(0x45, 0x20)
    SetChrChipByIndex(0x45, 25)
    SetChrSubChip(0x45, 0)

    def lambda_C92D():
        OP_8F(0xFE, 0x17A0C, 0x226, 0xCFEE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_C92D)

    def lambda_C948():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_C948)
    WaitChrThread(0x45, 0x1)
    Return()

    # Function_80_C891 end

    def Function_81_C962(): pass

    label("Function_81_C962")

    SetChrChipByIndex(0x46, 25)
    SetChrSubChip(0x46, 0)

    def lambda_C972():
        OP_9E(0xFE, 0x3C, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_C972)
    WaitChrThread(0x46, 0x2)

    def lambda_C991():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_C991)
    Sleep(1000)
    PlayEffect(0x1, 0x5, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x5, 0x2)
    OP_44(0x46, 0x2)
    SetChrFlags(0x46, 0x80)
    OP_83(0x5, 0x0)
    Return()

    # Function_81_C962 end

    def Function_82_C9EF(): pass

    label("Function_82_C9EF")

    SetChrChipByIndex(0x45, 25)
    SetChrSubChip(0x45, 0)

    def lambda_C9FF():
        OP_9E(0xFE, 0x3C, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_C9FF)
    WaitChrThread(0x45, 0x2)

    def lambda_CA1E():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_CA1E)
    Sleep(1200)
    PlayEffect(0x1, 0x6, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x6, 0x2)
    OP_44(0x45, 0x2)
    SetChrFlags(0x45, 0x80)
    OP_83(0x6, 0x0)
    Return()

    # Function_82_C9EF end

    def Function_83_CA7C(): pass

    label("Function_83_CA7C")

    OP_7D(0x0, 0x29, 0x14, 0x64)

    def lambda_CA8A():
        OP_96(0xFE, 0xFDFB, 0x4E2, 0xC6AC, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CA8A)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_CAB2():
        OP_8C(0xFE, 250, 300)
        ExitThread()

    QueueWorkItem(0x3A, 3, lambda_CAB2)
    OP_8C(0x29, 20, 0)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 0)

    def lambda_CAD1():
        OP_96(0xFE, 0x10B94, 0x4E2, 0xCD32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CAD1)
    Sleep(200)

    def lambda_CAF4():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_CAF4)
    WaitChrThread(0x29, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x3A, -500, 500, -500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_7D(0x1, 0x29, 0x0, 0x0)
    SetChrChipByIndex(0x3A, 17)
    SetChrSubChip(0x3A, 1)
    OP_44(0x3A, 0x3)
    OP_8C(0x3A, 200, 0)
    SetChrFlags(0x3A, 0x20)

    def lambda_CB76():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_CB76)

    def lambda_CB90():
        OP_8F(0xFE, 0x11008, 0x4E2, 0xD066, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_CB90)
    WaitChrThread(0x3A, 0x1)
    Return()

    # Function_83_CA7C end

    def Function_84_CBAB(): pass

    label("Function_84_CBAB")

    OP_7D(0x0, 0x29, 0x14, 0x64)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 6)

    def lambda_CBC3():
        OP_96(0xFE, 0x10806, 0x4E2, 0xC8E6, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CBC3)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_CBEB():
        OP_8C(0xFE, 340, 400)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_CBEB)

    def lambda_CBF9():
        OP_96(0xFE, 0x11242, 0x4E2, 0xC8E6, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CBF9)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_CC21():
        OP_8C(0xFE, 160, 400)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_CC21)

    def lambda_CC2F():
        OP_96(0xFE, 0x10996, 0x4E2, 0xD804, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CC2F)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x29, 0x0, 0x0)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 5)

    def lambda_CC69():
        OP_8F(0xFE, 0x10CE8, 0x4E2, 0xD188, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CC69)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x29, 500, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x3A, 31)
    SetChrSubChip(0x3A, 0)
    OP_8C(0x3A, 340, 0)

    def lambda_CCE5():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_CCE5)

    def lambda_CCFF():
        OP_96(0xFE, 0x11238, 0x4E2, 0xC832, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_CCFF)
    WaitChrThread(0x3A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x3A, 30)
    SetChrSubChip(0x3A, 0)

    def lambda_CD31():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_CD31)
    WaitChrThread(0x3A, 0x2)
    OP_7D(0x0, 0x29, 0x14, 0x64)
    SetChrChipByIndex(0x29, 1)
    SetChrSubChip(0x29, 2)

    def lambda_CD58():
        OP_8C(0xFE, 80, 400)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_CD58)

    def lambda_CD66():
        OP_96(0xFE, 0x104DC, 0x4E2, 0xCFDA, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_CD66)

    def lambda_CD84():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_CD84)

    def lambda_CD94():
        OP_8F(0xFE, 0x10F04, 0x4E2, 0xCEF4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_CD94)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x29, 0x0, 0x0)
    Return()

    # Function_84_CBAB end

    def Function_85_CDC6(): pass

    label("Function_85_CDC6")

    Sleep(400)
    SetChrFlags(0x3A, 0x20)
    SetChrChipByIndex(0x3A, 30)
    SetChrSubChip(0x3A, 0)

    def lambda_CDE0():
        OP_96(0xFE, 0x113A0, 0x4E2, 0xD570, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_CDE0)

    def lambda_CDFE():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_CDFE)
    WaitChrThread(0x3A, 0x1)
    OP_43(0x29, 0x0, 0x0, 0x54)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_CE1F():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_CE1F)

    def lambda_CE2F():
        OP_8F(0xFE, 0x10E32, 0x4E2, 0xD110, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_CE2F)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_85_CDC6 end

    def Function_86_CE4F(): pass

    label("Function_86_CE4F")

    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)
    OP_7D(0x0, 0x2A, 0x14, 0xC8)

    def lambda_CE67():
        OP_8F(0xFE, 0x11A4E, 0x4E2, 0xCF9E, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_CE67)
    Sleep(100)

    def lambda_CE87():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_CE87)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_7D(0x1, 0x2A, 0x0, 0x0)
    SetChrChipByIndex(0x39, 15)
    SetChrSubChip(0x39, 0)
    OP_44(0x39, 0x3)
    OP_8C(0x39, 100, 0)

    def lambda_CF02():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_CF02)

    def lambda_CF1C():
        OP_8F(0xFE, 0x114A4, 0x4E2, 0xCF9E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_CF1C)
    WaitChrThread(0x39, 0x1)
    Return()

    # Function_86_CE4F end

    def Function_87_CF37(): pass

    label("Function_87_CF37")


    def lambda_CF3D():
        OP_8F(0xFE, 0x11634, 0x4E2, 0xCF9E, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_CF3D)

    def lambda_CF58():
        OP_8F(0xFE, 0x11BDE, 0x4E2, 0xCF9E, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_CF58)

    def lambda_CF73():
        OP_9E(0xFE, 0x3C, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_CF73)

    def lambda_CF8D():
        OP_9E(0xFE, 0x3C, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_CF8D)
    WaitChrThread(0x39, 0x1)
    OP_44(0x39, 0x2)
    WaitChrThread(0x2A, 0x1)
    OP_44(0x2A, 0x2)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x39, 30)
    SetChrSubChip(0x39, 7)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x2A, 2)
    WaitChrThread(0x2A, 0x2)

    def lambda_D007():
        OP_96(0xFE, 0x12386, 0x4E2, 0xCF8A, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D007)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)
    OP_7D(0x0, 0x2A, 0x14, 0xC8)

    def lambda_D041():
        OP_8F(0xFE, 0x11BDE, 0x4E2, 0xCF9E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D041)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_7D(0x1, 0x2A, 0x0, 0x0)
    SetChrChipByIndex(0x39, 15)
    WaitChrThread(0x39, 0x0)

    def lambda_D0BE():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_D0BE)

    def lambda_D0D8():
        OP_8F(0xFE, 0x11314, 0x4E2, 0xCF9E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_D0D8)
    WaitChrThread(0x39, 0x1)
    Sleep(200)

    def lambda_D0FD():
        OP_8C(0xFE, 160, 400)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_D0FD)

    def lambda_D10B():
        OP_96(0xFE, 0x116E8, 0x4E2, 0xD6EC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_D10B)
    WaitChrThread(0x39, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x39, 30)
    SetChrSubChip(0x39, 3)

    def lambda_D13D():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_D13D)

    def lambda_D14D():
        OP_96(0xFE, 0x119AE, 0x4E2, 0xD1A6, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_D14D)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x2A, 27)
    SetChrSubChip(0x2A, 0)
    OP_8C(0x2A, 340, 0)

    def lambda_D1CC():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_D1CC)

    def lambda_D1E6():
        OP_8F(0xFE, 0x11FEE, 0x4E2, 0xC7A6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D1E6)
    WaitChrThread(0x2A, 0x1)
    Sleep(200)
    OP_7D(0x0, 0x2A, 0x14, 0xC8)

    def lambda_D213():
        OP_8C(0xFE, 250, 400)
        ExitThread()

    QueueWorkItem(0x2A, 3, lambda_D213)

    def lambda_D221():
        OP_96(0xFE, 0x1255C, 0x4E2, 0xCFDA, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D221)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)

    def lambda_D253():
        OP_8F(0xFE, 0x11D0A, 0x4E2, 0xCFDA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_D253)
    SetChrChipByIndex(0x39, 15)
    WaitChrThread(0x39, 0x0)

    def lambda_D278():
        OP_8C(0xFE, 70, 400)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_D278)

    def lambda_D286():
        OP_96(0xFE, 0x112A6, 0x4E2, 0xCFA8, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_D286)
    WaitChrThread(0x2A, 0x1)
    OP_7D(0x1, 0x2A, 0x0, 0x0)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_87_CF37 end

    def Function_88_D2B1(): pass

    label("Function_88_D2B1")


    def lambda_D2B7():

        label("loc_D2B7")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D2B7")

    QueueWorkItem2(0x43, 0, lambda_D2B7)

    def lambda_D2CA():

        label("loc_D2CA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_D2CA")

    QueueWorkItem2(0x44, 0, lambda_D2CA)

    def lambda_D2DD():
        OP_8E(0xFE, 0x188E4, 0xFA, 0x7800, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_D2DD)
    Sleep(100)

    def lambda_D2FD():
        OP_8E(0xFE, 0x183E4, 0xFA, 0x7D5A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_D2FD)
    Sleep(200)
    OP_8C(0x43, 225, 400)
    WaitChrThread(0x2B, 0x1)
    OP_8C(0x2B, 0, 400)
    SetChrChipByIndex(0x2B, 7)
    WaitChrThread(0x2C, 0x1)
    OP_8C(0x2C, 90, 400)
    SetChrChipByIndex(0x2C, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2B, 0x0, 0x7, 0xBB8)

    def lambda_D389():
        OP_9E(0x43, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_D389)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2C, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2B, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2C, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x0, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_D4A6():
        OP_96(0xFE, 0x188F8, 0xFA, 0x7364, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_D4A6)
    Sleep(100)

    def lambda_D4C9():
        OP_96(0xFE, 0x17FCA, 0xFA, 0x7D00, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_D4C9)
    WaitChrThread(0x2B, 0x1)
    SetChrChipByIndex(0x2B, 5)
    WaitChrThread(0x2C, 0x1)
    SetChrChipByIndex(0x2C, 5)
    OP_83(0x0, 0x2)
    SetChrFlags(0x43, 0x80)
    Return()

    # Function_88_D2B1 end

    def Function_89_D4FE(): pass

    label("Function_89_D4FE")


    def lambda_D504():
        OP_8E(0xFE, 0x1848E, 0xFA, 0x899E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_D504)
    Sleep(100)

    def lambda_D524():
        OP_8E(0xFE, 0x184C0, 0xFA, 0x8548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_D524)
    Sleep(200)
    WaitChrThread(0x2F, 0x1)
    OP_8C(0x2F, 90, 400)
    SetChrChipByIndex(0x2F, 7)
    WaitChrThread(0x30, 0x1)
    OP_8C(0x30, 90, 400)
    SetChrChipByIndex(0x30, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2F, 0x0, 0x7, 0xBB8)

    def lambda_D5A9():
        OP_9E(0x44, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_D5A9)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x30, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2F, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x30, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_D6C6():
        OP_96(0xFE, 0x180EC, 0xFA, 0x894E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_D6C6)
    Sleep(100)

    def lambda_D6E9():
        OP_96(0xFE, 0x18146, 0xFA, 0x8552, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_D6E9)
    WaitChrThread(0x2F, 0x1)
    SetChrChipByIndex(0x2F, 5)
    WaitChrThread(0x30, 0x1)
    SetChrChipByIndex(0x30, 5)
    OP_83(0x2, 0x2)
    SetChrFlags(0x44, 0x80)
    Return()

    # Function_89_D4FE end

    def Function_90_D71E(): pass

    label("Function_90_D71E")


    def lambda_D724():
        OP_8E(0xFE, 0x17BC4, 0xFA, 0x9178, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_D724)
    Sleep(100)

    def lambda_D744():
        OP_8E(0xFE, 0x17CB4, 0xFA, 0x8C50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_D744)
    Sleep(200)
    OP_8C(0x45, 270, 400)
    WaitChrThread(0x33, 0x1)
    OP_8C(0x33, 90, 400)
    SetChrChipByIndex(0x33, 7)
    WaitChrThread(0x34, 0x1)
    OP_8C(0x34, 45, 400)
    SetChrChipByIndex(0x34, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x33, 0x0, 0x7, 0xBB8)

    def lambda_D7D0():
        OP_9E(0x45, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_D7D0)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x34, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x33, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x34, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x4, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_D8ED():
        OP_96(0xFE, 0x178A4, 0x0, 0x91E6, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_D8ED)
    Sleep(100)

    def lambda_D910():
        OP_96(0xFE, 0x17A48, 0xFA, 0x89B2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_D910)
    WaitChrThread(0x33, 0x1)
    SetChrChipByIndex(0x33, 5)
    WaitChrThread(0x34, 0x1)
    SetChrChipByIndex(0x34, 5)
    OP_83(0x4, 0x2)
    SetChrFlags(0x45, 0x80)
    Return()

    # Function_90_D71E end

    def Function_91_D945(): pass

    label("Function_91_D945")


    def lambda_D94B():
        OP_8E(0xFE, 0x173E0, 0x0, 0x8110, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_D94B)
    Sleep(100)

    def lambda_D96B():
        OP_8E(0xFE, 0x16E7C, 0x0, 0x85A2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_D96B)
    Sleep(200)
    OP_8C(0x46, 180, 400)
    WaitChrThread(0x38, 0x1)
    OP_8C(0x38, 0, 400)
    SetChrChipByIndex(0x38, 7)
    WaitChrThread(0x37, 0x1)
    OP_8C(0x37, 90, 400)
    SetChrChipByIndex(0x37, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x38, 0x0, 0x7, 0xBB8)

    def lambda_D9F7():
        OP_9E(0x46, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_D9F7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x7, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x37, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x38, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x7, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x37, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x6, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_DB14():
        OP_96(0xFE, 0x17426, 0x0, 0x7DD2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_DB14)
    Sleep(100)

    def lambda_DB37():
        OP_96(0xFE, 0x16AB2, 0x0, 0x858E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_DB37)
    WaitChrThread(0x38, 0x1)
    SetChrChipByIndex(0x38, 5)
    WaitChrThread(0x37, 0x1)
    SetChrChipByIndex(0x37, 5)
    OP_83(0x6, 0x2)
    SetChrFlags(0x46, 0x80)
    Return()

    # Function_91_D945 end

    def Function_92_DB6C(): pass

    label("Function_92_DB6C")

    OP_8E(0x2E, 0x11116, 0xFA, 0xAAE6, 0x1388, 0x0)
    SetChrChipByIndex(0x2E, 3)
    OP_8C(0x2E, 90, 400)
    OP_99(0x2E, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x0, 0x3D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x3D, 17)

    def lambda_DBD5():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_DBD5)
    OP_8C(0x2E, 270, 400)
    OP_99(0x2E, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x1, 0x3E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x3E, 17)

    def lambda_DC2F():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_DC2F)
    Return()

    # Function_92_DB6C end

    def Function_93_DC3A(): pass

    label("Function_93_DC3A")

    OP_8E(0x31, 0x1147C, 0xFA, 0xA79E, 0x1388, 0x0)
    SetChrChipByIndex(0x31, 3)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x3D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x31, 0x0, 0x7, 0xBB8)

    def lambda_DC9C():
        OP_9E(0x3D, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_DC9C)
    Return()

    # Function_93_DC3A end

    def Function_94_DCB1(): pass

    label("Function_94_DCB1")

    OP_8E(0x32, 0x10DCE, 0xFA, 0xA79E, 0x1388, 0x0)
    SetChrChipByIndex(0x32, 3)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0x3E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x32, 0x0, 0x7, 0xBB8)

    def lambda_DD13():
        OP_9E(0x3E, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_DD13)
    Return()

    # Function_94_DCB1 end

    def Function_95_DD28(): pass

    label("Function_95_DD28")

    OP_8E(0x35, 0x117BA, 0xFA, 0xAFDC, 0x1388, 0x0)
    SetChrChipByIndex(0x35, 3)
    OP_8C(0x35, 315, 400)
    OP_99(0x35, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x4, 0x3B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_DD8C():
        OP_9E(0x3B, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_DD8C)
    SetChrChipByIndex(0x3B, 17)

    def lambda_DDAB():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_DDAB)
    Return()

    # Function_95_DD28 end

    def Function_96_DDB6(): pass

    label("Function_96_DDB6")

    OP_8E(0x36, 0x10AF4, 0xFA, 0xB004, 0x1388, 0x0)
    SetChrChipByIndex(0x36, 3)
    OP_8C(0x36, 45, 400)
    OP_99(0x36, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x5, 0x3C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_DE1A():
        OP_9E(0x3C, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_DE1A)
    SetChrChipByIndex(0x3C, 17)

    def lambda_DE39():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_DE39)
    Return()

    # Function_96_DDB6 end

    def Function_97_DE44(): pass

    label("Function_97_DE44")

    Sleep(200)

    label("loc_DE49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE67")
    OP_22(0x13A, 0x0, 0x64)
    Sleep(200)
    OP_23(0x13A)
    Sleep(200)
    Jump("loc_DE49")

    label("loc_DE67")

    Return()

    # Function_97_DE44 end

    def Function_98_DE68(): pass

    label("Function_98_DE68")

    Sleep(150)

    label("loc_DE6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE8D")
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(300)
    Jump("loc_DE6D")

    label("loc_DE8D")

    Return()

    # Function_98_DE68 end

    def Function_99_DE8E(): pass

    label("Function_99_DE8E")

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
        (0, "loc_DF0B"),
        (1, "loc_DF11"),
        (SWITCH_DEFAULT, "loc_DF17"),
    )


    label("loc_DF0B")

    OP_A2(0x1200)
    Jump("loc_DF17")

    label("loc_DF11")

    OP_A2(0x1201)
    Jump("loc_DF17")

    label("loc_DF17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DF25")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_DF29")

    label("loc_DF25")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_DF29")

    Return()

    # Function_99_DE8E end

    def Function_100_DF2A(): pass

    label("Function_100_DF2A")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    OP_6D(22110, 0, 124540, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DF7A")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_DF94")

    label("loc_DF7A")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_DF94")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_100_DF2A end

    def Function_101_DFB4(): pass

    label("Function_101_DFB4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #525
        (
            "\x07\x05导力式时钟２号机\x01",
            "　七耀历１１６３年·由蔡斯技术工房制造\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_101_DFB4 end

    def Function_102_E016(): pass

    label("Function_102_E016")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #526
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_102_E016 end

    def Function_103_E05C(): pass

    label("Function_103_E05C")

    SetPlaceName(0xBA)
    Return()

    # Function_103_E05C end

    def Function_104_E060(): pass

    label("Function_104_E060")

    SetPlaceName(0xB1)
    Return()

    # Function_104_E060 end

    def Function_105_E064(): pass

    label("Function_105_E064")

    SetPlaceName(0xBB)
    Return()

    # Function_105_E064 end

    def Function_106_E068(): pass

    label("Function_106_E068")

    SetPlaceName(0xBC)
    Return()

    # Function_106_E068 end

    def Function_107_E06C(): pass

    label("Function_107_E06C")

    SetPlaceName(0xBD)
    Return()

    # Function_107_E06C end

    def Function_108_E070(): pass

    label("Function_108_E070")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_108_E070 end

    SaveToFile()

Try(main)
