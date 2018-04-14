from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1103   ._SN',
        MapName             = 'Bose',
        Location            = 'T1103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1103_1 ._SN',
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
        '剑帝莱维',                             # 9
        '卢格兰老人',                           # 10
        '泊尔',                                 # 11
        '市民',                                 # 12
        '市民',                                 # 13
        '市民',                                 # 14
        '市民',                                 # 15
        '市民',                                 # 16
        '市民',                                 # 17
        '市民',                                 # 18
        '市民',                                 # 19
        '市民',                                 # 20
        '市民',                                 # 21
        '市民',                                 # 22
        '市民',                                 # 23
        '市民',                                 # 24
        '市民',                                 # 25
        '市民',                                 # 26
        '市民',                                 # 27
        '梅贝尔市长',                           # 28
        '士兵',                                 # 29
        '士兵',                                 # 30
        '士兵',                                 # 31
        '士兵',                                 # 32
        '古代龙',                               # 33
        '龙',                                   # 34
        '卡洛',                                 # 35
        '刚茨',                                 # 36
        '龙谷',                                 # 37
        '阿尔丹',                               # 38
        '博尔德',                               # 39
        '特里诺',                               # 40
        '巴克',                                 # 41
        '丽露露',                               # 42
        '格蕾娅',                               # 43
        '科尔娜',                               # 44
        '雅哈多老人',                           # 45
        '雷塔',                                 # 46
        '法娜',                                 # 47
        '王国军士官',                           # 48
        '王国军士兵',                           # 49
        '王国军士兵',                           # 50
        '王国军士兵',                           # 51
        '哈里',                                 # 52
        '米娜',                                 # 53
        '奥维德',                               # 54
        '木匠',                                 # 55
        '木匠',                                 # 56
        '木匠',                                 # 57
        '木匠',                                 # 58
        '木匠',                                 # 59
        '青年管家',                             # 60
        '玛依森老人',                           # 61
        '西柏斯街道方向',                       # 62
        '东柏斯街道方向',                       # 63
        '柏斯市·南街区',                       # 64
        '柏斯国际空港',                         # 65
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
        'ED6_DT07/CH02040 ._CH',             # 00
        'ED6_DT07/CH02380 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01570 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01690 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01150 ._CH',             # 0A
        'ED6_DT07/CH02360 ._CH',             # 0B
        'ED6_DT07/CH01300 ._CH',             # 0C
        'ED6_DT26/CH20363 ._CH',             # 0D
        'ED6_DT07/CH01030 ._CH',             # 0E
        'ED6_DT07/CH01270 ._CH',             # 0F
        'ED6_DT07/CH01660 ._CH',             # 10
        'ED6_DT07/CH01040 ._CH',             # 11
        'ED6_DT07/CH01680 ._CH',             # 12
        'ED6_DT07/CH01200 ._CH',             # 13
        'ED6_DT07/CH01140 ._CH',             # 14
        'ED6_DT07/CH01070 ._CH',             # 15
        'ED6_DT07/CH01150 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
        'ED6_DT07/CH01000 ._CH',             # 18
        'ED6_DT07/CH01040 ._CH',             # 19
        'ED6_DT07/CH01050 ._CH',             # 1A
        'ED6_DT07/CH01600 ._CH',             # 1B
        'ED6_DT07/CH01640 ._CH',             # 1C
        'ED6_DT07/CH01160 ._CH',             # 1D
        'ED6_DT07/CH01170 ._CH',             # 1E
        'ED6_DT07/CH01120 ._CH',             # 1F
        'ED6_DT07/CH01500 ._CH',             # 20
        'ED6_DT26/CH20243 ._CH',             # 21
        'ED6_DT27/CH04540 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
        'ED6_DT07/CH02380P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01570P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01690P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01150P._CP',             # 0A
        'ED6_DT07/CH02360P._CP',             # 0B
        'ED6_DT07/CH01300P._CP',             # 0C
        'ED6_DT26/CH20363P._CP',             # 0D
        'ED6_DT07/CH01030P._CP',             # 0E
        'ED6_DT07/CH01270P._CP',             # 0F
        'ED6_DT07/CH01660P._CP',             # 10
        'ED6_DT07/CH01040P._CP',             # 11
        'ED6_DT07/CH01680P._CP',             # 12
        'ED6_DT07/CH01200P._CP',             # 13
        'ED6_DT07/CH01140P._CP',             # 14
        'ED6_DT07/CH01070P._CP',             # 15
        'ED6_DT07/CH01150P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
        'ED6_DT07/CH01000P._CP',             # 18
        'ED6_DT07/CH01040P._CP',             # 19
        'ED6_DT07/CH01050P._CP',             # 1A
        'ED6_DT07/CH01600P._CP',             # 1B
        'ED6_DT07/CH01640P._CP',             # 1C
        'ED6_DT07/CH01160P._CP',             # 1D
        'ED6_DT07/CH01170P._CP',             # 1E
        'ED6_DT07/CH01120P._CP',             # 1F
        'ED6_DT07/CH01500P._CP',             # 20
        'ED6_DT26/CH20243P._CP',             # 21
        'ED6_DT27/CH04540P._CP',             # 22
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63800,
        Z                   = 0,
        Y                   = 43560,
        Direction           = 321,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29530,
        Z                   = 0,
        Y                   = 76910,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 37770,
        Z                   = 0,
        Y                   = 73470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 44080,
        Z                   = 0,
        Y                   = 76420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48620,
        Z                   = 0,
        Y                   = 81230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 42290,
        Z                   = 0,
        Y                   = 44430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 44100,
        Z                   = 0,
        Y                   = 42920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 61700,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 66890,
        Z                   = 0,
        Y                   = 49260,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 46080,
        Z                   = 0,
        Y                   = 42060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 68260,
        Z                   = 0,
        Y                   = 52310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 41990,
        Z                   = 0,
        Y                   = 46350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 0,
        Y                   = 47610,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 46060,
        Z                   = 0,
        Y                   = 77320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 72340,
        Z                   = 0,
        Y                   = 63740,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 22580,
        Z                   = 0,
        Y                   = 48730,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 45370,
        Z                   = 0,
        Y                   = 78340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 30140,
        Z                   = 0,
        Y                   = 73750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 30140,
        Z                   = 0,
        Y                   = 72630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 44780,
        Z                   = 4600,
        Y                   = 51050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53490,
        Z                   = 6420,
        Y                   = 59900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56870,
        Z                   = 4600,
        Y                   = 53430,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 41670,
        Z                   = 4600,
        Y                   = 68230,
        Direction           = 314,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55760,
        Z                   = 4600,
        Y                   = 62760,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 66030,
        Z                   = 0,
        Y                   = 70470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 29410,
        Z                   = 0,
        Y                   = 56670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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
        X                   = 75900,
        Y                   = -1000,
        Z                   = 53900,
        Range               = 76600,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x10554,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )

    DeclEvent(
        X                   = 17000,
        Y                   = -1000,
        Z                   = 50100,
        Range               = 18000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9D6C,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 67,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 68,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 70,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 72,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 73,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 74,
    )


    ScpFunction(
        "Function_0_A82",          # 00, 0
        "Function_1_CEF",          # 01, 1
        "Function_2_DDB",          # 02, 2
        "Function_3_EF8",          # 03, 3
        "Function_4_F45",          # 04, 4
        "Function_5_F97",          # 05, 5
        "Function_6_1024",         # 06, 6
        "Function_7_1094",         # 07, 7
        "Function_8_1370",         # 08, 8
        "Function_9_169C",         # 09, 9
        "Function_10_194D",        # 0A, 10
        "Function_11_1B7D",        # 0B, 11
        "Function_12_1C0E",        # 0C, 12
        "Function_13_1CA7",        # 0D, 13
        "Function_14_1E44",        # 0E, 14
        "Function_15_1F54",        # 0F, 15
        "Function_16_210C",        # 10, 16
        "Function_17_219F",        # 11, 17
        "Function_18_2314",        # 12, 18
        "Function_19_2526",        # 13, 19
        "Function_20_269B",        # 14, 20
        "Function_21_286E",        # 15, 21
        "Function_22_29A8",        # 16, 22
        "Function_23_2B48",        # 17, 23
        "Function_24_2D67",        # 18, 24
        "Function_25_3066",        # 19, 25
        "Function_26_310A",        # 1A, 26
        "Function_27_31EE",        # 1B, 27
        "Function_28_3492",        # 1C, 28
        "Function_29_35D0",        # 1D, 29
        "Function_30_3898",        # 1E, 30
        "Function_31_3912",        # 1F, 31
        "Function_32_4AF4",        # 20, 32
        "Function_33_4B0B",        # 21, 33
        "Function_34_4B52",        # 22, 34
        "Function_35_4CDC",        # 23, 35
        "Function_36_52A7",        # 24, 36
        "Function_37_5363",        # 25, 37
        "Function_38_53BF",        # 26, 38
        "Function_39_5405",        # 27, 39
        "Function_40_544B",        # 28, 40
        "Function_41_5491",        # 29, 41
        "Function_42_54D7",        # 2A, 42
        "Function_43_551D",        # 2B, 43
        "Function_44_5563",        # 2C, 44
        "Function_45_55A9",        # 2D, 45
        "Function_46_55DB",        # 2E, 46
        "Function_47_560B",        # 2F, 47
        "Function_48_5663",        # 30, 48
        "Function_49_5693",        # 31, 49
        "Function_50_56C3",        # 32, 50
        "Function_51_5831",        # 33, 51
        "Function_52_5CED",        # 34, 52
        "Function_53_5DD8",        # 35, 53
        "Function_54_5E4C",        # 36, 54
        "Function_55_5EC0",        # 37, 55
        "Function_56_5F34",        # 38, 56
        "Function_57_5FA8",        # 39, 57
        "Function_58_61E3",        # 3A, 58
        "Function_59_6263",        # 3B, 59
        "Function_60_62A0",        # 3C, 60
        "Function_61_62DF",        # 3D, 61
        "Function_62_631E",        # 3E, 62
        "Function_63_6B02",        # 3F, 63
        "Function_64_6B8C",        # 40, 64
        "Function_65_6BE7",        # 41, 65
        "Function_66_6C44",        # 42, 66
        "Function_67_6C9D",        # 43, 67
        "Function_68_6CA1",        # 44, 68
        "Function_69_6CA5",        # 45, 69
        "Function_70_6CA9",        # 46, 70
        "Function_71_6CAD",        # 47, 71
        "Function_72_6CB1",        # 48, 72
        "Function_73_6CB5",        # 49, 73
        "Function_74_6CB9",        # 4A, 74
    )


    def Function_0_A82(): pass

    label("Function_0_A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_AD4")
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x25, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x23, 40190, 0, 71770, 270)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3C, 0x80)
    Jump("loc_C75")

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_B84")
    SetChrPos(0x1B, 47960, 0, 76090, 180)
    SetChrPos(0x25, 65480, 0, 69210, 225)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x22, 29530, 0, 76910, 270)
    SetChrPos(0x33, 30140, 0, 73750, 135)
    SetChrPos(0x34, 30140, 0, 72630, 135)
    SetChrPos(0x24, 30060, 0, 66160, 90)
    SetChrPos(0x2C, 65269, 0, 59980, 275)
    OP_43(0x2C, 0x0, 0x6, 0x2)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    Jump("loc_C75")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_BFA")
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x22, 29530, 0, 76910, 270)
    SetChrPos(0x33, 30140, 0, 73750, 135)
    SetChrPos(0x34, 30140, 0, 72630, 135)
    SetChrPos(0x24, 30060, 0, 66160, 90)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    Jump("loc_C75")

    label("loc_BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C75")
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrPos(0x2D, 66520, 0, 53320, 283)
    OP_43(0x2D, 0x0, 0x6, 0x2)
    SetChrPos(0x2E, 67200, 0, 51980, 270)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x3B, 0x80)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)

    label("loc_C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_C85")
    SetChrFlags(0x35, 0x80)

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_C9B")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 57)
    Jump("loc_CEE")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_CBA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 62)
    Jump("loc_CEE")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_CD9")
    OP_A3(0x10F4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_CEE")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 31)

    label("loc_CEE")

    Return()

    # Function_0_A82 end

    def Function_1_CEF(): pass

    label("Function_1_CEF")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x230041)
    OP_72(0x13, 0x20)
    OP_72(0x13, 0x8)
    OP_71(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_D1F")
    OP_71(0x1F, 0x4)
    Jump("loc_D68")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x20, 0x4)

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D83")
    OP_72(0x21, 0x4)
    OP_72(0x22, 0x4)
    OP_72(0x23, 0x4)

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_D8D")
    Jump("loc_D9E")

    label("loc_D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D9E")
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)

    label("loc_D9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDA")
    OP_72(0xA, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0xC, 0x10)
    OP_72(0xD, 0x10)
    OP_6F(0xA, 59)
    OP_6F(0xB, 59)
    OP_6F(0xC, 59)
    OP_6F(0xD, 59)

    label("loc_DDA")

    Return()

    # Function_1_CEF end

    def Function_2_DDB(): pass

    label("Function_2_DDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EF7")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x7D0, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xEA7E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x7D0, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x7D0, 0x0)
    Jump("Function_2_DDB")

    label("loc_EF7")

    Return()

    # Function_2_DDB end

    def Function_3_EF8(): pass

    label("Function_3_EF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F44")
    OP_8E(0xFE, 0xF0BE, 0x0, 0xCC1A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xF104, 0x0, 0xD7E6, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(3000)
    Jump("Function_3_EF8")

    label("loc_F44")

    Return()

    # Function_3_EF8 end

    def Function_4_F45(): pass

    label("Function_4_F45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F96")
    Sleep(1500)
    OP_8E(0xFE, 0xA6AE, 0x0, 0xB50E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xA1A4, 0x0, 0xB50E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_4_F45")

    label("loc_F96")

    Return()

    # Function_4_F45 end

    def Function_5_F97(): pass

    label("Function_5_F97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1023")
    OP_8E(0xFE, 0x99DE, 0x11F8, 0xDEBC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x9AD8, 0x11F8, 0xC7B0, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xAF32, 0x11F8, 0xC7B0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x9AD8, 0x11F8, 0xC7B0, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(3000)
    Jump("Function_5_F97")

    label("loc_1023")

    Return()

    # Function_5_F97 end

    def Function_6_1024(): pass

    label("Function_6_1024")

    TalkBegin(0x3C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1090")

    ChrTalk(    #0
        0xFE,
        "呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "几天没见，\x01",
            "工程有了很大的进展啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "嗯，在超市里\x01",
            "边走边看古董真是一种乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1090")

    TalkEnd(0x3C)
    Return()

    # Function_6_1024 end

    def Function_7_1094(): pass

    label("Function_7_1094")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_11C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(    #3
        0xFE,
        (
            "王国军忙于消灭龙，\x01",
            "城里的人们拼命为推进工程而努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "那么，让我来认真努力地考虑一下\x01",
            "今晚的菜单吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BE")

    label("loc_1116")


    ChrTalk(    #5
        0xFE,
        (
            "王国军忙于消灭龙，\x01",
            "城里的人们拼命为推进工程而努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "那么，让我来认真努力地考虑一下\x01",
            "今晚的菜单吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "不管是多无聊的工作，\x01",
            "认真干的话其实都是很辛苦的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_11BE")

    Jump("loc_136C")

    label("loc_11C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_12A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(    #8
        0xFE,
        (
            "超市的人们，\x01",
            "好像正在宾馆里继续营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "真是对工作充满热情啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_129E")

    label("loc_121B")


    ChrTalk(    #10
        0xFE,
        (
            "超市的人们，\x01",
            "好像正在宾馆里继续营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "他们热心于工作真令人高兴……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "不过托他们的福，\x01",
            "我在料理制作上也不能偷懒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_129E")

    Jump("loc_136C")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_136C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12F8")

    ChrTalk(    #13
        0xFE,
        (
            "没想超市\x01",
            "居然会发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "已经没心情\x01",
            "考虑什么菜单了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136C")

    label("loc_12F8")


    ChrTalk(    #15
        0xFE,
        (
            "没想超市\x01",
            "居然会发生这样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "已经没心情\x01",
            "考虑什么菜单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "今天只有面包和汤，\x01",
            "如果有不满就别吃。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_136C")

    TalkEnd(0x22)
    Return()

    # Function_7_1094 end

    def Function_8_1370(): pass

    label("Function_8_1370")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13D4")

    ChrTalk(    #18
        0xFE,
        (
            "我也决定帮忙\x01",
            "加入修复工程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "希望蛋糕铺的姐姐\x01",
            "能早日回到过去待的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_13D4")


    ChrTalk(    #20
        0xFE,
        (
            "我也决定帮忙\x01",
            "加入修复工程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "希望蛋糕铺的姐姐\x01",
            "能早日回到过去待的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "如果超市重新开始经营，\x01",
            "未婚夫也会返回冰淇淋店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "……没、没有什么别的用心哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1480")

    Jump("loc_1698")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14FA")

    ChrTalk(    #24
        0xFE,
        (
            "蛋糕店的姐姐\x01",
            "是和未婚夫一起经营店铺的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "如果超市重新开始经营，\x01",
            "他们可能会分开工作一阵子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_14FA")


    ChrTalk(    #26
        0xFE,
        (
            "呼，真想见见\x01",
            "蛋糕店的姐姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "她现在和未婚夫一起\x01",
            "开店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "如果超市重新开始经营，\x01",
            "他们可能会分开工作一阵子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "唉，我也去帮忙工作吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1596")

    Jump("loc_1698")

    label("loc_1599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1698")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1602")

    ChrTalk(    #30
        0xFE,
        (
            "蛋糕店的姐姐\x01",
            "是和未婚夫一起经营店铺的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "虽说早知会有今天，\x01",
            "但还是挺受打击的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1698")

    label("loc_1602")


    ChrTalk(    #32
        0xFE,
        (
            "我是听说了\x01",
            "蛋糕店姐姐在酒馆避难才来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "进去里面一看，姐姐她原来\x01",
            "是和未婚夫一起经营店铺的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "虽说早知会有今天，\x01",
            "但还是挺受打击的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1698")

    TalkEnd(0x23)
    Return()

    # Function_8_1370 end

    def Function_9_169C(): pass

    label("Function_9_169C")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1706")

    ChrTalk(    #35
        0xFE,
        (
            "根据各地的传说，\x01",
            "龙应该是理智而温和的生物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "那又为何会\x01",
            "来袭击果园呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_1706")


    ChrTalk(    #37
        0xFE,
        (
            "外表特征看来\x01",
            "倒确实是古代龙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "但是，情况好像有点奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "传说中，龙被认为是\x01",
            "理智而温厚的生物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "然而，现实出现的龙\x01",
            "却袭击了果园不是吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "虽然传说不是１００％的真实，\x01",
            "但总会有一定的根据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "相差这么远，\x01",
            "不是很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_17FE")

    Jump("loc_1949")

    label("loc_1801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_187A")

    ChrTalk(    #43
        0xFE,
        (
            "那毫无疑问就是自太古时代就存在的\x01",
            "幻之生物，古代龙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "镇、镇定～～\x01",
            "首先从收集目击证言开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1949")

    label("loc_187A")


    ChrTalk(    #45
        0xFE,
        (
            "刚、刚才那个看到了吗！？\x01",
            "那毫无疑问就是古代龙啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "从１２００年前的『大崩坏』以前开始\x01",
            "就生存着的幻之生物！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "我主张其生存\x01",
            "的学说果然是正确的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "要、要赶快收集目击证言，\x01",
            "画下草图才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1949")

    TalkEnd(0x24)
    Return()

    # Function_9_169C end

    def Function_10_194D(): pass

    label("Function_10_194D")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_19C5")

    ChrTalk(    #49
        0xFE,
        (
            "我拍的龙的照片\x01",
            "卖给利贝尔通讯社了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "唔，下一期的利贝尔通讯…\x01",
            "忍不住从现在就开始期待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A62")

    label("loc_19C5")


    ChrTalk(    #51
        0xFE,
        (
            "那个怪物，看来\x01",
            "似乎是古代龙这种生物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "据说非常稀有，\x01",
            "我的照片也被利贝尔通讯社\x01",
            "买去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "唔，下一期的利贝尔通讯…\x01",
            "忍不住从现在就开始期待了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1A62")

    Jump("loc_1B79")

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1B79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AC6")

    ChrTalk(    #54
        0xFE,
        (
            "我那时拍下了\x01",
            "那头怪物的照片……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "这、这个似乎\x01",
            "是相当厉害的独家新闻吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B79")

    label("loc_1AC6")


    ChrTalk(    #56
        0xFE,
        (
            "从、从飞船坪过来到这里，\x01",
            "刚好碰上那个怪物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "想、想都没想就用手中的照相机\x01",
            "拍了一张……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "这、这个似乎\x01",
            "是相当厉害的独家新闻吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "说不定可以联系\x01",
            "哪个杂志社卖掉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1B79")

    TalkEnd(0x25)
    Return()

    # Function_10_194D end

    def Function_11_1B7D(): pass

    label("Function_11_1B7D")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1C0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BBE")

    ChrTalk(    #60
        0xFE,
        (
            "超市在柏斯中心。\x01",
            "要赶快研究对策才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0A")

    label("loc_1BBE")


    ChrTalk(    #61
        0xFE,
        (
            "究竟是什么事呢。\x01",
            "超市竟然被袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "……要赶快研究对策才行呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1C0A")

    TalkEnd(0x26)
    Return()

    # Function_11_1B7D end

    def Function_12_1C0E(): pass

    label("Function_12_1C0E")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C6D")

    ChrTalk(    #63
        0xFE,
        (
            "超市现在这个样子，\x01",
            "柏斯的经济真是前途未卜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "要赶快想办法了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA3")

    label("loc_1C6D")


    ChrTalk(    #65
        0xFE,
        "怎、怎么回事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "这下简直\x01",
            "像战争一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1CA3")

    TalkEnd(0x27)
    Return()

    # Function_12_1C0E end

    def Function_13_1CA7(): pass

    label("Function_13_1CA7")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1D08")

    ChrTalk(    #67
        0xFE,
        "工程进展很顺利哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "多亏大家齐心协力，\x01",
            "看样子能比预想的更早恢复哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D76")

    label("loc_1D08")


    ChrTalk(    #69
        0xFE,
        "工程进展很顺利哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "这样下去似乎能比预想的\x01",
            "更早重新开始营业哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "嗯，这才是柏斯商人的实力啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1D76")

    Jump("loc_1E40")

    label("loc_1D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DD2")

    ChrTalk(    #72
        0xFE,
        (
            "超市的修复工程\x01",
            "马上就开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "虽然力量微薄，\x01",
            "但我也来帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E40")

    label("loc_1DD2")


    ChrTalk(    #74
        0xFE,
        (
            "超市的修复工程\x01",
            "马上就开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "不能一直给\x01",
            "酒店的人添麻烦嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "把店委托给同伴，\x01",
            "我也来帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1E40")

    TalkEnd(0x28)
    Return()

    # Function_13_1CA7 end

    def Function_14_1E44(): pass

    label("Function_14_1E44")

    TalkBegin(0x29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1E74")

    ChrTalk(    #77
        0xFE,
        "早点修好的话就好了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EBA")

    label("loc_1E74")


    ChrTalk(    #78
        0xFE,
        (
            "好不容易可以\x01",
            "一个人来买东西了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "早点修好的话就好了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1EBA")

    Jump("loc_1F50")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1F50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1EF9")

    ChrTalk(    #80
        0xFE,
        "教区长说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "龙其实\x01",
            "是很安分的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F50")

    label("loc_1EF9")


    ChrTalk(    #82
        0xFE,
        "教区长说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "龙其实\x01",
            "是很安分的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "可是，那为什么会\x01",
            "做那么可怕的事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1F50")

    TalkEnd(0x29)
    Return()

    # Function_14_1E44 end

    def Function_15_1F54(): pass

    label("Function_15_1F54")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1FB2")

    ChrTalk(    #85
        0xFE,
        (
            "各位市民\x01",
            "都来帮工程的忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "因此工程的进展\x01",
            "似乎比预定中更快哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2030")

    label("loc_1FB2")


    ChrTalk(    #87
        0xFE,
        (
            "各位市民\x01",
            "都来帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "可以的话我\x01",
            "也想贡献自己的力量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "……但那样做的话只会拖后腿而已。\x01",
            "这点我还是知道的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2030")

    Jump("loc_2108")

    label("loc_2033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_208C")

    ChrTalk(    #90
        0xFE,
        (
            "真令人惊讶。\x01",
            "工程已经开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "什么时候\x01",
            "准备得这么周全的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2108")

    label("loc_208C")


    ChrTalk(    #92
        0xFE,
        (
            "早上开始就觉得很吵闹，\x01",
            "于是过来看看情况……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "真令人惊讶。\x01",
            "工程已经开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "什么时候\x01",
            "准备得这么周全的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2108")

    TalkEnd(0x2A)
    Return()

    # Function_15_1F54 end

    def Function_16_210C(): pass

    label("Function_16_210C")

    TalkBegin(0x2B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2159")

    ChrTalk(    #95
        0xFE,
        (
            "呼，这样找\x01",
            "竟然还没找到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "那女孩\x01",
            "真的在这城里吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_219B")

    label("loc_2159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_219B")

    ChrTalk(    #97
        0xFE,
        (
            "去南街区之前\x01",
            "再到这边找找……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "啊啊，到底在哪里？\x02",
    )

    CloseMessageWindow()

    label("loc_219B")

    TalkEnd(0x2B)
    Return()

    # Function_16_210C end

    def Function_17_219F(): pass

    label("Function_17_219F")

    TalkBegin(0x2C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_21DE")

    ChrTalk(    #99
        0xFE,
        (
            "现在城市的状况\x01",
            "就像战争结束那时一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_21DE")


    ChrTalk(    #100
        0xFE,
        (
            "唔，现在城市的样子\x01",
            "就像战争结束那时一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "那个时候，为了修复\x01",
            "在百日战役中荒废的城市，\x01",
            "市民们也都是全体出动来帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2260")

    Jump("loc_2310")

    label("loc_2263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_22AD")

    ChrTalk(    #102
        0xFE,
        "工程好像已经开始了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "梅贝尔市长\x01",
            "也很努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2310")

    label("loc_22AD")


    ChrTalk(    #104
        0xFE,
        (
            "唔，工程已经开始了啊。\x01",
            "市长看来也在努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "这方面的优秀能力\x01",
            "可以说是继承自父亲的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2310")

    TalkEnd(0x2C)
    Return()

    # Function_17_219F end

    def Function_18_2314(): pass

    label("Function_18_2314")

    TalkBegin(0x2D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_23E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_236F")

    ChrTalk(    #106
        0xFE,
        "梅贝尔市长来视察过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "百忙之中\x01",
            "还一个人接一个人的鼓励大家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DE")

    label("loc_236F")


    ChrTalk(    #108
        0xFE,
        "梅贝尔市长来视察过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "百忙之中\x01",
            "还一个人接一个人的鼓励大家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "看到她的样子\x01",
            "突然就有了干劲呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_23DE")

    Jump("loc_2522")

    label("loc_23E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_24A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_243A")

    ChrTalk(    #111
        0xFE,
        (
            "和法娜一起\x01",
            "在给工程帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "虽然力量微薄，\x01",
            "但也不能坐视不理啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A2")

    label("loc_243A")


    ChrTalk(    #113
        0xFE,
        (
            "和法娜一起\x01",
            "在给工程帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "虽然力量微薄，\x01",
            "但也不能坐视不理啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "嗯，尽可能\x01",
            "努力看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_24A2")

    Jump("loc_2522")

    label("loc_24A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_24D0")

    ChrTalk(    #116
        0xFE,
        "刚、刚才那个是什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2522")

    label("loc_24D0")


    ChrTalk(    #117
        0xFE,
        "刚、刚才那个是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "那、那么大的魔兽，\x01",
            "真是从来没见过也没听说过啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2522")

    TalkEnd(0x2D)
    Return()

    # Function_18_2314 end

    def Function_19_2526(): pass

    label("Function_19_2526")

    TalkBegin(0x2E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_258A")

    ChrTalk(    #119
        0xFE,
        (
            "嘿嘿，市长小姐\x01",
            "和我说话了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "虽然不是为了得到赞扬\x01",
            "才去做的，\x01",
            "但还是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2697")

    label("loc_258A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_264C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_25D7")

    ChrTalk(    #121
        0xFE,
        (
            "我们也来\x01",
            "帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "超市封锁的话，\x01",
            "也就不能打工了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2649")

    label("loc_25D7")


    ChrTalk(    #123
        0xFE,
        (
            "我们也去帮忙\x01",
            "加入修复工程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "超市封锁的话，\x01",
            "也就不能打工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "而且有困难的时候\x01",
            "就应该互相帮助嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2649")

    Jump("loc_2697")

    label("loc_264C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2697")

    ChrTalk(    #126
        0xFE,
        (
            "超，超市的顶棚\x01",
            "给破坏得乱七八糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "里面的人\x01",
            "怎么样了！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2697")

    TalkEnd(0x2E)
    Return()

    # Function_19_2526 end

    def Function_20_269B(): pass

    label("Function_20_269B")

    TalkBegin(0x2F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2796")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_270F")

    ChrTalk(    #128
        0xFE,
        (
            "虽然遗憾，但是第一次\x01",
            "捕获作战好像失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "竟能甩开舰队的追踪，\x01",
            "真是不得了的飞行能力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2793")

    label("loc_270F")


    ChrTalk(    #130
        0xFE,
        (
            "虽然遗憾，但是第一次\x01",
            "捕获作战好像失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "话说回来居然能\x01",
            "甩开飞行舰队的追踪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "只能形容为\x01",
            "超越人类智慧的力量了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_2793")

    Jump("loc_286A")

    label("loc_2796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_286A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_27F9")

    ChrTalk(    #133
        0xFE,
        (
            "在古龙捕获作战成功之前，\x01",
            "市街的警备由我们负责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "有什么问题\x01",
            "就马上联络。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_286A")

    label("loc_27F9")


    ChrTalk(    #135
        0xFE,
        "我们是国境师团的分遣队。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "在古龙捕获作战成功之前，\x01",
            "负责柏斯市街的警备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "有什么问题\x01",
            "就马上联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_286A")

    TalkEnd(0x2F)
    Return()

    # Function_20_269B end

    def Function_21_286E(): pass

    label("Function_21_286E")

    TalkBegin(0x30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_28D1")

    ChrTalk(    #138
        0xFE,
        (
            "似乎连一般市民\x01",
            "也参与修复工程了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "照这个情况看来，\x01",
            "超市很快就可以重开了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A4")

    label("loc_28D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_29A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_292C")

    ChrTalk(    #140
        0xFE,
        (
            "面对那古代龙，\x01",
            "我们可对抗不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "现在只能祈祷\x01",
            "捕获作战能够成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A4")

    label("loc_292C")


    ChrTalk(    #142
        0xFE,
        (
            "我们的任务\x01",
            "是让市民放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "虽说是警备，\x01",
            "但对手可是那古代龙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "如果再被袭击，\x01",
            "我们的火力可无法对抗啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_29A4")

    TalkEnd(0x30)
    Return()

    # Function_21_286E end

    def Function_22_29A8(): pass

    label("Function_22_29A8")

    TalkBegin(0x31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_29FC")

    ChrTalk(    #145
        0xFE,
        (
            "龙似乎逃进\x01",
            "迷雾峡谷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "不知道摩尔根将军\x01",
            "有什么对策。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A72")

    label("loc_29FC")


    ChrTalk(    #147
        0xFE,
        (
            "龙似乎逃进\x01",
            "迷雾峡谷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "在山岳地带飞行本就危险，\x01",
            "而且那里又起雾了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "不知道摩尔根将军\x01",
            "有什么对策。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_2A72")

    Jump("loc_2B44")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2AD0")

    ChrTalk(    #150
        0xFE,
        (
            "拉文努村的\x01",
            "果园似乎也遭殃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "但是，果园……\x01",
            "没理由袭击果园啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B44")

    label("loc_2AD0")


    ChrTalk(    #152
        0xFE,
        (
            "拉文努村的\x01",
            "果园似乎也遭殃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "派遣到那边的人\x01",
            "说过情况非常严重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "但是，果园……\x01",
            "没理由袭击果园啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_2B44")

    TalkEnd(0x31)
    Return()

    # Function_22_29A8 end

    def Function_23_2B48(): pass

    label("Function_23_2B48")

    TalkBegin(0x32)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2BA5")

    ChrTalk(    #155
        0xFE,
        (
            "关于龙的捕获作战\x01",
            "似乎帝国没有反对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "这也是因为互不侵犯条约吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C49")

    label("loc_2BA5")


    ChrTalk(    #157
        0xFE,
        (
            "本来还担心帝国方面\x01",
            "会反对捕获作战……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "不过似乎并没反对呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "但是，柏斯地区\x01",
            "可以说就在帝国隔壁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "那个有名的铁血宰相\x01",
            "可不像是个会沉默的人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_2C49")

    Jump("loc_2D63")

    label("loc_2C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2D63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2CC5")

    ChrTalk(    #161
        0xFE,
        (
            "龙的捕获作战可是需要军方\x01",
            "大张旗鼓地出动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "因为作战地区是国境边沿，\x01",
            "真担心会刺激到帝国军啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D63")

    label("loc_2CC5")


    ChrTalk(    #163
        0xFE,
        (
            "龙的捕获作战可是需要军方\x01",
            "大张旗鼓地出动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "附近有国境线，\x01",
            "还是慎重行事为妙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "虽说缔结了互不侵犯条约，\x01",
            "但说实话，真是担心帝国军的反应啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_2D63")

    TalkEnd(0x32)
    Return()

    # Function_23_2B48 end

    def Function_24_2D67(): pass

    label("Function_24_2D67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5C")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过后篇一章【食材收集】委托】\x01",                  # 0
            "【◇完成过前篇【寻找荧光菇】、【探索护卫】委托】\x01",      # 1
            "【◇没有完成】\x01",                                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E26"),
        (1, "loc_2E38"),
        (2, "loc_2E4A"),
        (SWITCH_DEFAULT, "loc_2E5C"),
    )


    label("loc_2E26")

    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_2E5C")

    label("loc_2E38")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_2E5C")

    label("loc_2E4A")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_2E5C")

    label("loc_2E5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E79")
    Call(1, 0)
    Return()

    label("loc_2E79")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2EF6")

    ChrTalk(    #166
        0x35,
        (
            "超市的修复\x01",
            "似乎还要一阵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x35,
        "唔～真令人着急。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x35,
        (
            "定期船停航的这个时期，\x01",
            "正是帮我的食材开拓市场的时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3062")

    label("loc_2EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2F95")

    ChrTalk(    #169
        0x35,
        (
            "呼，超市要\x01",
            "暂时封闭啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x35,
        (
            "在本地商人的帮助下，总算\x01",
            "和『安特洛丝餐厅』进行商谈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x35,
        (
            "……但是现在这样，我的远大计划\x01",
            "不是要打水漂了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3062")

    label("loc_2F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_2FF0")

    ChrTalk(    #172
        0x35,
        (
            "正、正打算去超市\x01",
            "开始营业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x35,
        (
            "这种时候没想到\x01",
            "居然会被怪物袭击！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3062")

    label("loc_2FF0")


    ChrTalk(    #174
        0x35,
        (
            "正、正打算去超市\x01",
            "开始营业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x35,
        (
            "这种时候没想到\x01",
            "居然会被怪物袭击！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x35,
        (
            "啊啊，女神啊！\x01",
            "为什么要这样！？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_3062")

    TalkEnd(0x35)
    Return()

    # Function_24_2D67 end

    def Function_25_3066(): pass

    label("Function_25_3066")

    TalkBegin(0x33)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_308C")

    ChrTalk(    #177
        0xFE,
        "………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3090")

    label("loc_308C")

    Call(0, 27)

    label("loc_3090")

    Jump("loc_3101")

    label("loc_3093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_30B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_30B2")

    ChrTalk(    #178
        0xFE,
        "失望……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30B6")

    label("loc_30B2")

    Call(0, 27)

    label("loc_30B6")

    Jump("loc_3101")

    label("loc_30B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_30FD")

    ChrTalk(    #179
        0xFE,
        (
            "确，确实避难\x01",
            "是最安全的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "（生气）……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3101")

    label("loc_30FD")

    Call(0, 27)

    label("loc_3101")

    TalkEnd(0x33)
    ClearChrFlags(0x34, 0x10)
    Return()

    # Function_25_3066 end

    def Function_26_310A(): pass

    label("Function_26_310A")

    TalkBegin(0x34)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_3169")

    ChrTalk(    #181
        0xFE,
        (
            "有目标是好，\x01",
            "不过哈利缺乏具体的计划哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "那不是目标，而是愿望啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_316D")

    label("loc_3169")

    Call(0, 27)

    label("loc_316D")

    Jump("loc_31E5")

    label("loc_3170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_31AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_31A4")

    ChrTalk(    #183
        0xFE,
        (
            "善意并不一定\x01",
            "会产生好的结果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A8")

    label("loc_31A4")

    Call(0, 27)

    label("loc_31A8")

    Jump("loc_31E5")

    label("loc_31AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_31E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_31E1")

    ChrTalk(    #184
        0xFE,
        (
            "不过，这份心意\x01",
            "倒是令人感激……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E5")

    label("loc_31E1")

    Call(0, 27)

    label("loc_31E5")

    TalkEnd(0x34)
    ClearChrFlags(0x34, 0x10)
    Return()

    # Function_26_310A end

    def Function_27_31EE(): pass

    label("Function_27_31EE")

    OP_4A(0x33, 255)
    OP_4A(0x34, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_32BD")

    ChrTalk(    #185
        0x33,
        "市长好厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x33,
        (
            "不只是市政的工作，\x01",
            "做商人也是一流啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x33,
        (
            "啊～啊，我将来也想\x01",
            "成为那样出色的人啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x34,
        "那么，就努力看看？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x34,
        (
            "首先从主日学校的考试\x01",
            "拿满分开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x33,
        "………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3483")

    label("loc_32BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_33A2")
    ClearChrFlags(0x33, 0x10)
    ClearChrFlags(0x34, 0x10)

    ChrTalk(    #191
        0x33,
        (
            "好厉害啊～\x01",
            "工程已经开始了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x33,
        (
            "我也去\x01",
            "帮点忙吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0x33, 400)

    ChrTalk(    #193
        0x34,
        "还是算了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x34,
        (
            "如果想帮忙工程，\x01",
            "最好就是待在这里哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x33, 0x34, 400)

    ChrTalk(    #195
        0x33,
        "咦？为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x34,
        "……就不会碍手碍脚了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x33,
        "………………\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x33, 0x10)
    SetChrFlags(0x34, 0x10)
    Jump("loc_3483")

    label("loc_33A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3483")

    ChrTalk(    #198
        0x33,
        (
            "米、米娜不要紧吗？\x01",
            "有没有受伤？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x34,
        "嗯嗯，不要紧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x33,
        (
            "放，放心！\x01",
            "城市有我来保护！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x34,
        "虽然你还算可靠……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x34,
        (
            "不过在保护城市之前，\x01",
            "应该先保护我们自己的人身安全吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x34,
        (
            "……乖乖\x01",
            "去避难所吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x33,
        "是，是……\x02",
    )

    CloseMessageWindow()

    label("loc_3483")

    OP_4B(0x33, 255)
    OP_4B(0x34, 255)
    OP_A2(0x10)
    OP_A2(0x11)
    Return()

    # Function_27_31EE end

    def Function_28_3492(): pass

    label("Function_28_3492")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_35CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_34FC")

    ChrTalk(    #205
        0xFE,
        (
            "看来超市的修复工程\x01",
            "好像非常顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "这么说，剩下的问题\x01",
            "就只有那条龙了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35CC")

    label("loc_34FC")


    ChrTalk(    #207
        0xFE,
        (
            "看来工程比预定\x01",
            "进展更快呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "这么说，剩下的问题\x01",
            "只剩下龙的问题了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "即使建筑都修复了，\x01",
            "但那种怪物在天空飞来飞去\x01",
            "可会让人没心情买东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "希望王国军的计划，也能像\x01",
            "工程这么顺利就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_35CC")

    TalkEnd(0xA)
    Return()

    # Function_28_3492 end

    def Function_29_35D0(): pass

    label("Function_29_35D0")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 5)), scpexpr(EXPR_END)), "loc_3638")

    ChrTalk(    #211
        0x1B,
        (
            "#610F总算勉强撑过最困难的时刻了。\x02\x03",

            "接下来的目标就是\x01",
            "修复超市和稳定市民生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3894")

    label("loc_3638")


    ChrTalk(    #212
        0x1B,
        "#610F呀，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#1011F啊，梅贝尔市长。\x02\x03",

            "#1001F真是令人惊讶，\x01",
            "工程竟然已经开始了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #214
        0x1B,
        (
            "#611F嗯嗯，多亏市民们帮忙，\x01",
            "所以开工比预期的早呢。\x02\x03",

            "给拉文努村的救援物资\x01",
            "也平安送到了……\x02\x03",

            "这下总算是\x01",
            "撑过最困难的时刻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#1015F原来如此，告一段落了吧。\x02\x03",

            "#1000F对了……\x01",
            "莉拉的情况怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1B,
        (
            "#618F很遗憾……\x01",
            "从昨天开始就没有变化。\x02\x03",

            "只有静静等待\x01",
            "药效发挥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        "#1007F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x1B,
        (
            "#615F但是，光是担心\x01",
            "也解决不了任何问题。\x02\x03",

            "总之，现在身为市长\x01",
            "必须履行自己的职责。\x02\x03",

            "#610F如果莉拉在这里……\x01",
            "一定会这样说我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        (
            "#1006F嗯……是啊。\x02\x03",

            "我们也\x01",
            "会尽全力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x1B,
        (
            "#611F嗯嗯，期待\x01",
            "你的好消息。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A45)

    label("loc_3894")

    TalkEnd(0x1B)
    Return()

    # Function_29_35D0 end

    def Function_30_3898(): pass

    label("Function_30_3898")

    TalkBegin(0x3B)

    ChrTalk(    #221
        0xFE,
        (
            "嗯，看来药的效果\x01",
            "可是发生了不少事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "不过，看起来\x01",
            "危险已经过去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "暂时\x01",
            "也好像没有避难的必要了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x3B)
    Return()

    # Function_30_3898 end

    def Function_31_3912(): pass

    label("Function_31_3912")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3929")
    Call(0, 63)
    Call(0, 64)

    label("loc_3929")

    Call(0, 50)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0xFA, 0x80)
    SetChrFlags(0xFB, 0x80)
    SetChrFlags(0xFC, 0x80)
    OP_6D(59000, 0, 77330, 0)
    OP_67(0, 8620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(344000, 0)
    OP_6E(262, 0)
    OP_72(0x12, 0x4)
    OP_A1(0x20, 0x12)
    SetChrPos(0x20, 48600, 7100, 60940, 45)
    SetChrPos(0x21, 0, 0, 0, 45)
    OP_CF(0x21, 0x12, "Frame127_FireEmitter")
    LoadEffect(0x1, "monster\\ms30703.eff")
    LoadEffect(0x2, "monster\\ms30704.eff")
    ClearMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x106, 0x0, 0x0, 0x25)
    Sleep(2000)

    ChrTalk(    #224
        0x101,
        "#1020F#5P啊啊！？\x02",
    )

    WaitChrThread(0x106, 0x0)
    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x2E)
    Sleep(300)

    def lambda_3AE3():
        OP_6C(200000, 7000)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3AE3)

    def lambda_3AF3():
        OP_6E(490, 7000)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3AF3)

    def lambda_3B03():
        OP_6D(45280, 500, 51530, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B03)

    def lambda_3B1B():
        OP_67(0, 7000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B1B)

    def lambda_3B33():
        OP_6B(5150, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B33)
    Sleep(5500)
    OP_72(0x12, 0x20)
    OP_73(0x12)
    OP_6F(0x12, 55)
    OP_70(0x12, 0x78)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(41420, 3160, 60230, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(3770, 0)
    OP_6C(223000, 0)
    OP_6E(490, 0)
    Sleep(500)
    OP_22(0x11F, 0x0, 0x64)
    OP_7C(0x258, 0x258, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x12)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x12, 0x20)
    OP_6F(0x12, 5)
    OP_70(0x12, 0x37)

    def lambda_3BFE():
        OP_6D(49070, 4400, 60770, 3500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3BFE)

    def lambda_3C16():
        OP_67(0, 8760, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C16)

    def lambda_3C2E():
        OP_6B(3870, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C2E)

    def lambda_3C3E():
        OP_6C(210000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C3E)
    OP_72(0xA, 0x800)
    OP_72(0xB, 0x800)
    OP_72(0xC, 0x800)
    OP_72(0xD, 0x800)
    OP_72(0xA, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0xC, 0x10)
    OP_72(0xD, 0x10)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3B)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x3B)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x3B)
    OP_73(0xD)
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xB, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xC, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0xD, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xE, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0xF, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x10, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0x11, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x12, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x13, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x14, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0x15, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x16, 0x1, 0x0, 0x31)
    Sleep(400)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x17, 0x1, 0x0, 0x2E)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x18, 0x1, 0x0, 0x2F)
    Sleep(50)
    OP_43(0x19, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_43(0x1A, 0x1, 0x0, 0x31)
    Sleep(3500)
    OP_63(0xB)
    OP_63(0xC)
    OP_63(0xD)
    OP_63(0xE)
    OP_63(0xF)
    OP_63(0x10)
    OP_63(0x11)
    OP_63(0x12)
    OP_63(0x13)
    OP_63(0x14)
    OP_63(0x15)
    OP_63(0x16)
    OP_63(0x17)
    OP_63(0x18)
    OP_63(0x19)
    OP_63(0x1A)
    Fade(500)
    OP_6D(58270, 0, 78850, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(344000, 0)
    OP_6E(283, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #225
        0x101,
        "#1020F#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x107,
        "#065F#5P啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x103,
        "#023F#5P怎么这么大……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x108,
        "#077F#2P这是……龙吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x105,
        (
            "#043F#2P是……是古代龙！\x02\x03",

            "传说自古\x01",
            "栖息在利贝尔\x01",
            "某处的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x104,
        "#032F#5P哎呀呀，吓死人了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x106,
        (
            "#057F#5P难不成……\x01",
            "这也是『结社』搞的鬼吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 54630, 4600, 69030, 45)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #232
        0x8,
        "青年的声音",
        "#2P……嗯，那也不必否认。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(20)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(20)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_40EB():
        OP_6D(53140, 0, 73070, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40EB)

    def lambda_4103():
        OP_67(0, 6620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4103)

    def lambda_411B():
        OP_6B(2150, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_411B)

    def lambda_412B():
        OP_6C(264000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_412B)

    def lambda_413B():
        OP_6E(588, 4000)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_413B)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #233
        0x101,
        "#1020F#2P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x106,
        "#052F#2P你是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x103,
        (
            "#024F#2P特务部队队长，\x01",
            "洛伦斯·博格少尉！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #236
        0x8,
        "银发的青年",
        "#121F呵呵，那只不过是假名。\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS191._CH")
    OP_C6(0x0, 0x0, 125000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("银发的青年")

    AnonymousTalk(    #237
        (
            "#124F执行者ＮＯ．Ⅱ。\x01",
            "『剑帝』莱恩哈特。\x02\x03",

            "以后，就这么称呼我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    Sleep(500)

    ChrTalk(    #238
        0x101,
        "#1020F#2P『剑帝』……莱恩哈特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x104,
        (
            "#035F#2P原来如此……\x01",
            "莱恩哈特（ＬＥＯＮＨＡＲＤＴ）就是『狮子的果敢』的意思。\x02\x03",

            "#030F那么说，莱维（狮子）\x01",
            "就是你的爱称吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #240
        0x101,
        "#1005F#2P你，你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        "#043F#2P你就是莱维……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x8,
        (
            "#124F……虽然我并不喜欢，\x01",
            "但在同伴间这样称呼我的人倒是不少。\x02\x03",

            "#123F算了，那就随便你们\x01",
            "怎么叫都好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x106,
        "#057F#2P……真是小看人……\x02",
    )

    CloseMessageWindow()
    OP_22(0x11F, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_444C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_444C)

    def lambda_445A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_445A)

    def lambda_4468():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_4468)
    Sleep(100)

    def lambda_447B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_447B)

    def lambda_4489():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4489)
    Sleep(100)

    def lambda_449C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_449C)

    def lambda_44AA():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_44AA)
    Sleep(100)

    def lambda_44BD():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_44BD)

    def lambda_44CB():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_44CB)
    Sleep(100)
    Fade(500)
    SetChrPos(0x20, 48600, 7100, 60940, 0)
    OP_6D(31950, 0, 69570, 0)
    OP_67(0, 6310, -10000, 0)
    OP_6B(3330, 0)
    OP_6C(251000, 0)
    OP_6E(490, 0)
    OP_72(0x12, 0x20)
    OP_6F(0x12, 55)
    OP_70(0x12, 0x73)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    PlayEffect(0x1, 0x0, 0x21, 0, 0, 0, 0, -45, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    OP_73(0x12)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x12, 0x20)
    OP_6F(0x12, 5)
    OP_70(0x12, 0x37)
    Sleep(1500)
    Fade(500)
    OP_71(0x12, 0x4)
    SetChrPos(0x20, 48600, 7100, 60940, 45)
    OP_6D(57430, 0, 76950, 0)
    OP_67(0, 8390, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(11000, 0)
    OP_6E(291, 0)
    OP_8C(0x8, 225, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #244
        0x101,
        "#1020F#2P啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x103,
        "#523F#5P打算烧了城市吗……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x8,
        (
            "#124F#5P……真是的。\x01",
            "让我多费工夫。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x8, 33)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(200)
    ClearChrFlags(0x8, 0x1)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    SetChrSubChip(0x8, 2)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0x8, 270, 0)

    def lambda_46B6():
        OP_96(0xFE, 0xBD2E, 0x3AFC, 0x10054, 0x2AF8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_46B6)
    Sleep(200)
    Fade(100)
    OP_72(0x12, 0x4)
    OP_6D(56240, 18870, 65550, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(312, 0)
    WaitChrThread(0x8, 0x3)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    ClearChrFlags(0x8, 0x4)
    OP_CF(0x8, 0x12, "Frame141_back_Null1")
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_8C(0x8, 90, 0)
    Sleep(500)
    SetChrChipByIndex(0x8, 34)
    SetChrSubChip(0x8, 0)
    OP_8C(0x8, 180, 400)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_477F():
        OP_67(0, 8740, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_477F)

    def lambda_4797():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4797)

    def lambda_47A7():
        OP_6E(442, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_47A7)

    def lambda_47B7():
        OP_6D(52240, 18870, 65550, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_47B7)

    def lambda_47CF():
        OP_8C(0xFE, 315, 80)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_47CF)
    OP_72(0x12, 0x20)
    OP_6F(0x12, 116)
    OP_70(0x12, 0x91)
    OP_73(0x12)
    OP_B0(0x12, 0x5)
    OP_71(0x12, 0x20)
    OP_6F(0x12, 145)
    OP_70(0x12, 0x9E)
    Sleep(200)
    OP_43(0x20, 0x3, 0x0, 0x20)
    Sleep(500)
    OP_43(0x20, 0x1, 0x0, 0x21)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #247
        0x106,
        "#055F#5P给、给我停下！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x8,
        (
            "#122F#6P……这次的实验\x01",
            "稍微有点不合常理。\x02\x03",

            "说实话，并不是你们\x01",
            "能够应付的事件。\x02\x03",

            "#125F把事情交给王国军，\x01",
            "然后待在一边乖乖看着吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_48D7():
        OP_6D(48240, 18870, 69550, 4000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_48D7)

    def lambda_48EF():
        OP_67(0, 10000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_48EF)

    def lambda_4907():
        OP_6B(4010, 4000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4907)

    def lambda_4917():
        OP_6C(270000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4917)

    def lambda_4927():
        OP_6E(395, 4000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_4927)

    def lambda_4937():

        label("loc_4937")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4937")

    QueueWorkItem2(0x101, 1, lambda_4937)

    def lambda_4948():

        label("loc_4948")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4948")

    QueueWorkItem2(0x106, 1, lambda_4948)

    def lambda_4959():

        label("loc_4959")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_4959")

    QueueWorkItem2(0xF8, 1, lambda_4959)

    def lambda_496A():

        label("loc_496A")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_496A")

    QueueWorkItem2(0xF9, 1, lambda_496A)

    def lambda_497B():

        label("loc_497B")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_497B")

    QueueWorkItem2(0xFA, 1, lambda_497B)

    def lambda_498C():

        label("loc_498C")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_498C")

    QueueWorkItem2(0xFB, 1, lambda_498C)

    def lambda_499D():

        label("loc_499D")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_499D")

    QueueWorkItem2(0xFC, 1, lambda_499D)

    def lambda_49AE():

        label("loc_49AE")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_49AE")

    QueueWorkItem2(0x9, 1, lambda_49AE)
    SetChrChipByIndex(0x8, 13)
    SetChrSubChip(0x8, 0)
    OP_72(0x12, 0x20)
    OP_73(0x12)
    OP_B0(0x12, 0x14)
    OP_6F(0x12, 145)
    OP_70(0x12, 0xAA)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x190, 0x1388, 0x5DC)
    PlayEffect(0x2, 0x0, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0x1, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x12, 0x20)
    OP_B0(0x12, 0x19)
    OP_6F(0x12, 170)
    OP_70(0x12, 0xBE)
    PlayEffect(0x2, 0x2, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x20, 0x1)
    OP_43(0x20, 0x0, 0x0, 0x22)
    WaitChrThread(0x101, 0x0)
    Sleep(2500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    OP_A2(0x10FE)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_3912 end

    def Function_32_4AF4(): pass

    label("Function_32_4AF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B0A")
    OP_22(0x120, 0x0, 0x64)
    Sleep(2700)
    Jump("Function_32_4AF4")

    label("loc_4B0A")

    Return()

    # Function_32_4AF4 end

    def Function_33_4B0B(): pass

    label("Function_33_4B0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B51")
    PlayEffect(0x2, 0xFF, 0x20, 0, -6000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(2700)
    Jump("Function_33_4B0B")

    label("loc_4B51")

    Return()

    # Function_33_4B0B end

    def Function_34_4B52(): pass

    label("Function_34_4B52")

    OP_22(0x120, 0x0, 0x64)

    def lambda_4B5D():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4B5D)
    Sleep(200)
    PlayEffect(0x2, 0x0, 0x20, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_4BB2():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4BB2)
    Sleep(200)
    PlayEffect(0x2, 0x1, 0x20, 0, -2000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x120, 0x0, 0x64)

    def lambda_4C0C():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4C0C)
    Sleep(200)
    PlayEffect(0x2, 0x1, 0x20, 0, -4000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_4C61():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4C61)
    Sleep(200)

    def lambda_4C81():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4C81)
    Sleep(200)
    OP_22(0x120, 0x0, 0x64)

    def lambda_4CA6():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0x7D00, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4CA6)
    Sleep(300)

    def lambda_4CC6():
        OP_8F(0xFE, 0xFFFF9BA6, 0x88B8, 0x1B012, 0xFA00, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4CC6)
    Return()

    # Function_34_4B52 end

    def Function_35_4CDC(): pass

    label("Function_35_4CDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(58650, 0, 78150, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(344000, 0)
    OP_6E(283, 0)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0xFC, 0x1)
    OP_44(0x9, 0x1)
    SetChrPos(0x101, 59570, 0, 76570, 315)
    SetChrPos(0x106, 58320, 0, 76730, 315)
    SetChrPos(0x107, 57360, 0, 77470, 315)
    SetChrPos(0x103, 58660, 0, 77700, 315)
    SetChrPos(0x104, 58080, 0, 78840, 315)
    SetChrPos(0x105, 60210, 0, 77350, 315)
    SetChrPos(0x108, 59500, 0, 78870, 315)
    SetChrPos(0x9, 59050, 500, 79890, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_4A(0x36, 255)
    OP_4A(0x37, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    OP_4A(0x3A, 255)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 59)
    OP_72(0xC, 0x10)
    OP_6F(0xC, 59)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #249
        0x101,
        (
            "#1005F#6P怎、怎么办……\x01",
            "这样下去会被他逃掉的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x106,
        (
            "#053F#5P……我现在\x01",
            "去追踪那个大家伙。\x02\x03",

            "#057F你们在军方到来之前\x01",
            "先确认受害状况吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F11():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F11)
    Sleep(10)

    def lambda_4F24():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4F24)
    Sleep(20)

    def lambda_4F37():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4F37)
    Sleep(10)

    def lambda_4F4A():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_4F4A)
    Sleep(30)

    def lambda_4F5D():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_4F5D)
    Sleep(10)

    def lambda_4F70():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_4F70)
    Sleep(20)

    def lambda_4F83():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F83)
    Sleep(400)

    def lambda_4F96():

        label("loc_4F96")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4F96")

    QueueWorkItem2(0x101, 1, lambda_4F96)

    def lambda_4FA7():

        label("loc_4FA7")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4FA7")

    QueueWorkItem2(0xF8, 1, lambda_4FA7)

    def lambda_4FB8():

        label("loc_4FB8")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4FB8")

    QueueWorkItem2(0xF9, 1, lambda_4FB8)

    def lambda_4FC9():

        label("loc_4FC9")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4FC9")

    QueueWorkItem2(0xFA, 1, lambda_4FC9)

    def lambda_4FDA():

        label("loc_4FDA")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4FDA")

    QueueWorkItem2(0xFB, 1, lambda_4FDA)

    def lambda_4FEB():

        label("loc_4FEB")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4FEB")

    QueueWorkItem2(0xFC, 1, lambda_4FEB)

    def lambda_4FFC():

        label("loc_4FFC")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_4FFC")

    QueueWorkItem2(0x9, 1, lambda_4FFC)

    ChrTalk(    #251
        0x101,
        "#1020F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x103,
        "#023F#2P阿加特？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x106,
        "#054F#5P稍后联络！\x02",
    )

    CloseMessageWindow()

    def lambda_5054():
        OP_6C(302000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5054)

    def lambda_5064():
        OP_6D(55320, 0, 76560, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5064)

    def lambda_507C():
        OP_8E(0xFE, 0x94E8, 0x0, 0x12066, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_507C)
    Sleep(2000)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0xFC, 0x1)
    OP_44(0x9, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #254
        0x107,
        "#065F#5P阿加特哥哥！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        "#1020F#6P等、等等！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 49540, 0, 70870, 0)
    ClearChrFlags(0xA, 0x80)

    ChrTalk(    #256
        0xA,
        (
            "#4P是、是你们！\x01",
            "还好找到了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5131():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5131)

    def lambda_513F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_513F)

    def lambda_514D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_514D)

    def lambda_515B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_515B)

    def lambda_5169():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_5169)

    def lambda_5177():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_5177)

    def lambda_5185():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5185)

    def lambda_5193():
        OP_6C(270000, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5193)

    def lambda_51A3():
        OP_6D(54350, 0, 74950, 1800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_51A3)

    def lambda_51BB():
        OP_8E(0xFE, 0xD232, 0x0, 0x121E2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_51BB)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0xA, 0x1)
    OP_4A(0xA, 255)

    def lambda_51F1():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_51F1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #257
        0xA,
        "#5P拜托了，来帮帮我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xA,
        (
            "#5P有人被压在瓦砾下面\x01",
            "还没有逃出来！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x108, 0x1)

    ChrTalk(    #259
        0x108,
        "#072F#2P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1005F#2P你、你说什么！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1123   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_4CDC end

    def Function_36_52A7(): pass

    label("Function_36_52A7")


    def lambda_52AD():
        OP_8F(0xFE, 0xC666, 0x0, 0x1249E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52AD)
    Sleep(300)

    def lambda_52CD():
        OP_8F(0xFE, 0xC6CA, 0x0, 0x12886, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_52CD)
    Sleep(100)

    def lambda_52ED():
        OP_8F(0xFE, 0xCB84, 0x0, 0x1255C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_52ED)
    Sleep(100)

    def lambda_530D():
        OP_8F(0xFE, 0xCA08, 0x0, 0x1200C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_530D)
    Sleep(100)

    def lambda_532D():
        OP_8F(0xFE, 0xCF26, 0x0, 0x11DB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_532D)
    Sleep(100)

    def lambda_534D():
        OP_8F(0xFE, 0xE8F8, 0x0, 0x13182, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_534D)
    Return()

    # Function_36_52A7 end

    def Function_37_5363(): pass

    label("Function_37_5363")

    OP_43(0x106, 0x1, 0x0, 0x27)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0x26)
    Sleep(400)
    OP_43(0x107, 0x1, 0x0, 0x28)
    Sleep(400)
    OP_43(0x103, 0x1, 0x0, 0x29)
    Sleep(400)
    OP_43(0x105, 0x1, 0x0, 0x2B)
    Sleep(400)
    OP_43(0x104, 0x1, 0x0, 0x2A)
    Sleep(400)
    OP_43(0x108, 0x1, 0x0, 0x2C)
    Sleep(400)
    OP_43(0x9, 0x1, 0x0, 0x2D)
    Return()

    # Function_37_5363 end

    def Function_38_53BF(): pass

    label("Function_38_53BF")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE8B2, 0x0, 0x12B1A, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_38_53BF end

    def Function_39_5405(): pass

    label("Function_39_5405")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE3D0, 0x0, 0x12BBA, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_39_5405 end

    def Function_40_544B(): pass

    label("Function_40_544B")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE010, 0x0, 0x12E9E, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_40_544B end

    def Function_41_5491(): pass

    label("Function_41_5491")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE524, 0x0, 0x12F84, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_41_5491 end

    def Function_42_54D7(): pass

    label("Function_42_54D7")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE2E0, 0x0, 0x133F8, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_42_54D7 end

    def Function_43_551D(): pass

    label("Function_43_551D")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xEB32, 0x0, 0x12E26, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_43_551D end

    def Function_44_5563(): pass

    label("Function_44_5563")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6B4, 0x1D6, 0x136AA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE86C, 0x0, 0x13416, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_44_5563 end

    def Function_45_55A9(): pass

    label("Function_45_55A9")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6AA, 0x1F4, 0x13812, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_45_55A9 end

    def Function_46_55DB(): pass

    label("Function_46_55DB")

    SetChrPos(0xFE, 54510, 0, 60010, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x11B8E, 0x0, 0xEA6A, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_46_55DB end

    def Function_47_560B(): pass

    label("Function_47_560B")

    SetChrPos(0xFE, 41460, 0, 59990, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x7F44, 0x0, 0xEA56, 0x1388, 0x0)
    OP_8E(0xFE, 0x7FC6, 0x0, 0xAAF0, 0x1388, 0x0)
    OP_8E(0xFE, 0x42F4, 0x0, 0xA776, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_47_560B end

    def Function_48_5663(): pass

    label("Function_48_5663")

    SetChrPos(0xFE, 48010, 0, 53480, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xBDBA, 0xFFFFF448, 0x4402, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_48_5663 end

    def Function_49_5693(): pass

    label("Function_49_5693")

    SetChrPos(0xFE, 48040, 0, 66510, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xBB76, 0xBB8, 0x163C8, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_49_5693 end

    def Function_50_56C3(): pass

    label("Function_50_56C3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56FC")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_56FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5749")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5731")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5749")

    label("loc_5731")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57BE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577E")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_57BE")

    label("loc_577E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57A6")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_57BE")

    label("loc_57A6")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_57BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_580B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57F3")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_580B")

    label("loc_57F3")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_580B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5830")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_5830")

    Return()

    # Function_50_56C3 end

    def Function_51_5831(): pass

    label("Function_51_5831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_591E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589A")

    ChrTalk(    #261
        0x108,
        (
            "#074F现在已经\x01",
            "没空乱逛了啊。\x02\x03",

            "#070F在街上买过东西之后\x01",
            "就去国际空港吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5900")

    label("loc_589A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_58B7")

    label("loc_58B0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_58B7")


    ChrTalk(    #262
        0x103,
        (
            "#020F现在已经\x01",
            "没时间闲逛了啊。\x02\x03",

            "在街上买完东西以后\x01",
            "就去国际空港吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5900")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5CEC")

    label("loc_591E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AFD")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_594C"),
        (2, "loc_598A"),
        (4, "loc_59D0"),
        (3, "loc_5A12"),
        (6, "loc_5A58"),
        (7, "loc_5AA0"),
        (SWITCH_DEFAULT, "loc_5ADF"),
    )


    label("loc_594C")


    ChrTalk(    #263
        0x101,
        (
            "#1002F不是这条路啦。\x02\x03",

            "准备完毕之后\x01",
            "马上回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_598A")


    ChrTalk(    #264
        0x103,
        (
            "#022F现在没时间\x01",
            "绕远路了。\x02\x03",

            "准备结束之后\x01",
            "就赶快回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_59D0")


    ChrTalk(    #265
        0x105,
        (
            "#042F现在没空\x01",
            "绕远路了。\x02\x03",

            "准备结束之后\x01",
            "赶快回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_5A12")


    ChrTalk(    #266
        0x104,
        (
            "#032F现在不是闲逛\x01",
            "的时候啊。\x02\x03",

            "准备完毕之后\x01",
            "赶快回拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_5A58")


    ChrTalk(    #267
        0x107,
        (
            "#062F……别再\x01",
            "磨磨蹭蹭的啦。\x02\x03",

            "准备好之后\x01",
            "赶快追上阿加特哥哥吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_5AA0")


    ChrTalk(    #268
        0x108,
        (
            "#072F已经没时间乱逛了。\x02\x03",

            "准备好之后\x01",
            "赶快回拉文努村吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADF")

    label("loc_5ADF")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5CEC")

    label("loc_5AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CEC")
    EventBegin(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_5B2B"),
        (2, "loc_5B6B"),
        (4, "loc_5BAC"),
        (3, "loc_5BED"),
        (6, "loc_5C2A"),
        (7, "loc_5C96"),
        (SWITCH_DEFAULT, "loc_5CD1"),
    )


    label("loc_5B2B")


    ChrTalk(    #269
        0x101,
        (
            "#1002F现在必须要\x01",
            "赶快到拉文努村…\x02\x03",

            "从西边的出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5B6B")


    ChrTalk(    #270
        0x103,
        (
            "#022F要去拉文努村的话，\x01",
            "得从西边的出口出去。\x02\x03",

            "快一点吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5BAC")


    ChrTalk(    #271
        0x105,
        (
            "#042F拉文努村\x01",
            "位于柏斯的西北方向。\x02\x03",

            "从西边的出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5BED")


    ChrTalk(    #272
        0x104,
        (
            "#032F拉文努村\x01",
            "是在西北方向呢。\x02\x03",

            "从西边的出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5C2A")


    ChrTalk(    #273
        0x107,
        (
            "#065F啊啊……\x01",
            "要去拉文努村的话，\x01",
            "应该从西边的出口出去啊。\x02\x03",

            "#062F我们必须要早点\x01",
            "追上阿加特哥哥……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5C96")


    ChrTalk(    #274
        0x108,
        (
            "#072F去拉文努村的话，\x01",
            "要从西边出去，\x02\x03",

            "赶快行动吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD1")

    label("loc_5CD1")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5CEC")

    Return()

    # Function_51_5831 end

    def Function_52_5CED(): pass

    label("Function_52_5CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DD7")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D56")

    ChrTalk(    #275
        0x108,
        (
            "#074F现在已经\x01",
            "没空乱逛了啊。\x02\x03",

            "#070F在街上买过东西之后\x01",
            "就去国际空港吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DBC")

    label("loc_5D56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D6C")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_5D73")

    label("loc_5D6C")

    TurnDirection(0x103, 0x0, 400)

    label("loc_5D73")


    ChrTalk(    #276
        0x103,
        (
            "#020F现在已经\x01",
            "没时间闲逛了啊。\x02\x03",

            "在街上买完东西以后\x01",
            "就去国际空港吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBC")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5DD7")

    Return()

    # Function_52_5CED end

    def Function_53_5DD8(): pass

    label("Function_53_5DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5DE0")
    Return()

    label("loc_5DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5E30")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #277
        "\x07\x05◆禁止进入用障壁的代替品\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5E30")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_53_5DD8 end

    def Function_54_5E4C(): pass

    label("Function_54_5E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5E54")
    Return()

    label("loc_5E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5EA4")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #278
        "\x07\x05◆禁止进入用障壁的代替品\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5EA4")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_54_5E4C end

    def Function_55_5EC0(): pass

    label("Function_55_5EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5EC8")
    Return()

    label("loc_5EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5F18")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #279
        "\x07\x05◆禁止进入用障壁的代替品\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5F18")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_55_5EC0 end

    def Function_56_5F34(): pass

    label("Function_56_5F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5F3C")
    Return()

    label("loc_5F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_5F8C")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #280
        "\x07\x05◆禁止进入用障壁的代替品\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5F8C")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_5F34 end

    def Function_57_5FA8(): pass

    label("Function_57_5FA8")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(47330, 400, 59690, 0)
    OP_67(0, 14540, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(314000, 0)
    OP_6E(556, 0)
    OP_71(0xC, 0x4)
    OP_71(0x23, 0x4)
    SetChrPos(0x1B, 45230, 0, 74390, 90)
    SetChrPos(0xB, 47000, 0, 73840, 270)
    SetChrPos(0xC, 46950, 0, 74750, 270)
    SetChrPos(0xD, 46540, 0, 72950, 315)
    SetChrPos(0x1D, 46630, 0, 75700, 225)
    SetChrPos(0x1C, 48040, 0, 71510, 90)
    SetChrPos(0xF, 49220, 0, 71700, 90)
    SetChrPos(0x11, 49940, 0, 72980, 135)
    SetChrPos(0x1E, 51670, 0, 72890, 90)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    OP_22(0x1C2, 0x0, 0x64)
    OP_43(0x1B, 0x1, 0x0, 0x3A)
    OP_43(0x1E, 0x1, 0x0, 0x3B)

    def lambda_60DF():
        OP_6C(213000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_60DF)
    FadeToBright(2000, 0)
    Sleep(5000)

    def lambda_60FD():
        OP_6D(46830, 400, 72760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_60FD)

    def lambda_6115():
        OP_67(0, 9760, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6115)

    def lambda_612D():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_612D)

    def lambda_613D():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_613D)
    OP_8E(0x1C, 0xBBA8, 0x12C, 0x10F7C, 0x7D0, 0x0)
    OP_72(0xC, 0x10)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3B)
    OP_73(0xC)
    TurnDirection(0x1C, 0xF, 400)
    Sleep(1000)
    OP_43(0xF, 0x1, 0x0, 0x3C)
    Sleep(800)
    OP_43(0x11, 0x1, 0x0, 0x3D)
    Sleep(2000)
    OP_8C(0x1C, 180, 400)

    def lambda_61A2():
        OP_8E(0xFE, 0xBBA8, 0x1F4, 0x103CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_61A2)
    WaitChrThread(0x1C, 0x1)
    SetChrFlags(0x1C, 0x80)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_57_5FA8 end

    def Function_58_61E3(): pass

    label("Function_58_61E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6262")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    Jump("Function_58_61E3")

    label("loc_6262")

    Return()

    # Function_58_61E3 end

    def Function_59_6263(): pass

    label("Function_59_6263")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_629F")
    OP_8C(0xFE, 0, 300)
    Sleep(1000)
    OP_8C(0xFE, 270, 300)
    Sleep(1000)
    OP_8C(0xFE, 0, 300)
    Sleep(1000)
    OP_8C(0xFE, 90, 300)
    Sleep(1000)
    Jump("Function_59_6263")

    label("loc_629F")

    Return()

    # Function_59_6263 end

    def Function_60_62A0(): pass

    label("Function_60_62A0")

    Sleep(500)
    TurnDirection(0xFE, 0x1C, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xBBA8, 0x12C, 0x10F7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBBA8, 0x1F4, 0x103CE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_60_62A0 end

    def Function_61_62DF(): pass

    label("Function_61_62DF")

    Sleep(500)
    TurnDirection(0xFE, 0x1C, 400)
    Sleep(2000)
    OP_8E(0xFE, 0xBE00, 0x0, 0x11A44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBBA8, 0x1F4, 0x103CE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_61_62DF end

    def Function_62_631E(): pass

    label("Function_62_631E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6335")
    Call(0, 63)
    Call(0, 66)

    label("loc_6335")

    OP_31(0xFF, 0xFE, 0x0)
    OP_6D(48700, 0, 83750, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 47650, 1500, 87720, 180)
    SetChrPos(0x106, 49120, 1500, 87720, 180)
    SetChrPos(0x107, 49200, 2500, 89250, 180)
    SetChrPos(0xF9, 47650, 2500, 89250, 180)
    FadeToBright(1000, 0)

    def lambda_63CA():
        OP_8E(0xFE, 0xBA22, 0x0, 0x14320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63CA)
    Sleep(70)

    def lambda_63EA():
        OP_8E(0xFE, 0xBFE0, 0x0, 0x14320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_63EA)
    Sleep(80)

    def lambda_640A():
        OP_8E(0xFE, 0xBA22, 0x0, 0x1491A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_640A)
    Sleep(70)

    def lambda_642A():
        OP_8E(0xFE, 0xC030, 0x0, 0x1491A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_642A)
    WaitChrThread(0x101, 0x1)

    def lambda_644A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_644A)
    WaitChrThread(0x106, 0x1)

    def lambda_645D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_645D)
    WaitChrThread(0xF9, 0x1)

    def lambda_6470():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6470)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 225, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6529")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在后篇见过维姆拉】\x01",        # 0
            "【◇在后篇没见过维姆拉】\x01",      # 1
            "【◇什么也没有变更】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_651D"),
        (1, "loc_6523"),
        (SWITCH_DEFAULT, "loc_6529"),
    )


    label("loc_651D")

    OP_A2(0x1A80)
    Jump("loc_6529")

    label("loc_6523")

    OP_A3(0x1A80)
    Jump("loc_6529")

    label("loc_6529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_659A")

    ChrTalk(    #281
        0x101,
        (
            "#1006F#6P好了，去找\x01",
            "迷雾峡谷的维姆拉先生对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x106,
        (
            "#053F#2P啊啊。\x02\x03",

            "#552F话说回来……\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x96, 0x1, 0x4)
    OP_28(0x96, 0x1, 0x8)
    Jump("loc_6620")

    label("loc_659A")


    ChrTalk(    #283
        0x101,
        (
            "#1006F#6P好了，去找\x01",
            "要去拜访叫做维姆拉的人对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x106,
        (
            "#053F#2P啊啊，应该住在\x01",
            "峡谷东侧的山中小屋。\x02\x03",

            "#552F话说回来……\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x96, 0x1, 0x10)
    OP_28(0x96, 0x1, 0x20)

    label("loc_6620")

    TurnDirection(0x106, 0x107, 400)
    Sleep(500)

    ChrTalk(    #285
        0x106,
        (
            "#555F……果然\x01",
            "打算跟着来吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)
    Sleep(500)

    ChrTalk(    #286
        0x107,
        (
            "#061F嘿嘿，当然了。\x02\x03",

            "#560F振动装置要是出故障了\x01",
            "就可以当场修理……\x02\x03",

            "如果是遇到会飞行的敌人，\x01",
            "导力炮也会有用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x106,
        (
            "#053F呼……真没办法。\x02\x03",

            "#051F不要太乱来，\x01",
            "免得拖我后腿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x107,
        "#067F好。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6753")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6787")

    label("loc_6753")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6775")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6787")

    label("loc_6775")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_6787")

    Sleep(1500)
    OP_8C(0x106, 270, 400)
    Sleep(100)
    TurnDirection(0x107, 0x101, 400)
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #289
        0x107,
        "#560F#5P什、什么，姐姐？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_63(0xF9)

    ChrTalk(    #290
        0x106,
        "#555F#2P……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1028F#6P呀～怎么说呢。\x02\x03",

            "觉得你们好像\x01",
            "比以前更要好了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6894")

    ChrTalk(    #292
        0x103,
        (
            "#027F#1P呵呵，看来\x01",
            "发生什么好事了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6943")

    label("loc_6894")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68D0")

    ChrTalk(    #293
        0x105,
        (
            "#048F#1P嘻……\x01",
            "好像发生什么好事了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6943")

    label("loc_68D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_690A")

    ChrTalk(    #294
        0x104,
        (
            "#037F#1P呼，看来\x01",
            "发生什么好事了呢㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6943")

    label("loc_690A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6943")

    ChrTalk(    #295
        0x108,
        (
            "#071F#1P哈哈，看来\x01",
            "发生什么好事了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6943")


    ChrTalk(    #296
        0x107,
        "#065F#5P啊啊……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #297
        0x106,
        "#055F#2P说、说什么呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x101,
        (
            "#1001F#6P啊哈哈，别着急。\x02\x03",

            "#1006F不过……心情似乎\x01",
            "已经调整好了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x106,
        (
            "#051F#2P……算是吧。\x02\x03",

            "不会再一个人穷追猛打，\x01",
            "做那种自杀式行为了。\x02\x03",

            "我可不想再被那个小不点\x01",
            "一脸凶凶地教训了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x107,
        (
            "#562F啊……\x01",
            "阿加特哥哥真是的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1012F#6P呵呵……是吗是吗。\x02\x03",

            "#1018F好～那么\x01",
            "立刻去迷雾峡谷吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x107,
        "#061F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x106,
        "#051F#2P噢！\x02",
    )

    CloseMessageWindow()
    OP_28(0x95, 0x1, 0x40)
    OP_28(0x95, 0x1, 0x80)
    OP_28(0x95, 0x1, 0x100)
    OP_28(0x96, 0x4, 0x2)
    OP_28(0x96, 0x4, 0x8)
    OP_28(0x96, 0x1, 0x1)
    OP_28(0x96, 0x1, 0x2)
    OP_20(0x3E8)
    OP_21()
    EventEnd(0x0)
    OP_1D(0xB)
    Return()

    # Function_62_631E end

    def Function_63_6B02(): pass

    label("Function_63_6B02")

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
        (0, "loc_6B7F"),
        (1, "loc_6B85"),
        (SWITCH_DEFAULT, "loc_6B8B"),
    )


    label("loc_6B7F")

    OP_A2(0x1200)
    Jump("loc_6B8B")

    label("loc_6B85")

    OP_A2(0x1201)
    Jump("loc_6B8B")

    label("loc_6B8B")

    Return()

    # Function_63_6B02 end

    def Function_64_6B8C(): pass

    label("Function_64_6B8C")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_64_6B8C end

    def Function_65_6BE7(): pass

    label("Function_65_6BE7")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_65_6BE7 end

    def Function_66_6C44(): pass

    label("Function_66_6C44")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_66_6C44 end

    def Function_67_6C9D(): pass

    label("Function_67_6C9D")

    SetPlaceName(0x2A)
    Return()

    # Function_67_6C9D end

    def Function_68_6CA1(): pass

    label("Function_68_6CA1")

    SetPlaceName(0x26)
    Return()

    # Function_68_6CA1 end

    def Function_69_6CA5(): pass

    label("Function_69_6CA5")

    SetPlaceName(0x25)
    Return()

    # Function_69_6CA5 end

    def Function_70_6CA9(): pass

    label("Function_70_6CA9")

    SetPlaceName(0x20)
    Return()

    # Function_70_6CA9 end

    def Function_71_6CAD(): pass

    label("Function_71_6CAD")

    SetPlaceName(0x28)
    Return()

    # Function_71_6CAD end

    def Function_72_6CB1(): pass

    label("Function_72_6CB1")

    SetPlaceName(0x2B)
    Return()

    # Function_72_6CB1 end

    def Function_73_6CB5(): pass

    label("Function_73_6CB5")

    SetPlaceName(0x21)
    Return()

    # Function_73_6CB5 end

    def Function_74_6CB9(): pass

    label("Function_74_6CB9")

    SetPlaceName(0x27)
    Return()

    # Function_74_6CB9 end

    SaveToFile()

Try(main)
